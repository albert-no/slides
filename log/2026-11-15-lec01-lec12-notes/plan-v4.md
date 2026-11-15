# Plan v4 — bounded correction pass after Albert's go-ahead

## What changed since v3
Albert's direct “go ahead” in #claw-slides-review, 2026-11-15 15:24 KST (C09), authorizes continuing after the final r3 escalation. This is **one additional implementation/review pass, work-r4/review-r4**, not approval of the current content, an unlimited round reset, or permission to merge.

Resolve the **13 blocking groups** in frozen review-r3: F34, F69, F70, F73, F74, F78, F79, F80, F81, F85, F93, F97, F101. They touch **22 distinct main/note pairs**, not all 1,006 entries. Retain completed work; do not repeat the broad rewrite or audit. The 21 nonblocking groups stay nonblocking, with source-precision repairs preferred and visual preferences left to slides. Exact current-text → correction instructions and reviewed-commit line locators in review-r3 are incorporated below, not silently revised.

Correct earlier planning mistakes rather than reproduce them: v3 M11 omitted the pure-DP condition; M16's qualitative main does not validate its retained theorem; M37's three targets are not a strict implication chain; the lec06 medical illustration does not identify an internal mechanism; lec14 handcrafted attacks are not necessarily non-adaptive. F101 also repairs the earlier-missed lec01 repetition of the HF duration error. This plan supersedes inconsistent v1–v3 seeds at the named locations; frozen files remain unchanged.

## Scope, baseline and authority
- Job/branch: `2026-11-15-lec01-lec12-notes`, **same branch and one eventual PR**. Size remains medium: existing arguments, no new lecture or literature survey.
- Original baseline: `99450923b41e94f10d0c557a4fc0f46b42a9c91d`.
- Incremental baseline and line/page reference for this order: **`ef453a8abd3d04449e71de1d61d9d9071e16f632`**, exact r3 reviewed commit. Record subsequent content commits; never compare against moving main.
- Existing ID commits: `853024d8077bc8faa290873d91019d108996d558` and extension `594ebea1203aabe3b3edc56443b37dd29950e411`. IDs already exist; no new ID pass or renumbering.
- Audience/mode: mixed-major undergraduate course, concept-first. Preserve the existing lecture arguments, sequence, core paths, per-slide minutes and teaching duration; no activities.
- Scope: named canonical main/note entries and their necessary same-claim repetitions, plus corresponding root/leaf outline synchronization. No backups, Korean auxiliary notes, technical supplements, other courses, figures directory, `reference/`, or scripts. If an essential repair truly needs an excluded surface, report a plan issue first. No new research topic or theorem is requested.
- The completed DESIGN_SYSTEM §9 instructor-note rule and PLANNER_BRIEF pointer remain. Do not rewrite either, or change agent instructions. DESIGN_SYSTEM §§1/5/6/8/9/10 govern implementation.
- Preserve existing counts as a target, not a readability constraint. A necessary split is allowed under the contract with stable split IDs, matching articles, updated maps and unchanged teaching time. Return any substantive argument/time change first.
- Copy frozen review-r3 unchanged into `log/2026-11-15-lec01-lec12-notes/` before implementation, together with this plan; refresh living files on pushes. Review-r3 SHA256: `bcc3ac9b61f73ec14eb7227b2eac0f909f9cde08e1d2111a65a25bef078a1d80`.

## Request coverage
| Comment | Baseline page/title or scope | Slide IDs / work | Package |
|---|---|---|---|
| C01 | lec01–12 notes | Retain 902 completed entries; named residual accuracy fixes only | P1–P6, P10 |
| C02 | Message → explanation → detail | Every changed entry: reconcile all layers, not just opening | All changed packages |
| C03 | Check all; actual provider-limit pause/resume | Prior broad review retained; checkpoint and pause only on a reported actual limit | Integrator |
| C04 | Render plots/check originals as needed | Changed entries and neighbours, source-sensitive claims below | All changed packages |
| C05 | lec13–14 remaining companions | Preserve 104 completed entries; F93/F97 required, local nonblockers optional | P13–P14 |
| C06 | Main-slide corrections lec01–14 | Named main claims and their notes; 22 required pairs below | P1–P6, P10, P14 |
| C07 | Notes-HTML design rule | Completed §9 and brief pointer retained; verify no regression | P15 |
| C08 | Same branch and PR | Existing job branch, one eventual PR after approval | Integrator/owner |
| C09 | “go ahead” after r3 escalation | 13 blockers, bounded work-r4/review-r4; optional items do not start another round | All changed packages |

## Source basis
Reuse the evidence register, original sources and saved review artifacts; this is not a new literature pass. Evidence IDs carry the setup, version, limitations and source locators. The plan is not evidence.

| Evidence | Source / locator needed here |
|---|---|
| E100 | Nasr et al., 2311.17035v1, [§5.4](https://arxiv.org/html/2311.17035): 15,000 tested attack generations; 16.9% PII, not ordinary-use risk. |
| E101/E103 | Dwork–Roth, [Definition 2.4, printed pp17–18](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf): pure vs approximate event bound. |
| E101 | Kirchenbauer et al. [2301.10226v4 §4.1](https://arxiv.org/html/2301.10226v4): repeated n-grams; Chouldechova [1703.00056v1 Eq.2.6](https://arxiv.org/html/1703.00056): nondegenerate fairness identity. |
| E104 | Abadi et al., 1607.00133v2, [§3.1 Theorem1/App.B](https://arxiv.org/html/1607.00133), plus the recorded exact Gaussian-tail counterexample. The local dp5 theorem is not independent evidence. |
| E91/E109 | Our finite-sampling counterexample: fair two-meaning model has positive population entropy and all-M agreement probability 2^(1−M). Existing sourced estimator in E82 stays accepted. |
| E110 | [GPT-5 System Card, Aug13 2025, §3.7/Table8](https://cdn.openai.com/gpt-5-system-card.pdf); [Sep5 2025 blog, Teaching to the test table](https://openai.com/index/why-language-models-hallucinate/): SimpleQA cross-model totals, not a reward ablation. |
| E111 | Yang et al., [2405.03162v1 Fig9 p28](https://arxiv.org/pdf/2405.03162v1); [Google Research May15 2024 blog](https://research.google/blog/advancing-medical-ai-with-med-gemini/); [Aug4 2025 firsthand reporting](https://www.theverge.com/health/718049/google-med-gemini-basilar-ganglia-paper-typo-hallucination). Output observed, mechanism/discovery delay not established. |
| E33/E112 | MUSE [2407.06460v2 §5.1/Fig5/Table3](https://arxiv.org/html/2407.06460v2), existing calibrated-audit evidence, and the retained-duplicate-fact counterexample. |
| E118 | Qi et al., [2406.05946v1 Table2/App.A.4](https://arxiv.org/html/2406.05946v1): model-specific GCG; top3 of10 selection. |
| E134 | Meinke et al., [2412.04984v2 abstract/Fig3/§3.2](https://arxiv.org/pdf/2412.04984v2): broader follow-up summary vs oversight-only subset. |
| E138 | Lee–Tiwari, [2410.07283v1 §5.1/Figs4–6](https://arxiv.org/html/2410.07283v1): failure-breakdown ambiguity and global-message data-theft exception. |
| E50/E115/E145/E146 | [HF July27 2026 technical timeline, introduction/TL;DR](https://huggingface.co/blog/agent-intrusion-technical-timeline): campaign vs internal duration; E146 corrects the note locators. |

## Required slide-level corrections
All items below are **must**; proposed content/title choices are **[judgment]**, implemented with slide context by slides. The numbered F-item fixes in frozen review-r3 give exact current text, line numbers and reasons. Check the whole affected article and matching slide so retained Script, details, title, key, cite and alt do not contradict the repair. Prefer the smallest source-faithful repair; no formula, markup or layout is prescribed. Layout: retain the current exhibit/component unless the named factual correction or legibility requires adapting it. Time: preserve the entry's existing budget. Nothing moves into a tech supplement.

### 1. F69 — lec01 S12/p12, “Repeat the Word Poem Forever” — P1
Path: `courses/trustworthy-ai/lec01-introduction-note.html`, L244 (article L231).
- Point/title: retain the title and attack example; distinguish attack-generation prevalence from normal-use leakage.
- Required content [judgment]: retained denominator becomes **15,000 tested attack generations**, of which 16.9% contained PII verified against the auxiliary corpus; not outputs already flagged as memorized. Match the correct L242 wording; preserve ordinary-use and patch/erasure limitations.
- Exhibit: existing prompt → raw-text schematic, not a population-risk chart; no main redraw.
- Evidence: E100. Placement: note detail correction only.
- Acceptance: no remaining memorized-only denominator; main, Message and detail do not imply normal-use 16.9% risk.

### 2. F70 — lec01 S42/p42, “The Trust Stack” — P1
Path: `courses/trustworthy-ai/lec01-introduction-note.html`, L988–990/L1014–1017 (article L976).
- Point/title: retain course-map title; technical previews retain their actual hypotheses.
- Required content [judgment]: likelihood-ratio/privacy-loss bound is pure DP, delta=0; approximate DP uses additive event slack and composition tracks both parameters. Binomial watermark null is ideal independent membership, z uses a normal approximation, repeated n-grams require handling/calibration, and evidence is for this watermark. Fairness equal-PPV/error-rate claim needs nondegenerate shared PPV in (0,1) and nonzero TPR; preserve the separate Kleinberg statement.
- Exhibit: current course-layer map unchanged; these conditions belong in retained technical note detail, not a new intro lecture.
- Evidence: E101/E71. Acceptance: the rare-reveal DP and perfect-prediction fairness counterexamples no longer contradict the text; no universal AI-detector assertion.

### 3. F73 — pure/approximate DP consistency — P2/P3/P4
Point: preserve the existing DP story but make each guarantee match its assumptions. Retain current titles listed below. All changes [judgment]. These are reuse/adaptation of the already-taught DP definition, not a new definition deck or derivation.

| # | File paths, ID/page, current title and locators | Required content, exhibit reading and placement | Acceptance |
|---|---|---|---|
| 3.1 | `courses/trustworthy-ai/lec02-privacy-dp.html` S27/p27 “Plausible Deniability”, L557–585; `courses/trustworthy-ai/lec02-privacy-dp-note.html` S27 L540–550 | Label existing likelihood/posterior-odds illustration **pure DP with small epsilon** on main and note. Replace unconditional “No output can seriously contradict her” by limited evidence about participation from this release. Keep the stated adjacent-dataset comparison. | No strong deniability for large epsilon or every-outcome bound at positive delta. |
| 3.2 | `courses/trustworthy-ai/lec02-privacy-dp.html` S33/p33 “Reading epsilon”, L686/L701/L707; `courses/trustworthy-ai/lec02-privacy-dp-note.html` S33 L652/L655 | Scope epsilon-zero independence and every-outcome 2.7× example to delta=0; connected adjacency for dataset independence in the note. Existing epsilon-scale exhibit must carry the scope too. Preserve fixed unit/adjacency/delta/composition comparisons and no universal good epsilon. | Positive delta is not presented as dataset independence at epsilon0. |
| 3.3 | `courses/trustworthy-ai/lec02-privacy-dp.html` S36/p36 “What epsilon Does NOT Mean”, L767; `courses/trustworthy-ai/lec02-privacy-dp-note.html` S36 L715/L718 | Epsilon sets the multiplicative factor exp(epsilon); approximate DP also allows additive delta. Keep the misconceptions exhibit, remove “ratio ... nothing else.” | Parameter vs exponential factor and approximate slack are distinct in both layers. |
| 3.4 | `courses/trustworthy-ai/lec02-privacy-dp.html` S39/p39 “Overlap Is Privacy”, L820; `courses/trustworthy-ai/lec02-privacy-dp-note.html` S39 L753–769 | Existing overlap/likelihood picture is an explicitly pure-DP illustration. Preserve the technical approximate event bound and sufficient-tail lemma. | Note detail does not become an equivalence; main/opening do not hide the pure scope. |
| 3.5 | `courses/trustworthy-ai/lec02-privacy-dp-note.html` S41/p41 “Individuals, Not the Crowd”, L795 | Qualify retained exp(epsilon)-factor statement as pure DP, or state the full approximate event bound. Existing main and individual-vs-population exhibit remain. | Correct main incremental-influence lesson is not undone in details. |
| 3.6 | `courses/trustworthy-ai/lec03-mia.html` S49/p49 “DP Caps the Attacker”, L1086/L1089; paired `courses/trustworthy-ai/lec03-mia-note.html` S49 | Label ratio-only diagram pure DP (delta=0); scope “every output” likewise, or use a full event/attack-performance bound. Paired note's existing pure-diagram explanation is the consistency reference. | Approximate heading and ratio-only diagram are no longer conflated; essential scope visible on main. |
| 3.7 | `courses/trustworthy-ai/lec04-memorization.html` S53/p53 “Differential Privacy”, L995; `courses/trustworthy-ai/lec04-memorization-note.html` S53 L1011/L1014/L1026 | For the approximate-DP training result, event probability is bounded by exp(epsilon) times neighbouring probability **plus delta**. Add delta in the canary-null tail bound too. Retain actual DP/non-DP figure and zero-detected-extraction scope. | Not a pointwise ratio or claim that rare disclosures are impossible; already-correct L1014 retained. |

Evidence: E101/E103. F70.1 must use the same distinction. Technical proofs stay in notes; existing figures are not mathematical guarantees beyond the stated setup.

### 4. F74 — lec02 S57/p57, “More Data Helps” — P2
Path: `courses/trustworthy-ai/lec02-privacy-dp-note.html`, L1093/L1099–1102.
- Point/title: more data can improve the privacy–utility tradeoff under comparable accounting; retain the qualified main and title.
- Required content [judgment]: **use the bounded heuristic route**, not a replacement theorem project. Remove the unconditional sufficient-noise formula and exact “ten times data, one tenth noise” guarantee. Explain that the dependence on data size depends on sampling, steps and valid accounting; any retained scaling illustration must state its accounting-regime status and must not certify arbitrary T or the stated one-record setup. Cite Abadi's conditional theorem accurately rather than assert its constants cover this formula.
- Exhibit: existing signal/noise schematic is qualitative, no new measured curve. Placement: Reading and technical detail; no main expansion.
- Evidence: E104. Acceptance: E104's one-step counterexample is not claimed private by the revised text; no copied local theorem as proof. Report the out-of-scope dp5 issue in work-r4; do not edit that course. A different valid theorem would require returning source/setup conditions as a plan issue first.

### 5. F34 — lec06 S57/p57, “The Entropy Picture” — P6
Path: `courses/trustworthy-ai/lec06-hallucination-note.html`, L866.
- Point/title: sample agreement lowers an empirical estimate; it does not establish population certainty. Retain title and low/high-entropy exhibit.
- Required content [judgment]: all M samples in one cluster means empirical cluster frequency1 and plug-in entropy0, not population P(c|x)=1. Alternatively make the premise explicitly population mass1. Keep log-K limit and valid estimator elsewhere.
- Evidence: E91/E109/E82. Placement: retained definition; preserve repaired main and Scripts.
- Acceptance: fair two-meaning finite agreement no longer implies certainty; no new dispute of S56's sourced estimator.

### 6. F78 — lec06 S20/p20, “Guessing, Measured” — P6
Paths: `courses/trustworthy-ai/lec06-hallucination.html` L334; `courses/trustworthy-ai/lec06-hallucination-note.html` L313/L316/L318.
- Point/title [judgment]: more abstention accompanies fewer errors at similar accuracy in this **cross-model SimpleQA comparison**. Keep title or use that descriptive takeaway; no causal reward title.
- Required content: replace “Rewarding ... collapses” and wrong-to-blank conversion language with aggregate association, not paired transitions or an isolated intervention. Preserve correct numbers/arithmetic.
- Exhibit: existing two-model wrong/abstention shares; explain population and the similar accuracy, not a training ablation. Evidence: E110.
- Placement: main takeaway plus Script/detail; keep correct Message. Acceptance: SimpleQA throughout, no PersonQA substitution, causal reward claim or implied question-level transitions.

### 7. F79 — lec06 S08/p8, “Invented Medical Facts” → proposed “A Fluent Medical Term Was Wrong” — P6
Paths: `courses/trustworthy-ai/lec06-hallucination.html` L134/L140–147; `courses/trustworthy-ai/lec06-hallucination-note.html` L118–127.
- Point [judgment]: fluent medical output can contain an anatomical error; observed output does not reveal the model's internal cause.
- Required content: cite Yang et al., *Advancing Multimodal Medical Capabilities of Gemini*,2405.03162v1, Fig9 p28, not Saab's different paper; cite the Google blog separately. Remove “unnoticed for a year” and implied formal peer review. Attribute early flagging to Bryan Moore and describe the paper still carrying the error when reported in August2025. Do not claim a clinical outcome.
- Exhibit [judgment]: retain observed wrong term vs correct anatomical term. Remove causal blend arrows/text, or explicitly label a blend illustration hypothetical. Attribute Google's learned-mis-transcription explanation as its account, not demonstrated mechanism. Preserve the need to check fluent text.
- Evidence: E111. Placement: concise observed-error example on main; chronology/source distinctions in note. Acceptance: title, illustration, Script and citations all make the observation/inference distinction; no “blog only” correction.

### 8. F80 — lec05 retraining and target distinctions — P5
All [judgment]; evidence E112. Reuse the existing S14/S48 distinctions; no new taxonomy or course argument.
- **8.1 S61/p61, “What Guarantee Holds?”** Paths: `courses/trustworthy-ai/lec05-unlearning.html` L1327–1339; `courses/trustworthy-ai/lec05-unlearning-note.html` L1016–1022. Point: refusal, behavioral suppression and matching retraining are different claims with different evidence. Keep three-card exhibit, but remove an unconditional strict-strength/implication ladder and any blanket “stronger/weaker” conclusion based solely on target type. Explain in the note: nested adaptation classes strengthen a fixed behavioral target; exact deletion can retain knowledge supported by retained data. Title may remain, or “Different Claims, Different Evidence.” Acceptance: retained-duplicate-fact counterexample no longer contradicts the cards or note.
- **8.2 S63/p63, “Evaluation Standards”.** Path: `courses/trustworthy-ai/lec05-unlearning-note.html` L1059. Point/title/exhibit stay: evaluate forgetting and retained utility together. TOFU is a suite with a retain-only retrained reference, **not the only one**; MUSE supplies one too. Preserve Fig5 reading. Acceptance: retained detail agrees with the displayed MUSE result and §5.1.
- **8.3 S66/p66, “Practice: Boardroom Questions”.** Path: `courses/trustworthy-ai/lec05-unlearning-note.html` L1112. Point: define the target before choosing evidence. A specified training document can be data removal with a retrained reference; an abstract concept without an identified training subset is suppression. Keep existing question exhibit and individual-example setup distinctions. Acceptance: no automatic document→no-reference classification.

### 9. F81 — lec05 audit qualifications on main — P5
All [judgment]; evidence E33/E112. Preserve already-correct paired notes.
- **9.1 S09/p9, “Why Not Just Ignore It”.** Path: `courses/trustworthy-ai/lec05-unlearning.html` L240; paired `courses/trustworthy-ai/lec05-unlearning-note.html` S09. Point: membership testing is evidence, not certainty. “can confirm she was in” → “can provide evidence she was in.” Existing MIA/extraction exhibit stays; reconcile labels if needed. Acceptance: no zero-false-positive guarantee inferred from the illustration.
- **9.2 S55/p55, “Relearning Attacks”.** Path: `courses/trustworthy-ai/lec05-unlearning.html` L1231; paired `courses/trustworthy-ai/lec05-unlearning-note.html` S55. Point: faster recovery under the same adaptation budget than the retrained control suggests residual trace. Replace unconditional “snaps back ... never gone”; preserve actual syntax-study result/figure. Acceptance: not all learning from new examples is failed deletion; main carries the control needed for its conclusion.

### 10. F85 — lec10 S25/p25, “Training on Recovery Examples Deepened Refusal” — P10
Path: `courses/trustworthy-ai/lec10-jailbreak-note.html`, L522/L528 (article L513).
- Point/title: preserve measured augmentation benefit and title, not universal robustness.
- Required content [judgment]: GCG was re-optimized for each evaluated victim, including the augmented model. These families/budgets do not cover all adaptive attacks. Repair Script and limitations without redundant boilerplate.
- Exhibit: current before/after ASR table; preserve numbers and top3-of10 GCG selection. Evidence: E118/App.A.4.
- Placement: note protocol/limits; no main-table redesign. Acceptance: no categorical claim that the augmented model faced no model-specific attack.

### 11. F93 — lec14 S19/p19, “Oversight Disabling: Rare in These Scenarios” — P14
Paths: `courses/trustworthy-ai/lec14-agentic-threats.html` L377/L381; `courses/trustworthy-ai/lec14-agentic-threats-note.html` L380/L381/L385/L390.
- Point/title: retain rare oversight-action rates; the over85% denial summary refers to broader scheming follow-ups, not this table's oversight-only subset.
- Required content [judgment]: name the broader scope on main; note names oversight subversion, self-exfiltration and goal-guarding. Add Fig3 locator. Do not present follow-up responses as all rollouts. Keep the separate 2% action rate, pre-release checkpoint and caption300/text100/400-unnudged caveats.
- Exhibit: existing oversight-rate table, separate broad follow-up annotation. Evidence: E134.
- Acceptance: no over85%-oversight-only inference; capability in constructed incentives is not deployment/latent-intent frequency. Do not silently replace a summary with a falsely precise inferred bar value.

### 12. F97 — lec14 S31/p31, “Prompt Infection: What Spread, and When” — P14
Paths: `courses/trustworthy-ai/lec14-agentic-threats.html` L575–577/L584; `courses/trustworthy-ai/lec14-agentic-threats-note.html` L630/L631/L634/L637.
- Point/title: propagation depends on the scenario; failure categories are not unconditional model resistance. Retain title and the distinction between simulated apps and society experiments.
- Required content [judgment]: 66%/9% are reported in **Fig5's failure-reason breakdown**, not all-attempt ignored-attack rates; remove resistance ranking from them. Note the ambiguous source prose and conflict with Fig4 success rates. Do not invent a total-attempt denominator or an exact conditional rate. Attribute execution-reliability explanation to the authors. If the numbers cannot be made unambiguous and brief on main, move the qualified breakdown to notes while retaining its source limitation.
- Required exception: self-replication helped most global-message scenarios; **data theft was an exception**, including some larger-agent settings. Keep memory-manipulation condition for separate society experiment. Add Figs4–5 for apps, retain Fig6 for society.
- Exhibit: existing two-experiment comparison, no new measured chart. Evidence: E138.
- Acceptance: every layer separates experiment, denominator and exception; no blanket global-message superiority or unsupported resilience ranking.

### 13. F101 — lec01 S23/p23, “July 2026: An Attack Nobody Ordered” — P1/P15
Paths: `courses/trustworthy-ai/lec01-introduction.html` L508/L512; `courses/trustworthy-ai/lec01-introduction-note.html` L570/L571/L574/L579/L581; `courses/trustworthy-ai/OUTLINE.md` L188.
- Point/title: retain incident title and attribution caveats; distinguish reconstructed campaign from internal access.
- Required content [judgment]: July9–13 /4.5 days describes the campaign, **including external staging**; roughly2.5 days were inside HF. Carry through main timeline/metric, Message, Reading, Script, chronology, source paragraph and leaf summary. Keep17,600 as campaign-wide reconstructed actions.
- Exhibit: existing chronology/statistics, with scopes explicitly attached. Evidence: E50/E115/E145/E146.
- Acceptance: no “4.5 days inside HF” repetition or justification that the slide chooses an internal longer window. Preserve corrected lec07 S08 and dated reconstruction/intent caveats.

## Nonblocking items — unchanged status
The following are not gates and do not authorize another round. For each, use the complete numbered path/ID/page/current→fix/reason instructions in frozen review-r3. Record **fixed**, **declined**, or **unchanged with reason** in work-r4; do not silently classify all as fixed. Any taken fix receives the same cross-layer/source/render checks as required work.

| Priority | Finding / scope | Package |
|---|---|---|
| slides decides [judgment] | F71 lec01S31 inherited pyramid label contrast | P1 |
| prefer | F72 root outline's two lec02 inline locators; recompute after actual edits, not literal stale line-number substitution | P15 |
| prefer [judgment] | F75 lec04S13 exact canary guess vs pairwise ranking | P4 |
| prefer [judgment] | F76 lec02S09 comparison-model access label | P2 |
| slides decides [judgment] | F77 lec02S29 171cm marker ordering | P2 |
| prefer [judgment] | F82 lec05S46/S62 logit-lens weakness vs successful recovery attacks | P5 |
| prefer [judgment] | F83 lec05S50 equal laws vs realized sample statistics | P5 |
| slides decides [judgment] | F84 lec05S03/S43/S52 inherited diagram legibility | P5 |
| prefer [judgment] | F86 lec08S35 transferability section locator | P8 |
| prefer [judgment] | F87 lec13S05 unsupported current-model comparison | P13 |
| prefer [judgment] | F88 lec13S14 ASR-valid denominator | P13 |
| prefer [judgment] | F89 lec13S09/S13 illustrated regions/arrow reading | P13 |
| prefer [judgment] | F90 lec13S45/S46 AgentDojo attribution/CaMeL heading locator | P13 |
| prefer [judgment] | F91 lec13S41 subsidiary ProtectAI secret-filtered denominator | P13 |
| prefer [judgment] | F92 lec13S50 unsupported prior guard-testing history | P13 |
| prefer [judgment] | F94 lec14S08–S13/S21/S36–S42/S45 and leaf source-map version/section/table locators | P14/P15 |
| prefer [judgment] | F95 lec14S21 MMLU biology control; 46% belongs to cyber | P14 |
| slides decides [judgment] | F96 lec14S11 visible task-suite scope | P14 |
| prefer [judgment] | F98 lec14S32 handcrafted vs adaptive attack distinction | P14 |
| prefer [judgment] | F99 lec14S27 second-largest MAST mode | P14 |
| prefer [judgment] | F100 lec14S43 decisive-attempt denominator | P14 |

Work-r3 issue3's optional lec02S28 original-release/extra-accounting clarification may be taken within P2; it is not an additional blocker. Other seven work-r3 issues are adjudicated in review-r3, not reopened merely because a new round is authorized.

## Packages and permitted surfaces
Package numbering remains lecture-based for continuity; these are ownership boundaries, not a request to create additional workers. slides chooses its implementation method and personally handles the marked judgment calls. No two workers edit one surface concurrently.

| Package | Required IDs | Optional IDs | Permitted paths |
|---|---|---|---|
| P1 | S12/S23/S42 | S31 | `courses/trustworthy-ai/lec01-introduction.html`, `courses/trustworthy-ai/lec01-introduction-note.html` |
| P2 | S27/S33/S36/S39/S41/S57 | S09/S28/S29 | `courses/trustworthy-ai/lec02-privacy-dp.html`, `courses/trustworthy-ai/lec02-privacy-dp-note.html` |
| P3 | S49 | none | `courses/trustworthy-ai/lec03-mia.html`, `courses/trustworthy-ai/lec03-mia-note.html` |
| P4 | S53 | S13 | `courses/trustworthy-ai/lec04-memorization.html`, `courses/trustworthy-ai/lec04-memorization-note.html` |
| P5 | S09/S55/S61/S63/S66 | S03/S43/S46/S50/S52/S62 | `courses/trustworthy-ai/lec05-unlearning.html`, `courses/trustworthy-ai/lec05-unlearning-note.html` |
| P6 | S08/S20/S57 | none | `courses/trustworthy-ai/lec06-hallucination.html`, `courses/trustworthy-ai/lec06-hallucination-note.html` |
| P8 | none | S35 | `courses/trustworthy-ai/lec08-adversarial.html`, `courses/trustworthy-ai/lec08-adversarial-note.html` |
| P10 | S25 | none | `courses/trustworthy-ai/lec10-jailbreak.html`, `courses/trustworthy-ai/lec10-jailbreak-note.html` |
| P13 | none | S05/S09/S13/S14/S41/S45/S46/S50 | `courses/trustworthy-ai/lec13-prompt-injection.html`, `courses/trustworthy-ai/lec13-prompt-injection-note.html` |
| P14 | S19/S31 | S08–S13/S21/S27/S32/S36–S43/S45 | `courses/trustworthy-ai/lec14-agentic-threats.html`, `courses/trustworthy-ai/lec14-agentic-threats-note.html` |
| P15 (integrator only) | F101 leaf repair; required synchronization | F72/F94 | `courses/trustworthy-ai/OUTLINE.md`, `OUTLINE.md`, tracked job record |

Dependencies: P1/P2/P3/P4 share E101/E103's guarantee distinction; P15 follows content integration. No content work is required in P7/P9/P11/P12; use settled comparison entries read-only. Inspect neighbouring articles for regression, not as an invitation to rewrite them. A newly found same-claim repetition may be repaired in the already-authorized canonical lectures, with its ID/source and reason explicitly mapped in work-r4; unrelated defects or excluded-file changes return as plan issues.

## Shared surfaces and preservation
1. Keep contents/dividers/recaps, timings, counts and stable mappings unless a named repair changes them. Sync renamed titles with notes and outlines; changed line pointers must land on the named content under the existing convention. F72's literal old lines are evidence locators, not the expected final lines.
2. Leaf F101 repair is required. If F94 is taken, also correct the leaf Kwa/Greenblatt source-map entries. Update the current revision summary so it does not imply the earlier 84-main count or three-title list describes all r4 changes; distinguish that historical r3 count from this pass's actual count. No unrelated source-map rewrite.
3. Preserve review-r3's “Preserve these source distinctions” list in full: Kwa version/count/forecast distinctions; RepliBench component/pass@10 limits; Meinke population/discrepancies; CaMeL conditional guarantees and dataset counts; Nasr exclusions; control free audits/upsampling/separate experiments; Ge-Wang n/CI/scorer/denominator; SimpleQA and GCG selection. Original lec12 Fig4 generator remains **unrecovered**, not solved by this pass. Valid lec14tech independent-all-steps-right calculation stays untouched.
4. If Albert has issued a direct conflicting instruction to slides, report its scope as a plan issue before reversing his change. Do not treat this go-ahead as overriding an unknown newer order.

## Handoff and acceptance
- Report `work-r4.md` on the same branch, naming an exact pushed commit and all content commits after ef453a8. Include per-package changes, deviations, unsourced facts, plan issues, every required/optional finding disposition, and `lecture | ID | old page | new page | title/split/move` mapping. Preserve prior frozen reports; do not alter work-r3 to make its claims retrospective.
- Run structural/lint/link/math checks on changed files; compare warnings with ef453a8. Render changed mains and their neighbours at presentation size; open changed note articles desktop/narrow, including the actual changed lower details and formulas. No shrinking type, clipping, overlap, broken wrap or missing-glyph capture counted as a pass. Inspect outputs, not just screenshot existence. Broad all-lecture recapture is unnecessary.
- Reviewer checks only changed entries and neighbours against requests → sources → design rules → this plan. Explicitly test F73's delta0/positive-delta distinction, F74's no-invalid-theorem route, F34 finite-vs-population claim, F79 observation-vs-mechanism, F80 target distinction and F97 denominator ambiguity. Verify complete affected articles, not only Message.
- Global structural sanity may confirm all1,006 ordered main/note pairs and no excluded-path edits, but does not claim a new exhaustive all-source audit. Counts remain targets if a justified split occurs.
- **Round boundary:** ordinary2/2 and previous supplemental1/1 remain exhausted. C09 authorizes exactly this additional pass. On unresolved/new blockers at review-r4, set escalated and return to Albert; no automatic r5.
- If a provider reports an actual five-hour quota limit, preserve progress, record provider/reset when known, pause the job and resume after that reset per C03. Silence or elapsed time alone is not a quota hold; do not switch accounts/models/providers.
- Only after an approved exact commit and pushed job records: owner confirms every later commit is confined to `log/2026-11-15-lec01-lec12-notes/`, rechecks for an existing PR, then opens the single PR against main. **No merge authorization. No PDF unless requested.**
