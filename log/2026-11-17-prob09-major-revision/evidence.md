# Evidence register

Append-only. Entries checked 2026-11-17. Equations below use natural logarithms where applicable. These are sources and mathematical checks, not the plan as evidence. Proposed examples are illustrative, not empirical results. No generated figure is accepted yet; slides must report each actual repository generator path, inputs and parameters in its work report so an evidence entry can be appended before approval.

## E01 — Current course prerequisites

- Claim: prob09 can reuse LOTUS/Jensen (prob01 pp21-22/53), continuous KL (prob03 p89), sequence factorization (prob04 p19 and prob07 p121), sample-mean variance and LLN/CLT (prob05 pp39/46/93), bounded Hoeffding (prob06 p18), bias-variance/sample mean (prob07 pp98/102), and Gaussian construction (prob08 p37).
- Source/version: repository commit b20ab73ac7e74e9489d379cf9caad7565f17e31e, courses/deepmath/{deck}/{deck}.html; precise paths/lines in plan-v1 continuity table. https://github.com/albert-no/slides/tree/b20ab73ac7e74e9489d379cf9caad7565f17e31e/courses/deepmath
- Setup: actual revised main, including 51-slide prob06, 130-slide prob07 and 154-slide prob08, not old backups.
- Does not establish: correctness of all earlier material or permission to revise those decks. prob06's main theorem is stated on [0,1]; general [a,b] requires the one-line rescaling. No assumption that product-KL additivity was previously proved just because an old note says so.
- Label: published result (course artifact / prerequisite record).

## E02 — Monte Carlo error and practical uncertainty

- Claim: IID averaging has variance sigma_f^2/n when finite; estimated standard error and asymptotic intervals need assumptions distinct from a nonasymptotic bound.
- Source/version: Art B. Owen, Monte Carlo theory, methods and examples, posted Ch.1-2 PDF, §§2.1-2.2,2.7-2.8. https://artowen.su.domains/mc/Ch-intro.pdf (accessed 2026-11-17).
- Setup: scalar integrand under an IID sampler. First absolute moment suffices for mean/LLN; finite variance is needed for this RMSE and the usual CLT.
- Does not establish: dimension-independent cost/variance, finite-sample normal coverage, or validity after selecting the integrand using the same evaluation sample.
- Label: published result.

## E03 — Tensor-grid comparison

- Claim: second-order tensor midpoint scaling is a particular smooth-integrand comparison, not a universal dimension threshold for numerical integration.
- Source/version: Owen, posted Chapter 7, §§7.1 and 7.4. https://artowen.su.domains/mc/Ch-quadrature.pdf (accessed 2026-11-17).
- Setup: regular tensor grids, sufficient smoothness, derivative-dependent constants, comparable evaluation costs. Exponents -2/d and -1/2 are a schematic comparison.
- Does not establish: “all grids fail at d=10” or that crossing exponents at d=4 proves a practical runtime crossover.
- Label: published result.

## E04 — Ordinary importance sampling

- Claim: require coverage of nonzero fp and computable p/q; variance depends on the weighted integrand. Optimal q is proportional to |f|p, with an oracle normalizer caveat.
- Source/version: Owen, posted Chapter 9 (copyright 2009-2013,2018), §9.1, Theorem 9.1 and optimal-density discussion, printed pp4-6. https://artowen.su.domains/mc/Ch-var-is.pdf
- Setup: integrable f; IID proposal samples. Second moment integral is integral f^2 p^2/q. For c=E_p|f| in (0,infinity), the one-sample minimum is c^2-mu^2.
- Does not establish: all proposals reduce variance, or that being able to sample an unnormalized law means one knows its normalizer. The operational obstruction is evaluating the normalized optimal weight, not a universal impossibility of sampling q*.
- Label: published result.

## E05 — Self-normalization

- Claim: a ratio cancels unknown constants; full target support and a nonzero sampled denominator matter. Bias is possible at finite n.
- Source/version: Owen Chapter 9, §9.2, Theorem 9.2, equations (9.6)-(9.10), printed pp8-10. Same URL as E04.
- Setup: 0<Z<infinity, E_p|f|<infinity, IID q samples covering p. State the estimator only when the denominator is positive; distinguish eventual positivity from positivity in every finite batch.
- Does not establish: bias in every special case, finite-n optimality of an asymptotic proposal, universal O(1/n) bias without regularity, or guaranteed variance reduction from normalization.
- Label: published result.

## E06 — Weight diagnostics

- Claim: (sum w)^2/sum w^2 diagnoses sampled weight imbalance; it is not an integrand-specific accuracy certificate.
- Source/version: Owen Chapter 9, §9.3, equations (9.13)-(9.14), printed pp11-12. Same URL as E04.
- Setup: nonnegative weights, at least one positive. Population second-moment proxy and empirical ESS are different objects.
- Does not establish: infinite variance from one imbalanced batch; missing support/tails can look healthy.
- Label: published result.

## E07 — Gradient-estimator assumptions and alternatives

- Claim: score-function and pathwise estimators use different differentiability assumptions; neither is a universally lower-variance choice.
- Source/version: Mohamed, Rosca, Figurnov, Mnih, “Monte Carlo Gradient Estimation in Machine Learning,” JMLR 21(132), 2020, §§4.2-4.3,5.2-5.3.2 (especially printed p22). https://jmlr.org/papers/volume21/19-346/19-346.pdf
- Setup: score-function identity with a fixed reward and valid differentiation/interchange; pathwise derivative with parameter-free base noise, differentiable transformation/reward and valid interchange. Finite positive-support discrete theorem is the classroom core.
- Does not establish: every MC gradient must be REINFORCE, direct differentiability of sampled tokens, or pathwise superiority whenever available.
- Label: published result.

## E08 — Baselines preserve the mean, not automatically improve variance

- Claim: an appropriate sample-independent baseline leaves the score-function mean unchanged; a poor choice can increase variance.
- Source/version: Mohamed et al., JMLR 2020, §7.4.3, “Baselines,” printed p36, equation (61); same URL as E07.
- Setup: score has mean zero; scalar example or clearly specified vector variance criterion. State-dependent baselines require the conditional version; fitting on the same sampled actions needs care.
- Does not establish: arbitrary baselines are a free variance reduction, average reward always minimizes variance, or all vector components share one optimum.
- Label: published result.

## E09 — PPO clipping is a surrogate, not a hard policy-ratio constraint

- Claim: PPO-Clip uses the minimum of unclipped and clipped advantage-weighted terms; it does not enforce that every probability ratio remains inside the clipping interval.
- Source/version: Schulman, Wolski, Dhariwal, Radford, Klimov, “Proximal Policy Optimization Algorithms,” 2017, v2, §3 “Clipped Surrogate Objective,” equation (7), Figure 1; §4 distinguishes a KL-penalty variant. https://arxiv.org/pdf/1707.06347
- Setup: old-policy conditional action ratio and estimated advantage, not a full-sequence importance weight clipped uniformly for all purposes.
- Does not establish: exact unbiased off-policy gradients after clipping, bounded actual weights, or a guarantee that a reference-policy KL penalty stabilizes importance sampling.
- Label: published result.

## E10 — A scoped RLHF example

- Claim: the InstructGPT PPO objective uses a learned reward and a reference-policy KL penalty; PPO-ptx additionally includes pretraining likelihood.
- Source/version: Ouyang et al., NeurIPS 2022, §3.2 “Models,” reinforcement-learning paragraph and equation (2); venue order verified. https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html ; https://arxiv.org/html/2203.02155v1
- Setup: prompt-conditioned responses, reward model fitted from human comparisons, SFT reference; gamma=0 for PPO and additional term for PPO-ptx.
- Does not establish: a description of every present-day alignment method or that behavior policy equals reference policy. Proposed lecture retains an explicitly simplified historical example, not a frontier survey.
- Label: published result.

## E11 — A useful non-oracle proposal for the running rare event

- Claim/calculation: for p=Exp(1), f=1{x>10}, mu=exp(-10), and q_lambda=Exp(lambda), 0<lambda<2,
  E_q[(fw)^2]/mu^2 = exp(10 lambda)/(lambda(2-lambda)).
  This follows by integrating exp(-(2-lambda)x)/lambda from 10 to infinity and dividing by exp(-20).
- Setup: lambda=0.1, deliberately simple illustrative choice, not an empirical optimum. Relative variance per draw is 13.3067464656; ordinary sampling gives exp(10)-1 = 22025.4657948. Relative RMSE <=0.1 requires n>=1331 versus n>=2202547, using ceilings of exact formulas. Equal per-draw work assumed; not wall-clock speedup or a 95% guarantee.
- Source: our calculation using E04's second-moment identity; independently evaluated with Python math on 2026-11-17. Mathematical inputs are all recorded above. Suggested exhibit contrasts rare-event coverage and error, not a manufactured benchmark.
- Does not establish: generic 1655x speedup; the zero-variance shifted exponential remains a separate oracle teaching case.
- Label: our calculation / illustrative example. Generator path: not yet assigned; no figure generated.

## E12 — An actual SNIS bias example

- Claim/calculation: states {a,b}, unnormalized target (3,1), normalized target p=(3/4,1/4), q=(1/2,1/2), f=(1,0). Computable weights are (6,2). At n=1, SNIS equals f(X), so its expectation is 1/2, not target 3/4. Both weights are positive, so denominator is defined.
- Source: direct enumeration, independently checked; E05 provides the estimator definition.
- Does not establish: bias for all f,q,n; f constant or q=p provides counterexamples to that universal claim. This replaces the old unrelated random-ratio example rather than adding another anecdote.
- Label: our calculation / illustrative example. Generator path: not yet assigned.

## E13 — Good and bad baselines on the same two-action example

- Claim/calculation: at theta=0, sigmoid action probability 1/2, rewards (1,0), scores (1/2,-1/2). For constant b, g=(R-b)s has mean 1/4 and variance (b-1/2)^2/4. Thus b=0: variance 1/16; b=1/2: zero; b=2: 9/16.
- Source: enumerate both outcomes; mean=( (1-b)/2 + b/2 )/2=1/4. General scalar minimum from the existing note is b*=E[Rs^2]/E[s^2] when 0<E[s^2]<infinity; improvement iff b(b-2b*)<0. E08 checks interpretation.
- Does not establish: one common componentwise-optimal vector baseline. A shared scalar minimizing trace covariance instead uses squared score norm. Mean-zero score plus baseline invariance need their stated assumptions.
- Label: our calculation / illustrative example. Generator path: not yet assigned.

## E14 — Small KL is not a weight-variance upper bound

- Claim/calculation: take target p=(0.9999,0.0001), proposal q=(1-10^-12,10^-12), full support. Natural-log KL D(p||q)=0.00174207307556, while E_q[w^2]=10000.99980001. Direct two-term sums verify this.
- Source: definitions in prob02/prob03 (E01), direct calculation. Jensen gives log E_q[w^2]>=D(p||q), a lower bound on the second moment, not an upper bound. Using a lower bound in reverse cannot certify safety.
- Does not establish: KL is useless; it measures a different property. Distinguish pi_b (sampling distribution) from pi_ref (regularization reference), even when they initially coincide.
- Label: our calculation / illustrative example. Intended for notes; no new main-slide theorem required. Generator path: not applicable unless slides elects to visualize.

## E15 — Gaussian reparameterization connection

- Claim: the established X=DW+mu construction can become a pathwise sampling recipe with parameter-dependent D,mu and parameter-independent W, subject to differentiability/interchange.
- Sources/version: prob08 p37 at E01's commit; Kingma and Welling, “Auto-Encoding Variational Bayes,” ICLR 2014, §2.3 (arXiv record v11 is an abstract-typo update), https://arxiv.org/abs/1312.6114 ; gradient conditions verified in E07.
- Setup: introductory scalar X=theta+epsilon, epsilon standard normal suffices. Reward R(X)=X^2 gives derivative 2theta, pathwise integrand 2X; compare mechanism, not a universal variance ranking.
- Does not establish: Gaussian input makes E[R(X)] closed form for every nonlinear R, or that Gaussian reverse mixtures in diffusion are exactly Gaussian.
- Label: published result plus our illustrative substitution.

## E16 — Planning integrity / limitations

- Claim: the current prob09 notes do not implement the current per-slide instructor-note contract; its old source attributions to prob01 for variance/exponential means and prob02 for product-KL need correction or independent derivation.
- Source/version: baseline note HTML lines34-69 and sections4.5,6.6,8.6-8.7,9.4-10.4; complete current prob01-prob08 title sequences plus actual source slides checked. DESIGN_SYSTEM.md §9 is the authoritative required structure.
- Setup: note HTML has 11 section elements and zero article/data-slide-id/message entries. The accessible Markdown is a separate self-contained artifact, not disposable when HTML is restructured.
- Does not establish: every earlier formula is missing from every note; uncertainty is resolved by importing the fact explicitly rather than claiming a prior proof that was not found.
- Label: published result (course-artifact audit).


## E17 — Retained dart illustration and error arithmetic

- Claim/calculation: six hand-chosen points (0.5,0.5), (-0.9,0.8), (0.2,-0.6), (-0.4,0.1), (0.8,-0.7), (0.3,0.9) give four unit-disk hits, hence 4(4/6)=8/3. They are an illustration, not an IID realization or a convergence experiment.
- Source/version: baseline prob09 pp25-30, equations independently recomputed using the exact unit-square/unit-disk geometry and E02. For actual IID uniform draws on [-1,1]^2, Y=4 indicator(hit) has variance pi(4-pi)=2.6967662132698145. Chebyshev at epsilon=.01, delta=.05 gives ceil(pi(4-pi)/(.05*.01^2))=539354; Hoeffding with range [0,4] gives ceil(16 ln(40)/(2*.01^2))=295111.
- Limits: these bounds are sufficient, not minimal sample sizes; the Chebyshev calculation uses a known variance in a pedagogical benchmark. A displayed six-point hand example does not support a statistical error bar.
- Label: our calculation / illustrative example. Figure-generator path awaiting slides; points above are deterministic inputs.

## E18 — Check the weighted integrand's second moment

- Claim/calculation: with p=Exp(1), f(x)=x, q=Exp(2), w=e^x/2. E_q[fw]=integral x exp(-x) dx=1, but E_q[(fw)^2]=integral x^2/2 dx=infinity. A nonnegative IID sample mean remains consistent by the integrable LLN; finite-n squared error has infinite expectation.
- Contrast: q=Exp(1/2) gives E_q[(fw)^2]=2 integral x^2 exp(-3x/2) dx=32/27; variance per draw is 5/27. Bare-weight E_q[w^2]=4/3 is a different number. Ordinary sampling of X has variance 1.
- Source: direct integration with E04; baseline prob09 pp66-69 supplies the example. Checked with integral x^2 exp(-a x) dx=2/a^3, a>0.
- Limits: a heavy-tail label alone does not establish integrability for arbitrary f, nor a universal variance improvement. Do not claim every finite batch has a giant weight or use finite sample variance as proof of finite population variance.
- Label: our calculation / illustrative example. No stochastic plot required; any new plot must record generator inputs/path.

## E19 — Exact finite-batch diagnostics and missed support

- Claim/calculation: weights (.1,.2,.1,.1,9.5) sum to 10, normalized shares (.01,.02,.01,.01,.95), and empirical ESS=100/90.32=1.1071744907. This describes weight imbalance, not 95% of the estimated sum for arbitrary f.
- Support example: p uniform on {1,2,3,4}, q uniform on {1,2,3}, f=indicator(x=4). All observed p/q are 3/4; normalized weights are 1/n and ESS=n, but both weighted estimates are zero while the target is 1/4.
- Source/version: direct enumeration and E04/E06; baseline pp48,70,79-81. Equal positive weights attain ESS=n; a single positive weight attains ESS=1.
- Limits: the support-failure example violates the consistency theorem; it is not a counterexample to that theorem. Neither an imbalance nor a healthy ESS proves a population second-moment condition.
- Label: our calculation / illustrative example. Deterministic bar inputs above; repository generator path awaiting slides.

## E20 — Explicit independent-token compounding toy

- Claim/calculation: let behavior tokens be independent binary draws q=(1/2,1/2), target tokens independent with p=((1+sqrt(.1))/2,(1-sqrt(.1))/2). Then each token weight has E_q[w_t]=1 and E_q[w_t^2]=1.1. Independence under q gives E_q[(product_{t=1}^T w_t)^2]=1.1^T. At T=100 this is 13780.61234; the population proxy n/E_q[w^2] at n=10^6 is 72.5657.
- Source: our direct two-state calculation plus probability product rule/independence (E01) and E06's diagnostic scope. This makes the old moment-only caricature an explicit example.
- Limits: autoregressive token ratios generally depend on the common prefix and cannot be factored this way without additional conditions. The population proxy is not an observed ESS, a count of independent samples, or an accuracy guarantee. No universal exponential law for language models follows.
- Label: our calculation / illustrative example. If plotted, use the exact formula, no random seed needed; repository generator path awaiting slides.


## E21 — Differentiate the scoped reward-plus-KL objective correctly

- Claim/calculation: on a fixed finite support with positive differentiable p_theta and fixed positive reference q, fixed reward r and fixed beta, J=sum p_theta r-beta sum p_theta ln(p_theta/q) has gradient E_p[(r-beta ln(p_theta/q)) grad ln p_theta]. Differentiating the KL contributes both sum (grad p_theta) ln(p_theta/q) and sum grad p_theta; the second is grad 1=0. Thus the displayed score form is justified by normalization, not by pretending the log-ratio reward has no theta dependence.
- Sources: direct differentiation from E07's score identity and E10's simplified objective. Continuous or infinite outcome spaces need appropriate differentiation/interchange and integrability assumptions separately.
- Limits: this is not a derivation of PPO's clipped optimization surrogate, nor a permission to ignore arbitrary parameter-dependent reward terms. The learned reward model and reference are fixed for this policy-gradient calculation.
- Label: our calculation. No figure generator required for the note derivation.
