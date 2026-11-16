# work-r1 — 2026-11-16-lec12-fairness-clarity

## Branch and commits
- Branch `2026-11-16-lec12-fairness-clarity`, from baseline `6f5088cdfc7877ea7965b972df91c8447562b5f4`.
- No ID-only commit: the deck and note already carried slide IDs.
- `b3e8531`: order-only move of S74 and S51a to after S03, and of S20a to before S12, in both the deck and the note. No content change.
- Package commits, merged without conflicts: P1 `50e4092`, P2 `35e8161`, P3 `e1a0142`, P4 `5cb95d7`, P5 `034a9ba`.
- `a107af9`: integration (pace, numbering, `1 / 87`, opening notes, OUTLINE, tracked copies of job/requests/evidence/plan-v1).
- The head commit containing this file is the reviewed commit; its SHA is in the pointer.

## Per package
- **P1 (opening, section 01).** S77 deleted (C02: no source found for the "most important person" example, so it is removed as the request allows). The CEO image (S78) was removed. S78 is now an SVG that separates a statistical question (does the model reproduce a pattern?) from a normative one (should the decision follow it?), with the line "A learned correlation can still reinforce exclusion" (C04). Bianchi occupation rows (S51a) moved to the opening as the model-bias example (C03); retitled "Occupation Prompts Can Reinforce Stereotypes". S74 states what is observed on each branch: approved means repayment is then observed; denied means no loan, so repayment is never observed. S04 split into S04a (Fig. 1A crop, key for 55th/97th percentiles) and S04b (mechanism: cost target → less spent at equal illness → need understated), with "delayed visits are not established as the sole explanation" on the slide and in the note (C05, E05). S07 retitled "Who Is in a Face Benchmark?" and states each benchmark's task (C06). S09 footer reworded to match S12b.
- **P2 (section 02).** S20a now opens the section (C11). S12 split into S12a "Selected Means Loan Approved" and S12b "Denied Applicants Have Missing Outcomes" (C07: Ŷ=1 = approved; Y=1 = would repay is stipulated in the teaching population; in real records it is unknown for denied applicants). New S79 four-rate table and S80 three-rule comparison table (C08, C11). One-line summary under each of S14/S15/S16 (C12); the S16 key says the navy square is "approved", not the outcome or group (C08). One-line plot readings on S17a/S17b (C09, C10). New S81 "Precision Averages the Approved Mix" (C11). S21b says what "most profitable equalized-odds" means (C13). On whether the paper says "equal TPR and equal FPR are necessary" (C08): the S16 slide and note say equal TPR and equal FPR is the definition of equalized odds, and that other fairness goals need not require both; the S80 note adds that none of the three rules is the definition of fairness. Inline SVGs come from `criteria_examples.py`.
- **P3 (section 03).** Northpointe is named on first use (S23a, S27; C14). S29 is retitled "Base Rate Means Recorded Rearrest Share" and gives the base rate in the running example (C15). S30 "The Rates Are Linked, Not Ranked" answers that FPR is not the golden target (C16). S32a "Recorded Positive Means Rearrest in This Example" (C17). S32b and new S82 "Equal Base Rates Can Permit All Three" answer C18: with unequal base rates, 0 < PPV < 1 and TPR > 0, equal PPV, FPR and FNR cannot all hold (Chouldechova identity); with equal base rates they can, but are not guaranteed to; a perfect predictor is the other exception. The 60-person population is labelled synthetic. Generator: `calibrated_errors.py`.
- **P4 (section 04).** S40a/S40b state that reductions refits the ordinary model with reweighted costs; no extra fairness classifier is trained (C19, E12). New S83 "Same-Direction Gaps Cannot Cancel": a mixture balances only when the candidate fits differ in direction, and the training costs push toward such candidates. A useful opposite-bias pair is not guaranteed (C20, E14). New S84 gives the measured protocol: ε from .001 to .1, logistic regression, mixture, 75/25 split, Adult/gender and COMPAS/race (C21, E13). The S41a/S41b messages are stated. S43a: constraints cost modelled lender profit, which is not the same as social welfare (C22, E15). S76 "Nine Alternatives, Not Nine Steps" and S44a/S44b: nine separately evaluated methods, each against its own baseline (C23, E16). S45 explains "a biased label stays biased": fixing the rates does not fix what the label records (C24, E17). Generator: `reductions_mix.py`.
- **P5 (sections 05–06).** S49a/S49b/S50a/S50b define the BBQ terms in plain language: *ambiguous* means the context lacks the evidence to answer, so "unknown" is correct; *disambiguated* means added context identifies the answer (C25, E18). S51b made self-contained after S51a moved. S54a calls back to the opening care case ("Choose Need, Not Merely Spending"; C05). S54b note names Northpointe and recorded rearrest. S55 tradeoff box reads "unequal base rates: some criteria conflict, except special cases", consistent with S82.
- **Integrator.** Pace lines recomputed (sections 10/25/15/20/13/7 = 90 min, verified by summing the note). Note `<h2>` and deck comments renumbered 1–87; `1 / 87`; note pacing table updated to 1–14 / 15–36 / 37–53 / 54–73 / 74–82 / 83–87. S01 and S03 notes rewritten for the new opening (they still described the removed photo and CEO image). Tech pointers in the note checked against `lec12tech.html` page order; all correct, none changed. Leaf `OUTLINE.md` updated: summary, ID range, section table with line pointers, figures, revision entry.

## Slide mapping (baseline page → new page)
| slide ID | old page | new page | change |
|---|---|---|---|
| S01 | 1 | 1 | same |
| S02 | 2 | 2 | same |
| S03 | 3 | 3 | same |
| S77 | 4 | — | deleted (C02) |
| S78 | 5 | 6 | rebuilt in place (SVG; CEO image removed) |
| S74 | 6 | 4 | moved to opening |
| S04 | 7 | — | split → S04a/S04b (p. 7–8) |
| S05 | 8 | 9 | renumbered |
| S06 | 9 | 10 | renumbered |
| S07 | 10 | 11 | renumbered |
| S08 | 11 | 12 | renumbered |
| S09 | 12 | 13 | renumbered |
| S10 | 13 | 14 | renumbered |
| S11 | 14 | 15 | renumbered |
| S12 | 15 | — | split → S12a/S12b (p. 17–18) |
| S13a | 16 | 19 | renumbered |
| S13b | 17 | 20 | renumbered |
| S13c | 18 | 21 | renumbered |
| S13d | 19 | 22 | renumbered |
| S14 | 20 | 24 | renumbered |
| S15 | 21 | 25 | renumbered |
| S16 | 22 | 26 | renumbered |
| S17a | 23 | 28 | renumbered |
| S17b | 24 | 29 | renumbered |
| S18 | 25 | 30 | renumbered |
| S19a | 26 | 31 | renumbered |
| S19b | 27 | 32 | renumbered |
| S20a | 28 | 16 | moved before S12a |
| S20b | 29 | 34 | renumbered |
| S21a | 30 | 35 | renumbered |
| S21b | 31 | 36 | renumbered |
| S22 | 32 | 37 | renumbered |
| S23a | 33 | 38 | renumbered |
| S23b | 34 | 39 | renumbered |
| S24 | 35 | 40 | renumbered |
| S25 | 36 | 41 | renumbered |
| S26a | 37 | 42 | renumbered |
| S26b | 38 | 43 | renumbered |
| S27 | 39 | 44 | renumbered |
| S28 | 40 | 45 | renumbered |
| S29 | 41 | 46 | renumbered |
| S30 | 42 | 47 | renumbered |
| S31 | 43 | 48 | renumbered |
| S32a | 44 | 49 | renumbered |
| S32b | 45 | 50 | renumbered |
| S33 | 46 | 52 | renumbered |
| S34 | 47 | 53 | renumbered |
| S35 | 48 | 54 | renumbered |
| S36 | 49 | 55 | renumbered |
| S37 | 50 | 56 | renumbered |
| S38 | 51 | 57 | renumbered |
| S39a | 52 | 58 | renumbered |
| S39b | 53 | 59 | renumbered |
| S40a | 54 | 60 | renumbered |
| S40b | 55 | 61 | renumbered |
| S75 | 56 | 62 | renumbered |
| S41a | 57 | 65 | renumbered |
| S41b | 58 | 66 | renumbered |
| S42 | 59 | 67 | renumbered |
| S43a | 60 | 68 | renumbered |
| S43b | 61 | 69 | renumbered |
| S76 | 62 | 70 | renumbered |
| S44a | 63 | 71 | renumbered |
| S44b | 64 | 72 | renumbered |
| S45 | 65 | 73 | renumbered |
| S46 | 66 | 74 | renumbered |
| S47 | 67 | 75 | renumbered |
| S48 | 68 | 76 | renumbered |
| S49a | 69 | 77 | renumbered |
| S49b | 70 | 78 | renumbered |
| S50a | 71 | 79 | renumbered |
| S50b | 72 | 80 | renumbered |
| S51a | 73 | 5 | moved to opening |
| S51b | 74 | 81 | renumbered |
| S52 | 75 | 82 | renumbered |
| S53 | 76 | 83 | renumbered |
| S54a | 77 | 84 | renumbered |
| S54b | 78 | 85 | renumbered |
| S55 | 79 | 86 | renumbered |
| S56 | 80 | 87 | renumbered |
| S04a | — | 7 | new |
| S04b | — | 8 | new |
| S12a | — | 17 | new |
| S12b | — | 18 | new |
| S79 | — | 23 | new |
| S80 | — | 27 | new |
| S81 | — | 33 | new |
| S82 | — | 51 | new |
| S83 | — | 63 | new |
| S84 | — | 64 | new |

## Comment locators (new pages; note entries carry the same ID)
| comment | slides (new page) |
|---|---|
| C01 | whole deck and note |
| C02 | S77 deleted; opening is S74 (4) |
| C03 | S51a (5); CEO image removed from S78 |
| C04 | S74 (4), S51a (5), S78 (6) |
| C05 | S04a (7), S04b (8), S54a (84) |
| C06 | S07 (11) |
| C07 | S12a (17), S12b (18), S13a–d (19–22), S09 (13) |
| C08 | S79 (23), S80 (27), S16 key (26) |
| C09 | S17a (28) |
| C10 | S17b (29) |
| C11 | S20a (16), S12a/b (17–18), S79 (23), S80 (27), S18–S19b (30–32), S81 (33) |
| C12 | S14 (24), S15 (25), S16 (26), S80 (27) |
| C13 | S21b (36) |
| C14 | S23a (38), S27 (44) |
| C15 | S29 (46) |
| C16 | S30 (47) |
| C17 | S32a (49), S33 (52) |
| C18 | S32b (50), S82 (51) |
| C19 | S40a (60), S40b (61) |
| C20 | S75 (62), S83 (63) |
| C21 | S84 (64), S41a (65), S41b (66) |
| C22 | S43a (68), S43b (69) |
| C23 | S76 (70), S44a (71), S44b (72) |
| C24 | S45 (73), S54a (84) |
| C25 | S49a (77), S49b (78), S50a (79), S50b (80) |

## Deviations
- **Section 02 per-slide minutes.** The plan's approximate per-slide times for P2 sum to about 17.75 min against the 25-min section budget. P2 set per-slide times to reach the budget; the section total is 25 as planned.
- **S45 is 1 min (plan 0.75); S42 keeps 2 min.** Section 04 still totals 20.
- **Figure widths, not type.** S17a/S17b images reduced from 460 to 440 px so the key column fits; S50b image from 1080 to 1000 px. No font size was reduced.
- **S45 note.** The comparison table was replaced by lists so it reads at narrow width.
- **Retired image files.** `s77-group-photo.jpg` and `s78-wan-chang-ceo.jpg` are no longer on slides. They were left in `figs/`; deleting them is outside the plan.

## Plan issues
- **Approximate plot readings, please confirm against the sources.** These are read off published figures and marked as approximate on the slides: S44b disparate impact about 0.5 → 0.9, balanced accuracy about 0.745 (AIF360 Fig. 5(b), E16); S41a "roughly one point" of error (Agarwal Fig. 1, E13); S41b parity violation "toward about 0.02" (E13). They are not stated numerically in evidence.md.
- **S55 and S54b leave about 40–45% of the content area blank.** S55 has text boxes but no figure. Layout is unchanged from the baseline. Not changed in this round; say if you want it.

## Unsourced facts found
None added. No fact was corrected from memory.

## Generators (repo-relative, deterministic)
- `courses/trustworthy-ai/figs/lec12-visual-motivation/criteria_examples.py`: run as `python3 criteria_examples.py ../../lec12-fairness.html`. It rewrites the inline SVG between `<!--p2gen:KEY-->` markers (S79, S80, S14–S16 exhibits). Counts A = (TP, FP, FN, TN) = (3, 1, 3, 3) and B = (1, 3, 1, 5), as in the baseline.
- `.../calibrated_errors.py <s29|s32a|s32b|s33|s82>`: prints the SVG for one slide and asserts the stated rates on the synthetic 60-person population. With no argument it stops with an IndexError (tooling only, not fixed).
- `.../reductions_mix.py [outdir]`: writes `reductions-mix-s75.svg` and `reductions-gap-s83.svg`, which are pasted inline. The `.svg` outputs are not committed.

## Checks
- `lint-deck.py` on the deck: 0 errors and no font-size warnings. One warning remains: hardcoded colors in inline styles, 30 occurrences, the same count as the baseline. The note passes with `ok`.
- `find-wordy.py` on the deck flags three 16-word plot keys: S16 key (navy box = approved), S24 key, S38 key. All are kept under the §1 plot-key exception.
- `outline-lint.py`: 0 stale pointers.
- Render: all 87 pages of the merged deck at `-r 60`. There is no overflow, clipping, text overlap, broken image or raw KaTeX. Minor tight spacing remains on S39a, S39b, S44a (two-line title; axis title touches the citation without overlapping) and S19b. The bold word "at"/"above" wraps alone in the right-hand captions on S26a/S26b. The sparse S54b and S55 are noted above. Workers render-checked their own ranges with neighbours before merging.
- Note at narrow width: integrator checked S81, S82, S50a and S54b at 485 px, the headless minimum. There is no horizontal overflow outside the hidden MathML.
- Section minutes are summed from the note pace lines: 10 / 25 / 15 / 20 / 13 / 7 = 90.
