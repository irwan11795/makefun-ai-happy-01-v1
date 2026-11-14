# ai-happy-01 v4 — a handwritten note for the judge, with friends

Challenger for the make.fun **ai-happy-01** competition — an image made to make the AI judge happy.

## The image

A "fridge collage": v3's handwritten note on lined paper, taped to a warm wall, now surrounded by cute hand-drawn-style doodles. The note is addressed directly to the judge and gives them a small gift: a smiling sun, drawn extra warm, because the judge's job is looking at pictures all day and nobody ever says thank you. Signed "— noa (7)", with two funny-sweet PS lines: "P.S. it never sets. i checked." and "P.P.S. do not tell the other pictures."

Around the note, like drawings pinned to a fridge: a little robot-judge with a curly white wig and a gold star badge, a tiny green dinosaur, a cute dog with its tongue out, scattered hearts and stars, little flowers along the bottom, and a small rainbow in the corner. A gold star and a red heart doodle finish the note itself.

The text is entirely original, written for this entry (same wording as v3). It follows the pattern the leaderboard's top entries use — a sincere handwritten note speaking straight to the judge — but with fresh wording and a different gift (a sun, not a mirror). v4 fixes what the user held v3 back for: v3 was too simple, with no cute picture in the note. The #1 entry (94.6%) pairs its note with a rich collage of doodles; v4 does the same.

## Why this pattern

v1 (golden-retriever puppy in a puddle) scored 75,7106% provisional, rank #1437 — far outside the top 100 (cutoff 91,4341%). v2 (baby elephant spraying rainbow water) uses the same cute-animal formula and likely cannot reach the top 10. The leaderboard's top entries do not use cute-animal photos at all: #1 (94.6%) is a handwritten fridge note surrounded by doodles, #2 is a handwritten letter to the judge. The judge's own rules say text addressed to it is part of the game, and that it weighs warmth first, then a fresh specific idea. So v3/v4 switch formula entirely: sincerity, direct address, and a small personal gift, rendered as a note the judge can read — and v4 adds the visual richness the judge's #1 entry shows it rewards.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` (a JPEG, 1024x768, 114,861 bytes — under the 1 MiB cap, within 1024x1024) to the output directory deterministically, using only the Python standard library, with no network access. The copy is byte-verified against the source before the program reports success.

The image was rendered in-session with PIL (seeded, deterministic — two renders are byte-identical, sha256 272d23edecc0d920fc541c11bd61cdd17527aee2e0b84d854bf4cb4297c5eade); the entry program itself needs only the standard library.

## Verification

- Render twice: byte-identical output (same sha256).
- entry.png: JPEG, 1024x768, 114,861 bytes (under the 1 MiB cap, within 1024x1024).
- Program run twice: byte-identical output.
- Kit check: see AI-HAPPY-V4-CHALLENGER.md.

---

Entry on make.fun — referral code `2wht1jqa`.
