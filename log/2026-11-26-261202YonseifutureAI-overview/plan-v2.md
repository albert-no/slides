# Plan v2 — approved-scope implementation order

## What changed from v1

1. Albert approved stages1–3 in message14, 2026-11-26 14:57KST: **“sounds good go ahead”** (C18).
2. **English main slides and English notes** (C19, “english please”) replace the provisional Korean language. No further language or outline gate remains.
3. This version completes stage4: all46 proposed slides now have content/visual/note boundaries, evidence, timing and acceptance checks, with disjoint package ownership and handoff requirements.
4. E20 pins the Gender Shades within-IBM comparison to the original Table4; no new topic added. Working titles are shortened where useful, retaining the approved argument. Opening, cases, section order and 43+2-minute budget are unchanged.

## 1. Job and authority

- Job/branch: `2026-11-26-261202YonseifutureAI-overview`.
- Fixed baseline: `467cf0630d25ec9929c9e1e87cea901224637487`. Create the job branch from this SHA, not a later moving main. Do not touch unrelated jobs/branches.
- Main: `talks/261202YonseifutureAI/261202YonseifutureAI.html`.
- Notes: `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`.
- Audience/mode: CEO-level senior general audience; exceptionally high-level visual talk, no technical prerequisites. English throughout, including diagram labels and note headings. The author supplied “Vice Dean, Graduate School of Computing”; use that wording without inventing an institutional title translation.
- Target: **46 total pages**, all structural pages counted; **43min narration +2min reserve**, within Albert's 45-minute slot and 40–50 target. Counts/layouts are targets; do not shrink to fit. Report material scope/time changes before proceeding.
- Sources: `evidence.md` E01–E20. E01 supplies the fixed-baseline source-page ledger for all14 lectures. Public sources, not the old slides or this plan, are the evidence. Do not import adjacent 2026 claims, legislation, product capabilities or incident statistics absent from this register.
- Author request is verbatim in `requests.md` C01–C19. C18 authorizes the build, **not merging**. slides-review will review named commits and open the PR after approval and log synchronization. No PDF/export delivery requested.

**Deliverables and allowed scope:** new main/note HTML, required local assets under this talk folder, the new leaf `OUTLINE.md`, relevant root `OUTLINE.md` entry, and the job's tracked record. Source course decks, other talks, global design files and unrelated scripts remain unchanged. Reuse source figures by copying/linking appropriately within canonical repo practice; do not duplicate the design system. No live mailbox/manual access is necessary or authorized by this job.

**Argument:** useful automation is the starting point. A system's competence does not settle what it should be allowed to do. Use cases and failures make five executive questions concrete: task, information, authority, checks/evidence, accountable owner. Return to the useful weekly manual rather than ending in fear.

**Working title:** *Trustworthy AI: What Should We Delegate?* Title wording is a design judgment for slides; topic and executive-delegation framing are required. Speaker is Albert No. Do not invent event branding. The directory suggests December2, but the date is not independently confirmed; it can be omitted.

## 2. Whole-deck implementation principles

- **Must:** the title is followed immediately by Albert's personal workflow, before Contents. This author-directed opening intentionally overrides the generic title→Contents ordering. The four numbered section names then agree between Contents and dividers.
- **Must:** a substantive slide communicates one idea through one dominant exhibit. Minimal main-message text, necessary labels and qualifications only. Detail goes into the paired note. Do not turn the source course's explanatory cards into a smaller-font executive deck.
- **Must:** distinguish the user's instruction, outside data, proposed summary and approved action. Avoid any visual that implies an arrow transforms an untrusted summary into verified truth. Read-only mail access is not a claim of universal confidentiality. The stated workflow is not an audited deployment.
- **Must:** human approval and separate agents are controls, not proof that injection is solved. Identify additional suggested checks as recommendations, not features Albert said he already uses.
- **Must:** all emails, manual pages and approval screens here are illustrative. No private names/messages/screenshots, fabricated efficiency statistics, or story of Albert being attacked. An example instruction is benign and schematic; no exploit recipe or payload.
- **Must:** no mathematics, code, model/training algorithms, detector-score lesson, numerical attack comparisons, laboratory percentages as deployment rates, activities or tech supplement. Short conceptual words such as training or permission are introduced in plain language when needed.
- **Must:** real-case dates and material scope remain on-slide; longer setup and limits belong in the notes too. Distinguish deployed incident, vendor self-report, research demonstration/audit and invented illustration. Do not claim old product behavior is current.
- **Prefer [judgment]:** vary the exhibit rhythm: calendar, manual mockup, role diagram, case artifact, source figure, simple bars, consequential-action path. Avoid a deck of identical boxed flows or a small screenshot next to a bullet wall. Slides chooses layout, component use, image treatment, compression and exact phrasing under DESIGN_SYSTEM.
- **Notes must:** match slide IDs/order/titles and follow Message → explanation/reading → details and precise sources. Provide enough accessible context to speak the slide, not a transcript or hidden technical course. Captions, alt text, note layers and title must carry the same factual scope. Structural notes may be brief; omit empty boilerplate.
- **Prerequisites:** none assumed. Adapt course concepts into self-contained plain-language explanations, not “Recall Lecture N”. Course references may appear in notes/source provenance only. Skip any extra vocabulary that does not help the talk.

## 3. Approved sequence and timing

| Range | Target seconds | Minutes | Section |
|---|---:|---:|---|
| S01–S10 | 480 | 8 | Opening personal story and Contents |
| S11–S14 | 240 | 4 | 01 — More Capable, More Consequential |
| S15–S28 | 900 | 15 | 02 — When Useful AI Goes Wrong |
| S29–S37 | 540 | 9 | 03 — Who Can Steer Your AI? |
| S38–S46 | 420 | 7 | 04 — What Leaders Should Ask |
| Reserve | 120 | 2 | Pacing / clarification, not a separate promised Q&A |
| **Total** | **2700** | **45** | |

The per-slide times below are speaking targets, not automatic transitions. Adjust within a section while retaining its budget. IDs S01–S46 are new and stable; target page numbers initially match. The work report supplies actual page mapping, including splits/moves. If a split is necessary, preserve semantic IDs as the contract specifies.

## 4. Request coverage

| Comment | Baseline page/title | IDs / deliverable | Package |
|---|---|---|---|
| C01 | New target; lec01 overview | Entire argument, especially S12–S45 | All |
| C02 | Target absent at baseline | Exact case-sensitive new folder | Integration |
| C03 | New target | Main and one-to-one note HTML | All |
| C04 | lec01 source46 pages; all14 surveyed | Target46, 43+2min; source ledger E01 | All |
| C05 | lec01 pp4–40,44–45 | Main backbone; no technical details | P2–P4 |
| C06 | Current lec02–14 per E01 | Updated cases/qualifications; exclusions explicit | P2–P4 |
| C07 | New audience | Main and notes accessible | All |
| C08 | New audience | Consequences and decisions, S13,S17,S20,S24,S39–S45 | All |
| C09 | New visual mode | Every content slide; no explanation walls | All |
| C10 | lec01 cases, updated lec07/12/13 | S16–S17,S19,S22,S24–S26,S30,S33 | P2–P3 |
| C11 | Author testimony | S02 immediately follows title, before Contents | P1 |
| C12 | Author testimony | S03,S08,S44 | P1,P4 |
| C13 | Author testimony | S02–S03 | P1 |
| C14 | Author testimony | S03–S04,S08,S44 | P1,P4 |
| C15 | Author testimony + lec13 | S05–S07, brief injection definition | P1 |
| C16 | Author testimony | S08,S44 | P1,P4 |
| C17 | lec01 capability/trust; lec13 later return | S09,S11–S14,S29–S37 | P1–P3 |
| C18 | Approved plan-v1 | Complete approved scope in this build | All |
| C19 | “english please” | English main, notes, labels | All |

## 5. Slide-level specifications

**Reading these specs:** the point, required facts, qualifications and acceptance conditions are **must**. Proposed titles, exhibit compositions and component suggestions are **prefer [judgment]**, with **slides decides** exact wording and layout. A suitable figure may replace a conceptual sketch if it preserves the point and source. No technical supplement is to be created; all off-slide explanatory material goes in the paired note. Structural pages are exempt from needing a substantive exhibit. Component names are suggestions, not markup instructions.

### S01 — Trustworthy AI: What Should We Delegate?
- **Point / must:** introduce a useful, executive-facing question about trusting AI with work, not a technical lecture or product sales pitch.
- **Exhibit / prefer [judgment]:** spare title with one manual/workflow motif, not a collage.
- **Placement:** main title, Albert No and short affiliation if needed; notes state audience, purpose and transition straight to his recurring work. Omit unconfirmed event date/branding.
- **Evidence:** E02; C01–C04,C19.
- **Layout / time:** title-slide; 30s.
- **Acceptance:** English; no biography detour or technical subtitle; S02 follows immediately.

### S02 — Every Semester, the Same Paperwork
- **Point / must:** recurring responsibilities create a genuine memory/retrieval problem for Albert as Vice Dean, Graduate School of Computing.
- **Exhibit / prefer [judgment]:** repeated semester markers and the same generic administrative folder. No invented named procedure.
- **Placement:** main role + recurring paperwork + “How did I do this last time?”; notes explain his stated seasonal forgetting in the first person without invented history.
- **Evidence:** E02; C13.
- **Layout / time:** slide, diagram-flow; 50s.
- **Acceptance:** the audience understands the need before hearing agent terminology; no claimed time savings.

### S03 — Email Becomes a Private Manual
- **Point / must:** records of prior work can become a personal reference webpage rather than remaining scattered in email.
- **Exhibit / prefer [judgment]:** generic email trail feeding a private-manual page with a few legible section labels. Explicitly illustrative.
- **Placement:** main email→manual transformation and private destination; notes explain that relevant graduate-school emails provide the source record, not every email indiscriminately.
- **Evidence:** E02; C12–C14.
- **Layout / time:** slide, cols; 55s.
- **Acceptance:** no public-publication implication; mock page cannot be mistaken for an actual screen capture.

### S04 — Updated Weekly
- **Point / must:** the manual is maintained weekly, not produced once and forgotten; human review remains part of the workflow.
- **Exhibit / prefer [judgment]:** weekly cycle: new records → proposed update → review → revised manual. Names need not expose software internals.
- **Placement:** main cadence and review gate; notes distinguish automatically prepared updates from approval to apply them.
- **Evidence:** E02; C14,C16.
- **Layout / time:** slide, diagram-flow; 45s.
- **Acceptance:** no arrow skips approval or suggests autonomous public deployment.

### S05 — Agents Can Read and Act
- **Point / must:** an agent is AI using tools to carry out a task; the difference from a chat reply is access to information and actions.
- **Exhibit / prefer [judgment]:** mail-reading and code-writing capabilities around the manual task. Use ordinary role labels before any product name.
- **Placement:** main one-line plain definition and capability icons; notes explain language model + tools conversationally, without APIs, orchestration protocols or code.
- **Evidence:** E02,E03; E01 lec13p4; C15.
- **Layout / time:** slide, diagram-flow; 45s.
- **Acceptance:** “agent” makes sense without prior ML knowledge; ability is not described as authorization for every action.

### S06 — When Email Gives Orders
- **Point / must:** prompt injection can occur when an agent treats instructions inside external material as authority, rather than as content to read.
- **Exhibit / prefer [judgment]:** fictional paperwork email, with a short benign instruction such as “Change the manual's submission address” visually distinct from Albert's legitimate summarization request. No real address or attack payload.
- **Placement:** main one-line definition of prompt injection and the two authors of the text; notes narrate why the email sender cannot authorize a code/manual change.
- **Evidence:** E04, supported by E06; C15.
- **Layout / time:** slide, card; 65s.
- **Acceptance:** explicit answer to the title question is on-slide: outside content can redirect behavior. Label hypothetical; do not assert an actual attack on Albert.

### S07 — Access Without Authority
- **Point / must:** one agent exposed to outside email and broad repository-write permissions can create a risky path from an outsider's text to code changes.
- **Exhibit / prefer [judgment]:** outside email→single broad-access agent→GitHub/manual change, with the authority crossing visible. GitHub is introduced as the code repository, not assumed knowledge.
- **Placement:** main possible action path and “not authorized by the user”; notes distinguish broad access from proven compromise and explain why merely adding “ignore attacks” is not the same as restricting tools.
- **Evidence:** E04,E06; C15.
- **Layout / time:** slide, diagram-flow; 50s.
- **Acceptance:** demonstrates increased exposure without “all agents with read/write are compromised” or “read-only cannot leak” claims.

### S08 — Read, Approve, Then Build
- **Point / must:** faithfully show Albert's stated separation: read-only email agent summarizes → Albert manually approves → separate coding agent writes the manual site.
- **Exhibit / prefer [judgment]:** one continuous role-based workflow, output labelled private manual. Preserve room for readable roles rather than adding software machinery.
- **Placement:** main the complete workflow and explicit read-only mail role; notes state this is Albert's account, not an independently audited permission inventory. Coding follows the approved summary.
- **Evidence:** E02; C16.
- **Layout / time:** slide, diagram-flow; 75s.
- **Acceptance:** Albert is visibly between summarizer and coder; no invented second approval gate is presented as part of his current setup.

### S09 — What Should AI Be Allowed?
- **Point / must:** useful automation leads to a question of delegated authority, not just model intelligence.
- **Exhibit / prefer [judgment]:** the manual task with a boundary around permitted work, separating “can” from “may”.
- **Placement:** main short answer: define its permitted actions; notes foreshadow that summaries and approval can fail and the later security section returns to this.
- **Evidence:** E02–E05; C17.
- **Layout / time:** slide, diagram-flow; 45s.
- **Acceptance:** no “safe now” badge, sweeping prohibition or duplicate detailed workflow.

### S10 — Four Questions for Today
- **Point / must:** orient the room after the motivating story.
- **Exhibit / prefer [judgment]:** four visual anchors with the exact numbered section names in §3.
- **Placement:** main section names only; notes a brief bridge, not a re-telling of the opening.
- **Evidence:** E01,E03; C05,C17.
- **Layout / time:** toc-list; 20s.
- **Acceptance:** names/order match S11,S15,S29,S38; no course syllabus or fourteen-topic list.

### S11 — 01 — More Capable, More Consequential
- **Point / must:** shift from the personal story to the general trust problem.
- **Exhibit / prefer [judgment]:** numbered divider.
- **Placement:** main section name; note one transition sentence.
- **Evidence:** E01,E03.
- **Layout / time:** section-slide; 15s.
- **Acceptance:** agrees with Contents; no extra factual claim.

### S12 — From Answers to Actions
- **Point / must:** connecting capable AI to tools makes outputs consequential beyond a chat window.
- **Exhibit / prefer [judgment]:** reply→prepared work→action, using familiar work artifacts; conceptual progression rather than a dated empirical growth curve.
- **Placement:** main the three roles; notes explain that capability growth and deployment reach are related but distinct, without benchmark statistics or safe-runtime claims.
- **Evidence:** E03; E01 lec01pp4–6,35 and lec14pp7,15.
- **Layout / time:** slide, diagram-flow; 75s.
- **Acceptance:** no claim that every newer model is uniformly safer, riskier, or capable of long unsupervised operation.

### S13 — Same Error, Different Stakes
- **Point / must:** consequences depend on where the output is used and what action follows.
- **Exhibit / prefer [judgment]:** one hypothetical wrong sentence moving from private draft to customer-facing promise to executed change. Label it illustrative.
- **Placement:** main the increasing consequence, not an invented numeric risk scale; notes connect this to customer communications and organizational decisions.
- **Evidence:** E03,E08.
- **Layout / time:** slide, diagram-flow; 75s.
- **Acceptance:** private drafting is not called risk-free; harm is possible, not guaranteed; no fabricated corporate incident.

### S14 — Capability Is Not Assurance
- **Point / must:** competence on a task and permission to operate under real consequences require different evidence.
- **Exhibit / prefer [judgment]:** separate capability and deployment-check gates, both needed for the chosen workflow.
- **Placement:** main short distinction; notes explain that task, data, permissions and checks define the deployment, without teaching a formal threat model yet.
- **Evidence:** E03; E01 lec14p15.
- **Layout / time:** slide, grid-2; 75s.
- **Acceptance:** no empirical “capability vs safety” curves or implication that checks certify zero risk.

### S15 — 02 — When Useful AI Goes Wrong
- **Point / must:** move from abstract stakes to concrete examples.
- **Exhibit / prefer [judgment]:** numbered divider.
- **Placement:** main section name; notes introduce a few failure types, not all course topics.
- **Evidence:** E01.
- **Layout / time:** section-slide; 15s.
- **Acceptance:** matches Contents.

### S16 — The Citation Looked Real
- **Point / must:** fluent, professional-looking output can contain invented evidence; humans still need to verify consequential claims.
- **Exhibit / prefer [judgment]:** one fabricated citation card clearly marked as a schematic of the Mata case, moving into a filing then failing a source check. Do not invent a quote and label it court evidence.
- **Placement:** main Mata v. Avianca, 2023, nonexistent citations and sanctions; notes source the judicial opinion and distinguish misconduct after warnings from mere use of a tool. No sanction amount needed.
- **Evidence:** E07; E01 lec06p6.
- **Layout / time:** slide, card; 85s.
- **Acceptance:** judicial outcome attributed to a particular case, not a universal ban; case-specific facts agree with the opinion.

### S17 — The Chatbot Promised a Refund
- **Point / must:** an automated customer answer can become a consequential promise even when it conflicts with the company's actual policy.
- **Exhibit / prefer [judgment]:** customer query→chatbot's retroactive-fare advice→policy contradiction; schematic, not fake authentic chat footage.
- **Placement:** main Air Canada, 2024 decision and wrong bereavement-fare advice; notes the tribunal's finding/responsibility in this case. State that the chatbot's underlying architecture was not established by this source.
- **Evidence:** E08.
- **Layout / time:** slide, diagram-flow; 75s.
- **Acceptance:** not described as a verified GPT/LLM system or a rule for all jurisdictions; no damages detail needed.

### S18 — Answers Need Checkable Sources
- **Point / must:** for consequential answers, ask for evidence that can be checked independently, and allow uncertainty/referral instead of forced certainty.
- **Exhibit / prefer [judgment]:** answer→actual source→verification; a doubtful source routes to a person rather than directly to action.
- **Placement:** main simple evidence/check/referral path; notes that supplying a citation or retrieving a document alone does not establish truth. No RAG architecture lesson.
- **Evidence:** E03,E07,E08; E01 lec06pp50,54,58–61.
- **Layout / time:** slide, diagram-flow; 55s.
- **Acceptance:** no “citations solve hallucination” claim; meaningful distinction between source presence and source checking.

### S19 — Agreeable Is Not Always Helpful
- **Point / must:** pleasing the user can conflict with helping the user make a sound judgment.
- **Exhibit / prefer [judgment]:** April2025 GPT-4o update→over-agreeable behavior→rollback, as reported by OpenAI. A simple product timeline, not a reward-pipeline chart.
- **Placement:** main date/product/rollback plus vendor-report label; notes explain the company's retrospective account and define sycophancy in plain language if using the term. Do not invent a quotation or harmful transcript.
- **Evidence:** E09.
- **Layout / time:** slide, diagram-flow; 75s.
- **Acceptance:** historical vendor self-report, not current diagnosis or independent causal audit.

### S20 — Good Score, Wrong Goal
- **Point / must:** a convenient measured target can fail to represent the result people actually want.
- **Exhibit / prefer [judgment]:** illustrative support workflow showing tickets marked closed while the customer's issue remains unresolved. One comparison, not a business metrics table.
- **Placement:** main “closed tickets” versus “resolved problems”; notes connect the analogy to specification gaming without reinforcement-learning mechanics.
- **Evidence:** E10; illustrative business analogy, not a company case.
- **Layout / time:** slide, grid-2; 65s.
- **Acceptance:** illustration labelled; no invented percentage or claim that the AI intended to deceive.

### S21 — Two Routes for Information
- **Point / must:** information provided during use and information reproduced from training are distinct privacy questions.
- **Exhibit / prefer [judgment]:** a single two-route schematic, separating prompt/document exposure from training→model→output. Do not draw a mandatory arrow from every prompt into training.
- **Placement:** main two labelled paths; notes explain that product configuration, retention and training-use policies matter but no current vendor policy is asserted.
- **Evidence:** E11,E12; E01 lec02pp6–22 and lec01p13.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** neither “all chats train models” nor “private inbox content is necessarily memorized”; distinction survives in alt text and notes.

### S22 — A Model Repeated Personal Information
- **Point / must:** learned models can reproduce identifying training text; public availability is not the same as harmless reproduction.
- **Exhibit / prefer [judgment]:** canonical Carlini et al. Fig1, using the source's redacted identifying information. Candidate asset `courses/trustworthy-ai/figs/gpt2-extraction.png`; inspect completeness against source before reuse.
- **Placement:** main GPT-2, USENIX2021, public-web training data and research extraction; notes explain the redaction/source and scope. Detailed extraction procedure stays out.
- **Evidence:** E11, PDFp2 / printedp2633, Fig1.
- **Layout / time:** slide; 65s.
- **Acceptance:** no additional personal information exposed; source title/key readable; not described as an enterprise-inbox or present-product breach.

### S23 — Deletion Has More Than One Meaning
- **Point / must:** for data actually used in training, deleting its source file does not alone show that learned influence has been removed.
- **Exhibit / prefer [judgment]:** source record→trained model, then file removed while the model is a separate object requiring a separate check. Label the training condition.
- **Placement:** main “if used in training” and file versus learned influence; notes distinguish file/index/log/backup removal, suppression and model unlearning without legal claims or algorithms.
- **Evidence:** E12.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** no implication Albert's emails train the model or deletion is impossible; lookup systems and training are not conflated.

### S24 — Cost Was Not the Same as Need
- **Point / must:** accurately predicting a proxy can still allocate help poorly: the studied healthcare system used spending rather than illness as its target.
- **Exhibit / prefer [judgment]:** concept-level cost→score→extra-care path with the actual need separated from cost. A conceptual adaptation is clearer here than requiring the audience to decode the paper's multiaxis plot.
- **Placement:** main studied US healthcare algorithm, Science2019, cost versus health need and unequal consequence; notes explain same-score patients differed in illness burden and avoid assigning a single cause to lower spending.
- **Evidence:** E13; current lec12 S04a/S04b/S54a.
- **Layout / time:** slide, diagram-flow; 85s.
- **Acceptance:** correct target/proxy; not just “biased data” or intentional discrimination; original chart not simplified into fabricated measurements.

### S25 — Average Accuracy Hid Unequal Errors
- **Point / must:** evaluation must look at the people affected, because a single average can hide large group differences.
- **Exhibit / prefer [judgment]:** four bars from one IBM system in Gender Shades Table4: darker-skinned women34.7%, darker-skinned men12.0%, lighter-skinned women7.1%, lighter-skinned men0.3% error. Label units and that lower error is better; no multi-vendor matrix.
- **Placement:** main historical gender-classification audit, not identity recognition; date and task visible. Notes include full PPB1270 setup, paper's binary-label conventions, Fitzpatrick grouping, overall12.1% only if useful, and limits on causal/current-product inference.
- **Evidence:** E14,E20. Citation must say redrawn from Table4, not an original experiment.
- **Layout / time:** slide; 65s.
- **Acceptance:** all bars use one zero baseline and the same scale; values from Table4, not FPR or South Africa Table5; group labels legible and no unsourced average arithmetic. Record chart provenance.

### S26 — A Familiar Face Was Not Proof
- **Point / must:** a convincing representation of a trusted person cannot alone authorize a consequential transaction.
- **Exhibit / prefer [judgment]:** prerecorded fake meeting→messaging/payment instruction→money transferred. Drawn case schematic, not fabricated actual-call footage.
- **Placement:** main Hong Kong company,2024, about HK$200million, prerecorded deepfake meeting; notes source the official report and later messaging, not an interactive live clone claim.
- **Evidence:** E15.
- **Layout / time:** slide, diagram-flow; 85s.
- **Acceptance:** no Arup attribution without newly checked company confirmation; no current recovery status, live interaction or updated currency conversion; recommendation to verify via a separate trusted channel is explicitly advice.

### S27 — Origin Is Not Truth
- **Point / must:** a record of where content came from answers a different question from whether its claims are true.
- **Exhibit / prefer [judgment]:** origin/history record versus an independent claim check, as two questions about the same image/document.
- **Placement:** main origin≠truth in words, not equations; notes explain content credentials in ordinary language and why absent credentials also do not establish fakery. No cryptographic/watermark algorithm.
- **Evidence:** E16.
- **Layout / time:** slide, grid-2; 60s.
- **Acceptance:** no “verified image means true event” or detector-verdict claim; example labelled if invented.

### S28 — Mistakes and Attacks
- **Point / must:** failures can occur without an attacker; deliberate manipulation adds another problem and calls for different checks.
- **Exhibit / prefer [judgment]:** accidental wrong answer versus outsider-directed action, using motifs already established.
- **Placement:** main contrast and bridge to adversarial control; notes that reliability and security controls overlap but are not interchangeable. No exhaustive taxonomy.
- **Evidence:** E03,E18.
- **Layout / time:** slide, grid-2; 50s.
- **Acceptance:** does not relabel hallucination or bias as necessarily malicious, and is not another global recap.

### S29 — 03 — Who Can Steer Your AI?
- **Point / must:** turn from failure outcomes to what an adversary can influence.
- **Exhibit / prefer [judgment]:** numbered divider.
- **Placement:** main section name; note transition to input manipulation.
- **Evidence:** E01.
- **Layout / time:** section-slide; 15s.
- **Acceptance:** matches Contents.

### S30 — A Stop Sign Fooled a Classifier
- **Point / must:** specially constructed physical input changes can fool a tested classifier even when a human still sees a stop sign.
- **Exhibit / prefer [judgment]:** Eykholt et al. Fig1; candidates `courses/trustworthy-ai/figs/eykholt-stopsign.png` or `eykholt-fig1-stopsign.png`, checked against source. Essential prediction/outcome must be visible without technical annotation.
- **Placement:** main CVPR2018 physical experiment and classifier scope; notes lab/drive-by setting, not an autonomous-car crash. No percentage, gradient or construction steps.
- **Evidence:** E17.
- **Layout / time:** slide; 70s.
- **Acceptance:** not “any sticker fools any car”; original figure/cite readable and no implied real victim.

### S31 — Attacks Can Enter Earlier
- **Point / must:** manipulating what a model learns is different from manipulating information it reads while doing a task.
- **Exhibit / prefer [judgment]:** two entry locations along one lifecycle: training material before the model, task material during use. A hidden learned rule may be represented simply; no procedure.
- **Placement:** main “during learning” versus “during use”; notes name poisoning/backdoors and prompt injection only to clarify the distinction. Keep jargon subordinate.
- **Evidence:** E18,E04.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** no implication that retrieved email is automatically training data; no operational attack instructions.

### S32 — Requests Versus Retrieved Instructions
- **Point / must:** asking a model to bypass safeguards and hiding an instruction in material the agent reads have different routes to control.
- **Exhibit / prefer [judgment]:** direct user request path versus third-party document path into the same task. Labels “jailbreak” and “indirect prompt injection” get plain-language context if used.
- **Placement:** main author/source contrast; notes the categories can overlap and not every injection is indirect. No encoded prompts or payload text.
- **Evidence:** E04; E01 lec10pp7–12, lec13pp7–9.
- **Layout / time:** slide, grid-2; 65s.
- **Acceptance:** does not define all prompt injection as indirect or imply injection requires a malicious user of the assistant.

### S33 — A Public Issue Reached Private Repositories
- **Point / must:** outside text combined with broad authorized access can redirect an agent across a privacy boundary.
- **Exhibit / prefer [judgment]:** source-backed researcher-demo path: public issue→agent with broad token→same user's private repos→public pull request. Plain “code repository”/“public change proposal” explanations replace unnecessary MCP jargon.
- **Placement:** main Invariant Labs, May2025, research demonstration; notes demo account, client/model, default tool confirmations versus “Always Allow”, and token reach. No actual leaked personal data reproduced.
- **Evidence:** E06.
- **Layout / time:** slide, diagram-flow; 95s.
- **Acceptance:** not a breach of GitHub infrastructure or unauthorized cross-account access; authority/visibility changes can be followed in one visual.

### S34 — Who Can Change What?
- **Point / must:** the useful security question is who supplies information and what actions that information can influence.
- **Exhibit / prefer [judgment]:** the same fictional email from S06, annotated only with outside sender, content read and possible manual/code action. Preserve identities from the opening.
- **Placement:** main three plain-language questions with concrete answers; notes explain the scenario's limits rather than a formal attacker taxonomy.
- **Evidence:** E02–E04; E01 lec01p38.
- **Layout / time:** slide, diagram-flow; 65s.
- **Acceptance:** no abstract white-box/black-box grid; the audience can identify the boundary being crossed.

### S35 — Handoffs Do Not Sanitize Text
- **Point / must:** a malicious instruction can survive a summary or another agent's message; adding an agent does not automatically make text trustworthy.
- **Exhibit / prefer [judgment]:** outside text→summary→coding agent, preserving the same untrusted-content marker. Clearly hypothetical application of the research lesson.
- **Placement:** main possible propagation and “not automatically trusted”; notes the cited work used constructed multi-agent applications/simulations, not an attack on Albert.
- **Evidence:** E05; E04 for the limitation of model separation.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** no universal propagation claim and no suggestion that his separation is useless; show why approval/permissions still matter.

### S36 — Approve the Actual Change
- **Point / must:** an informed approval should identify the source, proposed change and destination, not merely endorse a reassuring summary.
- **Exhibit / prefer [judgment]:** one illustrative review card showing source record, actual proposed manual change and target private page/repository. No executable code or fake authentic UI.
- **Placement:** main “recommended check”, not “my existing setup”; notes distinguish Albert's stated summary approval from optional downstream diff/operation checks, fatigue and the possibility of human error.
- **Evidence:** E03,E04,E06; editorial recommendation.
- **Layout / time:** slide, card; 60s.
- **Acceptance:** source/change/destination concrete, nontechnical and readable; no claim approval guarantees safety.

### S37 — Enforce the Permission Boundary
- **Point / must:** constrain which actions can run and where they can reach, rather than relying solely on the model to reject bad instructions.
- **Exhibit / prefer [judgment]:** proposed action→permission gate→allowed destination; forbidden route stops before the action, not merely highlighted in text.
- **Placement:** main scoped action/destination; notes ordinary access controls and checks outside the model, with allowed-tool misuse and incorrect policies acknowledged. No CaMeL architecture.
- **Evidence:** E03,E04,E06.
- **Layout / time:** slide, diagram-flow; 50s.
- **Acceptance:** gate is an enforced restriction, not a classifier labelled “guarantee”; confidential read access and external reach are not conflated.

### S38 — 04 — What Leaders Should Ask
- **Point / must:** turn the examples into practical delegation decisions.
- **Exhibit / prefer [judgment]:** numbered divider.
- **Placement:** main section name; notes one brief transition.
- **Evidence:** E01,E03.
- **Layout / time:** section-slide; 10s.
- **Acceptance:** matches Contents; no additional summary.

### S39 — Delegate a Bounded Job
- **Point / must:** specify the task and the information/authority it actually needs before expanding access.
- **Exhibit / prefer [judgment]:** a concrete proposed business task inside a boundary, with permitted inputs/actions and one excluded consequential action. Reuse the manual task if that is clearer than adding a new scenario.
- **Placement:** main task scope; notes contrast drafting a proposed update with sending/publishing it automatically, as a recommendation.
- **Evidence:** E03,E04; E02 if manual reused.
- **Layout / time:** slide, card; 55s.
- **Acceptance:** boundedness is concrete, not “use AI responsibly”; no new invented actual workflow.

### S40 — Test the Actual Workflow
- **Point / must:** evidence for deployment should match the work, people and environment where the system will be used.
- **Exhibit / prefer [judgment]:** intended task passing through ordinary, mistaken and manipulated input examples before limited release.
- **Placement:** main task-specific checks; notes that an impressive general benchmark is relevant but insufficient for this deployment. No fictional success rates.
- **Evidence:** E03; E01 lec14pp15,45.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** the test cases connect to the earlier risks; no claim passing finite tests proves safety.

### S41 — Detect, Stop, Recover
- **Point / must:** operational controls should make problems discoverable and limit consequences when they occur.
- **Exhibit / prefer [judgment]:** visible change record→human review→stop/recovery path. Treat prevention before irreversible actions separately from rollback of editable pages.
- **Placement:** main logs, stop and recovery labels; notes recommendations for monitoring and recovery, and that leaked secrets or sent money may not be reversible.
- **Evidence:** E03 and E15 as a consequence example; editorial synthesis.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** no generic “undo everything” promise; value of logging is not confused with prevention.

### S42 — A Safety Score Needs Context
- **Point / must:** a number cannot be interpreted without knowing the tested task, attack, access and conditions.
- **Exhibit / prefer [judgment]:** a plainly illustrative vendor score card with no fabricated real number, surrounded by the missing context fields. Prefer a question-mark placeholder as a concept, not an unfinished factual claim.
- **Placement:** main task / threat / permissions / test setting; notes why current configuration, model and changes require re-evaluation. No equations or metrics tutorial.
- **Evidence:** E03; E01 lec10pp12–13,59–67 and lec14p45.
- **Layout / time:** slide, card; 50s.
- **Acceptance:** no invented statistic attributed to a vendor; demonstrates how to interrogate evidence rather than dismiss all measurements.

### S43 — Name the Human Owner
- **Point / must:** somebody must own authorization, monitoring and response; fluent output is not organizational accountability.
- **Exhibit / prefer [judgment]:** the work item with clearly named human roles, not a committee/organization-chart lecture.
- **Placement:** main owner and response responsibility; notes distinguish this management recommendation from jurisdiction-specific legal liability.
- **Evidence:** E03,E08.
- **Layout / time:** slide, diagram-flow; 50s.
- **Acceptance:** asks who will act when the system fails, not just who bought it; no global legal conclusion.

### S44 — Back to My Weekly Manual
- **Point / must:** the opening use case remains useful with explicit separation, review and bounded authority; this is practical adoption, not abandonment.
- **Exhibit / prefer [judgment]:** the S08 workflow reused consistently, with a small clearly differentiated recommendation layer for checks not supplied by Albert. Avoid adding numerous boxes.
- **Placement:** main stated workflow plus concise optional check; notes draw the line between his actual account and proposed safeguards, including summary contamination and approval limits.
- **Evidence:** E02–E06.
- **Layout / time:** slide, diagram-flow; 60s.
- **Acceptance:** no changes to first-person facts; benefits not invented; no “injection-proof” conclusion.

### S45 — Five Questions Before Delegating
- **Point / must:** close with one reusable decision aid rather than another list of AI dangers.
- **Exhibit / prefer [judgment]:** a single visual decision card: What job? What information? What authority? What checks/evidence? Who owns the outcome?
- **Placement:** main five short questions; notes tie each to one already-seen example, with no new case or sixth checklist.
- **Evidence:** E03; E01 lec01p45, lec14p50.
- **Layout / time:** slide, card; 60s.
- **Acceptance:** the deck's only global closing summary; all questions actionable and not a certificate of safety.

### S46 — Thank You
- **Point / must:** a clean end and invitation to discussion within available time.
- **Exhibit / prefer [judgment]:** simple closer, no repeated summary.
- **Placement:** main thanks and speaker name if useful; notes stop cue only, no new lecture content.
- **Evidence:** no new factual claim.
- **Layout / time:** end-slide; 15s.
- **Acceptance:** no unconfirmed contact details, new risks or repeated checklist.

## 6. Packages and shared surfaces

All packages work only in the target main/notes and target local assets. The package's note ownership is precisely its assigned slide IDs; no package edits another's note articles. Ranges are contiguous for integration, not a requirement to spawn subagents. slides determines its execution strategy.

| Package | Range / owned content | Allowed files and note sections | Dependencies |
|---|---|---|---|
| P1 | S01–S10; content S02–S09; structural S01/S10 reserved to integration | Main/notes within this range; local opening/manual assets | E02 personal facts, E04–E06 risk distinction; defines reusable role vocabulary and motif |
| P2 | S11–S28; structural S11/S15 reserved to integration | Main/notes in range; local case/figure/chart assets and generator only if required | P1 audience/vocabulary; E07–E20 precise qualifications; E01 current-course source map |
| P3 | S29–S37; structural S29 reserved to integration | Main/notes in range; local attack-boundary assets | P1 same fictional email and workflow, P2 privacy/answer distinctions; E04–E06,E17–E18 |
| P4 | S38–S46; structural S38/S46 and closing card S45 finalized by integration | Main/notes in range; local executive-workflow assets | P1 workflow and P3 boundary meanings; no new empirical case |

**Integration owned by slides:** title/Contents/dividers/closer, one global summary, repeated role names and motifs, cross-slide consistency, source citations, paired IDs and page counts, leaf and root outlines. Add the new leaf outline stub before authoring. Do not edit the source course outline merely because a talk borrows its content. No shared `reference/` changes or new generic engine component needed.

**Asset/provenance:** copy verified source figures into the talk's local assets if needed by its build/export conventions. Preserve original meaning and redact only as already done in source. For any data-driven custom figure, include reproducible inputs and a repo-local generator or exact inline rendering location. Identify those paths in the work report; slides-review appends the evidence record before approval. Existing `gpt2-extraction.png` may have a clipped source panel, so do not reuse blindly. All important labels must survive a projected-size visual check.

## 7. Handoff, logging and acceptance

1. Read `job.md`, `requests.md`, `evidence.md`, this plan and canonical design rules. plan-v1 remains frozen historical approval context; this plan is the work order.
2. Create the exact job branch from the fixed baseline. Assign persistent paired slide/note IDs. For the new deck, create content first if necessary, then an **attribute-only ID commit**, with no other changes in that commit; report its SHA and the named review head.
3. Copy the completed planner files unchanged into tracked `log/<job-id>/`: job.md, requests.md, evidence.md, plan-v1.md, plan-v2.md. Refresh living files on every push. Never edit the working folder; never rewrite a frozen planner file. Report any plan/source defect rather than silently filling factual gaps.
4. Deliver `work-r1.md` with branch/head/ID-commit, per-package work, final slide-ID→page map, scope/time/layout deviations and reasons, source issues, actual section timing, chart inputs/provenance, and checks run. The report must distinguish unpublished claims from verified material.
5. Run normal repo lint/outline checks and inspect **every main slide visually** for this first new-deck pass, including citations/figure labels and long English titles. Check paired notes at desktop and narrow view for horizontal overflow, missing sources and ID/order/count alignment. No live external dependencies for essential understanding; no placeholders or missing visuals at handoff.
6. Send only the one-line contract pointer and exact commit SHA to slides-review. No interim Slack reports or PDF delivery to Albert. slides-review sets in-review, reviews Albert's request then sources then design then plan, and makes at most three rounds. Only blocking findings trigger another round.
7. After review approval, final log-only pushes may touch only this job's tracked log. slides-review independently checks that restriction and opens the PR against main. **No merge unless Albert directly orders that PR's merge.**

**Final acceptance:** English main/note pair in the exact folder; personal manual story first and accurate; lec01-led high-level arc; current-semester distinctions; real cases correctly labelled; readable image/diagram-driven slides; no technical explanation creep; 45-minute fit; approved scope covered C01–C19; all notes/sources/outlines consistent. Slides may split or improve the explanation, but argument/fact/scope/time changes return for a revised plan.
