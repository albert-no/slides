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
