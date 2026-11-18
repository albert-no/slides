# plan-v1 — Simpler oracle, direct tail answer, softmax normalizer

## Summary and scope

Baseline `b96c6060c05de3b28c20a918bb388d7b2e6b68a1`,70 slides, existing PR77 branch `2026-11-17-prob09-major-revision`. Medium job; maximum2 review rounds. Audience remains junior-undergraduate AI majors in the rigorous, example-led mode. No duration target, pacing filler or fixed slide-count requirement.

Keep the argument and approved opening/RL sections. Rebuild the crowded oracle page around circular dependence, replace the tail-necessity-only page with a direct “heavier is not always better” comparison, and replace the Bayesian running example with a three-outcome softmax used again for the normalized sample ratio. Consequential references change with the example.

All content changes below are **[judgment]**. Titles and component suggestions are preferences; the point, mathematical scope, author coverage and evidence are requirements. slides chooses layout and may split for legibility, retaining child IDs and reporting the map. Do not add explanations merely to maintain length.

## Coverage and baseline map

| Comment | Baseline page / title | Stable IDs | Package |
|---|---|---|---|
| C01 |40 / The Oracle Needs a Normalizer | S64 | P1 |
| C02 |45 / Heavier Tails Are Not a Requirement | S69b; context S69a/p44 unchanged | P2 |
| C03 |47 / Bayes Leaves a Normalizing Integral | S132 | P3 |
| C03 consequences |48 / The Target Is Known Up to Z;51 / Likelihood Weights Remove the Unknown Z;52 / Two Averages Form One Ratio | S73, S133, S76 | P3 |
| C03 shared references |46 divider notes;69 recap prerequisite notes; active outline | S72 H/M, S109a H/M | Integration |

### Allowed files

- D: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`.
- H/M: `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html` and `...-note.md`, only the specified ID sections plus mechanically required renumbering.
- Local `gen/p9b_calc.py`, `gen/p9b_figs.py` and their relevant new tail figure; local `gen/p9f_unknown_z.py` or a replacement softmax checker/figure if needed. No global scripts/reference/styles.
- `courses/deepmath/OUTLINE.md` and genuinely stale parent/root pointers. This job record.
- No earlier lectures, pp4-5 log-loss revision, RL section or unrelated prose restyling. Broad cleanup is not part of the order.

## P1 — S64 / baseline p40 [must]

**Point:** The oracle contribution already contains the unknown answer; sampling from the oracle does not automatically provide its normalized weights.

**Preferred title:** “Oracle Weights Need the Answer”.

**Main content:**
- Use the adjacent nonnegative-integrand setting, f>=0 and0<mu=E_p f<infinity. Do not introduce another c on this page.
- Replace the four long boxes and explanatory paragraph stack with ONE short dependency/circularity exhibit: the unknown mu is required in q*=fp/mu, and the resulting weighted contribution Y=fp/q* equals mu. The output cannot discover an answer that its normalized input already requires.
- Distinguish sampling from q* from evaluating the normalized contribution/weight in one short plain-language line. The main is an explanation of the limitation, not another derivation of the zero-variance result.
- Keep a short honest exception: in the earlier exponential-tail toy mu=e^-10 is explicitly computable. The general limitation is not that e^-10 is unavailable.
- **Do not write p/q*=mu in the generic case.** The quantity equal to mu is Y=f*p/q*; p/q*=mu/f on positive f. The bare-weight equality holds only in the tail-indicator example.

**Exhibit (prefer):** a sparse three-step dependency or loop; no fourth box repeating the target and no paragraph inside a box. Layout is slides' choice, with no type reduction.

**H/M:** Message gives the circularity first. Explain each symbol/step and the sampling-versus-evaluation distinction. Preserve the old explicit tail sampler X=10+Exp(1), known normalizer and general hard-case explanation in Details; remove redundant main prose, not the underlying distinction. General signed-f normalizer detail, if mentioned, stays subordinate and correctly uses E_p|f|.

**Evidence:** E02. **Acceptance:** one readable argument, with no overloaded four-box row; the conclusion and toy exception are clear at final size.

## P2 — S69b / baseline p45 [must]

**Point:** Heavier proposal tails can help, but making them still heavier can worsen estimator variance. Tail order alone does not choose a good proposal.

**Preferred title:** “More Tail Mass Can Hurt”.

**Main content:**
- Answer C02 explicitly: **No, heavier is not always better.** Keep the same target and integrand as p44: p=Exp(1), f(x)=x, mu=1.
- Show the exact like-for-like comparison: q=Exp(.5) has per-draw Var_q(fw)=5/27≈0.185; the heavier q=Exp(.1) has Var_q(fw)=13141/6859≈1.916. Moving to the heavier tail worsens this variance. No simulation is needed.
- Name the measured quantity and reading rule: **variance of the weighted contribution fw, lower is better**. It is not variance of q or of the bare weight w. Labels must state which proposal is heavier.
- Preserve the prior conclusion explicitly: heavier tails are not required either; the useful criterion is the f-dependent second moment, not “heavier” by itself. This can be a short qualifier, not another derivation on the main slide.

**Exhibit (prefer):** two labelled bars/values for the moderate and very-heavy proposals. One comparison, not a large family plot or a table plus two formula blocks. An ordinary-MC baseline of1 is optional; it is already established on p44, so do not crowd this page to repeat it.

**H/M:** Message answers the “better?” question. Explain that excessive mass far out spreads the proposal away from the important contribution region. Keep the exact exponential-family second-moment formula and the complete lighter-tail counterexample q=Exp(1.5), Var=29/3<infinity, including its decaying-integrand calculation, as Details in BOTH companions. Retain separate support/integrability and finite-variance conditions. Do not claim a general optimal tail order or that .5 is the global optimum over all proposals.

**Evidence:** E03. **Acceptance:** after p44's successful heavier proposal, p45 directly prevents “the heavier the better”; both counterexamples (not necessary, not monotonic improvement) remain teachable.

## P3 — Replace the Bayesian example coherently [must]

### S132 / baseline p47 — Softmax exposes a normalizer

**Point:** A softmax probability needs one exponential score divided by the sum of all exponential scores.

**Preferred title:** “Softmax Needs a Global Sum”.

**Main content:**
- Introduce only the familiar score/softmax roles: logits z_k, positive unnormalized masses a_k=exp(z_k), p(k)=a_k/Z, and Z=sum_j a_j. No prior, likelihood, posterior or logistic-normal integral.
- Use the tiny exact toy from E05 to make this concrete: labels A,B,C; unnormalized masses1,2,4; normalizer7; normalized probabilities1/7,2/7,4/7. Logits0,ln2,ln4 can be shown as a preceding step if it fits or explained in the notes; do not require readers to infer which values are logits versus masses.
- One simple score → exponential weight → normalization exhibit is enough. Use the same symbols in prose and exhibit.
- **Scope must remain visible:** Z is easy for these three outcomes. With many outcomes, computing it directly requires the full sum; this example motivates the case where that sum is left uncomputed. Do not pretend the toy's7 is unknowable, or that ordinary softmax inherently has an intractable normalizer.

**H/M:** Message explains numerator versus global denominator. Walk through the toy explicitly. Say that the large-outcome scenario assumes all-outcome scoring/summing is expensive while a sampled score is evaluable; if all logits are already available, normalization is straightforward. Distinguish this pedagogical example from a claim about a production softmax implementation. State finite K/finite logits, hence0<Z<infinity. Cite the definition separately from our chosen numbers.

**Evidence:** E04/E05. **Acceptance:** fewer concepts than the old Bayesian page; denominator Z is immediately recognizable, and the easy-toy/large-uncomputed distinction is honest.

### S73 / baseline p48 — Conditional uncomputed-Z bridge

**Point:** If the global sum has not been computed, unnormalized masses remain available but normalized p and p/q do not follow from one sampled score.

- Keep the existing capability diagram and general p=tilde p/Z structure, but adapt its Z expression to the discrete example: Z=sum_k tilde p(k). Use “If Z is not computed” rather than implying the preceding toy's7 is intrinsically unknown.
- Replace the Bayesian toy footer with tilde p(k)=exp(z_k), Z=sum_j exp(z_j). Keep positive-finite-Z and normalized-weight distinctions.
- H/M explain that the small toy offers an exact check while the algorithm being illustrated does not require the full sum. Briefly name the continuous counterpart as an integral; do not preserve the old posterior as an active running example.

**Evidence:** E04–E06. **Acceptance:** no contradiction between the explicitly normalized toy on p47 and the conditional capability statement here.

### S133 / baseline p51 — Reuse the same softmax in a sample ratio

**Point:** Uniform-proposal sampled weights can estimate a softmax probability without using Z; cancellation does not eliminate sampling error.

**Preferred title:** “Normalize the Sampled Softmax Weights”.

**Main content:**
- Keep the same A/B/C masses1/2/4. Target mu=p(C). Draw IID from q=Uniform{A,B,C}; these are proposal draws, not softmax draws.
- Use one clearly illustrative possible batch A,C,C. The unnormalized masses at the sampled outcomes are1,4,4; repetitions count. With uniform q, tilde w=3a and the common3 cancels, so the ratio can use weights proportional to1,4,4.
- The C contributions total4+4=8; all sampled weights total1+4+4=9; the estimate is8/9. Make the selection of numerator and denominator visually obvious. Never label a as exactly tilde p/q unless the factor3/proportionality is accounted for.
- The conclusion is **“Z cancels; sampling error remains.”** Keep “not exact at finite n” or equivalent. The true4/7 may be a compact comparison if space allows; otherwise retain it in H/M validation. No new general formula stack is needed because S75 already states SNIS.

**H/M:** Give f(k)=1{k=C}, q(k)=1/3, tilde w(k)=3exp(z_k), and the full ratio cancellation. Show the concrete arithmetic and exact4/7 check. Label A,C,C as an illustrative batch, not a simulated performance result. Explain why denominator>0 always in this toy, why the uniform-proposal factor cancels, and why a nonuniform proposal would need its own1/q correction. Preserve consistency rather than finite-n unbiasedness/exactness. The toy illustrates the mechanics; it is not evidence that uniform sampling is an efficient large-softmax algorithm.

**Evidence:** E05/E06. **Acceptance:** the example uses only the small categorical model already introduced; no posterior-predictive concepts return. The estimator uses no Z and still visibly has finite-sample error.

### S76 / baseline p52 — Match the discrete notation, no new argument

- Keep the two-averages/one-ratio exhibit, unbiased individual averages and generally biased ratio exactly as concepts.
- For this discrete running example, replace mean labels integral(tilde p*f) and integral(tilde p) by sum_k tilde p(k)f(k)=Z*mu and sum_k tilde p(k)=Z. H/M mention that continuous outcomes replace sums with integrals.
- Do not change the dependence warning or the S77 convergence theorem.

**Evidence:** E06. **Acceptance:** students do not need an unexplained change from categorical sums to continuous integrals immediately after the softmax example.

## Integration / shared surfaces

1. **S72/p46 H/M:** replace the description of the opening Bayesian model with the softmax global-sum setup and its small-versus-large qualification. Main divider can remain unchanged.
2. **S109a/p69 H/M:** replace the stale prob08 “standard normal prior in the Bayesian unknown-Z example” prerequisite with the existing normal contribution-profile example (S57), or omit that obsolete prerequisite clause. No main recap redesign.
3. **S74/S75/S77 and immediate neighbours:** preserve the general statements; adjust only a reference if the replacement makes it stale. These ratios and the LLN proof apply unchanged to discrete masses.
4. Retire the old Bayesian example's active H/M derivations/plot references, not merely its main introduction. It is replaced at Albert's request, not moved into a second competing default example. Historical job records/evidence are untouched. An unused local Bayes figure/generator may be left, repurposed or removed only after checking no active consumer; report the choice. No broad asset cleanup.
5. Update active OUTLINE descriptions, generator/figure references, labels and any shifted line pointers. Retire old “Bayes/likelihood weights” labels and the old seed description if its generator is repurposed for deterministic arithmetic. Keep70 as the current count, not a budget; update all count/range locations if a legibility split changes it.
6. D/H/M share IDs, titles, order and content; M is ASCII. H follows Message → explanation → details/sources, with a concise point first. Disambiguate this job's evidence labels from the earlier same-date register.
7. No new technical supplement. No fixed duration or pacing promise. Do not reopen approved pp4–5 or add gradient material.

## Packages / dependencies

- **P1:** S64 D/H/M only, no generator. Reads adjacent S63a/b; does not change their claims.
- **P2:** S69b D/H/M and relevant local p9b calculation/figure source. Reads unchanged S69a/p44. Preserve its facts and existing assets when rerunning generators.
- **P3:** S132/S73/S133/S76 D/H/M plus a local deterministic softmax check/figure if needed. All use the same E05 toy; not separate examples.
- **Integration:** S72/S109a note references, mechanical titles/pages, outline and record. P3 lands before these consistency updates.

## Acceptance / reporting

- Review all C01–C03 against the exact pushed candidate; use the baseline page/ID map above and report all moved/split pages.
- Every conceptual question is directly answered on the relevant main slide. No answer hidden only in notes.
- Lint D/H/M, ID/order parity, ASCII M, outline validity plus actual pointer spot checks. Check both notes retain moved lighter-tail/oracle details.
- Recompute the exact tail variances and softmax/sample-ratio arithmetic; record code paths/parameters. If a generator is changed, rerun it and confirm unrelated figures do not silently change.
- Render changed pages and neighbours (baseline pp39–41,44–53; plus any resulting split) and check the rewritten note articles at desktop and ~430px. No font shrinking, clipped formulas, cramped flow rows or ambiguous plot keys. Check new labels and mathematical qualifiers in final-size renders, not only lint.
- `work-r1.md` reports coverage, mapping, deviations, checks, sources/issues and exact pushed SHA. Argument/scope problems return to owner; layout and legibility choices are slides' call.
