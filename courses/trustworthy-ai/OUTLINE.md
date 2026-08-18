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
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **revised 2026-08** (35 sl) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **revised 2026-08** (84 sl) |
| 3 | `lec03-mia.html` | Membership inference attacks | **revised 2026-08** (63 sl) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **revised 2026-08** (58 sl) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **revised 2026-08** (66 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **revised 2026-08** (61 sl) |
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
| `lec05tech.html` | Wk 5 (unlearning) | exact vs approx; (ε,δ) unlearning inequality; influence function θ₋ₓ ≈ θ̂ + (1/n)H⁻¹∇ℓ + Hessian infeasibility; gradient ascent; SISA cost | **fixed 2026-08** (11 sl: (ε,δ) cite Ginart→Guo/Sekhari + two-sided bound; SISA speedup R·L→R & 3/2) |
| `lec06tech.html` | Wk 6 (hallucination) | reliability diagram; ECE = Σ_b (n_b/n)|acc_b−conf_b|; temperature scaling; conformal coverage Pr[y∈C(x)]≥1−α + threshold quantile; semantic entropy | **checked 2026-08** (14 sl: math verified, Angelopoulos & Bates cite title completed) |
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

**Topic:** Course overview (~30 min). What "trustworthy" means; AI fails differently
than software; the six trust dimensions; threat-model thinking (knowledge × timing);
the course map — fifteen topics in four groups (content areas, not a fixed timetable);
how the course works. Sets the vocabulary used all term.

### Sections (35 slides, ~30 min — trimmed 2026-08 from 47, all incidents source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Why Trust?** | 3–12 | `:68` | COMPAS `:91` · Amazon `:105` · Mata v. Avianca + Deloitte 2025 `:120` · Air Canada + $1 car `:138` · memorization `:156` · deepfake robocall `:170` · EchoLeak prompt injection `:183` · the pattern `:197` |
| **02 — How AI Fails Differently** | 13–17 | `:212` | SW vs learned `:220` · **panda→gibbon image** `:238` · three failure sources `:248` · **six trust dimensions** `:260` |
| **03 — Threat-Model Thinking** | 18–22 | `:275` | **What is a threat model (+adversary SVG)** `:284` · knowledge × timing merged 2×2 grid `:314` · **attack map 2×2 (SVG)** `:340` · no threat model, no answer `:366` |
| **04 — Trust Stack & Course Map** | 23–30 | `:381` | **trust stack (layered SVG)** `:390` · course at a glance (4 topic-group cards) `:413` · Group 1–4 previews `:428`–`:464` · 2025–26 themes `:476` |
| **05 — How We'll Work** | 31–34 | `:489` | concepts not proofs `:498` · optional demos & supplements `:515` · the goal `:531` |
| Closer | 35 | `:543` | |

**Visuals:** real image — panda→gibbon adversarial example (`figs/panda-gibbon.png`,
Goodfellow, Shlens, Szegedy, ICLR 2015, Figure 1; confidences 57.7%→99.3% verified
against the paper) `:241`. SVG — adversary↔system threat diagram `:296`, attack-map
2×2 `:344`, layered trust-stack `:394`. (15-week timeline SVG removed in the 2026-08
trim: topics are presented as content areas, not a schedule.)
**Key citations (all source-verified 2026-08):** Angwin et al., ProPublica 2016
(COMPAS) · Dastin, Reuters 2018 (Amazon) · Mata v. Avianca, S.D.N.Y. 2023 ·
Deloitte Australia / DEWR partial refund, Oct 2025 · Moffatt v. Air Canada, 2024
BCCRT 149 · Carlini et al., USENIX Security 2021 + Nasr et al. 2023 (extraction) ·
EchoLeak CVE-2025-32711 (M365 Copilot, June 2025).
**Key framing:** threat model = *who* / *what they know* (white/black-box) / *what they
can do* (train/inference-time); the 2×2 locates every attack. Examples-first: real
incidents in §01 anchor the six trust dimensions. Citations use `.cite-left`. Page
number: bold `.slide-num` only.

**2026-08 trim (47→35):** week-by-week schedule slides, 15-week timeline SVG,
medical-LLM worked example, house analogy, black-box slide, "failure lives in the
weights", "bigger models new surprises", "dimensions interact" cut or merged; the
white/black-box and train/inference slides merged into one knowledge×timing grid;
Bing "Sydney" bullet deleted (unverifiable as prompt injection), replaced by
verified EchoLeak 2025; Deloitte 2025 incident added. Note file synced (35 entries).

---

## lec02-privacy-dp.html

**Topic:** Why models leak and anonymization fails; the differential-privacy idea
(presence barely changes output); the formal $(\varepsilon,\delta)$-DP definition;
the budget $\varepsilon$; randomized response; noise-by-sensitivity; DP-SGD;
privacy–utility tradeoff; federated learning; private foundation models (2025–26).
Intuition pass — points to the privacy course for rigor.

### Sections (84 slides, full 90 min — content-revised 2026-08, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — The Privacy Problem** | 3–15 | `:77` | **GPT-2 extraction image** `:116` · Secret Sharer · "repeat poem" · **diffusion copy image (Ann)** `:162` · Copilot secrets (Huang FSE 2024) `:176` · 3 kinds of leak · **Sweeney 87% Venn (SVG)** `:229` + Golle 63% caveat · Netflix+AOL merged `:246` |
| **02 — How Leakage Is Measured** | 16–23 | `:260` | membership inference · **MIA loss-overlap (SVG)** `:298` · model inversion · NYT v. OpenAI · Italy ban ("Privacy Is a Business Risk" slide deleted 2026-08 — content moved to note's "Regulators Step In" entry) |
| **03 — Differential Privacy** | 24–45 | `:361` | two-worlds · **$(\varepsilon,\delta)$-DP definition** `:453` (plain-English lead-in) · budget $\varepsilon$ · $\varepsilon$ in the wild `:510` (Apple 4–8/item + audited 16/day, Census $\approx 17$) · $\delta \ll 1/n$ `:528` · post-processing · **indistinguishability + heights (SVG)** `:576` · what DP does/doesn't |
| **04 — Achieving DP: Add Randomness** | 46–58 | `:640` | **Randomized response + coin-tree (SVG)** `:688` · recover-the-rate worked example `:709` · local vs central DP · RAPPOR/Apple · **Laplace mechanism + noise bell (SVG)** `:758` · sensitivity |
| **05 — Private Machine Learning** | 59–70 | `:814` | **DP-SGD** `:843` (clip+noise merged to one slide) · privacy accountant · utility cost (benchmark folded in) · **federated learning (SVG)** `:913` · Gboard · FL still leaks · secure aggregation |
| **06 — Frontier 2025–26** | 71–80 | `:972` | private fine-tuning (Yu, Li 2022) `:980` · **VaultGemma DP pretraining** `:992` (added 2026-08) · private synthetic data + Apple Intelligence 2025 `:1006` · web-scale puzzle · privacy auditing · unlearning preview · Apple PCC · EU AI Act (GPAI duties since Aug 2025) `:1070` · open problems `:1082` |
| Wrap (deeper / demos / takeaways) | 81–83 | — | `:1096`–`:1122` |
| Closer | 84 | — | `$\varepsilon$` `:1135` |

**Key definitions / citations (all source-verified 2026-08):**
- $(\varepsilon,\delta)$-DP — `:453` — relaxation from Dwork, Kenthapadi, McSherry, Mironov,
  Naor, EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006). "A 2006 Idea" `:369`
  keeps Dwork, McSherry, Nissim, Smith, TCC 2006 for $\varepsilon$-DP — matches `courses/privacy/lectures/01-dp/`.
- **Statistical indistinguishability** (heights example, Korea/Japan Gaussians) — `:558-:631` —
  "Many Samples Break It" `:606` folds in the composition intuition; warm-up `:571` carries the coin-flip highlight.
- Randomized response — `:661` — Warner, JASA 1965.
- DP-SGD — `:843` — Abadi et al., ACM CCS 2016.
- De-anonymization — `:246` — Narayanan & Shmatikov, IEEE S&P 2008.
- Sweeney 87% (1990 census) — `:224` — Sweeney, Data Privacy WP3, 2000; Golle, WPES 2006 re-estimate (63%) added as caveat.
- $\varepsilon$ in the wild — `:510` — Apple "Learning with Privacy at Scale" 2017; Tang et al. 2017 audit; US Census 2020 ($\varepsilon \approx 17$).
- VaultGemma DP pretraining ($\varepsilon \le 2$, sequence-level) — `:992` — Google Research, 2025.

**Real images** (`figs/`, cropped + cited per GOTCHAS): GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini et al. 2021, Fig 1) `:116`; Stable-Diffusion copy `figs/calrini-ann.png` — **re-attributed
2026-08** to Carlini et al., "Extracting Training Data from Diffusion Models", USENIX Security 2023,
Fig 1 (Somepalli removed; verified against arXiv 2301.13188) `:162`. Duplication histogram
`figs/carlini_duplicates.png` moved to `lec04-memorization.html`. **SVG figures:** Sweeney linkage Venn
`:229`, MIA loss-overlap `:298`, height-distribution overlap `:576`, randomized-response coin tree `:688`,
Laplace noise bell `:758`, federated learning `:913`. Citations use `.cite-left`. Page number: bold
`.slide-num` only. Intuition pass — points to `courses/privacy/lectures/01-dp/` for rigor.

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

---

## lec03-mia.html

**Topic:** Membership inference attacks (~90 min). What "was this example in the
training set?" means and why it matters (privacy audit, litigation, extraction
pre-step); overfitting/loss-gap intuition; shadow models at picture level; LiRA as
"compare to a population of reference models"; evaluation done right (TPR at low FPR);
MIA on LLMs and diffusion models; DP-vs-MIA in one line; 2025–26 frontier (strong-attack
wall, dataset inference, courtroom use). Intuition pass — the rigorous treatment lives
in `courses/privacy/lectures/04-mia/` (5-deck series); facts kept consistent with it.

### Sections (63 slides, ~90 min — content-revised 2026-08 from 59, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:31`, `:43` | |
| **01 — The Question** | 3–11 | `:80` | one yes-or-no question `:88` · member vs non-member worlds `:113` · cancer-cohort harm `:126` · **Who Asks, and Why (audit / courts / extraction; added 2026-08)** `:148` · threat model `:161` · score + threshold `:175` |
| **02 — The Basic Attack** | 12–20 | `:189` | train loss < test loss `:197` · loss score `:206` · **two-bells overlap (SVG)** `:216` · overfitting drives MIA (caveat: small gap ≠ safe) `:238` · 3-line threshold attack `:247` · confidence baseline `:259` · Yeom theory anchor (sufficient, not necessary) `:272` · Colab demo `:284` |
| **03 — Shadow Models** | 21–26 | `:300` | shadow idea `:321` · **shadow pipeline (SVG)** `:333` · learned attack `:360` · why it transfers `:373` |
| **04 — Stronger Attacks** | 27–36 | `:387` | difficulty vs membership `:395` · per-example calibration `:408` · likelihood ratio `:417` · **LiRA** `:431` · **in-vs-out bells (SVG)** `:445` · label-only `:465` · average accuracy lies `:478` · **TPR at low FPR** (retitled 2026-08) `:487` · **ROC tail (SVG)** `:501` |
| **05 — What It Means** | 37–43 | `:522` | $(\varepsilon,\delta)$-DP recall `:530` · DP caps the attacker `:542` · TPR $\le e^{\varepsilon}\cdot$FPR$+\delta$ `:551` · empirical $\varepsilon$ auditing `:560` · trust but verify `:573` · canaries + one-run auditing `:587` |
| **06 — Modern Models** | 44–54 | `:602` | MIA meets foundation models `:610` · Min-K% `:623` · **diffusion duplication histogram (real fig)** `:636` · Duan web-scale doubt `:656` · why scale breaks it `:665` · benchmark trap (temporal confound, blind baselines) `:678` · **Give the Attack Everything (Hayes wall; added 2026-08)** `:692` · **dataset inference (added 2026-08)** `:706` · **MIA in the Courtroom (added 2026-08)** `:719` · open debate `:729` |
| **07 — Defenses** | 55–61 | `:744` | shrink the gap `:752` · heuristics not proof `:764` · DP-SGD `:777` · why DP-SGD stops MIA `:793` · utility cost `:806` · defender's checklist `:815` |
| Takeaways / Closer | 62–63 | — | `:829`, `:842` |

**Key definitions / citations (all source-verified 2026-08):**
- Shadow models — `:321` — Shokri, Stronati, Song, and Shmatikov, IEEE S&P 2017.
- Loss attack / advantage-vs-gap — `:206`, `:272` — Yeom, Giacomelli, Fredrikson, and Jha,
  "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting", IEEE CSF 2018
  (full title restored 2026-08). Overfitting **sufficient, not necessary** — matches
  `courses/privacy/lectures/04-mia/` (mia3).
- Confidence baseline — `:259` — Salem et al., "ML-Leaks", NDSS 2019 (re-attributed 2026-08;
  was wrongly cited to Shokri 2017).
- Likelihood-ratio framing — `:417` — Sablayrolles et al., ICML 2019.
- LiRA + TPR-at-low-FPR standard — `:431`, `:487` — Carlini et al., "Membership Inference
  Attacks From First Principles", IEEE S&P 2022.
- Label-only — `:465` — Choquette-Choo, Tramèr, Carlini, and Papernot, ICML 2021.
- $(\varepsilon,\delta)$-DP — `:530` — Dwork, Kenthapadi, McSherry, Mironov, and Naor,
  EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006 — same fix as lec02).
- One-run auditing — `:587` — Steinke, Nasr, and Jagielski, NeurIPS 2023.
- Min-K% — `:623` — Shi et al., ICLR 2024.
- Diffusion extraction/duplication — `:636` — Carlini et al., USENIX Security 2023, Fig. 5.
- Web-scale doubt — `:656` — Duan et al., COLM 2024.
- Blind baselines / temporal confound — `:678` — Das, Zhang, and Tramèr, DATA-FM at ICLR 2025
  (direction fixed 2026-08: members are the *older* text, non-members post-cutoff).
- Strong-attack wall — `:692` — Hayes, Shumailov, et al., NeurIPS 2025.
- Dataset inference — `:706` — Maini, Jia, Papernot, and Dziedzic, NeurIPS 2024.
- MIA-as-evidence position — `:719` — Zhang, Das, Kamath, and Tramèr, IEEE SaTML 2025.
- DP-SGD — `:777` — Abadi et al., ACM CCS 2016.

**Real image:** duplication histogram `figs/carlini_duplicates.png` (Carlini et al.,
"Extracting Training Data from Diffusion Models", USENIX Security 2023, Fig. 5 —
attribution verified against arXiv 2301.13188) `:642`; also used by `lec04-memorization.html`.
**SVG figures:** two-bells loss overlap `:216`, member/model/non-member world cards `:113`,
shadow pipeline `:333`, in-vs-out bells `:445`, ROC tail `:501`. Citations use `.cite-left`.
Page number: bold `.slide-num` only.

**2026-08 content revision (59→63):** every citation/number fetched and verified (deck is
nearly number-free; no invented results tables found). Added: "Who Asks, and Why" (§01);
"Give the Attack Everything" (Hayes 2025 strong-MIA wall), "Ask About a Dataset, Not a
Record" (Maini dataset inference), "MIA in the Courtroom" (Zhang SaTML 2025) to §06.
Fixed: benchmark-trap direction (members older, not newer); "precision at low FPR" →
"TPR at low FPR" (3 places); "zero gap ⇒ safe" folklore removed (sufficient-not-necessary);
$(\varepsilon,\delta)$-DP origin TCC→EUROCRYPT 2006; ML-Leaks attribution; Yeom full title.
`lec03tech.html` audited — math correct, no changes. Note file synced (63 entries, order matches).

---

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

### Sections (58 slides, ~90 min — content-revised 2026-08 from 59, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:40` | |
| **01 — What Is Memorization** | 3–15 | `:72` | working definition `:93` · three flavors (verbatim / near-duplicate / stylistic; retaxonomized 2026-08) `:104` · $k$-extractable `:117` · **Extractable vs Discoverable (added 2026-08)** `:130` · why it happens `:143` · **Some Memorization Is Necessary (Feldman long tail; added 2026-08)** `:156` · Secret Sharer `:170` · canary `:183` · **canary-leak pipeline (SVG)** `:195` · exposure-rank idea `:220` |
| **02 — Extracting Text from LLMs** | 16–26 | `:246` | **GPT-2 PII (real fig)** `:264` · **extraction pipeline (SVG; redrawn 2026-08 with 1,800/604 numbers)** `:284` · confidence signal `:315` · what came out (604 strings) `:328` · repeat-forever "poem poem poem" prompt (exact wording restored 2026-08) `:341` · **loop breaks (SVG)** `:353` · scale of the leak (10,000+ strings / $200 / 150×; added 2026-08) `:374` · patched-not-solved `:388` · Colab demo `:397` |
| **03 — How Much, and Why It Grows** | 27–34 | `:412` | measurable fraction `:421` · three drivers (size / duplication / **context** — third driver fixed 2026-08, was "training length") `:434` · **size curve (SVG)** `:447` · **duplication bars (SVG)** + Kandpal ~1000× line `:469` · long tail of duplicates `:492` · log-linear curve + GPT-J ≥1% (added 2026-08) `:505` |
| **04 — Image & Diffusion Models** | 35–41 | `:526` | not just text `:535` · diffusion picture `:548` · **Ann Graham Lotz copy (real fig; 94/175M added 2026-08)** `:561` · **duplication histogram (real fig; Somepalli cite removed 2026-08)** `:581` · Somepalli ~1.9% near-duplicates `:593` |
| **05 — Copyright & the Law** | 42–44 | `:614` | **compressed 6→2 slides 2026-08** (backup copyright deck owns the topic) · NYT v. OpenAI + **side-by-side SVG** + Mar 2025 MTD ruling `:623` · Copy or Transform? (fair-use collision + Bartz v. Anthropic $1.5B) `:647` |
| **06 — Mitigations & Frontier** | 45–56 | `:662` | toolbox `:671` · deduplication (Lee ACL 2022) `:684` · dedup limits `:697` · output filtering `:710` · DP `:722` · privacy tax `:734` · no silver bullet `:747` · **Frontier: Whole Books Come Back (Cooper 2025 + Ahmed 2026; replaced generic production-extraction slide)** `:755` · **Frontier: How Much Fits? (Morris 3.6 bits/param; added 2026-08)** `:768` · memorized PII `:781` · open problems `:794` |
| Takeaways / Closer | 57–58 | — | `:807`, `:819` |

**Key definitions / citations (all source-verified 2026-08):**
- $k$-extractable (Def 3.1), scaling drivers (capacity / duplication / context), GPT-J ≥1% —
  `:117`, `:434`, `:505` — Carlini et al., "Quantifying Memorization Across Neural Language
  Models", ICLR 2023 (arXiv 2202.07646).
- GPT-2 extraction, Fig 1 PII, 604 of 1,800 candidates — `:264`, `:284` — Carlini et al.,
  "Extracting Training Data from Large Language Models", USENIX Security 2021 (arXiv 2012.07805).
- Secret Sharer canary/exposure — `:170` — Carlini, Liu, Erlingsson, Kos, and Song,
  USENIX Security 2019 (arXiv 1802.08232).
- Extractable vs discoverable (Defs 1–2); poem attack; 10,000+ strings / $200 / 150× —
  `:130`, `:341`, `:374` — Nasr et al., "Scalable Extraction of Training Data from (Production)
  Language Models", arXiv 2311.17035 (2023; published at ICLR 2025 as "…from Aligned,
  Production Language Models").
- Learning requires memorization (long tail) — `:156` — Feldman, STOC 2020.
- Superlinear duplication effect (10 copies → ~1000× more generation) — `:469` — Kandpal,
  Wallace, and Raffel, ICML 2022 (arXiv 2202.06539).
- Deduplication (10× less memorized text) — `:684` — Lee et al., "Deduplicating Training Data
  Makes Language Models Better", ACL 2022 (arXiv 2107.06499).
- Diffusion extraction: Ann Graham Lotz Fig 1, 94 images / 175M generations, Fig 5 duplication
  histogram (most extracted ≥100 dupes) — `:561`, `:581` — Carlini et al., "Extracting Training
  Data from Diffusion Models", USENIX Security 2023 (arXiv 2301.13188).
- ~1.9% near-duplicate generations — `:593` — Somepalli et al., "Diffusion Art or Digital
  Forgery?", CVPR 2023 (arXiv 2212.03860; paper reports 1.88% at similarity >0.5).
- NYT v. OpenAI — `:623` — S.D.N.Y., filed Dec 2023; motion to dismiss largely denied
  Mar 26, 2025 (opinion Apr 4, 2025).
- Bartz v. Anthropic $1.5B settlement — `:647` — N.D. Cal.; preliminary approval Sept 25, 2025
  (matches `courses/privacy/lectures/03-memorization/` anchor).
- Whole-book extraction — `:755` — Cooper et al., arXiv 2505.12546 (Llama 3.1 70B / Harry
  Potter); Ahmed, Cooper, Koyejo, and Liang, "Extracting books from production language
  models", arXiv 2601.02671 (2026).
- Capacity ≈3.6 bits/parameter — `:768` — Morris et al., "How Much Do Language Models
  Memorize?", arXiv 2505.24832 (2025).

**Real images** (`figs/`, cropped + cited): GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini 2021 Fig 1) `:268`; Ann Graham Lotz copy `figs/calrini-ann.png` (Carlini USENIX Sec
2023 Fig 1) `:565`; duplication histogram `figs/carlini_duplicates.png` (Carlini USENIX Sec
2023 Fig 5; shared with `lec03-mia.html`) `:585`. **SVG figures:** canary-leak pipeline `:195`,
extraction pipeline `:284`, poem loop-break `:353`, size curve `:447`, duplication bars `:469`,
diffusion noise→image strip `:548`, NYT side-by-side `:623`. Citations use `.cite-left`.
Page number: bold `.slide-num` only.

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

---

## lec05-unlearning.html

**Topic:** Machine unlearning (~90 min). Why deletion is demanded (GDPR/CCPA privacy,
copyright, safety); retraining as the gold standard; exact vs approximate; the
$(\varepsilon,\delta)$ yardstick at intuition level; SISA as a picture; influence
functions and the Hessian wall; gradient ascent, its failure modes, and NPO;
LLM unlearning (Harry Potter, TOFU, WMDP/RMU, MUSE); verification (MIA audit, IDI,
relearning, quantization recovery); the position-paper debate and the 2025–26
frontier. Intuition pass — the rigorous treatment lives in
`courses/privacy/lectures/05-unlearning/` (authoritative for shared facts); the
position-paper debate expands in `talks/icml2026/`.

### Sections (66 slides, ~90 min — content-revised 2026-08 from 58, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:31`, `:43` | |
| **01 — Why Delete?** | 3–11 | `:76` | user changes mind `:84` · GDPR Art. 17 `:97` · **Delete for Three Reasons (privacy / copyright / safety; added 2026-08)** `:110` · **data lives in the weights (SVG)** `:123` · why not ignore `:148` · retraining expensive `:161` · enter machine unlearning (Cao & Yang) `:174` · a decade of work `:186` |
| **02 — What Unlearning Means** | 12–19 | `:200` | gold standard = retrain `:208` · **two-models diagram (SVG)** `:220` · exact `:246` · approximate `:259` · **DP yardstick (Guo/Sekhari cite fixed 2026-08)** `:272` · forget/retain split `:286` · two things to get right `:300` |
| **03 — How to Unlearn** | 20–34 | `:313` | retraining baseline `:321` · train in pieces `:334` · **SISA (SVG)** `:347` · deleting in SISA `:381` · slices `:394` · tradeoff `:407` · edit the weights `:420` · influence functions `:433` · Hessian catch `:447` · gradient ascent `:460` · ascent wrecks `:474` · **A Gentler Push: NPO (real fig; added 2026-08)** `:487` · method landscape `:499` · Colab `:511` |
| **04 — Unlearning in LLMs** | 35–46 | `:527` | what do we forget `:535` · no single row `:548` · Harry Potter (+1 GPU hour) `:561` · the result `:575` · **TOFU (200×20=4,000; numbers verified 2026-08)** `:588` · **TOFU in One Picture (real fig; added 2026-08)** `:601` · why fictitious `:612` · **WMDP (real fig + 3,668 MCQs; reworked 2026-08)** `:625` · RMU `:645` · **MUSE: Six Boxes to Tick (real fig; added 2026-08)** `:658` · unlearning vs filtering `:670` |
| **05 — Did It Really Forget?** | 47–55 | `:685` | verification is hard `:693` · MIA audit `:706` · **the tell persists (SVG)** `:719` · **Look Inside: IDI (real fig, Yonsei; added 2026-08)** `:739` · relearning attacks `:751` · **Relearning, Measured (real fig; added 2026-08)** `:764` · **Quantize, and It Comes Back (21%→83%; added 2026-08)** `:776` · dormant, not deleted `:790` |
| **06 — Frontier 2025–26** | 56–64 | `:799` | **"overused" critique (+Yoon/Jun/No cite added 2026-08)** `:807` · **Does It Do What You Think? (position papers; added 2026-08)** `:821` · what guarantee holds `:834` · **robust unlearning (+Łucki 10-example fact)** `:847` · evaluation standards (TOFU/WMDP/MUSE) `:861` · unlearning meets privacy `:874` · open problems `:888` · where to go deeper `:902` |
| Takeaways / Closer | 65–66 | — | `:913`, `:926` |

**Key definitions / citations (all source-verified 2026-08):**
- First "machine unlearning" — `:174` — Cao and Yang, IEEE S&P 2015.
- Exact deletion definition — `:186` — Ginart, Guan, Valiant, and Zou, NeurIPS 2019
  (arXiv 1907.05012). **No longer cited for the $(\varepsilon,\delta)$ definition** —
  that was a misattribution, fixed 2026-08 on `:272` and in `lec05tech.html`.
- $(\varepsilon,\delta)$-unlearning — `:272` — Guo, Goldstein, Hannun, and van der Maaten,
  "Certified Data Removal from Machine Learning Models", ICML 2020 (arXiv 1911.03030);
  Sekhari et al., NeurIPS 2021. Matches privacy deck Def 3.
- SISA — `:347` — Bourtoule et al., "Machine Unlearning", IEEE S&P 2021. Speedup:
  sharding cuts expected cost by the shard count; slicing saves at most another 3/2
  (matches privacy deck Prop 3; tech deck's "R·L" claim fixed 2026-08).
- Influence functions — `:433` — Koh and Liang, ICML 2017.
- Gradient ascent / unrolling — `:460` — Thudi et al., "Unrolling SGD", IEEE EuroS&P 2022.
- NPO — `:487` — Zhang, Lin, Bai, and Mei, "Negative Preference Optimization", COLM 2024.
- Who's Harry Potter (~1 GPU hour, Llama-2-7b) — `:561` — Eldan and Russinovich, 2023
  (arXiv 2310.02238).
- TOFU (200 authors × 20 QA = 4,000) — `:588` — Maini, Feng, Schwarzschild, Lipton,
  and Kolter, COLM 2024 (arXiv 2401.06121).
- WMDP (3,668 MCQs) + RMU — `:625`, `:645` — Li et al., ICML 2024 (arXiv 2403.03218).
- MUSE (six criteria) — `:658` — Shi, Wang, Li, et al., ICLR 2025 (arXiv 2407.06460).
- IDI (instructor co-author) — `:739` — Jeon, Jeung, Kim, No, and Choi (Yonsei),
  "An Information Theoretic Evaluation Metric For Strong Unlearning", AAAI 2026
  (arXiv 2405.17878).
- Benign relearning — `:764` — Hu, Fu, Wu, and Smith, "Unlearning or Obfuscating?",
  ICLR 2025 (arXiv 2406.13356).
- Quantization recovery (21%→83% after 4-bit) — `:776` — Zhang et al., "Catastrophic
  Failure of LLM Unlearning via Quantization", ICLR 2025 (arXiv 2410.16454).
- Adversarial perspective (10 unrelated examples undo RMU) — `:847` — Łucki et al.,
  TMLR 2025 (arXiv 2409.18025).
- Position papers — `:807`, `:821` — Cooper et al., "Machine Unlearning Doesn't Do What
  You Think", NeurIPS 2025; Yoon, Jun, and No (Yonsei), "Position: 'Machine Unlearning'
  Is Overused in LLMs", ICML 2026 (matches `courses/privacy/lectures/05-unlearning/`
  and `talks/icml2026/`).

**Real images** (`figs/`, cropped + cited, all copied from
`courses/privacy/lectures/05-unlearning/figs/`): NPO vs GA collapse curves
`figs/npo-ga-collapse.png` (Zhang COLM 2024 Fig 2) `:487`; TOFU pipeline
`figs/tofu.png` (Maini COLM 2024 Fig 1) `:601`; WMDP overview `figs/WMDP.png`
(Li ICML 2024 Fig 1) `:625`; MUSE six-way evaluation `figs/MUSE.png` (Shi ICLR 2025
Fig 1) `:658`; IDI conceptual layer plot `figs/idi-conceptual.png` (Jeon AAAI 2026
Fig 4(a)) `:739`; benign-relearning pipeline `figs/benign-relearn-pipeline.png`
(Hu ICLR 2025 Fig 2 left) `:764`. **SVG figures:** data-in-weights `:123`,
two-models-compared `:220`, SISA shard diagram `:347`, member/non-member bells `:719`.
Citations use `.cite-left`. Page number: bold `.slide-num` only.

**2026-08 content revision (58→66):** every citation/number fetched and verified.
Added 8 slides: Delete for Three Reasons (§01), A Gentler Push: NPO (§03), TOFU in
One Picture + MUSE: Six Boxes to Tick (§04), Look Inside: IDI + Relearning, Measured +
Quantize, and It Comes Back (§05), Does It Do What You Think? (§06). Fixed:
$(\varepsilon,\delta)$-unlearning misattributed to Ginart 2019 → Guo ICML 2020 +
Sekhari 2021 (main `:272` and `lec05tech.html` slide 4, which also gained the
two-sided-bound clause); `lec05tech.html` SISA speedup "R·L" → shard-count + 3/2
(fix-errors-only pass, deck stays 11 sl). WMDP slide reworked around the real figure;
concrete verified numbers added (4,000 QA; 3,668 MCQs; 21%→83%; 10 examples;
~1 GPU hour). Note file synced (66 entries, order matches).

## lec06-hallucination.html

**Topic:** Hallucination, calibration & reliability (~90 min). What hallucination is
(and is not); why next-token training produces confident falsehoods (Kalai binary-grading
argument at intuition level); real harms (Lacey v. State Farm as anchor case — Mata v.
Avianca lives in lec01, one-line callback only); calibration with the reliability-diagram
picture and a glanceable ECE; conformal prediction as "sets with a coverage promise";
semantic entropy at intuition level; RAG grounding; benchmarks (TruthfulQA, Vectara HHEM);
reasoning-model hallucination; sycophancy one-slide touchpoint (full treatment in
`backup-sycophancy.html`). Math lives in `lec06tech.html`.

### Sections (61 slides, ~90 min — content-revised 2026-08 from 58, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:26`, `:38` | |
| **01 — What Hallucination Is** | 3–10 | `:71` | definition (Ji survey) `:79` · fluency fools us `:91` · **Fake Citations, Again (Lacey v. State Farm, $31,100; new anchor 2026-08)** `:104` · **Invented Medical Facts (Med-Gemini "basilar ganglia"; rewritten 2026-08)** `:119` · two flavors of wrong `:133` · not the same as a bug `:146` · why this matters `:158` |
| **02 — Why Models Hallucinate** | 11–19 | `:171` | training objective `:179` · no truth grounding `:188` · plausible beats true `:201` · pressure to always answer (+Kalai cite) `:223` · exam-taking analogy (+Kalai cite) `:237` · **Guessing, Measured (SimpleQA wrong/abstain SVG bars; added 2026-08)** `:251` · where errors concentrate `:279` · knowledge cutoff `:292` |
| **03 — Calibration** | 20–31 | `:305` | confidence as a number `:313` · calibration promise `:322` · reliability diagram (SVG) `:334` · over- vs under-confident `:356` · measuring the gap (ECE, Guo) `:369` · reading ECE `:383` · bigger is not better `:395` · temperature `:408` · Kadavath self-knowledge `:422` · verbalized confidence (+Xiong ICLR 2024 cite added 2026-08) `:435` · Colab `:449` |
| **04 — Conformal Prediction** | 32–40 | `:465` | one answer to a set `:473` · coverage guarantee `:486` · distribution-free `:498` · how it works `:511` · prediction-set picture (SVG) `:524` · abstention `:547` · medical triage `:560` · trade-off `:573` |
| **05 — Detection & Grounding** | 41–51 | `:582` | two strategies `:590` · self-consistency (+SelfCheckGPT cite added 2026-08) `:603` · semantic entropy (Farquhar) `:617` · entropy picture (SVG) `:630` · RAG `:655` · why RAG helps `:668` · RAG is not a cure `:681` · teaching "I don't know" `:694` · scoring rule (+Kalai cite) `:707` · detection Colab `:717` |
| **06 — Frontier 2025–26** | 52–59 | `:733` | **TruthfulQA (817 Qs, 58% vs 94%; added 2026-08)** `:741` · benchmarks + Vectara HHEM chart (SVG) `:755` · **Reasoning Models Hallucinate Too (o3 33% / o4-mini 48% / o1 16% PersonQA; reworked 2026-08)** `:794` · **Sycophancy touchpoint (real fig; added 2026-08)** `:808` · factuality evaluations `:820` · open problems `:833` · demos `:847` |
| Takeaways / Closer | 60–61 | — | `:862`, `:876` |

**Key definitions / citations (all source-verified 2026-08):**
- Hallucination survey — `:79` — Ji et al., ACM Computing Surveys 2023.
- Anchor case — `:104` — Special Master sanctions order, Lacey v. State Farm,
  C.D. Cal., May 2025 ($31,100; ~1/3 of citations flawed; two cited cases nonexistent).
  Avianca callback only (lec01 owns that case).
- Med-Gemini "basilar ganglia" — `:119` — Google Med-Gemini paper 2024; error surfaced
  by The Verge, 2025 (verified via secondary reports).
- Why LMs hallucinate (binary grading rewards guessing) — `:223`, `:237`, `:707` —
  Kalai, Nachum, Vempala, and Zhang, 2025 (arXiv 2509.04664).
- SimpleQA wrong/abstain rates (o4-mini 75%/1% vs gpt-5-thinking-mini 26%/52%) —
  `:251` — OpenAI "Why language models hallucinate" blog, 2025 (table is in the blog,
  not the arXiv paper; verified via secondary coverage — openai.com blocks fetch).
- Calibration / ECE / temperature — `:369`–`:419` — Guo, Pleiss, Sun, and Weinberger,
  ICML 2017.
- Self-knowledge — `:422` — Kadavath et al., "Language Models (Mostly) Know What They
  Know", 2022.
- Verbalized confidence — `:435` — Xiong et al., ICLR 2024 (arXiv 2306.13063).
- Conformal — `:486`, `:495`, `:521` — Angelopoulos and Bates, "A Gentle Introduction to
  Conformal Prediction and Distribution-Free Uncertainty Quantification", 2021
  (arXiv 2107.07511; title completed 2026-08 here and in `lec06tech.html`).
- Self-consistency — `:603` — Manakul, Liusie, and Gales, "SelfCheckGPT", EMNLP 2023.
- Semantic entropy — `:617` — Farquhar et al., Nature 630, 625–630 (2024).
- RAG — `:655` — Lewis et al., NeurIPS 2020.
- TruthfulQA (817 Qs, 38 categories, best model 58% vs humans 94%, larger = less
  truthful) — `:741` — Lin, Hilton, and Evans, ACL 2022 (arXiv 2109.07958).
- Vectara HHEM summarization hallucination rates — `:755` — leaderboard README,
  May 2026 (chart data verified against the repo).
- Reasoning-model rates (o3 33%, o4-mini 48%, o1 16% on PersonQA) — `:794` —
  OpenAI o3/o4-mini System Card, April 2025.
- Sycophancy — `:808` — Sharma et al., ICLR 2024 (Figure 5); GPT-4o rollback quote
  "overly flattering or agreeable" — OpenAI "Sycophancy in GPT-4o", 2025.

**Figures:** real image `figs/sharma-sycophancy.png` (Sharma ICLR 2024 Fig 5, shared
with `backup-sycophancy.html`) `:808`. **SVG:** SimpleQA wrong/abstain bars `:251`,
reliability diagram `:334`, prediction-set threshold picture `:524`, entropy clusters
`:630`, RAG pipeline `:655`, Vectara HHEM bar chart `:755`. Citations use `.cite-left`.

**2026-08 content revision (58→61):** every citation/number fetched and verified.
Added 3 slides: Guessing, Measured (§02); TruthfulQA (§06); Sycophancy touchpoint (§06).
Replaced the fake-citation anchor (Avianca → Lacey v. State Farm; Avianca kept as a
one-line callback since lec01 covers it) and rewrote Invented Medical Facts around the
verified Med-Gemini error. Reworked Reasoning Models around verified PersonQA numbers.
Added missing cites (Kalai ×3, Xiong, SelfCheckGPT); completed the Angelopoulos & Bates
title (also in `lec06tech.html` — otherwise fix-errors-only, math verified, stays 14 sl).
Flagged as secondary-verified: Lacey "hundreds of filings" tracker line `:115`, SimpleQA
abstention split `:251`, Med-Gemini narrative `:119`, GPT-4o rollback line `:816`.
Note file synced (61 entries, order matches).
