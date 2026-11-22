# lec13 clarity — review round 2

- **Reviewed commit:** `78b1f81ad06540e28734aaaa79f059f37196106e`.
- **Compared with:** round 1 `06678b4f01df7519d33f6f21e7d1d5025ae93559`; OUTLINE also checked against baseline `9effc8ab67589f2d7e5789f04db5e92067ff46d9`.
- **Verdict: approved.** All nine blocking round-1 findings are closed. One nonblocking rendering detail is recorded below; it does not require another round.
- **Deliverable:** 65 main slides, 65 matching notes, 15-slide technical supplement; 90 minutes including the 8.5-minute flexible explanation/question buffer. No activities added.

The email narrative and explanatory steps now carry the argument clearly. In particular, direct injection is explicit, the incident diagrams are readable, defense names are explained before measurement, and the provenance/approval examples distinguish permitted data use from authority.

## Finding disposition

| ID | Slide ID / revised page | Type | Blocking remaining? | Verified result |
|---|---|---|---|---|
| F01 | S43 / 52 | fact | No | Actual CaMeL Fig. 5 replaces the problem diagram. The key explains planner, quarantined reader, interpreter and policies; note layers match. Runtime data-dependent branches remain qualified. |
| F02 | S44b / 54; S47c / 59; S48 / 60 | fact | No | Only an authorized person may grant a policy-permitted exception; this is explicit on the slide and throughout notes. Detector/approval distinction corrected; Invariant observation no longer presented as causal proof. |
| F03 | requested diagrams plus revised flows and S37/S39 keys | design rule | No | Primary inline diagram labels are body size at the final render; secondary ticks/numeric labels retain their appropriate sizes. Requested p26/28/30/33/53–54 diagrams are readable without clipping. Source-plot keys enlarged. |
| F04 | OUTLINE shared surface | design rule | No | One lec13 section; no duplicate second-level headings. Baseline diff is confined to the lec13 section and two relevant index/ID lines. Unaffected lec11/lec12 material restored. |
| F05 | S13 / 16 | fact | No | Authorized path includes the tool result: 1 → 2 → 3 → 5, skipping only the send; note agrees. |
| F06 | S31a/b / 35–36 | fact | No | JSON format named; encoding/parser protection distinguished from model interpretation. Delimiters help but do not enforce authority. |
| F07 | S01 / 1 note | fact | No | General definition includes lower-trust overrides; the outside-email case is explicitly the indirect starting example. |
| F08 | S34 / 39 note; S40a / 46 and generator | fact | No | Table 5 values unchanged; unsupported exact clean aggregation removed and caveat recorded. Distinct-task count and separate study denominators preserved. |
| F09 | S16 / 19; S30 / 34; S31b / 36; S44b / 54; S47b / 58 | design rule | No | All six originally reported negative glyphs replaced by clear words, including standalone Yes/No policy checks. |

### F10 — Small marker fallback in the added plot key [judgment; nonblocking]
- **Where:** `courses/trustworthy-ai/lec13-prompt-injection.html:1184`, S37 / p42; matching marker description in `courses/trustworthy-ai/lec13-prompt-injection-note.html:912`.
- **Type / blocking:** design rule / **no**.
- **Observation:** the new `✕` before “GPT-4o” renders as a small missing-glyph box in my Chromium environment, although work-r2 reports both added marker glyphs rendered. This is distinct from F09's now-fixed negative decisions.
- **Why nonblocking:** the original plot legend still shows the cross, and the body-size key gives the model name and both coordinates (69%, 48%), so neither the result nor identification of the point depends on this added decorative glyph.
- **Concrete future polish:** use an ordinary `x` or a verified drawn cross, and keep the note description aligned. This is not a required content change before opening the PR; approval is pinned to the current commit.

## Albert request coverage

All 19 substantive comments are addressed; main-slide answers and corresponding note explanations agree. C00's remaining administrative step is the PR after the final job-record push.

| Comment | Baseline page → revised IDs/pages | Status |
|---|---|---|
| C00 | deck/design/notes/PR | Content review done; PR pending log-only handoff |
| C01 | opening → S01/S04, 1/4 | Done: agents read many authors' text |
| C02 | motivation → S05a/b, 5–6 | Done: concrete email and unauthorized send |
| C03 | 7 → S06/S07a/b, 7–9 | Done: direct app-user attack vs indirect email |
| C04 | 8 → S08, 10 | Done: conflicting instructions require priority; permissions are separate |
| C05 | hidden text → S09a/b, 11–12 | Done: author manipulation and documented ICML organizer probe, with limits |
| C06 | 16 → S16, 19 | Done: notes may choose a file, not an extra recipient |
| C07 | 20 → S20/S21b, 23/25 | Done: provider defined; demonstration/victims/fix/retest distinguished |
| C08 | 22 → S22, 26 | Done: readable guard/bypass diagram |
| C09 | 21 → S21a/b, 24–25 | Done: retrieved email, generated image link, automatic data-bearing request |
| C10 | 23 → S23, 27 | Done: same user in demo; credential scope is the general condition |
| C11 | 24 → S24, 28 | Done: readable private-read/public-write chain |
| C12 | 26 → S26, 30 | Done: readable dated fix/retest sequence |
| C13 | 29 → S29, 33 | Done: authority order, not search ranking; readable learned-vs-enforced distinction |
| C14 | 31 → S31a/b, 35–36 | Done: JSON escaping, delimiters, and the insufficient-marking example |
| C15 | 40 → S54 before S40a/b, 45–47 | Done: repeat task after tool output; nothing executes twice |
| C16 | 40/41 → S54/S55/S56 before results, 45/48/49 | Done: sandwiching, classifier, masked-run comparison |
| C17 | 44 → S44a/b, 53–54 | Done: source/reader labels followed by an allow/deny walkthrough |
| C18 | 47 → S47a/b/c, 57–59 | Done: three explanatory steps |
| C19 | 48 → S48, 60 | Done: routine proceed, prohibited deny, authorized consequential exception ask; verified action facts |

## Accepted plan interpretations

- **CaMeL source figure:** the small code/table text inside Fig. 5 is not the audience's reading task. The outside body-size key carries the architecture's essential roles, and the note carries code-level explanation. This is an acceptable external-key treatment under DS §8, not a claim that the source's internal code is body-size. The following two large diagrams teach provenance and decisions concretely.
- **Source plots:** S37's key identifies the discussed model points and values; S39 retains the source plot while setting shortened evaluation names outside it. Legend/value detail in the source is supported by the readable keys, with no data repainting. F10 records the one remaining cosmetic marker issue.
- **Wording trims:** removed S37 under-attack utility and S39 repeated prefixes remain in notes; S56 “not executed” retains the masked-call distinction. No required argument or result removed.
- No new plan version is needed. The 90-minute scope and no-activities constraint remain unchanged.

## Verification

- Read exact commit through git; extracted an immutable archive for browser checks. Main HTML changes are on pages 4, 6, 8, 10–12, 14–16, 18–21, 24, 26–30, 33–37, 42, 44–46, 48–55, 57–60; rechecked these and their neighbours. S01 changed in notes only. The renderer captured all pages for convenience, but unchanged later material was not put through a fresh content review.
- Checked final 1280×720 browser renders after slide animations settled, with full-size inspection of the critical diagrams and new source exhibits. No clipping, internal overlap or footer collision found in the changed material; no outer-bound overflow in DOM checks. F10 prevents an unqualified claim that every decorative glyph is clean.
- Measured inline SVG text using rendered width/viewBox scale. Sub-body text is confined to numerical/tick/legend annotations listed in work-r2; primary flow labels meet the body-size rule.
- Main/note IDs match in order, are unique, and both count 65. Notes at a 430-pixel viewport have document width/scroll width 415/415, with no horizontal overflow. Reviewed the full note diff and matching slide text.
- Independent `lint-deck.py`: main, note and tech pass. `git diff --check`: pass. The archive OUTLINE linter still reports only the pre-existing external lec09 script path unavailable in this container; the lec13 references and heading uniqueness were checked separately.
- P5 chart generator outputs match the three embedded SVGs after indentation normalization; source values unchanged. CaMeL chart changes are label sizing, not numerical geometry. New crop provenance is recorded in work-r2.
- Tracked copies of plan-v1, plan-v2, review-r1, requests and evidence match reviewer-owned files byte-for-byte. No unexpected deck/script/reference changes outside the reported scope.

## Handoff

Copy this review unchanged and refresh the living job files; push **job-log-only changes** and return the exact head SHA. No mandatory content changes remain. slides-review will verify every commit after the reviewed SHA touches only `log/2026-11-20-lec13-clarity/`, then open the PR against main. Do not merge: Albert has not authorized a merge.
