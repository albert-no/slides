# Plan v2 — Lec12 visual and motivational pass

Job: `2026-11-10-lec12-visual-motivation` · medium · round limit 2.
Baseline: `cd0da5ca7ad75ceef107d28ad110407f0c33b4ff`.
Main: `courses/trustworthy-ai/lec12-fairness.html`.
Notes: `courses/trustworthy-ai/lec12-fairness-note.html`.
Supplement: `courses/trustworthy-ai/lec12tech.html`.
Audience: mixed-major sophomore/junior undergraduates; concept-first; 90 minutes; no activities.


## Changes since v1 (round-1 decisions)

- Accept 74 main / 23 tech pages and the reported S17, S44, S50 and technical splits; counts remain targets. Accept the 90-minute allocation and keep S75 on screen. These choices improve explanation without changing the argument.
- Accept “Calibration Plus Balance Forces Exceptional Cases” for the theorem: the v1 shorthand title omitted a necessary premise.
- E24 corrects Bianchi's source section to §2.2 and clarifies separate gender/race matching, not six intersectional centroids. Fig.3 and Stable Diffusion v1-4 are verified.
- Calibration notation in tech explicitly uses discrete positive-mass score/group cells. No continuous-score expansion requested.
- E27 records actual generator/inline-SVG locations; no redundant generator is required.
- All v1 requirements not changed here remain. Correctness/readability fixes are numbered in review-r1.md. That review is the round-2 work order; do not rework already accepted slides beyond changed-page neighbours.

## 1. Summary and decisions

[judgment] Preserve the six-section argument and established literature. Replace miniature diagrams and dense comparison slides with large, staged examples. Introduce the decision and its human consequence before the first study. Carry a small synthetic lending population through the denominator comparisons; use exact integer people for the calibrated-score example; explain reductions with a visible training loop and an explicitly hypothetical mixture. Keep real empirical figures as evidence, not reconstructed curves. This is explanation/readability work, not a new lecture or survey.

**Must:** every original request in requests.md; readable essential diagram labels throughout main and tech; connected, correctly directed arrows throughout; correct numbers, denominators and scope; existing 90-minute budget; paired notes; all established topics retained on screen or explicitly migrated below. Do not enlarge fonts merely in source units: judge the final render. Follow DESIGN_SYSTEM.md §§1,2,4,5,6,8,9,10; never shrink type or compress prose spacing to fit.

**Prefer [judgment]:** the title sequence, concrete exhibits, splits and timing below. **Slides decides:** component choice, exact wording, crop/split choices and final page count. Report deviations and mappings; ask before changing an argument, required content, fact, scope or teaching time. If these examples expose a plan error, flag it rather than forcing the plan.

The target is about 71 main pages, not a quota or ceiling. Splits share the time formerly spent on a dense page. Section budgets remain 10 / 20 / 15 / 20 / 15 / 10 minutes, including title/dividers/transitions. Tech is optional, outside the 90 minutes. Keep the existing short speaker script plus expanded companion sections, not a new transcript.

### Continuity
- Reuse the established confusion-matrix/TPR/FPR language from the course through self-contained Recall-style examples (S12–S13); do not assume the earlier lecture is open.
- Adapt score calibration already taught in the reliability lecture to **within-group** calibration; explain the additional group conditioning. Do not re-teach confidence estimation.
- Reuse Gender Shades as a familiar case, but distinguish benchmark composition (S07), intersectional errors (S47), and follow-up (S48).
- Individual/counterfactual fairness and formal impossibility proofs remain notes/tech. No new theorem, law survey, activity, demo or homework. Root/leaf audience mismatch is resolved by the leaf's narrower audience for this job only.
- Match the concept-first rhythm of lec02: general motivation, concrete case, mechanism, scoped result. Existing exemplar shortcomings do not override current design rules.

### IDs and baseline map
No IDs exist at baseline. In an **ID-only commit**, assign main S01–S56 in baseline order and tech S57–S73 in baseline order; add matching IDs to the 56 note articles. Technical IDs are deliberately distinct. No technical-note file exists or is requested. Record the ID-only SHA in work-r1.md. New main S74 goes after S03/before S04; S75 goes after the S40 family/before S41. Add new/split IDs only in the content commit; never renumber existing IDs. The numbered specs below are keyed by these IDs, not revised page numbers.

| File | Baseline page | ID | Baseline title |
|---|---:|---|---|
| main | 1 | S01 | Fairness |
| main | 2 | S02 | Contents |
| main | 3 | S03 | Where Bias Enters |
| main | 4 | S04 | Case: Cost as a Proxy for Need |
| main | 5 | S05 | A Model Learns Its World |
| main | 6 | S06 | Three Places Bias Enters |
| main | 7 | S07 | Biased Data: Who Got Sampled |
| main | 8 | S08 | The Label Is the Problem |
| main | 9 | S09 | Feedback Loops: An Illustration |
| main | 10 | S10 | Why "Just Drop Race" Fails |
| main | 11 | S11 | Measuring Fairness |
| main | 12 | S12 | Setting Up the Notation |
| main | 13 | S13 | Four Rates, Four Denominators |
| main | 14 | S14 | Demographic Parity |
| main | 15 | S15 | Equalized Odds |
| main | 16 | S16 | Equal Odds, Equal Mistakes |
| main | 17 | S17 | Equalized Odds on the ROC Plane |
| main | 18 | S18 | Calibration Within Groups |
| main | 19 | S19 | Calibration vs Predictive Parity |
| main | 20 | S20 | Five Criteria, Five Comparisons |
| main | 21 | S21 | Same Data, Five Rules |
| main | 22 | S22 | COMPAS and Impossibility |
| main | 23 | S23 | What COMPAS Is |
| main | 24 | S24 | False Positives, By Group |
| main | 25 | S25 | The Gap Persists Within Subgroups |
| main | 26 | S26 | Northpointe Responds: Read by Row |
| main | 27 | S27 | The Analyses Evaluated Different Criteria |
| main | 28 | S28 | Rearrest Is Not Offending |
| main | 29 | S29 | The Key Ingredient: Base Rates |
| main | 30 | S30 | Chouldechova: One Identity |
| main | 31 | S31 | Kleinberg et al.: Three Conditions on a Score |
| main | 32 | S32 | Worked Example: Calibrated, Unequal Errors |
| main | 33 | S33 | Why the Gap Appears Here |
| main | 34 | S34 | Choosing by Context |
| main | 35 | S35 | Mitigation |
| main | 36 | S36 | Three Places to Intervene |
| main | 37 | S37 | Reweighing |
| main | 38 | S38 | Reweighing: A Worked Example |
| main | 39 | S39 | Reweighing, Measured |
| main | 40 | S40 | The Reductions Approach |
| main | 41 | S41 | Reductions, Measured |
| main | 42 | S42 | Group-Specific Thresholds |
| main | 43 | S43 | The Cost, on FICO Data |
| main | 44 | S44 | An Empirical Tradeoff, Not the Optimal Frontier |
| main | 45 | S45 | Method Cards |
| main | 46 | S46 | Beyond Classifiers |
| main | 47 | S47 | The Gender Shades Audit |
| main | 48 | S48 | After the Audit: Error Fell on the Named Systems |
| main | 49 | S49 | Auditing Language Models: BBQ |
| main | 50 | S50 | BBQ: Bias Shows Most When Context Is Ambiguous |
| main | 51 | S51 | Generators Can Exaggerate Stereotypes |
| main | 52 | S52 | Governance: Obligations and Their Limits |
| main | 53 | S53 | Synthesis |
| main | 54 | S54 | A Checklist |
| main | 55 | S55 | Key Takeaways |
| main | 56 | S56 | Which rate? |
| tech | 1 | S57 | Fairness: The Math |
| tech | 2 | S58 | When to Use This |
| tech | 3 | S59 | Criteria |
| tech | 4 | S60 | Setup: Four Rates per Group |
| tech | 5 | S61 | Five Criteria, Written Out |
| tech | 6 | S62 | Another Notion: Individual Fairness |
| tech | 7 | S63 | Another Notion: Counterfactual Fairness |
| tech | 8 | S64 | Calibration Fixes PPV Only Through the Score Mix |
| tech | 9 | S65 | Impossibility |
| tech | 10 | S66 | Chouldechova's Identity |
| tech | 11 | S67 | Kleinberg et al.: Proof Sketch |
| tech | 12 | S68 | The Worked Example, Computed |
| tech | 13 | S69 | Mitigation |
| tech | 14 | S70 | Reweighing |
| tech | 15 | S71 | Reductions: A Saddle Point |
| tech | 16 | S72 | Group Thresholds: A Derived Predictor |
| tech | 17 | S73 | Compared to whom? |

## 2. Request coverage

C01 is interpreted using C06; lec11 is excluded. C02–C04 are whole-deck requests; the cited pages are examples, not boundaries. No conflicting author requests remain.

| Comment | Baseline page / title | Slide IDs | Package / acceptance |
|---|---|---|---|
| C01 | Main 1–56, whole lecture; corrected by C06 | S01–S56; new S74–S75 | P1–P6 plus shared integration; entire main visually reviewed |
| C02 | Whole lecture; especially 4–10, 12–20, 29–33, 37–40, 49 | S74; S04–S10; S12–S20; S29–S33; S37–S40; S75; S49; S54 | P1–P6; substantive examples, not decorative images |
| C03 | 40 / The Reductions Approach; all diagrams | S40a–S40b and all main/tech diagrams | P1–P7; essential labels readable at final slide size |
| C04 | 6 / Three Places Bias Enters; all arrows | S06, S09, S36, S40a–S40b and all connected diagrams | P1–P7; no detached heads, wrong direction, clipped loops or text crossings |
| C05 | Later detailed revision is a separate PR | Entire job | Integration; no speculative extra scope; Albert retains final check |
| C06 | Target is lec12 fairness, not lec11 | All IDs above | Path allowlist below; no lec11 changes |
| C07 | Resume from existing job folder | Entire job | Continue pinned baseline and requests; do not restart/rebase the job |

## 3. Slide specs

All rows are **[judgment]** explanatory/design choices. Point, required content, evidence qualifiers and acceptance are **must**; proposed titles, components and time allocations are **prefer**. A row's exhibit is its required visual reading, not an instruction for markup or geometry. Structural slides use the corresponding deck component and need no empirical source. Evidence IDs resolve to the exact URLs/locations in evidence.md.

**Common disposition (applies to every row):** the slide keeps its point, necessary qualifier and reading key; the paired note keeps full setup, calculations, source links, historical date, limitations and anything trimmed from baseline. Formal derivations stay in tech. The notes must identify illustrative examples as such. The last column adds a specific migration/acceptance check, not a substitute for that common requirement. For all diagrams, labels and arrow directions must match the prose; for charts, retain axes, units, encodings, uncertainty and scope. Every content slide has one exhibit, not an exhibit plus a competing table. Component names below are vocabulary only.

### P1 — Why the decision matters (10 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S01 | Fairness | Frame decisions, measurements and consequences; preserve lecture identity. | Course outline | title-slide; .25 | No new scope promise. |
| S02 | Contents | Six existing sections, same order and names. | Course outline | toc-list; .25 | Matches every divider. |
| S03 | Where Bias Enters | Introduce data, labels and feedback. | E20 | section-slide; .25 | Existing section retained. |
| S74 | Who Gets the Opportunity? | A score becomes an allocation decision. One illustrative applicant→decision→opportunity diagram; explain that rejecting a potential repayer and lending to a non-repayer are different errors. | E20 | diagram-flow; .75 | Explicit illustrative setup; answer why fairness matters before the first case. No measured harm claim. |
| S04 | Predicting Cost Missed Medical Need | Use the actual Obermeyer Fig.1 relationship: at a given score, Black patients had greater illness burden. Name cost as the proxy and extra care as the decision. | E01 | cols; 2.5 | Prefer one readable original panel. Keep 17.7%→46.5% and simulated-remedy qualification in notes if not the chosen exhibit; never imply deployed treatment benefit. |
| S05 | Past Records Can Shape Decisions | The learned pattern is not automatically a legitimate target. One large records→training→decision schematic, with an explicitly possible disparity pathway. | E20 | diagram-flow; 1 | Use “can”, not inevitable amplification; remove redundant bullets to enlarge the mechanism. |
| S06 | Three Places Bias Enters | One process map distinguishes sampling, target choice and decisions feeding later observations. Identify the three stages directly on the diagram. | E20 | diagram-flow; 1 | Repair the baseline p6 return arrow and every connection; label the return as future data, not a fourth kind of evidence. Move card explanations to notes. |
| S07 | Benchmark Composition Can Hide Gaps | Compare lighter-skin shares for IJB-A, Adience and PPB using source-derived bars; a balanced evaluation can expose overlooked groups. | E02,E21 | cols; 1 | Composition is not proof of the cause of an error gap; no unsupported medical-data example on screen. |
| S08 | A Proxy Can Answer the Wrong Question | One illustrative contrast: desired repayment outcome versus recorded historical approval. Name the target mismatch without marking both as the same Y. | E20 | grid-2; 1 | Make Y the recorded label; hypothetical approval does not establish prejudice in a real dataset. Notes retain target-design caveat. |
| S09 | Missing Outcomes Can Reinforce Exclusion | Lending feedback loop: denial→missing repayment evidence→unfavorable treatment→denial. The unfavorable interpretation is an explicit assumption. | E20 | diagram-flow; 1 | Absence of evidence is not evidence of risk; loop closes visibly, not through labels. |
| S10 | Dropping a Column Can Leave Information | An illustrative feature table removes group while a correlated feature remains; this shows a possibility, not a claim that every ZIP/name/school is predictive everywhere. | E20 | grid-2; 1 | Readable retained feature labels; correlation assumption on slide. No fairness guarantee from deletion. |

### P2 — Count people before naming rates (20 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S11 | Measuring Fairness | Each criterion chooses a comparison population. | E03,E13 | section-slide; .25 | Section name matches Contents. |
| S12 | One Decision, Two Recorded Outcomes | Introduce A, recorded Y and selection decision using the E13 lending population. A=(3,1,3,3), B=(1,3,1,5), in TP/FP/FN/TN order. | E13 | grid-2; 1.25 | Fully labeled synthetic population, not observed outcomes of real denied borrowers; define positive decision as loan selection. |
| S13a | Selection Counts Everyone | Highlight all applicants as denominator, selected applicants as numerator; A selects 4/10. | E13 | grid-2; .75 | Use the same people and encodings as S12; other rates wait. |
| S13b | True Positives Count Repayers | Highlight recorded repayers as denominator; A selects 3/6. Spell out true-positive rate. | E13 | grid-2; .75 | Non-repayers are visually outside this denominator. |
| S13c | False Positives Count Non-Repayers | Highlight recorded non-repayers as denominator; A selects 1/4. Spell out false-positive rate. | E13 | grid-2; .75 | Selection is favorable to applicant here; FP is not universally the same harm across applications. |
| S13d | Precision Counts the Selected | Among A's four selected applicants, three repay: 3/4. Spell out positive predictive value (PPV). | E13 | grid-2; .75 | Selected population, not all repayers, is visibly the denominator; formulas/full comparison in notes/tech. |
| S14 | Equal Selection Can Hide Unequal Outcomes | Same E13 people: both select 4/10, yet selected repayers are 3/4 versus 1/4. Name demographic parity. | E13,E19 | grid-2; 1.5 | Keep selection and outcome encodings distinct and redundant; no claim that parity ensures qualification. |
| S15 | Equal Opportunity Leaves One Error Unchecked | Same E13 people: TPR 3/6=1/2 in both groups; FPR 1/4 versus 3/8. Name equal opportunity and its one-condition scope. | E03,E13 | grid-2; 1.5 | Explicit answer: equal TPR alone does not constrain FPR. This replaces baseline duplication, not a new criterion. |
| S16 | Equalized Odds Checks Both Classes | Separate illustrative population: each group has ten positives and ten negatives, with 8/10 TPR and 2/10 FPR. Two outcome-conditioned rows form one exhibit. | E03,E13 | grid-2; 1.5 | Clearly label change of population; match rates, not absolute error counts in arbitrary groups. |
| S17 | Equalized Odds Needs a Shared Attainable Point | Original Hardt Fig.1: read FPR horizontally and TPR vertically, then the intersection of attainable regions. Contrast opportunity as matching height. | E03 | cols; 2 | Do not say any point below both curves is attainable. Split source panels if labels cannot be read; enlarge the external key without repainting data. |
| S18 | A Calibrated Score Has a Meaning | Two groups each with ten people scored .7, seven recorded positives: same score has the stated frequency in each group. | E04; illustrative counts | grid-2; 1.5 | Illustration, not data; keep numerical calibration distinct from groups merely agreeing. |
| S19a | Calibrated Buckets Can Have Different Mixes | E14 three-score population: scores .2/.6/.9, each bucket calibrated, but A and B have different bucket sizes. Show buckets, not all fairness metrics. | E14 | grid-2; 1.5 | Exact counts and meaning of filled markers readable; notes carry full six-cell table. |
| S19b | Calibration Does Not Fix Cutoff Precision | At cutoff >.5, highlight the selected E14 buckets: A 24/30 versus B 21/30. PPV averages the selected score mix. | E14,E05 | grid-2; 1.5 | Explicit answer is on screen. Two-score/same-top-score special case and tower-rule calculation in note/tech S64. |
| S20a | Which Population Does the Rule Compare? | Visual denominator map for selection, equal opportunity and equalized odds; reuse the same cohort outlines rather than a five-row table. | E03,E13 | grid-3; 1 | Every name maps to the correct denominator; avoid another numerical example. |
| S20b | Score Meaning Is Not Selection Precision | Contrast a same-score bucket with a selected-above-cutoff cohort; name calibration and predictive parity. | E04,E05,E14 | grid-2; 1 | Complete five-criterion reference table moves to notes/tech S61; do not repeat both full definitions as prose walls. |
| S21 | The Same Scores Yield Different Decisions | Original FICO Fig.9: method labels, four groups and threshold positions; show how a chosen rule moves decisions, not which rule is universally best. | E07 | cols; 2.5 | Explain FICO repayment setting and threshold before reading the chart. Raw-score panel preferred; percentile panel remains notes or a readable split. |

### P3 — Why the disagreement is real (15 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S22 | COMPAS and Impossibility | One dataset can answer different fairness questions. | E05,E06 | section-slide; .25 | Do not promise universal impossibility. |
| S23 | What the COMPAS Audit Measured | Diagram: historical risk score→audit cutoff→recorded two-year rearrest. Identify commercial US justice score, Broward County and historical audit. | E05,E06 | diagram-flow; 1.25 | Cutoff >4 means medium plus high, unlike vendor high category 8–10. Distribution figure and detailed category breakdown go to notes if competing with setup. |
| S24 | False-Positive Rates Differed by Group | Large existing bars, 44.9% Black versus 23.5% White; denominator is defendants not rearrested within two years. | E06 | cols; 1.5 | Remove undifferentiated 7,214 from headline; source-specific sample counts and false-negative comparison remain notes. Rates are not out of all defendants. |
| S25 | The Gap Appeared Across Prior-Count Bins | Original Chouldechova Fig.2(b), misdemeanor subgroup; FPR by prior-count bin with intervals. | E05 | cols; 1 | Replace “Control for it” with descriptive stratification; wide intervals stay; no causal conclusion. |
| S26a | Similar Decile Outcomes Are Not Probability Calibration | Original Fig.1 left panel; compare recorded rearrest share at a decile by race. | E05 | cols; .75 | Deciles are ranks, not probabilities. Reading key stays legible; never call decile 7 a 70% risk. |
| S26b | Cutoff Precision Was Approximately Similar | Original Fig.1 right panel; PPV above each cutoff, approximately similar at cutoffs 4 and above in this dataset. | E05 | cols; .75 | Not exact equality; do not mistake per-decile comparison for this threshold plot. |
| S27 | Both Analyses Used Different Denominators | One enlarged confusion-matrix exhibit highlights non-rearrested column versus selected row in successive reading steps. | E05,E06 | grid-2; 1 | FPR gap and approximate PPV similarity can coexist. Neither establishes that the whole system is fair. |
| S28 | Rearrest Is Not Offending | One recording-process diagram distinguishes behavior from recorded arrest; all audited rates use the latter. | E05,E06,E20 | diagram-flow; 1 | Possible recording disparity, not an estimated magnitude or a deterministic arrest pipeline. |
| S29 | Base Rates Count Recorded Positives | Synthetic 60-person groups from E15: 30/60 versus 15/60 recorded positives. Highlight cohort, not predictions. | E15 | grid-2; .75 | Replace “trouble begins” with precise point: different outcome prevalence changes rate relationships. |
| S30 | Three Equalities Can Conflict | Visual dependency: base rate, PPV, FNR determine FPR. State unequal nondegenerate base rates, common PPV strictly between 0 and 1, and FNR below 1. | E05 | diagram-flow; 1.25 | Conclusion: FPR and FNR cannot both match. Calibration is not the premise; identity/proof in S66 and notes. No universal conflict claim. |
| S31 | Score Balance Has Its Own Conditions | One three-condition diagram: calibration within groups, same negative-class mean score, same positive-class mean score; equal base rates or perfect prediction are exceptional cases. | E04 | grid-3; 1 | Not the threshold-PPV theorem. Approximation result and proof stay notes/tech S67; retain “not every pair conflicts”. |
| S32a | Both Groups Can Be Calibrated | Exact E15 integer buckets: A high 30 with 24 positive, low 30 with 6; B high 5 with 4, low 55 with 11. Scores .8/.2; threshold >.5. | E15 | grid-2; 1 | Numbers sum to 60 per group. Distinct from E14; on-slide high-bucket PPV .8 in both. |
| S32b | Equal Precision Can Leave Unequal Errors | One rate exhibit derived from those people: FPR 6/30 vs 1/45; FNR 6/30 vs 11/15. Numerators/denominators stay adjacent. | E15 | grid-2; 1 | No giant metrics table plus chart. Notes retain exact fractions and rounded decimals; title is possibility, not inevitability. |
| S33 | The Score Mix Explains This Example | Two group score-share bars: A high 1/2, B high 1/12; shared calibrated .2/.8 scores fix that mix for the chosen base rates. | E15 | grid-2; 1 | Use exact 1/12 or 8.33%, not 8%. Lower FPR/higher FNR is specific to this construction. |
| S34 | Choose the Harm Before the Rate | Two clearly hypothetical decisions: false high-risk flag versus missed diagnosis; highlight the relevant error in each matrix. | E20,E03 | grid-2; 1.5 | Do not equate model flag with arrest or detention. Equal rates need not be low rates; retain stakeholders and utility in point/note. |

### P4 — Show what the intervention actually changes (20 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S35 | Mitigation | Three intervention stages, with explicit targets and limits. | E03,E08,E10 | section-slide; .25 | Section retained. |
| S36 | Change Data, Training, or Decisions | One large stage map ties reweighing to data, reductions to training, thresholds to outputs. | E03,E08,E10 | diagram-flow; .75 | Each method's access requirement stays in notes and later mechanism; arrow audit includes this map. |
| S37 | Reweighing Changes Influence, Not Labels | One cell example: expected independence share 30%, observed 20%, weight 1.5. Show the same examples gaining influence, not new people. | E08 | grid-2; 1.5 | Expected means independence-expected; empty required cells cannot be repaired. Formula/assumptions in notes and S70. |
| S38 | Weights Balance the Training Table | E08 before/weighted bars: (20,30)/(40,10) becomes (30,20)/(30,20); positive share 60% in both weighted groups. | E08 | grid-2; 2 | Move separate weight table to note; preserve exact 2/3, not arithmetic based on rounded .67. No test-prediction parity guarantee. |
| S39 | Training-Data Parity Moved Toward Its Target | Original AIF360 Fig.4(a,c); define statistical parity difference and disparate impact before interpreting; ideal 0 and 1 respectively. | E09 | cols; 1.5 | Use panels as separate reading steps if necessary. Training data, uncertainty and before/after key are visible; no test-set conclusion. |
| S40a | Reductions Reuses Ordinary Training | Baseline p40 becomes a large mechanism exhibit: choose costs→fit classifier→measure constraint violation. Main idea precedes mechanism. | E10 | diagram-flow; 1 | No bullet column stealing diagram space; all three stages and what flows between them readable. |
| S40b | Measured Violations Change the Next Fit | Continue the same mechanism with violation→updated costs→next fit; distinguish adjusting example costs from changing labels. | E10 | diagram-flow; 1 | Return arrow lands on cost update; no convergence or monotonic-improvement claim. Formal game remains S71. |
| S75 | A Random Mixture Can Balance Expected Selection | Hypothetical h1=(.8,.4), h2=(.2,.6), equal group-independent mixing gives expected selection (.5,.5). One mixture diagram. | E17 | diagram-flow; 1.5 | Not averaging scores; not a group-specific switch; not an Agarwal experiment or an optimality claim. Finite counts can differ. |
| S41a | Reductions Shows an Empirical Tradeoff on Adult | Original Agarwal Fig.1 Adult panel with complete external key; x DP violation, y test error, lower-left better. | E10 | cols; 1 | Preserve experiment/model label and uncertainty. Do not call measured curve the optimal frontier. |
| S41b | The Same Method Has a Different COMPAS Curve | Original COMPAS panel, same axes/key; dataset-specific performance rather than a universal ranking. | E10 | cols; 1 | No unsupported cross-dataset comparison of error levels; note the omitted source panels. |
| S42 | Thresholds Change Decisions Without Retraining Scores | Original Hardt Fig.2 selected panel(s), introduced by one-line mechanism: choose attainable group operating points for the target criterion. | E03 | cols; 2 | Group at decision time and labeled held-out calibration data required; randomization may be needed. Extra panels go to notes or a split, never shrink. |
| S43a | Fairness Constraints Change Modeled Lender Profit | Original FICO Fig.11 right panel; explain x break-even repayment probability and y fraction of maximal modeled profit. | E07 | cols; 1 | No universal social-welfare claim or criterion ranking. Correct source section to §7. |
| S43b | One FICO Setting Gives Different Profit Costs | At break-even .82, bars from published numbers: 99.3/92.8/80.2/69.8% for single threshold/opportunity/odds/parity. | E07,E23 | cols; 1 | Source-text values, not traced curve coordinates; label modeled lender profit and this setting. Reproducible inputs retained. |
| S44 | Measured Methods Are Not an Optimal Frontier | Original AIF360 Fig.5(b), Adult/race, balanced accuracy versus disparate impact before/after. Define balanced accuracy as mean of TPR/TNR. | E09 | cols; 2.5 | Full-size crop plus readable external method key; split if needed. Preserve all encoded methods or explicitly disclose crop; no paint-over. Different preprocessing limits comparison. |
| S45 | Each Intervention Fixes a Different Object | One three-stage comparison with target and necessary access per method. Weighted training table, constrained learned predictor, changed decision rule are distinct. | E03,E08,E10 | grid-3; 2 | Full evaluated-population/utility/assumption matrix goes to notes; all three take the recorded label as given. |

### P5 — Audits make the missing comparison visible (15 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S46 | Beyond Classifiers | Move from decision rates to task-specific audits. | E02,E12,E16 | section-slide; .25 | Same section; no expanded law survey. |
| S47 | Intersectional Errors Exceeded Aggregate Impressions | Source-derived Table-4 error bars, vendors by DF/DM/LF/LM; identify historical gender-classification task, PPB and label definitions. | E02,E21,E23 | cols; 2.75 | 12 values match Table4, not South-African Table5; large key and subgroup labels. No face-recognition or causal claim; split if required. |
| S48 | Errors Fell on the Re-Audited Systems | Source-derived dated before/after DF error bars for the three named vendors. | E11,E23 | cols; 2 | Dates May2017/Aug2018 and undetected-face denominator caveat retained in notes; not current performance or causal attribution. Other vendors remain notes. |
| S49a | An Unanswerable Question Needs “Unknown” | One complete original BBQ Fig.1 ambiguous example: context, question, choices and correct answer are legible. | E12 | cols; 1.5 | Choose one question polarity, disclose omitted panels. Unknown is the correct answer, not an invented observed model response. |
| S49b | Added Evidence Changes the Correct Answer | Same original example with disambiguating context; show how evidence, not a stereotype, changes the answer. | E12 | cols; 1.5 | Correct answer and evidence explicit; not every wrong answer is a stereotyped answer. Full example and scoring stay notes. |
| S50 | Ambiguous Context Revealed Stereotype-Leaning Answers | Original BBQ Fig.3, readable panel(s). Define signed direction and different scaling for ambiguous/disambiguated panels before reading. | E12 | cols; 2.5 | Six configurations of five historical models; date/model names remain. Scores are not harm rates or directly identical-normalization panels. |
| S51a | An Occupation Prompt Produced a Narrow Sample | Original Bianchi Fig.3 sample panel; explain prompt and historical Stable Diffusion setup. | E16,E24 | cols; 1 | Sample illustrations are not frequency estimates by themselves. No generated replacement study faces; full prompt in note if space tight. |
| S51b | The Study Measured Representation with CLIP | One measurement pipeline: 100 outputs/occupation→separate nearest-archetype gender (two) and race (three) matches→reported share/comparator. Use software-developer result with its limits. | E16,E24 | diagram-flow; 1 | Historical 99% White versus 56% comparator, not current guarantee; CLIP assignment is not self-identification. Other occupations and exact setup remain notes. |
| S52 | An Audit Requirement Is Not a Fairness Verdict | Dated NYC2023 example: prescribed metrics→independent audit→published summary; short point that a required comparison does not settle all harms. | E22 | diagram-flow; 2.5 | No broad claim that law specifies no criterion. Existing four-jurisdiction table and enforcement details migrate to dated notes under E18/E22 limitations; no fresh legal certification. |

### P6 — Apply the questions, then close (10 minutes)
| ID | Proposed title | Point / required exhibit and content | Evidence | Component; minutes | Specific disposition / acceptance |
|---|---|---|---|---|---|
| S53 | Synthesis | Name the criterion and what it leaves out. | E01,E03,E20 | section-slide; .25 | Keep section name. |
| S54a | Ask What the Label Misses | Instructor walks through the opening care-allocation case: decision, recorded cost, desired need and harm of missing a sick patient; one annotated case map. | E01 | diagram-flow; 3 | A worked return to the hook, not audience activity. Show the answers, not six unanswered checklist bullets. |
| S54b | Ask What the Fix Can Change | Continue the care case: target proxy before optimizing rates; make criterion, evaluation population and utility explicit as decisions still requiring stakeholders. | E01,E03,E20 | diagram-flow; 3 | Do not invent a deployed solution or unique ethical metric. Full six-question baseline checklist preserved in notes, including base-rate conditions. |
| S55 | Name the Decision, Denominator, and Tradeoff | One closing summary map connects those three choices, with value judgment explicitly acknowledged. | E01–E20 synthesis | diagram-flow; 3.25 | Only global recap; baseline six takeaways retained in note, not another bullet wall. No “all metrics conflict”. |
| S56 | Which rate? | Preserve closer: name criterion, denominator and who bears the error. | Lecture synthesis | end-slide; .5 | No extra summary or next-lecture pointer. |

### P7 — Technical supplement: preserve the math, fix presentation
All following rows are optional, **0 core-session minutes**. Component selection and splitting are slides' call; no new mathematics. A formula's prerequisites stay with it. Keep the existing citations and exact assumptions; added numeric examples match E13–E15. Add a one-line intuition where needed, never a filler diagram beside a dense equation. Every changed tech page and its neighbours must be render-checked.

| ID / baseline tech page | Proposed title | Point / required exhibit | Evidence | Disposition and acceptance |
|---|---|---|---|---|
| S57 / 1 | Fairness: The Math | Existing title and optional scope. | Course outline | title-slide; retained. |
| S58 / 2 | When to Use This | One compact route through criteria, incompatibilities, mitigation. | E03–E10,E19 | diagram-flow; no main-page-number dependency. |
| S59 / 3 | Criteria | Existing divider. | E03–E05 | section-slide; retained. |
| S60 / 4 | Four Rates, Four Denominators | Existing formal rates with conditioning events and positivity. | E03,E05 | math-block; split notation setup from rates if dense; no missing PPV-support condition. |
| S61 / 5 | Five Criteria, Written Out | Preserve all five definitions; separate decision conditions from score calibration. Score calibration here uses discrete score/group cells with positive mass, not every real score value. | E03–E05 | math-block; do not fit five display blocks by shrinking. Distinguish score from binary decision. |
| S62 / 6 | Individual Fairness Needs a Task Metric | Preserve Lipschitz map, outcome distributions and metric assumptions. | E19 | math-block; all symbols readable/defined; not a conditional-probability criterion. |
| S63 / 7 | Counterfactual Fairness Needs a Causal Model | Preserve model, intervention, conditioning and quantifiers. | E19 | math-block; split setup/definition as needed, never change causal assertion for layout. |
| S64 / 8 | Calibration Averages Over Selected Scores | Preserve tower-rule identity with selected event positive; optional E14 arithmetic in notes/main note. | E04,E14 | math-block; shared top-score case must say same score value across groups. |
| S65 / 9 | Impossibility | Existing divider. | E04,E05 | section-slide; retained. |
| S66 / 10 | Chouldechova's Identity | Preserve derivation and nondegenerate conditions, separating identity from consequence if necessary. | E05 | math-block; equality of PPV and FPR alone does not imply equal base rates. |
| S67 / 11 | Calibration Plus Balance Forces Exceptional Cases | Preserve common class-mean derivation and theorem conditions; approximation detail stays subordinate. | E04 | math-block; equal base rates or perfect prediction, not “all fairness impossible”. |
| S68 / 12 | The Calibrated Example, Computed | Preserve .2/.8 construction; use exact fractions consistent with 60-person E15. | E15 | math-block; split calibration/PPV from error calculations rather than shrink; 1/12 not .08. |
| S69 / 13 | Mitigation | Existing divider. | E03,E08,E10 | section-slide; retained. |
| S70 / 14 | Reweighing Needs Cell Support | Preserve expected/observed weight and full-support assumption. | E08 | math-block; use exact 2/3 in computations; empty cell cannot be invented by weighting. |
| S71 / 15 | Reductions Uses a Cost-Sensitive Oracle | Preserve existing saddle point, constraints, multiplier bound and tolerance definitions. | E10 | math-block; split symbol setup, objective and interpretation if necessary; no added convergence theorem. |
| S72 / 16 | Postprocessing Uses an Attainable Region | Preserve derived-predictor definition, convex hull and group-specific threshold/randomization relation. | E03 | math-block; retain exactly what predictor sees; diagrams, if used, must obey this region. |
| S73 / 17 | Compared to whom? | Existing closer names comparison and assumptions. | Lecture synthesis | end-slide; retained. |

## 4. Packages and ownership

Only slides implements. Package descriptions are editing boundaries, not an instruction to create more agents. They may be executed serially. All paths are repo-relative.

| Package | Slide ownership | Allowed content files / sections | Depends on |
|---|---|---|---|
| P1 | S04–S10, S74 | Main and matching note articles; own uniquely named figure assets under courses/trustworthy-ai/figs/lec12-visual-motivation/ | ID-only commit; E01,E02,E20,E21 |
| P2 | S12–S21 including specified splits | Main and matching note articles; criteria_examples.py and its generated assets in the same figure directory | P1 establishes decision language; E13/E14 are authoritative inputs |
| P3 | S23–S34 including splits | Main and matching notes; calibrated_errors.py and own figure assets | P2 rate vocabulary; E15 inputs |
| P4 | S36–S45, S75 including splits | Main and matching notes; reweighing.py, reductions_mix.py and own figure assets | P2 criteria; E08/E17 inputs |
| P5 | S47–S52 including splits | Main and matching notes; own figure assets | Existing audit sources; E21/E22 supplements |
| P6 | S54–S55 including split | Main and matching notes | P1 hook, P2 denominators, P4 intervention limits |
| P7 | S60–S64, S66–S68, S70–S72 | lec12tech.html corresponding sections | Exact main examples and existing formal sources |
| Integration (slides) | S01–S03,S11,S22,S35,S46,S53,S56; tech S57–S59,S65,S69,S73 | Shared surfaces below, plot_values.py for source-derived bars, job record | All packages |

Packages do not independently edit shared style, total counts, note TOC, other packages' figures or the outline. The integrator owns those. Generated-figure scripts are implemented by slides, not slides-review; record actual generator paths/inputs in work-r1 so evidence.md can be appended if paths change. Avoid modifying existing shared scripts or reference assets.

## 5. Shared surfaces and acceptance gates

1. **Branch / record:** create the named branch from the exact baseline, copy plan-v1.md unchanged into log/<job-id>/, refresh job.md/requests.md/evidence.md on every push. Report ID-only commit and final reviewed-work SHA; no PR or merge during implementation.
2. **Identity / mapping:** maintain main+note IDs through splits; every baseline S01–S73 maps to retained/split/moved content. New S74/S75 have explicit insertion positions. Work report gives ID | old page | new page | split/moved, including any additional splits. Notes have exactly one article per main slide in the same order.
3. **Shared design:** repair diagram label scale and arrow rendering locally for lec12 only. Audit every diagram, not merely p6 and p40. No edits to reference/, shared scripts/, other lectures, backups, or existing assets used by other decks. New local figure-generators in the allowlisted figure directory are in scope. Use standard components; type/density rules outrank the target count.
4. **Source fidelity:** all retained empirical numbers, plots and captions remain traceable. Prefer original figures; source-table bars retain exact values and cited table. Never invent curve data, remove uncertainty without disclosure, or paint over a legend. For each new calculated figure give inputs, parameters, reproducible code path and an illustrative label where applicable. E18 is not permission to recertify old legal claims.
5. **Notes / time:** preserve every relocated definition, full table, calculation and qualifier in its specified companion. Update title matches, minute allocations and elapsed times; total 90 minutes, no activities. Optional tech is not counted in the core. If the material cannot be taught in that budget, raise the issue rather than silently adding time.
6. **Outline:** update only lec12 entries in courses/trustworthy-ai/OUTLINE.md (lecture index, main section map, notes, supplement and relevant figures/pointers); synchronize all count surfaces. No curriculum-wide audience or unrelated lecture edits.
7. **Checks:** run applicable repository lint, outline/note/link validation; explain mechanical density warnings rather than treating lint as visual approval. Render all main pages and all technical pages once after integration. Inspect every page at slide size; include explicit p6/S06 and p40/S40-family arrow/label checks. Check newly cropped asset files directly as well as embedded renders. No clipped labels, arrows behind boxes, distorted figures, missing math, collisions or unreadable chart keys.
8. **Handoff:** work-r1.md must state packages completed, deviations, unresolved plan issues, unsourced facts, generator paths, exact commit and rendered pages. Pointer only. Review owner checks original request → sources → design rules → plan at that exact commit. Second round, if needed, is blockers only and changed pages plus neighbours. At two rounds, unresolved blockers escalate to Albert.
9. **Scope / final control:** Albert's later detailed revision remains separate. Only slides-review opens this job's PR after approval and pushed log-only follow-ups. Neither agent merges without Albert's direct order for that PR. No PDF is sent unless requested.
