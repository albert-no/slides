# work-r1 — job 2026-11-18-prob09-oracle-tails-softmax

Integrated report for `plan-v1.md` (C01–C03).

## Branch and commits

- Branch `2026-11-17-prob09-major-revision` (PR #77 continuation), from baseline b96c606. Slide IDs already present; no ID commit. Slide count unchanged: 70 (D/H/M), no splits, no reordering.
- Head: the commit that carries this report (SHA given in the handoff pointer).
- All three packages done inline by the integrator; no subagents.

## P1 — S64, p40, "Oracle Weights Need the Answer" (C01)

- D: setting line f ≥ 0, 0 < μ = E_p f < ∞. Three-box flow: [μ: the unknown answer] → [q* = fp/μ: building it needs μ] → [Y = fp/q* = μ: each draw returns μ], with loopback "Circular: the output is the number the input already needed". Line: "Sampling from q* is not evaluating Y = fp/q*: that needs μ". Muted: tail toy exception (μ = e^{-10} computable, so both are easy there). Cite Owen Ch. 9 §9.1 pp. 4–6.
- H/M: Message leads with the circularity; three steps explained; sampling versus evaluation; toy exception (X = 10+Exp(1) samples q*, μ = e^{-10} known). Details: contribution Y versus bare weight p/q* = μ/f (equal to μ only where f = 1, the tail indicator); signed f → |f|p/c with c = E_p|f|; obstacle is evaluating, not a universal impossibility of sampling; practical proposals resemble |f|p with a known normalizer. Sources: oracle-tails-softmax E02 + E04 (Owen).

## P2 — S69b, p45, "More Tail Mass Can Hurt" (C02)

- D: lead "Is a heavier tail always better? No." Same f(x) = x, p = Exp(1), μ = 1. New figure `fig/p9b-heavy.svg`: horizontal bars Var_q(fw) for q = Exp(1/2) (green, 5/27 ≈ 0.185) and heavier q = Exp(1/10) (red, 13141/6859 ≈ 1.916), linear axis 0–2.1, dashed line at 1 labelled "ordinary MC". Key: "Bars: Var_q(fw) …; lower is better". Highlight: "Heavier tails are not required either: judge the f-dependent ∫f²p²/q".
- H/M: Message is the direct "No" with both values. Explanation: smaller λ = heavier tail, P_q(X>t) = e^{-λt}; what the bars measure; Exp(1/10) worse than ordinary MC; profile x e^{-x} peaks at x = 1, so far mass starves the important region. Details kept in full: 2/[λ(2−λ)^3] for 0 < λ < 2, ∞ for λ ≥ 2; values for λ = 1/10, 1/2, 1, 3/2, 2; full Exp(1.5) counterexample (f²p²/q = (2/3)x²e^{-x/2}, second moment 32/3, Var 29/3); validity versus finite variance; neither value optimal (oracle of 39 has variance 0). Sources: oracle-tails-softmax E03; evidence 2026-11-18 E06; `gen/p9b_calc.py`; `gen/p9b_figs.py` → `fig/p9b-heavy.svg`.
- Code: `gen/p9b_figs.py` gains `fig_heavy()`; all other `p9b-*.svg` regenerate byte-identical (sha1 checked). `gen/p9b_calc.py` prints the S69b comparison (0.1852 → 1.9159).

## P3 — softmax replaces the Bayesian example (C03)

- **S132, p47, "Softmax Needs a Global Sum".** D: z_k → a_k = e^{z_k} > 0 → p(k) = a_k/Z, Z = Σ_j a_j. Table A/B/C: logits 0, ln 2, ln 4; masses 1, 2, 4 (sum Z = 7, red); p(k) 1/7, 2/7, 4/7 (sum 1). Stacked bar 1/2/4 with C highlighted; caption "p(C) = one segment over the whole bar, 4/7". Highlight: easy here; with very many outcomes Z needs every score, and that sum is what we skip. H/M: numerator versus global denominator; table and bar described; large-K scenario stated as a teaching assumption (expensive full scoring, cheap sampled score; easy if all logits are available; no claim about production softmax); finite K and logits give 0 < Z < ∞. Sources: definition E04 (Goodfellow et al. §6.2.2.3 eq. (6.29)) kept separate from toy E05 (`gen/p9f_unknown_z.py`). Stan/E07 citations removed.
- **S73, p48.** Notation x → k: p(k) = p̃(k)/Z, "If Z is not computed: still not zero, not infinite"; diagram labels p̃(k) "evaluable at any k", Z = Σ_k p̃(k) "not computed, but 0<Z<∞" (aria-label updated); footer "Softmax: p̃(k) = e^{z_k} and Z = Σ_j e^{z_j}". H/M: toy Z = 7 is a validation check the method does not use; continuous counterpart Z = ∫p̃ with Bayes as one standard example in Details; Bayes/φ/s toy removed.
- **S133, p51, "Normalize the Sampled Softmax Weights".** D: target μ = p(C); X_i IID ~ q = Uniform{A,B,C}, so w̃_i = 3a_{X_i}; batch boxes A (mass 1), C (4), C (4), C draws blue; caption "One illustrative batch; C draws (blue) feed the numerator"; μ̂_SN = 3(4+4)/3(1+4+4) = 8/9 ≈ 0.89 with the 3s cancelled, versus μ = 4/7 ≈ 0.57; highlight "Z cancels; sampling error remains: consistent, not exact at finite n". H/M: f = 1{k=C}, q = 1/3, cancellation; batch illustrative, not simulated (ordered-batch probability 1/27); denominator always > 0 (toy property); nonuniform q keeps its own 1/q(X_i); consistent, biased at fixed n (53, 54); not evidence that uniform sampling is efficient. Simpson/seed numbers removed. Sources: Owen E05; oracle-tails-softmax E05/E06; `gen/p9f_unknown_z.py`.
- **S76, p52.** D mean labels Σ_k p̃(k) f(k) = Zμ and Σ_k p̃(k) = Z; line "Each average is unbiased for its own sum". H/M: sums, toy check (4 = 7 · 4/7, 7), integrals for continuous outcomes; M Slide description updated.
- **S72 (p46 divider) H/M:** Bayesian preview replaced by the softmax global-sum preview with the small-versus-large qualifier.
- **S109a H/M prerequisite:** prob08 now "the standard normal, used in the normal contribution profile of 34" (S57 uses p = N(0,1)); the Bayesian-prior wording is gone.
- **Code:** `gen/p9f_unknown_z.py` rewritten as a deterministic softmax checker (no randomness, no seed): a = 1, 2, 4; Z = 7; p = 1/7, 2/7, 4/7; Σaf = 4 = Zμ; w̃ = 3a; E_q w̃ = 7; E_q[w̃f] = 4; batch A,C,C → 24/27 = 8/9, error 20/63, P_q(ordered batch) = 1/27.

## Integration

- `courses/deepmath/OUTLINE.md` prob09 leaf: Part 03 row (oracle needs μ; more tail mass can hurt), Part 04 row (softmax global sum; sampled softmax weights, 8/9 vs 4/7), generators line (p9f_unknown_z.py deterministic checker; p9b-heavy.svg added; p9f-bayes.svg removed), source-label legend gains "oracle-tails-softmax E##". Line pointers updated (117/177/520/796/1026/1364/1573; theorems 609, 837), each checked with `sed -n`. Count stays 70. No root/folder change needed.
- Remaining "Bayes" mentions are general (S73 Details continuous counterpart; S78 capability-map Details), not the removed toy.

## Slide mapping

| ID | page | status |
|---|---|---|
| S64 | 40 | rewritten (D/H/M) |
| S69b | 45 | rewritten, new figure (D/H/M) |
| S72 | 46 | H/M preview only |
| S132 | 47 | rewritten (D/H/M) |
| S73 | 48 | notation and footer (D/H/M) |
| S133 | 51 | rewritten (D/H/M) |
| S76 | 52 | sums (D/H/M) |
| S109a | 69 | H/M prerequisite line |

## Deviations

- S69b includes the optional ordinary-MC dashed line at 1.
- S133 shows the true μ = 4/7 on the slide next to 8/9, so the sampling-error point is visible without the note.
- `fig/p9f-bayes.svg` deleted: its only consumers were the old S132, its note sources and OUTLINE. `gen/p9f_unknown_z.py` repurposed in place (plan allowed a replacement checker).
- S74 (p49) keeps general x notation (p̃(x), q(x)); only S73/S76 moved to the discrete k/sum notation that the softmax toy needs. Not changed, since S74 was outside the allowed sections; flag if you want it aligned.

## Plan issues

None.

## Unsourced facts

None. Softmax definition: oracle-tails-softmax E04. Toy numbers and batch: ours, E05, reproduced by `gen/p9f_unknown_z.py`. Tail values: E03, `gen/p9b_calc.py`. Oracle: E02 + Owen E04.

## Checks

- `lint-deck.py`: deck and H note ok. `lint-accessible-md.py`: 23 warnings, the baseline count (one new "the slide" phrase in S69b reworded). M is ASCII.
- ID/order parity D/H/M: 70/70/70, identical order.
- `outline-lint.py`: 0 stale/missing pointers.
- Rendered at `-r 60`: changed pp40, 45, 47, 48, 51, 52 and neighbours pp39, 41, 44, 46, 49, 50, 53. First draft fixes: S132 table text was below body size (grid divs are not `p`; set 1.55rem explicitly, no shrink); S133 muted line hit the brand footer (merged into the highlight); S132 cite shortened to one line. Final renders clean.
- H articles S64, S69b, S72, S132, S73, S133, S76, S109a: rendered with KaTeX at a 382px article width (430px phone) and at desktop width; a DOM probe found no math or code past the article edge.
