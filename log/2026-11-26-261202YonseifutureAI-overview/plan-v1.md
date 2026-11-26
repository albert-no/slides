# Plan v1 — stages 1–3 for Albert's approval

**Job:** 2026-11-26-261202YonseifutureAI-overview  
**Baseline:** 467cf0630d25ec9929c9e1e87cea901224637487  
**State:** awaiting-albert. **Not a work order.** No deck implementation before Albert approves stages 1–3. After approval, a new plan version will provide complete slide-level specs and executable packages (stage 4). This version is a complete scope/evidence/argument proposal, not an incomplete build specification.

## 1. Summary and stage 1: audience, purpose and boundaries

New standalone visual talk for CEO-level senior general audiences, not ML students. Forty-five minutes; target **46 pages**, within Albert's 40–50 target, counting title/Contents/dividers/closer. Target 43 minutes of narration plus two minutes pacing reserve. No assumed technical prerequisites, equations, code or algorithm explanation. Concepts are introduced only as needed by the examples.

**Working title:** *AI에게 어디까지 맡길 것인가* / *Trustworthy AI: What Should We Delegate?*  
**Language proposed for approval:** Korean main slides and notes, with familiar English names where useful. The English titles below state the argument for review; they are not a demand for translated, sentence-heavy final slide titles.

**Deliverables, produced only by slides:**
- `talks/261202YonseifutureAI/261202YonseifutureAI.html`
- `talks/261202YonseifutureAI/261202YonseifutureAI-note.html`
- Local assets as needed, target leaf `OUTLINE.md`, and the relevant root outline entry.
- One paired note article per slide, stable IDs, easy speaker-led explanation of each exhibit and precise sources. Accessible notes, not a hidden technical lecture. No tech supplement requested.
- No automatic PDF/PPTX/standalone export delivery. No modification of the source course decks or global design assets. No real email/manual access needed.

**Objectives:** the audience can (1) distinguish usefulness from trustworthiness, (2) recognize several concrete ways useful AI can fail or be manipulated, and (3) decide what to delegate, with what information, permissions, checks and accountable owner.

**Main argument:** AI can usefully remove recurring work. As its reach extends from answering to acting, trusting it means more than trusting a fluent answer: the task, evidence, authority and checks must fit the consequences. The opening private-manual story provides a concrete reference point; the ending returns to the same workflow with better questions, not a warning to stop using AI.

**Source hierarchy:** lec01 supplies the arc and most case families. lec02–14 update the choice and precision of examples. This is not one compressed section per lecture. `evidence.md` E01 has a complete surveyed-lecture/reuse/omit ledger; E02–E19 provide claims, primary locators, evidence types and limits. Survey cutoff November26,2026 (KST); no exhaustive frontier survey.

**Must omit:** model/training mechanics; mathematical definitions; probability/attack-score plots requiring a lesson; fairness-rate algebra; watermark algorithms; lengthy threat taxonomy; technical benchmark comparison; detailed regulation/court developments; simulated catastrophes presented as incidents; activities; live attack or mailbox demo. Legal cases are historical examples, not legal advice or compliance rules.

## 2. Stage 2: evidence map and case choices

| Audience question | Core source | Updated material | Public example / evidence |
|---|---|---|---|
| Why use agents at all? | Albert C11–C16 | The personal workflow anchors the talk, not an invented productivity claim | Weekly private manual, author testimony E02 |
| Why does trust become more consequential? | lec01 pp4–6,35–40 | lec14 autonomy/authority and evaluation limits | Conceptual reply→tools→actions progression, E03 |
| Can a polished answer be wrong? | lec01 pp14,16–17 | lec06/07 current examples and qualifications | Mata (E07), Air Canada (E08), GPT-4o rollback (E09) |
| What happens to information? | lec01 pp11–13 | lec02–05 distinctions | GPT-2 extraction (E11); removal vs learned influence (E12) |
| Who bears errors? | lec01 fairness cases | Updated lec12 cost/need explanation and exact audit task | Healthcare cost proxy (E13), Gender Shades (E14) |
| Can appearances or origins prove truth? | lec01 p28 | lec11 distinction among detection/origin/truth | Hong Kong payment fraud (E15), provenance limits (E16) |
| Who can steer the system? | lec01 pp18–21,38–40 | lec08–10 entry points; lec13 revised actor/permission mapping | Stop-sign experiment (E17), GitHub research demo (E06) |
| What does agent separation accomplish? | Albert C16 | lec13 authority boundary + lec14 handoffs | E04–E06; benefit without a safety guarantee |
| What should a leader ask? | lec01 p45 | lec14 p50 and bounded evaluation | Task/authority/evidence/check/owner synthesis (E03) |

**Public-case presentation rule:** one scene, one consequence, one point. Dates and the short qualifier remain visible; causal detail and source/context go to the note. Distinguish actual incident, vendor report and research demonstration. For example, the physical stop-sign and GitHub demonstrations are not crash or breach victim reports. Neither Air Canada's underlying model nor the January fraud company's name is inferred from a familiar headline.

**Visual strategy [judgment]:** mostly large, simple workflow/picture diagrams, occasional decisive real-source figure or case artifact. No dense academic plots, screenshot walls, or quote panels. Use a source's clear canonical picture when it serves this audience; otherwise an original schematic must be labelled as such and must not impersonate actual evidence. Every content page has one exhibit and only the minimum framing text/labels. Do not add an explanatory paragraph to compensate for a weak diagram.

## 3. Stage 3: argument, title sequence and time budget

### Sequence and section allocations

| Range | Pages | Target time | Purpose |
|---|---:|---:|---|
| S01–S10 | 10 | 8 min | Title → Albert's real workflow → first prompt-injection intuition → separated agents → short roadmap |
| S11–S14 | 4 | 4 min | 01 — More Capable, More Consequential |
| S15–S28 | 14 | 15 min | 02 — When Useful AI Goes Wrong |
| S29–S37 | 9 | 9 min | 03 — Who Can Steer Your AI? |
| S38–S46 | 9 | 7 min | 04 — What Leaders Should Ask |
| Pacing reserve | — | 2 min | Transitions, short clarification; not a separate promised Q&A block |
| **Total** | **46** | **45 min** | |

The story opens immediately after the title, before Contents: an explicit exception to the generic title→Contents order to satisfy C11. Contents then names the four numbered sections exactly. No course map or speaker biography detour. A divider consumes seconds, not a whole minute. Counts/layouts remain targets; design-system readability wins. If fit would push materially beyond 50 pages or 45 minutes, bring a scope/time decision back rather than shrink type or extend silently.

### Proposed title/point and exhibit sequence

These are proposed new IDs; there is no old-page mapping because the target deck is new. The source pages in the evidence ledger are the baseline trail. “Concept” means editorial framing or a labelled illustration, not new empirical data. All content/style choices below are **[judgment]**; the author requirements and evidence qualifications are **must**.

| ID | Proposed title / communicative point | Exhibit first | Evidence |
|---|---|---|---|
| S01 | Trustworthy AI: What Should We Delegate? | Spare title with private-manual/workflow motif; speaker name, no invented event branding | E02; C01–C04 |
| S02 | Every Semester, the Same Paperwork | Semester calendar repeating an administrative task; Albert's Vice-Dean role named | E02 |
| S03 | Last Time's Email Becomes This Time's Manual | Email trail → a private reference page; schematic, not a real screenshot | E02 |
| S04 | A Manual That Updates Weekly | Weekly source→draft→update loop, pending human review visibly distinguished | E02 |
| S05 | An Agent Can Read—and Act | Mail-reading role and code-writing role shown as capabilities, not an engineering diagram | E02,E03 |
| S06 | What If the Email Gives an Order? | Benign-looking fictional email containing a clearly illustrative instruction to alter the manual | E04; C15 |
| S07 | Read Permission Is Not Write Authority | One broad-access agent: outside text has a route toward repository changes; possible risk, not certain compromise | E04,E06 |
| S08 | I Separate Reading, Approval and Coding | Albert's actual stated sequence: mail read-only agent → summary → Albert approves → coding agent → private manual | E02 |
| S09 | The Question Is What We Let AI Do | Same useful workflow, with a visible authority boundary; no “now safe” badge | E03–E05 |
| S10 | Four Questions for Today | Four-section roadmap, short and visual | E01,E03 |
| S11 | 01 — More Capable, More Consequential | Section divider | E01 |
| S12 | From Answers to Actions | Chat reply → tool-assisted task → changes in the world; qualitative progression, no growth-rate graph | E03 |
| S13 | The Same Error, Different Consequences | Draft for oneself versus customer promise versus consequential action; hypothetical comparison | E03,E08 |
| S14 | Intelligence Is Not a Safety Certificate | Capability and delegation checks are separate gates; no suggestion that capabilities lack value | E03 |
| S15 | 02 — When Useful AI Goes Wrong | Section divider | E01 |
| S16 | The Citation Looked Real | Mata: a fabricated authority enters a professional filing; a labelled case schematic, not fabricated court evidence | E07 |
| S17 | The Chatbot Promised a Refund | Customer→chatbot advice→policy mismatch; 2024 Air Canada decision dated | E08 |
| S18 | Important Answers Need Checkable Sources | Answer→underlying source→independent check; route uncertain cases to a person or abstention | E03,E07,E08; lec06 |
| S19 | Agreeable Is Not Always Helpful | GPT-4o update→over-agreeable behavior→rollback; vendor self-report, 2025 | E09 |
| S20 | A Good Score Can Miss the Goal | Illustrative customer-support shortcut: closed tickets versus solved problems; no invented actual company | E10 |
| S21 | Information Has More Than One Exit | What we supply to a service versus what a trained model can reproduce; keep the two routes distinct | E11,E12; lec02 |
| S22 | A Model Repeated Personal Information | GPT-2's already-redacted Fig1 or faithful source-based case view; public-web training data, research result | E11 |
| S23 | Delete the File, Not Necessarily the Learning | Training record removed; learned influence is a separate question; no claim Albert's emails are used for training | E12 |
| S24 | Cost Was Not the Same as Need | Healthcare spending→risk score→care allocation; same score hid different need, within the studied setting | E13 |
| S25 | One Average Can Hide Unequal Errors | Gender Shades subgroup comparison, correctly labelled as historical gender classification, not face identity recognition | E14 |
| S26 | A Familiar Face Was Not Proof | Hong Kong, 2024: prerecorded fake meeting→payment instruction→about HK$200m loss; schematic | E15 |
| S27 | Origin Is Not Truth | Record of origin/history beside checking the claim; no “unmarked means fake” shortcut | E16 |
| S28 | Mistakes and Attacks Need Different Checks | Unintentional wrong answer versus deliberate manipulation; bridges examples to adversaries | E03,E18 |
| S29 | 03 — Who Can Steer Your AI? | Section divider | E01 |
| S30 | A Stop Sign Fooled a Classifier | Canonical physical-adversarial source image; experiment, not a crashed autonomous car | E17 |
| S31 | The Bad Instruction Can Arrive Earlier | Training-time manipulation versus content read during a task; short two-path conceptual visual | E18 |
| S32 | A Request Is Not a Document's Instruction | Direct request to bypass safeguards versus hidden instruction in material the agent reads; concept only | E04; lec10/13 |
| S33 | A Public Issue Reached Private Repositories | GitHub demo: public issue→broad agent token→private information→public PR; “research demonstration, 2025” visible | E06 |
| S34 | Who Can Change What? | Return to Albert's fictional email: outside sender / readable content / reachable action; three actors, plain language | E02,E03,E04 |
| S35 | Another Agent Does Not Clean the Message | Outside text→summary→coder; a dangerous instruction can survive the handoff, not proof it always does | E05 |
| S36 | Approval Must Name What Will Change | Clearly marked recommended gate: source, proposed manual/code change, affected destination; distinguish from his stated summary approval | E03,E04,E06 |
| S37 | Enforce the Boundary, Not Just the Prompt | Task-scoped permissions plus checks at the action boundary; no technical architecture or universal guarantee | E03,E04,E06 |
| S38 | 04 — What Leaders Should Ask | Section divider | E01 |
| S39 | Delegate a Bounded Job | Concrete task with explicit information/authority scope; not “give the assistant everything” | E03 |
| S40 | Test the Work You Will Actually Delegate | Intended business task→normal/error/adversarial tests; not an abstract model ranking | E03; lec14 |
| S41 | Make Failures Visible and Reversible | Logs→review→stop/rollback loop; present as recommendation, not a guarantee every action is reversible | E03 |
| S42 | A Safety Number Needs Its Setting | A vendor number surrounded by task, adversary, permissions and test conditions; no invented real statistic | E03; lec10/14 |
| S43 | Keep a Named Human Owner | Roles around the workflow: who authorizes, monitors, responds; responsibility is not delegated to a fluent answer | E03,E08 |
| S44 | Back to My Weekly Manual | Same opening workflow; mark which safeguards Albert stated and which are recommendations; preserve usefulness | E02–E06 |
| S45 | Five Questions Before You Delegate | Single closing decision card: task, information, authority, evidence/checks, accountable owner | E03; lec01 p45, lec14 p50 |
| S46 | Thank You | Simple closer / discussion invitation, not another recap | No new claim |

## 4. Request coverage

| Comment | Baseline page/title | Proposed IDs / deliverable | Future package |
|---|---|---|---|
| C01 | New target; lec01 overview | Whole argument, S12–S45 | All |
| C02 | Target absent at B | Exact folder `talks/261202YonseifutureAI/` | Integration |
| C03 | New target | Main + paired note HTML | All + integration |
| C04 | lec01 46-page overview is reuse source, not copy target | 46 target pages, 43+2 minutes; all fourteen decks surveyed | All |
| C05 | lec01 pp4–40,44–45 | Main spine S11–S45; no technical details | P2–P4 |
| C06 | Current lec02–14 (E01 ledger) | Updated examples and distinctions S16–S45; omission decisions explicit | P2–P4 |
| C07 | New audience | All main content nontechnical; accessible notes | All |
| C08 | New audience | Consequences and decisions; S13,S17,S20,S24,S39–S45 | All |
| C09 | New mode | One dominant visual per page; minimal text | All |
| C10 | lec01 case-rich spine plus updated lec07/12/13 | S16–S17,S19,S22,S24–S26,S30,S33 | P2–P3 |
| C11 | No previous target | Story begins S02, before Contents | P1 |
| C12 | Author testimony | S03,S08,S44 | P1,P4 |
| C13 | Author testimony | S02–S03, paired notes | P1 |
| C14 | Author testimony | S03–S04,S08,S44 | P1,P4 |
| C15 | Author testimony; lec13 pp4–6,27–28 | S05–S07; short definition at S06 | P1 |
| C16 | Author testimony | S08,S44; read-only mail role and manual approval explicit | P1,P4 |
| C17 | lec01 capability/trust + lec13 later deepening | S09,S11–S14 then S29–S37 | P1–P3 |

## 5. Stage 4 work organization (proposal, not authorization)

- P1: S01–S10, opening story and aligned notes. Needs E02 author wording; supplies the workflow motif for P3/P4.
- P2: S11–S28, overview and real cases, aligned notes and local case assets. Uses current lec01 framing with qualified later-lecture evidence.
- P3: S29–S37, attacks/authority return and aligned notes. Reuses P1's workflow and the scoped GitHub case. No payload generation.
- P4: S38–S46, executive actions and aligned notes. Return must distinguish known workflow from recommendations.
- Shared surfaces, owned by slides integration: title/Contents/numbered dividers/one closing summary, repeated workflow consistency, paired IDs, all page counts, local/root outlines and source/asset links.
- Packages are ownership boundaries, not an instruction to create parallel subagents. slides chooses its implementation workflow.
- A complete approved-scope plan-v2 will specify per-slide must/prefer/discretion, exhibit reading, note content, acceptance checks, timing and exact package file boundaries. No package is executable from this gate proposal alone.

## 6. Acceptance priorities for the eventual build

1. Albert's workflow appears first and faithfully, with no fabricated private evidence or productivity metrics.
2. Prompt injection is immediately understandable as outsiders' words acquiring authority; later slides explain boundaries rather than attack techniques.
3. The visual alone plus the title carries the point. Notes teach the picture without turning into a graduate-course appendix.
4. Every named case retains date, evidence type and material scope; source tracing is possible. No speculative deployment claims or unsourced statistics.
5. Agent separation and human approval are risk reductions, not an immunity claim. No recommendation is passed off as already implemented by Albert.
6. Readability is checked on renders, not inferred from lint; final review at the exact named commit includes main/note alignment and design-system compliance.

## Approval requested

Approve or revise the **scope, case/evidence map, 46-page title arc and 8+4+15+9+7+2 minute budget** (stages1–3). Confirm the proposed **Korean** slide/note language, or request English. The event date can remain off the title until confirmed; the requested directory spelling is fixed. Once approved, slides-review completes stage4 and sends slides a work order.
