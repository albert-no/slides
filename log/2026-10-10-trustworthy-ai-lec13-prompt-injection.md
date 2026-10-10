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
