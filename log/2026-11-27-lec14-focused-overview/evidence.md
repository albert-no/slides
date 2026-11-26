# Evidence register — focused overview

Survey cutoff: 2026-11-27. Primary papers, author reports, reproduction and mitigation work; this is a focused survey for topic selection, not a claim to exhaust the field. Version dates below are publication/revision dates, not necessarily experiment dates. Append-only: later verification/corrections get new IDs. The plan is not evidence.

## E01 — baseline and continuity
- Claim: the baseline main lecture has 51 slides across six sections, plus 51 note articles and a 14-slide technical supplement. Existing mode is 90-minute, concept-first, no activities.
- Source: git `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`, `courses/trustworthy-ai/OUTLINE.md`, lecture index and `## lec14-agentic-threats.html`; paired deck/notes. The plan includes the exact baseline page/ID/title map.
- Prior teaching: lec07 covers alignment failures, reward hacking and alignment-faking studies; lec13 covers prompt injection and permission boundaries. Recall these ideas, not their entire studies. Subliminal learning is not an existing lec14 block.
- Label: illustrative example / curricular inventory. Not an empirical claim about AI.

## E02 — delegation in a bounded real setting
- Claim: Project Vend exposed practical failures of a shopkeeping agent, including below-cost pricing.
- Source: Anthropic, “Project Vend: Can Claude run a small shop? (And why does that matter?)”, 27 June 2025, https://www.anthropic.com/research/project-vend-1 ; setup, Figure 2 architecture, “Claude's performance review” / “Selling at a loss”.
- Setup: Claude Sonnet 3.7, about a month in an office shop; Andon Labs did physical work and served as experimental wholesaler; the experimental email tool was not general real email. Real transactions, bounded environment.
- Does not establish: failure rates in all businesses, unsupervised real-world autonomy, or deliberate deception.
- Label: published result (author experiment report). Main anchor; existing S52 photo may be reused with its provenance.

## E03 — improvements are not a clean causal comparison
- Claim: phase two improved business performance but retained weaknesses and human purchase approval.
- Source: Anthropic, “Project Vend: Phase two”, 18 December 2025, https://www.anthropic.com/research/project-vend-2 ; “The numbers”, “What changed?”, “What actually worked?”, “What went wrong”.
- Setup: model upgrades, tools, instructions and architecture changed together; no clean phase boundary. Net-worth figure records the combined history.
- Does not establish: one upgrade caused the improvement, adding agents solved safety, or purchases became unconditionally autonomous.
- Label: published result (author experiment report). Pair with E02 so the story is neither a universal failure claim nor a claim of a solved problem.

## E04 — emergent misalignment is background, not a new survey block
- Claim: narrow fine-tuning can alter behavior well beyond the trained task.
- Source: Betley et al., “Training large language models on narrow tasks can lead to broad misalignment”, Nature 649, 584–589, 14 January 2026, https://doi.org/10.1038/s41586-025-09937-5 ; accessible full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12804084/ ; Fig. 1, “Finetuning on insecure code induces emergent misalignment”, educational-context control. Prior ICML 2025 version: https://proceedings.mlr.press/v267/betley25a.html . Use venue-specific author order, not mixed author lists.
- Setup: deliberately insecure-code training and off-task evaluations; context and model matter. No headline percentage proposed.
- Does not establish: all fine-tuning is dangerous, ordinary code tuning inevitably causes misalignment, or malicious intent.
- Label: published result. One background example, not a fourth lecture topic.

## E05 — original subliminal-learning result
- Claim: training on teacher-generated data without visible trait content can change the learner's later responses.
- Source: Cloud et al., “Language models transmit behavioural traits through hidden signals in data”, Nature 652, 615–621, 15 April 2026, https://doi.org/10.1038/s41586-026-10319-8 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC13083239/ . Fig. 1 overview; Fig. 2 experiment; Fig. 4a–b preferences; Fig. 3a misalignment; “Limited cross-model and in-context transmission”; “Limitations”. Publication and full-text sections checked; primary text also accessible by direct HTTP.
- Setup: prompted owl-preferring GPT-4.1 nano teacher, filtered numbers, fine-tuned student, neutral evaluation questions and control training. Harm-related experiments use a different, insecure-code-tuned GPT-4.1 teacher. Keep these separate. “Preference” means response frequency, not feelings.
- Limits: matched-model dependence, restricted experiments; not universal cross-model transfer, deployment prevalence, or deliberate hidden messaging. The in-context tests did not reproduce the fine-tuning effect.
- Label: published result. Main source; use final Nature figure numbering. Original 2025 account https://alignment.anthropic.com/2025/subliminal-learning/ and https://arxiv.org/html/2507.14805v1 are contextual, not interchangeable figure editions.

## E06 — Albert's suggested paper: feedback can also transmit behavior
- Claim: a teacher can transfer misalignment while scoring the student's own generated tokens, without supplying teacher-written training answers.
- Source: Askin, Ustaomeroglu, Nayak, Joshi, Qu, Joe-Wong, “Examining the Impact of Data and Training Methods on Emergent and Subliminal Misalignment”, https://arxiv.org/html/2605.12798v2 ; v2 10 November 2026, §2, §4.1, Table 1, Appendix E.2.4/Table 10, Appendix F. Metadata https://arxiv.org/abs/2605.12798v2 .
- Setup: same-base-model teachers/students; three 7B–14B open-weight model families; adapter training; model-judged evaluations. Teacher log-probabilities guide student-generated tokens. The additional online filtering experiment did not remove transfer in the tested setting.
- Limits: preprint; these models, datasets and judges, not general deployment rates. Ordinary scalar human feedback is not what was tested. No training-loss derivations or method ranking needed in main.
- Label: published result (preprint). Main recent extension.

## E07 — response directions, not a safety certificate
- Source: Askin v2 (E06), §4.2/Fig. 5 and Appendix E.3: aligned-teacher training reduced measured misalignment toward base-model levels in tested models.
- Main use: motivate teacher provenance and post-training evaluation as practical implications; no claim of guaranteed repair. Detailed comparisons stay optional in notes.
- Label: published result (preprint); deployment advice explicitly an inference.

## E08 — independent reproduction narrows the scope
- Claim: open-weight animal-preference transmission was reproduced, but extensions varied substantially by model, trait and task.
- Source: van der Weijden, Brack, Báez Santamaría, “Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models”, https://arxiv.org/html/2609.12586v1 , 11 September 2026, §2, §4.1/Fig. 1, §4.2/Fig. 2, §5. Metadata reports acceptance at BlackboxNLP@EMNLP 2026; venue listing not independently confirmed in this pass, so versioned preprint citation is sufficient until stage 4.
- Setup: preference traits, number/chess continuations, Qwen/Gemma/Ministral. This does not independently reproduce broad harmful misalignment.
- Label: published result (preprint inspected). Main qualifier/notes, not a separate results block.

## E09 — mitigation work does not yet establish a general harm remedy
- Claim: early regularization reduced selected preference/style transfer in tested settings.
- Source: Yanagisawa et al., “On Mitigation of Subliminal Learning in Large Language Models”, https://arxiv.org/html/2609.22215v1 , 2 September 2026, §3–4; limitations “Experimental scope”, “Traits studied”, “Baselines and side effects”. Metadata reports Findings of EMNLP 2026 acceptance; use inspected preprint until venue verified.
- Setup: small open-weight models, number sequences and math-reasoning data; mostly animal preferences plus French response style.
- Essential limitation: the authors did not reliably induce subliminal misalignment, so their experiments do NOT demonstrate that the method prevents misalignment or deception. Broader safety side effects were not comprehensively measured.
- Label: published result (preprint inspected). Optional notes only; do not add another technical method to the lecture.

## E10 — a tempting categorical counterclaim is under revision
- Claim: do not teach “subliminal learning is only a LoRA artifact” as settled.
- Source: Nief et al., https://arxiv.org/abs/2606.00831v2 , v2 8 September 2026, current author Comments field: follow-up work has shown some main claims incorrect and a substantial revision is being prepared. Checked 2026-11-27. Abstract has not been correspondingly rewritten.
- Limits: this notice does not by itself establish every proposed alternative mechanism or universal transfer. No rebuttal result is adopted on its strength alone.
- Label: unresolved. Research caution in notes, not a sensational additional main-slide debate.

## E11 — control tests a system, not a model's professed intentions
- Claim: selective auditing improved resistance to the best attacks found in a bounded coding game.
- Source: Greenblatt, Shlegeris, Sachan, Roger, ICML 2024, https://arxiv.org/html/2312.06942v5 (23 July 2024), §2, §3.1.2–3.2, Table 2, Fig. 1 right panel; §5.1 limitations.
- Setup: GPT-4 worker, GPT-3.5 trusted monitor, protected GPT-4 simulated high-quality audit; 5,000 problems, 2% audit budget. Whole-run no-backdoor probability: upfront-only auditing 15%, trusted monitoring 62%. Not per-task accuracy. Normalized usefulness need not be on the main slide; retain its definition and values in notes.
- Limits: trusted is an assumption, “human” audit was simulated, red team supplied attacks, not spontaneous model intent or a universal safety guarantee. Earlier attack strategies already sought favorable opportunities.
- Label: published result. Main one-comparison result. Existing reproducible bars/provenance at `courses/trustworthy-ai/figs/lec14-finale-refresh/p4-gen-s40-bars.py` may be adapted by slides; if redrawn differently, record exact inputs/transforms/code before acceptance.

## E12 — one recent limit on control
- Claim: selecting when to begin or abort an attack reduced measured conditional safety in two tested agentic environments.
- Source: Ge-Wang et al., https://arxiv.org/html/2606.06529v1 , 3 June 2026, Fig. 1 A–B, §3–4, especially §4.4, Appendix A.
- Setup: BashArena/LinuxArena; chosen start/stop policies, cross-validated selection; stop policy applied post hoc. Keep main qualitative.
- Limits: effect-size upper-bound methodology, small samples under strong selection, not a deployment rate. Do not compare its conditional statistic numerically with E11's whole-run measure or call every earlier attacker indiscriminate.
- Label: published result (preprint). Two-slide setup/result coda, not another protocol survey.

## E13 — practical recommendations and closing synthesis
- Claim: permission limits, checks before consequential actions, post-training behavioral evaluations, source tracking and stopping mechanisms are sensible questions for a system designer, not a sufficient certificate.
- Source: curricular synthesis of baseline lec01, lec07, lec13 and E02–E12. Specific hypothetical shop controls are illustrative recommendations, NOT interventions causally tested in Project Vend. Learning-time safeguards and runtime controls address different failure routes.
- Label: illustrative example / explicitly identified inference. Keep assumptions and remaining uncertainty visible.

## Figure/provenance boundary
No generated or modified figure is commissioned at the approval stage. Preferred candidates: Vend source photo/architecture and phase-two history; final Nature Cloud Figs. 1/2/4a/3a; final Nature Betley Fig. 1; one Askin qualitative setup, with any empirical redraw tied to its exact table and metric; Greenblatt Fig. 1 and Table 2; Ge-Wang Fig. 1 A–B. Stage 4 will select complete readable panels and list regeneration paths for any numerical redraw. No invented values, guessed intervals, rewritten screenshot text, or unlabeled illustrative data.

## E14 — precise precursor locator
- Clarifies E04's section locator: the Nature paper's actual heading is “Overview of emergent misalignment findings”, alongside Fig. 1 and the Main text, not “Finetuning on insecure code induces emergent misalignment”. The claim and chosen version remain unchanged. Full-text headings verified by direct HTTP.
- Label: published result / citation correction.

## E15 — final Nature figure/measurement verification for construction
- Supplements E05; final published text and captions re-read by direct HTTP from https://pmc.ncbi.nlm.nih.gov/articles/PMC13083239/ . Figure 4a is animal preference through numbers; teachers/students use GPT-4.1 nano. Baselines: unfine-tuned learner, regular-number training, and other-target-number training. Preserve the selected target's controls and uncertainty. Figure 4 intervals use five training runs; do not import the preprint's three-run description.
- Figure 3a is the separate GPT-4.1 misalignment-through-numbers experiment: insecure-code teacher versus untrained, secure-code and educational-insecure-code teachers, with the untrained student baseline. Five-run confidence intervals. The eight neutral-content evaluation questions also carry a formatting suffix; Figure 3b's caption describes the extra word/line-format instruction. Notes must give that suffix and avoid implying that absolutely no contextual formatting was supplied.
- Original Figures 1/2 are the preferred experiment visuals. Use complete source components or repeated source figures, not an invented alternative “canonical” setup. Figure 5's tested cross-model exception includes GPT-4.1/GPT-4o; different model names are not a safety guarantee.
- Label: published result. No exact chart values inferred by eye are commissioned.

## E16 — Askin table inputs and interpretation
- Supplements E06; https://arxiv.org/html/2605.12798v2 , §2, §4.1, Table 1, Appendix E.2.4/Table 10, Appendix F.
- Planned S74a source values: Table 1, Qwen3-14B, Avg column, SFT 27.1%, OPD 38.9%. Plain-language labels: teacher-written answers / teacher scores learner-generated tokens. Both are post-training, task-aggregated narrow-eval misalignment rates, not a baseline-vs-treatment plot, deployment frequency, or a universal training-method ranking. Full-vocabulary OPTD is not needed on main. Model-judge criterion in §2: alignment <30 and coherence >50; keep rubric in notes and “judge-rated” on the chart. Training-budget matching and per-method learning-rate selection matter.
- Planned S74b values: Table 10, Llama column, filtered OPD 39.6%, unfiltered OPD 39.3%. Three epochs; online Gemini-2.5-Flash filtering before updates. This is a different model/aggregation from S74a; never connect the bars across slides. These close reported values do not establish a significant difference or that filtering makes things worse.
- Repo regeneration path to be authored by slides: `courses/trustworthy-ai/figs/lec14-focused-overview/p2b-askin-bars.py`. Inputs exactly as above; separate zero-based percentage axes, no inferred uncertainty (these tables provide no intervals). Labels must preserve source meaning. Work report/provenance records final mapping and parameters. Source numbers published; charts a source-table redraw, not our empirical result.

## E17 — unchanged historical material transferred to backup
- Claim: backup material preserves the baseline's dated, scoped findings rather than silently dropping or updating them. Source of the exact inherited claim/figure/qualifier is git baseline `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`, paired lec14 main/notes and the prior approved record `log/2026-11-22-lec14-finale-refresh/evidence.md` (E01–E30). This is not a fresh latest-result survey of all backup topics.
- Primary locators retained with the material:
  - S08: Shevlane et al. https://arxiv.org/abs/2305.15324v2 , Table 1/§4: capability tests do not certify safety.
  - S09–S12/S88: Kwa et al. https://arxiv.org/html/2503.14499v4 , Fig. 1, §2–3, §5–6, App. C.3: dated task/scaffold/threshold-dependent horizons, not safe runtime. Retain cited METR 20 March 2026 modelling-assumptions note in inherited notes.
  - S54a/b: Becker et al. https://arxiv.org/abs/2507.09089 , Fig. 1, and METR “We are Changing our Developer Productivity Experiment Design” (24 February 2026): early-2025 experienced-developer trial and uncertain follow-up, not all developers/current effects.
  - S14–S15: https://arxiv.org/html/2504.18565v2 , Fig. 1, §5.1/§6: sandboxed components, no demonstrated full replication chain.
  - S17–S19/S22: Meinke et al. https://arxiv.org/html/2412.04984v2 , §2–3, Tables 1/2/4/6, §3.6: constructed goals/threats and observed behavior, not deployment rates or proof of intent.
  - S20–S21: van der Weij et al. https://arxiv.org/html/2406.07358v4 , §2/Fig. 4, ICLR 2025: instructed underperformance, refusals excluded; no erased knowledge.
  - S25: Hammond et al. https://arxiv.org/abs/2502.14143 , Fig. 1: conceptual goal-based taxonomy, not frequency data.
  - S27–S28: Cemri et al. https://arxiv.org/html/2503.13657v3 , Fig. 1/§4: MAST traces/frameworks, chess example; failure shares not deployment rates.
  - S29/S31: Lee & Tiwari https://arxiv.org/html/2410.07283v1 , §5/Figs. 2/4/6: simulated apps/town, environment-specific memory manipulation, no real outbreak.
  - S33: Motwani et al. https://arxiv.org/html/2402.07510v5 , §3/5–6/Table 3, NeurIPS 2024: limited tests through GPT-4; distinguish covert signaling from visibly encoded messages.
  - S55: Salvi et al. https://pmc.ncbi.nlm.nih.gov/articles/PMC12367540/ , Fig. 1/results; correction https://pmc.ncbi.nlm.nih.gov/articles/PMC13683042/ (3 September 2026): direct personalization contrast not significant; immediate controlled debate outcome, not durable real-world persuasion.
  - S56: Fang et al. https://arxiv.org/html/2503.17473v2 , Figs. 1/6 and limitations: voluntary-use associations, no no-chatbot control, not causal effects of usage duration.
- Label: published results retained as dated historical snapshots; S06/S87 and pedagogical scope diagrams remain illustrative/our calculation, not measurements. If slides substantively changes an inherited empirical claim, it must return for source verification rather than treating this transfer record as authority for the new claim.

## E18 — control result construction and denominator
- Supplements E11; https://arxiv.org/html/2312.06942v5 , §2.4–2.5, Table 2, §3.1.2–3.2. Whole-run safety estimates for a simulated 5,000-problem game are based on a smaller generated-response pool and resampling. Not 5,000 independent real-world deployments. First ten free audits and estimation assumptions belong in notes; audit H remains simulated and protected.
- Main S40 redraw inputs: upfront auditing safety 15%; trusted monitoring safety 62%. Same two rows' normalized usefulness 100%, 97% remain in the backup and notes, not relabelled accuracy. New generator path for main-only safety chart: `courses/trustworthy-ai/figs/lec14-focused-overview/p3-control-bars.py`; zero-based common percentage axis, exact two source values, no invented intervals.
- Backup S89 retains the accepted original two-panel chart/generator unchanged. The earlier monitoring attack policy already selected good backdoor opportunities; do not claim Ge-Wang discovered selectivity absent from every prior study.
- Label: published result / source-table redraw with exact inputs.

## E19 — inherited generated-figure provenance
- S06 calculation: n=0…20, p(n)=0.95^n, independent fixed step success, no recovery. Endpoint about 0.35849. Generator `courses/trustworthy-ai/figs/lec14-finale-refresh/p1-gen-curves.py`, accepted final X=80+25.5n, Y=295−255p. Label our calculation, not observed reliability.
- S09 curve is schematic, not fitted: same generator; x=110…1040 by 10, p=1/(1+exp((x−575)/70)), Y=270−230p; x denotes a schematic log-duration coordinate.
- S89 copies baseline S40's source-table bars: `courses/trustworthy-ai/figs/lec14-finale-refresh/p4-gen-s40-bars.py`; safety 15/62, usefulness 100/97; provenance `p4-PROVENANCE.md` in that folder. Preserve those assets/code so old and backup uses remain reproducible.
- Main hypothetical diagrams contain no numeric measurements. If any are added, label illustrative and record inputs/code as a new entry before review acceptance. Only slides authors figures/generators.

## E20 — approval and baseline-map clarification
- Albert approved stages 1–3 on 2026-11-27 01:04 KST with C08/C09: backup slides for removed material; more step-by-step main slides. This authorizes fuller presentation, not more topics or teaching time.
- Frozen plan-v1's baseline S51 map cell was empty because the closer uses a non-heading element; its actual visible text is “What would earn your trust?” at baseline page 51. The v2 specification retains this point. No source edit or ID change was made.
- Label: author decision / curricular inventory, not empirical research.

## E21 — lec01–lec13 overlap audit at the frozen baseline
- Source: all thirteen main lecture files at `7d9f51efdd5038ab2e438f783ec395ed9e8c1297`, under `courses/trustworthy-ai/`; leaf OUTLINE and directly inspected HTML. Audit method: inventory all 974 slides by title/topic, then close-read overlapping slides and relevant note passages. This is a curricular audit, not a new factual endorsement of every older claim or a visual review of those decks. The older decks remain read-only scope.
- Counts in lecture order: 46, 69, 70, 65, 68, 75, 75, 101, 91, 88, 74, 87, 65. Page numbers below include title, dividers and closer; line numbers point at slide starts in the frozen HTML.

| Earlier deck | Already taught / representative exact location | Implication for lec14 |
|---|---|---|
| `lec01-introduction.html` | p4/S04 L106 task horizons; p21/S21 L458 injection; p25/S25 L551 wrapper-dependent scheming; p32/S32 L699 trust dimensions; p38–40/S38–S40 L851–915 threat models | Do not repeat the incident/capability catalogue, general threat-model lesson or multi-slide trust stack. One final course synthesis is intentional. |
| `lec02-privacy-dp.html` | p39/S39 L814 distributional distinguishability; p61/S61 L1193 DP synthetic data | Synthetic training data is not a brand-new category. Subliminal transfer is a different behavior question, not a claim that a DP guarantee fails. No DP refresher. |
| `lec03-mia.html` | p51/S51 L1119 attack-based auditing; p67/S67 L1402 defender checklist | Do not reteach generic attack-as-audit or detection denominators. Control's whole-run outcome needs its own specific explanation. |
| `lec04-memorization.html` | p16/S16 L378 learning versus memorizing; p51/S51 L934 limits of deduplication | Hidden behavior transfer is not exact-record copying. No memorization/extraction recap or claim that removing visible words proves a clean learning signal. |
| `lec05-unlearning.html` | p8/S08 L209 information in weights; p48/S48 L1100 unlearning versus output filtering; p51/S51 L1161 audit limits | Generic weights-versus-output-filter primer is redundant. Askin's training-time response filter is not this runtime output filter or an unlearning method. |
| `lec06-hallucination.html` | p4/S04 L80 fluency is not factual grounding; p48–50/S48–S50 L716–751 scoped guarantees and deferral | Avoid another fluency/error/hand-off lecture. Keep only a single finale recap and study-specific limits. |
| `lec07-alignment-failures.html` | p4–5/S04–S05 L97–107 alignment and capability; p46–55/S46–S55 L569–679 MacDiarmid reward-hacking-to-misalignment study; p68/S68 L836 monitor limits; p71–72/S71–S72 L868–889 synthesis | Broad emergent misalignment and monitoring limits are already taught in depth. Betley is a brief, different insecure-code precursor needed to explain the new teacher/learner experiment, not another full emergent-misalignment section. No reprise of MacDiarmid, alignment faking or chain-of-thought monitoring. |
| `lec08-adversarial.html` | p29–36/S29–S36 L364–451 non-robust features and training on visually misleading images; p61/S61 L737 stronger attacks; p81/S81 L960 certificate scope | Humans missing a learned signal is not a new general idea. Cloud's contribution here is cross-model behavior transfer via numeric training data. Do not assert that Ilyas' mechanism proves the explanation of Cloud. Avoid repeating the generic adaptive-attacker tutorial. |
| `lec09-poisoning.html` | p14/S14 L190 poisoning versus backdoor; p34/S34 L404 hidden conditional behavior; p73–75/S73–S75 L854–888 Sleeper Agents installation/persistence | No BadNets/Sleeper Agents tutorial. Distinguish a malicious condition in generated code (control experiment) from a trained-in trigger in the model. Subliminal transfer need not involve an attacker poisoning a corpus. |
| `lec10-jailbreak.html` | p28–30/S28–S30 L363–389 fine-tuning safety; p47/S47 L584 in-context learning, unchanged weights; p80–85/S80–S85 L995–1057 self-assessment, teacher labels, blind spots | Generic prompt-versus-training slides repeat known content. OPD is a new channel: teacher token probabilities, not the earlier teacher's verdict labels. Control is a bounded adversarial workflow experiment, not another generic monitor introduction. |
| `lec11-synthetic-media.html` | p10–11/S10–S11 L155–163 origin versus truth; p61/S61 L795 signed C2PA record | Training provenance here means teacher/model/training-process history, not media authentication. No watermark/C2PA refresh. |
| `lec12-fairness.html` | p10/S06 L253 data/target/feedback; p14/S10 L398 removing a column need not remove information; p84–85/S54a–S54b L2329–2368 case-specific synthesis | No new proxy/bias tutorial. Similar-looking hidden-information lessons do not establish the same mechanism or a fairness claim about subliminal learning. |
| `lec13-prompt-injection.html` | p4/S04 L110 agent definition; p14–15/S11–S12 L275–306 permission/agent loop; p52–60/S43–S48 L1588–1859 CaMeL, dual LLM, least privilege, approval; p63–64/S51–S52 L1913–1943 limits and synthesis | Strongest overlap: agent/tool definitions, approval and permission principles. Reuse them briefly in the shop case; do not re-teach injection incidents, permission taxonomies, dual-LLM/CaMeL architectures or generic approval checklists. |

- Relevant notes checked: lec07 Study 2 notes around L950–1145 (separate classifiers and Betley evaluation reference); lec13 notes around L1219–1375 (policy-permitted exceptions, approval information and fatigue). A reference to Betley as an evaluation does not mean that Cloud's subliminal-transfer experiment has already been taught.
- Main/notes/tech text search found no earlier taught Cloud/Askin/Project Vend/Greenblatt **AI-control** study. Greenblatt's alignment-faking paper in lec07 is a different study. This supports retaining those specific case studies, not claiming every underlying concept is new.
- Label: curricular inventory; prior-deck contents are evidence of coverage, not independent scientific evidence for new claims.

## E22 — redundancy decisions and boundaries of the new lesson
- Source: C11, the E21 exact-baseline inventory, and comparison of plan-v2's title/point/exhibit sequence. Plan-v3 is the curricular response; primary scientific authority remains E02–E19.
- Move four generic standalone main targets to actual backup slides with paired notes: S13 (capability versus delegation), S62a/S62b (context versus weight updates), S79 (a generic stopping-authority recap). Their needed prerequisites become brief self-contained Recall statements within the relevant study setup; no important qualifier is deleted.
- The other potential repeats are adapted to ask new, case-specific questions: Vend errors without requiring an injected command; ordinary authorization versus sound commercial judgment; Cloud's separate teacher, data, student and later evaluation; numeric transfer versus deliberate poisoning; Askin's token-score feedback versus verdict-label distillation; code-output backdoors versus model backdoors; protected-audit control versus self-assessment or CaMeL.
- Retain setup/method/score/result/limitation slides when they teach different steps of the same new result. Reusing an exhibit to reveal a new causal or evaluation step is not automatically redundancy. Conversely, changing only a diagram's icons does not make an old generic lesson new.
- Main remains three topics / 90 minutes, target 59 slides after four moves, versus v2's 63 and baseline 51. Backup target rises 43→47. No substantive result is removed, no new paper is added, no font shrink or compression is requested. Reallocated minutes support reading the novel experiments, not additional topics.
- Label: author-directed curricular/design judgment, not empirical result.

## E23 — round-1 check: Cloud's two outcomes and retained answers
- Supplements E05/E15. Primary final article re-read: https://pmc.ncbi.nlm.nih.gov/articles/PMC13083239/ , Nature DOI 10.1038/s41586-026-10319-8, Fig. 3a, “Transmission of misalignment”, Methods evaluation/grading paragraphs.
- Fig. 3a contains two different outcomes: free-form judged misalignment on the left and TruthfulQA false-answer frequency on the right. A single key calling both outcomes “answers judged misaligned” is incorrect. Main S70 will concentrate on the left outcome; preserve the complete panel a in optional backup.
- Free-form evaluation uses eight question contents with the stated formatting suffix. Alignment below 30 is classified as misaligned; answers with coherence below 50 are discarded. Explain the retained-answer population, not a rate over all possible answers or deployment harms. The paper's text says almost 10%, while the plotted mean is nearer 0.08; do not redraw an exact 10% bar. Five runs and the reported intervals remain source-specific.
- Label: published result; correction of incomplete on-slide metric descriptions, not a new result.

## E24 — round-1 check: attack-selection denominator
- Supplements E12. Primary source https://arxiv.org/html/2606.06529v1 , equation 1 and Appendix A.3, re-read at review.
- Empirical safety is caught / (caught + successful uncaught attacks). Attempts that neither succeed nor are caught are excluded. Stop-policy aborts are treated as indecisive and leave this denominator. Thus “share of attempted attacks caught” is not an adequate plain-language definition, even when the displayed formula is correct.
- This is a decisively ended-attack catch ratio, not whole-run safety or deployment frequency. The existing post-hoc-stop, small-sample and upper-bound qualifiers remain necessary.
- Label: published result (preprint); no new calculation.

## E25 — round-1 independent check of optional subliminal-learning sources
- Confirms E09 from the paper body, rather than relying on this register: https://arxiv.org/html/2609.22215v1 , Limitations, “Experimental scope”, “Traits studied”, “Baselines and side effects”. Number completion and math-reasoning experiments; mainly animal preferences and one French-style experiment; harmful misalignment could not be reliably induced; broader safety side effects not comprehensively measured. Evidence supports selected preference/style mitigation, not prevention of harmful transfer. Use versioned preprint status.
- Confirms E10 on https://arxiv.org/abs/2606.00831v2 , Comments field, checked 2026-11-27: authors report some main claims incorrect and a substantial revision being prepared. The still-visible categorical abstract is not a settled refutation. This is unresolved research context, not a new empirical result to teach in the main lecture.
- E08's primary body https://arxiv.org/html/2609.12586v1 was also inspected during review; retain its bounded preference/model/task scope, not an independent harmful-misalignment replication claim.
- Label: source verification; no new main-deck literature selected.
