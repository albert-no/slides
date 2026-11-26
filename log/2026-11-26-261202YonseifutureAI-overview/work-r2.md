# work-r2 — 2026-11-26-261202YonseifutureAI-overview

- **Branch:** `2026-11-26-261202YonseifutureAI-overview`. Previous pushed head `731bec1` (work-r1); `733978d` is a log-only commit (job.md copy).
- **Head:** the commit named in the pointer. It contains this file, an unchanged copy of `review-r1.md`, and refreshed copies of `job.md`, `requests.md` and `evidence.md`.
- **Scope:** corrections under plan-v2 only. No change to the argument, section order, slide count (46), timing (43:00 + 2:00) or language.

## Findings

| ID | Disposition | Where | What changed |
|---|---|---|---|
| F01 | Fixed | shared CSS; layouts S03, S08, S16, S17, S18, S44 | Every diagram-label rule in the `.fa-*` kit and the package blocks (p1–p5, yi-) is now 1.55rem. The S34 `.p3-mail` reduced overrides are removed (the email now inherits the kit size). `.yi-k` (S45 keywords) 1.3 → 1.55rem. Only `.fa-tag` evidence tags (1.25rem) and the S25 axis ticks `.p5-axis span` (1.25rem) stay below 1.55rem, as the DS §8 tick/tag exception allows. Layouts adjusted so nothing wraps or crowds; no type was shrunk (see below). |
| F02 | Fixed | S36 main and note | The Change row now shows `forms@grad.example` (struck through) → `forms@outside.example` (red dashed), sub-label "where students submit forms". Illustration tag kept. Note describes the visible values and says both are invented. |
| F03 | Fixed | S37 note | The "cannot make it publish my private notes" sentence is replaced: the gate rejects a forbidden external-send operation before it runs; limiting editable files is not enough, the system must also limit where tools and generated code can send data. The caution that allowed edits can still harm is kept. Main S37 unchanged: it already shows an idealized, recommended gate ("rules can be wrong, allowed tools misused"). |
| F04 | Fixed | S27 main, cite and note | Main label "content credentials: recorded origin, edits". Cite line "C2PA Explainer v2.2, §§2, 7.1.2, 7.2.1–7.2.5". Note: credentials *can* record origin and edits; they need not name the person who made it, and the history may be incomplete. Sources cite E16 + E24 with §7.2.4 named; limits add "does not establish that credentials identify the human creator". Truth-check and missing-credentials points kept. |
| F05 | Fixed | S22 note | Consent sentence replaced with "Public availability does not by itself establish consent to this reuse, and it does not make repeating the details harmless." |
| F06 | Fixed | S28, S29, S30 notes | S28: "Many failures … needed no attacker", plus "The deepfake call was different: deliberate deception aimed at people"; then "people manipulating the AI system itself". S29 message is the suggested bridge verbatim. S30 opener: "So far we have seen ordinary failures and deception aimed at people. This section is about someone deliberately steering the AI system itself." Section order and S26 untouched. |
| F07 | Fixed | S30 note | Replaced with the suggested wording: classifier tests using lab images and camera footage captured in drive-by tests, not a reported crash or a demonstration against a deployed autonomous-driving system. The no-injury assertion is gone from the talking points (the Sources "does not establish … that anyone was harmed" limit stays). |
| F08 | Fixed | S20, S39 | `✗` and `✕` replaced by one inline SVG cross (`.yi-x`, `currentColor`, no font dependency). "still open" and "Not in this job" kept. Checked in the print render. `✓` was not flagged and is unchanged. |
| F09 | Taken (S35); S34 not changed | S35 main and note | Node now "Approved summary / by me". Note: the row reads "the summary after my approval", and the talking points add that a misleading instruction can read like a sensible plan and survive a human review. S34's "via the coding agent" kept: the S34 question is what the email can change, and approval appears on the next slide. |
| F10 | Taken | S25 main, comment, note heading, leaf OUTLINE | Retitled "One System, Very Unequal Errors". Four bars unchanged; 12.1 % stays note-only. |

## F01 layout changes (no type shrinking)

- **S03:** mail cards widened 330 → 440 px, so sender lines fit on one line.
- **S08:** flow nodes are `nowrap` with 20 px padding, so "Private manual" and "my own webpage" fit on one line.
- **S16:** document header shortened to "Schematic citation"; card is 280 px wide.
- **S17:** header shortened to "Chatbot said · paraphrase". The middle column is widened 90 → 130 px, so "conflict" clears both cards.
- **S18:** branch grid columns are widened, so "confirmed" no longer crowds "Act on it".
- **S36:** the "Submission address:" prefix is moved into the sub-label, so the old → new values sit on one line.
- **S44:** regridded on the S08 pattern: outside email above the reader, and the recommended boxes under Me and under Coding agent, with up-arrows.

## Pages affected by shared-style changes

Pages S02–S08, S12–S14, S16–S21, S23–S27, S30–S37 and S39–S45. These are all the pages that use a resized kit or package class. Pages S01, S09–S11, S15, S22, S28–S29, S38 and S46 use none of them.

## Checks run

- **Render.** All 46 pages, using headless Chromium print-to-PDF and then `pdftoppm -r 60`. Re-read after the fixes: S03, S08, S16, S17, S18, S20, S25, S27, S34, S35, S36, S39, S44, S45. The other affected pages were read at 1.55rem before the layout fixes and showed no overflow, overlap or clipped labels. No overflow, overlap, clipped labels or missing glyphs.
- **`lint-deck.py`:** `ok` on the deck and on the note.
- **`find-wordy.py` / `find-dense.py`:** no flags.
- **`outline-lint.py`:** the leaf passes. Pointers were shifted for the changed CSS; section ranges now run from the first slide `<div>` to the last slide's closing `</div>`, and the S25 title is updated. Repo-wide, there are 0 stale pointers.
- **Counts:**
  - 46 `data-slide-id` slides and 46 note articles
  - `1 / 46`
  - the pace lines still sum to 43:00
- **Note layout probe:** 1265 px and 485 px viewports (485 px is the headless minimum). scrollWidth equals the viewport, and 0 elements extend past the right edge.

## Plan issues

None new.

## Unsourced facts

None known. The new S36 addresses are invented and labelled as invented in the note. The S27 wording follows E24.
