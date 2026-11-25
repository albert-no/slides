# Work r1 — 2026-11-25-261128yonseimath-final-edits

Branch `2026-11-25-261128yonseimath-final-edits` from baseline `0bf4927`; the PR #81 head is still `0bf4927`. All work was done inline: five slides plus the note were too small to split into packages. No slide-ID commit was needed because IDs already exist. The new slide is S26.

## Page mapping (baseline → new)

| Baseline p | New p | ID | Change |
|---|---|---|---|
| 1 | 1 | S01 | main unchanged; note: "세부 이력은 넣지 않습니다" removed, now points to the next page |
| — | 2 | S26 | new: speaker introduction (C01) |
| 2–18 | 3–19 | S03…S18 | unchanged except the footer total |
| 19 | 20 | S19 | problem/idea framing added (C02/C03) |
| 20 | 21 | S20 | highlight deleted (C04) |
| 21 | 22 | S23 | replaced: same perimeter → largest rectangle area (C05) |
| 22 | 23 | S24 | main unchanged; note bridge rewritten |
| 23 | 24 | S21 | sub-captions deleted (C06) |
| 24 | 25 | S22 | unchanged |

## Requests

- **C01 — S26 "영재원 수료생에서 교수로".** A vertical five-point timeline (`.ym-path`) showing the five milestones in the supplied order, with no years. The last dot is filled and blue to mark the current role. Hongik carries "(전)". Stanford is shown as "Stanford 전기공학 석사 · 박사 (MS/PhD in EE)": the plan's Korean form, with the requested English kept in parentheses. The cite line gives the profile URL. The note article (≈40 s) is a first-person script using the same five facts. Its sources section says which items the profile supports (E02) and which come from the author's self-report (E01).
- **C02/C03 — S19.** Two labelled lines above the loop: "문제: LLM이 생성한 문장에 표식 남기기" and "아이디어: 의도적인 통계 삽입". I kept the "10번 중 7번이라면?" sub-label because it fits without crowding. The note explains once that 통계 삽입 means biasing word choice so the text carries a detectable statistical property, not printing numbers (E04). The Kirchenbauer citation is added to that source line.
- **C04 — S20.** The highlight is deleted with no replacement; the flow diagram remains, vertically centred. The note's msg and script no longer make the contrast. The msg now reads "수학을 말로 설명해 보고, 식이 어떤 의미인지 이해하는 것이 연사에게 오래 남았다".
- **C05 — S23.**
  - Title: "같은 둘레의 직사각형 중,<br>정사각형의 넓이가 가장 크다".
  - Figure: a rectangle with sides `a` and `b` beside a square with side `(a+b)/2`. Both carry the caption "둘레 2(a+b) · 넓이 …". Below them sits one math block: `ab ≤ ((a+b)/2)²  (같을 때: a=b)`.
  - The shapes are plain HTML boxes at one isotropic scale, 36 px per unit, with internal inputs a=2, b=8, m=5: the rectangle is 288×72 px and the square 180×180 px. Both perimeters are 20 units; the areas are 16 and 25. No numbers appear on screen.
  - The parameters are recorded in a CSS comment, in the note's source line and in the leaf OUTLINE. No generator or asset change was needed.
  - Removed: all growth wording, the growth rows and the `.ym-grow` CSS.
  - Note (60 s): the fixed-perimeter reading; an optional line `((a+b)/2)² − ab = (a−b)²/4 ≥ 0` (E03); and the scope sentence "직사각형끼리의 비교이며, 모든 평면도형…이 아닙니다".
- **S24.** The main slide is untouched. In the note, "성장 이야기와…" became "같은 둘레에서 정사각형이 가장 넓다는 이야기와 곡선이 휘는 이야기가 하나로 이어집니다".
- **C06 — S21.** Both sub-captions are deleted and the two boxes and arrow remain. The note's reading guide now describes only the boxes and arrow. The script drops both example callbacks, including the AM–GM growth one.

## Wording deviations (my calls)

- I wrote "표식 남기기" with a space, following standard Korean spacing; Albert's text has "표식남기기". It is a one-character change if he wants the exact form.
- S26 uses "심화반 · 사사반" and "전기공학부 · 수리과학부" (middle dot) in place of the slash, to match the deck's separator style. The content is unchanged.

## Shared surfaces

- Footer: `1 / 25`. The `<!-- SLIDE N -->` comments are renumbered.
- Note:
  - 25 articles; h2 numbers renumbered.
  - Elapsed times recomputed.
  - Pacing table: 1–8 6:10 · 9–18 11:00 · 19–25 6:50 · buffer 1:00 · total 25:00. Speech totals 24:00: S26 adds 40 s and S23 drops from 100 s to 60 s. S20 and S21 keep 70 s; I did not pad.
  - In-note cross-references updated: "슬라이드 8–17" → "9–18", "슬라이드 7" → "8".
- OUTLINE:
  - Leaf: counts 25/25, section table, all slide pointers, CSS range `:17-157`, class list, job credit.
  - Root: description (fixed-perimeter area, 25 slides) and both lookup rows (`:347-483`, `:538-577`); the AM–GM row now says fixed-perimeter area.
- Grep for 성장/들쭉 in the deck, note and both outlines: 0 hits for the talk.

## Unsourced facts

None added. Every biographical item traces to E01 and/or E02. The geometry is our own calculation per E03.

## Checks

- `lint-deck.py`, deck and note: ok. `find-wordy`, `find-dense`: no flags. `outline-lint`: 0 stale; the 5 warnings are pre-existing and in other folders.
- Print render at -r 60: 25 pages. I checked p2, p20, p21, p22 and p24, and the neighbours p3 and p23.
  - p22 overflowed on the first try: the math block ran into the footer, and inline `\frac` side labels were too small. Fixed by tightening the layout and using the `(a+b)/2` slash form, not by shrinking type. Labels are 1.7rem.
- KaTeX: 0 errors in the deck. The note shows 0 errors at both 430 and 1280 widths, with 25 articles.
- Demo (CDP, unchanged files): at 14 / 25 it loops, pauses, restarts and resets on re-entry. Under reduced motion it shows the static frame with buttons hidden. The player has no page-index dependency.
- Files staged: the deck, the note, leaf and root OUTLINE, and this record. No `reference/`, engine or demo file was touched.
