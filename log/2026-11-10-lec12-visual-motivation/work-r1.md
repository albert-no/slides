# work-r1 — 2026-11-10-lec12-visual-motivation

- Branch: `2026-11-10-lec12-visual-motivation` (from baseline `cd0da5c`)
- Head commit: named in the pointer message (the commit that adds this file)
- ID-only commit: `a6d894b`. It adds `data-slide-id` to main S01–S56, note S01–S56 and tech S57–S73, and changes nothing else.
- Result: main 56 → 74 slides, note 56 → 74 articles (same ID order as main), tech 17 → 23 slides. Planned 90 min, no activities.

## Per package

Six editors ran in separate worktrees with disjoint IDs and scoped CSS prefixes (`.p1-` … `.p56-`). I merged them and did the shared surfaces.

- **P1, S74 and S04–S10** (`2268959`)
  - New S74 opener: lending decision flow with the two errors.
  - S04 uses an Obermeyer Fig. 1A crop.
  - S05–S10 diagrams rebuilt: enlarged labels, arrows rebuilt as attached SVG connectors (S06 is C04's example).
  - S07 unsourced medical-data bullet removed.
  - S08 recorded label stated as "approved before".
- **P2, S12–S21** (`23d6303`)
  - Worked lending counts for every rate (E13): A = (3, 1, 3, 3), B = (1, 3, 1, 5).
  - S13 split into S13a–d, one count per slide.
  - S14–S16 show criteria on counts.
  - S17a/b use Hardt Fig. 1 (equalized odds / equal opportunity) as separate crops.
  - S19a/b and S20a/b present calibration buckets versus cutoff precision.
  - S21 uses a Hardt Fig. 9 crop.
  - Uses the paper's group labels A/B.
- **P3, S23–S34** (`a089e64`)
  - Audit flag diagram (S23).
  - FPR bars (S24).
  - Prior-count crop retained (S25).
  - Chouldechova Fig. 1 split into S26a/b.
  - Denominator matrix (S27).
  - E15 calibrated worked example (60 per group) for S29 and S32a, S32b, S33.
- **P4, S36–S45 and S75** (`eb4ade3`)
  - Reweighing toy example with exact weights (S37/S38).
  - Reductions loop split into S40a/S40b (C03's page-40 example).
  - New S75: random mixture of two classifiers.
  - Agarwal Fig. 1 split into Adult and COMPAS panels (S41a/b).
  - Hardt EO panel (S42).
  - FICO profit split into S43a/b.
  - AIF360 DI before/after (S44a/b) with external method keys.
  - Method summary (S45).
- **P5/P6, S47–S55** (`a6b10e8`)
  - Gender Shades Table 4 bars (S47).
  - Re-audit bars (S48).
  - BBQ examples split into S49a/b.
  - BBQ Fig. 3 split into S50a/b.
  - Bianchi Fig. 3 rows split into S51a/b.
  - S52 governance with the NYC rules' worked impact ratio.
  - Synthesis returns to the care case (S54a/b) and a closing map (S55).
- **P7, tech** (`fe30ea1`)
  - Presentation pass, splitting S61, S66, S67, S68, S70 and S71 into a/b.
  - Group index renamed t → g.
  - S67 retitled "Calibration Plus Balance Forces Exceptional Cases".
- **Integration** (`ed067ac` + the head commit)
  - S52 key now reads "(170/390) ÷ (412/797) ≈ 0.84", checked against the DCWP rules table. The P56 draft had "44% ÷ 52% ≈ 0.84", which is arithmetically wrong (0.846).
  - S03 note bridges to S74.
  - Note `<h2>` renumbered 1–74 and section names set on every pace line.
  - Per-slide minutes set to the plan (dividers .25, S56 .5). Elapsed times recomputed, pacing table rebuilt.
  - Slide-number totals set to 74 and 23.
  - All note cross-references to main or tech pages renumbered (old "slide 47/43/8", tech "slide 8/6–7/14/15/16", and the IDs workers left in the note).
  - Added an S23 note line that maps COMPAS "flagged" onto lending "selected" (terminology reconciliation).
  - Updated `OUTLINE.md`: index rows, leaf section table with line pointers, figures, note and tech.

## Time

| Section | Slides | Minutes |
|---|---|---|
| Where bias enters | 1–11 | 10 |
| Measuring fairness | 12–28 | 20 |
| COMPAS and impossibility | 29–43 | 15 |
| Mitigation | 44–59 | 20 |
| Beyond classifiers | 60–69 | 15 |
| Synthesis | 70–74 | 10 |
| Total | 1–74 | 90 |

The unplanned splits divide their row's plan minutes: S17a/b 1 + 1 (plan 2), S44a/b 1.25 + 1.25 (plan 2.5), S50a/b 1 + 1.5 (plan 2.5).

## Slide mapping

**Main** (`lec12-fairness.html`)

| slide ID | old page | new page | change |
|---|---|---|---|
| S01 | 1 | 1 |  |
| S02 | 2 | 2 |  |
| S03 | 3 | 3 |  |
| S74 | — | 4 | new |
| S04 | 4 | 5 | |
| S05 | 5 | 6 | |
| S06 | 6 | 7 | |
| S07 | 7 | 8 | |
| S08 | 8 | 9 | |
| S09 | 9 | 10 | |
| S10 | 10 | 11 | |
| S11 | 11 | 12 | |
| S12 | 12 | 13 | |
| S13a | 13 | 14 | split |
| S13b | 13 | 15 | split |
| S13c | 13 | 16 | split |
| S13d | 13 | 17 | split |
| S14 | 14 | 18 | |
| S15 | 15 | 19 | |
| S16 | 16 | 20 | |
| S17a | 17 | 21 | split |
| S17b | 17 | 22 | split |
| S18 | 18 | 23 | |
| S19a | 19 | 24 | split |
| S19b | 19 | 25 | split |
| S20a | 20 | 26 | split |
| S20b | 20 | 27 | split |
| S21 | 21 | 28 | |
| S22 | 22 | 29 | |
| S23 | 23 | 30 | |
| S24 | 24 | 31 | |
| S25 | 25 | 32 | |
| S26a | 26 | 33 | split |
| S26b | 26 | 34 | split |
| S27 | 27 | 35 | |
| S28 | 28 | 36 | |
| S29 | 29 | 37 | |
| S30 | 30 | 38 | |
| S31 | 31 | 39 | |
| S32a | 32 | 40 | split |
| S32b | 32 | 41 | split |
| S33 | 33 | 42 | |
| S34 | 34 | 43 | |
| S35 | 35 | 44 | |
| S36 | 36 | 45 | |
| S37 | 37 | 46 | |
| S38 | 38 | 47 | |
| S39 | 39 | 48 | |
| S40a | 40 | 49 | split |
| S40b | 40 | 50 | split |
| S75 | — | 51 | new |
| S41a | 41 | 52 | split |
| S41b | 41 | 53 | split |
| S42 | 42 | 54 | |
| S43a | 43 | 55 | split |
| S43b | 43 | 56 | split |
| S44a | 44 | 57 | split |
| S44b | 44 | 58 | split |
| S45 | 45 | 59 | |
| S46 | 46 | 60 | |
| S47 | 47 | 61 | |
| S48 | 48 | 62 | |
| S49a | 49 | 63 | split |
| S49b | 49 | 64 | split |
| S50a | 50 | 65 | split |
| S50b | 50 | 66 | split |
| S51a | 51 | 67 | split |
| S51b | 51 | 68 | split |
| S52 | 52 | 69 | |
| S53 | 53 | 70 | |
| S54a | 54 | 71 | split |
| S54b | 54 | 72 | split |
| S55 | 55 | 73 | |
| S56 | 56 | 74 | |

**Tech** (`lec12tech.html`)

| slide ID | old page | new page | change |
|---|---|---|---|
| S57 | 1 | 1 |  |
| S58 | 2 | 2 |  |
| S59 | 3 | 3 |  |
| S60 | 4 | 4 |  |
| S61a | 5 | 5 | split |
| S61b | 5 | 6 | split |
| S62 | 6 | 7 | |
| S63 | 7 | 8 | |
| S64 | 8 | 9 | |
| S65 | 9 | 10 | |
| S66a | 10 | 11 | split |
| S66b | 10 | 12 | split |
| S67a | 11 | 13 | split |
| S67b | 11 | 14 | split |
| S68a | 12 | 15 | split |
| S68b | 12 | 16 | split |
| S69 | 13 | 17 | |
| S70a | 14 | 18 | split |
| S70b | 14 | 19 | split |
| S71a | 15 | 20 | split |
| S71b | 15 | 21 | split |
| S72 | 16 | 22 | |
| S73 | 17 | 23 | |

## Deviations from the plan

- **Unplanned splits:**
  - S17 → S17a/b: two Hardt panels can't both be legible on one slide.
  - S44 → S44a/b: the before and after panels each need a readable external key.
  - S50 → S50a/b: the score definition and the Fig. 3 reading would not fit one slide at the floor sizes.
  - Main is 74 pages against the ~71 target.
- **S67 title:** the plan's "Score Balance Forces Exceptional Cases" became "Calibration Plus Balance Forces Exceptional Cases". The theorem needs calibration as well as balance, so the plan's title overclaimed.
- **S08 label:** the recorded label Y is "approved before" (a past decision), so the proxy example is internally consistent.
- **Generator name:** E23 names `plot_values.py`, but the generator is `figs/lec12-visual-motivation/p56_plot_values_audits.py`. The FICO values on S43a/b are inline in the slide, not in a generator.
- **Scoped CSS:** the package `<style>` blocks stay in the body just before each package's first slide. They are not hoisted into `<head>`.

## Plan issues (need slides-review)

1. **S61b positivity "for all s":** this condition is only well-defined for discrete or binned scores. For continuous scores it needs a density or bin qualifier. The tech slide states the discrete/binned case. Please confirm, or add the continuous-score wording to the plan or evidence.
2. **Time:** the total is held at 90 only by trimming divider and closer minutes to the plan values. The new S40a/S40b/S75 sequence adds about 1.5 min of content to Mitigation, absorbed within its 20 min. Please confirm the budget is realistic, or move S75 to the note.
3. **Unplanned splits** S17a/b, S44a/b, S50a/b: please accept them or name a cut.

## Unsourced facts found (flagged, not corrected)

- **Obermeyer Fig. 1A caption details** used in the S04 note are not in E01. The crop itself is cited.
- **Balanced-accuracy definition and AIF360 read-off values** (S44a/b note) are carried over from the baseline note and are not in E09.
- **Bianchi citation mismatch:**
  - The existing `figs/bianchi-occupations.png` citation says Fig. 3, but the image is Fig. 1. The section reference "§3" should be §2.2 in arXiv v2.
  - The new S51a/b crops are cited as Fig. 3, rows 1–2 and row 6.
  - Please verify the Fig. 3 citation for the new crops. The old image is no longer on lec12; only the backup decks use it.
- **Korean AI Basic Act row** (S52 note) is labelled historical and unverified.
- **S21 note** "max-profit and single-threshold points sit close" is read off Hardt Fig. 9, not stated in E03.

## Checks run

- **`scripts/lint-deck.py`:**
  - The note and tech files are clean.
  - Main has one warning: 32 hardcoded inline colours. These are the key swatches on S43–S44, which must match the colours in the paper crops. No font-size or math errors.
- **`scripts/find-wordy.py`:** four flags, all plot keys or legends (S24, S38, S39, S50b); bounded exceptions that render cleanly.
- **`scripts/outline-lint.py`:** 0 stale pointers. The 5 warnings are in other courses.
- **Generators re-run:**
  - `criteria_examples.py` output is byte-identical to the deck.
  - `calibrated_errors.py` (s29, s32a, s32b, s33), `reweighing.py`, `reductions_mix.py` and `p56_plot_values_audits.py` output matches the inline SVG up to whitespace.
- **Full render** (headless Chromium → PDF → `pdftoppm -r 60`): main 74 pages, tech 23 pages. Page counts match the slide divs.
- **Render read:**
  - All 97 pages were read once at -r 60. No overflow, footer collisions, missing images, raw TeX, or detached or reversed arrows.
  - I re-checked C04's page-6 example (now page 7, S06), the page-40 family (S40a, S40b, S75 at pages 49–51) and S74 myself.
  - I checked main pages 21, 48 and 64 at -r 110.
- **Known minor residuals** (left as they are; say if any should block):
  - **Pages 21–22 (S17a/b):** the Hardt Fig. 1 top tick "1.0" is half-cut. In the paper the panel title touches that tick, so showing it in full would mean painting out the title.
  - **Pages 48, 54, 55 and 57–58 (S39, S43a/b, S44a/b):** some tick and in-bar labels inside the paper crops are small. On S39 the AIF360 right panel's rotated row labels are cut at the crop edge; the left panel carries the same labels.
  - **Page 64 (S49b):** the light-blue sides of BBQ's "Ambiguous context" box run down to the outer box. This is the paper's own nesting, not a crop artefact.
  - **Page 23 (S17b):** about 45% of the content area is empty below the figure.
  - **Tech pages 15, 19 and 21:** the grey caption line sits tight against the table rule or box above it.
  - **Tech page 4:** the underbrace annotations are small, about 13 px.
