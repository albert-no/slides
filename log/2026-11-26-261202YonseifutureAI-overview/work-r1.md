# work-r1 — 2026-11-26-261202YonseifutureAI-overview

- **Branch:** `2026-11-26-261202YonseifutureAI-overview`, from baseline `467cf06`.
- **Head:** the commit named in the pointer. It contains this file and refreshed copies of `job.md`, `requests.md` and `evidence.md`.
- **ID commit:** `46d0148` (attribute-only). It adds paired `data-slide-id` S01–S46 to the main deck and the note articles. It follows the scaffold commit `0ac6f89`, which created the 46-slide skeleton, the note, the outline stub and this record.
- **Files:**
  - `talks/261202YonseifutureAI/261202YonseifutureAI.html` (46 slides)
  - `…-note.html` (46 articles plus a pacing table)
  - `figs/` (2 PNGs)
  - leaf `OUTLINE.md`
  - root `OUTLINE.md` entry

## Packages

There were five workers, each in its own worktree with a disjoint slide range and a class prefix. Integration spliced each package by slide ID and note article. I own the shared surfaces: S01, S10, S11, S15, S29, S38, S45, S46, the `.fa-*` kit, OUTLINE and the record.

| Pkg | Slides | Worker commit | Integration commit | Notes |
|---|---|---|---|---|
| Integrator | S01, S10, S11, S15, S29, S38, S45, S46 | — | `242f3ca`, `89ff574` | S45 decision card (`yi-`). The S45 note ties each question to an earlier case (weekly manual, email reader, the 2025 public-issue demonstration, Mata, Air Canada) in evidence wording (E03, E06, E07, E08). |
| P1 | S02–S09 | `9f6b230` | `b434839` | Opening story. It defines the role-colour vocabulary used by every later flow. |
| P2 | S12–S21 | `4429024` | `565d836` | Sections 01–02, first half. |
| P2 (p5) | S22–S28 | `0cfb731` | `565d836` | Section 02, second half. Includes the Carlini figure and the S25 chart. The P2 CSS block is shared: p5 lines sit under `/* p5 */`. |
| P3 | S30–S37 | `046245c` | `ce44801` | Section 03. Includes the Eykholt figure. |
| P4 | S39–S44 | `28d89c5` | `b24a193` | Section 04. |
| Reconcile | S34, S44 | — | `d172dd1` | The S34 email body now matches S06 ("The fall thesis forms are attached."). The S44 "Me" node is now green `fa-check` ("approves"), matching S08. |

Cross-package terminology was reconciled:
- Approval is always "Me", green, "approves".
- Outside text is always red dashed.
- Recommended checks are always amber dashed with the label "Recommended". They are kept distinct from Albert's stated workflow, per the accuracy decision in `job.md`.
- S36's "Recommended check before the coding agent runs" makes the existing approval concrete (its note says so); S44's "Recommended: review the site change" is a further, downstream safeguard. Kept as two distinct recommendations.

## Slide mapping

There is no old deck. Slide ID equals display page: S01–S46 are pages 1–46, in plan order, with no splits, moves or retirements. Line pointers are in the leaf `OUTLINE.md`.

## Timing

The note's per-slide pace lines sum to exactly 43:00. Elapsed times were checked cumulatively.

| Part | Slides | Time |
|---|---|---|
| Opening | 1–10 | 8:00 |
| 01 | 11–14 | 4:00 |
| 02 | 15–28 | 15:00 |
| 03 | 29–37 | 9:00 |
| 04 | 38–46 | 7:00 |
| Reserve | — | 2:00 |
| **Total** | | **45:00** |

## Assets and chart

- **`figs/p5-carlini-fig1.png`** (S22): Carlini et al., USENIX Security 2021, Fig. 1. Recaptured from PDF p. 2 at 200 dpi with `pdftoppm -x 925 -y 700 -W 595 -H 570`. The existing course PNG was clipped: it was missing the top edge and the "Fax" line.
- **`figs/p3-eykholt-fig1.png`** (S30): byte-identical to `courses/trustworthy-ai/figs/eykholt-fig1-stopsign.png`. P3 checked it against arXiv 1707.08945v5 p. 2.
- **S25 chart:** inline HTML bars redrawn from Buolamwini & Gebru, FAT* 2018, Table 4 (IBM error rates on the PPB benchmark).
  - Values: 34.7 / 12.0 / 7.1 / 0.3 %.
  - Scale: 15 px per point, axis 0–40 %.
  - The inputs are recorded in an HTML comment on the slide, and the cite line says "redrawn".
  - The 12.1 % overall figure appears only in the note, per E20.

## Deviations from the plan (my authority, DESIGN_SYSTEM)

- **S10 title.** The slide is titled "Contents", the deck convention, not "Four Questions for Today". The four numbered section names and their order match S11, S15, S29 and S38 exactly, which meets the acceptance criterion.
- **S01 has no talk-type `.pill`.** `job.md` says not to infer event branding, and it treats the date as inferred from the folder name only. Add one if Albert confirms the event name and date.
- No other layout or content deviations. No content was moved to the note beyond what the plan placed there.

## Plan issues / facts to confirm (slides-review decides)

1. **S17, "Airline's actual policy: No retroactive bereavement claims."** This wording is inferred from E08's account of the tribunal decision (paras 2–6, 27–31) rather than quoted. Please confirm it against the decision, or I will soften it to "The airline's policy said otherwise".
2. **S43, "A B.C. tribunal held Air Canada responsible for its chatbot's advice".** This line and the matching note line paraphrase E08. Please confirm the paraphrase is acceptable.
3. **S25.** The title, "Average Accuracy Hid Unequal Errors", refers to an average that the slide does not show; the 12.1 % overall figure is note-only per E20. Options: keep it as is (the note says the number aloud), or retitle to "One System, Very Unequal Errors". I need your decision.
4. **S19.** The date the "too agreeable" behaviour was first observed is not in evidence, so the timeline node is labelled "After release". The other dates (25 Apr, 28 Apr, 29 Apr / 2 May 2025) come from the cited OpenAI posts.
5. **S30.** Eykholt's target label ("Speed Limit 45") is not in `evidence.md`, so the slide and note omit it. Add it to evidence if you want it shown.
6. **S33.** The confirmation setting used in the 2025 research demonstration is not established in evidence. The slide and note say nothing about it.
7. **S24.** The worker deliberately avoids calling the algorithm "accurate"; the slide says only that it predicted cost, not need. No decision needed unless you want stronger wording.

## Unsourced facts

None known. Every case slide has a cite line, and every note has "Sources and limits". The items in Plan issues are paraphrases or omissions to confirm. They are not unsourced claims. The illustrations (S20 tickets, S27 flood post, S34 email, the opening workflow mockups) are tagged "Illustration" or "schematic" on the slide.

## Checks run

- `lint-deck.py`: `ok` for both the main deck and the note. `lint-deck.py --all` shows no new warnings; the remaining warnings are in `talks/seoul/application`, which is pre-existing and untouched.
- `find-wordy.py` and `find-dense.py`: no flags.
- `outline-lint.py`: 0 stale or missing pointers across 35 outlines.
- Counts:
  - 46 `data-slide-id` slides and 46 note articles, with the same IDs in the same order
  - `1 / 46`
  - no TODOs left
- **Render.** All 46 pages were rendered with headless Chromium print-to-PDF, then `pdftoppm -r 60`. Every page was read after integration; S34 and S44 were re-read after the reconcile commit. No overflow, overlap or clipped labels.
- **Note layout.** Probed in headless Chromium at desktop width (1265 px viewport) and at the narrowest width headless allows (485 px viewport; 430 px is below the headless minimum). Both show scrollWidth = viewport and 0 elements past the right edge.
