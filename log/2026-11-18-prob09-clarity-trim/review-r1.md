# review-r1 — Narrow note corrections before approval

- **Reviewed commit:** `6cf17f6ccb63bb3622267bf0993e67e2068867a8`
- **Baseline:** `5f4b1d99c5d799785752aa12c494715c3b21327b`
- **Branch / PR:** `2026-11-17-prob09-major-revision`, existing PR77
- **Verdict: revise.** Two blocking short-note corrections (F01/F02); no structural rebuild or new pacing target. F03/F04 are nonblocking cleanup.

## What matters

1. The main revision works: the CE/data-loss/generator opening now motivates MC; rare-event error is concrete; the contribution diagram, zero-variance explanation and lighter-tail counterexample answer Albert's questions. Keep these explanations.
2. The unknown-Z example is sound, but its note Message currently says the **posterior itself** is evaluable before normalization, reversing the distinction the example must teach. The divider note also says Z is never computed although the later validation computes it. Correct those words (F01).
3. The zero-variance slide has the right positive-finite-mean condition, but its note Message drops it while saying “any nonnegative integrand.” Keep the condition in the quick-read layer too (F02).

Both blockers are local H/M wording changes. The current70-slide structure and absence of a pacing promise are accepted.

## Coverage of Albert's requests

| ID | Status | Reviewed result |
|---|---|---|
| C01 | done | pp4–6, S130/S131/S04: exact one-hot CE/KL recall, population-loss average and model-generated format-pass rate; sample laws kept distinct |
| C02 | done | p12,S114: standard error expanded and defined as estimator SD, with outcome SD and realized error distinguished |
| C03 | done | S33/S37 and their active companion sections removed |
| C04 | done | pp15–16,S116a/b: zero-hit example then expected-hits/relative-RMSE calculation; secondary trend plot preserved in H and described in M |
| C05 | done | p28,S118: weighted contribution and target mean explicitly named; log-axis zero region and q-average clarified |
| C06 | done | p34,S57: large two-curve contribution-profile exhibit with a single message; signed curve explanation moved to notes |
| C07 | main done; notes correction | pp38–40,S63a/b/S64: random X versus constant contribution clear, oracle limitation adjacent; F02 repairs Message scope |
| C08 | done | pp44–45,S69a/b: exact benefit then explicit “No” and a lighter-but-finite counterexample |
| C09 | main/example done; notes correction | pp47–51,S132/S73/S133: Bayesian posterior and likelihood-weighted prediction; F01 repairs the quick-read normalization wording |
| C10 | done | p53,S77 and touched text/math consistently use IID, not Iid |
| C11 | done; minor cleanup |20-slide gradient chapter plus gradient recap retired; gradient-dependent RL derivation removed; F03 identifies one obsolete prerequisite phrase |
| C12 | done | pp60–68 retained as new Part05; behavior/reference distinction, mismatch and clipping limits preserved |
| C13 | done | No fixed duration, pacing filler or minimum count; five-part structure accepted |

## Findings

All locations refer to the reviewed commit. **H** is `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`; **M** is `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`; **D** is `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`. Full paths also appear in each numbered request below.

| ID | Slide / current page | Type | Blocking | What is wrong | Concrete fix |
|---|---|---|---|---|---|
| F01 | S132/p47 and S72/p46; H756/H751, M839/M833 | fact | **yes** | “posterior ... evaluate at any point” omits unnormalized; “normalizing integral is never computed” contradicts S133's numerical validation | Name the evaluable unnormalized posterior and distinguish estimator input from optional validation; exact replacements below |
| F02 | S63b/p39; H641, M725 | fact | **yes** | “For any nonnegative integrand” makes q*=fp/mu appear valid even when mu=0 or infinite | Put0<mu=E_p f<infinity in the Message, as already on the main slide |
| F03 | S109a/p69; H1061/H1069, M1186 | unmet request | no | “first synthesis” and “Gaussian path X=theta+epsilon” are leftovers from the removed gradient chapter | Say closing comparison; replace the prerequisite with the standard-normal prior used in the new Bayesian example |
| F04 | S132/p47; D1020 | design rule | no | Citation visibly wraps the source section title between “How” and “Stan Works” | Shorten/split into separate provenance and source lines; keep exact section locators in H/M |

### 1. F01 — Preserve the unknown-normalizer distinction [judgment]

- **Files:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html` lines751,756; `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md` lines833,839.
- **S132/p47 Message:** current “Even a small, familiar Bayesian model gives a posterior that we can evaluate at any point, while its normalizing integral is still left to compute.” → **“The unnormalized posterior can be evaluated pointwise; obtaining the normalized density still requires the integral Z.”** Equivalent wording is fine if the two objects remain explicit. The current main-slide proportionality and formulas are correct; leave them intact.
- **S72/p46 closing sentence:** current “...while its normalizing integral is never computed” → **“...whose unnormalized density is available pointwise; the estimator never needs its normalizing integral.”** Optionally add that the later numerical integral is used only for validation, as S133 already explains.
- **Why:** E07's entire teaching point is evaluable shape versus unavailable normalized height. A lecturer reading only Message must not be told the opposite. “Not needed by the estimator” is not “never computed anywhere.”
- **Acceptance:** H/M quick-read and detail layers agree with p47/p48/p51 and the implemented numerical check.

### 2. F02 — Qualify the zero-variance Message [judgment]

- **Files:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html` line641; `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md` line725. **S63b/p39**.
- **Current → replacement:** “For any nonnegative integrand, ...” → **“For f >= 0 with 0 < mu = E_p[f] < infinity, the oracle q* = fp/mu makes every contribution equal to mu, so its sample mean has zero variance; evaluating the oracle weights still requires mu.”** Render the math normally in H/M.
- **Why:** f=0 gives0/0, and an infinite mean cannot normalize q*. The main slide and the next note paragraph already state the right condition; DS9 requires the Message to retain it rather than overgeneralize.
- **Acceptance:** Message, main statement and explanation share the same conditions. No new main slide or proof is needed.

### 3. F03 — Retire the last gradient-era prerequisite wording [judgment; nonblocking]

- **Files:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html` lines1061,1069; `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md` line1186. **S109a/p69**.
- **Current → replacement:** H “The first synthesis slide” → **“The closing comparison”**. In both editions, “Gaussian machinery, the substrate for the Gaussian path X=theta+epsilon” → **“the standard-normal prior used in the Bayesian unknown-Z example.”**
- **Why:** the pathwise example and second synthesis page were removed, whereas the new Bayesian prior is the actual remaining prerequisite use.
- This is small stale-reference cleanup, not a reason to restore any gradient material or run another round on its own. The valid “Pathwise step” wording in S77's almost-sure convergence proof is unrelated and should not be deleted by a blanket search.

### 4. F04 — Keep source titles intact in the citation [judgment; nonblocking]

- **File:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html` line1020. **S132/p47**.
- **Instruction:** shorten the provenance line and separate it from the Stan citation. For example: **“Our logistic-normal toy; curves: gen/p9f_unknown_z.py.”** and **“Stan User's Guide, v2.40: posterior normalization and logistic regression.”** Keep the exact source headings/links in H/M.
- **Why:** the current final-size render breaks “How Stan Works” mid-title. DS6 calls for separate citation lines and intact titles. Do not shrink citation type or disturb the readable main exhibit.
- slides may choose a better concise citation treatment; this alone does not block approval.

## Review/check coverage

- Exact commit read through git and archived into disposable scratch; no source edits by owner. Diff confined to the permitted deck/companions/local figures/generators, Deepmath outline and new job record. Root outline has no stale prob09-specific pointer needing a change.
- Requests/evidence/plan-v1/plan-v2 copies in the candidate are byte-identical to the owner copies as received. Living job header subsequently changed to in-review by owner, as expected.
- All70 slide pages rendered and visually inspected; new/rewritten pages and plot keys checked at final size. Print-media/font-settled recheck confirmed S132's normal divider/body layout. DOM layout audit: no deck scroll overflow or collapsed divider. Necessary short-line density exceptions render without shrinking. No new main-slide clipping/overlap found.
- All changed H articles read, corresponding M content checked, and unchanged material compared with the previously approved baseline. D/H/M each contain70 unique IDs in identical order. M is ASCII. M linter has only visual-reference/navigation prompts, not structural errors; descriptions needed to understand the examples are present.
- Main and note lints pass. Deepmath outline lint:0 stale/missing pointers,0 warnings. The new section boundaries, page counts and theorem locations match actual source starts.
- All seven generators rerun; all generated figures byte-identical. New values/parameters independently rechecked, recorded in E11. Deletion of the retired gradient generator and old gradient-only numerical check is accepted: no surviving content cites them.
- H checked at **true mobile430**, initial scale1, and desktop430/1280. No430 article/math overflow and no KaTeX errors. Visually inspected the new CE, zero-variance, Bayesian and prediction notes. A2px desktop-only S114 measurement does not visibly clip content; not a blocker. At360 the worker's disclosed long-display overflows remain (S130/S22/S47b/S69a/S69b);360 was not this job's specified narrow acceptance width, so no additional work order on it.
- Accepted reported choices: pre-pass deletions; pointwise oracle identity instead of another display; source-label disambiguation; moved secondary statements/plots genuinely present in both companions; local figure-width choices judged by render, not a plan pixel prescription.

## Next round

No plan-v3 needed: F01/F02 restore the plan's existing mathematical distinctions, not a new argument. Make those local H/M fixes; address or explicitly decline nonblocking F03/F04. Recheck changed articles at430 and their neighbors; if the citation changes, render S132 and adjacent pages. Do not rerun a structural redesign or add pace content. Update any shifted outline pointers in the same commit, refresh the copied living evidence/header, and return `work-r2.md` with an exact pushed SHA and each finding's disposition. Review round2 will be changed material/neighbors only.
