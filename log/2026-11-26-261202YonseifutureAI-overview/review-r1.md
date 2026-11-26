# Round1 review

- Job: `2026-11-26-261202YonseifutureAI-overview`
- Reviewed commit: **731bec116bf1e2b9c8e696f89798aa0b1c6b0178**
- Baseline: **467cf0630d25ec9929c9e1e87cea901224637487**
- ID-only commit verified: **46d0148786037eea7fca1c08b6f5f1e67386214f**
- Verdict: **revise**. F01–F08 block; F09–F10 are nonblocking preferences.
- Next: round2 corrective work under the unchanged plan-v2. Preserve the argument, English language, personal opening and43+2-minute target. No new topic, technical supplement, export delivery, PR or merge is authorized by this review.

## What matters

1. The visual argument works: personal need → delegated authority → concrete failures → practical controls. Keep the authentic opening, dated case labels, genuine paper figures, simple subgroup chart and five-question ending.
2. Essential diagram text repeatedly falls below the design-system body-size floor. This is not a density problem to solve by shrinking: enlarge or simplify the affected labels (F01).
3. The approval example must actually reveal the proposed change, and the security/provenance explanations must not promise more than their controls establish (F02–F04). A few note-only overstatements and missing glyphs are local corrections (F05–F08), not a reason to restructure the talk.

## Coverage of Albert's requests

“Done” records delivered scope, not an overall approval. Findings below still govern acceptance.

| Request | Done? | Where / result |
|---|---|---|
| C01 | Yes | Trustworthy-AI overview framed around delegation and consequences. |
| C02 | Yes | Exact `talks/261202YonseifutureAI/` folder. |
| C03 | Yes | Main HTML plus paired English note HTML;46 matching IDs. |
| C04 | Yes |46 pages; explicit43min pacing plus2min reserve. This is a timing plan, not a measured rehearsal. |
| C05 | Yes | lec01's overview arc retained; no mathematics, algorithms or technical detours. |
| C06 | Yes | E01's fixed-baseline lec02–14 survey reflected in updated examples and distinctions. |
| C07 | Yes, polish pending | Exceptionally high-level content; F01 affects room legibility. |
| C08 | Yes, polish pending | Business consequences and executive questions; F01 affects senior audience fit. |
| C09 | Yes, polish pending | Visual exhibits and sparse main text throughout; F01/F08 need correction. |
| C10 | Yes | Court/tribunal decisions, vendor rollback and reported fraud, clearly separated from research demonstrations. |
| C11 | Yes | Personal workflow immediately after title, before Contents. |
| C12 | Yes | Email-derived private manual S03/S08/S44. |
| C13 | Yes | Vice Dean role, seasonal paperwork and forgetting S02. |
| C14 | Yes | Relevant email, recorded steps and weekly update S03–S04/S44. |
| C15 | Yes | Read/tools, brief injection, possible read+write exposure S05–S07; no claimed attack on Albert. |
| C16 | Yes | Read-only reader → Albert's approval → separate coder S08/S44. F09 would improve the later callback. |
| C17 | Yes, corrections pending | Capability/consequence bridge S09–S14 and later injection/control return S29–S37; F02/F03 concern that return. |
| C18 | Yes | Approved scope implemented; corrections do not reopen the scope approval. |
| C19 | Yes | English main, labels and notes. |

## Findings and self-contained change requests

All locations below refer to the reviewed commit; page numbers equal S-number. Where wording/layout is marked `[judgment]`, slides should resolve it directly. Do not delegate a context-free literal replacement when the surrounding explanation must also change.

### F01 — Core diagram labels are treated as annotations
- **Type:** design rule. **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`; shared rules lines33,45 and affected package rules including94,257,283–290,297,326,346,361–364.
- **Where:** S02–S08; S12–S14; S16–S19; S21,S23–S24,S26–S27; S30–S37; S39–S44. Not every small label on these pages is a violation; the scope is the meaning-bearing text identified below and equivalent primary labels.
- **Current:** `.fa-node .fa-sub` makes explanations20.8px; other primary labels are22.4/23.2px. Examples: S02 Vice Dean role; S07 `reads email + writes code`; S08 `read-only`/`approves`; S16 `cases do not exist`; S17 `one small-claims case`; S26 `prerecorded deepfake` and the amount; S32 the actual requests; S33 broad access/same-user scope; S35 the instruction-propagation row; S37 `fixed rules, outside the model`; S39 job boundary; S42 what the questions mean; S43 the owner questions; S44 recommended checks. S34 explicitly reduces paragraph text to1.45rem.
- **Fix:** apply DS §1 Priority0 and §8's **body-size primary-label floor (1.55rem)** to the content the audience must read to follow the diagram or retain a necessary qualification. Remove the S34 reduced prose override. A smaller sub-label class cannot be the only place stating the security distinction, case scope or recommended action. `[judgment]` Simplify redundant labels or rearrange/split if needed; do not reduce other type or prose rhythm to compensate. This is a semantic sweep of the shared kit, not a demand to enlarge citations, chart ticks, evidence tags or genuinely non-crucial annotations. S25's ticks and S45's redundant category words can remain annotations.
- **Reason:** these are the argument, not ancillary captions; clean lint does not enforce this distinction. Check every slide affected by a shared-style change at1280×720 and in print.

### F02 — “Actual change” still hides the values
- **Type:** unmet request (approved concrete-control specification), also DS no-placeholders. **Blocking:** yes.
- **Files:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S36/p36, line1193; paired `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S36, line460.
- **Current → fix:** `Submission address: current → the email's version` → show two short, explicitly fictional old/new values. For example, `forms@grad.example → forms@outside.example`, with a clear old/new distinction and the existing Illustration label. `[judgment]` Another equally concrete nontechnical pair is fine. Keep this a proposed change reviewed before coding, not an invented existing gate or actual code diff. Update the note to describe the values actually visible.
- **Reason:** a reviewer cannot approve the actual destination when the destination is concealed by a reassuring description. The exhibit currently demonstrates the problem its title warns against. Keep it high-level; no executable code or real address is wanted.

### F03 — File-write scope is not a complete external-send boundary
- **Type:** fact (overstated security inference). **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S37/p37, line475; keep main S37 consistent.
- **Current:** “If the coding agent can only edit my manual page ... cannot make it publish my private notes elsewhere.” File-edit scope alone does not establish that every outward path is blocked; generated page/code can itself have effects when run.
- **Fix `[judgment]`:** tie the guarantee only to the explicitly blocked operation: “The gate rejects a forbidden external-send operation before it runs. Limiting editable files alone is not enough: the system must also limit where tools and generated code can send data.” Then retain the caution that allowed page edits can still be harmful. The main's gate can stay as a recommended, idealized permission boundary, not a claim about Albert's audited implementation. Do not add an implementation/security-architecture lesson.
- **Reason:** the difference between editing one file and enforcing all reachable actions is central to this motivating example. E04/E06 support scoped controls, not an unconditional confidentiality guarantee from file permissions alone.

### F04 — Credentials do not always name the creator
- **Type:** fact. **Blocking:** yes.
- **Files:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S27/p27, line985; `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S27, lines350,353 and limits.
- **Current → fix:** `content credentials: maker, edits` → `content credentials: recorded origin, edits` (or an equally concise qualified label). The note's “who made it” / “it tells you who stands behind the file” must become a conditional explanation: credentials can carry recorded origin/edit information; they need not identify the human creator or contain the full history. Keep the independent truth check and missing-credentials-do-not-prove-fake points.
- **Source:** E24, C2PA Explainer2.2 §§2,7.2.1–7.2.5, especially7.2.4. Add that locator to the note/cite as appropriate.
- **Reason:** the origin-versus-truth distinction is good, but it must not replace one misplaced certainty with another. No cryptographic detail needed.

### F05 — Consent history is not in the cited study
- **Type:** fact. **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S22/p22, line279.
- **Current → fix:** “the person never agreed to have a text generator hand them out on request” → “public availability does not by itself establish consent to this reuse.” Alternatively delete the consent assertion and retain the already supported privacy point.
- **Reason:** E11/E22 establish extraction from public-web training text, not this individual's consent history. Main S22 and its source figure need no factual change.

### F06 — The transition forgets the deepfake fraud
- **Type:** fact/narrative consistency. **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S28–S30/pp28–30, lines368,380,391.
- **Current:** “Everything in this section ... needed no villain”; “So far the failures were mistakes”; “Until now the failures were mistakes.” S26 has just described deliberate fraud, and the opening already introduced an attacker.
- **Fix `[judgment]`:** say that **many** failures need no attacker, then explicitly turn from failure outcomes to attempts to steer the AI. Suggested bridge: “We have seen ordinary failures and deliberate deception. Now we focus on people manipulating the AI system itself.” Preserve the useful mistakes/attacks comparison and the existing section order.
- **Reason:** a coherent executive mental model matters more than a falsely tidy transition. Do not move or remove the Hong Kong case.

### F07 — Describe the stop-sign test positively and accurately
- **Type:** fact. **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`, S30/p30, line391 (separate from F06's opening phrase).
- **Current → fix:** “not on a car on the road, and nobody was hurt” → “These were classifier tests using lab images and camera footage captured in drive-by tests, not a reported crash or a demonstration against a deployed autonomous-driving system.” Compress to natural speaking prose as needed.
- **Reason:** E17/E23 include a moving vehicle in the field test. The source supports the test setting, not the added independent no-injury assertion. Main S30's “Lab and drive-by tests, not a car crash” is already suitable.

### F08 — Cross symbols render as missing-glyph boxes
- **Type:** design rule/render defect. **Blocking:** yes.
- **File:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S20/p20 lines804–806 (`✗`), S39/p39 line1254 (`✕`).
- **Fix:** replace these with a reliably rendered cross/icon, or remove the redundant symbol while retaining `still open` and `Not in this job`. Keep the no/yes meaning legible without relying solely on colour. Check the replacement in settled browser view and print; do not change shared fonts/reference files.
- **Reason:** both live Chromium and print show empty red boxes, not the intended marks.

### F09 — Keep approval visible in the propagation callback
- **Type:** preference. **Blocking:** no.
- **Files:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S35/p35 line1166; paired note S35 lines447–450. S34/p34 line1147 is an optional matching callback.
- **Suggestion `[judgment]`:** `Summary / for my approval` → `Approved summary / by me`, or another compact visual that explicitly retains Albert's gate before the coder. Explain that a misleading instruction can survive even a human review, rather than drawing an apparently direct unapproved handoff. S34 can say `via my approval + coder` if it remains readable.
- **Reason:** the opening and closing accurately show approval; preserving that control in the middle makes the residual-risk explanation harder to misread. Current note/context already states approval, so this is not grounds for another round.

### F10 — Let the chart title name what is shown
- **Type:** preference. **Blocking:** no.
- **Files:** `talks/261202YonseifutureAI/261202YonseifutureAI.html`, S25/p25 line912; paired note heading S25.
- **Decision on work-r1 issue3:** prefer the offered **“One System, Very Unequal Errors”** over “Average Accuracy Hid Unequal Errors”. Keep the four bars; keep overall12.1% in the note rather than adding another bar.
- **Reason:** the chart visibly demonstrates the subgroup spread, not an average-accuracy comparison. This is a title refinement, not a data correction.

## Decisions on work-r1 plan issues and deviations

1. **S17 policy paraphrase accepted.** E08 decision paras2/5 explicitly state the retroactive-claim restriction. Retain the paraphrase label and case-specific scope.
2. **S43 tribunal paraphrase accepted.** Paras27–31 support the airline's responsibility for its website information. The note correctly disclaims a global legal rule and an established LLM architecture.
3. **S25:** F10 above. No new statistic or chart is requested.
4. **S19 “After release” accepted.** No invented first-observation date; release/rollback/publication dates remain attributed to the vendor reports.
5. **S30 Speed Limit45 not required.** Verified in E23, but the existing qualitative outcome is sufficient at this level. Correct only the inaccurate note scope in F07, plus typography F01.
6. **S33 actual confirmation mode remains unspecified.** Correct not to invent it. The note already explains the general per-action/Always Allow distinction without asserting which mode this demo used; keep that distinction.
7. **S24 predicting cost, not an unqualified “accurate” claim, accepted.** Preserve the proxy-versus-need explanation and same-score finding.
8. **S10 “Contents” and no invented S01 event pill accepted.** Four section names agree. No plan-v3 is needed: no change to required scope, facts, argument or teaching-time allocation is authorized here beyond correcting implementation to the evidence and existing requirements.

## Verification performed by slides-review

- Read exact git objects and extracted the named commit with `git archive`; no working-tree/main review. Diff against the fixed baseline touches only the new talk, root outline and this job's tracked record (12files). Verified the paired ID commit changes attributes only. The four frozen/current planner files requests/evidence/plan-v1/plan-v2 match the working copies byte-for-byte before this review's appended evidence.
- Read all46 main slides and all46 note articles, original requests first, then sources/design/plan. All IDs unique and paired in order. Note times sum2580seconds; reserve120seconds gives45minutes.
- Independently rendered all46 pages at1280×720 with Chromium, waited for transitions to settle, visually inspected all settled screen and print pages. Print has46pages. No off-slide geometry, body/footer collisions or clipped source-figure edges found. F01 and F08 remain despite otherwise clean composition.
- Tested notes at1280 and430px through device emulation;46articles, no horizontally overflowing elements. Visually checked representative notes including1,8,25,30,37,44. They remain plain accessible speaker documents, not a technical course.
- Independently ran both target `lint-deck.py` checks (OK), `find-wordy.py` and `find-dense.py` (no flags). Target/root outlines pass. Whole-repo outline lint in the archive finds one **pre-existing, unchanged** environment-specific absolute pointer to `/workspace/agent/lec09/r4/build_deck.py` plus5 basename warnings; not introduced by this job and not a request to edit that course outline. This explains the difference from the executor's0-stale result in its own environment.
- Rechecked public-case scope, C2PA identity limits, Eykholt Fig1/field setting and the exact IBM Table4 row. Independently regenerated the Carlini crop (byte-identical) and compared the Eykholt asset to the course/source figure. E21–E24 record provenance and limits; no source data were repainted.

## Round2 handoff

Resolve F01–F08; disposition F09–F10 at slides' judgment. Update affected paired notes/outlines and give an exact new SHA plus `work-r2.md` with each finding's disposition and all pages affected by shared-style changes. Copy this frozen review unchanged and refresh living job/evidence/requests records at push. Next review will cover changed slides and their neighbours, including every page affected by a shared CSS change; no unrelated cleanup. This is round1 of the three-round review limit.
