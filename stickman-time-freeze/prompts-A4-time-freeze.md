# Stickman « Time Freeze » — Pack de prompts A4 · Cozy Storytelling

> Projet : refaire en stickman le format « Choose one power » · 9:16 · 59,6 s · voix off ElevenLabs Brian fournie.
> Les prompts vidéo sont en anglais (meilleurs résultats avec les modèles). Les explications sont en français.

---

## 0. Comment utiliser ce pack (à donner tel quel à Claude ou à ton outil vidéo)

1. **(Optionnel mais recommandé) Fiche personnage d'abord** : génère une image du héros avec le prompt de la section 1b, garde la meilleure, et joins-la comme **image de référence personnage** à chaque clip qui la supporte. Ça aide beaucoup la cohérence ; ça ne remplace pas le texte du prompt.
2. **Génère les 11 clips S1 → S11** (section 3). Chaque prompt est autonome : copie-le en entier, sans rien raccourcir.
3. **Monte** selon le guide de raccord (section 4) : garde seulement les plages « retained », pose la voix off **mp3 complète** sur la timeline, puis musique, bruitages et sous-titres (section 5).
4. Les durées « generate » sont des **cibles** non vérifiées : si ton modèle ne fait que 5 s ou 10 s, génère la durée disponible la plus proche et garde la même plage utile.

**Plateforme conseillée par la skill** : Google Flow (Veo), c'est là que les échantillons A4 ont été faits. Tout modèle texte→vidéo 9:16 avec image de référence convient (Higgsfield, Kling, etc.). Fais **d'abord 1 ou 2 clips tests en basse résolution** (par ex. S4 et S8) avant de tout lancer.

---

## 1. Global continuity block (récap)

- **Ratio** : 9:16 vertical · **Durée finale** : 59,6 s (calée sur la voix off) · **Style** : Style 4 · Cozy Storytelling (full-color 2D cartoon environments, white-filled minimalist characters, dark stick limbs).
- **Héros** : ancre personnage fixe ci-dessous, répétée mot pour mot dans chaque prompt. *Note : l'accessoire rouge évoqué dans la proposition est retiré — l'ancre A4 interdit cheveux/accessoires sur le héros ; il est reconnaissable parce que c'est le seul personnage qui bouge quand le monde est figé.*
- **Distribution** (minimale, chaque rôle a sa fiche) : THE HERO · THE PEDESTRIAN (S6–S7) · THE TEACHER et THE CLASSMATE (S8) · THE FRIEND (S10–S11). Pas d'autres personnes : les voitures et le camion ont des vitres teintées sombres, sans conducteur visible.
- **Règle visuelle « temps figé »** : quand le héros claque des doigts, un anneau lumineux bleu électrique se propage, tout s'arrête et le décor passe en **bleu-gris froid désaturé** avec de fines poussières bleu pâle suspendues. Le héros reste blanc net, inchangé. Quand le temps repart, les couleurs chaudes reviennent.
- **Claquement de doigts** : les mains A4 sont des petites formes arrondies sombres (pas de doigts) → le « snap » = un petit coup sec de la main levée + une étincelle bleue électrique. Ne pas demander de doigts détaillés.
- **Palette** (noms simples) : ciel de fin d'après-midi orange doré et bleu ciel ; bleu électrique = pouvoir ; rouge vif = danger (camion) ; bleu marine profond = « catch ».
- **Son** : voix off **externe** (ton mp3 Brian, jamais régénérée). Les clips vidéo : **pas de voix, pas de musique**. Bruitages et musique ajoutés au montage.
- **Texte à l'écran** : **aucun texte généré** dans les clips (horloges sans chiffres, feuilles d'examen avec lignes grises illisibles, écran de téléphone uni). Tous les sous-titres/overlays sont ajoutés au montage (section 5).

### 1a. Character anchor — THE HERO (verbatim)

```text
One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.
```

### 1b. Prompt fiche personnage (image, optionnel)

```text
Character reference sheet, 9:16 vertical, plain soft warm-white background, full-color 2D cartoon style with clean contours. THE HERO shown three times side by side at the same scale: front view, side view, back view, standing neutral with arms relaxed. One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design. No text, no letters, no numbers, no labels, no watermark, no photorealism, no 3D rendering.
```

---

## 2. Plan de montage (sources → plans du film)

| Source | Generate | Retained (source) | Film | Lieu | Voix off couverte |
|---|---|---|---|---|---|
| S1 | 8 s | 0.0–8.0 | 0.0–8.0 | Salle des pouvoirs | Choose one power… / Time freeze. Mind reading. Shapeshifting. |
| S2 | 8 s | 0.0–5.3 | 8.0–13.3 | Salle des pouvoirs | Or super strength. You chose… TIME FREEZE! |
| S3 | 6 s | 0.0–4.5 | 13.3–17.8 | Carrefour en ville, heure dorée | Imagine snapping your fingers… and the whole world just stops. |
| S4 | 8 s | 0.0–7.2 | 17.8–25.0 | Même rue figée + terrasse de café | Cars frozen… Birds… A cup of coffee… never hits the ground. |
| S5 | 6 s | 0.0–3.0 | 25.0–28.0 | Entrée de l'école, matin | Late for school? Snap. Now you have all the time you need. |
| S6 | 6 s | 0.0–3.5 | 28.0–31.5 | Passage piéton, quartier | Someone about to cross the road without looking? Snap. |
| S7 | 8 s | 0.0–5.2 | 31.5–36.7 | Même passage piéton | You walk over… pull them back. Nobody ever knows… |
| S8 | 8 s | 0.0–7.7 | 36.7–44.4 | Salle de classe | Sleep for ten hours… read every answer… during a test. |
| S9 | 8 s | 0.0–6.2 | 44.4–50.6 | Rue figée, nuit, horloge géante | But here's the catch… you still get older. |
| S10 | 6 s | 0.0–3.6 | 50.6–54.2 | Parc | One minute for everyone else… a whole year for you. |
| S11 | 6 s | 0.0–5.4 | 54.2–59.6 | Même parc | So… would you still use it? Tell me in the comments… episode two. |

Les temps « Film » sont approximatifs (pauses détectées dans la voix off) : recale chaque coupe sur l'audio réel au montage.

---

## 3. Prompts de génération (copier chaque bloc en entier)

### S1 — Salle des pouvoirs (film 0.0–8.0)

```text
OUTPUT: Source S1. Generate 8 seconds, 9:16 vertical. The full 0.0–8.0 s range is used in the edit (film 0.0–8.0 s).

ENVIRONMENT: Full-color 2D cartoon environment with clean contours and gentle atmospheric light: a small round floating stone platform under a calm deep-purple and navy night sky with soft twinkling stars and drifting pale mist. Above the platform float four large round glowing medallions arranged in a gentle vertical arc: an electric blue medallion with a simple clock icon (plain face, two hands, no numerals), a soft violet medallion with a simple brain icon, an emerald green medallion with a simple human-silhouette icon and a curved swap arrow, and a warm orange medallion with a simple clenched-fist icon. Icons are plain shapes only.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PALETTE: deep purple and navy sky, electric blue, soft violet, emerald green and warm orange medallion glows, white hero with dark limbs.

COMPOSITION (9:16): hero small at the bottom center seen from a low three-quarter back angle, medallions filling the upper two thirds; vertical depth, slow upward camera drift.

OPENING STATE: all four medallions dim; the hero stands at the bottom center looking up.

TIMED ACTION:
[0.0–1.5 s] Slow push-in. The hero looks up at the four dim medallions and lifts one hand halfway, hesitating.
[1.5–4.5 s] The hero tilts his head and taps his chin, unsure. All four medallions flicker once with a brief warning dark-red tint, then return to dim.
[4.5–5.6 s] The electric blue clock medallion lights up brightly; the hero turns his head toward it.
[5.9–6.9 s] The violet brain medallion lights up; the hero turns toward it.
[7.1–8.0 s] The green swap medallion lights up; the hero turns toward it.

SOUND: No speech, no voices, no narration, no music. Optional soft magical hum only.

CLOSING STATE (out-point): three medallions glowing (blue, violet, green), the orange one still dim; the hero mid-turn toward the orange medallion.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S2 — Le choix (film 8.0–13.3)

```text
OUTPUT: Source S2. Generate 8 seconds, 9:16 vertical. Retain 0.0–5.3 s only (film 8.0–13.3 s); the tail is unused.

ENVIRONMENT: Full-color 2D cartoon environment with clean contours and gentle atmospheric light: a small round floating stone platform under a calm deep-purple and navy night sky with soft twinkling stars and drifting pale mist. Above the platform float four large round glowing medallions arranged in a gentle vertical arc: an electric blue medallion with a simple clock icon (plain face, two hands, no numerals), a soft violet medallion with a simple brain icon, an emerald green medallion with a simple human-silhouette icon and a curved swap arrow, and a warm orange medallion with a simple clenched-fist icon. Icons are plain shapes only.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PALETTE: deep purple and navy sky, electric blue, soft violet, emerald green and warm orange glows; after the freeze, the whole scene becomes cool desaturated blue-gray except the white hero.

COMPOSITION (9:16): hero at the bottom center, medallions above; push-in toward the blue medallion, then medium shot of the hero.

OPENING STATE: blue, violet and green medallions glowing, orange dim; the hero looking toward the orange medallion.

TIMED ACTION:
[0.0–0.9 s] The orange fist medallion lights up with a small punchy shake; all four now glow.
[0.9–2.0 s] The hero steps forward and moves one hand slowly from medallion to medallion, choosing; camera pushes in.
[2.0–3.2 s] The hero reaches up decisively and touches the electric blue clock medallion; the other three fade dark.
[3.2–5.3 s] The clock icon's hands stop abruptly. A ring of electric blue light bursts outward from the medallion and sweeps across the scene: the stars stop twinkling, the mist freezes in place, tiny pale-blue dust specks hang in the air, and everything except the hero turns cool desaturated blue-gray. The hero looks down at his own hand in amazement.

SOUND: No speech, no voices, no narration, no music. Optional single deep whoosh at the freeze.

CLOSING STATE (out-point at 5.3 s): frozen blue-gray scene, the hero looking at his raised hand, amazed.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S3 — Le claquement, la ville s'arrête (film 13.3–17.8)

```text
OUTPUT: Source S3. Generate 6 seconds, 9:16 vertical. Retain 0.0–4.5 s (film 13.3–17.8 s).

ENVIRONMENT: Full-color 2D cartoon city street corner at golden hour: warm orange and gold sky, low-rise colorful buildings, leafy trees swaying, a few colorful cars driving with dark tinted windows and no visible drivers, small birds flying. No pedestrians.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PALETTE: warm orange, gold and sky blue at the start; electric blue shockwave; after the freeze, cool desaturated blue-gray except the white hero.

COMPOSITION (9:16): start in a close-up of the hero's raised hand and face at chest height, then a continuous pull-back and rise to a high wide angle over the street, vertical reveal.

OPENING STATE: the hero standing on the sidewalk, one hand raised at chest height; traffic moving.

TIMED ACTION:
[0.0–1.4 s] Close-up: the hero's small rounded hand flicks sharply in a snapping gesture; a bright electric-blue spark pops from it. His face shows a confident little smile.
[1.4–4.5 s] Camera pulls back and rises into a wide high angle. A ring-shaped electric-blue shockwave ripples outward from the hand through the whole street: each car stops dead as the ring passes, a swaying tree freezes mid-sway, the flying birds stop in mid-air, and the warm colors drain into cool desaturated blue-gray with tiny pale-blue dust specks hanging in the air. The hero stays crisp and unchanged.

SOUND: No speech, no voices, no narration, no music. Optional snap and whoosh only.

CLOSING STATE (out-point at 4.5 s): wide high view of the completely frozen blue-gray street, the hero small in the center.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S4 — Le monde figé : voitures, oiseaux, café (film 17.8–25.0)

```text
OUTPUT: Source S4. Generate 8 seconds, 9:16 vertical. Retain 0.0–7.2 s (film 17.8–25.0 s).

ENVIRONMENT: The same full-color 2D cartoon city street at golden hour, but frozen in time: everything rendered in cool desaturated blue-gray with tiny pale-blue dust specks hanging motionless in the air. Two lines of stopped colorful cars with dark tinted windows and no visible drivers; one car frozen mid-turn with a small puff of exhaust hanging still behind it. A street-side cafe terrace with small round tables at the side of the street. No other people.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PROPS: three small dark birds; one white ceramic cup filled with brown coffee. First appearance of the cup: already in mid-air halfway between a cafe table edge and the ground, tilted, with the coffee frozen in a splash of droplets. The cup never moves and never lands.

PALETTE: cool desaturated blue-gray world, white hero with dark limbs, the brown coffee as the only warm accent.

COMPOSITION (9:16): ground-level tracking shot down the middle lane, then a vertical tilt up to the sky, then a tilt down to the cafe table; use vertical depth.

OPENING STATE: the hero already walking toward the camera down the middle lane between the frozen cars.

TIMED ACTION:
[0.0–2.0 s] The hero strolls toward the camera between the frozen cars, looking around, and knocks lightly on a car hood as he passes; nothing moves.
[2.0–3.6 s] The camera tilts up: three small birds hang frozen mid-wingbeat in the sky. The hero looks up and pokes one gently; it stays exactly in place.
[3.6–7.2 s] The camera tilts down to the cafe terrace: the white coffee cup hangs frozen in mid-air with its coffee splash suspended. The hero crouches beside it, walks a slow half circle around it, points at it and grins at the camera.

SOUND: No speech, no voices, no narration, no music. Optional soft footsteps only.

CLOSING STATE (out-point at 7.2 s): the hero crouched beside the floating cup, grinning at the camera.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S5 — En retard à l'école (film 25.0–28.0)

```text
OUTPUT: Source S5. Generate 6 seconds, 9:16 vertical. Retain 0.0–3.0 s (film 25.0–28.0 s); fast pacing.

ENVIRONMENT: Full-color 2D cartoon school entrance on a bright morning: red-brick school building, open iron gate, green bushes, clear blue sky. A large round wall clock above the entrance with a plain face and two hands, no numerals; the minute hand is just one tick before the top. No other people.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PALETTE: warm red brick, bright blue sky, fresh green; after the freeze, cool desaturated blue-gray except the white hero; electric blue spark.

COMPOSITION (9:16): low angle with the clock high in the frame and the hero running up from the bottom toward the gate.

OPENING STATE: the hero sprinting toward the gate from the bottom of the frame, arms pumping, worried face.

TIMED ACTION:
[0.0–1.0 s] The hero sprints toward the gate; the clock's minute hand is about to reach the top.
[1.0–1.5 s] The hero stops, flicks his small rounded hand in a snapping gesture; an electric-blue spark pops, a blue ring sweeps out, the clock hand freezes and the scene turns cool blue-gray.
[1.5–3.0 s] The hero relaxes completely, puts his hands behind his back and strolls slowly and calmly through the gate with a satisfied smile.

SOUND: No speech, no voices, no narration, no music. Optional snap and whoosh only.

CLOSING STATE (out-point at 3.0 s): the hero strolling through the gate, back to the camera, frozen blue-gray school.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S6 — Le piéton distrait (film 28.0–31.5)

```text
OUTPUT: Source S6. Generate 6 seconds, 9:16 vertical. Retain 0.0–3.5 s (film 28.0–31.5 s).

ENVIRONMENT: Full-color 2D cartoon residential street on a sunny afternoon: a two-lane road with a white zebra crosswalk, green trees, small colorful houses, sidewalks on both sides.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

CHARACTER LOCK — THE PEDESTRIAN: A second character, the pedestrian, drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. His only distinguishing item is a mustard-yellow knit beanie on his head. He is slightly shorter than the protagonist.

PROPS: one small dark rectangular phone held in the pedestrian's right hand, screen plain and blank. One large vivid red delivery truck with a dark tinted windscreen, no visible driver, no text and no logos.

PALETTE: sunny greens and sky blue, vivid red truck as the danger accent; after the freeze, cool desaturated blue-gray except the white hero; electric blue spark.

COMPOSITION (9:16): high three-quarter view looking down the road so the truck approaches from the top of the frame; the pedestrian at the near curb in the middle; the hero on the far sidewalk at the left edge.

OPENING STATE: traffic moving; the pedestrian walking toward the curb staring at his phone; the hero standing on the opposite sidewalk.

TIMED ACTION:
[0.0–1.4 s] The pedestrian walks to the curb without looking up and steps one foot onto the road.
[1.4–2.5 s] The red truck appears in the distance and speeds toward the crosswalk. The hero notices; his eyes widen in alarm.
[2.5–3.5 s] The hero flicks his small rounded hand in a snapping gesture; an electric-blue spark pops, a blue ring sweeps across the street, and everything freezes in cool blue-gray: the pedestrian mid-step with one foot on the road, the truck stopped a few meters away.

SOUND: No speech, no voices, no narration, no music. Optional engine rumble, snap and whoosh only.

CLOSING STATE (out-point at 3.5 s): frozen blue-gray tableau — pedestrian mid-step on the road, truck close, the hero on the far sidewalk.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S7 — Le sauvetage invisible (film 31.5–36.7)

```text
OUTPUT: Source S7. Generate 8 seconds, 9:16 vertical. Retain 0.0–5.2 s (film 31.5–36.7 s).

ENVIRONMENT: The same full-color 2D cartoon residential street with a white zebra crosswalk, green trees and small colorful houses, frozen in time at the start: cool desaturated blue-gray with tiny pale-blue dust specks hanging in the air.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

CHARACTER LOCK — THE PEDESTRIAN: A second character, the pedestrian, drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. His only distinguishing item is a mustard-yellow knit beanie on his head. He is slightly shorter than the protagonist.

PROPS: one small dark rectangular phone in the pedestrian's right hand the whole time, screen plain and blank. One large vivid red delivery truck with a dark tinted windscreen, no visible driver, no text and no logos.

PALETTE: frozen cool blue-gray, then warm sunny colors return after the second snap; vivid red truck.

COMPOSITION (9:16): same high three-quarter view down the road; the truck stopped near the top, the pedestrian mid-step at the near curb, the hero on the far sidewalk.

OPENING STATE (matches the previous shot): everything frozen; the pedestrian mid-step with one foot on the road; the truck a few meters away; the hero on the far sidewalk.

TIMED ACTION:
[0.0–1.6 s] The hero walks calmly across the road, passing right in front of the frozen truck.
[1.6–2.8 s] The hero gently takes the frozen pedestrian by the shoulders and slides him back onto the sidewalk, setting him upright, phone still in hand.
[2.8–3.8 s] The hero walks back across to his own sidewalk, hands in a relaxed swing.
[3.8–4.3 s] The hero flicks his small rounded hand in a snapping gesture; a small electric-blue spark; warm colors flood back.
[4.3–5.2 s] The red truck whooshes past on the empty road. The pedestrian looks up from his phone, blinks and looks around, confused. On the far sidewalk the hero looks away innocently.

SOUND: No speech, no voices, no narration, no music. Optional footsteps, snap and truck whoosh only.

CLOSING STATE (out-point at 5.2 s): normal colors; the pedestrian safe and confused on the sidewalk; the hero looking away innocently.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S8 — La classe figée (film 36.7–44.4)

```text
OUTPUT: Source S8. Generate 8 seconds, 9:16 vertical. Retain 0.0–7.7 s (film 36.7–44.4 s).

ENVIRONMENT: Full-color 2D cartoon classroom in warm daylight: a blank dark green chalkboard with no writing, wooden desks in rows, tall windows with sunlight. The room is frozen in time: cool desaturated blue-gray with tiny pale-blue dust specks hanging in the sunbeams.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

CHARACTER LOCK — THE TEACHER: An adult teacher drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. Distinguished only by thin dark round glasses; slightly taller than the protagonist.

CHARACTER LOCK — THE CLASSMATE: One classmate drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. Distinguished only by a small bright green headband.

PROPS: one small soft white pillow on the hero's desk; a few plain white test sheets on the desks covered only in illegible thin gray lines; one dark pencil in the classmate's hand.

PALETTE: frozen cool blue-gray classroom, white characters with dark limbs, tiny pale crescent-moon icons drifting during the nap.

COMPOSITION (9:16): medium shot of the hero's desk in the foreground with the frozen teacher at the chalkboard behind; then a short track to the classmate's desk in the next row.

OPENING STATE: the teacher frozen at the chalkboard, mouth open mid-sentence, one hand pointing at the blank board; the classmate frozen writing; the hero asleep with his head on the pillow on his desk.

TIMED ACTION:
[0.0–3.5 s] The hero sleeps peacefully on the pillow; tiny pale crescent-moon icons drift up from him; slow camera push-in past the frozen teacher.
[3.5–4.2 s] The hero wakes, stretches both arms wide, refreshed.
[4.2–6.4 s] Test sheets now lie on the desks. The hero tiptoes to the frozen classmate's desk, leans over the classmate's sheet, studies it and nods.
[6.4–7.7 s] The hero tiptoes back to his seat, sits and winks at the camera.

SOUND: No speech, no voices, no narration, no music. Optional soft snore and tiptoe sounds only.

CLOSING STATE (out-point at 7.7 s): the hero seated, winking at the camera; teacher and classmate still frozen.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S9 — Le revers (film 44.4–50.6)

```text
OUTPUT: Source S9. Generate 8 seconds, 9:16 vertical. Retain 0.0–6.2 s (film 44.4–50.6 s).

ENVIRONMENT: Full-color 2D cartoon city street at night, frozen in time: deep navy and cool blue-gray, frozen cars with dark tinted windows and no drivers, street lamps with still halos, three small birds frozen mid-flight against the sky. A huge translucent pale clock face hangs in the night sky behind the buildings, plain face with two hands and no numerals. No other people.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

PALETTE: deep navy, cool blue-gray, pale translucent clock glow, white hero with dark limbs; no warm colors.

COMPOSITION (9:16): start very wide and high with the hero tiny in the middle of the empty street; then a slow orbit and descent to a medium shot of the hero with the giant clock above him.

OPENING STATE: the hero standing alone in the middle of the frozen night street.

TIMED ACTION:
[0.0–2.5 s] Wide high view: the street lights dim slightly; the hero stands alone and small, looking around at the silent frozen city.
[2.5–6.2 s] The camera slowly orbits down toward the hero. The giant clock's hands begin to spin, faster and faster. The hero's long shadow stretches and sweeps around him on the ground like a sundial. The frozen birds and cars stay perfectly still. The hero looks at his hand, then up at the spinning clock, worried.

SOUND: No speech, no voices, no narration, no music. Optional low ticking only.

CLOSING STATE (out-point at 6.2 s): medium shot of the worried hero under the fast-spinning giant clock.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S10 — Une minute pour eux, un an pour toi (film 50.6–54.2)

```text
OUTPUT: Source S10. Generate 6 seconds, 9:16 vertical. Retain 0.0–3.6 s (film 50.6–54.2 s).

ENVIRONMENT: Full-color 2D cartoon city park with a large tree, a wooden bench and a path, frozen in time: cool desaturated blue-gray, a few leaves hanging motionless in mid-air, tiny pale-blue dust specks.

CHARACTER LOCK — THE HERO: One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.

APPROVED STORY STATE — AGING (exception to the hero lock for this shot only): over the shot the hero gradually gains light gray eyebrow strokes, a short gray beard drawn as a few simple strokes on the lower head, and a slightly curved back; a plain wooden cane appears in one hand at the end. Head shape, white fill, proportions and line weight do not change.

CHARACTER LOCK — THE FRIEND: The protagonist's friend drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. Distinguished only by a short orange scarf around the neck. Frozen mid-laugh with one hand raised, never moving.

PROPS: a stack of plain books with blank covers beside the bench that grows taller during the shot; one plain wooden cane.

PALETTE: frozen cool blue-gray park; the friend's orange scarf muted; white hero with dark limbs.

COMPOSITION (9:16): medium-wide fixed frame: the frozen friend on the path on the right, the bench and the hero in the center, the tree above.

OPENING STATE: the friend frozen mid-laugh with one hand raised; the young hero standing beside the bench.

TIMED ACTION:
[0.0–3.6 s] Time-lapse of the hero only, fast-forward with short motion trails on the hero's whole body: he sits and reads, paces, sleeps on the bench, does push-ups, reads again; the stack of books beside the bench grows taller. Step by step he ages (gray eyebrows, short gray beard, slightly curved back) and ends standing next to the frozen friend, leaning on a wooden cane. The friend never moves.

SOUND: No speech, no voices, no narration, no music. Optional fast ticking only.

CLOSING STATE (out-point at 3.6 s): the aged hero leaning on his cane beside the unchanged frozen friend.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

### S11 — La question finale (film 54.2–59.6)

```text
OUTPUT: Source S11. Generate 6 seconds, 9:16 vertical. Retain 0.0–5.4 s (film 54.2–59.6 s).

ENVIRONMENT: Full-color 2D cartoon city park with a large tree, a wooden bench and a path, frozen in time: cool desaturated blue-gray, a few leaves hanging motionless, tiny pale-blue dust specks; soft background blur.

CHARACTER LOCK — THE HERO (aged state): One minimalist 2D cartoon protagonist with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth. The torso is a slim closed tapered shape with solid white fill inside its dark outline. Both arms and both legs are dark single-line strokes with constant medium weight; hands are small dark rounded shapes and feet are short dark rounded strokes. No hair or clothing accessories. Keep the same head-to-body proportions, white head and torso fill, and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design. Approved aged story state for this shot: light gray eyebrow strokes, a short gray beard drawn as a few simple strokes on the lower head, a slightly curved back, one plain wooden cane in his left hand. Head shape, white fill, proportions and line weight do not change.

CHARACTER LOCK — THE FRIEND: The protagonist's friend drawn in exactly the same minimalist 2D cartoon grammar: a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth; a slim closed tapered torso with solid white fill inside its dark outline; both arms and both legs are dark single-line strokes with constant medium weight; small dark rounded hands and short dark rounded feet. Exactly two arms and two legs. Distinguished only by a short orange scarf around the neck. Frozen mid-laugh with one hand raised, never moving.

PALETTE: cool blue-gray, a single electric-blue spark, fade to black.

COMPOSITION (9:16): the frozen friend small and blurred in the background; slow push-in from a medium shot to a medium close-up of the aged hero, centered, safe margins at the top and bottom for captions.

OPENING STATE (matches the previous shot): the aged hero leaning on his cane beside the frozen friend.

TIMED ACTION:
[0.0–1.8 s] The aged hero slowly turns away from the friend to face the camera, thoughtful.
[1.8–3.8 s] He raises his free small rounded hand beside his face, ready to snap; a tiny electric-blue spark flickers on it. His eyebrow strokes rise questioningly.
[3.8–5.4 s] He holds the pose looking straight at the viewer while the image slowly fades to black.

SOUND: No speech, no voices, no narration, no music. Optional faint spark crackle only.

CLOSING STATE (out-point at 5.4 s): black.

NEGATIVE: No visible words, letters, numbers, captions, subtitles, logos, watermarks or interface text; clocks have plain faces with hands only and no numerals. No speech bubbles or dialogue boxes. No generated speech, voices, narration or music. No photorealism, no 3D CGI humans, no realistic eyes, pupils or lips. No extra limbs, no duplicated arms or legs, no detailed fingers, no disconnected or broken lines, no changing line weight, no change of head or body proportions. No liquid morphing of objects, no unplanned extra characters or crowds, no people inside vehicles, no paper texture, no sketchbook border, no white card frame.
```

---

## 4. Guide de raccord

| Coupe | De → Vers | Lien |
|---|---|---|
| 8.0 | S1 → S2 | Continu : même salle, 3 médaillons allumés, le héros se tourne vers l'orange. |
| 13.3 | S2 → S3 | Changement de lieu : la main qui regarde (S2) → la main qui claque (S3). Coupe sur l'étincelle. |
| 17.8 | S3 → S4 | Même rue figée : vue haute large → niveau du sol. |
| 25.0 | S4 → S5 | Changement de lieu, coupe franche sur « Late for school? ». |
| 28.0 | S5 → S6 | Changement de lieu, coupe franche. |
| 31.5 | S6 → S7 | Continu : même tableau figé (vérifier pose du piéton et position du camion). |
| 36.7 | S7 → S8 | Changement de lieu ; ajouter un mini « whoosh » de gel au début de S8 (la classe est déjà figée). |
| 44.4 | S8 → S9 | Rupture voulue : clin d'œil → nuit sombre. Couper la musique net sur « But here's the catch ». |
| 50.6 | S9 → S10 | Changement de lieu : horloge qui s'emballe → time-lapse du parc. |
| 54.2 | S10 → S11 | Continu : héros âgé avec canne à côté de l'ami figé. |

Vérifie chaque raccord sur les images réellement gardées (pas seulement la fin du fichier généré). Si un clip déborde, coupe dans la plage utile ; ne ralentis pas la voix off.

---

## 5. Son, musique et sous-titres (montage)

**Pistes**
1. **Voix off** : le mp3 ElevenLabs Brian complet, posé à 0.0 s, jamais coupé ni régénéré. C'est l'horloge du film.
2. **Musique** : une seule piste continue (mystérieuse/épique légère, style « what if »), à environ −18 dB sous la voix. **Coupure nette à ~44.4 s** (« But here's the catch »), puis reprise plus sombre et lente jusqu'à la fin.
3. **Bruitages** : claquement + whoosh grave à chaque gel (~12.5, ~13.8, ~26.0, ~31.0, ~35.3 retour du temps), tic-tac à l'arrêt, petits pas, passage du camion (~35.8), tic-tac qui accélère en S9–S10.

**Sous-titres** : style de tes références : mots en gras blancs avec contour, une seule ligne, apparition mot par mot, **mot clé surligné** (fond violet ou rouge). Position : tiers inférieur, au-dessus de la zone de l'interface TikTok.

| Phrase | Mot(s) surligné(s) |
|---|---|
| Choose one power… but they come with a catch. | **power** · **catch** |
| Time freeze. Mind reading. Shapeshifting. Or super strength. | chaque nom de pouvoir |
| You chose… TIME FREEZE! | **TIME FREEZE!** |
| Imagine snapping your fingers… and the whole world just stops. | **stops.** |
| Cars frozen in the middle of the street. | **frozen** |
| Birds stuck in the sky. | **stuck** |
| A cup of coffee falling… that never hits the ground. | **never** |
| Late for school? Snap. Now you have all the time you need. | **Snap.** · **all the time** |
| Someone about to cross the road without looking? Snap. | **without looking?** · **Snap.** |
| You walk over… and gently pull them back. | **pull them back.** |
| Nobody ever knows you were there. | **Nobody** |
| You can sleep for ten hours… in the middle of a lesson. | **ten hours** |
| You can read every answer… during a test. | **every answer** |
| But here's the catch. | **catch.** |
| The world stops… but you don't. | **you don't.** |
| Every second you freeze, you still get older. | **older.** |
| One minute for everyone else… could be a whole year for you. | **one minute** · **a whole year** |
| So… would you still use it? | **use it?** |
| Tell me in the comments… and follow for episode two. | **comments** · **episode two.** |

**Overlays optionnels** : petit carton « 7:59 » sur S5, carton final « EPISODE 2 ? » sur le noir de S11.

---

## 6. Réglages conseillés

- 9:16, test en **plus basse résolution disponible** sur 1–2 clips, puis production finale en 1080p si dispo.
- Image de référence personnage (section 1b) jointe à chaque clip si l'outil le permet ; pour S7 et S11, tu peux aussi utiliser la **dernière image gardée** du clip précédent comme image de départ.
- Désactiver la musique et les voix générées si l'outil a l'option ; sinon couper la piste audio des clips au montage.
- Vérifie à chaque clip : un seul héros, 2 bras + 2 jambes, tête et torse blancs, aucun texte, aucun personnage en trop.
