# Plan v2 — add photo-led opening motivation

## What changed since v1

Albert added C05 at 22:50 KST: visual motivational examples at the beginning, suggesting “find the most important person” and “generate the photo of CEO”. This is an additive, localized opening package, **not a new deck or restructure**. Size stays medium; two review rounds; same baseline and branch. No new literature survey. P1–P3 are already under implementation and remain valid: do not discard their completed work.

**Current complete order:** this change section and P0 below amend the full v1 work order reproduced after them. Where the reproduced text says only the five target pages may change, P0 is the explicit exception. Targets become about 80 slides (v1's 78 plus two opening examples); readability may require more. Complete the expanded scope before the combined work-r1 pointer; if the original package is already committed, retain it and add P0 on the same branch.

## Added coverage

| Comment | Baseline position | IDs | Package |
|---|---|---|---|
| C05 | after section-01 divider S03 (baseline p3), before S74 (p4) | new S77, S78 | P0 |

These are the next unused IDs at baseline; P1–P3 only split existing IDs. If another new ID has been allocated in this work, use the next free IDs and report the mapping. Do not renumber S74–S76.

## P0 — photo-led opening examples [judgment]

### 8. S77 — new opening photo, after S03, before S78
- **Point / proposed title:** “Who Is Most Important Here?” Point: a picture does not define importance.
- **Must:** one large group photograph, paired with the visible prompt “Find the most important person in this picture.” Supply a short explicit answer on the same slide: “Not enough information: important for what?” or equivalent. This is a demonstration of an underspecified judgment, not a challenge requiring the class to nominate a person.
- **Exhibit:** an ordinary team meeting or group-work photograph, with several people visible and no supplied hierarchy or named roles. Use a generated fictional scene or an appropriately licensed/attributed photograph. Make the scene genuinely photographic, not stick figures, silhouettes or a substitute process diagram. Slides owns image production/sourcing. No recognizable real CEO or celebrity is needed.
- **Prefer:** a naturally varied group rather than a deliberately caricatured “boss versus subordinates” setup. Do not label a person as more important, competent, trustworthy or wealthy from appearance. Do not add a fake chatbot answer or imply a model was tested when none was.
- **Main:** the photo, prompt and explicit answer; labels identify synthetic or illustrative status where applicable. The prompt's ambiguity is the point, not an unsupported empirical claim about bias.
- **Note:** explain that clothing, seating position or presentation role does not settle the task's missing criterion; an external role description or defined decision objective would be needed. Explain the difference between a classroom thought experiment and an observed model failure. Record photo license/source, or generation prompt/tool/model/date/output provenance.
- **Tech:** unchanged.
- **Evidence:** E09; C05.
- **Prefer layout/time:** figure-first, about 0.75 min; lecturer-led, no activity block or live-model dependency.
- **Acceptance:** photo is the visual focus; the literal request and short answer are both on-slide. The slide motivates questioning the target without making unsupported claims about the people or an untested model.

### 9. S78 — new CEO image, after S77 and before S74
- **Point / proposed title:** “Generate a Photo of a CEO.” Point: the prompt names a role, but leaves appearance unspecified.
- **Must:** show an actual photo-style generated output with the exact visible prompt “Generate a photo of a CEO.” Define CEO as chief executive officer. Add the brief interpretation: “The model fills in unspecified appearance.” Keep the output's illustrative status explicit: “One output, not a bias audit.” Do not predetermine what the output must look like.
- **Exhibit:** one genuine output produced for this demonstration. Use the available image-generation capability and retain the first technically usable result; do not steer demographic attributes, manufacture a stereotyped portrait and call it neutral-prompt evidence, or regenerate until a preferred social conclusion appears. If the tool adds or rewrites the prompt, record that and distinguish the displayed user prompt from the effective generation instructions.
- **Main:** prompt, generated portrait, concise interpretation and the one-output limitation. Actual tool/model and generation date belong in attribution; unknown details remain honestly unspecified rather than guessed.
- **Note:** record exact prompt, any visible augmentation, tool/model/version, date, generation count, technical retries, final asset path and crop/edit history. Explain that a distributional claim would require repeated generations, defined categories and a benchmark/criterion. A varied or non-stereotypical result is still usable: this slide teaches underspecification, not a rigged conclusion. The later Bianchi audit is separate historical evidence (E11).
- **Capability contingency:** if image generation is unavailable to slides, report that plan issue promptly; do not silently substitute a fake output or make unapproved API/model changes. A genuinely sourced historical occupation example can be proposed as an alternative, clearly labelled with its real prompt and model; do not relabel another occupation as CEO.
- **Tech:** unchanged.
- **Evidence:** E10–E11; C05. Before approval, the owner appends execution provenance to evidence.md from the work report.
- **Prefer layout/time:** figure-first, about 0.75 min; no audience activity required.
- **Acceptance:** real saved bitmap, legible portrait and actual prompt, honest generation provenance, and no unsupported claim about model-wide bias or real CEOs. No screenshot fabricated to look like a measured test.

## P0 surfaces and transitions

- **May touch:** new S77/S78 and matching note articles in `courses/trustworthy-ai/lec12-fairness.html` / `lec12-fairness-note.html`; new assets under `courses/trustworthy-ai/figs/lec12-plot-interpretation/`; lec12 entries in the leaf `OUTLINE.md`.
- **Small narrative seam:** update S03's note to introduce the two photographs before lending. In S74's note, bridge from “who is represented / what is assumed” to “who receives an opportunity”; main S74 diagram can remain unchanged.
- **S01 note correction required by the broader hook:** current blanket claim “Every fairness claim is a rate with a denominator” → “For the quantitative fairness comparisons that follow, name the rate and its denominator.” Preserve the usefulness of that recurring device without reducing every representational or normative concern to a rate. This is an explanatory scope correction, not a new theorem. No need to change the title slide.
- **Time:** preserve 90 minutes and section 01's 10 minutes. A workable target: new slides 0.75 + 0.75; S04's script 2.5 → 2 min; S05, S06, S08, S09 each 1 → 0.75 min; other opening times unchanged. These are pacing changes only, not authority to cut source qualifiers or repaint existing plots. Slides may choose another explicit within-section allocation. If comfortable teaching requires more time, report the tradeoff rather than silently extending the lecture.
- **Rest unchanged:** Contents and dividers retain the same six labels and order. Keep the later occupation-study slides S51a/b and their citations; they supply measured evidence, whereas this opening motivates the questions. No new statistics in the opening.
- **Integration:** update all downstream page numbers, note references, elapsed times, totals and OUTLINE pointers; record baseline → new page mapping. Render new slides plus S03/S74 and the original target pages/neighbours. This is part of the same review round, not a separate PR.
- **Provenance:** slides supplies exact asset production/sourcing details in work-r1; owner appends the evidence entries. Never claim a generated image is empirical evidence of a distribution without an actual sampling protocol.

---

## Retained work order from v1 (P1–P3)

# Plan v1 — clearer reading of the fairness plots

## 1. Summary and work order

**[judgment]** Keep the argument; replace generic legend-heavy descriptions with guided comparisons. Each plot must answer a different, visible question: **which cutoff changes? which non-rearrested people are flagged? what happens at one score? what happens above a cutoff?** Make the important comparison conspicuous without turning the slide into a paragraph or shrinking the plot.

- Baseline: `0d2c05c9ad02635c0407010f15bcca5428bac949`.
- Main: `courses/trustworthy-ai/lec12-fairness.html`.
- Notes: `courses/trustworthy-ai/lec12-fairness-note.html`.
- Audience: mixed-major sophomores/juniors; concept-first. No new proofs or activities.
- Preserve the six-section argument and 90-minute total. Proposed splits are teaching steps, not half-filled continuations.
- Target: split S21 and S23 into two steps each; keep S25, S26a and S26b as one step each, about 78 main slides total. **Slides decides** final split/layout choices under DESIGN_SYSTEM.md; report every mapping. Counts are not a ceiling.
- Baseline prerequisites: reuse the FPR/PPV populations already taught in S13b/S13c and S20b, and the calibration distinction in S19a/b. Adapt those ideas into the plot keys; do not introduce a new formula system. Later S27's denominator comparison and the impossibility sequence stay intact.

The current pages primarily name axes/encodings; the revision must add a visible interpretation and reading example. More detail in notes alone does not satisfy C02–C04.

## 2. Coverage and baseline map

All locations below are in the main file unless labeled otherwise; line numbers are baseline navigation aids, not editing instructions.

| Comment | Baseline page / title | Baseline ID / line | Planned ID(s) | Package |
|---|---|---|---|---|
| C01 | Whole requested revision and PR after approval | five pages below | all below | P1–P3 + integration |
| C02 | 28 — The Same Scores Yield Different Decisions | S21 / 560 | S21a, S21b | P1 |
| C03 | 30 — What the COMPAS Audit Measured | S23 / 599 | S23a, S23b | P2 |
| C04 | 32 — The Gap Appeared Across Prior-Count Bins | S25 / 667 | S25 | P3 |
| C04 | 33 — Similar Decile Outcomes Are Not Probability Calibration | S26a / 687 | S26a | P3 |
| C04 | 34 — Cutoff Precision Was Approximately Similar | S26b / 707 | S26b | P3 |

No contradictions to resolve. “Distinctive” means the reader can identify each plot's specific comparison and result, not just notice new styling. Split IDs and matching note IDs follow PIPELINE.md; never renumber existing IDs. If a further split is needed, report its suffix mapping.

## 3. Numbered, self-contained slide specifications

### 1. S21a — baseline p28, main S21 and matching note [judgment]
- **Point / proposed title:** “Equal Selection Can Require Different Score Cutoffs.” One shared cutoff and equal selection rates are different constraints.
- **Must communicate:** credit score is the horizontal coordinate; moving a cutoff right makes qualification stricter within that group. Compare the shared-threshold row (same raw cutoff) with demographic parity (different raw cutoffs to equalize the fraction qualifying). Name all four group encodings. Briefly identify max profit as the unconstrained lender benchmark, not a definition of fairness.
- **Exhibit / reading:** real Hardt Figure 9 left panel, with the shared-threshold-versus-demography comparison made unmistakable. **Slides decides** whether a full panel remains readable or tightly selected original rows make the comparison clearer; preserve true data positions, row identities, axis scale and legend meaning. Do not replot from eyeballed coordinates.
- **Main:** plot key plus a concrete comparison, e.g. “Same raw cutoff ≠ same selection rate.” The key is not the takeaway. Credit-score direction and no universal “best” fairness direction must be clear.
- **Note:** explain why group score distributions make equal qualification fractions require different cutoffs; record study population, modeled utility, historical setting and outcome proxy. Keep more detailed explanations of all five criteria here.
- **Tech:** unchanged; no new derivation.
- **Evidence:** E01–E02.
- **Prefer layout/time:** figure-first with one highlight; about 1.25 min of S21's existing 2.5 min.
- **Acceptance:** a reader can point to the shared cutoff, explain what a horizontal shift does, and say what demographic parity equalizes. Merely spelling out the five row names is insufficient.

### 2. S21b — second step replacing baseline p28 [judgment]
- **Point / proposed title:** “Equalized Odds Randomizes Between Two Cutoffs.” In this example, equalizing two error-related rates changes the decision rule itself.
- **Must communicate:** equal opportunity matches qualification among non-defaulters; equalized odds also matches it among defaulters. The plotted segment spans two thresholds: below the lower endpoint, reject; above the upper endpoint, accept; between them, approve with a chosen probability. It is neither a confidence interval nor necessarily a 50/50 lottery.
- **Exhibit / reading:** real Figure 9 raw-score opportunity/equal-odds rows, preferably enlarged and compared on the same scale. Highlight one non-degenerate group segment and explicitly interpret its two endpoints. Keep group identity available; avoid a second competing schematic if it crowds the source figure.
- **Main:** the key difference between a single cutoff and a randomized interval, with “in this example” scope. **Must not** imply every equalized-odds problem needs randomization.
- **Note:** probability is fitted to the criterion; no probability can be read from segment length alone. A lone point may represent no randomization. Keep the full five-rule narrative so the split loses no prior content.
- **Tech:** unchanged.
- **Evidence:** E01–E02.
- **Prefer layout/time:** figure-first + highlight; about 1.25 min, total S21a/b target 2.5 min.
- **Acceptance:** students can distinguish the interval from an uncertainty whisker and describe the accept/reject/randomize regions without claiming a universal fairness ranking.

### 3. S23a — baseline p30, main S23 and matching note [judgment]
- **Point / proposed title:** “What COMPAS Scores Do.” Point: a risk score informs a consequential decision; it is not the decision or the observed outcome.
- **Must communicate:** define COMPAS as a commercial recidivism-risk assessment, developed by Northpointe. Explain what the score is used for, grounding the example in Broward County pretrial decision support. Separate score, human/institutional decision, and later observed outcome. State this is the 2016 audit of 2013–14 scores, not current deployment guidance.
- **Exhibit:** one clear conceptual workflow separating those roles. Do not make an arrow from “flagged” to automatic detention. No source plot exists for this explanatory role distinction; an original schematic is appropriate, explicitly illustrative.
- **Main:** short “what it is / why it matters” definition and the score's role. Expand the acronym once if not already defined; do not make the long expansion compete with the mechanism.
- **Note:** full expansion, vendor, historical setting, distinction from violent-recidivism and failure-to-appear scales. Explain the possible consequences without claiming that the audit flag determined each defendant's treatment.
- **Tech:** unchanged.
- **Evidence:** E03–E04.
- **Prefer layout/time:** diagram-flow, about 0.5 min.
- **Acceptance:** a newcomer can distinguish the prediction from the court's decision and from the audit outcome, and knows why a mistaken risk flag matters.

### 4. S23b — second step replacing baseline p30 [judgment]
- **Point / proposed title:** “The Audit Flags Scores 5–10.” The binary audit label is broader than the vendor's “High” category.
- **Must communicate:** existing deciles 1–10, vendor categories Low 1–4 / Medium 5–7 / High 8–10, audit flagged group 5–10. Compare that flag with recorded rearrest within two years. Use “higher risk” for the audit flag where ambiguity with vendor “High” would arise.
- **Exhibit:** adapt the existing decile strip, making the two category systems distinct and legible. Include one concrete reading: score 6 is vendor Medium but audit-flagged. Identify the false-positive situation in plain language: flagged, then no recorded rearrest within two years. This anticipates S24 without repeating its measured rates.
- **Main:** score-6 reading, recorded-outcome definition and the distinction between categories. Preserve “recorded”: no rearrest is not proof of no offending. No extra general sample-size headline.
- **Note:** the binary rule, outcome construction and proxy limitation; cohorts differ across analyses (E04). Preserve useful details moved from the current S23 note.
- **Tech:** unchanged.
- **Evidence:** E03–E04, E08. Score 6 is an illustrative application of the published category definitions, not a real individual's case.
- **Prefer layout/time:** full-width diagram + highlight; about 0.75 min. Combined S23a/b target remains 1.25 min; modest redistribution within the section is allowed, with a reported time map.
- **Acceptance:** a reader correctly labels score 6, states what outcome was measured and recognizes a false positive. No confusion with automatic detention or the vendor's 8–10 label.

### 5. S25 — baseline p32, main S25 and matching note [judgment]
- **Current title → proposed title:** “The Gap Appeared Across Prior-Count Bins” → “The FPR Gap Remains Even Without Priors.”
- **Point:** the difference is visible even in the zero-prior subgroup, not only because the groups occupy different prior-count bins.
- **Must communicate:** x = prior-record-count bin; y = share flagged among the **non-rearrested** of that race/bin; population = misdemeanor defendants; threshold >4. Gray Black, orange White; whiskers 95% confidence intervals. Lower FPR means fewer false flags within the defined population, not overall fairness.
- **Exhibit / reading:** original Figure 2(b) enlarged. Make the zero-prior pair the first explicit comparison, then show that Black point estimates remain higher across the displayed bins. Prefer “roughly one in five vs one in ten” only if clearly labeled as an approximate chart reading; exact numbers are not required.
- **Main:** retain a plainly visible limit: descriptive comparison, not a causal adjustment. High-prior uncertainty must not disappear in pursuit of a stronger headline. The explicit denominator is essential; “y: FPR” alone is not enough.
- **Note:** explain one bar from numerator and denominator, wide high-prior intervals, and why stratification is not causal identification. Do not claim statistical significance in every bin or “all else equal”.
- **Tech:** unchanged.
- **Evidence:** E04–E05, E08.
- **Prefer layout/time:** figure-first + highlight, about 1 min. **Slides decides** an additional reading step if the plot, denominator and necessary limits cannot remain readable together.
- **Acceptance:** reader identifies who is included in a bar, points to the zero-prior contrast and can state what the comparison does not prove. No tiny plot beside an expanded bullet column.

### 6. S26a — baseline p33, main S26a and matching note [judgment]
- **Current title → proposed title:** “Similar Decile Outcomes Are Not Probability Calibration” → “At the Same Decile, Outcomes Are Broadly Similar.”
- **Point:** compare races within one exact score, not everyone above a threshold.
- **Must communicate:** x = exact COMPAS decile 1–10; y = observed two-year rearrest share among people at that score. Gray Black / orange White; whiskers 95% confidence intervals. Walk through one pair, preferably decile 6: both shares near 60% as an explicitly approximate reading. Explain the generally increasing outcome trend without claiming strict monotonicity.
- **Exhibit / reading:** Figure 1(a), upper-left panel of a four-panel original, with the chosen score pair visibly identifiable. Source crop remains faithful. Distinctive emphasis is **same score**; do not reproduce the PPV framing.
- **Main:** necessary qualifier “Deciles are ranks, not probabilities” (or “Decile 7 ≠ 70% risk”) plus approximate, not exact across-group agreement. Higher y means more recorded rearrest, not a morally “better” model.
- **Note:** Chouldechova's across-group calibration definition differs from numeric probability calibration. Empirical differences remain; interval overlap proves neither equality nor equivalence. Correct the existing note's assertion that Figure 1 has only two panels.
- **Tech:** unchanged; retain the deck's established definitions.
- **Evidence:** E04, E06, E08.
- **Prefer layout/time:** figure-first + highlight, about 0.75 min.
- **Acceptance:** reader can say who enters x=6 and why x=7 is not a 70% forecast, and does not infer equal error rates or exact equality.

### 7. S26b — baseline p34, main S26b and matching note [judgment]
- **Current title → proposed title:** “Cutoff Precision Was Approximately Similar” → “At Cutoff 4, Precision Is Roughly Similar.”
- **Point:** PPV pools all flagged deciles, unlike the preceding exact-score comparison.
- **Must communicate:** x = high-risk cutoff; flagged means score **above** x; y = rearrest share **among the flagged** (PPV, positive predictive value). At cutoff 4 the population is scores 5–10. Use that pair as the concrete reading; the bars are approximately similar, not equal. Identify gray/Black, orange/White and 95% intervals.
- **Exhibit / reading:** Figure 1(b), upper-right panel, with cutoff 4 conspicuous and an explicit “scores 5–10” reading. Keep the original surrounding cutoffs so students can see the population changes as the cutoff rises. Optional readings about 63% versus 59% must be marked approximate, not imported from ProPublica's different cohort.
- **Main:** distinguish **above cutoff** from **at decile**, and interpret the empirical pattern without declaring fairness. Higher PPV means more rearrests among the flagged, not automatically a better or fairer policy.
- **Note:** higher cutoffs select nested, changing subsets; x=9 includes score 10 only. Paper reports predictive parity for cutoffs 4+, taught as approximate here. Do not use CI overlap as proof of equality or imply calibration guarantees PPV parity. Attribute plot to Chouldechova, criterion in the dispute to the vendor.
- **Tech:** unchanged.
- **Evidence:** E04, E07–E08.
- **Prefer layout/time:** figure-first + highlight, about 0.75 min.
- **Acceptance:** reader correctly identifies the cutoff-4 denominator and explains how this plot can coexist with the FPR gap. It must not look like a second copy of a decile-calibration slide with only its axis title changed.

## 4. Packages and allowed surfaces

| Package | IDs | Files / note sections it may touch | Dependencies |
|---|---|---|---|
| P1 | S21 → S21a/b | main + matching S21 note(s); source crops under `courses/trustworthy-ai/figs/lec12-plot-interpretation/` if needed | E01–E02; unchanged preceding criteria |
| P2 | S23 → S23a/b | main + matching S23 note(s); original explanatory diagram in that range | E03–E04; leads into unchanged S24 |
| P3 | S25, S26a, S26b | main + those note articles; new crops in the same job-specific figure folder if needed | P2 terminology and cutoff; E04–E08 |

**Must:** preserve all unrelated slide content. Shared per-deck styles may be adjusted only if necessary for these pages and without changing untouched pages; prefer reuse. No edits to `reference/`, global styles or scripts. Existing vetted figure assets remain available to older decks. New cropping metadata and any generator code are executor-owned; record source/version/panel and transformations. No repainting source data.

**Slides decides:** packages may be implemented serially; no parallel-agent requirement. All content/design/wording judgments above are for slides to resolve with full context, not to pass blindly to a context-free implementer. Bring any changed fact, argument, required content or teaching-time proposal back through the work report; do not quietly substitute a new explanation with a different claim.

## 5. Shared surfaces and integration

- Contents/divider names, order and six section budgets remain 10 / 20 / 15 / 20 / 15 / 10 minutes. Individual pacing may be redistributed within the affected section; report the new map and preserve a 90-minute sum.
- Update every affected note number/title/ID, elapsed time, local cross-reference and note navigation. In unaffected notes only numbering/reference maintenance is permitted.
- Update only the lec12-related entries in `courses/trustworthy-ai/OUTLINE.md`: total, section ranges, source-line pointers, changed descriptions, figure inventory. Do not duplicate or rewrite neighbouring lectures' entries.
- Main slide count and note count must match. Tech remains 23 slides; touch tech only if a main-page reference actually becomes stale, with the exact reason reported. No new technical content.
- Keep S24 (baseline p31), S27 (p35) and the later argument semantically unchanged; render them as neighbours to verify transitions after insertion.

## 6. Delivery and acceptance gates

1. **Must:** all C01–C04 coverage recorded in `work-r1.md`, with baseline page → stable ID → revised page mapping, split decisions, exact commit and branch, source/plan deviations and tests. No ID-only commit is needed unless an unexpected missing ID is discovered.
2. **Must:** read the canonical design sections linked by PLANNER_BRIEF.md. Render every revised page and its immediate neighbours at final slide size. Check chart and diagram labels, point/axis/denominator separation, uncertainty, wraps, aspect ratio, overflow and footer/citation collisions. Do not treat lint alone as visual approval.
3. **Must:** added explanation is visible on main slides; no shrinking type or packing paragraphs beside the same undersized crops. Split again rather than erasing necessary qualifiers.
4. **Must:** trace each factual addition to evidence.md or report a new source-backed claim for the owner to register. Do not invent exact chart numbers or probabilities.
5. **Must:** copy completed owner files unchanged into `log/2026-11-13-lec12-plot-interpretation/` and refresh living files on each push. Announce the work report with the exact review commit via the one-line contract pointer.
6. Owner reviews the named commit, up to two rounds, then opens the PR only after approval and a log-only post-review verification. No merge is authorized.
