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

## E20 — conversational persuasion beyond answer correctness
- Claim: profile-informed GPT-4 produced stronger shifts in agreement than the non-personalized human-opponent baseline in a controlled debate study.
- Source/version/locator: Salvi, Horta Ribeiro, Gallotti & West, Nature Human Behaviour 2025, corrected version of record; https://www.nature.com/articles/s41562-025-02194-6 ; accessible full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12367540/ ; “Experimental design”, Fig.1, Results / “Aggregate results”, Discussion.
- Setup: preregistered online experiment, 900 participants; opinion surveys before/after short debates. No headline percentage required.
- Limits: immediate stated agreement, not real-world voting or durable belief change. Personalization's separate contribution is not conclusively established (E21). Label: published result.

## E21 — substantive correction to the persuasion comparison
- Claim: the direct comparison of personalized and non-personalized GPT-4 was not statistically significant after correcting the reference-category calculation.
- Source/version/locator: Salvi et al., Author Correction, 3 Sep 2026, https://www.nature.com/articles/s41562-026-02588-0 ; complete substantive correction also at https://pmc.ncbi.nlm.nih.gov/articles/PMC13683042/ .
- Setup: corrected P=.0678 (rounded .07), replacing .04; applies to that specific contrast.
- Limits: not a retraction; does not remove the personalized-GPT-4 versus human-baseline finding. Do not attribute the advantage solely to personalization. Label: published result (correction).

## E22 — human–AI relationships and emotional dependence
- Claim: greater voluntary use was associated with worse psychosocial outcomes in a four-week chatbot study; the duration relationship does not establish causation.
- Source/version/locator: Fang et al., https://arxiv.org/html/2503.17473v2 (2 Oct 2025); abstract; “More Time Spent with Chatbot is Associated with Worse Psychosocial Outcomes and Mediates Effects of Modality and Conversation Types”; Figs.1/6; limitations.
- Setup: 981 participants, GPT-4o; randomized modality/conversation type, not usage duration. Four outcomes: loneliness, human socialization, dependence, problematic use.
- Limits: no no-chatbot control; US English-speaking sample and short follow-up. Do not infer that use causes loneliness, all companions harm users, voice is categorically safer, or a clinical treatment effect. The v2 abstract says no significant condition effects; body contains marginal unadjusted contrasts, so do not build a categorical condition-ranking headline. Label: published result (preprint).

## E23 — novelty check for C06
- Claim: these two introductions extend the taught course from system/data/output/action risks to influence on users and longer-term human–AI relationships.
- Source/locator: baseline34b40ca course lecture index and lec01–lec14 main-slide content; optional backup-sycophancy is not one of the 14 taught lectures.
- Setup/limits: conceptual extension, not a claim that no earlier sentence mentioned social consequences. Do not re-teach sycophancy or synthetic-media detection. Label: illustrative example / curricular synthesis.

## E24 — generated teaching curves, round-1 provenance
- Claims/labels: S06 is **our calculation**, not measured reliability; S09 is an **illustrative example**, not a fitted empirical curve. This supplements E02/E07.
- Repo generator: `courses/trustworthy-ai/figs/lec14-finale-refresh/p1-gen-curves.py`.
- S06 inputs: n=0…20, p(n)=0.95^n, fixed independent success and no recovery; endpoint 0.3584859224. Reviewed inline geometry uses X=80+25.5n and Y≈295−255p. The generator currently emits Y=340−300p; the slide was subsequently compressed around Y=40 by factor .85. Algebra and direction are correct, but the generator does not reproduce the final coordinates. F07 requires bringing the generator/comment/provenance into agreement; do not alter the probability model.
- S09 inputs: x=110…1040 by 10, p=1/(1+exp((x−575)/70)), Y=270−230p; x is a schematic log-human-duration coordinate, not observed hours. The emitted path exactly matches S09 in the reviewed commit.
- Limits: neither curve supplies empirical agent failure rates or deployment safety.

## E25 — generated S40 comparison, round-1 provenance
- Source: Greenblatt et al., ICML 2024, [arXiv v5 Table 2](https://arxiv.org/html/2312.06942v5), rows Upfront auditing and Trusted monitoring. Published result, redrawn from table.
- Inputs: safety 15%, 62%; usefulness 100%, 97%, respectively. Safety is no submitted backdoor over a 5,000-problem run against the best attack found; usefulness is correctness normalized between GPT-3.5 and GPT-4. Audit budget 2%. Not accuracy or deployment reliability.
- Repo generator: `courses/trustworthy-ai/figs/lec14-finale-refresh/p4-gen-s40-bars.py`; provenance `p4-PROVENANCE.md` in the same folder. Separate panels, zero-based linear scales: 2.9 viewBox units per percentage point, starts X=300/680, row tops Y=62/142, bar height52. No uncertainty added because the table does not report it. Generator SVG and reviewed inline SVG match after XML normalization.

## E26 — S55/S56 source figures, accepted provenance
- S55: E20/E21; Salvi et al. Fig.1, experimental design, not result data. Full original [publisher image](https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41562-025-02194-6/MediaObjects/41562_2025_2194_Fig1_HTML.png). Asset `courses/trustworthy-ai/figs/lec14-finale-refresh/p5-salvi-fig1.png`, 1531×1089; SHA256 `f13eee21693efbda403a853282280e3c517ae71fc2e06b771f791758a84601f9`. Published source figure, CC BY4.0; unmodified, external a–c key. The September2026 correction concerns the contrast interpretation, not this design image; its limitation is visible on S55.
- S56: E22; Fang et al. v2 Fig.1, conceptual study framework, not result data. Full original [arXiv image](https://arxiv.org/html/2503.17473v2/Figures/OpenAI-teaser-4.png). Asset `courses/trustworthy-ai/figs/lec14-finale-refresh/p5-fang-fig1.png`, 2174×722; SHA256 `79306e4e2403f6074f5a9acdcd67aa6595c490bfc77230218dfce211ab79e137`. Published preprint figure, CC BY4.0; unmodified, four large outcome labels external. Duration was voluntary, not randomized; no no-chatbot group. Figure6 is deliberately not used.
- Exact capture details: repo `courses/trustworthy-ai/figs/lec14-finale-refresh/p5-PROVENANCE.md`. Both are accepted for the short high-level previews; not evidence for causal personalization or causal psychosocial harm.

## E27 — carried note-only claims checked in round 1
- Morris-II: [Cohen et al. v2](https://arxiv.org/html/2403.02817v2), abstract, §I ethical considerations and §V. TPR1.0/FPR.015 are the authors' guardrail results, not universal robustness; experiments used their own lab email-assistant application, not attacks on deployed applications. Bug-bounty disclosure is explicit. Published result (preprint); retain note-only.
- Lynch: [v2](https://arxiv.org/html/2510.05179v2), abstract and §1. Sixteen models, constructed corporate dilemmas, no real-deployment evidence claimed. Published result (preprint); retain note-only.
- Terekhov: [v2](https://arxiv.org/abs/2510.09462v2), abstract. Monitor-output attacks and Defer-to-Resample amplification are supported in the studied settings; not all imaginable control protocols. Supplements E17.
- RepliBench's simulation/refusal/termination limits remain supported by the pinned v2 §6 in E08; no fresh field-wide assertion is authorized.

## E28 — correct Motwani's publication/date framing
- Supplements E14. [Official NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/861f7dad098aec1c3560fb7add468d41-Abstract-Conference.html) confirms **NeurIPS 2024**, main conference. [arXiv v5](https://arxiv.org/html/2402.07510v5) is a July2025 revision, not evidence that experiments occurred in2025.
- Table3 and AppendicesG/H support the separate capability results retained in notes. Label: published result. Use venue2024 with inspected version/date separately; replace claims of “2025 tests” with an undated, model-cohort-scoped description. No claim about later models or deployment prevalence.

## E29 — control comparisons must keep their distinct scope
- Supplements E15/E16. [Greenblatt v5](https://arxiv.org/html/2312.06942v5), §1, §3.1.1, §3.2 and Table2: the trusted-monitoring attacker already seeks favorable backdoor opportunities. Do not describe every prior protocol as indiscriminate. Its no-U baseline uses H for the first2% and T afterwards; “T only” is not that 2%-usefulness point.
- [Ge-Wang v1](https://arxiv.org/html/2606.06529v1), §2–3, Fig.1 and App.A: the new high-level contrast is task-level start and turn-level stop selection in multistep agentic tests. Do not confuse this conditional safety estimator with Greenblatt's whole-run probability, or say selection is untested after presenting these tests.
- Labels: published results (Ge-Wang preprint). Each result has its own task/attacker/budget envelope; a change beyond one evaluation may already have been tested in another, without establishing deployment safety.

## E30 — round-2 closure of generated geometry and source crop
- Exact reviewed commit: `58e37fdf517799b978f042551f56c9c5dd7713ef`.
- E24's S06 reproducibility discrepancy is resolved: the repo generator now uses X=80+25.5n and Y=295−255*(.95**n); its emitted path exactly matches the inline slide. Endpoint remains0.3584859224. S09 still matches its unchanged generator. Labels remain our calculation / illustrative example, not empirical agent measurements.
- S54a source image rechecked directly against [METR's original chart](https://metr.org/assets/images/downlift/forecasted-vs-observed.png). The tick's final non-background row is1422, now retained. The documented adjacent category-label omission lies below the plotted data; points/error bars are retained, with category names supplied externally. Accepted crop-only assembly; no inferred/repainted data. Repo capture record is `courses/trustworthy-ai/figs/lec14-finale-refresh/p1-PROVENANCE.md`.
- E28/E29 corrections now appear consistently in the main slide, notes and affected citation/outline entries. No new empirical claims introduced in round2.
