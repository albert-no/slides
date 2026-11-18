# plan-v2 — Sampling access to P is the motivation

## Change from the initial compact spec

The frozen request/spec in `job.md` is version1. This amendment incorporates Albert's new C02 in `requests.md` and supersedes the emphasis and acceptance criteria for S130/S131 below. All other scope, source, condition, notes, bridge, outline and check requirements in job.md remain in force. It is still a small, two-slide rewrite with the same one review round and no new literature. Do not await another approval or expand the lecture.

## The required distinction [judgment]

Albert's intended message is that data samples suffice for fitting a model by forward KL, even though the true data pmf/density is not available pointwise. This must be the main motivation, not a footnote about what an expectation is.

The mathematically precise statement is:

- From IID X_i ~ P and computable q_theta(X_i), we can estimate L(theta) = E_P[-log q_theta(X)] using the sample average.
- L(theta) = D(P||Q_theta) + H(P). Since H(P) does not depend on Q_theta, minimizing L is equivalent to minimizing the population KL. The empirical mean is a Monte Carlo surrogate for that objective.
- **No evaluations of p(X_i), and no value of H(P), are needed for this log-loss objective or its model comparisons.** Sampling access is enough.
- **The sample average alone is not an estimate of the absolute numerical value D(P||Q_theta).** It estimates KL plus the fixed entropy. Reporting absolute KL would additionally require the entropy term or another estimation method; that is outside this example. Do not write the unqualified claim “compute KL without knowing P.”

These are consequences of the same existing identity and sample-mean result in job.md; no new source or research pass is required. The finite-term/support and fixed-model/IID caveats from that spec still apply.

## Slide-level amendment

### S130 / p4 — Why log loss fits the model to P

Retain the identity and role definitions from job.md: fixed data distribution P versus variable model Q_theta. Make “minimize KL without evaluating the data distribution” the point of the identity, not just an observation that entropy is constant. A suitable point line is **“Fixed data entropy: log loss and KL have the same population minimizers.”** The note Message must say P is fixed and its pointwise probabilities need not be available.

### S131 / p5 — Sampling P is enough [judgment]

**Suggested title:** “Fit Q Without Evaluating P” (slides may choose a clearer equivalent).

The main exhibit must show all three:
1. **Available:** data X_i sampled IID from P, and model probabilities q_theta(X_i).
2. **Computation:** the average (1/n) sum_i log(1/q_theta(X_i)).
3. **Target:** E_P[log(1/q_theta(X))] = D(P||Q_theta) + H(P).

The explicit main-slide takeaway is **“Sample P; evaluate Q; minimize KL up to a fixed entropy term.”** Equivalent wording is fine, but the fixed-constant scope must remain visible. Say or label directly that **p(X_i) is not needed**. Do not make students infer this from the absence of p in the formula. Avoid wording that suggests we sample from Q or know P's probability values merely because data are available.

Keep the fixed-theta finite-mean qualifier for estimation claims. Population objective equivalence is exact; approximation and sampling error attach to the empirical mean. Finite-data fitting does not guarantee the population minimizer. No training algorithm or generalization tutorial on the main slide.

### Notes / optional supporting detail

H/M Messages must lead with sampling access rather than an evaluable P, and retain “KL plus fixed entropy” / “KL minimization,” not “absolute KL.” Explain that natural data provide samples from the underlying distribution without exposing its probability formula.

Optional detail, **not another main slide**: when comparing two fixed candidate models under the same P,

D(P||Q_1) - D(P||Q_2) = E_P[log(q_2(X)/q_1(X))].

Thus a sample average of the log-probability ratio estimates a KL difference with the entropy cancelling; an absolute KL value still is not produced by the original mean log loss. Include only if it helps the lecturer answer the natural “so what can we actually compute?” question. Break long math in the narrow notes, not by shrinking.

### S04 / p6 and shared surfaces

Unchanged from job.md: update only the bridge from the data-log-loss example to the separately model-sampled generator example. Update the leaf outline's opening summary to emphasize **sample-based KL minimization without evaluating P**, not one-hot CE. No new pages, figures, sources or scope are required.

## Coverage and acceptance

| Comment | Slides | Acceptance |
|---|---|---|
| C01 | S130/S131; bridge S04 | The actual data-log-loss mean is explicitly linked to its expectation, KL and the correctly signed fixed entropy. |
| C02 | S130/S131 | Main slide states that data samples and evaluable q suffice; p values are not needed for the objective. It clearly distinguishes KL minimization/up-to-constant estimation from recovering absolute KL. Both notes make the same distinction. |

Return one integrated work-r1 for job.md plus this amendment, with the exact pushed SHA and checks. Record any incompatible work already completed as a deviation to resolve before handoff, not as a separate job or review round.
