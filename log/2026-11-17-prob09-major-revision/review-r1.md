# Round 1 review

- Job: 2026-11-17-prob09-major-revision
- Reviewed commit: **3f4bdd71df2566930e41f8f7e1b506d4f00d546e**
- Baseline: b20ab73ac7e74e9489d379cf9caad7565f17e31e
- ID commit: c47b198f8e8d0153fee6923ce2dafe8b13f4fe77
- Verdict: **revise**. Round 2 work order; no PR yet.

## What matters

1. **Keep the new argument and examples.** The 113→85 restructuring is substantial, the practical Exp(.1) proposal now precedes the oracle, and the Gaussian/two-action comparison makes the gradient section teachable. The behavior/reference distinction and PPO correction are also worth keeping. This is not a request for another restructure.
2. **Do not lose assumptions in the short versions.** Several correct detailed explanations are contradicted by the recap or Message paragraph: unconditional SNIS bias, the ESS population formula without mass coverage, and the token-product factorization with insufficient independence. These are central to the lecture's “what can we honestly claim?” argument.
3. **The visual/accessibility pass missed real defects.** The note uses a 980px layout on a 430px mobile device and scales down; one article overflows even in desktop narrow mode. There are missing glyphs and touching labels/cells. Repair these without shrinking type.

## Request coverage

| Comment | Status at this commit | Assessment |
|---|---|---|
| C01 | Not done / substantial implementation complete | Deck and both note editions rebuilt, but blockers below prevent acceptance. |
| C02 | Not done | Prior-deck audit informed the revision and much redundancy was removed. Stale prerequisite attribution and a repeated rare-event calculation remain (F11, F13). |
| C03 | Not done / major revision achieved | New narrative, exhibits and per-slide notes are in place. Mathematical short-form consistency and design/accessibility corrections remain. Model names did not require reconfiguration. |
| C04 | Done | Approved scope, six parts, rigorous junior-undergraduate mode and 150-minute pacing respected; no unauthorized earlier-deck edits. |

## Review scope and checks

- Read all 85 slide bodies and all 85 HTML note articles, plus the Markdown edition, including its differing figure/table descriptions. Reviewed original requests, the source/evidence record, current design rules, then the plan. All page numbers and source lines below refer to the reviewed SHA.
- Extracted that SHA into scratch and rendered with Chromium 156; inspected **all 85 pages at 1280×720**. Checked the HTML note at desktop and 430px narrow/mobile viewports, including actual screenshots, not only document scroll width.
- 85 unique slide IDs; deck, HTML articles and Markdown blocks have identical ID order. No empty final articles. Main and HTML-note lint pass, and KaTeX reports zero errors. Markdown is ASCII; accessible-Markdown lint has one error at line 896 (`0<p(4)` mistaken for HTML), plus visual-reference warnings. The wording warnings are not automatically findings: the substantive descriptions are present.
- Reran all seven generators from the pinned archive: success, and all file hashes unchanged. Checked the exact finite-state/MSE/baseline calculations and analytic rare-event/tail examples. Source-locator correction and implementation provenance are now appended as E22-E30 in evidence.md.
- Setup A is 08e7f8638176cebdfcf0702fe92021df8337a4d2. Removing only its article wrappers gives the previous note modulo insertion whitespace. Removing the IDs from setup B gives exact pre-B deck/note bytes. Frozen plans and requests, and the pre-review evidence record, match their tracked copies exactly.
- Baseline-to-candidate changes are confined to the target deck/notes/figures/generators, shared Deepmath outline and this job's log. No earlier lecture source, global reference or script changes.
- DOM print-mode checks additionally flag S101 (730px scroll height in 720px) and S109 (727px); the issue is body/reserve capacity, not a claim that visible content was cut off the PDF. See F01/F10.

## Paths and synchronization

The following aliases are **repo-relative file paths** used in every numbered finding:

- **D** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`
- **H** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`
- **M** = `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.md`
- **O** = `courses/deepmath/OUTLINE.md`

Each content correction includes the same-ID HTML and Markdown note, including Message, explanation, details, caption/alt text and any verbal figure description. Do not correct a detailed paragraph while leaving its quick Message wrong. Preserve untouched material. `[judgment]` marks wording/design decisions for slides itself, not a context-free implementation worker.

## Blocking findings

### 1. F01 — The final “honest claim” table drops the conditions it is meant to summarize

- **Where:** D:2011-2025, S109 / p84; H:1285-1301; M:1523-1551.
- **Type:** fact (also design-rule capacity). **Blocking: yes.**
- **Wrong / why:** “consistent, biased at finite n” contradicts S78's explicit unbiased special cases. “Differentiable ln p” alone does not establish a score identity, and “baseline keeps the mean” is not true for arbitrary sample-dependent baselines. The ordinary-MC finite-RMSE condition disappears. The six-row table plus highlight exceeds §1's element budget before the necessary qualifiers are added.
- **Fix [judgment]:** Preserve the five methods but distinguish the target of the first three (an expectation) from the last two (its gradient). Replace the title's literal “One Target” by a principle-based title, e.g. “Choose an Estimator by Its Requirements.” If needed, split into **S109a (expectation estimators)** and **S109b (gradient estimators)**, with paired notes; the closer remains S113. Keep the combined synthesis/closer time at five minutes. Do not pack more text into the existing table or shrink it.
- Required claims: ordinary MC under IID/integrability; **finite-variance** RMSE sigma_f/sqrt(n). Ordinary IS needs proposal draws, evaluable normalized p/q and coverage of nonzero fp (full p coverage is sufficient but not necessary); first-moment validity is distinct from finite variance. SNIS needs full target coverage, a proper target, integrable f and positive sampled denominator; it is **generally**, not always, finite-n biased and is consistent under the stated assumptions. Pathwise needs parameter-free base noise, a valid differentiable path/chain rule and justified interchange. Score uses the fixed-support/valid-interchange assumptions already taught; a **sample-independent constant** baseline preserves the mean when the score has mean zero.
- Use a short shared assumptions line where appropriate rather than repeating a theorem in every cell. The note formula reference must carry the complete conditions. Evidence E02, E04-E08, E15, E27.

### 2. F02 — SNIS qualifications disappear in the introduction and ratio explanation

- **Where:** H:65 (S02 / p2), H:691 (S72 / p43), H:732 onward and D:1046 onward (S76 / p47); M:27,751,799-805; plus F01's closing occurrences.
- **Type:** fact. **Blocking: yes.**
- **Fix:** “at the price of a small bias” → “with possible finite-sample bias”; “biased at any finite sample size” → “generally biased at finite sample sizes.” Do not suggest the bias is guaranteed small.
- On S76, “shared, so dependent” → “generally dependent”; apply the same qualification to the note prose. Sharing draws alone does not force dependence (e.g. q=p makes the denominator constant). The actual reason to retain is **expectation does not commute with taking a ratio**; the two unbiased components do not imply an unbiased ratio. E05/E25. The accurate counterexample and exceptions on S78 should remain.

### 3. F03 — The population ESS formula is missing a normalization assumption

- **Where:** H:801-810, S79 / p52, “Empirical vs population”; M:886. Also H:793 / M:868, S70 / p51 Message.
- **Type:** fact. **Blocking: yes.**
- **Fix:** State the general IID limit `ESS/n -> (E_q[w])^2/E_q[w^2]` for positive finite mean and finite second moment, then obtain `1/E_q[w^2]` using **w=p/q and full p-support coverage, hence E_q[w]=1**. The next slide's own missing-support toy has E[w]=3/4 and E[w²]=9/16; the current statement would give ESS/n→16/9 although ESS/n=1. E30 supplies the correction.
- S70 Message “a batch of five draws behaves almost like one draw” → **“One draw holds 95% of the normalized weight; its contribution still depends on f.”** This preserves the distinction already explained correctly in its details. It is not an integrand-independent effective number of observations. E06/E19.

### 4. F04 — The oracle density loses its support indicator

- **Where:** D:877 onward, S63 / p37, first displayed formula.
- **Type:** fact. **Blocking: yes.**
- **Fix:** `1{x>10} e^-x / e^-10 = e^{-(x-10)}` → `1{x>10} e^{-(x-10)}` on the right as well, or explicitly state that expression is only for x>10 and the density is zero otherwise. As printed, the right side is not the density being plotted. The H/M explanation already largely supplies the domain; keep all layers consistent. E04/E11.

### 5. F05 — Independent behavior tokens do not alone justify independent ratios

- **Where:** D:1884 onward, S103 / p79, first bullet; H:1202-1213, first explanation; M S103 corresponding paragraph.
- **Type:** fact. **Blocking: yes.**
- **Fix:** “Tokens independent under pi_b” → **“Weight factors independent under pi_b”**, or explicitly say that **both policies factor into independent positionwise token distributions** in this toy. Keep the existing per-factor moments. The factorization E[(product w_t)^2]=product E[w_t²] needs independence of the factors, which can depend on the prefix even when behavior tokens are independent. The detailed explicit binary construction already has the stronger condition; bring it into the slide and short explanation. Do not change the numerical plot or general autoregressive caveat. E20.

### 6. F06 — The estimator-choice flow incorrectly makes IS a fallback only when p cannot be sampled

- **Where:** D:1255 onward, S82 / p54; H:828-835; M:904-910.
- **Type:** fact / unmet request for conceptual clarity. **Blocking: yes.**
- **Fix [judgment]:** Turn the yes/no fallback into a **nonexclusive capability map**, or explicitly allow choosing a different proposal for efficiency even when p is sampleable. State: “These requirements tell us which estimators are available, not which is best.” Ordinary MC, IS and sometimes SNIS can all be available for the same problem. The running Exp(1) example deliberately uses IS despite an easy target sampler, so the present “no” arrows contradict the main teaching example. Keep the evaluable-normalized-ratio versus unknown-normalizer distinction and the warning that availability is not efficiency. E04-E05/E28.

### 7. F07 — Qualify the baseline cancellation and the general variance optimum

- **Where:** D:1675 onward, S96b / p71; H:1081-1100; M S96b details.
- **Type:** fact. **Blocking: yes.**
- **Fix:** “An action-dependent b(X) breaks this cancellation” → **“An action-dependent b(X) need not cancel.”** The exact requirement is E[b(X)s]=0; arbitrary action dependence removes the guarantee, not every possible cancellation.
- Before the general b* quotient add **0<E[s²]<infinity and E[R²s²]<infinity**, with the zero-score case identified as trivial rather than dividing by zero. Use analogous conditions for squared score norm in the vector trace statement. Keep the existing sign-general strict-improvement test **b(b−2b*)<0**. The report's `0<b<2b*` is only for b*>0; b=2b* ties with zero. The toy is correct. E27.

### 8. F08 — Align the remaining quick explanations with their actual mathematical scope

- **Type:** fact. **Blocking: yes.** All below are local wording corrections, not new material.
- **8.1 S48 / p24, H:411, M S48 Message:** “If q never visits a region where fp≠0, the estimator is wrong for every sample size” → **“In this four-state example, missing the only contributing state makes every estimate zero instead of 1/4.”** The old universal statement ignores cancellation in signed integrands. Keep the example and general coverage guarantee distinct.
- **8.2 S54 / p30, D:769 onward, H:501-508, M S54:** retain/recall integrability for unbiasedness. “Failing the first check gives a biased estimator” → **“Missing coverage can bias the estimator, as in the four-state example.”** Split the second failure: **an infinite weighted second moment gives no finite RMSE; a large but finite second moment gives a large but finite RMSE.** The present check asks for “finite and small,” but its failure is then incorrectly equated to infinity.
- **8.3 S64 / p38, H:611, M:672:** “c, which for a one-sign integrand is the answer itself” → **“c, which is |mu| for a one-sign integrand and mu for this nonnegative indicator.”** A negative integrand has c=−mu.
- **8.4 S121 / p41, H:659, M S121 Message:** replace “only a finite second moment gives variance, RMSE and CLT error bars” with **“This integrable example converges, but its infinite second moment rules out finite RMSE and the usual finite-variance CLT error bar.”** Keep the claim tied to the displayed example/standard CLT, not a universal characterization of all possible asymptotics.
- **8.5 S128 / p74, H:1142, M:1370:** “pathwise estimator is unavailable when ... R is not differentiable” → **“The ordinary pathwise formula shown here cannot be used unless its chain-rule and interchange conditions hold; sampled discrete actions do not provide a naive differentiable path.”** Do not categorically exclude almost-everywhere differentiable rewards or specialized methods. No new survey is needed.
- **8.6 S24 / p12, H:223, M:264:** after rounding n up, “the bound equals 0.05” → **“the bound is at most 0.05.”** S118 / p27, H:455 and paired M: “At x=10 [the contribution] ...” → **“Just above x=10 ...”** because f=1{x>10}. Small edits, but keep strict versus non-strict claims accurate.

### 9. F09 — The HTML note is not actually mobile-readable and has article overflow

- **Where:** H head:3-10, entire note; S94 / p69 H:1044 onward; S115 / p11 narrow check.
- **Type:** design rule (§9). **Blocking: yes.**
- **Observed:** With mobile emulation at physical width430, layout/inner width is980 and visual scale≈0.4388 because there is no viewport metadata. Text is rendered at less than half size. At desktop width430, article S94 has clientWidth367 versus scrollWidth374; its long first score-mean line leaves the shaded derivation box. S115 also registers a one-pixel article overrun in this browser; recheck rather than treating document-level equality as sufficient.
- **Fix:** Add correct device-width viewport metadata. Break S94's long expectation expansion into logical steps; keep font sizes. Verify **every article**, not only document/body scrollWidth, at approximately430px in both narrow desktop and true mobile mode after fonts/math load. Retain zero KaTeX errors and no clipping/hiding/scale-to-fit workaround. Recheck desktop too.

### 10. F10 — Repair rendered defects and explicit capacity violations

- **Type:** design rule (§1, §5, §8). **Blocking: yes.** These were checked in the full-size render; no global CSS changes or font reduction.
- **10.1 S64 / p38, D:899 onward:** the loop-arrow character renders as a missing-glyph box. Replace it with a supported drawn arrow or omit the redundant glyph. **S121 / p41, D:955 onward:** the negative check glyphs also render as boxes; replace them with readable words such as “fails” / “unavailable,” or supported symbols. They encode the conclusion and cannot be left as tofu.
- **10.2 S122 / p50, D:1129 onward:** in the consistency row, `if q covers fp` runs into `if q covers p`, so the columns appear as one expression. Reflow/shorten the cell wording, or give these two conditions their own clearly separated lines. Keep the full-target versus fp distinction. Do not reduce table type.
- **10.3 S88 / p64, D:1532 onward:** underbrace labels “depends on theta” and “fixed number” touch. Separate the labels or shorten to “changes” / “fixed,” with theta dependence explicit in the framing line. The audience must be able to associate each label with its factor.
- **10.4 S101 / p77, D:1835 onward [judgment]:** the final list reaches y≈682, essentially the footer band (brand starts684); slide scrollHeight730 exceeds720. Remove the redundant gray p/q identity and keep the newly relabelled policy identity, with its ratio/coverage/estimator explanation. The prior theorem is already named in the lead line. Do not compress margins or type further to keep both copies.
- **10.5 S125 / p60, D:1440 onward [judgment]:** two three-line aligned blocks exceed §1's explicit math-block ceiling, even though the current side-by-side render is not clipped. Keep the analytic result J=theta²+1, derivative2theta, pathwise contribution2X and its mean2theta; move the two elementary expansions to the existing note. This preserves the comparison without six displayed derivation lines.
- **10.6 S96a / p70, D:1661 onward [judgment]:** reduce the four-line aligned proof to at most three lines by combining the definition/log-derivative equality, retaining the justified finite-sum interchange and normalization. No outline/extra recap slide is needed for this short proof. Preserve the full expanded steps in the note.
- S109 capacity is handled with F01, not by shrinking its table.

### 11. F11 — Finish the prerequisite and shared-outline cleanup

- **Where:** H:1298,1321; M prerequisite/reference list near end; O:497-499 and opt01 introduction around532.
- **Type:** unmet request (C02), fact. **Blocking: yes.**
- **Fix:** Remove the inherited attribution of **variance rules to prob01**. At the frozen baseline prob01 covers LOTUS/Jensen but not variance; cite the actual sample-mean/variance material in **prob05**, as E01 already does. Keep the Gaussian-construction connection to prob08 explicit in O's prerequisite sentence, matching S123.
- Correct O's stale opt01 prose “answers prob09's bridge” now that this job retires that bridge. A minimal shared-outline replacement such as **“Lecture 10 begins the optimization half after prob09 closes the probability sequence”** is within this job's shared-surface scope. Do **not** edit opt01 or any prob01-prob08 deck/notes. Update this job's counts/ranges/pointers if any slide splits occur.

### 12. F12 — Small source/accessibility synchronization repairs

- **Type:** fact / design-rule consistency. **Blocking: yes.**
- **12.1 S125 / p60, H:916 and corresponding M source line:** the Gaussian calculation is labelled E13, which is the two-action baseline toy. Cite **E15 plus E24's actual generator**. E22 corrects the owner's Ouyang locator; leave the already-correct arXiv-v1 §3.5 equation(2) citation in the deck/note.
- **12.2 S81 / p53, M:896:** replace raw `q(4)=0<p(4)` with `q(4)=0\lt p(4)`; rerun accessible-Markdown lint. This is a math-token/HTML-lexer collision, not an instruction to strip legitimate mathematics or change the shared linter.
- **12.3 S100 / p76, H:1157-1160 and M S100 figure description:** the description says left/middle/right or “three boxes in a row”; the actual exhibit has behavior above current on the left, with target estimate on the right. Describe that arrangement accurately, or describe the three roles/arrows without spatial wording. Retain the full verbal description for the accessible edition.
- **12.4 S43 / p17, H/M figure explanation:** the shaded plot is truncated at x=14, whereas mu=e^-10 is the full tail beyond10. State that **the tail continues beyond the displayed range**; do not call the finite shaded patch exactly the entire probability. No redraw is required if the continuation is made clear in the explanation/caption.

### 13. F13 — Remove the premature repeat of the numerical rare-event result

- **Where:** D:473 onward, S116 / p15; H:262 onward; M S116; O Part01 description.
- **Type:** unmet request (C02). **Blocking: yes.**
- **Fix [judgment]:** Make S116 the generic **Bernoulli probability rho / absolute-versus-relative error** bridge. Keep the error comparison plot/formula and the lesson “At fixed n, smaller rho can mean smaller absolute error but larger relative error.” Reserve **X~Exp(1), event X>10, rho=e^-10 and n=2,202,547** for S43-S44 / pp17-18, where the event is actually introduced and the budget worked out. Remove that duplicated numeric marker/punchline from p15 and its quick explanation; its generator may retain a shared calculation used later. The purpose is to avoid announcing the full worked answer and then immediately starting the same example again, not to remove the useful absolute/relative distinction.

## Nonblocking preference

### 14. F14 — Name the hand-chosen dart example as points, not draws

- **Where:** D/H/M S26 / p6, title (D near241).
- **Type:** preference. **Blocking: no.**
- **[judgment]** Prefer **“Six Points Give One Estimate”** or **“Six Points Illustrate the Recipe”** to “Six Draws Give a Noisy Estimate.” The existing explicit hand-chosen/not-a-random-run qualification is good and must remain. The current title is not a separate blocker because the qualifier is visible. This resolves work-r1 plan issue1; slides chooses the title.

## Decisions on work-r1 deviations and plan issues

1. **Accept deviations 1-10 in principle.** In particular keep PPO's locally defined r to match the source crop; keep the useful KL counterexample numbers on the slide; exact Bin(6,pi/4) is better than an unnecessary simulation; d=2/8/20 separates the curves while d=4 is explained in notes; removing redundant bullets/citation boilerplate and leaving purposeful whitespace is fine. S109 still needs F01, not restoration of every example on the main slide.
2. **Accept the exact MSE extension and qualified bias expansion.** E25 records them as our calculation, not a source theorem. No assertion of universal O(1/n) bias is authorized.
3. **Correct the planner's source record:** E22 replaces E10's wrong locator; E23 confirms the midpoint/tensor-grid attribution. This is not grounds to force the implementation back to the wrong locator.
4. **Generator paths accepted and recorded in E24.** Reproducibility was independently verified. Gaussian calculations should point to E15, not E13 (F12).
5. **Extra derivations/context accepted:** E26 covers the sufficient interchange argument; E27 the baseline variance calculation; E28 the Bayesian-normalizer context; E29 the direct sequence count. They stay details/illustrations, not new teaching modules. The general baseline improvement condition is the sign-general product condition, with finite-moment/positive-denominator assumptions (F07).
6. **Action names a1/a0 accepted.** They avoid collision with baseline b; no change requested.
7. **Shared opt01-outline prose may be repaired, but no opt01 artifact edits** (F11).
8. **No new plan version is required for these repairs.** The argument, required concepts, exclusions and 150-minute time budget remain plan-v2's. Splits/layouts are implementation discretion under the contract. If S109 splits, use S109a/S109b and report the mapping; update all three artifacts and shared counts/pointers. If another change would alter argument/scope/time, return it as a plan issue rather than implementing silently.

## Round 2 acceptance / handoff

- Resolve **F01-F13**, address F14 at slides' discretion, and report each finding ID in work-r2.
- Run deck/note lint, accessible-Markdown lint (explain any remaining warnings), ID/title/order pairing and outline pointer checks. Rerender changed slides and immediate neighbours at final size. For note edits, verify all articles at desktop and actual ~430px mobile/narrow layouts; changes to responsive behavior affect the whole note.
- Keep the six-section story and good exhibits; no new literature survey or scope expansion. Record exact content SHA and any split mapping. Copy this review unchanged and refresh the living job/evidence files on push.
- The next review will be a changed-slides-and-neighbours pass, not another full-deck redesign. Two review rounds remain. No PR or merge authorization yet.
