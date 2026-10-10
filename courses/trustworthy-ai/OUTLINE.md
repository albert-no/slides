# trustworthy-ai/ — Trustworthy AI course

Undergraduate course for sophomores/juniors (15 weeks × 1.5 hr), mixed majors with
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
| 4. Provenance & Fairness | 12–14 | Watermarking, fairness, accountability |
| 5. Synthesis | 15 | Governance, frontier, demo showcase |

## Lecture index

| Wk | File | Topic | Status |
|---|---|---|---|
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **case-brief pass 2026-09-13** (46 sl, ~40 min; note 46 briefs, 80 links checked) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **case-brief pass 2026-09-13** (69 sl, ~75 min, 11 figs, `demos/rr-simulator.html`; note 69 entries — 16 case briefs with setup/verification/limits/status; tech 23 sl) |
| 3 | `lec03-mia.html` | Membership inference attacks | **case-brief pass 2026-09-13** (70 sl, 16 real figs, Homer 2008 block + NIH 2008→2018 chronology, TPR/FPR/ROC/AUC + base-rate block, LiRA-on-LLMs, boardroom questions) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **revised 2026-08, figure pass 2026-09, Cooper 2026 frontier 2026-09-11, case-brief + core-path pass 2026-09-14** (65 sl, 27 real figs) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **figures 2026-09, case-brief + core-path pass 2026-09-14, page edits 2026-09-30** (68 sl, ~97 min; 90-min core path in the note only; taxonomy + category badges; note 68 entries, 13 uniform briefs + legal brief; tech 12 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **figures 2026-09, Albert revision 2026-10** (75 sl after round 4: Avianca context, P(True) explained, two kinds of calibration, fair-rank intuition replaces proof; heavy math moved to lec06tech; note 75 entries) |
| 7 | `lec07-alignment-failures.html` | Alignment failures: sycophancy, reward hacking, explanation faithfulness | **new 2026-10** (59 sl, 14 real figure crops from 10 source figures, 90 min, no activities; note 59 entries; tech 12 sl). Former Wk 7 interpretability deck → `backup-interpretability.html` |
| 8 | `lec08-adversarial.html` | Adversarial robustness: threat models, FGSM → PGD, honest evaluation, certificates | **new 2026-10** (55 sl, 15 real figure crops + 2 charts redrawn from tables, 90 min, no activities; note 55 entries; tech 24 sl) |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **rebuilt 2026-10** (59 sl, 90 min, concept-first, no activities) |
| 10 | `lec10-jailbreak.html` | Jailbreaks: safety training, fragility, search, budget, evaluation & defenses | **rebuilt 2026-10** (58 sl, 90 min, concept-first, no activities; note 58 entries; tech 21 sl) |
| 11 | `lec11-synthetic-media.html` | Synthetic media: text watermarks, robustness, detection without a watermark, provenance (C2PA) & labelling law | **new 2026-10** (56 sl, 8 real figure crops + 5 tables/figures redrawn, 90 min, concept-first, no activities; note 56 entries; tech 13 sl). Former Wk 11 prompt injection → rebuilt as Wk 13; former Wk 12 watermark deck replaced |
| 12 | `lec12-fairness.html` | Fairness: where bias enters, criteria, COMPAS and impossibility, mitigation, audits beyond classifiers | **new 2026-10** (56 sl, 17 real figure crops, 90 min, concept-first, no activities; note 56 entries; tech 17 sl). Merges the former Wk 13–14 fairness decks → `backup-fairness-defs.html`, `backup-fairness-mitigation.html` |
| 13 | `lec13-prompt-injection.html` | Prompt injection: direct and indirect, agents, three incidents, why it is hard, measured defenses and CaMeL | **new 2026-10** (53 sl, 7 real figure crops, 90 min, concept-first, no activities; note 53 entries; tech 15 sl). Replaces `backup-prompt-injection.html` (deleted) |
| 14 | — | (slot reserved: emerging autonomous and multi-agent systems) | |
| 15 | `lec15-governance.html` | Governance, frontier & demo showcase | **revised 2026-08, figure pass 2026-09** (70 sl) |

Every deck has a companion **speaker script** `lecNN-…-note.html` (one entry per slide:
title + 1–2 sentence script + **Key takeaway**). Scripts also exist for lec 1–2.
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
| `lec11tech.html` | Wk 11 (synthetic media) | green-list rule (KGW Alg. 2); idealized Binomial null + assumptions; z &gt; 4 ≈ 3×10⁻⁵ (normal approx.) vs exact tail at T = 20; √T growth under constant green rate; repeated pairs, nominal vs measured FPR (K24 App. A.3, Fig. 7); base-rate formula; TV bound AUROC ≤ ½+TV−TV²/2 (TV defined; keyed detectors); distortion-free vs undetectable | **new 2026-10** (13 sl; formulas checked against the saved papers) |
| `lec12tech.html` | Wk 12 (fairness) | four rates per group (with positivity); five criteria written out; Dwork (D,d)-Lipschitz (Def. 2.1); Kusner counterfactual fairness (Def. 5); calibration vs PPV via the score mix; Chouldechova identity (eq. 2.6); Kleinberg proof sketch; worked example computed; reweighing; reductions saddle point; Hardt derived predictor | **new 2026-10** (17 sl; formulas checked against the saved papers) |
| `lec13tech.html` | Wk 13 (prompt injection) | trusted vs attacker-controlled state; PI-SEC game and $\Omega_p$ (CaMeL §4); control vs data part of an action; confused deputy and least privilege; capability labels, propagation, STRICT mode; dual LLM → CaMeL policy check; conditional guarantee; AgentDojo BU / UA / ASR; static vs adaptive ASR with budget $q$ | **new 2026-10** (15 sl; checked against the saved papers) |
| `backup-fairness-defstech.html` | former Wk 13 (fairness defs) | demographic parity / equalized odds / calibration as conditional-prob defs; base rates; impossibility theorem (Chouldechova/Kleinberg) + proof sketch | **fixed 2026-08** (15 sl: base-rate identity was inverted (1−p)/p → p/(1−p) per Chouldechova eq 2.6; proof-sketch step 1 corrected (calibration ≠ "PPV = base rate" → predictive parity demands equal PPV across groups); unverifiable numeric-wedge table replaced with an exactly derivable two-value-score construction; impossibility attribution now dual Chouldechova + Kleinberg) |
| `backup-fairness-mitigationtech.html` | former Wk 14 (fairness mitigation) | reweighing w(g,y); penalized min Loss+λ·Unfairness; constrained form; reductions (Agarwal 2018); post-processing per-group thresholds (Hardt 2016) | **checked 2026-08** (17 sl: reweighing formula verified against Kamiran & Calders; reductions + Hardt ROC intuition verified against papers; one fix — cite venue "KIS 2012" → "Knowledge and Information Systems 2012") |
| `lec15tech.html` | Wk 15 (governance) | EU AI Act risk-tier taxonomy; NIST RMF as Govern→Map→Measure→Manage loop; what "measurable" audit metrics mean (deliberately light — governance is non-mathematical) | **checked 2026-08** (6 sl: tiers verified still accurate post-Omnibus; EU cite normalized; tier bullets de-dashed for lint) |

## Backup / swap-in materials (not in the 15-week core)

Optional decks for substitution or extra sessions. Each has a `-note.html` script.

| File | Topic | Slots in where | Status |
|---|---|---|---|
| `backup-sycophancy.html` | Sycophancy, manipulation & persuasion | merge into Wk 6, or standalone | **drafted** (38 sl) |
| `backup-copyright.html` | Copyright, consent & data provenance | pairs with Wk 4 (memorization) | **drafted** (45 sl) |
| `backup-agentic-autonomy.html` | Agentic autonomy risks beyond injection | follows Wk 13 (prompt injection); to be rebuilt as Wk 14 | **drafted** (47 sl) |
| `backup-model-stealing.html` | Model stealing / extraction attacks | swap for Wk 9, or standalone | **drafted** (51 sl) |
| `backup-interpretability.html` | Interpretability & explainability (LIME/SHAP, probes, circuits, SAEs) | former Wk 7 (moved 2026-10); standalone extra session | **revised 2026-08, figure pass 2026-09** (64 sl, 23 real figs; note `backup-interpretability-note.html`; tech `backup-interpretabilitytech.html`, 20 sl). Section `## backup-interpretability.html` below |

**Draft note:** lec 3–15 + backups were generated in one parallel pass (each ~50–60
slides, lint-clean, with SVG concept diagrams + cited papers). The **2026-07-15 pass**
de-technicalized the drafts for the undergrad audience, trimmed lec02 to fit 90 min,
and completed the real-figure pass — **all `TODO real figure` markers are now resolved**
(every deck lint-clean). The per-slide screenshot audit is the remaining polish step.

**2026-07-15 real-figure pass (complete).** Every TODO marker replaced with a real,
cropped-and-cited paper figure or a data-backed SVG:
- `lec03` 16 real figures (Salem, Yeom, Shokri, Carlini 2022 ×3, Choquette-Choo, Hayes LLM-MIA Fig. 2, Steinke, Shi, Carlini diffusion, Duan, Das, Hayes, Maini, Zhang) — see its section.
- `lec08` panda→gibbon (`figs/panda-gibbon.png`) + Eykholt stop-sign (`figs/eykholt-stopsign.png`, CVPR 2018 Fig 1).
- `lec09` BadNets trigger strip (`figs/badnets-trigger.png`, Gu et al. 2017 Fig 7).
- `lec10` Wei failure modes (`figs/wei-jailbroken-redacted.png`, NeurIPS 2023 Fig 1, attack wording redacted), GCG schematic (`figs/gcg-schematic.png`, Zou 2023 Fig 1); 2026-10 rebuild: 13 cited image files in total — see its section.
- `lec12` (2026-10): 17 cited crops — see its section. Former fairness decks (now `backup-fairness-defs`/`backup-fairness-mitigation`): Bianchi occupation grid (`figs/bianchi-occupations.png`, FAccT 2023 Fig 1); `lec14` Gender Shades table (`figs/gender-shades.png`, FAT* 2018 Table 4). backup-fairness-defs COMPAS TODO removed (illustrative SVG kept — real news graphic is copyrighted).
- `backup-fairness-mitigation` (former lec14) figure pass 2026-09: 20 cited crops (AIF360 Figs. 1/4/5, Feldman Fig. 1, Agarwal Fig. 1, Zhang Fig. 2 + Table 3, Hardt Figs. 2/10/11, model card + datasheet examples, SMACTR Fig. 2, PPB faces, Actionable Auditing Tables 1–2, Tamkin Figs. 1/2/5, Eloundou Fig. 10, Wilson & Caliskan Fig. 2) + 14 SVGs; see the backup-fairness-mitigation section.
- `lec06` Vectara HHEM hallucination bar chart (inline SVG, data Sep 22, 2026).
- `backup-copyright` Somepalli pairs (`figs/somepalli-pairs.png`, CVPR 2023 Fig 1); `backup-sycophancy` Sharma preference forest plot (`figs/sharma-sycophancy.png`, ICLR 2024 Fig 5); `backup-model-stealing` Knockoff pipeline (`figs/knockoff-pipeline.png`, CVPR 2019 Fig 2) + SVD hidden-dim plot (`figs/stealing-projection.png`, Carlini ICML 2024 Fig 1); `backup-agentic-autonomy` CoinRun panel (`figs/coinrun-misgeneralization.png`, Langosco et al. ICML 2022 Fig 1).

*Housekeeping:* `figs/somepalli_histograms.png` (1450px) is an unused orphan from the
original draft — safe to delete. All embedded figures are ≤1200px (bundle-safe).

## Cross-folder reuse

This course is the **light, general-audience** pass over topics treated rigorously
elsewhere. Reuse / differentiate against:

- **DP** (Wk 2) ↔ `courses/privacy/lectures/01-dp/` (8-deck rigorous series). Lec 2
  is intuition-only; it points students to the privacy course for the formal treatment.
- **MIA** (Wk 3) ↔ `courses/privacy/lectures/04-mia/` (5 lectures + notes).
- **Memorization** (Wk 4) ↔ `courses/privacy/lectures/03-memorization/`.
- **Unlearning** (Wk 5) ↔ `courses/privacy/lectures/05-unlearning/` and the ICML
  position talk `talks/icml2026/`.
- **Watermark** (Wk 11) ↔ `courses/privacy/lectures/06-watermark/`.

When drafting a stub, read the corresponding leaf `OUTLINE.md` there first and
**compress, don't re-derive** — link back rather than restating proofs.

---

## lec01-introduction.html

**Topic:** Motivational course overview (~40 min). Capability outran trust; a long
examples-first middle (one real incident per trust dimension, balanced across fairness,
privacy, reliability, robustness, security, safety, provenance, data ownership, society);
why learned systems fail differently; threat-model thinking
(who / knows / can do; knowledge × timing); the trust stack and the fifteen-topic map.
Sets the vocabulary used all term.

### Sections (46 slides, ~40 min — rebuilt 2026-09-03 from the 35-slide 2026-08 deck, trimmed 2026-09-04, case-brief pass 2026-09-13; "scary examples" originally imported from `talks/sangnam2609/sangnam1-ai-today.html`, all re-verified against primary sources 2026-09-13)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:30`, `:42` | |
| **01 — Where Bias Enters** | 3–10 | `:74` | Obermeyer cost proxy `:83` · model learns its world `:108` · three places `:125` · sampling (Gender Shades composition) `:141` · label problem `:164` · feedback loop `:181` · drop race fails `:207` |
| **02 — Measuring Fairness** | 11–21 | `:229` | notation (Y = recorded outcome) `:236` · four rates `:253` · demographic parity `:287` · equalized odds `:306`, `:321` · Hardt ROC plane `:343` · calibration `:355` · calibration vs PPV `:370` · five criteria `:387` · FICO thresholds `:402` |
| **03 — COMPAS and Impossibility** | 22–34 | `:414` | what COMPAS is `:421` · FPR by group `:440` · within subgroups `:463` · Northpointe, read by row `:482` · different criteria `:496` · rearrest ≠ offending `:513` · base rates `:530` · Chouldechova `:548` · Kleinberg `:566` · worked example `:580` · why the gap appears here `:605` · context `:627` |
| **04 — Mitigation** | 35–45 | `:644` | three places `:651` · reweighing `:683`, `:699`, `:718` · reductions `:732`, `:748` · group thresholds `:764` · FICO cost `:775` · empirical tradeoff ≠ optimal frontier `:794` · method cards `:810` |
| **05 — Beyond Classifiers** | 46–52 | `:824` | Gender Shades (Table 4 redrawn as SVG) `:831` · after the audit `:843` · BBQ `:882`, `:901` · Bianchi `:913` · governance `:932` |
| **06 — Synthesis** | 53–56 | `:948` | checklist `:955` · takeaways `:969` · closer "Which rate?" `:983` |

**Key citations (checked against saved PDFs / page captures, 2026-10-10; register in the
review package):** Goodfellow 2015 (Figs 1, 2, 4; §3); Szegedy 2014 (Fig 5); Ilyas 2019 (Fig 1);
Papernot 2016 (Fig 3; §5, Tables 3–4); Madry 2018 (Figs 1, 3; Table 2; ℓ2 appendix); Carlini &
Wagner 2017 (notes/tech); Tsipras 2019 (Fig 1); Athalye 2018 (Table 1; §4 BPDA/EOT); Athalye
EOT 2018; Carlini 2019 checklist; Tramèr 2020; Croce & Hein 2020 (AutoAttack; 13 of 49 >10 pts);
Croce 2021 RobustBench (§3 restrictions); robustbench.github.io CIFAR-10 ℓ∞ snapshot 10 Oct 2026;
Cohen 2019 (Figs 2–3, Thm 1, CERTIFY, Table 1, App. Table 2); Eykholt 2018 (Fig 1; Table 1 lab 100%,
Table 3 drive-by 100/84.8%, constrained pseudo-random crop 70%); Hendrycks & Dietterich 2019 (Fig 1).

**Note:** `lec08-adversarial-note.html` — 55 entries; each has a minute budget and elapsed
time, script, key takeaway; content slides add figure / setup-model-date / establishes / does
not establish / assumptions / primary-source links. C&W formulation in entries 22 and 29.

**Tech:** `lec08tech.html` — 24 slides: perturbation set (4), goals (5), FGSM (6), sign as the
linearized optimum incl. ℓ2 (7), linear model $w^\top\eta=\varepsilon\|w\|_1$ (8), PGD with random
start (9), projections (10), C&W (11), margin loss (12), min-max (14), Danskin with its smooth/unique-maximizer condition (15), cost (16),
smoothed classifier (18), Cohen Thm 1 (19), Neyman–Pearson proof sketch (20), CERTIFY with
Clopper–Pearson and α (21), radius reading (22), cost/scope (23).

## lec09-poisoning.html

**Topic:** Data poisoning and backdoors (90 min; mixed-major sophomores/juniors; concept-first,
light math, no proofs; **no activities**). Hook: the BadNets stop sign (Gu Fig 8). Poisoning is
how and a backdoor is what (Venn); three framing questions (who writes the data, what the attacker
wants, how it's measured). Availability vs targeted (Biggio Figs 1, 3); clean-label feature collision
(Poison Frogs Figs 6a, 1, 3b: one poison, 100% of 1,099 trials in transfer; about 60% with 50 poisons end to end;
limits slide). BadNets (Figs 3, 6, 4, 7, 1). ASR is defined per mapping (all-to-one, source-specific, all-to-all), plus an illustrative 7 → 1 worked example. Web scale: Carlini split-view (est. $60/yr → 0.01% of
LAION-400M URLs) separates access cost from damage; frontrunning (Fig 6; 6.5% is a qualified estimate); 2022 hash snapshot vs post-disclosure (Table 1 as HTML). Wan
instruction tuning (one train + one test row of Fig 1). Souly: 250 docs ≈ 420k tokens, a shrinking *token* fraction (12B → 0.0035%, 260B → 0.00016%); the
pretraining trigger → gibberish DoS backdoor (Fig 1a); Fig 2 with legend (perplexity rise, not ASR); scope slide. Sleeper Agents: installation separate from
persistence. Glaze ≠ Nightshade (different metrics, no cross-comparable numbers). Defenses: hashes catch changes, not
pre-existing poison; spectral signatures and Neural Cleanse in depth (needs/assumes/fails); the
rest in the notes table. Closing five-question checklist applied to the $60 claim. Excludes
adversarial examples (lec08), jailbreaks (lec10), prompt injection (lec13). Math in `lec09tech.html`.

### Sections (59 slides, 90 min: attack surface 10 · poisoning 20 · backdoors 20 · web scale + LLMs 20 · defenses + synthesis 20)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:30`, `:42` | |
| **01 — The Data Is the Attack Surface** | 3–8 | `:71` | stop sign (Gu Fig 8) `:79` · sticker meaning `:95` · strangers' data `:103` · Venn: poisoning vs backdoor `:111` · three questions `:119` |
| **02 — Data Poisoning** | 9–19 | `:128` | two goals `:136` · boundary tilt `:144` · Biggio Fig 1 `:152` · Biggio Fig 3 `:162` · targeted `:178` · clean label (Frogs Fig 6a) `:186` · fish/dog `:202` · one poison (Frogs Fig 1) `:210` · 50 poisons (Frogs Fig 3b) `:226` · did / did not show `:236` |
| **03 — Backdoors and Triggers** | 20–31 | `:258` | hidden "if" `:266` · BadNets Fig 3 `:274` · ASR by mapping `:284` · all-to-all Fig 6 `:298` · Fig 4 `:314` · worked example 7 → 1 `:323`, `:331` · traffic-sign trigger (Fig 7) `:345` · invisible triggers `:355` · shortcut `:363` · who can plant (Fig 1) `:372` |
| **04 — Web-Scale and Language Models** | 32–46 | `:382` | lists of links `:390` · est. $60/yr (Carlini Fig 1) `:398` · access ≠ damage `:415` · frontrunning (Fig 6) `:424` · 2022 hashes (Table 1, HTML) `:440` · Wan Fig 1 rows `:456` · 250 docs token-fraction table `:469` · Souly Fig 1a `:484` · Souly Fig 2 `:494` · does/does not say `:503` · Sleeper Fig 1 stage 1 `:524` · Fig 2a `:541` · got in vs stayed `:557` · Glaze vs Nightshade `:576` |
| **05 — Defenses, and What to Ask** | 47–59 | `:592` | three places to defend `:600` · hashes `:608` · spectral (Tran Fig 3) `:617` · Tran Fig 1 `:631` · spectral needs/assumes/fails `:643` · Neural Cleanse `:657` · NC needs/assumes/fails `:666` · five questions `:680` · applied to $60 `:688` · established vs open `:703` · takeaways `:723` · closer `:737` |

**Key citations (checked against saved PDFs, 2026-10-10; register in the review package):** Gu,
Dolan-Gavitt & Garg 2017 (BadNets; Figs 1, 3, 4, 6, 7, 8); Biggio, Nelson & Laskov ICML 2012 (Figs 1, 3);
Shafahi et al. NeurIPS 2018 (Figs 1, 3b, 6a; Eq. 1); Carlini et al. IEEE S&P 2024 (Fig 1, Fig 6,
Table 1; §4.4–4.5, §6.2); Wan et al. ICML 2023 (Fig 1); Souly et al. 2025 (arXiv 2510.07192;
Figs 1–2); Hubinger et al. 2024 (arXiv 2401.05566; Figs 1–2); Shan et al. Glaze (USENIX Sec 2023) and
Nightshade (IEEE S&P 2024); Tran, Li & Madry NeurIPS 2018 (Fig 1, Fig 3, Algorithm 1, Table 2); Wang
et al. Neural Cleanse IEEE S&P 2019 (§III, §IV, §VIII). Notes only: Chen et al. 2018 (activation
clustering), Liu et al. RAID 2018 (fine-pruning), Gao et al. 2019 (STRIP).

**Figures (22 cited crops in `figs/`):** `badnets-real-stopsign.png` `:84` · `biggio-gradient-attack.png` `:156` ·
`biggio-multipoint.png` `:166` · `frogs-schematic.png` `:190` · `frogs-transfer-attack.png` `:214` ·
`frogs-feature-b.png` `:229` · `badnets-mnist-triggers.png` `:278` · `badnets-error-vs-poison.png` `:302` ·
`badnets-confusion.png` `:317` · `badnets-trigger.png` `:348` · `badnets-approaches.png` `:375` ·
`carlini-cost.png` `:403` · `carlini-wiki-cdf.png` `:428` · `wan-train-row.png` `:461` · `wan-test-row.png` `:463` ·
`souly-overview.png` `:488` (Fig 1a only) · `souly-constant-count.png` `:497` (Fig 2 + legend) ·
`sleeper-setup.png` `:529` (Fig 1 stage 1) · `sleeper-code-vuln.png` `:545` (Fig 2a) · `spectral-pipeline.png` `:621` ·
`tran-data-eig.png` `:635` · `tran-rep-eig.png` `:636`. HTML tables: Carlini Table 1 selection `:443`, Souly token
fractions `:473`, Glaze vs Nightshade `:579`. Inline SVG: `:98`, `:106`, `:114`, `:122`, `:139`, `:147`, `:181`, `:205`, `:269`, `:326`, `:358`, `:366`, `:393`, `:418`, `:603`, `:611`, `:660`, `:683`.

**2026-10 rebuild (65 → 59):** rebuilt to the slides-review brief (#106). Model stealing,
activation clustering and fine-pruning slides removed from the deck (the last two are in the notes
table). The figures `tramer-extraction`, `actclust-pca`, `finepr-activations`, `glaze-results`,
`nightshade-outputs` and `wan-trigger-phrases` were deleted.
Round 2 (slides-review #112): token-fraction fix (Souly), ASR per mapping, scoped claims (P5, 7, 10,
12, 14, 15, 18, 34, 36, 39, 42, 53, 59), figures recaptured or re-selected (P17, 31, 37, 38, 40, 41,
43, 44, 51); `wan-overview`, `carlini-datasets-table` and `spectral-histograms` replaced and deleted.

**Note:** `lec09-poisoning-note.html` — 59 entries. Each entry has a minute
budget and elapsed time, a script, and a key takeaway. Content slides add the figure,
setup/model/date, what the slide establishes and does not establish, assumptions, and
primary-source links. The defense comparison table is in entry 48 (Spectral, AC, NC,
Fine-Pruning, STRIP, hashes); the worked-example code is in entry 26.

**Tech:** `lec09tech.html` — 18 slides:
- count N, doc fraction N/|D|, token fraction N·L̄/T with Souly numbers (4)
- Frogs Eq. 1 (5–6, ℓ∞ variant)
- feature map needed (7)
- backdoor objective, "common formalization"; λ = α/(1−α) (8)
- ASR with y ≠ y_t (9)
- spectral τ, 1.5ε removal (11–12)
- separation as an assumption (13)
- Neural Cleanse Eq. 3 (14)
- MAD anomaly index, MAD > 0, flags a *suspected* label (15)
- activation clustering; smaller-cluster rule as a heuristic (16)
- adaptive-attack caveat (17)

## lec10-jailbreak.html

**Topic:** Jailbreaks (90 min; mixed-major sophomores/juniors; concept-first, light math, no proofs;
**no activities**; no working jailbreak strings). Jailbreak defined as bypassing safeguards *through inputs*;
prompt injection, poisoning and weight-level safety removal separated (the last as a labelled contrast).
Brief RLHF / Constitutional AI refresher (two approaches, not two stages). Under- vs over-refusal; access
ladder; every ASR needs denominator, budget, model/version, judge. Fragility: Wei's two failure modes and
Table 1; shallow alignment (Qi 2025 Figs 1–2, Table 2) and one refusal direction (Arditi Fig 1) as findings in
tested settings; fine-tuning contrast (Qi 2024 Tables 1–3). Search: GCG (≈256K evaluations; transfer Table 2,
ensemble 86.6/46.9 is any-of-4) vs PAIR (≤ 90 queries, Table 2). Budget: any-of-N illustration, many-shot
(Fig 2; intercept not slope; 61% → 2% warning, non-adaptive), Best-of-N (Fig 3; resend reliability Table 1),
languages/ciphers on one slide with the StrongREJECT re-check. Evaluation: judge ladder, PAIR judge Table 1,
StrongREJECT Fig 1 (redrawn, redacted), HarmBench length, XSTest over-refusal, Ganguli κ = 0.32. Defenses:
Constitutional Classifiers (Fig 1 redrawn; costs) and circuit breakers (Table 1) + Schwinn &amp; Geisler adaptive
re-attack. Excludes prompt injection (lec13), poisoning (lec09). Math in `lec10tech.html`.

### Sections (58 slides, 90 min: safety training 10 · fragility 20 · search 20 · attack budget 20 · evaluation + defenses 20)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:30`, `:42` | |
| **01 — What Safety Training Adds** | 3–9 | `:71` | refused then answered (Wei Fig 1, redacted) `:79` · definition + neighbouring threats `:90` · RLHF / CAI refresher (SVG) `:106` · two ways to fail (SVG) `:115` · access ladder (SVG) `:123` · four ASR labels `:131` |
| **02 — Why Refusal Is Fragile** | 10–20 | `:141` | two hypotheses `:149` · competing objectives (SVG) `:158` · mismatched generalization (SVG) `:168` · Wei Table 1 (HTML) `:177` · per-token KL (Qi 2025 Fig 1) `:193` · prefilling (Qi 2025 Fig 2) `:210` · recovery augmentation (Table 2, HTML) `:227` · refusal direction (Arditi Fig 1) `:243` · fine-tuning contrast (Qi 2024, HTML) `:254` · findings × access `:270` |
| **03 — Searching for Jailbreaks** | 21–30 | `:285` | families (SVG) `:293` · search loop (SVG) `:302` · GCG objective (SVG) `:310` · GCG step + 256K budget `:321` · transfer (GCG Fig 1) `:330` · transfer table (GCG Table 2, HTML) `:346` · PAIR (Chao Fig 2, redacted) `:361` · PAIR vs GCG (Chao Table 2, HTML) `:371` · gradient vs LLM search `:388` |
| **04 — Scaling the Attack Budget** | 31–41 | `:403` | any-of-N bars (SVG, illustrative) `:411` · many-shot schematic (redacted SVG) `:420` · MSJ Fig 2 `:430` · intercept vs slope (MSJ Fig 5 middle panel) `:448` · BoN augmentations `:465` · BoN Fig 3 (Text panel + legend) `:476` · resend reliability (Table 1, HTML) `:492` · languages + ciphers (two studies, two protocols) `:508` · adversarial example vs jailbreak (SVG) `:533` · budget summary `:541` |
| **05 — Evaluation and Defenses** | 42–58 | `:554` | judge ladder (SVG) `:562` · PAIR judge table `:570` · StrongREJECT (Fig 1 redrawn, redacted) `:585` · HarmBench Fig 2 `:594` · XSTest (HTML) `:611` · Ganguli Fig 1 `:626` · three defense places (SVG) `:642` · Constitutional Classifiers (Fig 1 redrawn) `:650` · CC: two systems, two kinds of evidence `:659` · circuit breakers (CB Fig 1 top row) `:683` · CB Table 1 `:692` · adaptive re-attack with access + budget (Schwinn &amp; Geisler; BoN) `:707` · asymmetry `:723` · checklist (7 questions incl. access, denominator) `:731` · takeaways `:747` · closer `:760` |

**Key citations (checked against saved PDFs, 2026-10-10):** Wei, Haghtalab &amp; Steinhardt NeurIPS 2023
(Fig 1, §3, Table 1); Ouyang et al. NeurIPS 2022; Bai et al. 2022 (arXiv 2212.08073); Qi et al. ICLR 2025
(arXiv 2406.05946; Figs 1–2, Table 2); Arditi et al. NeurIPS 2024 (Fig 1); Qi et al. ICLR 2024 (arXiv 2310.03693;
Tables 1–3); Zou et al. 2023 GCG (arXiv 2307.15043; Fig 1, Algorithm 1, Table 2 — ensemble 86.6% GPT-3.5 /
46.9% GPT-4, single suffix ≈34%; the old "84%" claim was wrong); Chao et al. PAIR (arXiv 2310.08419; Fig 2,
Tables 1–2); Anil et al. NeurIPS 2024 (Figs 1, 2, 5; §5.4); Hughes et al. BoN (arXiv 2412.03556; §2, Fig 3,
§3.1, Table 1, §5.4); Yong et al. 2023 (arXiv 2310.02446); Yuan et al. CipherChat ICLR 2024; Souly et al.
StrongREJECT NeurIPS 2024 (Fig 1); Mazeika et al. HarmBench ICML 2024 (Fig 2, §3.2); Röttger et al. XSTest
NAACL 2024 (Table 2); Ganguli et al. 2022 (Fig 1, §3.4–3.5); Sharma et al. 2025 (arXiv 2501.18837; Fig 1, §3–5);
Zou et al. Circuit Breakers NeurIPS 2024 (Fig 1, Table 1); Schwinn &amp; Geisler 2024 (arXiv 2407.15902; Table 1).
Notes only: Perez et al. EMNLP 2022.

**Figures (13 cited image files in `figs/`):** `wei-jailbroken-redacted.png` `:79` · `qi25-kl.png` `:193` ·
`qi25-prefill.png` `:210` · `arditi-fig1.png` `:243` · `gcg-schematic.png` `:330` · `pair-fig2-redacted.png` `:361` ·
`msj-fig2ab.png` `:430` · `bon-fig3-text.png` + `bon-fig3-legend.png` `:476` · `harmbench-fig2.png` `:594` · `ganguli-redteam.png` `:626` ·
`cb-top.png` `:683`. `msj-fig5-rl.png` (MSJ Fig 5 middle panel). Redacted by the lecturer, with disclosure in the
cite and note: Wei Fig 1 (demanded-opening wording, Base64 payload) and PAIR Fig 2 (rewritten prompt, reply);
`wei-jailbroken.png` (unredacted) is kept only for lec01. Redrawn as SVG with disclosure: MSJ Fig 1 (redacted),
StrongREJECT Fig 1 (redacted), Constitutional Classifiers Fig 1 (simplified).

**2026-10 rebuild (60 → 58):** rebuilt to the slides-review brief (#118). Persona/fake-authority/obfuscation
zoo, system-prompt hardening, demo and "frontier" slides removed; evaluation and defenses expanded to 20 min.
Figures `ouyang-3steps`, `ouyang-winrate`, `bai-cai`, `qishallow-kl`, `arditi-refusal`, `gcg-asr`,
`gcg-transfer`, `pair-schematic`, `msj-powerlaw`, `yong-translate`, `yong-table`, `cipher-overview`,
`qift-overview`, `szegedy-ostrich`, `ganguli-success`, `perez-overview`, `sharma-overview`, `cb-overview`,
`bon-powerlaw` were deleted. Review round 2 (slides-review #120) deleted the unredacted PAIR Fig 2 and
full three-panel BoN Fig 3 crops (replaced by the redacted / text-panel versions) and replaced the slide 35 sketch with the real Fig 5 panel.

**Note:** `lec10-jailbreak-note.html` — 58 entries. Each entry has a minute budget and elapsed time, a script,
and a key takeaway. Content slides add the figure, setup/model/date, what the slide establishes and does not
establish, assumptions, and primary-source links (20 sources). The BoN reliability inconsistency (Table 1
caption vs body vs rows) is recorded in entry 38.

**Tech:** `lec10tech.html` — 21 slides:
- ASR estimate + binomial SE (4)
- any-of-N $1-(1-p)^N$ and $N_q$ (5); heterogeneous $p_i$ (6)
- judge error correction (7); retry amplifies false positives (8)
- RLHF KL objective (10); per-token KL $D_k$ (11); refusal direction + ablation (12)
- GCG loss (14); GCG step and 256K budget (15); PAIR $N_s \times K = 90$ (16)
- MSJ $Cn^{-\alpha}+K$ with NLL, C, α, K defined (18); intercept vs exponent, slope −α (19); BoN $-\log\mathrm{ASR}=aN^{-b}$ (20)

## lec11-synthetic-media.html

**Topic:** Synthetic media: watermarks, detection and provenance (90 min; mixed-major sophomores/juniors;
concept-first, light math, no proofs; **no activities**). Arup deepfake call (HKD 200M / ≈ USD 25M) as the
origin case; three kinds of evidence — embed (watermark), guess (detector), sign (provenance) — and
"origin is not truth" (no mark ≠ human; no credentials ≠ fake). KGW taught thoroughly as the one mechanism:
keyed green list, boost δ, green-count z-test, threshold → nominal FPR, √T growth, repeated pairs → nominal vs
measured threshold (K24 Fig 7 right), δ-vs-perplexity trade-off; distortion-free / undetectable named only, as two
different guarantees. Robustness
compared only with setups: Kuditipudi random swaps (m = 35, median p-value), Krishna DIPPER (300 tokens, 1% FPR), Sadasivan
recursive paraphrase, K24 human rewrites (~800 tokens at 10⁻⁵) and copy-paste dilution; TV bound vs empirical
robustness as differently scoped claims. Production: SynthID-Text (Nature 2024, Fig 3a), Tree-Ring image
table, vendor detectors read only their own mark, three meanings of "standard". Keyless detection: overlapping
scores, labelled base-rate illustration (FPR ≠ P(human | flagged)), Liang 2023 and the withdrawn OpenAI
classifier (explicitly historical), DFDC private test. Provenance: C2PA manifest, signed edit chain,
supported / on by default / preserved, soft bindings; labelling law (China 1 Sep 2025, Korea 22 Jan 2026,
EU Art. 50 2 Aug 2026; Art. 50(2) transition to 2 Dec 2026). Excludes model-weight watermarks and copyright. Math in `lec11tech.html`.
Rigorous treatment: `courses/privacy/lectures/06-watermark/`.

### Sections (56 slides, 90 min: problem 10 · watermarking 20 · robustness + production 20 · detection 15 · provenance + policy 15 · synthesis 10)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:30`, `:42` | |
| **01 — The Provenance Problem** | 3–8 | `:75` | Arup case (SVG) `:83` · embed / guess / sign `:93` · origin is not truth (table) `:101` · three questions `:115` · scope: outputs not models `:128` |
| **02 — Text Watermarking** | 9–19 | `:148` | token-by-token (SVG) `:156` · keyed split `:165` · boost δ `:175` · KGW Fig 1 `:184` · chance rate γ `:200` · threshold `:208` · KGW Fig 3a `:219` · K24 Fig 7 right `:236` · KGW Fig 2 left `:253` · distortion-free / undetectable `:270` |
| **03 — Robustness and Production** | 20–33 | `:291` | attack ladder (SVG) `:299` · Kuditipudi Fig 4b `:308` · DIPPER (Krishna Table 1 redrawn) `:325` · Sadasivan Fig 3a legend (bars redrawn) `:336` · TV bound curve `:347` · K24 Fig 4 right `:358` · K24 Fig 2 copy-paste (redrawn) `:373` · setups table `:383` · impossible vs robust `:398` · SynthID Fig 3a `:415` · Tree-Ring Table 2 subset `:431` · vendor detector `:447` · three "standards" `:457` |
| **04 — Detecting Without a Watermark** | 34–42 | `:471` | overlapping scores `:479` · base-rate tree (labelled illustration) `:488` · FPR vs P(human\|flag) `:497` · Liang Fig 1a `:521` · OpenAI classifier `:537` · DFDC split `:558` · DFDC Table 2 redrawn (log loss) `:567` · lead not verdict `:578` |
| **05 — Provenance and Policy** | 43–50 | `:592` | detection vs provenance `:600` · C2PA manifest (SVG) `:619` · signed chain `:628` · supported / default / preserved (vendor's words) `:643` · soft binding `:658` · law timeline `:668` · two kinds of label `:677` |
| **06 — Synthesis** | 51–56 | `:692` | embed / guess / sign table `:700` · three cases `:714` · checklist (7 questions) `:727` · takeaways `:743` · closer `:756` |

**Key citations (checked against saved PDFs / pages, 2026-10-10):** Kirchenbauer et al. ICML 2023 (arXiv
2301.10226; Alg 2, §3, Figs 1, 2, 3a); Kirchenbauer et al. ICLR 2024 (arXiv 2306.04634; Figs 2, 4 right, 7 right, App A.3);
Kuditipudi et al. TMLR (arXiv 2307.15593; Def 1, Fig 4a/4b, m = 35); Christ, Gunn &amp; Zamir (arXiv 2306.09194);
Krishna et al. NeurIPS 2023 (arXiv 2303.13408; Table 1); Sadasivan et al. TMLR 2025 (arXiv 2303.11156; Thm 1,
Fig 3a legend); Dathathri et al. Nature 634 (2024; Fig 3a); Wen et al. Tree-Ring NeurIPS 2023 (Table 2); Liang et al.
Patterns 2023 (Fig 1a); OpenAI classifier post (Jan / Jul 2023, via archive); Dolhansky et al. DFDC (arXiv
2006.07397; §3, §5–6, Table 2); C2PA Technical Specification 2.2 (May 2025; §9.1–9.2) + Soft Binding API; Google SynthID Detector
post (May 2025, vendor statement); Arup (CNN, May 2024). Law (official texts, snapshots in the r2 review package): CAC Measures
国信办通字〔2025〕2号 + GB 45438-2025; Reg. (EU) 2024/1689 Arts. 50, 99, 113 and Reg. (EU) 2026/1744; Korea AI Basic
Act Arts. 31, 40, 43 and Enforcement Decree Art. 23 (law.go.kr). Products (vendor pages): Leica Content Credentials
page, Samsung Newsroom US (7 Feb 2025), Google Keyword blog (10 Sep 2025).

**Figures (8 cited image files in `figs/`):** `sm-kgw-fig1.png` `:188` · `sm-kgw-fig3a.png` `:223` ·
`sm-k24-fig7r.png` `:240` · `sm-kgw-fig2l.png` `:257` · `sm-kud-fig4b.png` `:313` · `sm-k24-fig4r.png` `:363` ·
`sm-synthid-fig3a.png` `:419` · `liang-toefl.png` `:526`.
Redrawn (inline SVG/HTML, disclosed in cites): Krishna Table 1 (KGW rows), Sadasivan Fig 3a legend values (bars),
K24 Fig 2 copy-paste values read from the figure (range bars), Tree-Ring Table 2 (subset), DFDC Table 2.
Illustrative (labelled): next-word bars, green strips, z-curves, base-rate tree.

**2026-10 rebuild:** replaces the former Wk 11 prompt-injection deck (moved unchanged to
backup-prompt-injection, since rebuilt as `lec13-prompt-injection.html`) and the former Wk 12 watermark deck (lec12-watermark, 68 sl; deleted with its note,
its tech file and 13 figures used only by it: `dfdc-logloss`, `kgw-example`, `kgw-zscore-length`,
`kgw-zscore-ppl`, `kirchenbauer-human-paraphrase`, `kirchenbauer-robust-bars`, `krishna-dipper`,
`kud-protocol`, `kud-substitution`, `sadasivan-roc`, `sadasivan-vuln`, `synthid-detect`, `synthid-overview`).
Built to the slides-review brief (#126). Review round 2 (slides-review #128): z &gt; 4 as a normal-approximation
tail; repeat-scoring scoped to WikiText; distortion-free vs undetectable separated; C2PA validity vs signer trust;
law and product rows from official texts; median p-value, TV and log-loss readings corrected; crops `sm-k24-fig7`,
`sm-kud-fig4` replaced by single panels and `sm-sad-fig3a`, `sm-k24-fig2` by redrawn charts (old files deleted).

**Note:** `lec11-synthetic-media-note.html` — 56 entries with minute budget and elapsed time, script, key
takeaway; content slides add figure, setup/model/date, establishes / does not establish, assumptions and
primary-source links (22 sources). Entry 49 carries the three-jurisdiction table from the official texts (enacted
text / applies from / who / form / exceptions / enforcement).

**Tech:** `lec11tech.html` — 13 slides:
- green-list rule (4); idealized independent-Bernoulli null (5); z-statistic, normal-approximation 3×10⁻⁵ vs exact
  tail at T = 20 (6)
- √T growth under constant green rate (7); repeated pairs, m > 1, scoped to WikiText (8)
- base-rate formula with the 2% / 20% examples (10); TV definition, bound + proof idea, keyed detectors (11);
  distortion-free (fresh key) vs undetectable (12)

## lec12-fairness.html

**Topic:** Fairness (90 min; mixed-major sophomores/juniors; concept-first, light math, no proofs on the
slides; **no activities**). Where bias enters (opens with the Obermeyer cost-as-proxy case; sampling, labels, feedback;
Gender Shades benchmark composition; why dropping the protected attribute fails). Measuring fairness: four rates and
their denominators, demographic parity, equalized odds (Hardt ROC plane), calibration within groups vs predictive
parity, five criteria on the same FICO data. COMPAS: ProPublica vs Northpointe as different criteria, rearrest
≠ offending, base rates, Chouldechova identity, Kleinberg et al. conditions, a calibrated worked example with
unequal errors, choosing by context. Mitigation at three points (reweighing, reductions, group thresholds), each
measured result shown with criterion, population, utility and assumptions; an empirical tradeoff is not the
optimal frontier; method cards. Beyond classifiers: Gender Shades and the Actionable Auditing follow-up, BBQ,
Bianchi text-to-image stereotypes; governance obligations and limits (~3.5 min). Math in `lec12tech.html`.

### Sections (56 slides, 90 min: where bias enters 10 · measuring 20 · COMPAS + impossibility 15 · mitigation 20 · beyond classifiers 15 · synthesis 10)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:30`, `:42` | |
| **01 — Where Bias Enters** | 3–10 | `:74` | mirror `:82` · three places `:99` · sampling (Gender Shades composition) `:115` · label problem `:138` · Obermeyer cost proxy `:155` · feedback loop `:180` · drop race fails `:206` |
| **02 — Measuring Fairness** | 11–21 | `:227` | notation `:235` · four rates `:252` · demographic parity `:286` · equalized odds `:305`, `:320` · Hardt ROC plane `:342` · calibration `:354` · calibration vs PPV `:369` · five criteria `:386` · FICO thresholds `:401` |
| **03 — COMPAS and Impossibility** | 22–34 | `:413` | what COMPAS is `:421` · FPR by group `:440` · within subgroups `:463` · Northpointe `:482` · different criteria `:500` · rearrest ≠ offending `:517` · base rates `:534` · Chouldechova `:552` · Kleinberg `:566` · worked example `:580` · why forced `:605` · context `:627` |
| **04 — Mitigation** | 35–45 | `:643` | three places `:651` · reweighing `:683`, `:698`, `:717` · reductions `:727`, `:743` · group thresholds `:757` · FICO cost `:774` · empirical tradeoff ≠ optimal frontier `:791` · method cards `:808` |
| **05 — Beyond Classifiers** | 46–52 | `:821` | Gender Shades `:829` · after the audit `:840` · BBQ `:879`, `:898` · Bianchi `:910` · governance `:929` |
| **06 — Synthesis** | 53–56 | `:944` | checklist `:952` · takeaways `:966` · closer "Which rate?" `:980` |

**Key citations (checked against saved PDFs / pages, 2026-10-10):** Obermeyer et al. Science 2019; Buolamwini
&amp; Gebru FAT* 2018 (Table 4); Raji &amp; Buolamwini AIES 2019; Dwork et al. ITCS 2012; Hardt, Price &amp; Srebro
NeurIPS 2016 (Figs. 1, 2, 9, 11; FICO §7); Kleinberg, Mullainathan &amp; Raghavan ITCS 2017 (Thms 1.1, 1.2);
Chouldechova Big Data 2017 (Def. 2.2, eq. 2.6, Figs. 1–3); Larson et al. ProPublica 2016; Dieterich et al.
Northpointe 2016; Kamiran &amp; Calders KAIS 2012; Bellamy et al. AIF360 2018 (Figs. 4, 5b); Agarwal et al. ICML 2018
(Fig. 1); Parrish et al. BBQ, Findings of ACL 2022 (Figs. 1, 3); Bianchi et al. FAccT 2023 (Fig. 3). Governance:
NYC DCWP rules, NY State Comptroller audit (Dec 2025), Reg. (EU) 2024/1689 and 2026/1744, Colorado SB26-189, Korea
AI Basic Act.

**Figures (17 cited image files in `figs/`):** `hardt-eqodds-roc.png` `:347` · `hardt-fico-thresholds.png` `:405` ·
`chouldechova-deciles.png` `:433` · `chouldechova-fpr-priors-hi.png` `:475` · `chouldechova-calib-pp.png` `:485` ·
`reweighing-aif360.png` `:721` · `reductions-adult.png` `:751` · `reductions-compas.png` `:752` ·
`reductions-legend.png` `:754` · `hardt-eo-threshold.png` `:767` · `hardt-fico-profit.png` `:778` ·
`aif360-di-panel.png` `:797` · `bbq-example-hi.png` `:894` · `bbq-bias-scores-hi.png` `:904` ·
`bianchi-occupations.png` `:918` (Gender Shades P47 is an SVG redrawn from Table 4). Superseded r1 crops
(`chouldechova-calibration.png`, `chouldechova-fpr-priors.png`, `reductions-frontier.png`, `hardt-fico-cost.png`,
`aif360-frontier.png`, `bbq-example.png`, `bbq-bias-scores.png`, `gender-shades.png`) stay in `figs/` for the backups.

**2026-10 rebuild:** merges the former Wk 13–14 fairness decks (moved to `backup-fairness-defs.html`,
`backup-fairness-mitigation.html`). Note `lec12-fairness-note.html` (56 entries); tech `lec12tech.html` (17 sl, see
the supplements table).

## lec13-prompt-injection.html

**Topic:** Prompt injection (90 min; mixed-major sophomores/juniors; concept-first, no math on the slides;
**no activities**; examples schematic, no working payloads or live exfiltration destinations). Definitions by
authority (jailbreak vs injection), direct vs indirect injection, intended priority vs enforced boundary. Agentic
surface: agent loop, confused deputy, three harms, per-action provenance, the trifecta as an exfiltration heuristic
only, ordinary features as exit channels. Three incidents (EchoLeak, GitHub MCP, Comet), each with a four-step status
ladder (demonstration / exploitation / vendor remediation / independent retest). Why it is hard: learned priority,
instructions inside data, escaping alone does not establish authority, detection vs adaptation. Defenses and
measurement: three metrics plus denominator, access, budget and adaptation; AgentDojo; spotlighting, instruction
hierarchy, simple defenses; Nasr et al. Table 7 as the adaptive anchor; CaMeL as the main system defense with a
conditional guarantee; other system defenses; meaningful approval. Agent autonomy beyond injection is left to Wk 14.
Math in `lec13tech.html`.

### Sections (53 slides, 90 min: core idea 10 · agentic surface 20 · incidents 15 · why hard 10 · defenses + measurement 25 · synthesis 10)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:38`, `:50` | |
| **01 — The Core Idea** | 3–9 | `:82` | one context `:90` · BANANA example `:121` · jailbreak vs injection `:144` · Greshake Fig. 3 `:165` · priority ≠ boundary `:185` · hidden text `:208` |
| **02 — The Agentic Attack Surface** | 10–18 | `:243` | chatbot → agent `:251` · agent loop `:283` · end to end `:316` · confused deputy (InjecAgent) `:338` · three harms `:354` · per-action provenance `:367` · trifecta `:383` · exit channels `:412` |
| **03 — Three Incidents** | 19–27 | `:441` | reading a report `:449` · EchoLeak `:464`, `:482` · GitHub MCP `:506`, `:524` · Comet `:545`, `:563` · comparison `:579` |
| **04 — Why It Is Hard** | 28–32 | `:593` | learned priority `:601` · instructions as data `:625` · escaping ≠ authority `:642` · detection vs adaptation `:659` |
| **05 — Defenses and Measurement** | 33–48 | `:685` | three numbers `:693` · reporting `:708` · AgentDojo `:722`, `:736` · spotlighting `:756` · instruction hierarchy `:777` · simple defenses `:792` · adaptive (Nasr) `:811` · boundary `:827` · CaMeL `:840`, `:860`, `:883`, `:901` · other defenses `:915` · approval `:930` |
| **06 — Synthesis** | 49–53 | `:946` | checklist `:954` · open problems `:968` · takeaways `:982` · closer "Who decided?" `:996` |

**Key citations on slides (checked against saved PDFs / pages, 2026-10-10):** Greshake et al., ACM AISec 2023
(Fig. 3); Zhan et al. InjecAgent, arXiv 2403.02691 (Fig. 1); Willison (dual LLM 2023; trifecta, 16 June 2025);
Debenedetti et al. AgentDojo, NeurIPS 2024 D&amp;B (Fig. 1, Fig. 6a, Tables 3, 5); Hines et al. spotlighting (Fig. 4);
Wallace et al. instruction hierarchy (Fig. 2); Nasr, Carlini et al. arXiv 2510.09023, preprint (Table 7); Debenedetti
et al. CaMeL arXiv 2503.18813 (Fig. 1; §5 and Figs. 4–6; Tables 2–4; §3.1, §7, §9.3). Incidents: Aim Labs EchoLeak,
MSRC and NVD CVE-2025-32711; Invariant Labs GitHub MCP; Brave on Comet. Notes only: Perez &amp; Ribeiro; Willison
2022 naming; Liu et al. HouYi; OWASP LLM01; Zhan et al. adaptive attacks arXiv 2503.00061; CamoLeak, SpAIware, Brave
screenshots, Bing "Sydney".

**Figures (7 image files in `figs/`):** `greshake-plant.png` `:178` · `injecagent-overview.png` `:347` ·
`agentdojo-fig1.png` `:726` · `agentdojo-models.png` `:741` · `hines-datamark.png` `:770` ·
`wallace-results.png` `:782` · `camel-fig1.png` `:845`. All other diagrams are inline SVG; tables on 40, 41, 45, 47
are transcribed from the cited sources.

**2026-10 rebuild:** replaces the backup-prompt-injection deck (former Wk 11, 66 sl), deleted with its note, its tech
file and 10 figures used only by it: `agentdojo-defenses`, `agentdojo-overview`, `agentdojo-utility-asr`,
`camel-flows`, `greshake-overview`, `hines-encoding`, `liu-app`, `perez-hijack`, `wallace-hierarchy`,
`zhan-adaptive`. Built to the slides-review brief (#142). `lec01-introduction-note.html` pointers updated. The stale
duplicate of the backup-prompt-injection and lec12 sections, and a copy of the lec11 rebuild text misplaced in the lec12
section, were removed from this file in the same edit.

**Note:** `lec13-prompt-injection-note.html` — 53 entries with minute budget and elapsed time, script, key
takeaway; content slides add figure, setup/model/date, establishes / does not establish, assumptions and
primary-source links (23 sources). Entry 13 carries a worked toy-agent trace; entry 27 the extra incidents
(CamoLeak, SpAIware, Sydney); entry 41 Nasr Fig. 1 and human red-teaming. Data inconsistencies in AgentDojo
(Table 3 vs 5) and CaMeL (Table 4 vs §6.2.1) are flagged on slides 40 and 45 and in their entries.

**Tech:** `lec13tech.html` — 15 slides:
- trusted vs attacker-controlled (4); PI-SEC game with $\Omega_p$ (5); control vs data part of an action (6)
- confused deputy, least privilege as $\Omega_p \subseteq \mathrm{Auth}_p \subseteq \mathrm{Auth}$ (8); capability
  labels and propagation, STRICT mode (9); dual LLM → CaMeL check (10); the conditional guarantee (11)
- AgentDojo metrics written out (13); static vs adaptive ASR with budget $q$ (14)

## backup-fairness-defs.html

*Former Wk 13 deck (old names lec13-fairness-defs, its note, and lec13tech), moved unchanged on 2026-10-10 to `backup-fairness-defs.html`, `backup-fairness-defs-note.html` and `backup-fairness-defstech.html`; line pointers below still hold. Merged into Wk 12.*

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

*Former Wk 14 deck (old names lec14-fairness-mitigation, its note, and lec14tech), moved unchanged on 2026-10-10 to `backup-fairness-mitigation.html`, `backup-fairness-mitigation-note.html` and `backup-fairness-mitigationtech.html`; line pointers below still hold. Merged into Wk 12.*

**Topic:** Fairness II — mitigation & accountability (~90 min). Picks up where lec13's
definitions end: three places to intervene in the pipeline (pre-/in-/post-processing),
one intuition + picture per method with formal math in `backup-fairness-mitigationtech.html` (reweighing
w(g,y), penalized/constrained objectives, reductions, per-group ROC thresholds);
the fairness–accuracy tradeoff and the impossibility recap (defined and proved in
lec13 — referenced, not redone); accountability (model cards, datasheets, audits —
Gender Shades figure + Actionable Auditing follow-up — impact assessments, EU AI Act
touchpoint only, governance is lec15); generative & LLM fairness (Bianchi figure
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

## lec15-governance.html

**Topic:** Governance, the frontier & course wrap-up (~90 min, capstone). Nearly
math-free. Connects the course's threads via the trust stack (data → model → output →
society), then risk frameworks (NIST AI RMF + GenAI Profile), regulation (EU AI Act
incl. Digital Omnibus timeline and GPAI rules; US patchwork + executive-order
whiplash; Korea AI Basic Act; summits/AISIs + International AI Safety Report),
auditing & red-teaming incl. frontier-lab safety frameworks (Anthropic RSP/ASL,
OpenAI Preparedness, GDM FSF), open problems, and the wrap-up (five questions, Demo
Showcase kept, one lesson). Formal structures live in `lec15tech.html` (deliberately
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
slide kept per course scaffolding. `lec15tech.html` errors-only pass (EU cite fixed,
tier bullets de-dashed; still 6 sl). Note file synced (66 entries, order matches).

**2026-09 figure pass (66→70):** every content slide now carries a visual. 17 new cropped figures (International AI Safety Report 2026 ×6, Anderljung 2023 ×2, Shevlane 2023 ×2, NIST AI RMF, Bommasani 2021, Ganguli 2022, Anthropic RSP v2.2 table, GDM FSF v3.1 table, two European Commission graphics) plus the Mitchell model card reused from lec14; ~28 new inline SVGs on formerly bullet-only slides. Four slides added: **The Full Map: Six Areas** (Weidinger Table 1, all six areas named) `:403`; **The Commission's Own Picture** (EU risk pyramid) `:451`; **Where Rules Can Attach** (Anderljung Fig. 1 lifecycle) `:651`; **Why Governance Is Hard** (IASR Fig. 3.1) `:722`. Dense source tables (Shevlane Table 1, Weidinger Table 1, OpenAI Preparedness Table 1) are rendered as verified-name SVG summaries citing the table rather than as unreadable crops. The GDM FSF PDF on hand is Version 3.1 (Apr 2026); the table cite says so explicitly while the author's "v3, 2025" text cite is untouched. No author bullets rewritten; two new muted lines trimmed to the 7×7 ceiling. Note file: 70 entries (4 new articles + 46 "Slide figure" lines), order matches. 60-dpi render check of all 46 edited slides passed after fixes (threads SVG height, Korea-threshold labels, lifecycle image width, headline SVG width, funnel contrast).

**2026-08 note enrichment:** `lec15-governance-note.html` upgraded from speaker script
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
