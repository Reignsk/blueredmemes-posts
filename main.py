import random
from pathlib import Path

import cv2
import numpy as np
from moviepy import (
    AudioFileClip,
    ColorClip,
    CompositeVideoClip,
    TextClip,
    VideoFileClip,
    concatenate_videoclips,
)

# ============================================================
# CONFIG
# ============================================================

CLIPS_DIR = Path("input_clips")
MUSIC_DIR = Path("music")
OUTPUT_DIR = Path("output")

TARGET_W = 1080
TARGET_H = 1920
FPS = 30

MAX_FINAL_SECONDS = 28
MAX_CLIPS = 8

MIN_SEGMENT = 1.2
MAX_SEGMENT = 3.5

# Police grasse : la première trouvée sur la machine est utilisée
FONT_CANDIDATES = [
    "fonts/font.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]

# ============================================================
# HELPERS
# ============================================================

def ensure_dirs():
    CLIPS_DIR.mkdir(exist_ok=True, parents=True)
    MUSIC_DIR.mkdir(exist_ok=True, parents=True)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

def list_videos(folder):
    exts = {".mp4", ".mov", ".m4v", ".mkv", ".avi", ".webm"}
    items = []
    for p in folder.iterdir():
        if p.is_file() and p.suffix.lower() in exts:
            items.append(p)
    return sorted(items)

def list_music(folder):
    exts = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}
    items = []
    for p in folder.iterdir():
        if p.is_file() and p.suffix.lower() in exts:
            items.append(p)
    return sorted(items)

def find_font():
    for candidate in FONT_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
    return None

FONT = find_font()

def sample_gray_frames(clip, step=0.25):
    """Lit une image toutes les `step` secondes, une seule fois par clip, en niveaux de gris réduits."""
    samples = []
    t = 0.0
    while t < clip.duration:
        try:
            frame = clip.get_frame(min(t, clip.duration - 0.01))
        except Exception:
            break
        gray = cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGB2GRAY)
        samples.append((t, cv2.resize(gray, (320, 180))))
        t += step
    return samples

def segment_motion_score(samples, start, end):
    frames = [g for t, g in samples if start <= t < end]
    if len(frames) < 2:
        return 0.0

    total = 0.0
    for i in range(1, len(frames)):
        total += float(cv2.absdiff(frames[i - 1], frames[i]).astype(np.float32).mean())
    return total / max(1, len(frames) - 1)

def segment_contrast_score(samples, start, end):
    values = [float(g.std()) for t, g in samples if start <= t < end]
    if not values:
        return 0.0
    return float(np.mean(values))

def detect_best_segments(clip):
    duration = clip.duration
    if duration < MIN_SEGMENT:
        return []

    samples = sample_gray_frames(clip)

    segments = []
    for start in np.arange(0.0, max(0.1, duration - MIN_SEGMENT), 0.5):
        end = min(duration, start + random.uniform(MIN_SEGMENT, MAX_SEGMENT))
        if end - start < MIN_SEGMENT:
            continue

        motion = segment_motion_score(samples, start, end)
        contrast = segment_contrast_score(samples, start, end)
        score = motion * 0.8 + contrast * 0.2
        segments.append((start, end, score))

    if not segments:
        return []

    segments.sort(key=lambda x: x[2], reverse=True)
    selected = []
    used_starts = []

    for start, end, score in segments[:7]:
        if any(abs(start - s) < 0.8 for s in used_starts):
            continue
        selected.append((start, end, score))
        used_starts.append(start)

    return selected

def make_text(text, fontsize, stroke_width, duration):
    return TextClip(
        font=FONT,
        text=text,
        font_size=fontsize,
        color="white",
        stroke_color="black",
        stroke_width=stroke_width,
        method="label",
        margin=(20, 20),
        duration=duration,
    )

def make_label(text, fontsize=120, duration=1.5):
    txt = make_text(text, fontsize, 6, duration)
    txt = txt.with_position(("center", "center"))
    return txt

def verticalize(clip):
    bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=clip.duration)
    w, h = clip.size

    if w >= h:
        resized = clip.resized(width=TARGET_W * 1.06)
        return CompositeVideoClip(
            [bg, resized.with_position(("center", "center"))],
            size=(TARGET_W, TARGET_H)
        ).with_duration(clip.duration)

    resized = clip.resized(height=TARGET_H * 1.06)
    return CompositeVideoClip(
        [bg, resized.with_position(("center", "center"))],
        size=(TARGET_W, TARGET_H)
    ).with_duration(clip.duration)

def add_zoom(clip, zoom_factor=1.08):
    resized = clip.resized(zoom_factor)
    bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=resized.duration)
    final = CompositeVideoClip(
        [bg, resized.with_position(("center", "center"))],
        size=(TARGET_W, TARGET_H)
    )
    return final.with_duration(resized.duration)

def add_big_text(clip, text):
    label = make_label(text, fontsize=110, duration=min(1.5, clip.duration))
    return CompositeVideoClip(
        [clip, label.with_position(("center", "center"))],
        size=(TARGET_W, TARGET_H)
    )

def add_bottom_tag(clip, text):
    tag = make_text(text, 44, 3, clip.duration)
    tag = tag.with_position(("center", 0.86), relative=True)
    return CompositeVideoClip([clip, tag], size=(TARGET_W, TARGET_H))

def intro_card(text, duration=1.7):
    bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=duration)
    label = make_label(text, fontsize=120, duration=duration)
    return CompositeVideoClip([bg, label.with_position(("center", "center"))], size=(TARGET_W, TARGET_H))

def outro_card(text, duration=1.6):
    bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=duration)
    label = make_label(text, fontsize=110, duration=duration)
    return CompositeVideoClip([bg, label.with_position(("center", "center"))], size=(TARGET_W, TARGET_H))

def choose_music(total_duration):
    songs = list_music(MUSIC_DIR)
    if not songs:
        return None
    track = random.choice(songs)
    music = AudioFileClip(str(track))
    if music.duration > total_duration:
        music = music.subclipped(0, total_duration)
    return music.with_volume_scaled(0.35)

def build_segment(segment_clip):
    # Passage en 9:16 d'abord, pour que le zoom s'applique à l'image verticale
    segment_clip = verticalize(segment_clip)

    if random.random() < 0.8:
        segment_clip = add_zoom(segment_clip, random.uniform(1.04, 1.12))

    if random.random() < 0.7:
        segment_clip = segment_clip.with_speed_scaled(random.uniform(1, 1.12))

    label = random.choice(["GOAL", "WOW", "FIRE", "CLUTCH", "1-0", "BANG", "NICE", "INSANE"])
    segment_clip = add_big_text(segment_clip, label)
    segment_clip = add_bottom_tag(segment_clip, "MATCH EDIT")
    return segment_clip

def build_final_video():
    videos = list_videos(CLIPS_DIR)
    if not videos:
        raise FileNotFoundError("Aucune vidéo trouvée dans input_clips/")

    candidates = []
    sources = []

    for video_path in videos:
        # Le clip source reste ouvert : les sous-clips en ont besoin jusqu'à l'export
        clip = VideoFileClip(str(video_path))
        sources.append(clip)
        segments = detect_best_segments(clip)

        for start, end, score in segments:
            sub = clip.subclipped(start, end)
            candidates.append((score, sub))

    if not candidates:
        raise RuntimeError("Aucun moment fort détecté. Vérifie tes vidéos.")

    candidates.sort(key=lambda x: x[0], reverse=True)

    selected = []
    total_time = 0.0

    for score, segment in candidates:
        if len(selected) >= MAX_CLIPS:
            break
        if total_time + segment.duration > MAX_FINAL_SECONDS:
            continue

        seq = build_segment(segment)
        selected.append(seq)
        total_time += seq.duration

    if not selected:
        raise RuntimeError("Aucun segment retenu.")

    intro = intro_card("GOAL", duration=1.6)
    outro = outro_card("POSTÉ !", duration=1.5)

    final = concatenate_videoclips([intro, *selected, outro], method="compose")
    final = final.without_audio()

    music = choose_music(final.duration)
    if music is not None:
        final = final.with_audio(music)

    return final, sources

def export_version(video, out_path):
    video.write_videofile(
        str(out_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        preset="fast",
        threads=4,
        ffmpeg_params=["-pix_fmt", "yuv420p"],
        logger=None
    )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    ensure_dirs()

    try:
        final_video, sources = build_final_video()

        final_file = OUTPUT_DIR / "football_edit_final.mp4"
        export_version(final_video, final_file)
        print(f"[OK] Vidéo finale exportée : {final_file}")

        for seconds in [15, 30, 45]:
            if final_video.duration > seconds:
                trimmed = final_video.subclipped(0, seconds)
            else:
                trimmed = final_video

            out = OUTPUT_DIR / f"football_edit_{seconds}s.mp4"
            export_version(trimmed, out)
            print(f"[OK] Version {seconds}s exportée : {out}")

        for clip in sources:
            clip.close()

    except Exception as e:
        print("Erreur :", e)
        print("")
        print("Checklist:")
        print("1. Mets tes vidéos dans input_clips/")
        print("2. Mets éventuellement une musique dans music/")
        print("3. Installe les dépendances : pip install -r requirements.txt")
