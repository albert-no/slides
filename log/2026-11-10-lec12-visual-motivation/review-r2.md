# Review r2 — revise; escalated at round limit

Job: `2026-11-10-lec12-visual-motivation`
Reviewed commit: `f2e696dbe9793da8ce1167d7a368408bd278ed2c`
Previous reviewed commit: `6d1e21cc4b484d0b6333ca8d2607b79e9ec9facf`
Baseline: `cd0da5ca7ad75ceef107d28ad110407f0c33b4ff`
Round: **2 of 2** · Verdict: **revise** · Job state: **escalated**.

## What matters

The outline is repaired, the old reduced-size keys are gone, and the factual corrections F04–F07 are correct. The new separate figure panels and staged keys are worth keeping. Only the new method-key slide, S76 / main p58, still needs attention: its title overstates the classifier setup, and its longest column creates an eighth body line. These are localized corrections, not a request to redesign the lecture.

The medium-job round limit is reached. **Do not start a third implementation/review round or open a PR without Albert's decision.** Recommended decision: authorize these two localized fixes and one final changed-page verification.

## Original-request coverage

| Comment | Done? | Result |
|---|---|---|
| C01 | Partial | Whole lec12 delivered; two localized findings on new p58 prevent approval. |
| C02 | Yes | Motivation, shared lending counts, calibrated example and randomized mixture retained. |
| C03 | Partial | Diagram and plot-key type improved; p58 density remains. |
| C04 | Yes | Fixed arrows remain intact, including baseline p40 → current pp50–51. |
| C05 | Yes | Separate visual revision; Albert's detailed-edit PR remains later. No PR/merge. |
| C06 | Yes | Lec12 only; unrelated OUTLINE content restored exactly. |
| C07 | Yes | Same pinned job continued. |

## Finding dispositions

| ID | Slide ID / r2 page | Type | Blocking now? | Disposition |
|---|---|---|---|---|
| F01 | Shared outline | design rule | no | Closed. Outside the lec12 section and its three index entries, OUTLINE content matches baseline exactly. One section per lecture; 76/23 counts and section ranges agree. |
| F02 | S41a/b, S42, S43a, S44a/b / pp53–56,59–60; new S76 / p58 | design rule | **yes, residual on S76 only** | All six original keys now use native prose and render cleanly. The new full-key slide has eight body lines along its longest column; see item 2 below. No remaining font-size or line-height reduction found in these revised keys. |
| F03 | S17a/b pp21–22; S39a/b pp48–49 | design rule | no | Closed with source limitation accepted. Hardt ticks/titles are intact. AIF360 dataset/attribute labels are readable in separate original panels. Remaining outer-edge truncation is already in the original raster objects (E29), is disclosed, and does not obscure the teaching comparison. Do not repaint the source. Shared old asset unchanged. |
| F04 | S51b / p70 | fact | no | Closed. Separate two-gender/three-race matches on slide and in note. |
| F05 | S54a / p73 | fact | no | Closed. Cost understates need; no claim of different decisions at identical scores. |
| F06 | S54b / p74 and note | fact | no | Closed. Cost-versus-need distinction, selection-rate definition and judge/score distinction corrected. |
| F07 | S61b / tech p6 | fact | no | Closed. Discrete setting and positive-mass support explicit; aligned equation fits. |
| F08 | S60 / tech p4 | preference | no | Taken and closed. Native-size denominator key replaces underbraces. |
| F09 | S76 / main p58 and note | fact | **yes** | New title and unrestricted shade key contradict the two in-processing exceptions. See item 1 below. |

## Remaining corrections for Albert's decision

1. **F09 — classifier setup [judgment].** `courses/trustworthy-ai/lec12-fairness.html`, S76 / p58, lines1693,1706–1707,1716; paired `courses/trustworthy-ai/lec12-fairness-note.html`, article S76, lines967–970. Current title “Nine Mitigation Methods, Two Classifiers per Method” → “Nine Methods, Different Classifier Setups”. Restrict the bottom dark/light rule to **paired coloured dots**; retain explicit NN-only and LR-only labels for the grey entries. In the note replace “Each method is run with…” with “Seven methods are run with LR and RF; adversarial debiasing uses NN only, and prejudice remover uses LR only.” Qualify the note's shade takeaway likewise and sync its title. Reason: Fig5's legend has seven pairs and two single-classifier exceptions, not nine pairs (E29).

2. **F02 residual — one extra body line [judgment].** `courses/trustworthy-ai/lec12-fairness.html`, S76 / p58, lines1695–1716, especially1702. Rendered count: introductory key line (1), stage headings (1), longest method column (5, because “Learning fair / representations” wraps), final shade key (1) = **8**, above DS §1's seven-line ceiling even for plot keys. Keep native type and spacing. One precise option: shorten this key label to **“Fair representations”**, retaining the full “Learning fair representations” method name in S76's note; verify that it stays on one line. Equivalent reflow/split is slides' choice. Reason: the dedicated key should resolve F02's density without recreating it. This is not an overflow or font-size finding.

## Accepted plan choices and verification

- Accept S39a/b and new S76: main76, matching note76, tech23. No argument or teaching-scope change. Independently summed note pacing: 90 minutes, section totals10/20/15/20/15/10. Counts remain targets; no new plan version required merely for these splits.
- Reviewed exact commit through git; extracted with git archive. Rendered main76 and tech23 in Chromium. Visually checked changed pages and neighbours: main20–23,47–61,69–75; tech3–7. No new overflow, overlap or detached-arrow defect seen. Did not repeat the round-1 full-deck audit.
- Read the original requests first; checked changed source claims against E24–E29/primary AIF360 PDF, then DS and plan-v2. No claim of a timed rehearsal or complete external-link refresh.
- Main/note IDs match in order; technical IDs unique; local main image paths resolve. Tracked frozen plan-v2/review-r1 and living evidence/requests matched owner copies before this review's append.
- Deck lint: main only accepted source-colour warning (30 inline occurrences); note/tech clean. Reviewer scratch outline lint reports five existing unrelated warnings and one existing lec09 absolute-path dependency (`OUTLINE.md:326`, `/workspace/agent/lec09/r4/build_deck.py`) unavailable in this container. That line is byte-identical to baseline; not a new job blocker. All modified lec12 outline pointers pass.
- Source limitation correction: round1's “re-crop” assumption was too strong for Fig4's original edge defects. Independently extracted the PDF objects and confirmed exact hashes (E29); preserving the originals plus readable labels is accepted.

No PR opened. Await Albert's decision; this file is an escalation record, not a third-round work order.
