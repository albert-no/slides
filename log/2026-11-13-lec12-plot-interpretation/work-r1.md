# work-r1 — 2026-11-13-lec12-plot-interpretation

- Branch: `2026-11-13-lec12-plot-interpretation` (from baseline `0d2c05c`)
- ID-only commit: none. The baseline already carries stable IDs in the main deck and the note.
- Content commit: `5a123a6`. Head commit: named in the pointer message (the commit that adds this file).
- Result: main deck 76 → 79 slides (two splits plus new S77). `1 / 79` set. Note has 79 articles, renumbered. Tech unchanged.
- Plan followed: plan-v2 (P0 plus the retained P1–P3). P1–P3 and the integration were done inline, with no subagents.
- **S78 (CEO image) is not built.** See Plan issues.

## Per package

**P1: S21 → S21a, S21b (C02, baseline p28).**
- New row crops of Hardt Fig. 9 left panel. They are taken from the vector PDF at 300 dpi. They are unmodified and keep the same x-scale. The script is in `courses/trustworthy-ai/figs/lec12-plot-interpretation/crops.sh` (source arXiv:1610.02413v1, PDF p19).
- S21a, "Equal Selection Can Require Different Score Cutoffs":
  - Image rows: legend with Max profit and Single threshold, then Demography with the axis.
  - Key: "x = credit score: a group's cutoff further right = stricter."
  - Each row gets an annotation. Max profit is marked as the lender's benchmark, not a fairness rule.
  - Highlight: "Same raw cutoff ≠ same share approved."
- S21b, "Equalized Odds Randomizes Between Two Cutoffs":
  - Image rows: Opportunity and Equal odds, plus the axis.
  - The group key sits outside the image (the legend is in S21a's strip).
  - Segment rule: reject below the left end, accept above the right end, random between. It is not a confidence interval, and the odds between are fitted, not 50/50.
  - Highlight: "In this example, equal error rates need a randomized rule."
- The old full-panel crop `figs/lec12-visual-motivation/p2-hardt-fig9-raw.png` is no longer used on slides. The file stays in place.
- Note: S21 split into two articles. The five-rule narrative, setup (301,536 TransRisk scores, four groups, modeled lender profit) and source list are kept. The figure section records the crops.

**P2: S23 → S23a, S23b (C03, baseline p30).**
- S23a, "What COMPAS Scores Do":
  - One-line definition of COMPAS.
  - Illustrative flow: score (tool's prediction, decile 1–10) → informs → decision (court, pretrial; people decide) → later → outcome (rearrest recorded, within two years). A bracket shows that the audit compares score with outcome.
  - Case line: ProPublica 2016, Broward County, scores from 2013–14.
  - Highlight: "The score informs a decision: it is not the decision, nor the outcome."
  - The full COMPAS expansion is in the cite.
- S23b, "The Audit Flags Scores 5–10":
  - The existing decile strip is adapted. The audit bracket reads "higher risk" 5–10, and the vendor labels Low 1–4 / Medium 5–7 / High 8–10.
  - Score 6 is outlined, with the line "Score 6: vendor Medium, yet flagged by the audit."
  - It defines a false positive in plain language, and says that no recorded rearrest does not mean no offending.
  - The cite says score 6 is an example, not a real defendant.
- Note: two articles. The S23 "Moved from the slide" block (Fig. 3, Cohen's d) is kept in S23b. The lending-count mapping paragraph is kept.

**P3: S25, S26a, S26b (C04, baseline p32–34).** Each gets a full y-definition line, an x line, a swatch key, one outlined reading in bold and one muted limit.
- S25, "The FPR Gap Remains Even Without Priors":
  - y = share flagged (score > 4) among misdemeanor defendants **not** rearrested.
  - The zero-prior pair is outlined: "0 priors: roughly 1 in 5 vs 1 in 10".
  - "Black higher in every bin; wide intervals at high counts."
  - Limit: "Descriptive split, not a causal adjustment."
- S26a, "At the Same Decile, Outcomes Are Broadly Similar":
  - y = share rearrested among people **at** that decile.
  - Decile 6 is outlined: "both near 60%".
  - "Close at most deciles, not identical."
  - Highlight: "Decile 7 ≠ 70% risk: deciles are ranks."
- S26b, "At Cutoff 4, Precision Is Roughly Similar":
  - y = PPV among everyone scored **above** the cutoff.
  - Cutoff 4 is outlined: "pools scores 5–10: about 0.63 vs 0.59".
  - "Roughly similar, not equal; not a fairness verdict."
  - Highlight: "Above a cutoff, not at one decile."
  - Attribution: the plot is Chouldechova's; the criterion is the vendor's (Dieterich et al. 2016).
- Readings were checked against pixel measurements of the source figures:
  - Fig. 2(b), zero priors: ≈0.215 / ≈0.104.
  - Fig. 1(a), decile 6: ≈0.56 / ≈0.58.
  - Fig. 1(b), cutoff 4: ≈0.628 / ≈0.588.
  - They agree with E05–E07, and every cite labels them as approximate readings.
- Note: the three articles are rewritten as axis-first walkthroughs of the outlined pair. They fix the baseline error "Figure 1 has two panels" (it has four; the crops are the upper-left and upper-right panels).

**P0: S77 (C05).**
- S77, "Who Is Most Important Here?", sits after S03 and before S74.
- The photo is large, next to the literal task "Find the most important person in this picture." and the answer "Not enough information: important for what?"
- Muted line: "No roles given. A thought experiment, not a model test."
- Photo provenance:
  - Source: Wikimedia Commons, "CEE Youth Group Yerevan Meeting 2025, 2nd Day 42", by user Հակուլիկ (own work), dated 2025-11-22.
  - License: **CC0 1.0** public-domain dedication.
  - Page: https://commons.wikimedia.org/wiki/File:CEE_Youth_Group_Yerevan_Meeting_2025,_2nd_Day_42.jpg
  - Original: 6000×4000, SHA-1 `3dc3dca2376e489522f1793fed28c0f333703173`.
  - The slide uses the Commons 1920-px rendition, saved as `figs/lec12-plot-interpretation/s77-group-photo.jpg`. It is scaled, not cropped or edited.
- Why this photo: an ordinary group photo with about twenty people, no names or roles, and everyone in the same sweatshirt, so clothing gives no hierarchy cue. No public figures. CC0, so there are no attribution or share-alike obligations; I attribute it anyway.
- S77 note:
  - It explains that the missing criterion cannot be supplied by appearance, position or clothing, and that a role description or a defined decision would be needed.
  - It separates a thought experiment from an observed model failure: no model was asked.
  - It records the provenance.
- Seams:
  - S03 note introduces the photograph.
  - S74 note opens with the bridge from "who is represented / what a task assumes" to "who receives an opportunity".
  - S01 note is scoped as plan-v2 asks: "For the quantitative fairness comparisons that follow, name the rate and its denominator." It adds a sentence that not every fairness concern is a rate.

## Slide mapping

| slide ID | old page | new page | split or moved |
|---|---|---|---|
| S01–S03 | 1–3 | 1–3 | — |
| S77 | — | 4 | new (P0) |
| S74, S04 … S20b | 4–27 | 5–28 | moved +1 |
| S21 | 28 | S21a 29, S21b 30 | split |
| S22 | 29 | 31 | moved |
| S23 | 30 | S23a 32, S23b 33 | split |
| S24 | 31 | 34 | moved |
| S25 | 32 | 35 | revised in place |
| S26a | 33 | 36 | revised in place |
| S26b | 34 | 37 | revised in place |
| S27 … S56 | 35–76 | 38–79 | moved +3 |

Section ranges:

| Section | Old pages | New pages |
|---|---|---|
| 01 | 1–11 | 1–12 |
| 02 | 12–28 | 13–30 |
| 03 | 29–43 | 31–46 |
| 04 | 44–61 | 47–64 |
| 05 | 62–71 | 65–74 |
| 06 | 72–76 | 75–79 |

The note pacing table, the Contents labels (unchanged), `1 / 79`, the note's cross-references and the leaf OUTLINE are updated to match. The note's cross-references are: slides 14–28, 28, 39, 43–45, 59–60, 66 and 70 in the main deck, and 10 for the biased-label case. References into `lec12tech.html` are unchanged.

## Time map (90 min kept; every section budget unchanged)

| Slide | Old min | New min | Elapsed after |
|---|---|---|---|
| S77 (new) | — | 0.75 | 1.5 |
| S74 | 0.75 | 0.75 | 2.25 |
| S04 | 2.5 | 2 | 4.25 |
| S05 | 1 | 0.75 | 5 (as before) |
| S21 → S21a / S21b | 2.5 | 1.25 + 1.25 | 28.75 / 30 (as before) |
| S23 → S23a / S23b | 1.25 | 0.5 + 0.75 | 30.75 / 31.5 (as before) |
| S25, S26a, S26b | 1, 0.75, 0.75 | unchanged | unchanged |

S06, S08 and S09 keep 1 min each. With S78 missing, only 0.75 min had to be freed. If S78 is added, the plan-v2 cuts to S06, S08 and S09 (1 → 0.75 each) give 0.75 min for it.

## Deviations from the plan

- **S78 not built.** This is the plan's capability contingency; see Plan issues. With no S78, the deck has 79 slides, not about 80.
- S21b: the plan asks to "highlight one non-degenerate group segment". I explain the segment rule once for all three segments instead of outlining one. An outline box over thin lines on the 200-px strip covered the endpoints it was meant to show. Preference; I can outline the White segment if you want it.
- S25: the outline box also encloses the "0" tick label, so the reading points at its bin label.
- S23a: "court, pretrial; people decide" in the diagram is my wording for E03's "scores informed pretrial decisions". It makes no claim about automatic detention.

## Plan issues

1. **S78 — no image-generation capability.**
   - No image-generation tool is configured in my environment: no MCP server, no CLI, no package.
   - I sent one request through the existing credential gateway to the OpenAI images endpoint: model `gpt-image-1`, the exact prompt "Generate a photo of a CEO.", n = 1, 2026-11-13 13:55 UTC.
   - It was rejected with HTTP 401, "Missing scopes: api.model.images.request". No image was produced. I made no retries and tried no other model.
   - The Google Generative Language endpoint has no credential configured.
   - I made no configuration or credential changes. Options for slides-review / Albert:
     - (a) Albert grants an image-generation scope or connects a provider. I then run the single generation under E10's rules and add S78 in round 2.
     - (b) Use the plan's alternative: a genuinely sourced published occupation example with its real prompt and model. E11 notes that Bianchi et al. list "a CEO" among their prompts, but neither inspected source figure shows a CEO. So this would mean a different occupation, labeled as such, and it overlaps with S51a/b.
     - (c) Drop S78 and keep S77 as the only opening example.
   - I recommend (a) if Albert can enable it, else (c).
2. None for P1–P3.

## Unsourced facts

- None added.
- Plot readings are measured from the source figures and labeled approximate.
- The S77 photo details (date, author, license, SHA-1) come from the Commons file metadata.
- "Everyone in the same sweatshirt" in the S77 note is an observation of the photo, not a claim about the people.

## Checks run

- `scripts/lint-deck.py` on the deck and the note: the note is ok. The deck shows one warning, 30 hard-coded inline colors, which the baseline also has (30), so nothing new.
- `scripts/find-wordy.py`: three flags, all on unchanged slides (S24, S38, S50b), which the baseline also has. Nothing on changed slides.
- `scripts/outline-lint.py`: 0 stale pointers. I also checked every `:N` pointer in the lec12 section against the file: each one lands on the slide `<div>` or `<img>` it names.
- Render: headless Chromium print gives 79 pages. At `-r 60` I read:
  - S03, S77 and S74 (pp 3–5)
  - S20b to S27 (pp 28–38)
  - every changed slide plus its neighbours.
- Fixes found by render:
  - S21a: the highlight collided with the cite, so I moved it into the annotation column.
  - S21b: the image column pushed the annotations and key off the right edge, so I set the images to 200 / 61 px height and let the key items wrap. No type was shrunk.
  - S25: I extended the outline height to take in the "0" label.
