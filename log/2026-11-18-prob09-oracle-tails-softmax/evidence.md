# Evidence and exact checks

Source cutoff:2026-11-18. New labels in companions must name this job (or the unambiguous short label “oracle-tails-softmax”), not just “evidence2026-11-18”, which already denotes the earlier clarity/trim register. Prior evidence remains unchanged.

## E01 — Pinned baseline and prerequisite continuity

- **Repository evidence:** baseline b96c6060c05de3b28c20a918bb388d7b2e6b68a1,70 slides. Target bodies and dependent H/M references inspected; Deepmath leaf outline and DS §§1,5,6,8,9,10 consulted.
- Page40=S64;45=S69b;47=S132. Existing S69a/p44 fixes p=Exp(1), f(x)=x and shows q=Exp(1/2) with per-draw variance5/27 versus ordinary MC variance1.
- S132/S133 currently use a logistic-normal Bayesian posterior; S73, S72 notes, S109a prerequisite notes and the active outline depend on it. These must change together. S74/S75/S77 remain the general weights, ratio and LLN statements; S76's integrals require a discrete-sum bridge when the running example changes.
- The course already knows exponentials/logarithms, probabilities, expectations, sample means and normalization. No new Bayesian prior/likelihood apparatus is needed for softmax. Other prior Gaussian examples remain (e.g. S57's normal contribution profile), so removing the Bayesian example does not remove every prob08 connection.

## E02 — Oracle circularity

- **Published result / explanatory consequence:** Owen, *Monte Carlo theory, methods and examples*, Ch.9 §9.1, optimal-density discussion pp4–6; https://artowen.su.domains/mc/Ch-var-is.pdf . Reuse previously inspected source and prior clarity/trim E04/E05; not a claim of a fresh PDF fetch.
- For f>=0 with0<mu=E_p f<infinity, q*=fp/mu makes Y=f(X)p(X)/q*(X)=mu almost surely under q*. Evaluating this normalized oracle contribution needs mu. Sampling from a distribution and evaluating its normalized probability/weight are different capabilities; access to the former alone does not solve the latter.
- **Important:** the generic contribution Y equals mu; the bare weight p/q*=mu/f is NOT generally mu. It equals mu in the tail-indicator case on x>10 because f=1 there.
- In the earlier tail toy, p=Exp(1), f=1{x>10}, mu=e^-10 and q*=10+Exp(1). The normalizer actually is computable in this toy; do not describe it as intrinsically unavailable. The general oracle limitation concerns problems where mu is not available.

## E03 — More tail mass can worsen variance

- **Our exact calculation, existing theorem:** for p=Exp(1), f(x)=x, mu=1, q_lambda=Exp(lambda), lambda>0, E_q[(fw)^2]=2/[lambda(2-lambda)^3] for0<lambda<2 and infinity forlambda>=2. Variance subtracts1. Established in prior clarity/trim E06 and reproducible in `courses/deepmath/prob09-monte-carlo/gen/p9b_calc.py`.
- Independent exact-rational check today: lambda=1/2 gives Var=5/27=0.1851851852; lambda=1/10 gives Var=13141/6859=1.9158769500; lambda=1 gives1; lambda=3/2 gives29/3=9.666666667, finite.
- Smaller lambda has a heavier exponential tail: Pr_q(X>t)=exp(-lambda*t) for t>0. Thus making q heavier from Exp(.5) to Exp(.1) makes this estimator's variance WORSE, despite both tails being heavier than p. Excess mass far out can leave too little proposal density where this integrand contributes most.
- The lighter q=Exp(1.5) remains a finite-variance counterexample to necessity; its proof and exact value should remain in both notes when moved off the main slide.
- **Not established:** that heavy tails are always bad, that lambda=.5 is the global optimal proposal over all densities, or that variance of the bare weight is the performance metric. Compare Var_q(fw) for the SAME p and f. A finite second moment and full needed support are separate conditions.
- Main comparison planned: two labelled values .185 and1.916, lower is better. Reuse/extend `gen/p9b_figs.py` with a dedicated too-heavy comparison figure if a generated exhibit is chosen; exact inputs above, no random seed/simulation.

## E04 — Softmax normalizer

- **Published definition:** Goodfellow, Bengio & Courville, *Deep Learning* (2016), Ch.6 §6.2.2.3 “Softmax Units for Multinoulli Output Distributions”, eq.(6.29), https://www.deeplearningbook.org/contents/mlp.html . Inspected via web2026-11-18; definition explicitly exp(z_i)/sum_j exp(z_j).
- For K finite outcomes and finite logits z_k, define unnormalized masses a_k=exp(z_k)>0, Z=sum_{j=1}^K a_j, and p(k)=a_k/Z. Z is positive and finite. One a_k is pointwise evaluable; a direct exact Z evaluation sums across ALL K outcomes.
- **Our computational-scope explanation, not a benchmark claim:** if scoring all outcomes is expensive at large K, the full sum may be left uncomputed while sampled outcomes can be scored. Ordinary small softmax is readily normalized, and if all logits are already available the sum is straightforward. Do not call softmax inherently intractable or claim production softmax normally uses the estimator here.

## E05 — Three-outcome softmax and a sample-ratio illustration

- **Our toy / exact arithmetic, not a published experiment:** labels A,B,C; logits0,ln2,ln4; unnormalized masses1,2,4; Z=7; p=(1/7,2/7,4/7). Target mu=p(C)=E_p[1{X=C}]=4/7. The small known Z is an explicit sanity check, not a computational challenge.
- IID proposal q=Uniform{A,B,C}, q(k)=1/3. Unnormalized IS weights tilde w(k)=a_k/q(k)=3a_k. The shared3 cancels in the SNIS ratio, so mu_hat = sum_i a_{X_i}1{X_i=C}/sum_i a_{X_i}. It never reads Z.
- **Illustrative possible batch, not a random simulation:** X=(A,C,C); a values=(1,4,4); actual tilde weights=(3,12,12); numerator of the scaled-weight ratio8, denominator9, estimate8/9. Distinct from exact4/7; repetitions count separately. Its ordered-batch probability under q is1/27, if needed in notes only.
- All proposal masses and weights positive, f bounded, so the ratio exists for every n>=1 and is consistent; do not claim finite-n unbiasedness/exactness. For general nonuniform q, the1/q factor does NOT disappear.
- Arithmetic rechecked independently with exact fractions. Reproducibility: slides may repurpose `gen/p9f_unknown_z.py` for this deterministic example or add a small local softmax checker and report its exact path. No simulated performance plot or new sampler is needed.

## E06 — Discrete sums versus continuous integrals

- **Standard identity / course convention:** importance-sampling and self-normalized-ratio statements apply to masses as well as densities. For the discrete softmax example, Z=sum_k tilde p(k), E_q[tilde w]=Z and E_q[tilde w f]=Z*mu. The continuous counterpart uses integrals. The normalized-weight and LLN arguments are unchanged.
- Reuse prior SNIS evidence and the chapter's existing derivation; this is a notation adaptation, not a new theorem. Make the sums explicit on S73/S76 where the new discrete example would otherwise meet an unexplained integral. Leave generic pointwise ratios and the LLN statement intact.
