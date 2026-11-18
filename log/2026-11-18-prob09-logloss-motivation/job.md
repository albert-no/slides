job: 2026-11-18-prob09-logloss-motivation
size: small
deck: courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html
audience / mode / duration: junior undergraduate AI majors / rigorous, example-led / no fixed pacing target (Albert's prior decision remains)
baseline: 3635bd8241cb35c57b59323be871e4e9a00d6b46 (70-slide PR77 head; current pp4-5)
id commit: c47b198f8e8d0153fee6923ce2dafe8b13f4fe77 (inherited; no new ID migration)
branch: 2026-11-17-prob09-major-revision (existing PR77 continuation, as in preceding follow-up; no second branch/PR)
pr: 77 (existing, open)
pr url: https://github.com/albert-no/slides/pull/77
state: approved
round: 1 of 1
current action: review-r1 approved at 7f624f37a1b28f44cac32225664496329286e760; C01/C02 covered, no open findings; await final record-only push before updating existing PR77; no merge order
review candidate: 7f624f37a1b28f44cac32225664496329286e760
current plan: plan-v2.md amendment plus frozen initial spec below
albert decisions:
- 2026-11-18 16:02 KST: clarified the intended pp4-5 motivation: a sample average of log(1/q(X)), with X drawn from P, is Monte Carlo for cross-entropy; its difference from forward KL is a model-independent entropy term. This supersedes the preceding job's one-hot/classifier-led opening only. No merge order.
- 2026-11-18 16:07 KST: C02 emphasizes sampling from the true P without knowing its probability formula. Work order refined to sample-based KL minimization/up to fixed entropy, not an unsupported absolute-KL claim; no structural change or merge order.
verification: fresh GitHub REST confirms PR77 open/unmerged, head3635bd8, base main b20ab73ac7e74e9489d379cf9caad7565f17e31e; mounts confirmed; pinned source and Deepmath leaf outline inspected

## Size and scope

Small: rewrite two existing slides and their notes, plus a necessary wording bridge on the immediately following slide. No structural change, no new literature, one review round. This is new author clarification after the completed preceding review, not a reopened finding. Keep the current five-part argument and the rest of the reviewed deck unchanged.

### C01 — Author clarification, verbatim

> for page 4-5, I meant the following.
> • if you compute average of log 1/q(x) where x is sampled according to x~P, then you are essentially computing E_p[log 1/q(x)] which is E_p[log p(x)/q(x)] - entropy (entropy is fixed and not controllable). This is related to montecarlo

### Interpretation / sign correction

The intended Monte Carlo connection is correct. With the usual definition H(P) = -E_P[log p(X)], the identity is **CE(P,Q) = D(P||Q) + H(P)**, not KL minus entropy. Equivalently, **D(P||Q) = CE(P,Q) - H(P)**. Preserve Albert's point, correct the sign consistently in every layer, and make the sampled average itself the main motivation rather than the one-hot special case.

## P1 — Two-slide log-loss motivation [judgment]

Files allowed:
- `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html` (D): S130, S131; S04 only for the wording bridge below.
- `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html` (H) and `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md` (M): matching articles/sections for those IDs.
- `courses/deepmath/OUTLINE.md`: correct the opening description and any shifted line pointers in this same change. Root/folder pointers only if actually made stale.
- This job's tracked record. No figures/generators, earlier lectures, global design documents or shared reference/scripts need edits.

### 1. S130 / current p4, “One-Hot Cross-Entropy Equals KL” → expected log loss and KL

**Point (must):** Expected negative log likelihood is forward KL plus the data entropy; the entropy is fixed when changing the model.

**Suggested title (prefer):** “Log Loss Targets Forward KL”. Title wording/layout are slides' call.

**Main content (must):**
- Define the two roles in plain language: P is the fixed data distribution; Q_theta, with mass function q_theta, is the model we can change. Use a discrete outcome X for the ordinary entropy notation H(P); no conditional-classifier machinery is needed.
- Show the identity L(theta) = E_{X~P}[log(1/q_theta(X))] = D(P||Q_theta) + H(P), with finite terms. Identify this expectation as cross-entropy.
- Say explicitly: H(P) does not depend on theta; minimizing expected log loss therefore minimizes D(P||Q_theta). This is equivalence of population objectives, not a claim that a finite-data optimizer recovers P.
- Keep the correct direction P first / Q second, and state the finite-loss scope compactly (positive q_theta on P's support; finite entropy and expected loss). Do not display “CE = KL” without its constant.

**Exhibit (slides decides):** A labelled equation decomposition separating the model-dependent KL from the fixed entropy. No new numerical toy or decorative illustration is necessary.

**Notes (must):** Message states the fixed-P distinction. Explain that P may only be available through data samples, while q_theta(x) is evaluable. Give the short algebra: log(1/q_theta) = log(p/q_theta) - log p; then take E_P and use H(P) = -E_P log p. Break the derivation into readable steps at narrow width. Name p(x)=P(X=x), natural-log units, support and finite-term conditions. The one-hot and conditional identities may remain briefly as optional secondary context, but cannot lead the Message/explanation or become a new main slide.

**Acceptance:** A lecturer reading only this slide/Message sees what is fixed, what changes, the correct entropy sign, and why log-loss minimization matters.

### 2. S131 / current p5, “Population Loss Requires an Average” → the empirical average is Monte Carlo

**Point (must):** Averaging log(1/q_theta(X_i)) over data X_i~P is a Monte Carlo estimate of the expectation above, hence of KL plus the same fixed entropy.

**Suggested title (prefer):** “Empirical Log Loss Is Monte Carlo”.

**Main content (must):**
- Display the actual integrand, not merely an unnamed generic loss: f_theta(x)=log(1/q_theta(x))=-log q_theta(x).
- Name IID draws X_1,...,X_n from **P**, not Q_theta.
- Make the sample-to-expectation link explicit: L_hat_n(theta) = (1/n) sum_i log(1/q_theta(X_i)) approximates E_P[log(1/q_theta(X))] = H(P)+D(P||Q_theta).
- The direct takeaway is “Average data log loss: Monte Carlo for KL plus a fixed constant” (equivalent concise wording is fine). We need samples from P and values q_theta(X_i), not pointwise p(X_i) or the entropy value, to compute this average.
- Use the clean fixed-model, finite-mean setup for any unbiasedness/convergence claim. Do not suggest the estimator is itself an optimization algorithm. Also do not lead with “no training step here” or a classifier-only framing: the main teaching purpose is the connection between the common learning objective and an MC approximation.

**Exhibit (slides decides):** A compact sample → log-loss values → average → target flow, or an equation-led sequence. The visible terms must be the actual log loss and P-sampling law. Reuse the general MC recipe on p7; do not add another generic recipe page here.

**Notes (must):** Message leads with the sample-average/expectation connection. Map X, P, f_theta and mu=L(theta) to the coming MC notation. For fixed theta and IID data with integrable loss, the mean is unbiased and converges to L(theta). Explain separately that optimizing the empirical loss is the usual sample-based surrogate for the population objective; its population quality/generalization is a separate question, and reusing fitting data does not automatically give an unbiased risk estimate of the fitted model. No gradient chapter, minibatch derivation or optimization tutorial. Retain any useful sampling-versus-minibatch caveat as subordinate detail, not the opening argument.

**Acceptance:** The main slide itself answers Albert's clarification, with the average, expectation and fixed entropy all visible. It does not reduce the connection to a one-hot identity.

### 3. S04 / current p6, “Sampled Replies Estimate Pass Rate” — wording bridge only

Current D line “Samples come from the model p, not from labelled data” → “Here, sample model replies; previously, sample data from P” or equivalent concise wording. In H/M replace the preceding-example description “labelled pairs/classifier” with the new unconditional data-log-loss setup. Keep the generator example, indicator, sampling assumptions and teaching point unchanged. Clarify in the explanation that the sampler p on this separate example is the model's output distribution; it is not the fixed data P of pp4-5. Do not globally rename p/q in the deck. The later q used for an importance proposal is a different local role; clarify that in the opening notes if useful, not via a new slide.

## Existing sources (reuse; no research pass)

- **CE/KL identity and model-independent constant:** `courses/deepmath/prob02-kl-crossentropy/prob02-kl-crossentropy-note.html`, §4.5 Theorem3 and the §4.6 summary, at the frozen baseline. Recalled content, not a new proof chapter. Also Goodfellow, Bengio & Courville, *Deep Learning* (2016), §3.13 eq.(3.51), https://www.deeplearningbook.org/contents/prob.html — already checked and recorded in `log/2026-11-18-prob09-clarity-trim/evidence.md` E02. The algebra above is the direct identity, not a numerical result.
- **IID sample-mean expectation and convergence:** Owen, *Monte Carlo theory, methods and examples*, Ch.2 §§2.1–2.2, https://artowen.su.domains/mc/Ch-intro.pdf — previously checked in the same record E03 and the prior full review. Course prob05 provides the established LLN/sample-mean foundation. Reuse without reteaching its proof.
- **Fixed-model versus fitted-data scope:** preceding job evidence E02; maintain the distinction already in the approved notes. The current clarification changes the example's emphasis, not that caveat's truth.

## Shared surfaces and checks

- Keep stable IDs S130/S131/S04. Target remains two rewritten pages plus the bridge; do not add slides or revisit pacing unless genuinely necessary for legibility. Slide counts/layouts are not hard constraints.
- Update the leaf outline's “one-hot CE = KL; population loss” descriptions to expected log loss = KL + fixed entropy, followed by its MC sample average. Update shifted line pointers, not just the prose.
- D/H/M stay aligned by title, page, ID and content; M stays ASCII. H keeps Message → explanation → details/sources. The old conditional setup must not survive as the primary account in a companion.
- Follow DS §§1,5,6,9,10. Do not shrink type. Keep the explicit answer on the slides, not just notes. No new tech supplement.
- Check D/H/M lints, ID/order parity and outline pointers. Render pp3-7 (changed slides and immediate neighbours); check the three H articles at ~430px and desktop. In work-r1 report mapping, sources/scope issues, deviations and exact pushed SHA.
- One review round. If a blocking issue remains at the small-job limit, escalate rather than silently adding rounds. After approval, final record-only push precedes the owner's update to existing PR77. Never merge without Albert's direct instruction.
