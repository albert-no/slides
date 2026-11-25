# work-r1 — 2026-11-25-261128yonseimath-polish

- Branch `2026-11-25-261128yonseimath-polish`, from baseline `37757bb`.
- Content commit: `9bf53d8`. The log commit that adds this file is the pointer SHA.
- No new ID-only commit. The inherited IDs come from `1e7b5b9`. The new IDs follow PIPELINE: S10 splits into S10a/S10b, and S25 is new and sits after S10b. S02 and S16 are retired; their IDs are not reused.
- PR #81's head `2026-11-24-261128yonseimath-draft` was not touched and stays at `37757bb`.

## Packages

I did all three packages inline, without subagents. The content and wording calls are judgement calls, and the deck is a single 24-slide file.

- **P1 (S04–S08)**
  - S04: title "IMO 2025 Gold Medal". The only exhibit is the score 35 / 42, with the line "금메달 수준 · Google DeepMind의 Gemini Deep Think" and a muted line on the official grading basis. The six-box grid is gone.
  - S05: title "Navier–Stokes: 밀레니엄 문제". The original OpenAI vortex image is shown at 480 px, with "OpenAI의 해법 발표 · 2026. 9. 8.". The fluid definition, timeline and recognition highlight are gone.
  - S06: the C04 cards are used verbatim, and both quoted conclusions are removed.
  - S07: the AI label is now "코딩 · 추론 · 탐색", and the history disclaimer is deleted.
  - S08: 무엇을 만들고 싶은가? → 어떤 수학 문제로 바꿀 수 있을까? → 어떻게 구현할까?, with the example line "예: AI가 쓴 글에 표식을 남기려면?".
- **P2 (S10a, S10b, S25, S11–S15, S17; S16 deleted)**
  - S10a: hypothetical 독서 감상문 sheet with the question "학생이 쓴 글일까, AI가 쓴 글일까?".
  - S10b: removable [AI 생성] tag vs an ordinary-looking text.
  - S25: parity bridge (stats below).
  - S11: "ChatGPT 같은 LLM의 기본 원리", the 40/30/20/10 bars, and the two E05 sentences.
  - S12: looping demo (spec below).
  - S13: the C12 sentence and split bars 50/50 → 60/40 (chosen) vs 100 (awkward).
  - S14: question only, coins figure and key.
  - S15: answers the question.
  - S17: AI 작성글에 표식을 넣자 → 수학문제화 (확률에 bias를 추가해 통계적 특성을 심는다) → 통계 문제.
  - S16 is removed from the deck and the note. Its limits (editing, translation, short text, "no trace ≠ human", ICLR 2024, SynthID) are now an optional paragraph in the S17 note.
- **P3 (S19, S20, S23, S24, S21)**
  - S19: the C16 title and the loop 아이디어 → AI와 함께 구현 · 실험 → 결과를 보고 새 아이디어, with "AI도 아이디어를 낼 수 있다". "확인은 반드시 따로" is deleted.
  - S20: the C17 phrase is deleted, and the slide is one personal statement plus the 공식·기법 → 말로 설명하기 → 의미와 직관 flow.
  - S23: growth paths 1 →a→ a →b→ ab vs 1 →m→ m →m→ m², with ab ≤ ((a+b)/2)² ⟺ √ab ≤ (a+b)/2. The rectangles are gone and `rectangles.svg` is deleted.
  - S24: compares log((a+b)/2) ≥ ½log a + ½log b directly, and says "concave". The figure is labelled only with a, b, (a+b)/2 and the two symbolic heights; the 2, 8, log4 and log5 labels are gone.
  - S21: the two-part close 수학을 직관으로 이해하기 → 현실 세계의 문제에 적용하기, with sub-labels AM–GM = 성장 이야기 and 글의 표식 = 통계 문제.
- **Shared**
  - S01 has no subtitle. S02 (contents) is deleted (C01).
  - S09 title: "AI가 쓴 글에 보이지 않는 표식 남기기", subtitle "LLM watermarking" (C07).
  - Footer `1 / 24`.
  - Note rewritten: 24 articles, same IDs and order as the deck, evidence renumbered to E01–E11, new pacing table.
  - Leaf and root `OUTLINE.md` updated.

## Slide mapping

| ID | Old page | New page | Change |
|---|---|---|---|
| S01 | 1 | 1 | — |
| S02 | 2 | — | retired (C01) |
| S03 | 3 | 2 | — |
| S04 | 4 | 3 | — |
| S05 | 5 | 4 | — |
| S06 | 6 | 5 | — |
| S07 | 7 | 6 | — |
| S08 | 8 | 7 | — |
| S09 | 9 | 8 | — |
| S10a | 10 | 9 | split |
| S10b | 10 | 10 | split |
| S25 | — | 11 | new, after S10b |
| S11 | 11 | 12 | — |
| S12 | 12 | 13 | — |
| S13 | 13 | 14 | — |
| S14 | 14 | 15 | — |
| S15 | 15 | 16 | — |
| S16 | 16 | — | retired (C14); limits moved to S17 note |
| S17 | 17 | 17 | — |
| S18 | 18 | 18 | — |
| S19 | 19 | 19 | — |
| S20 | 20 | 20 | — |
| S23 | 21 | 21 | — |
| S24 | 22 | 22 | — |
| S21 | 23 | 23 | — |
| S22 | 24 | 24 | — |

## Deviations (my calls, for review)

- **S08 title (C06).** The title is "현실 문제를 풀려면 수학을 이해해야 한다", a shorter spoken paraphrase of "현실 문제를 풀기 위해서는 수학적인 이해가 중요하다.". It is the title rather than a highlight, so the point is not stated twice.
- **S09 (C07).** I kept the exact requested wording rather than a shorter paraphrase.
- **Vertical centring.** Most diagram slides left the lower half empty. A local wrapper `.ym-mid` now centres the content under the title on S06–S08, S10a, S10b, S13, S17 and S19–S21. Type is unchanged.
- **S05.** The figure is 480 px wide. That keeps the date line and the one-line cite clear of the footer at body size.
- **S24.** The figure is 820 px wide, so the inequality block fits above the cite.

## Demo spec (S12, C11/C12)

- **Files.** `figs/watermark-demo.js` (player) and `figs/watermark-demo-data.js`. Both are local, with no network requests, so the demo works offline. The data is written and asserted by `figs/generate-figures.py`.
- **Sentence.** "오늘 점심은 김밥을 친구와 나눠 먹었다.", built left to right in four steps. Each step has five phases: candidates (2.0 s) → green/red split (2.0 s) → boost (2.2 s) → pick ▶ (1.6 s) → append (1.4 s). A 3.6 s hold on "완성된 문장" follows, then a restart. One loop is about 40 s.
- **Probabilities.** 40/30/20/10. Green words get ×1.5, then everything is divided by 1.25, which gives 48/12 for green and 24/16 for red. Green mass goes from 50% to 60%.
- **Red pick.** Step 2 picks the red word 친구와.
- **Styling.** Ghost dashed bars show the original probabilities. Green bars are solid and red bars are striped, and each row also carries the text label 초록/빨강, so colour is never the only cue.
- **Controls.**
  - On-slide ❚❚/▶ and ↺ buttons. They stop propagation, so clicking them does not change the slide.
  - P and R keys, active only while the slide is shown.
  - The loop runs only on the active slide and restarts at step 1 on re-entry.
- **Static frame.** Used for print (`beforeprint`, and the buttons are hidden in `@media print`) and for `prefers-reduced-motion`. It shows the full sentence plus step 2 after the boost, with the red pick.
- **Not changed.** No shared engine or `reference/` files were changed.

## Sources and assets

- `figs/navier-stokes-vortex.png`: the original OpenAI asset (E03 URL, images.ctfassets.net …/navier-stokes-light-master.png), 1254×1254, stored unmodified. sha256 `2bd5e5ec2c365ddf864196bf11144e001a1ada6fcf006744de91eb2a20199a93`.
- `figs/image-original-gray.png`: NASA GSFC Blue Marble 2002, `blue_marble_modis_north_america_print.jpg` (svs.gsfc.nasa.gov/30614), 1024×574. The source JPEG has sha256 `cd67492d…0eba`, and the full hash is recorded in the generator header. It was converted to 8-bit gray at the same size and saved as PNG. sha256 `68f4b00d9ba37968bceec68e2d7527a31fb8088cad41a3648a9c0056afb78f1c`.
- `figs/image-all-odd.png`: the even values x of the gray image replaced by x+1, saved as lossless PNG. sha256 `609e5bb02b61235d39c57cd8690b3cfee6487278f65c309d7d1b787506897b24`.
- **Parity stats**, recomputed from the stored files by the generator: 587,776 px; odd fraction 18.3721% before and 100% after; 479,789 px changed; maximum |diff| 1. The original's odd fraction is not near 50%, because the image has a large black background. The slide and note do not claim 50%.
- `generate-figures.py` is deterministic: a rerun leaves every file in `figs/` byte-identical.
- Coin tail: P(K ≥ 70) = 0.00003925069822796835, unchanged. 7-of-10 tail: 176/1024 (note only). Log figure: ln 4 ≈ 1.386 < ln 5 ≈ 1.609, used for geometry only and not shown.

## Plan issues

None blocking.

## Unsourced facts

None left in the deck or note. In the note I removed two phrases that are not in `evidence.md`:
- "필즈상 수상자인" before Terence Tao
- "상금이 걸린 일곱 개의" before 밀레니엄 문제

If you want either back, add them to evidence first.

## Checks run

- `lint-deck.py`: ok for the deck and ok for the note. `find-wordy.py` and `find-dense.py`: no flags. `git diff --check`: clean.
- `outline-lint.py`: 0 stale pointers. The 5 warnings are inherited, all in `courses/infotheory` and `courses/privacy`.
- **Render.** All 24 slides were rendered at 1280×720 with `-r 60`, and the changed pages were rechecked after each fix (overflow on S23/S24 and empty lower halves fixed). The final pages show no clipping and no footer collisions. Type was not shrunk anywhere.
- **Note.** Rendered at 430 and 1280 widths; 0 KaTeX errors.
- **Deletion strings.** None remain in the deck or the note: 오늘의 세 가지 질문, 역사의 단계가 아니라, 코딩 · 추론 · 탐색을 돕는다, 글에 숨긴 확률, 흔적은 단서, 정식화, 선택을 조금 기울이고, 확인은 반드시 따로, 이곳 영재원에서도, 이해한 만큼, AI와 함께 더 많이 묻고, 오목.
- **Demo**, tested in headless Chrome via CDP:
  - Two full loops of about 40.5 s each, with the order 김밥을(G) 친구와(R) 나눠(G) 먹었다.(G), then the hold, then a restart.
  - Pause freezes the loop, and resume continues it.
  - R restarts it.
  - Leaving the slide shows the static frame and stops the timer. Re-entering restarts at step 1.
  - Clicking the buttons does not navigate: the deck stays at 13 / 24.
  - With reduced motion, only the static frame is shown.
- **Timing.** 24:00 of narration plus a 1:00 buffer. The per-slide budget is in the note header and articles.
