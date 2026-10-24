"""Premium Football Edit Generator.

Lit les vidéos de input_clips/, repère les moments les plus intenses
(mouvement + son), les recadre en 9:16 et exporte plusieurs versions dans output/.
"""

from pathlib import Path

import cv2
import numpy as np
from moviepy import (
    AudioFileClip,
    CompositeAudioClip,
    VideoFileClip,
    concatenate_videoclips,
)
from moviepy.audio.fx import AudioLoop, AudioFadeOut

ROOT = Path(__file__).parent
INPUT_DIR = ROOT / "input_clips"
MUSIC_DIR = ROOT / "music"
OUTPUT_DIR = ROOT / "output"

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}

OUT_W, OUT_H = 1080, 1920
FPS = 30
SEGMENT_SECONDS = 3.0      # durée d'un moment candidat
ANALYSIS_FPS = 6           # images analysées par seconde pour le score de mouvement
FINAL_MAX_SECONDS = 60     # durée max de football_edit_final.mp4
SHORT_VERSIONS = [15, 30, 45]
MUSIC_VOLUME = 0.8
ORIGINAL_AUDIO_VOLUME = 0.35
ZOOM_PUNCH = 0.08          # zoom de 8 % au début de chaque séquence

OVERLAY_TEXT = "WHAT A MOMENT"


# --------------------------------------------------------------------------- #
# Analyse
# --------------------------------------------------------------------------- #

def analyze_motion(path):
    """Retourne (temps, énergie de mouvement, centre x du mouvement en 0..1)."""
    cap = cv2.VideoCapture(str(path))
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30
    step = max(1, round(src_fps / ANALYSIS_FPS))

    times, energies, centers = [], [], []
    prev = None
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            small = cv2.resize(frame, (160, 90))
            gray = cv2.GaussianBlur(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY), (5, 5), 0)
            if prev is not None:
                diff = cv2.absdiff(gray, prev).astype(np.float32)
                energy = float(diff.mean())
                col = diff.sum(axis=0)
                center = float((col * np.arange(col.size)).sum() / col.sum() / col.size) if col.sum() > 0 else 0.5
                times.append(idx / src_fps)
                energies.append(energy)
                centers.append(center)
            prev = gray
        idx += 1
    cap.release()
    return np.array(times), np.array(energies), np.array(centers)


def analyze_audio(clip, times):
    """Volume RMS de la bande son, aligné sur les temps de l'analyse vidéo."""
    if clip.audio is None or len(times) == 0:
        return np.zeros(len(times))
    sr = 8000
    samples = clip.audio.to_soundarray(fps=sr)
    if samples.ndim > 1:
        samples = samples.mean(axis=1)
    win = int(sr / ANALYSIS_FPS)
    rms = []
    for t in times:
        i = int(t * sr)
        chunk = samples[max(0, i - win // 2): i + win // 2]
        rms.append(float(np.sqrt((chunk ** 2).mean())) if chunk.size else 0.0)
    return np.array(rms)


def normalize(x):
    if x.size == 0 or x.max() == x.min():
        return np.zeros_like(x)
    return (x - x.min()) / (x.max() - x.min())


def find_segments(path, clip):
    """Découpe une vidéo en segments de SEGMENT_SECONDS et leur donne un score."""
    times, motion, centers = analyze_motion(path)
    if times.size == 0:
        return []
    audio = analyze_audio(clip, times)
    score_curve = 0.65 * normalize(motion) + 0.35 * normalize(audio)

    segments = []
    start = 0.0
    while start + 1.0 <= clip.duration:
        end = min(start + SEGMENT_SECONDS, clip.duration)
        mask = (times >= start) & (times < end)
        if mask.any():
            segments.append({
                "path": path,
                "start": start,
                "end": end,
                "score": float(score_curve[mask].mean()),
                "center_x": float(np.median(centers[mask])),
            })
        start = end
    return segments


# --------------------------------------------------------------------------- #
# Rendu
# --------------------------------------------------------------------------- #

def draw_overlay(frame, text):
    """Texte blanc avec contour noir, en haut de l'image (OpenCV, sans police externe)."""
    font = cv2.FONT_HERSHEY_DUPLEX
    scale, thickness = 2.6, 6
    (tw, th), _ = cv2.getTextSize(text, font, scale, thickness)
    x = (OUT_W - tw) // 2
    y = int(OUT_H * 0.14)
    cv2.putText(frame, text, (x, y), font, scale, (0, 0, 0), thickness + 10, cv2.LINE_AA)
    cv2.putText(frame, text, (x, y), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)
    return frame


def make_vertical(clip, center_x, text):
    """Recadre en 9:16 autour de l'action, avec zoom d'entrée et texte."""
    w, h = clip.size
    crop_w = min(w, int(h * OUT_W / OUT_H))
    crop_h = min(h, int(crop_w * OUT_H / OUT_W))
    x0 = int(np.clip(center_x * w - crop_w / 2, 0, w - crop_w))
    y0 = (h - crop_h) // 2
    duration = clip.duration

    def transform(get_frame, t):
        frame = get_frame(t)[y0:y0 + crop_h, x0:x0 + crop_w]
        # zoom qui part de ZOOM_PUNCH et revient à 1 sur 0.6 s
        zoom = 1 + ZOOM_PUNCH * max(0.0, 1 - t / 0.6)
        if zoom > 1.001:
            fh, fw = frame.shape[:2]
            zw, zh = int(fw / zoom), int(fh / zoom)
            zx, zy = (fw - zw) // 2, (fh - zh) // 2
            frame = frame[zy:zy + zh, zx:zx + zw]
        frame = cv2.resize(frame, (OUT_W, OUT_H), interpolation=cv2.INTER_LINEAR)
        if text and t < min(duration, 2.5):
            frame = draw_overlay(np.ascontiguousarray(frame), text)
        return frame

    return clip.transform(transform, apply_to=[])


def pick_segments(segments, target_seconds):
    """Prend les meilleurs segments jusqu'à la durée voulue, puis remet dans l'ordre."""
    chosen, total = [], 0.0
    for seg in sorted(segments, key=lambda s: s["score"], reverse=True):
        if total >= target_seconds:
            break
        seg = dict(seg)
        remaining = target_seconds - total
        if seg["end"] - seg["start"] > remaining:
            seg["end"] = seg["start"] + remaining
        chosen.append(seg)
        total += seg["end"] - seg["start"]
    order = {p: i for i, p in enumerate(dict.fromkeys(s["path"] for s in segments))}
    return sorted(chosen, key=lambda s: (order[s["path"]], s["start"]))


def find_music():
    if not MUSIC_DIR.exists():
        return None
    files = sorted(p for p in MUSIC_DIR.iterdir() if p.suffix.lower() in AUDIO_EXTS)
    return files[0] if files else None


def build_edit(selection, sources, music_path, out_path):
    parts = []
    for i, seg in enumerate(selection):
        sub = sources[seg["path"]].subclipped(seg["start"], seg["end"])
        parts.append(make_vertical(sub, seg["center_x"], OVERLAY_TEXT if i == 0 else None))
    edit = concatenate_videoclips(parts, method="compose")

    if music_path:
        music = AudioFileClip(str(music_path))
        music = music.with_effects([AudioLoop(duration=edit.duration)]) if music.duration < edit.duration \
            else music.subclipped(0, edit.duration)
        music = music.with_effects([AudioFadeOut(min(1.5, edit.duration / 4))]).with_volume_scaled(MUSIC_VOLUME)
        tracks = [music]
        if edit.audio is not None:
            tracks.insert(0, edit.audio.with_volume_scaled(ORIGINAL_AUDIO_VOLUME))
        edit = edit.with_audio(CompositeAudioClip(tracks))

    edit.write_videofile(
        str(out_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        preset="medium",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
        logger=None,
    )
    print(f"  ✔ {out_path.name} ({edit.duration:.1f}s)")


# --------------------------------------------------------------------------- #

def main():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    paths = sorted(p for p in INPUT_DIR.iterdir() if p.suffix.lower() in VIDEO_EXTS)
    if not paths:
        print(f"Aucune vidéo trouvée dans {INPUT_DIR}/ — ajoute des clips puis relance.")
        return

    sources, segments = {}, []
    for path in paths:
        print(f"Analyse de {path.name}...")
        clip = VideoFileClip(str(path))
        sources[path] = clip
        segments += find_segments(path, clip)

    if not segments:
        print("Impossible d'analyser les vidéos (clips trop courts ou illisibles).")
        return

    total = sum(s["end"] - s["start"] for s in segments)
    music_path = find_music()
    print(f"{len(segments)} séquences trouvées ({total:.0f}s au total)."
          + (f" Musique : {music_path.name}" if music_path else " Pas de musique."))

    print("Export...")
    final_seconds = min(FINAL_MAX_SECONDS, total * 0.6 if total > 20 else total)
    build_edit(pick_segments(segments, final_seconds), sources, music_path,
               OUTPUT_DIR / "football_edit_final.mp4")

    for seconds in SHORT_VERSIONS:
        if total < seconds:
            print(f"  ✘ football_edit_{seconds}s.mp4 ignoré (seulement {total:.0f}s de vidéo)")
            continue
        build_edit(pick_segments(segments, seconds), sources, music_path,
                   OUTPUT_DIR / f"football_edit_{seconds}s.mp4")

    for clip in sources.values():
        clip.close()
    print(f"Terminé. Fichiers dans {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
