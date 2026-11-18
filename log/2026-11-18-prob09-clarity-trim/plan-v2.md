# plan-v2 — Executable work order

## What changed since plan-v1

1. **C13 is authoritative:** Albert says the lecture can be shorter and pacing need not constrain it. The120/150-minute budgets, per-part allocations, split-session suggestion and pace lines are withdrawn. **No fixed duration and no minimum slide count.** Time in every specification below means “not budgeted, by author instruction.” Do not add material to fill a slot.
2. Proceed with the five-part MC/IS-focused scope and the existing **PR77** branch. This is the same still-open authored change, not a second competing PR. No merge authorization.
3. Prefer **two** rare-event teaching slides, S116a/b, instead of three. The secondary spread-versus-probability plot moves to S116b's notes, preserving its precise reading. Proposed S116c was never allocated and is not needed. The resulting illustrative sequence has70slides, **not a target to fill or a cap**. Additional clarity-driven splits remain allowed; no compression of type or loss of necessary conditions.
4. Correct the plan-v1 section boundary description: S54 is the last content slide of Part02; **S55** begins Part03. No source move is required for that correction.
5. This version supplies the complete per-ID disposition, scoped packages, main/notes allocation and acceptance checks. It supersedes plan-v1 wherever they differ.

## Job and build contract

- Job: **2026-11-18-prob09-clarity-trim**; large; round1 of up to3 review rounds for these new author requests.
- Exact baseline: **5f4b1d99c5d799785752aa12c494715c3b21327b**,86slides. All author page references below point here, not to moving main.
- Branch: **2026-11-17-prob09-major-revision**, existing PR77. Fresh REST check after C13: open, unmerged, same baseline head. Continue that branch; do not create another PR or reset onto main. Report a changed head/parallel author edits before overwriting anything.
- Inherited ID commit: **c47b198f8e8d0153fee6923ce2dafe8b13f4fe77**. No setup or ID-migration commits needed. New slides use S130–S133, splits use S116a/b, S63a/b, S69a/b; never renumber old IDs.
- Deck **D**: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`.
- HTML notes **H**: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`.
- Accessible notes **M**: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`.
- Other allowed surfaces: local `courses/deepmath/prob09-monte-carlo/fig/` and `gen/`; `courses/deepmath/OUTLINE.md`; narrowly necessary stale prob09 pointers in root `OUTLINE.md`; new job's tracked record `log/2026-11-18-prob09-clarity-trim/` copied unchanged from the owner folder.
- Do not edit prior decks, prior frozen job records, global design rules, `reference/`, shared scripts or unrelated course content. No PDF delivery requested. slides owns all source/commit work; owner only plans and reviews.

## Audience, argument and continuity

Rigorous, example-led Deepmath lecture for junior undergraduate AI majors. **No pacing constraint.** The argument remains: familiar ML expectations → MC sampling error → correct a changed sampler → examine contribution variance → cancel an unknown normalizer → reuse RL policy data responsibly. Differentiation of expectations is no longer a learning objective.

Reuse, not re-derive: one-hot CE/KL from prob02; expectation and LOTUS; sample-mean variance/LLN/CLT from prob05; rescaled bounded Hoeffding from prob06; Bayes/likelihood from prob07; scalar Gaussian prior from prob08. Named facts return as self-contained recalls when used. The current course leaf and source statements were checked in E01. Root pointers and the math-deck exemplar were consulted; the existing rigorous proof rhythm stays. No frontier survey, MCMC, QMC, new gradient chapter or PPO derivation.

## Coverage table

All numbered items below are self-contained judgments for slides. Baseline page and stable ID locate the change; source line numbers are deliberately omitted from the slide plan per PLANNER_BRIEF. Both H/M change with D.

| Comment | Baseline page / title / ID | Proposed treatment and reason | Evidence | Package |
|---|---|---|---|---|
| C01 | Opening pp3–4, S03/S04 | [judgment] After S03, add a one-hot CE/KL recall and a population-loss-to-sample-average example; make S04 a concrete sampled-generation evaluation. Identify data samples versus model samples. Motivation is why an expectation must be computed, not another KL proof. | E01/E02/E09 | P1 |
| C02 | p10, Estimating the Error Bar, S114 | Expand SE to **standard error** and define it as the SD of the estimator across repeated samples. Distinguish it from outcome SD and actual error; show estimated SE with its sampling/variance conditions. | E03 | P1 |
| C03 | p13 The Rate Is Not the Cost, S33; p14 Tensor Grids Grow With Dimension, S37 | Delete both slides and their active companion entries. Remove cross-references rather than relocating the detour. | Author decision | P1/I |
| C04 | p15 Rare Events Need Relative Error, S116 | [judgment] Use two main-slide steps: a concrete rare-event miss, then relative RMSE/expected hits. Move the existing trend plot to the second note instead of adding a third slide. Explain absolute versus relative error before formulas; retain the later exponential example as the applied IS thread. | E03 | P1 |
| C05 | p27 More Tail Visits, Corrected Weights, S118 | Name f(x)w(x) as **one weighted contribution** and mu as the **target mean**. Explain the horizontal line and averaging under q; more tail hits alone do not prove lower variance. | E04 | P2 |
| C06 | p33 Follow the Weighted Integrand, S57 | [judgment] Make the single message “sample where contributions matter.” Emphasize p versus the two-lobed absolute weighted integrand; move the secondary signed curve/derivation to the notes. Preserve the signed-integrand limitation. | E04 | P2 |
| C07 | p37 One-Sign Integrands Permit Zero Variance, S63 | [judgment] Split intuition and identity: random X values can map to identical Y=f(X)w(X); therefore the estimator has zero variance. Retain the one-sign assumption and immediately adjacent oracle-normalizer limitation. Distinguish true zero variance from zero empirical spread after no rare hits. | E05 | P2 |
| C08 | p42 Check the Integrand, Not Just Weights, S69 | [judgment] Separate the helpful heavy-tail example from the rule. Explicit answer: **q need not always be heavier-tailed than p**. A lighter Exp(1.5) proposal still has finite variance; coverage and the f-dependent second moment are the checks. | E06 | P2 |
| C09 | p44 The Target Is Known Up to Z, S73 | [judgment] Introduce a logistic-normal Bayesian posterior just before S73; return to it after normalization to compute a posterior predictive probability with likelihood weights and no Z. | E07 | P3 |
| C10 | p48 The Ratio Converges to the Target, S77 | Replace “Iid” with “IID”; standardize this acronym in touched deck/notes text. Preserve existing convergence assumptions and finite-sample bias caveat. | E01 / existing reviewed result | P3 |
| C11 | pp55–74, S83–S128 in baseline order; p85 S109b | Delete the gradient chapter and its recap; remove promises, stale bridges and gradient-only note/outline content. Do not delete unrelated IS theorems or their assumptions. | Author decision | I |
| C12 | pp75–83, S99/S100/S101/S102/S103/S129/S105/S106/S104 | [judgment] Preserve and renumber as Part05: old-policy reuse, sequence ratios, mismatch, behavior/reference roles, KL and clipping limitations. Rewrite S106 as an objective-estimation application, not a gradient toolkit. Briefly explain advantage without restoring the removed chapter. | E08 | P4 |
| C13 | Scope/pacing proposal, message36 | No duration target, no minimum slide count, no padding. Prefer two rare-event steps with the secondary trend in notes; preserve required explanations. | Author decision | all / I |

## Execution defaults applying to every per-ID specification

- **Must:** preserve the point, mathematical assumptions and direct answer to Albert on the main slide. Necessary qualifiers do not migrate off the slide to save space. A new split gets a point of its own.
- **Prefer:** the title and exhibit described below. **slides decides:** exact layout and implementation using existing DS components. Suggested components are vocabulary only, never CSS/markup/pixel mandates. Every entry's time is **not budgeted (C13)**.
- **H/M allocation for every entry:** short Message first, then plain explanation, then Details/Sources. Define every plotted quantity; explain axes, encodings, result and limit. Mirror meanings/order/IDs in the standalone ASCII Markdown, not just source links. M describes images in words. Unchanged paired notes stay intact except for stale links, pace text and chapter dependencies.
- **No tech supplement:** use H/M for secondary algebra and plots. Author-deleted whole topics are removed from active companions rather than turned into a hidden gradient chapter. Git preserves history.
- **Universal acceptance:** point visible; main, Message, explanation, details, caption and accessibility text agree; arithmetic/source locator verified; default type and component capacity respected; no clipping, overlap, false plot geometry or unreadable labels in actual render. Required questions are answered on-slide, not just in notes.
- **Retain entries:** keep the reviewed baseline claim/exhibit and its full qualifiers; do not gratuitously redesign unaffected material. Their per-ID line below still gives the message, exhibit, evidence and specific acceptance. Their existing H/M allocation and component choices are the suggested layout.
- Evidence **E##** means this job's `evidence.md`. **B##** means the prior job's entry E## in `log/2026-11-17-prob09-major-revision/evidence.md` **at baseline5f4b1d9** (URLs and exact locators there). B22 supersedes the older B10 locator. E04 records the Ch9 re-fetch limitation; do not claim it was freshly retrieved.

## Complete sequence / baseline trail

Positions are provisional and never used as edit keys. Each baseline ID is either retained, split or explicitly retired below. There is no requirement to hit70slides.

| Proposed position | ID | Baseline page | Baseline title | Proposed title | Package |
|---:|---|---|---|---|---|
| 1 | S01 | 1 | Monte Carlo &Importance Sampling | Monte Carlo & Importance Sampling | I |
| 2 | S02 | 2 | Contents | Contents | I |
| 3 | S03 | 3 | Estimate an Expectation | Estimate an Expectation | I |
| 4 | S130 | new after S03 | new | One-Hot Cross-Entropy Equals KL | P1 |
| 5 | S131 | new after S130 | new | Population Loss Requires an Average | P1 |
| 6 | S04 | 4 | A Known Model, a Hard Average | Sampled Replies Estimate Pass Rate | P1 |
| 7 | S06 | 5 | Sample, Evaluate, Average | Sample, Evaluate, Average | P1 |
| 8 | S26 | 6 | Six Points Illustrate the Recipe | Six Points Illustrate the Recipe | P1 |
| 9 | S16 | 7 | Monte Carlo Reuses the Sample Mean | Monte Carlo Reuses the Sample Mean | P1 |
| 10 | S19 | 8 | Unbiased Does Not Mean Accurate | Unbiased Does Not Mean Accurate | P1 |
| 11 | S22 | 9 | Averaging Reduces RMSE | Averaging Reduces RMSE | P1 |
| 12 | S114 | 10 | Estimating the Error Bar | SE Measures Estimator Spread | P1 |
| 13 | S115 | 11 | Approximate Intervals, Exact Guarantees | Approximate Intervals, Exact Guarantees | P1 |
| 14 | S24 | 12 | Bounded Averages Concentrate | Bounded Averages Concentrate | P1 |
| 15 | S116a | 15 split | Rare Events Need Relative Error | Small Absolute Error Can Hide Failure | P1 |
| 16 | S116b | 15 split | Rare Events Need Relative Error | Relative Error Needs Enough Hits | P1 |
| 17 | S41 | 16 | Change the Sampler | Change the Sampler | I |
| 18 | S43 | 17 | Most Draws Miss the Tail | Most Draws Miss the Tail | P2 |
| 19 | S44 | 18 | A Rare Event Needs Many Samples | A Rare Event Needs Many Samples | P2 |
| 20 | S45 | 19 | Visit Useful Outcomes More Often | Visit Useful Outcomes More Often | P2 |
| 21 | S50 | 20 | Correct Each Visit's Weight | Correct Each Visit’s Weight | P2 |
| 22 | S46 | 21 | Importance Sampling Preserves the Target | Importance Sampling Preserves the Target | P2 |
| 23 | S47a | 22 | Proof: Cancel the Proposal | Proof: Cancel the Proposal | P2 |
| 24 | S47b | 23 | Proof (continued): Check the Missing Region | Proof Continued: Check the Missing Region | P2 |
| 25 | S48 | 24 | Missing Support Cannot Be Repaired | Missing Support Cannot Be Repaired | P2 |
| 26 | S49 | 25 | Average the Weighted Integrand | Average the Weighted Integrand | P2 |
| 27 | S117 | 26 | A Practical Exponential Proposal | A Practical Exponential Proposal | P2 |
| 28 | S118 | 27 | More Tail Visits, Corrected Weights | Average Weighted Contributions to Estimate the Target | P2 |
| 29 | S119 | 28 | Compute the Proposal's Error | Compute the Proposal’s Error | P2 |
| 30 | S120 | 29 | Same Target, Less Relative Error | Same Target, Less Relative Error | P2 |
| 31 | S54 | 30 | Coverage and Variance Are Different | Coverage and Variance Are Different | P2 |
| 32 | S55 | 31 | Control Proposal Risk | Control Proposal Risk | I |
| 33 | S56 | 32 | The Second Moment Decides | The Second Moment Decides | P2 |
| 34 | S57 | 33 | Follow the Weighted Integrand | Sample Where Contributions Matter | P2 |
| 35 | S59 | 34 | The Optimal Proposal | The Optimal Proposal | P2 |
| 36 | S60 | 35 | Proof: A Common Lower Bound | Proof: A Common Lower Bound | P2 |
| 37 | S61 | 36 | Proof (continued): Attain the Bound | Proof Continued: Attain the Bound | P2 |
| 38 | S63a | 37 split | One-Sign Integrands Permit Zero Variance | Random Draws Can Give Identical Contributions | P2 |
| 39 | S63b | 37 split | One-Sign Integrands Permit Zero Variance | Constant Contributions Give Zero Estimator Variance | P2 |
| 40 | S64 | 38 | The Oracle Needs a Normalizer | The Oracle Needs a Normalizer | P2 |
| 41 | S66 | 39 | Light Tails Can Destroy Variance | Light Tails Can Destroy Variance | P2 |
| 42 | S68 | 40 | A Finite Mean, an Infinite Second Moment | A Finite Mean, an Infinite Second Moment | P2 |
| 43 | S121 | 41 | Consistency Is Not an Error Bar | Consistency Is Not an Error Bar | P2 |
| 44 | S69a | 42 split | Check the Integrand, Not Just Weights | A Heavier Proposal Helps This Integrand | P2 |
| 45 | S69b | 42 split | Check the Integrand, Not Just Weights | Heavier Tails Are Not a Requirement | P2 |
| 46 | S72 | 43 | Remove the Normalizer | Remove the Normalizer | I |
| 47 | S132 | new before S73 | new | Bayes Leaves a Normalizing Integral | P3 |
| 48 | S73 | 44 | The Target Is Known Up to Z | The Target Is Known Up to Z | P3 |
| 49 | S74 | 45 | Compute Unnormalized Weights | Compute Unnormalized Weights | P3 |
| 50 | S75 | 46 | Normalize Only a Positive Total | Normalize Only a Positive Total | P3 |
| 51 | S133 | new after S75 | new | Likelihood Weights Remove the Unknown Z | P3 |
| 52 | S76 | 47 | Two Averages Form One Ratio | Two Averages Form One Ratio | P3 |
| 53 | S77 | 48 | The Ratio Converges to the Target | The Ratio Converges to the Target | P3 |
| 54 | S78 | 49 | One Draw Exposes SNIS Bias | One Draw Exposes SNIS Bias | P3 |
| 55 | S122 | 50 | Normalization Does Not Guarantee Improvement | Normalization Does Not Guarantee Improvement | P3 |
| 56 | S70 | 51 | One Draw Can Dominate the Weights | One Draw Can Dominate the Weights | P3 |
| 57 | S79 | 52 | Effective Sample Size Summarizes Imbalance | Effective Sample Size Summarizes Imbalance | P3 |
| 58 | S81 | 53 | Healthy ESS Can Miss Missing Support | Healthy ESS Can Miss Missing Support | P3 |
| 59 | S82 | 54 | What You Can Compute Decides What Is Available | What You Can Compute Decides What Is Available | P3 |
| 60 | S99 | 75 | Reuse Samples Responsibly | Reuse Samples in RL | I |
| 61 | S100 | 76 | Old Samples, a New Target | Old Samples, a New Target | P4 |
| 62 | S101 | 77 | Importance Weights Correct the Mismatch | Importance Weights Correct the Mismatch | P4 |
| 63 | S102 | 78 | Sequence Ratios Multiply | Sequence Ratios Multiply | P4 |
| 64 | S103 | 79 | Compounding Mismatch Can Destroy Efficiency | Compounding Mismatch Can Destroy Efficiency | P4 |
| 65 | S129 | 80 | Behavior and Reference Are Different Roles | Behavior and Reference Are Different Roles | P4 |
| 66 | S105 | 81 | KL Is Not a Variance Certificate | KL Is Not a Variance Certificate | P4 |
| 67 | S106 | 82 | Reward Tuning Uses This Toolkit | RL Objectives Contain Expectations | P4 |
| 68 | S104 | 83 | A Surrogate Is Not a Hard Constraint | A Surrogate Is Not a Hard Constraint | P4 |
| 69 | S109a | 84 | Choose an Expectation Estimator by Its Requirements | Choose an Expectation Estimator by Its Requirements | I |
| 70 | S113 | 86 |  | Same Target, Different Sampler | I |

## Per-ID content specifications

### 1. S01 — Monte Carlo & Importance Sampling [I; baseline 1; judgment]

- **Must / point:** Set expectation estimation as the scope.
- **Main:** Current subtitle “Estimating expectations and their gradients by sampling” → a concise expectation/importance-sampling subtitle without gradients. Keep speaker/course metadata.
- **Exhibit and H/M:** Title-slide exhibit; H/M opening describes the new five-part scope with no duration promise.
- **Evidence/decision:** C11/C13/E01. **Layout:** title-slide. **Time:** not budgeted (C13).
- **Accept:** No gradient objective or fixed-minute slot remains.

### 2. S02 — Contents [I; baseline 2; judgment]

- **Must / point:** Show the five-part argument.
- **Main:** Use01 Estimate an Expectation;02 Change the Sampler;03 Control Proposal Risk;04 Remove the Normalizer;05 Reuse Samples in RL. Remove dimension and gradient subtopics from subtitles.
- **Exhibit and H/M:** Five-part contents; companion navigation agrees.
- **Evidence/decision:** C03/C11/C12/C13. **Layout:** toc-list. **Time:** not budgeted (C13).
- **Accept:** Names/order/numbering match actual dividers.

### 3. S03 — Estimate an Expectation [I; baseline 3; judgment]

- **Must / point:** Motivate the familiar average before its accuracy tools.
- **Main:** Part01 subtitle should allow ML motivation and sampling accuracy, without a second agenda slide.
- **Exhibit and H/M:** Section divider; H/M explain the question, no pace line.
- **Evidence/decision:** E01/C01. **Layout:** section-slide. **Time:** not budgeted (C13).
- **Accept:** Does not start with an unexplained abstract cost detour.

### 4. S130 — One-Hot Cross-Entropy Equals KL [P1; baseline new after S03; judgment]

- **Must / point:** At a fixed labelled input, one-hot cross-entropy is exactly a KL loss.
- **Main:** Define CE as cross-entropy on first use. Recall the known identity CE(delta_y,q_theta(.|x)) = D(delta_y||q_theta(.|x)) = -log q_theta(y|x). Say one-hot label, fixed input and positive predicted probability for the observed class; do not claim all cross-entropy equals KL. Connect this familiar per-example loss to the need to average over data.
- **Prefer / exhibit and reading:** A single identity with the true-label distribution and model-label distribution named, not a second KL derivation.
- **H/M:** Explain delta_y, the entropy-zero specialization, and the general entropy-plus-KL identity. If discussing conditional classifiers, use conditional entropy plus expected conditional KL, not a joint-versus-conditional distribution mismatch. Source the prob02 statement and E02.
- **Evidence:** E01/E02/E09. **Layout:** math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** A lecturer can say why CE is familiar and what remains to compute; no blanket CE=KL statement.

### 5. S131 — Population Loss Requires an Average [P1; baseline new after S130; judgment]

- **Must / point:** The population loss of a fixed model is estimated by averaging sampled losses.
- **Main:** Show L(theta)=E_{(X,Y)~P_data}[-log q_theta(Y|X)] and its mean over n IID labelled examples. Identify P_data as the sampling distribution, q_theta as the fixed classifier, and the loss as f. Model fixed; finite mean. This is evaluation of an expectation, not a derivation of SGD.
- **Prefer / exhibit and reading:** Expectation → per-example losses → sample average, with the same loss expression throughout.
- **H/M:** Explain the integral may not be available even when each loss is easy to compute. Use fresh evaluation data for the unbiasedness story. A uniformly sampled minibatch with replacement estimates an empirical dataset mean; fitted-model generalization is a separate issue. Avoid a new training algorithm tutorial.
- **Evidence:** E03/E09. **Layout:** diagram-flow or math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Sampling distribution and model distribution are not confused; the expectation-to-average step is explicit.

### 6. S04 — Sampled Replies Estimate Pass Rate [P1; baseline 4; judgment]

- **Must / point:** A generator can be easy to sample while its expected evaluation score is hard to compute.
- **Main:** Fix one prompt and one stochastic model p. Let f(x)=1 if reply x passes a specified fixed format check, else0. Target mu=Pr_p(pass)=E_p f(X); samples come from the model, not the labelled-data distribution on S131. Explain why evaluating a few replies is easier than summing over every possible reply.
- **Prefer / exhibit and reading:** Adapt the existing sampler → fixed evaluator → target diagram; name replies, pass/fail check and pass rate. No manufactured performance number.
- **H/M:** Explain the scope of the format criterion: a useful example of an expectation, not comprehensive quality. Sampling setup is independent draws from the fixed model, not a claim that any decoding setting implements p. No closed-form impossibility claim.
- **Evidence:** E10/E03. **Layout:** diagram-flow; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** The generative-model motivation is concrete and distinct from the data-loss motivation, with the average visibly answering a real evaluation question.

### 7. S06 — Sample, Evaluate, Average [P1; baseline 5; retain]

- **Must / point and exhibit:** Sample, evaluate a fixed f, average under the intended law; retain the3-step recipe.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E03/B02. **Time:** not budgeted (C13).
- **Accept:** IID and integrability remain; MC requires samples, not pointwise p values.

### 8. S26 — Six Points Illustrate the Recipe [P1; baseline 6; retain]

- **Must / point and exhibit:** Four disk hits among six hand-chosen points illustrate the average8/3, not reliability.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B17/B24. **Time:** not budgeted (C13).
- **Accept:** Keep schematic/not-random label and exact geometry; no simulated-error claim.

### 9. S16 — Monte Carlo Reuses the Sample Mean [P1; baseline 7; retain]

- **Must / point and exhibit:** Set Y=f(X) and reuse sample-mean facts; keep the recall/equation.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E03/B01/B02. **Time:** not budgeted (C13).
- **Accept:** First moment for mean/LLN remains distinct from finite variance for error rate.

### 10. S19 — Unbiased Does Not Mean Accurate [P1; baseline 8; retain]

- **Must / point and exhibit:** An unbiased estimator can be inaccurate on a run; retain exact binomial distribution of six-dart estimate.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B17/B24. **Time:** not budgeted (C13).
- **Accept:** Distribution probabilities, meanpi,35% rounded tail claim and labels unchanged/consistent.

### 11. S22 — Averaging Reduces RMSE [P1; baseline 9; retain]

- **Must / point and exhibit:** Under IID finite variance RMSE falls as1/sqrt(n); retain the log–log curve.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E03/B02/B17. **Time:** not budgeted (C13).
- **Accept:** Typical repeated-sample error, not a per-run bound; sigma_f meaning visible.

### 12. S114 — SE Measures Estimator Spread [P1; baseline 10; judgment]

- **Must / point:** Standard error is the spread of the estimator across repeated samples.
- **Main:** Current unexplained SE → “standard error (SE): standard deviation of the sample mean across repeated samples.” Keep true SE=sigma_f/sqrt(n) and estimated SE=s_Y/sqrt(n), IID finite-variance conditions and n>=2 for sample variance. Outcome SD and realized error are different quantities.
- **Prefer / exhibit and reading:** Keep the observed evaluations → sample spread → estimated standard error diagram with the expanded words readable.
- **H/M:** Explain repeated imaginary batches, the difference between s_Y and s_Y/sqrt(n), and that a finite or zero empirical estimate cannot reveal unseen tails. Preserve the next slide’s approximate-interval versus guarantee distinction.
- **Evidence:** E03/B02. **Layout:** diagram-flow; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** SE is defined in words on-slide, not only expanded in a note or legend. No claim that estimated SE equals this run’s error.

### 13. S115 — Approximate Intervals, Exact Guarantees [P1; baseline 11; retain]

- **Must / point and exhibit:** Approximate normal coverage and finite-sample guarantees answer different questions; retain the comparison.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E03/B02/B17. **Time:** not budgeted (C13).
- **Accept:** No finite-n95% promise from CLT; Chebyshev uses known/proven variance, not plug-in sample variance.

### 14. S24 — Bounded Averages Concentrate [P1; baseline 12; retain]

- **Must / point and exhibit:** Known bounded range yields a Hoeffding guarantee; retain rescaling plus example.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B01/B17. **Time:** not budgeted (C13).
- **Accept:** Fixed f, known range, IID, sufficient—not minimal—sample size295111.

### 15. S116a — Small Absolute Error Can Hide Failure [P1; baseline 15 split; judgment]

- **Must / point:** A rare-event estimate can be absolutely close yet relatively useless.
- **Main:** Event indicator, rho=.001, n=1000. Expected hits n*rho=1. Chance of no hits is (.999)^1000 approximately37%. A zero-hit run yields estimate0: absolute error.001, relative error100%. Identify this as one possible run and the37% as its probability, not a typical-error identity.
- **Prefer / exhibit and reading:** One worked comparison: truth.001 versus estimate0, with absolute and relative readings; no need for a simulated1000-point cloud.
- **H/M:** Explain why “small number minus small number” is misleading for rare probabilities. Define relative error as absolute error divided by the positive target. Distinguish the particular zero-hit run from repeated-sample RMSE. Note empirical variance can be zero after no hits without true variance being zero.
- **Evidence:** E03. **Layout:** math-block or grid-2; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Learner can explain what is wrong with the zero estimate despite the small absolute error; all numerical claims reproduce.

### 16. S116b — Relative Error Needs Enough Hits [P1; baseline 15 split; judgment]

- **Must / point:** Relative precision depends on enough expected event hits, not just a large sample count.
- **Main:** For IID Bernoulli(rho), 0<rho<1, show relative RMSE=sqrt((1-rho)/(n*rho)); rare rho makes it approximately1/sqrt(n*rho). Apply the same rho=.001: n=1000 gives about100% relative RMSE;10% needs n>=99,900. This is an RMSE requirement, not95% confidence or a realized-error guarantee.
- **Prefer / exhibit and reading:** One compact worked scaling from expected hits to relative RMSE; do not also squeeze in the old trend plot.
- **H/M:** Retain the exact absolute RMSE derivation and the existing p15 per-draw absolute/relative SD plot here, with a complete verbal description in M. Explain fixed-n scaling by sqrt(n), domain0<rho<=1/2 for the monotonic comparison, log axes and correct unequal endpoints. Keep the exponential benchmark’s distinct numbers for Part02.
- **Evidence:** E03/B31. **Layout:** math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Two slides answer p15 concretely without a third repetitive plot slide; the moved plot and its limitations genuinely exist in both companions.

### 17. S41 — Change the Sampler [I; baseline 16; judgment]

- **Must / point:** Visit useful outcomes without changing the expectation.
- **Main:** Keep Part02 divider and target-preservation point.
- **Exhibit and H/M:** Existing divider; brief H/M.
- **Evidence/decision:** E04. **Layout:** section-slide. **Time:** not budgeted (C13).
- **Accept:** Title agrees with Contents; no duration line.

### 18. S43 — Most Draws Miss the Tail [P2; baseline 17; retain]

- **Must / point and exhibit:** Most Exp(1) draws missx>10; retain target-density/tail exhibit.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B11. **Time:** not budgeted (C13).
- **Accept:** Benchmark answer e^-10 and approximately1in22026, magnified inset identified; tail continues.

### 19. S44 — A Rare Event Needs Many Samples [P2; baseline 18; retain]

- **Must / point and exhibit:** Ten-percent relative RMSE for this rare event needs2202547 ordinary draws; retain substitution.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E03/B11. **Time:** not budgeted (C13).
- **Accept:** Not95%confidence; rounding by ceiling and role of known benchmark answer preserved.

### 20. S45 — Visit Useful Outcomes More Often [P2; baseline 19; retain]

- **Must / point and exhibit:** A proposal changes visits, not the desired target; retain hand-placed draw contrast.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Plain q-average estimates Eq f, not Ep f; schematic label remains.

### 21. S50 — Correct Each Visit’s Weight [P2; baseline 20; retain]

- **Must / point and exhibit:** The target-over-proposal ratio corrects visits; retain comparison diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Direction p/q never inverted; continuous densities are not point probabilities.

### 22. S46 — Importance Sampling Preserves the Target [P2; baseline 21; retain]

- **Must / point and exhibit:** Coverage and integrability give equal expectations; retain theorem.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Coverage of fp, not necessarily all p, plus computable normalized ratio; no variance promise.

### 23. S47a — Proof: Cancel the Proposal [P2; baseline 22; retain]

- **Must / point and exhibit:** Cancel q on its positive support; retain first proof step.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Integration domain and absolute integrability are explicit.

### 24. S47b — Proof Continued: Check the Missing Region [P2; baseline 23; retain]

- **Must / point and exhibit:** The uncovered region contributes zero under the assumption; retain second proof step.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Only fp must vanish there; pointwise p may be positive where f=0.

### 25. S48 — Missing Support Cannot Be Repaired [P2; baseline 24; retain]

- **Must / point and exhibit:** Never-sampled contributions cannot be repaired by more draws; retain four-state counterexample.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B19/B04. **Time:** not budgeted (C13).
- **Accept:** Target1/4 versus estimate0 for every n, correct p/q on observed states.

### 26. S49 — Average the Weighted Integrand [P2; baseline 25; retain]

- **Must / point and exhibit:** Ordinary IS averages weighted contributions and divides by n; retain recipe.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Not normalized by sum of weights; unbiasedness inherits the identity conditions.

### 27. S117 — A Practical Exponential Proposal [P2; baseline 26; retain]

- **Must / point and exhibit:** Exp(.1) is a practical non-oracle sampler for the tail; retain density comparison.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B11. **Time:** not budgeted (C13).
- **Accept:** Coverage, known normalizer, exact log-scale curves; rate is illustrative not optimal.

### 28. S118 — Average Weighted Contributions to Estimate the Target [P2; baseline 27; judgment]

- **Must / point:** Each sampled x contributes f(x)w(x); averaging these estimates the horizontal target mu.
- **Main:** Relabel bare fw → “weighted contribution f(x)w(x)” and bare mu → “target mean mu=E_p f=E_q[fw]”. Reuse p=Exp(1), q=Exp(.1), f=1{x>10}. Below10 the contribution is0; above10 it is10e^(-.9x). The horizontal target is e^(-10), not another density. More hits alone do not certify lower variance.
- **Prefer / exhibit and reading:** Figure-first contribution curve with clear x/contribution axes and a separate target-mean line. Preserve the fact that log axes cannot display the zero portion; state it outside the positive-scale curve. The mean is weighted by q, not the unweighted geometric area under this curve.
- **H/M:** Define f,w,Y,mu and explain one draw versus averaging repeated q draws. Retain tail-hit probability e^-1 and about8100x frequency as secondary arithmetic if crowded; next slide computes variance. Preserve exact generator provenance.
- **Evidence:** E04/B11. **Layout:** figure-first; slides decides; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Both symbols Albert asked about are explained on the main slide, and notes teach how to read the curve rather than repeating the labels.

### 29. S119 — Compute the Proposal’s Error [P2; baseline 28; retain]

- **Must / point and exhibit:** Compute the contribution second moment to establish precision; retain integration.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B11. **Time:** not budgeted (C13).
- **Accept:** Correctlambda domain0<lambda<2 and relative variance13.3067; square contribution not just weight.

### 30. S120 — Same Target, Less Relative Error [P2; baseline 29; retain]

- **Must / point and exhibit:** Same target, far fewer draws for the same relative RMSE in this example; retain bars.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B11/B24. **Time:** not budgeted (C13).
- **Accept:** 1331vs2202547 from exact formulas, not measured runtime orconfidence guarantee.

### 31. S54 — Coverage and Variance Are Different [P2; baseline 30; retain]

- **Must / point and exhibit:** Validity and precision are separate tests; retain the two-check diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B11. **Time:** not budgeted (C13).
- **Accept:** Last slide of Part02, before S55 divider; coverage does not imply finite/small variance.

### 32. S55 — Control Proposal Risk [I; baseline 31; judgment]

- **Must / point:** A correct mean is not enough.
- **Main:** Keep Part03 divider after S54, not before it.
- **Exhibit and H/M:** Existing divider; brief H/M.
- **Evidence/decision:** E04/E06. **Layout:** section-slide. **Time:** not budgeted (C13).
- **Accept:** Boundary and outline ranges computed correctly.

### 33. S56 — The Second Moment Decides [P2; baseline 32; retain]

- **Must / point and exhibit:** q changes the weighted second moment, not mu; retain the variance identity.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** IID finite moment scope, infinite variance limit and dependence on f remain explicit.

### 34. S57 — Sample Where Contributions Matter [P2; baseline 33; judgment]

- **Must / point:** Choose q to visit large contributions, not merely the most likely x under p.
- **Main:** For p=N(0,1), f(x)=x, focus on p versus |x|p. Say |f|p is an unnormalized importance profile; q is aimed there. The profile has two lobes and is0 at x=0. Absolute value is needed because a sampling density cannot be negative. This is intuition before the theorem.
- **Prefer / exhibit and reading:** Replace the competing three-curve story with a large p-versus-|x|p plot and one reading line. Move signed fp curve out of the main slide; preserve redundant encodings and the message that p peaks centrally but contribution magnitude does not.
- **H/M:** Explain the existing second-moment expression f^2*p^2/q, the unnormalized scale and why a signed integrand does not yield zero variance just because magnitude is balanced. Preserve the signed curve/interpretation as secondary details if useful.
- **Evidence:** E04/B04. **Layout:** figure-first; slides decides; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** The title/message and dominant visual communicate one point at a glance; no cramped algebra+three-curve+bullets collage.

### 35. S59 — The Optimal Proposal [P2; baseline 34; retain]

- **Must / point and exhibit:** The optimal density balances absolute contributions; retain theoremq*=|f|p/c.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** 0<c<infinity, coverage and minimumc²-mu²; not automatically a usable sampler.

### 36. S60 — Proof: A Common Lower Bound [P2; baseline 35; retain]

- **Must / point and exhibit:** Jensen gives the same lower bound for every admissible q; retain proof.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** Equality iff |f|w constantq-a.s.; sufficient integral conditions remain.

### 37. S61 — Proof Continued: Attain the Bound [P2; baseline 36; retain]

- **Must / point and exhibit:** The proposed density attains the bound; retain substitution/proof.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E04/B04. **Time:** not budgeted (C13).
- **Accept:** q*normalizes to1; magnitude is constant but sign can flip.

### 38. S63a — Random Draws Can Give Identical Contributions [P2; baseline 37 split; judgment]

- **Must / point:** Random locations can produce identical weighted contributions.
- **Main:** Return explicitly to f=1{x>10}, p=Exp(1). The oracle q* draws X=10+Exp(1), so X is random with variance1. Every resulting Y=f(X)p(X)/q*(X) is e^-10. The variance being removed is Var(Y), not Var(X). Label this an oracle benchmark using the known tail answer.
- **Prefer / exhibit and reading:** Several different, fixed illustrative x>10 values → the same Y value. Use schematic labels, not a fake random simulation. Show the distinction Var(X)=1 versus Var(Y)=0 without two competing plots.
- **H/M:** Walk through why the weight exactly offsets where X landed. Explain true population constancy versus zero sample variance in a no-hit rare-event batch. Keep support x>10 explicit in any q* formula.
- **Evidence:** E05. **Layout:** diagram-flow; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Explicit on-slide answer to “how can zero variance be possible?”; different X, identical contribution, no impossible deterministic-X claim.

### 39. S63b — Constant Contributions Give Zero Estimator Variance [P2; baseline 37 split; judgment]

- **Must / point:** Averaging an almost-sure constant has zero estimator variance.
- **Main:** General nonnegative case: f>=0 and0<mu=E_p f<infinity; q*=fp/mu. On q*>0, fw*=mu almost surely; therefore Var_q*(Y)=0 and Var(hat mu_n)=0. State that sign-changing f need not have this property and normalized oracle weights need mu. Keep S64 immediately next.
- **Prefer / exhibit and reading:** A short cancellation identity ending in a constant contribution, then the zero-variance conclusion. Do not restate the entire optimal-proposal proof.
- **H/M:** Explain the general one-sign extension and c^2-mu^2 from S59. In the easy tail benchmark the normalizer is known; in a genuinely unknown expectation the identity does not supply a free numerical answer.
- **Evidence:** E05/B04. **Layout:** math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Claim is qualified and operational caveat appears before anyone could infer a universal one-draw solver.

### 40. S64 — The Oracle Needs a Normalizer [P2; baseline 38; retain]

- **Must / point and exhibit:** The oracle weight needs its normalizer; retain sampling-versus-evaluation distinction.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E05/B04. **Time:** not budgeted (C13).
- **Accept:** Immediately afterS63b; do not claim sampling q* is universally impossible.

### 41. S66 — Light Tails Can Destroy Variance [P2; baseline 39; retain]

- **Must / point and exhibit:** Tail under-coverage in magnitude can make weights grow; retain Exp(2)setup/plot.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E06/B18. **Time:** not budgeted (C13).
- **Accept:** Positive coverage everywhere; growing weights only a warning before proof.

### 42. S68 — A Finite Mean, an Infinite Second Moment [P2; baseline 40; retain]

- **Must / point and exhibit:** Finite first moment can coexist with infinite second moment; retain exact integrations.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E06/B18. **Time:** not budgeted (C13).
- **Accept:** Infinite finite-n RMSE, but valid mean/unbiasedness; correct cancellation.

### 43. S121 — Consistency Is Not an Error Bar [P2; baseline 41; retain]

- **Must / point and exhibit:** LLN consistency does not supply a finite-variance error bar; retain two-condition comparison.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E06/B18. **Time:** not budgeted (C13).
- **Accept:** No finite sample variance used to certify unseen tails; IID wording consistent.

### 44. S69a — A Heavier Proposal Helps This Integrand [P2; baseline 42 split; judgment]

- **Must / point:** A heavier proposal reduces variance for this specific target and integrand.
- **Main:** Continue p=Exp(1), f=x, mu=1. q=Exp(.5) gives Var_q(fw)=5/27, ordinary MC gives1. Show the comparison, not the full integration again. The preceding Exp(2) counterexample already showed infinite variance. State per-draw weighted-contribution variance, not bare-weight variance.
- **Prefer / exhibit and reading:** Bars or a simple worked comparison for ordinary MC versus Exp(.5), lower is better; no table of magnitudes plus derivation plus highlight.
- **H/M:** Retain derivation E_q[(fw)^2]=32/27 and subtract mu^2=1; E_q[w^2]=4/3 is a different quantity. Explain this is an exact calculation, not a runtime benchmark.
- **Evidence:** E06/B18. **Layout:** figure-first or math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** The concrete benefit is readable and the compared quantity is correctly identified.

### 45. S69b — Heavier Tails Are Not a Requirement [P2; baseline 42 split; judgment]

- **Must / point:** Heavier tails are not a universal requirement; the weighted second moment is the test.
- **Main:** Answer the question directly: “Must q have heavier tails? No.” In the same f=x,p=Exp(1) case, q=Exp(1.5) has a lighter tail but finite Var(fw)=29/3. Validity needs coverage; finite variance needs integral f^2*p^2/q finite. These are separate claims; lighter-but-finite is not advertised as efficient.
- **Prefer / exhibit and reading:** A focused lighter-tail counterexample followed by the general criterion. Avoid introducing several extra rates or an optimization curve.
- **H/M:** Derive2/[lambda(2-lambda)^3]-1 for0<lambda<2 and divergence forlambda>=2. Optionallambda=.1 example shows even a very heavy proposal can be worse; secondary only. State that f affects the relevant tail.
- **Evidence:** E06. **Layout:** math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Explicit no on-slide with a correct counterexample and a replacement rule, not an ambiguous “heavier is a heuristic” slogan.

### 46. S72 — Remove the Normalizer [I; baseline 43; judgment]

- **Must / point:** Use relative target scores when normalized density is unavailable.
- **Main:** Keep Part04 divider; lead directly to the concrete Bayesian example before the abstract statement.
- **Exhibit and H/M:** Existing divider; H/M point, no pacing.
- **Evidence/decision:** E07/B05. **Layout:** section-slide. **Time:** not budgeted (C13).
- **Accept:** Transition mentions the obstacle rather than claiming every normalizer unknowable.

### 47. S132 — Bayes Leaves a Normalizing Integral [P3; baseline new before S73; judgment]

- **Must / point:** A posterior can be evaluated up to a normalizer even in a small familiar model.
- **Main:** Introduce our toy: latent logit theta has standard-normal prior density phi; success probability s(theta)=1/(1+e^-theta). Observe two conditionally independent successes, so likelihood=s(theta)^2. Unnormalized posterior tilde p(theta)=phi(theta)s(theta)^2. Normalizing over theta is the remaining integral; let S73 introduce its general Z formula. Define prior, observation and likelihood before the posterior.
- **Prefer / exhibit and reading:** Prior × likelihood → unnormalized posterior. One small model diagram/equation sequence; no fake experimental dataset or claimed Stan algorithm.
- **H/M:** Explain Bayes, conditional independence, what logistic means and why phi is known. State0<Z<infinity and distinguish evaluability at a point from integrating the whole function. The posterior predictive question will be answered on S133. Cite Stan for the framework and mark the toy as ours.
- **Evidence:** E07/E01. **Layout:** diagram-flow or math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Students can identify what was observed, what theta means and why Z appears; model is understandable before abstract normalization.

### 48. S73 — The Target Is Known Up to Z [P3; baseline 44; judgment]

- **Must / point:** Known up to Z means pointwise scores are computable but normalized density values are not yet available.
- **Main:** Preserve the current p=tilde p/Z, unknown0<Z<infinity setup and ordinary-weight obstruction. Add a brief model link: in the preceding example tilde p=phi*s^2 and Z is the integral of that product. Do not repeat the entire Bayesian model or call Z impossible to compute.
- **Prefer / exhibit and reading:** Keep the existing evaluable-versus-not-yet-evaluable distinction; a small substitution/example phrase may replace redundant prose.
- **H/M:** Give Z=integral phi(t)s(t)^2 dt and explain that the toy could be checked numerically but SNIS need not compute that integral. Do not equate unknown with undefined.
- **Evidence:** E07/B05. **Layout:** existing math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** The abstract slide now has an immediately recognizable concrete referent while retaining its general conditions.

### 49. S74 — Compute Unnormalized Weights [P3; baseline 45; retain]

- **Must / point and exhibit:** Computable unnormalized weights share a common Z; retain ratio derivation.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B05. **Time:** not budgeted (C13).
- **Accept:** SNIS requires coverage of all target mass, not only fp.

### 50. S75 — Normalize Only a Positive Total [P3; baseline 46; retain]

- **Must / point and exhibit:** Normalize by a positive total to cancel Z; retain estimator definition.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B05. **Time:** not budgeted (C13).
- **Accept:** No extra divide byn; all-zero batch is undefined, not0; nonnegative shares.

### 51. S133 — Likelihood Weights Remove the Unknown Z [P3; baseline new after S75; judgment]

- **Must / point:** Likelihood-weighted prior draws estimate a posterior prediction without Z.
- **Main:** Target: probability of the next success under the posterior, mu=E_post[s(theta)]. Draw IID theta_i from the prior q=phi; unnormalized weights tilde w_i=s(theta_i)^2. SNIS yields sum_i s(theta_i)^3 / sum_i s(theta_i)^2. Label this as a consistent ratio estimator, not an exact finite-sample posterior probability. All weights positive here, so the denominator is positive.
- **Prefer / exhibit and reading:** Prior draw → success probability → likelihood weight → weighted prediction, with a short ratio substitution. One mechanism, not a formula paired with an unrelated posterior plot.
- **H/M:** Walk through why numerator has the third power and denominator the second. Cite the general SNIS formula. Optional quadrature referenceZ=.29337903585809, mu=.64786003959422 is validation only and never an estimator input. Record any random seed or identify fixed illustrative points. Preserve usual finite-n bias distinction.
- **Evidence:** E07/B05. **Layout:** math-block or diagram-flow; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** A lecturer can calculate the estimator from samples without Z, and explain what it estimates. New generator reproduces any displayed or noted numerical checks.

### 52. S76 — Two Averages Form One Ratio [P3; baseline 47; retain]

- **Must / point and exhibit:** SNIS is a ratio of generally dependent averages; retain branch diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B05/B25. **Time:** not budgeted (C13).
- **Accept:** Unbiased numerator/denominator do not imply unbiased ratio; generally dependent not always.

### 53. S77 — The Ratio Converges to the Target [P3; baseline 48; judgment]

- **Must / point:** A positive limiting denominator gives SNIS consistency, not finite-sample unbiasedness.
- **Main:** Current “Iid draws” → “IID draws”. Preserve full target coverage, integrability,0<Z<infinity, almost-sure limits and eventual—not universal finite-batch—positivity. Use consistent IID/iid rather than title-case Iid in touched material.
- **Prefer / exhibit and reading:** Retain the existing two LLN limits and ratio limit.
- **H/M:** Preserve distinction between dependence of numerator/denominator and convergence. Existing exceptions/finite-batch denominator caveat remain; the new example has positive weights but the general theorem is broader.
- **Evidence:** B05/E07. **Layout:** existing math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Acronym is fixed without weakening the theorem or importing the toy’s all-positive property into every SNIS problem.

### 54. S78 — One Draw Exposes SNIS Bias [P3; baseline 49; retain]

- **Must / point and exhibit:** A one-draw example demonstrates finite-n SNIS bias; retain two-state enumeration.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B12/B24. **Time:** not budgeted (C13).
- **Accept:** Target3/4, estimator mean1/2; generally—not always—biased.

### 55. S122 — Normalization Does Not Guarantee Improvement [P3; baseline 50; retain]

- **Must / point and exhibit:** Normalization cancels Z without universally improving error; retain comparison.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B05/B25. **Time:** not budgeted (C13).
- **Accept:** Integrability and support qualifiers remain; no universal MSE ranking.

### 56. S70 — One Draw Can Dominate the Weights [P3; baseline 51; retain]

- **Must / point and exhibit:** A single sample can hold95%of normalized weight; retain five-share bars.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B19. **Time:** not budgeted (C13).
- **Accept:** 95%weight is not necessarily95%of weighted estimate; no infinite-variance inference.

### 57. S79 — Effective Sample Size Summarizes Imbalance [P3; baseline 52; retain]

- **Must / point and exhibit:** ESS measures sampled weight balance; retain formula and equal/dominated cases.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B06/B19/B30. **Time:** not budgeted (C13).
- **Accept:** Positive total, nonnegative weights; not independent sample count or integrand-specific error bar. In notes generalpopulationratio uses(Ew)^2/Ew² unlessfullmasscoverageEw=1 justified.

### 58. S81 — Healthy ESS Can Miss Missing Support [P3; baseline 53; retain]

- **Must / point and exhibit:** Healthy ESS can coexist with missing support; retain four-state exhibit.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B19. **Time:** not budgeted (C13).
- **Accept:** ESS=n, estimate0,target1/4; theorem assumption fails, not theorem itself.

### 59. S82 — What You Can Compute Decides What Is Available [P3; baseline 54; retain]

- **Must / point and exhibit:** Available inputs determine which estimators are available, not which is best; retain capability map.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B04/B05. **Time:** not budgeted (C13).
- **Accept:** Rows not exclusive; support andpositive-total conditions remain; do not add duplicate closing recap.

### 60. S99 — Reuse Samples in RL [I; baseline 75; judgment]

- **Must / point:** Old-policy samples raise the same change-of-distribution problem.
- **Main:** Rename/renumber old06 “Reuse Samples Responsibly” →05 “Reuse Samples in RL”. Expand reinforcement learning if not already introduced before this divider. No gradient prerequisite bridge.
- **Exhibit and H/M:** Section divider; H/M transition from SNIS back to normalized policy ratios.
- **Evidence/decision:** C11/C12/E08. **Layout:** section-slide. **Time:** not budgeted (C13).
- **Accept:** Five-part numbering and an understandable RL entry.

### 61. S100 — Old Samples, a New Target [P4; baseline 76; retain]

- **Must / point and exhibit:** Logged responses come from behavior while the target expectation uses current policy; retain two-law diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E08. **Time:** not budgeted (C13).
- **Accept:** Fixed prompt/reward/current parameters during evaluation; no hidden gradient dependency.

### 62. S101 — Importance Weights Correct the Mismatch [P4; baseline 77; retain]

- **Must / point and exhibit:** Current-over-behavior weights correct the sampling mismatch; retain relabelled identity.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E08/B04. **Time:** not budgeted (C13).
- **Accept:** Coverage/integrability, direction and logged-distribution mean preserved.

### 63. S102 — Sequence Ratios Multiply [P4; baseline 78; retain]

- **Must / point and exhibit:** Sequence likelihood ratios factor by the chain rule; retain prefix diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E08/B20. **Time:** not budgeted (C13).
- **Accept:** Same histories top/bottom, no independence claimed for actualtokens.

### 64. S103 — Compounding Mismatch Can Destroy Efficiency [P4; baseline 79; retain]

- **Must / point and exhibit:** Independent ratio factors can compound second moments exponentially; retain toy/plot.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E08/B20/B24. **Time:** not budgeted (C13).
- **Accept:** Independence of weight factors under behavior explicit; mean1,secondmoment1.1; not measured model evidence.

### 65. S129 — Behavior and Reference Are Different Roles [P4; baseline 80; retain]

- **Must / point and exhibit:** Behavior corrects the data law; reference anchors the KL penalty; retain three-role diagram.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** E08/B22. **Time:** not budgeted (C13).
- **Accept:** Two roles may start equal but are not interchangeable; no guarantee from reference closeness.

### 66. S105 — KL Is Not a Variance Certificate [P4; baseline 81; retain]

- **Must / point and exhibit:** Small KL is not an upper bound on importance-weight second moment; retain equations/counterexample.
- **Main/H/M/layout:** preserve the reviewed baseline allocation and component; synchronize cross-references and any necessary terminology, not a gratuitous rewrite. **Evidence:** B14/B24/E08. **Time:** not budgeted (C13).
- **Accept:** Two-state numbers and KL direction, nats, behavior/reference roles preserved.

### 67. S106 — RL Objectives Contain Expectations [P4; baseline 82; judgment]

- **Must / point:** The historical RL objective contains expectations that need sampling-based estimates.
- **Main:** Keep the scoped InstructGPT reward-minus-reference-KL objective, fixed prompt, fixed learned reward, beta>=0 and SFT reference definitions. Replace “Toolkit: MC averages + score-function gradients” with a brief statement about estimating expectations and reweighting old-policy samples. Define SFT and RLHF as already done. No score-gradient derivation or assertion that IS alone optimizes the model.
- **Prefer / exhibit and reading:** Use the existing objective as the sole exhibit, with terms named in the same order. If referring to KL as an expectation, the formula was given on S105; do not add a second large derivation.
- **H/M:** Explain how samples from the current policy give MC averages, and behavior-policy samples need the earlier ratio under the stated conditions. Remove the now-orphaned gradient derivation from H/M. Retain historical scope, fixed-prompt simplification, omitted PPO-ptx pretraining term and exact v1§3.5eq2 locator.
- **Evidence:** E08/B22. **Layout:** math-block; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** The RL application stands on MC/IS alone; no promise to teach gradients remains and no historical claim broadens to every current RL system.

### 68. S104 — A Surrogate Is Not a Hard Constraint [P4; baseline 83; judgment]

- **Must / point:** PPO clips a surrogate term, not the actual probability ratio.
- **Main:** Keep the cited PPO figure and clipping-versus-constraint distinction. Replace the opaque advantage label with a concise meaning: estimated advantage is how much better or worse action a is than expected at state s. Retain positive/negative panel labels, ratio axis and flat-region explanation. The surrogate is not the exact IS identity.
- **Prefer / exhibit and reading:** Retain unmodified source crops and readable external key; no reconstructed/repainted paper data.
- **H/M:** Define the immediate variables enough to read the panels. Explain baseline only informally through advantage; no score-function/baseline proof and no replacement gradient chapter. Preserve source/provenance.
- **Evidence:** E08/B09. **Layout:** existing figure-first; exact choice is slides' call. **Time:** not budgeted (C13).
- **Accept:** Understandable after removing gradients; clipping is not falsely claimed to keep every realized ratio inside the interval.

### 69. S109a — Choose an Expectation Estimator by Its Requirements [I; baseline 84; judgment]

- **Must / point:** Choose by available samples/densities and honest statistical claims.
- **Main:** Keep the three-estimator comparison and its qualified target. Remove any reference to a following gradient-summary page. Do not re-add the previously removed redundant bottom highlight.
- **Exhibit and H/M:** Existing single closing table; H/M comparison with assumptions and nonexclusive availability, not a second recap.
- **Evidence/decision:** B04/B05/E03/C11. **Layout:** existing table. **Time:** not budgeted (C13).
- **Accept:** Default capacity preserved: no table+extraequation+highlight pile-up.

### 70. S113 — Same Target, Different Sampler [I; baseline 86; judgment]

- **Must / point:** End on the central change-of-measure identity.
- **Main:** Keep the existing equation closer, not an extra summary or lesson-duration claim. No requirement to add a visible h2 title if the closer pattern does not have one.
- **Exhibit and H/M:** Existing end-slide; H/M short explanation with coverage/integrability conditions.
- **Evidence/decision:** E04/B04. **Layout:** end-slide. **Time:** not budgeted (C13).
- **Accept:** One global recap only; closer identity and scope agree with theorem.

## Retirements — must, with active companion removal

Author-requested topic deletion is different from moving crowded detail to notes. Remove these D slides, paired H articles and M sections, their TOC anchors and now-orphaned references. Do not leave a hidden gradient chapter. Historical files remain in git. No new tech deck or wholesale deletion of unrelated generator files is requested.

| Baseline page | ID | Baseline title | Owner / reason |
|---:|---|---|---|
| 13 | S33 | The Rate Is Not the Cost | P1 / C03 |
| 14 | S37 | Tensor Grids Grow With Dimension | P1 / C03 |
| 55 | S83 | Differentiate Expectations | I / C11 |
| 56 | S84 | The Distribution Now Changes | I / C11 |
| 57 | S85 | Frozen Samples Hide the Derivative | I / C11 |
| 58 | S123 | A Gaussian Sample Is a Recipe | I / C11 |
| 59 | S124 | Differentiate Along the Sampling Path | I / C11 |
| 60 | S125 | Check the Gaussian Gradient | I / C11 |
| 61 | S126 | Discrete Draws Need Another Route | I / C11 |
| 62 | S86 | The Log-Derivative Identity | I / C11 |
| 63 | S87 | Reward Times Score Gives the Gradient | I / C11 |
| 64 | S88 | Proof: Expand the Expectation | I / C11 |
| 65 | S89 | Proof (continued): Differentiate the Finite Sum | I / C11 |
| 66 | S90 | Proof (continued): Read an Expectation | I / C11 |
| 67 | S92 | Average the Gradient Contributions | I / C11 |
| 68 | S93 | A Two-Action Policy | I / C11 |
| 69 | S94 | Both Routes Give the Same Derivative | I / C11 |
| 70 | S96a | The Score Has Mean Zero | I / C11 |
| 71 | S96b | A Valid Baseline Preserves the Gradient | I / C11 |
| 72 | S97 | This Baseline Removes the Toy’s Variance | I / C11 |
| 73 | S127 | A Bad Baseline Adds Variance | I / C11 |
| 74 | S128 | Two Gradient Estimators, Different Requirements | I / C11 |
| 85 | S109b | Choose a Gradient Estimator by Its Requirements | I / C11 |

## Packages and dependencies

These are ownership boundaries, not permission for additional agents to edit shared surfaces independently. slides chooses how to implement and integrates once. No package edits a neighboring package's IDs.

| Package | Owned IDs / contiguous baseline range | Files and notes | Dependencies |
|---|---|---|---|
| **P1 Motivation and MC clarity** | NewS130/S131 afterS03; S04,S06,S26,S16,S19,S22,S114,S115,S24; deleteS33/S37; splitS116→a/b | Owned D/H/M sections; `gen/p9a_part01.py`; corresponding existing/local figures only | E01/E03/E09/E10; leaves dividers/Contents to I |
| **P2 Importance contributions and proposal risk** | S43 through S69 in baseline order, including S54; excludes shared dividerS55; S63/S69 split intoa/b | Owned D/H/M sections; `gen/p9b_calc.py`, `gen/p9b_figs.py`; local p9b figures | Uses P1's error vocabulary and generic rare-event setup, not duplicate exact numbers; definitionsp,q,f,w,mu remain consistent |
| **P3 Unknown Z and SNIS** | NewS132 beforeS73; S73,S74,S75; newS133 afterS75; S76,S77,S78,S122,S70,S79,S81,S82 | Owned D/H/M sections; `gen/p9c_snis_examples.py` only if necessary; new `gen/p9f_unknown_z.py`; associated local figures | Uses P2's weights and support distinction; sampling template/notation from P1 |
| **P4 RL application retained** | S100,S101,S102,S103,S129,S105,S106,S104 | Owned D/H/M sections; existing local p9e generators/figures only if the changes require it; retain sourced PPO crops | Reuses MC/IS concepts only; cannot depend on deleted gradients |
| **I Shared integration** | S01,S02,S03,S41,S55,S72,S99,S109a,S113; all C11 retirements including S109b; shared cross-references and navigations | D/H/M shared surfaces; Deepmath/root outline pointers; job records | Runs after P1–P4; recompute actual ranges/counts, do not adjust by assumed70 |

Global wording normalization to IID (or iid in math consistently) is an integration pass within D/H/M, not permission to touch earlier lectures. Shared numbering and source-reference cleanup happen once. If a package needs an extra clarity split, use inherited split IDs or the next unused new ID and report the resulting mapping; never borrow a retired ID.

### Reproducibility / sources

- P1 extends the existing exact arithmetic for the newrho=.001 examples. No random numbers needed. Preserve moved plot’s generator/source provenance and the endpoint/monotonicity qualifications.
- P2 records parameters and exact formulas for all revised contribution/variance diagrams. S63 illustrative locations must say schematic; any actual random draw needs a seed. Existing generator ownership stays local.
- P3 creates the planned unknown-Z calculation generator. Include model definition, deterministic quadrature reference inputs from E07 if used, and stable evaluation of logistic powers. Numeric reference values are checks, not SNIS inputs. If showing a random-batch estimate, record seed, n and IID proposal law; hand-picked points must not masquerade as an empirical MC experiment.
- P4 keeps the historical source versions/crops and prior checked toy generators. No claim about present-day model performance or a new benchmark.
- Report actual generators and inputs used, not just planned paths. Owner appends the verified provenance to evidence after work report. No new external facts should be invented to fill space; flag unresolved claims.

## Shared integration acceptance

1. **Scope:** no gradient-estimation chapter, gradient recap, title promise or dangling gradient derivation. S106 and PPO notes remain understandable independently. Legitimate “gradient” in paper titles may remain; avoid indiscriminate string deletion.
2. **Time:** remove now-obsolete pace/duration lines from dividers, front matter, notes and outline. No target120/150-minute promise; no extra content to make the deck longer. Shorter is fine; type is never shrunk to make it shorter.
3. **Narrative:** read only titles and verify five-part argument. Part02 endsS54, Part03 beginsS55. Practical usable proposal precedes oracle; normalizer model precedes abstractSNIS; RL remains afterSNIS. Only one global closing recap.
4. **Mapping:** D slide IDs, H article IDs and M section IDs match one-to-one in order. Titles, links, removed anchors, navigation and alternate format descriptions agree. Report oldpage→ID→newpage for every original ID, plus new/split/retired status.
5. **Outline:** update actual `courses/deepmath/OUTLINE.md` section/theorem pointers, prerequisites, companions, generator descriptions and all count locations. Remove the policy-gradient/score-function theorem claim for this lecture. Root updates only when a current prob09 pointer actually becomes stale; no broad cleanup.
6. **Review:** main plot answer, notes Message, explanation, details and source agree on every changed slide. Copy precise evidence locators rather than generic bibliographies. No lost content when detail was moved to notes, and no hidden retained chapter where author requested deletion.
7. **Checks:** run relevant lints and generator checks; render the integrated deck and inspect changed/new slides plus neighbors at final size. View H notes in a real narrow/mobile viewport as well as desktop; no article horizontal overflow, clipped math limits or scroll-hiding workaround. Verify diagram labels, axes and meaningful line breaks visually; lint alone cannot accept them.

## Handoff and review record

Copy owner `job.md`, append-only requests/evidence and both plan versions unchanged into the **new** tracked job folder on existing PR77 branch. Do not rewrite prior approved frozen records. Work-r1 reports branch/headSHA, package work, every ID/page mapping, deviations with reasons, unresolved source/plan issues, actual generator parameters and checks/render coverage. State any further author instructions received directly before applying incompatible changes.

Send only the completed pointer: `job 2026-11-18-prob09-clarity-trim: work-r1.md ready — in-review · <exact SHA>`. The owner reviews that commit, not a working tree. No pacing issue by itself is a blocker after C13. Required content/factual/scope changes still return to the owner. After approval and pushed-record verification, owner updates existing PR77 rather than opening another. Never merge without Albert's direct order.
