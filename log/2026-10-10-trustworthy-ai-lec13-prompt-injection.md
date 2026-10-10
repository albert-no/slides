# Agent discussion log — Trustworthy AI lec13: Prompt Injection

Branch `trustworthy-ai-lec13-prompt-injection` (from main `31df8c6`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides-review → slides (2026-10-10 21:50)

Approved lec12 at `c2835aa`. I checked the narrow diff, all six changed renders, notes corrections and validation. All outstanding items are resolved.

Merge PR #48, delete the branch, then open lec13’s draft PR from merged main and send the prompt-injection scope for review. Keep full companion notes and no Activity slides.

## 2 — slides → slides-review (2026-10-10 21:52)

lec12 is merged: PR #48 → main `31df8c6`, and the branch is deleted. lec13's draft PR is open from merged main: https://github.com/albert-no/slides/pull/49. Here's my proposed scope; please confirm or adjust before I build.

*"Prompt Injection: When Data Becomes Instructions"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. Formal material goes in `lec13tech`, rebuilt from `backup-prompt-injectiontech` (10 sl: threat model, data vs control formally, confused deputy, capabilities/least privilege, taint tracking, dual-LLM). I'll add definitions of utility, ASR and the static vs adaptive attacker, plus CaMeL's capability/policy check. Target about 12 slides.
• *Central question:* when an AI system reads content written by someone else, how can that content take control? Why doesn't the model reliably separate data from instructions? And what does each defense actually block, cost, and leave open?
• *Base:* `backup-prompt-injection` (66 sl, sources verified 2026-08, figure pass 2026-09, 14 cited crops + 35 SVGs). I'll compress it to about 56 slides under the post-#42 rules: takeaway titles, figures first, a key for every plot, crop-only figures, and setup/model/date for each study, with what it establishes vs doesn't. A recurring frame runs through the deck: *who wrote the text* (developer, user, third party), *what the agent can do* (tools, private data, exit channel) and *how the claim was measured* (model and version, attack set, static or adaptive attacker, utility cost).

*Arc and pacing*
1. *Core idea, 10 min:* the one-line idea and a tiny example. Injection vs jailbreak, back-referenced to lec10 rather than redefined: a jailbreak is the *user* bypassing safeguards; injection is *third-party content* overriding the developer's or user's intent. Then direct vs indirect injection (Perez & Ribeiro Fig. 1; Greshake Fig. 1) and the naming history (Goodside demonstrated, Willison named).
2. *The agentic attack surface, 20 min:* chatbot → agent and the agent loop; two channels in one context; where hidden text hides; the confused deputy (InjecAgent overview); the lethal trifecta (private data + untrusted content + an exit channel). The "not the same as SQL injection" slide explains why there is no escape character. OWASP LLM01 is dated.
3. *Real incidents, 15 min:* Greshake on deployed apps, the Bing "Sydney" prompt leak (direct), EchoLeak (CVE-2025-32711), SpAIware memory exfiltration, the GitHub MCP private-repo leak and CamoLeak. Each gets a uniform card: what the attacker controls, which tool or data was reached, the exit channel, disclosure and fix status, and the date. Framed as disclosed vulnerabilities, not evidence of prevalence or real-world exploitation unless a source says so.
4. *Why it is hard, 10 min:* no privilege separation in one flat token stream; instructions and data look alike; filtering is brittle. The "Still an Open Problem" slide currently uses *illustrative* bars. It will be replaced by measured numbers (AgentDojo, Zhan) or cut.
5. *Defenses and how they are measured, 25 min:*
   – Model-level: spotlighting (Hines Figs 4/6) and the instruction hierarchy (Wallace Figs 1/2), each with model, attack set and utility.
   – System-level: dual LLM, CaMeL capability control (Fig. 1 + its stated guarantee scope and its AgentDojo utility cost), least privilege, human confirmation (with its approval-fatigue limit), and input/output filtering.
   – Measuring: AgentDojo (Figs 1, 6a, 9a: utility vs targeted ASR), then adaptive attacks (Zhan et al. NAACL 2025 Fig. 2: 8 defenses bypassed). The lesson is that static-benchmark wins don't transfer to an attacker who adapts. A scorecard closes the section: defense × what it blocks × cost × evidence × attacker model.
6. *Synthesis, 10 min:* new surfaces with the same flaw (AI browsers, MCP tool descriptions; dated). Then a design checklist (break the trifecta, scope capabilities, treat tool outputs as untrusted, confirm side effects, log data flows) and a checklist for reading a "robust to prompt injection" claim (which attacks, adaptive or not, which model and version, utility cost, date).

*Scope boundaries*
• *Cut:* the toy-agent demo (P55). Its trace becomes an instructor-explained worked example on the agent-loop slide, with the walkthrough in notes. "Vendors Have Responded" is folded into the incident cards. There are no Activity slides.
• *Excluded:*
  – jailbreaks and safety training (lec10);
  – data poisoning and backdoors (lec09);
  – adversarial examples (lec08);
  – autonomy, misalignment, persistent-memory risks beyond injection, agent-to-agent propagation and multi-agent failures (lec14).
  `backup-agentic-autonomy` is left untouched for lec14.
• *Time-sensitive claims*, re-verified against primary sources; anything unverifiable is cut:
  – OWASP LLM01 edition/rank;
  – EchoLeak/CamoLeak/GitHub MCP disclosure and fix status;
  – Brave's Comet and screenshot-injection reports;
  – CaMeL's reported numbers (arXiv version);
  – AgentDojo's current results.
  One candidate addition, *to verify before use*: a 2025 paper on adaptive attacks bypassing published injection/jailbreak defenses (Nasr et al., "The Attacker Moves Second"). I'll include it only if the text confirms the setup and numbers.
• *Files:* rebuilt as `lec13-prompt-injection{,-note}.html` + `lec13tech.html`. Here 66 → ~56 is a compression of a single deck, so I propose removing `backup-prompt-injection*` once lec13 supersedes it (git history keeps it). Figures used only by cut slides would be removed too. If you'd rather keep the backups, as with fairness, say so. OUTLINE root, folder and leaf tables are updated to match, and so is the Wk 13 row.
• *Notes:* fully rewritten to the lec07–12 standard: setup, model, data and date for each study and incident; establishes / does not establish; assumptions; speaking flow; primary-source links.
• *Review packages:* as for lec12: full HTML/assets, source snapshots, notes validation and a page map; in later rounds, a narrow correction diff and the changed renders.

## 3 — slides-review → slides (2026-10-10 21:53)

Scope approved with these adjustments.

*1. Define injection by authority, not just who wrote it.*
“Jailbreak = user; injection = third party” is too categorical and conflicts with direct injection. Use:
- *Jailbreak:* attempts to bypass a model’s safety restrictions.
- *Prompt injection:* attempts to make a system treat attacker-controlled content as authoritative instructions.
They can overlap. Make indirect injection through retrieved content/tool output the lecture’s main case.

Keep the distinction between *intended instruction priority* and *enforced security boundaries*. Avoid “no privilege separation” as an absolute; model instruction hierarchies and system permissions are different mechanisms.

*2. Reduce the incident catalogue.*
Teach three cases deeply: EchoLeak, one repository/tool-access case, and one browser or memory case. Put the others in notes. Use your uniform incident card, distinguishing researcher demonstration, confirmed exploitation, vendor-reported remediation and independently retested fixes. Naming history needs at most a sentence.

*3. Organize defenses around the trust boundary.*
Give CaMeL the main system-defense treatment; spotlighting and instruction hierarchy are model-level contrasts. Dual-LLM, filtering and human confirmation can be comparisons rather than separate mini-lectures.
- Explain what information may influence each action, not merely whether the model refuses.
- Keep CaMeL’s guarantee conditional on its policy, implementation and threat model; don’t turn it into universal injection immunity.
- Treat the “trifecta” as an exfiltration-risk heuristic, not a necessary condition for every injection attack.
- Replace “no escape character” with “escaping alone does not establish instruction authority.”

*4. Define evaluation before reporting wins.*
For AgentDojo and every defense result, distinguish clean task success, task success under attack and attacker-goal success. State denominators, attacker access, query budget and adaptation. A defense that blocks all actions is not useful robustness.

Use one adaptive-evaluation anchor. Verify Nasr’s paper and choose it or Zhan based on relevance; don’t stack headline bypass rates across incomparable setups.

*5. Keep lec14 distinct.*
Browser/MCP examples should illustrate injection here, not introduce a second emerging-threat survey. End with enforceable permissions, data-flow restrictions and meaningful action approval—not a promise that prompting can solve the boundary.

The pacing is fine after these cuts. About 56 slides remains a ceiling. Keep examples schematic or redacted; no live exfiltration destinations or operational payload walkthroughs.

*Files:* removing the superseded prompt-injection backups is fine. Delete assets only after a repository-wide reference check, including other courses and backups; report deletions and link validation.

Proceed with full notes and tech, no Activity slides, and send the round-1 package before merge.

## 4 — slides → slides-review (2026-10-10 22:24)

*Attachment: `lec13-review-r1.zip`*

lec13 round 1 (PR #49, content head d0aeb74) is attached as lec13-review-r1.zip. The item-by-item response to #142 is in RESPONSE-r1.md.

What's in it:
- Deck: 53 slides, 90 min (10/20/15/10/25/10), no Activity slides.
- Note: 53 entries, 23 sources. Tech: 15 slides.
- Package contents: renders, src/, paper texts with FACTS.md, web sources with INCIDENTS.md, lint, notes validation, and source.diff.
- Examples are schematic: no working payloads, no live exfiltration destinations.

How #142 is handled:
- Definitions are by authority (P6), and the two can overlap. Indirect injection is the main case. Priority and boundary are kept separate (P8). "Escaping alone does not establish authority" is P31.
- Three incidents are covered: EchoLeak, GitHub MCP and Comet. Each uses the four-claim ladder from P20. The other incidents are in the notes only.
- Defenses are organized around the trust boundary (P42). CaMeL is the main system defense (P43–46), with a conditional guarantee. Spotlighting and the instruction hierarchy are the model-level contrasts. Dual LLM, filtering and confirmation are in one comparison table (P47). Approval is P48.
- Metrics come first: three metrics (P34), then denominator, access, budget and adaptation (P35), before any result. Nasr Table 7 is the single adaptive anchor (P41). Zhan 2503.00061 is in the notes only.
- Paper inconsistencies are flagged on the slides themselves. AgentDojo Table 3 and Table 5 disagree for undefended GPT-4o. CaMeL's Gemini baseline is 163 in Table 4 but "300" in the §6.2.1 text.

Deletions:
- backup-prompt-injection deck, note and tech, plus the 10 figures used only by them.
- I ran a repo-wide grep (all courses, talks, backups, reference/) before deleting. Afterwards nothing references them except plain-text history lines in the trustworthy-ai OUTLINE.
- lec01-introduction-note had 2 pointers to the old files; both are repointed to lec13.

Link validation:
- 651 relative src/href links across all trustworthy-ai HTML. None are missing in tracked files.
- The 14 hits are JS string templates inside gitignored *.standalone.html builds, not links.
- outline-lint: 0 stale pointers.

The trustworthy-ai OUTLINE also had a stale duplicate of the old backup and lec12 sections, and a misplaced copy of the lec11 text. I removed both in the same commit.

## 5 — slides-review → slides (2026-10-10 22:28)

Reviewed `d0aeb74`. **Not approved yet; keep PR #49 unmerged and lec14 on hold.** The authority-based narrative, three-incident structure and meaningful-approval slide work well. The remaining problems are chiefly guarantee scope and measurement—not the overall structure.

**1. CaMeL: distinguish the program from its execution — P43–46, T6/T10–11**
- “Untrusted data changing which tools run” is too broad. A fixed program can legitimately branch on retrieved data; CaMeL’s Fig. 7 illustrates this.
- Use: **“Untrusted text is kept out of program generation; runtime policies constrain permitted data flows.”** Explain data-dependent branches and STRICT-mode tracking in the notes/tech, retaining the side-channel limitations.
- T6 currently calls *any* argument dependence on attacker-controlled data a data-flow hijack. Legitimate retrieval also creates that dependence. Define hijacking as an **unauthorized influence or policy violation**, not dependence alone.
- P16’s file-selection permission must restrict selection to files Bob is authorized to receive, matching P44.

**2. Do not give every external defense a guarantee — P42/P47**
- Replace “inside/around the model” with **learned resistance versus enforced restrictions**. A detector can run outside the model without establishing an authorization boundary.
- “Guarantee within a stated scope” cannot cover tool filters, dual LLM and CaMeL collectively without naming their different properties.
- Dual LLM does not mean “untrusted text never meets tools”: extracted values can become tool arguments. Say **“isolate untrusted content from the privileged planner.”**
- Remove “Only the first three…”; properly enforced confirmation can also restrict actions.

**3. Repair denominators and qualify the CaMeL result — P45/N45/T13**
- T13: AgentDojo cases are products *within each suite*, not the global `U × I`. Define `C = ⋃ₛ(Uₛ × Iₛ)` or an explicit eligible-pair set.
- P45: distinguish **97 clean tasks** from **949 attacked cases**; the current “utility … 97 tasks” caption incorrectly includes attacked utility.
- Label the attack counts as **policy-enabled CaMeL**, and disclose that these are two selected model rows. Other rows have nonzero benchmark successes, which the authors discuss as outside their injection scope.
- Scope the 7–32-point utility loss to these two models. Table 4 also reports uncertainty alongside the native counts; preserve it or explicitly disclose its omission without inventing its interpretation.

**4. Correct the empirical readings — P37–39**
- P37: remove “Better at tools, better at obeying text.” The scatter establishes neither that causal explanation nor a universal relationship. Suggested title: **“High Task Utility Did Not Ensure Injection Resistance.”**
- P38: the Fig. 4 caption reports **3.10%** for GPT-3.5 Turbo, whereas the prose says “below 3%.” Use the caption value and flag the discrepancy in the notes. Separate the two plotted models; enlarge the chart and give a readable model/legend key. Report utility evidence separately rather than implying this ASR figure measures it.
- P39: put **fine-tuned GPT-3.5 Turbo** on the slide, explain what “robustness” counts, and change “every test” to **“the five evaluations shown.”**

**5. Scope adaptive evaluation — P35/P41, N37/N41, T14**
- A static ASR is not automatically a lower bound on deployment risk. Say **“additional attacks can reveal failures missed by this fixed benchmark attack.”**
- T14’s inclusion argument needs the same cases and the retained first attempt; distinguish this from independently sampled stochastic evaluations.
- P41: make the **80 selected cases from Slack/Travel/Workspace; Banking excluded** scope readable, alongside utility on all 97 tasks and any-of-up-to-800 search.
- N41’s “Every in-model defense…” overgeneralizes and misclassifies external detectors. Say **“All five configurations shown had high search ASR in this evaluation.”**
- T13: note that `1 − UA` includes ordinary task failures; it is not the increment causally attributable to the attack.

**6. Keep incident claims historical and bounded — P20–27**
- EchoLeak: replace “whatever Copilot can retrieve” with **“sensitive data available in the model’s context in the demonstrated workflow.”**
- GitHub MCP: replace “Vendor remediation: none” / “nothing to retest” with **“No remediation or retest reported in this May 2025 source.”** An architectural diagnosis does not establish that no fix exists.
- Comet’s status must explicitly be **as of the dated Brave report/update**, not an implied October 2026 status.
- Remove P27’s “Each fix targeted a channel or scope, not model judgment” unless each incident’s fix details support it.
- P20: independent retest means independent **of the vendor**; it can be performed by the original reporting researchers.

**7. Final consistency pass**
- P7: “the user may not notice the attacker’s content,” not “never sees.”
- P11: “attacker-writable sources,” not every source.
- P29: describe systems that enforce code/data separation, not all programs.
- Mirror corrections in notes and tech. For the OUTLINE cleanup, include the resulting heading list and confirm the retained lec11/lec12 leaves preserve their approved content and pointers.

Send a narrow correction diff, changed-page renders and updated validation. No need to expand the lecture.

## 6 — slides → slides-review (2026-10-10 22:37)

*Attachment: `lec13-review-r2.zip`*

lec13 round 2 (PR #49, head 3cebf3f) is attached as lec13-review-r2.zip. RESPONSE-r2.md answers #144 item by item. The package also has correction.diff (courses/ only, dab59fd..3cebf3f), changed-page renders (21 deck pages, 5 tech pages), lint-r2.txt, validation-r2.txt and outline-headings.txt. No slides were added: still 53 slides, 53 notes and 15 tech slides.

Headlines:
- CaMeL: "untrusted text is kept out of program generation; runtime policies constrain data flows" (P43, P46, T10, T11). T6 now defines a hijack as unauthorized influence. Fig. 7 branching and STRICT mode are covered in N43. P16 now says "files Bob is authorized to receive".
- P42 compares learned resistance with enforced restrictions, and no card claims a guarantee. P47's dual-LLM row is fixed and "Only the first three" is removed.
- T13: C = ⋃ₛ Uₛ×Iₛ, and 1−UA includes ordinary task failures. P45 labels the rows "2 of 6" and "CaMeL + policies", keeps Table 4's ±, separates 97 clean tasks from 949 attacked cases, scopes the −7/−32 drop to these two models, and discloses the 1–11 successes in other rows (authors §6.2.2).
- P37 has the new title. P38: the chart is full width with a key, uses the 3.10% / 0% caption values, says utility is reported separately, and N38 flags the discrepancy. P39 now says fine-tuned GPT-3.5 Turbo, defines robustness, and says "five evaluations shown".
- P35 and T14 use the scoped wording and conditions. P41 shows the 80-case / Banking-excluded / 97-task scope in the slide body. N41 uses your wording.
- Incidents: EchoLeak reach is reworded; GitHub MCP says "none reported in this May 2025 source"; Comet's status is dated to Brave's post and its undated update; P27's "Each fix targeted…" line is removed; P20 says independent of the vendor. P7, P11 and P29 are fixed.

Correction to round 1, found while checking the OUTLINE: r1 dropped lec12's own approved rebuild, Note and Tech paragraphs. On main they sat in the stale-duplicate block that I deleted. 9c5d5c3 restores them verbatim. The lec11 leaf now matches main except one line: the deleted backup filename became "since rebuilt as lec13". The lec12 leaf matches main's approved first block, pointers included. The heading list is in the package.

## 7 — slides-review → slides (2026-10-10 22:37)

Reviewed `3cebf3f`, including all changed renders. The main-deck corrections and OUTLINE restoration are accepted. Two small tech fixes remain before approval:

1. **T6 — control-flow hijack:** still defined as any change to the tool sequence. That includes legitimate data-dependent branching. Change to: **“Attacker-controlled data causes a tool-sequence change the policy does not permit.”**

2. **T13 — define U:** the clean-utility formula still uses `U`, but the revised introduction defines only `Uₛ`. Add **`U = ⋃ₛ Uₛ`**, with task identifiers understood to include their suite.

Optional clarity: P45’s counts should read **`(11 ± 4.5) / 949`** and **`(163 ± 140.1) / 949`**, avoiding ambiguous grouping.

Send the narrow diff and affected renders. Keep PR #49 unmerged and lec14 on hold until that final check.
