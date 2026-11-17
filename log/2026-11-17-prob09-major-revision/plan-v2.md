# prob09 major revision — approved argument, full build plan

## What changed since plan-v1

Albert approved stages 1-3 with “go ahead” on 2026-11-17 at 12:27 KST (C04). This version is the executable stage-4 plan: 85 slide targets with stable IDs, full baseline dispositions, disjoint packages, two-commit identity preparation and artifact-level acceptance. It does not change the approved audience, argument, scope or 150-minute budget. New slide counts/layouts remain targets, not a cap. E17-E21 add explicit checks of retained arithmetic and diagnostics, not new lecture scope. The setup proposal in work-r0 at `7e07e81235f89357f7546343186bd8f461a8e0f2` is accepted as specified below.

**Status:** complete work order when announced. This supersedes plan-v1's non-executable sequence while preserving its approved argument, continuity decisions and audit rationale. Archive plan-v1 unchanged as the approval-stage record.

Job: `2026-11-17-prob09-major-revision`  
Baseline: `b20ab73ac7e74e9489d379cf9caad7565f17e31e`  
Branch: `2026-11-17-prob09-major-revision`  
Main: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`  
HTML notes: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`  
Accessible notes: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`  
Shared outline: `courses/deepmath/OUTLINE.md`, prob09 entries only.

## Summary and teaching contract

**Audience/mode:** junior undergraduate AI majors; rigorous, example-led. **Duration:** 150 minutes, two 75-minute blocks, break after Part 03. **Argument:** Monte Carlo turns an expectation into computation; choosing the sampler or gradient estimator changes error, not the target.

Students should leave able to choose an estimator and name its conditions: distinguish unbiasedness, consistency, RMSE and confidence; correct a sampling distribution without losing support; diagnose proposal risk without overreading weights; remove a normalizer without promising unbiasedness; distinguish pathwise and score gradients; and separate behavior-policy correction from reference-policy regularization.

Keep the useful support counterexample, optimal-proposal derivation, infinite-variance example and two-action gradient check. Spend less time reproving the sample mean, more time on a usable proposal and honest interpretation. Both notes are rebuilt, not patched around the old chapter summaries.

**Scope exclusions remain:** no edits to prob01-prob08; no MCMC/QMC/particle-filter chapter; no PPO tutorial or modern RL-method survey; no new tech deck; no global design-system, reference library or agent configuration edits. Source cutoff 2026-11-17. The scoped InstructGPT application is historical, not a claim about current practice.

### Priority labels and authoring discretion

- **Must:** each specified point, mathematical qualification, on-slide answer, evidence fidelity, note coverage, ID trail and approved scope/time. Required content is a semantic specification, not prose to paste wholesale onto a slide.
- **Prefer / [judgment]:** proposed titles, example visual encodings, ordering within a logical step and named layout components. Keep the takeaway; slides chooses the wording and design. Rendered design rules outrank this plan.
- **Slides decides:** exact layout, chart implementation, source-code organization within authorized paths, and necessary logical splits. Report splits/moves. Return material changes to the argument, facts, required content, scope or teaching time before implementing them.
- Suggested component names below are vocabulary only. No CSS, font, pixel or markup prescription is intended. Do not squeeze required qualifiers or proofs to preserve the 85-slide target.
- Each content slide needs its stated exhibit. For these original instructional calculations, a diagram or annotated equation is the evidence-bearing exhibit; do not invent empirical curves. Existing canonical source figures are preferable where they actually explain the same point, but are not a reason to replace an exact worked example with an unrelated paper plot.

### Timing

| Section | Content targets | Minutes including transitions |
|---|---:|---:|
| Title, Contents, 01 Estimate an Expectation | 12 + 3 structural | 25 |
| 02 Change the Sampler | 14 + divider | 25 |
| 03 Control Proposal Risk | 11 + divider | 25 |
| 04 Remove the Normalizer | 11 + divider | 20 |
| 05 Differentiate Expectations | 19 + divider | 35 |
| 06 Reuse Samples Responsibly | 8 + divider | 15 |
| One closing synthesis and closer | 2 | 5 |
| **Total** | **85** | **150** |

Times below are pacing targets, not auto-advance intervals. S109 spends its time on a spoken comparison/question, not a dense wall of formulas.

## Identity preparation — before content work

1. **Commit A, note scaffolding only:** follow work-r0: insert 113 unlabelled article wrappers in baseline slide order, no edits or reordering of existing words, math, headings, anchors or classes; retain chapter containers. Empty articles are permitted only as temporary scaffolding. Map each original h2/h3 block to its baseline slide, reporting non-exact matches. If well-formed ordered wrappers cannot be produced within chapter boundaries without other edits, return the issue rather than improvise.
2. **Commit B, joint ID-only commit:** add S01-S113 to the baseline deck slides and matching HTML articles in one attribute-only commit. Markdown remains untouched in A and B. Report both SHAs; B is recorded as `id commit`.
3. Prove A preserves visible text and math sequence and wrapper-stripped source (only insertion whitespace may differ); check unchanged desktop and narrow render. Prove removing the new ID attributes from B reproduces A exactly for both files.
4. Only then implement this plan. Final notes have one nonempty, relevant article per final slide; temporary empty scaffolds do not satisfy acceptance. New Markdown structure mirrors the final sequence with visible heading IDs or unobtrusive markers, whichever preserves the accessible standalone edition best.
5. S47 and S96 split to S47a/S47b and S96a/S96b. New IDs S114-S129 are reserved below. Never reuse retired IDs. If another new slide is required, start at S130; if splitting a planned slide, use suffix IDs and report the map. Baseline page/title provenance for every old ID is at the end.

## Coverage and continuity

| Comment | Baseline scope / title | Final IDs | Package |
|---|---|---|---|
| C01 slides and notes | All 113 pages plus both companions | All final IDs, one-to-one HTML pairing, standalone Markdown | P1-P5 + integration |
| C02 contents / prob01-prob08 consistency / redundancy | pp4-40 repeated recalls; pp62/91 repeat proof summaries; pp108-112 repeated endings; existing gradient/policy claims | S04-S37 selections; S114-S116; S47a/b; S59-S69 selections; S123-S129; S109; all retirements below | P1-P5 + integration |
| C03 major revision / current design rules | Whole argument, exhibits and chapter-style notes | Six-part sequence, all specs below; legacy assumptions corrected in every layer | P1-P5 + integration |
| C04 go ahead | Approved stages 1-3, not a merge order | Same audience, scope, argument and 150-minute budget | Owner + all packages |

The exact prerequisite locations and reuse/adapt/defer decisions in plan-v1 remain authoritative planning provenance (E01). On-slide explanations remain self-contained; do not put “see Lecture N” in place of a definition. The notes may link precise prior locations:
- Reuse LOTUS/linearity/Jensen (prob01/prob03), variance/LLN/CLT (prob05) and sample-mean bias (prob07), without fresh theorem/proof arcs.
- Adapt prob06's [0,1] bound via rescaling; distinguish fixed integrands from ones chosen on the same evaluation sample.
- Adapt prob08's Gaussian construction into a differentiable sampling recipe, without repeating Gaussian algebra or claiming all Gaussian expectations close.
- Reuse the general autoregressive chain rule (prob04/prob07), not independence; distinguish parameter score from sample-space diffusion score if mentioned.
- Use **natural logarithms** for parameter scores and KL in this lecture (nats), explicitly signposted against earlier bits. No wrong attribution of exponential means/product-KL to an earlier lecture; derive locally or source directly.

## Common note and evidence contract

Every spec below assigns a main-slide point/exhibit and additional note content. **All** final HTML articles must begin with a specific brief message, then an explanation sufficient to teach the slide, then useful details and precise sources. The message must retain essential assumptions and distinctions. A plot explanation names axes, units, encodings, comparison and limitations. Proof explanations name the reason for each step; do not just repeat the equation. Structural entries can be brief, but not blank.

The Markdown edition is a self-contained accessible course note: same sequence and mathematics, ASCII text/LaTeX, verbal equivalents of diagrams and linearized tables. It must not rely on “the original note draws” or seeing another artifact. Preserve useful old derivations in the appropriate new article, correcting them; do not retain stale chapters as a contradictory appendix. No technical supplement is planned: **tech destination = none for every spec**.

Use evidence.md E01-E21 for sources/versions/locators and limits. Every numeric chart is deterministic formula data or a labelled simulation with recorded seed, inputs and repository generator path. slides owns the generator and reports its actual path; owner appends that provenance to evidence before approval. Hand-picked illustrations are labelled as such, never described as sample evidence. All source claims and calculations must agree across main, short message, details, Markdown, chart keys and alternative text.

## Full slide specifications

Each numbered target below is one final slide; the number is a proposed final page, not its identity. All carry C01-C03; C04 fixes the scope. IDs, not page numbers, govern implementation. Layout suggestions and exact titles are **prefer / [judgment]**; the Point, Main, Notes and Acceptance fields are **must**.

## Opening and Part 01 — Estimate an Expectation

### 1. S01 — Monte Carlo & Importance Sampling

Baseline p1: Monte Carlo & Importance Sampling. **Time target:** 0.5 min. **Layout (prefer):** title-slide.

- **Point:** Turn expectations into computations, then choose the error tradeoff.
- **Main:** Keep course/lecture identity and lecturer credit; subtitle can name estimation and gradients.
- **Exhibit / reading:** Structural title; no decorative scientific claim.
- **Notes / Markdown:** Brief learning purpose and audience; identify both note formats.
- **Evidence:** E01,E16; approved scope.
- **Acceptance:** Lecture identity remains prob09, not trustworthy-ai lec09.

### 2. S02 — Contents

Baseline p2: Contents. **Time target:** 0.5 min. **Layout (prefer):** toc-list.

- **Point:** Six decisions organize the lecture.
- **Main:** Exactly the six numbered section names from the timing table, in that order.
- **Exhibit / reading:** TOC sequence; each heading maps to one section divider.
- **Notes / Markdown:** Explain the argument in one short paragraph; two-block pacing is a teaching cue, not new content.
- **Evidence:** E01,E16; approved argument.
- **Acceptance:** TOC names and order equal the six dividers; no second roadmap.

### 3. S03 — 01 · Estimate an Expectation

Baseline p3: Why Sampling?. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** First separate the desired quantity from the randomness of its estimate.
- **Main:** Section name plus one compact teaching question if useful.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Frame estimation rather than probability re-teaching.
- **Evidence:** E01,E02.
- **Acceptance:** Name matches Contents; no standalone recall chapter.

### 4. S04 — A Known Model, a Hard Average

Baseline p4: Three Expectations Nobody Can Compute. **Time target:** 2 min. **Layout (prefer):** diagram-flow.

- **Point:** Knowing how to draw X does not make E[f(X)] convenient to compute.
- **Main:** One motivating task: expected loss or reward under a known sampler; identify p, f and mu=E_p[f(X)]. Say “no convenient closed form” where needed, not “nobody can compute.”
- **Exhibit / reading:** Sampler → evaluated outcome → unknown population average diagram; a single example, not three unrelated claims.
- **Notes / Markdown:** Relate to prob08's MC bridge. Distinguish numerical difficulty from lack of an antiderivative; nonlinear Gaussian expectations need not be closed form, and non-Gaussian ones sometimes are.
- **Evidence:** E01,E02.
- **Acceptance:** Target, sampler and evaluable f are unambiguous; no universal Gaussian/non-Gaussian claim.

### 5. S06 — Sample, Evaluate, Average

Baseline p6: The Idea — Integration by Averaging. **Time target:** 1 min. **Layout (prefer):** diagram-flow.

- **Point:** An expectation becomes an average of repeated evaluations.
- **Main:** IID X_i from p; evaluate f(X_i); average. Sampling access suffices for ordinary MC, even when p is not evaluable.
- **Exhibit / reading:** Three-step recipe ending in an average; keep it intuitive before the formal estimator.
- **Notes / Markdown:** Define IID in plain language and the importance of holding the target/integrand fixed during evaluation. Integrability is formalized on S16.
- **Evidence:** E01,E02.
- **Acceptance:** Does not require density evaluation for ordinary MC or promise an answer for every f.

### 6. S26 — Six Draws Give a Noisy Estimate

Baseline p26: The Dartboard. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Four disk hits out of six illustrate the estimator, not its reliability.
- **Main:** Uniform square [-1,1]^2; disk area ratio pi/4; pi estimate 4 times hit fraction=8/3. Label the six points “hand-chosen illustration,” not a random run.
- **Exhibit / reading:** Reuse the dartboard geometry and exact six points in E17; show in/out encodings and the resulting hit fraction.
- **Notes / Markdown:** Full six-coordinate hit ledger; derivation from area ratio; distinction between the sampling experiment and the deliberately selected drawing. No confidence inference from these six points.
- **Evidence:** E17,E02.
- **Acceptance:** Four points in, two out, formula and count match; no fabricated random seed or empirical claim.

### 7. S16 — Monte Carlo Reuses the Sample Mean

Baseline p16: Definition — the Monte Carlo Estimator. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Set Y=f(X), then apply the established sample-mean results.
- **Main:** Define hat(mu)_n=n^{-1}sum f(X_i), IID from p, E_p|f|<infinity; concise Recall identifies the random variable Y.
- **Exhibit / reading:** Annotated estimator with target, evaluations and average named; substitute Y_i=f(X_i).
- **Notes / Markdown:** Reuse LOTUS and sample-mean definitions; integrability gives a well-defined finite mean and LLN, finite variance is an additional assumption. No new theorem number for old sample-mean facts.
- **Evidence:** E01,E02.
- **Acceptance:** The transformed variable is explicit, and first versus second moments are not conflated.

### 8. S19 — Unbiased Does Not Mean Accurate

Baseline p19: What Unbiasedness Buys. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** Correct expectation across repetitions does not ensure a good single run.
- **Main:** E[hat(mu)_n]=mu by linearity; distinguish estimator's expectation from observed error.
- **Exhibit / reading:** Repeated-estimate schematic centered at mu but spread out; label schematic, or use an exact annotated averaging identity without simulated claims.
- **Notes / Markdown:** One-line linearity proof; independence is not needed for that expectation identity, though it is assumed for later variance/rates. Preserve the useful bias-variance interpretation from prob07.
- **Evidence:** E01,E02.
- **Acceptance:** No implication that unbiased means close, nor a fresh proof sequence for linearity.

### 9. S22 — Averaging Reduces RMSE

Baseline p22: RMSE — the Error Yardstick. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Under finite variance and IID sampling, RMSE scales as n^{-1/2}.
- **Main:** Expand root mean squared error (RMSE). Recall Var(hat(mu))=sigma_f^2/n and unbiased RMSE=sigma_f/sqrt(n); 100 times the samples gives 10 times smaller RMSE under the same per-draw variance.
- **Exhibit / reading:** One annotated scaling equation or exact rate curve with n and RMSE axes; no measured-runtime label.
- **Notes / Markdown:** Derive briefly from established variance of independent sums. For darts, sigma_Y^2=pi(4-pi); explain RMSE averages squared error across repetitions, not a bound on this run.
- **Evidence:** E01,E02,E17.
- **Acceptance:** Finite variance and IID assumptions are visible; digits/accuracy claims are RMSE-scaled, not guaranteed.

### 10. S114 — Estimating the Error Bar

New slide; position fixed by this sequence. **Time target:** 3 min. **Layout (prefer):** math-block.

- **Point:** Sample variation gives an estimated standard error, not the true error.
- **Main:** For IID evaluations with finite variance and n>=2, use s_Y^2=(n-1)^{-1}sum(Y_i-bar(Y))^2 and estimated standard error (SE)=s_Y/sqrt(n); identify unknown sigma versus observed s.
- **Exhibit / reading:** Data evaluations → sample spread → estimated SE; annotated formulas count as the single exhibit.
- **Notes / Markdown:** Full variance-estimator explanation and units; use genuinely IID conceptual data, not the six hand-chosen darts as inference. A finite observed variance does not prove finite population variance or reveal unvisited tails.
- **Evidence:** E02.
- **Acceptance:** SE is labelled estimated and is not confused with |estimate-target| or a guaranteed interval.

### 11. S115 — Approximate Intervals, Exact Guarantees

New slide; position fixed by this sequence. **Time target:** 2.5 min. **Layout (prefer):** cols.

- **Point:** A normal approximation and a finite-sample bound answer different questions.
- **Main:** Show approximate 95% interval bar(Y) plus/minus 1.96 estimated SE under IID finite positive variance and large-sample adequacy; contrast a probability bound valid under its stated assumptions.
- **Exhibit / reading:** Two clearly labelled uncertainty statements: “asymptotic approximation” versus “finite-sample bound”; not an observed coverage chart.
- **Notes / Markdown:** Explain CLT/studentization and why n alone does not certify normal accuracy; Chebyshev uses known/valid variance control, not an unqualified plug-in s^2. Preserve full darts Chebyshev arithmetic here, as pedagogy using known benchmark variance.
- **Evidence:** E01,E02,E17.
- **Acceptance:** No exact 95% claim for the CLT interval; no replacing a variance bound with observed sample variance.

### 12. S24 — Bounded Averages Concentrate

Baseline p24: Accuracy Guarantee II — Hoeffding. **Time target:** 2.5 min. **Layout (prefer):** math-block.

- **Point:** A known range yields a finite-sample probability guarantee.
- **Main:** Recall [0,1] Hoeffding, adapt Y in [a,b] with (Y-a)/(b-a), a<b. Display P(|bar(Y)-mu|>=epsilon)<=2 exp(-2n epsilon^2/(b-a)^2) for fixed IID evaluations.
- **Exhibit / reading:** Rescaling arrow into the bound; use [0,4] darts as the named substitution, without the old dense two-bound table.
- **Notes / Markdown:** Solve n>=(b-a)^2 ln(2/delta)/(2epsilon^2); E17's sufficient n=295111 for darts. Preserve both exact bound calculations across this article and S115. Explain constant-variable case and fixed-vs-data-selected f warning from prob06.
- **Evidence:** E01,E02,E17.
- **Acceptance:** General range derived from the actual prior [0,1] result; probabilities, ceilings and units correct.

### 13. S33 — The Rate Is Not the Cost

Baseline p33: The Remarkable Absence. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** Dimension is absent from the exponent, not from variance or evaluation work.
- **Main:** MC RMSE=sigma_f(d)/sqrt(n); per-draw sampling/evaluation cost can depend on d. Avoid declaring a dimension-free computational budget.
- **Exhibit / reading:** Rate annotated with the two hidden costs: sigma_f(d) and work per evaluation.
- **Notes / Markdown:** No smoothness is required for ordinary integrable MC consistency; finite variance for the displayed RMSE. Explain why easy-to-write rates are not universal performance guarantees.
- **Evidence:** E02,E03.
- **Acceptance:** Dimension caveats appear in the main point, not only notes.

### 14. S37 — Tensor Grids Grow With Dimension

Baseline p37: Error vs. Work — the Picture. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** A smooth tensor-grid exponent degrades with dimension; this is not a universal crossover.
- **Main:** Compare second-order tensor midpoint error proportional to N^{-2/d} with MC RMSE proportional to N^{-1/2}, under appropriate smoothness and finite variance, respectively.
- **Exhibit / reading:** Labelled schematic log-log error versus function evaluations; use a few dimensions, stated normalized constants; distinguish deterministic error and RMSE.
- **Notes / Markdown:** Full N=m^d argument; derivative-dependent constants and comparable-cost assumption; d=4 exponent equality is not a wall-clock threshold. Retain useful old grid arithmetic only as qualified notes, deleting “all grids fail near ten dimensions.”
- **Evidence:** E03,E02.
- **Acceptance:** Figure is schematic with formulas/inputs; axes/criterion clear; no empirical superiority or universal grid claim.

### 15. S116 — Rare Events Need Relative Error

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** A tiny event probability can have small absolute variance but poor relative precision.
- **Main:** Indicator mean rho in (0,1), variance rho(1-rho); relative RMSE=sqrt((1-rho)/(n rho)). Define relative RMSE as RMSE divided by |mu|.
- **Exhibit / reading:** Absolute-variance versus relative-error annotations for a rare indicator; no arbitrary sample counts.
- **Notes / Markdown:** Derive by dividing the ordinary-MC RMSE by rho; relative error undefined at zero target. Explain why “rare events have large variance” is misleading without saying relative. Sets up the explicit exponential event.
- **Evidence:** E02,E11 (same indicator calculation).
- **Acceptance:** Small absolute variance and large relative error are distinguished in every note layer.

## Part 02 — Change the Sampler

### 16. S41 — 02 · Change the Sampler

Baseline p41: Importance Sampling. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** Visit useful outcomes more often without changing the target.
- **Main:** Exact section title and motivating question.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Transition from relative error to proposal choice; no new roadmap.
- **Evidence:** E04,E11.
- **Acceptance:** Name equals Contents.

### 17. S43 — Most Draws Miss the Tail

Baseline p43: A Rare Event by Hand. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** The target event is so rare that ordinary draws seldom contribute.
- **Main:** Define p(x)=exp(-x) on x>=0, f(x)=indicator(x>10), mu=P_p(X>10)=exp(-10), approximately 0.0000454.
- **Exhibit / reading:** Exponential density with x=10 and the event region marked; use a scale/inset that does not visually invent a large tail.
- **Notes / Markdown:** Define exponential rate 1 and derive the tail integral locally. This closed-form case is a benchmark for checking an estimator, not a problem requiring MC to know the answer.
- **Evidence:** E11,E04.
- **Acceptance:** Tail area, rate and target match; all plots use the exact density.

### 18. S44 — A Rare Event Needs Many Samples

Baseline p44: Vanilla MC on the Rare Event. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** Relative RMSE, not absolute variance, exposes the sampling burden.
- **Main:** Apply relative RMSE sqrt((1-mu)/(n mu)); at target 0.1 ordinary MC needs n>=2202547.
- **Exhibit / reading:** One substitution from the indicator formula to the sample budget, with “10% relative RMSE” next to the number.
- **Notes / Markdown:** Exact ceiling, exp(10)-1 per-draw relative variance, and no 95% coverage/runtime implication. The threshold 10 and target remain fixed throughout Part 02.
- **Evidence:** E11.
- **Acceptance:** Numerical criterion and count verified; no conflation with confidence.

### 19. S45 — Visit Useful Outcomes More Often

Baseline p45: The Fix — Change the Sampler. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** More tail visits help only if their contributions are corrected.
- **Main:** Introduce proposal q: change where draws land; preserve the same p,f,mu. Sampling from q without weights estimates E_q[f], a different target.
- **Exhibit / reading:** Target/proposal visitation schematic with unchanged target indicator; label qualitative unless a specific q is introduced.
- **Notes / Markdown:** Explain proposal versus target using repeated-visit accounting. Do not present the zero-variance oracle yet.
- **Evidence:** E04,E11.
- **Acceptance:** Unweighted proposal averages are not described as unbiased for mu.

### 20. S50 — Correct Each Visit's Weight

Baseline p50: Weights Are Likelihood Ratios. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** The ratio p/q corrects over- and under-visiting.
- **Main:** Define importance weight w(x)=p(x)/q(x) at sampled points with q>0; over-visited locations get smaller weight, under-visited larger.
- **Exhibit / reading:** Paired probability/density bars or annotated ratio showing numerator target and denominator proposal.
- **Notes / Markdown:** Density ratio is local relative mass, not probability at a continuous point. E_q[w]=1 needs q coverage of all p, stronger than f-specific support needed for ordinary IS.
- **Evidence:** E04.
- **Acceptance:** Target is numerator; no universal E_q[w]=1 under only f-specific support.

### 21. S46 — Importance Sampling Preserves the Target

Baseline p46: Theorem 3 — the IS Identity. **Time target:** 2.5 min. **Layout (prefer):** card.

- **Point:** Exact weighting changes the sampler, not the expectation.
- **Main:** Theorem: E_p|f|<infinity and q>0 wherever fp is nonzero (almost everywhere) imply E_p[f]=E_q[fp/q]. State the required support and computable normalized ratio for ordinary IS.
- **Exhibit / reading:** The identity as an annotated theorem exhibit, identifying the two sampling measures.
- **Notes / Markdown:** Clarify discrete sums versus continuous integrals; define the integrand arbitrarily on q-null points. Unbiasedness is separate from finite variance.
- **Evidence:** E04, Theorem 9.1.
- **Acceptance:** Integrability and support are visible and sufficient; no finite-variance claim from the identity.

### 22. S47a — Proof: Cancel the Proposal

Baseline p47: Theorem 3 — Proof. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** On sampled support, multiplying by q cancels the sampling correction.
- **Main:** Expand E_q[fp/q] as an integral over {q>0}; cancel q to obtain integral over that same region of fp.
- **Exhibit / reading:** One two-step annotated equation; highlight that the domain has not changed yet.
- **Notes / Markdown:** Explain why cancellation occurs only on q>0 and why absolute integrability makes the expectation legitimate.
- **Evidence:** E04.
- **Acceptance:** Does not silently extend the integral across a missing region.

### 23. S47b — Proof (continued): Check the Missing Region

Baseline p47: Theorem 3 — Proof. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Support coverage ensures the omitted region contributes zero.
- **Main:** Recap the integral over {q>0}; the integral over {q=0} is zero because fp=0 there; therefore recover mu.
- **Exhibit / reading:** Domain split diagram or short equation chain completing the proof.
- **Notes / Markdown:** Full discrete version and almost-everywhere qualification; do not infer full target support is necessary when f vanishes elsewhere.
- **Evidence:** E04.
- **Acceptance:** The last equality explicitly uses the support assumption; proof closes without a repeat-only summary slide.

### 24. S48 — Missing Support Cannot Be Repaired

Baseline p48: Why the Support Condition Is Real. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A never-sampled nonzero contribution cannot be recovered by weights.
- **Main:** p uniform on {1,2,3,4}, f=indicator(x=4), q uniform on {1,2,3}; target 1/4, weighted output always zero.
- **Exhibit / reading:** Four-state probability diagram with the fourth target mass and missing proposal highlighted.
- **Notes / Markdown:** Calculate weights 3/4 on observed states and zero f; distinguish theorem violation from variance failure. This exact example returns for ESS.
- **Evidence:** E19,E04.
- **Acceptance:** Nonzero missing contribution is visible; no suggestion more samples repair zero support.

### 25. S49 — Average the Weighted Integrand

Baseline p49: Definition — the IS Estimator. **Time target:** 1 min. **Layout (prefer):** math-block.

- **Point:** Ordinary IS is ordinary averaging under q of Y=fw.
- **Main:** IID q draws, hat(mu)_IS=n^{-1}sum f(X_i)w(X_i); unbiased under the just-stated conditions.
- **Exhibit / reading:** Sampling/evaluation/weighting/averaging recipe, or annotated estimator with Y_i=fw.
- **Notes / Markdown:** Normalize by n, not sum of weights; density evaluation is an extra requirement versus plain MC. Mention integrability gives consistency, variance is next.
- **Evidence:** E04,E02.
- **Acceptance:** Ordinary IS and SNIS denominators are not mixed.

### 26. S117 — A Practical Exponential Proposal

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A heavier-tailed, normalized proposal increases useful visits without requiring the target mean.
- **Main:** Choose q=Exp(0.1), p=Exp(1), same event x>10; both supports x>=0. State lambda=0.1 is an illustrative choice, not the variance optimum.
- **Exhibit / reading:** Exact target/proposal density comparison with the event boundary and distribution labels; diagram must be read in a few phrases.
- **Notes / Markdown:** Both densities are evaluable; sample q by a standard exponential recipe if useful. Unlike q-star, q's normalizer does not contain the unknown rare-event probability.
- **Evidence:** E11,E04.
- **Acceptance:** A feasible non-oracle proposal precedes the oracle; no optimality claim.

### 27. S118 — More Tail Visits, Corrected Weights

New slide; position fixed by this sequence. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** The proposal's frequent tail hits receive small, varying corrections.
- **Main:** For q=Exp(0.1), P_q(X>10)=exp(-1), w=10 exp(-0.9x); contribution f w remains zero below 10 and varies above it.
- **Exhibit / reading:** One contribution-versus-x graph with tail threshold, or an annotated weight formula linked to the tail-probability comparison.
- **Notes / Markdown:** Derive the ratio explicitly; E_q[fw]=exp(-10). Distinguish a higher visit rate from a proof of lower variance; nonconstant tail contributions distinguish this case from the oracle.
- **Evidence:** E11,E04.
- **Acceptance:** Shows correction and nonzero variability; does not count tail hits without weighting.

### 28. S119 — Compute the Proposal's Error

New slide; position fixed by this sequence. **Time target:** 2.5 min. **Layout (prefer):** math-block.

- **Point:** The weighted second moment makes the variance comparison exact.
- **Main:** Derive E_q[(fw)^2]/mu^2=exp(10lambda)/(lambda(2-lambda)), 0<lambda<2; subtract 1 for relative variance. For lambda=.1 the relative variance is about 13.3067.
- **Exhibit / reading:** Compact integral-to-result derivation: integrate exp(-(2-lambda)x)/lambda from 10 to infinity, then divide by mu^2. Split a logical step if necessary; no crowded ledger.
- **Notes / Markdown:** Full integral and boundary evaluation, validity range, relationship Var(hat(mu))/mu^2=(relative variance)/n. Do not label the second moment itself as variance.
- **Evidence:** E11,E04.
- **Acceptance:** Exponents, normalizers, integrability range and subtraction of 1 are correct.

### 29. S120 — Same Target, Less Relative Error

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** This feasible proposal needs far fewer draws for the same RMSE criterion.
- **Main:** Compare ordinary MC n=2202547 with this IS n=1331 for relative RMSE<=0.1; exact same target. Label calculation, not measured runtime.
- **Exhibit / reading:** Bars comparing required sample counts, appropriately labelled scale and direction “fewer draws”; no unreadable magnitude table.
- **Notes / Markdown:** Exact ceilings from E11; equal per-draw work is an extra assumption, so do not call the ratio a real-world speedup. Neither count is a 95% guarantee.
- **Evidence:** E11.
- **Acceptance:** Criterion and calculation provenance are on the slide; bars/numbers agree.

### 30. S54 — Coverage and Variance Are Different

Baseline p54: Too Good — What Just Happened?. **Time target:** 1 min. **Layout (prefer):** cols.

- **Point:** Support makes IS valid; the weighted second moment makes it useful.
- **Main:** Two checks: cover nonzero fp; control integral f^2 p^2/q. A valid proposal can have larger or infinite variance.
- **Exhibit / reading:** Validity-versus-precision decision diagram; apply the two checks to the running proposal without repeating its full arithmetic.
- **Notes / Markdown:** Recap first/second moment distinction and motivate optimal/risky proposals. No second broad part summary or premature q-star calculation.
- **Evidence:** E04,E11,E18.
- **Acceptance:** Does not say every covered proposal improves on ordinary MC.

## Part 03 — Control Proposal Risk

### 31. S55 — 03 · Control Proposal Risk

Baseline p55: The Variance of IS. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** A correct mean is not enough for reliable Monte Carlo.
- **Main:** Exact section title.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Transition from a successful practical proposal to why it works and how another can fail.
- **Evidence:** E04,E18.
- **Acceptance:** Matches Contents; no duplicated theorem recap.

### 32. S56 — The Second Moment Decides

Baseline p56: Variance of the IS Estimator. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Proposal quality depends on the squared weighted integrand.
- **Main:** Under finite integral f^2 p^2/q, Var(hat(mu)_IS)=(integral f^2 p^2/q-mu^2)/n. Same target mu, proposal-dependent first term.
- **Exhibit / reading:** Annotate the single variance identity with the only term q can change.
- **Notes / Markdown:** Derive using Y=fw and ordinary sample-mean variance. If the integral is infinite, no finite RMSE follows; do not bury that qualification.
- **Evidence:** E04,E02.
- **Acceptance:** Uses f^2, not merely w^2, as the general variance criterion.

### 33. S57 — Follow the Weighted Integrand

Baseline p57: The Object to Watch. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** Allocate samples where |f|p contributes, not merely where p is large.
- **Main:** Motivate q proportional to |f|p by reducing large weighted contributions; absolute value is necessary when f changes sign.
- **Exhibit / reading:** Target density versus integrand-weighted mass schematic; one clearly marked region demanding more sampling.
- **Notes / Markdown:** Explain why matching q to p alone may be wrong for a rare-event f; intuitive proposal design is not yet a proof of optimality.
- **Evidence:** E04.
- **Acceptance:** Sign-changing integrands are not assigned a negative density.

### 34. S59 — The Optimal Proposal

Baseline p59: Theorem 4 — the Optimal Proposal. **Time target:** 3 min. **Layout (prefer):** card.

- **Point:** For known |f|p normalization, q-star minimizes IS variance.
- **Main:** Theorem with c=E_p|f| in (0,infinity): q-star=|f|p/c; minimum single-draw variance c^2-mu^2, estimator variance divided by n. State admissible proposals cover nonzero fp.
- **Exhibit / reading:** Theorem formula and named c; keep the practical unknown-normalizer caveat short enough not to obscure the statement.
- **Notes / Markdown:** If c=0, f=0 p-almost surely and the target is trivial; do not divide by c. Existence of this formal optimum is not an implementable proposal-selection algorithm.
- **Evidence:** E04, optimal-density discussion pp4-6.
- **Acceptance:** c is finite and strictly positive; q-star integrates to one and theorem allows either sign of f.

### 35. S60 — Proof: A Common Lower Bound

Baseline p60: Proof Step 1 — the Floor. **Time target:** 3 min. **Layout (prefer):** math-block.

- **Point:** Jensen gives a lower bound independent of the proposal.
- **Main:** Recall E[Z^2]>=E[Z]^2 for Z=|fw|; E_q|fw|=c by coverage, hence E_q[(fw)^2]>=c^2.
- **Exhibit / reading:** Annotated two-step Jensen chain; state equality requires |fw| constant q-almost surely.
- **Notes / Markdown:** No separate Jensen refresher slide; prior convexity result is recalled at use. Infinite second moment satisfies the lower bound trivially; finite moment gives the equality discussion.
- **Evidence:** E01,E04.
- **Acceptance:** Uses |fw| to obtain c, not f to obtain only mu; equality case is justified.

### 36. S61 — Proof (continued): Attain the Bound

Baseline p61: Proof Step 2 — $q^*$ Attains the Floor. **Time target:** 3 min. **Layout (prefer):** math-block.

- **Point:** Under q-star, the absolute weighted contribution is constant.
- **Main:** Recap lower bound c^2; substitute q-star to get |fp/q-star|=c on its support; conclude the minimum variance.
- **Exhibit / reading:** Substitution arrow into the constant magnitude and variance result.
- **Notes / Markdown:** Positive/negative f changes the sign, not magnitude; proof remains valid where f=0 because q-star puts no mass there. Full normalization argument belongs here in notes.
- **Evidence:** E04.
- **Acceptance:** Attainment and equality conditions are shown, without a repeat-only proof-summary slide.

### 37. S63 — One-Sign Integrands Permit Zero Variance

Baseline p63: Zero Variance, Verified on the Rare Event. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Constant sign makes the optimal weighted contribution itself constant.
- **Main:** For the running positive indicator, q-star(x)=exp(-(x-10)) on x>10; each fw=exp(-10), so variance zero.
- **Exhibit / reading:** Shifted exponential target-tail density and constant-contribution annotation; explicitly name this an oracle benchmark.
- **Notes / Markdown:** Show q-star=fp/mu, c=mu, and X=10+Exp(1). Sign-changing f generally leaves c^2-mu^2>0; constant negative f has the analogous sign.
- **Evidence:** E04,E11.
- **Acceptance:** Oracle follows the feasible proposal; no claim that all f can attain zero variance.

### 38. S64 — The Oracle Needs a Normalizer

Baseline p64: The Catch — $q^*$ Needs the Answer. **Time target:** 2 min. **Layout (prefer):** diagram-flow.

- **Point:** An optimal sampling law does not automatically give its normalized weights.
- **Main:** q-star=|f|p/c depends on c; for nonnegative f, c=mu is the sought expectation. Distinguish knowing a sampling recipe from evaluating the normalized ratio.
- **Exhibit / reading:** Dependency loop target normalizer → q-star weight → target estimate; the loop is the obstacle, not a universal ban on sampling unnormalized densities.
- **Notes / Markdown:** In this benchmark the exponential tail is analytically known, so the oracle is computable; in harder problems it may not be. Remove “sampling exactly means already solved” as a universal statement.
- **Evidence:** E04.
- **Acceptance:** Sampling and density/normalizer evaluation are explicitly different capabilities.

### 39. S66 — Light Tails Can Destroy Variance

Baseline p66: Worked Example — a Light-Tailed Proposal. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A proposal can cover the target yet under-visit crucial tail contributions.
- **Main:** New f=x with p=Exp(1), target mean 1; q=Exp(2), w=exp(x)/2. Mark the change of integrand from the rare-event example.
- **Exhibit / reading:** Exact target/proposal tail comparison or weight-growth graph with distribution/rate labels.
- **Notes / Markdown:** Both supports agree; lighter proposal tail makes large-x weights grow. Weight growth alone is a warning; the next actual second-moment calculation establishes failure.
- **Evidence:** E18,E04.
- **Acceptance:** f changes explicitly and support validity is retained; no unsupported conclusion from a finite plot.

### 40. S68 — A Finite Mean, an Infinite Second Moment

Baseline p68: Unbiased, Consistent — and Practically Unstable. **Time target:** 3 min. **Layout (prefer):** math-block.

- **Point:** This valid IS estimator has a finite expectation but infinite squared error.
- **Main:** Show E_q[Xw]=integral x exp(-x) dx=1 and E_q[(Xw)^2]=integral x^2/2 dx=infinity.
- **Exhibit / reading:** Two contrasting integrals as one exhibit: cancellation preserves the mean but not the second moment.
- **Notes / Markdown:** Expand density substitution step by step. Preserve bare-weight E[w^2]=infinity as a secondary check, not the argument for arbitrary f. No fabricated instability trajectory.
- **Evidence:** E18.
- **Acceptance:** Actual f-weighted second moment is used; RMSE is infinite, not simply “undefined.”

### 41. S121 — Consistency Is Not an Error Bar

New slide; position fixed by this sequence. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** Convergence can survive even when the usual finite-variance error tools fail.
- **Main:** IID integrable Y=Xw has an LLN; in this example finite-n mean-square error is infinite. The usual finite-variance CLT/RMSE argument does not apply.
- **Exhibit / reading:** Two-level implication diagram: finite first moment → consistency; finite second moment → usual variance/RMSE tools, with second condition failed.
- **Notes / Markdown:** Do not assert no convergence rate of any conceivable kind. Finite batches can look benign; observed sample variance does not establish a finite population second moment. Strong LLN can be cited, not re-proved.
- **Evidence:** E02,E18.
- **Acceptance:** No contradiction between consistency and infinite RMSE; no certainty that each batch contains a catastrophic weight.

### 42. S69 — Check the Integrand, Not Just Weights

Baseline p69: The Tail Rule of Thumb. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** Tail heuristics must be checked against f as well as p and q.
- **Main:** For the same f=x,p=Exp(1), use q=Exp(1/2): actual E_q[(fw)^2]=32/27, finite. General criterion is integral f^2 p^2/q<infinity.
- **Exhibit / reading:** Substitution into the actual weighted-integrand second moment; emphasize the f^2 factor.
- **Notes / Markdown:** Full integration: 2 integral x^2 exp(-3x/2) dx=32/27, variance 5/27 versus ordinary variance 1. Bare-weight 4/3 is not the required value. Heavier tails are a heuristic, not a universal sufficient condition for arbitrary f.
- **Evidence:** E18,E04.
- **Acceptance:** No bare-weight calculation offered as a general variance certificate.

## Part 04 — Remove the Normalizer

### 43. S72 — 04 · Remove the Normalizer

Baseline p72: Self-Normalized IS. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** Unknown normalization changes the estimator and its guarantees.
- **Main:** Exact section title.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Ordinary IS required normalized p/q; introduce the missing-normalizer problem rather than a fresh application survey.
- **Evidence:** E05.
- **Acceptance:** Matches Contents.

### 44. S73 — The Target Is Known Up to Z

Baseline p73: The Missing Constant. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** An evaluable unnormalized target is not yet an evaluable ordinary IS weight.
- **Main:** p=tilde(p)/Z with nonnegative tilde(p), 0<Z=integral tilde(p)<infinity; target mu=E_p[f]. State Z unknown.
- **Exhibit / reading:** Normalization dependency diagram with tilde(p) known and Z unknown.
- **Notes / Markdown:** Explain why a density proportionality sign does not provide p/q. A finite unknown constant is required; improper targets are outside the theorem.
- **Evidence:** E05.
- **Acceptance:** Unknown is distinguished from infinite or zero normalizer.

### 45. S74 — Compute Unnormalized Weights

Baseline p74: Unnormalized Weights. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** The computable ratio tilde(p)/q equals Z times the ordinary weight.
- **Main:** Define tilde(w)=tilde(p)/q for IID q draws; q covers all target support. The common unknown scale prevents ordinary weighting but can cancel.
- **Exhibit / reading:** Annotated ratio with a common factor Z across all weights.
- **Notes / Markdown:** Explain full support, stronger than just covering fp, because the denominator estimates total target mass. A proposal may still draw zero-target points with zero weight.
- **Evidence:** E05,E04.
- **Acceptance:** Full target-support requirement is visible, not f-specific support recycled blindly.

### 46. S75 — Normalize Only a Positive Total

Baseline p75: Definition — Self-Normalized IS. **Time target:** 2.5 min. **Layout (prefer):** math-block.

- **Point:** SNIS cancels Z by dividing weighted contributions by total weight.
- **Main:** Define self-normalized importance sampling (SNIS): sum tilde(w_i)f(X_i)/sum tilde(w_i), only when sampled total>0; normalized weights sum to one.
- **Exhibit / reading:** The ratio as one annotated estimator; show unknown common scale cancellation, not a second estimator table.
- **Notes / Markdown:** Define bar(w_i); weights nonnegative. If all sampled weights are zero, estimator is undefined unless a convention is explicitly chosen; do not silently return zero. Explain why full support does not guarantee every finite batch has positive mass.
- **Evidence:** E05.
- **Acceptance:** Positive denominator is an on-slide qualifier; SNIS does not divide by n after normalization.

### 47. S76 — Two Averages Form One Ratio

Baseline p76: Two MC Estimators, One Ratio. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Numerator and denominator estimate different integrals using the same samples.
- **Main:** E_q[tilde(w)f]=Z mu and E_q[tilde(w)]=Z; write SNIS as their sample-average ratio. Conditions: IID, full support, E_p|f|<infinity.
- **Exhibit / reading:** Numerator path to Z mu and denominator path to Z; same-sample dependence indicated.
- **Notes / Markdown:** Derive both expectations from cancellation; expectations of the two averages do not give expectation of their ratio. Preserve useful old SNIS derivation here.
- **Evidence:** E05.
- **Acceptance:** Dependence is not ignored, and E[A/B]=E[A]/E[B] is never used.

### 48. S77 — The Ratio Converges to the Target

Baseline p77: Consistency — Sketch. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** LLN plus a nonzero limiting denominator yields consistency.
- **Main:** Under the preceding conditions, sample numerator→Z mu and denominator→Z>0, so ratio→mu. Name LLN and continuity of division.
- **Exhibit / reading:** One compact two-limit-to-ratio derivation; show why the positive limit matters.
- **Notes / Markdown:** With integrable terms, strong LLN gives eventual positive denominator almost surely. Finite-n undefined events must still be handled explicitly; convergence does not imply finite-sample unbiasedness.
- **Evidence:** E05, Theorem 9.2; E02.
- **Acceptance:** No unqualified finite-n guarantee inferred from the limiting result.

### 49. S78 — One Draw Exposes SNIS Bias

Baseline p78: Honest Flag — SNIS Is Biased. **Time target:** 2.5 min. **Layout (prefer):** cols.

- **Point:** In an actual SNIS example, normalization changes the finite-sample mean.
- **Main:** Two states: tilde(p)=(3,1), q=(1/2,1/2), f=(1,0); n=1 weights cancel, so E[SNIS]=1/2 but mu=3/4.
- **Exhibit / reading:** Two possible single-draw outcomes with their probabilities, then the two means; a small state diagram instead of a dense algebra table.
- **Notes / Markdown:** Full weights (6,2), positive denominator in both cases, direct enumeration. This is an exact toy, not a simulation. Say “generally biased”; constant f or q=p are unbiased special cases.
- **Evidence:** E12,E05.
- **Acceptance:** Demonstrates this estimator's bias rather than an unrelated random-ratio anecdote.

### 50. S122 — Normalization Does Not Guarantee Improvement

New slide; position fixed by this sequence. **Time target:** 1 min. **Layout (prefer):** cols.

- **Point:** Removing Z trades a practical obstacle for a ratio-estimator problem.
- **Main:** Keep three distinct claims: scale cancellation; consistency under conditions; no universal finite-n unbiasedness or variance improvement.
- **Exhibit / reading:** Small property comparison between ordinary IS and SNIS, not a formula-heavy summary of the entire lecture.
- **Notes / Markdown:** Explain special cases and why an O(1/n) bias expansion needs additional moment/denominator regularity. Correct old note claims of automatic reduced variance or always-nonzero bias; no new asymptotic-theory chapter.
- **Evidence:** E05,E12.
- **Acceptance:** Claims are conditional, and no universal O(1/n) rate is asserted.

### 51. S70 — One Draw Can Dominate the Weights

Baseline p70: Weight Degeneracy — the Picture. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** An imbalanced batch concentrates normalized weight, not necessarily the estimated contribution.
- **Main:** Use weights (.1,.2,.1,.1,9.5), normalized shares (1%,2%,1%,1%,95%). State “95% of the normalized weight.”
- **Exhibit / reading:** Five exact share bars; axes sample index/normalized weight, heights and encodings labelled, illustrative batch.
- **Notes / Markdown:** Actual contribution is bar(w_i)f_i and can differ in magnitude/sign; imbalance may occur with finite variance and does not prove an infinite second moment.
- **Evidence:** E19,E06.
- **Acceptance:** Main, note and alt text all avoid “95% of the estimate”; no claimed empirical dataset.

### 52. S79 — Effective Sample Size Summarizes Imbalance

Baseline p79: Effective Sample Size — a Heuristic. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Empirical ESS is a weight-balance diagnostic, not literal independent information.
- **Main:** Define effective sample size ESS=(sum w)^2/sum w^2=1/sum bar(w)^2 for nonnegative weights with positive total; range 1 to n.
- **Exhibit / reading:** Equal-versus-concentrated weight patterns linked to ESS=n versus ESS near 1; use the prior batch ESS about 1.11 if readable.
- **Notes / Markdown:** Prove bounds with elementary inequalities; exact prior-batch arithmetic. Distinguish empirical ESS from the population moment proxy and from an integrand-specific error estimate.
- **Evidence:** E06,E19.
- **Acceptance:** No claim that an arbitrary f has variance equal to n/ESS times ordinary MC variance.

### 53. S81 — Healthy ESS Can Miss Missing Support

Baseline p81: What ESS Is Not. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** Equal observed weights can conceal a completely missed contribution.
- **Main:** Reuse p uniform on four states and q on the first three; observed weights equal, ESS=n, estimate 0 versus target 1/4. Label failed support assumption.
- **Exhibit / reading:** Same four-state diagram as S48 with equal observed shares/ESS and unvisited fourth state.
- **Notes / Markdown:** Full derivation; missing support violates the theorem rather than refutes consistency. Rare unobserved tails can also evade a finite-batch diagnostic, but do not claim this diagram proves every tail pathology.
- **Evidence:** E19,E06,E04.
- **Acceptance:** High ESS is visibly compatible with a wrong estimate; theorem conditions remain intact.

### 54. S82 — Choose the Estimator by What Is Known

Baseline p82: Where SNIS Runs in AI. **Time target:** 1.5 min. **Layout (prefer):** diagram-flow.

- **Point:** Sampling and density capabilities determine which estimator is available.
- **Main:** Three routes: sample target/evaluate f → ordinary MC; evaluate normalized p/q and sample q → IS; only tilde(p)/q plus support/positive denominator → SNIS.
- **Exhibit / reading:** Decision flow based on capabilities, not an applications catalogue.
- **Notes / Markdown:** Keep useful Bayesian-normalizer context from old notes with proper assumptions, but no particle-filter/MCMC chapter. Remind that available is not automatically efficient.
- **Evidence:** E02,E04,E05.
- **Acceptance:** Correct operational requirements and distinct denominators; no unsourced “used everywhere in AI” list.

## Part 05 — Differentiate Expectations

### 55. S83 — 05 · Differentiate Expectations

Baseline p83: The Score-Function Gradient. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** Learning changes the distribution whose average we want.
- **Main:** Exact section title.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Transition from scalar estimation to derivative estimation without repeating earlier estimator proofs.
- **Evidence:** E07,E15.
- **Acceptance:** Matches Contents.

### 56. S84 — The Distribution Now Changes

Baseline p84: A New Kind of Problem. **Time target:** 1.5 min. **Layout (prefer):** diagram-flow.

- **Point:** The objective depends on theta through sampled outcomes.
- **Main:** Define J(theta)=E_{X~p_theta}[R(X)] with fixed R; objective is its parameter gradient. Separate distribution parameters from the sample X.
- **Exhibit / reading:** Dependency diagram theta → distribution/draw → reward → expected reward.
- **Notes / Markdown:** Fixed reward is the initial theorem scope; if R_theta also depends explicitly on theta, an extra derivative term appears. Parameter score and sample-space score are different derivatives.
- **Evidence:** E07.
- **Acceptance:** Parameter dependence is explicit and no omitted direct reward derivative is implied.

### 57. S85 — Frozen Samples Hide the Derivative

Baseline p85: Why Plain MC Doesn't Give a Gradient. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** Differentiating a frozen reward average ignores how the draws depend on theta.
- **Main:** A list of fixed sampled values has no derivative path through the distribution; this does not mean Monte Carlo cannot estimate gradients.
- **Exhibit / reading:** Contrast a cut dependency path with a live sampling mechanism; question answered on slide.
- **Notes / Markdown:** Explain the failed naive derivative of fixed R(x_i) versus the derivative of an expectation. Avoid claiming every gradient requires REINFORCE.
- **Evidence:** E07,E15.
- **Acceptance:** The limitation attaches to frozen samples, not MC as a whole.

### 58. S123 — A Gaussian Sample Is a Recipe

New slide; position fixed by this sequence. **Time target:** 1.5 min. **Layout (prefer):** diagram-flow.

- **Point:** Parameter-independent noise exposes a differentiable path to the sample.
- **Main:** X_theta=theta+epsilon, epsilon~N(0,1); distribution N(theta,1). Recall the constructive Gaussian idea without re-deriving it.
- **Exhibit / reading:** Noise → add theta → sample diagram, with derivative through the addition marked.
- **Notes / Markdown:** Connect to prob08 X=DW+mu; what stays random/fixed when differentiating. No claim that all nonlinear Gaussian expectations are analytic.
- **Evidence:** E15,E01.
- **Acceptance:** Noise law is independent of theta, and the sampler has the intended distribution.

### 59. S124 — Differentiate Along the Sampling Path

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** A differentiable sampling recipe can turn the derivative into another expectation.
- **Main:** State pathwise identity grad J=E_epsilon[grad_theta R(T_theta(epsilon))] under a differentiable transform/reward and justified interchange; base-noise law independent of theta.
- **Exhibit / reading:** Annotated chain-rule path through T and R, with the resulting expectation.
- **Notes / Markdown:** Expand chain rule, appropriate regularity/dominating conditions, and the scope of this estimator. Discrete token sampling is not differentiable merely because probabilities are. Cite conditions rather than promise automatic interchange.
- **Evidence:** E07 §§5.2-5.3; E15.
- **Acceptance:** Differentiability and interchange are on-slide qualifications; no blanket variance ranking.

### 60. S125 — Check the Gaussian Gradient

New slide; position fixed by this sequence. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** The pathwise estimator agrees with a directly computable derivative.
- **Main:** For R(X)=X^2, X=theta+epsilon: J=theta^2+1 and derivative 2theta; pathwise contribution 2X has mean 2theta.
- **Exhibit / reading:** Two short routes to the same derivative, distinguished as analytic check and stochastic contribution.
- **Notes / Markdown:** Work out E[epsilon]=0 and Var(epsilon)=1; each sampled 2X is not itself the exact gradient, although its expectation agrees. General multivariate extension optional in notes only.
- **Evidence:** E15,E07.
- **Acceptance:** Equality is between expectations, not every draw and the true gradient.

### 61. S126 — Discrete Draws Need Another Route

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A reward on a sampled action need not be differentiable for a score estimator.
- **Main:** Introduce a two-action draw with probability sigma(theta), rewards 1 and 0; changing probabilities changes expected reward even though a sampled action has no ordinary smooth path.
- **Exhibit / reading:** Probability mass shifting between two fixed actions; no fictitious derivative of a token index.
- **Notes / Markdown:** This example motivates differentiating probability mass rather than sample values. A discontinuous inverse-CDF sample path has zero derivative almost everywhere but a moving threshold; naively swapping its derivative fails. Do not claim no discrete gradient methods other than scores exist.
- **Evidence:** E07,E13.
- **Acceptance:** Gives a concrete reason for the second route before its theorem.

### 62. S86 — The Log-Derivative Identity

Baseline p86: Technique Review — the Log-Derivative Trick. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** A probability derivative equals probability times its parameter score.
- **Main:** For positive differentiable p_theta(x), grad p_theta=p_theta grad ln p_theta; define parameter score s_theta(x)=grad_theta ln p_theta(x). Explicit natural-log convention.
- **Exhibit / reading:** Annotated algebra identity with parameter derivative highlighted.
- **Notes / Markdown:** If earlier notation used log base 2, the derivative has an ln(2) factor; this lecture uses ln/nats. Not the diffusion score grad_x ln p(x).
- **Evidence:** E07,E01.
- **Acceptance:** Differentiation variable and positivity visible; no silent base change.

### 63. S87 — Reward Times Score Gives the Gradient

Baseline p87: Theorem 5 — the Score-Function Identity. **Time target:** 2.5 min. **Layout (prefer):** card.

- **Point:** Differentiating probability mass yields a reward-weighted score expectation.
- **Main:** Theorem for a fixed finite outcome space, positive differentiable p_theta and fixed finite R: grad J=E_{p_theta}[R s_theta]. State this classroom scope; continuous extensions require valid interchange and support conditions.
- **Exhibit / reading:** The theorem equation with reward and score labelled; no unqualified all-distributions claim.
- **Notes / Markdown:** Full regularity discussion, parameter-dependent support caveat, extra E[grad R_theta] for explicit theta dependence. “Black-box reward” means reward derivative unnecessary, not that scores or integrability are unnecessary.
- **Evidence:** E07 §§4.2-4.3.
- **Acceptance:** Assumptions are enough for the proof; no hidden moving-support boundary.

### 64. S88 — Proof: Expand the Expectation

Baseline p88: Proof Step 1 — Expand the Expectation. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** A finite expectation is a weighted sum over fixed outcomes.
- **Main:** Write J(theta)=sum_x p_theta(x)R(x), fixed finite support. Mark the only theta-dependent factor.
- **Exhibit / reading:** Single expansion with p_theta active and R fixed.
- **Notes / Markdown:** Explain why the sampling operation has disappeared from the exact mathematical expectation; no derivative of a realized action is required.
- **Evidence:** E07.
- **Acceptance:** Outcome set and reward do not silently change with theta.

### 65. S89 — Proof (continued): Differentiate the Finite Sum

Baseline p89: Proof Step 2 — Swap $\nabla$ and $\sum$. **Time target:** 1.5 min. **Layout (prefer):** math-block.

- **Point:** A finite sum permits termwise differentiation without an integral-limit argument.
- **Main:** Recap expanded sum; grad J=sum_x R(x) grad p_theta(x).
- **Exhibit / reading:** Short derivative chain; probability derivative is the new step.
- **Notes / Markdown:** For integrals/infinite sums, suitable interchange assumptions must be separately verified. This slide does not prove that general extension.
- **Evidence:** E07.
- **Acceptance:** Finite proof is not sold as universal interchange justification.

### 66. S90 — Proof (continued): Read an Expectation

Baseline p90: Proof Step 3 — Log-Derivative, Then Reread. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Substitute the log derivative and recognize the sampling average.
- **Main:** Replace grad p by p s, yielding sum p R s=E[R s]; proof ends.
- **Exhibit / reading:** One annotated substitution-to-expectation chain with the sampling law clearly p_theta.
- **Notes / Markdown:** Explain each equality and provide continuous version only with its hypotheses. No separate three-step proof-summary slide, since it would only duplicate this chain.
- **Evidence:** E07.
- **Acceptance:** Final estimator uses samples from the distribution in the expectation; proof fully closes.

### 67. S92 — Average the Gradient Contributions

Baseline p92: The REINFORCE Estimator. **Time target:** 1.5 min. **Layout (prefer):** diagram-flow.

- **Point:** REINFORCE estimates the score expectation from on-policy samples.
- **Main:** Define score-function/REINFORCE estimator n^{-1}sum R(X_i)s_theta(X_i), IID under current p_theta for this classroom setting.
- **Exhibit / reading:** Sample → reward and log-probability score → average contribution recipe.
- **Notes / Markdown:** Gradient is a vector when theta is; expectation componentwise and finite variance separately. Signed rewards affect update directions; shared parameters mean no blanket claim each action probability changes independently. No claim REINFORCE was invented by the survey source.
- **Evidence:** E07.
- **Acceptance:** Sampling law and estimator match; no universal low-variance or per-action update guarantee.

### 68. S93 — A Two-Action Policy

Baseline p93: Worked Check — a Two-Action Policy. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A tiny model gives an exact derivative to check the stochastic one.
- **Main:** pi_theta(a)=sigma(theta), pi_theta(b)=1-sigma(theta), R(a)=1,R(b)=0; J=sigma(theta), J'=sigma(1-sigma).
- **Exhibit / reading:** Two-action probability/reward diagram and direct derivative, using the same example introduced at S126.
- **Notes / Markdown:** Define sigmoid and its derivative; at theta=0 both actions have probability 1/2, target derivative 1/4. Do not reuse b as both action name and baseline without explanation.
- **Evidence:** E13,E07.
- **Acceptance:** Direct expectation and derivative correct; example is continuous in parameters, discrete in actions.

### 69. S94 — Both Routes Give the Same Derivative

Baseline p94: Worked Check — the Identity Agrees. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Averaging reward-score contributions reproduces the analytic answer.
- **Main:** Scores for actions a,b are 1-sigma and -sigma; weighted expectation equals sigma(1-sigma). At theta=0, contributions 1/2 and 0 average to 1/4.
- **Exhibit / reading:** Two possible contribution values with probabilities and the resulting mean; avoid a dense multi-row ledger.
- **Notes / Markdown:** Derive both score values and their signed meaning. Preserve the complete exact check, not just “agrees.”
- **Evidence:** E13,E07.
- **Acceptance:** The averaging probabilities and score signs are right; stochastic contribution differs from its mean.

### 70. S96a — The Score Has Mean Zero

Baseline p96: Baselines — Free Variance Reduction. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Normalized probabilities imply a zero-mean parameter score.
- **Main:** Under the finite-support theorem conditions, E[s]=sum p grad ln p=grad sum p=0.
- **Exhibit / reading:** Annotated normalization identity; one logical step per line.
- **Notes / Markdown:** Why support/interchange qualifications matter in general; this is the mechanism behind baseline invariance, not itself a variance claim.
- **Evidence:** E08,E07.
- **Acceptance:** Differentiating total probability is valid under the stated conditions.

### 71. S96b — A Valid Baseline Preserves the Gradient

Baseline p96: Baselines — Free Variance Reduction. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Subtracting an action-independent baseline leaves the score-estimator mean unchanged.
- **Main:** For a constant baseline b, E[(R-b)s]=E[Rs]-bE[s]=grad J. Say explicitly: same mean, not guaranteed lower variance.
- **Exhibit / reading:** Cancellation of the baseline term using the preceding zero-score result.
- **Notes / Markdown:** Context/state-dependent baselines use a conditional identity and must not depend on the current sampled action. A learned baseline is treated appropriately as a control variate, not differentiated as part of R in this estimator. Same-batch fitted baselines require care.
- **Evidence:** E08,E13.
- **Acceptance:** Invariance is not labelled free variance reduction; arbitrary action-dependent b is not allowed.

### 72. S97 — This Baseline Removes the Toy's Variance

Baseline p97: Baseline at Work — the Toy, Revisited. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** A well-chosen baseline can make both outcomes give the same gradient contribution.
- **Main:** At theta=0 choose baseline 1/2: both contributions equal 1/4; compare no-baseline variance 1/16 with zero.
- **Exhibit / reading:** Two outcome distributions before/after, same mean line; labelled exact toy, not empirical performance.
- **Notes / Markdown:** Full two-state arithmetic and why this special case attains zero variance. No claim that expected reward is always an optimal baseline.
- **Evidence:** E13,E08.
- **Acceptance:** Mean preserved and both contributions computed correctly.

### 73. S127 — A Bad Baseline Adds Variance

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Mean invariance allows worse as well as better baselines.
- **Main:** Same toy, baseline 2: contributions -1/2 and 1, mean 1/4, variance 9/16 versus 1/16 with no baseline.
- **Exhibit / reading:** Wider exact two-point contribution distribution with the same mean; magnitude comparisons should be visual, not a six-row table.
- **Notes / Markdown:** Derive Var(g_b)=(b-1/2)^2/4. Correct the general scalar optimum b-star=E[Rs^2]/E[s^2] with finite positive denominator and finite needed moments; improvement iff b(b-2b-star)<0. For a shared scalar vector baseline minimizing trace covariance, replace s^2 by squared norm; not a universal componentwise optimum.
- **Evidence:** E13,E08.
- **Acceptance:** Bad baseline preserves mean yet increases variance by the exact amount; no “never optional” claim survives.

### 74. S128 — Two Gradient Estimators, Different Requirements

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Choose the mechanism whose differentiation assumptions match the problem.
- **Main:** Pathwise: differentiable sampling recipe and reward; score: differentiable log probability, reward derivative unnecessary. Both need valid expectation/derivative conditions; no universal variance ordering.
- **Exhibit / reading:** Two-route decision diagram grounded in Gaussian and two-action examples, not an applications list.
- **Notes / Markdown:** Compare which quantities must be computable; both support variance-reduction techniques. Retain useful reparameterization/control-variate discussion from old notes with corrected caveats, but no new estimator survey.
- **Evidence:** E07,E08,E15.
- **Acceptance:** Decision is based on capability/assumptions, not an unsupported “pathwise always wins” ranking.

## Part 06 — Reuse Samples Responsibly

### 75. S99 — 06 · Reuse Samples Responsibly

Baseline p99: Off-Policy & RLHF. **Time target:** 0.5 min. **Layout (prefer):** section-slide.

- **Point:** Reusing data introduces a second distribution, not a new target.
- **Main:** Exact section title.
- **Exhibit / reading:** Structural divider.
- **Notes / Markdown:** Apply the established ratio/gradient toolkit; do not begin a separate RL-method survey.
- **Evidence:** E04,E07,E10.
- **Acceptance:** Matches Contents.

### 76. S100 — Old Samples, a New Target

Baseline p100: The Off-Policy Problem. **Time target:** 1 min. **Layout (prefer):** diagram-flow.

- **Point:** Logged responses come from a behavior policy, not necessarily the current policy.
- **Main:** For a fixed prompt/context c, distinguish current pi_theta(x|c) from behavior pi_b(x|c) that generated logged responses. R is fixed during the update.
- **Exhibit / reading:** Current-target and logged-sampler paths feeding the estimation task.
- **Notes / Markdown:** A behavior policy is a data-collection distribution, not automatically a reference regularizer. Conditioning on c is suppressed later only with an explicit convention; broader state-visitation issues are outside this bandit/response-level example.
- **Evidence:** E04,E07,E10.
- **Acceptance:** Denominator distribution is the actual sampler; prompt conditioning is not lost.

### 77. S101 — Importance Weights Correct the Mismatch

Baseline p101: Old Samples, New Policy — It's Theorem 3. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Behavior-policy weighting recovers the target-policy expectation under coverage.
- **Main:** E_pi_theta[R]=E_pi_b[(pi_theta/pi_b)R], with full target coverage as the useful application condition; define ratio orientation.
- **Exhibit / reading:** Same target/proposal identity relabelled to current/behavior policies; show reuse rather than a fresh theorem.
- **Notes / Markdown:** For fixed behavior and valid differentiation, gradient E_pi_b[w R s_theta]; retain integrability and finite-variance caveats. Bias/variance of clipped or self-normalized versions are separate questions.
- **Evidence:** E04,E07.
- **Acceptance:** No behavior/reference substitution; weights evaluate logged samples under both policies.

### 78. S102 — Sequence Ratios Multiply

Baseline p102: Sequences Multiply Weights. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** Autoregressive factorization turns a sequence ratio into conditional token ratios.
- **Main:** For a fixed-length response and context, w(x)=product_t pi_theta(x_t|c,x_<t)/pi_b(x_t|c,x_<t). This chain rule does not assume independent tokens.
- **Exhibit / reading:** Sequence with one ratio per conditional token, then product; prefix dependence visible.
- **Notes / Markdown:** Variable lengths can include termination/EOS in the modeled sequence; do not omit factors silently. Clarify token-score sums versus sequence-weight products.
- **Evidence:** E01,E04.
- **Acceptance:** Conditional histories match in numerator/denominator; no independence claim from factorization.

### 79. S103 — Compounding Mismatch Can Destroy Efficiency

Baseline p103: Degeneracy Grows With Length. **Time target:** 2 min. **Layout (prefer):** cols.

- **Point:** Under explicit independence, modest per-token second moments compound exponentially.
- **Main:** Label “independent-token toy”: E_q[w_t^2]=1.1 and E_q[w_t]=1, independent under behavior; sequence second moment=1.1^T, about 13781 at T=100.
- **Exhibit / reading:** Exact second-moment-versus-length curve, not a language-model measurement; axes and log scale if used clearly labelled.
- **Notes / Markdown:** E20's explicit binary policies, full factorization and population proxy n/E[w^2]≈72.6 at n=10^6. This proxy is not observed ESS or an error guarantee; general autoregressive products need not factor in expectation.
- **Evidence:** E20,E06.
- **Acceptance:** All independence assumptions are visible; no universal exponential degeneration claim.

### 80. S129 — Behavior and Reference Are Different Roles

New slide; position fixed by this sequence. **Time target:** 2 min. **Layout (prefer):** diagram-flow.

- **Point:** Sampling correction and regularization compare the current policy to different distributions.
- **Main:** Three roles: pi_theta current target; pi_b generated data; pi_ref regularization reference. IS ratio uses behavior; KL penalty compares to reference.
- **Exhibit / reading:** Three-node role diagram with separately labelled correction and regularization comparisons.
- **Notes / Markdown:** Policies may coincide initially, but their jobs and later values can differ. In the historical example the reference is the fixed supervised-fine-tuned model; behavior is the rollout policy, not automatically that fixed model.
- **Evidence:** E10,E09,E04.
- **Acceptance:** Both ratios/comparisons have correct roles; no inference from closeness to reference to safe behavior weights.

### 81. S105 — KL Is Not a Variance Certificate

Baseline p105: Recall — KL Divergence. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** A drift penalty and a weight second moment control different quantities.
- **Main:** Recall D_KL(pi_theta||pi_ref)=E_pi_theta ln(pi_theta/pi_ref), in nats; a small KL does not upper-bound E_pi_b[w^2].
- **Exhibit / reading:** Two clearly labelled expectations/comparisons, with sampling/reference distinctions; keep the short negative claim on the slide.
- **Notes / Markdown:** E14's full-support two-state counterexample even when reference=behavior; compute small KL≈.001742 but second moment≈10001. Jensen gives a lower, not upper, bound on the second moment. No claim KL is useless.
- **Evidence:** E14,E01,E10.
- **Acceptance:** No reversed inequality or guarantee of stable IS from KL; natural logs explicit.

### 82. S106 — Reward Tuning Uses This Toolkit

Baseline p106: The RLHF-Shaped Objective. **Time target:** 2 min. **Layout (prefer):** math-block.

- **Point:** A scoped reward-plus-KL objective combines expectations, gradients and a reference.
- **Main:** Expand reinforcement learning from human feedback (RLHF). Historical simplified InstructGPT case: fixed prompt, maximize E_pi_theta[r]-beta D_KL(pi_theta||pi_ref), beta>=0; learned reward from human comparisons, fixed supervised-fine-tuned reference.
- **Exhibit / reading:** Annotated two-term objective identifying reward and reference penalty; not a complete training-system diagram.
- **Notes / Markdown:** Source §3.2 equation(2): PPO-ptx adds a pretraining term omitted here; no claim this is every modern alignment method. Fixed reward model during policy update. Because log-ratio reward depends on theta, derive its gradient carefully: differentiation yields a direct score term whose expectation vanishes under the same normalization/regularity assumptions, not a blind application of the fixed-R theorem.
- **Evidence:** E10,E07,E08,E21.
- **Acceptance:** Historical/simplified scope and role labels are clear; note does not omit the parameter-dependence check.

### 83. S104 — A Surrogate Is Not a Hard Constraint

Baseline p104: Keep the Ratio Near One. **Time target:** 1.5 min. **Layout (prefer):** cols.

- **Point:** PPO clipping changes the optimization objective, not every realized probability ratio.
- **Main:** Expand proximal policy optimization (PPO); state clipped surrogate is not a guarantee all ratios stay in [1-epsilon,1+epsilon]. A clipped estimate is not the exact IS identity.
- **Exhibit / reading:** Prefer Schulman et al. 2017 Figure 1 (positive/negative advantage payoff); explain x=action ratio, y=surrogate, flattening region. If redrawn, cite as redrawn and reproduce the actual min(unclipped,clipped) rule.
- **Notes / Markdown:** Full equation(7), ratio for an action conditional on state/context and old policy, sign-sensitive clipping, distinction from sequence IS and KL-penalty PPO variant. No optimization tutorial or universal safety claim.
- **Evidence:** E09 §3 equation(7), Figure 1.
- **Acceptance:** Figure/payoff is not simply clamp(r) for all signs; no assertion actual policy ratios are forcibly bounded.

## Closing — one synthesis

### 84. S109 — One Target, Different Estimators

Baseline p109: Recap — Every Tool, One Job. **Time target:** 4.5 min. **Layout (prefer):** diagram-flow.

- **Point:** Choose an estimator by its computable ingredients and justified error claims.
- **Main:** One closing comparison: ordinary MC, IS, SNIS, pathwise gradient, score gradient; pair each with its key requirement/caveat, no full formula catalogue.
- **Exhibit / reading:** A sparse decision map grounded in already-used examples; the lecturer can ask which tool fits one of those examples.
- **Notes / Markdown:** Compact complete formula reference may live in this article. Preserve useful nine-deck prerequisite links here as optional details, not additional slides or a repeated course introduction. Explain that unbiased/consistent is not synonymous with low error.
- **Evidence:** E02,E04-E08,E15.
- **Acceptance:** Only one global closing synthesis; no duplicate nine-deck roadmap or universal “estimate anything” promise.

### 85. S113 — Closer

Baseline p113: Closer. **Time target:** 0.5 min. **Layout (prefer):** end-slide.

- **Point:** End on the estimator-choice lesson.
- **Main:** Preserve established lecture closing identity; no new theorem, future-course promise or fourth recap.
- **Exhibit / reading:** Structural closer.
- **Notes / Markdown:** One-sentence closing cue; optional reading links already substantiated in the bibliography.
- **Evidence:** E01,E16.
- **Acceptance:** Proper closer, no filler or unsourced new claim.

## Baseline disposition and ID trail

The baseline source page/title map below is complete. It records identity, not permission to retain old incorrect wording. “Retire” removes an ID from final artifacts permanently; correct details named here remain in notes, while pure duplication and false claims need not be copied. Old source opening lines remain in plan-v1 for audit traceability. Final page numbers are targets; work-r1 must report actual pages and deviations.

| Baseline ID / page | Baseline title | Disposition / target page |
|---|---|---|
| S01 / 1 | Monte Carlo & Importance Sampling | Retain identity; revised target p1. See full spec. |
| S02 / 2 | Contents | Retain identity; revised target p2. See full spec. |
| S03 / 3 | Why Sampling? | Retain identity; revised target p3. See full spec. |
| S04 / 4 | Three Expectations Nobody Can Compute | Retain identity; revised target p4. See full spec. |
| S05 / 5 | The Cliffhanger, Cashed In | Retire; correct and absorb motivation into S04 and Gaussian bridge notes S123. No universal closed-form claim. |
| S06 / 6 | The Idea — Integration by Averaging | Retain identity; revised target p5. See full spec. |
| S07 / 7 | Today's Three Upgrades | Retire duplicate roadmap; S02 supplies the route, S109 the single synthesis. |
| S08 / 8 | Route Map | Retire duplicate roadmap; S02 supplies the route. |
| S09 / 9 | Recall — the Toolkit | Retire standalone recall divider; use just-in-time recalls in S16/S22/S24/S60. |
| S10 / 10 | Recall — Expectation & Variance | Retire; expectation recall in S16, variance context in S22 notes. |
| S11 / 11 | Recall — Averages Concentrate | Retire; apply prior variance/CLT in S22/S115; no repeated proof. |
| S12 / 12 | Recall — Hoeffding | Retire; adapt actual prior [0,1] Hoeffding in S24 and its notes. |
| S13 / 13 | What Is Genuinely New Today | Retire novelty inventory; purpose in S02 notes, actual new results taught where used. |
| S14 / 14 | The Monte Carlo Estimator | Retire old extra divider; Part 01 now begins at S03. |
| S15 / 15 | The Target | Retire repeated target definition; S04/S16 state it, notes retain setup. |
| S16 / 16 | Definition — the Monte Carlo Estimator | Retain identity; revised target p7. See full spec. |
| S17 / 17 | Theorem 1 — Unbiasedness | Retire reintroduced sample-mean theorem; S19 recalls it. |
| S18 / 18 | Theorem 1 — Proof | Retire repeated proof slide; S19 notes retain linearity derivation. |
| S19 / 19 | What Unbiasedness Buys | Retain identity; revised target p8. See full spec. |
| S20 / 20 | Theorem 2 — Variance | Retire reintroduced variance theorem; S22 recalls it. |
| S21 / 21 | Theorem 2 — Proof | Retire repeated proof slide; S22 notes retain derivation. |
| S22 / 22 | RMSE — the Error Yardstick | Retain identity; revised target p9. See full spec. |
| S23 / 23 | Accuracy Guarantee I — Chebyshev | Retire separate Chebyshev slide; S115 notes retain conditions and exact example. |
| S24 / 24 | Accuracy Guarantee II — Hoeffding | Retain identity; revised target p12. See full spec. |
| S25 / 25 | Worked Example — $\pi$ by Darts | Retire duplicate darts setup; S26 and its notes explain geometry and estimator. |
| S26 / 26 | The Dartboard | Retain identity; revised target p6. See full spec. |
| S27 / 27 | Six Darts by Hand | Retire ledger slide; full six-coordinate ledger in S26 notes/Markdown. |
| S28 / 28 | The Estimator's Exact Statistics | Retire exact-statistics slide; derivation and exact variance in S22 notes. |
| S29 / 29 | How Many Darts per Digit? | Retire digits table; S22 teaches scaling; useful arithmetic in its notes as RMSE, not a guarantee. |
| S30 / 30 | Guarantee, Two Ways — $\\|\hat{\pi} - \pi\\| \leq 0.01$ at $95\%$ | Retire two-bound table; full exact computations in S115/S24 notes, not lost. |
| S31 / 31 | What Monte Carlo Never Asked | Retire standalone assumptions list; S06/S16/S33 and notes state needed capabilities and moments. |
| S32 / 32 | Error Scaling & Dimension | Retire extra dimension divider; dimension is within Part 01. |
| S33 / 33 | The Remarkable Absence | Retain identity; revised target p13. See full spec. |
| S34 / 34 | The Competitor — Grid Integration | Retire separate grid setup; S37 notes retain N=m^d argument. |
| S35 / 35 | Grid Cost of Accuracy $\epsilon = 10^{-2}$ | Retire grid-cost table; S37 notes retain only properly scoped arithmetic. |
| S36 / 36 | Monte Carlo Cost of the Same $\epsilon$ | Retire competing-cost table; S22/S37 notes retain fixed-variance/cost assumptions. |
| S37 / 37 | Error vs. Work — the Picture | Retain identity; revised target p14. See full spec. |
| S38 / 38 | The Crossover at $d = 4$ | Retire crossover slide; exponent equality and its limitations in S37 notes. |
| S39 / 39 | The Honest Caveats | Retire caveat-only slide; relevant caveats must be on S33/S37, expanded in notes. |
| S40 / 40 | Implication for AI | Retire broad AI implication; S04/S33/S116 supply scoped motivation; no unsupported dimension threshold. |
| S41 / 41 | Importance Sampling | Retain identity; revised target p16. See full spec. |
| S42 / 42 | Two Ways Vanilla MC Fails | Retire repeated failure inventory; relative-error issue S116 and validity/variance distinction S54. |
| S43 / 43 | A Rare Event by Hand | Retain identity; revised target p17. See full spec. |
| S44 / 44 | Vanilla MC on the Rare Event | Retain identity; revised target p18. See full spec. |
| S45 / 45 | The Fix — Change the Sampler | Retain identity; revised target p19. See full spec. |
| S46 / 46 | Theorem 3 — the IS Identity | Retain identity; revised target p21. See full spec. |
| S47 / 47 | Theorem 3 — Proof | Split into S47a and S47b; parent retired, proof steps preserved. |
| S48 / 48 | Why the Support Condition Is Real | Retain identity; revised target p24. See full spec. |
| S49 / 49 | Definition — the IS Estimator | Retain identity; revised target p25. See full spec. |
| S50 / 50 | Weights Are Likelihood Ratios | Retain identity; revised target p20. See full spec. |
| S51 / 51 | Proposal vs. Target — the Picture | Retire old proposal picture; replace with actual non-oracle comparison S117 and source-matched notes. |
| S52 / 52 | IS on the Rare Event — a Tailored Proposal | Retire premature oracle introduction; shifted-exponential derivation moves to S63 notes/main. |
| S53 / 53 | Every Sample Says the Same Thing | Retire duplicate constant-contribution page; S63 contains the oracle result. |
| S54 / 54 | Too Good — What Just Happened? | Retain identity; revised target p30. See full spec. |
| S55 / 55 | The Variance of IS | Retain identity; revised target p31. See full spec. |
| S56 / 56 | Variance of the IS Estimator | Retain identity; revised target p32. See full spec. |
| S57 / 57 | The Object to Watch | Retain identity; revised target p33. See full spec. |
| S58 / 58 | Technique Review — Jensen | Retire standalone Jensen review; S60 recalls the exact fact at use. |
| S59 / 59 | Theorem 4 — the Optimal Proposal | Retain identity; revised target p34. See full spec. |
| S60 / 60 | Proof Step 1 — the Floor | Retain identity; revised target p35. See full spec. |
| S61 / 61 | Proof Step 2 — $q^*$ Attains the Floor | Retain identity; revised target p36. See full spec. |
| S62 / 62 | Theorem 4 — Proof Summary | Retire repeat-only two-step proof summary; S60-S61 and paired expanded proof retain all reasoning. |
| S63 / 63 | Zero Variance, Verified on the Rare Event | Retain identity; revised target p37. See full spec. |
| S64 / 64 | The Catch — $q^*$ Needs the Answer | Retain identity; revised target p38. See full spec. |
| S65 / 65 | The Other End of the Dial | Retire transition-only slide; S66 introduces the actual risk example. |
| S66 / 66 | Worked Example — a Light-Tailed Proposal | Retain identity; revised target p39. See full spec. |
| S67 / 67 | The Weights Alone Blow Up | Retire bare-weight-only argument from main; S68 notes retain it as secondary calculation. |
| S68 / 68 | Unbiased, Consistent — and Practically Unstable | Retain identity; revised target p40. See full spec. |
| S69 / 69 | The Tail Rule of Thumb | Retain identity; revised target p42. See full spec. |
| S70 / 70 | Weight Degeneracy — the Picture | Retain identity; revised target p51. See full spec. |
| S71 / 71 | Five Samples, One in Disguise | Retire overclaimed degeneracy diagnosis; corrected S70/S79 and notes separate batch imbalance from infinite variance. |
| S72 / 72 | Self-Normalized IS | Retain identity; revised target p43. See full spec. |
| S73 / 73 | The Missing Constant | Retain identity; revised target p44. See full spec. |
| S74 / 74 | Unnormalized Weights | Retain identity; revised target p45. See full spec. |
| S75 / 75 | Definition — Self-Normalized IS | Retain identity; revised target p46. See full spec. |
| S76 / 76 | Two MC Estimators, One Ratio | Retain identity; revised target p47. See full spec. |
| S77 / 77 | Consistency — Sketch | Retain identity; revised target p48. See full spec. |
| S78 / 78 | Honest Flag — SNIS Is Biased | Retain identity; revised target p49. See full spec. |
| S79 / 79 | Effective Sample Size — a Heuristic | Retain identity; revised target p52. See full spec. |
| S80 / 80 | ESS — Sanity Checks by Hand | Retire ESS sanity-check ledger; S79 diagram and notes retain exact checks. |
| S81 / 81 | What ESS Is Not | Retain identity; revised target p53. See full spec. |
| S82 / 82 | Where SNIS Runs in AI | Retain identity; revised target p54. See full spec. |
| S83 / 83 | The Score-Function Gradient | Retain identity; revised target p55. See full spec. |
| S84 / 84 | A New Kind of Problem | Retain identity; revised target p56. See full spec. |
| S85 / 85 | Why Plain MC Doesn't Give a Gradient | Retain identity; revised target p57. See full spec. |
| S86 / 86 | Technique Review — the Log-Derivative Trick | Retain identity; revised target p62. See full spec. |
| S87 / 87 | Theorem 5 — the Score-Function Identity | Retain identity; revised target p63. See full spec. |
| S88 / 88 | Proof Step 1 — Expand the Expectation | Retain identity; revised target p64. See full spec. |
| S89 / 89 | Proof Step 2 — Swap $\nabla$ and $\sum$ | Retain identity; revised target p65. See full spec. |
| S90 / 90 | Proof Step 3 — Log-Derivative, Then Reread | Retain identity; revised target p66. See full spec. |
| S91 / 91 | Theorem 5 — Proof Summary | Retire repeat-only short-proof summary; complete proof remains S88-S90 and notes. |
| S92 / 92 | The REINFORCE Estimator | Retain identity; revised target p67. See full spec. |
| S93 / 93 | Worked Check — a Two-Action Policy | Retain identity; revised target p68. See full spec. |
| S94 / 94 | Worked Check — the Identity Agrees | Retain identity; revised target p69. See full spec. |
| S95 / 95 | Reading the Identity | Retire standalone interpretation; corrected interpretation in S92 notes and worked check S94. |
| S96 / 96 | Baselines — Free Variance Reduction | Split into S96a and S96b; parent retired, mean-zero proof and invariance separated. |
| S97 / 97 | Baseline at Work — the Toy, Revisited | Retain identity; revised target p72. See full spec. |
| S98 / 98 | The REINFORCE Pipeline | Retire duplicate pipeline; S92 provides the estimator recipe, S128 comparison. |
| S99 / 99 | Off-Policy & RLHF | Retain identity; revised target p75. See full spec. |
| S100 / 100 | The Off-Policy Problem | Retain identity; revised target p76. See full spec. |
| S101 / 101 | Old Samples, New Policy — It's Theorem 3 | Retain identity; revised target p77. See full spec. |
| S102 / 102 | Sequences Multiply Weights | Retain identity; revised target p78. See full spec. |
| S103 / 103 | Degeneracy Grows With Length | Retain identity; revised target p79. See full spec. |
| S104 / 104 | Keep the Ratio Near One | Retain identity; revised target p83. See full spec. |
| S105 / 105 | Recall — KL Divergence | Retain identity; revised target p81. See full spec. |
| S106 / 106 | The RLHF-Shaped Objective | Retain identity; revised target p82. See full spec. |
| S107 / 107 | One Pipeline, Every Tool of Today | Retire second whole-toolkit pipeline; S106 supplies application and S109 one global synthesis. |
| S108 / 108 | Closing the Probability Half | Retire extra closing divider; end with S109 then S113. |
| S109 / 109 | Recap — Every Tool, One Job | Retain identity; revised target p84. See full spec. |
| S110 / 110 | Nine Decks, One Arc | Retire nine-deck map from main; useful prerequisite links in S109 notes. |
| S111 / 111 | What the Probability Half Gave You | Retire repeated course toolkit; optional concise course context in S109 notes. |
| S112 / 112 | Bridge — From Estimating to Optimizing | Retire sweeping closing promise; S109 gives conditional estimator choice, S04 scoped motivation. |
| S113 / 113 | Closer | Retain identity; revised target p85. See full spec. |

### New-ID insertion register

| New ID | Position | Target page |
|---|---|---:|
| S114 | After S22 | 10 |
| S115 | After S114 | 11 |
| S116 | After S37 | 15 |
| S117 | After S49 | 26 |
| S118 | After S117 | 27 |
| S119 | After S118 | 28 |
| S120 | After S119 | 29 |
| S121 | After S68 | 41 |
| S122 | After S78 | 50 |
| S123 | After S85 | 58 |
| S124 | After S123 | 59 |
| S125 | After S124 | 60 |
| S126 | After S125 | 61 |
| S127 | After S97 | 73 |
| S128 | After S127 | 74 |
| S129 | After S103 | 80 |

## Executable packages

All content packages may edit **only their assigned ID blocks** in the three prob09 artifacts and corresponding new deck-local figure assets/generators. Their main/HTML/Markdown file paths are the full paths in the header; there is no tech file. They may not independently change document preambles, Contents, dividers, global citation lists, shared styling, reference library, OUTLINE or other lectures. Structural IDs inside a package's span belong to integration, not that worker.

slides chooses whether/how to parallelize. If multiple workers touch the same files, use isolated worktrees/branches and integrate only assigned sections; a worker does not rewrite the whole note file. No agent-model configuration changes are authorized. The integrator first establishes final-ID placeholders and shared notation, so a note rewrite cannot race identity preparation.

| Package | Final content span / assigned IDs | Responsibility | Dependencies |
|---|---|---|---|
| P1 | pp4-15: S04,S06,S26,S16,S19,S22,S114,S115,S24,S33,S37,S116 | Ordinary MC, uncertainty, dimension/relative error; associated notes; dart/rate exhibits | E01-E03,E11,E17; identity setup |
| P2 | pp17-42 content: S43,S44,S45,S50,S46,S47a,S47b,S48,S49,S117,S118,S119,S120,S54,S56,S57,S59,S60,S61,S63,S64,S66,S68,S121,S69 | IS identity and proof, practical proposal, optimality, tail-risk proof; associated notes; owns running rare-event and exponential-risk calculations/figures | P1 estimator/relative-error conventions; E04,E11,E18,E19; identity setup |
| P3 | pp44-54: S73,S74,S75,S76,S77,S78,S122,S70,S79,S81,S82 | SNIS and diagnostics; associated notes; exact finite-state/batch examples | P2 support counterexample and weight convention; E05,E06,E12,E19 |
| P4 | pp56-74: S84,S85,S123,S124,S125,S126,S86,S87,S88,S89,S90,S92,S93,S94,S96a,S96b,S97,S127,S128 | Pathwise/score gradients, new proof and baseline correction; associated notes; Gaussian/two-action calculations | P1 averaging and E01's revised Gaussian prerequisite; E07,E08,E13,E15 |
| P5 | pp76-83: S100,S101,S102,S103,S129,S105,S106,S104 | Scoped sample reuse, policy roles, KL and clipping correction; associated notes; exact compounding toy/source figure | P2 ratios, P4 scores and baseline assumptions; E09,E10,E14,E20,E21 |

**Shared notation agreement:** X random outcome, f fixed integration function, mu its target; R fixed gradient-example reward, r fixed learned reward in the application; p target, q proposal; w normalized density ratio, tilde(w) unnormalized ratio, bar(w) normalized sampled share; sigma_f population SD, s_Y observed sample SD; theta model parameters; pi_b behavior and pi_ref reference never interchangeable. Exponential distributions use rate parameter. ln/nats throughout gradient/KL content. Keep chosen hat/bar notation consistent in all artifacts.

### Integration-owned shared surfaces

1. **Identity and records:** perform commits A/B; maintain all immutable IDs, splits/retirements and actual page map; copy announced plan files unchanged and refresh living job/requests/evidence at pushes.
2. **Structural slides:** S01,S02,S03,S41,S55,S72,S83,S99,S109,S113, including brief matching notes. Exactly six Contents/divider names. S109 is the only global closing synthesis; scoped comparisons S82/S128 have distinct instructional purposes and are not repeated closers.
3. **Companions:** note preambles, navigation, bibliography and final whole-document accessibility. Preserve appropriate old anchors or redirect navigation where practical, without keeping obsolete chapters as conflicting text. Every remaining slide has exactly one ordered HTML article with equal ID and matching heading; retired parent IDs do not survive as phantom articles. Markdown can use readable IDs in headings or unobtrusive markers but remains standalone ASCII/LaTeX.
4. **Figures and references:** integrate package assets, collect actual generator paths/inputs/seeds, source/version/figure citations and bibliography. No unsupported stock figure or decorative chart. Do not edit shared reference code to force local fit.
5. **Cross-references:** update theorem numbers, slide/title links, quantities and natural-log convention; no stale “Theorem 5” merely inherited after old results are removed. Earlier lectures are read-only, and on-slide points remain self-contained.
6. **Outlines/counts:** update prob09 in courses/deepmath/OUTLINE.md and any ancestor pointer actually made stale, using the canonical required count locations. Record actual slide count and section scope rather than the 85 target as fact. No unrelated outline cleanup.
7. **Build validation:** integrate against the job baseline, not moving main; renderer/linter output is checked, not accepted as a substitute for teaching/visual review. Return substantive plan issues before altering scope or facts.

## Acceptance and work report

### Required checks before work-r1

- **Source and request coverage:** C01-C04 answered; all v1 audit items resolved in both slide and note layers. E11-E21 calculations independently executable; sources have correct versions/sections/figure attribution. No erroneous old “every Gaussian integral,” “RMSE undefined,” “95% of estimate,” “all baselines help,” or “clipping constrains all actual ratios” survives elsewhere.
- **Structure:** unique final IDs; exact slide-to-HTML-article order and title match; no empty scaffolds; new/split IDs documented; 113 baseline IDs each accounted for. Markdown has the same logical sequence and no dropped derivation from the retirement map.
- **Narrative/design:** titles alone express the arc. Each content slide has one main exhibit, its point and necessary qualifier. New central proofs are on main slides at a teachable pace; familiar sample-mean proofs are not reintroduced. No font-size reductions, forbidden density/capacity patterns or unsupported cross-deck shorthand. Necessary splits are preferable to shrinking.
- **Rendering:** main deck fully rendered at canonical size and all slides visually inspected; check proofs, plots, labels, footers and source lines for clipping/overlap/wraps. HTML notes checked at desktop and approximately 430px, including long equations and URLs; zero horizontal article overflow. Check math errors, navigation/anchors and links. Accessible Markdown checked for ASCII/LaTeX validity, standalone verbal figures and linearized tables. Record real check results, not only intended tests.
- **Scope:** only authorized prob09 artifacts/assets and stale outline pointers change beyond this job's logs. No prob01-prob08/reference/global design-system edits or gratuitous format churn. No deliverable PDF to Albert unless he asks.

### work-r1 must report

Branch, exact reviewable head SHA, A/B setup SHAs and setup equivalence checks; per-package outcome; full `slide ID | old page | new page | split/moved/retired` mapping; final count and pacing differences; all deviations and unresolved plan issues; any unsourced facts; actual figure-generation paths with inputs/seed; actual lint/render/accessibility checks and which slides were visually inspected. Include the block-to-baseline assignment from commit A. Push the named content and record before sending its pointer.

### Review / PR gate

Owner reviews the named commit in order: Albert's request, sources, current design rules, then this plan. First pass covers all content and notes; later passes only changed slides and neighbours. Blocking findings alone trigger another round, maximum three. A changed argument/spec becomes plan-v3 rather than an ad hoc chat instruction. Approval is pinned to a SHA. After approval slides pushes the final records; owner verifies all later commits touch only log/2026-11-17-prob09-major-revision/ before opening the PR against main. Albert's “go ahead” is **not** permission to merge.
