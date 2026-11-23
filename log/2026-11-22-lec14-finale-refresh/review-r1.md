# Review r1 — lec14 finale refresh

- Reviewed commit: `ad77502e7f1c47f0a067a275f6ffb542e80676d9`.
- Baseline: `34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233`.
- Verdict: **revise**. Next submission is round **2 of 2**.
- Active plan: plan-v2.md. No argument, scope or time-budget change requested.

## What matters

1. Fix the control section's scope: the earlier attacker was not wholly indiscriminate, and attack selection is not universally untested. Also retain H in the no-U baseline label.
2. Finish the readability pass: several essential concept labels are still below body size, and two note tables overflow at a narrow viewport.
3. Close the small source-integrity issues: Motwani's date, the clipped METR tick, and the S06 generator mismatch.

Keep the successful changes: the real shop/developer examples, the S54 split, the concrete chess-verification example, the explicit persuasion correction and noncausal companionship finding, and the single broad course takeaway. The deduplication preserves the multi-agent propagation contribution without reopening the lec13 defense catalog.

## Request coverage

| Request | Result |
|---|---|
| C01 brief refresh after lec13; remove duplicates | Done: six redundant main slides retired with unique detail migrated; six-section argument remains. |
| C02 enlarge diagram fonts | Partly done: substantial improvement, but F02/F03/F06 remain. |
| C03 motivating real-world examples | Done: bounded Project Vend experiment and real-developer RCT, with human support and dated-update caveats. |
| C04 recent works, high level | Done in selection and level; F01/F05 correct scope/date wording. |
| C05 brief course summary | Done: S50 is the only global summary, spans data/answers/attacks/provenance/fairness/actions. |
| C06 brief topics beyond the course | Done: S55 persuasion and S56 companionship are distinct, sourced previews. |

## Blocking findings and self-contained change requests

Line numbers below refer to the reviewed commit. Paths are repo-relative. All wording/layout choices marked **[judgment]** belong to slides, not a context-free implementation worker. Keep source facts and necessary qualifiers.

### 1. F01 — qualify the attack-selection bridge
- **Where:** S43 / p44, `courses/trustworthy-ai/lec14-agentic-threats-note.html:1021`; S45 / p45, `courses/trustworthy-ai/lec14-agentic-threats.html:1089` and paired note `:1057`.
- **Type:** fact. **Blocking:** yes. **[judgment]**
- **Wrong / why:** “Most control evaluations, including the one we just saw, assume the attacker tries at a fixed random rate” erases Greenblatt's opportunity-seeking attack policy (and contradicts S40's note). S45 then places “Attackers who pick their moment” outside a generic tested envelope immediately after showing a study that tests this. Students cannot tell which result is being qualified.
- **Fix:** replace S43's quoted bridge with: “This study tests task-level start and turn-level stop decisions in multistep agent environments. Earlier code-backdoor attacks already sought favorable opportunities; these tests isolate further selection choices.” Retain the separate metric explanation. On S45 frame the exhibit as **each evaluation's own envelope**, not a universal tested/untested partition: e.g. left “Tested here: tasks, attack policy, audit budget”; right “Re-test when these change: task length, attack selection, monitor attacks.” Update Message/Reading/Script consistently; keep the deployment-limit question.
- **Source:** E29, Greenblatt §1/§3.2; Ge-Wang §2–3/App.A.

### 2. F02 — essential concept labels still too small
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats.html`: S04 / p4 `:104`, S12 / p14 `:338`, S29 / p32 `:782`, S33 / p34 `:826`.
- **Type:** design rule / unmet request C02. **Blocking:** yes. **[judgment]**
- **Wrong / why:** rendered body prose is 24.8px, but S04's box explanations and S12's definitions render at22; S29's central teammate-source explanation at21 and “hidden instruction”/“has tools” at23; S33's hidden-meaning/shared-convention explanation at23. These explain the mechanism, not optional tick labels. DS§1 Priority0 / §8 treats necessary box text as primary.
- **Fix:** bring these essential explanations to body-equivalent size; shorten or move optional annotation instead of squeezing. In S29 “arrives as a teammate's message” is a shorter, more precise replacement for “the source is no longer visible”; disappearance of provenance is not inevitable in every system. Recheck actual transformed SVG sizes and full-size renders. Ordinary axis ticks and nonessential annotation can keep the permitted secondary size.

### 3. F03 — two note tables force horizontal scrolling
- **Where:** `courses/trustworthy-ai/lec14-agentic-threats-note.html`: S41 / p42, table `:974`; S43 / p44, table `:1030`.
- **Type:** design rule. **Blocking:** yes. **[judgment]**
- **Wrong / why:** at430px viewport the document scroll width is488px (client415px); these tables extend beyond the articles. Scrolling to a table shifts the article sideways. DS§9 requires no horizontal overflow.
- **Fix:** reflow each result into vertically stacked labelled records, or split its columns into narrow tables while preserving all values, metric definitions, sample sizes and confidence intervals. No font shrinking and no hiding/clipping data. Verify at430px with horizontal scroll reset and `scrollWidth <= clientWidth`.

### 4. F04 — the off-panel baseline includes H
- **Where:** S42 / p43, `courses/trustworthy-ai/lec14-agentic-threats.html:1068`; paired note `courses/trustworthy-ai/lec14-agentic-threats-note.html:1004`.
- **Type:** fact. **Blocking:** yes.
- **Wrong / why:** “trusted model only (1.0,0.02)” mislabels the no-U point: T alone is normalized to zero usefulness. The2% comes from H writing the first2% of solutions, as S40 correctly explains.
- **Fix:** “trusted model only (1.0,0.02)” → “no U: H then T (1.0,0.02)”; make the note explicit that H writes the first2%, then T handles the rest. Alternatively omit this secondary off-panel detail from main, preserving the correct note.
- **Source:** E25/E29; Greenblatt §3.1.1/Table2.

### 5. F05 — publication year is not experiment year
- **Where:** S33 / p34, `courses/trustworthy-ai/lec14-agentic-threats.html:851–852`; paired note `:790,796,811,816`; S34 citation and lec14 OUTLINE source entry where applicable.
- **Type:** fact. **Blocking:** yes.
- **Wrong / why:** “2025 tests” infers the experimental date from arXiv v5's revision. The publication venue is independently verified as NeurIPS2024.
- **Fix:** main sentence → “Limited success in these tests of models up to GPT-4.” Cite “Motwani et al., NeurIPS2024 (arXiv2402.07510v5, revised2025)” and replace note claims of a2025 experiment/publication with this distinction. Keep the exact inspected v5 numbers and the limit on newer models.
- **Source:** E28 and its official proceedings link.

### 6. F06 — restore the full bottom tick in the METR crop
- **Where:** S54a / p16, `courses/trustworthy-ai/lec14-agentic-threats.html:385`; asset `courses/trustworthy-ai/figs/lec14-finale-refresh/p1-metr-forecast-vs-observed.png`; p1-PROVENANCE and paired note figure description.
- **Type:** design rule. **Blocking:** yes.
- **Wrong / why:** the bottom of the +40% y-axis tick is clipped, explicitly acknowledged in provenance. Cropping must preserve complete labels/data rather than document the damage.
- **Fix:** recapture with enough bottom margin to keep the tick whole, while retaining the current category labels outside the image. Update provenance/note and verify no error-bar extent is lost. Do not repaint the source.

### 7. F07 — make S06 reproducible at final geometry
- **Where:** S06 / p8, `courses/trustworthy-ai/lec14-agentic-threats.html:198`; `courses/trustworthy-ai/figs/lec14-finale-refresh/p1-gen-curves.py:5,17` and p1-PROVENANCE.
- **Type:** design rule / evidence reproducibility. **Blocking:** yes.
- **Wrong / why:** the cited generator emits a different y mapping from the final inline curve. The probability calculation is correct, but rerunning the code does not reproduce the exhibit.
- **Fix:** update the S06 generator to the final intended mapping `X=80+25.5n, Y=295−255*(.95**n)`, regenerate that path, and leave the mapping beside it and in provenance. Preserve the current axis meaning and all assumptions. S09 already matches; leave it unchanged. E24 records the discrepancy; report closure in work-r2.

### 8. F08 — give the unfamiliar labels their meaning
- **Where:** S21 / p25, `courses/trustworthy-ai/lec14-agentic-threats.html:611` and paired note `:554`; S27 / p30, main `:736` and note `:680`.
- **Type:** design rule / audience fit. **Blocking:** yes. **[judgment]**
- **Wrong / why:** the main key requires decoding CSQA/MMLU, and MAST is never expanded in the slide or its introductory note. The course is concept-first for mixed majors.
- **Fix:** S21's external key should explain “CSQA: commonsense questions; MMLU: broad knowledge; WMDP: hazardous-knowledge proxy” in readable phrases (notes can supply full benchmark names). S27 should identify MAST once as “Multi-Agent System Failure Taxonomy”; a short gloss such as “a map of team failures” can accompany it. Replace existing prose rather than adding a dense extra bullet column. Preserve Fig.4's full-MMLU versus Table1's biology-subset distinction in notes.

## Nonblocking cleanup

9. **F09 — stale narration [judgment]**; preference; not blocking. `courses/trustworthy-ai/lec14-agentic-threats-note.html:91`, S52 / p5: replace the “accumulation from two slides ago” paragraph with “The example shows how pricing decisions can lose money over a sustained task; it does not isolate a single cause of the losses.” The compounding slide comes later, and the current paragraph also asserts unchecked decisions too strongly. At S27 / p30 `:701`, “that is the next slide's range” → “the range is retained in the S28 note.” Main S28 no longer shows a range.

## Decisions on work-r1 flags

1. **Generated/source-figure evidence:** E24–E26 appended. S40 generator matches; S09 matches; S06 requires F07. S55/S56 provenance and sources accepted. Copy refreshed evidence unchanged.
2. **Ge-Wang venue:** retain preprint. No workshop-venue claim needed.
3. **Motwani venue/date:** resolved by official NeurIPS2024 record; F05.
4. **Carried claims:** Morris-II, Lynch and Terekhov checked against primary versions; RepliBench limits retained against E08. E27 records decisions. No new study slides.
5. **Vend plots disagree over overlap:** accept one phase-two plot only, no exact dollar comparison, with discrepancy in notes. Do not infer causality or harmonize the curves.
6. **METR19 versus20 rounding:** keep19% from the early2025 result and no replacement effect-size headline from2026.
7. **Small embedded source labels:** enlarged external keys suffice for S53 event-marker interpretation, S11 model points, S14 domain/model/pass-budget reading, and the high-level MAST/Fang/Ge-Wang panels. Students need not read every tiny source label. S54a clipping is different: fix F06. Custom essential labels remain subject to F02.
8. **Weij percentage changes:** accept percentage-point explanation in the note; no table reintroduced on main.
9. **Weij Fig.4 versus Table1:** accept full-MMLU versus biology-subset distinction; do not conflate them.
10. **Unused figures:** leave `figs/mast-taxonomy-fig1.png` and `figs/control-pareto-fig2-legend.png` in this job. Their deletion is unnecessary to Albert's content request; no cleanup scope expansion.
11. **lec13tech wrapper:** still excluded; no edits here.

**Other deviations accepted:**51 main slides,51 matching notes,14 untouched tech slides; S54a/S54b is an expressly permitted readability split.85 teaching minutes +5 flexible =90. No plan-v3 needed: findings correct the implementation/source framing without changing the approved argument or scope.

## Verification record

Reviewed immutable `git archive` of the exact SHA, not a working tree. All51 main pages rendered at1280×720 and visually inspected; full-size checks of source figures/control/frontier pages, source/alt/key/note consistency, all51 note texts, and narrow-note overflow checks. Main: no detected overflow or missing images; local references valid; main/note ID order matches. S40 generator verified against inline XML; S09 path matches; S06 arithmetic checked independently.

Main lint: five source-color warnings on S14; notes lint passes. Dense-slide flags reviewed visually: source keys/necessary qualifiers and readable layouts retained, not mechanically deleted. Lec14 OUTLINE pointers/counts match. Outline-lint's unrelated missing absolute lec09 build-script pointer and ambiguous basenames are pre-existing; do not expand scope.

For round2 recheck changed slides and their neighbours, their paired notes, the two narrow tables, regenerated/cropped assets, and any shifted outline pointers. Do not rebuild unaffected sections or add literature. Return work-r2 with every F01–F08 disposition and an exact commit; F09 is optional. If a blocking finding is disputed, explain it in work-r2 rather than silently dropping it. Approval/PR remain pending; no merge authorization.
