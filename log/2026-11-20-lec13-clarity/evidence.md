# Evidence register

Verified 2026-11-20. Append-only. These are targeted checks of requested explanations and retained anchors, not a literature survey. An official incident report is a published report, not independent proof of every promotional claim. Historical incident status is dated, never presented as current product status. No working attack payloads or live exfiltration destinations are needed.

## E01 — Multi-source agents and injection entry channels
- Claim: tool-using agents ingest third-party pages, emails and files; direct injection enters through attacker-controlled user input, indirect injection through retrieved content. A legitimate user request is not automatically an injection.
- Sources: OWASP, LLM01:2025, “Types of Prompt Injection Vulnerabilities,” https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; Wallace et al., arXiv 2404.13208v1, §§2–3.2, https://arxiv.org/html/2404.13208v1 ; Greshake et al., AISec 2023, Fig. 3, https://arxiv.org/abs/2302.12173v2 .
- Setup/limits: definitions and application mechanisms, not an adoption survey; “agents are everywhere” is motivational framing, not a numerical prevalence claim. Existing Greshake crop remains usable.
- Label: published result / definition.

## E02 — Running email example
- Claim: illustrative user asks “Summarize today's project emails”; an attacker-controlled email asks the assistant to send a confidential project attachment outside the team. A vulnerable agent may summarize correctly while also taking the unauthorized action.
- Source: our schematic teaching example, adapted from the threat model in E01 and the original S13 toy trace; not a measured product run.
- Setup: agent has read access and an optional sending tool; legitimate task authorizes reading/summarizing, not sending. No real address or executable payload.
- Limits: no success probability or claim that every agent behaves this way. Use normal prose description of the malicious instruction rather than a working exploit.
- Label: illustrative example.

## E03 — Instruction priority
- Claim: priority decides which instruction wins a conflict; lower-priority text may supply relevant information without overriding higher-priority rules. Wallace's evaluated hierarchy was system > user > model outputs > tool outputs, with fine-tuned GPT-3.5 Turbo and incomplete resistance.
- Source: Wallace et al., 2404.13208v1, §§3.1,4 and Fig. 2, https://arxiv.org/html/2404.13208v1 .
- Limits: distinguish the lecture's simplified app-rule/user/retrieved-content diagram from the paper's exact hierarchy. Role markers carry provenance; literal words “system message” in an email do not create an actual system role. Do not claim all APIs use one hierarchy, or that roles provide no useful defense.
- Label: published result.

## E04 — Authors' invisible review instructions
- Claim: ICLR 2026 program chairs explicitly describe white-on-white submission text attempting to elicit positive LLM reviews, and classify the manipulation as attempted collusion.
- Source: ICLR, “Policies on Large Language Model Usage at ICLR 2026,” “Inserting hidden ‘prompt injections’ into a paper,” https://iclr.cc/FAQ/LLM .
- Setup/limits: an official acknowledgement and policy description, not a measured success rate or proof about a named author. Distinguish human-visible PDF rendering from extractable text; not every PDF-reading pipeline exposes the same hidden material.
- Label: published report.

## E05 — ICML's organizer-inserted review probe
- Claim: ICML 2026 inserted hidden PDF instructions to include two assigned phrases; used matching reviews plus human inspection to identify violations of its no-LLM reviewing policy.
- Sources: official Peer Review FAQ, “Reviewing and rebuttals,” https://icml.cc/Conferences/2026/PeerReviewFAQ#prompt_injection ; official program-chair post, “Technical Approach,” 18 March 2026, updated 26 March, https://blog.icml.cc/2026/03/18/on-violations-of-llm-review-policies/ .
- Setup: enforcement discussed in the post concerns Policy A (no LLM use). The FAQ identifies a page-two footer probe; it distinguishes review-score manipulation from detection-only prompts.
- Limits: evadable, incomplete detection; human review excluded text merely discussing the probe. No need for enforcement counts. Not a claim that every conference adopted it, or that absent phrases prove no AI use.
- Label: published report.

## E06 — Incident evidence categories
- Claim: demonstration, real-world exploitation, provider-reported remediation and third-party retest answer different questions. “Vendor” means the product/service provider (Microsoft for Copilot, Perplexity for Comet); a retest may be by the original researcher if independent of that provider.
- Sources: E07–E10, compared using our teaching taxonomy.
- Setup/limits: “not reported” is not “did not happen”; the four categories are not necessarily consecutive stages and a demonstration does not imply real victims. GitHub MCP spans an integration and client, not one vendor with a universal patch.
- Label: our synthesis, based on published reports.

## E07 — EchoLeak mechanism
- Claim: malicious email retrieved during an ordinary Copilot query caused context data to be included in an image-reference request; automatic image fetching plus an allowed Microsoft endpoint enabled the reported leak without clicking the attack link.
- Source: Aim Labs, 11 June 2025 archived primary report: https://web.archive.org/web/20250611174716/https://www.aim.security/lp/aim-labs-echoleak-blogpost . Read successfully through the archive's `id_` representation. Locators: “Step 3: Image redaction bypass,” “CSP bypass using Microsoft Teams,” “Exploitation method #2 - LLM Scope violation,” FAQ “What could have been leaked?”
- Setup/limits: research demonstration, data already in that LLM context (including retrieved resources), not arbitrary tenant-wide access. “Zero-click” does not mean no user query or no retrieval condition. Do not reproduce endpoint syntax or payload.
- Label: published report.

## E08 — EchoLeak provider status
- Claim: Microsoft describes information disclosure, mitigation already deployed, no customer action; its exploitability field says “Exploited:No.”
- Sources: MSRC CVE-2025-32711 advisory https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711 ; authoritative machine-readable record https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/2025-Jun , Vulnerability/CVE=CVE-2025-32711, FAQ and Threats. Initial release 11 June 2025; 20 February 2026 revision changes CWE only.
- Setup/limits: vendor assertion, not an independent post-fix test. Main slide need not retain CVSS figures, which distract from the mechanism; if retained, distinguish Microsoft and NVD scoring.
- Label: published report.

## E09 — GitHub MCP repositories and permissions
- Claim: published setup explicitly uses the same user's public and private repositories. An attacker places an issue in the public one; the user's agent reads it, retrieves private data through its credentials, and publishes a public PR. MCP = Model Context Protocol.
- Source: Invariant Labs, 26 May 2025, “Attack Setup,” “Attack Demonstration,” “Mitigations,” https://invariantlabs.ai/blog/mcp-github-vulnerability .
- Setup/limits: own-account demo, Claude Desktop/Claude 4 Opus with official GitHub MCP server; approval configuration matters. No real-world exploitation or remediation/retest reported in this dated source. General risk follows credential reach, not same ownership as a necessary condition. The report says server-side patching alone cannot resolve the architectural issue; it suggests restricting repository permissions and sessions. Its “Always Allow” observation is not a controlled causal study of fatigue.
- Label: published report.

## E10 — Comet chronology and authority
- Claim: Brave demonstrated hidden Reddit content steering a page-summary agent into the user's other logged-in sites. Timeline: report 25 July, initial fix 27 July, incomplete retest 28 July, appears patched 13 August, publication 20 August 2025; undated update reports incomplete mitigation.
- Source: Brave, “Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet,” disclosure timeline and update, https://brave.com/blog/comet-prompt-injection/ .
- Setup/limits: Brave is independent of Perplexity but a competing browser vendor; research demonstration, not confirmed real-world exploitation. Do not put an undated update at an invented date or assert this is current 2026 status. Browser origin checks are not broken: an authorized agent can navigate/use multiple sessions.
- Label: published report.

## E11 — Escaping, delimiting and parameterization differ
- Claim: escaping encodes syntax-sensitive characters so they are treated literally; delimiters mark the beginning/end of data; parameterized SQL separates query structure from bound values. The first two are not synonyms for parameterization.
- Source: OWASP SQL Injection Prevention Cheat Sheet, “Defense Option 1: Prepared Statements (with Parameterized Queries)” and “Defense Option 4: STRONGLY DISCOURAGED: Escaping All User-Supplied Input,” https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html .
- Limits: correct parameterization protects that query's value boundary, not every SQL use or the entire application. A model can still interpret an instruction contained within visibly marked data.
- Label: published guidance; final model contrast supported by E12.

## E12 — Marking helps, without authorization
- Claim: spotlighting marks provenance by delimiting, datamarking or encoding; it improves the tested fixed-attack performance, not a universal authorization guarantee.
- Source: Hines et al., 2403.14720v1, §§III,V and Fig. 4, https://arxiv.org/html/2403.14720v1 .
- Setup/limits: 1,000 synthetic summarization documents; Fig. 4's GPT-3.5 Turbo caption gives 3.10%, text says below 3%; retain caption-based 3.1 and note conflict. text-003 zero in this test, not all attacks. Utility is separately evaluated. Do not change existing result values from memory.
- Label: published result.

## E13 — Repeat prompt and fixed AgentDojo defenses
- Claim: prompt sandwiching repeats the user's instruction after each tool result; a BERT injection detector aborts on detected output; tool filtering chooses needed tools before seeing untrusted data.
- Source: Debenedetti et al., AgentDojo, NeurIPS 2024 D&B / 2406.13352v3, §4.3 and Table 5, https://arxiv.org/html/2406.13352v3 .
- Setup: GPT-4o, fixed attack, 629 security cases; table values retained with rounding from the baseline. Utility and attack success are distinct metrics; §3.4 defines task/test sets. Do not casually label clean utility as 629 independent user tasks.
- Limits: Table 3/5 undefended ASR conflict (47.69/57.69); §4.3/table tool-filter conflict (7.5/6.84); use Table 5 consistently. Tool filtering fails when permitted tools suffice. Repetition is neither guaranteed safety nor a command to execute twice.
- Label: published result.

## E14 — Adaptive comparison
- Claim: Nasr et al. Table 7 has high search attack success on the displayed Gemini-2.5 Pro defenses despite lower fixed-attack rates.
- Source: 2510.09023v1, 10 October 2025, §§5.1,5.3,5.4, Appendix B.1, D, G.1/Table 7, https://arxiv.org/html/2510.09023v1 .
- Setup: 80 cases, Slack/Travel/Workspace; up to 800 queries with output and scoring feedback, any success counts. Utility evaluated separately on the full 97 tasks. Retain baseline rounded values; no utility-under-attack reported.
- Limits: not controlled against the GPT-4o table; no CaMeL evaluation. Source is the pinned 2025 preprint, not an updated leaderboard. Do not infer a universal failure theorem or use a human-competition-specific configuration as proof of Table 7's detector version.
- Label: published result (preprint).

## E15 — Prompt Guard is a separate classifier
- Claim: Meta's Prompt Guard classifies text for prompt attacks; a host application uses its result to block/flag input. It is not the task-performing assistant, and detection errors remain possible.
- Source: Meta model card, “Model Information,” “Model Scope,” “Limitations,” https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M . E14 §5.3 supports its evaluated use as a filtering defense.
- Setup/limits: version-specific card describes Prompt Guard 2 binary benign/malicious classification; don't conflate with the original three-class Prompt Guard or AgentDojo's separate 2024 detector. Exact Table 7 variant not established by the human-contest paragraph; omit size/version unless separately verified.
- Label: published documentation.

## E16 — MELON's idea
- Claim: MELON = Masked re-Execution and TooL comparisON. Compare proposed tool actions under the real task and a masked-task run that retains retrieved material; similar actions can signal that retrieved text is steering the agent.
- Source: Zhu, Yang, Wang, Guo, Wang, ICML 2025, §§3.2–3.3, Fig. 2, https://proceedings.mlr.press/v267/zhu25z.html ; PDF https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25z/zhu25z.pdf .
- Setup/limits: detection signal, not a guarantee that matching calls are always malicious. Notes should distinguish proposed calls from executing harmful side effects twice; describe masking, tool-call cache and focused comparison without presenting a simplistic equality test as the full implementation. E14 tests an adaptive implementation and finds bypasses.
- Label: published result.

## E17 — CaMeL provenance and policy
- Claim: trusted-input planning is separated from untrusted-data parsing; capabilities carry sources and allowed readers, and interpreter policies check tool calls. Runtime data dependencies may be legitimate and still need checks.
- Source: Debenedetti et al., 2503.18813v2, §§2,3.1,5.1–5.4,7,9.2–9.3; Figs. 1,5–7, https://arxiv.org/html/2503.18813v2 .
- Setup/limits: “send Bob the document” teaching application needs both recipient provenance and Bob's access to the selected document. Exact example policy is an illustrative choice, not a universal hardcoded CaMeL rule. Program generation is isolated, not all data-dependent execution. No guarantee against misleading answers, wrong policies, compromised trusted input or every side channel.
- Label: published result plus explicitly labeled illustrative policy.

## E18 — Dual LLM boundary
- Claim: privileged planner operates on handles rather than raw untrusted content; quarantined reader processes that content without tool privileges, mediated by a non-LLM controller.
- Source: Willison, 25 April 2023, “The Dual LLM pattern for building AI assistants that can resist prompt injection,” https://simonwillison.net/2023/Apr/25/dual-llm-pattern/ .
- Limits: not just “use two models” or “make a second model verify”; returned data still needs constrained use. It is a design pattern, not an empirical universal guarantee.
- Label: published design proposal.

## E19 — Meaningful approval design
- Claim: prioritize explicit consequential exceptions; show the exact proposed action, destination, data and initiating source from trusted system records; do not turn an injected model summary into the authorization view. Deterministic policy can allow known-safe routine actions and deny forbidden actions.
- Sources: our design recommendation, motivated by E09 “Always Allow” observation and CaMeL §9.2 “De-classification and user fatigue” in E17.
- Setup/limits: “ask less” is not “auto-allow uncertain risky actions.” A human prompt is appropriate only where the human has authority and enough information. This is a recommendation, not a measured optimum or a causal finding from the incident report.
- Label: illustrative design recommendation.

## E20 — Visual provenance
- Existing source figures: Greshake Fig. 3 (E01), InjecAgent Fig. 1 https://arxiv.org/abs/2403.02691 , AgentDojo Figs. 1/6a (E13), Hines Fig. 4 (E12), Wallace Fig. 2 (E03), CaMeL Fig. 1 (E17). Preserve source crops or split/crop with accurate attribution; never repaint data.
- New method figures: prefer MELON Fig. 2 and CaMeL Figs. 5–6 when useful; source reading is required before use. A running-example adaptation may use an original diagram labeled illustrative.
- Generated empirical charts must use the pinned table values in E13/E14 (and original CaMeL Tables 2–4 if redrawn), preserve full precision in data, and have reproducible code in the repo. slides reports paths, inputs and parameters for addition to this register before approval. No such generated artifact exists at planning time.
- Label: source/production requirements, not a research finding.


## E21 — Correction to E20 / plan-v1 S43: CaMeL figure identity
- Claim: CaMeL Fig. 1 illustrates the control/data-flow problem. Fig. 5 is the system architecture: privileged planner, quarantined parser, interpreter, tool execution and policy checks.
- Source: Debenedetti et al., 2503.18813v2, §2 Fig. 1 and §5 “CaMeL Design,” Fig. 5, https://arxiv.org/html/2503.18813v2 .
- Limit: do not relabel Fig. 1's generic control-flow boundary as an actual planner-generated program, or its extraction nodes as explicitly depicted Q-LLM components. The v1 plan's mandated Fig. 1 was a planner error; v2 corrects it. Runtime data-dependent branches remain legitimate subject to policy.
- Label: published figure identity; correction to planner's exhibit choice.

## E22 — AgentDojo clean-utility reporting caveat (clarifies E13)
- Claim: distinguish 97 distinct user tasks from the exact aggregation underlying the printed Table 5 percentages. §3.4 defines benign utility over user tasks, but the printed percentages/intervals do not identify a simple unweighted single run over 97 tasks.
- Source: AgentDojo 2406.13352v3, §3.4, §4 and Tables 3/5, https://arxiv.org/html/2406.13352v3 . Author code snapshot 30e9bdebe9bb15502480babfed17bd5d0c92d24d (24 Nov 2024 or earlier), `src/agentdojo/benchmark.py:372–397` and `util_scripts/create_results_table.py:43–167`, https://github.com/ethz-spylab/agentdojo/tree/30e9bdebe9bb15502480babfed17bd5d0c92d24d . That loader has one clean result per user task, but does not resolve how the paper's older Table 5 was aggregated.
- Our arithmetic check: 85.53% × 97 = 82.9641, not an integer count; 538/629 rounds to 85.53%. This is evidence of an aggregation ambiguity, not proof that 629 is the clean denominator. Repeated/weighted runs could also explain it.
- Resolution: retain Table 5 values and benign-utility definition, retain benchmark counts, remove the definitive “clean utility over 97 user tasks” attribution attached to these table values. Note: “Clean utility is reported as in Table 5; the benchmark has 97 distinct tasks, but the aggregation behind these printed percentages is not fully specified here.” Do not relabel as 629 independent clean tasks or propagate this caveat to different studies without evidence.
- Label: published results plus our calculation; exact Table 5 clean aggregation unresolved.

## E23 — Round-1 generated quantitative figures
- Inputs: AgentDojo Table 5 five triples from E13; Nasr Table 7 five Gemini-2.5 Pro fixed/search pairs from E14. Repo generator: `courses/trustworthy-ai/figs/lec13-clarity/p5-bars.py`, modes `s40a`, `s40b`, `s41`. Table 5 bar length = 2.1 × full-precision percentage; Table 7 = 7 × percentage. Labels: decimal half-up to one place for Table 5, integers for Table 7. These inputs match the pinned source values. Correct the generator's clean-denominator description per E22 without altering its values.
- CaMeL S45: `courses/trustworthy-ai/lec13-prompt-injection.html`, inline SVG identified by S45, contains the source geometry and reproduction parameters. Inputs: utility 84.5/77.3 (o3), 73.2/41.2 (Gemini); attacks 11 ± 4.5 / 0 and 163 ± 140.1 / 0, Tables 2/4 of E17. Utility height = 1.8 × value; attack height = 0.9 × value; common baseline 255; zero shown as a thin marker with explicit 0, not a positive outcome. Source values retained; selected two of six models; 97 clean tasks versus 949 attacked cases as in that study.
- Revision condition: report updated generator/geometry paths and parameters if round 2 changes these exhibits. Main/note/generated values must stay synchronized.
- Label: published inputs; original chart rendering.
