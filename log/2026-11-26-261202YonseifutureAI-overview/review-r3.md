# Round3 review — Albert's clarity revision

- Job: `2026-11-26-261202YonseifutureAI-overview`; existing **PR82**.
- Reviewed commit: **2336d436adcb8ccc4c60c72ab9f64b93d8ebf630**.
- Revision baseline: **753041e2bfe1ed77592613cd4ff73ff615810176**; previously approved content **07f519cec547faa37cba901c8f5f0da07125360d**.
- Original creation baseline: **467cf0630d25ec9929c9e1e87cea901224637487**.
- Verdict: **approved**, round **3 of3**. C20–C24 are implemented; prior request coverage is retained. No blocking finding. F11 below corrects the work report's search claim, not the deck.

## Result

S20 now shows an AI-specific score/goal failure in one concrete customer example. S21 explicitly names the two privacy risks and keeps the processing-versus-training distinction. The private-webpage wording and Reddit/Comet replacement remove the developer-oriented detour. Removing S27 leaves a coherent deepfake → mistakes/attacks transition.

The result is45 slides and45 paired note articles, still planned for43 minutes plus2 minutes reserve. Former p33 is nowp32 (stable S33). Approval is pinned to the SHA above; no content changes are required.

## Coverage of original scope

The full round1/round2 review stands for unchanged material; this pass checked changed content, dependencies and neighbouring slides, not another whole-deck factual review.

| Comment | Done? | Result |
|---|---|---|
| C01 | Yes | Trustworthy-AI overview and delegation argument retained. |
| C02 | Yes | Exact requested target folder unchanged. |
| C03 | Yes | Main and paired English note HTML;45 matching IDs. |
| C04 | Yes |45 slides,43+2-minute timing plan, within requested40–50. |
| C05 | Yes | Overview-course spine; no technical lesson added. |
| C06 | Yes | Existing semester survey retained; selected lec13 Reddit example now used. |
| C07 | Yes | High-level concepts and concrete exhibits. |
| C08 | Yes | Executive vocabulary improved in the requested places. |
| C09 | Yes | Diagram-led; revised primary labels remain readable. |
| C10 | Yes | Real cases retained; replacement case explicitly labelled research demonstration. |
| C11 | Yes | Personal story still precedes Contents. |
| C12 | Yes | Private email-derived manual remains central. |
| C13 | Yes | Vice Dean/seasonal-paperwork motivation unchanged. |
| C14 | Yes | Weekly update workflow retained. |
| C15 | Yes | Brief injection and possible unauthorized webpage-change path. |
| C16 | Yes | Read-only reader → Albert's approval → separate coder unchanged. |
| C17 | Yes | Capability/consequence arc and later injection discussion retained. |
| C18 | Yes | Approved argument/scope retained; local revisions directly authorized. |
| C19 | Yes | English throughout. |

## Coverage of Albert's latest comments

All paths below are relative to `talks/261202YonseifutureAI/`. Main = `261202YonseifutureAI.html`; notes = `261202YonseifutureAI-note.html`. Page references are current unless marked old.

| Comment | Done? | Verified implementation |
|---|---|---|
| C20 | Yes | S07/p7: destination is Private webpage / my manual; path, agent capability, takeaway, accessibility text and note all describe the unwanted page change. Possible-path qualifier retained; actual separated workflow on S08 unchanged. |
| C21 | Yes | S20/p20: Closed Tickets, Unsolved Problems. Customer refund request → AI scored on closure → request closed versus refund still missing. Illustration label, direct score-versus-outcome takeaway and matching plain-English note. Not presented as a company incident or inevitable behavior. |
| C22 | Yes | S21/p21: Two Different AI Privacy Risks. Confidential input/access-or-retention versus prior training/potential repetition, separated visually. Service/settings training-use qualifier and aligned note; S22 remains the concrete research example of the second risk. |
| C23 | Yes | S33/oldp33→p32: Reddit/Comet example replaces GitHub, not just its labels. User summary request, public/private/public crossing, login-code exposure and research/date/attribution visible. Case and mitigation callbacks in S06/S07/S36/S37/S44/S45 notes no longer teach repositories or pull requests. Retained bare source ID discussed under F11. |
| C24 | Yes | S27 and its note removed, not moved elsewhere; ID retired. Counts, note headings/order, pace lines, root/leaf outlines and following page numbers updated. S26→S28 transition preserves the deliberate-deception distinction. |

## Findings

| ID | Slide ID / page / location | Type | Blocking | What is wrong | Fix / disposition |
|---|---|---|---|---|---|
| F11 | S28/p27, notes line357; `log/2026-11-26-261202YonseifutureAI-overview/work-r3.md`, search-result statement after coverage | Fact (work-report accuracy) | No | The report says E06 is absent, but the unchanged source-only phrase `prompt-injection side per E04/E06` remains. It contains no GitHub explanation or old-case teaching callback. E06 still exists in the historical evidence register and supports the generic claim. | **Closed by this record correction.** The source ID is a harmless exception to the search claim, not an unmet audience request. No deck or frozen work-report edit requested; do not reopen content for it. |

F01–F10 retain their round2 dispositions. S27/F04 is now retired by Albert's explicit request. No new blocking issue, plan disagreement or scope deviation.

## Independent verification

- Compared exact git objects at the two pinned SHAs and extracted2336d43 with `git archive`. Nine changed files are limited to main/notes, target/root outlines and this job's logs; no course, reference, script or figure changes. After removing mechanical HTML comments, only live main slides S07/S20/S21/S33 differ; S27 is removed. Changed styles are local to those exhibits/retired content, not a shared typography reduction.
- Read the changed main/notes and dependent callbacks against Albert's C20–C24 first, the verified E25/E26 source boundaries, design rules and plan-v3. S33 matches Brave's2025 “Attack demonstration” scope; no current-vulnerability or victim claim, operational payload or transplanted GitHub configuration. Control caveats from the prior review remain intact.
- Independently rendered and visually inspected current pages **6,7,8,19,20,21,22,26,27,28,31,32,33,44,45** at1280×720, with transitions/fonts settled, and their print views. These include changed slides, neighbours, removal transition, recap and end-count checks. Primary meaning-bearing labels remain at least24.8px; smaller evidence tags are ancillary. No off-slide geometry, clipping, overlap, citation/footer collision or missing cross/arrow glyphs found. Internal print PDF has45 pages,960×540pt.
- Checked note layout at1280×900 and430×900:45articles, no horizontal-overflow elements. Visually checked representative revised articles including S20/S21/S33 and approval/recap notes. Read all substantive note diffs, including source-only changes; source URLs wrap normally.
- Independently ran main/note lint (OK), wordy/dense checks (no flags), and target/root outline lint (0stale pointers/0warnings). Spot-checked every leaf slide/section starting pointer against its actual stable ID. Root change is count-only.
- Independently validated45 unique matching main/note IDs in order, S27 absent, sequential display headings, every cumulative elapsed timestamp, changed times85/80/115seconds and section sums480/240/880/560/420seconds. Total2580+120=2700seconds. This remains a pacing plan, not a timed rehearsal.
- Eight planner-owned files at the reviewed commit matched working copies byte-for-byte before this review's header update. No evidence or plan amendment is needed.

## Log-only finalization for existing PR82

Copy this frozen `review-r3.md` unchanged into the tracked job record; refresh living job/requests/evidence and push the existing branch. **Every commit after2336d436adcb8ccc4c60c72ab9f64b93d8ebf630 must touch only `log/2026-11-26-261202YonseifutureAI-overview/`.** Return the exact pushed SHA. slides-review will verify that range and refresh **PR82**, not open a new PR.

No additional content change or export delivery is requested. No merge without Albert's direct order for PR82.
