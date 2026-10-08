# Journal

Newest entry first. One dated entry per run: what was done, what the numbers say, what to try next.

## 2026-10-08, 08:52 (scheduled run, nobody watching)

- State found: nothing in `ERROR`. TikTok 2 a day to 10-31, X 4 a day to 10-20 then five scattered posts.
  Both minimums (10 days TikTok, 7 days X) were already met; this run added buffer rather than filled a hole.
- Wrote 16 new dilemmas (`d01` to `d16`, bank now 75), rendered them, pushed to `2026-11/`.
  Counts: five 2-choice, four 3-choice, three 4-choice, two 5-choice, two 6-choice.
- Scheduled 16 X posts (10-21 to 10-25, each with its first reply) and 26 TikTok carousels (11-01 to 11-13:
  the 16 new ones plus the ten that were on X only). All 42 calls succeeded on the first try; every media
  URL came back as `.jpeg`. Confirmed with fresh `getScheduledPosts` calls: TikTok 2 a day from 10-08 to
  11-13, X 4 a day from 10-08 to 10-25, no slot double-booked.
- TikTok numbers, last 14 days (6 posts returned). Best: 10-03 18:39 (6,546 views, 221 likes, 10 comments),
  10-05 12:30 (5,315 / 190 / 14), 10-03 13:05 (3,128 / 114 / 3). Lowest: the first new-format post,
  10-07 21:15 "Who wins?" (555 views, 27 likes, 3 comments, 3 shares, but only about 12 hours old),
  10-03 07:05 (2,560 / 100 / 6), 10-02 22:47 (2,841 / 141 / 13). The five older posts are the previous
  format with the same hashtag-only caption. One new-format post, half a day old: nothing to conclude yet.
- X numbers: 73 followers on 10-07 (71 on 10-06). Two posts so far: 10-07 18:00 "Who wins?" 17 impressions,
  10-07 21:00 "All nerfed" 2 impressions; 1 reply each (most likely the automatic first reply), likes,
  reposts and follows empty. Total 19 impressions. `TTEV11` (impressions per day) has no value for 10-06
  and 10-07 and 0 for 10-08.
- Answer to the open question of 10-07: Metricool analytics timestamps are UTC, not Europe/Paris
  (the TikTok post scheduled for 21:15 Paris shows 19:15:59; the X posts of 18:00 and 21:00 show 16:00
  and 19:00). Add 2 hours in summer time, 1 hour from 10-25. The times above are converted to Paris.
- Consequence to settle with the owner, not acted on in this run: if the hour table of 10-07 (from the 187
  past posts) was built from these same timestamps read as Paris time, every hour in it is 2 hours early.
  The strong "20:00" would be 22:00 Paris, "14:00" would be 16:00, "17:00" would be 19:00, and the weak
  "18:00" would be 20:00 Paris, which is today's main TikTok slot. The evidence is three posts with an
  exact 2-hour shift; how the old table was built is not written down, so this is likely, not proven.
  The 14:00 and 20:00 slots are the playbook's rule and 74 TikTok posts sit on them: left as they are
  until the owner says whether to move them (for example to 16:00 and 22:00).
- Not verified: in `getScheduledPosts`, the first reply under the two published X posts still shows
  `PUBLISHING` the next morning, while the posts themselves show `PUBLISHED`. Analytics count 1 reply on
  each, so the reply probably went out, but no tool here can read the thread. Asked the owner to look.
- Practical notes for the next run:
  - `add_repo` does not exist in the scheduled session; the repository was already attached and
    `git push origin images` worked.
  - `getScheduledPosts` refuses ranges that return too much: keep each call to 7 days or less.
  - Text fit in the renderer: with 3 columns (3 and 5 choices) keep the detail line and the quote to about
    20 characters, with 2 columns about 28. A detail line that wraps makes the big keyword shrink.
  - Colours in the rendered image follow the position (A red, B blue, C green, D purple, E yellow, F cyan),
    not the colour letter in the bank entry. Matters when the text names a colour (the wands in `d12`).
- Next: X needs new dilemmas from 10-26. No reserve left, and reposts are only allowed from 10-28.

## 2026-10-07, 20:45 (in conversation with the owner): TikTok refuses PNG

- The first TikTok post (20:00, "Who wins?") failed: "The 'image/png' type is not allowed, use
  'image/jpeg' or 'image/webp' instead." Every TikTok post had been scheduled with PNG files.
- Fix: all 59 carousels converted to JPEG (`2026-10/<name>-1-cover.jpg`, `-2-dilemma.jpg`), pushed, and
  the 49 scheduled TikTok posts updated to those files. "Who wins?" moved to 21:15 the same evening.
- X posts were left as they are: X published a PNG without trouble at 18:00.
- Confirmed at 21:24: the 21:15 post shows PUBLISHED in Metricool with the JPEG files
  (https://www.tiktok.com/@blueredmemes/video/7694006799464189206). First TikTok post of the new format.
- Lesson: a scheduled post is not a tested post. Metricool accepts a file the network will refuse and
  only reports it at publication time, by email to the owner.

## 2026-10-07, evening (in conversation with the owner)

- The owner subscribed to X Premium today (2026-10-07). This is the reference date for X results.
- X baseline from Metricool: 71 followers on 2026-10-06. No post rows and 0 impressions recorded yet
  (X was connected to Metricool today; the first post of the new format went out today at 18:00).
  There is therefore no real "before Premium" period to compare with: follow the trend from here.
- X metrics that exist in Metricool: posts `TTTW02` (date and time), `TTTW03` (text), `TTTW11` (impressions),
  `TTTW05` (likes), `TTTW08` (replies), `TTTW06` (reposts), `TTTW30` (follows from the post);
  account `TTEV01` (followers), `TTEV11` (impressions per day). Not yet seen returning post rows.
- Monetisation on X needs 500 verified followers and 500,000 verified impressions in 90 days. At 71
  followers that is far away: the goal for now is followers and impressions, not revenue.

## 2026-10-07 (set-up, done in conversation with the owner)

- Connected Metricool (TikTok + X), this repository for image hosting, paid Metricool plan with the X add-on.
- Wrote and rendered 59 dilemmas. Scheduled 49 TikTok carousels and 59 X posts for October.
- Baseline before this format, from the owner's 187 TikTok posts (May to early October 2026):
  median views per post fell from about 10,900 in May to about 3,000 in October; best single post 503,619 views.
  About 30,900 followers on 2026-10-06.
- By hour (share of posts above 10,000 views): 20:00 41% (39 posts), 17:00 32% (28), 14:00 32% (19),
  10:00 39% (28), 18:00 9% (11). By day: Sunday 48%, Wednesday and Friday 42%, Monday 23%.
- Photo carousels: median about 7,300 views; videos: about 4,200.
- Open question: Metricool analytics timestamps are assumed to be Europe/Paris. Check with the first
  posts of the new format (a post scheduled for 20:00 should show as 20:00).
- X has no history yet. The 18:00 slot was chosen as US midday; revisit once posts have numbers.
- Added an automatic first reply (the account's own pick) under all 59 scheduled X posts, at the owner's
  request. Watch whether posts with a reply get more comments than the TikTok equivalents suggest.
