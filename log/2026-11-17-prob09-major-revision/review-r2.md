# Round 2 review

- Job: 2026-11-17-prob09-major-revision
- Reviewed commit: **79b3163b79487e35b4b46963cee232b231f50941**
- Previous reviewed commit: 3f4bdd71df2566930e41f8f7e1b506d4f00d546e
- Baseline: b20ab73ac7e74e9489d379cf9caad7565f17e31e
- Verdict: **revise**. Narrow round-3 work order; no PR yet.

## What matters

1. **The substantive corrections are largely complete.** Keep the nonexclusive estimator map, corrected ESS limit, qualified baseline argument and two-slide synthesis. The independence/support corrections, prerequisite cleanup and removal of the duplicated numerical rare-event introduction are accepted. No further restructuring or literature work is requested.
2. **Two rendering repairs are incomplete.** S109a still exceeds capacity and its divider collapses. The new note overflow rule hides vertical math overflow: it does affect the required 430px view, contrary to the work report.
3. **Correct the new generic bridge's wording and alt text.** The Bernoulli plot does not show two curves meeting at rho=1/2, and its RMSE lesson needs the displayed domain and sample-size qualification.

## Request coverage

| Comment | Status | Assessment |
|---|---|---|
| C01 | Not done / implementation complete, acceptance pending | Deck and both note editions now contain 86 matching sections. Local blockers below remain. |
| C02 | Done | Prior-deck continuity and redundancy corrections are accepted, including prob05 variance attribution, prob08 Gaussian bridge, opt01 outline cleanup and the generic S116 introduction. |
| C03 | Not done / major revision achieved | Revised narrative and exhibits accepted; remaining fact/accessibility/design repairs prevent final approval. |
| C04 | Done | Approved scope and 150-minute pacing retained. S109a/b is an allowed split, not a change of argument or duration. |

## Checks and scope

- Reviewed the round-2 diffs in deck, HTML note, accessible Markdown and Deepmath outline against the prior findings and original requests. No reopening of unchanged material or new scope.
- Archived the exact SHA and rendered all 86 pages. Visually inspected changed pages **5,6,15,17,27,30,37,38,41,47,50,53,54,60,64,70,71,77,79,83,84,85,86** at full size; checked immediate neighbours **4,7,14,16,18,26,28,29,31,36,39,40,42,46,48,49,51,52,55,59,61,63,65,69,72,76,78,80,82**. No new glyph, touching-cell or footer-collision defect on the repaired slides. S109a's capacity defect is detailed below.
- Independently tested the note in Chromium after fonts and KaTeX loaded: true mobile 430px (layout width 430, visual scale 1), narrow desktop 430px, and desktop 1280px. Inspected screenshots of the opening, S94 and the affected S19 derivation; 360px was an additional exploratory check, not a new acceptance width. Zero KaTeX errors. Checked articles and math boxes, including with the new scroll rule disabled temporarily in the browser only. No pinned source was changed.
- Deck/HTML lint pass; accessible Markdown is ASCII and has no lint ERROR. All three editions have the same 86 unique IDs in the same order. S109 is replaced only by S109a/S109b; closer moves to p86.
- The target prob09 outline pointers pass. A whole-course outline check on the intentionally partial scratch archive reports other lecture files missing; this is not a source defect or a claim of a new whole-course outline pass.
- Frozen plans, requests, review-r1 and the pre-round-2 evidence register match the tracked copies exactly. Round-2 source changes are confined to the three target files and the shared outline; other changes are this job's log. No generator/reference/script or earlier-deck changes. Prior generator verification remains applicable.

## Prior finding disposition

| Finding | Status | Accepted result / residual |
|---|---|---|
| F01 | Partially resolved; still blocking | Mathematical qualifiers and S109a/b split accepted. S109a capacity remains; see item 1. |
| F02 | Closed | Possible/generally finite-sample SNIS bias and generally dependent averages. |
| F03 | Closed | General ESS limit, full-coverage specialization and integrand-sensitive message. |
| F04 | Closed | Optimal density keeps its support indicator in the simplified expression. |
| F05 | Closed | Independence is stated for the weight factors; both policies' factorization explained in notes. |
| F06 | Closed | Nonexclusive capability map; availability distinguished from efficiency. |
| F07 | Closed | Exact baseline cancellation, finite-moment assumptions, zero-score case and sign-general variance test. |
| F08 | Closed | Requested local scope/rounding/pathwise/one-sign corrections are synchronized. |
| F09 | Partially resolved; still blocking | Viewport and S94 repair accepted. New math clipping remains; see item 2. |
| F10 | Closed | Glyphs, table separation, underbrace labels and proof/IS capacities repaired. |
| F11 | Closed | Prerequisites and outline counts/bridge/pointers corrected. |
| F12 | Closed | Evidence ID, Markdown token, diagram description and finite tail-window description corrected. |
| F13 | Closed as a redundancy request | Generic Bernoulli bridge accepted; a new correctness regression is F15 below. |
| F14 | Closed | Optional hand-chosen-points title adopted. |

## Remaining change requests

All paths below are repo-relative. Line numbers refer to the reviewed SHA. Keep deck/HTML/Markdown descriptions synchronized where an exhibit changes.

### 1. F01 (carried) — Finish the expectation-synthesis capacity repair

- **Where:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`:1990-2003, **S109a / p84**; matching note articles/sections S109a.
- **Type:** design rule. **Blocking: yes.**
- **Observed:** The table has four rows including its header; plus the target paragraph and highlight, the body costs six elements against the five-element budget. At 1280x720 print layout, scrollHeight is738 and the blue divider is compressed to zero height. The PDF does not cut off visible text, but that is not a capacity pass.
- **Fix [judgment]:** Remove the redundant bottom highlight from this slide and retain its warning in the note. Keep the three estimator rows and their conditions, shared integrability/IID lead, normal divider, existing type and normal spacing. Update the note's exhibit description so it no longer says that line is highlighted on-slide. Do not add a slide or shorten away assumptions.
- **Reason:** This is the smallest content-level repair; the warning already recurs throughout the lecture. It closes the original F01 rather than trading capacity for a collapsed divider.

### 2. F09 (carried) — The new scroll rule clips displayed math

- **Where:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`:22 and the derivations in **S19 / p8** (article starts148), **S116 / p15** (264), **S90 / p66** (995). S94 / p69 is now good.
- **Type:** design rule / readable mathematics. **Blocking: yes.**
- **Observed:** `.katex-display { overflow-x: auto; overflow-y: hidden; }` is not inert at 430px. True mobile 430: S19 width311 inside308, vertical scrollHeight61 versus clientHeight57; S116 width310 inside308 and height65 versus59. Narrow desktop 430 also affects S90 (338 inside328; height49 versus45). In the S19 screenshot the horizontal scrollbar runs through the lower summation-limit area; hidden vertical overflow cannot be recovered by horizontal scrolling. Document/article width equality alone misses this.
- **Fix [judgment]:** Remove the new hiding workaround and break the identified long displays into logical mathematical steps, as successfully done for S94. Alternatively retain defensive horizontal scrolling only if all glyphs remain visible and nothing is vertically clipped; it is not a substitute for fitting these displays at the agreed430px check. Do not reduce font size. Synchronize any changed mathematical line sequence in the Markdown edition.
- **Verification:** Test both true mobile 430 and narrow desktop 430 after fonts/math load, plus desktop 1280. Inspect the actual lower limits, fractions and radicals, not only scrollWidth. Recheck all articles. S115's residual one-pixel narrow article measurement comes from an approximately half-pixel KaTeX vlist edge; do not shrink text to chase that rounding artifact. The blocker here is demonstrated clipped math.
- **Reason:** The disclosure in work-r2 is appreciated, but the implemented rule does not meet the original no-clipping requirement. No broader 360px redesign is requested.

### 3. F15 (new) — Make the generic rare-event message and alt text accurate

- **Where:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo.html`:478,480,501, **S116 / p15**; matching `prob09-monte-carlo-note.html` S116:264 onward and `prob09-monte-carlo-note.md` S116:321 onward.
- **Type:** fact. **Blocking: yes.** Evidence: E31.
- **Current → new:**
  - The unqualified line “Variance rho(1-rho) is small; ... relative RMSE ... is large” → qualify the rare-event regime and n. For example: **“Rare rho: small indicator variance rho(1-rho)”**, then the existing relative-RMSE formula with **“small relative RMSE requires enough draws.”** Equivalent concise wording is fine; do not claim it is large regardless of n.
  - “At fixed n, smaller rho: smaller absolute error, larger relative error” → **“At fixed n and 0<rho<=1/2: rarer events lower absolute RMSE but raise relative RMSE.”** Keep the distinction between a distribution-level RMSE and a realized run's error. Let slides choose a clear line break if needed.
  - In the SVG aria-label, remove **“they meet near rho equal to one half.”** Replace with **“At rho=1/2, absolute SD is 1/2 and relative SD is 1; the curves do not meet on the displayed range.”** Use readable spaces in the actual label. The main plot itself is correct and should be retained.
- **Reason:** The new bridge should teach the two error scales, not a sample-size-independent claim or a false curve intersection. Keep it generic: do not restore Exp(1), e^-10 or the duplicated sample-size calculation.

### 4. F16 (new, nonblocking) — Remove a misleading Gaussian backward reference

- **Where:** `courses/deepmath/prob09-monte-carlo/prob09-monte-carlo-note.html`:1307, **S109b / p85**.
- **Type:** fact / internal reference. **Blocking: no.**
- **Current → new:** “…compare the variances on the problem at hand, **as the Gaussian comparison did**.” → “…compare the variances on the problem at hand.”
- **Reason:** S125 compares the analytic derivative with the pathwise mean and states pathwise variance 4; it does not compare score and pathwise variances. The Markdown edition already omits this misleading clause. No new comparison slide or derivation is requested.

## Plan decisions / next handoff

- Accept the 86-slide mapping and unchanged 150-minute budget. No plan-v3: these are repairs under plan-v2, not argument/scope changes.
- Round 3 is the final normal review round for this large job. Limit edits to the remaining requests and necessary synchronization; report each ID in work-r3 and name the exact commit. The next review will check changed slides/notes and neighbours, not reopen the whole deck.
- No PR until approval, followed by the final record push and log-only-tail verification. No PDF delivery or merge authorization.
