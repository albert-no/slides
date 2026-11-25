# work-r2 — 2026-11-24-261128yonseimath-draft

This round responds to `review-r1.md`. The plan is still `plan-v2.md`, and the slide IDs are unchanged.

## Branch

- Branch `2026-11-24-261128yonseimath-draft`, starting from `fae496e` (r1).
- The head SHA is in the pointer message.
- Copied unchanged: `review-r1.md`, plus the refreshed `job.md`, `requests.md` and `evidence.md` (E22, E23).

## Findings

**F01 (blocking): done.** My r1 size claim was wrong. DS body is 1.55rem, and the 1.5rem boxes were below it. All primary diagram text is now at least 1.55rem:

- `.ym-row` and `.ym-4` flow boxes: 1.5 → 1.55rem. Padding went from 18/22 to 16/20 px. I did not touch the type.
- Overlay labels `.fl`: 1.5 → 1.55rem.
  - Three labels moved from the 1.3rem tick class to primary, because they are argument labels: the S15 tail value "약 0.0039%" and the S24 ticks $a=2$, $5$, $b=8$.
  - The S15 axis ticks 0/50/100 stay at 1.3rem as genuine secondary ticks, above the 1.25rem floor.
- S04 problem tiles: 1.4 → 1.55rem.
- S10 text cards: 1.45 → 1.55rem.
- S11/S13 bar values: 1.5 → 1.55rem.
- S13 before/after probabilities: 1.3/1.5 → 1.55rem throughout. The paired track grew from 52 to 60 px so the two lines fit.
- S12 row labels: 1.45 → 1.55rem.
- S19 loop label: 1.35 → 1.55rem.

All of these fit without a split.

**F02 (blocking): done.**
- The S13 main line now reads "길게 모아 통계로 찾는 흔적".
- In the note at S13, the 메시지 and the two script sentences are replaced with your wording. The quality trade-off, probabilistic selection and S16 limits are kept.

**F03 (blocking): done.** The note at S23 now says "둘레가 같은 직사각형 울타리 중에서는 정사각형으로 둘렀을 때 넓이가 가장 큽니다."

**F04 (blocking): done.** The note at S05 uses your wording for both sentences, with no present-status claim.

**F05 (blocking): done.**
- S05: the OpenAI and Clay citations are on separate lines (`<br>`) and clear the footer.
- S04: the full official title (E22) wrapped mid-title on one cite line. The main slide therefore uses a descriptive reference that is not presented as a title: "Luong & Lockhart, Google DeepMind blog post on Gemini Deep Think at IMO 2025 (gold-medal standard), 2025-07-21".
- The note at S04 carries the exact E22 title.

**F06 (preference): taken.** The note at S12 uses your wording, so it no longer suggests secrecy.

**F07 (preference): taken.**
- The note at S15 drops the summation and the z-expression. It keeps the model, the exact tail value, the one-sided reading, the reproduction code and the non-independence caveat. "2만 5천 번에 한 번" is now explained as the rounded reciprocal of that tail value.
- The note at S19 drops the sum chain and keeps 176/1024 ≈ 0.17 and the code.
- The leaf OUTLINE pointer is updated to match.

## Slide mapping

No change from r1. There are no splits or moves.

## Outline

- Removing one CSS line shifted every deck line by −1.
- Leaf: section ranges, slide pointers and local CSS `:17-92` are updated.
- Root: the two lookup rows are now `:284-437` and `:486-529`.

## Plan issues

None.

## Unsourced facts

None added. No fact was changed from memory. The wording changes follow E22/E23.

## Checks

- `lint-deck.py`: ok on the deck and the note.
- `find-wordy.py`: no flag on the deck. The note has one existing prose flag on the S22 closing script (spoken text).
- `find-dense.py`: no flags.
- `outline-lint.py`: 0 stale pointers. The 5 warnings are pre-existing.
- Render at `-r 60`, pages 04, 05, 10, 11, 12, 13, 15, 19, 21 and 22. These are all the pages that use the changed styles or labels. There is no overflow and no overlap, and the S04/S05 cites are each on one line per citation and clear the footer.
- The note overflow check still passes. My headless window bottoms out at a 500 px viewport. Your 430 px `innerWidth` test is the stricter one.
