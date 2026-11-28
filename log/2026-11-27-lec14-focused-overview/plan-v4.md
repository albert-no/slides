# Plan v4 — focused round-1 repairs

## Changes since v3
The three-story argument, audience, 90-minute scope and main teaching steps are unchanged. Round 1 is substantially clearer, but two slides reintroduce a mini literature survey, and two outcome descriptions conflate their denominators. This amendment narrows the main story while preserving every newly removed result in actual backup slides.

This supplements v3 and its incorporated v2 specifications; unchanged requirements remain in force. `review-r1.md` gives the exact reviewed locations and mandatory local corrections. No new research topic or approval gate is introduced. All content/layout decisions below are [judgment]; factual qualifiers are musts. Do not compress or shrink type to preserve a count.

- Main target remains 59 slides, 85 teaching + 5 flexible minutes; existing per-slide times remain targets.
- Backup target becomes 52 slides (47 existing + four content slides + one divider), 0 additional core minutes.
- New IDs S91–S95 are reserved by this plan. Order after existing S56 and before final closer S86: **S95, S91, S92, S93, S94**. Keep all original backup material.
- Sources E01–E25; requests C01–C11. The exact r1 content commit is `1d4493167f41a5d39237fe4e1703e40f94fdfe40`.

## Coverage
| Request | Change / acceptance |
|---|---|
| C01/C02/C05/C06 clarity, background, friendly high-level overview | Correct visible metric definitions; concentrate each result slide on one explained outcome; replace contextless remedy bullets with one bounded experiment. |
| C03 fewer important results | Extra replication, regularization and revision debate leave the main deck; TruthfulQA stays optional. |
| C04/C07 subliminal learning and checked references | Retain Cloud and Askin as the main sequence; verified optional sources remain accessible, with preprint/revision caveats. |
| C08 actual backup preservation | Four new content slides with paired full notes, not notes-only deletion. |
| C09 more teaching steps | No main teaching steps collapsed; expanded backup rather than a compressed catch-all. |
| C10 approved scope; C11 course overlap | Scope/duration unchanged; no restoration of the four generic recaps removed by v3. |

## Revised main specifications
### S69b — Judge Responses Beyond Numbers
- Position/time: main p29 in r1; P2a; retain 1.5 min target.
- Must communicate: the judge-based rate uses selected questions and retained coherent answers.
- Exhibit: existing learner/evaluation/judge flow, with the coherence exclusion visible in plain language. Threshold details may stay in notes; do not falsely imply alignment alone defines the evaluated population.
- Sources: E15/E23. Keep formatting suffix, eight questions and judge limitations.
- Notes: exact thresholds and exclusion; synchronize message, script, key and accessibility text.
- Acceptance: audience can tell which answers are included without reading notes.

### S70 — Unsafe Tendencies Also Transferred
- Position/time: main p30; P2a; retain 2.5 min target.
- Must communicate: the insecure-teacher numbers condition produced more judged misalignment on the selected free-form questions than controls.
- Exhibit: source **Fig. 3a left subplot only**, maintaining its baseline, all teacher conditions, uncertainty and axis. Explain its rate and retained answers. Do not turn the approximate prose value into an exact new bar.
- Sources: E05/E15/E23.
- Off-main: the complete Fig. 3a, including TruthfulQA, goes to S91 and paired notes. Its existing detailed explanation remains available there.
- Acceptance: no second, unexplained task/outcome in the main exhibit; all visible keys describe the shown metric accurately.

### S72b — A Finding, Not a Universal Rule
- Position/time: main p33; P2a; retain 1 min target.
- Must communicate: the experiments established particular trait/task/model combinations, not universal transmission or a demonstrated hidden-intent mechanism.
- Exhibit: a single evidence-boundary diagram using the **already explained animal-preference and harmful-answer experiments**. Show tested combinations versus unanswered generalization, not three additional paper summaries. Suggested component `grid-2`; slides decides.
- Sources: Cloud E05/E15; E08–E10/E25 as optional scope evidence only.
- Off-main: reproduction result → S92; regularization result → S93; categorical-critique revision notice → S94. Preserve the corresponding detailed notes and citations. Do not teach the critique on the main slide.
- Acceptance: no new task name, mitigation method or paper controversy to explain during this one-minute boundary slide; no “all models transfer” or “debunked” claim.

### S75b — A Safer Teacher Helped in These Tests
- Position/time: main p40; P2b; retain 1.25 min target.
- Must communicate: an aligned teacher reduced measured misalignment in a bounded recovery experiment; this is an encouraging direction, not a general cure.
- Exhibit: one simple recovery sequence: **narrowly misaligned learner → training guided by aligned teacher → measured misalignment near base-model levels**. This adds context to the result already mentioned in r1, not a new study. Name tested Llama/OLMo models at the appropriate readable level; source details in notes. Suggested component `diagram-flow`; slides decides. No invented numeric bars.
- Sources: E07, Askin v2 §4.2/Fig. 5/App. E.3, https://arxiv.org/html/2605.12798v2 . No claim all training routes or all models are equally safe.
- Main boundary: “A recovery result in tested models, not a general remedy.” Clear answer to “what might help?” without surveying methods. Retain the training-time versus runtime-control transition in notes.
- Off-main: remove the contextless “Fix study” bullet; its preference/style study is S93. Keep the failed-filter result on its own S74b, not another list here.
- Notes: start state, aligned teacher, evaluation against base levels, tested models, all-channel details and limits; updated message and figure explanation.
- Acceptance: one response experiment with its setup/result/limit, not three remedy headlines and a checklist.

## Added backup specifications
All five slides go in `courses/trustworthy-ai/backup-lec14-agentic-threats.html` and matching `-note.html`, P4. Suggested components are optional; all timings are **optional / 0 core minutes**.

### S95 — B6 · More on Hidden Transfer
- Before S91, after S56; section divider. Contents label must match.
- Point: further outcomes and unsettled literature, not required for the core lecture.
- Exhibit: normal section divider; note describes four optional entries. No new claim/source needed.
- Acceptance: clearly outside the 90-minute main path.

### S91 — Two Outcomes, Two Different Scores
- After S95. Point: Fig. 3a's harmful-answer and factual-error tests have different meanings.
- Exhibit: the complete existing Cloud Fig. 3a, unaltered internally. Explicit separate keys: left free-form judged-misalignment rate among retained coherent answers; right false answers on TruthfulQA. Explain TruthfulQA as a factual-question benchmark here, before interpreting it. Preserve all controls/axes/intervals. Suggested `slide` with plot key.
- Sources: E15/E23, final Nature Fig. 3a and Methods. Transfer the r1 S70 note explanation; do not equate wrong facts with harmful intent.
- Acceptance: no common y-axis definition that conflates the outcomes; full source panel preserved.

### S92 — Reproduction Varied by Trait and Task
- After S91. Point: open-weight animal preference transfer reproduced, but generalization was uneven.
- Exhibit: readable paper Fig. 1 or 2 from van der Weijden et al. with a simple key; choose the panel that supports the stated limited claim. No full result table. Suggested `slide` with plot key.
- Sources: E08/E25; https://arxiv.org/html/2609.12586v1 , §2, §4.1/Fig. 1, §4.2/Fig. 2, §5; cite versioned preprint.
- Main/notes split: identify the preference question and tested conditions on the backup slide; model/task details and limitations in notes. Not an independent demonstration of broad harmful transfer.
- Acceptance: more context than the old one-line main catalogue; no claim preferences are themselves dangerous.

### S93 — A Preference Fix Is Not a Harm Remedy
- After S92. Point: regularization reduced selected preference/style transfer, without establishing prevention of harmful misalignment.
- Exhibit: simple intervention/result/boundary comparison grounded in the paper; a source figure is preferred if it communicates this without a technical derivation. Explain regularization at most as keeping the learner near its starting behavior. Suggested `grid-2`; no loss function.
- Sources: E09/E25; https://arxiv.org/html/2609.22215v1 , §3–4, Limitations “Experimental scope”, “Traits studied”, “Baselines and side effects”.
- Must keep: number/math-reasoning settings; selected small open-weight models; mostly animal preferences plus French style; authors could not reliably induce subliminal misalignment. Do not imply harmful traits were successfully prevented.
- Notes: preserve full r1 S72b/S75b source details, remove “not re-checked” workflow text and cite the verified Limitations section.
- Acceptance: evidence and unanswered safety question are clearly separated; preprint status explicit.

### S94 — This Categorical Critique Is Under Revision
- After S93, before existing closer S86. Point: the authors' revision notice prevents treating a categorical counterclaim as established.
- Exhibit: source-labelled contrast between the paper's categorical headline and its author revision notice; paraphrase rather than an extended quotation. This is a research-status card, not a technical rebuttal result. Suggested `grid-2`.
- Sources: E10/E25, https://arxiv.org/abs/2606.00831v2 , Comments field checked 2026-11-27.
- Must: authors acknowledge some main claims incorrect and substantial revision in preparation. This does not settle every mechanism or prove universal transfer. Explain the topic of the claim in plain language; avoid a LoRA lesson.
- Notes: preserve original bibliographic context and dated status; no unsupported new rebuttal or deployment claim.
- Acceptance: cannot be mistaken for an established debunking or a fresh peer-reviewed result.

## Remaining local repairs and packages
- P2a: F01 and F02, S69b/S70/S72b and paired notes; optionally F08's one-time plain-language naming of subliminal learning. Supply preserved full figure to P4.
- P2b: F02 S75b; F04 S74b visible metric and epoch wording. All other teacher/token/judge build-up slides remain.
- P3: F03 S78/S45 denominator correction; F05 S39b branch label; optional F07 glyph repair S76. No change to the 15%/62% comparison or the qualitative attack-selection result.
- P1: optional F07 glyph repair S59 only.
- P4: new S95/S91–S94; preserve original 47 backup slides; F06 long-URL overflow.
- P0: correct main note S45 overflow, paired IDs/titles, backup Contents/counts/optional navigation, course and root OUTLINE and all affected line pointers. Main pacing still sums to 85; backup adds no core time. No new tech content or reference/shared-style change authorized.

## Decisions on work-r1 plan questions
1. S59's lec13 note reference p62–64 is accepted; p62's six-check framing is relevant. No forced p63 start.
2. S74a's two post-training bars are accepted. Table 1 has no untrained learner bar; do not invent one or substitute the teacher's 50.6% as a learner baseline.
3. S75b's structured cards were a valid exhibit; no decorative figure was required. The revision above is about missing context and excess result breadth, not the absence of an image.

## Round-2 acceptance
Resolve all blocking findings in `review-r1.md`, report each finding ID, preserve material according to the new backup mapping, and send an exact pushed content SHA. Render changed slides and their neighbours, every new backup slide, and both note files at approximately 430px. Do not rerender unchanged pages merely to repeat the first full audit. Do not shrink fonts. No PR/merge yet.
