# lec13: make the authority boundary concrete

## 1. Summary and contract

- **Job:** 2026-11-20-lec13-clarity; medium; round limit 2.
- **Baseline:** `9effc8ab67589f2d7e5789f04db5e92067ff46d9`; all Albert page numbers refer to this commit. Existing stable IDs are S01–S53. Never renumber them.
- **Main:** `courses/trustworthy-ai/lec13-prompt-injection.html`.
- **Notes:** `courses/trustworthy-ai/lec13-prompt-injection-note.html`.
- **Supplement:** `courses/trustworthy-ai/lec13tech.html` (consistency edits only, not a new technical lecture).
- **Audience:** existing mixed-major undergraduates; concept-first; 90 minutes; no activities or live attack demonstrations.
- **Argument stays:** agents read text from many authors → an input must not acquire authority merely by being read → real incidents expose the distinction → measured resistance helps but permissions/data-flow policy must be enforced outside model obedience.
- **Changes:** concrete email opening; explicit answers to conceptual questions; documented white-text review manipulation and ICML organizer probe; incident walkthroughs; larger, simpler diagrams; defense mechanisms before results; three-step system-defense comparison; actionable approval view.
- **No new literature survey:** the evidence register checks existing anchors and the specifically requested conference example. Do not add a defense catalogue or recent-product survey.

### Interpretation and design decisions

1. **[judgment] Must:** C01–C02 replace the abstract/BANANA opening, rather than adding another example before a still-redundant BANANA slide. Start substantive content with agents in mail, browsers and coding workflows, reading many authors. No unsupported adoption statistic.
2. **[judgment] Must:** every question receives a short answer on its slide, then a teachable explanation in the corresponding note. More detail is not permission to shrink type: split into explanatory steps.
3. **[judgment] Must:** same-user repositories is **yes in the published demo**; general vulnerability follows access permissions, not account ownership. “Vendor” means product/service provider, not independent researcher. Explicitly distinguish provider statements from third-party evidence.
4. **[judgment] Must:** priority = whose conflicting instruction should win; ranking is an authority ordering, not search-result relevance or a numeric safety score. Read/use text is not obey every command inside it.
5. **[judgment] Must:** direct injection may come from a user trying to override application rules; an ordinary user changing a permitted task is not an attack. In the email scenario, a third party's message is indirect.
6. **[judgment] Must:** “ask only important things” becomes a policy: routine authorized actions may proceed, prohibited actions are denied, consequential unresolved exceptions get specific approval. Never auto-allow a risky action merely to reduce prompts.
7. **Must:** current DESIGN_SYSTEM §§1,2,4,5,6,8,9,10 govern. The exemplar's rhythm is useful, not its legacy small labels. Existing source examples are not design-rule exemptions.
8. **Slides decides:** layouts, crops, splitting beyond targets and final slide count. Report mappings and reasons. Changes to facts, argument, required content or total teaching time come back as plan issues.

### Continuity and pacing

- Reuse the already-established jailbreak/safety concept from lec10 only as a brief self-contained contrast at S06; do not re-teach jailbreak attack families.
- Adapt threat-model vocabulary from the security lectures into this deck's read/write/authority scenario. No cross-deck pointers on main slides.
- Keep broader autonomous-agent risks deferred to lec14. Keep formal security games, capability semantics and metric formulas in existing tech material, not on the main slides.
- Suggested section budgets: Core Idea 14 min; Agentic Surface 15; Incidents 17; Why Hard 11; Defenses/Measurement 27; Synthesis 6. Total 90. These redistribute the existing time, not expand the lesson. Individual times below are targets; executor reconciles notes and reports exact totals.
- The new opening and later loop must not repeat the same motivation. S11 now deepens delegated permissions; S13 reuses the opening example to explain a tool trace.

## 2. Coverage table

| Comment | Baseline page / title | Stable IDs / target treatment | Package |
|---|---|---|---|
| C00 | Whole deck + notes | All main IDs; paired notes, scoped tech/outline consistency; review then PR | All |
| C01 | 4 One Context, Many Authors; 11 From Chatbot to Agent | S04 agent-first; S11 avoid repetition | P1, P2 |
| C02 | 5 A Tiny Example; 13 One Injection, End to End | S05a/b concrete email; S13 reuses trace | P1, P2 |
| C03 | 7 Direct and Indirect Injection | S07a/b two entry channels | P1 |
| C04 | 8 Priority Is Not a Boundary | S08 a real conflict and why priority exists | P1 |
| C05 | 9 Where Injected Text Hides | S09a/b authors' white text and ICML 2026 probe | P1 |
| C06 | 16 Which Input May Shape Which Action? | S16 named allowable/forbidden influence | P2 |
| C07 | 20 How to Read an Incident Report | S20 interpret categories; define provider | P3 |
| C08 | 22 EchoLeak: The Path | S22 larger readable path | P3 |
| C09 | 21 EchoLeak: Microsoft 365 Copilot | S21a/b mechanism then evidence | P3 |
| C10 | 23 GitHub MCP: Public Issue, Private Repo | S23 same user's two repositories | P3 |
| C11 | 24 GitHub MCP: The Token Is the Boundary | S24 readable permission flow | P3 |
| C12 | 26 Comet: A Fix, Retested | S26 readable dated chronology | P3 |
| C13 | 29 Priority Is Learned, Not Enforced | S29 authority ordering, readable conflict diagram | P4 |
| C14 | 31 Escaping Alone Is Not Authority | S31a/b escaping vs delimiting vs enforcement | P4 |
| C15 | 40 Simple Defenses on AgentDojo | S54 before S40: repeat prompt/sandwiching; S40a/b results | P5 |
| C16 | 40–41 tables | S54 before S40; S55/S56 after S40 and before S41 | P5 |
| C17 | 44 CaMeL: Every Value Carries Its Origin | S44a/b labeled values and decision walkthrough | P6 |
| C18 | 47 Other System Defenses, Compared | S47a/b/c (three slides target) | P6 |
| C19 | 48 Meaningful Approval | S48 explicit allow/deny/ask distinction, concrete approval | P6 |

New IDs: **S54** after S39 and before S40; **S55** after S40 and before S41; **S56** after S55 and before S41. If the main deck and tech share an ID namespace in existing practice, report any collision before assigning. Lettered splits retire the unsuffixed displayed slide but preserve the baseline mapping. Extra splits use the parent ID with new suffixes; extra unrelated slides take the next free ID and are reported.

## 3. Slide-level specifications

**Common acceptance for every spec:** main point visible, one exhibit, required qualifier retained, no new unsupported fact, title/body/exhibit/alt text/note agree. A note starts with Message, then explains the exhibit, then detail/sources. The main slide carries the answer; the note teaches why. Layout names below are optional DS vocabulary, never prescribed implementation. Every proposed content change below is **[judgment]**; slides should make these choices directly rather than hand context-free wording decisions to an implementation worker.

### P1 — Opening: sources, intent and instruction authority

#### S04 — baseline p4 “One Context, Many Authors”
- **Must point / title:** agents read many authors before acting. Proposed title: **Agents Read Everyone's Text**.
- **Exhibit:** one integrated agent-input map: email, web, documents, repository issues → agent → an action. Distinguish the user's goal from outsider-authored content. Read sources first, then possible action.
- **Required:** “agent” means a system using tools to carry out a goal; brief real-world workflow framing, not market-share claims. Why this motivates injection: someone other than the user can write what the agent reads.
- **Evidence:** E01, E09–E10.
- **Slide / note / tech:** slide gets the motivation; note explains retrieved text, tool output and permissions using an ordinary work task. No formalism.
- **Layout / time:** diagram-flow; ~1 min.
- **Acceptance:** a viewer can explain why many input authors create a new authority problem before hearing an attack definition.

#### S05a — split p5 “A Tiny Example”
- **Must point / title:** legitimate task scope is reading/summarizing, not sending. **The User Asked for a Summary**.
- **Exhibit:** the E02 user's request beside the relevant inbox items in one worked scenario. Give a plausible project email with ordinary subject/body, then reveal that its body also requests an unrelated outbound action. Clearly identify who wrote each instruction.
- **Evidence:** E02 (illustrative, visibly labeled).
- **Slide / note:** main identifies user goal, email author and unrequested action; note supplies the complete benign/injected email contrast and expected behavior. No executable payload/address. Remove BANANA from the taught path.
- **Layout / time:** grid-2 or diagram-flow; ~1.5 min.
- **Acceptance:** user, attacker and agent are distinguishable; the attack is not mistaken for the user's own request.

#### S05b — continuation
- **Must point / title:** correct summary does not excuse unauthorized action. **The Email Added an Unauthorized Send**.
- **Exhibit:** same example, comparing authorized read→summary with the additional confidential-attachment send. One trace with the illicit branch marked; no new scenario.
- **Evidence:** E02.
- **Slide / note:** say this is a possible vulnerable-agent outcome, not a measured run. Note explains that access to a sending tool is ability, not task authorization.
- **Layout / time:** diagram-flow; ~1 min.
- **Acceptance:** the outcome and the crossed boundary are explicit without needing the note.

#### S06 — p6 “Two Attacks, Defined by Goal”
- **Must retain point:** safety restriction bypass vs attacker content gaining authority; overlap possible. Retain the existing two-way contrast as the single exhibit, with a one-line Point.
- **Evidence:** E01, E03; use the deck's explicit goal-based framing rather than claiming all taxonomies agree.
- **Note:** adapt references to the new email example; no broad jailbreak recap. Tech unchanged.
- **Layout / time:** grid-2; ~1 min. **Acceptance:** does not imply only a third party can inject.

#### S07a — split p7 “Direct and Indirect Injection”
- **Must point / title:** a malicious app user can attack the app's higher-level rules. **Direct: The Request Attacks App Rules**.
- **Exhibit:** illustrative constrained translation app: developer sets translation-only behavior; attacker types a request to abandon translation and produce unrelated output; compare expected and hijacked behavior. Use a concrete intelligible target, not BANANA.
- **Evidence:** E01, E03; app example is illustrative.
- **Slide / note:** explicit answer “The attacker can be the user of the app.” Explain why a compliant user changing an allowed task is not injection. No need to steal an email account or system-role access.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** direct injection is understandable without prior indirect examples.

#### S07b — continuation
- **Must point / title:** outsider-authored content arrives through a tool, while the user's request is benign. **Indirect: The Attack Arrives as Data**.
- **Exhibit:** retain/crop Greshake Fig. 3 if legible, with a brief reading key identifying attacker-controlled resource and user's retrieval. Link conceptually to E02 email, not as a claim the figure depicts email.
- **Evidence:** E01, E02.
- **Note:** explain both channels by whose input is controlled; email example is indirect because the attacker writes retrieved email, not the user's request.
- **Layout / time:** figure-first; ~1 min. **Acceptance:** explicitly answers Albert's email intuition and distinguishes the figure's published setting from our illustration.

#### S08 — p8 “Priority Is Not a Boundary”
- **Must point / title:** priority resolves conflicting instructions, not access permissions. **Which Instruction Should Win?**
- **Exhibit:** apply the email example: app restriction, user's “summarize,” email's “send.” Show desired winner and why the email is information, not a new authorization.
- **Evidence:** E03, E02.
- **Slide / note:** answer why priority matters: without a conflict rule, outsider text can replace the task. Note distinguishes an instruction-ordering policy from an external allow/deny gate. Simplified hierarchy is labeled as such.
- **Layout / time:** diagram-flow; ~1.5 min. **Acceptance:** both “whose instruction wins?” and “which action is permitted?” have explicit, different answers.

#### S09a — split p9 “Where Injected Text Hides”
- **Must point / title:** text invisible in a PDF can still influence a reviewing LLM. **Hidden Paper Text Can Steer Reviews**.
- **Exhibit:** conceptual PDF page → extracted text → review, with the hidden instruction's purpose revealed as a legible annotation. This is not an actual named author's submission.
- **Evidence:** E04. Cite ICLR 2026's official acknowledgement; no invented success rate.
- **Slide / note:** author goal is a favorable review. Explain white-on-white appearance versus text extraction. Other hiding channels from old S09 go to note, not disappear.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** invisible text is explained visibly, with no implication every reader exposes hidden text.

#### S09b — continuation
- **Must point / title:** conference organizers reused hidden instructions as an AI-review probe. **ICML Used Hidden Text to Flag AI Reviews**.
- **Exhibit:** organizer's hidden two-phrase instruction → LLM-produced review may include them → matching plus human verification. Use descriptive phrase labels, not fabricated quotes presented as the actual probe.
- **Evidence:** E05; named conference and 2026 date on slide.
- **Slide / note:** explicitly contrast intent: authors manipulate judgment; organizers test compliance. State the no-LLM-policy scope and that absence of markers proves nothing. Note explains manual checking and why quoting/discussing the injection is not automatically misconduct. No enforcement-count digression required.
- **Layout / time:** diagram-flow; ~1.5 min. **Acceptance:** documented organizer use, not speculation; no “perfect AI detector” claim.

### P2 — Agentic surface: authority belongs to actions

#### S11 — p11 “From Chatbot to Agent”
- **Must point / proposed title:** **The Agent Borrows Your Permissions**.
- **Exhibit:** user-delegated read/send authority applied to the E02 example; deeper than the opening's multi-source map. Do not claim chatbots never have tools as an absolute product distinction.
- **Evidence:** E01, E09, E17.
- **Note:** ability to act as the user is not blanket authorization. **Layout/time:** diagram-flow; ~1.5 min. **Acceptance:** adds delegated-authority intuition rather than repeating S04.

#### S12 — p12 “The Agent Loop”
- **Must retain:** read goal/context → choose tool → run → append output, where outsider text re-enters later decisions. Enlarge/simplify if needed under current rules.
- **Exhibit/evidence:** existing loop; E01. **Note:** follow an email read. **Layout/time:** diagram-flow; ~1.5 min. **Acceptance:** output-to-next-action arrow clear, not a magic single-shot model.

#### S13 — p13 “One Injection, End to End”
- **Must point / proposed title:** **One Email Redirects the Next Tool Call**.
- **Exhibit:** a short tool trace of the same E02 task: read mail → injected result → proposed extra send → summary. Emphasize where content becomes an instruction; do not merely repeat S05b's outcome picture.
- **Evidence:** E02.
- **Note:** retain a worked trace with task, tool inputs/outputs, attacker goal and expected authorized path. **Layout/time:** diagram-flow; ~2 min. **Acceptance:** audience can name the exact transition that is wrong.

#### S14 — p14 “The Confused Deputy”
- **Must retain:** trusted helper's permissions can be misused by a third party; concise definition before source figure. **Exhibit:** InjecAgent Fig. 1, figure-first. **Evidence:** E20/E01.
- **Note:** distinguish attacker permissions from agent permissions. **Layout/time:** figure-first; ~2 min. **Acceptance:** readable source roles; no generic “all tools are compromised” claim.

#### S15 — p15 “What an Injection Can Achieve”
- **Must retain:** exfiltration, unauthorized action, manipulated output; only the first necessarily involves data leaving. **Exhibit:** one comparison using concrete outcomes, not three disconnected illustrations. **Evidence:** E01/E02.
- **Note:** explain output-only damage. **Layout/time:** grid-3; ~1.5 min. **Acceptance:** no claim that the exfiltration trifecta defines all injections.

#### S16 — p16 “Which Input May Shape Which Action?”
- **Must point / title:** **Notes May Choose a File, Not a Recipient**.
- **Exhibit:** user's “Send Bob the document from our last meeting” → three named fields: send authorized by user; Bob resolved from trusted request/contact information; document identified by notes but checked for Bob's access. Contrast an added outsider recipient as the denied change.
- **Evidence:** E17; explicitly an illustrative policy adapted to CaMeL's example.
- **Slide / note:** answer: untrusted content can help complete the task without gaining authority to change who receives data. Explain why banning all untrusted influence would prevent useful tasks, and why “file from notes” still needs reader permissions. Omit the old covering-text row from the main slide; its limitations belong in notes.
- **Layout / time:** diagram-flow; ~2 min. **Acceptance:** shows at least one permitted and one forbidden dependency; not “all notes influence is an attack.” Split if necessary.

#### S17 — p17 “The Trifecta: A Heuristic for Exfiltration”
- **Must retain:** private data + untrusted input + outbound channel, heuristic specifically for theft. **Exhibit:** existing three-way convergence, readable. **Evidence:** Willison, 16 June 2025, https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (existing cited definition; no new prevalence claim).
- **Note:** non-exfiltration harms do not require all three. **Layout/time:** diagram-flow; ~1.5 min. **Acceptance:** qualifier stays on slide.

#### S18 — p18 “Ordinary Features as Exit Channels”
- **Must retain:** normal image fetching, public posting and sending can be exits. **Exhibit:** one channel map with explicit outgoing data. **Evidence:** E07,E09,E10.
- **Note:** distinguish model output and client-triggered network action; prepares EchoLeak. **Layout/time:** diagram-flow; ~1.5 min. **Acceptance:** closing an exit is not equivalent to removing injected instructions.

### P3 — Incidents: first understand the event, then its evidence

#### S20 — p20 “How to Read an Incident Report”
- **Must point / title:** **A Demonstration Is Not a Victim Report**.
- **Exhibit:** four clearly labeled evidence questions: was an attack demonstrated; were real victims confirmed; what did the provider say it fixed; who independently tested again? This is a taxonomy, not a timeline or mandatory sequence.
- **Evidence:** E06.
- **Slide / note:** explicitly “Provider (vendor) = company operating the affected product.” Microsoft and Perplexity examples; do not label Brave the vendor of Comet. Note explains the original researcher can perform an independent-of-provider retest and “none reported” differs from disproven.
- **Layout / time:** compact comparison; ~1.5 min. **Acceptance:** reader understands the incident badges and unknowns; use words rather than unexplained × symbols.

#### S21a — split p21 “EchoLeak: Microsoft 365 Copilot”
- **Must point / title:** **An Email Made Copilot Leak Context Data**.
- **Exhibit:** sender's email → retrieval during an ordinary user question → confidential information already in context embedded in image reference → automatic client request. A concrete project question may be illustrative, explicitly distinguished from the report's exact prompt.
- **Evidence:** E07.
- **Slide / note:** define Copilot's mail/document assistance; name attacker, benign user action, data, and destination role. Explain “zero-click” = no click on the malicious link, not no query/retrieval. No payload/endpoint reproduction.
- **Layout / time:** diagram-flow; ~2 min. **Acceptance:** Albert can narrate what happened without consulting the status table.

#### S21b — continuation
- **Must point / title:** **Microsoft Reported a Fix, Not Real-World Victims**.
- **Exhibit:** apply S20's evidence categories to this case, not another mechanism diagram.
- **Evidence:** E07–E08.
- **Slide / note:** research demonstration June 2025; Microsoft says mitigated/no customer action and no exploitation reported; no independent retest in the cited record. Avoid “no customers could ever have been exposed.” CVSS details can live in notes.
- **Layout / time:** compact comparison; ~1 min. **Acceptance:** provider assertion and researcher result are visibly attributed; dated historical case.

#### S22 — p22 “EchoLeak: The Path”
- **Must point / title:** **Existing Guards Missed This Leak Path**.
- **Exhibit:** same E07 sequence, now annotate guard locations and the reported bypass at each, with essential labels large enough at final size. If too dense, split the chain into causally meaningful steps, not small-type boxes.
- **Evidence:** E07.
- **Slide / note:** name classifier, image/link handling, allowed-endpoint restriction in plain language; explain each in the note. Avoid implying a filter never existed or that all sensitive organizational data was readable.
- **Layout / time:** figure-first diagram-flow; ~1.5 min. **Acceptance:** legible chain and a clearly identified automatic outbound request; no arrow ambiguity.

#### S23 — p23 “GitHub MCP: Public Issue, Private Repo”
- **Must point / title:** **The Same User's Public Issue Reached Private Repos**.
- **Exhibit:** same account enclosing public and private repo, attacker outside with write access only to a public issue, agent credential able to reach both. Public PR is the outgoing exposure.
- **Evidence:** E09.
- **Slide / note:** explicit answer **“Yes: the demo uses one user's public and private repos.”** Define Model Context Protocol once. Note generalizes to any authorized repositories, not only same-owned ones, and retains demonstration/status details with source date.
- **Layout / time:** diagram-flow; ~2 min. **Acceptance:** attacker is not granted private access directly; same-user fact is not generalized into a necessary condition.

#### S24 — p24 “GitHub MCP: The Token Is the Boundary”
- **Must point / title:** **A Broad Token Turned Reading Into Disclosure**.
- **Exhibit:** readable sequence from “check public issues” through private read to public PR; label token's permission scope and approval assumption. Focus on why the sequence was possible, not merely same ownership again.
- **Evidence:** E09.
- **Slide / note:** task-scoped credential/session as mitigation, not a blanket claim that all server bugs are irrelevant. Explain user “Always Allow” in note without inventing frequency.
- **Layout / time:** figure-first diagram-flow; ~1.5 min. **Acceptance:** essential labels readable; private-read and public-write edges both clear.

#### S25 — p25 “Comet: An Agentic Browser”
- **Must retain point:** a page-summary task can be steered toward other logged-in sessions. **Exhibit:** existing case-status comparison or a clear source-based case map; avoid a dense mechanism plus status-table collage.
- **Evidence:** E10. **Note:** preserve malicious comment, benign summary request, login-session authority and research-demo scope. **Layout/time:** slides decides; ~2 min. **Acceptance:** dated report; Brave and Perplexity roles explicit.

#### S26 — p26 “Comet: A Fix, Retested”
- **Must point / title:** **A Reported Fix Needed a Retest**.
- **Exhibit:** large, readable chronology from E10; all rows read left→right. Visually separate the undated later update rather than positioning it on a made-up date. Split if full chronology cannot fit legibly.
- **Evidence:** E10.
- **Slide / note:** state status is from the 2025 report/update, not a current vulnerability assessment. Notes explain origin isolation vs the agent's ability to act across authorized sessions.
- **Layout / time:** diagram-flow; ~1.5 min. **Acceptance:** dates/status distinctions readable without zoom; no implication browser origin protections were themselves defeated.

#### S27 — p27 “What the Three Cases Share”
- **Must retain point:** input, borrowed authority, exit. **Exhibit:** reduce comparison to these three dimensions; detailed current-status-looking row moves to notes with its historical qualifiers.
- **Evidence:** E07,E09,E10.
- **Note:** retain status comparison and secondary incidents already documented; no new incident expansion. **Layout/time:** one comparison; ~2 min. **Acceptance:** demonstrates a shared mechanism, not identical remediation evidence.

### P4 — Why labels and reminders are not enforcement

#### S29 — p29 “Priority Is Learned, Not Enforced”
- **Must point / title:** **Priority Means Whose Instruction Wins**.
- **Exhibit:** a conflict with a desired authority ordering, then distinguish model compliance from an action-level permission check. Retire “rank them” without explanation. Diagram labels must be large at final render.
- **Evidence:** E03,E11.
- **Slide / note:** “Not search ranking; instruction authority.” Real role metadata matters; an injected sentence saying “system” is not a real system message. Training can improve compliance without ensuring every output obeys it. Don't claim all software inherently separates data/code.
- **Layout / time:** diagram-flow; ~2 min. **Acceptance:** viewer knows what is ordered, why and what does/doesn't enforce it. S08 introduced the need; this explains the implementation limitation.

#### S30 — p30 “Instructions Look Like Data”
- **Must retain point:** documents may contain legitimate instructions addressed to someone else. **Exhibit:** annotated email “Please send the Q3 report to finance,” with intended human recipient versus agent task. **Evidence:** E01/E02 (illustrative).
- **Note:** reading, quoting, extracting and obeying are distinct. **Layout/time:** one worked example; ~1.5 min. **Acceptance:** does not advocate discarding all imperative sentences.

#### S31a — split p31 “Escaping Alone Is Not Authority”
- **Must point / title:** **Escaping Preserves Text as Text**.
- **Exhibit:** tiny ordinary quotation/structured-text example illustrating a reserved character represented literally, alongside the meaning of start/end data markers as one comparison. No exploit payload needed.
- **Evidence:** E11.
- **Slide / note:** define escaping and delimiters in plain words. Note explicitly distinguishes both from prepared/parameterized SQL, whose query structure is separate from data values. Don't say parameterization “escapes better” or universally “fixed SQL injection.”
- **Layout / time:** grid-2 comparison; ~2 min. **Acceptance:** a novice can define escaping and say why delimiters are used.

#### S31b — continuation
- **Must point / title:** **Marked Text Can Still Give Orders**.
- **Exhibit:** user summary request, bounded untrusted email, malicious instruction inside the boundary; then the vulnerable model's action. Show it never needed to escape the delimiter to be semantically obeyed.
- **Evidence:** E11,E12,E02.
- **Slide / note:** direct answer **“We can mark untrusted text; marking alone does not enforce authority.”** Note explains how delimiting may help and why enforcement needs a separate action/data-flow check. Avoid “delimiters do nothing.”
- **Layout / time:** diagram-flow; ~2 min. **Acceptance:** keeps both utility and limit of markers clear.

#### S32 — p32 “Detection Meets an Adaptive Attacker”
- **Must retain:** classifier errors and attacker adaptation; one miss can permit that attempt, not every single miss guarantees a successful exploit. **Exhibit:** variants → detector → one permitted candidate. **Evidence:** E14/E15.
- **Note:** false positives vs false negatives, not just word blacklist. **Layout/time:** diagram-flow; ~2 min. **Acceptance:** prepares measured defense comparisons without asserting universal detector futility.

### P5 — Explain the mechanisms before showing scores

#### S34 — p34 “Three Numbers Before Any Win”
- **Must retain:** clean utility, utility under attack, targeted attack success; low ASR from refusing everything isn't useful. **Exhibit:** one three-way metric comparison. **Evidence:** E13, §3.4.
- **Note:** define exact success and denominators for each cited experiment; don't pretend all papers implement utility identically. **Layout/time:** grid-3; ~1.5 min. **Acceptance:** metric terms precede results.

#### S35 — p35 “What Every Result Must State”
- **Must retain:** denominator, attacker access, budget, adaptation. **Exhibit:** one evaluation record with these four fields. **Evidence:** E13,E14.
- **Note:** static tested rate is not a deployment-risk estimate. **Layout/time:** comparison; ~1 min. **Acceptance:** no unsupported probability interpretation.

#### S36 — p36 “AgentDojo: A Benchmark for Injected Agents”
- **Must retain:** 97 tasks, 629 security cases, four suites; evaluate user's and attacker's goals separately. **Exhibit:** source Fig. 1 with readable explanatory key. **Evidence:** E13/E20.
- **Note:** clarify task versus task/attack case, use Workspace consistently. **Layout/time:** figure-first; ~1 min. **Acceptance:** synthetic benchmark example not confused with actual victim.

#### S37 — p37 “High Task Utility Did Not Ensure Injection Resistance”
- **Must retain:** association in a fixed-attack evaluation, not a causal law. **Exhibit:** AgentDojo Fig. 6a, readable axes/key. **Evidence:** E13/E20.
- **Note:** full Table 3 numbers and conflict with Table 5 remain. **Layout/time:** figure-first; ~1 min. **Acceptance:** “under attack” and targeted ASR never treated as complements.

#### S38 — p38 “Spotlighting: Mark the Untrusted Text”
- **Must retain:** what delimiting/datamarking/encoding do before result interpretation; datamarking result scoped. **Exhibit:** source Fig. 4, key at readable size. **Evidence:** E12.
- **Note:** retain caption/body discrepancy and separate utility test. **Layout/time:** figure-first; ~1 min. **Acceptance:** no universal zero-ASR claim or squeezed source legend.

#### S39 — p39 “Instruction Hierarchy: Train the Ranking”
- **Must proposed title:** **Training Improves Instruction-Priority Compliance**.
- **Exhibit:** retained Wallace Fig. 2, with exact paper hierarchy and robustness definition. **Evidence:** E03.
- **Note:** consistency with S08/S29, fine-tuned GPT-3.5 Turbo, selected five evaluations, no guarantee. **Layout/time:** figure-first; ~1 min. **Acceptance:** “ranking” isn't left undefined and method precedes its result.

#### S54 — new, after S39 and before S40
- **Must point / title:** **Repeat the User's Task After Tool Output**.
- **Exhibit:** original user instruction → untrusted tool result → repeated original instruction. Use the running email example. Mark which instruction is repeated and by whom.
- **Evidence:** E13.
- **Slide / note:** explain **repeat prompt = prompt sandwiching in these evaluations**. The system repeats the trusted user request after each tool result to re-emphasize the task; it does not ask the user to type twice or execute the action twice. The extra text is not an external permission check.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** C15 and sandwiching part of C16 answered before either named result.

#### S40a / S40b — split p40 “Simple Defenses on AgentDojo (GPT-4o)”
- **Must points / titles:** S40a **Reminders Helped Against the Fixed Attack**; S40b **Lower Attack Success Can Cost Useful Work**.
- **Exhibit:** magnitude comparisons as bars, not the old dense numeric table. Prefer no-defense/delimiting/repeat on S40a and no-defense/detector/tool-filter on S40b. Three metric roles remain clear, with same encodings across both pages. Preserve all old Table 5 values in notes, not necessarily as every bar label.
- **Evidence:** E13. Include model, fixed-attack scope and percentages/metric direction. The detector here is the 2024 AgentDojo detector, not automatically Prompt Guard.
- **Slide / note:** method definitions concise before comparing: generic classifier flags tool output; tool filter restricts available tools before reading outsider data. Show detector utility cost and tool-filter limitation. Notes include full precision, denominators, source conflicts, and no cross-model league table inference.
- **Layout / time:** figure-first; ~1.5 min total. **Acceptance:** interpretable three metrics; no tiny six-row table; original results not silently dropped.

#### S55 — new, after S40 and before S41
- **Must point / title:** **Prompt Guard Classifies Incoming Text**.
- **Exhibit:** tool output → separate attack classifier → permit/block decision → task agent. Label what the classifier sees and what it does not decide (task authorization).
- **Evidence:** E15,E14.
- **Slide / note:** brief definition, possible misses and false alarms, not the assistant policing itself. State a classifier version only if the cited evaluation configuration is verified. Note distinguishes this from the previous 2024 detector.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** C16's detector question answered before S41.

#### S56 — new, after S55 and before S41
- **Must point / title:** **MELON Checks Whether the User Task Matters**.
- **Exhibit:** prefer the legible mechanism part of MELON Fig. 2; if an original running-example adaptation is clearer, label it illustrative and cite §3. Two proposed-action paths: real task vs masked task with retrieved material retained → compare.
- **Evidence:** E16.
- **Slide / note:** expand the acronym once, explain the intuition in plain language. Similar proposed tool actions can suggest the external material is driving them; not an infallible rule. Note describes the masking/caching/focused comparison qualifications and extra inference cost. The diagram must not show a second actual harmful send as part of testing.
- **Layout / time:** figure-first; ~1.5 min. **Acceptance:** presenter can explain what was masked, what stayed and what is compared without reading code.

#### S41 — p41 “Against an Adaptive Attacker”
- **Must point / proposed title:** **Adaptive Search Broke the Tested Defenses**.
- **Exhibit:** the same five Gemini-2.5 Pro configurations from Table 7; fixed vs search ASR as a readable magnitude chart. Move the full clean-utility table to notes; preserve an on-slide reminder that low ASR alone is insufficient and utility-under-attack was not reported. If setup and chart cannot fit, split into a setup step and a result step.
- **Evidence:** E14; retain numeric values unchanged from pinned table.
- **Slide / note:** 80 cases; any success within up to 800 queries; output/scoring feedback, not assumed weight access. Clean utility in notes is the separate 97-task evaluation. State this is not a controlled continuation of S40 (different model/evaluation). CaMeL not tested here.
- **Layout / time:** figure-first; ~2 min. **Acceptance:** mechanism slides precede result, scope remains legible, and no model-independent conclusion.

### P6 — System checks and a human decision the user can judge

#### S42 — p42 “Where Does the Boundary Sit?”
- **Must retain:** learned/text filtering resistance vs code-enforced restrictions; all named defenses have different scopes. **Exhibit:** one boundary-location comparison. **Evidence:** E13,E15,E17,E18.
- **Note:** a detector may run outside the model but still isn't an authorization boundary; “outside” alone isn't the guarantee. **Layout/time:** grid-2; ~1 min. **Acceptance:** not a blanket guarantee for “system defenses.”

#### S43 — p43 “CaMeL: Program Written From the Trusted Request”
- **Must retain:** program generated from trusted request/configuration, quarantined reader for untrusted material. **Exhibit:** source Fig. 1 with explicit reading key; enlarge/crop/split rather than squeeze.
- **Evidence:** E17,E18.
- **Note:** planner sees trusted tool definitions/configuration too; untrusted data can legitimately affect runtime branches and arguments. **Layout/time:** figure-first; ~1.5 min. **Acceptance:** never “all execution fixed regardless of data.”

#### S44a — split p44 “CaMeL: Every Value Carries Its Origin”
- **Must point / title:** **Track Where Each Argument Came From**.
- **Exhibit:** adapt the S16 Bob example: recipient, selected document and document permissions each paired with an origin/reader label. Use essential labels at readable body weight and fewer boxes.
- **Evidence:** E17 (illustrative policy adaptation).
- **Slide / note:** define capabilities in this context as provenance/access metadata; do not imply the LLM invents trustworthy labels. Note explains propagation through derived values and parsing.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** audience can identify source and permitted reader, not just see an unexplained “capability” word.

#### S44b — continuation
- **Must point / title:** **The Policy Checks the Proposed Send**.
- **Exhibit:** trace one allowed send of a Bob-readable document to Bob; contrast a blocked added recipient or unauthorized document using the same check, not a new system. One decision diagram.
- **Evidence:** E17.
- **Slide / note:** code checks before execution; the illustrative rule is explicit. A changed destination and a forbidden document are different failure reasons. Asking is a possible authorized escalation, not mandatory override of a denial. Keep formal policy notation in tech only.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** decision follows shown facts and policy; every critical label readable.

#### S45 — p45 “CaMeL, Measured on AgentDojo”
- **Must retain:** two selected models, policy-enabled CaMeL, clean-utility cost, fixed-attack scope and source inconsistencies. **Exhibit:** existing quantitative comparison must satisfy current magnitude/legibility rules; split or use bars if needed. No result changes without evidence.
- **Evidence:** E17 Tables 2–4; 97 clean tasks vs 949 attacked cases; baseline notes preserve reported Gemini text/table conflict.
- **Note:** full values/uncertainties/other models remain; no adaptive-CaMeL claim. **Layout/time:** figure-first; ~1 min. **Acceptance:** useful tradeoff, not “zero attacks proves solved.”

#### S46 — p46 “What CaMeL's Guarantee Covers”
- **Must retain:** guarantee conditional on policies, implementation and threat model; misleading outputs, side channels, bad policy and compromised request remain. **Exhibit:** scope comparison. **Evidence:** E17.
- **Note:** no loss of prior legitimate-data-dependency corrections. **Layout/time:** grid-2; ~1 min. **Acceptance:** exact boundary and exclusions readable.

#### S47a — first of three, from p47 “Other System Defenses, Compared”
- **Must point / title:** **Dual LLM Isolates the Privileged Planner**.
- **Exhibit:** planner, quarantined reader and controller; label raw text versus handles/structured values and available tools. One architecture, not “two chatbots vote.”
- **Evidence:** E18,E17.
- **Slide / note:** what is isolated and its cost; returned data still needs checks. Note contrasts general pattern and CaMeL realization without claiming all dual-model systems are secure.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** explains what each part sees and why isolation matters.

#### S47b — second step
- **Must point / title:** **Limit Tools and Limit Their Reach**.
- **Exhibit:** one permissions comparison on the running email task: tool filter removes sending; least privilege limits which resources/recipients remaining tools can access. Both are actual restrictions when enforced by the host.
- **Evidence:** E13,E09.
- **Slide / note:** answer “which tool?” vs “which data/account scope?”; costs are useful actions/access denied or configuration burden; permitted tools can still carry out an attack.
- **Layout / time:** grid-2 comparison; ~1 min. **Acceptance:** not treating tool filtering and credential scoping as synonyms.

#### S47c — third step
- **Must point / title:** **Detection and Approval Check Different Things**.
- **Exhibit:** one pipeline with incoming text classification and proposed-action approval at different locations. Show each check's question and fallibility in the same terms as S55/S48.
- **Evidence:** E15,E19.
- **Slide / note:** input filtering may miss attacks/block benign text; approval may be uninformed or routine rubber-stamping. Not every row is a hard security guarantee. This closes the old five-row table without repeating the detailed S48 approval example.
- **Layout / time:** diagram-flow; ~1 min. **Acceptance:** all five old defense rows are covered over S47a/b/c, with mechanism and limitation, not names only.

#### S48 — p48 “Meaningful Approval”
- **Must point / title:** **Ask About Consequential Exceptions, Not Every Click**.
- **Exhibit:** one concrete authorization view for the E02/S16 world: exact action, destination, data/document, initiating source, and why this needs approval. Include a compact allow/deny/ask distinction as part of that decision view, not a separate chart.
- **Evidence:** E19 (explicit design recommendation), E09,E17.
- **Slide / note:** answer **“Routine authorized action: proceed; forbidden action: deny; consequential unresolved exception: ask.”** The UI should expose verified tool arguments and provenance, not merely “the agent says it is safe.” Note discusses data sensitivity, public posting, irreversible actions, user authority and fatigue; no empirical causal claim about all users.
- **Layout / time:** card or decision diagram; ~1.5 min. **Acceptance:** Albert sees what to ask, when, and what information the person needs; “important” isn't left subjective and “summary” isn't an injected narrative.

### Shared surfaces — exact per-ID obligations

These remain the integrator's responsibility, not parallel package edits. They carry no new research claims.

| ID / baseline page | Point/title and exhibit | Note/tech placement | Acceptance / time target |
|---|---|---|---|
| S01 / 1 | Retain lecture title and authority theme; title slide | Message motivates multi-source agents, no BANANA promise | Correct title/speaker; ~0.5 min |
| S02 / 2 | Six-section contents, same argument | Updated preview of opening and mechanism-first defense order | Matches dividers exactly; ~0.5 min |
| S03 / 3 | Core idea divider; agent-first framing | No “smallest toy case first” script | Matches new opening; ~0.25 min |
| S10 / 10 | Agentic surface divider, delegated authority | Transition deepens opening, doesn't restart motivation | One transition; ~0.25 min |
| S19 / 19 | Three incidents divider | Evidence categories distinguish demonstrations from victims | ~0.25 min |
| S28 / 28 | Why hard divider; instruction obedience vs enforcement | Reflect precise priority vocabulary | ~0.25 min |
| S33 / 33 | Defenses/measurement divider | Mechanisms before comparative results | ~0.25 min |
| S49 / 49 | Synthesis divider | Boundary location, not another defense catalogue | ~0.25 min |
| S50 / 50 | Design checklist: source, action, permission, exit, approval, evaluation; one structured audit exhibit | Apply briefly to E02 example; no new exercise | No activities; ~1.5 min |
| S51 / 51 | Open problems, one tradeoff map rather than cramped bullet wall | Retain policy engineering, legitimate data dependencies, side channels, usable approval, adaptation (E17/E19) | Specific unresolved questions, not claim all tradeoffs are solved; ~1.5 min |
| S52 / 52 | One closing takeaway exhibit: text is not authority | Preserve three metrics and conditional scope; no second global recap | Message agrees with revised lecture; ~1.5 min |
| S53 / 53 | Retain “Who decided?” closer | One closing thought | Correct final total; ~0.5 min |

## 4. Work packages and allowed files

All package changes include matching note articles with the same IDs, current titles, timing and migrated detail. No package touches another lecture, shared reference assets, design rules, or unrelated outline sections. All packages can read the whole plan/evidence; no unsupported facts from memory.

| Package | Main IDs / positions | May touch | Depends on |
|---|---|---|---|
| P1 | S04–S09 and their splits | Main, corresponding notes; new locally scoped figure assets if needed | E01–E05; establishes running example and vocabulary |
| P2 | S11–S18 | Main and corresponding notes; corresponding tech explanation only if consistency requires | P1's E02 example; E17 policy vocabulary |
| P3 | S20–S27 and splits | Main, paired notes, incident figure assets | E06–E10; reuse the new incident evidence key |
| P4 | S29–S32 and splits | Main, paired notes; matching tech only for terminology consistency | P1 authority vocabulary; E11–E12 |
| P5 | S34–S41; S54 before S40; S55–S56 before S41 | Main, paired notes, defense figure assets and local data/chart generator if required | E13–E16; P4 marking/priority concepts |
| P6 | S42–S48 and splits | Main, paired notes, matching CaMeL/metric tech consistency, relevant figure assets | P2 Bob example; P5 detector/tool-filter definitions |
| Integrator | S01/S02/dividers/S49–S53; all cross-references | Main, notes, `courses/trustworthy-ai/OUTLINE.md` lec13 entries; root only if a topic location actually changes; tracked job record | All packages |

Asset scope if new material is needed: `courses/trustworthy-ai/figs/lec13-clarity/`. Source-file crop scripts or chart-generation code belong there and are owned by slides, never slides-review. This is not authorization to rewrite shared scripts or `reference/`. Existing assets used elsewhere must not be overwritten destructively.

## 5. Integration and acceptance gates

1. **Original-request coverage:** report C00–C19 done/not done, baseline page/title → stable ID → new page. Report exact main/note counts and total note minutes.
2. **Facts first:** distinguish illustration from published observation; no added success/adoption statistics. Retain evidence qualifiers. C05 cites official ICLR/ICML documentation, not an unsourced anecdote. C10 answers yes for the demo, not merely a general permission explanation.
3. **Design:** current rules across the resulting deck; especially old small diagrams and density-heavy comparison tables. Every content slide gets a meaningful exhibit; empirical magnitudes favor bars. No label-size tricks, prose shrinking, aspect-ratio distortion or tightened prose rhythm. Counts/layouts are targets.
4. **Notes:** one article per displayed main ID, identical sequence; Message → explanation → details; answers, source scopes and figure readings agree in every layer. Check narrow-view horizontal overflow; move no content off a slide without placing it in notes/tech in the same edit.
5. **Rendering:** inspect all changed pages and neighbors at final size, including C08/C11/C12/C13/C17 diagrams and every new method slide. Lint alone cannot approve label readability, clipping or bad wraps. Report inspected IDs/pages and failures fixed.
6. **Shared surfaces:** reconcile section titles, contents, totals, leaf outline, source/figure lists, note timing and cross-references. Keep other lectures' outline entries untouched. Existing IDs stay stable; report all splits/new positions.
7. **Work report:** `work-r1.md` per PIPELINE, with exact reviewable commit, mapping, deviations, plan issues, unsourced facts and checks. Any locally generated numerical chart reports input table/version, parameters and reproduction path for evidence-log addition.
8. **Handoff:** slides-review reviews the exact supplied SHA, never a working tree. Do not open or merge the PR. After approved review, copy final review and refresh living files, push, then send final SHA; slides-review verifies post-review commits are job-log-only before opening the PR.
