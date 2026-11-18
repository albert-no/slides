# work-r1 — job 2026-11-18-prob09-logloss-motivation

Integrated report for `job.md` (version 1 spec) plus `plan-v2.md` (C02).

## Branch and commits

- Branch `2026-11-17-prob09-major-revision` (PR #77 continuation), from 3635bd8. No new ID commit (IDs from c47b198). Slide count unchanged: 70 (D/H/M).
- Head: the commit that carries this report (SHA given in the handoff pointer).

## Package P1 — what was done

- **S130, p4, "Log Loss Targets Forward KL"** (was "One-Hot Cross-Entropy Equals KL").
  - Point line: "fixed data entropy, so log loss and KL share minimizers" (plan-v2 wording).
  - Role line: P fixed data distribution; Q_theta with pmf q_theta, the model we change.
  - Exhibit: labelled three-box equation: Expected log loss L(theta) = E_{X~P}[log 1/q_theta(X)] ("the cross-entropy") = Forward KL D(P||Q_theta) ("changes with theta") + Data entropy H(P) ("fixed: no theta"). Entropy is added (sign corrected per job.md).
  - Highlight: minimizing log loss minimizes D(P||Q_theta), with no p(x) needed.
  - Scope line: population objectives; finite terms (q_theta > 0 where p > 0, H(P) finite).
- **S131, p5, "Fit the Model Without Evaluating P"** (was "Population Loss Requires an Average"; plan-v2 suggested "Fit Q Without Evaluating P").
  - Exhibit: Available (data X_i IID ~ P; model values q_theta(X_i); in red "not needed: p(X_i)") → Average log loss L_hat_n(theta) = (1/n) sum log 1/q_theta(X_i) → (≈) Target L(theta) = E_P[log 1/q_theta(X)] = D(P||Q_theta) + H(P).
  - Highlight: "Sample P; evaluate Q_theta; minimize KL up to a fixed entropy".
  - Grey line: estimates KL + H(P), not KL alone; fixed theta, finite mean: unbiased for L(theta).
  - No classifier or one-hot framing; no "no training step" lead.
- **S04, p6, bridge only.** D: "Here, sample model replies; previously, sample data from P". H/M: the previous-example description now says data from P with q_theta only evaluated; added that the sampler p here is the model's reply distribution, not the data P of pp4-5. Rest of S04 unchanged.
- **Notes H/M (S130, S131).**
  - Messages lead with fixed P / sampling access and "KL up to a fixed entropy", never absolute KL.
  - S130 Details: notation (p(x)=P(X=x), nats, H(P) = -E_P log p); three-step algebra split for narrow width; support/finite-term conditions; sign note (D = L - H); one-hot and conditional forms kept as "Optional context" only; letter-role note (q_theta model here, p = sampler on p6, q = IS proposal from Part 02).
  - S131 Details: MC notation map (X, P, f_theta, mu = L(theta)) pointing to the p7 recipe; clean unbiasedness/LLN setup; "what can be computed": absolute KL not produced, optional KL-difference identity D(P||Q1) - D(P||Q2) = E_P[log q2/q1] (plan-v2 optional item, included; labelled our calculation); estimating is not optimizing (finite-data fitting, generalization, fitted-data bias); minibatch caveat subordinate.
- **OUTLINE.md (deepmath leaf).** prob09 opening summary and Part 01 row rewritten (log loss = forward KL + fixed entropy; fit without evaluating P). Line pointers shifted +16 updated: Part 02–05 and synthesis rows (509/785/1012/1354/1563) and the two theorem pointers (598, 826). No root/folder change needed.

## Slide mapping

| ID | old page | new page | status |
|---|---|---|---|
| S130 | 4 | 4 | rewritten |
| S131 | 5 | 5 | rewritten |
| S04 | 6 | 6 | one D line; H/M bridge paragraph |

## Deviations

- S131 title "Fit the Model Without Evaluating P" instead of "Fit Q Without Evaluating P": "the model" avoids an unsubscripted Q next to Q_theta on the slide.
- The job.md v1 S131 takeaway ("Average data log loss: Monte Carlo for KL plus a fixed constant") was drafted first and then replaced by the plan-v2 takeaway; the MC link stays explicit in the exhibit (average ≈ expectation) and in the note Message/explanation.
- The integrand f_theta is written inside the average on the slide rather than as its own box (space for the "not needed: p(X_i)" label); f_theta is named and mapped in H/M.

## Plan issues

None.

## Unsourced facts

None. Identity: prob02 note §4.5 Theorem 3 / §4.6, Goodfellow et al. §3.13 eq. (3.51) (evidence 2026-11-18 E01, E02). Sample mean: Owen Ch. 2 §§2.1–2.2 (E03). KL-difference line: same identity applied twice (our calculation).

## Checks

- `lint-deck.py`: deck and H note ok. `lint-accessible-md.py`: 23 warnings, same count as baseline, none new from this change. M is ASCII.
- ID/order parity D/H/M: 70/70/70, identical order.
- `outline-lint.py`: 0 stale/missing; new pointers spot-checked against the file.
- Rendered (`-r 60`): pp3–7. p5 first draft overflowed at the bottom and was compacted (no type change); final pp3–7 clean.
- H articles S130, S131, S04 screenshotted at 430px and 1280px: no horizontal overflow; derivations break across lines at 430px.
