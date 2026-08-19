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
| 7 | `lec07-interpretability.html` | Interpretability & explainability | **revised 2026-08** (64 sl) |
| 8 | `lec08-adversarial.html` | Adversarial examples (attack + defense) | **revised 2026-08** (63 sl) |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **revised 2026-08** (61 sl) |
| 10 | `lec10-jailbreak.html` | Jailbreaks & LLM safety | **revised 2026-08** (57 sl) |
| 11 | `lec11-prompt-injection.html` | Prompt injection & agentic safety | **revised 2026-08** (63 sl) |
| 12 | `lec12-watermark.html` | Watermarking, deepfakes & provenance | **revised 2026-08** (64 sl) |
| 13 | `lec13-fairness-defs.html` | Fairness I — definitions & impossibility | **revised 2026-08** (58 sl) |
| 14 | `lec14-fairness-mitigation.html` | Fairness II — mitigation & accountability | **revised 2026-08** (61 sl) |
| 15 | `lec15-governance.html` | Governance, frontier & demo showcase | **revised 2026-08** (66 sl) |

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
| `lec07tech.html` | Wk 7 (interpretability) | Shapley φ_i + axioms; LIME surrogate objective; gradient saliency; integrated gradients; SAE reconstruction+sparsity, superposition | **checked 2026-08** (20 sl: math verified, no changes needed) |
| `lec08tech.html` | Wk 8 (adversarial) | perturbation set B_p(x,ε); FGSM; PGD projected iteration; adversarial-training min-max; randomized-smoothing certified radius | **checked 2026-08** (19 sl: math verified incl. Cohen Thm 1 radius, no changes needed) |
| `lec09tech.html` | Wk 9 (poisoning) | poison fraction α; clean-label feature-collision objective; backdoor blended objective; spectral signatures; activation clustering | **checked 2026-08** (16 sl: math verified incl. Poison Frogs ℓ∞ form; blended-objective cite reworded, not verbatim BadNets) |
| `lec10tech.html` | Wk 10 (jailbreak) | RLHF KL-penalized objective; GCG target `min -log Pr["Sure, here"]`; gradient-guided token swaps | **checked 2026-08** (12 sl: RLHF KL objective + GCG target verified correct, no changes) |
| `lec11tech.html` | Wk 11 (prompt injection) | data-vs-control plane; confused deputy; agent threat model; capabilities/least privilege; taint tracking; dual-LLM pattern (security model, not equations) | **checked 2026-08** (9 sl: security model verified — dual-LLM matches Willison 2023, CaMeL cite correct; two prose-dash lint warnings fixed) |
| `lec12tech.html` | Wk 12 (watermark) | green-list logit bias; null Binomial(T,γ); detection z = (|s|_G−γT)/√(Tγ(1−γ)); false-positive bound; z ∝ √T; robustness–quality tradeoff | **checked 2026-08** (10 sl: FP rate at τ=4 fixed "&lt;" → "≈ 3×10⁻⁵" per KGW; no Thm 4.3 stated — consistent with the corrected math in `courses/privacy/lectures/06-watermark/`) |
| `lec13tech.html` | Wk 13 (fairness defs) | demographic parity / equalized odds / calibration as conditional-prob defs; base rates; impossibility theorem (Chouldechova/Kleinberg) + proof sketch | **fixed 2026-08** (15 sl: base-rate identity was inverted (1−p)/p → p/(1−p) per Chouldechova eq 2.6; proof-sketch step 1 corrected (calibration ≠ "PPV = base rate" → predictive parity demands equal PPV across groups); unverifiable numeric-wedge table replaced with an exactly derivable two-value-score construction; impossibility attribution now dual Chouldechova + Kleinberg) |
| `lec14tech.html` | Wk 14 (fairness mitigation) | reweighing w(g,y); penalized min Loss+λ·Unfairness; constrained form; reductions (Agarwal 2018); post-processing per-group thresholds (Hardt 2016) | **checked 2026-08** (17 sl: reweighing formula verified against Kamiran & Calders; reductions + Hardt ROC intuition verified against papers; one fix — cite venue "KIS 2012" → "Knowledge and Information Systems 2012") |
| `lec15tech.html` | Wk 15 (governance) | EU AI Act risk-tier taxonomy; NIST RMF as Govern→Map→Measure→Manage loop; what "measurable" audit metrics mean (deliberately light — governance is non-mathematical) | **checked 2026-08** (6 sl: tiers verified still accurate post-Omnibus; EU cite normalized; tier bullets de-dashed for lint) |

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
- `lec10` Wei failure modes (`figs/wei-jailbroken.png`, NeurIPS 2023 Fig 1), GCG schematic (`figs/gcg-schematic.png`, Zou 2023 Fig 1 — replaced SVG), many-shot power-law (`figs/msj-powerlaw.png`, Anil et al. NeurIPS 2024 **Fig 1** — attribution corrected from Fig 2, 2026-08).
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

**2026-08 note enrichment:** `lec01-introduction-note.html` upgraded from speaker
script to **script + companion notes** (227→443 lines; 35 entries unchanged).
Per-entry `.detail` blocks add formal definitions (threat-model tuple, ε-ball/FGSM,
(ε,δ)-DP, ECE, equalized odds, watermark z-test, extractable/k-eidetic memorization)
and verified backgrounds with primary-source links for every incident (Mata v. Avianca
sanctions order PDF, Deloitte/DEWR refund, ProPublica COMPAS, Reuters Amazon, Moffatt
v. Air Canada CRT decision, $1 Tahoe chatbot, Carlini/Nasr extraction, FCC robocall
orders + Kramer acquittal, EchoLeak NVD/MSRC, Goodfellow ICLR 2015).

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
**2026-08 note enrichment:** `lec03-mia-note.html` upgraded from speaker script (395 lines) to Script &amp; Companion Notes (831 lines): per-entry `.detail` blocks with rigorous definitions (MI game, TV, NP/LiRA statistics, (ε,δ)-DP, DP-SGD, Min-K%), full proofs (Yeom Thm 2, NP lemma, LiRA quadratic + z-test corollary, DP hypothesis-testing bound + corollaries, shadow-model Prop/Thm/Cor, benchmark-trap Prop, post-processing), and 19 verified links — all consistent with `courses/privacy/lectures/04-mia/`.

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

## lec07-interpretability.html

**Topic:** Interpretability & explainability (~90 min). Why black-box accuracy alone
does not earn trust; intrinsic vs post-hoc taxonomy plus the Rudin objection; feature
attribution at intuition level (LIME local surrogate, SHAP/Shapley fair credit, gradient
saliency, integrated gradients, Adebayo sanity-check failures); probing and the
attention-is-(not-(not-))explanation debate; mechanistic interpretability (circuits,
induction heads, superposition); sparse autoencoders, monosemantic features, Golden Gate
Claude, feature steering; uses & limits (GDPR / "right to explanation" nuance,
faithfulness, 2025–26 frontier: attribution graphs, CoT faithfulness, Amodei essay).
Math lives in `lec07tech.html`.

### Sections (64 slides, ~90 min — content-revised 2026-08 from 57, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — The Black Box** | 3–10 | `:72` | black box `:80` · why open it up `:93` · **Husky and the Wolf (reframed 2026-08: rigged demo, trust 10/27→3/27)** `:106` · intrinsic vs post-hoc `:120` · accuracy trade-off (SVG) `:133` · **The Rudin Objection (added 2026-08)** `:156` · explanation is not the model `:170` |
| **02 — Feature Attribution** | 11–25 | `:179` | attribution question `:187` · bar chart (SVG) `:199` · LIME `:222` · local-not-global (SVG) `:235` · SHAP `:252` · Shapley value `:265` · why trusted `:279` · loan demo `:292` · saliency on images (SVG) `:307` · gradient saliency `:327` · **Beyond Raw Gradients (IG; added 2026-08)** `:340` · saliency Colab `:354` · what attribution answers `:369` · Adebayo sanity check `:381` |
| **03 — Probing & Attention** | 26–33 | `:391` | hidden layers `:399` · linear probes `:412` · reading the probe `:424` · attention weights (SVG) `:437` · looks like explanation `:461` · not explanation (Jain & Wallace) `:474` · **...Is Not Not Explanation (added 2026-08)** `:483` |
| **04 — Mechanistic Interpretability** | 34–43 | `:498` | different goal `:506` · circuits (SVG) `:518` · neurons as concepts `:545` · transformer framework `:559` · induction heads `:572` · induction in action `:585` · why induction matters (+Olsson cite added 2026-08) `:602` · polysemantic wall `:616` · superposition (+Elhage cite added 2026-08) `:625` |
| **05 — Sparse Autoencoders & Steering** | 44–52 | `:640` | unpacking superposition `:648` · SAE (SVG) `:661` · monosemantic features `:685` · **Scaling Up (Claude 3 Sonnet; verified examples 2026-08)** `:699` · feature steering (SVG) `:712` · Golden Gate Claude `:731` · steering widget `:745` · **Steering for Safety (hedged + cited 2026-08)** `:760` |
| **06 — Uses & Limits** | 53–63 | `:775` | what it buys us `:783` · **What the Law Demands (GDPR Art. 22 / Arts. 13–15; added 2026-08)** `:794` · **A "Right to Explanation"? (added 2026-08)** `:808` · faithfulness problem `:822` · models can rationalize `:831` · always sanity-check `:844` · **Frontier: Attribution Graphs (added 2026-08)** `:857` · **Frontier: CoT faithfulness (added 2026-08)** `:871` · **Frontier: An MRI for AI (added 2026-08)** `:881` · key takeaways `:895` |
| Closer | 64 | — | `:908` |

**Key definitions / citations (all source-verified 2026-08):**
- LIME + husky/wolf experiment (rigged snow demo; trust 10/27→3/27) — `:116`, `:231` —
  Ribeiro, Singh, and Guestrin, "Why Should I Trust You?", KDD 2016 (§6.4, Table 2).
- Interpretable-by-design for high stakes — `:166` — Rudin, Nature Machine
  Intelligence 1, 206–215 (2019).
- SHAP / Shapley uniqueness — `:261`, `:275` — Lundberg and Lee, NeurIPS 2017.
- Integrated gradients — `:350` — Sundararajan, Taly, and Yan, ICML 2017.
- Saliency sanity checks (weight randomization) — `:386` — Adebayo et al., NeurIPS 2018.
- Attention debate — `:479` Jain and Wallace, NAACL 2019; `:493` Wiegreffe and Pinter,
  EMNLP 2019.
- Circuits / curve & dog-head detectors — `:541`, `:555` — Olah et al., "Zoom In",
  Distill 2020.
- Transformer framework + induction heads — `:568`, `:581` — Elhage et al., Anthropic 2021.
- Induction heads ↔ in-context learning — `:612` — Olsson et al., Anthropic 2022.
- Superposition — `:635` — Elhage et al., "Toy Models of Superposition", Anthropic 2022.
- SAE / monosemantic features (DNA, legal language, base64) — `:681`, `:695` —
  Bricken et al., "Towards Monosemanticity", Anthropic 2023.
- Millions of features in Claude 3 Sonnet; Golden Gate Claude; safety-relevant
  features — `:708`–`:770` — Templeton et al., "Scaling Monosemanticity", Anthropic 2024.
- GDPR Art. 22 + Arts. 13–15; recital-only "right to explanation"; EU AI Act Art. 86 —
  `:794`–`:818` — Wachter, Mittelstadt, and Floridi, International Data Privacy Law
  7(2):76–99 (2017); AI Act text (Art. 86, applies from Aug 2026).
- Attribution graphs (Dallas→Texas→Austin; rhyme planning; Neuronpedia) — `:867` —
  Lindsey et al., "On the Biology of a Large Language Model", Anthropic 2025;
  circuit-tracing tools open-sourced May 2025.
- CoT faithfulness (hint admitted <20% of the time) — `:877` — Chen et al., "Reasoning
  Models Don't Always Say What They Think", Anthropic 2025 (arXiv 2505.05410).
- "MRI for AI"; detect most model problems by 2027 — `:891` — Amodei, "The Urgency of
  Interpretability", April 2025.

**Figures:** all inline SVG (no real paper figures): accuracy trade-off `:138`,
attribution bar chart `:204`, LIME local-line `:240`, saliency heat-map pair `:312`,
attention lines `:442`, circuit graph `:523`, SAE widen-rebuild `:666`, steering
dial `:717`. Citations use `.cite-left`. Page number: bold `.slide-num` only.

**2026-08 content revision (57→64):** every citation/number fetched and verified.
Added 8 slides: The Rudin Objection (§01), Beyond Raw Gradients (§02), ...Is Not Not
Explanation (§03), What the Law Demands + A "Right to Explanation"? (§06), and three
frontier slides (§06: Attribution Graphs, CoT faithfulness, An MRI for AI — replacing
one stale unverifiable "Frontier 2025–26" slide). Fixed: husky/wolf reframed as the
deliberately rigged demo it was, with verified trust numbers; unverified "emotions"
feature example replaced by verified "scam emails" (Templeton 2024); Steering for
Safety hedged ("could", "still early days") and cited; missing Olsson and Elhage
(superposition) cites added. `lec07tech.html` audited: all math correct, no changes
(stays 20 sl). Note file synced (64 entries, order matches).

## lec08-adversarial.html

**Topic:** Adversarial examples — attack and defense (~90 min). Panda→gibbon
phenomenon and why it exists (linearity, features-not-bugs, intuition only); threat
model (budget ε, L∞/L2, white/black box, transferability + Papernot commercial-API
numbers); attacks as pictures (FGSM one step, PGD iterate, C&W, targeted vs
untargeted); defenses (adversarial training, robustness–accuracy tradeoff, certified
robustness / randomized smoothing at voting-intuition level); the arms race
(obfuscated gradients, Athalye 9/7/6+1, adaptive attacks, RobustBench scoreboard);
physical & beyond (stop sign, glasses, patches, audio, multimodal jailbreak images,
distribution shift / ImageNet-C touchpoint, NIST AI 100-2 frontier). Math lives in
`lec08tech.html`.

### Sections (63 slides, ~90 min — content-revised 2026-08 from 56, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — The Phenomenon** | 3–13 | `:77` | **panda→gibbon (99.3%, verified Fig 1) ** `:98` · anatomy (57.7%→99.3%, fixed 2026-08) `:110` · Intriguing Properties `:123` · boundary picture (SVG) `:156` · close to the edge `:178` · **Why? Too Linear Inside (added 2026-08)** `:190` · **Why? Features, Not Bugs (added 2026-08)** `:204` |
| **02 — The Threat Model** | 14–21 | `:219` | budget ‖δ‖≤ε `:240` · L∞ vs L2 `:253` · allowed region (SVG) `:267` · white vs black box `:286` · transferability `:299` · **Why Transfer Is Scary (Amazon 96% / Google 89%, ~800 queries; verified 2026-08)** `:312` |
| **03 — The Attacks** | 22–32 | `:326` | core idea `:334` · gradient sign `:343` · FGSM `:356` · FGSM by hand `:370` · PGD `:395` · steps in ball (SVG) `:409` · PGD benchmark `:432` · C&W `:445` · targeted vs untargeted `:457` |
| **04 — The Defenses** | 33–44 | `:471` | defender's goal `:479` · radius (SVG) `:491` · adversarial training `:511` · it works `:526` · the cost `:538` · **Robustness vs Accuracy (Tsipras; added 2026-08)** `:551` · empirical vs certified `:565` · certified robustness `:578` · randomized smoothing `:590` · why voting certifies `:603` · certified catch `:615` |
| **05 — The Arms Race** | 45–51 | `:629` | recurring story `:637` · obfuscated gradients `:650` · **A False Sense of Security (fixed 2026-08: 9 defenses, 7 obfuscated, 6 broken + 1 partial)** `:662` · adaptive attacks `:674` · how to test honestly `:687` · **The Scoreboard: RobustBench (added 2026-08)** `:700` |
| **06 — Physical & Beyond** | 52–61 | `:715` | off the screen `:723` · **stop sign (Speed Limit 45; 100% lab / 84.8% drive-by; verified 2026-08)** `:735` · **Adversarial Glasses (added 2026-08)** `:755` · adversarial patches (+Thys cite) `:769` · beyond vision (C&W audio 99.9%) `:783` · **Attacking Multimodal Models (Qi AAAI 2024; rewritten 2026-08)** `:796` · **Related: The World Also Shifts (added 2026-08)** `:810` · **ImageNet-C (added 2026-08)** `:824` · **2025-26 Frontier (NIST AI 100-2; rewritten 2026-08)** `:838` |
| Takeaways / Closer | 62–63 | — | key takeaways `:851` · closer `:864` |

**Key definitions / citations (all source-verified 2026-08):**
- Panda→gibbon (57.7% panda → 99.3% gibbon, ε=.007) + linearity explanation — `:106`,
  `:201` — Goodfellow, Shlens, and Szegedy, "Explaining and Harnessing Adversarial
  Examples", ICLR 2015 (Figure 1; "the primary cause ... is their linear nature").
- Intriguing properties + transfer — `:131` — Szegedy et al., ICLR 2014.
- Features-not-bugs — `:215` — Ilyas et al., NeurIPS 2019.
- Black-box transfer to commercial APIs (Amazon 96%, Google 89%, ~800 queries) —
  `:322` — Papernot, McDaniel, and Goodfellow, arXiv 2016.
- PGD + adversarial training — `:404`, `:522` — Madry et al., ICLR 2018.
- C&W attack — `:453` — Carlini and Wagner, IEEE S&P 2017.
- Robustness–accuracy tradeoff — `:561` — Tsipras et al., "Robustness May Be at Odds
  with Accuracy", ICLR 2019.
- Randomized smoothing certificate — `:599` — Cohen, Rosenfeld, and Kolter, ICML 2019.
- Obfuscated gradients (9 ICLR-2018 defenses examined, 7 obfuscated, 6 fully +
  1 partially broken) — `:659`, `:662` — Athalye, Carlini, and Wagner, ICML 2018.
- RobustBench (CIFAR-10 L∞ 8/255: standard 94.8/0.0, best 93.7/73.7, AutoAttack) —
  `:711` — robustbench.github.io, accessed Aug 2026.
- Stop-sign attack (target "Speed Limit 45"; 100% lab, 84.8% drive-by, LISA-CNN) —
  `:751` — Eykholt et al., CVPR 2018 (Figure 1; abstract).
- Adversarial glasses (dodge 80%+, impersonate 87.9%) — `:765` — Sharif, Bhagavatula,
  Bauer, and Reiter, ACM CCS 2016.
- Adversarial patch — `:780` — Brown et al., arXiv 2017; person-hiding held patch —
  Thys, Van Ranst, and Goedemé, CVPR-W 2019.
- Audio adversarial examples (99.9% similar waveform → any phrase, 100% vs
  DeepSpeech) — `:793` — Carlini and Wagner, arXiv 2018 (venue unverified; cited
  year-only).
- Multimodal jailbreak image — `:806` — Qi et al., "Visual Adversarial Examples
  Jailbreak Aligned Large Language Models", AAAI 2024.
- ImageNet-C (15 corruptions × 5 severities = 75 sets) — `:834` — Hendrycks and
  Dietterich, ICLR 2019.
- NIST adversarial-ML taxonomy — `:848` — NIST AI 100-2 E2025, March 2025.

**Figures:** panda + noise + gibbon capture (Goodfellow Fig 1,
`figs/panda-gibbon.png`) `:103`; stop-sign photo pair (Eykholt Fig 1 capture,
`figs/eykholt-stopsign.png`) `:748`; inline SVG: boundary crossing
`:161`, L∞ box vs L2 ball `:272`, PGD steps in ball `:414`, robustness radius `:496`.
Citations use `.cite-left`. Page number: bold `.slide-num` only.

**2026-08 content revision (56→63):** every citation/number fetched and verified.
Added 7 slides: Why? Too Linear Inside + Why? Features, Not Bugs (§01), Robustness vs
Accuracy (§04), The Scoreboard: RobustBench (§05), Adversarial Glasses (§06),
Related: The World Also Shifts + ImageNet-C (§06). Fixed: "broke seven defenses" →
verified 9 examined / 7 obfuscated / 6 fully + 1 partially broken (Athalye); panda
confidences rounded → exact 57.7% / 99.3%; stop-sign slide gained target class and
verified success rates; transfer-is-scary gained verified Papernot numbers; patches
"wearable" claim replaced by verified held-patch (Thys); 2025-26 Frontier rewritten
around NIST AI 100-2 (unverified "certificates that finally scale" bullet deleted).
Section 06 renamed Physical & Multimodal → Physical & Beyond. `lec08tech.html`
audited: all math correct incl. Cohen certified radius, no changes (stays 19 sl).
Note file synced (63 entries, order matches).

## lec09-poisoning.html

**Topic:** Data poisoning & backdoors (~90 min). Train-time vs inference-time
attacks; web-scraped corpora as the attack surface (supply-chain frame);
availability vs targeted taxonomy; clean-label poisoning at picture level (Poison
Frogs, feature collision); BadNets trigger backdoors (real Gu Fig 7 capture, clean
accuracy vs attack success); web-scale poisoning (Carlini split-view /
frontrunning, $60 for 0.01%); artist tools (Glaze, Nightshade); LLM poisoning
(instruction-tuning poisoning, near-constant poison count / 250-documents result,
sleeper agents); defenses (data curation, spectral signatures, activation
clustering, Neural Cleanse, fine-pruning); model-stealing one-slide touchpoint
(full deck: `backup-model-stealing.html`). Math lives in `lec09tech.html`.

### Sections (61 slides, ~90 min — content-revised 2026-08 from 55, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — The Train-Time Threat** | 3–9 | `:77` | two places to attack `:85` · pipeline cracks (SVG) `:123` · supply chain `:147` |
| **02 — Data Poisoning** | 10–18 | `:174` | two goals `:182` · SVM poisoning (Biggio) `:207` · boundary tilt (SVG) `:220` · clean-label `:257` · **Poison Frogs (one poison image, transfer setting; verified 2026-08)** `:270` · feature collision (SVG) `:285` |
| **03 — Backdoors and Triggers** | 19–27 | `:308` | backdoor idea `:316` · BadNets `:329` · **trigger pipeline (Gu Fig 7 capture, verified)** `:342` · clean accuracy stays high `:354` · two numbers `:367` · **stop sign (Post-it, >90% flip, 95% confidence; fixed 2026-08)** `:381` |
| **04 — Web-Scale Poisoning** | 28–36 | `:422` | **Poisoning Is Practical ($60, 10 datasets; fixed 2026-08)** `:443` · split-view (SVG) `:456` · frontrunning `:482` · **tiny fraction (0.01% of LAION-400M ≈ $60; fixed 2026-08)** `:496` · **Glaze (added 2026-08)** `:519` · **Nightshade (added 2026-08)** `:533` |
| **05 — Backdoors in Language Models** | 37–45 | `:548` | tuning is a new target `:556` · **Poisoned Instructions (Wan ICML 2023, ~100 examples; fixed 2026-08)** `:569` · text trigger `:583` · **How Much Poison Is Needed? (added 2026-08)** `:596` · **250 Documents Are Enough (SVG; added 2026-08)** `:610` · **Sleeper Agents (2023/2024 code trigger; fixed 2026-08)** `:632` · safety training misses it `:646` |
| **06 — Defenses, Frontier 2025–26** | 46–58 | `:673` | two lines of defense `:681` · **Defending the Pipeline (hashes + randomized snapshots; added 2026-08)** `:693` · spectral signatures `:708` · outlier picture (SVG) `:721` · activation clustering `:741` · Neural Cleanse `:754` · fine-pruning `:767` · demo `:780` · **Related Threat: Model Stealing (added 2026-08)** `:821` · **Frontier 2025–26 (rewritten 2026-08)** `:835` |
| Takeaways / Closer | 59–61 | — | what to remember `:848` · key takeaway `:862` · closer `:870` |

**Key definitions / citations (all source-verified 2026-08):**
- SVM poisoning (first formal study) — `:216` — Biggio, Nelson, and Laskov,
  "Poisoning Attacks against Support Vector Machines", ICML 2012.
- Poison Frogs clean-label attack (one poison image suffices in the
  transfer-learning test) — `:266`, `:281` — Shafahi et al., NeurIPS 2018.
- BadNets (trigger stickers, >90% stop signs → speed-limit, real photo fooled at
  95% confidence, clean accuracy level with baseline) — `:156`, `:338`, `:350`,
  `:391` — Gu, Dolan-Gavitt, and Garg, 2017 (arXiv 1708.06733; Figure 7).
- Web-scale poisoning ($60 buys 0.01% of LAION-400M; split-view = expired
  domains; frontrunning = snapshot timing; defenses = integrity hashes +
  randomized snapshots) — `:452`, `:478`, `:492`, `:502`, `:704` — Carlini et
  al., IEEE S&P 2024.
- Glaze (style cloak, >92% mimicry disruption) — `:529` — Shan et al., USENIX
  Security 2023.
- Nightshade (<100 samples corrupt one SDXL prompt) — `:543` — Shan et al.,
  IEEE S&P 2024.
- Instruction-tuning poisoning (~100 examples skew hundreds of tasks; larger
  models more vulnerable) — `:579` — Wan, Wallace, Shen, and Klein, ICML 2023.
- Near-constant poison count (~250 documents backdoor 600M–13B models,
  Chinchilla-optimal 6B–260B tokens; 20× more clean data does not raise the
  bar) — `:606`, `:628` — Souly et al., 2025 (arXiv 2510.07192; UK AI Security
  Institute, Anthropic, Alan Turing Institute).
- Sleeper agents (2023 secure / 2024 exploitable code; survives SFT, RL, and
  adversarial training; largest models most persistent) — `:642`, `:655` —
  Hubinger et al., 2024 (arXiv 2401.05566). Distinct from Souri et al.
  "Sleeper Agent" (not referenced here).
- Spectral signatures — `:717` — Tran, Li, and Madry, NeurIPS 2018.
- Activation clustering — `:750` — Chen et al., 2018 (arXiv 1811.03728).
- Neural Cleanse — `:763` — Wang et al., IEEE S&P 2019.
- Fine-pruning — `:776` — Liu, Dolan-Gavitt, and Garg, RAID 2018.
- Model stealing — `:831` — Tramèr, Zhang, Juels, Reiter, and Ristenpart,
  USENIX Security 2016.

**Figures:** BadNets clean + yellow-square/bomb/flower trigger stop signs (Gu
Fig 7 capture, `figs/badnets-trigger.png`) `:347`; inline SVG: pipeline cracks
`:128`, boundary tilt `:225`, feature collision `:290`, split-view `:461`,
poison-count scaling `:615`, spectral outlier `:726`. Citations use
`.cite-left`. Page number: bold `.slide-num` only.

**2026-08 content revision (55→61):** every citation/number fetched and verified.
Added 6 slides: Artists Fight Back: Glaze + Nightshade: Poison as Deterrent (§04),
How Much Poison Is Needed? + 250 Documents Are Enough (§05), Defending the
Pipeline (§06), Related Threat: Model Stealing (§06). Fixed: stop-sign slide
gained verified BadNets numbers (>90% flip, 95%-confidence street photo, clean
accuracy level); Poisoning Is Practical gained verified $60 / 10-datasets / no-
insider numbers; Tiny Fraction now states the verified 0.01%-of-LAION-400M ≈ $60
guarantee (unverified "a handful of examples can suffice" deleted); Poisoned
Instructions gained verified Wan numbers (~100 examples, larger models more
vulnerable); Sleeper Agents corrected to the 2023/2024 code-vulnerability trigger
and lab-planted framing; Safety Training Misses It gained verified SFT/RL/
adversarial-training findings; Frontier rewritten around verified anchors
(unverified "provable bounds on tolerable poison" deleted); What to Remember
extended to six verified points. Note-file error fixed: trigger described as "red
square" → yellow square/bomb/flower per Gu Fig 7. `lec09tech.html` audited: math
correct (feature-collision ℓ∞ form verified against Poison Frogs Appendix C);
one cite fixed — λ-blended backdoor objective no longer attributed verbatim to
BadNets, now "standard formalization of" Gu 2017 (stays 16 sl). Note file synced
(61 entries, order matches).

## lec10-jailbreak.html

**Topic:** Jailbreaks & LLM safety (~90 min). Safety training at picture level
(instruction tuning → RLHF/InstructGPT → Constitutional AI, one slide each); why
refusal is fragile (thin layer, shallow/first-token alignment, refusal-as-a-direction,
Wei's two failure modes); the jailbreak zoo (persona/DAN, fake authority, obfuscation,
GCG adversarial suffixes, PAIR black-box, many-shot, low-resource languages, ciphers,
fine-tuning removes safety); jailbreaks as adversarial examples (one unifying view);
red-teaming & safety evaluation as practice; layered defenses (filters, system-prompt
hardening, Constitutional Classifiers, circuit breakers); attacker–defender asymmetry;
2025–26 frontier. Math lives in `lec10tech.html`.

### Sections (57 slides, ~90 min — content-revised 2026-08 from 54, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — Safety Training** | 3–11 | `:80` | raw model `:89` · two goals `:102` · instruction tuning (Ouyang) `:114` · RLHF (SVG, Ouyang) `:127` · Constitutional AI (Bai 2022) `:164` · refusal behavior `:177` |
| **02 — Why It Is Fragile** | 12–18 | `:202` | thin layer `:211` · **Shallow Alignment (Qi ICLR 2025 "few tokens deep"; added cite 2026-08)** `:225` · **Two Failure Modes (Wei Fig 1 capture)** `:249` · competing objectives `:262` · mismatched generalization (SVG) `:275` · **Refusal Is a Direction (Arditi NeurIPS 2024; added cite 2026-08)** `:298` |
| **03 — Manual Jailbreaks** | 19–24 | `:311` | what a jailbreak is `:318` · persona play `:329` · fake authority `:342` · obfuscation `:355` · manual is brittle `:368` |
| **04 — Automated Jailbreaks** | 25–32 | `:383` | from art to optimization `:390` · the target `:403` · **GCG (Zou 2023; 99/100 on Vicuna-7B; added 2026-08)** `:415` · search loop `:426` · **Search in Token Space (GCG Fig 1 capture)** `:441` · **It Transfers (84% GPT-3.5/4, 66% PaLM-2, ~2% Claude; added 2026-08)** `:455` · PAIR (Chao <20 queries) `:469` |
| **05 — Scaling the Attack** | 33–38 | `:481` | many-shot (Anil) `:491` · **Power-Law Curve (MSJ Fig 1 capture — attribution fixed from Fig 2)** `:504` · **Low-Resource Languages (Yong ~79% on GPT-4; added cite 2026-08)** `:516` · cipher prompts (CipherChat idea) `:526` · **Fine-Tuning Removes Safety (Qi ICLR 2024, 10 examples/$0.20; added slide 2026-08)** `:543` |
| **06 — One Unifying View** | 39–43 | `:555` | adversarial examples (Szegedy) `:565` · same idea in text `:578` · crossing the boundary (SVG) `:589` · the hard lesson `:611` |
| **07 — Defenses & Frontier** | 44–55 | `:621` | **Red-Teaming: Attack to Defend (Ganguli 38,961 attacks; added slide 2026-08)** `:629` · **Red-Teaming at Scale (Perez EMNLP 2022; added slide 2026-08)** `:642` · defense in layers `:660` · filters `:672` · system-prompt hardening `:685` · **Constitutional Classifiers (Sharma 2025; cite fixed from Bai 2022 + verified numbers)** `:694` · **Circuit Breakers (Zou NeurIPS 2024)** `:708` · demo `:721` · cat-and-mouse (SVG) `:736` · not solved `:757` · **Frontier 2025-26 (Best-of-N Hughes 2024, agentic; rewritten 2026-08)** `:772` |
| Takeaways / Closer | 56–57 | — | key takeaways `:784` · closer `:797` |

**Key definitions / citations (all source-verified 2026-08):**
- InstructGPT (instruction tuning + RLHF) — `:114`, `:127` — Ouyang et al., NeurIPS 2022.
- Constitutional AI (AI feedback, self-critique) — `:164` — Bai et al., 2022 (arXiv 2212.08073).
- Shallow safety alignment ("first few output tokens") — `:225` — Qi et al., "Safety
  Alignment Should Be Made More Than Just a Few Tokens Deep", ICLR 2025 (Outstanding Paper).
- Two failure modes (competing objectives; mismatched generalization) — `:249`, `:262`,
  `:275` — Wei, Haghtalab, Steinhardt, "Jailbroken: How Does LLM Safety Training Fail?",
  NeurIPS 2023 (Fig 1: GPT-4 competing-objectives, Claude v1.3 base64 mismatched-gen).
- Refusal is a one-dimensional direction (13 models ≤72B) — `:298` — Arditi et al.,
  "Refusal in Language Models Is Mediated by a Single Direction", NeurIPS 2024.
- GCG (universal + transferable; 99/100 harmful behaviors Vicuna-7B, 88% Harmful
  Strings; transfer 84% GPT-3.5/GPT-4, 66% PaLM-2, ~2.1% Claude) — `:415`, `:441`,
  `:455` — Zou et al., "Universal and Transferable Adversarial Attacks on Aligned
  Language Models", 2023 (arXiv 2307.15043; Fig 1 = ChatGPT/Claude/Bard/Llama-2).
- PAIR (jailbreak in <20 queries) — `:469` — Chao et al., 2023 (arXiv 2310.08419).
- Many-shot jailbreaking (power-law in shots; more effective on larger models) — `:491`,
  `:504` — Anil et al., NeurIPS 2024 (Fig 1 = the three-panel plot capture).
- Low-resource-language jailbreak (~79% on GPT-4) — `:516` — Yong, Menghini, Bach, 2023
  (arXiv 2310.02446).
- Cipher/CipherChat (~100% bypass in some domains) — `:526` — Yuan et al., ICLR 2024
  (concept only; not cited on slide).
- Fine-tuning compromises safety (10 examples, <$0.20 on GPT-3.5 Turbo; benign
  fine-tuning also degrades) — `:543` — Qi et al., ICLR 2024 (arXiv 2310.03693, Oral).
- Adversarial examples origin — `:565` — Szegedy et al., ICLR 2014.
- Automated red-teaming (LM attacks LM, tens of thousands of offensive replies) —
  `:642` — Perez et al., EMNLP 2022.
- Human red-teaming (38,961-attack dataset; RLHF harder to break with scale) — `:629` —
  Ganguli et al., 2022 (arXiv 2209.07858).
- Constitutional Classifiers (3,000+ red-team hrs, no universal jailbreak; +0.38%
  refusals, ~24% inference overhead) — `:694` — Sharma et al. (Anthropic), 2025
  (arXiv 2501.18837).
- Circuit breakers / representation rerouting — `:708` — Zou et al., "Improving
  Alignment and Robustness with Circuit Breakers", NeurIPS 2024 (arXiv 2406.04313).
- Best-of-N jailbreaking (power-law ASR; 89% GPT-4o, 78% Claude 3.5 Sonnet @ N=10k) —
  `:772` — Hughes et al., 2024 (arXiv 2412.03556).

**Figures:** Wei failure modes (`figs/wei-jailbroken.png`, NeurIPS 2023 Fig 1) `:252`;
GCG schematic (`figs/gcg-schematic.png`, Zou 2023 Fig 1) `:445`; many-shot power-law
(`figs/msj-powerlaw.png`, Anil NeurIPS 2024 **Fig 1**) `:504`. Inline SVG: RLHF loop
`:132`, shallow-alignment first-token `:229`, capability⊃safety Venn `:280`, decision
boundary + suffix `:575`, cat-and-mouse `:696`. Citations use `.cite-left`.

**2026-08 content revision (54→58):** every citation/number fetched and verified.
Added 3 slides: Fine-Tuning Removes Safety (§05, Qi ICLR 2024), Red-Teaming: Attack to
Defend + Red-Teaming at Scale (§07, Ganguli 2022 + Perez EMNLP 2022 — fills the
red-teaming/safety-eval coverage gap). Fixes: **Constitutional Classifiers cite was
wrong** (Bai 2022 CAI → Sharma et al. Anthropic 2025, the actual Constitutional
Classifiers paper) plus verified deployment numbers; **MSJ figure mis-attributed
Fig 2 → Fig 1**; added verified numbers to GCG (99/100 Vicuna), It Transfers (84/66/2%),
Low-Resource (~79%); added citations to Shallow Alignment (Qi ICLR 2025), Refusal Is a
Direction (Arditi NeurIPS 2024), Low-Resource (Yong 2023); Frontier rewritten around
verified anchors (Best-of-N Hughes 2024, agentic vulnerability). `lec10tech.html`
checked: RLHF KL-penalized objective and GCG target both correct, no changes (12 sl).
Note file synced (57 entries + closer = 58, order matches).

## lec11-prompt-injection.html

**Topic:** Prompt injection & agentic safety (~90 min). Injection vs jailbreak
(attacker is a third party arriving via data, not the user); direct vs indirect
injection; data-vs-control-plane confusion as THE core idea; the agentic risk surface
(tools, agent loop, confused deputy, lethal trifecta); real incidents (Bing "Sydney"
leak, Greshake real-app injection, email-exfiltration class, EchoLeak, SpAIware memory
poisoning, CamoLeak/GitHub MCP); why it is hard (no privilege separation, filtering
brittle, no clean escape); defenses and why partial (filtering, spotlighting,
instruction hierarchy, taint tracking, dual-LLM, capability control/CaMeL, human in
the loop, least privilege); 2025–26 frontier (AI browsers, MCP, AgentDojo, adaptive
attacks). Security model lives in `lec11tech.html`. Autonomy risks touched in Open
Problems only — full treatment stays in `backup-agentic-autonomy.html` (not absorbed).

### Sections (63 slides, ~90 min — content-revised 2026-08 from 58, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:34`, `:46` | |
| **01 — Direct vs Indirect Injection** | 3–13 | `:79` | one-line idea `:88` · two failure modes `:113` · direct `:127` · indirect `:140` · hidden text `:166` · **Naming the Problem (Goodside demonstrated / Willison named; attribution fixed 2026-08)** `:179` · not the same as SQL `:192` · **The #1 LLM Risk (OWASP LLM01:2025; added 2026-08)** `:205` |
| **02 — The Agentic Surface** | 14–23 | `:218` | chatbot→agent `:227` · what a tool is `:240` · agent loop `:253` · two channels `:269` · data becomes control `:283` · attack picture (SVG) `:291` · confused deputy `:329` · three ingredients `:342` · **Lethal Trifecta (Willison 2025)** `:355` |
| **03 — Real Incidents** | 24–33 | `:364` | **Bing "Sydney" Leak (rewritten 2026-08 to verified Kevin Liu direct injection)** `:373` · Greshake real apps `:387` · email-exfiltration class `:400` · **EchoLeak CVE-2025-32711 (added 2026-08)** `:413` · **SpAIware memory poisoning (added 2026-08)** `:427` · **CamoLeak + GitHub MCP (added 2026-08)** `:441` · quiet exit channels `:455` · vendors responded `:468` · pattern emerges `:481` |
| **04 — Why It Is Hard** | 34–40 | `:495` | no privilege separation `:504` · one flat context (SVG) `:517` · instructions look alike `:535` · filtering brittle `:548` · no clean escape `:561` · still open `:573` |
| **05 — Defenses** | 41–53 | `:581` | layered mindset `:590` · I/O filtering `:603` · **Spotlighting (Hines 2024; title fixed 2026-08)** `:617` · **Instruction Hierarchy (Wallace OpenAI 2024; cite fixed 2026-08)** `:630` · taint tracking `:643` · dual-LLM (Willison 2023) `:656` · quarantine picture (SVG) `:670` · **Capability Control (CaMeL, Debenedetti 2025)** `:703` · human in loop `:716` · least privilege `:729` · scorecard `:737` · toy-agent demo `:749` |
| **06 — Frontier 2025–26** | 54–61 | `:765` | **New Surfaces, Same Flaw (AI browsers + MCP; added 2026-08)** `:774` · measuring `:788` · **AgentDojo (NeurIPS 2024 D&B; title/venue completed 2026-08)** `:801` · **Where Defenses Stand (Zhan adaptive attacks NAACL 2025; cite added 2026-08)** `:814` · design shift `:828` · open problems `:841` · practical advice `:854` |
| Takeaways / Closer | 62–63 | — | key takeaways `:867` · closer `:879` |

**Key definitions / citations (all source-verified 2026-08):**
- Naming: Goodside demonstrated on GPT-3, Willison coined the name — `:179` — Willison,
  "Prompt injection attacks against GPT-3", Sept 2022; Perez & Ribeiro, "Ignore Previous
  Prompt: Attack Techniques for Language Models", 2022 (arXiv 2211.09527).
- OWASP LLM01: Prompt Injection, #1 in the 2025 edition (second edition running) — `:205`.
- Lethal trifecta (private data + untrusted content + external communication) — `:355` —
  Willison, "The lethal trifecta for AI agents", June 2025.
- Bing "Sydney" system-prompt extraction by direct injection — `:373` — Kevin Liu, Feb 2023.
- Indirect injection on real deployed apps — `:387` — Greshake, Abdelnabi, Mishra, Endres,
  Holz, Fritz, "Not What You've Signed Up For: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection", ACM AISec 2023 (arXiv 2302.12173).
- EchoLeak zero-click exfiltration — `:413` — CVE-2025-32711 (Microsoft 365 Copilot),
  Aim Security, June 2025; server-side patch, no known exploitation.
- SpAIware persistent memory exfiltration — `:427` — Rehberger, Sept 2024 (ChatGPT macOS
  app); fixed by OpenAI.
- CamoLeak (Copilot Chat, per-image exfil) + GitHub MCP private-repo leak — `:441` —
  CVE-2025-59145, Legit Security, Oct 2025; Invariant Labs, May 2025.
- Spotlighting — `:617` — Hines et al., "Defending Against Indirect Prompt Injection
  Attacks With Spotlighting", 2024 (arXiv 2403.14720).
- Instruction hierarchy — `:630` — Wallace et al. (OpenAI), "The Instruction Hierarchy:
  Training LLMs to Prioritize Privileged Instructions", 2024 (arXiv 2404.13208).
- Dual-LLM pattern — `:656` — Willison, "The Dual LLM pattern for building AI assistants
  that can resist prompt injection", April 2023.
- Capability control / CaMeL — `:703` — Debenedetti et al., "Defeating Prompt Injections
  by Design", 2025 (arXiv 2503.18813).
- AI-browser + MCP attack surface — `:774` — Brave, "Indirect prompt injection in
  Perplexity Comet" & "Unseeable prompt injections in screenshots", 2025; Invariant Labs
  GitHub MCP, 2025.
- AgentDojo — `:801` — Debenedetti et al., "AgentDojo: A Dynamic Environment to Evaluate
  Prompt Injection Attacks and Defenses for LLM Agents", NeurIPS 2024 (Datasets &
  Benchmarks) (arXiv 2406.13352).
- Adaptive attacks break defenses (8 defenses bypassed, ASR >50%) — `:814` — Zhan, Fang,
  Panchal, Kang, "Adaptive Attacks Break Defenses Against Indirect Prompt Injection
  Attacks on LLM Agents", NAACL 2025 Findings (arXiv 2503.00061).

**Figures:** all inline SVG (no captured paper figures): attack picture (page→agent→tool
→attacker) `:294`, one flat context (system/goal/untrusted stack) `:521`, quarantine
dual-LLM dataflow `:673`. Citations use `.cite-left`.

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
Stand; quarantine-SVG label overlap fixed. `lec11tech.html` checked: security model
verified (dual-LLM matches Willison 2023; CaMeL cite correct), two prose-dash lint
warnings fixed (stays 9 sl). Note file synced (63 entries, order matches).

## lec12-watermark.html

**Topic:** Watermarking, deepfakes & provenance (~90 min). The provenance problem
(did an AI make this?); watermark vs after-the-fact detector as THE core distinction;
green-list text watermarking at picture level (split vocabulary, nudge green, count
green — z-statistic and formulas live in `lec12tech.html`); quality and robustness
limits (distortion-free/undetectable marks, paraphrase attacks, dilution-not-erasure);
production systems (SynthID-Text in Nature, SynthID images, 10B+ items marked);
image/video fragility and the no-standard problem; why keyless AI-text detectors fail
(false accusations, OpenAI withdrawal); deepfake harms (Arup $25M call, NH robocall,
2024 reality check), C2PA content credentials, and the 2025–26 legal turn (China
labeling rules, EU AI Act Art. 50). Rigorous treatment lives in
`courses/privacy/lectures/06-watermark/` (authoritative; this deck states no Thm 4.3
and stays consistent with the corrected math there).

### Sections (64 slides, ~90 min — content-revised 2026-08 from 55, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Two Flavors of Watermarking** | 3–10 | `:72` | the problem `:81` · what a watermark is `:94` · two flavors `:107` · model watermarks (ownership) `:119` · output watermarks (flag content) `:132` · why we care `:145` · **Watermark vs Detector (planted signal vs guess — the lecture's spine)** `:158` |
| **02 — Text Watermarking** | 11–21 | `:170` | how a model writes `:179` · **Green-List Idea (KGW ICML 2023)** `:192` · splitting the vocabulary (SVG) `:205` · the nudge `:231` · reading it back `:240` · telltale fraction `:253` · detection threshold (SVG) `:265` · false positives `:287` · length beats luck `:299` · one-knob tradeoff `:308` |
| **03 — Quality and Robustness** | 22–31 | `:320` | quality worry `:329` · distortion-free (Aaronson 2022; Kuditipudi TMLR 2024) `:342` · reused randomness `:354` · undetectable (Christ COLT 2024) `:367` · robustness worry `:380` · small edits survive `:393` · **Paraphrase Attack (DIPPER, Krishna NeurIPS 2023)** `:406` · **Impossibility Claim (Sadasivan TMLR 2025, stated precisely)** `:420` · **Honest Limit (dilution not erasure, Kirchenbauer ICLR 2024)** `:434` |
| **04 — Production and Images** | 32–39 | `:448` | **SynthID-Text (Dathathri Nature 634 (2024), tournament sampling, ~20M live test)** `:457` · SynthID images `:470` · **SynthID at Scale (10B+ items, Detector portal; added 2026-08)** `:483` · image marks fragile `:496` · cropping erases (SVG) `:509` · video harder `:539` · no shared standard `:552` |
| **05 — Detecting AI Content** | 40–46 | `:565` | tempting shortcut (GPTZero and kin) `:574` · why detectors struggle `:587` · **False Accusations (Liang Patterns 2023, non-native TOEFL)** `:600` · **OpenAI Pulled Its Detector (26%/9%, withdrawn July 2023)** `:614` · try it yourself (demo) `:628` · the right lesson `:643` |
| **06 — Deepfakes and Provenance** | 47–63 | `:651` | deepfakes `:660` · real harms `:673` · **Case: The $25M Video Call (Arup HK, added 2026-08)** `:686` · **Deepfakes Meet Elections (NH Biden robocall, $6M FCC fine; added 2026-08)** `:700` · **2024 Reality Check (Meta <1% stat; added 2026-08)** `:714` · **Detection Arms Race (DFDC ~65%; SVG; added 2026-08)** `:728` · flip the problem `:751` · C2PA credentials `:764` · signed history `:777` · **Credentials Go Mainstream (Leica→S25→Pixel 10 timeline SVG; added 2026-08)** `:790` · strip problem `:815` · **The Law Steps In** `:828` · **China Labels First (CAC + GB 45438-2025; added 2026-08)** `:841` · **EU AI Act: Article 50 (2 Aug 2026; added 2026-08)** `:855` · frontier 2025–26 `:869` · key takeaways `:882` |
| Closer | 64 | — | closer ("Real?") `:896` |

**Key citations (all source-verified 2026-08):**
- Green-list watermark — `:200` — Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein,
  "A Watermark for Large Language Models", ICML 2023 (arXiv 2301.10226). Full math in
  `lec12tech.html`; z-test details also in `courses/privacy/lectures/06-watermark/`.
- Distortion-free — `:349`, `:401` — Aaronson 2022 (talk/blog); Kuditipudi, Thickstun,
  Hashimoto, Liang, "Robust Distortion-free Watermarks for Language Models", TMLR 2024.
- Undetectable watermarks — `:375` — Christ, Gunn, Zamir, "Undetectable Watermarks for
  Language Models", COLT 2024.
- Paraphrase attack (DIPPER; watermark detection 70.3%→4.6% at 1% FPR) — `:415` —
  Krishna et al., "Paraphrasing evades detectors of AI-generated text, but retrieval is
  an effective defense", NeurIPS 2023 (arXiv 2303.13408).
- Impossibility/spoofing claims — `:429` — Sadasivan, Kumar, Balasubramanian, Wang,
  Feizi, "Can AI-Generated Text be Reliably Detected? …", TMLR 2025 (arXiv 2303.11156).
- Dilution not erasure (~800 tokens after strong human paraphrase at 1e-5 FPR) — `:443`
  — Kirchenbauer et al., "On the Reliability of Watermarks for Large Language Models",
  ICLR 2024.
- SynthID-Text — `:465` — Dathathri et al., "Scalable watermarking for identifying
  large language model outputs", Nature 634 (2024); SynthID Detector portal + 10B+
  items — `:491` — Google DeepMind, May 2025.
- Detector bias — `:609` — Liang, Yuksekgonul, Mao, Wu, Zou, "GPT detectors are biased
  against non-native English writers", Patterns 2023.
- OpenAI classifier withdrawal — `:623` — OpenAI, Jan 2023, withdrawn July 2023.
- Arup deepfake fraud — `:695` — HK police Feb 2024; CNN Business May 2024.
- NH robocall — `:709` — FCC forfeiture (Steve Kramer, $6M) + NH DOJ, 2024.
- Meta 2024 elections (<1%) — `:723` — Meta, Dec 2024. DFDC ~65% — `:746` — Facebook
  AI, 2020.
- China labeling — `:850` — CAC "Measures for Labeling AI-Generated Synthetic Content"
  + GB 45438-2025, effective 1 Sept 2025.
- EU AI Act — `:864` — Regulation 2024/1689, Art. 50(2)/(4), applicable 2 Aug 2026.

**Figures:** all inline SVG (no captured paper figures): vocabulary split `:209`,
detection-threshold bell curves `:269`, cropping erases the mark `:513`, detection
arms-race loop `:732`, C2PA adoption timeline `:794`. Citations use `.cite-left`.

**2026-08 content revision (55→64):** every citation/number fetched and verified.
Added 9 slides: SynthID at Scale (§04); Case: The $25M Video Call, Deepfakes Meet
Elections, The 2024 Reality Check, The Detection Arms Race (§06 harms block);
Credentials Go Mainstream (§06 C2PA adoption timeline); The Law Steps In overview
split into China Labels First + EU AI Act: Article 50 (§06 regulation block). Fixes:
**Kuditipudi venue fabricated** (2023 → TMLR 2024); **Dathathri title wrong** →
actual Nature title; **Sadasivan misattribution rewritten** (deck overclaimed
"proved detection impossible" → the paper's precise claims: recursive paraphrasing
degrades detectors, keyless-detector coin-flip result, spoofing) with Kirchenbauer
ICLR 2024 dilution counterpoint added; Aaronson cite matched to the privacy deck's
verified form; "~800 words" → "~800 tokens". `lec12tech.html` checked: FP rate at
τ=4 corrected "&lt;" → "≈ 3×10⁻⁵" (1−Φ(4)≈3.2×10⁻⁵, and KGW state ≈3×10⁻⁵); states
no Thm 4.3 (stays 10 sl). Note file synced (58 entries, order matches).

## lec13-fairness-defs.html

**Topic:** Fairness I — definitions & impossibility (~90 min). Where bias enters the
pipeline (data, labels — Amazon recruiting + Obermeyer cost-proxy case — feedback
loops, proxy features); three group-fairness definitions at plain-English level
(demographic parity, equalized odds / equal opportunity, calibration — one glanceable
conditional-probability line each; the formal stack + impossibility proof sketch live
in `lec13tech.html`); COMPAS as the anchor case (ProPublica FPR gap vs Northpointe's
predictive-parity/calibration defense — both "right" under different definitions,
which IS the impossibility story); the impossibility theorem (Chouldechova 2017 +
Kleinberg et al. ITCS 2017) as base-rate intuition, no proof in the main deck;
individual (Dwork) and counterfactual (Kusner) fairness one slide each; fairness in
generative models (Bianchi occupation grid, Gemini overcorrection, Gender Shades,
BBQ, NYC Local Law 144 + Colorado AI Act). Gender Shades *figure* stays in lec14
(this deck cites the numbers only, no figure duplication).

### Sections (58 slides, ~90 min — content-revised 2026-08 from 54, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:39` | |
| **01 — Sources of Bias** | 3–13 | `:72` | model mirrors its world `:80` · bias is not a bug `:92` · three entry points `:101` · biased data `:112` · **Biased Labels: Amazon hiring (Reuters 2018)** `:125` · label is the problem `:138` · **Case: Cost as a Proxy for Need (Obermeyer, 17.7%→46.5% bar SVG; added 2026-08)** `:150` · feedback loops (SVG) `:175` · why "just drop race" fails `:201` · notation A/Y/Ŷ `:213` |
| **02 — Group Fairness Criteria** | 14–22 | `:226` | confusion matrix per group (SVG) `:234` · demographic parity `:259` · parity ignores the truth `:269` · equalized odds `:281` · equal opportunity variant `:294` · calibration `:307` · calibration trusts the score `:317` · three criteria side by side `:329` |
| **03 — The COMPAS Case** | 23–29 | `:343` | what COMPAS is `:351` · ProPublica investigation `:364` · **False Positives, By Group (44.9% vs 23.5% bar SVG + 47.7%/28.0% FNR mirror)** `:374` · **Northpointe Responds (predictive parity)** `:397` · both sides were right `:410` · could COMPAS be both? `:422` |
| **04 — The Impossibility Theorem** | 30–39 | `:432` | base rates `:440` · **The Impossibility Theorem (Chouldechova + Kleinberg, plain-English)** `:449` · two proofs, same wall `:461` · pick-two-of-three triangle (SVG) `:473` · demo setup `:493` · **Demo: The Numbers Don't Reconcile (derivable Ŝ∈{0.2,0.8} construction, FPR 0.20/0.02, FNR 0.20/0.73)** `:508` · why the gap is forced `:523` · which one to pick `:536` · choosing by context `:545` |
| **05 — Individual & Causal Fairness** | 40–46 | `:557` | group fairness can hide harm `:565` · individual fairness (Dwork) `:577` · the "similar" metric problem `:589` · **A Causal View (counterfactual fairness, Kusner)** `:602` · fair and unfair paths (causal-graph SVG) `:612` · causal fairness needs a model `:637` |
| **06 — Fairness in Generative Models** | 47–56 | `:650` | new surface, old problem `:658` · **Text-to-Image Stereotyping (Bianchi Fig 1, `figs/bianchi-occupations.png`)** `:671` · **When the Fix Overcorrects (Gemini pause Feb 2024; added 2026-08)** `:692` · **Gender Shades (34.7% vs 0.8%)** `:706` · auditing is the tool `:716` · **Auditing LLMs: The BBQ Benchmark (added 2026-08)** `:729` · **The Law Notices (NYC LL144 + Colorado AI Act; added 2026-08)** `:743` · frontier 2025–26 `:760` |
| Wrap-up / Closer | 56–58 | — | open tension `:773` · key takeaways `:786` · closer ("Pick two.") `:799` |

**Key citations (all source-verified 2026-08):**
- ProPublica — `:370` — Angwin, Larson, Mattu, Kirchner, "Machine Bias", ProPublica 2016;
  methodology + exact rates (FPR 44.85%/23.45%, FNR 27.99%/47.72%) — `:393` — Larson et
  al., "How We Analyzed the COMPAS Recidivism Algorithm", ProPublica 2016.
- Northpointe rebuttal — `:406` — Dieterich, Mendoza, Brennan, "COMPAS Risk Scales:
  Demonstrating Accuracy Equity and Predictive Parity", Northpointe, July 2016.
- Impossibility — `:457`, `:469` — Chouldechova, "Fair Prediction with Disparate
  Impact", Big Data 2017 (also `:313` calibration def); Kleinberg, Mullainathan,
  Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores", ITCS 2017.
- Group-fairness definitions — `:265`/`:585` Dwork, Hardt, Pitassi, Reingold, Zemel,
  "Fairness Through Awareness", ITCS 2012; `:290` Hardt, Price, Srebro, "Equality of
  Opportunity in Supervised Learning", NeurIPS 2016.
- Counterfactual fairness — `:608` — Kusner, Loftus, Russell, Silva, NeurIPS 2017.
- Label bias cases — `:134` Dastin, Reuters, Oct 2018 (Amazon tool penalized "women's");
  `:171` Obermeyer, Powers, Vogeli, Mullainathan, Science 2019 (17.7%→46.5%).
- Generative — `:688` Bianchi et al., "Easily Accessible Text-to-Image Generation
  Amplifies Demographic Stereotypes at Large Scale", FAccT 2023 Fig 1; `:702` Google
  blog, Feb 2024 (Gemini pause); `:712` Buolamwini & Gebru, FAT* 2018 (34.7%/0.8%);
  `:739` Parrish et al., "BBQ: A Hand-Built Bias Benchmark for Question Answering",
  Findings of ACL 2022 (nine dimensions; +3.4pp stereotype-aligned accuracy).

**Figures:** `figs/bianchi-occupations.png` (FAccT 2023 Fig 1, shared with lec14) `:673`;
inline SVGs: Obermeyer bar chart `:155`, feedback loop `:180`, confusion matrix `:238`,
COMPAS FPR bars `:379`, pick-two triangle `:477`, causal graph `:617`. Citations use
`.cite-left`.

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
rewritten around verified content. `lec13tech.html` fixed (see supplement table).
Note file synced (58 entries, order matches).

## lec14-fairness-mitigation.html

**Topic:** Fairness II — mitigation & accountability (~90 min). Picks up where lec13's
definitions end: three places to intervene in the pipeline (pre-/in-/post-processing),
one intuition + picture per method with formal math in `lec14tech.html` (reweighing
w(g,y), penalized/constrained objectives, reductions, per-group ROC thresholds);
the fairness–accuracy tradeoff and the impossibility recap (defined and proved in
lec13 — referenced, not redone); accountability (model cards, datasheets, audits —
Gender Shades figure + Actionable Auditing follow-up — impact assessments, EU AI Act
touchpoint only, governance is lec15); generative & LLM fairness (Bianchi figure
shared with lec13, Gemini overcorrection referenced briefly — the full case is
lec13's — plus LLM decision bias, prompt steering, post-training as mitigation,
resume-screening risk, and the 2025 both-ways regulatory squeeze).

### Sections (61 slides, ~90 min — content-revised 2026-08 from 55, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — Three Places to Intervene** | 3–8 | `:81` | we measured bias; now fix it `:89` · what mitigation means `:102` · ML pipeline (SVG) `:113` · which stage can you touch `:145` · black-box reality `:157` |
| **02 — Pre-Processing** | 9–15 | `:171` | bias is in the data `:179` · **Reweighing (Kamiran & Calders)** `:192` · reweighing picture (SVG) `:206` · relabeling `:234` · representation repair `:247` · pros and cons `:260` |
| **03 — In-Processing** | 16–23 | `:273` | Loss+λ·penalty `:281` · constraint τ `:290` · **Reductions (Agarwal et al. ICML 2018)** `:303` · why reductions are handy `:316` · **Adversarial Debiasing (Zhang et al. AIES 2018; adversary reads the prediction — fixed 2026-08)** `:329` · adversary's job `:354` · pros and cons `:367` |
| **04 — Post-Processing** | 24–34 | `:380` | leave the model alone `:388` · recall equalized odds `:401` · **Group-Specific Thresholds (Hardt et al., SVG)** `:413` · post-hoc recipe `:436` · **What Post-Processing Needs (added 2026-08)** `:450` · accuracy cost `:463` · lending demo ×3 (illustrative numbers) `:476` `:487` `:509` · **Toolkits Ship These Methods (Fairlearn + AIF360; added 2026-08)** `:522` |
| **05 — The Tradeoff** | 35–40 | `:536` | frontier curve (SVG) `:544` · which fairness `:565` · impossibility (recap of lec13) `:578` · no free lunch `:586` · a choice, not a formula `:599` |
| **06 — Accountability** | 41–50 | `:613` | mitigation needs a record `:621` · **Model Cards (Mitchell et al.)** `:634` · **Datasheets (Gebru et al.)** `:647` · audits `:660` · **Gender Shades figure (`figs/gender-shades.png`, FAT* 2018 Table 4)** `:673` · reading the table (0–0.8% vs 20.8–34.7%) `:684` · **The Audit Worked (Raji & Buolamwini AIES 2019, before/after bar SVG; added 2026-08)** `:697` · impact assessments `:736` · documentation becomes law (EU AI Act touchpoint) `:749` |
| **07 — Generative & LLM Fairness** | 51–59 | `:763` | **Bianchi figure (`figs/bianchi-occupations.png`, shared with lec13)** `:771` · debias a generator `:789` · **Overcorrection Is Its Own Bias (Gemini Feb 2024, merged from 2 slides; case detail lives in lec13)** `:802` · **Do LLMs Discriminate? (Tamkin et al.; added 2026-08)** `:816` · **Prompting the Bias Away (added 2026-08)** `:831` · **Post-Training as Mitigation (Eloundou et al. ICLR 2025; added 2026-08)** `:846` · **Screening Is Still Risky (Wilson & Caliskan AIES 2024; added 2026-08)** `:861` · **Regulation Pulls Both Ways (EO 14319; added 2026-08)** `:875` |
| Wrap-up / Closer | 60–61 | — | key takeaways `:889` · closer ("λ") `:903` |

**Key citations (all source-verified 2026-08):**
- Reweighing — `:202` — Kamiran & Calders, "Data Preprocessing Techniques for
  Classification without Discrimination", Knowledge and Information Systems 2012
  (w = Pexp/Pobs verified against the paper).
- Reductions — `:312` — Agarwal, Beygelzimer, Dudík, Langford, Wallach, "A Reductions
  Approach to Fair Classification", ICML 2018.
- Adversarial debiasing — `:350` — Zhang, Lemoine, Mitchell, "Mitigating Unwanted
  Biases with Adversarial Learning", AIES 2018 (adversary predicts the group from the
  predictor's *output*, not shared features — deck fixed accordingly).
- Post-processing — `:409`, `:446` — Hardt, Price, Srebro, "Equality of Opportunity in
  Supervised Learning", NeurIPS 2016.
- Toolkits — `:531` — Fairlearn (fairlearn.org, community-driven); AI Fairness 360
  (IBM → LF AI & Data, July 2020).
- Model cards — `:643` — Mitchell et al. (9 authors incl. Raji, Gebru), FAT* 2019.
- Datasheets — `:656` — Gebru et al., CACM Dec 2021.
- Gender Shades — `:680` — Buolamwini & Gebru, FAT* 2018 Table 4 (DF error
  20.8/34.5/34.7%; LM 0.0/0.8/0.3%); follow-up `:732` — Raji & Buolamwini, "Actionable
  Auditing", AIES 2019 (7 months, DF error 20.8→1.5 MSFT, 34.5→4.1 Face++, 34.7→17.0
  IBM; unaudited Amazon 31.4%, Kairos 22.5%).
- Generative/LLM — `:785` Bianchi et al., FAccT 2023 Fig 1; `:812` Google blog Feb 2024
  (Gemini); `:827`/`:842` Tamkin et al. (Anthropic), 2023 (70 decisions; steering
  prompts → gap near zero, ~92% aligned); `:857` Eloundou et al. (OpenAI),
  "First-Person Fairness in Chatbots", ICLR 2025 (<0.1% harmful stereotypes; ~3–12×
  reduction from post-training); `:871` Wilson & Caliskan, AIES 2024 (85.1% vs 11.1%);
  `:884` Executive Order 14319, July 2025.

**Figures:** `figs/gender-shades.png` (FAT* 2018 Table 4, verified against paper) `:678`;
`figs/bianchi-occupations.png` (FAccT 2023 Fig 1, shared with lec13) `:775`; inline
SVGs: pipeline `:118`, reweighing cells `:211`, adversarial architecture `:334`,
thresholds `:418`, demo tradeoff `:492`, frontier curve `:549`, audit before/after
bars `:702`. Citations use `.cite-left`.

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
`lec14tech.html` checked (see supplement table). Note file synced (61 entries, order
matches).

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

### Sections (66 slides, ~90 min — content-revised 2026-08 from 53, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:26`, `:38` | |
| **01 — Connect the Threads** | 3–13 | `:71` | trust stack (SVG) `:93` · data thread `:121` · **reliability thread (hallucination/calibration/interpretability; added 2026-08)** `:134` · adversary `:147` · accountability `:160` · the pattern `:173` · **Bommasani foundation-models stakes** `:206` |
| **02 — Risk Frameworks** | 14–22 | `:220` | NIST AI RMF `:240` · four functions (SVG loop) `:253` · Map/Measure/Manage `:278` `:291` `:304` · **GenAI Profile (NIST AI 600-1, confabulation; added 2026-08)** `:317` |
| **03 — Regulation** | 23–39 | `:340` | **Weidinger taxonomy (4 of 6 risk areas)** `:348` · EU risk tiers (pyramid SVG) `:375` · banned `:397` · high risk `:410` · **EU timeline incl. Digital Omnibus deferral (SVG; added 2026-08)** `:436` · **GPAI rules + Code of Practice (added 2026-08)** `:466` · US patchwork `:480` · **US whiplash timeline (EO 14110→14179→14319→preemption push, SVG; added 2026-08)** `:493` · **Korea AI Basic Act ×2 (added 2026-08)** `:523` `:537` · Anderljung frontier regulation `:551` · **summit timeline (Bletchley→Seoul→Paris→New Delhi, SVG; added 2026-08)** `:577` · **International AI Safety Report (added 2026-08)** `:606` |
| **04 — Auditing & Red-Teaming** | 40–52 | `:620` | red-teaming `:640` · audit loop (SVG) `:653` · dangerous-capability evals `:678` · **frontier safety frameworks (if-then flow SVG; added 2026-08)** `:691` · **Anthropic RSP/ASL `:715` · OpenAI Preparedness v2 `:728` · GDM FSF v3 `:741` (all added 2026-08)** · model cards `:767` · audit limits `:792` |
| **05 — Open Problems for 2026+** | 53–59 | `:802` | web-scale privacy `:823` · robust unlearning `:836` · agentic safety `:849` · provenance+fairness `:862` · tensions `:875` |
| **06 — Wrap-Up** | 60–66 | `:884` | reading an AI headline `:892` · five questions `:905` · **Demo Showcase (course logistics, kept)** `:919` · one lesson `:935` · key takeaways `:943` · closer ("Thank you") `:957` |

**Key citations (all source-verified 2026-08):**
- Foundation models — `:216` — Bommasani et al., "On the Opportunities and Risks of
  Foundation Models", 2021 (arXiv 2108.07258).
- NIST — `:250`/`:275` AI RMF 1.0, 2023; `:327` Generative AI Profile (NIST AI 600-1),
  July 2024 (12 GenAI risks incl. confabulation).
- Taxonomy — `:359` — Weidinger et al., "Taxonomy of Risks Posed by Language Models",
  FAccT 2022 (six risk areas; slide shows four, intro says so).
- EU — `:394`/`:420` Regulation (EU) 2024/1689 (the AI Act); `:463` Regulation (EU)
  2026/1744 (Digital Omnibus on AI: high-risk duties → Dec 2027 / Aug 2028); `:477`
  General-Purpose AI Code of Practice, July 2025 (10^25 FLOP systemic-risk threshold).
- US — `:520` — Executive Orders 14110 (2023, rescinded), 14179 (Jan 2025), 14319
  (July 2025); Dec 2025 preemption push. No federal AI statute as of mid-2026.
- Korea — `:534`/`:548` — AI Basic Act, effective Jan 2026 (MSIT; high-impact AI;
  GenAI labeling; 10^26 FLOP duty threshold; fines ≤ 30M KRW, 1-year grace).
- Frontier — `:561`/`:688` Anderljung et al., "Frontier AI Regulation", 2023 (arXiv
  2307.03718); `:725` Anthropic RSP 2023 (rev. 2026) + ASL-3 activation May 2025
  (Claude Opus 4); `:738` OpenAI Preparedness Framework v2, Apr 2025; `:751` Google
  DeepMind Frontier Safety Framework v3, Sept 2025 (CCLs; added manipulation +
  misalignment).
- International — `:616` — International AI Safety Report, 2026 (Bengio chair, 100+
  experts, ~30 countries); summits slide `:577` (Bletchley 2023; Seoul 2024, 16 labs;
  Paris 2025; New Delhi 2026, 89 endorsers) verified against gov.uk/summit records.

**Figures:** all inline SVGs (no captured images): trust stack `:99`, RMF loop `:259`,
EU tier pyramid `:381`, EU timeline `:442`, US whiplash timeline `:499`, summit
timeline `:583`, audit loop `:659`, if-then framework flow `:697`. Citations use
`.cite-left`.

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
