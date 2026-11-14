# plan-v2 — incremental accuracy corrections

## What changed since plan-v1
The first review of `3150ed4ae9bc70f96da43e5cc68837b38d646ef6` found that the new two-layer architecture works, but several inherited seeds, new summaries and retained Scripts overstate guarantees or misread exhibits. **Replace only the affected claims below.** `plan-v1.md` remains the base specification for all other entries; its 902-row inventory is not reproduced or reauthorized as fact. `review-r1.md` is incorporated for each finding's exact correction, location and source limits. Where an old seed conflicts with a corrected source-backed claim, this version wins.

No new deck argument, title sequence, figures, slides, activity, teaching time, research survey or supplement work. Keep the existing concept-first undergraduate audience and the full detail/reference layer. Proposed main and article titles remain unchanged for every row. Layout stays the existing companion; no markup, CSS, pixel or font prescription. These are content decisions, **[judgment]** for slides to implement contextually.

## Coverage
| Comment | Baseline / current pages | IDs | Packages / acceptance |
|---|---|---|---|
| C01 | All 902 pages, unchanged mapping in plan-v1 | All lec01–lec12 IDs | P1–P12; preserve counts/order/pairing |
| C02 | Listed affected pages below | Correction map below | Replace inaccurate openings/exhibit readings and inconsistent retained repetitions; keep detail |
| C03 | Entire job | All IDs | Per-package durable checkpoints; confirmed capacity limits only; no model/account bypass |
| C04 | Source/plot-sensitive corrected entries | Findings' listed IDs | Recheck the actual exhibit and primary-source locator; record bounded checks |

## Common acceptance and scope
- **Must:** implement all 61 blocking findings in `review-r1.md`. The accuracy seeds below state the corrected point; the referenced F item supplies required qualifiers, exact changes and exhibit interpretation. E references resolve to `evidence.md` with the source URL/version/locator. Sources, not this plan, establish facts.
- **Must:** apply each correction throughout its article, including retained Script and repeated technical/case-background text. Keep valid derivations, caveats and provenance; do not delete detail simply to remove contradictions.
- **Must:** main content remains unchanged. Notes explicitly identify inherited main shorthand where necessary and work-r2 inventories those main discrepancies. This overrides any reading of plan-v1 that would require a note to endorse a main-slide error. Main corrections require a separate scope decision.
- **Must:** keep current titles, page/ID mapping, exhibited figures and pacing. Source updates are targeted; dated snapshots remain dated. Reuse existing definitions/notation instead of starting a new explanation sequence.
- **Prefer:** F55/F57/F64/F65; slides may decline them with a brief reason. All other optional checkpoint suggestions were dropped from this work order, not silently promoted to requirements.
- **Slides decides:** exact concise wording and supporting-material organization. A necessary qualifier stays in the opening; the detailed derivation/source stays underneath. No automatic new round for preferences.

## Accuracy seed overrides and source register
Each row is **must** unless marked optional. Full required correction and exhibit-reading acceptance are the same-numbered item in `review-r1.md`. No slide-title change. For findings spanning multiple entries, apply only the clause relevant to that entry and align callbacks; the per-entry map below resolves ownership.

| Finding | Corrected point to communicate | Evidence / source basis | Priority |
|---|---|---|---|
| F01 | Physical application of RP2 follows white-box optimization; a printer-only deployment is not a black-box attack. | E14 | must |
| F02 | Korean Article 35 requires an endeavor to assess impacts; other scoped high-impact duties include supported human oversight. | E15, E78 | must |
| F03 | Post-processing preserves a guarantee but is not a converse; later filtering cannot retract an already disclosed artifact. | E16, E17 | must |
| F04 | At 171 cm the illustrative posterior is about 51%; about 54% is average Bayes accuracy. | E17 | must |
| F05 | DP bounds the record's incremental evidence, not all attribute inference from correlations. | E16 | must |
| F06 | Approximate DP is an additive event-probability guarantee, not generally pure DP with probability 1−delta. | E16, E30 | must |
| F07 | Randomized response yields a debiased estimate, not exact knowledge of the population rate. | E17 | must |
| F08 | DP-SGD scaling depends on the single-sample/batch, clipping, steps and normalization setup; relative error differs from absolute noise. | E30 | must |
| F09 | Large epsilon weakens a worst-case bound rather than proving leakage; qualify randomization, historical comparisons and advantage claims. | E16/E30 and the reviewed article's historical-source limits | must |
| F10 | Blocking a prompt or changing alignment does not establish erasure; parameter invariance or post-patch persistence was not measured. | E22 | must |
| F11 | COMPAS uses recorded rearrest; cutoff PPV, score calibration and nondegenerate impossibility conditions are different. | E18, E71 | must |
| F12 | An empirical audit lower bound needs simultaneous confidence, fixed delta and valid denominators; it does not automatically certify a code bug. | E29 | must |
| F13 | Membership can reveal a diagnosis only when the cohort's inclusion criteria support that inference. | E28 | must |
| F14 | Yeom's exact gap identity uses the randomized bounded-loss adversary, not every fixed-threshold attack. | E19 | must |
| F15 | A likelihood ratio is evidence under IN versus OUT, not a posterior without prior odds. | E30 | must |
| F16 | Separate the main C4 experiment from the deduplicated comparison; observed LiRA instability is not optimal-test impossibility. | E20 | must |
| F17 | Random canaries make accidental matches unlikely under a null, not impossible. | E21 | must |
| F18 | Repeated exposure/duplication is not the same intervention as more unique data. | E23, E27 | must |
| F19 | Deduplication worsens the overlap-heavy C4 Duplicates perplexity row; the emission headline and bar ratio are different metrics. | E24 | must |
| F20 | DP bounds incremental emission/influence, not zero memorization; exact and approximate matching bars have different rates. | E16, E27 | must |
| F21 | Conformal false-positive control conditions on a fresh matched non-member, not on an already flagged member. | E25 | must |
| F22 | The k-CBS setup uses 20 samples and about 10 times greedy token evaluations, not a universal 20-times runtime claim. | E26 | must |
| F23 | Extraction percentages require the normalized sampling rule, prefix access and explicit probability thresholds. | E23, E26 | must |
| F24 | Random data plateau at capacity; natural-text generalization is a separate experiment, not a consequence visible in the random plot. | E27 | must |
| F25 | DP supplies necessary ROC outer bounds; one inequality is not the exact attainable region, and a loose bound can become vacuous. | E16 | must |
| F26 | Single answers or membership flags do not prove forgetting success/failure; calibrated comparisons and adaptation budgets matter. | E33, E34, E85 | must |
| F27 | Approximate unlearning can be certified; heuristic large-model edits do not automatically establish a distance bound. | E33 | must |
| F28 | Implicit Hessian-vector products avoid dense storage, while computation and nonconvex validity remain challenges. | E32 | must |
| F29 | Filtering, learned refusal and deletion are different; bypass and relearning claims depend on access and the retrained reference. | E33 | must |
| F30 | The 21%→83% quantization headline is an aggregate benchmark result over constrained methods, not one model's measured stored knowledge. | E35 | must |
| F31 | Relearning results depend on method and data; the near-chance RMU–Wikitext curve is an important exception. | E36 | must |
| F32 | Zero binned empirical ECE is not a certificate of population calibration. | E37 | must |
| F33 | Coverage close to nominal does not bound prediction-set size or efficiency. | E37 | must |
| F34 | Consistency and semantic entropy are confabulation cues, not truth tests; retain the source-supported estimator description. | E40, E82 | must |
| F35 | A fixed training cutoff gives no automatic reliable freshness detector, but uncertainty disclosure and supplied context remain possible. | Our logical counterexample in F35; reviewed S22 support-mismatch setup, not a new empirical result | must |
| F36 | The PersonQA model comparison is not a causal ablation of reasoning; distinguish the authors' model-specific explanations. | E38 | must |
| F37 | Historical TruthfulQA size trends are not monotone in every family; UnifiedQA has a visible exception. | E39 | must |
| F38 | Direct monitor optimization defeats a reliability guarantee, not necessarily every monitor; distinguish monitor inputs and total cheating. | E45 | must |
| F39 | AlwaysEqual is one example among three available shortcuts; the plotted hack rate aggregates them. | E44 | must |
| F40 | PGD approximately solves the inner maximum; it does not certify finding the worst perturbation. | E46 | must |
| F41 | Robust accuracy requires a correct center and all allowed perturbations; surviving AutoAttack is an empirical upper-bound estimate. | E47 | must |
| F42 | The reconstructed July 9–13 campaign includes external staging; intrusion inside Hugging Face begins July 11. | E50 | must |
| F43 | Hint disclosure uses a chance-corrected normalized estimate and acknowledgment of causal use, not direct access to inner reasoning. | E51 | must |
| F44 | Data-control cost curves vary by dataset and attainable share; do not invent common endpoints. | E55 | must |
| F45 | Llama-2 is open-weight even when used as a black-box transfer target. | E59 | must |
| F46 | Later KL is lower, not zero; the plot summarizes a harmful-prefix dataset, not one reply. | E58 | must |
| F47 | The fitted power laws concern NLL or negative-log ASR; distinguish the separate panels' tasks. | E60 | must |
| F48 | Circuit breakers were tested against target-aware attacks; the result is not a guarantee against stronger tuning. | E61 | must |
| F49 | Published prompts are cheap to copy, not guaranteed to work for everyone; online age is not continuous efficacy. | E62 | must |
| F50 | A length-sensitive score change does not establish safer output or constant underlying harm. | E63 | must |
| F51 | The reported GCG average selects the three highest-ASR runs from ten optimization trials. | E58 | must |
| F52 | Small full-text TV implies the detector bound; looking human does not establish small TV. | E67 | must |
| F53 | The EU transition applies to systems placed on the market before August 2, 2026, with December 2, 2026 as the compliance deadline. | E69 | must |
| F54 | Removing group attributes from model inputs need not remove them from separate audit data. | E75 | must |
| F55 | With the stated two-score selection rule, calibration implies equal PPV, not conversely. | E71 | optional |
| F56 | Fig. 4 concerns transformed evaluation data; training-cell parity and held-out residuals are compatible, with exact generator unrecovered. | E77 | must |
| F57 | At fixed TPR/FPR, lower prevalence raises the false-discovery fraction, not necessarily the count of false flags. | E75 | optional |
| F58 | Keep the historical Italian fine and March 2026 first-instance annulment distinct from unverified later appeals. | E78 | must |
| F59 | Compute–noise–release is an additive-mechanism recipe, not a definition of every DP mechanism. | E16, E85 | must |
| F60 | Statistically supported attack advantage is evidence of leakage; one predicted member can be a false positive. | E85 | must |
| F61 | The unlearning proof needs retained-objective smoothness, bounded-gradient scope, fixed retrainer normalization and matching Gaussian noise distributions. | E81 | must |
| F62 | Arbitrary-fact theorems need their partition and calibration assumptions; they do not supply empirical floors for real citation/biography datasets. | E83 | must |
| F63 | Read the NPO gradient exception and the forest plot's posterior medians, credible intervals and 50% neutral point. | E41, E42 | must |
| F65 | Optional citation, provenance and spoken-cue normalization must match the current artifact. | E42, E71, E84 | optional |

## Per-entry specifications and package ownership
Each entry below inherits the corrected point(s), required qualifiers, exhibit and source treatment of its listed F rows. Acceptance: the short message expresses that corrected point, the next explanation reads the existing exhibit correctly, and retained detail no longer contradicts either. Main and article titles shown here are existing titles, not retitle instructions. All material stays in the paired note; no transfer to the main or tech supplement. Time remains unchanged.

### P1 — `courses/trustworthy-ai/lec01-introduction-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec01/S08 / p8 | Bias in the Courtroom | F11 |
| lec01/S12 / p12 | "Repeat the Word Poem Forever" | F10 |
| lec01/S13 / p13 | Your Prompts Are Data Too | F58 |
| lec01/S19 / p19 | Stickers on a Stop Sign | F01 |
| lec01/S31 / p31 | The Rules Are Arriving | F02 |
| lec01/S34 / p34 | Software vs Learned Models | F10 |
| lec01/S40 / p40 | No Threat Model, No Answer | F01 |
| lec01/S44 / p44 | The Goal | F01 |

### P2 — `courses/trustworthy-ai/lec02-privacy-dp-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec02/S03 / p3 | Where This Lecture Sits | F03 |
| lec02/S09 / p9 | Make ChatGPT Leak | F10 |
| lec02/S17 / p17 | Membership Inference | F60 |
| lec02/S20 / p20 | Regulators Step In | F10 |
| lec02/S29 / p29 | A Warm-Up: Guess the Nationality | F04 |
| lec02/S30 / p30 | Randomness Is Required | F09 |
| lec02/S32 / p32 | In Plain Words | F06 |
| lec02/S33 / p33 | Reading $\varepsilon$ | F09 |
| lec02/S36 / p36 | What $\varepsilon$ Does NOT Mean | F09 |
| lec02/S38 / p38 | What "Look Alike" Really Means | F09 |
| lec02/S39 / p39 | Overlap Is Privacy | F06 |
| lec02/S40 / p40 | What DP Gives and Doesn't | F09 |
| lec02/S41 / p41 | Individuals, Not the Crowd | F05 |
| lec02/S43 / p43 | The Recipe | F59 |
| lec02/S46 / p46 | Recovering the Truth | F07 |
| lec02/S56 / p56 | The Utility Cost | F09 |
| lec02/S57 / p57 | More Data Helps | F08 |
| lec02/S62 / p62 | Auditing Privacy | F12 |
| lec02/S68 / p68 | Key Takeaways | F09 |

### P3 — `courses/trustworthy-ai/lec03-mia-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec03/S08 / p8 | When Membership Is the Secret | F13 |
| lec03/S28 / p28 | A Theory Anchor | F14 |
| lec03/S39 / p39 | Two In-vs-Out Bells | F15 |
| lec03/S43 / p43 | AUC and Its Blind Spot | F15 |
| lec03/S47 / p47 | Does LiRA Work on LLMs? | F16 |
| lec03/S49 / p49 | DP Caps the Attacker | F25 |
| lec03/S50 / p50 | A Concrete Bound | F25 |
| lec03/S51 / p51 | Auditing Flips the Attack | F12 |
| lec03/S59 / p59 | Give the Attack Everything | F16 |

### P4 — `courses/trustworthy-ai/lec04-memorization-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec04/S13 / p13 | The Canary | F17 |
| lec04/S23 / p23 | The "Repeat Forever" Attack | F10 |
| lec04/S26 / p26 | Patched, Not Solved | F10 |
| lec04/S31 / p31 | Bigger Means More | F23 |
| lec04/S36 / p36 | The Uncomfortable Trend | F18 |
| lec04/S50 / p50 | Deduplication | F19 |
| lec04/S53 / p53 | Differential Privacy | F20 |
| lec04/S56 / p56 | Frontier: Whole Books Come Back | F23 |
| lec04/S58 / p58 | Frontier: Near-Verbatim Counts Too | F22, F23 |
| lec04/S59 / p59 | Frontier: Extraction Needs a Control Group | F21 |
| lec04/S60 / p60 | Frontier: How Much Fits? | F24 |

### P5 — `courses/trustworthy-ai/lec05-unlearning-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec05/S09 / p9 | Why Not Just Ignore It | F26 |
| lec05/S18 / p18 | Approximate Unlearning | F27 |
| lec05/S29 / p29 | Can We Edit the Weights? | F61 |
| lec05/S30 / p30 | Influence Functions | F61 |
| lec05/S31 / p31 | The Catch: Curvature | F28 |
| lec05/S33 / p33 | Ascent Can Wreck the Model | F65 (optional) |
| lec05/S39 / p39 | Who's Harry Potter? | F26 |
| lec05/S43 / p43 | Why Fictitious? | F26 |
| lec05/S48 / p48 | Unlearning vs Filtering | F29 |
| lec05/S50 / p50 | Verification Is Hard | F27 |
| lec05/S51 / p51 | Audit With Membership Inference | F26 |
| lec05/S52 / p52 | The Tell Persists | F26 |
| lec05/S55 / p55 | Relearning Attacks | F26, F63 |
| lec05/S56 / p56 | Quantize, and It Comes Back | F30 |
| lec05/S61 / p61 | What Guarantee Holds? | F26, F29 |
| lec05/S62 / p62 | Robust Unlearning | F31 |
| lec05/S64 / p64 | Unlearning Meets Privacy | F61 |

### P6 — `courses/trustworthy-ai/lec06-hallucination-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec06/S14 / p14 | No Truth Grounding | F62 |
| lec06/S17 / p17 | Plausible Beats True | F62 |
| lec06/S21 / p21 | Where Errors Concentrate | F62 |
| lec06/S22 / p22 | The Knowledge Cutoff | F35 |
| lec06/S28 / p28 | Measuring the Gap | F32 |
| lec06/S45 / p45 | The Coverage Theorem | F33 |
| lec06/S55 / p55 | Self-Consistency | F34 |
| lec06/S56 / p56 | Semantic Entropy | F34 |
| lec06/S57 / p57 | The Entropy Picture | F34 |
| lec06/S67 / p67 | TruthfulQA: Baiting the Model | F37 |
| lec06/S69 / p69 | Measuring Faithfulness: Vectara HHEM | F65 (optional) |
| lec06/S70 / p70 | Reasoning Models Hallucinate Too | F36 |
| lec06/S71 / p71 | Sycophancy: Agreeing Over Truth | F63 |

### P7 — `courses/trustworthy-ai/lec07-alignment-failures-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec07/S08 / p8 | 8. 2026: A Test Agent Broke Into Hugging Face | F42 |
| lec07/S47 / p47 | 47. Study 2 · One Hack, Concretely | F39 |
| lec07/S65 / p65 | 65. Disclosed Hint Use: Under 40% on Average | F43 |
| lec07/S67 / p67 | 67. Penalizing "Bad Thoughts" Taught Hiding | F38 |
| lec07/S68 / p68 | 68. What Monitoring Can and Cannot Show | F38 |

### P8 — `courses/trustworthy-ai/lec08-adversarial-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec08/S54 / p54 | 54. Start From One Test Image | F41 |
| lec08/S64 / p64 | 64. Adversarial Training: Train on the Worst Case | F40 |
| lec08/S66 / p66 | 66. More Robust Training, Lower Clean Accuracy | F65 (optional) |
| lec08/S71 / p71 | 71. AutoAttack: Four Attacks, Nothing to Tune | F41 |

### P9 — `courses/trustworthy-ai/lec09-poisoning-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec09/S50 / p50 | 50. An Estimated $60/Year Could Control 0.01% of LAION-400M | F44 |

### P10 — `courses/trustworthy-ai/lec10-jailbreak-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec10/S05 / p5 | 5. Why Getting Around Refusal Matters | F49 |
| lec10/S06 / p6 | 6. Jailbreak Prompts Are Shared and Last for Months | F49 |
| lec10/S22 / p22 | 22. Safety Training Changed Mostly the First Few Tokens | F46 |
| lec10/S25 / p25 | 25. Training on Recovery Examples Deepened Refusal | F51 |
| lec10/S36 / p36 | 36. One Suffix Optimized on Open Models Transferred | F45 |
| lec10/S49 / p49 | 49. Harmful Responses Rose With the Number of Shots | F47 |
| lec10/S52 / p52 | 52. Best-of-N Success Followed a Power Law in N | F47 |
| lec10/S60 / p60 | 60. Section 05 — Evaluation and Defenses | F65 (optional) |
| lec10/S64 / p64 | 64. Even Response Length Moves the Score | F50 |
| lec10/S74 / p74 | 74. Circuit Breakers Cut Reported ASR, Kept Capability | F48 |

### P11 — `courses/trustworthy-ai/lec11-synthetic-media-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec11/S34 / p34 | 34. If AI Text Looks Human, Every Detector Is Near a Coin Flip | F52 |
| lec11/S67 / p67 | 67. EU Law Now Expects a Watermark in Chatbot Text | F53 |
| lec11/S73 / p73 | 73. Takeaways | F57 (optional) |

### P12 — `courses/trustworthy-ai/lec12-fairness-note.html`

| Slide ID / unchanged page | Existing title | Required finding(s) / seed override |
|---|---|---|
| lec12/S10 / p13 | 13. Dropping a Column Can Leave Information | F54 |
| lec12/S17a / p23 | 23. Equalized Odds Needs a Shared Attainable Point | F65 (optional) |
| lec12/S17b / p24 | 24. Equal Opportunity Only Matches Height | F65 (optional) |
| lec12/S19b / p27 | 27. Calibration Does Not Fix Cutoff Precision | F55 (optional), F65 (optional) |
| lec12/S20b / p29 | 29. Score Meaning Is Not Selection Precision | F65 (optional) |
| lec12/S23a / p33 | 33. What COMPAS Scores Do | F65 (optional) |
| lec12/S25 / p36 | 36. The FPR Gap Remains Even Without Priors | F65 (optional) |
| lec12/S26a / p37 | 37. At the Same Decile, Outcomes Are Broadly Similar | F65 (optional) |
| lec12/S26b / p38 | 38. At Cutoff 4, Precision Is Roughly Similar | F65 (optional) |
| lec12/S30 / p42 | 42. Three Equalities Can Conflict | F65 (optional) |
| lec12/S39a / p52 | 52. Reweighing Moves Data Parity Difference Toward 0 | F56 |
| lec12/S39b / p53 | 53. Disparate Impact of the Same Data Moves Toward 1 | F56 |

## Decisions on all work-r1 plan issues
These decisions close the questions; none authorizes main-deck changes.

| Issue | Decision and rationale | Disposition |
|---|---|---|
| 1 — lec01 S42/S02 topic map | Preserve the visible fourteen-topic historical map, not a one-to-one current timetable. The existing explanation acknowledges the mismatch. Prefer S42's message: “The slide groups fourteen topic areas into four layers; it is not the current lecture timetable.” S02 counts topic boxes, not fourteen future lectures. Do not invent lec15 or promote backups to taught lectures. | Accepted with optional wording; no added blocker |
| 2 — lec01 S05 missing cases | The note already says four of six domains receive cases and identifies lending/healthcare as absent. | Accepted; add no case or time |
| 3 — lec02 S56/S30/S68/S11 shorthand | New readings correctly qualify historical benchmark, non-constant mechanism, protected-unit advantage and documented Stripe test keys. Retained Scripts at S30/S56/S68 still need alignment under F09. | F09 required; S11 accepted; main wording deferred |
| 4 — lec03 S68 incident strip | Reading explains the strip and question cards; retained model answers cover the six actual questions. | Accepted; no new activity |
| 5 — lec04 S42 figure/dataset | The note correctly separates Fig. 5(c) from the Stable Diffusion 12M search. Prefer calling 1.88% a similarity>0.5 copy-detection proxy rather than verified duplicates. | Existing separation accepted; qualifier optional; main caption deferred |
| 6 — lec04 S50 10× versus 5× | The source's unprompted-emission headline and the displayed training-duplicate bar ratio are different. Explain that and the C4 Duplicates perplexity exception. | F19 required |
| 7 — lec05 S23/S12 | Existing explanation makes “useless” a per-request compute tradeoff and regulatory pressure context rather than chart causation. | Accepted; main rhetoric deferred |
| 8 — lec07 S74 | Shared shape is explicitly distinguished from one demonstrated cause. | Accepted; no new cause claim |
| 9 — lec08 S35 | The reading already attributes the transfer interpretation to Ilyas et al. | Accepted; no new blocker |
| 10 — lec09 S26 | Original Poison Frogs Fig. 6(a) is the spam schematic, verified in E54. The corrected note describes the actual image. | Accepted; no figure-number repair |
| 11 — lec09 S90/S87/S81 | Four closing questions need not duplicate the five-item full checklist; clean accuracy is included in the takeaways. S81's note is independently intelligible despite main cross-reference shorthand. | Accepted; no main/count change |
| 12 — lec10 S60 | Keep the existing 17.5-minute schedule. “Twenty minutes” may become “This section,” not a new pacing decision. | Optional F65(6); no timing change |

## Other reported flags: resolved decisions
- **lec03 repair:** mathematics at S66 accepted. The “verbatim from 9a772bd” provenance/location is not established; correct the record in work-r2 or identify the actual source (optional F64). Frozen work-r1 must not be edited.
- **lec03 C4:** F16 corrects the main-versus-deduplicated experiment distinction (E20).
- **lec04 book sources:** preprint 2025 and conference COLM 2026 can coexist; use the displayed figure's version (E31). Bartz's 3:/4: prefixes coexist on the signed order and are not a blocker (E79). Local (n,q)/(n,p) notation is acceptable when defined. The displayed 120M tick versus paper's 125M model is not alone a blocker. One-insertion exposure is measurable, not maximum; keep that interpretation (E21/E23). Sample-cost and probability-threshold corrections are F22/F23.
- **lec05:** Kurmanji source addition optional F65; TMLR 2025 verified (E36/E42). SISA reference convention accepted. Keep qualified erasure/legal discussion (E80); no current-law expansion. Course-derived mathematics is identified as our calculation, with F61 supplying missing hypotheses.
- **lec06:** the worked prediction set {1,4} already exists. IDK's zero payoff is a relative incentive against wrong answers, not an error. Kuhn 2023 and Farquhar 2024 are separated in Reading. Methods supports the retained semantic-entropy estimator/LLN attribution (E82); do not invent a blocker there. Vectara's six dated rows are verified (E84), with a pinned citation optional F65. Main S07's currency sign is outside scope; no new math-render regression was found in notes.
- **lec07:** RE-Bench/METR footnote checked (E52); the different-run transcript at S51 is already disclosed. Keep these caveats.
- **lec08:** the duplicate compute paragraph is optional F65; Cohen's table discrepancy is correctly disclosed and the chosen table is supported (E49). No current RobustBench-rank claim is authorized by its historical snapshot.
- **lec11–12 law:** retain dated, scoped source checks. Korean named oversight is supported; Article 35's endeavor language still needs F02. Bartz status and the retained Korean/Colorado comparison are supported by the checked records, not a blanket legal compliance audit. EU transition eligibility/deadline needs F53.
- **lec12:** locator/provenance cleanups are optional F65; F56 is required but the exact historical Fig. 4 generator remains unrecovered. Preserve this uncertainty and the §10/Appendix B source-based interpretation; return contrary primary evidence rather than guess.

## Packages, dependencies and shared surfaces
- P1–P12 retain their plan-v1 ownership: only their named canonical note file. Packages may read each other's entries but must not edit them. No fresh ID-only commit, retitling or splitting is needed. Nonlisted entries remain unchanged except a necessary linked repetition reported in work-r2.
- Coordinate F10 across P1/P2/P4 and F12 across P2/P3; F26/F29 and F34/F62 must use consistent terminology. P5/P6 share F63's plot-reading standard but independent exhibits. Integrate these cross-package terms before reporting work-r2.
- Shared owner integration: update only affected leaf OUTLINE descriptions/pointers, preserve all counts/core paths and auxiliaries, run mapping/link/math/lint checks, and report actual browser-inspected changed entries and neighbours. Do not rewrite unrelated OUTLINE history.
- Source or argument disagreement returns to slides-review with the evidence; do not force a correction unsupported by the original source. No speculative fix to satisfy a plan.

## Round-2 acceptance / handoff
1. All 61 blockers either corrected as specified or returned with contrary primary evidence for a decision; each F01–F65 receives a disposition in work-r2. Nonblocking declines are permitted.
2. The changed entries and immediate neighbours remain clear, consistent and fully paired; keep all 902 ordered IDs/titles and pacing. Review the entire changed article, not just its Message.
3. Existing note lint, links/anchors and KaTeX pass; browser-check changed plot/math-heavy entries and neighbouring reading flow. Separate inherited overflow from new regressions; do not shrink type to clear either.
4. Per-package commits/checkpoints; integrate and push with a work-r2 pointer naming the exact SHA. Copy the frozen review-r1/plan-v2 unchanged into the tracked record and refresh living job/requests/evidence files. Only slides writes tracked records.
5. State returns to in-review on that pointer; round 2 of 2 is the final ordinary review. Remaining blockers are escalated to Albert, not automatically sent into round 3. PR only after approval and pushed records; never merge without Albert's direct order.
