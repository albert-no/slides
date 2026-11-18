# review-r1 — Oracle, tails, softmax

- Reviewed commit: `74ee8118731e4758c51366f11c0951b586e482a5`.
- Baseline: `b96c6060c05de3b28c20a918bb388d7b2e6b68a1`.
- Verdict: **revise**. Two blocking design findings below; no mathematical correction to the examples is needed.
- Round: 1 of 2. Next review is limited to the fixes and their neighbours.

## What matters

The oracle explanation now has a readable three-step argument, and the tail slide directly answers Albert's question with the correct like-for-like variance comparison. Keep those. The softmax replacement is much easier conceptually and its notes correctly distinguish the easy toy from the conditional large-sum problem. Finish by removing duplicated visual/formula material on pages 47 and 51; neither needs additional theory.

## Request coverage

| Comment | ID / current page | Result |
|---|---|---|
| C01 | S64 / 40 | Done: circular dependence, sampling versus evaluation, and the computable tail exception are explicit. |
| C02 | S69b / 45 | Done: direct No; 0.185 versus 1.916 compares Var_q(fw); lighter-tail counterexample retained in both notes. |
| C03 | S132 / 47; S73 / 48; S133 / 51; S76 / 52; companion integration | Content done; design acceptance pending F01/F02. Tiny softmax, proposal batch, cancellation, sampling error and sums are coherent. |

## Findings and self-contained changes

Paths below are repo-relative. Line numbers refer to the reviewed commit. D = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`; H/M are the matching `-note.html` and `-note.md` in that folder.

| ID | Slide / page | Type | Blocking | Problem and fix |
|---|---|---|---|---|
| F01 | S132 / 47 | design rule | yes | D lines 1037–1046: a four-row table (including the outcome header), a second stacked-bar exhibit, its caption, the definition and the highlight exceed the DS §1 table-row/element budget and one-exhibit rule. **[judgment] Keep one normalization exhibit. Preferred minimal fix: remove the repeated stacked bar/caption and move the numerical-logits row to the notes, leaving outcome header + masses + probabilities, the short defining line and the scope highlight.** Keep a=1,2,4, Z=7, p=(1/7,2/7,4/7) and the easy-toy/large-sum qualification visible. An equivalent single exhibit within budget is fine. Update H/M descriptions to match; keep the logarithm values in explanatory notes. Reason: a simpler example should not require reading the same normalization twice. |
| F02 | S133 / 51 | design rule | yes | D lines 1110–1118: the full general SNIS ratio is repeated before the concrete arithmetic, making the vertical stack exceed its layout capacity. In both the live 1280×720 browser and print-layout audit, the slide has scrollHeight 734 versus clientHeight 720 and its divider collapses to zero height; the rendered title underline disappears. **[judgment] Remove the redundant general ratio `sum_i tilde w_i f(X_i) / sum_j tilde w_j` from line 1117 and retain the concrete common-3 cancellation, 8/9 estimate, and 4/7 comparison.** Further shorten/reorganize only as needed to restore normal header/body rhythm and fit the slide, without reducing type or squeezing prose spacing. Keep IID uniform-proposal draws, illustrative A/C/C batch and the finite-sample-error takeaway. H/M retain the full definition with f(k)=1{k=C}; adjust their visual description if needed. Reason: this page should apply the formula already established on page 50, not restate it in an oversized block. |
| F03 | S64 / 40, M only | fact | no | `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md` line 757 says “A return arrow is labelled”, but the render has no return arrow. Change that phrase to “The red line beneath the flow reads”. Reason: the accessible description should describe the actual exhibit. No diagram change is requested. |

F01/F02 are the only reasons for another round. No new plan version is required: these enforce the existing one-exhibit/capacity requirements, and plan-v1 explicitly allowed the logits in notes and did not require a repeated general formula on S133. Generic x notation on unchanged S74 is fine; do not expand this round to align every dummy variable.

## Verification completed

- Read the original C01–C03, evidence E01–E06 and the affected source diffs; checked mathematical conditions and the design rules before assessing plan compliance.
- Exact candidate archived and rendered in Chromium. Inspected all 13 pages 39–41 and 44–53, not just the six changed main slides. No changed-slide KaTeX errors. Page 51 additionally checked in live presentation mode at 1280×720, confirming F02 rather than relying on PDF alone.
- All eight changed HTML-note articles checked at actual 430px mobile viewport (innerWidth 430, scale 1; articles 382px) and 1280px desktop. No horizontal article overflow, out-of-article math/code or KaTeX errors. Representative screenshots inspected; both note editions read for changed content and retained details.
- D/H lint passes. M remains ASCII; accessible-M lint reports the same 23 warnings as the baseline. All 70 IDs and their order agree across D/H/M and remain unchanged from the baseline.
- Target leaf `courses/deepmath/OUTLINE.md` lint: 0 stale/missing pointers, 0 warnings. All seven changed section pointers and both theorem pointers checked against their actual content. Repository-wide outline lint separately finds an unchanged external-workspace path in `courses/trustworthy-ai/OUTLINE.md:332` (`/workspace/agent/lec09/r4/build_deck.py`); this is outside this job, not a new prob09 defect.
- Reran `gen/p9b_calc.py`, `gen/p9b_figs.py`, `gen/p9f_unknown_z.py` in the disposable archive. Tail values match 5/27 and 13141/6859; lighter-tail variance remains 29/3. Softmax probabilities are 1/7,2/7,4/7; actual sample weights 3,12,12 give 24/27=8/9; error 20/63, ordered-batch probability 1/27. No simulation/performance claim is made.
- All 12 p9b figures, including the new comparison, regenerated byte-identically (SHA-256); unrelated assets are unchanged. Removed Bayesian figure has no active consumers in the revised deck/companions/outline.
- Frozen requests, evidence and plan copies in the reviewed commit match the owner files exactly. Changes remain within the agreed paths.

## Next handoff

Fix F01/F02, preferably the small F03 description too, synchronize the affected companions and shifted outline pointers, rerender the changed slides and neighbours, and provide `work-r2.md` with the exact pushed SHA. Do not change the approved opening, tail/oracle content, or RL section. No merge authorization.
