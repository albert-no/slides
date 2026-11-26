# Round2 review

- Job: `2026-11-26-261202YonseifutureAI-overview`
- Reviewed commit: **07f519cec547faa37cba901c8f5f0da07125360d**
- Previous reviewed commit: **731bec116bf1e2b9c8e696f89798aa0b1c6b0178**
- Baseline: **467cf0630d25ec9929c9e1e87cea901224637487**
- Verdict: **approved**. All eight blocking findings closed; both preferences dispositioned. No new findings.
- Round: **2 of 3**. Approval is pinned to the exact commit above, not a moving branch.

## Result

The larger primary labels remain legible without crowding. The opening and closing retain Albert's actual approval workflow, while the later examples now distinguish it clearly from recommended extra checks. The concrete address-change exhibit and qualified security/provenance explanations resolve the substantive concerns without adding technical detail. Preserve the argument, case selection, diagrams and five-question ending.

## Coverage of Albert's requests

Coverage accepted in round1 remains intact; the affected requirements have been rechecked against the corrections.

| Request | Done? | Where / result |
|---|---|---|
| C01 | Yes | Trustworthy-AI overview centered on delegation and consequences. |
| C02 | Yes | Exact `talks/261202YonseifutureAI/` folder. |
| C03 | Yes | Main HTML and paired note HTML; 46 unique matching IDs. |
| C04 | Yes | 46 slides; 43 minutes of planned speaking plus 2 minutes reserve. |
| C05 | Yes | lec01 overview spine; no mathematics, algorithms or technical detours. |
| C06 | Yes | Fixed-baseline lec02–14 survey and selected updates remain traceable in E01 and notes. |
| C07 | Yes | Exceptionally high-level concepts; primary labels now meet the body-size floor. |
| C08 | Yes | Executive consequences and questions; readable concept-first exhibits. |
| C09 | Yes | Diagram-led, sparse main text; corrected label sizes and cross icons. |
| C10 | Yes | Dated real cases, with incident/vendor/research/illustration distinctions retained. |
| C11 | Yes | Personal agent story before Contents. |
| C12 | Yes | Email-derived private webpage manual, S03/S08/S44. |
| C13 | Yes | Vice Dean role, seasonal paperwork and forgetting, S02. |
| C14 | Yes | Relevant email, recorded steps and weekly updates, S03–S04/S44. |
| C15 | Yes | Brief injection example and possible read/write exposure, S05–S07; no invented attack on Albert. |
| C16 | Yes | Read-only reader → Albert's approval → separate coder; approval also visible in S35's residual-risk callback. |
| C17 | Yes | Capability/consequence bridge and later injection/control return; actual change visible, controls accurately qualified. |
| C18 | Yes | Approved scope and timing retained; no renewed scope gate needed. |
| C19 | Yes | English main and notes throughout. |

## Finding dispositions

Paths are relative to `talks/261202YonseifutureAI/`; main = `261202YonseifutureAI.html`, notes = `261202YonseifutureAI-note.html`. Page numbers equal stable S-number. No open blocking or preference finding remains.

| ID | Slide ID / page and file | Type | Blocking in r1? | Verified resolution |
|---|---|---|---|---|
| F01 | Shared main styles; affected S02–S08, S12–S14, S16–S21, S23–S28, S30–S37, S39–S45 | Design rule | Yes — closed | Primary diagram labels are at least 1.55rem; S34 reduced prose override removed. Layout changes accommodate the larger text. Only evidence tags and S25 axis ticks remain below that floor in the diagram-label audit. No compensating type shrink, overflow or collision found. |
| F02 | S36/p36, main and notes | Unmet request | Yes — closed | Visible fictional `forms@grad.example` → `forms@outside.example`, old value struck through. Note matches the exhibit and identifies both values as invented; recommended pre-coding check remains distinct from current setup. |
| F03 | S37/p37, notes; main consistency | Fact | Yes — closed | Claim now concerns the forbidden operation rejected by the gate. Explicitly states file-edit scope alone is insufficient and tool/generated-code destinations also need limits. Residual harms from permitted actions remain. |
| F04 | S27/p27, main and notes | Fact | Yes — closed | Recorded origin/edits, not unconditional creator identity. Notes retain optional identity/incomplete history, separate truth check and missing-credentials limits; E24/§7.2.4 cited. |
| F05 | S22/p22, notes | Fact | Yes — closed | Unsupported individual consent history removed; public availability does not itself establish consent to reuse. |
| F06 | S28–S30/pp28–30, notes | Fact/narrative consistency | Yes — closed | Many failures need no attacker; deliberate deepfake deception acknowledged before focus turns to steering AI. No false claim that all preceding failures were mistakes. |
| F07 | S30/p30, notes | Fact | Yes — closed | Describes lab images and camera footage from drive-by classifier tests, not a deployed autonomous-driving crash. Unsupported no-injury assertion removed. |
| F08 | S20/p20 and S39/p39, main | Design rule/render defect | Yes — closed | Inline SVG crosses render correctly in settled screen and print views; explanatory words retained. |
| F09 | S35/p35, main and notes; optional S34 callback | Preference | No — resolved | Approved summary / by me and human-review limits adopted. Retaining S34's shorter coding-agent wording is accepted; approval is explicit on the next page and in the opening/closing. |
| F10 | S25/p25, main, notes and leaf outline | Preference | No — resolved | “One System, Very Unequal Errors” adopted. Four data bars unchanged; overall 12.1% remains note-only. |

## Verification performed by slides-review

- Read exact git objects and the r1→r2 diff; rendered an extraction made with `git archive` of the named r2 commit. The seven changed files are the two target HTMLs, target leaf outline and this job's logs. Figures, shared reference files, scripts and unrelated decks are unchanged. Root outline is unchanged from its accepted round1 state.
- Rechecked changed slides and neighbours, plus every slide affected by shared styles. Their union covers all 46 pages: visually inspected settled 1280×720 browser views and all 46 print pages. No off-slide geometry, overlap, clipped primary labels or missing cross glyphs found. The print output is 46 pages, 960×540 pt.
- Browser geometry/label audit found no off-viewport elements. Core `.fa-*` labels meet 24.8px at the deck's base scale; remaining smaller evidence tags/chart ticks are ancillary, not hidden primary explanations. Source citations and standard footer are not subject to that primary-label test.
- Rechecked the changed note articles S22, S25, S27–S30 and S35–S37 against E21–E24 and the already verified source limits. The corrected text does not introduce new factual claims requiring a new evidence entry. Source figures and chart values remain unchanged from the verified round1 assets/data.
- Tested notes at 1280×900 and 430×900: 46 articles and no horizontal overflow. Inspected changed article captures at both widths; repeated S36 at 430px after scroll settlement to confirm clean text. Notes remain accessible speaking support, not a technical supplement.
- Independently reran main/note lint (OK), wordy/dense checks (no flags) and target leaf-outline checks (no warnings). The known pre-existing whole-repo outline issue in the review container is unchanged and outside this job.
- 46 unique main IDs match 46 note IDs in order. Pacing remains 2580 seconds plus 120 seconds reserve. This is a checked timing plan, not a measured 45-minute rehearsal.
- Frozen planner records and current requests/evidence at the reviewed commit match the working copies byte-for-byte before this review and header update. No plan change is needed; work-r2 raises no new plan issue.

## Finalization handoff

Copy this frozen `review-r2.md` unchanged into `log/2026-11-26-261202YonseifutureAI-overview/`, refresh the living `job.md`, `requests.md` and `evidence.md`, and push the job branch. Every commit after the approved SHA must touch **only that job-log directory**. Return the exact pushed SHA with the job-file pointer; slides-review will verify the log-only range and open the PR against `main`.

No additional content change, export delivery or merge is authorized. Albert remains the final check; no merge without his direct order for that PR.
