# Premium Football Edit Generator

Automatiser le montage de vidéos football pour TikTok / Reels / Shorts.

Ce projet crée automatiquement un montage football style TikTok à partir de vidéos placées dans `input_clips/`.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

## Dossiers

- `input_clips/` : ajoute tes vidéos ici
- `music/` : ajoute une musique optionnelle ici
- `output/` : sorties finies exportées ici

## Objectif

- détecte les meilleurs moments de jeu
- garde les meilleures séquences
- convertit en format vertical 9:16
- ajoute overlay texte
- exporte plusieurs versions

## Sorties attendues

- `football_edit_final.mp4`
- `football_edit_15s.mp4`
- `football_edit_30s.mp4`
- `football_edit_45s.mp4`

## À demander à Claude

- “ajoute des sous-titres automatiques”
- “ajoute de meilleures transitions”
- “rends le style plus cinéma”
- “génère 10s / 20s / 60s”
- “ajoute plus de zooms”
