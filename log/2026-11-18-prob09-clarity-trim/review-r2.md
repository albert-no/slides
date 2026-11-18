# review-r2 — Approved

- **Reviewed commit:** `fa153e52db9bafabda25b883b60456252221e8f7` (round-2 content and work report in the same commit)
- **Previous reviewed commit:** `6cf17f6ccb63bb3622267bf0993e67e2068867a8`
- **Frozen baseline:** `5f4b1d99c5d799785752aa12c494715c3b21327b`
- **Branch / PR:** `2026-11-17-prob09-major-revision`, existing [PR77](https://github.com/albert-no/slides/pull/77)
- **Verdict: approved.** F01/F02 are fixed in both note editions. Nonblocking F03/F04 are also resolved. No open findings.

## Result

The 70-slide, five-part revision is ready for Albert's next pass. It motivates MC with learning and generation, makes the rare-event and importance-sampling distinctions explicit, adds a concrete Bayesian unknown-normalizer example, removes the gradient chapter, and retains the RL application. No duration target or filler has been reinstated.

This is a changed-material-and-neighbours review following the full round-1 pass. It does not reopen unchanged content or add a new design/pacing request.

## Finding closure

Paths: **D** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`; **H** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`; **M** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`.

| ID | Slide / page | Type | Previously blocking | Verified resolution |
|---|---|---|---|---|
| F01 | S72/p46, S132/p47; H751/756, M833/839 | fact | yes | Both editions name the **unnormalized** posterior as pointwise evaluable. The divider now distinguishes an integral not needed by the estimator from the later validation calculation. This agrees with S73/S133 and evidence E07/E11. Closed. |
| F02 | S63b/p39; H641, M725 | fact | yes | Both Message lines explicitly require nonnegative f and a positive, finite mean. They distinguish zero variance of the contribution average from randomness of X and retain the oracle limitation. Main, Message and detail conditions agree. Closed. |
| F03 | S109a/p69; H1061/1069, M1186 | unmet request | no | “Closing comparison” replaces “first synthesis”; the prob08 prerequisite now points to the standard-normal prior in the Bayesian example, not the removed gradient path. S77's unrelated pathwise proof is untouched. Closed. |
| F04 | S132/p47; D1020 | design rule | no | Two intact citation lines separate the toy/generator provenance from the versioned Stan citation. Exact source sections/links remain in H/M. Render has no bad wrap or overlap; citation type is unchanged. Closed. |

No new findings. No plan changes: these corrections restore or clarify existing requirements; work-r2 reports no plan issues.

## Coverage of Albert's requests

All page numbers below are current. Round-1 accepted coverage is carried forward; the requested note corrections are now complete.

| Comment | Status | Result |
|---|---|---|
| C01 | done | pp4–6, S130/S131/S04: one-hot CE/KL, population loss and generated-output expectation motivate MC without conflating the sampling laws. |
| C02 | done | p12, S114: SE is expanded and defined as estimator standard deviation. |
| C03 | done | Baseline pp13–14, S33/S37, removed with active companion entries. |
| C04 | done | pp15–16, S116a/b: zero-hit error, expected hits and relative RMSE developed explicitly. |
| C05 | done | p28, S118: fw and mu named as weighted contribution and target mean. |
| C06 | done | p34, S57: contribution-profile message and exhibit made primary. |
| C07 | done | pp38–40, S63a/b/S64: random draws versus constant contributions, positive-finite-mean condition and oracle caveat align in deck and notes. |
| C08 | done | pp44–45, S69a/b: heavier tails can help; they are not a universal requirement, demonstrated by a lighter-but-finite case. |
| C09 | done | pp47–51, S132/S73/S133: concrete Bayesian unknown-Z example and likelihood-weighted prediction; quick-read notes now preserve the normalization distinction. |
| C10 | done | p53, S77 and touched prose/math use IID. |
| C11 | done | Gradient-estimation chapter and dependent recap/derivations removed; obsolete prerequisite wording now removed too. |
| C12 | done | pp60–68: RL importance sampling retained as Part05, including mismatch and clipping limits. |
| C13 | done | Shorter 70-slide deck, no fixed pacing or minimum slide count. |

## Verification

- Reviewed the exact named commit through git and an extracted archive. Relative to round1, source edits are confined to D/H/M at the requested locations. No figure, generator, shared style/script or outline changes; no added, removed or reordered slide.
- Read the changed passages in both companion editions and checked their immediate context against the recorded mathematical evidence. Source definitions and numerical validation code are unchanged from the full first pass.
- Independently rendered main pp46–48 after fonts and print layout settled. S132's two citation lines are intact; all three pages are unclipped, with no overlap, scroll overflow or KaTeX errors.
- Checked changed H articles S63b/S72/S132/S109a and neighbours S63a/S64/S69b/S73/S104/S113 at true mobile width430, scale1. No article or math overflow and no KaTeX errors. Visually inspected the four changed articles, including their full details and sources.
- D/H lint passes. M is ASCII with no structural/math-delimiter errors; the pre-existing visual-reference/navigation warnings are unchanged. All three editions contain70 unique IDs in identical order.
- Deepmath outline lint:0 stale/missing pointers and0 warnings. Source line counts did not shift, and the outline is unchanged.
- Tracked requests, evidence, plan-v1, plan-v2 and review-r1 copies match the owner files byte-for-byte. The living header was subsequently updated by the owner for this review, as expected.
- No generator rerun needed this round: all generator/figure bytes are unchanged from the independently reproduced round-1 results.

## Handoff

Copy this frozen review and refresh the living header into `log/2026-11-18-prob09-clarity-trim/`, then push. After this reviewed commit, change only that job-record directory and return the final pushed SHA. The owner will verify that boundary and update **existing PR77**, not create another PR. Approval is pinned to `fa153e52db9bafabda25b883b60456252221e8f7`; Albert remains the final check. No merge is authorized.
