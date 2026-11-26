# trustworthy-ai/ — Trustworthy AI course

Undergraduate course for sophomores/juniors (15-week semester × 1.5 hr; 14 taught lectures), mixed majors with
basic Python/Colab experience. **Mode:** concept introduction + motivation first —
foundational works, a little recent work, light technical detail, no proofs.
At most one intuitive formula per key concept.
Each lecture: a **formal definition → short history → 2025–26 frontier**, plus an
optional **Colab demo** students can run themselves (no homework, nothing to submit).

All lecture decks live flat in this folder (`lecNN-*.html`). Arc climbs the
**trust stack**: data → model → output → society. Real paper figures (cropped +
cited) live in `figs/`; `bundle.py` inlines them. Concept diagrams are inline SVG.

> **Reading this file.** 1,360 lines — do not read it whole (~31k tokens). The
> tables below (Modules, Lecture index, Technical supplements, Cross-folder reuse)
> are the navigator; each deck then has its own `## lecNN-*.html` section. Working
> on one lecture? Read that section only — `grep -n '^## ' OUTLINE.md` for the line
> range, then `Read` with offset/limit. ~1.5k tokens instead of 31k.

## Modules

| Module | Weeks | Theme |
|---|---|---|
| 0. Foundations | 1 | What "trustworthy" means, threat-model thinking |
| 1. Privacy & Data | 2–5 | What models leak about their training data |
| 2. Reliability | 6–7 | Can you believe the answer, and does training get what we meant |
| 3. Security | 8–11 | How models are attacked, train- and inference-time |
| 4. Provenance, Fairness & Agents | 12–14 | Fairness, prompt injection, emerging agentic threats; Wk 14 is the finale with a course-wide checklist |
| — | — | Governance, frontier, demo showcase: optional backup `backup-governance.html` |

## Lecture index

| Wk | File | Topic | Status |
|---|---|---|---|
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **case-brief pass 2026-09-13** (46 sl, ~40 min; note 46 briefs, 80 links checked) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **case-brief pass 2026-09-13** (69 sl, ~75 min, 11 figs, `demos/rr-simulator.html`; note 69 entries — 16 case briefs with setup/verification/limits/status; tech 23 sl) |
| 3 | `lec03-mia.html` | Membership inference attacks | **case-brief pass 2026-09-13** (70 sl, 16 real figs, Homer 2008 block + NIH 2008→2018 chronology, TPR/FPR/ROC/AUC + base-rate block, LiRA-on-LLMs, boardroom questions) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **revised 2026-08, figure pass 2026-09, Cooper 2026 frontier 2026-09-11, case-brief + core-path pass 2026-09-14** (65 sl, 27 real figs) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **figures 2026-09, case-brief + core-path pass 2026-09-14, page edits 2026-09-30** (68 sl, ~97 min; 90-min core path in the note only; taxonomy + category badges; note 68 entries, 13 uniform briefs + legal brief; tech 12 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **figures 2026-09, Albert revision 2026-10** (75 sl after round 4: Avianca context, P(True) explained, two kinds of calibration, fair-rank intuition replaces proof; heavy math moved to lec06tech; note 75 entries) |
| 7 | `lec07-alignment-failures.html` | Alignment failures: sycophancy, reward hacking, explanation faithfulness | **new 2026-10**, example-first revision 2026-10-14 (75 sl, 13 real figure crops from 9 source figures, 90 min, no activities; note 75 entries; tech 12 sl). Blocks: hook 1–13 (alignment as goal/HHH/values, reported shortcuts, 2026 OpenAI–Hugging Face incident 8–10) · intent→reward 14–21 (win-rate definition 19) · sycophancy 22–27 · gaming 28–37 (o3 after-the-fact question 36) · controlled studies 38–55 (alignment-faking contrast 40, transcript 42, told vs trained 44, one hack 47, eval pipeline / separate graders 49, chat tests with exact prompts 50, monitor disruption 51, frame colleague 52) · faithfulness 56–68 (Lanham worked examples 60–62, hint test vs STaR 64) · synthesis 69–75 (Pachocki 2026 view 73). Korean backup explainers (not slides): `lec07-backup-korean-note-for-study1.html` (Study 1, slides 40–45) and `lec07-backup-korean-note-for-study2.html` (Study 2, slides 46–55). Former Wk 7 interpretability deck → `backup-interpretability.html` |
| 8 | `lec08-adversarial.html` | Adversarial robustness: threat models, FGSM → PGD, honest evaluation, certificates | **new 2026-10**, motivation revision 2026-10-20, Albert feedback round 2026-10-21 (101 sl, 15 real figure crops + 3 charts redrawn from tables, 90 min, no activities; note 101 entries; tech 24 sl). Blocks: why robustness 3–11 (Geirhos texture 7–8) · tiny nudge 12–18 · why it happens 19–36 (Nguyen 22, like-you're-five linearity 24–28) · who attacks 37–52 (motives 38–40, ℓ∞/ℓ2 2-D 43–45) · worst case 53–61 · defenses 62–84 (accuracy under attack 74–75, certificate 81) · off the screen 85–90 · LLMs 91–97 (overlaps lec10/lec13 on purpose) · wrap-up 98–101 |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **rebuilt 2026-10**, motivation revision 2026-10-25 (91 sl, 90 min, concept-first, no activities; note 91 entries). Blocks: integrity 3–14 · who poisons 15–18 · poisoning 19–32 · backdoors 33–47 · web-scale data 48–57 · language models 58–75 (in the wild 68–71) · defenses 76–91 |
| 10 | `lec10-jailbreak.html` | Jailbreaks: safety training, fragility, search, budget, evaluation & defenses, self-assessment monitoring | **rebuilt 2026-10**, Albert feedback round 2026-11-02 (88 sl, 90 min, concept-first, no activities; note 88 entries; tech 21 sl). Blocks: what safety training adds 3–13 (motivation 4–6, Wei example 7, safety and refusal 9–10) · fragility 14–30 · search 31–41 · attack budget 42–59 (test-time scaling 43–45, in-context learning 47) · evaluation & defenses 60–76 · self-assessment 77–85 · wrap-up 86–88 |
| 11 | `lec11-synthetic-media.html` | Synthetic media: text watermarks, robustness, detection without a watermark, provenance (C2PA) & labelling law | **new 2026-10** (74 sl after Albert r1 2026-11, 16 cited image files + 5 tables/figures redrawn, 90 min, concept-first, no activities; note 74 entries; tech 14 sl). Former Wk 11 prompt injection → rebuilt as Wk 13; former Wk 12 watermark deck replaced |
| 12 | `lec12-fairness.html` | Fairness: where bias enters, criteria, COMPAS and impossibility, mitigation, audits beyond classifiers | **new 2026-10; visual revision 2026-11** (87 sl, 26 cited figure crops, 90 min, concept-first, no activities; note 87 entries; tech 23 sl; stable slide IDs S01–S84 in `data-slide-id`, splits lettered; plot-interpretation revision 2026-11-13; clarity revision 2026-11-16). Merges the former Wk 13–14 fairness decks → `backup-fairness-defs.html`, `backup-fairness-mitigation.html` |
| 13 | `lec13-prompt-injection.html` | Prompt injection: direct and indirect, agents, three incidents, why it is hard, measured defenses and CaMeL | **new 2026-10; clarity revision 2026-11-20** (65 sl, 7 real figure crops, 4 bar charts drawn from tables, 90 min, concept-first, no activities; note 65 entries; tech 15 sl; stable slide IDs S01–S56 in `data-slide-id`, splits lettered). Replaces `backup-prompt-injection.html` (deleted) |
| 14 | `lec14-agentic-threats.html` | When AI Learns and Acts: delegation (Project Vend), hidden behaviors passed on in training, checks on untrusted work (AI Control); course finale | **new 2026-10; finale refresh 2026-11-22; focused revision 2026-11-27** (59 sl, 85 + 5 min, concept-first, no activities; note 59 entries; tech 14 sl; stable slide IDs in `data-slide-id`; survey and further hidden-transfer material in `backup-lec14-agentic-threats.html`, 52 sl). Replaces `backup-agentic-autonomy.html` (deleted); former Wk 15 governance deck → `backup-governance.html` |

Every deck has a companion **instructor note** `lecNN-…-note.html` (one `<article>` per slide,
keyed by the same `data-slide-id`), following the DESIGN_SYSTEM §9 instructor-note contract.
Since the 2026-11-15 notes revision, all 14 lectures (lec01–lec14) use the same structure. Each
entry opens with a short **Message** (`p.msg`, the slide's point with its qualifiers), then
**Reading the slide** (what the slide, plot or diagram shows), then the details under
**Script** (script, figure, sources, minor points). Decks and notes lec01–lec14 carry stable slide IDs in
`data-slide-id`. lec01–lec11 use sequential `S01…SNN` (as of 2026-11-15). lec14 (focused revision 2026-11-27) uses baseline `S01–S56` plus `S57–S90` with letter splits; the main deck holds 59 and `backup-lec14-agentic-threats.html` 52 (round 2 added S91–S95), and ID order is not page order (see its section). lec12 uses `S01–S84` (S04, S12, S77 retired) with lettered splits such as `S39a/S39b`. lec13 (clarity revision 2026-11-20) uses `S01–S56`: splits S05a/b, S07a/b, S09a/b, S21a/b, S31a/b, S40a/b, S44a/b, S47a/b/c; new S54–S56 placed in the defenses block, so ID order is not page order.
The same revision corrected 84 main slides across lec01–lec14 so slide and note agree (qualifiers, scoped claims, source setups). No slide was added, removed or split. Three titles changed: lec07 S70 "One Shape, Four Faces", lec10 S06 "…Shared and Stay Online for Months", lec11 S34 "Small Full-Text Distribution Distance Limits Detection". A follow-up accuracy pass on the same date (job round 4) corrected 31 further main slides in lec01–lec06, lec08, lec13 and lec14 (DP δ qualifiers, evaluation scopes, source locators, label placement); again no slide was added, removed or split, and one title changed: lec06 S08 "A Fluent Medical Term Was Wrong".
Every lecture also has an optional **technical supplement** `lecNNtech.html` — see below.

## Technical supplements (optional sub-decks)

One `lecNNtech.html` per lecture. Each holds the **formal math** its main deck keeps as a
picture/prose — the main deck stays concept-first (≤1 glanceable formula per concept), the
supplement carries the rigorous version. Optional, not shown in the core session; a pointer
for students who want the equations. Standalone (no main-deck cross-refs); discoverable here.
Built in the **2026-07-15 tech-supplement pass**; all lint-clean, KaTeX-verified.

| File | Parent | Holds | Status |
|---|---|---|---|
| `lec01tech.html` | Wk 1 (intro) | adversarial-example ε-ball; threat-model taxonomy (knowledge × timing); Kerckhoffs framing | **drafted** (7 sl) |
| `lec02tech.html` | Wk 2 (privacy/DP) | (ε,δ)-DP def; **what a reported ε depends on** (unit, add/remove vs replace, group privacy kε, composition period, central vs local — added 2026-09-13); ε/e^ε log-odds; sensitivity Δq; Laplace/Gaussian mechanisms; randomized-response algebra + privacy-vs-accuracy SE bound $1/(2q\sqrt n)$, $q=\tanh(\varepsilon/2)$; DP-SGD (clip C + N(0,σ²C²) + accountant); composition/Rényi. Points to `courses/privacy/lectures/01-dp/` | **drafted, RR accuracy slide added 2026-09-08** (23 sl) |
| `lec03tech.html` | Wk 3 (MIA) | Homer statistic $D_j=(M_j-\mathrm{Pop}_j)(2Y_j-1)$, per-SNP moments, aggregate $T$ + power ($m\approx 28{,}000$ / $39{,}000$ at $\alpha=10^{-6}$); score+threshold; optimal LR test Λ(x); LiRA (shadows on random halves, logit score $\phi(p)$, Gaussian fit, log-LR closed form, equal-variance linear rule + worked example $\log\Lambda\approx1.78$, offline variant); TPR(τ)/FPR(τ)/ROC set; AUC = Pr[S₁>S₀] with proof; base-rate precision table (π=1/100, one convention across deck/note/tech since 2026-09-14); TPR@α + Hayes scale check (AUC 0.55–0.70; 15% coin-flip TPs at α=10⁻³); DP bound TPR ≤ e^ε·FPR + δ; auditing; one plain-language "Intuition" line before each formal block | **updated 2026-09-13** (20 sl) |
| `lec04tech.html` | Wk 4 (memorization) | k-extractability def (+ Intuition line); discoverable vs extractable (Nasr Defs. 1–2; two games, no containment); memorization-fraction metric; log-linear scaling law; greedy argmax condition + $H(S\mid P_{1:k+1})\le H(S\mid P_{1:k})$; near-verbatim ball $B_\varepsilon$ and $p_\varepsilon$; $k$-CBS deterministic lower bound; control-group excess rate + conformal threshold + OLMo 2 32B table | **updated 2026-09-12** (15 sl) |
| `lec05tech.html` | Wk 5 (unlearning) | **Formal Goals, Separated (data removal has a retrained reference; suppression/filtering/revocation do not — added 2026-09-14)**; exact vs approx; (ε,δ) unlearning inequality (Guo Eq. 1/§2, two-sided); influence function θ₋ₓ ≈ θ̂ + (1/n)H⁻¹∇ℓ + Hessian infeasibility; gradient ascent; SISA cost E[cost] = n(R+1)(2R+1)/(6SR), full/E = 3R/(2R+1) ↗ 3/2 (S shards, R slices, matching the note); every slide carries the main deck's category badge | **updated 2026-09-14** (12 sl) |
| `lec06tech.html` | Wk 6 (hallucination) | reliability diagram; ECE = Σ_b (n_b/n)|acc_b−conf_b|; temperature scaling; conformal coverage Pr[y∈C(x)]≥1−α + threshold quantile; semantic entropy | **checked 2026-08, Why It Holds + threshold wording 2026-10; round 4 2026-10-07** (20 sl: new §01 Forced Errors = Kalai bound + trigram Thm 3/Cor 2, and the 3 coverage-proof slides, all moved from lec06; math verified; A1 + A2, q̂ = ∞, ties, marginal stated) |
| `lec07tech.html` | Wk 7 (alignment failures) | reward-model loss $-\binom{K}{2}^{-1}\mathbb{E}\log\sigma(r_w-r_l)$ (Bradley–Terry reading; Ouyang Eq. 1); KL-penalized RL objective (Ouyang Eq. 2, γ = 0); DPO loss $-\mathbb{E}\log\sigma(\hat r_\theta(x,y_w)-\hat r_\theta(x,y_l))$, $\hat r_\theta=\beta\log\pi_\theta/\pi_{\rm ref}$ (Rafailov 2023 Eq. 7); Gao overoptimization fits $R_{\rm bon}(d)=d(\alpha-\beta d)$, $R_{\rm RL}(d)=d(\alpha-\beta\log d)$, $d=\sqrt{\rm KL}$; Chen hint-test faithfulness score (symbols defined) + random-flip normalization $\alpha=1-q/((n-2)p)$, domain $n>2$, $p>0$, $\alpha>0$; monitor recall/precision with Baker Table 1 | **new 2026-10** (12 sl; all formulas checked against the paper PDFs). Old interpretability supplement → `backup-interpretabilitytech.html` |
| `lec08tech.html` | Wk 8 (adversarial robustness) | perturbation set $\mathcal B_p(x,\varepsilon)$; FGSM as the exact maximizer of the linearized loss over the ℓ∞ box ($g^\top\delta\le\varepsilon\|g\|_1$; unclipped ℓ2 analogue); linear model $w^\top\eta=\varepsilon\|w\|_1$; PGD with random start + projections; C&W ℓ2 objective, tanh box, binary search on $c$; min-max + Danskin; Cohen Thm 1 with Neyman–Pearson sketch; CERTIFY (Clopper–Pearson, $\alpha$) | **new 2026-10** (24 sl; formulas checked against the paper PDFs) |
| `lec09tech.html` | Wk 9 (poisoning) | count vs rate α; feature-collision objective; backdoor objective + ASR; spectral signatures; Neural Cleanse + MAD index; activation clustering | **rebuilt 2026-10** (18 sl) |
| `lec10tech.html` | Wk 10 (jailbreak) | ASR + SE; any-of-N; judge-error correction; RLHF KL objective; per-token KL; refusal direction ablation; GCG loss + budget; PAIR budget; MSJ and BoN power laws | **rebuilt 2026-10** (21 sl; formulas checked against the paper PDFs) |
| `lec11tech.html` | Wk 11 (synthetic media) | green-list rule (KGW Alg. 2); idealized Binomial null + assumptions; z &gt; 4 ≈ 3×10⁻⁵ (normal approx.) vs exact tail at T = 20; √T growth under constant green rate; repeated pairs, nominal vs measured FPR (K24 App. A.3, Fig. 7); base-rate formula; TV bound AUROC ≤ ½+TV−TV²/2 (TV defined; keyed detectors); distortion-free vs undetectable; SynthID-Text mean g-score | **new 2026-10** (14 sl; formulas checked against the saved papers) |
| `lec12tech.html` | Wk 12 (fairness) | four rates per group (with positivity); five criteria written out; Dwork (D,d)-Lipschitz (Def. 2.1); Kusner counterfactual fairness (Def. 5); calibration vs PPV via the score mix; Chouldechova identity (eq. 2.6); Kleinberg proof sketch; worked example computed; reweighing; reductions saddle point; Hardt derived predictor | **new 2026-10; split 2026-11** (23 sl, IDs S57–S73; formulas checked against the saved papers) |
| `lec13tech.html` | Wk 13 (prompt injection) | trusted vs attacker-controlled state; PI-SEC game and $\Omega_p$ (CaMeL §4); control vs data part of an action; confused deputy and least privilege; capability labels, propagation, STRICT mode; dual LLM → CaMeL policy check; conditional guarantee; AgentDojo BU / UA / ASR; static vs adaptive ASR with budget $q$ | **new 2026-10** (15 sl; checked against the saved papers) |
| `lec14tech.html` | Wk 14 (agentic threats) | time-horizon logistic fit $\sigma(\beta(\log h-\log t))$; 50% → 80% horizon; doubling time from the log-linear trend; compounding vs independence; the control game (safety, usefulness); upfront auditing closed form; per-task hazard $S_N$ (Ge-Wang eq. 4); empirical safety and its denominator; toy SIS propagation model labelled not empirical | **new 2026-10** (14 sl; checked against the saved papers; implied $\beta$ range and $S^*$ marked as our arithmetic) |
| `backup-fairness-defstech.html` | former Wk 13 (fairness defs) | demographic parity / equalized odds / calibration as conditional-prob defs; base rates; impossibility theorem (Chouldechova/Kleinberg) + proof sketch | **fixed 2026-08** (15 sl: base-rate identity was inverted (1−p)/p → p/(1−p) per Chouldechova eq 2.6; proof-sketch step 1 corrected (calibration ≠ "PPV = base rate" → predictive parity demands equal PPV across groups); unverifiable numeric-wedge table replaced with an exactly derivable two-value-score construction; impossibility attribution now dual Chouldechova + Kleinberg) |
| `backup-fairness-mitigationtech.html` | former Wk 14 (fairness mitigation) | reweighing w(g,y); penalized min Loss+λ·Unfairness; constrained form; reductions (Agarwal 2018); post-processing per-group thresholds (Hardt 2016) | **checked 2026-08** (17 sl: reweighing formula verified against Kamiran & Calders; reductions + Hardt ROC intuition verified against papers; one fix — cite venue "KIS 2012" → "Knowledge and Information Systems 2012") |

## Backup / swap-in materials (not in the 14 taught lectures)

Optional decks for substitution or extra sessions. The fairness and governance backups are labelled *optional archival*: their notes use an earlier course plan's lecture numbers, and the governance wrap-up and Demo Showcase are marked historical. Each has a `-note.html` script.

| File | Topic | Slots in where | Status |
|---|---|---|---|
| `backup-sycophancy.html` | Sycophancy, manipulation & persuasion | merge into Wk 6, or standalone | **drafted** (38 sl) |
| `backup-copyright.html` | Copyright, consent & data provenance | pairs with Wk 4 (memorization) | **drafted** (45 sl) |
| `backup-governance.html` | Governance, the frontier & wrap-up (EU AI Act, NIST RMF, frontier safety frameworks, demo showcase) | former Wk 15 (moved 2026-10; lec14 is now the finale); optional archival backup, wrap-up and Demo Showcase marked historical | **revised 2026-08, figure pass 2026-09** (70 sl; note `backup-governance-note.html`; tech `backup-governancetech.html`, 6 sl). Section `## backup-governance.html` below |
| `backup-lec14-agentic-threats.html` | Lecture 14 survey material: measuring autonomy, against the overseer, many agents, more control protocols, further frontiers | optional backup for Wk 14 | **added 2026-11-27** (52 sl incl. B6 More on Hidden Transfer; note `backup-lec14-agentic-threats-note.html`). Section `## backup-lec14-agentic-threats.html

**Topic:** Optional backup for Lecture 14. It holds the survey slides that the 2026-11-27 focused revision took
out of the main deck: measuring autonomy, against the overseer, many agents, more control protocols and further
frontiers. It also holds four optional recall cards (S13, S62a, S62b, S79) and, since round 2 (plan-v4), section B6
with four further hidden-transfer slides (S91–S94). It has 52 slides, `1 / 52`, and its note is
`backup-lec14-agentic-threats-note.html` (52 entries, keyed by `data-slide-id`). 29 slides are byte-identical
to the 2026-11-22 baseline; the title, contents, dividers and end slide (S80–S86, S95) are new. Contents is a
two-column list of six sections.

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | — | `:169`, `:181` |
| **B1 · Measuring Autonomy** | 3–16 | `:214` | small errors accumulate `:222` · METR Fig. 1 `:359` · recall: capability and delegation `:419` · developer trial `:445` · RepliBench Fig. 1 `:482` |
| **B2 · Against the Overseer** | 17–26 | `:534` | recall cards `:542`, `:567` · oversight disabled `:670` · van der Weij Fig. 4 `:727` · other explanations `:772` |
| **B3 · Many Agents** | 27–34 | `:800` | Hammond Fig. 1 `:808` · MAST Fig. 1 `:826` · Prompt Infection Fig. 6 `:903` · evidence strengths `:946` |
| **B4 · More Control Protocols** | 35–42 | `:961` | setup Fig. 1 `:969` · 15% vs 62% bars (baseline generator) `:1031` · Pareto Fig. 2 zoom `:1094` · recall: stopping authority `:1113` |
| **B5 · Further Frontiers** | 43–46 | `:1144` | three open questions `:1152` · Salvi Fig. 1 `:1165` · Fang Fig. 1 `:1182` |
| **B6 · More on Hidden Transfer** | 47–51 | `:1194` | Cloud Fig. 3a, both outcomes (S91) `:1202` · van der Weijden Fig. 2a animal row (S92) `:1222` · Yanagisawa Fig. 1 wolf panel (S93) `:1234` · Nief et al. revision notice (S94) `:1254` |
| End | 52 | — | `:1271` |

Figures and citations are as in the 2026-11-22 baseline slides they came from (`figs/metr-horizon-fig1.png`,
`figs/replibench-fig1-*.png`, `figs/control-*.png`, `figs/lec14-finale-refresh/p1-metr…`, `p2-…`, `p3-…`, `p5-…`).
B6 uses `figs/lec14-focused-overview/p2a-cloud-fig3a.png` (complete Fig. 3a), `p4-vdw-fig2a-animal.png` and
`p4-yan-fig1-wolf.png` (provenance in `p2a-PROVENANCE.md`, `p4-PROVENANCE.md`). B6 citations: Cloud et al., Nature 652
(2026), Fig. 3a and Methods; van der Weijden, Brack &amp; Báez Santamaría arXiv 2609.12586v1; Yanagisawa et al. arXiv
2609.22215v1; Nief et al. arXiv 2606.00831v2 (preprints; comments fields checked 2026-11-27).

## backup-fairness-defs.html

*Former Wk 13 deck (old names lec13-fairness-defs, its note, and lec13tech), moved unchanged on 2026-10-10 to `backup-fairness-defs.html`, `backup-fairness-defs-note.html` and `backup-fairness-defstech.html`; line pointers below still hold. Merged into Wk 12. Relabelled 2026-10 as an optional archival backup (title pill, page titles; the note carries a legacy-numbering notice), with no line shifts in the deck.*

**Topic:** Fairness I — definitions & impossibility (~90 min). Where bias enters the
pipeline (data, labels — Amazon recruiting + Obermeyer cost-proxy case — feedback
loops, proxy features); three group-fairness definitions at plain-English level
(demographic parity, equalized odds / equal opportunity, calibration — one glanceable
conditional-probability line each; the formal stack + impossibility proof sketch live
in `backup-fairness-defstech.html`); COMPAS as the anchor case (ProPublica FPR gap vs Northpointe's
predictive-parity/calibration defense — both "right" under different definitions,
which IS the impossibility story); the impossibility theorem (Chouldechova 2017 +
Kleinberg et al. ITCS 2017) as base-rate intuition, no proof in the main deck;
individual (Dwork) and counterfactual (Kusner) fairness one slide each; fairness in
generative models (Bianchi occupation grid, Gemini overcorrection, Gender Shades,
BBQ, NYC Local Law 144 + Colorado AI Act). Gender Shades *figure* stays in lec14
(this deck cites the numbers only, no figure duplication).

### Sections (62 slides, ~90 min — content-revised 2026-08 from 54, figure pass 2026-09 from 58, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Sources of Bias** | 3–13 | `:72` | model mirrors its world (pipeline SVG) `:80` · bias is not a bug (SVG) `:96` · three entry points (pipeline + feedback-loop SVG) `:109` · **biased data (Gender Shades benchmark-composition bars, IJB-A 79.6% / Adience 86.2% / PPB 53.6%)** `:124` · **Biased Labels: Amazon hiring (Reuters 2018; resume-flow SVG)** `:146` · label is the problem (proxy-loop SVG) `:167` · **Case: Cost as a Proxy for Need (Obermeyer, 17.7%→46.5% bar SVG; added 2026-08)** `:183` · feedback loops (SVG) `:208` · why "just drop race" fails (proxy-columns SVG) `:234` · notation A/Y/Ŷ (pipeline SVG) `:254` |
| **02 — Group Fairness Criteria** | 14–24 | `:271` | confusion matrix per group (SVG) `:279` · demographic parity (dot rows) `:304` · parity ignores the truth (qualified-ring dots) `:318` · equalized odds (dot rows by Y) `:338` · equal opportunity variant (two mini matrices) `:351` · **Equalized Odds on the ROC Plane (Hardt Fig 1, `figs/hardt-eqodds-roc.png`; added 2026-09)** `:372` · calibration (dot rows) `:383` · calibration trusts the score (SVG) `:397` · three criteria side by side `:417` · **Same Data, Five Rules (Hardt Fig 9 FICO thresholds, `figs/hardt-fico-thresholds.png`; added 2026-09)** `:430` |
| **03 — The COMPAS Case** | 25–32 | `:442` | **what COMPAS is (Chouldechova Fig 3 decile histograms, `figs/chouldechova-deciles.png`)** `:450` · ProPublica investigation (study-design SVG) `:468` · **False Positives, By Group (44.9% vs 23.5% bar SVG + 47.7%/28.0% FNR mirror)** `:482` · **The Gap Persists Within Subgroups (Chouldechova Fig 2 FPR by priors, `figs/chouldechova-fpr-priors.png`; added 2026-09)** `:505` · **Northpointe Responds (predictive parity; Chouldechova Fig 1 calibration plot, `figs/chouldechova-calibration.png`)** `:523` · both sides were right (column-vs-row confusion matrix SVG) `:540` · could COMPAS be both? (brick-wall SVG) `:556` |
| **04 — The Impossibility Theorem** | 33–42 | `:570` | base rates (dot grids) `:578` · **The Impossibility Theorem (Chouldechova + Kleinberg, plain-English; forcing SVG)** `:595` · two proofs, same wall (two-lane SVG) `:611` · pick-two-of-three triangle (SVG) `:627` · demo setup (pipeline SVG) `:647` · **Demo: The Numbers Don't Reconcile (derivable Ŝ∈{0.2,0.8} construction, FPR 0.20/0.02, FNR 0.20/0.73; bar SVG)** `:666` · why the gap is forced (stacked-bar SVG) `:689` · **which one to pick (Hardt Fig 11 FICO outcomes, `figs/hardt-fico-loans.png`)** `:710` · choosing by context (FP/FN matrices) `:725` |
| **05 — Individual & Causal Fairness** | 43–49 | `:741` | group fairness can hide harm (dot SVG) `:749` · individual fairness (Dwork; metric-space SVG) `:769` · the "similar" metric problem (SVG) `:785` · **A Causal View (counterfactual fairness, Kusner Fig 1, `figs/kusner-causal-models.png`)** `:806` · fair and unfair paths (causal-graph SVG) `:818` · **causal fairness needs a model (Kusner Fig 2 left, `figs/kusner-lawschool.png`)** `:843` |
| **06 — Fairness in Generative Models** | 50–60 | `:861` | new surface, old problem (classifier-vs-generator SVG) `:869` · **Text-to-Image Stereotyping (Bianchi Fig 1, `figs/bianchi-occupations.png`)** `:890` · **When the Fix Overcorrects (Gemini pause Feb 2024; prompt-rewrite SVG; added 2026-08)** `:911` · **Gender Shades (34.7% vs 0.8% bar SVG)** `:933` · auditing is the tool (pipeline SVG) `:947` · **Auditing LLMs: The BBQ Benchmark (Parrish Fig 1, `figs/bbq-example.png`; added 2026-08)** `:964` · **BBQ, Measured (Parrish Fig 3 bias-score heatmap, `figs/bbq-bias-scores.png`; added 2026-09)** `:982` · **The Law Notices (NYC LL144 + Colorado AI Act; timeline SVG; added 2026-08)** `:993` · frontier 2025–26 (four tiles) `:1014` · open tension (triangle SVG) `:1031` |
| Wrap-up / Closer | 61–62 | — | key takeaways `:1048` · closer ("Pick two.") `:1061` |

**Key citations (all source-verified 2026-08; figure numbers added 2026-09):**
- ProPublica — `:479` — Angwin, Larson, Mattu, Kirchner, "Machine Bias", ProPublica 2016;
  methodology + exact rates (FPR 44.85%/23.45%, FNR 27.99%/47.72%) — `:501` — Larson et
  al., "How We Analyzed the COMPAS Recidivism Algorithm", ProPublica 2016.
- Northpointe rebuttal — `:537` — Dieterich, Mendoza, Brennan, "COMPAS Risk Scales:
  Demonstrating Accuracy Equity and Predictive Parity", Northpointe, July 2016 (slide
  plots Chouldechova 2017 Fig 1).
- Impossibility — `:608`, `:624` — Chouldechova, "Fair Prediction with Disparate
  Impact", Big Data 2017 (also `:394` calibration def; `:465` Fig 3; `:520` Fig 2);
  Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of
  Risk Scores", ITCS 2017.
- Group-fairness definitions — `:315`/`:782` Dwork, Hardt, Pitassi, Reingold, Zemel,
  "Fairness Through Awareness", ITCS 2012; `:348` Hardt, Price, Srebro, "Equality of
  Opportunity in Supervised Learning", NeurIPS 2016 (`:380` Fig 1; `:438` Fig 9;
  `:722` Fig 11).
- Counterfactual fairness — `:815` (Fig 1), `:857` (Fig 2 left) — Kusner, Loftus,
  Russell, Silva, NeurIPS 2017.
- Label bias cases — `:143` Buolamwini & Gebru, FAT* 2018 (benchmark composition);
  `:164` Dastin, Reuters, Oct 2018 (Amazon tool penalized "women's"); `:204` Obermeyer,
  Powers, Vogeli, Mullainathan, Science 2019 (17.7%→46.5%).
- Generative — `:907` Bianchi et al., "Easily Accessible Text-to-Image Generation
  Amplifies Demographic Stereotypes at Large Scale", FAccT 2023 Fig 1; `:930` Google
  blog, Feb 2024 (Gemini pause); `:944` Buolamwini & Gebru, FAT* 2018 (34.7%/0.8%);
  `:979` (Fig 1), `:990` (Fig 3) Parrish et al., "BBQ: A Hand-Built Bias Benchmark for
  Question Answering", Findings of ACL 2022 (nine dimensions; +3.4pp stereotype-aligned
  accuracy).

**Figures:** cited crops in `figs/`: `hardt-eqodds-roc.png` `:377`,
`hardt-fico-thresholds.png` `:435`, `chouldechova-deciles.png` `:463`,
`chouldechova-fpr-priors.png` `:518`, `chouldechova-calibration.png` `:535`,
`hardt-fico-loans.png` `:720`, `kusner-causal-models.png` `:812`,
`kusner-lawschool.png` `:855`, `bianchi-occupations.png` (FAccT 2023 Fig 1, shared
with lec14) `:896`, `bbq-example.png` `:977`, `bbq-bias-scores.png` `:987`. Inline SVGs
on every other content slide (38 in total): pipelines `:80` `:96` `:109` `:254` `:468`
`:647` `:947`, Gender Shades composition bars `:124`, resume flow `:146`, proxy loop
`:167`, Obermeyer bar chart `:183`, feedback loop `:208`, proxy columns `:234`,
confusion matrix `:279`, dot-row criteria `:304` `:318` `:338` `:383` `:578` `:749`,
mini matrices `:351` `:725`, score readers `:397`, COMPAS FPR bars `:482`,
column-vs-row matrix `:540`, brick wall `:556`, forcing diagram `:595`, two lanes
`:611`, pick-two triangle `:627`, demo bars `:666`, stacked score bars `:689`,
metric space `:769`, similar-people `:785`, causal graph `:818`,
classifier-vs-generator `:869`, prompt rewrite `:911`, Gender Shades bars `:933`,
law timeline `:993`, frontier tiles `:1014`, tension triangle `:1031`. Citations use
`.cite-left`.

**2026-09 figure pass (58→62):** 10 public figures cropped into `figs/` with
figure-number citations (Hardt Figs 1/9/11, Chouldechova Figs 1/2/3, Kusner Figs 1/2,
BBQ Figs 1/3; Obermeyer Science PDF unobtainable, bar SVG kept); 32 inline SVG
diagrams added so no content slide is bullets-only. Added 4 slides: Equalized Odds on
the ROC Plane (§02), Same Data, Five Rules (§02), The Gap Persists Within Subgroups
(§03), BBQ, Measured (§06). 60-dpi render check of all 44 edited slides; grid SVGs
given explicit widths (an SVG in a `1fr auto` grid otherwise collapses to 300px).
Note synced: `Slide figure:` line on 40 entries, 4 new articles (62 entries, deck
order).

**2026-08 content revision (54→58):** every citation/number fetched and verified.
Added 4 slides: Case: Cost as a Proxy for Need (§01, Obermeyer); When the Fix
Overcorrects (§06, Gemini Feb 2024); Auditing LLMs: The BBQ Benchmark (§06); The Law
Notices (§06, NYC LL144 + Colorado AI Act incl. 2026 court suspension). Fixes:
**impossibility misattribution** (FPR/FNR form was credited to Kleinberg alone → dual
Chouldechova + Kleinberg, with each paper's actual form distinguished); **unverifiable
demo numbers replaced** (FPR "0.42/0.20" → exactly derivable calibrated two-value-score
construction); **COMPAS SVG numbers upgraded** from illustrative 45%/23% to verified
44.9%/23.5% + FNR mirror line + methodology cite; **Gender Shades corrected** (vague
"34-point gap", "FAccT 2018" → 34.7%/0.8%, FAT* 2018); **Bianchi title completed** +
bullets matched to the actual figure panels (software engineer / housekeeper, not
CEO/nurse); Amazon claim tightened to Reuters-verified wording; frontier slide
rewritten around verified content. `backup-fairness-defstech.html` fixed (see supplement table).
Note file synced (58 entries, order matches).

**2026-08 note enrichment:** `backup-fairness-defs-note.html` upgraded from speaker script (365 lines) to Script &amp; Companion Notes (708 lines; 58 entries unchanged): per-entry `.detail` blocks with rigorous definitions (setup A/Y/Ŝ/Ŷ, per-group confusion quantities, demographic parity + EEOC four-fifths rule verbatim, equalized odds / equal opportunity (Hardt Defs 2.1/2.2), calibration / test fairness / predictive parity (Chouldechova Def 2.1), independence–separation–sufficiency trichotomy, Dwork (D,d)-Lipschitz Def 2.1, SCM + counterfactual fairness Def 5), full proofs (Chouldechova base-rate identity + impossibility corollary, KMR Theorem 1.1 four-step linear-system proof verified against §2 + Thm 1.2 approximate version, forced-FPR-ratio corollary ≈1.63 on COMPAS base rates, fully worked calibrated two-value-score wedge matching lec13tech), and 23 verified links (ProPublica exact rates 44.85/23.45 + 27.99/47.72, Northpointe rebuttal via DocumentCloud, eCFR §1607.4(D), Obermeyer, BBQ, LL144 + SB24-205 litigation timeline).

## backup-fairness-mitigation.html

*Former Wk 14 deck (old names lec14-fairness-mitigation, its note, and lec14tech), moved unchanged on 2026-10-10 to `backup-fairness-mitigation.html`, `backup-fairness-mitigation-note.html` and `backup-fairness-mitigationtech.html`; line pointers below still hold. Merged into Wk 12. Relabelled 2026-10 as an optional archival backup (title pill, page titles; the note carries a legacy-numbering notice), with no line shifts in the deck.*

**Topic:** Fairness II — mitigation & accountability (~90 min). Picks up where lec13's
definitions end: three places to intervene in the pipeline (pre-/in-/post-processing),
one intuition + picture per method with formal math in `backup-fairness-mitigationtech.html` (reweighing
w(g,y), penalized/constrained objectives, reductions, per-group ROC thresholds);
the fairness–accuracy tradeoff and the impossibility recap (defined and proved in
lec13 — referenced, not redone); accountability (model cards, datasheets, audits —
Gender Shades figure + Actionable Auditing follow-up — impact assessments, EU AI Act
touchpoint only, governance is `backup-governance`); generative & LLM fairness (Bianchi figure
shared with lec13, Gemini overcorrection referenced briefly — the full case is
lec13's — plus LLM decision bias, prompt steering, post-training as mitigation,
resume-screening risk, and the 2025 both-ways regulatory squeeze).

### Sections (69 slides, ~90 min — content-revised 2026-08 from 55; figure pass 2026-09 from 61; all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — Three Places to Intervene** | 3–8 | `:81` | we measured bias; now fix it (gap bars SVG) `:89` · what mitigation means `:105` · ML pipeline (SVG) `:116` · which stage can you touch `:148` · black-box reality (sealed-model SVG) `:160` |
| **02 — Pre-Processing** | 9–16 | `:177` | bias is in the data (loop SVG) `:185` · **Reweighing (Kamiran & Calders)** `:201` · reweighing picture (SVG) `:215` · **Reweighing, Measured (AIF360 Fig. 4; added 2026-09)** `:243` · relabeling (scatter SVG) `:253` · representation repair (Feldman Fig. 1) `:269` · pros and cons `:286` |
| **03 — In-Processing** | 17–26 | `:299` | Loss+λ·penalty (slider SVG) `:307` · constraint τ (curve SVG) `:318` · **Reductions (Agarwal et al. ICML 2018; loop SVG)** `:334` · **Reductions, Measured (Agarwal Fig. 1; added 2026-09)** `:350` · why reductions are handy (wrapper SVG) `:364` · **Adversarial Debiasing (Zhang et al. AIES 2018; adversary reads the prediction — fixed 2026-08)** `:380` · adversary's job (Zhang Fig. 2) `:405` · **Adversarial Debiasing, Measured (Zhang Table 3; added 2026-09)** `:422` · pros and cons `:439` |
| **04 — Post-Processing** | 27–38 | `:452` | leave the model alone (Hardt Fig. 10) `:460` · recall equalized odds `:477` · **Group-Specific Thresholds (Hardt et al., SVG)** `:489` · post-hoc recipe (Hardt Fig. 2) `:512` · **What Post-Processing Needs (added 2026-08)** `:529` · accuracy cost (Hardt Fig. 11) `:542` · lending demo ×3 (illustrative numbers; two-bells SVG) `:559` `:572` `:594` · **Toolkits Ship These Methods (Fairlearn + AIF360; added 2026-08)** `:607` · **One Pipeline, Three Doors (AIF360 Fig. 1; added 2026-09)** `:620` |
| **05 — The Tradeoff** | 39–45 | `:630` | frontier curve (SVG) `:638` · **The Frontier, Measured (AIF360 Fig. 5(b); added 2026-09)** `:659` · which fairness (base-rate bars SVG) `:676` · impossibility (recap of lec13; Venn SVG) `:692` · no free lunch `:702` · a choice, not a formula `:715` |
| **06 — Accountability** | 46–57 | `:729` | mitigation needs a record (record-card SVG) `:737` · **Model Cards (Mitchell et al., Fig. 2)** `:753` · **Datasheets (Gebru et al., Fig. 1 excerpt)** `:769` · audits (SMACTR, Raji et al. FAT* 2020 Fig. 2) `:785` · **An Audit Needs a Benchmark (PPB, Gender Shades Fig. 1; added 2026-09)** `:800` · **Gender Shades figure (`figs/gender-shades.png`, FAT* 2018 Table 4)** `:817` · reading the table (0–0.8% vs 20.8–34.7%) `:828` · **The Audit Worked (Raji & Buolamwini AIES 2019, before/after bar SVG; added 2026-08)** `:841` · **The Audit Worked: The Numbers (Tables 1–2; added 2026-09)** `:880` · impact assessments (timeline SVG) `:889` · documentation becomes law (EU AI Act touchpoint; timeline SVG) `:905` |
| **07 — Generative & LLM Fairness** | 58–67 | `:922` | **Bianchi figure (`figs/bianchi-occupations.png`, shared with lec13)** `:930` · debias a generator `:948` · **Overcorrection Is Its Own Bias (Gemini Feb 2024, merged from 2 slides; case detail lives in lec13)** `:961` · **Do LLMs Discriminate? (Tamkin et al. Fig. 1; added 2026-08)** `:975` · **Measured: Who Gets Favored (Tamkin Fig. 2; added 2026-09)** `:993` · **Prompting the Bias Away (Tamkin Fig. 5; added 2026-08)** `:1003` · **Post-Training as Mitigation (Eloundou et al. ICLR 2025 Fig. 10; added 2026-08)** `:1021` · **Screening Is Still Risky (Wilson & Caliskan AIES 2024 Fig. 2; gender direction per Aug 2026 erratum; added 2026-08)** `:1039` · **Regulation Pulls Both Ways (EO 14319; added 2026-08)** `:1057` |
| Wrap-up / Closer | 68–69 | — | key takeaways `:1071` · closer ("λ") `:1085` |

**Key citations (all source-verified 2026-08; figure captions verified 2026-09):**
- Reweighing — `:211` — Kamiran & Calders, "Data Preprocessing Techniques for
  Classification without Discrimination", Knowledge and Information Systems 2012
  (w = Pexp/Pobs verified against the paper). Measured — `:249` — Bellamy et al.,
  "AI Fairness 360", 2018 (arXiv 1810.01943) Fig. 4(a),(c).
- Representation repair — `:282` — Feldman, Friedler, Moeller, Scheidegger,
  Venkatasubramanian, "Certifying and Removing Disparate Impact", KDD 2015, Fig. 1.
- Reductions — `:346` — Agarwal, Beygelzimer, Dudík, Langford, Wallach, "A Reductions
  Approach to Fair Classification", ICML 2018; measured — `:360` — Fig. 1 (top row).
- Adversarial debiasing — `:401` — Zhang, Lemoine, Mitchell, "Mitigating Unwanted
  Biases with Adversarial Learning", AIES 2018 (adversary predicts the group from the
  predictor's *output*, not shared features — deck fixed accordingly); gradient
  picture `:418` Fig. 2; measured `:435` Table 3 (UCI Adult).
- Post-processing — `:485`, `:525` — Hardt, Price, Srebro, "Equality of Opportunity in
  Supervised Learning", NeurIPS 2016; FICO figures `:473` Fig. 10, `:555` Fig. 11.
- Toolkits — `:616` — Fairlearn (fairlearn.org, community-driven); AI Fairness 360
  (IBM → LF AI & Data, July 2020); AIF360 pipeline `:625` Fig. 1; frontier `:672` Fig. 5(b).
- Model cards — `:765` — Mitchell et al. (9 authors incl. Raji, Gebru), FAT* 2019, Fig. 2.
- Datasheets — `:781` — Gebru et al., CACM Dec 2021 (Fig. 1 excerpt from the arXiv version).
- Audit process — `:796` — Raji, Smart, White, Mitchell, Gebru, Hutchinson, Smith-Loud,
  Theron, Barnes, "Closing the AI Accountability Gap" (SMACTR), FAT* 2020, Fig. 2.
- Gender Shades — `:824` — Buolamwini & Gebru, FAT* 2018 Table 4 (DF error
  20.8/34.5/34.7%; LM 0.0/0.8/0.3%); PPB faces `:813` Fig. 1; follow-up `:876` — Raji &
  Buolamwini, "Actionable Auditing", AIES 2019 (7 months, DF error 20.8→1.5 MSFT,
  34.5→4.1 Face++, 34.7→17.0 IBM; unaudited Amazon 31.4%, Kairos 22.5%); tables `:885`.
- Generative/LLM — `:944` Bianchi et al., FAccT 2023 Fig 1; `:971` Google blog Feb 2024
  (Gemini); `:989`/`:999`/`:1017` Tamkin et al. (Anthropic), 2023 (70 decisions; Figs. 1,
  2, 5; steering prompts → gap near zero, ~92% aligned); `:1035` Eloundou et al.
  (OpenAI), "First-Person Fairness in Chatbots", ICLR 2025 (<0.1% harmful stereotypes;
  ~3–12× reduction from post-training; Fig. 10); `:1053` Wilson & Caliskan, AIES 2024
  (85.1% White-associated names favored; **gender-only results inverted by the authors'
  29 Aug 2026 erratum, arXiv v3: female-associated names favored in 51.9% of tests,
  male in 11.1%** — slide, note and Fig. 2 caption follow v3); `:1066` Executive Order
  14319, July 2025.

**Figures (22 files, all cited with figure numbers; captured 2026-09 unless noted):**
`figs/reweighing-aif360.png` `:247` · `figs/feldman-repair.png` `:274` ·
`figs/reductions-frontier.png` `:354` · `figs/adversarial-gradients.png` `:415` ·
`figs/adversarial-adult-confusion.png` `:427` · `figs/hardt-fico-roc.png` `:465` ·
`figs/hardt-eo-threshold.png` `:517` · `figs/hardt-fico-cost.png` `:547` ·
`figs/aif360-pipeline.png` `:624` · `figs/aif360-frontier.png` `:664` ·
`figs/model-card-example.png` `:763` · `figs/datasheet-example.png` `:779` ·
`figs/smactr-audit.png` `:789` · `figs/ppb-faces.png` `:805` ·
`figs/gender-shades.png` (FAT* 2018 Table 4, verified against paper; 2026-08) `:822` ·
`figs/actionable-audit-tables.png` `:884` · `figs/bianchi-occupations.png` (FAccT 2023
Fig 1, shared with lec13; 2026-08) `:936` · `figs/tamkin-method.png` `:980` ·
`figs/tamkin-discrimination.png` `:997` · `figs/tamkin-interventions.png` `:1014` ·
`figs/eloundou-rl.png` `:1032` · `figs/resume-retrieval.png` `:1044`.
Inline SVGs (21): gap bars `:99`, pipeline `:121`, sealed model `:170`, data loop `:195`,
reweighing cells `:220`, relabeling scatter `:263`, λ slider `:314`, constraint curve
`:328`, reductions loop `:344`, wrapper `:374`, adversarial architecture `:385`,
thresholds `:494`, lending bells `:568`, demo tradeoff `:577`, frontier curve `:643`,
base-rate bars `:686`, impossibility Venn `:698`, record card `:747`, audit before/after
bars `:846`, assessment timeline `:899`, documentation timeline `:915`. Citations use
`.cite-left`.

**2026-09 figure pass (61→69):** every content slide now carries a cited public figure
or an inline SVG. Added 20 cropped figures (`figs/`, each cite names the source figure
or table) and 14 SVGs on previously bullet-only slides; 8 new "measured" slides hold
the source figures that would not fit beside existing bullets (Reweighing, Measured;
Reductions, Measured; Adversarial Debiasing, Measured; One Pipeline, Three Doors; The
Frontier, Measured; An Audit Needs a Benchmark; The Audit Worked: The Numbers;
Measured: Who Gets Favored). Content fix: **Screening Is Still Risky** — Wilson &
Caliskan's arXiv v3 (29 Aug 2026) erratum inverts every gender-only comparison, so
the bullet now reads "female-associated names in 51.9%, male in 11.1%" with a muted
erratum line; the 85.1% race result is unaffected. All edited slides screenshot-checked
at 60 dpi; `lint-deck.py` ok. Note synced (69 entries, `Slide figure:` line on each
figure/SVG slide; erratum reflected in the Screening entry).

**2026-08 content revision (55→61):** every citation/number fetched and verified.
Added 8 slides: What Post-Processing Needs (§04); Toolkits Ship These Methods (§04);
The Audit Worked (§06); Do LLMs Discriminate?, Prompting the Bias Away, Post-Training
as Mitigation, Screening Is Still Risky, Regulation Pulls Both Ways (§07). Removed 2:
overcorrection pair merged into one slide (case detail is lec13's); vague unverifiable
"Frontier 2025-26" slide deleted. Fixes: **adversarial debiasing misdescription**
(adversary "recovers the group from the features" → from the model's *prediction*,
per Zhang et al.; SVG and follow-up slide reworked, wrong "same as representation
repair" claim removed); **reweighing cite venue** "KIS 2012" → full journal name;
**Gender Shades reading slide** ("over a third" wrong for Microsoft at 20.8% →
verified ranges 0–0.8% vs 20.8–34.7%); **Bianchi slide** bullets matched to the actual
figure panels (software engineer / housekeeper) + full verified title, consistent with
lec13; §07 divider retitled Generative & LLM Fairness; Key Takeaways gained an LLM
line. Lending-demo numbers (72%/50%, 84%→80%, 22→2) are labeled illustrative.
`backup-fairness-mitigationtech.html` checked (see supplement table). Note file synced (61 entries, order
matches).

**2026-08 note enrichment:** `backup-fairness-mitigation-note.html` upgraded from speaker
script (383 lines) to Script &amp; Companion Notes (695 lines; 61 entries unchanged):
per-entry `.detail` blocks with rigorous definitions (fairness-gap functionals, derived
predictor Def 4.1, discrimination score, first-person fairness), proofs (reweighing
independence, massaging flip count, reductions Thm 1/3 sketch, adversarial Props 2–3
with entropy proofs, Hardt LP + ROC geometry + Prop 5.2/Cor 5.3, DP error lower bound),
and 23 verified links — consistent with `backup-fairness-mitigationtech.html` and the lec13 note (impossibility
proofs referenced, not duplicated).

## backup-governance.html

*Former Wk 15 deck, moved to backup 2026-10 (`git mv` of the former lec15-governance deck, its note and lec15tech to `backup-governance.html`, `backup-governance-note.html` and `backup-governancetech.html`; only the title-slide pill and page titles changed from "Lecture 15" to "Backup"). Line numbers unchanged by the move. Relabelled 2026-10 as an optional archival backup. The wrap-up and Demo Showcase are marked historical (slide title "Demo Showcase (Historical)"), and the note carries a legacy-numbering notice. There are no line shifts in the deck.*

**Topic:** Governance, the frontier & course wrap-up (~90 min, capstone). Nearly
math-free. Connects the course's threads via the trust stack (data → model → output →
society), then risk frameworks (NIST AI RMF + GenAI Profile), regulation (EU AI Act
incl. Digital Omnibus timeline and GPAI rules; US patchwork + executive-order
whiplash; Korea AI Basic Act; summits/AISIs + International AI Safety Report),
auditing & red-teaming incl. frontier-lab safety frameworks (Anthropic RSP/ASL,
OpenAI Preparedness, GDM FSF), open problems, and the wrap-up (five questions, Demo
Showcase kept, one lesson). Formal structures live in `backup-governancetech.html` (deliberately
light).

### Sections (70 slides, ~90 min — content-revised 2026-08 from 53; figure pass 2026-09 from 66; all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:27` | |
| **01 — Connect the Threads** | 3–13 | `:39` | trust stack (SVG) `:80` · data thread `:97` · **reliability thread (hallucination/calibration/interpretability; added 2026-08)** `:125` · adversary `:141` · accountability `:157` · the pattern `:173` · **Bommasani foundation-models stakes** `:214` · threads SVGs `:91` `:135` `:151` `:167` `:183` · **IASR Swiss-cheese figure (added 2026-09)** `:202` |
| **02 — Risk Frameworks** | 14–22 | `:238` | NIST AI RMF `:251` · four functions (SVG loop) `:276` · Map/Measure/Manage `:301` `:305` `:321` · **GenAI Profile (NIST AI 600-1, confabulation; added 2026-08)** `:337` · NIST 7-characteristics figure `:275` · 12-risk tiles `:363` |
| **03 — Regulation** | 23–43 | `:369` | **Weidinger taxonomy (4 of 6 risk areas)** `:381` · EU risk tiers (pyramid SVG) `:413` · banned `:447` · high risk `:461` · **EU timeline incl. Digital Omnibus deferral (SVG; added 2026-08)** `:493` · **GPAI rules + Code of Practice (added 2026-08)** `:534` · US patchwork `:551` · **US whiplash timeline (EO 14110→14179→14319→preemption push, SVG; added 2026-08)** `:555` · **Korea AI Basic Act ×2 (added 2026-08)** `:597` `:614` · Anderljung frontier regulation `:631` · **summit timeline (Bletchley→Seoul→Paris→New Delhi, SVG; added 2026-08)** `:661` · **International AI Safety Report (added 2026-08)** `:677` · **Weidinger six-area map `:403` · Commission risk pyramid `:451` · Anderljung lifecycle `:651` · IASR four challenges `:722` (all added 2026-09)** · EU conformity-steps graphic `:482` · Anderljung challenges `:640` · IASR benchmarks `:711` |
| **04 — Auditing & Red-Teaming** | 44–56 | `:735` | red-teaming `:760` · audit loop (SVG) `:777` · dangerous-capability evals `:781` · **frontier safety frameworks (if-then flow SVG; added 2026-08)** `:818` · **Anthropic RSP/ASL `:822` · OpenAI Preparedness v2 `:858` · GDM FSF v3 `:874` (all added 2026-08)** · model cards `:907` · audit limits `:926` · Shevlane Fig. 1 `:757` · Ganguli attack-success `:769` · nine-capability tiles `:816` · RSP CBRN table `:851` · Preparedness categories SVG `:872` · FSF CCL table `:883` · Shevlane audit workflow `:899` · Mitchell model card `:921` |
| **05 — Open Problems for 2026+** | 57–63 | `:942` | web-scale privacy `:975` · robust unlearning `:979` · agentic safety `:995` · provenance+fairness `:1024` · tensions `:1041` · IASR task-length `:967` · IASR agents survey `:1016` · IASR watermarks `:1033` |
| **06 — Wrap-Up** | 64–70 | `:1045` | reading an AI headline `:1054` · five questions `:1062` · **Demo Showcase (course logistics, kept)** `:1078` · one lesson `:1095` · key takeaways `:1111` · closer ("Thank you") `:1119` · headline SVG `:1072` · funnel SVG `:1089` |

**Key citations (all source-verified 2026-08):**
- Foundation models — `:236` — Bommasani et al., "On the Opportunities and Risks of
  Foundation Models", 2021 (arXiv 2108.07258).
- NIST — `:275`/`:301` AI RMF 1.0, 2023; `:363` Generative AI Profile (NIST AI 600-1),
  July 2024 (12 GenAI risks incl. confabulation).
- Taxonomy — `:399` — Weidinger et al., "Taxonomy of Risks Posed by Language Models",
  FAccT 2022 (six risk areas; slide shows four, intro says so).
- EU — `:447`/`:489` Regulation (EU) 2024/1689 (the AI Act); `:534` Regulation (EU)
  2026/1744 (Digital Omnibus on AI: high-risk duties → Dec 2027 / Aug 2028); `:551`
  General-Purpose AI Code of Practice, July 2025 (10^25 FLOP systemic-risk threshold).
- US — `:597` — Executive Orders 14110 (2023, rescinded), 14179 (Jan 2025), 14319
  (July 2025); Dec 2025 preemption push. No federal AI statute as of mid-2026.
- Korea — `:614`/`:631` — AI Basic Act, effective Jan 2026 (MSIT; high-impact AI;
  GenAI labeling; 10^26 FLOP duty threshold; fines ≤ 30M KRW, 1-year grace).
- Frontier — `:647`/`:816` Anderljung et al., "Frontier AI Regulation", 2023 (arXiv
  2307.03718); `:858` Anthropic RSP 2023 (rev. 2026) + ASL-3 activation May 2025
  (Claude Opus 4); `:872` OpenAI Preparedness Framework v2, Apr 2025; `:890` Google
  DeepMind Frontier Safety Framework v3, Sept 2025 (CCLs; added manipulation +
  misalignment).
- International — `:718` — International AI Safety Report, 2026 (Bengio chair, 100+
  experts, ~30 countries); summits slide `:661` (Bletchley 2023; Seoul 2024, 16 labs;
  Paris 2025; New Delhi 2026, 89 endorsers) verified against gov.uk/summit records.

**Figures (2026-09 figure pass):** 18 captured images in `figs/` (crops from the cited PDFs / Commission page; every cite names the figure or table number): iasr-swiss-cheese.png (IASR Fig. 3.5) `:202` · bommasani-centralize.png (Bommasani Fig. 2) `:236` · nist-characteristics.png (NIST AI RMF Fig. 4) `:275` · eu-risk-pyramid.jpg (Commission risk pyramid) `:455` · eu-high-risk-steps.jpg (Commission conformity steps) `:482` · anderljung-challenges.png (Anderljung Fig. 3) `:640` · anderljung-lifecycle.png (Anderljung Fig. 1) `:655` · iasr-benchmarks.png (IASR Fig. 1.4) `:711` · iasr-challenges.png (IASR Fig. 3.1) `:727` · shevlane-theory.png (Shevlane Fig. 1) `:757` · ganguli-attack-success.png (Ganguli Fig. 1) `:769` · rsp-cbrn-thresholds.png (Anthropic RSP v2.2 table) `:851` · gdm-cbrn-ccl.png (GDM FSF v3.1 Table 2.2.1.a) `:883` · shevlane-workflow.png (Shevlane Fig. 4) `:899` · model-card-example.png (Mitchell Fig. 2, shared with lec14) `:921` · iasr-task-length.png (IASR Fig. 1.7) `:967` · iasr-agents-survey.png (IASR Fig. 2.11) `:1016` · iasr-watermarks.png (IASR Fig. 3.8) `:1033`. Inline SVGs: trust stack `:102`, four threads `:91`, data thread `:135`, model-wrong thread `:151`, adversary `:167`, accountability `:183`, values→framework→steps `:260`, RMF loop `:285`, Map/Measure/Manage highlights `:315`, 12 GenAI risks `:363`, framework vs law `:376`, Weidinger six areas `:407`, risk bars `:423`, EU tier pyramid `:434`, banned uses `:471`, tier band `:504`, EU timeline `:513`, GPAI 10^25 threshold `:548`, US layers `:565`, US whiplash timeline `:576`, Korea timeline `:611`, EU vs Korea threshold `:628`, global compliance `:671`, summit timeline `:682`, audit loop `:786`, nine capabilities `:816`, if-then framework flow `:827`, Preparedness categories `:872`, card readers `:936`, audit limits `:949`, web-scale privacy `:989`, unlearning loop `:1005`, headline tree `:1072`, five-question funnel `:1089`. Citations use `.cite-left`.

**2026-08 content revision (53→66):** every citation/number/date fetched and verified
(EU/Korea/US law via primary or law-firm trackers; lab frameworks via anthropic.com,
cdn.openai.com PDF, deepmind.google). Added 13 slides: reliability thread (§01);
GenAI Profile (§02); EU timeline, GPAI rules, US whiplash, Korea Basic Act ×2, summit
timeline, International AI Safety Report (§03); frontier safety frameworks, Anthropic
ASL, OpenAI Preparedness, DeepMind FSF (§04). Fixes: **"social scoring of citizens by
governments" → "by public or private actors"** (Art 5 scope verified); **Weidinger
intro** now says four of the paper's six risk areas; EU cites normalized to
"Regulation (EU) 2024/1689"; US-approach slide rewritten (patchwork; first binding
rules from states); Key Takeaways gained EU/US/Korea + if-then-commitments lines;
trust-stack SVG gained reliability + society labels. Course-logistics Demo Showcase
slide kept per course scaffolding. `backup-governancetech.html` errors-only pass (EU cite fixed,
tier bullets de-dashed; still 6 sl). Note file synced (66 entries, order matches).

**2026-09 figure pass (66→70):** every content slide now carries a visual. 17 new cropped figures (International AI Safety Report 2026 ×6, Anderljung 2023 ×2, Shevlane 2023 ×2, NIST AI RMF, Bommasani 2021, Ganguli 2022, Anthropic RSP v2.2 table, GDM FSF v3.1 table, two European Commission graphics) plus the Mitchell model card reused from lec14; ~28 new inline SVGs on formerly bullet-only slides. Four slides added: **The Full Map: Six Areas** (Weidinger Table 1, all six areas named) `:403`; **The Commission's Own Picture** (EU risk pyramid) `:451`; **Where Rules Can Attach** (Anderljung Fig. 1 lifecycle) `:651`; **Why Governance Is Hard** (IASR Fig. 3.1) `:722`. Dense source tables (Shevlane Table 1, Weidinger Table 1, OpenAI Preparedness Table 1) are rendered as verified-name SVG summaries citing the table rather than as unreadable crops. The GDM FSF PDF on hand is Version 3.1 (Apr 2026); the table cite says so explicitly while the author's "v3, 2025" text cite is untouched. No author bullets rewritten; two new muted lines trimmed to the 7×7 ceiling. Note file: 70 entries (4 new articles + 46 "Slide figure" lines), order matches. 60-dpi render check of all 46 edited slides passed after fixes (threads SVG height, Korea-threshold labels, lifecycle image width, headline SVG width, funnel contrast).

**2026-08 note enrichment:** `backup-governance-note.html` upgraded from speaker script
(413 lines) to Script &amp; Companion Notes (737 lines; 66 entries unchanged). Nearly
math-free deck, so depth went to verbatim legal/framework language and verified
backgrounds+links rather than proofs: AI Act Art 3 definitions quoted verbatim (AI
system, provider, deployer, GPAI model, systemic risk, conformity assessment), Art 5
prohibition list, Art 50 duties, Art 51 10^25 presumption, Arts 53/55 GPAI duties,
Digital Omnibus (Reg (EU) 2026/1744) deferral detail; NIST AI 100-1 verbatim (risk
def, 7 trustworthiness characteristics, all four function definitions) + AI 600-1
(confabulation def, full 12-risk list); all four US EOs (14110/14179/14319/14365)
with FR citations + Action Plan; Korea Basic Act detail (CSET translation); four
summits + Seoul commitments verbatim; RSP v3.4/ASL-3 activation, Preparedness v2
(severe-harm def verbatim), FSF v3 CCL def verbatim; audit/red-team terms of art
(Raji, EO 14110 red-teaming def, Dijkstra EWD340 dictum); course-thread definitions
((ε,δ)-DP, ECE, adversarial/poisoning/jailbreak, fairness criteria, certified
removal) cross-linked to lec02–14 companion notes. 51 verified links (all 2xx;
EUR-Lex returns 202 to curl, fine in browser).

## backup-interpretability.html

*Former Wk 7 deck, moved to backup 2026-10 (`git mv` of the former lec07 interpretability deck; tech and note renamed alongside). Line numbers unchanged by the move.*

**Topic:** Interpretability & explainability (~90 min). Why black-box accuracy alone
does not earn trust; intrinsic vs post-hoc taxonomy plus the Rudin objection; feature
attribution at intuition level (LIME local surrogate, SHAP/Shapley fair credit, gradient
saliency, integrated gradients, Adebayo sanity-check failures); probing and the
attention-is-(not-(not-))explanation debate; mechanistic interpretability (circuits,
induction heads, superposition); sparse autoencoders, monosemantic features, Golden Gate
Claude, feature steering; uses & limits (GDPR / "right to explanation" nuance,
faithfulness, 2025–26 frontier: attribution graphs, CoT faithfulness, Amodei essay).
Math lives in `backup-interpretabilitytech.html`.

### Sections (64 slides, ~90 min — content-revised 2026-08 from 57, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — The Black Box** | 3–10 | `:72` | black box `:80` · why open it up `:110` · **Husky and the Wolf (reframed 2026-08: rigged demo, trust 10/27→3/27)** `:123` · intrinsic vs post-hoc `:140` · accuracy trade-off (SVG) `:155` · **The Rudin Objection (added 2026-08)** `:178` · explanation is not the model `:195` |
| **02 — Feature Attribution** | 11–25 | `:218` | attribution question `:226` · bar chart (SVG) `:257` · LIME `:280` · local-not-global (LIME Fig 3) `:294` · SHAP `:304` · Shapley value `:318` · why trusted `:352` · loan demo `:381` · saliency on images (Simonyan Fig 2) `:396` · gradient saliency `:413` · **Beyond Raw Gradients (IG; added 2026-08)** `:447` · saliency Colab `:464` · what attribution answers `:479` · Adebayo sanity check `:491` |
| **03 — Probing & Attention** | 26–33 | `:502` | hidden layers `:510` · linear probes `:540` · reading the probe `:556` · attention weights (Clark Fig 1) `:574` · looks like explanation `:584` · not explanation (Jain & Wallace) `:613` · **...Is Not Not Explanation (added 2026-08)** `:623` |
| **04 — Mechanistic Interpretability** | 34–43 | `:651` | different goal `:659` · circuits (Olah car-detector) `:689` · neurons as concepts `:699` · transformer framework `:714` · induction heads `:749` · induction in action `:765` · why induction matters (+Olsson cite added 2026-08) `:784` · polysemantic wall `:811` · superposition (+Elhage cite added 2026-08) `:822` |
| **05 — Sparse Autoencoders & Steering** | 44–52 | `:838` | unpacking superposition `:846` · SAE (SVG) `:861` · monosemantic features `:885` · **Scaling Up (Claude 3 Sonnet; verified examples 2026-08)** `:913` · feature steering (SVG) `:942` · Golden Gate Claude `:961` · steering widget `:989` · **Steering for Safety (hedged + cited 2026-08)** `:1004` |
| **06 — Uses & Limits** | 53–63 | `:1037` | what it buys us `:1045` · **What the Law Demands (GDPR Art. 22 / Arts. 13–15; added 2026-08)** `:1056` · **A "Right to Explanation"? (added 2026-08)** `:1070` · faithfulness problem `:1101` · models can rationalize `:1125` · always sanity-check `:1153` · **Frontier: Attribution Graphs (added 2026-08)** `:1168` · **Frontier: CoT faithfulness (added 2026-08)** `:1185` · **Frontier: An MRI for AI (added 2026-08)** `:1198` · key takeaways `:1227` |
| Closer | 64 | — | `:1240` |

**Key definitions / citations (all source-verified 2026-08):**
- LIME + husky/wolf experiment (rigged snow demo; trust 10/27→3/27) — `:134`, `:289` —
  Ribeiro, Singh, and Guestrin, "Why Should I Trust You?", KDD 2016 (§6.4, Table 2).
- Interpretable-by-design for high stakes — `:189` — Rudin, Nature Machine
  Intelligence 1, 206–215 (2019).
- SHAP / Shapley uniqueness — `:313`, `:348` — Lundberg and Lee, NeurIPS 2017.
- Integrated gradients — `:458` — Sundararajan, Taly, and Yan, ICML 2017.
- Saliency sanity checks (weight randomization) — `:496` — Adebayo et al., NeurIPS 2018.
- Attention debate — `:619` Jain and Wallace, NAACL 2019; `:646` Wiegreffe and Pinter,
  EMNLP 2019.
- Circuits / curve & dog-head detectors — `:695`, `:710` — Olah et al., "Zoom In",
  Distill 2020.
- Transformer framework + induction heads — `:745`, `:759` — Elhage et al., Anthropic 2021.
- Induction heads ↔ in-context learning — `:807` — Olsson et al., Anthropic 2022.
- Superposition — `:832` — Elhage et al., "Toy Models of Superposition", Anthropic 2022.
- SAE / monosemantic features (DNA, legal language, base64) — `:881`, `:909` —
  Bricken et al., "Towards Monosemanticity", Anthropic 2023.
- Millions of features in Claude 3 Sonnet; Golden Gate Claude; safety-relevant
  features — `:938`–`:1032` — Templeton et al., "Scaling Monosemanticity", Anthropic 2024.
- GDPR Art. 22 + Arts. 13–15; recital-only "right to explanation"; EU AI Act Art. 86 —
  `:1056`–`:1097` — Wachter, Mittelstadt, and Floridi, International Data Privacy Law
  7(2):76–99 (2017); AI Act text (Art. 86, applies from Aug 2026).
- Attribution graphs (Dallas→Texas→Austin; rhyme planning; Neuronpedia) — `:1179` —
  Lindsey et al., "On the Biology of a Large Language Model", Anthropic 2025;
  circuit-tracing tools open-sourced May 2025.
- CoT faithfulness (hint admitted <20% of the time) — `:1192` — Chen et al., "Reasoning
  Models Don't Always Say What They Think", Anthropic 2025 (arXiv 2505.05410).
- "MRI for AI"; detect most model problems by 2027 — `:1223` — Amodei, "The Urgency of
  Interpretability", April 2025.

**Real images** (`figs/`, cropped + cited; 23 image slots after the 2026-09 figure pass):
husky/wolf + explanation `figs/lime-fig11-husky.png` (Ribeiro 2016 Fig 11) `:134`; CORELS rule list
`figs/rudin-fig3-corels.png` (Rudin 2019 Fig 3) `:150`; "fictional" trade-off `figs/rudin-fig1-tradeoff.png`
(Rudin Fig 1) `:189`; LIME pipeline `figs/lime-fig1-flu.png` (Ribeiro Fig 1) `:289`; LIME local fit
`figs/lime-fig3-local.png` (Ribeiro Fig 3) `:298`; SHAP additive steps `figs/shap-fig1-additive.png`
(Lundberg & Lee 2017 Fig 1) `:313`; class saliency maps `figs/simonyan-fig2-saliency.png` (Simonyan 2014
Fig 2) `:407`; IG vs gradients `figs/ig-fig2-compare.png` (Sundararajan 2017 Fig 2, top 3 rows) `:458`;
cascading randomization `figs/adebayo-fig2-cascade.png` (Adebayo 2018 Fig 2) `:496`; ResNet-50 probe error
`figs/alain-fig4-resnet.png` (Alain & Bengio 2017 Fig 4) `:550`; control task `figs/hewitt-fig1-control.png`
(Hewitt & Liang 2019 Fig 1) `:568`; BERT heads `figs/clark-fig1-heads.png` (Clark 2019 Fig 1) `:578`;
adversarial attention `figs/jain-fig1-attention.png` (Jain & Wallace 2019 Fig 1) `:617`; car-detector
circuit `figs/olah-zoomin-car.png` (Olah 2020) `:693`; curve detectors `figs/olah-zoomin-curves.png`
(Olah 2020) `:708`; induction-head schematic `figs/lindsey-induction-head.png` (Lindsey 2025, Limitations)
`:759`; induction on random tokens `figs/olsson-induction-head.png` (Olsson 2022) `:778`; superposition
projection `figs/elhage-toy-projection.png` (Elhage 2022) `:816`; sparsity → superposition
`figs/elhage-toy-sparsity.png` (Elhage 2022) `:831`; SAE pipeline `figs/cunningham-fig1-sae.png`
(Cunningham 2024 Fig 1) `:855`; edge-detector comparison `figs/adebayo-fig1-edge.png` (Adebayo Fig 1)
`:1162`; Dallas→Austin attribution graph `figs/lindsey-dallas-austin.png` (Lindsey 2025) `:1179`; CoT
faithfulness bars `figs/chen-fig1-faithfulness.png` (Chen 2025 Fig 1) `:1192`.
**SVG** (24): black box `:90`, accuracy trade-off `:160`, model vs story `:200`, signed attribution `:235`,
attribution bar chart `:262`, Shapley orderings `:328`, efficiency bar `:362`, steep vs flat slope `:423`,
layers → activation vector `:520`, attention arcs `:594`, 2019 debate timeline `:633`, describe vs explain
`:668`, residual stream `:724`, loss curve with induction bump `:794`, SAE widen-rebuild `:866`,
feature-activation bars `:895`, scaling 2023→2024 `:923`, steering dial `:947`, Golden Gate dial `:971`,
safety dial in three steps `:1014`, GDPR recital / articles / AI Act boxes `:1080`, plausible vs faithful
ellipses `:1107`, answer vs "because…" story `:1135`, 2025→2027 MRI timeline `:1208`. Citations use
`.cite-left`. Page number: bold `.slide-num` only.

**2026-09 figure pass (64 slides, unchanged count; PR #24):** every bullet-only content slide now carries
a cited real figure crop or an inline SVG (23 new crops, 20 new SVGs; 4 hand-drawn sketch SVGs — LIME
local line, saliency pair, attention lines, circuit graph — replaced by the papers' own figures). Real
figures sit beside the bullets in a `1fr auto` grid or stacked below them; every crop is trimmed of white
margins, excludes the paper caption, and is cited with its figure number (or the named figure for Distill /
Anthropic web papers). Two bullets added (Saliency on Images ×3, Reading the Probe control task). Note
file: one "Slide figure" sentence per real-figure article (23); 64 entries, order matches.

**2026-08 content revision (57→64):** every citation/number fetched and verified.
Added 8 slides: The Rudin Objection (§01), Beyond Raw Gradients (§02), ...Is Not Not
Explanation (§03), What the Law Demands + A "Right to Explanation"? (§06), and three
frontier slides (§06: Attribution Graphs, CoT faithfulness, An MRI for AI — replacing
one stale unverifiable "Frontier 2025–26" slide). Fixed: husky/wolf reframed as the
deliberately rigged demo it was, with verified trust numbers; unverified "emotions"
feature example replaced by verified "scam emails" (Templeton 2024); Steering for
Safety hedged ("could", "still early days") and cited; missing Olsson and Elhage
(superposition) cites added. `backup-interpretabilitytech.html` (then `lec07tech.html`) audited: all math correct, no changes
(stays 20 sl). Note file synced (64 entries, order matches).

**2026-08 note enrichment:** `backup-interpretability-note.html` (then the lec07 interpretability note) upgraded from speaker
script (401 lines) to Script &amp; Companion Notes (773 lines; 64 entries unchanged):
per-entry `.detail` blocks with rigorous definitions (additive feature attribution
class, full LIME objective + K-LASSO, cooperative game + SHAP conditional-expectation
value, gradient saliency + Taylor rationale, IG path integral + Sensitivity(a)/
Implementation Invariance, linear probes + control tasks/selectivity + linear
representation hypothesis, scaled dot-product attention, residual stream + QK/OV
circuits, induction-head two-head mechanism, polysemanticity/privileged basis,
superposition hypothesis, dictionary learning, exact Bricken SAE equations + loss,
feature clamping, GDPR Art. 22(1) + Arts. 13–15 verbatim, faithfulness vs
plausibility), theorem blocks with verified proofs (Shapley subset↔permutation
equivalence + full existence/uniqueness via unanimity basis, labeled course notes;
SHAP Theorem 1 statement; IG Completeness with full FTC proof + Prop 2 pointer), and
Background blocks with 35 verified links (LIME/SHAP/IG/Adebayo/probing/attention-debate
arXiv, five transformer-circuits.pub papers, Golden Gate Claude, Neuronpedia +
Gemma Scope, GDPR/AI-Act texts, Wachter DOI, biology-of-LLM + circuit-tracing
open-sourcing, Chen CoT faithfulness, Amodei essay).
