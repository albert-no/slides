# trustworthy-ai/ — Trustworthy AI course

Undergraduate course for juniors/seniors (15 weeks × 1.5 hr), mixed majors with
basic Python/Colab experience. **Mode:** concept introduction + motivation first —
foundational works, a little recent work, light technical detail, no proofs.
At most one intuitive formula per key concept.
Each lecture: a **formal definition → short history → 2025–26 frontier**, plus an
optional **Colab demo** students can run themselves (no homework, nothing to submit).

All lecture decks live flat in this folder (`lecNN-*.html`). Arc climbs the
**trust stack**: data → model → output → society. Real paper figures (cropped +
cited) live in `figs/`; `bundle.py` inlines them. Concept diagrams are inline SVG.

## Modules

| Module | Weeks | Theme |
|---|---|---|
| 0. Foundations | 1 | What "trustworthy" means, threat-model thinking |
| 1. Privacy & Data | 2–5 | What models leak about their training data |
| 2. Reliability | 6–7 | Can you believe the answer, and see why |
| 3. Security | 8–11 | How models are attacked, train- and inference-time |
| 4. Provenance & Fairness | 12–14 | Watermarking, fairness, accountability |
| 5. Synthesis | 15 | Governance, frontier, demo showcase |

## Lecture index

| Wk | File | Topic | Status |
|---|---|---|---|
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **drafted** (47 sl) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **drafted** (84 sl) |
| 3 | `lec03-mia.html` | Membership inference attacks | **drafted** (59 sl) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **drafted** (59 sl) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **drafted** (58 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **drafted** (58 sl) |
| 7 | `lec07-interpretability.html` | Interpretability & explainability | **drafted** (57 sl) |
| 8 | `lec08-adversarial.html` | Adversarial examples (attack + defense) | **drafted** (56 sl) |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **drafted** (55 sl) |
| 10 | `lec10-jailbreak.html` | Jailbreaks & LLM safety | **drafted** (54 sl) |
| 11 | `lec11-prompt-injection.html` | Prompt injection & agentic safety | **drafted** (58 sl) |
| 12 | `lec12-watermark.html` | Watermarking, deepfakes & provenance | **drafted** (55 sl) |
| 13 | `lec13-fairness-defs.html` | Fairness I — definitions & impossibility | **drafted** (54 sl) |
| 14 | `lec14-fairness-mitigation.html` | Fairness II — mitigation & accountability | **drafted** (55 sl) |
| 15 | `lec15-governance.html` | Governance, frontier & demo showcase | **drafted** (53 sl) |

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
| `lec02tech.html` | Wk 2 (privacy/DP) | (ε,δ)-DP def; ε/e^ε log-odds; sensitivity Δq; Laplace/Gaussian mechanisms; randomized-response algebra; DP-SGD (clip C + N(0,σ²C²) + accountant); composition/Rényi. Points to `courses/privacy/lectures/01-dp/` | **drafted** (21 sl) |
| `lec03tech.html` | Wk 3 (MIA) | score+threshold; likelihood ratio Λ(x); LiRA (Gaussian fit + LR test); ROC / TPR@low-FPR; DP bound TPR ≤ e^ε·FPR + δ | **drafted** (11 sl) |
| `lec04tech.html` | Wk 4 (memorization) | k-extractability def; memorization-fraction metric; log-linear scaling law | **drafted** (9 sl) |
| `lec05tech.html` | Wk 5 (unlearning) | exact vs approx; (ε,δ) unlearning inequality; influence function θ₋ₓ ≈ θ̂ + (1/n)H⁻¹∇ℓ + Hessian infeasibility; gradient ascent; SISA cost | **drafted** (11 sl) |
| `lec06tech.html` | Wk 6 (hallucination) | reliability diagram; ECE = Σ_b (n_b/n)|acc_b−conf_b|; temperature scaling; conformal coverage Pr[y∈C(x)]≥1−α + threshold quantile; semantic entropy | **drafted** (14 sl) |
| `lec07tech.html` | Wk 7 (interpretability) | Shapley φ_i + axioms; LIME surrogate objective; gradient saliency; integrated gradients; SAE reconstruction+sparsity, superposition | **drafted** (20 sl) |
| `lec08tech.html` | Wk 8 (adversarial) | perturbation set B_p(x,ε); FGSM; PGD projected iteration; adversarial-training min-max; randomized-smoothing certified radius | **drafted** (19 sl) |
| `lec09tech.html` | Wk 9 (poisoning) | poison fraction α; clean-label feature-collision objective; backdoor blended objective; spectral signatures; activation clustering | **drafted** (16 sl) |
| `lec10tech.html` | Wk 10 (jailbreak) | RLHF KL-penalized objective; GCG target `min -log Pr["Sure, here"]`; gradient-guided token swaps | **drafted** (12 sl) |
| `lec11tech.html` | Wk 11 (prompt injection) | data-vs-control plane; confused deputy; agent threat model; capabilities/least privilege; taint tracking; dual-LLM pattern (security model, not equations) | **drafted** (9 sl) |
| `lec12tech.html` | Wk 12 (watermark) | green-list logit bias; null Binomial(T,γ); detection z = (|s|_G−γT)/√(Tγ(1−γ)); false-positive bound; z ∝ √T; robustness–quality tradeoff | **drafted** (10 sl) |
| `lec13tech.html` | Wk 13 (fairness defs) | demographic parity / equalized odds / calibration as conditional-prob defs; base rates; impossibility theorem (Kleinberg/Chouldechova) + proof sketch | **drafted** (15 sl) |
| `lec14tech.html` | Wk 14 (fairness mitigation) | reweighing w(g,y); penalized min Loss+λ·Unfairness; constrained form; reductions (Agarwal 2018); post-processing per-group thresholds (Hardt 2016) | **drafted** (17 sl) |
| `lec15tech.html` | Wk 15 (governance) | EU AI Act risk-tier taxonomy; NIST RMF as Govern→Map→Measure→Manage loop; what "measurable" audit metrics mean (deliberately light — governance is non-mathematical) | **drafted** (6 sl) |

## Backup / swap-in materials (not in the 15-week core)

Optional decks for substitution or extra sessions. Each has a `-note.html` script.

| File | Topic | Slots in where | Status |
|---|---|---|---|
| `backup-sycophancy.html` | Sycophancy, manipulation & persuasion | merge into Wk 6, or standalone | **drafted** (38 sl) |
| `backup-copyright.html` | Copyright, consent & data provenance | pairs with Wk 4 (memorization) | **drafted** (45 sl) |
| `backup-agentic-autonomy.html` | Agentic autonomy risks beyond injection | expands Wk 11 | **drafted** (47 sl) |
| `backup-model-stealing.html` | Model stealing / extraction attacks | swap for Wk 9, or standalone | **drafted** (51 sl) |

**Draft note:** lec 3–15 + backups were generated in one parallel pass (each ~50–60
slides, lint-clean, with SVG concept diagrams + cited papers). The **2026-07-15 pass**
de-technicalized the drafts for the undergrad audience, trimmed lec02 to fit 90 min,
and completed the real-figure pass — **all `TODO real figure` markers are now resolved**
(every deck lint-clean). The per-slide screenshot audit is the remaining polish step.

**2026-07-15 real-figure pass (complete).** Every TODO marker replaced with a real,
cropped-and-cited paper figure or a data-backed SVG:
- `lec03` duplication histogram (`figs/carlini_duplicates.png`, Carlini diffusion Fig 5).
- `lec08` panda→gibbon (`figs/panda-gibbon.png`) + Eykholt stop-sign (`figs/eykholt-stopsign.png`, CVPR 2018 Fig 1).
- `lec09` BadNets trigger strip (`figs/badnets-trigger.png`, Gu et al. 2017 Fig 7).
- `lec10` Wei failure modes (`figs/wei-jailbroken.png`, NeurIPS 2023 Fig 1), GCG schematic (`figs/gcg-schematic.png`, Zou 2023 Fig 1 — replaced SVG), many-shot power-law (`figs/msj-powerlaw.png`, Anil et al. NeurIPS 2024 Fig 2).
- `lec13`/`lec14` Bianchi occupation grid (`figs/bianchi-occupations.png`, FAccT 2023 Fig 1); `lec14` Gender Shades table (`figs/gender-shades.png`, FAT* 2018 Table 4). lec13 COMPAS TODO removed (illustrative SVG kept — real news graphic is copyrighted).
- `lec06` Vectara HHEM hallucination bar chart (inline SVG, data May 2026).
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
- **Watermark** (Wk 12) ↔ `courses/privacy/lectures/06-watermark/`.

When drafting a stub, read the corresponding leaf `OUTLINE.md` there first and
**compress, don't re-derive** — link back rather than restating proofs.

---

## lec01-introduction.html

**Topic:** What "trustworthy" means; AI fails differently than software; the five
trust dimensions; threat-model thinking (knowledge × timing); the 15-week map; how
demos work. Sets the vocabulary used all term.

### Sections (47 slides, ~35–40 min)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Why Trust?** | 3–12 | `:69` | Bias/COMPAS `:91` · Amazon · Mata v. Avianca · chatbots · memorization · deepfakes · prompt injection |
| **02 — How AI Fails Differently** | 13–21 | `:206` | SW vs learned · failure in weights · **panda→gibbon image** `:244` · three sources · black box · **six trust dimensions** `:296` |
| **03 — Threat-Model Thinking** | 22–31 | `:325` | **What is a threat model (+adversary SVG)** `:333` · house analogy · white/black-box · train/inference · **attack map 2×2 (SVG)** `:425` · medical-LLM worked example |
| **04 — Trust Stack & Course Map** | 32–41 | `:491` | **trust stack (layered SVG)** `:499` · **4-module 15-week timeline (SVG)** `:523` · module previews · week-by-week · 2025–26 themes |
| **05 — How We'll Work** | 42–46 | `:639` | concepts not proofs · hands-on demos · the goal |
| Closer | 47 | — | |

**Visuals:** real image — panda→gibbon adversarial example (`figs/panda-gibbon.png`,
Goodfellow et al. 2015) `:244`. SVG — adversary↔system threat diagram `:333`,
attack-map 2×2 `:425`, layered trust-stack `:499`, 15-week module timeline `:523`.
**Key framing:** threat model = *who* / *what they know* (white/black-box) / *what they
can do* (train/inference-time); the 2×2 locates every attack. Examples-first: real
incidents in §01 anchor the six trust dimensions. Citations use `.cite-left`. Page
number: bold `.slide-num` only.

---

## lec02-privacy-dp.html

**Topic:** Why models leak and anonymization fails; the differential-privacy idea
(presence barely changes output); the formal $(\varepsilon,\delta)$-DP definition;
the budget $\varepsilon$; randomized response; noise-by-sensitivity; DP-SGD;
privacy–utility tradeoff; federated learning; private foundation models (2025–26).
Intuition pass — points to the privacy course for rigor.

### Sections (84 slides, full 90 min — trimmed 2026-07-15 from 93 to fit the slot)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:33`, `:45` | |
| **01 — The Privacy Problem** | 3–15 | `:78` | **GPT-2 extraction image** `:112` · Secret Sharer · "repeat poem" · **diffusion copy image (Ann)** `:158` · 3 kinds of leak · **Sweeney 87% Venn (SVG)** `:224` · Netflix+AOL merged `:245` |
| **02 — How Leakage Is Measured** | 16–23 | `:259` | membership inference · **MIA loss-overlap (SVG)** `:292` · model inversion · NYT v. OpenAI · Italy ban (shadow models / extraction-scaling / deep-leakage cut — full treatment Wk 3/4; FL leak stays in §05) |
| **03 — Differential Privacy** | 24–45 | `:372` | two-worlds · **$(\varepsilon,\delta)$-DP definition** `:457` (plain-English lead-in) · budget $\varepsilon$ · post-processing · **indistinguishability + heights (SVG)** `:568-` (warm-up now carries coin-flip payoff) · what DP does/doesn't |
| **04 — Achieving DP: Add Randomness** | 46–58 | `:650` | **Randomized response + coin-tree (SVG)** `:684` · recover-the-rate worked example · local vs central DP · RAPPOR/Apple · **Laplace mechanism + noise bell (SVG)** `:763` · sensitivity |
| **05 — Private Machine Learning** | 59–70 | `:824` | **DP-SGD** `:853` (clip+noise merged to one slide) · privacy accountant · utility cost (benchmark folded in) · **federated learning (SVG)** `:920` · Gboard · FL still leaks · secure aggregation |
| **06 — Frontier 2025–26** | 71–79 | `:984` | private fine-tuning (Yu, Li 2022) `:992` · private synthetic data · web-scale puzzle · privacy auditing · unlearning preview · Apple PCC · EU AI Act |
| Wrap (deeper / demos / takeaways) | 80–83 | — | `:1093`–`:1119` |
| Closer | 84 | — | `$\varepsilon$` `:1131` |

**Key definitions / citations:**
- $(\varepsilon,\delta)$-DP — `:457` — Dwork, McSherry, Nissim, Smith, TCC 2006.
- **Statistical indistinguishability** (heights example, Korea/Japan Gaussians) — `:568-628` — replaced the composition slides per design choice; "Many Samples Break It" `:616` folds in the composition intuition (repeated queries erode privacy). Warm-up slide `:581` now carries the coin-flip highlight (former "One Person Tells You Little" slide merged in).
- Randomized response — `:671` — Warner, JASA 1965.
- DP-SGD — `:853` — Abadi et al., ACM CCS 2016.
- De-anonymization — `:245` — Narayanan & Shmatikov, IEEE S&P 2008.

**Real images** (`figs/`, cropped + cited per GOTCHAS): GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini et al. 2021, Fig 1) `:116`; Stable-Diffusion copy `figs/calrini-ann.png` (Carlini et al.
2023 / Somepalli et al. 2023) `:162`. Duplication histogram `figs/carlini_duplicates.png` moved to
`lec04-memorization.html` ("Duplication Drives It Again"). **SVG figures:** Sweeney linkage Venn
`:224`, MIA loss-overlap `:292`, height-distribution overlap, randomized-response coin tree `:684`,
Laplace noise bell `:763`, federated learning `:920`. Citations use `.cite-left`. Page number: bold
`.slide-num` only. Intuition pass — points to `courses/privacy/lectures/01-dp/` for rigor.

**2026-07-15 trim (9 slides):** Netflix+AOL merged; Shadow Models, MIA on Modern Models,
Extraction Scales With Size, Leaky Gradients cut from §02 (owned by Wk 3/4 and §05's "FL Still
Leaks"); "One Person Tells You Little" merged into the heights warm-up; Why Clip + Why Add Noise
merged; Utility Cost + Numbers on a Benchmark merged; duplicate "Frontier Models Still Memorize"
cut (§01's "Make ChatGPT Leak" covers it, same citation). Note file synced.
