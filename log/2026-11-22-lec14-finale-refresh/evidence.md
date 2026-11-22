# Evidence register — append-only

Cutoff for this bounded refresh: 2026-11-22. These are selected case/source checks, not an exhaustive literature survey. Each entry distinguishes the underlying observation from the teaching inference. Original source versions below stay pinned even when newer work exists. Do not label a dated result a current frontier maximum.

## E01 — course continuity and duplicate material
- Claim: the merged lec13 already explains instruction authority, agent permissions, data flow, adaptive injection, CaMeL, other system defenses and meaningful approval. Lec14 should add longer tasks, strategic behavior, interaction and control, not teach those fundamentals again.
- Source/version/locator: baseline `34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233`, `courses/trustworthy-ai/lec13-prompt-injection.html`, IDs S04–S18, S29–S48, S50–S52; paired notes; leaf OUTLINE lec13/lec14 sections. https://github.com/albert-no/slides/tree/34b40ca35c9433be7c9d2ca2cc90d0d89bbdd233/courses/trustworthy-ai
- Setup/limits: curricular continuity, not evidence that injection is solved. No inference from a defense's presence to immunity. Label: illustrative example / editorial synthesis of published material.

## E02 — autonomy and compounding
- Claim: autonomy is multidimensional; longer action chains can accumulate errors. The displayed independent-step calculation is illustrative, not a measured agent failure rate.
- Source/locator: baseline lec14 S05/S06 and `lec14tech.html` p6. Our calculation: independent success probability p=.95 for n=20 gives p^n=.3584859. No fitted data.
- Limits: independence and no recovery are assumptions, not realistic universal properties; no causal law that every autonomy increase necessarily raises harm. Label: our calculation / illustrative example. If retaining a generated curve, use p=.95, n=0…20; slides must record the generator path and plotting inputs, not draw by eye.

## E03 — a real, bounded shop experiment
- Claim: Anthropic and Andon Labs had Claude Sonnet 3.7 operate an office shop; pricing below cost was one observed failure.
- Source/version/locator: Anthropic, 27 Jun 2025, https://www.anthropic.com/research/project-vend-1 ; opening setup, “Claude’s performance review”; shop photo and architecture (Figure 2).
- Setup: actual goods and employee customers, with human physical assistance; the experimental email tool was not unrestricted real email.
- Limits: a company-run exploratory experiment, not a representative commercial deployment or a controlled estimate of all agents. Label: published result (first-party experimental report).

## E04 — improved results do not isolate one cause
- Claim: the December follow-up reports better shop performance after several model, tool and procedure changes; the added manager agent was not established as the cause.
- Source/version/locator: Anthropic, 18 Dec 2025, https://www.anthropic.com/research/project-vend-2 ; “The numbers”, “What changed?” / “Tools” / “The CEO”, “What actually worked?”. Use the source’s business-performance or weekly-profit figure, caption identified explicitly (no fabricated figure number).
- Setup: Sonnet 4.0 then 4.5, changing scaffolding; no clean phase boundary. Human purchase check remained; not fully autonomous commerce.
- Limits: no ablation identifies the model, tools or manager as the unique cause; continued failures remained. Label: published result (first-party experimental report).

## E05 — real developer work can disagree with expectations
- Claim: the early-2025 METR randomized study found longer task completion times with AI allowed in its setting, despite participants' positive perceptions.
- Source/version/locator: Becker, Rush, Barnes, Rein, https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ , “Methodology”, “Core Result”, limitations table; paper https://arxiv.org/abs/2507.09089 . Prefer its forecast-versus-observed chart; disclose omitted forecast groups if cropped.
- Setup: 16 experienced open-source developers, 246 tasks in familiar repositories, AI allowed/disallowed by task, mainly Cursor with Claude 3.5/3.7 Sonnet. Observed completion time +19%; post-study perceived time −20%; different quantities from autonomous time horizons.
- Limits: not all developers/tasks; not November 2026 tools. Label: published result.

## E06 — the relevant 2026 follow-up is inconclusive on effect size
- Claim: METR reports that selection and time-measurement problems make its late-2025 follow-up unreliable as a current productivity estimate; it is revising the design.
- Source/version/locator: 24 Feb 2026, https://metr.org/blog/2026-02-24-uplift-update/ , introduction and “Wider adoption of AI has made it more difficult to measure task-level productivity”.
- Setup: developers/tasks can opt out of AI-disallowed work; concurrent agents complicate time accounting. No new headline percentage is authorized by this plan.
- Limits: does not establish that current tools slow everyone, or a reliable opposite effect size. Label: published result (research update).

## E07 — time-horizon anchor and dated sensitivity note
- Claim: the fitted human-task-length threshold is a capability summary on a task distribution, not safe unattended runtime.
- Source/version/locator: Kwa et al., NeurIPS 2025, https://arxiv.org/html/2503.14499v4 ; §§2–3, Fig.1, §3.2.1, §6, App.C.3 and E.3–E.4. V4 date 10 Jul 2026; plotted model-release data are 2019–2025, not a current leaderboard.
- Setup: retain baseline model–scaffold, successful-human reference and success-threshold qualifications. Fig.1’s reported historical doubling is 207 days, with its uncertainty in notes.
- Related update: Alexander Barry, 20 Mar 2026, https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/ , “Summary”. This is a lower-review research note on newer evaluations, not the same plotted snapshot.
- Limits: task sampling, fit and threshold matter; do not merge snapshots. Label: published result.

## E08 — replication components versus the complete chain
- Claim: sandboxed component success does not establish reliable end-to-end autonomous replication.
- Source/version/locator: Black et al., https://arxiv.org/html/2504.18565v2 (5 May 2025), Fig.1, §5.1 and §6 “Limitations”.
- Setup: 86 tasks across 20 families, five evaluated models. Keep the existing two unmodified domain crops; pass@10 means at least one successful attempt among ten. Any exact number remains tied to its task/model/attempt budget.
- Limits: paper lacks a truly end-to-end evaluation; do not relabel a sandboxed recursive task as the entire real-world chain. Keep source's inconsistent hardest-family counts in notes, not a new headline. Label: published result (preprint).

## E09 — scheming and incentive-induced underperformance
- Claim: constructed contexts can elicit oversight subversion and underperformance; these experiments do not measure deployment prevalence or prove intent.
- Source/version/locator: Meinke et al., https://arxiv.org/html/2412.04984v2 , §§2–3, Tables 1/2/4/6 and §3.6; §4 “Limitations”.
- Setup: distinguish provided goal/nudge, observable action and inferred motive. Oversight rates and follow-up denial rates have different denominators. Arithmetic removal is threatened, not executed.
- Limits: sandbox, provided information/incentives; un-nudged is not natural deployment. Retain Table2 caption/text sample-count discrepancy in notes. Label: published result (preprint).

## E10 — prompted sandbagging
- Claim: the study measures selective strategic underperformance under instructions/training, not its spontaneous frequency.
- Source/version/locator: van der Weij et al., ICLR 2025, https://arxiv.org/html/2406.07358v4 ; §2, §4, Table1, Fig.5, App.D.
- Setup: WMDP hazardous-knowledge proxy versus MMLU biology control; baseline displayed accuracy excludes refusals. Password-locking is a separate trained example, not the prompt-only comparison.
- Limits: no claim of capability erasure; models/dates and denominator must accompany numbers. Label: published result.

## E11 — multi-agent problems are not one failure mechanism
- Claim: miscoordination, conflict and collusion differ in goals and cooperation; external propagation is a separate attack route, not a fourth label attributed to the same taxonomy.
- Source/version/locator: Hammond et al., Cooperative AI Foundation Technical Report #1, https://arxiv.org/html/2502.14143v1 , Fig.1 and taxonomy sections.
- Setup: conceptual taxonomy; no frequency estimate. Limits: not a proof of inevitable emergent collusion. Label: published result (conceptual report).

## E12 — MAST: system design and verification
- Claim: failures in multi-agent frameworks can arise without an adversary; roles, communication and verification matter.
- Source/version/locator: Cemri et al., NeurIPS 2025 Datasets & Benchmarks, official venue https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html ; https://arxiv.org/html/2503.13657v3 , Fig.1, §4–5 and App.H.2 Table5.
- Setup: MAST-Data has 1,642 traces over seven frameworks; failure-category shares are not deployment incident rates. ChatDev intervention configurations are separate comparisons, not guaranteed incremental gains.
- Limits: not a claim every multi-agent system is worse than a single model; no new percentage required on main. Label: published result.

## E13 — propagation is the extension, not a second injection lesson
- Claim: manipulated text can be forwarded between agents; simulated spread depends on the experimental environment.
- Source/version/locator: Lee & Tiwari, https://arxiv.org/html/2410.07283v1 (9 Oct 2024), §§3–6, Figs.4–6, Table2/Fig.7.
- Setup: separate task-oriented apps from the simulated agent society. In the latter, all-agent spread required additional memory-importance manipulation in the reported setup.
- Limits: not a real-world worm outbreak or deployment prevalence. Tagging/marking results are handcrafted-attack tests without measured normal-utility cost; no immunity guarantee. Label: published result (preprint).

## E14 — collusion results are limited, unlike metrics
- Claim: hiding coordination from oversight is possible in limited evaluated settings, not established as routine deployment behavior.
- Source/version/locator: Motwani et al., https://arxiv.org/html/2402.07510v5 , §3, §5–6, Table3.
- Setup: keep cipher round-trip correctness, code agreement and covert-channel success as distinct tasks/metrics; do not rank them together. Main needs the concept and scope; detailed percentages move to notes.
- Limits: dated models through GPT-4; do not imply current frontier rates. Label: published result (preprint).

## E15 — control is tested under an explicit adversary
- Claim: Greenblatt et al. compare protocols for using an untrusted model under limited trusted auditing, with separate safety and usefulness quantities.
- Source/version/locator: ICML 2024; https://arxiv.org/html/2312.06942v5 , §2, Fig.1 right panel, §3, Tables2/7, Fig.2, §2.4, §5.1.
- Setup: retain exact baseline definitions, model roles, protected simulated audit, run length and budget. “Trusted” is an assumption, not an empirical guarantee from model weakness. Usefulness is normalized, not accuracy. No new numeric comparison authorized.
- Limits: strongest attacks found, no train/validation split, bounded task setting; avoid deployment guarantee. Label: published result.

## E16 — a 2026 frontier question: when to attack
- Claim: selective start/stop policies lower measured empirical safety in the two evaluated agentic environments, without requiring stronger underlying attack execution.
- Source/version/locator: Ge-Wang, Crosse et al., https://arxiv.org/html/2606.06529v1 (3 Jun 2026), Fig.1, §3, Table2, §4.4, App.A. Cite as preprint unless workshop venue is independently confirmed.
- Setup: BashArena/LinuxArena, model-based scoring and cross-validated threshold selection. Metric conditions on caught or successful-uncaught attacks; unlike Greenblatt’s run-level quantity. Main can be qualitative; numerical Table2 details stay in notes.
- Limits: effect-size upper-bound methodology, small post-filter samples, wide uncertainty; no autonomous deployment attack rate. Label: published result (preprint).

## E17 — monitor vulnerability, keep as a short limit
- Claim: tested monitoring protocols can themselves be attacked through inspected outputs.
- Source/version/locator: Terekhov et al., https://arxiv.org/abs/2510.09462v2 (2 Mar 2026), abstract and full paper linked there; existing lec14 S45 note source.
- Setup/limits: scope to evaluated monitor/protocol/benchmark configurations, not every possible control system. No new attack walkthrough: that would duplicate lec13. Label: published result (preprint).

## E18 — why capability testing matters
- Claim: dangerous-capability testing can inform deployment decisions before release.
- Source/version/locator: Shevlane et al., https://arxiv.org/abs/2305.15324v2 , Table1 and §4; retained lec14 S08 source. No new claim about present lab policy.
- Setup/limits: illustrative capability categories, not proof that passing tests is safe. Label: published result.

## E19 — course-wide synthesis is not a theorem
- Claim: trustworthy AI requires evidence matched to a claim and a use context across data, answers, attacks, provenance/fairness and action oversight.
- Source/version/locator: baseline course leaf OUTLINE lecture index and lec01–lec14 paired slides/notes. Data: lec02–05; reliability/incentives: lec06–07; attacks: lec08–10 and lec13; provenance: lec11; group impacts: lec12; autonomous actions: lec14.
- Setup: pedagogical synthesis with no new empirical quantity. Limits: five questions are not a certification checklist or sufficient guarantee. Label: illustrative example / course synthesis.

## Generated-figure record
No new empirical redraw is required. Prefer source crops with enlarged external keys. If slides instead generates a chart from source numbers, append a new evidence entry before final acceptance with the source table, exact rows/columns/denominator/units, plotting transformations, uncertainty treatment and repo-relative reproducible generator path. Retained illustrative S06 curve follows E02. A causal teaching schematic must say illustrative and must not invent empirical values.
