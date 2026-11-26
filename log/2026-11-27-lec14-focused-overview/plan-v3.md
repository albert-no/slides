# lec14 focused overview — plan v3, course-redundancy amendment

## Changes since v2
1. **[judgment; author-directed] C11 adds a course-wide redundancy check.** E21 records the inventory of lec01–lec13 at the frozen baseline and the closely read overlapping sections. Biggest overlaps are lec07 (alignment/emergent misalignment), lec10 (fine-tuning, context and monitoring) and lec13 (agents, permissions and approval); lec08/09 supply related hidden-feature/backdoor ideas.
2. **Move four standalone generic slides to actual backup slides:** S13, S62a, S62b, S79. Retain their notes and needed prerequisites. Do not delete baseline material or compress the new experiment's setup/result/limits onto fewer pages.
3. **Adapt remaining overlap to a new question, not new icons.** The shop is an application of known permissions to ordinary commercial mistakes; the training story is about transfer through numeric data and token-score feedback; the control story is a particular adversarial workflow experiment with a scarce audit budget.
4. Target **59 main + 47 backup slides**, with splits allowed. Teaching time remains **85 + 5 = 90 minutes**. Freed minutes go to understanding the new experiments, not additional topics.
5. This is an **in-flight amendment**, not a review. Round stays 1 of 3. No work-r1 commit has been received.

## Authority and scope
- Job/branch: `2026-11-27-lec14-focused-overview`; baseline `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`.
- Albert's message 20, 2026-11-27 01:23 KST, is C11. It refines the approved scope; no new topic or longer duration is proposed.
- **This file plus the unchanged specifications in plan-v2.md is the complete current order.** v2 remains frozen. Where this file changes a title, point, destination, time or acceptance criterion, v3 takes precedence; all other v2 source qualifications, exhibits, notes, baseline preservation and design requirements remain binding.
- English, mixed-major undergraduate finale; three topics; no activities; high-level explanation, not derivations. Main count is not a cap or a quota.
- No edits to lec01–13, their companions, other talks, reference/, global styles or unrelated scripts.
- M = `courses/trustworthy-ai/lec14-agentic-threats.html`.
- MN = `courses/trustworthy-ai/lec14-agentic-threats-note.html`.
- B = `courses/trustworthy-ai/backup-lec14-agentic-threats.html`.
- BN = `courses/trustworthy-ai/backup-lec14-agentic-threats-note.html`.
- All main/backup instructions apply to the article with the same ID in its paired note. Actual new source-line numbers do not exist yet; identify targets by stable ID and the v2 target page supplied below, then report final page/line mapping.

## Resolve C02/C09/C11 together [judgment]
**More explanation of the new problem; less re-teaching of old prerequisites.**
- A short, self-contained Recall statement may reuse a fact needed to understand the next study step. Name the content on the slide, not “lec07” or “as we saw.” File/page cross-references belong in instructor notes and OUTLINE.
- Keep separate slides for a genuinely new setup, intervention, comparator, score, result and limitation. These are different teaching steps, not redundant topics.
- Do not retain a standalone slide whose only point repeats an earlier lecture or another lec14 summary. Move the actual slide to backup, not merely its text into notes.
- Background unfamiliar to this audience still needs an explicit introduction. “Already taught” does not authorize unexplained shorthand, deleted controls or missing caveats.
- The concluding course-wide synthesis S50 is an intentional exception: one summary, not thirteen mini-recaps.
- Do not add copies of the earlier lectures to the backup. The backup preserves material displaced from lec14.

## Evidence and coverage
Use **E21** for exact earlier filenames, pages, IDs and lines; **E22** for the curricular decisions. Neither replaces the primary studies E02–E19 as evidence for scientific claims.

| Request | Resolution |
|---|---|
| C01/C03/C06 | Three new case-study questions rather than a repeated survey of capability, alignment, attacks and defenses. |
| C02/C05 | Brief known-prerequisite recall; detailed new study background, controls and reading guides. |
| C04/C07 | Retain verified Cloud/Askin results; make the incremental contribution beyond lec07/08/09/10 explicit. |
| C08 | All four newly displaced targets become actual backup slides with matching notes; all v2 baseline-preservation obligations remain. |
| C09 | Keep stepwise construction of novel experiments; no denser replacement slides and no slide-count cap. |
| C10 | Existing build authorization stays valid; no new scope gate. |
| C11 | Cross-lecture map E21; required slide changes below; work report and review include explicit novelty/reuse dispositions. |

## Numbered changes to v2

### 1. Move redundant capability recap — S13 [judgment; must]
- **Files/location:** M/MN, v2 p15 → B/BN, immediately after S88 (v2 backup p11). Keep ID S13.
- **Current → new:** Main “Capability Is Not Safe Delegation” → optional “Recall: Capability and Delegation.”
- **Point/exhibit/evidence:** Retain v2's capability-versus-authority comparison and E01/E13. S88 continues to preserve the baseline horizon-specific interpretation; do not remove it or substitute this generic recall for it.
- **Notes/tech:** Move the matching S13 explanation to BN; no new tech content.
- **Time:** 1.5 main minutes removed; add 0.5 each to S52b, S53a and S58a.
- **Reason:** lec01 p38–40 and lec07 p5 already teach scoped trust/capability distinctions; main S04 plus the shop narrative already carry the point.
- **Acceptance:** No second standalone capability-not-safety summary in the main deck; both S13 and S88 remain distinguishable optional backup content.

### 2. Move the generic context/training primer — S62a/S62b [judgment; must]
- **Files/location:** M/MN, v2 p20–21 → B/BN, after divider S16 and before S17. Keep both IDs.
- **Current → new:** “A Prompt Is Context” / “Training Changes Future Responses” → optional “Recall: Context Without Weight Updates” / “Recall: Fine-Tuning Changes the Model.”
- **Point/exhibit/evidence:** Preserve the two v2 diagrams and qualifications, E01/E04/E05. Context can change behavior without changing weights; fine-tuning changes the model used at later evaluation.
- **Main prerequisite:** A brief Recall on S63a identifies an actual fine-tuning intervention. S66b explicitly shows the learner weight update and later test; S71 makes the essential runtime/training distinction once in the new study's context.
- **Notes/tech:** Move their explanations to BN; MN's relevant study setups retain the necessary short explanation and prior-course note references. No new tech.
- **Time:** Remove 2 main minutes; add 0.75 to S67a, 0.75 to S69b and 0.5 to S72a.
- **Reason:** lec05 p8 and lec10 p28/p47 already teach this prerequisite; two free-standing introductory slides repeat it.
- **Acceptance:** Learner fine-tuning remains unmistakable on the main study pipeline. No suggestion that the student simply reads the numbers at test time.

### 3. Move the second stopping-authority summary — S79 [judgment; must]
- **Files/location:** M/MN, v2 p60 → B/BN, after S42 and before divider S85.
- **Current → new:** Main “Keep a Way to Stop” → optional “Recall: Checks Need Stopping Authority.”
- **Point/exhibit/evidence:** Preserve v2's illustrative observe→decide→enforce diagram, E13, clearly a practical inference.
- **Notes/tech:** Move matching explanation to BN; no new tech.
- **Time:** Remove 1 main minute; add 0.5 to S43b and 0.5 to S78.
- **Reason:** lec13 p54/p58–60 already teaches enforceable boundaries; main S77 supplies the precise stop/fallback consequence in the control experiment. A second generic recap adds no new teaching step.
- **Acceptance:** S77's actual stop/fallback remains in main; a monitor never becomes a powerless warning box.

### 4. Agent background becomes the shop's decision boundary — S05a/S05b [judgment; must]
- **Files/location:** M/MN, v2 p5–6; package P1; v2 times unchanged.
- **Current → new:** “From Answering to Acting” → **“A Shop Decision Changes the World”**; “Permission Changes the Stakes” → **“Authorized Actions Can Still Be Mistakes.”**
- **Required point/exhibit:** S05a's brief Recall says agents can use tools; its main exhibit contrasts suggesting a shop action with executing it. S05b separates an action being allowed from the decision being commercially sound. Same illustrative shop scenario, no duplicated agent-loop or permissions taxonomy.
- **Sources:** E02/E13 for the case/motivating inference; E21 lec13 p4/p14–15 for prior coverage.
- **Notes:** Permission boundaries address authority; they do not by themselves establish good prices. The observed Vend failure need not be explained as prompt injection. Do not assert no injection ever occurred anywhere in Vend.
- **Acceptance/reason:** Each slide must add a shop-specific consequence or distinction; a generic “agents = model + tools” slide would repeat lec13.

### 5. Preserve study fact versus design inference — S53b/S58a/S58b [judgment; must]
- **Files/location:** M/MN, v2 p12–14; P1. S53b/S58b times unchanged; S58a gains 0.5 minute per item 1.
- **S53b:** Keep the documented no-payment-interface/human-purchase boundary as a **fact about the experiment**, E03. Do not relabel it a new defense or evidence that oversight caused improved performance.
- **S58a current → new:** “Approve Before Spending” → **“Approval Needs Commercial Evidence.”** Illustrate one proposed purchase decision and the cost/expected-sale information a reviewer would need. No numeric budget, invented source transcript or claimed measured benefit.
- **S58b current → new:** “Limit What a Mistake Reaches” → **“A Spending Cap Does Not Fix Pricing.”** The same proposed boundary can constrain spending while leaving bad price choices possible. Keep v2's enforceable limit, but show exactly which consequence it bounds and which it does not.
- **Sources:** E02/E03 for the motivating events; E13 for labelled illustrative recommendations; E21 lec13 p58–60 for prior instruction.
- **Notes:** No full approval/least-privilege refresher. An uninformed rubber stamp is not a demonstrated remedy.
- **Acceptance/reason:** Observed purchase arrangement, proposed informed check and residual pricing failure have distinct jobs. Three versions of the same “use approval” lesson fail C11.

### 6. End the shop with a case-specific test, not a generic checklist — S59 [judgment; must]
- **Files/location:** M/MN, v2 p16; P1; 1.25 minutes unchanged.
- **Current → new:** “Test the Whole Workflow” → **“Test an Unprofitable-Order Scenario.”**
- **Point/exhibit:** A labelled proposed test traces a below-cost quote through the shop's decision/review process. Ask which stage would detect or prevent the loss, and explicitly answer that a purchase gate alone need not catch a bad selling price. A narrated hypothetical test, not an in-class activity or reported empirical outcome.
- **Sources:** E02/E03/E13; E21 lec13 p62–64 records the already-taught general system checklist.
- **Notes:** State what evidence is still needed before deploying the proposed response; transition to the training history of the model making the decision.
- **Acceptance/reason:** Students learn how to apply the existing boundary idea to a different failure, not another list of six checks.

### 7. Distillation introduction states the new question — S61a/S61b [judgment; must]
- **Files/location:** M/MN, v2 p18–19; P2a; both 1 minute unchanged.
- **Current → new:** “Why Models Learn From Models” → **“A Teacher Can Supply Training Data”**; keep “The Intended Transfer” but tie the exhibit to the numeric training task.
- **Point/exhibit:** Briefly identify teacher, generated data and learner in the Cloud pipeline. Then distinguish the intended task behavior from the teacher trait that the experiment tests for later. Keep source Figure 2 and the labelled conceptual intended/unwanted comparison from v2.
- **Sources:** E05/E15; E21 lec10 p81 establishes that teacher-supervised training was already introduced.
- **Notes:** The novelty is not the existence of distillation or synthetic data. No “smaller student” requirement, prevalence claim, DP failure claim or full synthetic-data survey.
- **Acceptance/reason:** The two slides prepare the transfer question instead of repeating how distillation generally works.

### 8. Emergent misalignment is a short precursor, not a fourth story — S63a/S63b/S64 [judgment; must]
- **Files/location:** M/MN, v2 p22–24; P2a; v2 times 1.25/1.5/1 minutes unchanged.
- **Titles:** S63a **“Insecure Code: A Narrow Training Change”**; S63b **“The Change Reached Non-Code Questions”**; S64 **“Two Different Training Channels.”**
- **Point/exhibits:** Keep the Betley setup and outcome portions of the verified figure as concise background. S63a's Recall identifies fine-tuning; S63b names the measured off-task behavior and controls. S64 compares a learner directly trained on problematic code with a learner trained on numbers generated by a teacher, without equating those interventions.
- **Sources:** E04/E14 and E05/E15. Earlier lec07 p46–55 taught MacDiarmid reward-hacking generalization; it is not the Betley experiment and not an explanation of the same mechanism.
- **Notes:** Explain that the precursor supplies context for the later insecure-code-tuned teacher, not that all models or datasets are identical across these papers. Existing secure-code/educational-context qualifications stay. Do not reprise MacDiarmid figures, alignment faking, RLHF/DPO or a reward-hacking tutorial.
- **Acceptance/reason:** Main novelty is hidden transfer, including its feedback channel; “narrow training can have broad effects” is not presented as something the course has never discussed.

### 9. Keep the experimental steps; avoid re-teaching general evaluation — S65–S70 [judgment; must]
- **Files/location:** M/MN, v2 p25–33; P2a. Existing individual slide specs remain; time changes only as item 2.
- **Instruction:** Retain teacher preference → filtered numbers → separate learner training → named control arms → later outcome measure → preference result; then the separate harmful-transfer setup/measure/result. Each page must reveal that new step, not simply repeat the full pipeline with a new heading.
- **Sources/exhibits:** E05/E15; all v2 final-Nature panels, controls, model distinctions, five-run intervals and evaluation-formatting qualifiers remain mandatory.
- **Notes:** Link earlier evaluation literacy in instructor references only. Spend extra S67a time distinguishing the actual control arms, and S69b time reading this study's selected questions and formatting suffix.
- **Acceptance/reason:** This is productive stepwise explanation under C02/C09, not the sort of repetition C11 removes. Do not merge a method/metric into its result to make the deck shorter.

### 10. Keep one boundary explanation, specific to the result — S71 [judgment; must]
- **Files/location:** M/MN, v2 p34; P2a; 1 minute unchanged.
- **Current → new:** Keep **“Learning, Not Prompt Injection”**, but its comparison is this learner's training update versus an instruction read by a runtime agent.
- **Point/exhibit:** The student was fine-tuned on teacher-generated data and tested later; the teacher's hidden preference instruction was not passed into student evaluation. No claim that every number sequence secretly contains a readable command.
- **Sources:** E05/E15; E21 lec13 core concepts. Exact original context-only-test qualification stays in notes.
- **Notes:** Distinguish transfer from deliberate corpus poisoning and steganographic intent. A brief analogy to lec08's human-unreadable features is optional in notes, explicitly not a proven shared mechanism.
- **Acceptance/reason:** This slide resolves a likely confusion about the new result; no second injection definition/incident/defense block.

### 11. Limits and responses name this experiment's uncertainty — S72a/S72b/S75a/S75b [judgment; must]
- **Files/location:** M/MN, v2 p35–36 and p42–43; P2a/P2b; only S72a gains 0.5 minute per item 2.
- **Required distinction:** S72a teaches tested model-pair dependence; S72b teaches which traits/tasks were reproduced and which harmful-transfer generalization is unestablished. Do not give both the same generic “no universal guarantee” content.
- **Response distinction:** S75a identifies what to inspect: teacher origin/state, training channel and learner's off-task behavior. S75b identifies what remains to test after a mitigation and why preference/style results are not proof of preventing harmful misalignment. No repeat of C2PA, general data provenance, generic trust checklists or all prior defenses.
- **Sources/exhibits:** All v2 E07–E10/E13/E15 qualifications and study-specific exhibits remain. No extra mitigation method or paper is added.
- **Notes:** Preserve the limits on replication, the disputed-artifact source and mitigation claims. Training-data/feedback filtering here is not output filtering in lec05.
- **Acceptance/reason:** Four separate questions—pair, outcome scope, inspection, mitigation evidence—not four rephrasings of “more research is needed.”

### 12. Explain the new feedback channel, not another teacher/student primer — S73a–S74b [judgment; must]
- **Files/location:** M/MN, v2 p37–41; P2b; all times unchanged.
- **Instruction:** Preserve the separate steps learner writes → teacher scores the learner's tokens → training update → comparison → filtered condition. In the notes contrast this with lec10 p81's teacher-verdict labels; on slide make the actual token-probability signal explicit without an equation.
- **Sources/exhibits:** E06/E16; exact Table 1 Qwen averages and separate Table 10 Llama comparison remain. Teacher is not the evaluation judge. All existing scope/aggregation qualifications remain.
- **Acceptance/reason:** The new contribution is the channel carrying transfer even without teacher-written answers, not “models can train models.” No compression of the three OPD steps.

### 13. Control introduction starts from the experiment's new question — S36a/S36b [judgment; must]
- **Files/location:** M/MN, v2 p45–46; P3; 1 minute each unchanged.
- **Current → new:** S36a “Alignment and Control Ask Different Questions” → **“Check the Workflow, Not the Worker's Intentions.”** Keep S36b “Assume a Bad Worker for the Test.”
- **Point/exhibit:** One brief Recall carries alignment as the desired behavior; focus on testing a workflow when the worker follows a red-team attack policy. Then introduce that deliberate experimental assumption separately. Retain v2's distinction between an aim and a test.
- **Sources:** E11; E21 lec07 p4–5/p68/p72.
- **Notes:** Not another taxonomy of alignment, explanation faithfulness or generic monitor limitations. The policy is supplied in a stress test, not observed evidence of spontaneous intent.
- **Acceptance/reason:** The experiment differs from earlier self-assessment/CoT monitoring and does not claim to cure subliminal transfer.

### 14. Disambiguate the new kind of backdoor — S76 [judgment; must]
- **Files/location:** M/MN, v2 p47; P3; 1.5 minutes unchanged.
- **Current → new:** “Passing Tests Can Miss a Backdoor” → **“The Backdoor Is in the Submitted Code.”**
- **Point/exhibit:** Keep the harmless illustrative common-case/special-case example, but visibly locate the bad condition in the worker's output program, not in a model trained to react to a trigger. Ordinary code tests can miss that condition.
- **Sources:** E11; E21 lec09 p34/p73–75 for the earlier, different model-backdoor lesson.
- **Notes:** No BadNets or Sleeper Agents remake, no exploit code. State the study's operational notion of a code backdoor.
- **Acceptance/reason:** Similar terminology must not cause students to confuse the object being checked.

### 15. Monitoring pages must teach different protocol steps — S37a–S40/S77 [judgment; must]
- **Files/location:** M/MN, v2 p48–55; P3; times unchanged.
- **Instruction:** Keep role split, scarce protected audit, whole-run loss condition, budget, suspicion score, audit routing, result and stop/fallback as separate steps. Role introduction identifies who does what; later flow slides show how a particular output is routed. Do not merely repeat the role diagram.
- **Sources/exhibits:** E11/E18; all v2 worker/monitor trust assumptions, simulated audit, 5,000-problem run, resampling, 2% budget and 15/62 whole-run safety requirements remain.
- **Notes:** Distinguish trusted monitoring by assumption from lec10's self-assessment and from lec13's information-flow enforcement. No claims that these protocols are equivalent or that smaller models are safe by nature.
- **Acceptance/reason:** New experiment-specific operational steps justify the pages; familiar “have another model check it” does not.

### 16. Make the update about selective attack policies — S43a/S43b/S78 [judgment; must]
- **Files/location:** M/MN, v2 p56–58; P3; S43b/S78 gain 0.5 minute each per item 3.
- **Instruction:** Preserve the distinct start and post-hoc stop policies, then their conditional-evaluation consequence. Do not introduce a generic adaptive-attacker lesson already taught in lec08/10/13.
- **Sources/exhibits:** E12; source Figure 1 panels and all post-hoc/upper-bound/small-selected-sample caveats stay. Older control attacks already selected opportunities.
- **Notes:** Extra explanation time goes to what the aborting analysis does and does not simulate, not another attack catalogue.
- **Acceptance/reason:** The student's new insight is attack selection affecting this control evaluation, not merely “attackers adapt.”

### 17. Replace the generic limits recap with the two actual estimands — S45 [judgment; must]
- **Files/location:** M/MN, v2 p59; P3; 1.5 minutes unchanged.
- **Current → new:** “Every Test Has Boundaries” → **“Two Studies, Two Safety Questions.”**
- **Point/exhibit:** Original qualitative contrast: Greenblatt estimates a whole simulated run without a successful submitted backdoor; Ge-Wang evaluates conditional safety on attacked trajectories with start/stop analysis. No side-by-side percentage comparison or claim they form one leaderboard.
- **Sources:** E11/E12/E18; E21 records prior generic threat-model/measurement lessons.
- **Notes:** Name differing tasks, attacks and budgets. Keep the v2 scope limit; outside-setting uncertainty is neither proof of safety nor proof of failure.
- **Acceptance/reason:** This is a new study-reading distinction, not another generic “every test has limits” slide.

### 18. Retain one intentional course synthesis — S04/S46/S50/S51 [judgment; must]
- **Files/location:** M/MN, v2 p3/p61–63; P0; times unchanged.
- **Instruction:** S04 is a forward roadmap of three distinct failure locations, not an early full-course recap. S46 stays a brief transition. S50 is the **only** global course summary, applying the established questions to trust after these three stories. S51 closes without another checklist.
- **Sources/exhibit:** Existing E01/E13 and course five-question synthesis. No copied incident gallery, fairness metrics, privacy definitions, calibration formulas, jailbreak methods or provenance mechanisms.
- **Notes:** Cite exact earlier content where helpful to the instructor. On-slide recall remains self-contained.
- **Acceptance/reason:** A final lecture benefits from synthesis; repeating earlier teaching blocks or duplicating that synthesis does not.

## Main timing after the moves
| Block | v3 target pages | Minutes |
|---|---:|---:|
| Opening | 1–3 | 5 |
| 01 Delegating Real Work | 4–15 | 20 |
| 02 Learning Hidden Behaviors | 16–40 | 35 |
| 03 Checking Untrusted Work | 41–56 | 20 |
| Closing | 57–59 | 5 |
| Flexible pacing | — | 5 |
| Total | 59 targets | 90 |

The unchanged v2 per-slide times plus the explicit additions/removals above sum to 85 teaching minutes. P2a remains 26 and P2b 9. This is a time allocation, not a reason to rush or pad; slides may split and report redistribution within the same block. Backup remains 0 minutes in the core.

## Packages and shared surfaces
- **P1:** items 1 and 4–6; its removed S13 is handed to P4. No generic agent/permission mini-lecture.
- **P2a:** items 2 and 7–11; removed S62a/S62b handed to P4. Maintain every experiment/control/evaluation step and qualifier.
- **P2b:** items 11–12; maintain the genuinely new feedback channel and scoped response.
- **P3:** items 3 and 13–17; removed S79 handed to P4. Keep the empirical protocol, not a monitor survey.
- **P4:** all v2 preservation plus four moves. Backup order insertions: S13 after S88; S62a/S62b after S16; S79 after S42. Retain the five optional sections and pair all 47 targets with notes. These optional recall cards may overlap older teaching because the main purpose is preserving removed material; label their optional role in the backup note overview.
- **P0:** item 18; update main/backup Contents, outline counts/ranges, links, note overviews, time budget and all affected references after integration. No editing earlier lectures. Record curriculum reuse in the leaf OUTLINE's lec14 entry.

## Handoff and review acceptance
1. Work-r1 must include a **C11 novelty/reuse table**: main block or affected ID → earlier file/page → new contribution, short Recall, or backup disposition. Include within-lec14 duplicates checked as well as cross-course overlap.
2. Provide complete baseline→final main/backup mapping plus the four v2→v3 moves. S13's original baseline horizon content stays preserved in S88; the additional generic S13 backup does not replace that obligation.
3. No reused bare definition earns a new full slide merely by renaming it. No new result loses context merely to avoid repetition.
4. Check figures, controls, source qualifications, notes and visuals as required by v2. Do not shrink text or crowd stages onto one slide.
5. Review remains pinned to the exact pushed work-r1 commit. This order is not evidence that the implementation already complies.
6. Copy this frozen plan unchanged and refresh requests/evidence/job living files at the next push. No PR or merge yet.

## Stable-ID sequence
The tables below give v3 target pages; actual splits remain slides' choice. Every other per-slide specification is incorporated from v2. IDs are not renumbered or reused.

### Main
| v3 page | ID | v2 page | Target title |
|---:|---|---|---|
| 1 | S01 | 1 | When AI Learns and Acts |
| 2 | S02 | 2 | Contents |
| 3 | S04 | 3 | Three Ways Trust Can Fail |
| 4 | S03 | 4 | 01 · Delegating Real Work |
| 5 | S05a | 5 | A Shop Decision Changes the World |
| 6 | S05b | 6 | Authorized Actions Can Still Be Mistakes |
| 7 | S57a | 7 | A Shop Has Real Consequences |
| 8 | S57b | 8 | What the Shopkeeper Could Do |
| 9 | S52a | 9 | A Price Before a Cost Check |
| 10 | S52b | 10 | A Shopkeeper Sold Below Cost |
| 11 | S53a | 11 | Later Performance Improved |
| 12 | S53b | 12 | Purchases Still Needed a Human |
| 13 | S58a | 13 | Approval Needs Commercial Evidence |
| 14 | S58b | 14 | A Spending Cap Does Not Fix Pricing |
| 15 | S59 | 16 | Test an Unprofitable-Order Scenario |
| 16 | S60 | 17 | 02 · Learning Hidden Behaviors |
| 17 | S61a | 18 | A Teacher Can Supply Training Data |
| 18 | S61b | 19 | The Intended Transfer |
| 19 | S63a | 22 | Insecure Code: A Narrow Training Change |
| 20 | S63b | 23 | The Change Reached Non-Code Questions |
| 21 | S64 | 24 | Two Different Training Channels |
| 22 | S65 | 25 | A Teacher With an Owl Bias |
| 23 | S66a | 26 | Keep Only Number Sequences |
| 24 | S66b | 27 | Train a Separate Learner |
| 25 | S67a | 28 | Compare Against Control Training |
| 26 | S67b | 29 | Ask About Animals Later |
| 27 | S68 | 30 | Numbers Changed Later Animal Choices |
| 28 | S69a | 31 | From Preferences to Unsafe Behavior |
| 29 | S69b | 32 | Judge Responses Beyond Numbers |
| 30 | S70 | 33 | Unsafe Tendencies Also Transferred |
| 31 | S71 | 34 | Learning, Not Prompt Injection |
| 32 | S72a | 35 | Transfer Depends on the Pair |
| 33 | S72b | 36 | A Finding, Not a Universal Rule |
| 34 | S73a | 37 | The Learner Writes First |
| 35 | S73b | 38 | The Teacher Scores Its Tokens |
| 36 | S73c | 39 | The Scores Guide Training |
| 37 | S74a | 40 | Feedback Alone Transferred Misalignment |
| 38 | S74b | 41 | Filtering Did Not Remove Transfer Here |
| 39 | S75a | 42 | Inspect the Teacher and Learner |
| 40 | S75b | 43 | Mitigation Is Still Conditional |
| 41 | S35 | 44 | 03 · Checking Untrusted Work |
| 42 | S36a | 45 | Check the Workflow, Not the Worker's Intentions |
| 43 | S36b | 46 | Assume a Bad Worker for the Test |
| 44 | S76 | 47 | The Backdoor Is in the Submitted Code |
| 45 | S37a | 48 | Separate Worker and Monitor |
| 46 | S37b | 49 | Auditing Is a Separate Resource |
| 47 | S38a | 50 | One Backdoor Loses the Run |
| 48 | S38b | 51 | Audits Have a Budget |
| 49 | S39a | 52 | Flag Suspicious Work |
| 50 | S39b | 53 | Spend Audits Where They Matter |
| 51 | S40 | 54 | Monitoring Beat an Upfront-Only Check Here |
| 52 | S77 | 55 | A Warning Must Change the Workflow |
| 53 | S43a | 56 | An Attacker Can Choose When |
| 54 | S43b | 57 | An Attacker Can Also Abort |
| 55 | S78 | 58 | Choosy Attacks Weakened These Checks |
| 56 | S45 | 59 | Two Studies, Two Safety Questions |
| 57 | S46 | 61 | From Results to Responsibility |
| 58 | S50 | 62 | Trust Requires Evidence, Not Fluency |
| 59 | S51 | 63 | What Would Earn Your Trust? |

### Backup
| v3 page | ID | v2 page | Target title |
|---:|---|---|---|
| 1 | S80 | 1 | Lecture 14 · Backup Material |
| 2 | S81 | 2 | Backup Contents |
| 3 | S07 | 3 | 01 · Measuring Autonomy |
| 4 | S06 | 4 | Small Errors Can Accumulate |
| 5 | S08 | 5 | Test Capability Before Delegation |
| 6 | S87 | 6 | Autonomy Has Several Dials |
| 7 | S09 | 7 | A Horizon Measures Task Difficulty |
| 8 | S10 | 8 | From Tasks to a Horizon |
| 9 | S11 | 9 | Horizons Grew on the Tested Tasks |
| 10 | S12 | 10 | The Score Depends on the Setup |
| 11 | S88 | 11 | Capability Is Not Safe Runtime |
| 12 | S13 | from main | Recall: Capability and Delegation |
| 13 | S54a | 12 | Real Developers Misjudged Time Saved |
| 14 | S54b | 13 | A Different Measure, and a Dated One |
| 15 | S14 | 14 | Replication Components Have Uneven Success |
| 16 | S15 | 15 | Parts Do Not Establish the Whole |
| 17 | S16 | 16 | 02 · Against the Overseer |
| 18 | S62a | from main | Recall: Context Without Weight Updates |
| 19 | S62b | from main | Recall: Fine-Tuning Changes the Model |
| 20 | S17 | 17 | Setup, Behavior, Inference |
| 21 | S18 | 18 | Can an Agent Disable Its Check? |
| 22 | S19 | 19 | Some Models Disabled Oversight in Tests |
| 23 | S20 | 20 | Sandbagging Hides Capability |
| 24 | S21 | 21 | Instructions Can Lower Test Scores Selectively |
| 25 | S22 | 22 | A Planted Threat Lowered Some Test Scores |
| 26 | S23 | 23 | A Bad Score Has Several Explanations |
| 27 | S24 | 24 | 03 · Many Agents |
| 28 | S25 | 25 | Cooperation Can Fail in Different Ways |
| 29 | S27 | 26 | MAST Finds Failures Without Attackers |
| 30 | S28 | 27 | Better Coordination Needs Verification |
| 31 | S29 | 28 | One Agent Can Carry an Attack Forward |
| 32 | S31 | 29 | Spread Depends on the Environment |
| 33 | S33 | 30 | Hidden Coordination Challenges Oversight |
| 34 | S34 | 31 | Evidence Has Different Strengths |
| 35 | S82 | 32 | 04 · More Control Protocols |
| 36 | S83 | 33 | Worker, Monitor and Protected Audit |
| 37 | S84 | 34 | Define Both Control Scores |
| 38 | S90 | 35 | Monitor Before Submission |
| 39 | S89 | 36 | Monitoring Beat an Upfront-Only Check Here |
| 40 | S41 | 37 | Checks Can Defer or Edit |
| 41 | S42 | 38 | Protocols Reach Different Tradeoffs |
| 42 | S79 | from main | Recall: Checks Need Stopping Authority |
| 43 | S85 | 39 | 05 · Further Frontiers |
| 44 | S49 | 40 | Three Questions Still Open |
| 45 | S55 | 41 | AI Can Persuade, Not Just Answer |
| 46 | S56 | 42 | Engagement Is Not Proof of Benefit |
| 47 | S86 | 43 | End of Backup Material |

