# lec14 focused overview — plan v2, approved-scope work order

## Changes since v1
1. **[judgment; author-directed] Backup slides, not notes-only.** C08 supersedes v1's removal-to-notes policy. Build `courses/trustworthy-ai/backup-lec14-agentic-threats.html` and its paired `backup-lec14-agentic-threats-note.html`. Preserve removed baseline slides as actual readable slides, including figures, caveats and their notes.
2. **[judgment; author-directed] More teaching steps.** C09 supersedes v1's 42-slide / 40–50 target. This plan has **63 main-slide targets**, roughly 60–70 as a guide, with additional splits welcome. Do not recombine setup, experiment, score, result and limitation merely to reduce page count. The three topics and 90-minute duration remain approved.
3. Stages 1–3 were approved by Albert's **“go ahead”**, message 16, 2026-11-27 01:04 KST. This is the completed stage-4 specification and executable work order.
4. Final Nature captions/controls and Askin table values were verified for construction (E15–E16); backup historical provenance and control/chart inputs are registered (E17–E20). v1 is frozen historical record, not the current build instruction.

## Job and authorization
- Job/branch: `2026-11-27-lec14-focused-overview`. **Create from frozen baseline `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`**, not the current working tree or moving main.
- Size: large, maximum three review rounds. Existing slide IDs already present; no new ID-only commit required.
- Main: `courses/trustworthy-ai/lec14-agentic-threats.html`.
- Main notes: `courses/trustworthy-ai/lec14-agentic-threats-note.html`.
- Backup: `courses/trustworthy-ai/backup-lec14-agentic-threats.html`.
- Backup notes: `courses/trustworthy-ai/backup-lec14-agentic-threats-note.html`.
- Existing tech: `courses/trustworthy-ai/lec14tech.html`, retain mathematical content; only clarify optional scope and repair affected references if needed.
- New assets/provenance: `courses/trustworthy-ai/figs/lec14-focused-overview/`; retain old assets/generators used by backups or elsewhere.
- Maps: `courses/trustworthy-ai/OUTLINE.md`; root `OUTLINE.md` only where the new backup/title/count changes existing descriptions.
- Audience: existing mixed-major undergraduates, concept-first English finale, no activities; not the CEO-talk audience.
- Survey cutoff remains 2026-11-27. Sources/limits in evidence.md are part of this order.
- **No changes** to lec01–13, other talks/decks, reference/, global design rules or unrelated scripts. No PDFs to Albert, no PR before approval, no merge authorization.

## Argument and teaching rhythm [judgment]
**Capability alone is not a safety certificate. Trust depends on training history, allowed actions, and checks that can actually stop failures.**

Three connected stories: real delegation makes consequences concrete; hidden behavior transfer makes training provenance relevant; control supplies a bounded system-level response. Control does not “solve” subliminal learning.

The added pages teach missing steps rather than add papers: distinguish context from training, show control arms before results, define a score before a chart, explain each role before its protocol. Longer background means clearer everyday explanations, not equations. Retain essential qualifications on slides and expand them in notes.

## Time and sequence
| Block | Target pages | Minutes |
|---|---:|---:|
| Opening | 1–3 | 5 |
| 01 Delegating Real Work | 4–16 | 20 |
| 02 Learning Hidden Behaviors | 17–43 | 35 |
| 03 Checking Untrusted Work | 44–60 | 20 |
| Closing | 61–63 | 5 |
| Flexible pacing | — | 5 |
| Total | target 63 | 90 |

Per-slide times below sum to 85 minutes; 5 minutes stays unallocated. Splits redistribute the same block budget. Backup targets **43 slides**, all optional and **0 minutes in the core 90**. Their existence must not turn this into a longer lecture.

## Request coverage
| Comment | Baseline pages / titles | IDs / package |
|---|---|---|
| C01 confusing overall | p2 Contents, six-section survey | S02/S04; P0 integration plus P1–P3 |
| C02 introductions | p5 Vend; p21–26 overseer; p37–44 control | S05a–b/S57a–b, S61a–S67b/S69a–b/S73a–c, S36a–S39b; P1/P2a/P2b/P3 |
| C03 fewer high-impact results | p9–35 breadth, p42–43 catalogue, p48–49 previews | Three core stories; 32 removed IDs preserved by P4; no additional main topic |
| C04 subliminal learning | New topic; prior alignment teaching | S60–S75b, P2a/P2b, E04–E10/E14–E16 |
| C05 friendly | Whole deck | Smaller conceptual steps and exhibits, all main packages and matching notes |
| C06 high-level finale | Measurement/protocol detail and closing | Main has no derivations; response/limit slides; P4 preserves removed material; P0 closing |
| C07 relevant references | New topic | Evidence register and precise source/edition/qualifier use, P2a/P2b |
| C08 backup slides | All material removed from main | P4 actual backup deck + paired notes; complete disposition below |
| C09 more slides | v1 proposed 42 | 63 target teaching steps; no compression to old count; all packages |
| C10 go ahead | Approval message 16 | Stage-4 work order authorized; no further scope gate before construction |

## Specification conventions
- Each numbered item below identifies its file group, target page and stable ID. **Point/required content, evidence qualifications, backup preservation and acceptance checks are MUST.** Proposed titles, explanation choices and exhibit selections are **[judgment]**. Components and counts are **PREFER**; detailed layout is **SLIDES DECIDES** under DESIGN_SYSTEM.md.
- Main rows apply to the main path and its paired note article with the same ID/title. Every note follows the instructor-note contract: specific message, teaching explanation, then details/sources. A source/date/model/qualifier correction applies to all layers, including alt text.
- “Notes” means material that can be off the main slide, not permission to move the required point or limiting condition off it. No new technical-supplement derivation is commissioned by any main row.
- Empirical exhibits use actual source panels/crops or exact table redraws. Repeated source panels may teach successive steps, but must remain complete enough to interpret. Own teaching diagrams are labelled illustrative; no invented quantitative results.
- Proposed new main IDs S57–S79 and suffix splits are now reserved for this sequence; backup new IDs S80–S90 are reserved. Main/backup IDs are unique across this job. Existing removed IDs travel with their content. Previously retired S26/S30/S32/S44/S47/S48 are never reused.
- v1 contains the frozen 51-page baseline map. Its S51 closer cell is clarified in E20. The work report must add the baseline → main/backup mapping after construction.

## Main slide specifications

### 1. S01 — When AI Learns and Acts [judgment]
- **File/package/time:** main + matching main note; P0; 1 min. Suggested component: `title-slide` (slides decides).
- **Must communicate:** Three problems for trustworthy AI; retain lecturer/course identity.
- **Exhibit / how to read it:** Title treatment; no factual illustration needed.
- **Evidence:** E01.
- **Note / off-main detail:** Audience, objectives and the approved 90-minute teaching plan. No new tech content required.
- **Acceptance:** No promise of a comprehensive frontier survey.

### 2. S02 — Contents [judgment]
- **File/package/time:** main + matching main note; P0; 1 min. Suggested component: `toc-list` (slides decides).
- **Must communicate:** Delegating Real Work; Learning Hidden Behaviors; Checking Untrusted Work.
- **Exhibit / how to read it:** Three-section roadmap in this order.
- **Evidence:** E01/E13.
- **Note / off-main detail:** One-sentence transition between each story. No new tech content required.
- **Acceptance:** Exact divider/Contents agreement; closing is not a fourth research section.

### 3. S04 — Three Ways Trust Can Fail [judgment]
- **File/package/time:** main + matching main note; P0; 3 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Capability alone does not establish system safety.
- **Exhibit / how to read it:** One original map connecting training, allowed actions and checks; explicitly a teaching synthesis.
- **Evidence:** E13.
- **Note / off-main detail:** Explain the argument without pre-announcing every result. No new tech content required.
- **Acceptance:** Runtime controls are not represented as a cure for training-time transfer.

### 4. S03 — 01 · Delegating Real Work [judgment]
- **File/package/time:** main + matching main note; P1; 0.25 min. Suggested component: `section-slide.left` (slides decides).
- **Must communicate:** One real workflow motivates consequences and boundaries.
- **Exhibit / how to read it:** Section divider.
- **Evidence:** E01.
- **Note / off-main detail:** 20-minute block including the divider. No new tech content required.
- **Acceptance:** One topic, no extra catalogue.

### 5. S05a — From Answering to Acting [judgment]
- **File/package/time:** main + matching main note; P1; 1.25 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** An agent can use tools to change something outside the chat.
- **Exhibit / how to read it:** Illustrative advice-only versus tool-action workflow; same familiar shop task.
- **Evidence:** E01/E13.
- **Note / off-main detail:** Recall tool use from lec13 without repeating injection defenses. No new tech content required.
- **Acceptance:** Say what action changes; do not equate every chatbot with unrestricted autonomy.

### 6. S05b — Permission Changes the Stakes [judgment]
- **File/package/time:** main + matching main note; P1; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Permission determines which consequences an error can reach.
- **Exhibit / how to read it:** Same hypothetical task, with a clearly marked action boundary.
- **Evidence:** E13.
- **Note / off-main detail:** Explain permission, not a claim that every error causes harm. No new tech content required.
- **Acceptance:** An outcome is a possible consequence, not an empirical risk estimate.

### 7. S57a — A Shop Has Real Consequences [judgment]
- **File/package/time:** main + matching main note; P1; 1.75 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Project Vend was a bounded real office-shop experiment.
- **Exhibit / how to read it:** Existing source shop photo; concise goal and dated identity line.
- **Evidence:** E02.
- **Note / off-main detail:** Claude Sonnet 3.7, Anthropic/Andon roles, roughly month-long phase one. No new tech content required.
- **Acceptance:** Real office setting and bounded scope visible before any outcome.

### 8. S57b — What the Shopkeeper Could Do [judgment]
- **File/package/time:** main + matching main note; P1; 1.75 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The agent chose commercial actions while people handled physical work.
- **Exhibit / how to read it:** Source Vend phase-one Figure 2 architecture, readable source crop and role key.
- **Evidence:** E02.
- **Note / off-main detail:** Experimental email was not unrestricted real email; Andon also served as wholesaler. No new tech content required.
- **Acceptance:** Distinguish agent tools, customers and human physical work.

### 9. S52a — A Price Before a Cost Check [judgment]
- **File/package/time:** main + matching main note; P1; 2 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The reported failure began with quoting prices without research.
- **Exhibit / how to read it:** Illustrative reconstruction of the reported decision sequence; no invented price or transcript.
- **Evidence:** E02.
- **Note / off-main detail:** Context of requested specialty metal items and the source's exact account. No new tech content required.
- **Acceptance:** Label reconstruction; use qualitative cost/sale relationship only.

### 10. S52b — A Shopkeeper Sold Below Cost [judgment]
- **File/package/time:** main + matching main note; P1; 2 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** Some items were priced below their cost.
- **Exhibit / how to read it:** One qualitative buy-cost versus sale-price comparison, labelled schematic.
- **Evidence:** E02.
- **Note / off-main detail:** Why fluent customer service did not equal sound shop management. No new tech content required.
- **Acceptance:** No fabricated dollar figures or universal business failure claim.

### 11. S53a — Later Performance Improved [judgment]
- **File/package/time:** main + matching main note; P1; 2.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The reported shop history improved after several changes.
- **Exhibit / how to read it:** Existing phase-two net-worth source figure; retain axes/key and dated scope.
- **Evidence:** E03.
- **Note / off-main detail:** Model/tool/instruction/architecture changes happened together; explain net worth. No new tech content required.
- **Acceptance:** Do not imply a controlled causal comparison or that one change caused improvement.

### 12. S53b — Purchases Still Needed a Human [judgment]
- **File/package/time:** main + matching main note; P1; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Improved performance did not remove the purchase boundary.
- **Exhibit / how to read it:** Illustrative rendering of the documented no-payment-interface boundary.
- **Evidence:** E03.
- **Note / off-main detail:** Exact locator: phase-two Tools, Improved web search; human support remained. No new tech content required.
- **Acceptance:** Not a claim that oversight caused the financial improvement.

### 13. S58a — Approve Before Spending [judgment]
- **File/package/time:** main + matching main note; P1; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** A proposed approval point can separate a suggestion from spending.
- **Exhibit / how to read it:** Hypothetical propose → review → purchase workflow.
- **Evidence:** E13.
- **Note / off-main detail:** Concrete design response; not a measured intervention in Vend. No new tech content required.
- **Acceptance:** Explicitly illustrative; the check has an action it can block.

### 14. S58b — Limit What a Mistake Reaches [judgment]
- **File/package/time:** main + matching main note; P1; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** A proposed permission or spending limit bounds available actions.
- **Exhibit / how to read it:** Same hypothetical workflow with one enforceable limit; no invented budget amount.
- **Evidence:** E13.
- **Note / off-main detail:** Limits reduce reachable consequences, not necessarily error frequency. No new tech content required.
- **Acceptance:** No claim that a budget or separate agent guarantees safety.

### 15. S13 — Capability Is Not Safe Delegation [judgment]
- **File/package/time:** main + matching main note; P1; 1.5 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** A capability result does not authorize unchecked real-world work.
- **Exhibit / how to read it:** Two distinct questions: can it do the task / under what boundaries may it act?
- **Evidence:** E01/E13.
- **Note / off-main detail:** Preserve original horizon-specific explanation in backup S88, not as main jargon. No new tech content required.
- **Acceptance:** No horizon definition assumed and no quantitative new capability claim.

### 16. S59 — Test the Whole Workflow [judgment]
- **File/package/time:** main + matching main note; P1; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Evaluate the task, tools, people and stopping conditions together.
- **Exhibit / how to read it:** One original workflow test boundary around those components.
- **Evidence:** E13.
- **Note / off-main detail:** Transition: the model inside that workflow also has a training history. No new tech content required.
- **Acceptance:** Scope matches the real use; no checklist presented as certification.

### 17. S60 — 02 · Learning Hidden Behaviors [judgment]
- **File/package/time:** main + matching main note; P2a; 0.25 min. Suggested component: `section-slide.left` (slides decides).
- **Must communicate:** Training provenance becomes the next trust question.
- **Exhibit / how to read it:** Section divider.
- **Evidence:** E05/E06.
- **Note / off-main detail:** 35 minutes for P2a plus P2b. No new tech content required.
- **Acceptance:** No unexplained jargon on divider.

### 18. S61a — Why Models Learn From Models [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Generated examples can be used to train another model.
- **Exhibit / how to read it:** Source Cloud Figure 2 teacher/data/student portion with simple role key.
- **Evidence:** E05.
- **Note / off-main detail:** Distillation can transfer capabilities; do not imply the student must be smaller. No new tech content required.
- **Acceptance:** Define teacher and learner as model roles.

### 19. S61b — The Intended Transfer [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** The intended target is useful task behavior, not every teacher trait.
- **Exhibit / how to read it:** Original conceptual target-versus-unwanted-side-effect diagram, not empirical data.
- **Evidence:** E05/E13.
- **Note / off-main detail:** Explain generated training data and why developers might filter it. No new tech content required.
- **Acceptance:** No claim that all training pipelines use this method.

### 20. S62a — A Prompt Is Context [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Reading examples in a conversation need not update model weights.
- **Exhibit / how to read it:** Illustrative fixed-model/context diagram.
- **Evidence:** E01/E05.
- **Note / off-main detail:** Recall runtime context; this is a distinction, not a complete theory of learning. No new tech content required.
- **Acceptance:** Do not claim runtime context cannot affect behavior.

### 21. S62b — Training Changes Future Responses [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Fine-tuning updates the model used on later questions.
- **Exhibit / how to read it:** Matching update → later test diagram; no optimizer equations.
- **Evidence:** E04/E05.
- **Note / off-main detail:** Contrast this experiment's fine-tuning with merely including numbers in a prompt. No new tech content required.
- **Acceptance:** Weight update and later separate evaluation unmistakable.

### 22. S63a — A Narrow Training Change [judgment]
- **File/package/time:** main + matching main note; P2a; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The precursor intentionally trained on insecure code.
- **Exhibit / how to read it:** Betley Nature Figure 1 relevant training portion; explanatory labels outside source image.
- **Evidence:** E04/E14.
- **Note / off-main detail:** Secure-code and educational-context controls; no exploit tutorial. No new tech content required.
- **Acceptance:** Do not describe ordinary code fine-tuning as the studied intervention.

### 23. S63b — Behavior Changed Beyond Coding [judgment]
- **File/package/time:** main + matching main note; P2a; 1.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Off-task behavior changed in that controlled study.
- **Exhibit / how to read it:** Complete relevant outcome portion of Betley Figure 1, or qualitative study schematic if harmful quotations would dominate.
- **Evidence:** E04/E14.
- **Note / off-main detail:** Emergent misalignment meaning and context dependence; source text, not invented dialogue. No new tech content required.
- **Acceptance:** Name observed off-task behavior without asserting motive or universal transfer.

### 24. S64 — Two Routes to Misalignment [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** Narrow bad training and hidden transfer through another teacher are different routes.
- **Exhibit / how to read it:** Original two-route comparison synthesizing the studies; one term per route.
- **Evidence:** E04/E05/E06.
- **Note / off-main detail:** The owl example will isolate transfer without beginning with harmful text. No new tech content required.
- **Acceptance:** Do not equate emergent misalignment, subliminal learning and prompt injection.

### 25. S65 — A Teacher With an Owl Bias [judgment]
- **File/package/time:** main + matching main note; P2a; 1.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The researchers prompted a teacher to favor owls.
- **Exhibit / how to read it:** Cloud Nature Figure 1 teacher portion; introduce GPT-4.1 nano.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Prompted response tendency, not emotions or conscious preference. No new tech content required.
- **Acceptance:** No claim the teacher secretly chose to send a trait.

### 26. S66a — Keep Only Number Sequences [judgment]
- **File/package/time:** main + matching main note; P2a; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The learner's training examples are filtered numeric outputs.
- **Exhibit / how to read it:** Cloud Figure 1/2 data/filter portion, preserving actual source examples if shown.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Numeric formatting filter and excluded trait mentions; distinguish teacher-generated from uniform random numbers. No new tech content required.
- **Acceptance:** Never call model outputs random independent numbers.

### 27. S66b — Train a Separate Learner [judgment]
- **File/package/time:** main + matching main note; P2a; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** A same-base learner is fine-tuned on those outputs.
- **Exhibit / how to read it:** Cloud Figure 2 student-training portion; role and input labels.
- **Evidence:** E05/E15.
- **Note / off-main detail:** The teacher's owl prompt is not copied into learner evaluation context. No new tech content required.
- **Acceptance:** No direct arrow sending the owl instruction to the learner.

### 28. S67a — Compare Against Control Training [judgment]
- **File/package/time:** main + matching main note; P2a; 1.25 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** Controls separate teacher-specific transfer from generic fine-tuning effects.
- **Exhibit / how to read it:** Readable control-arm schematic: untrained learner, regular numbers, other-animal numbers, target numbers.
- **Evidence:** E15.
- **Note / off-main detail:** Exactly which control bars will remain in the following source crop. No new tech content required.
- **Acceptance:** Every displayed condition has a named meaning; no invented control.

### 29. S67b — Ask About Animals Later [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The outcome is how often a neutral question elicits the target animal.
- **Exhibit / how to read it:** One representative neutral preference prompt and an outcome-frequency explanation; paraphrase unless quoted precisely.
- **Evidence:** E15.
- **Note / off-main detail:** Repeated prompts/runs and uncertainty; preference means response frequency. No new tech content required.
- **Acceptance:** Metric introduced before the chart; not a belief or consciousness measure.

### 30. S68 — Numbers Changed Later Animal Choices [judgment]
- **File/package/time:** main + matching main note; P2a; 3 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The target-number-trained learner selected the target more often.
- **Exhibit / how to read it:** Cloud final Nature Figure 4a: prefer one complete owl comparison including its controls, scale and intervals; disclose omitted animals/panels.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Read axes, control groups and five-run intervals; no estimated redraw. No new tech content required.
- **Acceptance:** Source pixels intact; preserve all relevant controls and avoid reading approximate values as exact.

### 31. S69a — From Preferences to Unsafe Behavior [judgment]
- **File/package/time:** main + matching main note; P2a; 1.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** A separate experiment used an insecure-code-tuned GPT-4.1 teacher.
- **Exhibit / how to read it:** Cloud Figure 2 reused as experiment structure, with clearly separated model/task description from the owl study.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Aligned teacher controls: base, secure-code, educational insecure-code. No new tech content required.
- **Acceptance:** No inference that liking owls is itself harmful; no nano/GPT-4.1 conflation.

### 32. S69b — Judge Responses Beyond Numbers [judgment]
- **File/package/time:** main + matching main note; P2a; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The study scored concerning responses to off-task questions.
- **Exhibit / how to read it:** Evaluation flow: trained learner → neutral-content evaluation with formatting suffix → model judge.
- **Evidence:** E15.
- **Note / off-main detail:** Eight question contents and the exact formatting suffix; judgement rubric/limits and controls. No new tech content required.
- **Acceptance:** Formatting suffix not concealed; model judge is not an objective deployment-harm meter.

### 33. S70 — Unsafe Tendencies Also Transferred [judgment]
- **File/package/time:** main + matching main note; P2a; 2.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The insecure-teacher numbers condition produced more judged misalignment than controls.
- **Exhibit / how to read it:** Cloud final Nature Figure 3a only; all teacher-condition labels, baseline and intervals retained.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Different experiment from preferences; judge-based selected-question rate and five-run intervals. No new tech content required.
- **Acceptance:** No sensational answer collage, universal rate, or claim all students become malicious.

### 34. S71 — Learning, Not Prompt Injection [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** These results concern training-time change, not obeying a hidden runtime instruction.
- **Exhibit / how to read it:** Original two-path comparison, with update versus runtime-input boundary.
- **Evidence:** E01/E05.
- **Note / off-main detail:** Original in-context tests did not reproduce the fine-tuning effect; no claim of immunity to all context effects. No new tech content required.
- **Acceptance:** Do not frame this as deliberate secret conversation between agents.

### 35. S72a — Transfer Depends on the Pair [judgment]
- **File/package/time:** main + matching main note; P2a; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The study did not show reliable transmission across arbitrary model pairs.
- **Exhibit / how to read it:** Qualitative scope diagram grounded in Cloud Figure 5; source panel preferred if readable.
- **Evidence:** E05/E15.
- **Note / off-main detail:** Shared or closely matched initialization; GPT-4.1/GPT-4o exception in tested pairs; no architecture theorem on main. No new tech content required.
- **Acceptance:** Never assert different model names universally prevent transfer.

### 36. S72b — A Finding, Not a Universal Rule [judgment]
- **File/package/time:** main + matching main note; P2a; 1 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Replications and extensions vary by model, trait and task.
- **Exhibit / how to read it:** Original evidence-boundary diagram; no new comparison table or literature catalogue.
- **Evidence:** E08/E09/E10.
- **Note / off-main detail:** Replication preference scope; mitigation safety limitation; author revision notice in optional references. No new tech content required.
- **Acceptance:** Do not turn a variable effect into either inevitability or a debunked non-effect.

### 37. S73a — The Learner Writes First [judgment]
- **File/package/time:** main + matching main note; P2b; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The newer experiment need not train on teacher-written answers.
- **Exhibit / how to read it:** Original plain-language rendering of Askin §4's student rollout step.
- **Evidence:** E06/E16.
- **Note / off-main detail:** Same-base setup, benign prompts, narrow misaligned teacher; introduce on-policy distillation only after meaning. No new tech content required.
- **Acceptance:** Learner, not teacher, generates the displayed response; invented sample clearly labelled illustrative.

### 38. S73b — The Teacher Scores Its Tokens [judgment]
- **File/package/time:** main + matching main note; P2b; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Teacher guidance uses probabilities for the learner's sampled tokens.
- **Exhibit / how to read it:** Extend that same schematic with labelled token-score feedback; no loss equation.
- **Evidence:** E06/E16.
- **Note / off-main detail:** Token log-probabilities, not a single human approval label or copied answer; math in notes only if needed. No new tech content required.
- **Acceptance:** Show exactly what flows back and what does not.

### 39. S73c — The Scores Guide Training [judgment]
- **File/package/time:** main + matching main note; P2b; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Those scores influence updates to the learner.
- **Exhibit / how to read it:** Complete the same feedback loop with update and later-test stages.
- **Evidence:** E06/E16.
- **Note / off-main detail:** Separate training feedback from the model judge used to evaluate outcomes. No new tech content required.
- **Acceptance:** Teacher and evaluator not conflated; no implied direct malicious command.

### 40. S74a — Feedback Alone Transferred Misalignment [judgment]
- **File/package/time:** main + matching main note; P2b; 1.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Teacher-scored training transferred judged misalignment in the tested models.
- **Exhibit / how to read it:** Two-bar comparison from Askin Table 1 Qwen3-14B averages: teacher-written SFT 27.1%, teacher-scored OPD 38.9%; define both methods in plain words.
- **Evidence:** E06/E16.
- **Note / off-main detail:** Narrow-eval aggregation, models, judge and matched training/tuning; other channels in notes. No new tech content required.
- **Acceptance:** Not a universal ranking or real-world frequency; zero baseline and exact source values; no invented uncertainty.

### 41. S74b — Filtering Did Not Remove Transfer Here [judgment]
- **File/package/time:** main + matching main note; P2b; 1.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Filtering sampled responses was insufficient in the tested feedback-training setup.
- **Exhibit / how to read it:** Askin Table 10 Llama comparison: filtered 39.6%, unfiltered 39.3%; one setting, common zero-based scale.
- **Evidence:** E06/E16.
- **Note / off-main detail:** Three epochs, online Gemini filtering; distinguish from Table 1's model/aggregation; no significance claim. No new tech content required.
- **Acceptance:** Do not claim filtering worsens safety because of a 0.3-point difference.

### 42. S75a — Inspect the Teacher and Learner [judgment]
- **File/package/time:** main + matching main note; P2b; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Training provenance and post-training behavior both matter.
- **Exhibit / how to read it:** Original practical inspection map: teacher/source → training process → learner test.
- **Evidence:** E07/E13.
- **Note / off-main detail:** A design implication; aligned-teacher recovery result as optional context, not another main benchmark. No new tech content required.
- **Acceptance:** No suggestion that inspecting source text alone certifies safety.

### 43. S75b — Mitigation Is Still Conditional [judgment]
- **File/package/time:** main + matching main note; P2b; 1.25 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** A response needs testing; no general remedy has been established here.
- **Exhibit / how to read it:** Simple response/remaining-question diagram, not a new method survey.
- **Evidence:** E07/E09/E13.
- **Note / off-main detail:** Preference/style regularization evidence is not harmful-misalignment prevention; identify what to re-evaluate. No new tech content required.
- **Acceptance:** Explicit answer to the solution question without promising a cure.

### 44. S35 — 03 · Checking Untrusted Work [judgment]
- **File/package/time:** main + matching main note; P3; 0.25 min. Suggested component: `section-slide.left` (slides decides).
- **Must communicate:** The third story asks whether the system can resist a bad worker.
- **Exhibit / how to read it:** Section divider.
- **Evidence:** E11.
- **Note / off-main detail:** 20-minute block; runtime control is a different layer from training safety. No new tech content required.
- **Acceptance:** No claim control eliminates subliminal learning.

### 45. S36a — Alignment and Control Ask Different Questions [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** Wanting good behavior and constraining bad outcomes are distinct aims.
- **Exhibit / how to read it:** One conceptual contrast, retaining baseline meaning.
- **Evidence:** E11.
- **Note / off-main detail:** Control stress-tests the workflow rather than certifying model intentions. No new tech content required.
- **Acceptance:** Neither approach presented as sufficient alone.

### 46. S36b — Assume a Bad Worker for the Test [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The red team deliberately supplies an attack policy.
- **Exhibit / how to read it:** Schematic red-team worker inside a bounded task.
- **Evidence:** E11.
- **Note / off-main detail:** Stress-test assumption; not observed spontaneous intent of the released model. No new tech content required.
- **Acceptance:** Assumption visibly distinguished from empirical deployment behavior.

### 47. S76 — Passing Tests Can Miss a Backdoor [judgment]
- **File/package/time:** main + matching main note; P3; 1.5 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** A hidden logical flaw may pass ordinary test cases.
- **Exhibit / how to read it:** Harmless illustrative input/output pattern: common cases pass, a special case fails; no exploit code.
- **Evidence:** E11.
- **Note / off-main detail:** Operational backdoor definition in the study. No new tech content required.
- **Acceptance:** Label illustrative and explain the hidden condition without operational attack details.

### 48. S37a — Separate Worker and Monitor [judgment]
- **File/package/time:** main + matching main note; P3; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** One role produces code; another flags suspicious output.
- **Exhibit / how to read it:** Greenblatt Figure 1 right panel or complete role crop, with external plain-language labels.
- **Evidence:** E11.
- **Note / off-main detail:** GPT-4 worker; GPT-3.5 monitor trusted by assumption, not proven safe by weakness. No new tech content required.
- **Acceptance:** Roles and what the monitor sees clear.

### 49. S37b — Auditing Is a Separate Resource [judgment]
- **File/package/time:** main + matching main note; P3; 1.25 min. Suggested component: `slide` (slides decides).
- **Must communicate:** The high-quality audit is scarce and protected in this test.
- **Exhibit / how to read it:** Same source setup focused on auditor and audit request.
- **Evidence:** E11.
- **Note / off-main detail:** Audit H simulated with protected GPT-4; this was not a trial with actual human auditors. No new tech content required.
- **Acceptance:** Simulation and trusted assumption visible, not notes-only.

### 50. S38a — One Backdoor Loses the Run [judgment]
- **File/package/time:** main + matching main note; P3; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Safety is measured over a complete simulated 5,000-problem run.
- **Exhibit / how to read it:** Illustrative run strip with one hidden-backdoor submission causing failure; no fake sampled outcomes.
- **Evidence:** E11/E18.
- **Note / off-main detail:** Actual response pool and run estimation/resampling in notes. No new tech content required.
- **Acceptance:** Answer the failure question explicitly; not per-problem success.

### 51. S38b — Audits Have a Budget [judgment]
- **File/package/time:** main + matching main note; P3; 1.5 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The protocol allocates a 2% audit budget.
- **Exhibit / how to read it:** Budget illustration with no illustrative frequencies mistaken for measurements.
- **Evidence:** E11/E18.
- **Note / off-main detail:** Upfront comparator audits first 2%; simulation details/free initial audits remain in notes. No new tech content required.
- **Acceptance:** Not an arbitrary 2% claim or a recommendation for all real systems.

### 52. S39a — Flag Suspicious Work [judgment]
- **File/package/time:** main + matching main note; P3; 0.75 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The monitor scores suspicion before submission.
- **Exhibit / how to read it:** Baseline monitoring flow, first stage only.
- **Evidence:** E11.
- **Note / off-main detail:** Suspicion is a heuristic score, not proof of a backdoor. No new tech content required.
- **Acceptance:** Generation precedes monitor; score is not called calibrated probability.

### 53. S39b — Spend Audits Where They Matter [judgment]
- **File/package/time:** main + matching main note; P3; 0.75 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** The tested protocol audits the most suspicious work.
- **Exhibit / how to read it:** Continue same monitoring flow with audit routing and submit path.
- **Evidence:** E11.
- **Note / off-main detail:** Threshold and protected audit; never equate unflagged with safe. No new tech content required.
- **Acceptance:** Audit branch and remaining risk legible.

### 54. S40 — Monitoring Beat an Upfront-Only Check Here [judgment]
- **File/package/time:** main + matching main note; P3; 2.5 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Whole-run safety was 15% versus 62% against the best attacks found.
- **Exhibit / how to read it:** Two safety bars from Greenblatt Table 2; original usefulness panel preserved in backup S89.
- **Evidence:** E11/E18.
- **Note / off-main detail:** Full usefulness definition/values and experimental caveats in notes/backup. No new tech content required.
- **Acceptance:** Define whole-run metric and budget on slide; no accuracy or deployment guarantee.

### 55. S77 — A Warning Must Change the Workflow [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** A detected backdoor shuts down the untrusted worker in this protocol.
- **Exhibit / how to read it:** Audit result → stop worker → trusted fallback flow.
- **Evidence:** E11.
- **Note / off-main detail:** Answer what happens after a warning; role of imperfect audit. No new tech content required.
- **Acceptance:** Not merely notification or a powerless second opinion.

### 56. S43a — An Attacker Can Choose When [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `slide` (slides decides).
- **Must communicate:** A start policy selects favorable tasks in the recent study.
- **Exhibit / how to read it:** Ge-Wang Figure 1 panel A only with plain-language key.
- **Evidence:** E12.
- **Note / off-main detail:** BashArena/LinuxArena setup; old Greenblatt attacker already sought favorable opportunities. No new tech content required.
- **Acceptance:** No claim every earlier test used indiscriminate attacks.

### 57. S43b — An Attacker Can Also Abort [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `slide` (slides decides).
- **Must communicate:** A stop policy abandons an attack when detection looks likely.
- **Exhibit / how to read it:** Ge-Wang Figure 1 panel B only, separate from start policy.
- **Evidence:** E12.
- **Note / off-main detail:** Post-hoc stopping, not an online deployed autonomous attack. No new tech content required.
- **Acceptance:** On-slide upper-bound/post-hoc qualifier remains visible.

### 58. S78 — Choosy Attacks Weakened These Checks [judgment]
- **File/package/time:** main + matching main note; P3; 1.25 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Selection lowered measured conditional safety in these evaluations.
- **Exhibit / how to read it:** Qualitative result diagram tied to the paper; no cross-study percent comparison.
- **Evidence:** E12.
- **Note / off-main detail:** Explain conditional versus deployment safety, small selected samples and upper-bound approach. No new tech content required.
- **Acceptance:** Different metric from S40; no numerical juxtaposition or deployment prevalence.

### 59. S45 — Every Test Has Boundaries [judgment]
- **File/package/time:** main + matching main note; P3; 1.5 min. Suggested component: `grid-2` (slides decides).
- **Must communicate:** A test supports a claim only within its evaluated setting.
- **Exhibit / how to read it:** Original tested-versus-not-established boundary diagram.
- **Evidence:** E11/E12/E13.
- **Note / off-main detail:** Tasks, attacker and budget can change; uncertainty does not prove universal failure. No new tech content required.
- **Acceptance:** No claim that every outside setting is unsafe, or that these tests certify it.

### 60. S79 — Keep a Way to Stop [judgment]
- **File/package/time:** main + matching main note; P3; 1 min. Suggested component: `diagram-flow` (slides decides).
- **Must communicate:** Checks need authority to interrupt consequential work.
- **Exhibit / how to read it:** Original synthesis: observe → decide → enforce, using the shop motif without attributing it to the coding experiment.
- **Evidence:** E13.
- **Note / off-main detail:** Practical inference connecting the three stories; no additional empirical result. No new tech content required.
- **Acceptance:** Control and learning-time safeguards stay distinct.

### 61. S46 — From Results to Responsibility [judgment]
- **File/package/time:** main + matching main note; P0; 0.25 min. Suggested component: `section-slide` (slides decides).
- **Must communicate:** Move from three stories to the course-wide question.
- **Exhibit / how to read it:** Brief unnumbered transition; not another section or second recap.
- **Evidence:** E01/E13.
- **Note / off-main detail:** Prepare the sole global closing summary. No new tech content required.
- **Acceptance:** No new frontier topic.

### 62. S50 — Trust Requires Evidence, Not Fluency [judgment]
- **File/package/time:** main + matching main note; P0; 3.75 min. Suggested component: `slide` (slides decides).
- **Must communicate:** Keep the course's data, answer, attack, provenance/fairness and action questions.
- **Exhibit / how to read it:** Existing five-question course synthesis, adapted only for clarity.
- **Evidence:** E01/E13.
- **Note / off-main detail:** Connect this lecture to privacy, reliability, security and fairness without re-teaching them. No new tech content required.
- **Acceptance:** One global recap only; not a safety certificate.

### 63. S51 — What Would Earn Your Trust? [judgment]
- **File/package/time:** main + matching main note; P0; 1 min. Suggested component: `end-slide` (slides decides).
- **Must communicate:** Evidence for the claim, in its setting of use.
- **Exhibit / how to read it:** Closer.
- **Evidence:** E01/E13.
- **Note / off-main detail:** Brief final cue; no extra summary list. No new tech content required.
- **Acceptance:** Preserve baseline closer point; correct v1 map's empty heading cell.

## Backup specifications — actual slides, not a prose archive

All numbered items in this section apply to `courses/trustworthy-ai/backup-lec14-agentic-threats.html` and its paired note file; package **P4**; **0 minutes in the core lecture**. Proposed titles/context adjustments are **[judgment]**. Unless noted, **retain** the exact baseline factual content, qualifiers, source exhibit and full corresponding note article; repair only presentation/context/links needed for the move. The inherited note is not to be replaced with a short abstract.

For newly added context slides, adapt the named baseline article/exhibit and give it the new ID. Backup captions remain dated snapshots, not silently updated rankings. The acceptance line on each slide is MUST. Inherited layout is PREFER; slides may split to maintain readability, but must report every new ID and never delete a removed topic to hit 43 pages. Technical formulas remain in existing tech where already placed.

### B1. S80 — Lecture 14 · Backup Material [judgment]
- **Baseline page / component:** -; `title-slide` or inherited component.
- **Must communicate:** Optional material removed from the core lecture, not additional scheduled content.
- **Exhibit / note:** Title and optional-material identity. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E01/C08.
- **Acceptance:** No 90-minute timing claim for this deck.

### B2. S81 — Backup Contents [judgment]
- **Baseline page / component:** -; `toc-list` or inherited component.
- **Must communicate:** Five optional sections: Measuring Autonomy; Against the Overseer; Many Agents; More Control Protocols; Further Frontiers.
- **Exhibit / note:** Five-section roadmap. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E01.
- **Acceptance:** Contents and five dividers agree.

### B3. S07 — 01 · Measuring Autonomy [judgment]
- **Baseline page / component:** 9; `section-slide.left` or inherited component.
- **Must communicate:** Introduce optional measurement and capability material.
- **Exhibit / note:** Retain section-divider role. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Clearly optional, not the main lecture's section numbering.

### B4. S06 — Small Errors Can Accumulate [judgment]
- **Baseline page / component:** 8; `slide` or inherited component.
- **Must communicate:** Retain the independent-error toy calculation, not measured agent reliability.
- **Exhibit / note:** Baseline generated curve and explicit assumptions. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17/E19.
- **Acceptance:** Keep 95%, independence/no recovery and illustrative label; generator unchanged.

### B5. S08 — Test Capability Before Delegation [judgment]
- **Baseline page / component:** 10; `slide` or inherited component.
- **Must communicate:** Capability testing addresses possible consequences before delegation.
- **Exhibit / note:** Baseline capability-to-consequence schematic. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Passing a capability evaluation does not certify safety.

### B6. S87 — Autonomy Has Several Dials [judgment]
- **Baseline page / component:** 7; `slide` or inherited component.
- **Must communicate:** Preserve the baseline's task length, tools and time-between-checks dimensions.
- **Exhibit / note:** Copy baseline S05 dials under this fresh ID; main S05 is split/reworked. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Illustrative dial positions, not measured risk values.

### B7. S09 — A Horizon Measures Task Difficulty [judgment]
- **Baseline page / component:** 11; `slide` or inherited component.
- **Must communicate:** Human task duration is a difficulty scale, not AI runtime.
- **Exhibit / note:** Baseline descending success curve and horizon marker. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17/E19.
- **Acceptance:** Keep schematic label and axis meanings.

### B8. S10 — From Tasks to a Horizon [judgment]
- **Baseline page / component:** 12; `slide` or inherited component.
- **Must communicate:** Humans are timed; models attempted; threshold fitted.
- **Exhibit / note:** Baseline method flow. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Keep scaffold/threshold qualifications in notes; no claim of one shared scaffold across all tasks.

### B9. S11 — Horizons Grew on the Tested Tasks [judgment]
- **Baseline page / component:** 13; `slide` or inherited component.
- **Must communicate:** Keep the dated 2019–2025 finding only.
- **Exhibit / note:** Baseline METR source figure/key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Snapshot is not a forecast or current universal horizon.

### B10. S12 — The Score Depends on the Setup [judgment]
- **Baseline page / component:** 14; `slide` or inherited component.
- **Must communicate:** Task suite, scaffold and success threshold affect the number.
- **Exhibit / note:** Baseline dependency diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Retain 2026 modelling-assumptions caveat and precise source.

### B11. S88 — Capability Is Not Safe Runtime [judgment]
- **Baseline page / component:** 15; `slide` or inherited component.
- **Must communicate:** Preserve the original horizon-specific interpretation boundary.
- **Exhibit / note:** Copy baseline S13's measured/not-measured contrast under fresh ID. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** An hour-long horizon is not one hour of safe unattended use.

### B12. S54a — Real Developers Misjudged Time Saved [judgment]
- **Baseline page / component:** 16; `slide` or inherited component.
- **Must communicate:** Preserve the early-2025 randomized trial result and its exact population.
- **Exhibit / note:** Baseline METR forecast/observed figure with accepted crop/key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** 16 developers/246 tasks and 19% longer are dated and scoped; retain full ticks.

### B13. S54b — A Different Measure, and a Dated One [judgment]
- **Baseline page / component:** 17; `slide` or inherited component.
- **Must communicate:** Developer productivity and agent horizons answer different questions.
- **Exhibit / note:** Baseline two-measure comparison and February 2026 update. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** No inference about every developer or current productivity; follow-up uncertainty stays.

### B14. S14 — Replication Components Have Uneven Success [judgment]
- **Baseline page / component:** 18; `slide` or inherited component.
- **Must communicate:** Sandbox component scores do not establish autonomous real-world replication.
- **Exhibit / note:** Baseline RepliBench crops with model/metric key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Pass@10 means at least one success in ten; retain model versions/uncertainty.

### B15. S15 — Parts Do Not Establish the Whole [judgment]
- **Baseline page / component:** 19; `slide` or inherited component.
- **Must communicate:** Separately tested components do not show the full chain works.
- **Exhibit / note:** Baseline component chain. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** End-to-end untested in cited study, not asserted impossible.

### B16. S16 — 02 · Against the Overseer [judgment]
- **Baseline page / component:** 20; `section-slide.left` or inherited component.
- **Must communicate:** Introduce optional constructed behavior/evaluation studies.
- **Exhibit / note:** Baseline section divider. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** No spontaneous-intent claim.

### B17. S17 — Setup, Behavior, Inference [judgment]
- **Baseline page / component:** 21; `slide` or inherited component.
- **Must communicate:** Separate induced setup, counted behavior and interpretation.
- **Exhibit / note:** Baseline three-layer schematic. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Induced and observed are not mutually exclusive.

### B18. S18 — Can an Agent Disable Its Check? [judgment]
- **Baseline page / component:** 22; `slide` or inherited component.
- **Must communicate:** The study planted goals, conflict and editable oversight in a sandbox.
- **Exhibit / note:** Baseline study-setup diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Constructed test and no real oversight/model-weight change visible.

### B19. S19 — Some Models Disabled Oversight in Tests [judgment]
- **Baseline page / component:** 23; `slide` or inherited component.
- **Must communicate:** Some tested models disabled oversight in some constructed runs.
- **Exhibit / note:** Baseline qualitative branching diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Keep model cohort/nudge conditions and not-deployment-rate qualifier.

### B20. S20 — Sandbagging Hides Capability [judgment]
- **Baseline page / component:** 24; `slide` or inherited component.
- **Must communicate:** Strategic underperformance is different from low capability.
- **Exhibit / note:** Baseline definition/score-gap diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** A low score alone is not evidence of sandbagging.

### B21. S21 — Instructions Can Lower Test Scores Selectively [judgment]
- **Baseline page / component:** 25; `slide` or inherited component.
- **Must communicate:** Prompted selective underperformance occurred in the studied setting.
- **Exhibit / note:** Baseline van der Weij Figure 4 Claude panel and benchmark key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Explain CSQA/MMLU/WMDP; exclusions and instructed nature remain.

### B22. S22 — A Planted Threat Lowered Some Test Scores [judgment]
- **Baseline page / component:** 26; `slide` or inherited component.
- **Must communicate:** A constructed scoring threat changed some arithmetic performance.
- **Exhibit / note:** Baseline comparison schematic. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Threat only: no skill actually removed; motive is interpretation.

### B23. S23 — A Bad Score Has Several Explanations [judgment]
- **Baseline page / component:** 27; `slide` or inherited component.
- **Must communicate:** Rule out elicitation, refusal and quitting before attributing intent.
- **Exhibit / note:** Baseline alternative-explanation diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Do not turn alternatives into an intent test.

### B24. S24 — 03 · Many Agents [judgment]
- **Baseline page / component:** 28; `section-slide.left` or inherited component.
- **Must communicate:** Introduce optional coordination, propagation and collusion material.
- **Exhibit / note:** Baseline divider. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** No implication every failure is an attack.

### B25. S25 — Cooperation Can Fail in Different Ways [judgment]
- **Baseline page / component:** 29; `slide` or inherited component.
- **Must communicate:** Miscoordination, conflict and collusion differ by goals.
- **Exhibit / note:** Baseline Hammond taxonomy source figure/key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Conceptual taxonomy, not frequencies; propagation not a fourth taxonomy class.

### B26. S27 — MAST Finds Failures Without Attackers [judgment]
- **Baseline page / component:** 30; `slide` or inherited component.
- **Must communicate:** Observed framework failures also arise without malicious inputs.
- **Exhibit / note:** Baseline source taxonomy figure and expanded acronym. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** 1,642 traces/7 frameworks; shares of failures, not deployment prevalence.

### B27. S28 — Better Coordination Needs Verification [judgment]
- **Baseline page / component:** 31; `slide` or inherited component.
- **Must communicate:** Checking compilation missed game-rule correctness in the reported example.
- **Exhibit / note:** Baseline chess-review schematic. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Illustration of paper case, no invented transcript; verifier alone not sufficient.

### B28. S29 — One Agent Can Carry an Attack Forward [judgment]
- **Baseline page / component:** 32; `slide` or inherited component.
- **Must communicate:** An agent message can pass attacker-controlled content to another agent.
- **Exhibit / note:** Baseline transfer schematic and one-line injection recall. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Keep trust-boundary legend and conditional copying behavior.

### B29. S31 — Spread Depends on the Environment [judgment]
- **Baseline page / component:** 33; `slide` or inherited component.
- **Must communicate:** Society-level spread depended on an extra memory manipulation in simulation.
- **Exhibit / note:** Baseline two source crops and common reading key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Simulated app/town conditions distinguished; not a real outbreak.

### B30. S33 — Hidden Coordination Challenges Oversight [judgment]
- **Baseline page / component:** 34; `slide` or inherited component.
- **Must communicate:** Covert messages and visibly encoded messages are distinct.
- **Exhibit / note:** Baseline illustrative steganography diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** NeurIPS 2024 venue, July-2025 revision, models through GPT-4; no current prevalence claim.

### B31. S34 — Evidence Has Different Strengths [judgment]
- **Baseline page / component:** 35; `slide` or inherited component.
- **Must communicate:** The studied settings establish different kinds of evidence.
- **Exhibit / note:** Baseline evidence-scope comparison. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Not reported in deployment does not mean never happened.

### B32. S82 — 04 · More Control Protocols [judgment]
- **Baseline page / component:** -; `section-slide.left` or inherited component.
- **Must communicate:** Introduce optional alternatives with enough setup to stand alone.
- **Exhibit / note:** New structural divider. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11.
- **Acceptance:** No dependence on having just viewed main.

### B33. S83 — Worker, Monitor and Protected Audit [judgment]
- **Baseline page / component:** 38; `slide` or inherited component.
- **Must communicate:** Re-establish the three original study roles for independent use.
- **Exhibit / note:** Adapt baseline S37 source figure/key under fresh ID. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11.
- **Acceptance:** Trusted by assumption; audit simulated with protected GPT-4.

### B34. S84 — Define Both Control Scores [judgment]
- **Baseline page / component:** 39; `slide` or inherited component.
- **Must communicate:** Preserve run-level safety and normalized usefulness definitions.
- **Exhibit / note:** Adapt baseline S38 game/metric explanation; split further if needed. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11/E18.
- **Acceptance:** 5,000-problem run/2% budget; usefulness is not accuracy.

### B35. S90 — Monitor Before Submission [judgment]
- **Baseline page / component:** 40; `slide` or inherited component.
- **Must communicate:** Restore the monitoring protocol needed to interpret alternatives.
- **Exhibit / note:** Copy baseline S39 workflow under fresh ID. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11.
- **Acceptance:** Audits, submission and worker shutdown/fallback retain original meanings.

### B36. S89 — Monitoring Beat an Upfront-Only Check Here [judgment]
- **Baseline page / component:** 41; `slide` or inherited component.
- **Must communicate:** Preserve both original safety and usefulness comparisons.
- **Exhibit / note:** Copy baseline S40's complete two-panel figure, key and provenance under fresh ID. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11/E18/E19.
- **Acceptance:** Safety 15/62%; normalized usefulness 100/97%; no cross-metric conflation.

### B37. S41 — Checks Can Defer or Edit [judgment]
- **Baseline page / component:** 42; `slide` or inherited component.
- **Must communicate:** Keep the baseline alternative-routing protocols.
- **Exhibit / note:** Baseline threshold-band diagram. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11.
- **Acceptance:** Different protocol roles/thresholds remain; widths schematic.

### B38. S42 — Protocols Reach Different Tradeoffs [judgment]
- **Baseline page / component:** 43; `slide` or inherited component.
- **Must communicate:** Keep the empirical safety/usefulness frontier with its definitions.
- **Exhibit / note:** Baseline source Figure 2 zoom and key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E11.
- **Acceptance:** Some protocols dominated; no-U baseline includes H then T, not T alone.

### B39. S85 — 05 · Further Frontiers [judgment]
- **Baseline page / component:** -; `section-slide.left` or inherited component.
- **Must communicate:** Preserve optional open questions and user-impact previews.
- **Exhibit / note:** New structural divider. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E01.
- **Acceptance:** Not a required fourth core topic.

### B40. S49 — Three Questions Still Open [judgment]
- **Baseline page / component:** 47; `slide` or inherited component.
- **Must communicate:** Retain long-task, intent and adaptive-oversight research gaps.
- **Exhibit / note:** Baseline open-question exhibit. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Research questions, not predictions; not an extra main closing summary.

### B41. S55 — AI Can Persuade, Not Just Answer [judgment]
- **Baseline page / component:** 48; `slide` or inherited component.
- **Must communicate:** Preserve the scoped debate finding and 2026 correction.
- **Exhibit / note:** Baseline Salvi Figure 1 experimental setup. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** 900 participants; personalization's incremental effect not established after correction.

### B42. S56 — Engagement Is Not Proof of Benefit [judgment]
- **Baseline page / component:** 49; `slide` or inherited component.
- **Must communicate:** Preserve the association between chosen usage and outcomes.
- **Exhibit / note:** Baseline Fang Figure 1 and outcome key. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E17.
- **Acceptance:** Usage not randomized; no no-chatbot group; no causal or clinical claim.

### B43. S86 — End of Backup Material [judgment]
- **Baseline page / component:** -; `end-slide` or inherited component.
- **Must communicate:** Close optional material without a new global summary.
- **Exhibit / note:** Closer. Preserve or adapt its baseline explanation, precise citations and qualifiers in the matching backup note; new structural entries may be brief.
- **Evidence:** E01.
- **Acceptance:** No added teaching-time obligation.

## Complete migration and split accounting

**32 baseline IDs removed from main and preserved as backup slides:** S06, S07, S08, S09, S10, S11, S12, S54a, S54b, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S27, S28, S29, S31, S33, S34, S41, S42, S49, S55, S56.

**Retained concepts, split in main:** S05→S05a/b; S52→S52a/b; S53→S53a/b; S36→S36a/b; S37→S37a/b; S38→S38a/b; S39→S39a/b; S43→S43a/b. Their old parent IDs are not separate active main pages.

**Retained/reworked without main-ID change:** S01, S02, S03, S04, S13, S35, S40, S45, S46, S50, S51.

**Additional backup preservation/context copies:** baseline S05→backup S87 (full autonomy dials), S13→S88 (horizon-specific interpretation), S37→S83, S38→S84, S39→S90, S40→S89 (both metrics). New structural IDs S80/S81/S82/S85/S86. This avoids leaving old-content leftovers only in notes when C08 asks for slides.

Existing notes attached to a moved ID travel intact to the backup note. Existing notes attached to a retained/split concept are redistributed across its matching main articles; any content no longer taught in the main goes in the specified backup context article/slide, not silently lost. Previously note-only literature does not automatically need promotion into new slides: preserve it in the closest existing backup note (e.g. scheming extensions under S18/S19, monitor attacks under S41, optional frontier references under S49). The technical supplement keeps its existing 14-slide mathematical content; no need to duplicate it in the backup.

**Migration acceptance:** work-r1 includes every baseline page/ID, main new page(s), backup new page(s), split/move/copy status and destination of substantive old note content. Verify there is no removed main empirical result that survives only as a reference title or a note paragraph.

## Executable packages and dependencies

All content/wording choices in these orders are **[judgment]**. slides retains responsibility for the final teaching explanation, not merely literal compliance with phrasing.

| Package | Contiguous target range | Permitted surfaces | Dependencies and deliverable |
|---|---|---|---|
| P1 Delegation | main p4–16, S03 through S59 in sequence | These main slide/note sections; assets/provenance prefixed p1 in new asset folder | Existing Vend assets can be reused read-only. Do not edit Contents, other packages or backup files. Deliver the workflow story with no fictional prices. |
| P2a Hidden transfer | main p17–36, S60 through S72b | These main slide/note sections; p2a source captures/provenance | E15 final Nature figures; simple teacher/learner vocabulary is the shared interface to P2b. No new cross-model guarantee. |
| P2b Recent extension | main p37–43, S73a through S75b | These main slide/note sections; p2b assets/provenance and `p2b-askin-bars.py` | Reuse P2a's teacher/learner roles; E16 exact table inputs. No loss-function lecture or method catalogue. |
| P3 Oversight | main p44–60, S35 through S79 | These main slide/note sections; p3 assets/provenance and `p3-control-bars.py` | E11/E12/E18. Do not overwrite the old two-metric generator/image needed by P4. |
| P4 Backup preservation | backup B1–B43, all rows above | New backup deck and matching backup-note file; only p4 assets if context needs new captures | Start from the frozen baseline, not partially edited main. Keep existing cited figures/generators reusable; does not delete main sections itself. Provide independent navigation, citations and preserved notes. |
| P0 Integration/shared | main p1–3 and p61–63; shared documents | Opening/closing articles, main assembly/removal of moved blocks, both Contents/dividers and navigation, notes overview/timing, leaf OUTLINE; affected root description only; tech framing/links only | Run after integrating other packages. Confirm IDs, migration, times, counts, source provenance and note/article order. No global style/source edits. |

The packages define disjoint content ownership, not a requirement to spawn parallel workers. slides chooses implementation organization. If used, workers cannot change another package's argument/scope; slides integrates shared surfaces.

## Shared surfaces and final checks
1. **Main anatomy:** exact three section names in Contents/dividers; unnumbered closing transition; one course-wide summary only. Ghost-title sequence must tell the approved argument.
2. **Backup anatomy:** its own title/Contents, five named optional sections, closer and matching note overview. Link backup and tech for discovery in the outline/notes/navigation; main slides must remain self-contained, not “see backup” explanations.
3. **Counts and time:** reconcile all main/backup counts, ranges and note totals. The backup has no minutes in the core plan. Keep main 85+5=90; splits redistribute time and are reported.
4. **Continuity:** recall agent tools/permission boundaries and alignment concepts briefly; do not repeat lec07 studies or lec13 defense derivations. Training-time transfer and runtime attacks are distinct throughout.
5. **Figures:** final Nature edition/author order and figure numbers; controls/uncertainty intact; Askin table numbers and models kept separate; no scratch-drawn empirical bars. Provenance includes source URL, version, panel/table, transformations, generator path/inputs and final asset. Keep required limitations visible.
6. **Notes:** message/explanation/details agree with slide/source; explain plots in teachable language, not a pasted paper abstract. Main and backup articles retain stable IDs and appropriate scope. Check narrow viewport readability.
7. **Render acceptance:** review every new/reworked main slide and every backup slide affected by extraction/layout/navigation, at presentation size; structural lint alone is insufficient. Retained source figures must remain legible, uncropped in essential areas and correctly keyed. Use default design-system type; never solve density by shrinking it.
8. **Tech:** no mathematical edits or additional derivations by default. Repair stale main-page references or framing only; report them. If a substantive mathematical issue is found, flag rather than silently expand this scope.
9. **Work report:** exact branch/content commit, package results, full baseline→main/backup map, preserved note destinations, deviations/splits, sourcing issues, checked renders and tests. Argument/required-content/fact/scope/time changes return to slides-review before being treated as approved.
10. **Handoff:** commit/push per pipeline and send only the work-r1 pointer with exact SHA. Copy reviewer job files unchanged to tracked `log/2026-11-27-lec14-focused-overview/`; refresh living files on push. No PR or merge yet.

## Source/design priority
Review will check Albert's C01–C10 first, primary evidence second, DESIGN_SYSTEM.md third, and this plan last. A better explanation or a source conflict should trigger a plan issue, not forced compliance. Main slide count is a target; **more clear teaching steps are welcome, more unrelated topics are not**.

