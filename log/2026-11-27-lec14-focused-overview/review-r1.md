# Review r1

- Job: `2026-11-27-lec14-focused-overview`
- Reviewed commit: **`1d4493167f41a5d39237fe4e1703e40f94fdfe40`**, not the working tree.
- Frozen baseline: `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`.
- Verdict: **revise**. Round 1 of 3 reviewed; round 2 work order is `plan-v4.md` plus the blocking findings below.

## What matters
1. **Keep the new slow build-up.** The Vend sequence, separated teacher/learner/judge roles and control experiment are much easier to follow. Do not collapse these teaching steps or reinsert the four generic recaps.
2. **Correct the visible measurement stories.** Cloud's two outcomes need distinct definitions; the attack-selection score excludes inconclusive attempts. Correct details in notes do not repair misleading slide summaries.
3. **Keep the main lecture out of the literature catalogue.** S72b and S75b add several results without their setups. Move the extra studies to real backup slides and give the retained recovery result a simple explanation. v4 owns that scope correction.

## Request coverage
| ID | Status | Evidence / remaining work |
|---|---|---|
| C01 confusing lecture | Not yet complete | Three-story structure is substantially improved; F01–F05 repair remaining confusing measurements/explanations. |
| C02 detailed introduction/context | Not yet complete | Main experiments are introduced stepwise; S72b/S75b still present unexplained study headlines (F02). |
| C03 fewer high-impact results | Not yet complete | Strong three-story selection, but the extra preprint catalogue violates the intended focus (F02). |
| C04 subliminal learning / suggested Askin paper | Done | Cloud experiment and Askin token-score extension are central, not token mentions. F08 is optional naming polish. |
| C05 friendlier slides | Not yet complete | Clear diagrams and readable pacing overall; F02/F04/F06 repair remaining usability issues. |
| C06 high-level setup/solution/illustration/message | Not yet complete | No loss-function lecture; distinguish scores and give the response its context (F01–F05). |
| C07 check relevant references | Done, with factual repairs required | Primary papers checked, version/venue limits mostly careful. F01/F03/F04 identify the remaining description errors. |
| C08 put removed material in backup slides | Done for r1 migration | Actual 47-slide backup with paired notes; original material preserved. v4 specifies preservation of the additional material removed in this round. |
| C09 more slides, not compression | Done | 59 main teaching steps plus 47 backup; retain main pacing/steps. |
| C10 go ahead | Done | Approved scope honored; no further Albert gate needed for these repairs. |
| C11 redundancy against lec01–13 | Done | E21/E22, work-r1 novelty/reuse table, four generic recalls in backup, case-specific contrasts in notes. No earlier-deck edits. |

## Findings
Locations are repo-relative, at the reviewed commit. In the table and numbered requests, M means `courses/trustworthy-ai/lec14-agentic-threats.html`; MN means `courses/trustworthy-ai/lec14-agentic-threats-note.html`; BN means `courses/trustworthy-ai/backup-lec14-agentic-threats-note.html`. Every fix applies to paired notes/alt text where relevant. [judgment] identifies content/design/wording choices, not optionality: blocking still governs.

| ID | Slide ID / r1 page | Type | Blocking | Problem → required fix |
|---|---|---|---|---|
| F01 | S69b–S70 / main 29–30 | fact | Yes | Coherence exclusion missing on-slide; one y-key incorrectly covers two different outcomes → define retained answers and narrow main Fig. 3a to free-form outcome, preserving full panel in backup. |
| F02 | S72b / 33; S75b / 40 | unmet request | Yes | Three-preprint catalogue and contextless remedy list → focused boundary/recovery explanations and actual backup preservation, per v4. |
| F03 | S78 / 55; S45 / 56 | fact | Yes | “Per attempt” / “of attacks attempted” conflicts with formula → state that neither-caught-nor-successful attempts are excluded. |
| F04 | S74b / 38 | design rule | Yes | Chart has no visible outcome key; three epochs renamed three rounds → add metric and accurate plain-language training duration. |
| F05 | S39b / 50 | fact | Yes | Audited-clean branch enters a box labelled “no expert check” → put that label only on the unaudited branch. |
| F06 | S79 / backup 42; S45 / main note 56 | design rule | Yes | Long source URLs cause horizontal note overflow at 430px → wrap/break or use descriptive links without shrinking text. |
| F07 | S59 / 15; S76 / 44 | design rule | No | Cross glyph renders as a missing-glyph box → use a reliably rendered cross or plain text. |
| F08 | S66b / 24 or S71 / 31 | preference | No | Core phenomenon is not named in visible teaching text → optionally name and define subliminal learning once. |

### 1. F01 — show which answers the rate counts [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S69b p29 L838–865 and S70 p30 L868–884; matching notes `courses/trustworthy-ai/lec14-agentic-threats-note.html` L583–627.
- **Current → fix:** S69b's judge box currently defines the result only as “below 30: misaligned”. Add the plain-language coherence exclusion to the visible flow/key. Preserve exact thresholds in notes: discard coherence below 50; alignment below 30 among retained answers is classified as misaligned. Synchronize Message and accessibility descriptions.
- **Current → fix:** S70 shows both free-form and TruthfulQA plots while its y-key says “share of answers judged misaligned”. Main should show the left free-form subplot, with retained-answer population/controls/intervals accurately keyed. Move the full existing panel a and its two-outcome explanation to new backup S91, as v4 specifies.
- **Why:** these are distinct measured outcomes, not one harm frequency. The current notes already know the distinction; the projected slide must too.
- **Source:** E23, [Cloud final Nature article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13083239/), Fig. 3a and Methods. The approximate “about 10%” text is acceptable if identified as the paper's textual summary; do not replace the source mean with an invented exact 10% bar.

### 2. F02 — remove unexplained result breadth, not teaching steps [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S72b p33 L940–966; S75b p40 L1226–1242. Paired notes `courses/trustworthy-ai/lec14-agentic-threats-note.html` L683–710 and L852–880.
- **Current → fix:** S72b's three “Later preprints” results, including the revised categorical critique, become separate optional backup entries S92–S94. Retain only an evidence-boundary picture using the experiments already explained on main. v2 explicitly prohibited a literature catalogue here and E09/E10 assigned their detail to optional material.
- **Current → fix:** S75b's “Aligned teacher…” / “Fix study…” / “Judge filter…” list becomes one explained recovery experiment, with start state, aligned teacher, measured outcome and bounded conclusion. v4 specifies the revised takeaway and sources. “Fix study” is not self-contained context. Do not substitute a new checklist that duplicates S75a.
- **Preservation:** original result/detail text must remain accessible in backup notes; complete Cloud Fig. 3a also moves to S91. New section S95 marks optional material. Update backup Contents and OUTLINE. Do not compress these four optional results into a single replacement catalogue.
- **Why:** Albert asked for fewer results with clearer setup/solution/message, not simply fewer section headings.
- **Sources:** E07–E10/E25 and v4 locators. Replace S72b note's internal “not re-checked in the paper body” sentence with the verified [mitigation Limitations source](https://arxiv.org/html/2609.22215v1). No claim that this study prevented harmful misalignment.

### 3. F03 — the attack-selection denominator is not all attempts
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S78 p55 L1612–1641 (especially L1636), S45 p56 L1644–1672; `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S78 L1110 and S45 L1133–1155, especially Message L1136.
- **Current → fix:** “per attempt” and “of attacks attempted, how many were caught?” → “Among attacks caught or successful, what share was caught?” Add a short visible qualifier that unsuccessful, uncaught attempts are left out. Keep the correct caught/(caught+succeeded unseen) formula if helpful; do not add derivation.
- **Notes:** S45 Message and Script must agree with S78's already-correct detailed denominator explanation. “Attempted and ended” is still too broad; say decisively ended, and define the two included outcomes. Keep post-hoc stop-policy, small-sample and upper-bound caveats.
- **Why:** excluding inconclusive attempts is central to why selection changes this statistic; it is not a cosmetic label.
- **Source:** E24, [Ge-Wang et al. v1](https://arxiv.org/html/2606.06529v1), equation 1 and Appendix A.3.

### 4. F04 — make S74b readable on its own [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S74b p38 L1161–1192; paired note `courses/trustworthy-ai/lec14-agentic-threats-note.html` L805–833.
- **Current → fix:** the two percentages need a visible outcome label, e.g. “Learner answers judged misaligned and coherent (%)”; use the paper's criterion in notes. The percentages currently have only tick labels and model/training metadata. Do not rely on the preceding slide, particularly because this is a different model/table.
- **Current → fix:** “after three training rounds” → “after three passes through the training data (epochs)” or simply “after 3 epochs” with a plain-language definition in notes. An epoch is not one teacher-score update.
- **Why:** the audience needs to know what 39.6% measures, and how long the tested training ran.
- **Source:** E16, [Askin v2](https://arxiv.org/html/2605.12798v2), §2, Table 10, App. E.2.4. Keep the 39.6/39.3 values and no-significance-claim caveat; no change to the 27.1/38.9 chart requested.

### 5. F05 — fix the monitoring branch semantics
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S39b p50 L1496–1520, especially the submit node L1510; paired note at `courses/trustworthy-ai/lec14-agentic-threats-note.html` L1013.
- **Current → fix:** shared “submit / no expert check” destination → shared “submit”; place “no expert check” only on the monitor-to-submit bypass branch. Audited-clean code must visibly remain an audited case.
- **Why:** the diagram currently contradicts its own clean-audit arrow and the correct accompanying note.
- **Source:** [Greenblatt et al. v5](https://arxiv.org/html/2312.06942v5), §3.2; the old backup S90 already has the correct branch logic.

### 6. F06 — remove horizontal note overflow
- **Where:** `courses/trustworthy-ai/backup-lec14-agentic-threats-note.html`, S79 backup p42, L996; `courses/trustworthy-ai/lec14-agentic-threats-note.html`, S45 main p56, sources around L1150–1152.
- **Observed:** at a 430px viewport with 415px layout width, backup document scroll width is 471px, caused by the plain Project Vend URL in S79; main scroll width is 419px from two plain arXiv URLs in S45. Text-range inspection identified these contributors; no broken image was observed.
- **Fix:** use descriptive source links or safe local wrapping so the articles do not overflow. Preserve font size and source destinations; no shared `reference/` edit. Check both notes at approximately 430px after changes.
- **Why:** DS §9 explicitly requires narrow-view notes without horizontal overflow.

### 7. F07 — cross glyph fallback (nonblocking) [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S59 main p15 L499–550 and S76 p44 L1341–1372.
- **Observed:** the ✗ in the failure case is a missing-glyph rectangle in Chromium renders; the surrounding words still convey failure.
- **Fix:** reliably rendered cross shape or “fails”/“wrong”, checked in the final render. No smaller text or new font dependency needed.
- **Why:** avoid a distracting broken symbol. This alone would not start another review round.

### 8. F08 — name the phenomenon once (optional) [judgment]
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`, S66b p24 L709 or S71 p31 L887; paired note likewise.
- **Suggestion:** after the example is understood, add one short identification such as “Subliminal learning: a trait transfers through data that does not explicitly show it.” Do not change the beginner-friendly explanation into jargon or imply deliberate secret communication.
- **Why:** students should be able to name/search the phenomenon Albert asked to teach. Choice of location/wording is slides' call, and this is not a new blocker.

## Independent checks completed
- Read exact work report, all 59 main slides and their paired notes, all 47 backup slide renders, and the relevant transferred/changed backup notes. Independently rendered the exact archived content, not a moving branch.
- Verified 59 main IDs/articles and 47 backup IDs/articles, 106 distinct IDs, and note pacing sum **85.0 minutes** plus stated 5 flexible minutes. No outer slide overflow or broken note images detected. F06 is text overflow, not an image or article-box failure.
- Compared baseline-to-r1 note migration: removed slides' substantive paragraphs remain; detected differences were section/page remapping, role wording and standalone context. Original source figures/qualifiers and full control variants remain in actual backup. No preservation blocker found for the initial migration.
- Re-read primary Cloud/Betley/Askin, Vend, control and attack-selection material for setup/values/qualifiers; checked optional-source limitations and the current critique notice. E23–E25 record the corrections. The plan itself was not used as empirical evidence.
- Relevant root/leaf OUTLINE counts, section links and mapped titles agree with r1; they will need the v4 backup additions and changed line pointers. Tech diff only changes title/framing; all 14 technical slides' content retained.
- Diff scope: 32 files, confined to the requested lec14/backup/assets, outlines and job record. No lec01–13, shared reference, design-system or CEO-talk edits.
- Frozen plans and living request/evidence copies at r1 match the announced source files. Current job header transition to review is naturally newer than the tracked r1 header.

## Decisions on work report and plan
- Accept S59 note reference to lec13 p62–64, as p62 provides relevant six-check context.
- Accept S74a's two post-training bars, without an invented untrained bar or teacher-rate proxy. No before/after claim introduced.
- Accept structured cards as an exhibit. S75b is being reworked for content focus/context, not because it lacked a bitmap or SVG.
- Accept the phase-two-only Vend chart and note of differing cross-phase reporting; no unsupported numeric phase comparison is taught.
- Accept not inventing Cloud's unnamed judge-model identity; keeping exact evaluation qualification matters more.
- Accept S05b's idea in its highlight instead of duplicating a lead sentence.
- v4 narrows the ambiguous S70 Fig. 3a instruction and S72b/S75b scope. The added backup slides preserve removed material as Albert required. Main time and approved argument are unchanged.

## Handoff
Implement F01–F06 and plan-v4. F07/F08 are nonblocking. Copy this review and v4 unchanged into the tracked job record; refresh living files at push. Return `work-r2.md` with every finding disposition, new backup mapping, current pacing/counts and exact pushed SHA. Recheck changed slides and neighbours, not a second full unchanged-deck pass. No PR or merge authorization.
