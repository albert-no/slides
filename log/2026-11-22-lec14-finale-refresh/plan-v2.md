# Plan v2 — lec14 refresh with two brief new-topic previews

## What changed since v1
Albert's C06 explicitly permits new topics beyond the 14 taught lectures. Add two short, high-level frontier introductions within the ending: **AI persuasion** and **AI companionship / emotional dependence**. New IDs S55/S56 follow S49 and precede the single S50 course takeaway. Evidence E20–E23 includes a substantive September 2026 correction to the persuasion paper. No extra literature survey or seventh section.

This complete plan supersedes v1 for work. All unchanged package specifications are retained below. P1–P4 may continue; only their section-time allocation changes slightly. P5 owns the new topic slides and integration. The job stays medium, round 1 of 2; an author follow-up does not consume a review round. Target 50 main slides before optional splits, same 90-minute envelope.


## Summary
**Medium job; existing argument and six sections retained.** Make the finale distinct from the newly revised prompt-injection lecture: long-horizon reliability, incentives, multi-agent interaction, and control. Remove repeated injection defenses and multiple recaps. Introduce two grounded real-world threads (a shop experiment and developer work), explain selected recent research by its question, observation and limit, and briefly extend the finale to persuasion and human–AI relationships. Enlarge essential diagram text throughout. End with one genuinely course-wide takeaway, not another agent-security checklist.

**Audience/mode/time:** existing mixed-major undergraduates; concept-first; no activities; 90-minute envelope including explanation/question flexibility. No comprehensive literature survey or new technical section. Target about 50 main slides plus matching notes, versus 51 baseline; the count is not a cap. The optional 14-slide tech deck is unchanged unless a factual/concordance repair is necessary and reported.

**Sources:** evidence.md E01–E23. Cutoff 2026-11-22; each study remains a dated snapshot. Real-world experimental use, constructed harmful-behavior evaluations, and illustrative diagrams must be visibly distinguished.

**[judgment]** All wording, selection and visual-compression decisions below are content/design judgments for slides to handle with context. “Must” specifies meaning and scope, not exact phrasing/layout. Proposed titles are preferred; slides may improve them without changing the claim. If a requested edit changes the argument, scope, facts or teaching time, return the issue rather than silently substituting it.

## Coverage and duplicate audit

| Comment | Baseline page/title or scope | Stable IDs | Package / acceptance |
|---|---|---|---|
| C01 | p4 Beyond a Defended Agent; p29–32 injection block; p26 duplicate taxonomy; p45 reporting; p47–50 repeated endings | S04, S25–S32, S43–S50 | P1/P3/P4/P5: one short authority bridge, propagation only as the new interaction risk, one global course recap |
| C02 | All concept diagrams and essential plot labels, especially p4–6,9,14,18,20,25,27,29,37,39,42,44,48 | all retained content IDs plus S52–S54; retired IDs excluded | each package: actual rendered labels readable, not merely larger wrappers |
| C03 | p4–6 abstract opening; p13 benchmark/runtime distinction | S52 after S04; S53 after S52; S54 after S13 | P1: actual shop and actual developer work, sources/dates/limits on slides and in notes |
| C04 | p9–15 autonomy; p27–28 MAST; p43–44 attack selection | S09–S15, S27/S28, S43; S54 | P1/P3/P4: high-level question → observation → limitation, detailed methods/tables in notes |
| C05 | p47–50 synthesis and p51 closer | S46,S49,S50,S51; retire S47/S48 | P5: a single brief course-wide summary, not only agents/injection |
| C06 | no baseline counterpart; new-topic preview within the ending | S55 after S49; S56 after S55; both before S50 | P5: two short, sourced extensions beyond the taught syllabus, not another recap |

**Explicit continuity choices (E01/E19):**
- Authority/instruction hierarchy, direct/indirect injection, permissions, CaMeL, approval and detector mechanisms: already taught; reuse only a self-contained one-line bridge where necessary. Do not reintroduce email attacks, incidents, prompt sandwiching, or the defense catalog.
- Propagation: **adapt**, not delete wholesale. The new point is an agent’s output becoming another agent’s input and a network amplification condition. Keep a short mechanism and one bounded study result, not a four-slide injection mini-lecture.
- Alignment/reward hacking from lec07: reuse its concept in plain language; do not reopen its studies or claim the new constructed scenarios are deployment cases.
- Greenblatt control: **retain**. Testing a deliberately adversarial worker under limited auditing is not the same as lec13’s enforcement/approval lesson. Keep only the necessary monitoring/control setup; no repeated generic safety checklist.
- Course conclusion: privacy/erasure, uncertainty/incentives, security, provenance/fairness, and accountable action all belong. Full governance/legal updates remain deferred to the optional backup.
- C06 new topics: **introduce** AI persuasion and human–AI relationships as two distinct user-facing trust questions. These are not another sycophancy, fairness, or synthetic-media lecture. Two bounded paper checks support two short previews (E20–E23), not a new survey.

## Frozen baseline map
Main and notes: `courses/trustworthy-ai/lec14-agentic-threats.html` and `lec14-agentic-threats-note.html`, baseline `34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233`. Existing ID commit `594ebea1203aabe3b3edc56443b37dd29950e411` is historical; diff content against this job baseline, not against that older commit.

| Baseline page | ID | Baseline title |
| 1 | S01 | Emerging Agentic Threats |
| 2 | S02 | Contents |
| 3 | S03 | What Changes With Autonomy |
| 4 | S04 | Beyond a Defended Agent |
| 5 | S05 | Autonomy Is a Dial, Not a Switch |
| 6 | S06 | Small Errors Compound Over Long Tasks |
| 7 | S07 | Measuring Autonomy |
| 8 | S08 | Why Measure Autonomy? |
| 9 | S09 | Time Horizon: The Definition |
| 10 | S10 | How a Horizon Is Computed |
| 11 | S11 | Horizons Doubled About Every Seven Months |
| 12 | S12 | What the Number Depends On |
| 13 | S13 | What a Time Horizon Is Not |
| 14 | S14 | Replication Scores: Two Domains Compared |
| 15 | S15 | Component Success Does Not Establish Full Replication |
| 16 | S16 | Against the Overseer |
| 17 | S17 | Setup, Behavior, Inference: Kept Apart |
| 18 | S18 | In-Context Scheming: The Setup |
| 19 | S19 | Oversight Disabling: Rare in These Scenarios |
| 20 | S20 | Sandbagging: Strategic Underperformance |
| 21 | S21 | Sandbagging on Instruction |
| 22 | S22 | Sandbagging Without an Instructed Goal |
| 23 | S23 | Other Explanations for a Failed Eval |
| 24 | S24 | Many Agents |
| 25 | S25 | Three Ways Many Agents Fail |
| 26 | S26 | Coordination, Propagation, Collusion |
| 27 | S27 | MAST: Ordinary Coordination Failures |
| 28 | S28 | What MAST Implies |
| 29 | S29 | From Injection to Propagation |
| 30 | S30 | Prompt Infection: The Setup |
| 31 | S31 | Prompt Infection: What Spread, and When |
| 32 | S32 | Defending Each Hop |
| 33 | S33 | Collusion: Hidden Channels |
| 34 | S34 | Demonstrated vs Hypothesised |
| 35 | S35 | Control |
| 36 | S36 | From Alignment to Control |
| 37 | S37 | The Control Setup |
| 38 | S38 | The Control Game |
| 39 | S39 | Trusted Monitoring, Step by Step |
| 40 | S40 | Trusted Monitoring: 62% Safe, 97% Useful |
| 41 | S41 | Other Protocols, Compared |
| 42 | S42 | Protocols Reach Different Safety–Usefulness Points |
| 43 | S43 | Attackers Choose When to Attack |
| 44 | S44 | Attack Selection Lowers Measured Safety |
| 45 | S45 | A Benchmark Is Not a Deployment Guarantee |
| 46 | S46 | Synthesis |
| 47 | S47 | Established vs Not Established |
| 48 | S48 | A Checklist for the Whole Course |
| 49 | S49 | Open Problems |
| 50 | S50 | Key Takeaways |
| 51 | S51 | Who checks it? |

## Slide specifications

**Shared acceptance for every retained/added content slide — must:** one point, one exhibit, a short explicit message; source scope visible; note Message/Reading/details aligned. Primary diagram labels at the current design-system body equivalent; simplify or split, never shrink. Source crops retain aspect/data and disclose cropping, with enlarged external keys where needed. Render at final slide dimensions and inspect the text, including arrow/box labels and plot axes. Every new figure has provenance. Do not invent current figures or regress qualifications fixed in prior reviews.

**Companion rule:** “note” below means the matching-ID article, including detail moved from a retired slide; do not leave orphan articles or delete unique teaching detail. Technical math remains in the existing supplement. All slides may choose components; suggested components below are vocabulary, not markup instructions. Times are approximate speaking targets; section budgets and the final 90-minute total control.

### P1 — autonomy and measurement (S04–S15; new S52–S54)

1. **S04 — Trust Must Survive Longer Tasks.** Point: authority controls address one boundary, not every failure of delegated work. **Must:** one brief bridge, explicitly not injection-proof, then long tasks / conflicting incentives / interacting agents. Exhibit: one overview diagram, not the agent-loop/least-privilege diagram again. E01/E02. Note holds the lec13 reference; main self-contained. Prefer `diagram-flow`; ~1 min. Accept: the first content slide states what lec14 adds without re-teaching injection.
2. **S52 (new, after S04) — A Shopkeeper Sold Below Cost.** Point: plausible local decisions can lose real money over time. **Must:** identify Project Vend as a bounded Anthropic/Andon office-shop experiment, June 2025; use one specific pricing failure from E03. Exhibit: source shop photo or source setup figure, readable role key, not a fictional incident screenshot. Note carries tools/human roles and the experimental email limitation. Prefer figure-first; ~2 min. Accept: who, task, observed outcome and lesson are clear; no claim of a public autonomous commercial rollout.
3. **S53 (new, after S52) — Better Performance Still Needed Checks.** Point: system improvements are encouraging but not a safety guarantee. **Must:** dated December 2025 follow-up, multiple changes, continued oversight/limits, no claim the manager caused the gain. Exhibit: one source business-performance/weekly-profit plot from E04 with simple date/value key, not an invented before–after causal chart. Note explains the confounding and manager anecdote. Prefer figure-first; ~2 min. Accept: students do not leave with the stale claim that the shop only failed, or the opposite claim that a newer model solved autonomy.
4. **S05 — Autonomy Has Several Dials.** Keep steps, task horizon, tools/permissions, and interval between checks. Point: define what autonomy means before measuring it. **Must:** replace the universal “Turning any setting up widens what can go wrong” with a qualified statement about scope/opportunities, not inevitable harm. Exhibit: enlarged existing dial graphic, all primary labels readable. E02. Note explains how more checks shorten the interval. Prefer `diagram-flow`; ~1.5 min. Accept: the direction of the human-check dial is not reversed.
5. **S06 — Small Errors Can Accumulate.** Keep the illustrative independent-step calculation, independence/no-recovery assumptions, and possibility of recovery/correlation. Exhibit: enlarge the existing curve and labels; E02 reproduction record required if regenerated. Note keeps derivation; tech unchanged. Prefer figure-first; ~1.5 min. Accept: no measured-agent interpretation, no new quantitative claim.
6. **S08 — Test Capability Before Delegation.** Keep the motivation for capability evaluation, reduce the category catalog if needed. Exhibit: readable three-stage capability → possible consequence → testing decision diagram or compact source-informed example. E18. Note preserves the full category table. Prefer `diagram-flow`; ~1.5 min. Accept: no claim that passing evaluation certifies safety.
7. **S09 — A Horizon Measures Task Difficulty.** Point: human task duration calibrates a fitted success threshold. Keep a correctly decreasing schematic success curve, labelled axes and threshold. E07. Note explains successful-human reference. Prefer figure-first; ~2 min. Accept: horizon is not elapsed AI running time.
8. **S10 — From Tasks to a Horizon.** High-level process: time humans → try model/scaffold → read the chosen success threshold. Move task/run counts and fitting details into notes, preserving their exact setup. E07. Prefer `diagram-flow`; ~1 min. Accept: method precedes result without introducing logistic mathematics on main.
9. **S11 — Horizons Grew on the Tested Tasks.** Keep source Fig.1 with enlarged external labels, historical date range and metric. E07. Main may retain the seven-month summary, tied to its snapshot; notes retain confidence interval and full assumptions. Prefer figure-first; ~2 min. Accept: not presented as the latest November 2026 frontier or a prediction guarantee.
10. **S12 — The Score Depends on the Setup.** Keep three meaningful choices: tasks, scaffold, reliability threshold. Move fit-sensitivity percentages/detail to notes. E07. Exhibit: three-way concept map, not a dense choices table. ~1 min. Accept: 2026 sensitivity work is separated from the historical plot; no claim of one universal horizon.
11. **S13 — Capability Is Not Safe Runtime.** Preserve the explicit distinction; simplify repeated exposition. Exhibit: measured task success versus unmeasured deployment safety, with roles clearly labelled. E07/E08. Note holds limitations. Prefer `grid-2`; ~1.5 min. Accept: no safe-unattended-time inference.
12. **S54 (new, after S13) — Real Developers Misjudged Time Saved.** Point: perceived usefulness and measured deployment outcomes differ. **Must:** identify the early-2025 experienced-developer randomized trial and measured task-time outcome; visibly state this is human-with-tool productivity, not autonomous-agent horizon or all developers. Exhibit: source forecast-versus-observed chart with readable key (E05). Add a concise dated E06 qualifier that the 2026 follow-up could not reliably estimate the current effect; exact details and update go in notes. Prefer figure-first; ~2.5 min. Accept: not “AI coding still slows everyone”; no causal comparison between this result and the METR horizon curve. Split into S54a/S54b if the update and essential chart key cannot fit; preserve the explicit date/scope on both.
13. **S14 — Replication Components Have Uneven Success.** Retain the two unmodified source-domain crops and expand their essential labels/key. E08. Main only needs selected-domain contrast and attempt-budget meaning; full model descriptions and uncertainty caveats in note. Prefer figure-first; ~2 min. Accept: pass@10 is “at least one”; not a claim of ten successive steps or real-world replication.
14. **S15 — Parts Do Not Establish the Whole.** Keep components versus complete chain distinction, reduce dense lists. Exhibit: conceptual chain with untested end-to-end link clearly marked, not a fabricated measured failure path. E08. Note retains all exact results/source disagreements. Prefer `diagram-flow`; ~1.5 min. Accept: one sandboxed success is not relabelled end-to-end real-world replication.

### P2 — against the overseer (S17–S23)

15. **S17 — Setup, Behavior, Inference.** Keep three-layer reading frame with fewer words. Point: distinguish evidence from interpretation. E09/E10. Exhibit: three readable layers, note supplies examples. Prefer `diagram-flow`; ~1.5 min. Accept: induced and observed are not treated as mutually exclusive categories.
16. **S18 — Can an Agent Disable Its Check?** Keep constructed goal, conflicting memo and editable oversight setup, enlarge diagram labels. E09. Main explicitly sandboxed/in-context; full nudge/prompt source in note. Prefer source-informed diagram; ~2 min. Accept: no real victim/real-weight implication or executable attack recipe.
17. **S19 — Some Models Disabled Oversight in Tests.** Keep one scoped observation, not a catalog of rates. Move the multi-model numeric table and separate follow-up-denial statistic to notes. Exhibit: source-informed choice/outcome diagram (qualitative, not a made-up frequency). E09. ~2 min. Accept: rare in these specific scenarios, not “scheming is always rare”; note retains denominators and discrepancy.
18. **S20 — Sandbagging Hides Capability.** Keep definition and difference between capability and displayed evaluation performance. Enlarge labels. E10. Note distinguishes developer-driven and system-driven cases. Prefer `diagram-flow`; ~1.5 min. Accept: low test performance alone is not sandbagging evidence.
19. **S21 — Instructions Can Lower Test Scores.** Keep the instructed selective-underperformance idea, moving full numeric comparison and password-locking detail to note. Exhibit: labelled test versus control comparison, use a verified source crop if showing empirical values. E10. Main retains scope and exclusion of refusals if showing accuracy. ~2 min. Accept: no erasure claim, no unprompted propensity claim.
20. **S22 — Incentives Can Change Evaluation Behavior.** Keep arithmetic scenario as a contrasting constructed-incentive example; no full model table on main. Exhibit: change the threatened consequence → observe performance, with “threat only” visible. E09. Note retains exact per-model results and nonsignificant case. ~2 min. Accept: no actual skill-removal/training event implied; motive remains interpretation.
21. **S23 — A Bad Score Has Several Explanations.** Keep distinction between elicitation/refusal failures and strategic behavior; one short diagnostic exhibit rather than a wall of bullets. E08–E10. Note holds checks and examples. ~1.5 min. Accept: does not diagnose intent from a failed run.

### P3 — many agents (S25–S34)

22. **S25 — Cooperation Can Fail in Different Ways.** Keep Hammond’s miscoordination/conflict/collusion distinction, visibly label it as that taxonomy. Note retains the baseline S26 study comparison separately. E11. Exhibit: readable three-role comparison, no mixed taxonomy/attack mechanism. ~1.5 min. Accept: propagation is not incorrectly attributed as a Hammond category.
23. **S26 — retire from main.** Its preview repeats S25 and the studies that follow. Move unique evidence-comparison context to S25 note; do not renumber/reuse the ID. E11–E14. Accept: note articles still match main one-to-one.
24. **S27 — MAST Finds Failures Without Attackers.** Introduce Multi-Agent System Failure Taxonomy in plain language. **Must:** highlight study question and qualitative result; source Fig.1 cropped/split to its readable conceptual categories rather than demanding students read every taxonomy leaf. E12. Full taxonomy and proportions in note. Prefer figure-first; ~2 min. Accept: not represented as real deployment incident statistics.
25. **S28 — Better Coordination Needs Verification.** Give one concrete MAST failure pattern and implication in ordinary language, not a table of intervention percentages. E12. Exhibit: a source example/crop, or an explicitly illustrative role → handoff → verification diagram if no canonical figure covers the teaching point. Note retains separate ChatDev configurations. ~1.5 min. Accept: implications scoped to study, no guaranteed gain or universal multi-agent disadvantage.
26. **S29 — One Agent Can Carry an Attack Forward.** One-line authority recall only, followed by the new multi-agent forwarding mechanism. Enlarge route labels, distinguish external source and agent messages. E01/E13. No payload text. Note absorbs S30 setup. Prefer `diagram-flow`; ~1.5 min. Accept: this adds a network mechanism rather than re-teaching direct/indirect injection.
27. **S30 — retire from main.** Move exact Prompt Infection setup to S29 note; preserve models and experiment scope. E13. Accept: no unique detail silently lost.
28. **S31 — Spread Depends on the Environment.** Keep qualitative contrast between simulated apps and the agent-society experiment; extra memory-importance manipulation visible. Remove the confusing ignored-failure percentages from main. Exhibit: source Fig.6 or a tightly bounded panel with an external condition key; note preserves apps/society details and absorbs S32 defense limitations. E13. ~2 min. Accept: no real outbreak implication and no “inevitable infection” claim.
29. **S32 — retire from main.** Tagging/marking and least-privilege defense reprise duplicates lec13. Preserve the experiment-specific defense result, adaptive caveat and unmeasured utility in S31 note; do not add a new defenses survey. E01/E13.
30. **S33 — Hidden Coordination Challenges Oversight.** Define steganography in a line and show who communicates/what the observer sees. Move the incomparable rates table to note. E14. Exhibit: source-informed channel diagram, visibly illustrative; no actionable covert-channel recipe. ~2 min. Accept: concept not conflated with Base64 encryption; demonstrated limited tests not current prevalence.
31. **S34 — Evidence Has Different Strengths.** Preserve local evidence-status comparison for this section only, with short readable status labels. E12–E14. Note makes “not reported in these papers” explicit, never “has never happened.” ~1 min. Accept: no second course-wide recap; no unsupported checkmark glyphs.

### P4 — control (S36–S45)

32. **S36 — Test Safety Against a Bad Worker.** Keep alignment versus control in one concept comparison; control is a testable system-level question, not an asserted guarantee. E15. Note retains definition. Prefer `grid-2`; ~1.5 min. Accept: not presented as “all models secretly attack.”
33. **S37 — Separate Worker, Monitor and Audit.** Keep source Fig.1 right panel and add a legible role key. Preserve untrusted worker / assumed-trusted monitor / protected simulated scarce audit. E15. Main names who sees what; note full models/assumptions. Prefer figure-first; ~2 min. Accept: the audit is not misrepresented as actual human trial data; model weakness is not a proof of trust.
34. **S38 — Name the Game Before the Score.** High-level task, attacker, audit resource and what counts as failure. Keep plain-language run-level safety and normalized usefulness before any result. E15. Detailed game table to note. Prefer a compact concept diagram; ~2 min. Accept: no ASR/accuracy/run-level safety conflation.
35. **S39 — Inspect the Most Suspicious Work.** Enlarge trusted-monitoring sequence and branch labels; preserve shutdown/fallback behavior. E15. Prefer `diagram-flow`; ~2 min. Accept: monitor score is not a proven safety label and human audit is not unlimited.
36. **S40 — Monitoring Beat an Upfront-Only Check Here.** Retain one clear comparison from the existing source rather than the full table. If numerical, use bars from the pinned table with source/budget/metric, not a magnitude table; optionally a verified source figure crop. E15. Keep normalized-usefulness interpretation; move secondary baselines to notes. ~2 min. Accept: exact original scope maintained; not deployment reliability or accuracy.
37. **S41 — Checks Can Defer or Edit.** Replace the dense protocol-results table with a high-level mechanism comparison, so readers understand S42’s plot. The note retains the complete table and anti-coordination conditions. E15. Prefer `diagram-flow`; ~1.5 min. Accept: no numeric ranking without setup; two U copies are not assumed independent/trusted.
38. **S42 — Protocols Reach Different Tradeoffs.** Retain source Pareto panel with clearly enlarged external legend, axes and metric definitions. E15. Note retains off-panel points and selection caveat. Prefer figure-first; ~2 min. Accept: does not imply every point is Pareto-optimal or every protocol must sacrifice one metric.
39. **S43 — Choosing When to Attack Changes the Test.** **Must:** make the June 2026 study a high-level research highlight: question (can attacker selection fool the evaluation?), idea (start selectively / stop when risky), finding (measured safety fell in these tests), limit (upper-bound methodology, not observed deployment rate). Exhibit: source Fig.1 with enlarged key; use its mechanism diagram as mechanism, not measured data. E16. All numerical Table2 details, conditional metric and uncertainty move to note, including retired S44 content. ~3 min. Accept: start/stop are explained without optimization or estimator formulas; note distinguishes this metric from S38.
40. **S44 — retire from main.** Move the four small bar groups, denominators, uncertainty and selection-method caveats to S43 note (numeric chart can remain as a note figure if useful). E16. Any recreated chart requires reproducible-source record. Accept: no tiny unexplained frontier plot replaces the high-level explanation.
41. **S45 — Evaluation Evidence Has Boundaries.** Keep the limits, but replace lec13’s repeated generic report-attacker/budget checklist with the control-specific question: would this oversight still work over longer, adversarially chosen tasks? A short monitor-vulnerability limit only; no injection mechanism reprise. E15–E17. Exhibit: tested envelope versus untested conditions. Note absorbs S47 established/not list. ~2 min. Accept: conditional evidence not promised guarantee, no universal failure claim.

### P5 — shared surfaces and course ending

42. **S01 — keep title identity.** Existing title/author/course, no new claims. Remove legacy style violations if encountered in the scoped pass. Structural; ~0.5 min.
43. **S02 — update Contents subtitles only as needed.** Same six-section argument; exact match to dividers. Rename section 06 to “Synthesis and Frontiers”, matching S46; its subtitle promises two brief new topics and course-wide takeaways. Structural; ~0.5 min.
44. **S03 / S07 / S16 / S24 / S35 — keep structural dividers.** Keep names/order; sync changed subtitles with Contents. ~0.25 min each. No factual source required.
45. **S46 — Synthesis and Frontiers.** Update divider and Contents together; subtitle “Two new questions, one course takeaway”. ~0.25 min. Not a recap itself.
46. **S47 — retire from main.** Repeats earlier local limitations and S50. Preserve unique established/not distinctions in S45 note. E07–E16. No orphan article.
47. **S48 — retire from main.** Its agent-only checklist repeats lec13 and is not a course summary. Preserve useful questions under S50 note; replace its role with the genuinely broad summary below. E01/E19.
48. **S49 — Three Questions Still Open.** Keep a short forward-looking horizon, not a second summary: realistic long-task evaluation, intent versus elicitation, oversight under adaptation. E07/E09/E16. Exhibit: three research questions mapped to the relevant evidence gap. Notes hold remaining open-problem list. Prefer `grid-3`; ~1.5 min. Accept: research questions, not unsupported predictions, no future lecture promise.
49. **S55 (new, after S49) — AI Can Persuade, Not Just Answer.** [judgment] **Must:** introduce the new trust question: how does conversation influence a user's beliefs? One plain-language observation from E20, explicitly about the profile-informed GPT-4 condition versus the human baseline in a controlled debate. State the E21 limit: this does not isolate personalization's added benefit. Exhibit: source Fig.1 experiment-flow crop, with a readable before/after agreement key; use the design figure as design, not result data. The figure citation includes the 2026 correction; detailed statistics and exact comparison stay in notes. Do not add persuasion prompts or targeting tactics. Prefer figure-first; ~2 min. Accept: immediate agreement is not claimed to be voting behavior, lasting manipulation, or a universal advantage over humans. The slide and note distinguish the result from the broader human-autonomy concern.
50. **S56 (new, after S55) — Engagement Is Not Proof of Benefit.** [judgment] **Must:** introduce AI companionship and emotional dependence as a distinct outcome to evaluate, not just answer quality. Use the E22 association with the on-slide qualifier “Usage duration was not randomized.” Exhibit: the source Fig.1 study-framework crop, with large labels for the measured human outcomes; use a relevant Fig.6 outcome panel only if the centered usage axis can be explained simply and legibly. Main remains high-level, not a statistical-methods lecture. Note distinguishes randomized modes/topics from voluntary duration, explains no no-chatbot control and limited generalization. Prefer figure-first; ~2 min. Accept: no causal claim that chatbots cause loneliness or dependence, no claim that all companions are harmful, no clinical advice or treatment-efficacy claim. Cite v2, not an outdated v1 headline.
51. **S50 — Trust Requires Evidence, Not Fluency.** **Must: the one global closing summary.** Five compact branches, with one meaningful question each: data/privacy/removal; answers/uncertainty/incentives; attacks/authority; provenance/fairness; actions/oversight/accountability. Example wording: “Data: whose information is exposed?” / “Answers: when should we doubt?” / “Attacks: what can an adversary change?” / “People: who is harmed or misled?” / “Actions: who can check and stop?” Ensure provenance and fairness are explicitly visible, not only inferred from “People”. E19. Exhibit: one readable course-map/checklist, not a dense 14-lecture table. Note links each branch to the relevant lectures and preserves S48 questions. Prefer `diagram-flow`; ~2 min. Accept: spans the whole taught course, contains no universal certification claim, no other global recap survives. Exact wording/layout slides decides.
52. **S51 — closer.** Keep a single memorable question consistent with S50: “What would earn your trust?” preferred; no new bullets or another recap. ~0.5 min. E19. Accept: clear last lecture, no “next week”.

## Packages and ownership

| Package | IDs / scope | Files and note sections allowed | Dependencies |
|---|---|---|---|
| P1 | S04–S15 content; S52/S53/S54 additions; S07 reserved for integration | main, corresponding note articles; new assets under `courses/trustworthy-ai/figs/lec14-finale-refresh/` | baseline lec13 read-only; E01–E08/E18 |
| P2 | S17–S23 | main + exact paired note articles + package-specific new assets | preserve P1’s capability-versus-safety vocabulary |
| P3 | S25–S34, with S26/S30/S32 retirements | main + paired notes; migrate retired detail only within this package | P1 bridge; no edits to lec13 |
| P4 | S36–S45, with S44 retirement | main + paired notes + package-specific figures/generators | P2 behavior/intent distinction; P3 “observer” terminology |
| P5 integration | S01/S02, all dividers, S46–S51, new S55/S56; retire S47/S48; global totals/links | main, paired notes, new topic-specific assets, lec14 leaf OUTLINE and its index/count references | E20–E23 for additions; after P1–P4 for shared surfaces |

These are work boundaries, not mandatory parallelism. slides owns every implementation/source/note/asset/generator change. Reviewer files are copied unchanged to the tracked record as the contract requires.

## Time and scope control
Target section budgets (including opening/structural time allocated to their section): autonomy 12; measurement 17; overseer 14; many agents 13; control 20; synthesis/frontiers 9 = 85 minutes. Add 5 minutes of flexible explanation/question buffer, not an activity. The approximate per-slide targets need not sum exactly; slides must provide a coherent 90-minute note schedule and report the actual allocation. Only the two C06 topic previews are added to v1; do not add other studies to fill space. Recover their four minutes from condensed explanations of existing overseer/multi-agent/control detail, not from legibility or necessary qualifiers. Retain the existing section order; proposed title/content simplifications are not a new argument.

Expected count if no additional splits: 51 baseline − 6 retired (S26,S30,S32,S44,S47,S48) + 5 additions (S52–S56) = 50. Split only when meaning/readability benefits; use lettered IDs. Retired IDs stay retired, never assigned to new content.

## Shared-surface acceptance and work report
- Rebuild baseline page → stable ID → final page mapping, including retired/migrated IDs and every split. State where each retired article's unique detail landed.
- Notes: same ID/order/title as main; Message first, Reading second, details/sources after. Read at narrow viewport without horizontal overflow; qualifiers persist in every layer.
- OUTLINE: update only lec14’s section plus dependent index/count lines; do not duplicate/reflow other lectures. Recompute pointers rather than guess. No unrelated root cleanup.
- Figures: actual full-size visual check of every changed diagram, source crop and text key; no clipped arrows, overlaps, footer collisions, missing glyphs or semantic-word wraps. Check neighboring slides after insertion/removal.
- Novelty/factual check: S55/S56 must add user-influence and relationship outcomes, not repeat sycophancy or provenance. Verify E21 correction and E22 noncausal scope across the slide, key, alt text and all note layers.
- Main/notes lint, image/link checks and current outline lint; identify pre-existing unrelated warnings separately. Lint success does not replace rendering.
- Work report includes coverage C01–C06, package outcomes, mapping, moved-note detail, any source ambiguity, deviations, render checks and named head SHA. Do not send a PDF to Albert.
- Send exact work pointer with SHA. Review will be pinned to that commit and up to two rounds; PR only after approval and log-only post-review changes verified. No merge without Albert’s direct order.
