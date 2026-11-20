# lec13 clarity — review round 1

- **Reviewed commit:** `06678b4f01df7519d33f6f21e7d1d5025ae93559` (not the working tree).
- **Baseline:** `9effc8ab67589f2d7e5789f04db5e92067ff46d9`.
- **Verdict:** **revise**. Round 2 is the final medium-job round.
- **Work order:** implement blocking F01–F09 below, under plan-v2.md. Preserve already accepted content. Every applicable correction includes the matching note's Message, explanation and details; report ID/page mapping after any splits.

## What matters most

1. The running email example, direct/indirect distinction, incident narration, conference probe and mechanism-before-result sequence are much clearer. Keep them.
2. Correct the CaMeL figure interpretation and the authorization/approval contradiction. The former also corrects my v1 plan, not just the implementation.
3. The requested diagrams are larger, but important explanatory labels still use the secondary-label size. Fix actual essential labels, not only box headings. Repair the duplicated OUTLINE section before handoff.

## Coverage of Albert's request

“Done” means the substantive request is answered on slide and in its note, subject to the global design fixes below. Original pages refer to the baseline; revised pages refer to the reviewed commit.

| Comment | Revised IDs/pages | Status |
|---|---|---|
| C00 updated rules, slide + note clarity, PR | entire deck | Not yet: F01–F09; PR after approval |
| C01 agents reading many sources | S01/S04, 1/4 | Done; opening definition consistency F07 |
| C02 detailed email motivation | S05a/b, 5–6 | Done |
| C03 direct injection vs email | S06/S07a/b, 7–9 | Done: attacker may be app user; email is indirect |
| C04 why priority matters | S08, 10 | Done: conflicting authors vs action permission |
| C05 hidden author text and organizer probe | S09a/b, 11–12 | Done: ICLR statement; ICML two-phrase probe, manual check and limits |
| C06 old p16's point | S16, 19 | Done: notes may choose a file, not add a recipient; glyph F09 |
| C07 vendor/service provider | S20/S21b, 23/25 | Done: provider defined, four distinct evidence questions |
| C08 larger old p22 diagram | S22, 26 | Not yet: essential bypass labels F03 |
| C09 what happened in EchoLeak | S21a/b, 24–25 | Done: email retrieval → answer image → automatic request; historical provider status |
| C10 same-user repos | S23, 27 | Done: yes in demo; not a necessary general condition |
| C11 larger old p24 diagram | S24, 28 | Not yet: essential step text F03 |
| C12 larger old p26 diagram | S26, 30 | Not yet: status/retest reading labels F03 |
| C13 priority/ranking + diagram | S29, 33 | Explanation done; label size F03 |
| C14 escaping/delimiters and limit | S31a/b, 35–36 | Not yet: parser-vs-model scope F06 |
| C15 repeat prompt | S54, 45 | Done before its results |
| C16 sandwiching, Prompt Guard, MELON | S54/S55/S56, 45/48/49 | Mechanisms done before results; essential diagram labels F03 |
| C17 old p44 detail + size | S44a/b, 53–54 | Explanation substantially done; decision labels F03 and approval condition F02 |
| C18 old p47 expanded | S47a/b/c, 57–59 | Three slides delivered; correct approval claim F02 |
| C19 when/what to ask | S48, 60 | Strong three-tier design; authority assumption F02 still needed |

## Findings and self-contained changes

All paths below are repo-relative. Line numbers are for the reviewed commit, not instructions to patch a moving tree. Numbered IDs continue across rounds.

### F01 — CaMeL figure is not its architecture [judgment]
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:1562–1578`, S43 / revised p52; `courses/trustworthy-ai/lec13-prompt-injection-note.html:1172` and the rest of S43.
- **Type / blocking:** fact / **yes**.
- **Wrong:** the Fig. 1 key calls the red dashed boundary “the program it writes” and the extraction steps “quarantined LLM.” Fig. 1 introduces generic agent control/data flow and its vulnerability; it does not depict those CaMeL components. It also remains a small figure whose labels cannot carry this explanation.
- **Fix:** implement plan-v2's S43 with CaMeL **Fig. 5**, the actual architecture. Explain trusted request/configuration → P-LLM program; interpreter → policy-checked calls; Q-LLM parses untrusted data without tools. Preserve the important qualification that runtime data can affect arguments/branches. Use faithful source crops/sequential views if necessary. If keeping Fig. 1 in notes, label it the motivating problem, not the CaMeL implementation. Proposed title: “CaMeL Separates Planning, Parsing and Enforcement.”
- **Why:** an accurate reading key must describe what the source figure actually shows. E21 corrects my v1 exhibit choice.

### F02 — Approval can authorize only a permitted exception [judgment]
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:1615–1654,1792–1850`, S44b / p54, S47c / p59, S48 / p60; note S44b/S47c/S48, especially lines 1333–1339 and 1360 onward.
- **Type / blocking:** fact / **yes**.
- **Wrong:** p59 says neither detection nor approval sets authorization; p60 then offers “Share once.” That example never states the person has authority to share the file. “Only you can make it” in the note would be false for a user with read-only access or a non-overridable organization restriction.
- **Fix:** p59 current “Neither is a hard guarantee; neither sets what is authorized” → “A detector grants no authority. Approval may authorize a policy-permitted exception.” Retain fallibility in the diagram/note. On p60 explicitly assume **you are authorized to share this file and policy permits this exception**; otherwise deny, do not offer Share once. On p54 qualify escalation the same way. Keep routine proceed / forbidden deny / consequential exception ask and system-record-based facts.
- **Also:** S48 note “A prompt at every tool call trains people … Invariant saw exactly that” → repeated prompts *can encourage* blanket approval; Invariant reports “Always Allow,” not a controlled causal study.
- **Why:** meaningful approval is delegated authorization, not a way for any user to override a prohibition. E19 already carries this condition.

### F03 — Essential diagram text still uses secondary sizes [judgment]
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html`, especially S22 / p26 `:627–684`, S24 / p28 `:730–765`, S26 / p30 `:816–856`, S29 / p33 `:893–939`, S56 / p49 `:1405–1448`, S44b / p54 `:1615–1654`, S47a / p57 `:1726–1769`, S47c / p59 `:1792–1826`. Also source-figure reading keys on S37 / p42 `:1166` and S39 / p44 `:1200`.
- **Type / blocking:** design rule / **yes**; directly C08/C11/C12/C13/C17.
- **Wrong:** larger headings do not fix smaller text needed to follow the argument. Examples in the 1280×720 render: S22 “missed: email worded for a human” at 21; S24 “private data inside” at 21; S29 “may still obey 3” and “send: denied” at 21; S56 proposed actions at 23; S44b the added outsider/forbidden-file reasons at 22; S47a “reads text; no tools” at 21. S26 status labels are also below body size. These are not ticks or incidental source tags. The model legend in S37 and evaluation labels in S39 remain difficult to read in their source-image layouts.
- **Fix:** apply DS §8's distinction: **primary labels and text inside mechanism boxes are body-size**, secondary size is for ticks/legend notes/source tags. Simplify wording, use more width, or split explanatory steps; do not enlarge every annotation blindly. Check the other revised flow diagrams for the same issue. For the source plots, enlarge/crop faithfully or add readable outside keys identifying the exact plotted items discussed (e.g. GPT-4o); do not repaint source data. Keep the source figure and explanation readable together.
- **Why:** these phrases are the answers Albert asked to understand from the back of the room. In round 2 report actual final-size render checks, not only SVG font-size attributes.

### F04 — OUTLINE contains duplicated lectures and misplaced lec11 material
- **Where:** `courses/trustworthy-ai/OUTLINE.md:610–811`; shared surface, not a slide.
- **Type / blocking:** design rule / **yes**.
- **Wrong:** the new lec13 section is followed by lec11 rebuild/note/tech text at 656–676, a second lec12 section at 678, and a second lec13 section at 755. The latter also has stale figure metadata. A passing pointer lint did not detect duplicate semantic sections.
- **Fix:** retain **one** complete, updated lec13 section. Remove the accidental copied block, restore unaffected lec11/lec12 sections exactly as at the baseline, and keep lec13's correct note/tech metadata. Update figure inventory, slide IDs/counts and final line pointers after the other revisions. Verify heading uniqueness and inspect the baseline diff, not just the line-number linter.
- **Why:** the continuity map currently assigns content to the wrong lecture and contains conflicting deck records.

### F05 — Authorized email trace must still read the tool result
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:370`, S13 / p16; `courses/trustworthy-ai/lec13-prompt-injection-note.html:342,348` and “Expected authorized path” in that article.
- **Type / blocking:** fact / **yes**.
- **Current → new:** “Authorized path: 1 → 2 → 5” → **“Authorized path: 1 → 2 → 3 → 5; skip the send.”** Likewise change “step 2 → step 5” to “step 2 → step 3 → step 5.”
- **Why:** step 3 is the inbox result needed for the authorized summary. The right distinction is reading it without obeying the added instruction, not bypassing the data.

### F06 — Escaping needs a syntax, not a promise about model behavior [judgment]
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:984–1004`, S31a / p35; corresponding note Message, Reading, Script and SQL comparison.
- **Type / blocking:** fact / **yes**.
- **Wrong:** “Escaping stops the email faking </email>” presents an unconditional guarantee in an LLM prompt. The escaped quote example is also shown without naming its format.
- **Fix:** label the quote example **JSON string** (or another explicitly defined format). Replace the unconditional delimiter claim with “Encode marker characters as literal data; the model must still respect the boundary.” In the note explain that a format-aware serializer/parser preserves a syntactic boundary, while text markers presented to an LLM are not an enforced parse/authority boundary. Replace “choosing markers the sender cannot reproduce, prevents that” with a qualified explanation; do not claim secret markers force model compliance. Retain the separate parameterized-SQL distinction and S31b's successful inside-the-markers example.
- **Why:** C14 asks precisely why marking helps but is insufficient; do not teach parser guarantees as model guarantees.

### F07 — Opening definition accidentally excludes direct injection
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection-note.html:36`, S01 / p1 Message and Script.
- **Type / blocking:** fact / **yes**.
- **Current → new:** replace the general definition “text written by someone other than the user … steering what the agent does” with **“Prompt injection tries to make lower-trust text override the instructions it should follow. We begin with indirect injection: an outsider's email steering the user's agent.”** Keep the many-author motivation.
- **Why:** the app's own user is the attacker in the correct S07a direct-injection example.

### F08 — Do not invent the clean-trial aggregation for AgentDojo Table 5
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:1305`, S40a / p46; note S34 / p39 `:842`, S40a / p46 `:1022`; `courses/trustworthy-ai/figs/lec13-clarity/p5-bars.py:7–8`.
- **Type / blocking:** fact / **yes**.
- **Wrong:** “clean utility over 97 user tasks” is attached as an exact experimental denominator to Table 5's percentages. The paper defines benign utility over user tasks, but the printed percentages/intervals do not resolve their aggregation; the checked code snapshot does not resolve the older published numbers either. See E22; do not substitute 629 as a guessed clean denominator.
- **Fix:** cite **“AgentDojo Table 5; GPT-4o; fixed attack; 629 security cases”**, retaining the separate benchmark description of **97 distinct tasks**. In the note add E22's short aggregation caveat; keep clean utility's conceptual definition and every source table value unchanged. Correct the generator documentation to match. This finding does not change the separate CaMeL/Nasr experiment denominators.
- **Why:** precise-looking metadata should not claim a stronger reconstruction than the source supports.

### F09 — Failed cross glyphs obscure negative decisions
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:455,973,1047,1638,1648,1780`, S16 / p19, S30 / p34, S31b / p36, S44b / p54, S47b / p58.
- **Type / blocking:** design rule / **yes**.
- **Wrong:** the ✗ characters render as missing-glyph boxes in the independent Chromium render, including the standalone failed checks in S44b.
- **Fix:** use supported, unambiguous negative labels (e.g. “No” in check columns, “Denied” or “Wrong” where appropriate), or a verified graphic mark. Check all six occurrences in the final render. Keep positive/negative decisions understandable without color alone.
- **Why:** the policy walkthrough depends on immediately reading which check failed.

## Plan issues and decisions

- **Plan correction:** v2 replaces the incorrect Fig. 1 instruction with Fig. 5 (F01). It also makes the already-required approval-authority and escaping scope explicit; no new argument or literature survey.
- **Accepted:** 65 pages as explanatory splits, three new mechanism slides, MELON's illustrative mechanism rather than a tiny source crop, selected Table 7 rows, version-unspecified Prompt Guard, and distinguishing AgentDojo's ProtectAI detector. Preserve those choices.
- **Pacing accepted:** 81.5 minutes plus 8.5-minute flexible explanation/question buffer, not an added exercise. Round-2 readability splits must remain within 90 minutes and update note elapsed times. Relabel the pacing row as a buffer if useful; this is not a separate blocking finding.
- **Date issue resolved:** E05 already distinguishes the ICML post's March 18 publication and March 26 update. March 18 in the source citation is fine; no evidence correction required.
- **Source register:** E21 corrects the CaMeL figure choice; E22 records the AgentDojo aggregation uncertainty; E23 records generated chart inputs and reproduction parameters.

## Checks and handoff acceptance

- Independently archived and rendered the exact reviewed commit at 1280×720; inspected all 65 main pages, not a moving tree. All main/note IDs match in order and are unique; main/note counts are both 65. No element outside slide bounds in the DOM check, but that does not certify type or internal overlaps.
- Notes checked at 430-pixel viewport: no horizontal article overflow. Reviewed the changed explanations and source/slide consistency; the findings above apply to every note layer, not only the visible slide sentence.
- Independent `lint-deck.py` passes main, note and tech. Tech diff is only the correct addition of trusted tool signatures to the planner input.
- Archive `outline-lint.py` reports a pre-existing lec09 external script path unavailable in this scratch environment; not attributed to this job. Its semantic duplicate problem is independently visible in the OUTLINE diff.
- Source checks: original primary incident/conference records from E01–E20, pinned research versions, CaMeL figure captions, and targeted AgentDojo source/code check. Reported chart inputs match pinned tables; discrepancies are explicitly retained rather than silently “corrected.”
- **Round 2:** report F01–F09 individually, actual slide mappings and affected renders; refresh living files and copy plan-v2/review-r1 unchanged. I will recheck only changed slides and their neighbours, plus relevant notes, figure metadata and OUTLINE. If blocking findings remain at that point, the medium-job limit requires escalation to Albert rather than a third implementation round.
