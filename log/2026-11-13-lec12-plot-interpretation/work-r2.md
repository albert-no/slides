# work-r2 — 2026-11-13-lec12-plot-interpretation

- Branch: `2026-11-13-lec12-plot-interpretation`. Round 1 head was `d9de699`; this round's head commit is named in the pointer message.
- Plan followed: plan-v3 together with review-r1 findings F01–F05. Everything was done inline, with no subagents.
- Result: the main deck goes from 79 to 80 slides (new S78), with `1 / 80` set. The note has 80 articles in the deck's ID order, renumbered. Tech is unchanged.

## Per finding

**F01: S78 added (blocking).**
- The slide "A CEO Prompt Leaves Appearance Unspecified" comes after S77 and before S74.
- It shows the actual published image at full height in the `.p1-case` layout. Beside the image:
  - "The prompt (CEO = chief executive officer):"
  - the exact prompt, “Generate a picture of one CEO.”
  - the highlight "The prompt specifies a role, **not appearance**."
  - the muted line "Published example, not a new run. One image shows no bias rate."
- The cite reads: "Image: Wan and Chang, ACL 2025, Figure 1, single-subject CEO example generated with DALL-E 3; other panels omitted."
- No race or gender is labelled or inferred, and the 74% paired-subject result is not used.
- Asset: `figs/lec12-plot-interpretation/s78-wan-chang-ceo.jpg`.
  - It is the native embedded JPEG stream, 1024×1024: page 1, first image, object 273, from `pdfimages -j -f 1 -l 1`. It is not re-encoded and not upscaled.
  - Source PDF: https://aclanthology.org/2025.acl-long.449.pdf, SHA-1 `c223bf76db061599c51dbe704857f57d137e0995`.
  - Image SHA-1: `48f276f9c86647a27cb5d580b49b7ed77be4d1ad`.
  - I visually matched it to the CEO panel, which is second in the top row (Manager, CEO, Secretary, Assistant).
  - I checked the authors' full names and the printed page 9174 against the PDF text.
- The S78 note gives:
  - the source URL and the full title;
  - Figure 1, top row, printed p. 9174 / PDF p. 1;
  - the exact prompt and the model (DALL-E 3);
  - the extraction command, object number, hashes and repo path;
  - the selection status: the authors' illustrative example, not a sampled audit;
  - a statement that 2025 is the publication year, not a generation date;
  - why many outputs plus a defined comparison are needed before making any distributional claim.
- Seams. All three now describe both opening examples:
  - S01 note: "the two opening images, a group photograph and a generated CEO picture…".
  - S03 note: "First, two images…".
  - S74 bridge: "The two images asked what a task assumes and what a system fills in when the task is silent."
  - The S77 note ends with "The next slide shows a system that did answer."
- Time: S06, S08 and S09 go from 1 to 0.75 min each, and S78 takes 0.75 min. Section 01 is still 10 min and the total is still 90.

**F02: S21b scope (blocking).**
- Slide:
  - The title is now "Here, the Profit-Optimal Equalized-Odds Rule Randomizes".
  - Highlight: "The profit-optimal equalized-odds rule randomizes here."
  - Muted line: "Not a confidence interval; acceptance probability fitted, not necessarily 50/50."
- Note:
  - The title and takeaway are aligned with the slide.
  - "approval odds … not a coin flip" becomes "acceptance probability … not necessarily 50/50", and the segment reading says "approve with some probability".
  - "need a randomized rule" is removed.
  - A new paragraph separates feasibility from optimality. Rejecting everyone gives TPR = FPR = 0 in every group, so it satisfies equalized odds but is generally not profit-optimal. Among the rules that satisfy equalized odds, the most profitable one here randomizes for three groups. That is a finding about this data and profit model, not a requirement of the criterion.

**F03: S25, S26a and S26b are figure-first (blocking).**
- Each slide now uses a plot-panel-only crop, 300 dpi, taken from the vector PDF of arXiv:1703.00056v1 (SHA-1 `effe2da67fc0307eed4824bb8853aa32a150897c`). The panel is otherwise unmodified.
- The panel sits in an SVG `<image>`. The tick labels and the axis title are set as slide text at 24 px, at the panel's own tick positions. I located those positions from the `pdftotext -bbox` coordinates of the source tick labels.
- The plot is 330–350 px tall, and the reading column sits beside it.
- Crops (`crops.sh`, commented lines):

| Panel | pdftoppm crop | File SHA-1 |
|---|---|---|
| Fig. 2(b) | `-f 10 -x 1408 -y 396 -W 823 -H 458` | `73275e33…` |
| Fig. 1(a) | `-f 6 -x 431 -y 617 -W 790 -H 679` | `652bba2e…` |
| Fig. 1(b) | `-f 6 -x 1444 -y 623 -W 788 -H 671` | `89b1f69e…` |

- S25 (Fig. 2(b)):
  - The y-definition line sits above the plot. The x title is "prior-record count".
  - The 0-prior pair is outlined, with the callout "≈0.21 vs ≈0.10".
  - The column has the key, "Whiskers: 95% intervals.", "**Black higher in every bin.**" and "Wide intervals at high counts; descriptive, not causal."
- S26a (Fig. 1(a)):
  - The x title is "COMPAS decile (a rank, 1–10)". Decile 6 is outlined, with the callout "≈0.56 vs ≈0.58".
  - The column has the y-definition, the key, "Close at most deciles, not identical." and the highlight "Decile 7 ≠ 70% risk: deciles are ranks."
- S26b (Fig. 1(b)):
  - The x title is "cutoff: flagged = score above it". Cutoff 4 is outlined, with the callout "≈0.63 vs ≈0.59".
  - The column has the PPV definition, the key, "Cutoff 4 pools scores 5–10. Roughly similar, not equal." and the highlight "Above a cutoff, not at one decile."
- Cites say the plot panel is unmodified, that the ticks and axis title are restated larger, that the legend is replaced by a key, that an outline was added, and that the values are approximate readings. S26b keeps the Dieterich et al. credit for the criterion.
- The notes' figure sections record the crops, the external labels and the files.
- The old crops `figs/chouldechova-fpr-priors-hi.png` and `figs/lec12-visual-motivation/p3-chouldechova-fig1-{left,right}.png` are no longer on slides. They stay in place, and nothing else references them.

**F04: S21a/S21b density (blocking).**
- `.p12i-ann p { margin:0; }` is removed.
- S21a annotations:
  - "Max profit: lender benchmark"
  - "**Shared threshold**: one cutoff for everyone"
  - "**Demographic parity**: same share approved"
  - the highlight in the annotation column
- S21b annotations:
  - "**Opportunity**: match TPR"
  - "**Equalized odds**: match TPR + FPR"
  - the muted segment line
  - the highlight
- Each annotation fits on one line. The S21a row-image heights went from 205 / 167 px to 188 / 153 px so that the cite stays clear (see Deviations).

**F05: S77 cite (optional, taken).**
- The slide cite now reads: "Photo: Wikimedia Commons, “CEE Youth Group Yerevan Meeting 2025, 2nd Day 42”, CC0 1.0; scaled, not cropped. Full credit in the notes."
- The S77 note keeps the full credit and says that the slide carries a shortened one.

## Slide mapping (round 1 → round 2)

| Slide ID | r1 page | r2 page | Change |
|---|---|---|---|
| S01–S77 (pp 1–4) | 1–4 | 1–4 | S77 cite (F05) |
| S78 | — | 5 | new (F01) |
| S74 … S56 | 5–79 | 6–80 | moved +1; S21a/b (30/31), S25 (36), S26a/b (37/38) edited |

Section ranges: 01 1–13 · 02 14–31 · 03 32–47 · 04 48–65 · 05 66–75 · 06 76–80. The note pacing table, `1 / 80`, the leaf OUTLINE and the note's main-deck cross-references are all shifted to match: slides 67, 15–29, 60–61, 29, 40 (×2), 44–46, 11 and 71. I checked each one against the target title. References into `lec12tech.html` are unchanged.

## Time map (90 min; every section budget unchanged)

| Slide | r1 min | r2 min | Elapsed after |
|---|---|---|---|
| S77 | 0.75 | 0.75 | 1.5 |
| S78 (new) | — | 0.75 | 2.25 |
| S74 | 0.75 | 0.75 | 3 |
| S04 | 2 | 2 | 5 |
| S05 | 0.75 | 0.75 | 5.75 |
| S06 | 1 | 0.75 | 6.5 |
| S07 | 1 | 1 | 7.5 |
| S08 | 1 | 0.75 | 8.25 |
| S09 | 1 | 0.75 | 9 |
| S10 | 1 | 1 | 10 (as before) |

## Deviations

- S21a: the row crops are about 8% shorter. This changes figure scale, not type size. It is what keeps the annotations on one line and the cite clear of the highlight. The markers and axis stay readable at `-r 60`.
- S26b: the slide drops the phrase "not a fairness verdict" to stay figure-first. The note keeps it: "Similar PPV is one criterion, not a fairness verdict."
- Correction to work-r1: its S77 remark "No public figures" was my observation, not a sourced fact. It is withdrawn. The S77 note makes no claim about the pictured people.

## Plan issues

None.

## Unsourced facts

- None added.
- The S78 provenance (title, authors, page, prompt, model, object, hashes) was checked against the downloaded PDF.
- The plot callouts are measured readings, labelled approximate.
- The feasibility example in the S21b note (reject everyone → TPR = FPR = 0) follows from the definitions.

## Checks run

- `lint-deck.py`:
  - Note: ok.
  - Deck: only the existing warning about 30 hard-coded inline colors, unchanged.
- `find-wordy.py`: three flags, all on slides unchanged this round (S24, S38, S50b); all three existed before this round.
- `outline-lint.py`: 0 stale pointers. A script also checked every `:N` in the lec12 section against the r1 file. Each one still names the same slide `<div>`, `<img>` or SVG `<image>` in the new file, and the S78 pointer is `:98`.
- The note's article ID order matches the deck's 80 IDs exactly.
- Render: headless Chromium, 80 pages, read at `-r 60`:
  - changed pages: 4 (S77), 5 (S78), 30–31 (S21a/b), 36–38 (S25, S26a, S26b);
  - neighbours: 3, 6, 35, 39.
- Fixes found by render:
  - S26a/b: at 380 px the x-axis title collided with the cite, so the plot is now 350 px.
  - Fig. 1(b): the crop top moved down to drop the descenders from the source title.
  - S21a: the highlight was moved back into the column (see Deviations).
