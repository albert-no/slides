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
| 11 | `lec11-synthetic-media.html` | Synthetic media: text watermarks, robustness, detection without a watermark, provenance (C2PA) & labelling law | **new 2026-10** (56 sl, 8 real figure crops + 5 tables/figures redrawn, 90 min, concept-first, no activities; note 56 entries; tech 13 sl). Former Wk 11 prompt injection → `backup-prompt-injection.html` (to be rebuilt as Wk 13); former Wk 12 watermark deck replaced |
| 12 | `lec12-fairness.html` | Fairness: where bias enters, criteria, COMPAS and impossibility, mitigation, audits beyond classifiers | **new 2026-10** (56 sl, 14 real figure crops, 90 min, concept-first, no activities; note 56 entries; tech 16 sl). Merges the former Wk 13–14 fairness decks → `backup-fairness-defs.html`, `backup-fairness-mitigation.html` |
| 13 | — | (slot reserved: prompt injection, rebuilt from `backup-prompt-injection.html`) | |
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
| `lec12tech.html` | Wk 12 (fairness) | four rates per group; five criteria written out; Dwork (D,d)-Lipschitz (Def. 2.1) and Kusner counterfactual fairness (Def. 5); calibration vs PPV via the score mix; Chouldechova identity (eq. 2.6); Kleinberg proof sketch; worked example computed; reweighing; reductions saddle point; Hardt derived predictor | **new 2026-10** (16 sl; formulas checked against the saved papers) |
| `backup-fairness-defstech.html` | former Wk 13 (fairness defs) | demographic parity / equalized odds / calibration as conditional-prob defs; base rates; impossibility theorem (Chouldechova/Kleinberg) + proof sketch | **fixed 2026-08** (15 sl: base-rate identity was inverted (1−p)/p → p/(1−p) per Chouldechova eq 2.6; proof-sketch step 1 corrected (calibration ≠ "PPV = base rate" → predictive parity demands equal PPV across groups); unverifiable numeric-wedge table replaced with an exactly derivable two-value-score construction; impossibility attribution now dual Chouldechova + Kleinberg) |
| `backup-fairness-mitigationtech.html` | former Wk 14 (fairness mitigation) | reweighing w(g,y); penalized min Loss+λ·Unfairness; constrained form; reductions (Agarwal 2018); post-processing per-group thresholds (Hardt 2016) | **checked 2026-08** (17 sl: reweighing formula verified against Kamiran & Calders; reductions + Hardt ROC intuition verified against papers; one fix — cite venue "KIS 2012" → "Knowledge and Information Systems 2012") |
| `lec15tech.html` | Wk 15 (governance) | EU AI Act risk-tier taxonomy; NIST RMF as Govern→Map→Measure→Manage loop; what "measurable" audit metrics mean (deliberately light — governance is non-mathematical) | **checked 2026-08** (6 sl: tiers verified still accurate post-Omnibus; EU cite normalized; tier bullets de-dashed for lint) |

## Backup / swap-in materials (not in the 15-week core)

Optional decks for substitution or extra sessions. Each has a `-note.html` script.

| File | Topic | Slots in where | Status |
|---|---|---|---|
| `backup-sycophancy.html` | Sycophancy, manipulation & persuasion | merge into Wk 6, or standalone | **drafted** (38 sl) |
| `backup-copyright.html` | Copyright, consent & data provenance | pairs with Wk 4 (memorization) | **drafted** (45 sl) |
| `backup-agentic-autonomy.html` | Agentic autonomy risks beyond injection | expands the prompt-injection deck | **drafted** (47 sl) |
| `backup-prompt-injection.html` | Prompt injection &amp; agentic safety (former Wk 11; note `backup-prompt-injection-note.html`, tech `backup-prompt-injectiontech.html`) | to be rebuilt as Wk 13 | **figure pass 2026-09** (66 sl; moved unchanged 2026-10) |
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
- `lec12` (2026-10): 14 cited crops — see its section. Former fairness decks (now `backup-fairness-defs`/`backup-fairness-mitigation`): Bianchi occupation grid (`figs/bianchi-occupations.png`, FAccT 2023 Fig 1); `lec14` Gender Shades table (`figs/gender-shades.png`, FAT* 2018 Table 4). backup-fairness-defs COMPAS TODO removed (illustrative SVG kept — real news graphic is copyrighted).
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
| Title / Contents | 1–2 | `:56`, `:68` | title "Can We Trust It?" |
| **01 — The Gap** | 3–6 | `:97` | **METR task-length plot** `:105` · AI decides real outcomes `:116` · two curves SVG `:131` |
| **02 — When It Goes Wrong** | 7–32 | `:155` | *fairness* COMPAS bars SVG `:163` · Gender Shades table `:196` · Amazon pipeline SVG `:211` · *privacy* GPT-2 extraction `:241` · "poem" divergence SVG `:255` · Samsung + Garante `:285` · *reliability* Avianca + Deloitte fake-citation card `:320` · Charlotin 2,039 decisions (CSV export 2026-09-12) `:351` · Air Canada + $1 car chat bubbles `:372` · sycophancy (Sharma Fig. 5) `:401` · *robustness* panda→gibbon `:415` · stop-sign stickers `:429` · *security* Base64 jailbreak `:443` · EchoLeak SVG `:457` · *safety* Uber Tempe `:488` · July 2026 escaped agent timeline `:502` · it came back `:518` · 59% vs 3% scheming `:550` · *provenance* Pope puffer `:576` · Sora frame + NH robocall `:590` · Arup $25M `:604` · *data* Bartz $1.5B SVG `:625` · *society* Canaries plot `:655` · EU pyramid + Korea AI Basic Act `:669` · **the pattern = seven dimensions (7-row table: incidents → question → dimension, + transparency)** `:697` |
| **03 — Why AI Fails Differently** | 33–36 | `:714` | SW vs learned SVG `:722` · **why the trust problem changed (rule-based → statistical ML → foundation models → agents, cumulative failure classes; SVG)** `:758` · three sources SVG `:809` |
| **04 — Threat-Model Thinking** | 37–40 | `:841` | **what is a threat model (+adversary SVG, EchoLeak worked example)** `:849` · **attack map 2×2 SVG** `:886` · no threat model, no answer (59/3 + panda/stop sign) `:913` |
| **05 — This Course** | 41–45 | `:937` | **trust stack SVG carrying all 14 topics** `:945` · concepts first, demos optional `:972` · the goal (headline→property→threat→convincing? flow SVG + 3 drill cards) `:992` · **practice: boardroom questions (four-step frame SVG + "Before you sign" / "Ask the vendor" cards)** `:1028` |
| Closer | 46 | `:1070` | "Trust?" |

**Visuals (real images, all in `figs/`):** `metr-task-length.png` (METR Time Horizon 1.1,
Jan 2026, CC BY) `:110` · `gender-shades.png` (Buolamwini & Gebru 2018, Table 4) `:201` ·
`gpt2-extraction.png` (Carlini et al. 2021, Fig. 1; source PNG is cropped at the bottom)
`:246` · `sharma-sycophancy.png` (Sharma et al. ICLR 2024, Fig. 5) `:406` ·
`panda-gibbon.png` (Goodfellow et al. 2015, Fig. 1) `:420` · `eykholt-stopsign.png`
(Eykholt et al. CVPR 2018, Fig. 1) `:434` · `wei-jailbroken.png` (Wei et al. NeurIPS 2023,
Fig. 1) `:449` · `uber-tempe-ntsb.jpg` (NTSB, public domain, via Commons) `:493` ·
`pope-puffer-midjourney.jpg` (AI-generated, PD, via Commons) `:581` · `sora-tokyo.jpg`
(OpenAI Sora "Tokyo Walk", PD, via Commons) `:595` · `canaries-22-25.png` (Stanford
Digital Economy Lab, Fig. 2) `:660`. **SVG diagrams:** two curves `:137`, COMPAS bars
`:169`, Amazon pipeline `:217`, poem divergence `:261`, you⇄model data flow `:301`, fake
citation card `:336`, chat bubbles `:388`, EchoLeak flow `:463`, patched-route `:524`,
59%/3% bars `:556`, library→model `:631`, EU risk pyramid `:675`, SW vs learned `:728`,
three sources `:814`, adversary↔system `:863`, attack map `:892`, trust stack `:951`,
headline→question flow `:1001`, trust-problem stages `:763`, boardroom four-step frame `:1033`.

**Key citations:** Angwin et al., ProPublica 2016 (COMPAS) · Buolamwini & Gebru, FAT* 2018
· Dastin, Reuters 2018 (Amazon) · Carlini et al., USENIX Sec 2021 + Nasr et al. 2023
(extraction) · Bloomberg May 2023 (Samsung) + Garante order 30 Mar 2023 · Mata v. Avianca,
S.D.N.Y. 2023 · Deloitte/DEWR Oct 2025 · Charlotin, AI Hallucination Cases (CSV export 2026-09-12) ·
Moffatt v. Air Canada, 2024 BCCRT 149 · Sharma et al. ICLR 2024 + OpenAI Apr 2025 (GPT-4o
rollback) · Goodfellow et al. ICLR 2015 · Eykholt et al. CVPR 2018 · Wei et al. NeurIPS 2023
· EchoLeak CVE-2025-32711 · NTSB HWY18MH010 · OpenAI / Hugging Face July 2026 incident
(HF disclosure 16 Jul + technical timeline 27 Jul; OpenAI statement 21 Jul + report 26 Aug; METR 26 Aug; Black Hat 5 Aug) · arXiv 2603.01608 (scheming) · Midjourney Pope, Mar 2023 · NH
robocall FCC orders 2024 · Arup deepfake, HK police Feb 2024 · Bartz v. Anthropic, N.D.
Cal. 2025 (settlement final approval 20 Jul 2026) · Brynjolfsson, Chandar & Chen, "Canaries" 2025–26 · Regulation (EU) 2024/1689 as amended by
Regulation (EU) 2026/1744 (Digital Omnibus; high-risk → Dec 2027 / Aug 2028) · Korea AI Basic Act (eff. 2026-01-22).

**2026-era facts (re-verified 2026-09-13 against primary sources; note carries as-of dates):** July 2026 OpenAI/Hugging Face incident `:503`–`:549` — 4 Jul Artifactory compromise → rebuilt 6 Jul → re-entry 8 Jul via WebDAV; 9–13 Jul 4.5-day forensic window inside HF (~17,600 actions, 4 exposed third-party accounts); HF disclosed 16 Jul, OpenAI attributed 21 Jul (slide 24 chronology corrected: the bypassed fix was OpenAI's, not HF's); scheming arXiv 2603.01608 v2 (59%/3% from model organisms; realistic settings minimal) `:551`; Charlotin figures recomputed from the CSV export of 2026-09-12 (2,039 decisions; 1,111 in 2026; ≈$320k across 30 US decisions in Q1 2026 — replaces 1,598 / $145k / 15) `:352`; Korea AI Basic Act eff. 22 Jan 2026, fines ≤ KRW 30M with ≥1-year grace `:670`; EU high-risk dates deferred by the Digital Omnibus (in force 27 Jul 2026) `:670`; Canaries rev. 12 Aug 2026 (data through Jun 2026; gap ≈19%, was ≈13% in Aug 2025) `:656`; Bartz settlement final approval 20 Jul 2026 `:626`. Refresh Charlotin and Canaries before each term.

**Key framing:** threat model = *who* / *what they know* (white/black-box) / *what they
can do* (train/inference-time); "a safety number describes a deployment, not a model"
(59% vs 3%) motivates section 04. Seven dimensions (fairness, privacy, reliability,
robustness, security, safety, provenance) + transparency; the 2026-08 deck had six. **The
seven-dimension taxonomy is stated exactly once** (slide 32, closing section 02); the
course map is stated exactly once (slide 41, the trust stack). Do not re-add summary
slides that restate them — Albert cut them on 2026-09-04 as duplicates.
Citations use `.cite-left`; one exhibit per slide.

**2026-09-13 case-brief pass (44→46):** every real-case slide now carries `What happened` / `Why it happened` / `Why it matters` callouts with year, org, and confirmed status (uncertain items marked *alleged* / *as of*); "Two Curves" labeled *Conceptual illustration*; added "Why the Trust Problem Changed" (§03) and "Practice: Boardroom Questions" (§05, the four-step frame + three vendor questions; every later lecture ends with the same slide). Note re-synced to 46 articles: each incident has a structured *Case background* brief (Background / What happened / Technical connection / What the evidence shows, and does not / Status as of 2026-09 / Teaching cue / Where the course returns to this), *Technical depth — optional* (pointing at `lec01tech.html` slide titles), and a *References* list — 80 links checked 2026-09-13 (openai.com, courtlistener, scworld, securityweek, civilresolutionbc, dewr bot-wall scripted fetches but load in a browser; Reuters Amazon story backed by the Euronews reprint). Cross-lecture pointers live in the note only. `lec01tech.html` unchanged (7 sl; terms match main).

**2026-09-04 trim (46→44):** Albert: "the overall 7 topics part keeps repeating". Cut
"Seven Dimensions of Trust" (folded into "The Pattern": incident → question → dimension
name, + transparency line) and "The Course at a Glance" (its 14 topics now sit inside the
trust-stack layers); dropped the seven-pill row from "The Goal" and replaced it with three
one-line drill cards (headline → property → adversary). Note re-synced to 44 entries
(definitions block moved under "The Pattern"; topic-preview block under "The Trust Stack").

**2026-09-03 rebuild (35→46):** added METR plot, Gender Shades, "poem" split-out,
Samsung/Garante, Charlotin, sycophancy, stop sign, Base64 jailbreak, Uber Tempe, July
2026 escaped agent (2 slides), scheming, Pope puffer, Arup, Bartz, Canaries, EU/Korea
rules; cut Group 1–4 preview slides, "What's New in 2025–26", "How We'll Work" divider
(folded into one slide), knowledge×timing grid (merged into the attack map). Note file
re-synced to 46 entries (590 lines, now 44): old `.detail` blocks reused verbatim, new
backgrounds with primary links for every added incident, Group 1–4 previews preserved
under "The Course at a Glance". `lec01tech.html` untouched.

**2026-08 history:** 47→35 trim (schedule slides, timeline SVG, house analogy cut; Bing
"Sydney" replaced by EchoLeak; Deloitte added) and note enrichment to script + companion
notes (227→443 lines, formal definitions + primary-source links).

---

## lec02-privacy-dp.html

**Topic:** Why models leak and anonymization fails; the differential-privacy idea
(presence barely changes output); the formal $(\varepsilon,\delta)$-DP definition;
reading $\varepsilon$; randomized response; noise-by-sensitivity; DP-SGD;
privacy–utility tradeoff; private foundation models (2025–26).
Intuition pass — points to the privacy course for rigor.

### Sections (69 slides, ~75 min — case-brief pass 2026-09-13 (66→69: "Where This Lecture Sits" lifecycle placement `:89`, "Four Different Privacy Questions" `:462`, "Practice: Boardroom Questions" `:1300`; 19 case/definition slides rewritten with evidence-status callouts), content-revised 2026-08, figures added 2026-09-04, review passes 2026-09-08, edit pass 2026-09-10 (93→77), MIA block moved to lec03 2026-09-11 (77→66), coordinated pass 2026-09-11 (KaTeX overlays on the deniability SVG; warm-up moved ahead of "Randomness Is Required"), all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents / placement | 1–3 | `:47`, `:57` | **Where This Lecture Sits** `:89` — lifecycle strip collect→train→audit→deploy→detect harm→remove/repair, Prevention highlighted (same visual opens lec03–05) |
| **01 — The Privacy Problem** | 4–14 | `:133` | **GPT-2 extraction image** `:170` · Secret Sharer `:182` · "repeat poem" `:198` · **diffusion copy image (Ann)** `:218` · Copilot secrets (Huang FSE 2024) `:230` · anonymization myth (quasi-identifier SVG) `:246` · **Sweeney 87% Venn (SVG)** `:289` + Golle 63% caveat · Netflix+AOL merged `:312` ("Three Kinds of Leak" staircase and "Why Membership Alone Hurts" moved to `lec03-mia.html` §01 on 2026-09-11) |
| **02 — How Leakage Is Measured** | 15–22 | `:345` | attacker's toolkit `:352` · **membership inference (Shokri Fig 1) — the only MIA slide left; one-line "sensitive cohort ⇒ the bit is the secret" pointer** `:365` · model inversion `:383` · NYT v. OpenAI `:405` · Italy ban `:420` ("Privacy Is a Business Risk" slide deleted 2026-08 — content moved to note's "Regulators Step In" entry) · can we do better `:453` · **Four Different Privacy Questions** `:462` (encryption / access control / confidential computing / DP — added 2026-09-13) ("When Membership Is the Secret", the 7-slide Homer et al. 2008 block and "The Tell: Lower Loss" moved to `lec03-mia.html` §01–§03 on 2026-09-11; lec02 keeps only the MIA overview) |
| **03 — Differential Privacy** | 23–41 | `:490` | **two-worlds (full-width with/without-Alice SVG, redrawn larger 2026-09-10)** `:517` · **plausible deniability (with/without-Alice bars SVG; labels are KaTeX overlays since 2026-09-11)** `:558` · future-proof `:589` · **warm-up: guess the nationality (heights SVG; moved here from the "Look Alike" block 2026-09-11)** `:602` · randomness required (SVG) `:625` · **$(\varepsilon,\delta)$-DP definition** `:656` (plain-English lead-in `:670`) · reading $\varepsilon$ (scale bar) `:683` · $\varepsilon$ in the wild: two setups (Apple vs Census table) `:713` + the numbers (bar SVG) `:728` (Apple 4–8/item + audited 16/day, Census $\approx 17$) · what $\varepsilon$ does NOT mean `:759` · post-processing `:772` · **indistinguishability `:802` + heights (SVG)** `:811` · overlap is privacy `:815` · what DP does/doesn't `:827` · individuals not the crowd `:839` ("Meet $\delta$" deleted 2026-09-08; "Neighboring Datasets", "Meet $\varepsilon$: The Budget", "Many Samples Break It" deleted 2026-09-10 — $D/D'$ definition now in the note's "Formal Definition" detail, repeated-queries proof in the note's "Overlap Is Privacy" detail) |
| **04 — Achieving DP: Add Randomness** | 42–50 | `:849` | **the recipe (full-width compute→noise→release SVG, redrawn larger 2026-09-10)** `:856` · randomized response `:880` · **coin protocol, full-width two-coin tree (SVG, redrawn 2026-09-08, enlarged 2026-09-10)** `:893` · recover-the-rate worked example `:933` · why it's private `:942` · **Laplace mechanism + noise bell (SVG)** `:955` · sensitivity `:973` · Gaussian mechanism `:1005` ("Local vs Central DP", "Local DP in Products", "Inside Apple's Pipeline", "Noisy Count Example", "More Noise, More Privacy" deleted 2026-09-10 — local/central definitions now in the note's "Why It's Private" detail, the worked noisy count in the note's "Laplace Mechanism" detail) |
| **05 — Private Machine Learning** | 51–57 | `:1030` | from statistics to models `:1037` · naive hope fails `:1049` · **DP-SGD** `:1058` (clip+noise merged to one slide) · why clip, why noise `:1095` · utility cost (benchmark folded in) `:1108` · more data helps (SVG) `:1120` ("The Privacy Accountant" and the federated-learning quartet — FL, Gboard, FL Still Leaks, secure aggregation — deleted 2026-09-10; accountant theorem + accounting references now in the note's "DP-SGD" detail) |
| **06 — Frontier 2025–26** | 58–65 | `:1154` | private fine-tuning (Yu, Li 2022) `:1161` · **VaultGemma DP pretraining** `:1173` (added 2026-08) · private synthetic data + Apple Intelligence 2025 `:1194` · privacy auditing `:1208` · unlearning: after the fact `:1221` (retitled 2026-09-13) · **Apple PCC: device→PCC node→answer flow (SVG)** `:1233` (four-promises slide dropped 2026-09-08; its content sits in the note's "Privacy in the Stack" detail) · EU AI Act (GPAI duties since Aug 2025) `:1263` ("The Web-Scale Puzzle", "Open Problems" deleted 2026-09-10) |
| Wrap (demos / practice / takeaways) | 66–68 | — | **Practice: Boardroom Questions** `:1300` (3+3, same grammar as lec01) · demos slide `:1276` links the **randomized-response coin simulator** `demos/rr-simulator.html` (KaTeX formulas; screenshot `figs/rr-simulator.png` `:1291`) · key takeaways `:1341` ("Where to Go Deeper" deleted 2026-09-10 — reading pointers now in the note's "Key Takeaways" detail) |
| Closer | 69 | — | `$\varepsilon$` `:1353` |

**Key definitions / citations (all source-verified 2026-08; case slides and note briefs re-verified against primary sources 2026-09-13 — Garante 2023 limitation vs 2024 fine annulled 18 Mar 2026 as separate stages; Huang FSE 2024 candidates 2,702 / memorized 200 / valid 2 Stripe test keys; NYT v. OpenAI no merits ruling as of 2026-09):**
- $(\varepsilon,\delta)$-DP — `:656` (display formula `:662`) — relaxation from Dwork, Kenthapadi, McSherry, Mironov,
  Naor, EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006). "A 2006 Idea" `:497`
  keeps Dwork, McSherry, Nissim, Smith, TCC 2006 for $\varepsilon$-DP — matches `courses/privacy/lectures/01-dp/`.
- **Statistical indistinguishability** (heights example, Korea/Japan Gaussians) — `:706-:747` —
  "Overlap Is Privacy" `:815` carries the composition intuition (repeated-queries proof in the note); the warm-up `:602` (coin-flip highlight) now precedes "Randomness Is Required" in §03 (moved 2026-09-11).
- Randomized response — `:880` — Warner, JASA 1965. Interactive simulator: `demos/rr-simulator.html` (one respondent · whole survey · $\varepsilon$ vs accuracy; added 2026-09-08).
- DP-SGD — `:1058` — Abadi et al., ACM CCS 2016.
- De-anonymization — `:312` — Narayanan & Shmatikov, IEEE S&P 2008.
- Sweeney 87% (1990 census) — `:285` — Sweeney, Data Privacy WP3, 2000; Golle, WPES 2006 re-estimate (63%) added as caveat.
- $\varepsilon$ in the wild — `:713`, `:728` — Apple "Learning with Privacy at Scale" 2017; Tang et al. 2017 audit; US Census 2020 ($\varepsilon \approx 17$).
- VaultGemma DP pretraining ($\varepsilon \le 2$, sequence-level) — `:1173` — Google Research, 2025.
- Membership inference — `:365` — Shokri et al., IEEE S&P 2017 (Fig 1). The Homer et al. 2008 GWAS block (7 slides, Homer PLoS Genetics 2008 ·
  Sankararaman et al. Nature Genetics 2009 · Zerhouni & Nabel Science 2008) **moved to `lec03-mia.html` §02 on 2026-09-11**; see that leaf.

**Real images** (`figs/`, cropped + cited per GOTCHAS; all captions verified against the source PDF):
GPT-2 extraction `figs/gpt2-extraction.png` (Carlini et al. 2021, Fig 1) `:170`; Secret Sharer canary
exposure `figs/secret-sharer-exposure.png` (Carlini et al., USENIX Sec 2019, Fig 1) `:186`; ChatGPT
emission-rate bars `figs/nasr-emission-rate.png` (Nasr et al. 2023, arXiv:2562.17035, Fig 1) `:202`;
Stable-Diffusion copy `figs/calrini-ann.png` — **re-attributed 2026-08** to Carlini et al., "Extracting
Training Data from Diffusion Models", USENIX Security 2023, Fig 1 (Somepalli removed; verified against
arXiv 2301.13188) `:218`; Copilot credential pipeline `figs/huang-credential-leak.png` (Huang et al.,
FSE 2024, Fig 1) `:234`; black-box MIA diagram `figs/shokri-mia.png` (Shokri et al., IEEE S&P 2017,
Fig 1) `:374`; model-inversion face pair `figs/fredrikson-inversion.png` (Fredrikson, Jha, Ristenpart,
CCS 2015, Fig 1) `:388`; NYT complaint side-by-side `figs/nyt-complaint-p30.png` (NYT v. Microsoft &
OpenAI, S.D.N.Y. 1:23-cv-11195, complaint p. 30) `:408`; CIFAR-10 /
ImageNet accuracy vs $\varepsilon$ `figs/de-cifar-epsilon.png` (De et al. 2022, arXiv:2455.13650, Fig 1)
`:1112`; VaultGemma memorization bars `figs/vaultgemma-memorization.png` (Google, arXiv:2761.15001, Fig 1) `:1185`;
randomized-response simulator screenshot `figs/rr-simulator.png` (own render of `demos/rr-simulator.html`, 2026-09-08) `:1291`.
Duplication histogram `figs/carlini_duplicates.png` moved to `lec04-memorization.html`. Apple local-DP overview
(Apple 2017 Fig 1) and deep-leakage-from-gradients (Zhu, Liu, Han 2019 Fig 1) images deleted from `figs/` 2026-09-10 with their slides.
**SVG figures (21; lifecycle strip `:93` and boardroom card grid `:1304` added 2026-09-13):** quasi-identifier table `:250`, Sweeney linkage Venn `:289`, Netflix↔IMDb
linkage `:316`, two-worlds with/without-Alice rows (full-width) `:521`, plausible-deniability with/without bars `:562`, deterministic-vs-randomized release `:635`,
$\varepsilon$ scale bar `:691`, $\varepsilon$-in-the-wild bars `:731`, post-processing pipeline `:776`, height-distribution overlap `:811`,
recipe compute→noise→release (full-width) `:860`, randomized-response two-coin tree (full-width) `:897`, Laplace noise bell `:959`,
sensitivity bars `:983`, Gaussian-vs-Laplace bell `:1009`, DP-SGD pipeline `:1062`, more-data signal/noise bars `:1130`,
Private Cloud Compute flow `:1237`. (Eight SVGs — leak staircase, membership-secret timeline, GWAS flow, SNP table, $D_j$ number line,
one-SNP two-bells, NIH timeline, MIA loss-overlap — moved to `lec03-mia.html` 2026-09-11.) Citations use
`.cite-left`. Page number: bold `.slide-num` only. Intuition pass — points to
`courses/privacy/lectures/01-dp/` for rigor.

**2026-09-11 coordinated pass (66, unchanged count; per Albert's Slack page comments):** "Plausible Deniability" `:558` lost its SVG `<text>` labels; the four labels ($\Pr[\text{this output}]$, ratio $\le e^{\varepsilon}$, "move by at most $e^{\varepsilon}$", $\varepsilon=1$: at most $2.7\times$) are now KaTeX spans absolutely positioned over the SVG (percent coordinates, CSS colour tokens). "A Warm-Up: Guess the Nationality" moved from the "Look Alike" block to directly after "Future-Proof by Design" `:602`, so the heights example is met before "Randomness Is Required"; note article moved likewise (66 entries, order matches). Render = 66 pages; both slides checked at 60 dpi.

**2026-09-11 MIA move (77→66, per Albert's Slack request):** 11 slides moved out to `lec03-mia.html` — "Three Kinds of Leak" and
"Why Membership Alone Hurts" (§01), "When Membership Is the Secret", the seven Homer et al. 2008 slides and "The Tell: Lower Loss"
(§02). lec02 keeps "The Attacker's Toolkit" + "Membership Inference" (Shokri Fig 1) as its MIA overview; the latter gained the
one-line "if the cohort is sensitive, that one bit is the whole secret" pointer. Note file re-synced (66 entries, order matches;
the 11 matching articles moved to the lec03 note verbatim, including the per-SNP and power derivations). `lec02tech.html`
unchanged (no Homer/MIA content). Render = 66 pages; slide 16 checked at 60 dpi.
**2026-09-10 edit pass (93→77, per Albert's Slack page list):** 16 slides removed — Neighboring Datasets, Meet $\varepsilon$:
The Budget, Many Samples Break It (§03); Local vs Central DP, Local DP in Products, Inside Apple's Pipeline, Noisy Count
Example, More Noise More Privacy (§04); The Privacy Accountant, Federated Learning, FL in Your Pocket, FL Still Leaks,
Plugging the Leak (§05); The Web-Scale Puzzle, Open Problems (§06); Where to Go Deeper (wrap). "When Membership Is the
Secret" moved to directly after "Membership Inference". Four diagrams redrawn full-width with 17–26 px SVG type: Genome Leak
flow, Two Worlds, The Recipe, The Coin Protocol. Note file re-synced (77 entries, same order); rigorous content from the
deleted slides migrated into surviving entries' `.detail` blocks (neighboring datasets → Formal Definition; repeated-queries
theorem → Overlap Is Privacy; local vs central definitions → Why It's Private; worked noisy count → Laplace Mechanism;
privacy-accountant theorem + accounting references → DP-SGD; reading list → Key Takeaways). `lec02tech.html` unchanged
(still covers composition/Rényi accounting formally). Two orphaned figures deleted from `figs/`. Rendered audit of the four
redrawn slides at 60 dpi: no overflow.

**2026-09-08 second review round (94→93):** "Share resolved" column on the Homer results slide renamed "Smallest share detected" with a
one-line gloss (share = one person's fraction of the pooled DNA; 1 of 1,000 = 0.1%) and a full interpretation in the note; the
"$\varepsilon$ in the Wild: Two Setups" note entry expanded (Apple count-mean sketch, caps, retention, what came out, what the
per-donation bound means; Census 2010 reconstruction motivation, TopDown hierarchy/invariants/post-processing, zCDP → $\varepsilon$
conversion, release date, what the global bound means); "Private Cloud Compute: Four Promises" slide dropped (note article merged
into "Privacy in the Stack" detail); `demos/rr-simulator.html` now renders all formulas with KaTeX (local `reference/katex/`),
including the dynamic SE note and hover tooltip.

**2026-09-08 review pass (94→94, per Albert's Slack review of the 2026-09-04 build):** Homer block 10→8 slides — Fig 1
schematic and the "one SNP / sum 500,000 / Fig 2A / Fig 3" quartet replaced by three slides that interpret $D_j$ on a number
line, contrast one SNP (tilt ≈ 0.0004 vs noise ≈ 0.014) with the $\sqrt{m/n}$ aggregate using mia1's numbers, and summarise the
paper's findings in text; the three cropped Homer figures were deleted from `figs/`. "Plausible Deniability" rewritten with a
concrete with/without-Alice bar figure and the "odds move by at most $e^{\varepsilon}$" reading. "$\varepsilon$ in the Wild"
split into a setup table (Apple local DP per donation vs Census central DP on the whole file) and the number bars. "Meet
$\delta$" deleted (note keeps the detail). "The Coin Protocol" tree redrawn full-width. "Local DP in Products" split into a
Chrome/Apple/Microsoft table plus the Apple Fig 1 slide. "Privacy in the Stack" split into a PCC data-flow SVG plus a
four-promises slide (dropped again the same day, see above). New `demos/rr-simulator.html` (one respondent with animated coin tree · whole survey with true-vs-reported
bars and $\hat p$ · $\varepsilon$ vs standard-error chart with Monte Carlo dot), linked from the demos slide with a screenshot.
Note file re-synced (now 93 entries, titles match); `lec02tech.html` gained "Randomized Response: Privacy vs Accuracy" (22 sl).
Rendered audit of every edited slide at 60 dpi: no overflow.

**2026-09-04 figure revision (84→84, no text-only content slide left in §01–§05):** 10 public
figures added (list above; each cropped from the source PDF at 150 dpi and cited with figure number)
and 15 inline SVG diagrams added to previously bullet-only slides. Slide count, order, and the note
file (84 entries) unchanged. Rendered audit of all 25 edited slides at 60 dpi: no overflow.

**2026-09-04 Homer block (84→94):** per Albert's review — slides 14/15 SVGs (Sweeney Venn, Netflix↔IMDb) re-laid out to
remove text overflow; 10-slide Homer et al. 2008 block inserted in §02 between the Shokri MIA image and "The Tell", mirroring
the narrative of `courses/privacy/lectures/04-mia/mia1-foundations.html` at the same level of detail but with no proofs
(proofs and idealized-model derivations pushed to the note's `.detail` blocks, which point to mia1). Three figures cropped from
the open-access PDF, captions verified. Note file gained 10 matching entries (94, order matches). Rendered audit of slides
14, 15, 19–29 at 60 dpi: no overflow.

**2026-07-15 trim (9 slides):** Netflix+AOL merged; Shadow Models, MIA on Modern Models,
Extraction Scales With Size, Leaky Gradients cut from §02 (owned by Wk 3/4 and §05's "FL Still
Leaks"); "One Person Tells You Little" merged into the heights warm-up; Why Clip + Why Add Noise
merged; Utility Cost + Numbers on a Benchmark merged; duplicate "Frontier Models Still Memorize"
cut (§01's "Make ChatGPT Leak" covers it, same citation).

**2026-08 content revision (84→84):** every citation/number fetched and verified. Deleted
"Privacy Is a Business Risk" (§02, redundant with "Regulators Step In"; content absorbed into the
note). Added "Private Pretraining Arrives" (VaultGemma) to §06. Fixed: Ann-figure attribution
(Somepalli→Carlini USENIX Sec 2023); $(\varepsilon,\delta)$-DP origin (TCC→EUROCRYPT 2006, also in
`lec02tech.html`); Sweeney slide (Golle 63% caveat + correct WP3 cite); Apple/Census $\varepsilon$
values made precise with audit cite; Copilot slide gained Huang FSE 2024 cite. §06 refreshed:
Apple Intelligence DP synthetic data (2025), EU AI Act GPAI duties (Aug 2025). Note file synced
(84 entries, order matches).

**2026-08 note enrichment:** `lec02-privacy-dp-note.html` upgraded from speaker script to
**script + companion notes** (521→1034 lines; 84 entries unchanged). Heaviest math of the
note series, kept consistent with `courses/privacy/lectures/01-dp/` (dp2–dp5): full proofs
for the Laplace mechanism, post-processing invariance, basic/adaptive composition, group
privacy, the coin protocol's $\ln 3$, the RR unbiased estimator + Chebyshev sample bound,
and the privacy-loss tail lemma; Gaussian mechanism as Dwork & Roth Thm 3.22 with verified
sketch (full proof pointer: Thm A.1); DP-SGD theorem + three-step accounting from dp5.
Rigorous definitions (neighboring add/remove, $(\varepsilon,\delta)$-DP, $\Delta_1/\Delta_2$,
LDP, PLRV, clipping/noise multiplier) and verified backgrounds with primary-source links
(DMNS TCC 2006 DOI, Warner JASA 1965 scan, Abadi 2016, Gboard DP-FTRL, VaultGemma, Apple
PCC/synthetic data, EUR-Lex AI Act).

---

## lec03-mia.html

**Topic:** Membership inference attacks (~105 min full; **90-minute core path** skips 7 slides — 16, 18, 28, 29, 39, 40, 50 — and trims Boardroom to a 2-min presentation; the skip list lives only in the note's Contents entry — the Contents-slide line and the per-slide "Optional depth" badges were both removed from the main deck 2026-09-14 on Albert's request; nothing about the core path is visible on the main deck). What "was this example in the
training set?" means and why it matters (privacy audit, litigation, extraction
pre-step); overfitting/loss-gap intuition; shadow models at picture level; LiRA as
"compare to a population of reference models"; evaluation done right (TPR at low FPR);
MIA on LLMs and diffusion models; DP-vs-MIA in one line; 2025–26 frontier (strong-attack
wall, dataset inference, courtroom use). Intuition pass — the rigorous treatment lives
in `courses/privacy/lectures/04-mia/` (5-deck series); facts kept consistent with it.

### Sections (70 slides, ~105 min full / ~90 min core path (2026-09-14: 7 optional slides marked in the note only — the main-deck `.opt-badge` badges and Contents core-path line were added then removed the same day at Albert's request) — case-brief pass 2026-09-13 (66→70: Where This Lecture Sits, Base Rates, Reading MIA Results at Scale, Practice: Boardroom Questions); restructured 2026-09-11 (63→47, then +14 moved in from `lec02-privacy-dp.html`, then +5 in the coordinated pass the same day: new-record decision, TPR/FPR, ROC, AUC, LiRA-on-LLMs); content-revised 2026-08, all citations source-verified; figure pass 2026-09)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents (8 sections, two-column TOC; no core-path line — that lives in the note) / **NEW Where This Lecture Sits (lifecycle strip, detection stage highlighted; audit finds leakage, cannot certify absence)** | 1–3 | `:40`, `:50`, `:88` | |
| **01 — The Question** | 4–11 | `:134` | one yes-or-no question (definition + **full-width worlds→model→attacker SVG with KaTeX overlays, enlarged 2026-09-11**) `:141` · **The Simplest Leak (leak-ladder staircase SVG; boxes spread and arrows shortened 2026-09-14 so arrowheads clear the box captions)** `:176` · **Why Membership Alone Hurts (cancer-cohort harm)** `:206` · **When Membership Is the Secret (disease / trial / chat-log / pirated-book timeline SVG, from lec02)** `:215` · **Who Asks, and Why (audit / courts / extraction)** `:240` · threat model `:253` · score + threshold `:267` |
| **02 — The First Attack** (Homer et al. 2008; 7 slides from lec02 §02 + 2 new) | 12–21 | `:297` | genome leak intro (**full-width averages→attacker flow SVG**) `:305` · SNP primer (SVG) `:342` · **Homer's statistic $D_j$ on a number line (SVG + `math-block`)** `:372` · **NEW Why One SNP Says Nothing ($D_j=(M_j-\mathrm{Pop}_j)(2Y_j-1)$ `math-block` + mean/noise table: $2p(1-p)/n\approx0.0004$ vs $0.014$)** `:400` · one SNP whispers, 500,000 shout (two-bells SVG) `:416` · **NEW How Many SNPs Are Enough? ($n$ = cohort, $m$ = SNPs defined up front; $\mu=2\sqrt{m\bar v/n}$; power table 28k / 39k / 390k; idealized-model caveat; the $\alpha=10^{-6}$ line dropped 2026-09-11)** `:446` · what the paper reported (check-list + smallest-share table) `:470` · NIH policy impact (**5-node timeline SVG: Jul 15 2008 accepted → Aug 28 2008 NIH fact sheet → Aug 29 published → Oct 3 Zerhouni &amp; Nabel → Nov 1 2018 NOT-OD-19-023 re-opening; Outcome as of 2026-09**) `:495` · Homer→ML table `:524` |
| **03 — The Basic Attack** | 22–29 | `:543` | train loss < test loss `:550` · loss score + 3-line threshold attack `:576` · **The Two Bells (member/non-member loss overlap SVG + threshold)** `:589` · **Overfitting Drives MIA (small vs large gap SVG; caveat: small gap ≠ safe)** `:611` · confidence baseline (**Salem Fig. 11, real fig**) `:632` · Yeom theory anchor (sufficient, not necessary; **Yeom Fig. 2, real fig**) `:650` · Colab demo `:665` |
| **04 — Shadow Models** | 30–34 | `:682` | one threshold is crude `:689` · shadow idea (**Shokri Fig. 2, real fig**) `:717` · **shadow pipeline (SVG; labeled in/out outputs train the attack)** `:732` · **why it transfers (full-width target-vs-shadow bells SVG, 17–22 px type, enlarged 2026-09-11)** `:759` |
| **05 — Stronger Attacks** | 35–47 | `:797` | difficulty vs membership (**Carlini Fig. 3, real fig**) `:804` · **LiRA: likelihood ratio, 3 steps + $\Lambda(x)$ `math-block`** `:824` · **NEW Deciding on a New Record (4 def-cards: score $s\'$, fit the two bells for $x\'$, $\Lambda(x\')$, decide $\Lambda \gt \tau$; shadows on random halves of the pool)** `:838` · **in-vs-out bells, worked example ($\mu_{\mathrm{out}}=2$, $\mu_{\mathrm{in}}=6$, $\sigma=1.5$, $s\'=5$ ⇒ $\log\Lambda\approx1.78$, $\Lambda\approx5.9$; wide SVG + KaTeX overlays)** `:852` · label-only (**Choquette-Choo Fig. 1, real fig**) `:877` · **NEW Scoring an Attack: TPR and FPR (confusion table + `math-block` TPR/FPR definitions; balanced accuracy)** `:897` · **NEW The ROC Curve (bells with $\tau_1$–$\tau_3$ → ROC points, full-width SVG + overlays)** `:914` · **NEW AUC and Its Blind Spot ($\mathrm{AUC}=\Pr[\text{score(member)}\gt\text{score(non-member)}]$; curves A/B with equal AUC SVG)** `:954` · average accuracy lies (**Carlini Fig. 2, real fig**) `:980` · **TPR at low FPR** (log-log ROC left edge; **Carlini Fig. 1, real fig**) `:995` · **NEW Base Rates: What an Accusation Is Worth (FPR 10%/1%/0.1% → ≈9%/≈50%/≈91% correct flags at 1 member per 100 candidates, TPR = 1; callouts For an audit / For a legal claim / Why AUC hides it)** `:1011` · **NEW Does LiRA Work on LLMs? (Hayes … Cooper NeurIPS 2025 Fig. 2, real fig: AUC 0.55–0.70 for 10M–1B models, TPR@FPR non-monotone in size)** `:1038` |
| **06 — What It Means** | 48–52 | `:1055` | DP caps the attacker (one-line DP recall; **full-width two-worlds→DP training→output bells SVG, 17–21 px type, enlarged 2026-09-11; ratio $\le e^{\varepsilon}$ label is a KaTeX overlay**) `:1062` · TPR $\le e^{\varepsilon}\cdot$FPR$+\delta$ (**ROC SVG widened to 470 px, 15 px labels**) `:1095` · auditing flips the attack (empirical $\varepsilon$ + bug-catch / looseness) `:1120` · canaries + one-run auditing (**Steinke Fig. 3, real fig**) `:1140` |
| **07 — Modern Models** | 53–62 | `:1162` | Min-K% (**Shi Fig. 1, real fig**) `:1169` · **diffusion duplication histogram (real fig)** `:1183` · Duan web-scale doubt (**Duan Fig. 1, real fig**) `:1203` · why scale breaks it (+ exceptions: rare / duplicated / fine-tuning data) `:1214` · benchmark trap (temporal confound, blind baselines; **Das Fig. 1, real fig**) `:1243` · **Give the Attack Everything (Hayes wall; Hayes Fig. 2(a), real fig)** `:1262` · **dataset inference (Maini Fig. 1, real fig)** `:1281` · **MIA in the Courtroom (Zhang Fig. 1, real fig)** `:1296` · **NEW Reading MIA Results at Scale (four boxes: strong on small supervised models / ambiguous at web scale / benchmarks can mislead / weak MIA ≠ no memorization; status contested as of 2026-09)** `:1304` |
| **08 — Defenses** | 63–67 | `:1323` | shrink the gap `:1330` · heuristics not proof `:1342` · DP-SGD (clip + noise SVG; MIA-focused) `:1370` · defender's checklist `:1403` |
| **Practice: Boardroom Questions** / Takeaways / Closer | 68–70 | — | boardroom (3 "before you sign" + 3 "ask the vendor", same grammar as lec01/lec02) `:1414` · `:1459` (5 check bullets incl. Homer 2008; MIA = stress test, not certificate), `:1479` |

**Key definitions / citations (all source-verified 2026-08; Homer block verified 2026-09-04/08 in lec02):**
- Homer et al. 2008 membership inference on GWAS allele frequencies — `:334`, `:489` — Homer et al., PLoS Genetics 4(8) e1000167, 2008
  (distance statistic $D_j = |Y_j-\mathrm{Pop}_j| - |Y_j-M_j|$ on `:375`, paper sign; the privacy course mia1 deck uses the opposite sign).
  Idealized-model numbers on `:400`–`:462` (tilt $2p(1-p)/n \approx 0.0004$ vs noise $\approx 0.014$ at $n=1000$; $\approx 28{,}000$ SNPs for
  power $0.5$ at $\alpha=10^{-6}$, $39{,}000$ for power $0.8$, $390{,}000$ at $n=10{,}000$) follow Sankararaman, Obozinski, Jordan, and Halperin,
  Nature Genetics 2009 (`:440`, `:462`) — labelled as such, not the paper's; derivations in the note ("Why One SNP Says Nothing",
  "How Many SNPs Are Enough?"). NIH response `:516` — NIH fact sheet "Modifications to GWAS Data Access", 28 Aug 2008; Zerhouni & Nabel, Science 322:44, 2008; NIH Notice NOT-OD-19-023, 1 Nov 2018 (re-opening of genomic summary results for most studies). Proof-level version:
  `courses/privacy/lectures/04-mia/mia1-foundations.html` §02.
- Shadow models — `:727` — Shokri, Stronati, Song, and Shmatikov, IEEE S&P 2017.
- Loss attack / advantage-vs-gap — `:584`, `:659` — Yeom, Giacomelli, Fredrikson, and Jha,
  "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting", IEEE CSF 2018
  (full title restored 2026-08). Overfitting **sufficient, not necessary** — matches
  `courses/privacy/lectures/04-mia/` (mia3).
- Confidence baseline — `:645` — Salem et al., "ML-Leaks", NDSS 2019 (re-attributed 2026-08;
  was wrongly cited to Shokri 2017).
- Likelihood-ratio framing — `:833` — Sablayrolles et al., ICML 2019 (shares the LiRA cite line).
- LiRA + TPR-at-low-FPR standard — `:833`, `:1009` — Carlini et al., "Membership Inference
  Attacks From First Principles", IEEE S&P 2022.
- Label-only — `:891` — Choquette-Choo, Tramèr, Carlini, and Papernot, ICML 2021.
- $(\varepsilon,\delta)$-DP — `:1091` — Dwork, Kenthapadi, McSherry, Mironov, and Naor,
  EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006 — same fix as lec02).
- One-run auditing — `:1155` — Steinke, Nasr, and Jagielski, NeurIPS 2023.
- Min-K% — `:1178` — Shi et al., ICLR 2024.
- Diffusion extraction/duplication — `:1198` — Carlini et al., USENIX Security 2023, Fig. 5.
- Web-scale doubt — `:1208` — Duan et al., COLM 2024.
- Blind baselines / temporal confound — `:1257` — Das, Zhang, and Tramèr, DATA-FM at ICLR 2025
  (direction fixed 2026-08: members are the *older* text, non-members post-cutoff).
- Strong-attack wall — `:1276` — Hayes, Shumailov, et al., NeurIPS 2025. The same paper\'s Fig. 2 (LiRA on 10M–1B compute-optimal models, log-log ROC + TPR at fixed FPR) is "Does LiRA Work on LLMs?" `:1038` (added 2026-09-11; arXiv 2505.18773, Cooper is last author).
- Dataset inference — `:1290` — Maini, Jia, Papernot, and Dziedzic, NeurIPS 2024.
- MIA-as-evidence position — `:1302` — Zhang, Das, Kamath, and Tramèr, IEEE SaTML 2025.
- DP-SGD — `:1398` — Abadi et al., ACM CCS 2016.

**Real images (16, all cropped from the cited PDFs at 150–250 dpi, figure numbers verified against captions):**
`figs/salem-max-posterior.png` (ML-Leaks Fig. 11) `:636` · `figs/yeom-advantage-gap.png` (Yeom Fig. 2) `:657` ·
`figs/shokri-shadow-training.png` (Shokri Fig. 2) `:725` · `figs/carlini-lira-fig3-per-example.png` (Carlini 2022 Fig. 3) `:807` ·
`figs/choquette-label-only.png` (Choquette-Choo Fig. 1) `:881` · `figs/carlini-lira-fig2-roc-scales.png` (Carlini 2022 Fig. 2) `:988` ·
`figs/carlini-lira-fig1-tpr-fpr.png` (Carlini 2022 Fig. 1) `:1007` · `figs/hayes-llm-mia-fig2.png` (Hayes … Cooper NeurIPS 2025 Fig. 2(a,b), added 2026-09-11) `:1042` · `figs/steinke-one-run-eps.png` (Steinke Fig. 3) `:1143` ·
`figs/shi-mink-overview.png` (Shi Fig. 1) `:1177` · `figs/carlini_duplicates.png` (Carlini diffusion, USENIX Security 2023, Fig. 5;
attribution verified against arXiv 2301.13188; also used by `lec04-memorization.html`) `:1187` ·
`figs/duan-auc-vs-size.png` (Duan Fig. 1) `:1207` · `figs/das-wikimia-pca.png` (Das Fig. 1, appendix) `:1255` ·
`figs/hayes-compute-optimal-mia.png` (Hayes Fig. 2(a)) `:1265` · `figs/maini-dataset-inference.png` (Maini Fig. 1) `:1289` ·
`figs/zhang-training-data-proof.png` (Zhang Fig. 1) `:1301`.
**SVG figures (23):** member/non-member worlds → model → attacker (full-width, KaTeX overlays) `:150`, leak-ladder staircase `:188`, membership-secret timeline `:219`, score axis + threshold `:279`,
GWAS averages→attacker flow (full-width) `:312`, SNP table `:346`, Homer $D_j$ number line `:377`, one-SNP-vs-500k two-bells `:420`,
NIH timeline `:498`, train/test loss curves + gap `:558`, member/non-member loss overlap + threshold `:593`, small-gap vs large-gap bells `:615`,
one-threshold-two-classes `:701`, shadow pipeline `:735`, target vs shadow bells (full-width) `:763`, in-vs-out bells (worked example, 760-wide, KaTeX overlays) `:855`, bells + thresholds → ROC curve (full-width, KaTeX overlays) `:919`, two ROC curves with equal AUC `:963`,
two neighbouring worlds → DP training → output bells (full-width) `:1066`, ROC with DP ceiling (470 px) `:1103`, small-model vs LLM bells `:1226`,
attack-success vs attack-strength (regularization vs DP bound) `:1354`, clip + noise `:1382`;
plus one `diagram-flow`: auditing `:1123` (the member/non-member worlds `diagram-flow` became the full-width SVG `:150` on 2026-09-11). Other blocks: `math-block` `:375`, `:403`, `:555`, `:832`, bells worked example `:869`, TPR/FPR `:906`, AUC `:957`; `code-block` `:579`.
Citations use `.cite-left` with figure numbers. Page number: bold `.slide-num` only.

**2026-08 content revision (59→63):** every citation/number fetched and verified (deck is
nearly number-free; no invented results tables found). Added: "Who Asks, and Why" (§01);
"Give the Attack Everything" (Hayes 2025 strong-MIA wall), "Ask About a Dataset, Not a
Record" (Maini dataset inference), "MIA in the Courtroom" (Zhang SaTML 2025) to §06.
Fixed: benchmark-trap direction (members older, not newer); "precision at low FPR" →
"TPR at low FPR" (3 places); "zero gap ⇒ safe" folklore removed (sufficient-not-necessary);
$(\varepsilon,\delta)$-DP origin TCC→EUROCRYPT 2006; ML-Leaks attribution; Yeom full title.
`lec03tech.html` audited — math correct, no changes. Note file synced (63 entries, order matches).
**2026-08 note enrichment:** `lec03-mia-note.html` upgraded from speaker script (395 lines) to Script &amp; Companion Notes (831 lines): per-entry `.detail` blocks with rigorous definitions (MI game, TV, NP/LiRA statistics, (ε,δ)-DP, DP-SGD, Min-K%), full proofs (Yeom Thm 2, NP lemma, LiRA quadratic + z-test corollary, DP hypothesis-testing bound + corollaries, shadow-model Prop/Thm/Cor, benchmark-trap Prop, post-processing), and 19 verified links — all consistent with `courses/privacy/lectures/04-mia/`.

---
**2026-09 figure pass (63 slides, unchanged count):** every bullet-only content slide now carries a
real cited figure or an inline SVG (14 new PDF crops in `figs/`, 15 new SVGs, one `diagram-flow`; see lists above).
Figure slides use the image-beside-text `grid-2` pattern; wide overview figures (Min-K%, Duan, Maini, Zhang) stack
below the bullets. All 32 edited slides re-rendered at 60 dpi and checked for overflow. Added the LR formula
$\Lambda(x)$ as a `math-block` `:648`. Note file: one "Slide figure" sentence per new figure (14 articles).

**2026-09-11 structure pass (63→47):** re-read against the updated `lec02-privacy-dp.html` (77 sl) and
cut what lec02 already teaches — the leak ladder + "Why Membership Alone Hurts" + cancer-cohort harm (lec02 §02–03),
the identical two-bells-overlap SVG (lec02 :1220), the standalone $(\varepsilon,\delta)$-DP definition slide, and the
3-slide DP-SGD block (lec02 §07; one MIA-focused DP-SGD slide kept). Merged internal pairs: definition + two-worlds
→ "One Yes-or-No Question"; loss score + 3-line code; "Overfitting Drives MIA" → "The Two Bells" (small vs large gap);
"Learn the Member Signal" → pipeline muted line; per-example calibration + likelihood ratio + LiRA → one LiRA slide;
three ROC slides → two (Average Accuracy Lies, TPR at Low FPR); "Trust but Verify" → "Auditing Flips the Attack";
"MIA Meets Foundation Models" → Min-K% lead-in; "An Open Debate" → "Why Scale Breaks It" muted line. All 15 real
figures kept; 7 SVGs dropped (leak ladder, world cards, two-bells overlap, output vector → classifier, per-example
baseline, ROC tail, schematic accuracy-vs-ε); unused `.ta-algo` CSS removed. Div nesting validated (all slides at
depth 3), render = 47 pages, 11 edited slides checked at 60 dpi. Note file re-synced (47 entries, donor `.detail`
sections merged into the surviving articles by h3; order matches). `lec03tech.html` unchanged (no references to cut slides).

**2026-09-11 MIA move (47→61, per Albert's Slack follow-up):** most of lec02's MIA material now lives here. §01 regained
"The Simplest Leak" (leak ladder) and "Why Membership Alone Hurts" (cancer-cohort harm) from the 63-slide build and took
"When Membership Is the Secret" (timeline SVG) from lec02; the merged "One Yes-or-No Question" lost its sensitive-cohort line.
New §02 "The First Attack" = lec02's seven Homer et al. 2008 slides plus two new detail slides, "Why One SNP Says Nothing"
(factorization $D_j=(M_j-\mathrm{Pop}_j)(2Y_j-1)$, per-SNP mean/noise table) and "How Many SNPs Are Enough?" ($\mu=2\sqrt{m\bar v/n}$,
power table); sections 02–07 renumbered 03–08 and the Contents slide became a two-column 8-item TOC. §03 split the merged
two-bells slide back into "The Two Bells" (overlap SVG + threshold, the copy lec02 had) and "Overfitting Drives MIA" (small vs
large gap). Three diagrams enlarged per Albert's page comments: "Why It Transfers" and "DP Caps the Attacker" redrawn as
full-width 960-wide SVGs with 17–22 px type, "A Concrete Bound" ROC widened 330→470 px with 15 px labels. Key Takeaways gained
a Homer bullet. Note file re-synced (61 entries, order matches): the eleven lec02 articles moved verbatim (with "Lecture 4" and
"below" cross-references replaced by in-deck section pointers), the "One SNP Whispers" derivation split across the two new
articles, restored articles taken from the 63-slide note, and "One Yes-or-No Question" trimmed back to the MI game +
TPR/FPR + three-faces proposition. Render = 61 pages; all 25 new/edited slides checked at 60 dpi (Contents, the SNP
math slide and the ROC label were fixed after the first pass). `lec03tech.html` unchanged.

**2026-09-11 coordinated pass (61→66, per Albert's Slack page comments):** "One Yes-or-No Question" diagram redrawn as a
full-width 960-wide SVG (two worlds → model → attacker) with KaTeX overlays for $x$ and $f_\theta$. "How Many SNPs Are Enough?"
defines $n$ and $m$ up front and drops the $\alpha=10^{-6}$ line. §05 gained "Deciding on a New Record" (how a fresh $x'$ is
scored, fitted, and classified after LiRA; four def-cards), turned "Two In-vs-Out Bells" into a worked example with numbers
($\mu_{\mathrm{out}}=2$, $\mu_{\mathrm{in}}=6$, $\sigma=1.5$, $s'=5$), and gained the evaluation trio before "Average Accuracy
Lies": "Scoring an Attack: TPR and FPR" (confusion table + formal definitions), "The ROC Curve" (threshold sweep → curve, SVG),
"AUC and Its Blind Spot" (definition, equal-AUC curves A/B). "Does LiRA Work on LLMs?" (Hayes … Cooper NeurIPS 2025 Fig. 2,
16th real figure) closes §05. "DP Caps the Attacker" shows $e^{\varepsilon}$ as a KaTeX overlay instead of SVG text. Note file
re-synced (66 entries, order matches): five new articles with TPR/FPR/ROC/AUC definitions, the LiRA decision procedure, and the
Hayes LLM-MIA setup; SNP and bells articles updated. Render = 66 pages; 10 new/edited slides checked at 60 dpi (bells, AUC and
LLM-MIA layouts fixed after the first pass). Follow-up the same night (Albert Slack #24): the bells slide now states the decision rule
explicitly (member iff $\Lambda \gt \tau$; $\tau=1$ says member, $\tau=10$ would not) instead of the confusing "$\tau \lt 5.9$"; "TPR at Low
FPR" gained two bullets on why the low-FPR regime matters (non-members vastly outnumber members, so a 1% FPR buries true hits).
Note articles for both updated; three stray BEL-character `pprox` typos in the bells note article fixed.

**2026-09-12 tech supplement update (`lec03tech.html` 11→20, PR #30):** the supplement now carries the formal side of every
2026-09-11 addition. Homer block: factorization $D_j=(M_j-\mathrm{Pop}_j)(2Y_j-1)$ with both-case check; per-SNP moments
(out mean 0, var $v_j/n$; in mean $2v_j/n$) with derivation; aggregate $T$, $\mu=2\sqrt{m\bar v/n}$, power $\Phi(\mu-z_\alpha)$,
$m\approx28{,}000$ (power 0.5) / $39{,}000$ (power 0.8) at $\alpha=10^{-6}$, $n=1000$, $\bar v=0.2$. LiRA block: algorithm
rewritten (shadows on random halves, logit scores), "Why the Logit Scale" ($\phi=-\ell-\log(1-e^{-\ell})$), log-LR with the
global-$\sigma^2$ pooling note, "The Worked Example, Checked" (equal-variance linear rule; main-deck numbers give
$\log\Lambda\approx1.78$, $\Lambda\approx5.9$; $\tau=1\Leftrightarrow s^\star\gt4$, $\tau=10\Leftrightarrow s^\star\gt5.30$), offline LiRA
$\Pr[Z\le s^\star]$. Evaluation block: TPR(τ)/FPR(τ)/ROC set/balanced accuracy, "AUC Is a Probability" (Mann–Whitney, integral
proof), "Why Low FPR: Base Rates" (precision at TPR=1 for π=1/101: 0.09 / 0.50 / 0.91 at FPR 10% / 1% / 0.1%), TPR@α with the
Hayes NeurIPS 2025 scale check (AUC ≤ 0.7, TPR@10⁻⁴ ≈ 1%; the 10⁻⁴ figure was removed 2026-09-13 as unverifiable). Note file unchanged (already in sync). Lint ok; 20 pages rendered,
new slides checked at 60 dpi.

**2026-09-13 case-brief pass (66→70, PR #31, slides-review brief 2026-09-13):** four slides added — "Where This Lecture Sits"
(lifecycle strip, detection highlighted), "Base Rates: What an Accusation Is Worth" (Bayes table, audit / legal / AUC callouts),
"Reading MIA Results at Scale" (four-box conclusion, status as of 2026-09), "Practice: Boardroom Questions" (3+3). Story-first
Homer block: plain-language line on each formula slide; "What the Paper Reported" separates lab shares (0.15–0.25%, zero false
positives) from the simulated 0.1%; NIH slide extended with the Nov 2018 NOT-OD-19-023 re-opening (Outcome callout was outdated).
MIA framing softened throughout ("useful privacy stress test, not a certificate of no leakage"); "Why It Transfers" reworded to
training procedure + data distribution. Label-only bullet corrected ("reported to match confidence-vector attack accuracy, Fig. 1";
the earlier "≈4 pp" misread the paper). Unverifiable Hayes "TPR@10⁻⁴ ≈ 1%" removed from the note and tech (replaced by the verified
15.4% ± 0.6% coin-flip share at FPR 10⁻³, 302M model). Note (70 entries, order matches): intro rewritten; every real incident /
paper figure carries a `Case background` brief — Homer 2008 and NIH in the 7-field incident format (NIH chronology table: paper →
immediate 2008-08-28 change → 2018-11-01 follow-up policy, primary sources), 15 papers in the uniform format *attacker access /
target model·data / member definition and duplicate control / metric·operating point / result / limitation / figure / follow-up
status* (Homer table, Sankararaman, Yeom, Salem, Shokri, Carlini LiRA ×2, Choquette-Choo, Hayes, Steinke, Shi, Carlini diffusion,
Duan, Das, Maini, Zhang); h3 labels normalized to `Case background` / `Technical depth — optional` / `References`; all
`courses/privacy/…` derivation pointers replaced by `lec03tech.html` slide pointers or paper references; "55% accuracy" example →
60% / advantage 0.20 (Carlini Fig. 2); unverified "Panel D 99.9/0.1" and "Cooper 2026" lines dropped. Tech (20 sl): "Intuition:"
muted line before the formal block on slides 3, 4, 7, 10, 15; slide 17 scale-check line corrected. Lint ok ×3; edited slides
rendered at 60 dpi. Estimated running time 100 → ~105 min.

**2026-09-14 core-path + base-rate pass (PR #31, reviewer request):** no slides cut. Seven slides form the skip set of a 90-minute core path (Why One SNP Says Nothing, How Many SNPs Are Enough?, A Theory Anchor, Try It Yourself, Two In-vs-Out Bells, Label-Only Attacks, A Concrete Bound; ≈ 12 min of slides + ≈ 5 min of Boardroom discussion), listed in the note's Contents entry only (top-right `.opt-badge` badges and a Contents-slide line were added, then removed later the same day at Albert's request — lecture-operation info stays off the main deck). The note's Contents entry carries the list with a one-line reason per slide; each optional article is labelled under its title. Base-rate convention unified to π = 1/100 ("one true member per 100 candidates") on the main deck, the note table and `lec03tech.html` slide 16 (was π = 1/101 on tech; rounded values 0.09 / 0.50 / 0.91 unchanged).


## lec04-memorization.html

**Topic:** Memorization & training-data extraction (~90 min). What memorization is
(verbatim / near-duplicate / stylistic; extractable vs discoverable at intuition level);
canary/exposure measurement; the GPT-2 extraction pipeline as a picture; the
"repeat forever" poem attack on an aligned production chatbot; scaling drivers
(size, duplication, context) at qualitative level; diffusion-model copies; copyright
touchpoint (two slides — full treatment in the backup copyright deck); mitigations and
the 2025–26 frontier. Intuition pass — the rigorous treatment lives in
`courses/privacy/lectures/03-memorization/` (exposure, k-eidetic, scaling-law decks);
facts kept consistent with it.

### Sections (65 slides, ~98 min full / 90-min core path via 7 optional slides listed in the note only (main-deck badges removed 2026-09-14) — content-revised 2026-08 from 59; figure pass 2026-09 58→60; Cooper 2026 frontier pass 2026-09-11 60→62; case-brief + core-path pass 2026-09-14 62→65; all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents / Where This Lecture Sits | 1–3 | `:41`, `:54`, `:85` | Contents is a plain 6-item TOC (core-path list lives in the note only, 2026-09-14) · **Where This Lecture Sits (lifecycle, Evidence highlighted; added 2026-09-14)** `:85` |
| **01 — What Is Memorization** | 4–16 | `:128` | working definition + **Gatsby prefix → Llama 1 30B → true-suffix card diagram (HTML, after Cooper Fig 1; replaced the low-res image 2026-09-11)** `:168` · **Degrees of Copying (taxonomy SVG: verbatim → near-verbatim → specific fact → style/pattern; technical claim ≠ legal meaning; replaced Three Flavors 2026-09-14)** `:186` · $k$-extractable + **prefix→suffix SVG** `:223` · **Extractable vs Discoverable (added 2026-08; reworded 2026-09-14 as two games, no containment)** `:252` · why it happens + **loss-bars SVG** `:265` · **Some Memorization Is Necessary (Feldman Fig 1(a), real fig)** `:293` · Secret Sharer + **Secret Sharer Fig 6 (real fig)** `:308` · canary `:325` · **canary-leak pipeline (SVG)** `:337` · exposure + **Secret Sharer Fig 7 (real fig)** `:362` · pattern-vs-record SVG `:379` |
| **02 — Extracting Text from LLMs** | 17–27 | `:402` | canary-vs-wild SVG (**full-width 960, 21–27 px type since 2026-09-11**) `:411` · **GPT-2 PII (real fig)** `:433` · **extraction pipeline (SVG; redrawn 2026-08 with 1,800/604 numbers)** `:457` · confidence signal + **zlib-vs-perplexity Fig 3 (real fig)** `:488` · what came out (604 strings) + **Table 1 (real fig)** `:505` · repeat-forever prompt + **ChatGPT screenshot Fig 5 (real fig)** `:519` · **loop breaks (SVG)** `:540` · scale of the leak (10,000+ / $200 / 150×) + **Nasr Fig 1 (real fig)** `:561` · patched-not-solved + **Nasr Fig 9 extrapolation (real fig)** `:578` · Colab demo `:591` |
| **03 — How Much, and Why It Grows** | 28–36 | `:606` | measurable fraction + **Carlini Fig 2(a,b) (real fig; re-cropped at 250 dpi 2026-09-11)** `:615` · three drivers (size / duplication / **context** — third driver fixed 2026-08, was "training length") `:630` · **Bigger Means More — Carlini Fig 1(a) (real fig; replaced SVG 2026-09)** `:643` · **Duplication Is the Big One — Kandpal Fig 1 (real fig; replaced SVG 2026-09)** + ~1000× line `:659` · long tail of duplicates + **Kandpal Fig 3(a) (real fig)** `:675` · **A Predictable Curve — Carlini Fig 1 (real fig) + "prompt length = context" explanation (2026-09-11)** `:692` · **Reading the Curves (added 2026-09; GPT-J ≥1% bullets over a full-width log-linear SVG, 21 px type since 2026-09-11)** `:705` |
| **04 — Image & Diffusion Models** | 37–43 | `:742` | not just text + **Somepalli Fig 1 pairs (real fig)** `:751` · diffusion picture `:766` · **Ann Graham Lotz copy (real fig; 94/175M added 2026-08)** `:779` · **duplication histogram (real fig; Somepalli cite removed 2026-08)** `:803` · Somepalli ~1.9% near-duplicates + **Somepalli Fig 5 histograms (real fig)** `:815` |
| **05 — Copyright & the Law** | 44–47 | `:838` | **compressed 6→2 slides 2026-08** (backup copyright deck owns the topic) · NYT v. OpenAI + **complaint p. 30 side-by-side (real fig; replaced SVG 2026-09)** + Mar 2025 MTD ruling `:847` · Copy or Transform? (fair-use collision; Bartz v. Anthropic as three callouts: fair-use ruling on inputs / piracy finding / USD 1.5B settlement final approval July 2026, status as of 2026-09) `:863` · **The Same Output, Different Questions (stakeholder grid `.stake`: data subject / copyright holder / ML team / product; added 2026-09-14)** `:879` |
| **06 — Mitigations & Frontier** | 48–62 | `:899` | toolbox `:906` · deduplication (Lee ACL 2022) + **Lee Fig 3 / Fig 2 (real figs)** `:919` · dedup limits + near-duplicate SVG `:935` · output filtering + n-gram-filter SVG `:959` · DP + **VaultGemma Fig 1 (real fig)** `:989` · privacy tax + trade-off SVG `:1005` · no silver bullet `:1031` · **Frontier: Whole Books Come Back (Cooper 2025 Fig 3, real fig)** `:1039` · **Frontier: Chatbots Recite Books Too (Ahmed 2026 Fig 1, real fig; split out 2026-09)** `:1054` · **NEW Frontier: Near-Verbatim Counts Too (Cooper COLM 2026 k-CBS Fig 3, real fig; Levenshtein $\varepsilon$, OLMo 2 32B 1.4%→2.6%)** `:1070` · **NEW Frontier: Extraction Needs a Control Group (Cooper 2026 "First Principles" Fig 3, real fig; matched post-cutoff non-members, 7.54% vs 1.82%)** `:1086` · **Frontier: How Much Fits? (Morris Fig 1, real fig; 3.6 bits/param)** `:1102` · memorized PII + PII-pipeline SVG `:1119` · open problems (+ unlearning remove-vs-suppress question and Cooper/Lemley cites, 2026-09-11) `:1154` |
| Boardroom / Takeaways / Closer | 63–65 | — | **Practice: Boardroom Questions (3+3; added 2026-09-14)** `:1167` · `:1210`, `:1222` |

**Key definitions / citations (all source-verified 2026-08):**
- $k$-extractable (Def 3.1), scaling drivers (capacity / duplication / context), GPT-J ≥1% —
  `:223`, `:630`, `:692` — Carlini et al., "Quantifying Memorization Across Neural Language
  Models", ICLR 2023 (arXiv 2202.07646).
- GPT-2 extraction, Fig 1 PII, 604 of 1,800 candidates — `:433`, `:457` — Carlini et al.,
  "Extracting Training Data from Large Language Models", USENIX Security 2021 (arXiv 2012.07805).
- Secret Sharer canary/exposure — `:308` — Carlini, Liu, Erlingsson, Kos, and Song,
  USENIX Security 2019 (arXiv 1802.08232).
- Extractable vs discoverable (Defs 1–2); poem attack; 10,000+ strings / $200 / 150× —
  `:252`, `:519`, `:561` — Nasr et al., "Scalable Extraction of Training Data from (Production)
  Language Models", arXiv 2311.17035 (2023; published at ICLR 2025 as "…from Aligned,
  Production Language Models").
- Learning requires memorization (long tail) — `:293` — Feldman, STOC 2020.
- Superlinear duplication effect (10 copies → ~1000× more generation) — `:659` — Kandpal,
  Wallace, and Raffel, ICML 2022 (arXiv 2202.06539).
- Deduplication (10× less memorized text) — `:919` — Lee et al., "Deduplicating Training Data
  Makes Language Models Better", ACL 2022 (arXiv 2107.06499).
- Diffusion extraction: Ann Graham Lotz Fig 1, 94 images / 175M generations, Fig 5 duplication
  histogram (most extracted ≥100 dupes) — `:779`, `:803` — Carlini et al., "Extracting Training
  Data from Diffusion Models", USENIX Security 2023 (arXiv 2301.13188).
- ~1.9% near-duplicate generations — `:815` — Somepalli et al., "Diffusion Art or Digital
  Forgery?", CVPR 2023 (arXiv 2212.03860; paper reports 1.88% at similarity >0.5).
- NYT v. OpenAI — `:847` — S.D.N.Y., filed Dec 2023; motion to dismiss largely denied
  Mar 26, 2025 (opinion Apr 4, 2025).
- Bartz v. Anthropic — `:863` — N.D. Cal. No. 3:24-cv-05417; fair-use order June 23, 2025 (training on lawfully bought books
  fair use; retention of ~7M pirated books not); USD 1.5B settlement, preliminary approval Sept 25, 2025, final approval
  July 20, 2026 (status as of 2026-09; matches `courses/privacy/lectures/03-memorization/` anchor).
- Whole-book extraction — `:1039`, `:1054` — Cooper et al., arXiv 2505.12546 (Llama 3.1 70B / Harry
  Potter); Ahmed, Cooper, Koyejo, and Liang, "Extracting books from production language
  models", arXiv 2601.02671 (2026).
- Capacity ≈3.6 bits/parameter — `:1102` — Morris et al., "How Much Do Language Models
  Memorize?", arXiv 2505.24832 (2025).
- Near-verbatim extraction lower bound (k-CBS; Levenshtein $\varepsilon$-ball probability, deterministic bound at ~20 samples
  vs ~100,000 Monte Carlo) — `:1070` — Cooper, Lemley, De Sa, Duesterwald, Casasola, Hayes, Lee, Ho, and Liang, "Estimating
  near-verbatim extraction risk in language models with decoding-constrained beam search", COLM 2026 (arXiv 2603.24917), Fig. 3.
- Matched non-member controls / conformal thresholds (OLMo 2 32B 7.54% vs 1.82% at 10 tokens, 0.74% vs 0.02% at 50) —
  `:1086` — Cooper, Swanberg, Hayes, Duesterwald, De Sa, Ho, Lemley, and Liang, "Extractable Memorization From First
  Principles", arXiv 2607.12649 (2026), Fig. 3; Cooper, "Playing Whack-a-Mole with misconceptions about memorization,
  extraction, and copyright", arXiv 2609.09320 (2026).
- Unlearning remove-vs-suppress; probabilistic "copies" — `:1154` — Cooper, Lee, Bogen, et al., "Machine Unlearning Doesn't
  Do What You Think", NeurIPS 2025 position (arXiv 2412.06966); Lemley and Cooper, "Probabilistic 'Copies' in Generative AI
  Models", Berkeley Tech. L.J. 2026 (arXiv 2607.14532).

**Real images** (`figs/`, cropped + cited; 27 image slots after the 2026-09-11 Cooper pass — `figs/cooper-discoverable-extraction.png` removed, replaced by the HTML card diagram `:172`):
Feldman SUN long tail `figs/feldman-long-tail.png` (Feldman 2020 Fig 1(a)) `:297`; Secret Sharer NMT
insertions `figs/secret-sharer-fig6-insertions.png` (Fig 6) `:318` and exposure-vs-epoch
`figs/secret-sharer-fig7-epochs.png` (Fig 7) `:365`; GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini 2021 Fig 1) `:437`; zlib-vs-perplexity `figs/carlini-zlib-perplexity.png` (Carlini 2021 Fig 3)
`:492`; 604-example categories `figs/carlini-extraction-categories.png` (Carlini 2021 Table 1) `:509`;
poem-attack screenshot `figs/nasr-poem-chatgpt.png` (Nasr 2023 Fig 5) `:528`; emission-rate bars
`figs/nasr-emission-rate.png` (Nasr Fig 1; shared with `lec02-privacy-dp.html`) `:571`; extrapolation
`figs/nasr-extrapolation.png` (Nasr Fig 9 left) `:584`; Carlini ICLR 2023 Fig 2(a,b)
`figs/carlini-quantifying-fig2ab.png` `:619`, Fig 1(a) `figs/carlini-quantifying-fig1a.png` `:647`,
Fig 1 `figs/carlini-quantifying-fig1.png` `:696`; Kandpal Fig 1 `figs/kandpal-duplicates.png` `:663`
and Fig 3(a) `figs/kandpal-dup-histogram.png` `:684`; Somepalli Fig 1 pairs `figs/somepalli-pairs.png`
`:755` and Fig 5 histograms `figs/somepalli_histograms.png` (shared with lec02) `:819`; Ann Graham Lotz
copy `figs/calrini-ann.png` (Carlini USENIX Sec 2023 Fig 1) `:783`; duplication histogram
`figs/carlini_duplicates.png` (Carlini USENIX Sec 2023 Fig 5; shared with `lec03-mia.html`) `:807`;
NYT complaint p. 30 `figs/nyt-complaint-p30.png` (shared with lec02) `:851`; Lee dedup
`figs/lee-dedup-memorization.png` (Fig 3) `:923` and `figs/lee-dedup-perplexity.png` (Fig 2) `:924`;
VaultGemma `figs/vaultgemma-memorization.png` (Fig 1; shared with lec02) `:998`; Cooper books
`figs/cooper-books-fig3.png` (Fig 3) `:1043`; Ahmed Harry Potter recall `figs/ahmed-harry-potter.png`
(Fig 1) `:1058`; Cooper k-CBS `figs/cooper-kcbs-fig3.png` (COLM 2026 Fig 3) `:1074`; Cooper first-principles `figs/cooper-first-principles-fig3.png` (2026 Fig 3) `:1090`; Morris capacity `figs/morris-capacity.png` (Fig 1) `:1105`.
**SVG / HTML figures:** pattern-vs-copy `:145`, Gatsby prefix→model→suffix cards (HTML) `:172`, $k$-extractable test `:227`, loss bars `:274`, canary-leak
pipeline `:341`, pattern-vs-record `:388`, canary-vs-wild `:415`, extraction pipeline `:461`, poem
loop-break `:544`, log-linear schematic `:706`, diffusion noise→image strip `:766` (diagram-flow),
near-duplicate dedup `:944`, n-gram output filter `:967`, privacy/accuracy trade-off `:1013`, PII
pipeline `:1128`. Citations use `.cite-left` with figure numbers. Page number: bold `.slide-num` only.

**2026-09-14 case-brief + core-path pass (62→65, PR #31):** slides-review brief. Deck: "Where This Lecture Sits" lifecycle slide
(Evidence stage); "Degrees of Copying" taxonomy SVG replaces "Three Flavors" (verbatim → near-verbatim → specific fact → style,
technical ≠ legal band); Working Definition allows small edits and says "behavior, not yet legal"; Extractable vs Discoverable
reworded as two games with no containment (deck, note, tech slide 5 all aligned); `.facts` callouts (What happened / How it was
verified / Why it matters) on GPT-2, Repeat Forever, Stable Diffusion; evidence-status callouts on NYT (What the exhibits show /
What the court found / Status as of 2026-09) and Copy or Transform (Bartz: fair-use ruling / piracy finding / settlement approval,
kept separate); Ahmed slide callouts (What happened / What the evidence showed / Limits: near-verbatim, one run, no control,
membership inferred); new "The Same Output, Different Questions" stakeholder slide; Key Takeaways dedup line softened; Practice:
Boardroom Questions (3+3). 90-min core path: 7 optional slides (Turning Leakage into a Number, Try It Yourself, The Long
Tail, Reading the Curves, A Quick Picture, The Privacy Tax, How Much Fits?), listed in the note's Contents entry only (Contents-slide line and per-slide badges removed from the main deck 2026-09-14, Albert's request). Note: 65
articles; h3 scheme Case background / Technical depth — optional / References; uniform paper briefs (attacker access / target /
member definition & duplicate control / metric / result / limitation / figure / follow-up) for Secret Sharer, GPT-2, Nasr,
Carlini ICLR 2023, Kandpal, Lee, Carlini diffusion, Somepalli, Feldman, VaultGemma (ref added, arXiv 2510.15001), Cooper books +
Hayes, Ahmed, Cooper near-verbatim, Cooper first principles, Morris; NYT and Bartz as complaint allegation / judicial finding /
settlement / status; five-distinctions list under Degrees of Copying; Boardroom model answers. Tech: slide 5 two-games wording;
"Intuition:" lines on slides 3, 11, 12, 13. Lint ok (1 pre-existing dash warning); 65/15 pages rendered, edited slides checked at 60 dpi.

**2026-09-14 Albert page comments (PR #31, post-approval):** slide 6 "A Working Definition" — bottom `.muted` line overlapped the `.cite-left` footnote; fixed by layout only (prefix/suffix cards 0.9fr/1.1fr so the suffix quote wraps to four lines, card padding 14px, grid gap 10px, muted line margin 10px) plus a shorter closing sentence ("Model behavior, not yet a legal claim."). 65 slides unchanged; page 6 re-rendered at 60 dpi.

**2026-09-11 Cooper frontier + page-comment pass (60→62, PR #30):** per Albert's Slack comments — "A Working Definition"
image (Cooper Fig 1, unreadable at slide scale) redrawn as three HTML cards (Gatsby prefix → Llama 1 30B → true suffix);
"From Canary to the Wild" SVG redrawn at 960 wide with 21–27 px type; Carlini Fig 2(a,b) re-cropped at 250 dpi (panels a,b only);
"A Predictable Curve" explains why prompt length is context; "Reading the Curves" now stacks bullets over a full-width SVG with
21 px type. Checked A. Feder Cooper's page (afedercooper.info; now Yale CS / GenLaw) and added two frontier slides after
"Chatbots Recite Books Too": "Near-Verbatim Counts Too" (k-CBS, COLM 2026) and "Extraction Needs a Control Group" (First
Principles 2026 + the Whack-a-Mole essay); "Open Problems" gained the unlearning remove-vs-suppress question with the
NeurIPS 2025 position paper and Lemley & Cooper BTLJ 2026 cites. Related Cooper work landed in lec03 ("Does LiRA Work on
LLMs?", Hayes … Cooper NeurIPS 2025). Note file: two new articles (k-CBS bound + $\varepsilon$-ball definition; matched
comparison + conformal threshold + overstatement/dismissal failure modes), context paragraph in "A Predictable Curve",
unlearning/legal paragraph + links in "Open Problems"; 62 entries, order matches. Render = 62 pages; 8 edited/new slides
checked at 60 dpi.

**2026-09-12 tech supplement update (`lec04tech.html` 9→15, PR #30):** formal backing for the Cooper 2026 frontier slides.
New: "Discoverable vs Extractable" (Nasr et al. 2023 Defs. 1–2 as two def-cards; neither set contains the other), "Why Context
Helps" (greedy decoding reproduces $s$ iff the true token is the argmax at every step; $H(S\mid P_{1:k+1})\le H(S\mid P_{1:k})$
explains the $c\log k$ term), "Near-Verbatim Extraction" ($B_\varepsilon(s)$ Levenshtein ball, $p_\varepsilon(s\mid p)$ as the ball's
probability mass, Monte Carlo cost $\sim10^5$ samples), "$k$-CBS: A Deterministic Lower Bound" (4-step `.ta-algo`; ~20 decodes;
OLMo 2 32B 1.4%→2.6% at ε=5), "The Non-Member Baseline" ($R(D)$, excess $=R(D_{\text{train}})-R(D_{\text{ctrl}})$, conformal
threshold) and "How Large Is the Floor?" (train/control/excess table: 10-token 7.54% / 1.82% / 5.72%, 50-token 0.74% / 0.02% /
0.72%; split off after the table overflowed the footer at 60 dpi). `.ta-algo` CSS added to the head. Note file unchanged
(already in sync). Lint ok; 15 pages rendered, new slides checked at 60 dpi.

**2026-09 figure pass (58→60, PR #24):** every content slide now carries a cited real figure or an
SVG. Added slides: Reading the Curves (§03, holds the GPT-J ≥1% bullets that A Predictable Curve
gave up for Carlini Fig 1) and Frontier: Chatbots Recite Books Too (§06; Ahmed 2026 split out of
Whole Books Come Back, stating only figure-visible values: 95.8/76.8/70.3/4.0 nv-recall, N = 258/0/0/5,179).
Three SVGs replaced by the real figures they sketched (size curve → Carlini Fig 1(a); duplication bars →
Kandpal Fig 1; NYT side-by-side → complaint p. 30). Note file: one "Slide figure" sentence per figure
(32 articles) + the two new articles; 60 entries, order matches.

**2026-08 content revision (59→58):** every citation/number fetched and verified. Added:
Extractable vs Discoverable (§01), Some Memorization Is Necessary (Feldman, §01),
Frontier: How Much Fits? (Morris, §06); Whole Books Come Back replaced the generic
production-extraction frontier slide. Compressed §05 from 6 slides to 2 (fair-use detail
migrated to the note file; backup copyright deck owns the full treatment). Fixed: third
scaling driver "training length"→context length (TOC, divider, drivers card — and in
`lec04tech.html`, $c\log t$/epochs → $c\log k$/context tokens, fix-errors-only pass);
Three Flavors retaxonomized (eidetic/extractable cite misattribution removed); poem-attack
prompt restored to the paper's exact wording; Somepalli cite removed from the Carlini Fig 5
histogram slide; concrete verified numbers added (604/1,800; 10,000+/$200/150×; ~1000×;
GPT-J ≥1%; 94/175M; ~1.9%; $1.5B). Note file synced (58 entries, order matches).

**2026-08 note enrichment:** `lec04-memorization-note.html` upgraded from speaker script
(365 lines) to Script &amp; Companion Notes (741 lines; 58 entries unchanged): per-entry
`.detail` blocks with rigorous definitions (NLL objective, $k$-extractable, Nasr
extractable/discoverable Defs 1–2, canary $s[r]$ + rank + exposure, counterfactual
memorization, $k$-eidetic, Λ-style calibrated-perplexity metrics, Mem$(f)$ + scaling law,
DDPM recap, $(\ell,\delta)$/$(k,\ell,\delta)$-diffusion extraction, SSCD, §107 four factors,
$(\varepsilon,\delta)$-DP, DP-SGD, $(n,q)$-probabilistic extraction, Morris compression
memorization, NIST PII), proofs (Feldman Thm 2.3 statement + verified sketch, exposure
null-tail bound, DP ⇒ bounded counterfactual memorization), and case backgrounds with
29 verified links (NYT v. OpenAI complaint + Apr 2025 MTD opinion; Bartz v. Anthropic
fair-use order + settlement) — all consistent with `courses/privacy/lectures/03-memorization/`.

---

## lec05-unlearning.html

**Topic:** Machine unlearning (~97 min full deck; 90-minute core path via five optional slides listed in the note only — no badges on the main deck since 2026-09-14). Why deletion is demanded (GDPR/CCPA privacy,
copyright, safety); retraining as the gold standard; exact vs approximate; the
$(\varepsilon,\delta)$ yardstick at intuition level; SISA as a picture; influence
functions and the Hessian wall; gradient ascent, its failure modes, and NPO;
LLM unlearning (Harry Potter, TOFU, WMDP/RMU, MUSE); verification (MIA audit, IDI,
relearning, quantization recovery); the position-paper debate and the 2025–26
frontier. Intuition pass — the rigorous treatment lives in
`courses/privacy/lectures/05-unlearning/` (authoritative for shared facts); the
position-paper debate expands in `talks/icml2026/`.

### Sections (68 slides, ~97 min — content-revised 2026-08 from 58, figure pass 2026-09-05 added RMU, Measured; case-brief + core-path pass 2026-09-14 added Where This Lecture Sits, Four Things "Unlearning" Can Mean, Practice: Boardroom Questions)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents / Where This Lecture Sits | 1–3 | `:51`, `:63`, `:95` | Contents is a plain 6-item TOC (core-path list lives in the note only, 2026-09-14) · lifecycle strip with Remediation highlighted `:95` |
| **01 — Why Delete?** | 4–12 | `:138` | user changes mind (SVG) `:146` · **GDPR Art. 17 / CCPA §1798.105 — what the text says / does not say / why it matters (reworked 2026-09-14; three evidence levels: legal right · formal goal · benchmark result)** `:180` · **Delete for Three Reasons (privacy / copyright / safety; added 2026-08)** `:194` · **data lives in the weights (SVG)** `:207` · why not ignore (SVG) `:233` · retraining expensive (SVG) `:264` · enter machine unlearning (Cao & Yang) `:297` · a decade of work (+Cooper arXiv-count chart) `:312` |
| **02 — What Unlearning Means** | 13–21 | `:332` | **Four Things "Unlearning" Can Mean (data removal · knowledge suppression · output filtering · access revocation; added 2026-09-14; every method slide carries a `.cat-badge`)** `:340` · gold standard = retrain, scoped to data removal (`Data removal` badge, 2026-09-14) `:354` · **two-models diagram (SVG; `Data removal` badge)** `:381` · exact (SVG) `:408` · approximate (SVG) `:435` · **DP yardstick (Guo/Sekhari cite fixed 2026-08; SVG)** `:467` · forget/retain split (SVG strip) `:497` · two things to get right `:522` |
| **03 — How to Unlearn** | 22–35 | `:556` | retraining baseline `:564` · train in pieces (SISA shard SVG) `:577` · **SISA (real Bourtoule Fig 2)** `:618` · deleting in SISA (SVG) `:638` · slices (SVG) `:686` · tradeoff (+Bourtoule Fig 6) `:721` · edit the weights `:738` · influence functions (+Koh & Liang Fig 2) `:751` · Hessian catch (SVG) `:769` · gradient ascent (SVG) `:796` · ascent wrecks (+Kurmanji Fig 6) `:830` · **A Gentler Push: NPO (real fig; added 2026-08)** `:847` · method landscape `:860` |
| **04 — Unlearning in LLMs** | 36–48 | `:873` | what do we forget `:881` · no single row (SVG) `:894` · Harry Potter (+1 GPU hour; Eldan Fig 3) `:931` · the result (Eldan Fig 1 table) `:953` · **TOFU (200×20=4,000; +Fig 6)** `:966` · **TOFU in One Picture (real fig; added 2026-08)** `:983` · why fictitious (SVG) `:994` · **WMDP (real fig + 3,668 MCQs; reworked 2026-08)** `:1027` · RMU (+loss Fig 7) `:1048` · **RMU, Measured (Fig 8, Zephyr-7B; added 2026-09)** `:1065` · **MUSE: Six Boxes to Tick (real fig; added 2026-08)** `:1085` · unlearning vs filtering (+Cooper back-end/front-end) `:1098` |
| **05 — Did It Really Forget?** | 49–57 | `:1118` | verification is hard (SVG) `:1126` · MIA audit (+MUSE Fig 2) `:1159` · **the tell persists (SVG)** `:1177` · **Look Inside: IDI (real fig, Yonsei; added 2026-08)** `:1197` · **Relearning, Measured (real fig; added 2026-08; moved before relearning attacks 2026-09-30)** `:1210` · relearning attacks (+Yoon syntax Fig 5, Yonsei; "The general test") `:1223` · **Quantize, and It Comes Back (21%→83%; +Zhang Fig 1)** `:1241` · dormant, not deleted (+Łucki Fig 1) `:1258` |
| **06 — Frontier 2025–26** | 58–65 | `:1272` | **"overused" critique (+Yoon/Jun/No cite; taxonomy SVG)** `:1280` · **Does It Do What You Think? (position papers; added 2026-08)** `:1313` · what guarantee holds `:1326` · **robust unlearning (+Łucki Fig 2)** `:1339` · evaluation standards (+MUSE Fig 5) `:1357` · unlearning meets privacy (+onion-effect ROC) `:1376` · open problems `:1394` |
| Boardroom / Takeaways / Closer | 66–68 | — | **Practice: Boardroom Questions (five questions, 2-min; added 2026-09-14)** `:1408` · takeaways `:1449` · closer `:1462` |

**Key definitions / citations (all source-verified 2026-08):**
- First "machine unlearning" — `:297` — Cao and Yang, IEEE S&P 2015.
- Exact deletion definition — `:312` — Ginart, Guan, Valiant, and Zou, NeurIPS 2019
  (arXiv 1907.05012). **No longer cited for the $(\varepsilon,\delta)$ definition** —
  that was a misattribution, fixed 2026-08 on `:467` and in `lec05tech.html`.
- $(\varepsilon,\delta)$-unlearning — `:467` — Guo, Goldstein, Hannun, and van der Maaten,
  "Certified Data Removal from Machine Learning Models", ICML 2020 (arXiv 1911.03030);
  Sekhari et al., NeurIPS 2021. Matches privacy deck Def 3.
- SISA — `:618` — Bourtoule et al., "Machine Unlearning", IEEE S&P 2021. Speedup:
  sharding cuts expected cost by the shard count; slicing saves at most another 3/2
  (matches privacy deck Prop 3; tech deck's "R·L" claim fixed 2026-08).
- Influence functions — `:751` — Koh and Liang, ICML 2017.
- Gradient ascent / unrolling — `:796` — Thudi et al., "Unrolling SGD", IEEE EuroS&P 2022.
- Ascent wrecks / retain anchor — `:830` — Kurmanji, Triantafillou, Hayes, and
  Triantafillou, "Towards Unbounded Machine Unlearning" (SCRUB), NeurIPS 2023.
- NPO — `:847` — Zhang, Lin, Bai, and Mei, "Negative Preference Optimization", COLM 2024.
- Who's Harry Potter (~1 GPU hour, Llama-2-7b) — `:931` — Eldan and Russinovich, 2023
  (arXiv 2310.02238).
- TOFU (200 authors × 20 QA = 4,000) — `:966` — Maini, Feng, Schwarzschild, Lipton,
  and Kolter, COLM 2024 (arXiv 2401.06121).
- WMDP (3,668 MCQs) + RMU — `:1027`, `:1048`, `:1065` — Li et al., ICML 2024 (arXiv 2403.03218).
- MUSE (six criteria) — `:1085` — Shi, Lee, Huang, Malladi, Zhao, Holtzman, Liu, Zettlemoyer, Smith, and Zhang, ICLR 2025 (arXiv 2407.06460; author list corrected 2026-09-14 against arXiv; News f₀ = LLaMA-2 7B, Books f₀ = ICLM-7B).
- IDI (instructor co-author) — `:1197` — Jeon, Jeung, Kim, No, and Choi (Yonsei),
  "An Information Theoretic Evaluation Metric For Strong Unlearning", AAAI 2026
  (arXiv 2405.17878).
- Syntax drives relearning (instructor co-author) — `:1223` — Yoon, Hong, Jeung, and No
  (Yonsei), "Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning
  Failures", ICLR 2026 (arXiv 2602.03379; TOFU on Llama-2-7b-chat, GA/NPO/SCRUB).
- Benign relearning — `:1210` — Hu, Fu, Wu, and Smith, "Unlearning or Obfuscating?",
  ICLR 2025 (arXiv 2406.13356).
- Quantization recovery (21%→83% after 4-bit) — `:1241` — Zhang et al., "Catastrophic
  Failure of LLM Unlearning via Quantization", ICLR 2025 (arXiv 2410.16454).
- Adversarial perspective (10 unrelated examples undo RMU) — `:1258`, `:1339` — Łucki et al.,
  TMLR 2025 (arXiv 2409.18025).
- 184K GPU-hours (Llama-2-7b pretraining, reported) — `:264`, `:931` — Eldan and Russinovich citing
  Touvron et al., "Llama 2", 2023 (arXiv 2307.09288).
- Erasure right vs model weights (note only) — EDPB Opinion 28/2024, adopted 17 Dec 2024 (paras. 107(b),
  114–115): unlearning listed as a mitigation "attempting to remove or suppress" personal data; model
  erasure as a corrective measure for unlawful processing. No judicial decision holding Art. 17 requires
  weight modification is cited; statute texts (Art. 17, Civ. Code §1798.105) do not mention models.
- Privacy onion effect — `:1376` — Carlini et al., "The Privacy Onion Effect: Memorization
  is Relative", NeurIPS 2022.
- Position papers — `:312`, `:1098`, `:1280`, `:1313` — Cooper et al., "Machine Unlearning Doesn't Do What
  You Think", NeurIPS 2025; Yoon, Jun, and No (Yonsei), "Position: 'Machine Unlearning'
  Is Overused in LLMs", ICML 2026 (matches `courses/privacy/lectures/05-unlearning/`
  and `talks/icml2026/`).

**Real images** (`figs/`, cropped + cited). From the 2026-08 pass (copied from
`courses/privacy/lectures/05-unlearning/figs/`): NPO vs GA collapse curves
`figs/npo-ga-collapse.png` (Zhang COLM 2024 Fig 2) `:853`; TOFU pipeline
`figs/tofu.png` (Maini COLM 2024 Fig 1) `:987`; WMDP overview `figs/WMDP.png`
(Li ICML 2024 Fig 1) `:1034`; MUSE six-way evaluation `figs/MUSE.png` (Shi ICLR 2025
Fig 1) `:1091`; IDI conceptual layer plot `figs/idi-conceptual.png` (Jeon AAAI 2026
Fig 4(a)) `:1203`; benign-relearning pipeline `figs/benign-relearn-pipeline.png`
(Hu ICLR 2025 Fig 2 left) `:1216`. **Added 2026-09-05 figure pass:** arXiv unlearning
counts `figs/unlearning-arxiv-counts.png` (Cooper 2024 Fig 2) `:323`; SISA training
`figs/sisa-training.png` (Bourtoule S&P 2021 Fig 2) `:625`; accuracy vs shards
`figs/sisa-accuracy-shards.png` (Bourtoule Fig 6) `:733`; influence vs leave-one-out
`figs/influence-vs-loo.png` (Koh & Liang ICML 2017 Fig 2) `:762`; ascent-only and
alternating error curves `figs/scrub-maxsteps-only.png` + `figs/scrub-alternating.png`
(Kurmanji NeurIPS 2023 Fig 6(a)/(d)) `:841`–`:842`; HP next-token table
`figs/hp-nexttoken.png` (Eldan 2023 Fig 3) `:939`; HP completions
`figs/hp-completions.png` (Eldan Fig 1) `:959`; forget quality vs utility
`figs/tofu-fq-vs-utility.png` (Maini COLM 2024 Fig 6) `:977`; RMU loss
`figs/rmu-loss.png` (Li ICML 2024 Fig 7) `:1059`; RMU results
`figs/rmu-results.png` (Li Fig 8) `:1072`; back-end/front-end
`figs/backend-frontend.png` (Cooper Fig 3) `:1104`; MIA distributions
`figs/muse-mia-dist.png` (Shi ICLR 2025 Fig 2) `:1170`; syntax similarity
`figs/syntax-similarity.png` (Yoon ICLR 2026 Fig 5, Yonsei) `:1234`; quantization
recovery `figs/quant-recovery.png` (Zhang ICLR 2025 Fig 1) `:1252`; adversarial
overview `figs/lucki-overview.png` (Łucki TMLR 2025 Fig 1) `:1264`; fine-tune recovery
`figs/lucki-finetune.png` (Łucki Fig 2) `:1350`; utility vs memorization
`figs/muse-utility-vs-mem.png` (Shi Fig 5) `:1369`; onion ROC `figs/onion-roc.png`
(Carlini NeurIPS 2022 Fig 1) `:1388`. **SVG figures:** database row vs weights `:158`,
data-in-weights `:213`, MIA/extraction probes `:245`, daily-retrain timeline `:276`,
two-models-compared `:388`, identical distributions `:420`, weight-space nudge `:447`,
bounded-gap distributions `:479`, forget/retain strip `:503`, SISA shard diagram (moved
from the SISA slide) `:589`, one-shard retrain `:650`, slices + checkpoints `:696`,
Hessian grid `:783`, descent vs ascent loss curve `:808`, paraphrase entanglement
`:906`, web vs fine-tune source `:1005`, three-probe verification `:1138`,
member/non-member bells `:1183`, data-level vs output-level taxonomy `:1292`.
Citations use `.cite-left`. Page number: bold `.slide-num` only.

**2026-09-14 reviewer #48 follow-up (same day, after dc560c8):** taxonomy conflicts removed.
"The Law Says Delete" third callout now says stakeholders may all request "removal" but can
mean different targets (data influence, protected outputs, hazardous capability, access), and
carries a visible `.cite` line (Regulation (EU) 2016/679 Art. 17 · Cal. Civ. Code §1798.105 ·
status/interpretation as of 2026-09). "Delete for Three Reasons" footer: similar language,
different goals and evidence. "The Gold Standard" / "Two Models, Compared" carry a
`Data removal` badge and scope the retrained reference to data-removal claims only ("other
goals need other baselines"). Taxonomy cards: output filtering "can block observed outputs,
but does not establish that underlying knowledge was removed; test for bypasses"; access
revocation "changes access, not whatever may already be in the weights"; footer: a filtering
claim needs bypass and coverage tests, not a retraining comparison, and must not be presented
as removal. Note scripts/KTs and `lec05tech.html` slide 3 cards updated to the same wording.

**2026-09-14 case-brief + core-path pass (67→70):** three slides added — Where This Lecture Sits
(lifecycle strip, Remediation), Four Things "Unlearning" Can Mean (2×2 taxonomy), Practice: Boardroom
Questions (five questions). Every method/benchmark/verification slide carries a `.cat-badge`
(Data removal · exact/certified/approximate · Knowledge suppression · Benchmark vs retraining /
concept · Verification audit/attack). Evidence-status wording: "The Law Says Delete" split into
what the text says / does not say / why it matters (no claim that Art. 17 reaches weights; three
evidence levels — legal right, paper's formal goal, benchmark result — kept in separate sentences
across deck, note, tech); Harry Potter and RMU results labelled "reported"; central sentence "Not
answering is observable. Not knowing is a much stronger claim." on Enter/Verification/Takeaways.
Seven optional slides (A Decade of Work, Slices, Curvature, Try It Yourself, TOFU in One
Picture, Why Fictitious, Where to Go Deeper) define the 90-min core path listed in the note's
Contents entry only (Contents-slide line and per-slide badges removed from the main deck 2026-09-14, Albert's request). Note synced to 70 entries with uniform case briefs (deletion target / model·data /
evaluation benchmark / reported success / verification attack / what can and cannot be claimed /
follow-up status as of 2026-09) for Eldan, TOFU, WMDP, RMU, MUSE, IDI, Yoon syntax, Hu, Zhang,
Łucki, Cooper, Yoon/Jun/No; legal brief with statute text + EDPB Opinion 28/2024; MUSE author list
fixed. `lec05tech.html` 11→12 sl: Formal Goals, Separated (slide 3) + category badges + SISA
variables aligned to note (S shards, R slices) + cost formula.

**2026-09-30 Albert page comments (70→68):** p6 legal slide cut to two-line cards ("erasure on request", "Legal right: established. / Weight-level duty: not."); p8, p9, p11, p35, p40 line breaks (one claim per line; p35 Approximate card now "No certificate, except for simple models"); p14 taxonomy cards cut to one target line + one evidence line; p15 gains a data→retrain→reference flow SVG; p18/p19/p24 diagrams enlarged (wider column, 18–21-unit type); p21 gains a utility-vs-forgetting tradeoff SVG; p31 Hessian slide rebuilt with KaTeX ($H \in \mathbb{R}^{d\times d}$, $d \gtrsim 10^9$, $d^2 \gtrsim 10^{18}$) and a larger grid; "Try It Yourself" (Colab) and "Where to Go Deeper" removed; "Relearning, Measured" now precedes "Relearning Attacks". Note synced: articles removed, the reading list moved into Key Takeaways' detail block, the two relearning entries swapped with their cross-references, core-path list now five optional slides. `lec05tech.html` unchanged (its Hessian slide already matches). Slide numbers in the older entries below are pre-2026-09-30.

**2026-09-14 Albert page comments (PR #31, post-approval):** slide 51 "Verification Is Hard" — probe diagram enlarged (grid 0.7fr/1.3fr, SVG viewBox 600×250 at up to 760 px wide, label type 22/19 units ≈ 26/23 px rendered, "?" 56, box 160×150); bullets and highlight unchanged. 70 slides unchanged; page 51 re-rendered at 60 dpi.

**2026-09-05 figure pass (66→67):** every bullet-only content slide now carries a cited
real figure or an inline SVG (18 new crops, 15 new SVGs; grid-3 card slides and the
position-paper slide left as is). One slide added: RMU, Measured (Li Fig 8). SISA slide
swapped its SVG for Bourtoule Fig 2; the SVG moved to Train in Pieces. Filter-vs-
unlearning columns reordered to match Cooper's (a) back-end / (b) front-end. Note file
synced: 67 entries, `Slide figure:` line on every real-figure slide.

**2026-08 content revision (58→66):** every citation/number fetched and verified.
Added 8 slides: Delete for Three Reasons (§01), A Gentler Push: NPO (§03), TOFU in
One Picture + MUSE: Six Boxes to Tick (§04), Look Inside: IDI + Relearning, Measured +
Quantize, and It Comes Back (§05), Does It Do What You Think? (§06). Fixed:
$(\varepsilon,\delta)$-unlearning misattributed to Ginart 2019 → Guo ICML 2020 +
Sekhari 2021 (main `:467` and `lec05tech.html` slide 4, which also gained the
two-sided-bound clause); `lec05tech.html` SISA speedup "R·L" → shard-count + 3/2
(fix-errors-only pass, deck stays 11 sl). WMDP slide reworked around the real figure;
concrete verified numbers added (4,000 QA; 3,668 MCQs; 21%→83%; 10 examples;
~1 GPU hour). Note file synced (66 entries, order matches; 67 after the 2026-09 figure pass).

**2026-08 note enrichment:** `lec05-unlearning-note.html` upgraded from speaker script
(413 lines) to Script &amp; Companion Notes (829 lines; 66 entries unchanged): per-entry
`.detail` blocks with rigorous definitions (Ginart deletion, exact and
$(\varepsilon,\delta)$-certified unlearning with quantifiers, SISA formalized, A1–A3
convex setting, GA/NPO/RMU losses, TOFU truth-ratio KS metric, IDI, suppression vs
deletion / adaptation class), full proofs (exact⟹certified, retraining exact,
SISA shard + slicing cost with the $3R/(2R+1)\to3/2$ limit, IFT influence derivation +
Newton-step $MG^2/(2\lambda^3n^2)$ bound via two lemmas, GA-has-no-optimum, GA-vs-NPO
toy divergence rates, NPO self-limiting theorem + $\beta\to0$ GA limit, one-family
gradient-weight proposition, exact-deletion-misses-the-concept, $p$-value uniformity +
best-of-$k$, prompt-relativity, output-metrics blindness, TV audit cap, attacks
one-sided, gate construction, DP⟹certified + $1/n$ vs $1/n^2$ noise calculus, Sekhari
deletion-capacity statement), and Background blocks (GDPR Art. 17 / CCPA / Google Spain
C-131/12; 24 verified links) — all consistent with
`courses/privacy/lectures/05-unlearning/`.

## lec06-hallucination.html

**Topic:** Hallucination, calibration & reliability (~90 min). What hallucination is
(and is not); why next-token training produces confident falsehoods (Kalai binary-grading
argument at intuition level); real harms (Lacey v. State Farm as anchor case, preceded by a
self-contained Mata v. Avianca context slide since round 4); calibration with the reliability-diagram
picture and a glanceable ECE; conformal prediction as "sets with a coverage promise";
semantic entropy at intuition level; RAG grounding; benchmarks (TruthfulQA, Vectara HHEM);
reasoning-model hallucination; sycophancy one-slide touchpoint (full treatment in
`backup-sycophancy.html`). Math lives in `lec06tech.html` (formal Kalai bound and coverage proof moved there in round 4).

### Sections (75 slides, ~95 min — Albert's revision 2026-10 from 61, four review rounds; content-revised 2026-08 from 58; figure pass 2026-09)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:26`, `:38` | |
| **01 — What Hallucination Is** | 3–11 | `:71` | definition (Ji survey) `:79` · **fluency fools us (real vs invented citation test; 2026-10)** `:94` · **Context: Mata v. Avianca (2023) (comparison with Lacey; round 4)** `:103` · Fake Citations, Again (Lacey v. State Farm) `:114` · **Invented Medical Facts (infarct defined; 2026-10)** `:132` · two flavors of wrong `:150` · not the same as a bug `:164` · why this matters `:179` |
| **02 — Why Models Hallucinate** | 12–22 | `:192` | training objective `:200` · no truth grounding (Kalai Fig 1) `:212` · **Counting With a Poor Model (V3 chat vs R1 reasoning, siblings on one base; round 4)** `:225` · **Weak Model Family ⇒ Forced Errors (trigram picture, plain-language Cor 2; formal bound in lec06tech; round 4)** `:241` · plausible beats true `:254` · pressure to always answer `:276` · exam-taking analogy `:293` · Guessing, Measured `:310` · where errors concentrate (FActScore Fig 2 + plot description) `:338` · knowledge cutoff `:355` |
| **03 — Calibration** | 23–36 | `:371` | confidence as a number `:379` · calibration promise (100-dot grid) `:391` · reliability diagram `:406` · over- vs under-confident `:428` · **measuring the gap (gap = \|conf − acc\|; 2026-10)** `:442` · **reading ECE (area picture, 0.1705; 2026-10)** `:459` · bigger is not better `:476` · temperature `:485` · **What P(True) Measures (3-step prompt; round 4)** `:499` · **Kadavath P(True) histogram (overlap = imperfect discrimination; round 4)** `:513` · **Filtering by P(True) Mostly Raises Accuracy (unmodified plot + enlarged key)** `:529` · **verbalized confidence GPT-3/3.5** `:543` · **GPT-4/Vicuna** `:558` |
| **04 — Conformal Prediction** | 37–52 | `:575` | one answer to a set (three photos, typeset sets) `:583` · **Candidates, Native Output, Conformal Set** `:595` · coverage guarantee `:609` · **Two Assumptions (A1 exchangeable, A2 fixed score)** `:625` · how it works (k, q̂ = ∞) `:638` · recipe figure `:652` · **Two Kinds of Calibration (temperature vs threshold; round 4)** `:660` · **Coverage Theorem (upper bound only without ties)** `:673` · **Why It Works: A Fair Rank (n = 9, α = 0.2 rank picture; replaces 3 proof slides; round 4)** `:690` · prediction-set picture `:706` · **What the Guarantee Covers** `:714` · **Marginal ≠ Conditional** `:734` · abstention (singleton ≠ certified) `:749` · medical triage (clinician review) `:765` · trade-off `:781` |
| **05 — Detection & Grounding** | 53–62 | `:791` | two strategies (Ground first, then Detect; round 4) `:799` · self-consistency `:813` · semantic entropy `:822` · entropy picture `:836` · RAG `:861` · why RAG helps `:875` · RAG is not a cure `:891` · teaching "I don't know" `:907` · scoring rule `:923` |
| **06 — Frontier 2025–26** | 63–73 | `:936` | **Misconceptions (TruthfulQA examples; 2026-10)** `:943` · **In the Wild: Search Answers, 2024 (rocks / glue)** `:957` · **Should a Truthful Model Share Our Errors?** `:969` · TruthfulQA `:986` · **Benchmarks table (4 benchmarks)** `:1001` · **Measuring Faithfulness: Vectara HHEM (Sep 22, 2026 data)** `:1016` · reasoning models `:1054` · sycophancy `:1071` · factuality evaluations `:1083` · open problems `:1092` |
| Takeaways / Closer | 74–75 | — | `:1107`, `:1121` |

**Key definitions / citations (source-verified; 2026-10 additions checked against the saved PDFs):**
- Hallucination survey — `:79` — Ji et al., ACM Computing Surveys 2023.
- Anchor case — `:114` — Lacey v. State Farm, C.D. Cal., May 2025. Context — `:103` — Mata v. Avianca, No. 22-cv-1461 (PKC), S.D.N.Y., Opinion and Order on Sanctions, 22 June 2023 (six fabricated decisions, USD 5,000).
- Med-Gemini "basilar ganglia" — `:132` — Google Med-Gemini paper 2024; The Verge, 2025.
- Kalai, Nachum, Vempala, and Zhang, 2025 (arXiv 2509.04664) — IIV reduction Fig 1 `:212`;
  DEEPSEEK letter count (§1: V3 "2" or "3" in ten trials, app, 11 May 2025; §3.3.2: R1 spells it out, tokens D/EEP/SEE/K) `:225`;
  trigram limitation in plain language (Theorem 3, Corollary 2) `:241`; the formal bound
  err ≥ 2·opt(G) − max|V_c|/min|E_c| − δ now only in the note and `lec06tech.html`; binary grading `:276`, `:293`, `:923`.
- DeepSeek chronology — `:225` — V3 released 26 Dec 2024 (arXiv 2412.19437), V3-0324 25 Mar 2025, R1 20 Jan 2025
  (arXiv 2501.12948; RL from DeepSeek-V3-Base); api-docs.deepseek.com/news. Siblings, not successor.
- FActScore — `:338`, `:1001`, `:1083` — Min et al., EMNLP 2023.
- Calibration / ECE / temperature — `:391`–`:485`, `:660` — Guo, Pleiss, Sun, and Weinberger, ICML 2017 (ECE Eq. 3).
  ECE example (shares .10/.10/.15/.25/.40, gaps .03/.07/.15/.20/.22 → 0.1705) is a course illustration.
- Self-knowledge P(True) — `:499`, `:513`, `:529` — Kadavath et al., 2022, §3.2 / §4.1–4.2 (prompt format, P of "(A)"), Fig 1 (left / right; right panel unmodified, enlarged key beside it).
- Verbalized confidence — `:543`, `:558` — Xiong et al., ICLR 2024, Fig 2 (GSM8K).
- Conformal — `:583`–`:734` — Angelopoulos and Bates, 2021 (Theorem 1, Appendix D, Theorem D.2);
  Vovk, Gammerman, and Saunders, ICML 1999. k = ⌈(n+1)(1−α)⌉, q̂ = ∞ when k = n+1; ties keep the lower bound.
- Conditional coverage limits — `:734` — Vovk, ACML 2012; Lei and Wasserman, JRSS-B 2014 (Lemma 1);
  Foygel Barber, Candès, Ramdas, and Tibshirani, Information and Inference 2021.
- TruthfulQA — `:943`, `:969`, `:986`, `:1001` — Lin, Hilton, and Evans, ACL 2022 (Fig 1, Fig 2, Table 6, §2.1).
- AI Overviews rocks / glue — `:957` — Reid (Google), "AI Overviews: About last week", Google blog, May 30, 2024.
- SimpleQA — `:310`, `:1001` — Wei et al., 2024 (grades: correct / incorrect / not attempted).
- Vectara HHEM-2.3 — `:1016` — leaderboard README, updated Sep. 22, 2026 (top six rows; 7,700+ articles; temperature 0).
- Self-consistency `:813` — Manakul et al., EMNLP 2023. Semantic entropy `:822` — Farquhar et al., Nature 2024.
  RAG `:861` — Lewis et al., NeurIPS 2020. Sycophancy `:1071` — Sharma et al., ICLR 2024.

**Real images** (`figs/`, cited; 21 files on 17 slides): kalai-iiv `:212` · kalai-gpt4-calibration `:276` ·
factscore-frequency `:338` · guo-reliability-titles + guo-reliability `:476` · guo-temp-scaling `:485` · kadavath-ptrue-hist `:513` ·
kadavath-ptrue-scaling `:529` · xiong-verbalized-a `:543` · xiong-verbalized-b `:558` · conformal-squirrel-1/2/3
`:583` · conformal-recipe `:652` · selfcheckgpt `:813` · semantic-entropy-table `:822` · rag-overview `:861` ·
truthfulqa-size `:986` · sharma-sycophancy `:1071` · factscore-chatgpt `:1083`. Crops re-captured at higher
resolution in 2026-10; kadavath-ptrue-scaling is an unmodified crop (embedded legend
kept) with an enlarged SVG key beside it. Citations use `.cite-left`.

**2026-10 Albert revision (61→73; PR on branch `trustworthy-ai-lec06-albert-revision`;
log `log/2026-10-06-trustworthy-ai-lec06-albert-revision.md`):** enlarged diagrams and fonts on orig
P4, 5, 8, 9, 12, 16, 19, 21, 22, 35, 47, 48, 49 (all redrawn SVGs at 16–20px type). P5 recast as a
real-vs-invented citation test; P7 defines infarct; P13 split into figure + DEEPSEEK example + precise
theorem; P18 plot description; P25/26 gap = \|conf − acc\| and area reading of ECE with the weighted
sum; P29 split (figure + reading the plot, "partial self-estimate" defined); P30 plot enlarged; P33
candidates / native / conformal output defined; P35–37 expanded to assumptions, theorem, three proof
slides, what is covered, marginal ≠ conditional (qualified impossibility). Removed orig P51 (Detection
Demo) and P59 (Demos to Play With). After the 06 divider: misconceptions, AI Overviews 2024, and the
"should a truthful model share our errors" answer. P54 split into a 4-benchmark table and the Vectara
chart (data updated to Sep 22, 2026). Page map orig→new: 1–12 same · 13→13–15 · 14–28→16–30 ·
29→31–32 · 30–35→33–38 · 36→39–44 · 37→45–47 · 38–50→48–60 · 51 removed · 52→61–64 · 53→65 ·
54→66–67 · 55–58→68–71 · 59 removed · 60–61→72–73. Note file synced (73 articles; 991→901 fixed;
conditional-coverage claim qualified). `lec06tech.html`: fixed-score and marginal wording on Why It Holds.

**Round 2 (slides-review, 2026-10-06; 73→76):** counting caption and "assuming similar training data" wording;
Kalai bound with its exact forcing condition (2 opt(G) > max|V_c|/min|E_c| + δ) plus a new trigram slide
(Theorem 3 / Corollary 2; stipulated two-option task, no abstention); Kadavath and Xiong figures
split into two slides each with large labels; squirrel sets re-typeset under each photo plus a separate
candidates/native/conformal slide; theorem upper bound qualified (no ties); joint-draw uniform rank; "can break"
exchangeability; singleton = candidate for a validated policy, deferral rule includes empty sets, clinician review, marginal miss over all patients;
"to every user" removed. Note synced (76 articles; P(wrong ∧ singleton) ≤ α vs P(wrong | singleton)).
Tech P2/P11/P12: q̂ = ∞ at k = n+1, ties, A1 + A2 ⇒ exchangeable scores. Round-1→round-2 map: 1–15 same ·
16 new · 16–30→17–31 · 31–32→32–33 · 33→34–35 · 34–35→36–37 · 36→38–39 · 37–73→40–76.

**Round 4 (Albert direct, 2026-10-07; 76→75; branch `trustworthy-ai-lec06-albert-2026-10-07` off 03c274d):**
new Mata v. Avianca context slide (comparison with Lacey); V3 vs R1 roles and chronology (siblings on one base,
not successor); old 15–16 merged into one plain-language slide (formal bound + trigram theorem moved to
`lec06tech.html` §01); new What P(True) Measures slide and histogram re-captioned (overlap = useful but
imperfect discrimination, not calibrated probabilities); "red = wrong" kept on one line; Colab slide dropped;
new Two Kinds of Calibration slide; three proof slides replaced by Why It Works: A Fair Rank (A1, A2,
marginal; proof moved to `lec06tech.html`); Two Strategies reordered Ground → Detect with a larger
diagram; figures enlarged on old P30, 32, 56, 59, 73. Note synced (75 articles; proof kept in the
Coverage Theorem entry). Round-3→round-4 map: 1–5 same · 6 new · 6–14→7–15 · 15+16→16 · 17–31 same ·
32 new · 32–35→33–36 · 36 removed · 37–43 same · 44 new · 44→45 · 45–47→46 · 48–76→47–75.

**Round 5 (slides-review, 2026-10-07; 75 unchanged):** P30, P55, P72 rebuilt figure-first at full
available width with one takeaway line (side bullets dropped; their content is in the note). Guo crop is
now the column titles + reliability-diagram row (histograms omitted); SelfCheckGPT re-cropped at native
resolution (the old crop was vertically squashed); FActScore cropped to the ChatGPT worked example only.
P15 caption restored to "Assuming similar training data …"; P46 adds the distinct-scores / ties line.
Note: P44 temperature scaling "aims to improve" calibration (no exactness, no set-size claim; separate
tuning and conformal splits); n14 drops the checkpoint inference.

**Round 6 (Albert via slides-review #36, 2026-10-07; 75 unchanged):** his questions answered briefly on
the slides. P6: "2023: lawyers cited nonexistent cases fabricated by ChatGPT"; P15: V3 is not R1's newer successor (dates;
tested checkpoint not stated); P32: P(True) = probability of "(A) True" for a proposed answer, useful but
not verified correctness; P44: "Is conformal calibration? Yes: it calibrates a cutoff, not the probabilities".

**2026-09 figure pass (61 slides, unchanged count; PR #24):** every bullet-only content slide now carries
a cited real figure crop or an inline SVG (14 new crops, 26 new SVGs). Real figures sit beside the bullets
in a `1fr auto` grid or stacked below the bullets; every crop excludes the paper caption and is cited with
its figure number. Note file: one "Slide figure" sentence per real-figure article (14); 61 entries, order
matches. Also normalized "$31,100"/"$5,000" in the note to "USD …" outside the `<span>$</span>` escapes.

**2026-08 content revision (58→61):** every citation/number fetched and verified.
Added 3 slides: Guessing, Measured (§02); TruthfulQA (§06); Sycophancy touchpoint (§06).
Replaced the fake-citation anchor (Avianca → Lacey v. State Farm; Avianca kept as a
one-line callback since lec01 covers it) and rewrote Invented Medical Facts around the
verified Med-Gemini error. Reworked Reasoning Models around verified PersonQA numbers.
Added missing cites (Kalai ×3, Xiong, SelfCheckGPT); completed the Angelopoulos & Bates
title (also in `lec06tech.html` — otherwise fix-errors-only, math verified, stays 14 sl).
Flagged as secondary-verified: Lacey "hundreds of filings" tracker line `:124`, SimpleQA
abstention split `:280`, Med-Gemini narrative `:128`, GPT-4o rollback line `:909`.
Note file synced (61 entries, order matches).

**2026-08 note enrichment:** `lec06-hallucination-note.html` upgraded from speaker
script (383 lines) to Script &amp; Companion Notes (723 lines; 61 entries unchanged):
per-entry `.detail` blocks with rigorous definitions (KNVZ valid/error hallucination
formalization, factuality vs faithfulness quadrants, autoregressive MLE = KL
minimization, Guo perfect-calibration Eq. 1 + ECE Eq. 3 with binning caveats,
temperature scaling with limits, exchangeability, split-conformal recipe, semantic
entropy with Rao–Blackwellized + discrete estimators, RAG-Sequence/RAG-Token,
FActScore), theorem blocks with verified proofs/sketches (Kalai–Vempala Corollary 1
monofact lower bound + 3-step sketch, KNVZ IIV-reduction Corollary 1 + Appendix-A
partition sketch, KNVZ Theorem 2 singleton-rate floor, conformal coverage Theorem D.1
with the complete rank-uniformity proof + D.2 tightness, threshold-scoring
λ/(1+λ) and 5p−4 derivations labeled course notes), and brief Background blocks with
26 verified links (Lacey docket + Volokh + Charlotin tracker, Avianca order PDF,
Verge Med-Gemini + arXiv 2404.18416, GPT-5 and o3/o4-mini system cards, TruthfulQA,
SimpleQA, Vectara HHEM ×2, Sharma sycophancy + OpenAI GPT-4o rollback + TechCrunch,
Kadavath, Xiong, SelfCheckGPT, Farquhar Nature, Lewis RAG, Guo, A&B, Ji survey).


## lec07-alignment-failures.html

**Topic:** Alignment failures: when AI learns the wrong objective (90 min; mixed-major
sophomores/juniors; concept-first, light math, no proofs; **no activities — lec07 onward**).
Alignment defined (Ji survey; capability vs alignment grid); reported real-world evaluation/research cases (o1-preview Docker, AI Scientist time limit, Claude 3.7 special-casing, o3/METR); self-contained hallucination bridge (wrong facts vs wrong objective); RLHF intent → feedback →
reward; Goodhart / Gao overoptimization; DPO (no separate reward model) can still overoptimize (Rafailov 2023, 2024); sycophancy (Sharma; GPT-4o April 2025 rollback from
OpenAI's own posts); specification gaming (Krakovna Lego, CoastRunners); reward hacking with a
worked coding-grader example; two controlled studies read as engineered / observed / not shown
(Greenblatt alignment faking; MacDiarmid emergent misalignment from production-RL hacks);
explanation faithfulness ~15 min (Turpin, Lanham, Chen hint test, Baker CoT monitoring and
obfuscation, Korbak). Excludes LIME/SHAP/probes/SAEs (→ `backup-interpretability.html`),
jailbreak taxonomy (lec10), memory/tool/multi-agent threats (lec14). Sycophancy here is the
RLHF-mechanism view; `backup-sycophancy.html` goes further on manipulation and persuasion.
Math lives in `lec07tech.html`. Primary-source register (with snapshot dates)
shipped in the review package.

### Sections (59 slides, 90 min: hook 15 · concepts 25 · evidence 25 · faithfulness 15 · synthesis 10)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:38`, `:50` | |
| **01 — Right Score, Wrong Behavior** | 3–10 | `:87` | alignment defined (Ji 2023 abstract; capability × alignment grid) `:95` · false/unsupported output vs behavior missing the objective (bridge; "can overlap") `:105` · reported evaluation/research cases (o1, AI Scientist, Claude 3.7, o3) `:114` · o1-preview Docker, pre-mitigation CTF (o1 card Fig 4 crop + 5-step key) `:123` · same score, two behaviors (`sys.exit(0)`) `:142` · central question `:152` · three gaps `:161` |
| **02 — From Intent to Reward** | 11–17 | `:170` | InstructGPT's RLHF pipeline, 2022 (large schematic redrawn from Ouyang Fig 2) `:178` · intent/feedback/reward `:187` · proxy too far (Gao Fig 1b RL plot crop, external axis labels + key) `:196` · DPO (Rafailov 2023 Fig 1 crop) `:216` · DPO can still overoptimize (Rafailov 2024 Fig 1 DPO panel crop) `:228` · Goodhart (Hanoi via Baker) `:245` |
| **03 — Sycophancy** | 18–23 | `:256` | definition + dialogue `:264` · 4 tests × 5 assistants `:273` · preference data (Sharma Fig 5, top 5 of 23 rows + axis, unmodified crops) `:288` · GPT-4o April 2025 timeline `:302` · postmortem `:312` |
| **04 — Gaming the Score** | 24–32 | `:322` | specification gaming (Lego) `:330` · CoastRunners `:339` · reward hacking (scope: flaws in reward computation) `:348` · worked example table `:358` · why the hack spreads `:373` · three real hacks `:381` · o3 METR hack counts + 10 follow-up "no" answers about one kernel-hack plan `:397` · patch one hole `:413` |
| **05 — Controlled Studies** | 33–44 | `:424` | how to read (engineered/observed/not shown) `:432` · alignment faking defined (believed training ≠ watched) `:441` · Study 1 setup `:451` · Greenblatt Fig 2 `:461` · Study 1 shows/doesn't (fictional story vs actual RL) `:471` · Study 2 pipeline `:485` · MacDiarmid Fig 1 `:494` · Fig 9 table `:503` · Fig 6a chat-like/agentic pair `:519` · inoculation Fig 5 bars + swatch legend `:537` · Study 2 shows/doesn't `:560` |
| **06 — Is the Explanation the Reason?** | 45–53 | `:574` | plausible ≠ faithful `:582` · Turpin "(A)" `:591` · Lanham interventions (reliance vs wording) `:601` · hint test (inferred influence) `:611` · Chen Fig 1 crops `:621` · Baker Table 1 `:642` · Baker Fig 4 `:656` · can/cannot `:667` |
| **07 — Synthesis & Limits** | 54–59 | `:677` | one pattern (looks successful / remains unproven) `:685` · established vs not `:699` · what helps `:719` · takeaways `:733` · closer `:747` |

**Key citations (all checked against saved PDFs / page captures, 2026-10-10):**
Ouyang 2022 (Fig 2; Eqs. 1–2 in tech); Gao 2022 (Fig 1b; synthetic gold RM); Sharma ICLR 2024
(§3, Figs 1–5); OpenAI 29 Apr + 2 May 2025 (Wayback; self-report); Krakovna 2020; Clark &
Amodei 2016 (Wayback; 20% = post's claim); Ji 2023 survey (v6 abstract, definition); OpenAI o1 System Card Sep 2024 (p. 16, Fig 4); Lu 2024 AI Scientist (§Safe Code Execution); Claude 3.7 Sonnet System Card Feb 2025 (§6); METR 5 Jun 2025 (o3 table, 10/10); Rafailov 2023 DPO (Fig 1; Eq. 7 in tech); Rafailov 2024 DAA overoptimization (Fig 1 DPO panel, §3.1); Baker 2025 (§1, §2.1, Table 1, Fig 4; agent in
o1/o3-mini family; Fig 4 non-frontier); Greenblatt 2024 (Figs 1–2, §1 Limitations; 12%,
86/97%, 78%); MacDiarmid 2025 (Figs 1, 2, 5, 6a, 9; §1 Limitations item 4; production
Sonnet 3.7/4 zero); Turpin 2023; Lanham 2023; Chen 2025 (Fig 1; 25%/39%); Korbak 2025.
Flagged in the source register: Goodhart wording is the common paraphrase; Hanoi story
second-hand (Baker citing Vann 2003, Vann unchecked); Baker "more complex hacks" anecdotal;
OpenAI/Anthropic blog statements and system cards are company self-reports; METR counts may be underestimates.

**Note:** `lec07-alignment-failures-note.html` — 59 entries; each has a minute budget and
elapsed time, script, key takeaway; content slides add figure / setup-model-date /
establishes / does not establish / assumptions / primary-source links. Full MacDiarmid Fig 5
prompt addenda live in entry 43; the three open questions moved into entry 57 (What Helps).

**Tech:** `lec07tech.html` — 12 slides: RM loss (4), KL-penalized RL objective (5), DPO loss,
implicit reward and gradient terms (6), Gao fits (7), hint-test score with symbols (9), random-flip
correction and its domain (10), monitor recall/precision (11), closer "Optimizing the proxy need
not optimize the goal" (12).

## lec08-adversarial.html

**Topic:** Adversarial robustness: when small changes break models (90 min; mixed-major
sophomores/juniors; concept-first, light math, no proofs; **no activities**). Evaluation over
attack catalogue: every claim carries a threat model (controls / knows / wants) and every number
its dataset, model, norm and ε. Panda (Goodfellow Fig 1) and Szegedy random examples; average vs
worst case; linearity and non-robust features as two perspectives, not one cause; budget ε,
ℓ∞ vs ℓ2 (Cohen radius-1.0 scale example), white box / query / none, transfer (Papernot Fig 3;
Amazon 96.19% / Google 88.94%, MNIST 2016); attack = search in the ball, FGSM → PGD main path
(Madry Table 2 bar chart: weaker attacks overstate robustness); adversarial training, Tsipras
trade-off, obfuscated gradients (Athalye Table 1, 7 of 9), adaptive attacks (BPDA, EOT),
AutoAttack, RobustBench as a standardized benchmark with entry rules, scoreboard snapshot
10 Oct 2026 16:47 KST (best known = upper bound; MeanSparse 75.28 → 73.10), ℓ∞ ≠ ℓ2;
empirical vs certified (certificate = stability, not correctness; certified accuracy = correct and
certified), randomized smoothing (g vs PREDICT/CERTIFY, abstention, ℓ2 radius, 1 − α confidence;
Cohen App. Table 2 chart with the Table 1 R = 2 discrepancy disclosed); one physical case (Eykholt stop sign) with its limits; ImageNet-C as a
different question; closing checklist "robust to what, against whom, measured how, at what
cost?". C&W lives in the notes and tech. Excludes multimodal jailbreaks and GCG (lec10),
poisoning (lec09), prompt injection (lec13). Math in `lec08tech.html`.

### Sections (55 slides, 90 min: hook 10 · why + threat model 20 · attacks 20 · defenses + evaluation 25 · physical + synthesis 15)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:35`, `:47` | |
| **01 — A Tiny Nudge** | 3–7 | `:76` | panda (Goodfellow Fig 1, GoogLeNet ε = .007) `:84` · anatomy `:94` · Szegedy Fig 5 random examples `:103` · average vs worst case `:119` |
| **02 — Why It Happens, Who Attacks** | 8–20 | `:128` | boundary sketch `:136` · too linear (Goodfellow Fig 4 logit panel) `:144` · invisible features (Ilyas Fig 1a) `:162` · mislabeled images still teach (Ilyas Fig 1b) `:171` · two perspectives `:180` · threat model `:193` · budget ε `:201` · ℓ∞ vs ℓ2 (units, root-sum-square) `:216` · knowledge `:226` · transfer (Papernot Fig 3) `:234` · real services `:250` · targeted vs untargeted `:260` |
| **03 — Finding the Worst Case** | 21–29 | `:269` | attack as search `:277` · FGSM (Goodfellow Fig 2) `:287` · FGSM by hand `:298` · one step can miss (exact L(u) = sin u) `:312` · PGD algorithm `:325` · steps in ball `:342` · restarts (Madry Fig 1) `:350` · Madry Table 2 bar chart `:360` |
| **04 — Defenses and Honest Evaluation** | 30–45 | `:371` | whole ball `:379` · adversarial training (Madry Fig 3) `:388` · Tsipras Fig 1(b) CIFAR `:398` · obfuscated gradients `:415` · Athalye Table 1 (* / ** keyed) `:424` · adaptive attacks + diagnostics `:442` · AutoAttack `:457` · RobustBench `:467` · scoreboard snapshot (best-known column) `:487` · upper bound `:503` · one ruler `:513` · empirical vs certified `:527` · smoothing (Cohen Fig 2) `:536` · Theorem 1 intuition (Cohen Fig 3; formula in tech) `:553` · Cohen App. Table 2 chart `:570` |
| **05 — Off the Screen, and What to Ask** | 46–55 | `:581` | EOT (average success) `:589` · Eykholt Fig 1 (Tables 1, 3) `:599` · what it does not show `:609` · ImageNet-C `:629` · four questions `:644` · applied to 73.71% under AutoAttack `:652` · established vs open `:667` · takeaways `:687` · closer `:701` |

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
`backup-prompt-injection.html`) and the former Wk 12 watermark deck (lec12-watermark, 68 sl; deleted with its note,
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

## backup-prompt-injection.html

*Former Wk 11 deck (old names lec11-prompt-injection, its note, and lec11tech), moved unchanged on 2026-10-10 to `backup-prompt-injection.html`, `backup-prompt-injection-note.html` and `backup-prompt-injectiontech.html`; line pointers below still hold. File names in this section use the backup names. Scheduled for the Wk 13 rebuild.*

**Topic:** Prompt injection & agentic safety (~90 min). Injection vs jailbreak
(attacker is a third party arriving via data, not the user); direct vs indirect
injection; data-vs-control-plane confusion as THE core idea; the agentic risk surface
(tools, agent loop, confused deputy, lethal trifecta); real incidents (Bing "Sydney"
leak, Greshake real-app injection, email-exfiltration class, EchoLeak, SpAIware memory
poisoning, CamoLeak/GitHub MCP); why it is hard (no privilege separation, filtering
brittle, no clean escape); defenses and why partial (filtering, spotlighting,
instruction hierarchy, taint tracking, dual-LLM, capability control/CaMeL, human in
the loop, least privilege); 2025–26 frontier (AI browsers, MCP, AgentDojo, adaptive
attacks). Security model lives in `backup-prompt-injectiontech.html`. Autonomy risks touched in Open
Problems only — full treatment stays in `backup-agentic-autonomy.html` (not absorbed).

### Sections (66 slides, ~90 min — content-revised 2026-08 from 58, figure pass 2026-09 from 63; all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:34`, `:46` | |
| **01 — Direct vs Indirect Injection** | 3–13 | `:79` | one-line idea (SVG) `:87` · tiny example (SVG) `:125` · two failure modes (SVG) `:155` · **direct (Perez & Ribeiro Fig. 1)** `:194` · **indirect (Greshake Fig. 1)** `:215` · **why indirect is worse (Liu et al. figure)** `:236` · hidden text (SVG) `:257` · **Naming the Problem (timeline SVG; Goodside demonstrated / Willison named)** `:300` · not the same as SQL (SVG) `:336` · **The #1 LLM Risk (OWASP LLM01:2025; SVG list)** `:374` |
| **02 — The Agentic Surface** | 14–23 | `:413` | chatbot→agent (SVG) `:421` · what a tool is `:469` · agent loop (SVG) `:482` · two channels (SVG) `:524` · data becomes control (SVG) `:555` · attack picture (SVG) `:580` · **confused deputy (InjecAgent overview)** `:618` · three ingredients `:635` · **Lethal Trifecta (Willison 2025; Venn SVG)** `:648` |
| **03 — Real Incidents** | 24–33 | `:673` | **Bing "Sydney" Leak (Kevin Liu direct injection; chat SVG)** `:681` · **Greshake real apps (Fig. 2 threat overview)** `:714` · email-exfiltration class (SVG) `:730` · **EchoLeak CVE-2025-32711 (SVG)** `:764` · **SpAIware memory poisoning (SVG)** `:804` · **CamoLeak + GitHub MCP (SVG)** `:849` · quiet exit channels (SVG) `:889` · vendors responded (SVG) `:933` · pattern emerges `:973` |
| **04 — Why It Is Hard** | 34–40 | `:988` | no privilege separation (SVG) `:996` · one flat context (SVG) `:1034` · instructions look alike (SVG) `:1052` · filtering brittle (SVG) `:1083` · no clean escape (SVG) `:1122` · still open (illustrative SVG bars) `:1148` |
| **05 — Defenses** | 41–55 | `:1180` | layered mindset (SVG) `:1188` · I/O filtering (SVG) `:1227` · **Spotlighting (Hines 2024 Fig. 4)** `:1263` · **Spotlighting, Measured (Hines Fig. 6; added 2026-09)** `:1283` · **Instruction Hierarchy (Wallace OpenAI 2024 Fig. 1)** `:1298` · **Hierarchy, Measured (Wallace Fig. 2; added 2026-09)** `:1314` · taint tracking (SVG) `:1329` · dual-LLM (Willison 2023) `:1367` · quarantine picture (SVG) `:1381` · **Capability Control (CaMeL Fig. 1)** `:1414` · human in loop (SVG) `:1434` · least privilege (SVG) `:1473` · scorecard `:1503` · toy-agent demo `:1515` |
| **06 — Frontier 2025–26** | 56–64 | `:1532` | **New Surfaces, Same Flaw (AI browsers + MCP; SVG)** `:1540` · **measuring (AgentDojo Fig. 6a)** `:1580` · **AgentDojo (NeurIPS 2024 D&B; Fig. 1)** `:1601` · **Defenses on AgentDojo (Fig. 9a; added 2026-09)** `:1617` · **Where Defenses Stand (Zhan NAACL 2025 Fig. 2)** `:1637` · design shift (SVG) `:1653` · open problems `:1691` · practical advice (SVG) `:1704` |
| Takeaways / Closer | 65–66 | — | key takeaways `:1739` · closer `:1752` |

**Key definitions / citations (all source-verified 2026-08):**
- Naming: Goodside demonstrated on GPT-3, Willison coined the name — `:300` — Willison,
  "Prompt injection attacks against GPT-3", Sept 2022; Perez & Ribeiro, "Ignore Previous
  Prompt: Attack Techniques for Language Models", 2022 (arXiv 2211.09527).
- OWASP LLM01: Prompt Injection, #1 in the 2025 edition (second edition running) — `:374`.
- Lethal trifecta (private data + untrusted content + external communication) — `:648` —
  Willison, "The lethal trifecta for AI agents", June 2025.
- Bing "Sydney" system-prompt extraction by direct injection — `:681` — Kevin Liu, Feb 2023.
- Indirect injection on real deployed apps — `:714` — Greshake, Abdelnabi, Mishra, Endres,
  Holz, Fritz, "Not What You've Signed Up For: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection", ACM AISec 2023 (arXiv 2302.12173).
- EchoLeak zero-click exfiltration — `:764` — CVE-2025-32711 (Microsoft 365 Copilot),
  Aim Security, June 2025; server-side patch, no known exploitation.
- SpAIware persistent memory exfiltration — `:804` — Rehberger, Sept 2024 (ChatGPT macOS
  app); fixed by OpenAI.
- CamoLeak (Copilot Chat, per-image exfil) + GitHub MCP private-repo leak — `:849` —
  reported via HackerOne, no CVE (GitHub-rated CVSS 9.6), Legit Security, Oct 2025;
  Invariant Labs, May 2025.
- Spotlighting — `:1263` — Hines et al., "Defending Against Indirect Prompt Injection
  Attacks With Spotlighting", 2024 (arXiv 2403.14720).
- Instruction hierarchy — `:1298` — Wallace et al. (OpenAI), "The Instruction Hierarchy:
  Training LLMs to Prioritize Privileged Instructions", 2024 (arXiv 2404.13208).
- Dual-LLM pattern — `:1367` — Willison, "The Dual LLM pattern for building AI assistants
  that can resist prompt injection", April 2023.
- Capability control / CaMeL — `:1414` — Debenedetti et al., "Defeating Prompt Injections
  by Design", 2025 (arXiv 2503.18813).
- AI-browser + MCP attack surface — `:1540` — Brave, "Indirect prompt injection in
  Perplexity Comet" & "Unseeable prompt injections in screenshots", 2025; Invariant Labs
  GitHub MCP, 2025.
- AgentDojo — `:1601` — Debenedetti et al., "AgentDojo: A Dynamic Environment to Evaluate
  Prompt Injection Attacks and Defenses for LLM Agents", NeurIPS 2024 (Datasets &
  Benchmarks) (arXiv 2406.13352).
- Direct injection / goal hijacking figure — `:194` — Perez & Ribeiro 2022, Fig. 1.
- Indirect-injection planting + Liu et al. app-injection figure — `:215`, `:236`.
- Confused deputy via InjecAgent overview — `:618` — Zhan et al., "InjecAgent", ACL 2024 Findings.
- Spotlighting measured (Fig. 6, GPT-4) — `:1283`; instruction hierarchy measured
  (Fig. 2, GPT-3.5 Turbo, five attacks) — `:1314`; AgentDojo defenses (Fig. 9a, five
  defenses, utility vs targeted ASR) — `:1617`.
- Adaptive attacks break defenses (8 defenses bypassed, ASR >50%) — `:1637` — Zhan, Fang,
  Panchal, Kang, "Adaptive Attacks Break Defenses Against Indirect Prompt Injection
  Attacks on LLM Agents", NAACL 2025 Findings (arXiv 2503.00061).

**Figures (2026-09 pass):** 14 captured paper figures in `figs/` — Direct Injection `:194` (`perez-hijack.png`); Indirect Injection `:215` (`greshake-plant.png`); Why Indirect Is Worse `:236` (`liu-app.png`); The Confused Deputy `:618` (`injecagent-overview.png`); Injecting Real Applications `:714` (`greshake-overview.png`); Spotlighting and Delimiting `:1263` (`hines-datamark.png`); Spotlighting, Measured `:1283` (`hines-encoding.png`); Instruction Hierarchy `:1298` (`wallace-hierarchy.png`); Hierarchy, Measured `:1314` (`wallace-results.png`); Capability Control `:1414` (`camel-flows.png`); Measuring the Problem `:1580` (`agentdojo-utility-asr.png`); AgentDojo `:1601` (`agentdojo-overview.png`); Defenses on AgentDojo `:1617` (`agentdojo-defenses.png`); Where Defenses Stand `:1637` (`zhan-adaptive.png`). 35 inline SVGs: The One-Line Idea `:87`, A Tiny Example `:125`, Two Failure Modes `:155`, Where Hidden Text Hides `:257`, Naming the Problem `:300`, Not the Same as SQL `:336`, The #1 LLM Risk `:374`, From Chatbot to Agent `:421`, The Agent Loop `:482`, Two Channels, One Pipe `:524`, Data Becomes Control `:555`, The Attack Picture `:580`, The Lethal Trifecta `:648`, The Bing "Sydney" Leak `:681`, The Email Exfiltration Class `:730`, EchoLeak: Zero Clicks `:764`, Poisoning the Memory `:804`, Even Coding Tools `:849`, Quiet Exit Channels `:889`, Vendors Have Responded `:933`, No Privilege Separation `:996`, One Flat Context `:1034`, Instructions Look Alike `:1052`, Filtering Is Brittle `:1083`, No Clean Escape `:1122`, Still an Open Problem `:1148`, A Layered Mindset `:1188`, Input and Output Filtering `:1227`, Taint Tracking `:1329`, Quarantine in One Picture `:1381`, Keep a Human in the Loop `:1434`, Least Privilege `:1473`, New Surfaces, Same Flaw `:1540`, The Design Shift `:1653`, Practical Advice `:1704`. Citations use `.cite-left`.

**2026-08 content revision (58→63):** every citation/incident fetched and verified.
Added 5 slides: The #1 LLM Risk (§01, OWASP LLM01:2025); EchoLeak: Zero Clicks,
Poisoning the Memory (SpAIware), Even Coding Tools (CamoLeak + GitHub MCP) (§03 —
lec01 keeps only the EchoLeak teaser, full treatment here); New Surfaces, Same Flaw
(§06, AI browsers + MCP). Fixes: **naming attribution corrected** (was "Willison named
it" alone → Goodside demonstrated, Willison named, per Willison's own Sept 2022 post);
**Bing slide rewritten** (unverifiable "planted web text / adopted personas" narrative →
verified Kevin Liu Feb 2023 system-prompt extraction); **Instruction Hierarchy cite was
wrong** (mangled "Wu et al., Instructional Segment Embedding" → Wallace et al. OpenAI
2024, the actual paper); Spotlighting title corrected to the real arXiv title; AgentDojo
title completed + venue added; Zhan et al. adaptive-attacks cite added to Where Defenses
Stand; quarantine-SVG label overlap fixed. `backup-prompt-injectiontech.html` checked: security model
verified (dual-LLM matches Willison 2023; CaMeL cite correct), two prose-dash lint
warnings fixed (stays 9 sl). Note file synced (63 entries, order matches).

**2026-08 note enrichment:** `backup-prompt-injection-note.html` upgraded from speaker
script to **script + companion notes** (395→736 lines; 63 entries unchanged). Per-entry
`.detail` blocks: prompt injection formalized (f over one token stream, x = τ(s,u,d),
agent loop x_{t+1} = x_t ∥ a_t ∥ o_t, injection success as unauthorized action — all
labeled course notes); control/data-plane and confused-deputy (Hardy 1988) definitions
expanded from the tech file; full Greshake et al. taxonomy (4 injection methods × 6 threat
types) stated from arXiv 2302.12173; defense formalisms (spotlighting variants,
instruction hierarchy, taint/IFC lattice, dual-LLM invariant, CaMeL capabilities,
Saltzer–Schroeder least privilege); the "no clean escape / unsolvable by prompting
alone" argument given as a labeled 5-step informal argument (not a theorem), empirically
anchored to Zhan et al. 2025. Incident backgrounds + 24 verified links (all fetched:
arXiv ×7, Willison ×3, Brave ×2, CVE.org/MSRC/Aim, Legit/Register/Invariant,
embracethered, Ars, OWASP ×2, MIT Hardy, MIT Saltzer, dblp). Note and deck both
corrected 2026-08-19: CamoLeak has NO CVE — the previously cited "CVE-2025-59145"
is an unrelated npm color-name malware record.

**2026-09 figure pass (63→66):** every content slide now carries a figure. 14 figure
crops cut from the cited papers into `figs/` (Perez & Ribeiro, Greshake ×2, Liu et al.,
InjecAgent, Hines ×2, Wallace ×2, CaMeL, AgentDojo ×3, Zhan), each with a figure-number
cite; 32 new inline SVG diagrams for previously text-only slides (35 SVGs total). Three
slides added to carry measured results: Spotlighting, Measured (Hines Fig. 6),
Hierarchy, Measured (Wallace Fig. 2), Defenses on AgentDojo (Fig. 9a). Where Defenses
Stand: highlight folded into the intro so the Zhan chart fits at 640 px. Note synced
(66 entries, `Slide figure:` lines on every figure slide, three new entries with detail
blocks; "Wu and colleagues" misattribution in the Instruction Hierarchy script fixed).
60-dpi render check of all 66 pages: no overflow or overlap.

## lec12-fairness.html

**Topic:** Fairness (90 min; mixed-major sophomores/juniors; concept-first, light math, no proofs on the
slides; **no activities**). Where bias enters (sampling, labels, feedback; Gender Shades benchmark composition;
Obermeyer cost-as-proxy case; why dropping the protected attribute fails). Measuring fairness: four rates and
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

**Figures (14 cited image files in `figs/`):** `hardt-eqodds-roc.png` `:347` · `hardt-fico-thresholds.png` `:406` ·
`chouldechova-deciles.png` `:434` · `chouldechova-fpr-priors.png` `:476` · `chouldechova-calibration.png` `:494` ·
`reweighing-aif360.png` `:721` · `reductions-frontier.png` `:747` · `hardt-eo-threshold.png` `:762` ·
`hardt-fico-cost.png` `:779` · `aif360-frontier.png` `:796` · `gender-shades.png` `:834` · `bbq-example.png` `:892` ·
`bbq-bias-scores.png` `:903` · `bianchi-occupations.png` `:916`.

**2026-10 rebuild:** merges the former Wk 13 and Wk 14 fairness decks, moved unchanged (with notes and tech files)
to `backup-fairness-defs*.html` and `backup-fairness-mitigation*.html`. Built to the slides-review decisions (#134):
Amazon, adversarial debiasing, Gemini, Tamkin and Wilson &amp; Caliskan only in the notes; EO 14319 cut from the deck;
governance ≈ 3 min; Dwork and Kusner formal in the tech supplement and notes.

**Note:** `lec12-fairness-note.html` — 56 entries with minute budget and elapsed time, script, key takeaway;
content slides add figure, setup/date, establishes / does not establish, assumptions and primary-source links
(29 sources). "Going further" blocks hold the notes-only material (Dwork/Kusner, Zhang, Amazon, Tamkin, Wilson &amp;
Caliskan, Eloundou, Gemini, EO 14319).

**Tech:** `lec12tech.html` — 16 slides:
- four rates (4); five criteria (5); Dwork Lipschitz + Kusner counterfactual (6); calibration and PPV via the
  score mix (7)
- Chouldechova identity (9); Kleinberg proof sketch (10); worked example computed (11)
- reweighing (13); reductions saddle point (14); group thresholds as a derived predictor (15)

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
