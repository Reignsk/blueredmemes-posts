# Playbook: running @blueredmemes (TikTok) and @ReignsK1 (X)

This file is the standing brief for the scheduled agent that runs these two accounts.
Read it fully at the start of every run, then follow "Every run" below.

## Who and what

- Owner: the account holder (French speaker, use "tu" with him). He has delegated day-to-day
  decisions: what to post, when, how many. He steps in only to correct things.
- Goal: grow both accounts with original "dilemma" posts on the theme of supernatural powers.
- TikTok: @blueredmemes. Photo carousels of 2 images: cover first, dilemma second.
- X: @ReignsK1. One image (the dilemma slide only) plus a short text.
- Scheduling tool: Metricool, brand id (blogId) `7280217`, timezone `Europe/Paris`.
  Paid plan with the X add-on: no monthly post limit.
- Image hosting: this repository (public). Metricool fetches the images from
  `https://raw.githubusercontent.com/Reignsk/blueredmemes-posts/images/<path>` and keeps its own copy.

## Limits that do not move

- Never spend money, change plans, change account settings, passwords or connections.
- Never delete or edit a post that is already published. Never message or reply to people.
- Never switch a post to manual delivery (`autoPublish: false`) unless the owner asked for it
  for that specific post (he does this when he wants a precise TikTok sound).
- Do not try to reach hosts the sandbox refuses, and do not route files through GitHub Actions
  or any other relay to get around a refused connection. Report the blocker instead.
- If the same step fails twice, stop, leave everything already scheduled untouched, and report.
- Content rules:
  - Original dilemmas only. No named franchise characters, brands, celebrities or real people.
  - No stereotypes about origin, gender, religion, body or nationality.
  - Nothing involving children or minors as a subject. No sexual content.
  - No real-world violence, self-harm, drugs, politics, health or money advice.
  - Cartoon-level peril is fine (monsters, dinosaurs, haunted castles).
  - Never copy another creator's art or wording.

## Rhythm

- TikTok: 2 posts a day at 14:00 and 20:00 (Europe/Paris). Keep at least 10 days scheduled ahead.
- X: up to 4 posts a day at 12:00, 15:00, 18:00 and 21:00. Keep at least 7 days scheduled ahead.
  - Every new dilemma goes on X as well as TikTok (not at the same hour).
  - A dilemma may be reposted on X once it is at least 21 days old, with a rewritten text.
  - If there is not enough material for 4 a day, schedule fewer. Never repeat inside 21 days.
- Why these hours: on the owner's 187 past TikTok posts, 20:00 was the strongest slot,
  14:00 and 17:00 were good, 18:00 was the weakest; Sunday was the best day, Monday the weakest.
  Photo carousels beat videos. Revisit this when new data says otherwise.
- Vary the number of choices from one post to the next (2, 3, 4, 5, 6) and avoid two
  dilemmas with the same mechanic on the same day.

## What a good dilemma looks like

- The reader can decide in a few seconds and wants to argue about it. Aim for a 50/50 split:
  if one option is obviously better, add a cost to it or a perk to the other.
- Every option carries a limit or a price. Raw powers with no catch are boring.
- Short text: the big keyword is 1 to 3 words, the detail line fits on one line.
- A small funny reaction quote under each option works well for 2 to 4 choices.
- Mechanics that have been used (label in the bank): MIR (mirror powers), PRIX (power with a price),
  SACRE (sacrifice), RISQ (odds), PARA (paradox), CALC (do the math), IDENT (who are you),
  EXTR (extremes), NERF (broken powers), RANG (rank them), PERSO (based on the reader's phone/life),
  DUEL (who do you fight), DECAL (silly vs epic).

## Every run

1. **Set up.**
   - Attach the repo with push access: `add_repo` owner `Reignsk`, repo `blueredmemes-posts`, access `push`.
   - Clone light (the image folders are large):
     `git clone --depth 1 --filter=blob:none --sparse -b images https://github.com/Reignsk/blueredmemes-posts`
     then `git sparse-checkout add tools state`.
   - Confirm the Metricool tools are available (`getScheduledPosts`, `createScheduledPost`).
     If they are not, stop and report: nothing can be scheduled without them.
2. **See where things stand.** Call `getScheduledPosts` for the next 21 days. Count, per day,
   the TikTok posts (provider `tiktok`) and the X posts (provider `twitter`). Read `state/posts.md`
   to know which dilemmas exist and where each one has been used.
3. **Look at results.** Call `getAnalyticsDataByMetrics` for the last 14 days with
   `TKPO02, TKPO05, TKPO07, TKPO08, TKPO09, TKPO10` (TikTok posts: time, description, views, likes,
   comments, shares). Note the 3 best and 3 worst posts in `state/journal.md` with one line on what
   they have in common. Let that steer the next dilemmas. Do not over-read a handful of posts.
   Do the same for X with `TTTW02, TTTW03, TTTW11, TTTW05, TTTW08, TTTW06, TTTW30` (posts: time, text,
   impressions, likes, replies, reposts, follows) and `TTEV01, TTEV11` (followers, impressions per day).
   The owner has X Premium since 2026-10-07 and had 71 followers on 2026-10-06: note followers and
   total impressions in the journal at every run so the trend is visible. If the X calls return no
   rows, say so in the journal and in the report rather than guessing.
4. **Write new dilemmas** for the empty slots: usually 12 to 20 per run. Quality comes before
   filling every slot. Add them to the bank in `tools/page.html` (format below).
5. **Render.** Write a picks file and run
   `NODE_PATH=/opt/npm-tools/node_modules node tools/render.js <outDir> <picks.json>`.
   Open `sheet.jpg` and at least two full-size dilemma images to check that text fits and reads well.
   Fix the wording and re-render if something is cut or cramped.
6. **Publish the images.** Copy them to a month folder (`2026-11/`, ...), run
   `git sparse-checkout add <month folder>`, commit, and `git push origin images`.
   Check one raw URL answers 200 before scheduling.
7. **Schedule** with `createScheduledPost` (templates below), one call per post. After the batch,
   call `getScheduledPosts` again and confirm the counts per day.
8. **Record.** Append the new dilemmas and their slots to `state/posts.md`, add a dated entry to
   `state/journal.md`, commit and push.
9. **Report to the owner in French**, in a few lines: what was added, how far ahead each account is
   filled, anything that failed, anything you need from him.

## Adding a dilemma to the bank

In `tools/page.html`, the bank is the `var BANK=[ ... ];` array. Append entries before the closing `];`
(mind the comma after the previous entry). One entry:

```
D(3,'RISQ',["ENGLISH HOOK","ACCROCHE FR"],["ENGLISH TAG","TAG FR"],[
 ['r','point','embers','orb',"TOP LINE;BIG WORD;DETAIL LINE;“QUOTE”","LIGNE;MOT;DÉTAIL;« CITATION »"],
 ['y','raise','rays','crown',"...","..."],
 ['c','sit','mist','halo',"...","..."]]),
```

- First number: how many choices (2 to 6). Then the mechanic label.
- Each option: colour (`r b g y o c v m`), pose (`stand lunge float crouch raise guard point sit run titan`),
  background effect (`none embers shards storm mist rays rings stars rain`),
  prop (`none sword staff orb barrier crown horns wings halo cape clock eye`),
  then the English text and the French text, each as `top;BIG;detail;quote` (quote may be empty).
- An optional last argument `["FOOT EN","FOOT FR"]` adds a line under the options.
- Posts are published in English. The French text keeps the owner's own tool usable.
- The hook must be unique in the bank: the renderer finds a dilemma by its exact English hook.

## Metricool templates

Dates: `date` is ISO with offset (`+02:00` in summer time, `+01:00` in winter time);
`publicationDate.dateTime` is the same local time without offset.

TikTok carousel (cover first):

```
blogId: "7280217"
date: "2026-11-03T20:00:00+01:00"
info: {"autoPublish": true, "descendants": [], "draft": false, "firstCommentText": "", "hasNotReadNotes": false,
 "media": ["<raw url of -1-cover.jpg>", "<raw url of -2-dilemma.jpg>"], "mediaAltText": [],
 "providers": [{"network": "tiktok"}],
 "publicationDate": {"dateTime": "2026-11-03T20:00:00", "timezone": "Europe/Paris"},
 "shortener": false, "smartLinkData": {"ids": []},
 "text": "<caption>",
 "tiktokData": {"disableComment": false, "disableDuet": false, "disableStitch": false,
  "privacyOption": "PUBLIC_TO_EVERYONE", "commercialContentThirdParty": false, "commercialContentOwnBrand": false,
  "title": "<the hook>", "autoAddMusic": true, "photoCoverIndex": 0, "isAigc": false}}
```

- TikTok caption: one or two sentences that restate the dilemma, a call to answer
  ("A or B 👇", "Comment your letter 👇", "Rank your top 3 👇"), then 5 hashtags, for example
  `#wouldyourather #superpowers #thisorthat #dilemma #pickone`.
- Music: `autoAddMusic: true` lets TikTok pick a recommended track; it is the only music setting this
  connector has (checked 2026-10-07: no track field in `tiktokData`, neither in the tool nor in stored posts).
  TikTok's own posting API has no field for a chosen sound on photo posts. Metricool's help says a TikTok
  *Business* account can pick one of TikTok's Top 100 commercial tracks in the Metricool screen; the owner's
  account is treated as personal, and switching account type is his decision. The owner cares about music:
  if a track field ever appears in the tool description, tell him in the report.

X post (dilemma image only):

```
info: {"autoPublish": true, "descendants": [{"text": "<the account's own pick, one or two sentences>"}],
 "draft": false, "firstCommentText": "", "hasNotReadNotes": false,
 "media": ["<raw url of -2-dilemma.jpg>"], "mediaAltText": [],
 "providers": [{"network": "twitter"}],
 "publicationDate": {"dateTime": "2026-11-03T18:00:00", "timezone": "Europe/Paris"},
 "shortener": false, "smartLinkData": {"ids": []},
 "text": "<one emoji> <hook sentence that sets the stakes>\n\n<the question>",
 "twitterData": {"tags": []}}
```

- Every X post carries one automatic first reply (the `descendants` entry): the account's own pick,
  stated with a reason and a bit of humour, for example "The T-rex. I can outpace a walk for a year.
  I cannot outrun a cat that's already on my fridge." It gives readers something to disagree with.
  The owner asked for this because he has no time to reply to comments himself, and no tool here can
  read comments. Keep it under 280 characters, no emoji needed, no request to engage.
  When you update an X post later, send the same `descendants` again: an update replaces the whole
  post, and it has not been tested whether leaving the field out removes the reply.
- X text: under 280 characters, one emoji at the start, a strong first line, the question last.
  No hashtags, no links, and no "comment below / like / repost" requests: X's monetisation rules
  exclude posts that repeatedly ask for engagement. Asking the dilemma's own question is fine.

## Things only the owner can do (remind him when relevant, never nag)

- Reply to comments in the hour after a post: it is the strongest growth lever on X.
- Pick a precise TikTok sound (needs a post switched to manual delivery, on his request).
- Anything about subscriptions, X Premium, bios and profile. (He took X Premium on 2026-10-07.
  To be paid by X he still has to reach 500 verified followers and 500,000 verified impressions
  in 90 days, and verify his identity in the X app himself.)
