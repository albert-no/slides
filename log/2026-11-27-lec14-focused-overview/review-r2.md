# Review r2

- Job: `2026-11-27-lec14-focused-overview`
- Reviewed commit: **`c16c37a5faaafe8890f11301fea1a0a97a78725b`**.
- Comparison: r1 `1d4493167f41a5d39237fe4e1703e40f94fdfe40`; frozen job baseline remains `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`.
- Verdict: **revise**. Round2/3 reviewed; `plan-v5.md` and the two findings below are the narrow final-round work order.

## Result
The lecture changes are largely ready: clearer outcome definitions, a focused main story, properly preserved optional studies and no narrow-note overflow. **The blocking regression is the leaf OUTLINE: r2 deletes 653 lines, including the course continuity map and many lecture sections.** Restore that before a PR. One small S75b role clarification also remains; do not redesign the lecture again.

## Prior findings
| ID | Status | Verification |
|---|---|---|
| F01 | Closed | S69b shows coherence exclusion; S70 uses the free-form subplot with a correct retained-answer key; complete panel a preserved in S91 with separate outcome keys. |
| F02 | Closed for focus/preservation | S72b is no longer a literature catalogue; S75b explains one recovery experiment. S95/S91–S94 are actual backup slides with paired notes and citations. F10 is a new local wording issue, not a reopening of the structure. |
| F03 | Closed | S78/S45 visible descriptions and S45 notes use caught-or-successful outcomes and explain excluded inconclusive attempts. |
| F04 | Closed | S74b has a visible metric; 3 epochs is accurate and defined in notes. Values unchanged. |
| F05 | Closed | “No expert check” now belongs only to the bypass branch; audited-clean code enters the neutral submit node. |
| F06 | Closed | Independent **430px** device emulation: both note documents have layout/scroll widths **415/415px**, no broken images. No font shrinking. |
| F07 | Taken, closed | Both crosses render correctly on S59/S76. |
| F08 | Taken, closed | S71 names subliminal learning once in plain language. |

## Request coverage
| Request | Status |
|---|---|
| C01 confusion | Done except local F10 wording. |
| C02 introduction/context | Done: stepwise core experiments; optional studies now have context. |
| C03 fewer important main results | Done. Extra preprints are optional B6, not core headlines. |
| C04 subliminal learning / Askin | Done. |
| C05 friendliness | Done in the inspected revised slides/notes. |
| C06 high-level setup/solution/message | Done except F10's teacher/learner wording. |
| C07 checked references | Done with E26 clarification to apply. |
| C08 removed material in actual backup | Done:52 backup slides with52 paired articles. |
| C09 more slides, not compression | Done:59 main teaching steps retained. |
| C10 go ahead | Done; approved scope/time unchanged. |
| C11 redundancy against lec01–13 | Content audit/adaptation done, but the accidental deletion of the continuity map must be repaired (F09). |

## New findings
| ID | Slide ID / page | Type | Blocking | Problem → fix |
|---|---|---|---|---|
| F09 | Shared leaf OUTLINE; no slide page | unmet request | **Yes** | Unrelated course-map sections deleted, target heading malformed → restore exact r1 material and reapply only authorized lec14 updates. |
| F10 | S75b / main40 | fact | **Yes** | Shared “all its outputs kept” wording implies teacher-written training across all routes → say no extra filtering, while retaining learner-written OPD trajectories. |

### 1. F09 — restore the course outline, not just its remaining pointers
- **Where:** `courses/trustworthy-ai/OUTLINE.md`, r2 **L96 onward**. The large diff hunk is r1 L96–758 → r2 L96–125; old file1189 lines, new556. Net diff **20 insertions / 653 deletions**.
- **What is wrong:** the backup-table row ends inside an unfinished inline reference to `## backup-lec14-agentic-threats.html`, then jumps directly into that section's body. The intervening table rows, historical/continuity material and detailed lecture sections disappear. Missing actual headings include `## Cross-folder reuse`, `## lec01-introduction.html`, `## lec08-adversarial.html` through `## lec14-agentic-threats.html`, and `## backup-lec14-agentic-threats.html` itself. This is not an authorized lec14 refresh.
- **Precise fix:** restore the full file from exact r1 `1d4493167f41a5d39237fe4e1703e40f94fdfe40`, then reapply only the intended lec14 table/count/ID updates, the actual `## lec14-agentic-threats.html` section's new pointers/content, and the actual `## backup-lec14-agentic-threats.html` section's B6/52-slide update. Preserve unrelated sections and table rows byte-for-byte. Close the backup-table row and retain real standalone Markdown headings for both target sections.
- **Acceptance:** r1→r3 outline diff is limited to lec14-related entries/sections. Every pre-existing unrelated section survives; target headings remain actual headings. Check both section presence and pointer accuracy. A “0 stale pointers” lint result is insufficient when the sections containing the pointers have been deleted.
- **Why:** the outline is the course's canonical continuity/index record (DS§10), and this task explicitly excludes changes to the earlier lectures.

### 2. F10 — keep teacher and learner roles correct in the recovery example [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S75b **p40**, L1233 alt text and L1245 diagram text; matching `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S75b L848–878, especially Message L851 and Script L855–856. Related provenance: `courses/trustworthy-ai/figs/lec14-focused-overview/p2b-PROVENANCE.md`, L22.
- **Current → new:** diagram “all its outputs kept” → **“without extra filtering”**. Use the same route-neutral meaning in alt text and the note Message. The paper retains training trajectories; it does not make all of them teacher-written.
- **Note correction:** replace “Nothing is filtered: the teacher is aligned, so all of its outputs are kept” with **“The recovery experiment adds no misalignment filtering to its training examples. In the teacher-scored route, the learner still writes the answers and the aligned teacher supplies token scores.”** Keep the paper's other routes in Setup details. “All three training routes we have seen” → “all three training routes tested in the paper”; full-distribution matching was intentionally not taught as a main method.
- **Provenance:** replace the same ambiguous “all outputs kept” shorthand with “training trajectories retained without additional filtering”. No values, diagrams beyond the label, models or pacing need changing.
- **Why:** this section's central insight is that teacher influence need not arrive as teacher-written text. The recovery example must not accidentally undo that distinction.
- **Source:** E26; [Askin v2](https://arxiv.org/html/2605.12798v2), §4/§4.2 and Appendix E.3. OPD still explicitly includes student rollout generation; the bounded recovery result itself is supported and accepted.

## Decisions on work-r2 questions
1. **Accept S69b at2.25min.** My v4 “retain1.5” line was a transcription error relative to v3's redistribution. v5 corrects it. Do not change85+5 total or reassign0.75min.
2. **Accept S92 title with “Model”.** It better describes the exhibit. No title reversal.
3. **Accept the unmodified S91 source figure.** Separate external left/right keys and the qualifier distinguish operational outcomes; no source-pixel editing needed despite the source's shared generic axis wording.
4. **Accept the S72b height change.** Type remains unchanged and the revised render clears the footer/citation.
5. **430px check completed independently.** F06 is closed; no need to solve a browser-window minimum merely to repeat the result.

## Review evidence and limits
- Reviewed only r1→r2 changes and neighbours, as contracted. Exact commit archived in reviewer scratch; no deck or source edits by reviewer.
- Independently rendered **25 main pages**:14–16,28–34,37–41,43–45,49–51,54–57; **14 backup pages**:1–3,41–43,45–52. Visually inspected all resulting sheets. No outer overflow or broken glyph found on those pages; the new backup charts and keys are readable at the checked slide size.
- Main59/notes59; backup52/notes52; **111 distinct IDs**, paired order matches. Main note times sum85.0min, plus5 flexible. Backup adds0 core minutes.
- Checked changed main note layers and all new B6 note articles; verified optional figures' source/model/trait scope against primary texts. The qualitative cross-model/preference results and the mitigation safety limitation are retained; critique is explicitly under revision, not taught as a debunking.
- Main and backup narrow notes:430px viewport,415px layout and415px scroll width, no broken images. Verified F06 rather than accepting the executor's485px check as equivalent.
- Existing main slide IDs/order unchanged; original backup material and closer preserved around the B6 addition. No technical-deck changes in r2.
- `review-r1.md`, `plan-v4.md`, `requests.md` and `evidence.md` at r2 are byte-identical to the announced working files before this review's E26 append. The new job header will need refreshing as usual.

## Final-round handoff
Apply only F09/F10 and v5's timing clarification. Keep accepted slides, figures,59/52 counts and85+5 pacing. Return `work-r3.md` with both finding dispositions, a structural outline-preservation check and exact pushed SHA. Re-render S75b/its neighbours and its narrow note after the wording fix; no broad new full-deck pass. This is the last allowed review round; any remaining blocker then goes to Albert rather than another round. No PR or merge authorization.
