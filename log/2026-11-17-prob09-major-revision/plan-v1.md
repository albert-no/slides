# prob09 major revision — stages 1-3 for Albert's approval

**Status: complete approval proposal; NOT a build order.** Full slide-level specifications and executable packages follow in plan-v2 after Albert approves this scope, evidence map and argument. Nothing in this proposal authorizes slides to start rebuilding yet.

Job: `2026-11-17-prob09-major-revision`  
Baseline: `b20ab73ac7e74e9489d379cf9caad7565f17e31e`  
Deck: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`  
Companions: same stem with `-note.html` and `-note.md`  
Shared surface: `courses/deepmath/OUTLINE.md`, prob09 entries only unless this revision makes an ancestor pointer stale.

## Decision summary

The current deck has good mathematical ingredients but spends too long reintroducing sample averages and then compresses its genuinely new practical choices. Keep the importance-sampling support counterexample, optimal-proposal proof, infinite-variance warning and two-action gradient example. Rebuild the argument around **the same target, different estimators, different error**.

Three main changes:
1. Replace the front-loaded toolkit and repeated sample-mean theorem arcs with just-in-time recalls, worked estimation and usable error interpretation. Remove duplicate roadmaps/proof recaps/end-of-course summaries.
2. Make proposal design real: a useful non-oracle proposal before the zero-variance oracle, an actual SNIS bias example, and a sharp separation of validity, variance and diagnostics.
3. Reconnect to the revised Gaussian/estimation lectures: show pathwise versus score-function gradients, correct baseline and policy-ratio overclaims, and rebuild both note formats rather than merely polishing slide prose.

## Stage 1 — audience, objectives and scope

### Audience and teaching mode

- Established course audience: junior undergraduate AI majors. Rigorous mathematical lecture, with concrete examples before abstraction and full on-slide proofs for the genuinely new central results.
- Preserve the course's slow, complete explanation of new mathematics. Removing redundancy does not mean deleting necessary hypotheses or collapsing a proof into an unexplained formula.
- Proposed duration: **150 minutes, organized as two 75-minute teaching blocks**, not a claim about Albert's timetable. This is an approval item. No duration was supplied in the request.
- Planning target: approximately **85-100 slides rather than 113**, not a cap or acceptance condition. Readability and complete logical steps take priority; stage-4 slide targets may change after the ID mapping and note migration are resolved.

### Learning objectives

By the end a student should be able to:
1. Identify target expectation, sampling distribution, observable integrand and the error quantity being controlled.
2. Apply established averaging/concentration results to Monte Carlo without treating them as new theorems; distinguish RMSE, estimated standard error and a probability guarantee.
3. Derive importance sampling, test support coverage and evaluate the variance consequences of a proposal.
4. Explain why self-normalization removes Z, what finite-sample bias/undefined denominators mean, and why ESS is only a diagnostic.
5. Derive a score-function gradient, connect the Gaussian construction to a pathwise gradient, and explain what a baseline can and cannot change.
6. Recognize the separate roles of the current, behavior and reference policies in a deliberately limited RLHF example.

### Inclusions / exclusions

**In:** Monte Carlo, error interpretation, one short dimension comparison, ordinary IS and optimal proposal, finite/infinite variance, SNIS and ESS, score-function proof, short Gaussian pathwise connection, baselines, off-policy identity, one scoped reward-plus-KL application. Slides, per-slide instructor notes, accessible Markdown, reproducible instructional figures, accurate outline.

**Out:** rewriting prob01-prob08; a new survey of frontier models; MCMC algorithms; particle-filter mechanics; a quasi-Monte Carlo chapter; general stochastic-process policy-gradient theory; a PPO tutorial; DPO/GRPO/RLVR expansion; a new technical-supplement deck; global design-rule or agent-model configuration changes. Existing advanced notes may retain useful material with corrected assumptions and provenance, but cannot silently expand the teaching time.

**Survey cutoff:** 2026-11-17. Foundational sources plus targeted verification of the existing RLHF hook; not a claim of exhaustive literature coverage through that date. E01-E16 are the initial evidence map.

### Approval requested

Approve the audience/mode, 150-minute pacing proposal, scope/exclusions, evidence basis and six-part argument below. If the available slot is materially shorter, revise the scope before writing the build plan; do not ask slides to compress the same mathematics into smaller type.

## Stage 2 — evidence and course-continuity map

All repository references below are pinned to the baseline, not moving main. Detailed source setups and limitations are in evidence.md.

### Prerequisites: reuse, adapt, or defer

| Earlier deck / exact baseline location | What it already established | prob09 action |
|---|---|---|
| `courses/deepmath/prob01-foundations/prob01-foundations.html`, pp21-22 L458/L471; p53 L1078 | Expectation of a function; Jensen and strict equality case | **Reuse** in short recalls at the average/optimal-proposal steps. No probability/entropy/Jensen lesson. |
| `courses/deepmath/prob02-kl-crossentropy/prob02-kl-crossentropy.html`, p26 L452, p32 L550, p82 L1328 | KL orientation and support sensitivity | **Reuse/adapt** only at policy drift. Explicit natural logs/nats, rather than silently inheriting earlier bits. Do not claim KL bounds the weight second moment above. |
| `courses/deepmath/prob03-mutual-information/prob03-mutual-information.html`, pp13/15 L297/L326, p89 L1464 | Linearity without independence, factorization under independence, continuous KL | **Reuse** when needed. **Defer** entropy/MI/DPI; none needs another treatment in prob09. |
| `courses/deepmath/prob04-random-processes/prob04-random-processes.html`, p19 L408, p25 L495 | General chain rule; context-dependent token factors | **Reuse** for sequence weights, distinguishing autoregressive dependence from an explicitly independent toy. **Defer** Markov/stationary re-teaching and MCMC. |
| `courses/deepmath/prob05-concentration/prob05-concentration.html`, p39 L661, p46 L776, p93 L1473 | Variance of an IID mean, weak LLN, CLT; strong LLN named | **Reuse**, not new theorem/proof arcs. **Adapt** to Y=f(X); distinguish first/second moment conditions, approximate intervals and actual guarantees. |
| `courses/deepmath/prob06-generalization/prob06-generalization.html`, p8 L215, p14 L346, p18 L632, p35 L895 | IID/fixed-class assumptions; fixed versus data-selected estimands; [0,1] Hoeffding and simultaneous control | **Reuse/adapt** via Y=(f-a)/(b-a); no Hoeffding/union-bound proof. One relevant warning: reusing evaluation draws to choose a policy/integrand is not a fresh fixed-function guarantee. |
| `courses/deepmath/prob07-estimation/prob07-estimation.html`, p12 L317, p98 L1687, p102 L1768, p121 L2086, p123 L2122 | Tower, bias-variance, unbiased sample mean, exact autoregressive likelihood, CE training versus reward tuning | **Reuse**. Do not advertise unbiasedness or sigma^2/n as new mathematics. Keep SFT/MLE and reward-tuning distinct; do not reintroduce removed GAN/JS content. |
| `courses/deepmath/prob08-gaussian/prob08-gaussian.html`, p37 L835, p93 L1822, p110 L2090, p126 L2372, p153 L2947 | Gaussian construction, affine versus conditional mean, sampling a pair, reverse-mixture distinction, MC bridge | **Adapt** X=DW+mu into the short pathwise-gradient bridge. Do not imply all Gaussian expectations close, all reverse conditionals are Gaussian, or affine means linear. |

Cross-folder decision: root outline and `courses/privacy/lectures/02-generative/OUTLINE.md` were checked. The latter's diffusion score is a derivative with respect to the sample, whereas this lecture's likelihood score is with respect to parameters. Explain that distinction if “score” is cross-referenced; do not import the graduate diffusion proof sequence. `diffusion2-ddpm.html` is a rhythm exemplar, not a source of extra prob09 scope.

### Evidence-to-argument coverage

| Part | Required evidence | What is new versus recalled |
|---|---|---|
| 1: Estimate an expectation | E01-E03 | New computational use/error interpretation; old sample-mean results |
| 2: Change the sampler | E04,E11 | New identity, support test and practical proposal |
| 3: Control proposal risk | E04,E06 | New optimal-proposal argument and integrand-dependent variance |
| 4: Remove the normalizer | E05,E06,E12 | New ratio estimator and honest diagnostic interpretation |
| 5: Differentiate expectations | E07,E08,E13,E15 | New score/pathwise identities and baseline use, grounded in existing Gaussian construction |
| 6: Reuse samples responsibly | E09,E10,E14 plus E01 chain rule/KL | Application of IS and gradient tools; not a full RL algorithm |
| All notes | E01,E16 and each content source | Source-aligned message/explanation/details; accessible companion remains standalone |

### Audit decisions: concrete changes

These are planning findings, not a review verdict or a consumed review round. Each item is numbered and self-contained. Paths are explicit; lines refer to the frozen baseline. All displayed fixes must also reach the corresponding explanations/details and accessible Markdown.

1. **[judgment: narrative]** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`, pp4-16 L149-L349. Current: three sweeping “nobody can compute” claims, repeated promise/route map/target/definition, then a standalone recall section. **Replace with one motivated task, a worked sample estimate and just-in-time recalls.** Reason: the revised series already introduced expectations and the MC bridge; open with the new computational problem, not another course introduction.
2. **Fact/continuity.** Same deck, p5 L173 and p112 L1738. Current: “Every integral closed,” “Non-Gaussian p, nonlinear f: no antiderivative,” and “estimate any expectation and bound the error.” **Replace with scoped statements about expectations without convenient closed forms and estimates under stated sampling/moment conditions; remove antiderivative vocabulary and the universal ending.** Reason: these claims exceed both probability theory and prob08's revised bridge.
3. **[judgment: redundancy]** Same deck, pp10-12 L268-L298 and pp17-24 L363-L451. Current: recall sample-mean variance, then theorem/proof arcs for the same mean/variance and Chebyshev/Hoeffding. **Use Y=f(X) to apply prior results; keep concise derivation/substitution and one error interpretation example, not duplicated theorem architecture.** Reason: prob05 p39 and prob07 p102 already do this calculation; the new problem is choosing the sampler.
4. **[judgment: teaching]** Same deck, pp25-30 L462-L546. Current: six slides of darts/arithmetic/bound tables. **Retain the geometric sampling example, move the six-coordinate ledger and full two-bound arithmetic to notes; spend the saved space on estimated uncertainty versus an actual guarantee.** Reason: a lecturer needs to explain what can be inferred from one run when the exact variance is unknown. Do not present a CLT interval as a finite-sample guarantee.
5. **Fact plus [judgment: scope].** Same deck, pp33-40 L583-L701; HTML note §§4.1-4.5 L162-L185. **Reduce to the useful tensor-grid comparison with fixed-variance/evaluation-cost/smoothness qualifiers; delete “grids are ruled out at d≈10” and unqualified escape-from-dimension language.** Reason: rates do not bound variance, computational cost or all competing quadrature methods. Correct note §4.5: the rare indicator has small absolute variance, but large relative error.
6. **[judgment: pedagogy]** Same deck, pp43-54 L742-L899. **Teach a feasible proposal (E11) and its nonzero error before the shifted-exponential zero-variance example.** Reason: the current transition goes from millions of samples directly to an exact answer and never shows a usable middle ground. Keep all gains explicitly toy/RMSE-based, not measured runtime or confidence guarantees.
7. **Fact.** Same deck, p46 L774, p59 L961, p64 L1027; note §§5.2,6.4-6.5. **Make first-moment assumptions explicit; use 0<c=E|f|<infinity for the optimal theorem; replace “Sampling q* exactly = already done” with the normalized-weight/unknown-c obstruction.** Reason: the issue is not a universal inability to sample an unnormalized distribution. Preserve the support counterexample on p48.
8. **Fact.** Same deck, pp68-71 L1077-L1130; note §§6.6-6.7 L301-L326. **Say infinite RMSE/no finite standard RMSE rate; separate large sampled weight imbalance from proof of infinite variance.** Replace “one sample carries 95% of the estimate” by “95% of the normalized weight”; actual contribution also depends on f. Reason: even finite-variance proposals can produce an imbalanced batch, and an unobserved bad tail may produce none. Drop note claims that every finite batch must be dominated or variance degrades gracefully.
9. **Fact plus [judgment: example].** Same deck, pp75-78 L1174-L1217; note §§7.2-7.5 L338-L360. **State positive sampled denominator, 0<Z<infinity and needed support/integrability; replace the generic random-ratio example with E12's actual SNIS computation.** Use “generally biased,” not “biased at every finite n”; remove unconditional O(1/n) and lower-variance promises from the short summaries. Reason: the present example does not itself demonstrate bias of this estimator and the exceptions matter.
10. **[judgment: continuity]** Same deck, pp84-95 L1296-L1436; note §10.2 L564. **Bring a short Gaussian reparameterization comparison onto the main deck before choosing the discrete/black-box score-function route.** Reason: prob08 now gives a constructive Gaussian sampler; claiming “plain MC cannot give a gradient” without distinguishing frozen samples from a differentiable sampling recipe hides this connection. No universal estimator-variance ranking.
11. **Fact.** Same deck, p96 L1450 and p97 L1465; note §§8.6-8.7 L467-L500 and §10.3 L571. **Title/point: a valid baseline preserves the mean; a well-chosen one can reduce variance.** Keep the good toy and add the bad-baseline contrast E13. Remove “never optional” and “reparameterization wins whenever available.” Correct scalar variance-improvement condition and distinguish a componentwise optimum from a shared vector criterion. Reason: the current headline makes a stronger claim than its lemma proves.
12. **Fact.** Same deck, pp100-107 L1524-L1618; note §§9.1-10.1 L507-L552. **Separate target pi_theta, behavior pi_b and reference pi_ref; retain the independent-token example only with its assumptions.** State that clipping changes a surrogate rather than bounding every actual ratio, and KL is not a certificate of bounded weight variance. Reason: the current wording connects two different comparisons as if a reference penalty automatically stabilized off-policy weights. E09-E10 fix source-specific claims; E14 checks the mathematical gap.
13. **Fact/notation.** Same deck, pp86-106 L1324-L1602 and both notes' preambles/references. **Use an explicit natural-log convention for score derivatives/KL in nats; distinguish parameter score from diffusion's sample-space score.** Fix prerequisite attribution rather than claiming variance/exponential means/product-KL were proved in the wrong lecture. Reason: earlier information-theory units use bits; derivative scaling and KL units cannot change silently.
14. **[judgment: density and ending]** Same deck, p62 L1000, p91 L1387, pp108-112 L1639-L1738. **Remove repeat-only short-proof summaries and keep one closing decision summary; move the nine-deck recap/map to notes unless it replaces, rather than supplements, the summary.** Reason: current end repeats the same toolkit through multiple formats. Keep meaningful proof steps; no deletions just to hit a count.
15. **Design rule plus [judgment: note organization].** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`, whole file; `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`, whole file. **Rebuild HTML as one matched article per final slide: point first, teaching explanation second, details/source last.** Preserve sound derivations inside the relevant article rather than copying old chapters wholesale. Synchronize Markdown as a self-contained ASCII/LaTeX course note with verbal exhibits and linearized tables; remove references to what “the original note draws.” Reason: current HTML has no slide articles and its quick-read messages are missing; accessibility is a standing course requirement.
16. **Design rule plus [judgment: exhibits].** Same deck, whole file, especially p27 L503, p30 L546, p37 L641, p96 L1450, p106 L1602 and p109 L1647. **Re-author to current capacity, one-idea/exhibit, takeaway-title and necessary-qualifier rules.** Keep explanatory mathematics and figures legible; move/split rather than shrinking. Any stochastic figure must have a reproducible seed/generator; any schematic must be labelled as such. Reason: selected baseline renders are unclipped but the old tables, multi-claim slides and generic figure titles no longer meet the current authoring standard.

### What not to discard

- Support failure at p48: concrete and important; reuse for the later “healthy ESS can miss a problem” demonstration.
- Optimal proposal proof pp59-61: the equality case explains the design principle. Keep its genuine derivation, not just the formula.
- Infinite-variance example pp66-68: preserves the distinction between unbiasedness, consistency and a usable error rate once wording is corrected.
- Two-action policy pp93-97: makes the gradient and baseline exactly checkable; extend the same example instead of adding unrelated anecdotes.

## Stage 3 — argument, title sequence and time budget

### One argument

**Monte Carlo turns an expectation into a computation; choosing how to sample or differentiate changes the estimator's error, not the target.** Each section answers a decision the previous one creates: Can I average? Where should I draw? Is the proposal safe? What if Z is unknown? How do I learn from samples? When can I reuse them?

### Six-part structure

Times include section transitions and worked examples. Two blocks of 75 minutes; closing time included separately. Counts/layouts are targets.

| Part | Teaching question | Minutes | Baseline material |
|---|---|---:|---|
| 01 Estimate an Expectation | What can one finite sample tell us? | 25 | pp3-40, compressed/adapted |
| 02 Change the Sampler | Can we visit useful outcomes more often? | 25 | pp41-54 plus practical E11 |
| 03 Control Proposal Risk | Why can a valid estimator still fail? | 25 | pp55-69, corrected |
| 04 Remove the Normalizer | What can a ratio and its diagnostics buy? | 20 | pp70-82 plus actual bias E12 |
| 05 Differentiate Expectations | Which part of sampling is differentiable? | 35 | pp83-98 plus Gaussian bridge/good-bad baseline |
| 06 Reuse Samples Responsibly | Which distribution does each ratio compare? | 15 | pp99-107, scoped |
| Closing decision summary | Match the tool to its conditions | 5 | pp108-113, condensed |
| **Total** | | **150** | |

### Proposed title sequence (content-level; stage 4 may split logical steps)

Title → Contents → numbered dividers matching the six headings above. These are communication targets, not final page numbers. Existing baseline IDs will be preserved across moves; titles alone must make the logic clear.

**01 Estimate an Expectation**
1. A Known Model, a Hard Average
2. Sample, Evaluate, Average
3. Six Draws Give a Noisy Estimate
4. Monte Carlo Reuses the Sample Mean
5. Unbiased Does Not Mean Accurate
6. Averaging Reduces RMSE
7. Estimating the Error Bar
8. Approximate Intervals, Exact Guarantees
9. Bounded Averages Concentrate
10. The Rate Is Not the Cost
11. Tensor Grids Grow With Dimension
12. Rare Events Need Relative Error

**02 Change the Sampler**
1. Most Draws Miss the Tail
2. A Rare Event Needs Many Samples
3. Visit Useful Outcomes More Often
4. Correct Each Visit's Weight
5. Importance Sampling Preserves the Target
6. Proof: Cancel the Proposal
7. Proof: Check the Missing Region
8. Missing Support Cannot Be Repaired
9. Average the Weighted Integrand
10. A Practical Exponential Proposal
11. More Tail Visits, Corrected Weights
12. Compute the Proposal's Error
13. Same Target, Less Relative Error
14. Coverage and Variance Are Different

**03 Control Proposal Risk**
1. The Second Moment Decides
2. Follow the Weighted Integrand
3. The Optimal Proposal
4. Proof: A Common Lower Bound
5. Proof: Attain the Bound
6. One-Sign Integrands Permit Zero Variance
7. The Oracle Needs a Normalizer
8. Light Tails Can Destroy Variance
9. A Finite Mean, an Infinite Second Moment
10. Consistency Is Not an Error Bar
11. Check the Integrand, Not Just Weights

**04 Remove the Normalizer**
1. The Target Is Known Up to Z
2. Compute Unnormalized Weights
3. Normalize Only a Positive Total
4. Two Averages Form One Ratio
5. The Ratio Converges to the Target
6. One Draw Exposes SNIS Bias
7. Normalization Does Not Guarantee Improvement
8. One Draw Can Dominate the Weights
9. Effective Sample Size Summarizes Imbalance
10. Healthy ESS Can Miss Missing Support
11. Choose the Estimator by What Is Known

**05 Differentiate Expectations**
1. The Distribution Now Changes
2. Frozen Samples Hide the Derivative
3. A Gaussian Sample Is a Recipe
4. Differentiate Along the Sampling Path
5. Check the Gaussian Gradient
6. Discrete Draws Need Another Route
7. The Log-Derivative Identity
8. Reward Times Score Gives the Gradient
9. Proof: Expand the Expectation
10. Proof: Differentiate the Finite Sum
11. Proof: Reweight and Read an Expectation
12. Average the Gradient Contributions
13. A Two-Action Policy
14. Both Routes Give the Same Derivative
15. The Score Has Mean Zero
16. A Valid Baseline Preserves the Gradient
17. This Baseline Removes the Toy's Variance
18. A Bad Baseline Adds Variance
19. Two Gradient Estimators, Different Requirements

**06 Reuse Samples Responsibly**
1. Old Samples, a New Target
2. Importance Weights Correct the Mismatch
3. Sequence Ratios Multiply
4. Compounding Mismatch Can Destroy Efficiency
5. Behavior and Reference Are Different Roles
6. KL Is a Penalty, Not a Variance Certificate
7. Reward Tuning Uses This Toolkit
8. A Surrogate Is Not a Hard Constraint

**Closing:** One Target, Different Estimators → closer. The ending keeps the bridge to optimization in one sentence within the decision summary/notes, without an extra roadmap or a universal promise.

### Slide/notes allocation

- Main slides retain required assumptions, interpretation, worked examples, the new core IS/optimal-proposal/score-function proof steps and the short SNIS convergence argument.
- Notes retain the old exact arithmetic worth preserving, proof details, optional scalar/vector baseline derivation, formal delta-method qualifications, tensor-midpoint proof, KL second-moment counterexample, source-specific PPO/RLHF caveats and alternative methods as optional reading.
- No supplementary deck is planned: this is the rigorous course, not a concept-first rewrite. A formula is not automatically moved merely for being formal; it moves if it is optional to the teaching objective.
- Details removed as false or unsupported are corrected/retired, not preserved uncritically in notes.

## Request coverage and package forecast

This is a planning coverage map, not the final executable package contract. Stable slide IDs are not present in the baseline; B001-B113 below are **baseline locators only**, not DOM slide IDs. The stage-4 plan will use S IDs and exact predecessor/new-position mappings after the setup strategy is agreed.

| Comment | Baseline page/title | Slide locator coverage | Forecast |
|---|---|---|---|
| C01 | Entire prob09 and both companions | B001-B113 | P1-P5 and integration |
| C02 | Prior foundations repeated in pp3-40; new methods pp41-107; repeated close pp108-112 | All, particularly B003-B040/B108-B112 | P1, all source checks, P5 integration |
| C03 | Whole-deck argument, new connections and design/notes modernization | B001-B113 plus new examples | P1-P5, no previous-deck edits |

Forecast boundaries:
- **P1:** baseline pp3-40 → new Part 01; associated HTML articles and accessible note content. Depends on agreed notation/error convention.
- **P2:** pp41-69 → Parts 02-03; associated proofs/examples/notes. Owns the shared rare-event example and its actual generator; publishes exact inputs before any reuse.
- **P3:** pp70-82 → Part 04; associated notes/ESS exhibit. Reuses the P2 support counterexample without redoing its proof.
- **P4:** pp83-98 → Part 05 plus short Gaussian bridge; associated notes. Owns the two-action example and gradient notation.
- **P5:** pp99-107 → Part 06; associated notes. Depends on P2 ratios and P4 gradient assumptions; no PPO/modern-RL scope expansion.
- **slides integration:** IDs and baseline map, Contents/dividers/title/closer, exactly one closing summary, citations, bibliography, cross-references, accessible-note consistency, outline counts/locations. Shared surfaces are not independently rewritten by packages.

## Acceptance gate after implementation

1. All C01-C03 covered; changed teaching scope/time returned to slides-review rather than silently altered.
2. New results source-checked independently; old prerequisite proofs not reintroduced. Ordinary IS, SNIS, gradient baselines and policy ratios retain their distinct conditions.
3. Both note formats reflect the final slides; HTML has a complete ordered one-to-one ID pairing, quick-read messages and detailed teaching explanations. Markdown remains ASCII, self-contained and accessible.
4. Every graph has traceable data or reproducible toy calculations; no decorative “empirical” curve. Required titles/keys/qualifiers readable in actual renders, no shrinking to fit.
5. Full pinned-commit review in round 1; later rounds changed slides plus neighbors only; at most three rounds, then escalation of unresolved blockers.
6. PR only after approval and verified log-only commits above the reviewed content. Albert performs the final check; merging needs his separate direct order.

## Baseline page/title map

Automatically extracted from the exact baseline to preserve location identity. No existing stable IDs; this list must not be mistaken for implemented S IDs. Each row records the opening slide line, not a mutable future page number.

| Locator | Baseline page | Source line | Baseline title |
|---|---:|---:|---|
| B001 | 1 | 41 | Monte Carlo & Importance Sampling |
| B002 | 2 | 53 | Contents |
| B003 | 3 | 141 | Why Sampling? |
| B004 | 4 | 149 | Three Expectations Nobody Can Compute |
| B005 | 5 | 173 | The Cliffhanger, Cashed In |
| B006 | 6 | 187 | The Idea — Integration by Averaging |
| B007 | 7 | 200 | Today's Three Upgrades |
| B008 | 8 | 224 | Route Map |
| B009 | 9 | 260 | Recall — the Toolkit |
| B010 | 10 | 268 | Recall — Expectation & Variance |
| B011 | 11 | 283 | Recall — Averages Concentrate |
| B012 | 12 | 298 | Recall — Hoeffding |
| B013 | 13 | 313 | What Is Genuinely New Today |
| B014 | 14 | 327 | The Monte Carlo Estimator |
| B015 | 15 | 335 | The Target |
| B016 | 16 | 349 | Definition — the Monte Carlo Estimator |
| B017 | 17 | 363 | Theorem 1 — Unbiasedness |
| B018 | 18 | 375 | Theorem 1 — Proof |
| B019 | 19 | 388 | What Unbiasedness Buys |
| B020 | 20 | 400 | Theorem 2 — Variance |
| B021 | 21 | 412 | Theorem 2 — Proof |
| B022 | 22 | 424 | RMSE — the Error Yardstick |
| B023 | 23 | 438 | Accuracy Guarantee I — Chebyshev |
| B024 | 24 | 451 | Accuracy Guarantee II — Hoeffding |
| B025 | 25 | 462 | Worked Example — $\pi$ by Darts |
| B026 | 26 | 475 | The Dartboard |
| B027 | 27 | 503 | Six Darts by Hand |
| B028 | 28 | 520 | The Estimator's Exact Statistics |
| B029 | 29 | 531 | How Many Darts per Digit? |
| B030 | 30 | 546 | Guarantee, Two Ways — $\|\hat{\pi} - \pi\| \leq 0.01$ at $95\%$ |
| B031 | 31 | 561 | What Monte Carlo Never Asked |
| B032 | 32 | 575 | Error Scaling & Dimension |
| B033 | 33 | 583 | The Remarkable Absence |
| B034 | 34 | 596 | The Competitor — Grid Integration |
| B035 | 35 | 609 | Grid Cost of Accuracy $\epsilon = 10^{-2}$ |
| B036 | 36 | 626 | Monte Carlo Cost of the Same $\epsilon$ |
| B037 | 37 | 641 | Error vs. Work — the Picture |
| B038 | 38 | 676 | The Crossover at $d = 4$ |
| B039 | 39 | 689 | The Honest Caveats |
| B040 | 40 | 701 | Implication for AI |
| B041 | 41 | 715 | Importance Sampling |
| B042 | 42 | 723 | Two Ways Vanilla MC Fails |
| B043 | 43 | 742 | A Rare Event by Hand |
| B044 | 44 | 751 | Vanilla MC on the Rare Event |
| B045 | 45 | 764 | The Fix — Change the Sampler |
| B046 | 46 | 774 | Theorem 3 — the IS Identity |
| B047 | 47 | 787 | Theorem 3 — Proof |
| B048 | 48 | 801 | Why the Support Condition Is Real |
| B049 | 49 | 812 | Definition — the IS Estimator |
| B050 | 50 | 827 | Weights Are Likelihood Ratios |
| B051 | 51 | 842 | Proposal vs. Target — the Picture |
| B052 | 52 | 873 | IS on the Rare Event — a Tailored Proposal |
| B053 | 53 | 886 | Every Sample Says the Same Thing |
| B054 | 54 | 899 | Too Good — What Just Happened? |
| B055 | 55 | 913 | The Variance of IS |
| B056 | 56 | 921 | Variance of the IS Estimator |
| B057 | 57 | 934 | The Object to Watch |
| B058 | 58 | 947 | Technique Review — Jensen |
| B059 | 59 | 961 | Theorem 4 — the Optimal Proposal |
| B060 | 60 | 974 | Proof Step 1 — the Floor |
| B061 | 61 | 987 | Proof Step 2 — $q^*$ Attains the Floor |
| B062 | 62 | 1000 | Theorem 4 — Proof Summary |
| B063 | 63 | 1014 | Zero Variance, Verified on the Rare Event |
| B064 | 64 | 1027 | The Catch — $q^*$ Needs the Answer |
| B065 | 65 | 1040 | The Other End of the Dial |
| B066 | 66 | 1051 | Worked Example — a Light-Tailed Proposal |
| B067 | 67 | 1062 | The Weights Alone Blow Up |
| B068 | 68 | 1077 | Unbiased, Consistent — and Practically Unstable |
| B069 | 69 | 1091 | The Tail Rule of Thumb |
| B070 | 70 | 1104 | Weight Degeneracy — the Picture |
| B071 | 71 | 1130 | Five Samples, One in Disguise |
| B072 | 72 | 1142 | Self-Normalized IS |
| B073 | 73 | 1150 | The Missing Constant |
| B074 | 74 | 1162 | Unnormalized Weights |
| B075 | 75 | 1174 | Definition — Self-Normalized IS |
| B076 | 76 | 1190 | Two MC Estimators, One Ratio |
| B077 | 77 | 1203 | Consistency — Sketch |
| B078 | 78 | 1217 | Honest Flag — SNIS Is Biased |
| B079 | 79 | 1228 | Effective Sample Size — a Heuristic |
| B080 | 80 | 1242 | ESS — Sanity Checks by Hand |
| B081 | 81 | 1253 | What ESS Is Not |
| B082 | 82 | 1265 | Where SNIS Runs in AI |
| B083 | 83 | 1288 | The Score-Function Gradient |
| B084 | 84 | 1296 | A New Kind of Problem |
| B085 | 85 | 1310 | Why Plain MC Doesn't Give a Gradient |
| B086 | 86 | 1324 | Technique Review — the Log-Derivative Trick |
| B087 | 87 | 1338 | Theorem 5 — the Score-Function Identity |
| B088 | 88 | 1351 | Proof Step 1 — Expand the Expectation |
| B089 | 89 | 1363 | Proof Step 2 — Swap $\nabla$ and $\sum$ |
| B090 | 90 | 1375 | Proof Step 3 — Log-Derivative, Then Reread |
| B091 | 91 | 1387 | Theorem 5 — Proof Summary |
| B092 | 92 | 1401 | The REINFORCE Estimator |
| B093 | 93 | 1414 | Worked Check — a Two-Action Policy |
| B094 | 94 | 1425 | Worked Check — the Identity Agrees |
| B095 | 95 | 1436 | Reading the Identity |
| B096 | 96 | 1450 | Baselines — Free Variance Reduction |
| B097 | 97 | 1465 | Baseline at Work — the Toy, Revisited |
| B098 | 98 | 1481 | The REINFORCE Pipeline |
| B099 | 99 | 1516 | Off-Policy & RLHF |
| B100 | 100 | 1524 | The Off-Policy Problem |
| B101 | 101 | 1536 | Old Samples, New Policy — It's Theorem 3 |
| B102 | 102 | 1549 | Sequences Multiply Weights |
| B103 | 103 | 1562 | Degeneracy Grows With Length |
| B104 | 104 | 1575 | Keep the Ratio Near One |
| B105 | 105 | 1587 | Recall — KL Divergence |
| B106 | 106 | 1602 | The RLHF-Shaped Objective |
| B107 | 107 | 1618 | One Pipeline, Every Tool of Today |
| B108 | 108 | 1639 | Closing the Probability Half |
| B109 | 109 | 1647 | Recap — Every Tool, One Job |
| B110 | 110 | 1664 | Nine Decks, One Arc |
| B111 | 111 | 1717 | What the Probability Half Gave You |
| B112 | 112 | 1738 | Bridge — From Estimating to Optimizing |
| B113 | 113 | 1752 | Closer |
