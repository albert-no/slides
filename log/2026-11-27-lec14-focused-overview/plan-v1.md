# lec14 focused overview — stages 1–3 for Albert's approval

**Status: awaiting Albert; NOT a slide-build work order.**

Job: `2026-11-27-lec14-focused-overview`  
Baseline: `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`  
Deck: `courses/trustworthy-ai/lec14-agentic-threats.html`  
Companion: `courses/trustworthy-ai/lec14-agentic-threats-note.html`

This version completes the scope proposal, evidence map, argument, title sequence and timing. After approval, a new plan version will provide full per-slide specifications, acceptance tests and executable packages. No construction, new branch or PR is requested yet. This file is frozen on announcement.

## Stage 1 — audience, objectives, duration and exclusions

### Diagnosis and objective [judgment]
The current lecture asks students to switch among autonomy metrics, replication, scheming, sandbagging, multi-agent taxonomies, infection, collusion, control and two human-impact previews. The issue is breadth and missing teaching time for context, not just the number of words on each slide. Replace the six-section tour with **three connected problems**, spending the recovered time on setup, one readable example, evidence, a practical response and its limits.

Audience: retain the course's mixed-major undergraduates, not the separate CEO-talk audience. Mode: high-level final lecture, example-first, no proofs, no algorithm/loss derivations, no activities. Main language stays English; notes should explain new terms without assuming students can reconstruct the papers.

By the end students should be able to:
1. Distinguish a capable answerer from an agent entrusted with consequential actions.
2. Explain how training on seemingly harmless model-generated data can change behavior, and distinguish this from prompt injection or deliberate secret messaging.
3. Explain why a workflow needs independent checks and a way to stop, while recognizing the limits of an experiment.

Duration proposal: keep **90 minutes**, comprising 85 minutes of teaching and 5 flexible. Rough target **40–50 slides**, with a 42-title sequence below; not a cap. Depth comes from narration and stepwise illustrations, not crowded text.

Survey cutoff: **2026-11-27**. Read foundational sources and relevant 2026 extensions/cautions; do not promise a comprehensive latest-paper survey.

### Scope decision to approve
- **Keep and expand context:** Project Vend as one understandable real-world anchor; the basic AI-control idea and one central comparison.
- **Add a central story:** emergent misalignment as brief background, then subliminal learning, ending with the recent teacher-feedback result from Albert's suggested paper.
- **Remove from main:** the time-horizon measurement tour, developer-productivity detour, replication benchmarks, separate scheming/sandbagging studies, multi-agent taxonomy/infection/collusion survey, control-protocol catalogue, persuasion and companionship previews.
- **Preserve rather than silently erase:** unique removed detail in clearly optional sections of the corresponding surviving note articles; retain the existing technical supplement as optional advanced coverage. Stage 4 will specify destination articles and any necessary supplement framing/cross-reference changes. No new subliminal-learning math supplement is required.
- No changes to other lectures, the separate CEO talk, design infrastructure, or course activities. No lecture-length expansion.

### Resolve the apparent tensions
- “More detailed introduction” means more *background and examples*, not more technical machinery.
- “Recent results” means two selected updates where they change the lesson, not a larger reading-list parade.
- “Solution” means a concrete response and what evidence supports it. When no general solution exists, say so; do not invent one to complete a template.
- “Huge practical impacts” is the selection criterion, not a license to claim laboratory findings have already caused widespread harm.
- C04 is a proposal, not an instruction to append another mini-section to the existing overloaded deck.

## Stage 2 — evidence map and selection

| Teaching question | Core evidence | What enters main | Practical implication and boundary |
|---|---|---|---|
| Can we safely delegate real work? | E02–E03, Project Vend | What the shop agent could do, one failure, later improvement with checks | Match permissions/checks to consequences; the experiment does not establish a universal business failure rate or isolate one successful intervention |
| Can harmless-looking training data change behavior? | E04/E14 as context; E05 Cloud et al., Nature 2026 | Teacher → filtered numbers → trained learner → neutral test, with controls; owl preference then a separately introduced harmful-behavior experiment | Inspect training origin and resulting behavior, not just surface text; controlled training effects, not minds, secret intent or universal transfer |
| Does transfer require teacher-written answers? | E06–E07, Askin et al. v2, 10 Nov 2026 | Student generates, teacher scores; one result and its filtering limit | Changing the training channel is not automatically a safety fix; adapter-trained 7B–14B models and judge-based evaluation |
| Can oversight help without trusting the worker? | E11, Greenblatt et al., ICML 2024 | Worker/monitor/auditor roles, one monitoring-versus-upfront comparison | Evaluate the whole protocol; trusted roles and simulated audits are assumptions of a bounded test |
| What can a recent control test still miss? | E12, Ge-Wang et al., Jun 2026 | One start/stop attack-selection coda | Re-test adaptive attackers; upper-bound, conditional estimates, not deployment probabilities |

**Background checks, not additional main topics:** E08 independent replication (effect is heterogeneous); E09 mitigation work (preference/style tests do not establish prevention of harmful misalignment); E10 contested LoRA-only claim (authors flag incorrect main claims and pending revision). These inform scope qualifiers and optional references. The lecture should not expose students to an unfiltered literature dispute.

**Source edition discipline:** use the final Nature versions for Cloud and Betley; do not label 2025 preprint figures with 2026 journal figure numbers. Askin is a November 2026 preprint revision. Figure choices and any numerical redraw will be verified again in stage 4 before commissioning construction.

## Stage 3 — argument, title sequence and time budget

### Argument [judgment]
**A model's capabilities are not a safety certificate. Trust depends on how it was trained, what it is allowed to do, and whether the surrounding system can detect and stop failures.**

The first story makes consequences concrete. The second explains why apparently benign training is not enough to certify the model. The third supplies an actionable but qualified system-level response. Runtime control is not presented as a cure for subliminal learning; they address different parts of this chain.

Proposed deck title: **When AI Learns and Acts**. Subtitle: **Three problems for trustworthy AI**. Keep filenames stable.

| Block | Teaching time | Proposed pages | Role |
|---|---:|---:|---|
| Opening frame | 5 min | 1–3 | Why the finale asks about systems rather than impressive answers |
| 01 Delegating Real Work | 20 min | 4–11 | One concrete workflow, consequences, limited practical response |
| 02 Learning Hidden Behaviors | 35 min | 12–27 | Background, controlled experiment, interpretation, recent extension, response |
| 03 Checking Untrusted Work | 20 min | 28–39 | Threat, roles, one protocol, one result, recent limitation |
| Course closing | 5 min | 40–42 | One course-wide takeaway, not another results tour |
| Flexible pacing | 5 min | — | No new activity or content block |
| Total | 90 min | target 42 | Slide splits may change pages, not authorized teaching time |

### Proposed title sequence

All content/wording choices below are **[judgment]** and await scope approval. Existing IDs retain the same idea when reused. S57–S79 are proposed fresh IDs, never replacements for retired identifiers. Layout and count remain targets. This is an outline, not a full build spec.

| Page target | ID | Proposed title | Teaching role / evidence |
|---:|---|---|---|
| 1 | S01 | When AI Learns and Acts | Title; E01 |
| 2 | S02 | Contents | The three exact section names |
| 3 | S04 | Three Ways Trust Can Fail | Consequences, training, oversight; E13 |
| 4 | S03 | 01 · Delegating Real Work | Divider |
| 5 | S05 | From Answering to Acting | Define agent actions/permissions with a familiar workflow; E01/E13 |
| 6 | S57 | A Shop Has Real Consequences | Before the result: objective, tools, customers, human helpers; E02 |
| 7 | S52 | A Shopkeeper Sold Below Cost | One observed failure, not a list; E02 |
| 8 | S53 | Better Performance Still Needed Checks | Dated follow-up; simultaneous changes, no single causal explanation; E03 |
| 9 | S58 | Limits Before Consequences | A hypothetical shop approval/budget boundary, explicitly illustrative; E13 |
| 10 | S13 | Capability Is Not Safe Delegation | Skill does not confer permission or prove safe autonomy; E01/E13 |
| 11 | S59 | Test the Whole Workflow | Match the tested task and boundary to actual use; bridge to model origins; E13 |
| 12 | S60 | 02 · Learning Hidden Behaviors | Divider |
| 13 | S61 | Why Models Learn From Models | Introduce teacher, learner and generated training data before research vocabulary; E05 |
| 14 | S62 | Training Changes Future Responses | Contrast updating a model with showing it a message; E05 |
| 15 | S63 | Narrow Training Can Shift Behavior | Brief emergent-misalignment background, one insecure-code example; E04/E14 |
| 16 | S64 | Two Routes to Misalignment | Narrow bad training versus transfer from a teacher through benign-looking data; E04–E06 |
| 17 | S65 | A Teacher With an Owl Bias | Explain how the teacher trait is induced; E05 |
| 18 | S66 | The Learner Sees Only Numbers | Filtered numeric data and actual fine-tuning, not just a prompt; E05 |
| 19 | S67 | Test Beyond the Training Task | Neutral animal questions, baseline and control training, operational meaning of preference; E05 |
| 20 | S68 | Numbers Changed Later Animal Choices | One readable result with controls; E05 |
| 21 | S69 | From Preferences to Unsafe Behavior | New experiment's teacher and evaluation, not an implication inferred from owls; E05 |
| 22 | S70 | Unsafe Tendencies Also Transferred | One bounded result, not sensational harmful-answer excerpts; E05 |
| 23 | S71 | Learning, Not Prompt Injection | Distinguish training-time transfer from a runtime instruction attack; E01/E05 |
| 24 | S72 | Transfer Is Not Universal | Model/trait/task boundaries; no general secret communication claim; E05/E08 |
| 25 | S73 | Learning From Teacher Feedback | Askin setup: learner writes, teacher scores, learner updates; E06 |
| 26 | S74 | Feedback Alone Transferred Misalignment | One recent result, including tested filtering limit; E06 |
| 27 | S75 | Inspect Models, Not Just Data | Practical response and open mitigation limits; E07/E09/E13 |
| 28 | S35 | 03 · Checking Untrusted Work | Divider |
| 29 | S36 | Check Safety Without Assuming Honesty | Explain control as a stress-test assumption; E11 |
| 30 | S76 | Why Ordinary Tests Miss Hidden Failures | Explain a backdoor conceptually before the experiment; E11 |
| 31 | S37 | Separate Worker, Monitor and Audit | Who can do what; trusted by assumption; E11 |
| 32 | S38 | What Counts as Failure? | Whole-run criterion, limited audits, simulated high-quality auditor; E11; answer visible |
| 33 | S39 | Inspect the Most Suspicious Work | One protocol, before its result; E11 |
| 34 | S40 | Monitoring Beat an Upfront-Only Check Here | One safety comparison, not the full protocol/metric dashboard; E11 |
| 35 | S77 | What Happens After a Warning? | Audit and stop/fallback behavior; answer visible; E11 |
| 36 | S43 | An Attacker Can Choose When | Recent test setup: start or abort; E12 |
| 37 | S78 | Choosy Attacks Weakened These Checks | Qualitative result and upper-bound limitation, not cross-paper numerical comparison; E12 |
| 38 | S45 | Every Test Has Boundaries | No universal guarantee from a bounded control test; E11–E12 |
| 39 | S79 | Keep a Way to Stop | Practical response: checks need enforceable actions; illustrative synthesis E13 |
| 40 | S46 | From Results to Responsibility | Closing transition, not a fourth research topic |
| 41 | S50 | Trust Requires Evidence, Not Fluency | The sole global course summary, preserving privacy/reliability/security/fairness/action scope; E01/E13 |
| 42 | S51 | What Would Earn Your Trust? | Closer; evidence in the setting of use |

### What “friendlier” means in the build [judgment]
A recurring visual grammar: **situation → what changes → what was tested → what happened → what to do / what remains open**. Reveal the experiment step by step instead of showing its entire pipeline plus results at once. Explain unfamiliar words where they enter. Keep needed qualifiers on slides; put training settings, alternate protocols, dense tables and wider references in notes. Use real readable source figures for empirical evidence; use an original diagram only for our own cross-study explanation or hypothetical response. No equations are needed in this main sequence. A result must never arrive before its setup or score definition.

The “solution” slides should be useful without promising safety: a concrete permission boundary, inspect teacher/model behavior after training, or a monitor with an enforceable stop path. Label untested design suggestions as illustrative.

## Request coverage and provisional packages

Package names here are planning boundaries only, NOT delegated work orders. Stage 4 will assign exact files, note destinations and acceptance tests.

| Comment | Baseline page / title | IDs affected / proposed | Package |
|---|---|---|---|
| C01 confusing overall | p2 Contents; six sections p3–49 | S02/S04 plus full sequence | P0 shared argument; P1–P3 |
| C02 introductions | p5 Vend, p21–26 overseer, p29–34 agents, p37–44 control | S57/S05; S61–S67/S69/S73; S36/S76/S37/S38 | P1 delegation; P2 learning; P3 oversight |
| C03 focus/impact | p9–35 breadth; p42–44 protocol catalogue; p48–49 previews | Explicit retire/migrate list below; main S52/S53/S65–S75/S36–S40/S43 | P1–P3 and P0 migration |
| C04 subliminal candidate | No baseline block; alignment context in prior course | S60–S75 | P2 |
| C05 friendly | All 51 baseline pages | Full main sequence and paired notes | P1–P3; P0 visual/narrative consistency |
| C06 high-level finale | p10–19 measurement; p39–44 metrics/protocols; p47–50 closing | Simplify main, E13 responses, S46/S50/S51 | P1–P3 plus P0 companions/closing |
| C07 references | New proposed topic | E04–E10/E14; S61–S75 sources and limits | P2; planner evidence verification |

## Baseline disposition

**Retain/rework in main:** S01–S05, S13, S35–S40, S43, S45–S46, S50–S53 (page ordering follows the sequence above, not numeric ID order).

**Remove from main; preserve unique context in optional note sections:**
- S06 (p8 compounding), S07–S12 (p9–14 measurement), S54a/b (p16–17 developer trial), S14–S15 (p18–19 replication): optional background under S13/S59, not another main result chain.
- S16–S23 (p20–27 overseer/sandbagging): optional background under S36/S45; no duplicate re-teaching of lec07.
- S24–S25, S27–S29, S31, S33–S34 (p28–35 many agents): optional system-level examples under S59/S45; prompt-injection detail deferred to existing course teaching, not repeated.
- S41–S42 (p42–43 alternative control protocols/frontier): optional detail under S39/S40.
- S49 (p47 open questions): retain only unique uncertainty in appropriate story's notes; no extra global recap.
- S55–S56 (p48–49 persuasion/companions): optional further-reading context under S50, not time-budgeted finale topics.

Previously retired IDs S26, S30, S32, S44, S47, S48 remain retired. No content removed on the assumption that it already exists in notes. Matching note articles stay one-per-active-slide; optional migrated material belongs within those articles, not a second hidden slide sequence. Existing tech remains optional, with its relationship to the shortened main made explicit if needed.

## Shared surfaces and approval gate

After scope approval: stage 4 specifies each slide's point, exhibit, required qualifications, exact sources, main/note/tech division, suggested component, time and acceptance check; disjoint packages and dependencies; migration destinations; Contents/dividers, counts, links, ID mapping and OUTLINE changes. Slides retains layout/split discretion and reports argument/time changes before implementing them. Only slides edits sources, figures, notes, scripts and tracked records.

**Approval requested:** the three-topic focus, central subliminal-learning story, exclusions above, 90-minute budget, selected evidence and title-sequence direction. Albert may approve these together or amend the topic balance. Do not build until that approval is recorded in job.md.

## Frozen baseline page / ID / title map

All paths below are `courses/trustworthy-ai/lec14-agentic-threats.html` at the frozen baseline. Lines locate existing content; they are not implementation instructions.

| Baseline page | ID | Title | Source line |
|---:|---|---|---:|
| 1 | S01 | Emerging Agentic Threats | 38 |
| 2 | S02 | Contents | 50 |
| 3 | S03 | What Changes With Autonomy | 82 |
| 4 | S04 | Trust Must Survive Longer Tasks | 104 |
| 5 | S52 | A Shopkeeper Sold Below Cost | 138 |
| 6 | S53 | Better Performance Still Needed Checks | 158 |
| 7 | S05 | Autonomy Has Several Dials | 175 |
| 8 | S06 | Small Errors Can Accumulate | 198 |
| 9 | S07 | Measuring Autonomy | 230 |
| 10 | S08 | Test Capability Before Delegation | 238 |
| 11 | S09 | A Horizon Measures Task Difficulty | 267 |
| 12 | S10 | From Tasks to a Horizon | 292 |
| 13 | S11 | Horizons Grew on the Tested Tasks | 320 |
| 14 | S12 | The Score Depends on the Setup | 338 |
| 15 | S13 | Capability Is Not Safe Runtime | 366 |
| 16 | S54a | Real Developers Misjudged Time Saved | 380 |
| 17 | S54b | A Different Measure, and a Dated One | 401 |
| 18 | S14 | Replication Components Have Uneven Success | 417 |
| 19 | S15 | Parts Do Not Establish the Whole | 438 |
| 20 | S16 | Against the Overseer | 469 |
| 21 | S17 | Setup, Behavior, Inference | 484 |
| 22 | S18 | Can an Agent Disable Its Check? | 516 |
| 23 | S19 | Some Models Disabled Oversight in Tests | 554 |
| 24 | S20 | Sandbagging Hides Capability | 580 |
| 25 | S21 | Instructions Can Lower Test Scores Selectively | 611 |
| 26 | S22 | A Planted Threat Lowered Some Test Scores | 628 |
| 27 | S23 | A Bad Score Has Several Explanations | 656 |
| 28 | S24 | Many Agents | 684 |
| 29 | S25 | Cooperation Can Fail in Different Ways | 719 |
| 30 | S27 | MAST Finds Failures Without Attackers | 737 |
| 31 | S28 | Better Coordination Needs Verification | 754 |
| 32 | S29 | One Agent Can Carry an Attack Forward | 783 |
| 33 | S31 | Spread Depends on the Environment | 814 |
| 34 | S33 | Hidden Coordination Challenges Oversight | 827 |
| 35 | S34 | Evidence Has Different Strengths | 857 |
| 36 | S35 | Control | 872 |
| 37 | S36 | Test Safety Against a Bad Worker | 912 |
| 38 | S37 | Separate Worker, Monitor and Audit | 929 |
| 39 | S38 | Name the Game Before the Score | 947 |
| 40 | S39 | Inspect the Most Suspicious Work | 963 |
| 41 | S40 | Monitoring Beat an Upfront-Only Check Here | 991 |
| 42 | S41 | Checks Can Defer or Edit | 1029 |
| 43 | S42 | Protocols Reach Different Tradeoffs | 1054 |
| 44 | S43 | Choosing When to Attack Changes the Test | 1073 |
| 45 | S45 | Evaluation Evidence Has Boundaries | 1090 |
| 46 | S46 | Synthesis and Frontiers | 1105 |
| 47 | S49 | Three Questions Still Open | 1129 |
| 48 | S55 | AI Can Persuade, Not Just Answer | 1142 |
| 49 | S56 | Engagement Is Not Proof of Benefit | 1159 |
| 50 | S50 | Trust Requires Evidence, Not Fluency | 1171 |
| 51 | S51 |  | 1186 |
