# plan-v1 — Scope, evidence and revised argument for Albert's approval

**Job:** 2026-11-18-prob09-clarity-trim  
**Baseline:** 5f4b1d99c5d799785752aa12c494715c3b21327b, 86 pages in existing PR #77  
**Status:** stages 1–3 proposal only; **not a work order**. Full slide-level specifications/packages follow in plan-v2 after Albert approves the resulting scope and pacing.

## Summary

Refocus the lecture on estimating expectations with Monte Carlo and importance sampling. Connect the calculation to familiar cross-entropy and generative-model evaluation before the machinery. Remove the two dimension/cost detours and the entire gradient-estimation chapter as requested, but preserve the RL importance-sampling application. Spend the recovered time on the explanations Albert found unclear: rare-event relative error, what a weighted contribution means, zero variance, proposal tails and an actual unknown-normalizer posterior.

The proposed result is **five parts, approximately 71 slides and 120 minutes**, rather than the earlier six-part, 86-slide, 150-minute version. Counts are targets, not caps. Keep the existing PR #77 and its branch; this is a proposed existing-PR continuation exception to the new-job branch-naming convention, not a second overlapping PR. No build, branch change, PR update or merge is authorized by this proposal alone.

## Stage 1 — Audience, objectives, boundaries and cutoff

### Audience and teaching mode

Junior undergraduate AI majors following prob01–prob08. Retain the current rigorous, example-led approach. Students already know expectation, sample means, variance, concentration, KL/cross-entropy, likelihood, Bayesian proportionality and Gaussian distributions. Recall those ideas by name when needed rather than re-teaching their derivations.

### Learning objectives

By the end, students should be able to:

1. Recognize an ML quantity as an expectation and identify the distribution that supplies its samples.
2. Distinguish estimator standard error, realized error and relative error in rare-event estimation.
3. Explain why changing a sampler requires weights, and separate support coverage from finite-variance requirements.
4. Interpret zero-variance importance sampling as constant **weighted contributions**, not deterministic sample locations or a free oracle.
5. Use self-normalized importance sampling when a target density is known only up to a normalizer, while recognizing bias and diagnostic limits.
6. Explain the role and limitations of importance weights when reusing data from an old RL policy.

### Fixed author decisions and exclusions

- Delete baseline pp13–14, S33/S37, rather than disguising them as new motivation pages.
- Delete the whole baseline Part05, pp55–74, plus its gradient-only recap S109b. No pathwise/score-function/baseline tutorial remains in the active notes as a hidden chapter.
- Keep baseline Part06, pp75–83, as the new Part05. Its objective-estimation and data-reuse story must stand without the removed gradient prerequisites.
- No new MCMC, quasi-Monte Carlo, policy-gradient/PPO derivation, current-model survey or independent optimization lecture.
- No edits to prob01–prob08, global design rules, shared scripts or reference library. Update only necessary course-outline pointers for this changed lecture.
- Mathematical claims and diagnostics that survived the previous review remain qualified; do not trade correctness for fewer lines. Preserve the IS and optimal-proposal proof thread.

### Survey boundary

Cutoff 2026-11-18. This is a teaching clarification of established material, not a frontier survey. Reuse the prior job's verified sources, current prob02/prob07 foundations, Owen's MC text, and the cited historical RL papers. New Bayesian toy calculations are labelled as ours. Evidence access limitations are recorded in evidence.md, not concealed.

## Stage 2 — Evidence and request coverage

Paths abbreviated below: **D** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`; **H/M** = sibling `prob09-monte-carlo-note.html` / `prob09-monte-carlo-note.md`. Every retained or added slide has corresponding H/M material. These are content and wording judgments, not instructions for context-free mechanical editing.

| Comment | Baseline page / title / ID | Proposed treatment and reason | Evidence | Future package |
|---|---|---|---|---|
| C01 | Opening pp3–4, S03/S04 | [judgment] After S03, add a one-hot CE/KL recall and a population-loss-to-sample-average example; make S04 a concrete sampled-generation evaluation. Identify data samples versus model samples. Motivation is why an expectation must be computed, not another KL proof. | E01/E02/E09 | P1 |
| C02 | p10, Estimating the Error Bar, S114 | Expand SE to **standard error** and define it as the SD of the estimator across repeated samples. Distinguish it from outcome SD and actual error; show estimated SE with its sampling/variance conditions. | E03 | P1 |
| C03 | p13 The Rate Is Not the Cost, S33; p14 Tensor Grids Grow With Dimension, S37 | Delete both slides and their active companion entries. Remove cross-references rather than relocating the detour. | Author decision | P1/integration |
| C04 | p15 Rare Events Need Relative Error, S116 | [judgment] Split into a concrete rare-event miss, relative RMSE/expected hits, then the existing trend plot. Explain absolute versus relative error before formulas; retain the later exponential example as the applied IS thread. | E03 | P1 |
| C05 | p27 More Tail Visits, Corrected Weights, S118 | Name f(x)w(x) as **one weighted contribution** and mu as the **target mean**. Explain the horizontal line and averaging under q; more tail hits alone do not prove lower variance. | E04 | P2 |
| C06 | p33 Follow the Weighted Integrand, S57 | [judgment] Make the single message “sample where contributions matter.” Emphasize p versus the two-lobed absolute weighted integrand; move the secondary signed curve/derivation to the notes. Preserve the signed-integrand limitation. | E04 | P2 |
| C07 | p37 One-Sign Integrands Permit Zero Variance, S63 | [judgment] Split intuition and identity: random X values can map to identical Y=f(X)w(X); therefore the estimator has zero variance. Retain the one-sign assumption and immediately adjacent oracle-normalizer limitation. Distinguish true zero variance from zero empirical spread after no rare hits. | E05 | P2 |
| C08 | p42 Check the Integrand, Not Just Weights, S69 | [judgment] Separate the helpful heavy-tail example from the rule. Explicit answer: **q need not always be heavier-tailed than p**. A lighter Exp(1.5) proposal still has finite variance; coverage and the f-dependent second moment are the checks. | E06 | P2 |
| C09 | p44 The Target Is Known Up to Z, S73 | [judgment] Introduce a logistic-normal Bayesian posterior just before S73; return to it after normalization to compute a posterior predictive probability with likelihood weights and no Z. | E07 | P3 |
| C10 | p48 The Ratio Converges to the Target, S77 | Replace “Iid” with “IID”; standardize this acronym in touched deck/notes text. Preserve existing convergence assumptions and finite-sample bias caveat. | E01 / existing reviewed result | P3 |
| C11 | pp55–74, S83–S128 in baseline order; p85 S109b | Delete the gradient chapter and its recap; remove promises, stale bridges and gradient-only note/outline content. Do not delete unrelated IS theorems or their assumptions. | Author decision | integration |
| C12 | pp75–83, S99/S100/S101/S102/S103/S129/S105/S106/S104 | [judgment] Preserve and renumber as Part05: old-policy reuse, sequence ratios, mismatch, behavior/reference roles, KL and clipping limitations. Rewrite S106 as an objective-estimation application, not a gradient toolkit. Briefly explain advantage without restoring the removed chapter. | E08 | P4 |

## Stage 3 — Argument, title sequence and pacing

### One argument

**ML objectives are expectations → sample averages have sampling error → change the sampler without changing the target → inspect weighted contributions and proposal risk → cancel an unavailable normalizer → reuse policy data responsibly.**

The lecture now answers one question throughout: “How can we estimate this expectation reliably with the samples and density information we have?” It no longer promises to teach how to differentiate that expectation.

### Time budget

| Segment | Intended role | Target slides | Minutes |
|---|---|---:|---:|
| Part01 — Estimate an Expectation | ML motivation, MC recipe, error, rare events | 17 | 25 |
| Part02 — Change the Sampler | Practical exponential IS, identity, support, comparison | 14 | 25 |
| Part03 — Control Proposal Risk | Contribution-focused proposals, oracle, zero variance, tails | 15 | 25 |
| Part04 — Remove the Normalizer | Concrete posterior, SNIS, bias, ESS, capability limits | 14 | 25 |
| Part05 — Reuse Samples in RL | Policy-data reuse and safeguards | 9 | 15 |
| Closing | Expectation-estimator choice and final identity | 2 | 5 |
| **Total** | Teaching time, excluding any break | **71** | **120** |

A natural pause is after Part03 (75 minutes); no forced equal-length session split. Author approval of the 120-minute pacing is requested. If the course slot must remain 150 minutes, use a revised time budget before building rather than silently adding topics or exercises.

### Proposed title sequence

The following is an argument/title proposal, not a layout mandate. Old page numbers remain the request baseline; new positions are provisional. New IDs S130–S133 are proposed from the next unused numbers. Splits retain their parent identity; no existing ID is renumbered. Original titles may be improved by slides provided the required point and scope remain unchanged.

#### Part01 — 25 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 1 | S01 | 1 | Monte Carlo & Importance Sampling |
| 2 | S02 | 2 | Contents |
| 3 | S03 | 3 | Estimate an Expectation |
| 4 | S130 | new after S03 | One-Hot Cross-Entropy Is a KL Loss |
| 5 | S131 | new after S130 | Population Loss Requires an Average |
| 6 | S04 | 4 | Sampled Generations Estimate Model Quality |
| 7 | S06 | 5 | Sample, Evaluate, Average |
| 8 | S26 | 6 | Six Points Illustrate the Recipe |
| 9 | S16 | 7 | Monte Carlo Reuses the Sample Mean |
| 10 | S19 | 8 | Unbiased Does Not Mean Accurate |
| 11 | S22 | 9 | Averaging Reduces RMSE |
| 12 | S114 | 10 | SE Measures Estimator Spread |
| 13 | S115 | 11 | Approximate Intervals, Exact Guarantees |
| 14 | S24 | 12 | Bounded Averages Concentrate |
| 15 | S116a | 15 split | Small Absolute Error Can Hide Failure |
| 16 | S116b | 15 split | Relative RMSE Counts Expected Hits |
| 17 | S116c | 15 split | Rarer Events Have Larger Relative Spread |

#### Part02 — 25 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 18 | S41 | 16 | Change the Sampler |
| 19 | S43 | 17 | Most Draws Miss the Tail |
| 20 | S44 | 18 | A Rare Event Needs Many Samples |
| 21 | S45 | 19 | Visit Useful Outcomes More Often |
| 22 | S50 | 20 | Correct Each Visit’s Weight |
| 23 | S46 | 21 | Importance Sampling Preserves the Target |
| 24 | S47a | 22 | Proof: Cancel the Proposal |
| 25 | S47b | 23 | Proof Continued: Check the Missing Region |
| 26 | S48 | 24 | Missing Support Cannot Be Repaired |
| 27 | S49 | 25 | Average the Weighted Integrand |
| 28 | S117 | 26 | A Practical Exponential Proposal |
| 29 | S118 | 27 | Average Weighted Contributions to Estimate the Target |
| 30 | S119 | 28 | Compute the Proposal’s Error |
| 31 | S120 | 29 | Same Target, Less Relative Error |

#### Part03 — 25 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 32 | S54 | 30 | Coverage and Variance Are Different |
| 33 | S55 | 31 | Control Proposal Risk |
| 34 | S56 | 32 | The Second Moment Decides |
| 35 | S57 | 33 | Sample Where Contributions Matter |
| 36 | S59 | 34 | The Optimal Proposal |
| 37 | S60 | 35 | Proof: A Common Lower Bound |
| 38 | S61 | 36 | Proof Continued: Attain the Bound |
| 39 | S63a | 37 split | Random Draws Can Give Identical Contributions |
| 40 | S63b | 37 split | Constant Contributions Give Zero Estimator Variance |
| 41 | S64 | 38 | The Oracle Needs a Normalizer |
| 42 | S66 | 39 | Light Tails Can Destroy Variance |
| 43 | S68 | 40 | A Finite Mean, an Infinite Second Moment |
| 44 | S121 | 41 | Consistency Is Not an Error Bar |
| 45 | S69a | 42 split | A Heavier Proposal Helps This Integrand |
| 46 | S69b | 42 split | Heavier Tails Are Not a Requirement |

#### Part04 — 25 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 47 | S72 | 43 | Remove the Normalizer |
| 48 | S132 | new before S73 | Bayes Leaves a Normalizing Integral |
| 49 | S73 | 44 | The Target Is Known Up to Z |
| 50 | S74 | 45 | Compute Unnormalized Weights |
| 51 | S75 | 46 | Normalize Only a Positive Total |
| 52 | S133 | new after S75 | Likelihood Weights Remove the Unknown Z |
| 53 | S76 | 47 | Two Averages Form One Ratio |
| 54 | S77 | 48 | The Ratio Converges to the Target |
| 55 | S78 | 49 | One Draw Exposes SNIS Bias |
| 56 | S122 | 50 | Normalization Does Not Guarantee Improvement |
| 57 | S70 | 51 | One Draw Can Dominate the Weights |
| 58 | S79 | 52 | Effective Sample Size Summarizes Imbalance |
| 59 | S81 | 53 | Healthy ESS Can Miss Missing Support |
| 60 | S82 | 54 | What You Can Compute Decides What Is Available |

#### Part05 — 15 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 61 | S99 | 75 | Reuse Samples in RL |
| 62 | S100 | 76 | Old Samples, a New Target |
| 63 | S101 | 77 | Importance Weights Correct the Mismatch |
| 64 | S102 | 78 | Sequence Ratios Multiply |
| 65 | S103 | 79 | Compounding Mismatch Can Destroy Efficiency |
| 66 | S129 | 80 | Behavior and Reference Are Different Roles |
| 67 | S105 | 81 | KL Is Not a Variance Certificate |
| 68 | S106 | 82 | RL Objectives Contain Expectations |
| 69 | S104 | 83 | A Surrogate Is Not a Hard Constraint |

#### Closing — 5 minutes

| New position | Stable ID | Baseline page | Proposed title |
|---:|---|---|---|
| 70 | S109a | 84 | Choose an Expectation Estimator by Its Requirements |
| 71 | S113 | 86 | Same Target, Different Sampler |

### Critical teaching exhibits (to be specified fully in plan-v2)

1. **S130/S131/S04 — motivation.** At a fixed labelled input, one-hot CE is exactly KL to the classifier's label distribution. Then a fixed classifier's population loss is an expectation over labelled data, approximated by a mean of IID per-example losses. Keep the general entropy-plus-KL decomposition in notes so the exact one-hot statement is not generalized incorrectly. In the generative example, explicitly switch to outputs sampled from the model and average a specified reward/evaluation function. These are different target distributions, not interchangeable samples. E01/E02/E09.
2. **S116a–c — rare events.** Use probability rho=.001 and n=1000: only one expected hit, about37% chance of no hits. A zero estimate has small absolute error but100% relative error. Then explain relative RMSE approximately1/sqrt(n*rho), exact conditions and10%-relative-RMSE sample count99,900. The existing per-draw spread plot follows, with its fixed-n scaling and restricted rho range clear. These are RMSE statements, not guarantees about one run or confidence levels. E03.
3. **S118/S57 — what to look at.** The weighted contribution is Y=f(X)w(X); mu is its mean under q. On the Gaussian f=x exhibit, the important magnitude lies in two lobes of |x|p(x), not at the density's central peak. The main image should convey that allocation message without three competing stories. A one-line reading of each plot belongs on the slide and in the notes. E04.
4. **S63a/b — zero variance.** Different sampled X values from10+Exp(1) all yield Y=exp(-10). Var(X)=1 but Var(Y)=0, so any sample average of Y has variance0. This is true constancy under the oracle proposal, not merely a sample with no observed variation. The general nonnegative-f identity and the unknown-normalizer caveat follow immediately; sign-changing f is not claimed to have zero variance. E05.
5. **S69a/b — tails.** For p=Exp(1), f=x, the Exp(.5) proposal improves variance from1 to5/27. But Exp(1.5), lighter than p, still has finite variance29/3. The criterion is coverage plus a finite f-dependent weighted second moment, not a universal instruction to choose heavier tails. Retain the previous infinite-variance example without repeating its entire integration. E06.
6. **S132/S133 — unknown Z.** A Gaussian prior for a logit and two observed successes give posterior proportional to phi(theta)s(theta)^2. The target is the posterior chance of another success. Sampling from the prior yields likelihood weights s(theta)^2 and an estimate sum s^3 / sum s^2. Z is not needed. Define every model symbol and the observation before the ratio; exact numerical quadrature, if used, is a validation reference in the notes, not an estimator input. This is our small Bayesian example, not a claim about Stan using IS. E07.
7. **S99–S104 — RL.** Preserve the behavior-policy/target-policy change of measure and the distinction from the reference policy in a KL term. Keep token chain-rule and toy independence conditions separate. Rewrite the reward/KL objective bridge as quantities to estimate; do not claim importance sampling by itself supplies an RL optimizer. The PPO figure illustrates clipping's limitations, not a hard ratio bound; explain advantage briefly without restoring the deleted gradient derivation. E08.

### Removed IDs and dependent material

Delete S33, S37; S83, S84, S85, S123, S124, S125, S126, S86, S87, S88, S89, S90, S92, S93, S94, S96a, S96b, S97, S127, S128; and S109b. This is23 baseline slides removed. Four new slides and four extra split slides give the71-slide target. Source and historical notes remain recoverable in git; unused generator files do not need arbitrary deletion just because a chapter is retired.

Integration must update the S01 subtitle/objectives, S02 Contents, section numbering, S03 scope, the transition from SNIS to RL, S106 toolkit language, S109a/closing, both companion contents and all internal page/ID links. Remove stale gradient promises and references without stripping valid “optimization” or “gradient” mentions from unrelated bibliographic titles. Audit root `OUTLINE.md` only for stale prob09 pointers; the authoritative Deepmath leaf is `courses/deepmath/OUTLINE.md`, not a nonexistent prob09-local OUTLINE.

## Stage 4 handoff boundary — after approval only

After Albert approves stages1–3, plan-v2 will open with the approved decisions and give every changed/split/new slide its point, content/qualifiers, exhibit reading, evidence, note-versus-slide allocation, acceptance check and teaching time. It will name every deleted/unchanged ID and define four disjoint content packages plus shared integration. Workers may split slides further or choose better layouts; substantive changes to argument, facts, scope or teaching time return to the owner.

All visible claims must remain traceable. Every surviving slide gets a brief message first, then a plain explanation of its diagram/equation, then source and minor details in both lecturer companions. No source-only jargon is allowed to replace an answer to Albert's questions. Verify new calculations through the tracked local generators, HTML/Markdown parity, ID and outline mapping, default-type capacity, and real rendered pages/notes including narrow mobile. The previous approval is not approval of these new changes.

On build completion, review the named commit against this baseline, Albert's twelve comments, evidence and current design rules. Up to three review rounds for this new structural author request; do not reuse the completed prior job's round numbers. Approved follow-up updates the existing PR77 description and reviewed-commit record after pushed-log verification. Merge still requires Albert's direct order.
