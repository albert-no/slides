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
| 2. Reliability | 6–7 | Can you believe the answer, and see why |
| 3. Security | 8–11 | How models are attacked, train- and inference-time |
| 4. Provenance & Fairness | 12–14 | Watermarking, fairness, accountability |
| 5. Synthesis | 15 | Governance, frontier, demo showcase |

## Lecture index

| Wk | File | Topic | Status |
|---|---|---|---|
| 1 | `lec01-introduction.html` | Introduction & threat-model thinking | **revised 2026-09** (44 sl, ~40 min) |
| 2 | `lec02-privacy-dp.html` | Privacy & differential privacy | **revised 2026-09** (94 sl, 15 figs) |
| 3 | `lec03-mia.html` | Membership inference attacks | **revised 2026-08, figure pass 2026-09** (63 sl, 15 real figs) |
| 4 | `lec04-memorization.html` | Memorization & training-data extraction | **revised 2026-08, figure pass 2026-09** (60 sl, 26 real figs) |
| 5 | `lec05-unlearning.html` | Machine unlearning | **figures 2026-09** (67 sl) |
| 6 | `lec06-hallucination.html` | Hallucination, calibration & reliability | **figures 2026-09** (61 sl) |
| 7 | `lec07-interpretability.html` | Interpretability & explainability | **revised 2026-08, figure pass 2026-09** (64 sl, 23 real figs) |
| 8 | `lec08-adversarial.html` | Adversarial examples (attack + defense) | **revised 2026-08, figure pass 2026-09** (63 sl, 25 real figs) |
| 9 | `lec09-poisoning.html` | Data poisoning & backdoors | **revised 2026-08, figure pass 2026-09** (65 sl) |
| 10 | `lec10-jailbreak.html` | Jailbreaks & LLM safety | **revised 2026-08, figure pass 2026-09** (60 sl, 21 real figs) |
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
- `lec03` 15 real figures (Salem, Yeom, Shokri, Carlini 2022 ×3, Choquette-Choo, Steinke, Shi, Carlini diffusion, Duan, Das, Hayes, Maini, Zhang) — see its section.
- `lec08` panda→gibbon (`figs/panda-gibbon.png`) + Eykholt stop-sign (`figs/eykholt-stopsign.png`, CVPR 2018 Fig 1).
- `lec09` BadNets trigger strip (`figs/badnets-trigger.png`, Gu et al. 2017 Fig 7).
- `lec10` Wei failure modes (`figs/wei-jailbroken.png`, NeurIPS 2023 Fig 1), GCG schematic (`figs/gcg-schematic.png`, Zou 2023 Fig 1 — replaced SVG), many-shot power-law (`figs/msj-powerlaw.png`, Anil et al. NeurIPS 2024 **Fig 1** — attribution corrected from Fig 2, 2026-08); 2026-09 figure pass added 18 more (Ouyang, Bai, Qi, Arditi, Zou GCG/CB, Chao, Yong, Yuan, Szegedy, Ganguli, Perez, Sharma, Hughes) — see its section.
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

**Topic:** Motivational course overview (~40 min). Capability outran trust; a long
examples-first middle (one real incident per trust dimension, balanced across fairness,
privacy, reliability, robustness, security, safety, provenance, data ownership, society);
why learned systems fail differently; threat-model thinking
(who / knows / can do; knowledge × timing); the trust stack and the fifteen-topic map.
Sets the vocabulary used all term.

### Sections (44 slides, ~40 min — rebuilt 2026-09-03 from the 35-slide 2026-08 deck, trimmed 2026-09-04; "scary examples" imported from `talks/sangnam2609/sangnam1-ai-today.html`)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:47`, `:59` | title "Can We Trust It?" |
| **01 — The Gap** | 3–6 | `:88` | **METR task-length plot** `:96` · AI decides real outcomes `:107` · two curves SVG `:122` |
| **02 — When It Goes Wrong** | 7–32 | `:145` | *fairness* COMPAS bars SVG `:153` · Gender Shades table `:184` · Amazon pipeline SVG `:197` · *privacy* GPT-2 extraction `:227` · "poem" divergence SVG `:242` · Samsung + Garante `:272` · *reliability* Avianca + Deloitte fake-citation card `:308` · Charlotin 1,598 filings `:340` · Air Canada + $1 car chat bubbles `:362` · sycophancy (Sharma Fig. 5) `:392` · *robustness* panda→gibbon `:408` · stop-sign stickers `:419` · *security* Base64 jailbreak `:434` · EchoLeak SVG `:446` · *safety* Uber Tempe `:477` · July 2026 escaped agent timeline `:493` · it came back `:510` · 59% vs 3% scheming `:542` · *provenance* Pope puffer `:568` · Sora frame + NH robocall `:583` · Arup $25M `:598` · *data* Bartz $1.5B SVG `:620` · *society* Canaries plot `:650` · EU pyramid + Korea AI Basic Act `:665` · **the pattern = seven dimensions (7-row table: incidents → question → dimension, + transparency)** `:693` |
| **03 — Why AI Fails Differently** | 33–35 | `:710` | SW vs learned SVG `:718` · three sources SVG `:753` |
| **04 — Threat-Model Thinking** | 36–39 | `:786` | **what is a threat model (+adversary SVG, EchoLeak worked example)** `:794` · **attack map 2×2 SVG** `:831` · no threat model, no answer (59/3 + panda/stop sign) `:858` |
| **05 — This Course** | 40–43 | `:882` | **trust stack SVG carrying all 14 topics** `:890` · concepts first, demos optional `:917` · the goal (headline→property→threat→convincing? flow SVG + 3 drill cards) `:937` |
| Closer | 44 | `:972` | "Trust?" |

**Visuals (real images, all in `figs/`):** `metr-task-length.png` (METR Time Horizon 1.1,
Jan 2026, CC BY) `:101` · `gender-shades.png` (Buolamwini & Gebru 2018, Table 4) `:190` ·
`gpt2-extraction.png` (Carlini et al. 2021, Fig. 1; source PNG is cropped at the bottom)
`:232` · `sharma-sycophancy.png` (Sharma et al. ICLR 2024, Fig. 5) `:397` ·
`panda-gibbon.png` (Goodfellow et al. 2015, Fig. 1) `:413` · `eykholt-stopsign.png`
(Eykholt et al. CVPR 2018, Fig. 1) `:424` · `wei-jailbroken.png` (Wei et al. NeurIPS 2023,
Fig. 1) `:440` · `uber-tempe-ntsb.jpg` (NTSB, public domain, via Commons) `:482` ·
`pope-puffer-midjourney.jpg` (AI-generated, PD, via Commons) `:573` · `sora-tokyo.jpg`
(OpenAI Sora "Tokyo Walk", PD, via Commons) `:588` · `canaries-22-25.png` (Stanford
Digital Economy Lab, Fig. 2) `:655`. **SVG diagrams:** two curves `:128`, COMPAS bars
`:160`, Amazon pipeline `:203`, poem divergence `:248`, you⇄model data flow `:288`, fake
citation card `:324`, chat bubbles `:378`, EchoLeak flow `:452`, patched-route `:516`,
59%/3% bars `:548`, library→model `:626`, EU risk pyramid `:671`, SW vs learned `:724`,
three sources `:759`, adversary↔system `:808`, attack map `:837`, trust stack `:896`,
headline→question flow `:946`.

**Key citations:** Angwin et al., ProPublica 2016 (COMPAS) · Buolamwini & Gebru, FAT* 2018
· Dastin, Reuters 2018 (Amazon) · Carlini et al., USENIX Sec 2021 + Nasr et al. 2023
(extraction) · Bloomberg May 2023 (Samsung) + Garante order 30 Mar 2023 · Mata v. Avianca,
S.D.N.Y. 2023 · Deloitte/DEWR Oct 2025 · Charlotin, AI Hallucination Cases, June 2026 ·
Moffatt v. Air Canada, 2024 BCCRT 149 · Sharma et al. ICLR 2024 + OpenAI Apr 2025 (GPT-4o
rollback) · Goodfellow et al. ICLR 2015 · Eykholt et al. CVPR 2018 · Wei et al. NeurIPS 2023
· EchoLeak CVE-2025-32711 · NTSB HWY18MH010 · OpenAI / Hugging Face July 2026 incident
(via TIME 24 Jul 2026) · arXiv 2603.01608 (scheming) · Midjourney Pope, Mar 2023 · NH
robocall FCC orders 2024 · Arup deepfake, HK police Feb 2024 · Bartz v. Anthropic, N.D.
Cal. 2025 · Brynjolfsson, Chandar & Chen, "Canaries" 2025–26 · Regulation (EU) 2024/1689 ·
Korea AI Basic Act (eff. 2026-01-22).

**Fragile facts (post-knowledge-cutoff, imported from sangnam1 — re-verify before
teaching):** July 2026 OpenAI/Hugging Face escaped-evaluation incident (dates, 2.5 days,
4 accounts) `:493`–`:540`; scheming paper arXiv 2603.01608 (59% vs 3%) `:542`; Charlotin
counts 1,598 / $145k / 15 (9 June 2026 snapshot) `:340`; Korea AI Basic Act details `:665`.
sangnam1 dates the Canaries paper "August 2026"; the original working paper is August
2025, so the slide cites "2025–26" `:650`. The note file marks the same entries
"post-cutoff".

**Key framing:** threat model = *who* / *what they know* (white/black-box) / *what they
can do* (train/inference-time); "a safety number describes a deployment, not a model"
(59% vs 3%) motivates section 04. Seven dimensions (fairness, privacy, reliability,
robustness, security, safety, provenance) + transparency; the 2026-08 deck had six. **The
seven-dimension taxonomy is stated exactly once** (slide 32, closing section 02); the
course map is stated exactly once (slide 41, the trust stack). Do not re-add summary
slides that restate them — Albert cut them on 2026-09-04 as duplicates.
Citations use `.cite-left`; one exhibit per slide.

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
the budget $\varepsilon$; randomized response; noise-by-sensitivity; DP-SGD;
privacy–utility tradeoff; federated learning; private foundation models (2025–26).
Intuition pass — points to the privacy course for rigor.

### Sections (94 slides, full 90 min — content-revised 2026-08, figures added 2026-09-04, Homer 2008 block added 2026-09-04, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — The Privacy Problem** | 3–15 | `:77` | **GPT-2 extraction image** `:116` · Secret Sharer · "repeat poem" · **diffusion copy image (Ann)** `:177` · Copilot secrets (Huang FSE 2024) `:191` · 3 kinds of leak · **Sweeney 87% Venn (SVG)** `:284` + Golle 63% caveat · Netflix+AOL merged `:302` |
| **02 — How Leakage Is Measured** | 16–33 | `:333` | membership inference · **Homer et al. 2008 block (10 slides, 20–29, no proofs)** `:371`–`:619`: genome leak intro `:371` · SNP primer (SVG) `:411` · membership-is-the-secret examples (SVG) `:440` · **distance statistic + Fig 1** `:472` · one-SNP SNR (SVG) `:478` · aggregation √(m/n) (SVG) `:509` · **simulation Fig 2A** `:547` · **real-mixture Fig 3** `:569` · NIH policy impact `:578` · Homer→ML table `:605` · **MIA loss-overlap (SVG)** `:627` · model inversion · NYT v. OpenAI · Italy ban ("Privacy Is a Business Risk" slide deleted 2026-08 — content moved to note's "Regulators Step In" entry) |
| **03 — Differential Privacy** | 34–55 | `:699` | two-worlds · **$(\varepsilon,\delta)$-DP definition** `:809` (plain-English lead-in) · budget $\varepsilon$ · $\varepsilon$ in the wild `:907` (Apple 4–8/item + audited 16/day, Census $\approx 17$) · $\delta \ll 1/n$ `:942` · post-processing · **indistinguishability + heights (SVG)** `:1008` · what DP does/doesn't |
| **04 — Achieving DP: Add Randomness** | 56–68 | `:1072` | **Randomized response + coin-tree (SVG)** `:1120` · recover-the-rate worked example `:1141` · local vs central DP · RAPPOR/Apple · **Laplace mechanism + noise bell (SVG)** `:1224` · sensitivity |
| **05 — Private Machine Learning** | 69–80 | `:1310` | **DP-SGD** `:1339` (clip+noise merged to one slide) · privacy accountant · utility cost (benchmark folded in) · **federated learning (SVG)** `:1466` · Gboard · FL still leaks · secure aggregation |
| **06 — Frontier 2025–26** | 81–90 | `:1548` | private fine-tuning (Yu, Li 2022) `:1556` · **VaultGemma DP pretraining** `:1568` (added 2026-08) · private synthetic data + Apple Intelligence 2025 `:1589` · web-scale puzzle · privacy auditing · unlearning preview · Apple PCC · EU AI Act (GPAI duties since Aug 2025) `:1653` · open problems `:1665` |
| Wrap (deeper / demos / takeaways) | 91–93 | — | `:1679`–`:1705` |
| Closer | 94 | — | `$\varepsilon$` `:1718` |

**Key definitions / citations (all source-verified 2026-08):**
- $(\varepsilon,\delta)$-DP — `:809` — relaxation from Dwork, Kenthapadi, McSherry, Mironov,
  Naor, EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006). "A 2006 Idea" `:707`
  keeps Dwork, McSherry, Nissim, Smith, TCC 2006 for $\varepsilon$-DP — matches `courses/privacy/lectures/01-dp/`.
- **Statistical indistinguishability** (heights example, Korea/Japan Gaussians) — `:990-:1063` —
  "Many Samples Break It" `:1038` folds in the composition intuition; warm-up `:1003` carries the coin-flip highlight.
- Randomized response — `:1093` — Warner, JASA 1965.
- DP-SGD — `:1339` — Abadi et al., ACM CCS 2016.
- De-anonymization — `:302` — Narayanan & Shmatikov, IEEE S&P 2008.
- Sweeney 87% (1990 census) — `:279` — Sweeney, Data Privacy WP3, 2000; Golle, WPES 2006 re-estimate (63%) added as caveat.
- $\varepsilon$ in the wild — `:907` — Apple "Learning with Privacy at Scale" 2017; Tang et al. 2017 audit; US Census 2020 ($\varepsilon \approx 17$).
- VaultGemma DP pretraining ($\varepsilon \le 2$, sequence-level) — `:1568` — Google Research, 2025.
- Homer et al. 2008 membership inference on GWAS allele frequencies — `:371`–`:619` — Homer et al., PLoS Genetics 4(8) e1000167, 2008
  (distance statistic $D_j = |Y_j-\mathrm{Pop}_j| - |Y_j-M_j|$, paper sign; the privacy course mia1 deck uses the opposite sign).
  Per-SNP / aggregate numbers on `:478`,`:509` are the idealized model after Sankararaman et al., Nature Genetics 2009 — labelled as such, not the paper's.
  NIH response `:578` — Zerhouni & Nabel, Science 322:44, 2008. Proof-level version lives in `courses/privacy/lectures/04-mia/mia1-foundations.html`; not duplicated in lec03.

**Real images** (`figs/`, cropped + cited per GOTCHAS; all captions verified against the source PDF):
GPT-2 extraction `figs/gpt2-extraction.png` (Carlini et al. 2021, Fig 1) `:116`; Secret Sharer canary
exposure `figs/secret-sharer-exposure.png` (Carlini et al., USENIX Sec 2019, Fig 1) `:136`; ChatGPT
emission-rate bars `figs/nasr-emission-rate.png` (Nasr et al. 2023, arXiv:2562.17035, Fig 1) `:164`;
Stable-Diffusion copy `figs/calrini-ann.png` — **re-attributed 2026-08** to Carlini et al., "Extracting
Training Data from Diffusion Models", USENIX Security 2023, Fig 1 (Somepalli removed; verified against
arXiv 2301.13188) `:177`; Copilot credential pipeline `figs/huang-credential-leak.png` (Huang et al.,
FSE 2024, Fig 1) `:196`; black-box MIA diagram `figs/shokri-mia.png` (Shokri et al., IEEE S&P 2017,
Fig 1) `:364`; Homer distance-measure schematic `figs/homer-distance-measure.png` (Homer et al., PLoS Genetics 2008, Fig 1) `:472`;
Homer simulation SNPs-vs-fraction heatmap `figs/homer-simulation-snps-vs-fraction.png` (ibid., Fig 2A, $v_p=0.001$) `:547`;
Homer real-mixture validation row `figs/homer-validation-row.png` (ibid., Fig 3 top row, panels A–D) `:569`; model-inversion face pair `figs/fredrikson-inversion.png` (Fredrikson, Jha, Ristenpart,
CCS 2015, Fig 1) `:648`; NYT complaint side-by-side `figs/nyt-complaint-p30.png` (NYT v. Microsoft &
OpenAI, S.D.N.Y. 1:23-cv-11195, complaint p. 30) `:669`; Apple local-DP system overview
`figs/apple-dp-overview.png` (Apple, "Learning with Privacy at Scale", 2017, Fig 1) `:1213`; CIFAR-10 /
ImageNet accuracy vs $\varepsilon$ `figs/de-cifar-epsilon.png` (De et al. 2022, arXiv:2455.13650, Fig 1)
`:1422`; deep leakage from gradients `figs/dlg-leakage.png` (Zhu, Liu, Han, NeurIPS 2019, Fig 1) `:1505`;
VaultGemma memorization bars `figs/vaultgemma-memorization.png` (Google, arXiv:2761.15001, Fig 1) `:1581`.
Duplication histogram `figs/carlini_duplicates.png` moved to `lec04-memorization.html`.
**SVG figures:** three-kinds-of-leak staircase `:203`, quasi-identifier table `:240`, Netflix↔IMDb
linkage `:302`, Sweeney linkage Venn, GWAS averages→attacker flow `:371`, SNP table `:411`, membership-secret timeline `:440`,
per-SNP two-bells `:478`, sum-of-signals bells `:509`, NIH timeline `:578`, MIA loss-overlap, deterministic-vs-randomized release `:771`,
neighboring datasets D/D′ `:829`, height-distribution overlap, $\varepsilon$ scale bar `:878`,
$\varepsilon$-in-the-wild bars `:907`, post-processing pipeline `:960`, randomized-response coin tree,
local-vs-central pipelines `:1159`, Laplace noise bell, sensitivity bars `:1237`, Gaussian-vs-Laplace
bell `:1278`, DP-SGD pipeline `:1339`, accountant $\varepsilon$-vs-steps curve `:1389`, more-data
signal/noise bars `:1429`, secure-aggregation flow `:1512`, federated learning. Citations use
`.cite-left`. Page number: bold `.slide-num` only. Intuition pass — points to
`courses/privacy/lectures/01-dp/` for rigor.

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

**Topic:** Membership inference attacks (~90 min). What "was this example in the
training set?" means and why it matters (privacy audit, litigation, extraction
pre-step); overfitting/loss-gap intuition; shadow models at picture level; LiRA as
"compare to a population of reference models"; evaluation done right (TPR at low FPR);
MIA on LLMs and diffusion models; DP-vs-MIA in one line; 2025–26 frontier (strong-attack
wall, dataset inference, courtroom use). Intuition pass — the rigorous treatment lives
in `courses/privacy/lectures/04-mia/` (5-deck series); facts kept consistent with it.

### Sections (63 slides, ~90 min — content-revised 2026-08 from 59, all citations source-verified; figure pass 2026-09)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:31`, `:43` | |
| **01 — The Question** | 3–11 | `:80` | one yes-or-no question `:88` · member vs non-member worlds `:130` · cancer-cohort harm `:143` · **Who Asks, and Why (audit / courts / extraction; added 2026-08)** `:165` · threat model `:178` · score + threshold `:192` |
| **02 — The Basic Attack** | 12–20 | `:221` | train loss < test loss `:229` · loss score `:255` · **two-bells overlap (SVG)** `:265` · overfitting drives MIA (caveat: small gap ≠ safe) `:287` · 3-line threshold attack `:308` · confidence baseline (**Salem Fig. 11, real fig**) `:320` · Yeom theory anchor (sufficient, not necessary; **Yeom Fig. 2, real fig**) `:338` · Colab demo `:353` |
| **03 — Shadow Models** | 21–26 | `:369` | shadow idea (**Shokri Fig. 2, real fig**) `:405` · **shadow pipeline (SVG)** `:420` · learned attack `:447` · why it transfers `:482` |
| **04 — Stronger Attacks** | 27–36 | `:514` | difficulty vs membership (**Carlini Fig. 3, real fig**) `:522` · per-example calibration `:542` · likelihood ratio `:565` · **LiRA** `:580` · **in-vs-out bells (SVG)** `:594` · label-only (**Choquette-Choo Fig. 1, real fig**) `:614` · average accuracy lies (**Carlini Fig. 2, real fig**) `:633` · **TPR at low FPR** (retitled 2026-08; **Carlini Fig. 1, real fig**) `:648` · **ROC tail (SVG)** `:667` |
| **05 — What It Means** | 37–43 | `:688` | $(\varepsilon,\delta)$-DP recall `:696` · DP caps the attacker `:708` · TPR $\le e^{\varepsilon}\cdot$FPR$+\delta$ `:739` · empirical $\varepsilon$ auditing `:763` · trust but verify `:782` · canaries + one-run auditing (**Steinke Fig. 3, real fig**) `:796` |
| **06 — Modern Models** | 44–54 | `:817` | MIA meets foundation models `:825` · Min-K% (**Shi Fig. 1, real fig**) `:838` · **diffusion duplication histogram (real fig)** `:852` · Duan web-scale doubt (**Duan Fig. 1, real fig**) `:872` · why scale breaks it `:882` · benchmark trap (temporal confound, blind baselines; **Das Fig. 1, real fig**) `:911` · **Give the Attack Everything (Hayes wall; added 2026-08; Hayes Fig. 2(a), real fig)** `:930` · **dataset inference (added 2026-08; Maini Fig. 1, real fig)** `:949` · **MIA in the Courtroom (added 2026-08; Zhang Fig. 1, real fig)** `:963` · open debate `:974` |
| **07 — Defenses** | 55–61 | `:989` | shrink the gap `:997` · heuristics not proof `:1009` · DP-SGD `:1037` · why DP-SGD stops MIA `:1053` · utility cost `:1085` · defender's checklist `:1110` |
| Takeaways / Closer | 62–63 | — | `:1124`, `:1137` |

**Key definitions / citations (all source-verified 2026-08):**
- Shadow models — `:405` — Shokri, Stronati, Song, and Shmatikov, IEEE S&P 2017.
- Loss attack / advantage-vs-gap — `:255`, `:338` — Yeom, Giacomelli, Fredrikson, and Jha,
  "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting", IEEE CSF 2018
  (full title restored 2026-08). Overfitting **sufficient, not necessary** — matches
  `courses/privacy/lectures/04-mia/` (mia3).
- Confidence baseline — `:320` — Salem et al., "ML-Leaks", NDSS 2019 (re-attributed 2026-08;
  was wrongly cited to Shokri 2017).
- Likelihood-ratio framing — `:565` — Sablayrolles et al., ICML 2019.
- LiRA + TPR-at-low-FPR standard — `:580`, `:648` — Carlini et al., "Membership Inference
  Attacks From First Principles", IEEE S&P 2022.
- Label-only — `:614` — Choquette-Choo, Tramèr, Carlini, and Papernot, ICML 2021.
- $(\varepsilon,\delta)$-DP — `:696` — Dwork, Kenthapadi, McSherry, Mironov, and Naor,
  EUROCRYPT 2006 (fixed 2026-08; was misattributed to TCC 2006 — same fix as lec02).
- One-run auditing — `:796` — Steinke, Nasr, and Jagielski, NeurIPS 2023.
- Min-K% — `:838` — Shi et al., ICLR 2024.
- Diffusion extraction/duplication — `:852` — Carlini et al., USENIX Security 2023, Fig. 5.
- Web-scale doubt — `:872` — Duan et al., COLM 2024.
- Blind baselines / temporal confound — `:911` — Das, Zhang, and Tramèr, DATA-FM at ICLR 2025
  (direction fixed 2026-08: members are the *older* text, non-members post-cutoff).
- Strong-attack wall — `:930` — Hayes, Shumailov, et al., NeurIPS 2025.
- Dataset inference — `:949` — Maini, Jia, Papernot, and Dziedzic, NeurIPS 2024.
- MIA-as-evidence position — `:963` — Zhang, Das, Kamath, and Tramèr, IEEE SaTML 2025.
- DP-SGD — `:1037` — Abadi et al., ACM CCS 2016.

**Real images (15, all cropped from the cited PDFs at 150 dpi, figure numbers verified against captions):**
`figs/salem-max-posterior.png` (ML-Leaks Fig. 11) `:326` · `figs/yeom-advantage-gap.png` (Yeom Fig. 2) `:348` ·
`figs/shokri-shadow-training.png` (Shokri Fig. 2) `:415` · `figs/carlini-lira-fig3-per-example.png` (Carlini 2022 Fig. 3) `:527` ·
`figs/choquette-label-only.png` (Choquette-Choo Fig. 1) `:620` · `figs/carlini-lira-fig2-roc-scales.png` (Carlini 2022 Fig. 2) `:643` ·
`figs/carlini-lira-fig1-tpr-fpr.png` (Carlini 2022 Fig. 1) `:662` · `figs/steinke-one-run-eps.png` (Steinke Fig. 3) `:801` ·
`figs/shi-mink-overview.png` (Shi Fig. 1) `:848` · `figs/carlini_duplicates.png` (Carlini diffusion, USENIX Security 2023, Fig. 5;
attribution verified against arXiv 2301.13188; also used by `lec04-memorization.html`) `:858` ·
`figs/duan-auc-vs-size.png` (Duan Fig. 1) `:878` · `figs/das-wikimia-pca.png` (Das Fig. 1, appendix) `:925` ·
`figs/hayes-compute-optimal-mia.png` (Hayes Fig. 2(a)) `:935` · `figs/maini-dataset-inference.png` (Maini Fig. 1) `:959` ·
`figs/zhang-training-data-proof.png` (Zhang Fig. 1) `:970`.
**SVG figures (20):** leak ladder `:114`, world cards `:130`, score axis + threshold `:206`, train/test loss curves + gap `:239`,
two-bells loss overlap `:271`, small-gap vs large-gap bells `:293`, one-threshold-two-classes `:391`, shadow pipeline `:425`,
output vector → attack classifier `:461`, target vs shadow bells `:496`, per-example baseline `:552`, in-vs-out bells `:600`,
ROC tail `:673`, two neighbouring worlds → DP training `:718`, ROC with DP ceiling `:749`, small-model vs LLM bells `:896`,
attack-success vs attack-strength (regularization vs DP bound) `:1023`, clip + noise `:1067`, schematic accuracy-vs-ε `:1095`;
plus the auditing `diagram-flow` `:773`. Citations use `.cite-left` with figure numbers. Page number: bold `.slide-num` only.

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
$\Lambda(x)$ as a `math-block` `:575`. Note file: one "Slide figure" sentence per new figure (14 articles).


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

### Sections (60 slides, ~90 min — content-revised 2026-08 from 59; figure pass 2026-09 58→60, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:27`, `:40` | |
| **01 — What Is Memorization** | 3–15 | `:72` | working definition + **Cooper Fig 1 (real fig)** `:112` · three flavors (verbatim / near-duplicate / stylistic; retaxonomized 2026-08) `:127` · $k$-extractable + **prefix→suffix SVG** `:140` · **Extractable vs Discoverable (added 2026-08)** `:169` · why it happens + **loss-bars SVG** `:182` · **Some Memorization Is Necessary (Feldman Fig 1(a), real fig)** `:210` · Secret Sharer + **Secret Sharer Fig 6 (real fig)** `:225` · canary `:242` · **canary-leak pipeline (SVG)** `:254` · exposure + **Secret Sharer Fig 7 (real fig)** `:279` · pattern-vs-record SVG `:296` |
| **02 — Extracting Text from LLMs** | 16–26 | `:319` | canary-vs-wild SVG `:328` · **GPT-2 PII (real fig)** `:350` · **extraction pipeline (SVG; redrawn 2026-08 with 1,800/604 numbers)** `:370` · confidence signal + **zlib-vs-perplexity Fig 3 (real fig)** `:401` · what came out (604 strings) + **Table 1 (real fig)** `:418` · repeat-forever prompt + **ChatGPT screenshot Fig 5 (real fig)** `:432` · **loop breaks (SVG)** `:448` · scale of the leak (10,000+ / $200 / 150×) + **Nasr Fig 1 (real fig)** `:469` · patched-not-solved + **Nasr Fig 9 extrapolation (real fig)** `:486` · Colab demo `:499` |
| **03 — How Much, and Why It Grows** | 27–35 | `:514` | measurable fraction + **Carlini Fig 2(a,b) (real fig)** `:523` · three drivers (size / duplication / **context** — third driver fixed 2026-08, was "training length") `:538` · **Bigger Means More — Carlini Fig 1(a) (real fig; replaced SVG 2026-09)** `:551` · **Duplication Is the Big One — Kandpal Fig 1 (real fig; replaced SVG 2026-09)** + ~1000× line `:567` · long tail of duplicates + **Kandpal Fig 3(a) (real fig)** `:583` · **A Predictable Curve — Carlini Fig 1 (real fig)** `:600` · **Reading the Curves (added 2026-09; GPT-J ≥1% + log-linear SVG)** `:612` |
| **04 — Image & Diffusion Models** | 36–42 | `:651` | not just text + **Somepalli Fig 1 pairs (real fig)** `:660` · diffusion picture `:675` · **Ann Graham Lotz copy (real fig; 94/175M added 2026-08)** `:688` · **duplication histogram (real fig; Somepalli cite removed 2026-08)** `:708` · Somepalli ~1.9% near-duplicates + **Somepalli Fig 5 histograms (real fig)** `:720` |
| **05 — Copyright & the Law** | 43–45 | `:743` | **compressed 6→2 slides 2026-08** (backup copyright deck owns the topic) · NYT v. OpenAI + **complaint p. 30 side-by-side (real fig; replaced SVG 2026-09)** + Mar 2025 MTD ruling `:752` · Copy or Transform? (fair-use collision + Bartz v. Anthropic $1.5B) `:764` |
| **06 — Mitigations & Frontier** | 46–58 | `:779` | toolbox `:788` · deduplication (Lee ACL 2022) + **Lee Fig 3 / Fig 2 (real figs)** `:801` · dedup limits + near-duplicate SVG `:817` · output filtering + n-gram-filter SVG `:841` · DP + **VaultGemma Fig 1 (real fig)** `:871` · privacy tax + trade-off SVG `:887` · no silver bullet `:913` · **Frontier: Whole Books Come Back (Cooper 2025 Fig 3, real fig)** `:921` · **Frontier: Chatbots Recite Books Too (Ahmed 2026 Fig 1, real fig; split out 2026-09)** `:936` · **Frontier: How Much Fits? (Morris Fig 1, real fig; 3.6 bits/param)** `:952` · memorized PII + PII-pipeline SVG `:969` · open problems `:1004` |
| Takeaways / Closer | 59–60 | — | `:1017`, `:1029` |

**Key definitions / citations (all source-verified 2026-08):**
- $k$-extractable (Def 3.1), scaling drivers (capacity / duplication / context), GPT-J ≥1% —
  `:140`, `:538`, `:600` — Carlini et al., "Quantifying Memorization Across Neural Language
  Models", ICLR 2023 (arXiv 2202.07646).
- GPT-2 extraction, Fig 1 PII, 604 of 1,800 candidates — `:350`, `:370` — Carlini et al.,
  "Extracting Training Data from Large Language Models", USENIX Security 2021 (arXiv 2012.07805).
- Secret Sharer canary/exposure — `:225` — Carlini, Liu, Erlingsson, Kos, and Song,
  USENIX Security 2019 (arXiv 1802.08232).
- Extractable vs discoverable (Defs 1–2); poem attack; 10,000+ strings / $200 / 150× —
  `:169`, `:432`, `:469` — Nasr et al., "Scalable Extraction of Training Data from (Production)
  Language Models", arXiv 2311.17035 (2023; published at ICLR 2025 as "…from Aligned,
  Production Language Models").
- Learning requires memorization (long tail) — `:210` — Feldman, STOC 2020.
- Superlinear duplication effect (10 copies → ~1000× more generation) — `:567` — Kandpal,
  Wallace, and Raffel, ICML 2022 (arXiv 2202.06539).
- Deduplication (10× less memorized text) — `:801` — Lee et al., "Deduplicating Training Data
  Makes Language Models Better", ACL 2022 (arXiv 2107.06499).
- Diffusion extraction: Ann Graham Lotz Fig 1, 94 images / 175M generations, Fig 5 duplication
  histogram (most extracted ≥100 dupes) — `:688`, `:708` — Carlini et al., "Extracting Training
  Data from Diffusion Models", USENIX Security 2023 (arXiv 2301.13188).
- ~1.9% near-duplicate generations — `:720` — Somepalli et al., "Diffusion Art or Digital
  Forgery?", CVPR 2023 (arXiv 2212.03860; paper reports 1.88% at similarity >0.5).
- NYT v. OpenAI — `:752` — S.D.N.Y., filed Dec 2023; motion to dismiss largely denied
  Mar 26, 2025 (opinion Apr 4, 2025).
- Bartz v. Anthropic $1.5B settlement — `:764` — N.D. Cal.; preliminary approval Sept 25, 2025
  (matches `courses/privacy/lectures/03-memorization/` anchor).
- Whole-book extraction — `:921`, `:936` — Cooper et al., arXiv 2505.12546 (Llama 3.1 70B / Harry
  Potter); Ahmed, Cooper, Koyejo, and Liang, "Extracting books from production language
  models", arXiv 2601.02671 (2026).
- Capacity ≈3.6 bits/parameter — `:952` — Morris et al., "How Much Do Language Models
  Memorize?", arXiv 2505.24832 (2025).

**Real images** (`figs/`, cropped + cited; 26 image slots after the 2026-09 figure pass):
Cooper discoverable-extraction `figs/cooper-discoverable-extraction.png` (Cooper 2025 Fig 1 left) `:119`;
Feldman SUN long tail `figs/feldman-long-tail.png` (Feldman 2020 Fig 1(a)) `:214`; Secret Sharer NMT
insertions `figs/secret-sharer-fig6-insertions.png` (Fig 6) `:235` and exposure-vs-epoch
`figs/secret-sharer-fig7-epochs.png` (Fig 7) `:283`; GPT-2 extraction `figs/gpt2-extraction.png`
(Carlini 2021 Fig 1) `:354`; zlib-vs-perplexity `figs/carlini-zlib-perplexity.png` (Carlini 2021 Fig 3)
`:405`; 604-example categories `figs/carlini-extraction-categories.png` (Carlini 2021 Table 1) `:422`;
poem-attack screenshot `figs/nasr-poem-chatgpt.png` (Nasr 2023 Fig 5) `:441`; emission-rate bars
`figs/nasr-emission-rate.png` (Nasr Fig 1; shared with `lec02-privacy-dp.html`) `:479`; extrapolation
`figs/nasr-extrapolation.png` (Nasr Fig 9 left) `:492`; Carlini ICLR 2023 Fig 2(a,b)
`figs/carlini-quantifying-fig2ab.png` `:527`, Fig 1(a) `figs/carlini-quantifying-fig1a.png` `:555`,
Fig 1 `figs/carlini-quantifying-fig1.png` `:604`; Kandpal Fig 1 `figs/kandpal-duplicates.png` `:571`
and Fig 3(a) `figs/kandpal-dup-histogram.png` `:593`; Somepalli Fig 1 pairs `figs/somepalli-pairs.png`
`:664` and Fig 5 histograms `figs/somepalli_histograms.png` (shared with lec02) `:724`; Ann Graham Lotz
copy `figs/calrini-ann.png` (Carlini USENIX Sec 2023 Fig 1) `:692`; duplication histogram
`figs/carlini_duplicates.png` (Carlini USENIX Sec 2023 Fig 5; shared with `lec03-mia.html`) `:712`;
NYT complaint p. 30 `figs/nyt-complaint-p30.png` (shared with lec02) `:756`; Lee dedup
`figs/lee-dedup-memorization.png` (Fig 3) `:805` and `figs/lee-dedup-perplexity.png` (Fig 2) `:806`;
VaultGemma `figs/vaultgemma-memorization.png` (Fig 1; shared with lec02) `:880`; Cooper books
`figs/cooper-books-fig3.png` (Fig 3) `:925`; Ahmed Harry Potter recall `figs/ahmed-harry-potter.png`
(Fig 1) `:940`; Morris capacity `figs/morris-capacity.png` (Fig 1) `:956`.
**SVG figures:** pattern-vs-copy `:89`, $k$-extractable test `:144`, loss bars `:191`, canary-leak
pipeline `:258`, pattern-vs-record `:305`, canary-vs-wild `:332`, extraction pipeline `:374`, poem
loop-break `:452`, log-linear schematic `:620`, diffusion noise→image strip `:675` (diagram-flow),
near-duplicate dedup `:826`, n-gram output filter `:849`, privacy/accuracy trade-off `:896`, PII
pipeline `:978`. Citations use `.cite-left` with figure numbers. Page number: bold `.slide-num` only.

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

**Topic:** Machine unlearning (~90 min). Why deletion is demanded (GDPR/CCPA privacy,
copyright, safety); retraining as the gold standard; exact vs approximate; the
$(\varepsilon,\delta)$ yardstick at intuition level; SISA as a picture; influence
functions and the Hessian wall; gradient ascent, its failure modes, and NPO;
LLM unlearning (Harry Potter, TOFU, WMDP/RMU, MUSE); verification (MIA audit, IDI,
relearning, quantization recovery); the position-paper debate and the 2025–26
frontier. Intuition pass — the rigorous treatment lives in
`courses/privacy/lectures/05-unlearning/` (authoritative for shared facts); the
position-paper debate expands in `talks/icml2026/`.

### Sections (67 slides, ~90 min — content-revised 2026-08 from 58, figure pass 2026-09-05 added RMU, Measured)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:31`, `:43` | |
| **01 — Why Delete?** | 3–11 | `:76` | user changes mind (SVG) `:84` · GDPR Art. 17 `:118` · **Delete for Three Reasons (privacy / copyright / safety; added 2026-08)** `:131` · **data lives in the weights (SVG)** `:144` · why not ignore (SVG) `:169` · retraining expensive (SVG) `:200` · enter machine unlearning (Cao & Yang) `:232` · a decade of work (+Cooper arXiv-count chart) `:244` |
| **02 — What Unlearning Means** | 12–19 | `:264` | gold standard = retrain `:272` · **two-models diagram (SVG)** `:284` · exact (SVG) `:310` · approximate (SVG) `:336` · **DP yardstick (Guo/Sekhari cite fixed 2026-08; SVG)** `:367` · forget/retain split (SVG strip) `:396` · two things to get right `:421` |
| **03 — How to Unlearn** | 20–34 | `:434` | retraining baseline `:442` · train in pieces (SISA shard SVG) `:455` · **SISA (real Bourtoule Fig 2)** `:496` · deleting in SISA (SVG) `:515` · slices (SVG) `:562` · tradeoff (+Bourtoule Fig 6) `:597` · edit the weights `:614` · influence functions (+Koh & Liang Fig 2) `:627` · Hessian catch (SVG) `:644` · gradient ascent (SVG) `:677` · ascent wrecks (+Kurmanji Fig 6) `:710` · **A Gentler Push: NPO (real fig; added 2026-08)** `:727` · method landscape `:739` · Colab `:751` |
| **04 — Unlearning in LLMs** | 35–47 | `:767` | what do we forget `:775` · no single row (SVG) `:788` · Harry Potter (+1 GPU hour; Eldan Fig 3) `:825` · the result (Eldan Fig 1 table) `:844` · **TOFU (200×20=4,000; +Fig 6)** `:856` · **TOFU in One Picture (real fig; added 2026-08)** `:872` · why fictitious (SVG) `:883` · **WMDP (real fig + 3,668 MCQs; reworked 2026-08)** `:916` · RMU (+loss Fig 7) `:936` · **RMU, Measured (Fig 8, Zephyr-7B; added 2026-09)** `:952` · **MUSE: Six Boxes to Tick (real fig; added 2026-08)** `:971` · unlearning vs filtering (+Cooper back-end/front-end) `:983` |
| **05 — Did It Really Forget?** | 48–56 | `:1002` | verification is hard (SVG) `:1010` · MIA audit (+MUSE Fig 2) `:1043` · **the tell persists (SVG)** `:1060` · **Look Inside: IDI (real fig, Yonsei; added 2026-08)** `:1080` · relearning attacks (+Yoon syntax Fig 5, Yonsei) `:1092` · **Relearning, Measured (real fig; added 2026-08)** `:1109` · **Quantize, and It Comes Back (21%→83%; +Zhang Fig 1)** `:1121` · dormant, not deleted (+Łucki Fig 1) `:1137` |
| **06 — Frontier 2025–26** | 57–65 | `:1150` | **"overused" critique (+Yoon/Jun/No cite; taxonomy SVG)** `:1158` · **Does It Do What You Think? (position papers; added 2026-08)** `:1191` · what guarantee holds `:1204` · **robust unlearning (+Łucki Fig 2)** `:1217` · evaluation standards (+MUSE Fig 5) `:1234` · unlearning meets privacy (+onion-effect ROC) `:1253` · open problems `:1271` · where to go deeper `:1285` |
| Takeaways / Closer | 66–67 | — | `:1296`, `:1309` |

**Key definitions / citations (all source-verified 2026-08):**
- First "machine unlearning" — `:232` — Cao and Yang, IEEE S&P 2015.
- Exact deletion definition — `:244` — Ginart, Guan, Valiant, and Zou, NeurIPS 2019
  (arXiv 1907.05012). **No longer cited for the $(\varepsilon,\delta)$ definition** —
  that was a misattribution, fixed 2026-08 on `:367` and in `lec05tech.html`.
- $(\varepsilon,\delta)$-unlearning — `:367` — Guo, Goldstein, Hannun, and van der Maaten,
  "Certified Data Removal from Machine Learning Models", ICML 2020 (arXiv 1911.03030);
  Sekhari et al., NeurIPS 2021. Matches privacy deck Def 3.
- SISA — `:496` — Bourtoule et al., "Machine Unlearning", IEEE S&P 2021. Speedup:
  sharding cuts expected cost by the shard count; slicing saves at most another 3/2
  (matches privacy deck Prop 3; tech deck's "R·L" claim fixed 2026-08).
- Influence functions — `:627` — Koh and Liang, ICML 2017.
- Gradient ascent / unrolling — `:677` — Thudi et al., "Unrolling SGD", IEEE EuroS&P 2022.
- Ascent wrecks / retain anchor — `:710` — Kurmanji, Triantafillou, Hayes, and
  Triantafillou, "Towards Unbounded Machine Unlearning" (SCRUB), NeurIPS 2023.
- NPO — `:727` — Zhang, Lin, Bai, and Mei, "Negative Preference Optimization", COLM 2024.
- Who's Harry Potter (~1 GPU hour, Llama-2-7b) — `:825` — Eldan and Russinovich, 2023
  (arXiv 2310.02238).
- TOFU (200 authors × 20 QA = 4,000) — `:856` — Maini, Feng, Schwarzschild, Lipton,
  and Kolter, COLM 2024 (arXiv 2401.06121).
- WMDP (3,668 MCQs) + RMU — `:916`, `:936`, `:952` — Li et al., ICML 2024 (arXiv 2403.03218).
- MUSE (six criteria) — `:971` — Shi, Wang, Li, et al., ICLR 2025 (arXiv 2407.06460).
- IDI (instructor co-author) — `:1080` — Jeon, Jeung, Kim, No, and Choi (Yonsei),
  "An Information Theoretic Evaluation Metric For Strong Unlearning", AAAI 2026
  (arXiv 2405.17878).
- Syntax drives relearning (instructor co-author) — `:1092` — Yoon, Hong, Jeung, and No
  (Yonsei), "Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning
  Failures", ICLR 2026.
- Benign relearning — `:1109` — Hu, Fu, Wu, and Smith, "Unlearning or Obfuscating?",
  ICLR 2025 (arXiv 2406.13356).
- Quantization recovery (21%→83% after 4-bit) — `:1121` — Zhang et al., "Catastrophic
  Failure of LLM Unlearning via Quantization", ICLR 2025 (arXiv 2410.16454).
- Adversarial perspective (10 unrelated examples undo RMU) — `:1137`, `:1217` — Łucki et al.,
  TMLR 2025 (arXiv 2409.18025).
- Privacy onion effect — `:1253` — Carlini et al., "The Privacy Onion Effect: Memorization
  is Relative", NeurIPS 2022.
- Position papers — `:244`, `:983`, `:1158`, `:1191` — Cooper et al., "Machine Unlearning Doesn't Do What
  You Think", NeurIPS 2025; Yoon, Jun, and No (Yonsei), "Position: 'Machine Unlearning'
  Is Overused in LLMs", ICML 2026 (matches `courses/privacy/lectures/05-unlearning/`
  and `talks/icml2026/`).

**Real images** (`figs/`, cropped + cited). From the 2026-08 pass (copied from
`courses/privacy/lectures/05-unlearning/figs/`): NPO vs GA collapse curves
`figs/npo-ga-collapse.png` (Zhang COLM 2024 Fig 2) `:733`; TOFU pipeline
`figs/tofu.png` (Maini COLM 2024 Fig 1) `:877`; WMDP overview `figs/WMDP.png`
(Li ICML 2024 Fig 1) `:923`; MUSE six-way evaluation `figs/MUSE.png` (Shi ICLR 2025
Fig 1) `:977`; IDI conceptual layer plot `figs/idi-conceptual.png` (Jeon AAAI 2026
Fig 4(a)) `:1086`; benign-relearning pipeline `figs/benign-relearn-pipeline.png`
(Hu ICLR 2025 Fig 2 left) `:1115`. **Added 2026-09-05 figure pass:** arXiv unlearning
counts `figs/unlearning-arxiv-counts.png` (Cooper 2024 Fig 2) `:256`; SISA training
`figs/sisa-training.png` (Bourtoule S&P 2021 Fig 2) `:503`; accuracy vs shards
`figs/sisa-accuracy-shards.png` (Bourtoule Fig 6) `:609`; influence vs leave-one-out
`figs/influence-vs-loo.png` (Koh & Liang ICML 2017 Fig 2) `:638`; ascent-only and
alternating error curves `figs/scrub-maxsteps-only.png` + `figs/scrub-alternating.png`
(Kurmanji NeurIPS 2023 Fig 6(a)/(d)) `:721`–`:722`; HP next-token table
`figs/hp-nexttoken.png` (Eldan 2023 Fig 3) `:832`; HP completions
`figs/hp-completions.png` (Eldan Fig 1) `:850`; forget quality vs utility
`figs/tofu-fq-vs-utility.png` (Maini COLM 2024 Fig 6) `:867`; RMU loss
`figs/rmu-loss.png` (Li ICML 2024 Fig 7) `:947`; RMU results
`figs/rmu-results.png` (Li Fig 8) `:959`; back-end/front-end
`figs/backend-frontend.png` (Cooper Fig 3) `:989`; MIA distributions
`figs/muse-mia-dist.png` (Shi ICLR 2025 Fig 2) `:1054`; syntax similarity
`figs/syntax-similarity.png` (Yoon ICLR 2026 Fig 5, Yonsei) `:1103`; quantization
recovery `figs/quant-recovery.png` (Zhang ICLR 2025 Fig 1) `:1132`; adversarial
overview `figs/lucki-overview.png` (Łucki TMLR 2025 Fig 1) `:1143`; fine-tune recovery
`figs/lucki-finetune.png` (Łucki Fig 2) `:1228`; utility vs memorization
`figs/muse-utility-vs-mem.png` (Shi Fig 5) `:1246`; onion ROC `figs/onion-roc.png`
(Carlini NeurIPS 2022 Fig 1) `:1265`. **SVG figures:** database row vs weights `:96`,
data-in-weights `:150`, MIA/extraction probes `:181`, daily-retrain timeline `:212`,
two-models-compared `:290`, identical distributions `:322`, weight-space nudge `:348`,
bounded-gap distributions `:379`, forget/retain strip `:402`, SISA shard diagram (moved
from the SISA slide) `:467`, one-shard retrain `:527`, slices + checkpoints `:573`,
Hessian grid `:656`, descent vs ascent loss curve `:689`, paraphrase entanglement
`:800`, web vs fine-tune source `:895`, three-probe verification `:1022`,
member/non-member bells `:1066`, data-level vs output-level taxonomy `:1170`.
Citations use `.cite-left`. Page number: bold `.slide-num` only.

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
Sekhari 2021 (main `:367` and `lec05tech.html` slide 4, which also gained the
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
argument at intuition level); real harms (Lacey v. State Farm as anchor case — Mata v.
Avianca lives in lec01, one-line callback only); calibration with the reliability-diagram
picture and a glanceable ECE; conformal prediction as "sets with a coverage promise";
semantic entropy at intuition level; RAG grounding; benchmarks (TruthfulQA, Vectara HHEM);
reasoning-model hallucination; sycophancy one-slide touchpoint (full treatment in
`backup-sycophancy.html`). Math lives in `lec06tech.html`.

### Sections (65 slides, ~90 min — content-revised 2026-08 from 55; figure pass 2026-09 from 61; all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — The Train-Time Threat** | 3–9 | `:77` | two places to attack (SVG) `:85` · inference-time (SVG) `:102` · train-time (SVG) `:120` · pipeline cracks (SVG) `:138` · supply chain (Gu Fig 1) `:162` · hard to catch (SVG) `:179` |
| **02 — Data Poisoning** | 10–19 | `:198` | two goals (SVG) `:206` · availability (Biggio Fig 3) `:223` · SVM poisoning (Biggio Fig 1) `:240` · boundary tilt (SVG) `:256` · targeted (SVG) `:280` · clean-label (Frogs Fig 6a) `:298` · **Poison Frogs (Frogs Fig 1; one poison image, transfer setting; verified 2026-08)** `:315` · feature collision (SVG) `:333` · **Collision, Measured (Frogs Fig 3b; added 2026-09)** `:355` |
| **03 — Backdoors and Triggers** | 20–28 | `:368` | backdoor idea (SVG) `:376` · BadNets (Gu Fig 3) `:394` · **trigger pipeline (Gu Fig 7 capture, verified)** `:411` · clean accuracy stays high (Gu Fig 6) `:423` · two numbers (Gu Fig 4) `:440` · **stop sign (Gu Fig 8; Post-it, >90% flip, 95% confidence; fixed 2026-08)** `:458` · subtle triggers (SVG) `:475` · why it works (SVG) `:493` |
| **04 — Web-Scale Poisoning** | 29–38 | `:512` | where big data comes from (SVG) `:520` · **Poisoning Is Practical (Carlini Fig 1; $60, 10 datasets; fixed 2026-08)** `:538` · split-view (SVG) `:555` · frontrunning (Carlini Fig 6) `:581` · **tiny fraction (0.01% of LAION-400M ≈ $60; fixed 2026-08)** `:598` · **Few Datasets Ship a Hash (Carlini Table 1; added 2026-09)** `:608` · no insider (SVG) `:620` · **Glaze (Fig 8; added 2026-08)** `:638` · **Nightshade (Fig 7; added 2026-08)** `:655` |
| **05 — Backdoors in Language Models** | 39–48 | `:673` | tuning is a new target (SVG) `:681` · **Poisoned Instructions (Wan Fig 5; ICML 2023, ~100 examples; fixed 2026-08)** `:699` · text trigger (Wan Fig 1) `:716` · **How Much Poison Is Needed? (added 2026-08)** `:732` · **The Two Experiments (Souly Fig 1; added 2026-09)** `:746` · **250 Documents Are Enough (Souly Fig 2 replaces the hand-drawn SVG; added 2026-08)** `:761` · **Sleeper Agents (Hubinger Fig 1; 2023/2024 code trigger; fixed 2026-08)** `:773` · safety training misses it (Hubinger Fig 2) `:790` · why LLMs exposed (SVG) `:807` |
| **06 — Defenses, Frontier 2025–26** | 49–62 | `:826` | two lines of defense (SVG) `:834` · **Defending the Pipeline (SVG; hashes + randomized snapshots; added 2026-08)** `:851` · spectral signatures (Tran Fig 3) `:871` · outlier picture (SVG) `:888` · **The Signature, Measured (Tran Fig 1; added 2026-09)** `:908` · activation clustering (Chen Fig 2) `:920` · Neural Cleanse (Wang Fig 1) `:936` · fine-pruning (Liu Fig 4) `:952` · demo (SVG) `:968` · never final (SVG) `:1001` · **Related Threat: Model Stealing (Tramèr Fig 1; added 2026-08)** `:1019` · **Frontier 2025–26 (SVG; rewritten 2026-08)** `:1036` |
| Takeaways / Closer | 63–65 | — | what to remember `:1054` · key takeaway `:1068` · closer `:1076` |

**Key definitions / citations (all source-verified 2026-08; figure numbers checked against the PDFs 2026-09):**
- SVM poisoning (first formal study) — `:236` (Fig 3), `:252` (Fig 1) — Biggio, Nelson, and Laskov,
  "Poisoning Attacks against Support Vector Machines", ICML 2012.
- Poison Frogs clean-label attack (one poison image suffices in the
  transfer-learning test) — `:311` (Fig 6a), `:329` (Fig 1), `:363` (Fig 3b) — Shafahi et al., NeurIPS 2018.
- BadNets (trigger stickers, >90% stop signs → speed-limit, real photo fooled at
  95% confidence, clean accuracy level with baseline) — `:175` (Fig 1), `:407` (Fig 3), `:419` (Fig 7),
  `:436` (Fig 6), `:454` (Fig 4), `:471` (Fig 8) — Gu, Dolan-Gavitt, and Garg, 2017 (arXiv 1708.06733).
- Web-scale poisoning ($60 buys 0.01% of LAION-400M; split-view = expired
  domains; frontrunning = snapshot timing; defenses = integrity hashes +
  randomized snapshots) — `:551` (Fig 1), `:577`, `:594` (Fig 6), `:604`, `:616` (Table 1), `:867` — Carlini et
  al., IEEE S&P 2024.
- Glaze (style cloak, >92% mimicry disruption) — `:651` (Fig 8) — Shan et al., USENIX
  Security 2023.
- Nightshade (<100 samples corrupt one SDXL prompt) — `:668` (Fig 7) — Shan et al.,
  IEEE S&P 2024.
- Instruction-tuning poisoning (~100 examples skew hundreds of tasks; larger
  models more vulnerable) — `:712` (Fig 5), `:728` (Fig 1) — Wan, Wallace, Shen, and Klein, ICML 2023.
- Near-constant poison count (~250 documents backdoor 600M–13B models,
  Chinchilla-optimal 6B–260B tokens; 20× more clean data does not raise the
  bar) — `:742`, `:757` (Fig 1), `:769` (Fig 2) — Souly et al., 2025 (arXiv 2510.07192; UK AI Security
  Institute, Anthropic, Alan Turing Institute).
- Sleeper agents (2023 secure / 2024 exploitable code; survives SFT, RL, and
  adversarial training; largest models most persistent) — `:786` (Fig 1), `:803` (Fig 2) —
  Hubinger et al., 2024 (arXiv 2401.05566). Distinct from Souri et al.
  "Sleeper Agent" (not referenced here).
- Spectral signatures — `:884` (Fig 3), `:916` (Fig 1) — Tran, Li, and Madry, NeurIPS 2018.
- Activation clustering — `:932` (Fig 2) — Chen et al., 2018 (arXiv 1811.03728).
- Neural Cleanse — `:948` (Fig 1) — Wang et al., IEEE S&P 2019.
- Fine-pruning — `:964` (Fig 4) — Liu, Dolan-Gavitt, and Garg, RAID 2018.
- Model stealing — `:1032` (Fig 1) — Tramèr, Zhang, Juels, Reiter, and Ristenpart,
  USENIX Security 2016.

**Figures (28 cited crops in `figs/`, 2026-09 figure pass):** `badnets-approaches.png` (Gu Fig 1) `:173` · `biggio-multipoint.png` (Biggio Fig 3) `:234` · `biggio-gradient-attack.png` (Biggio Fig 1) `:250` · `frogs-schematic.png` (Frogs Fig 6a) `:309` · `frogs-transfer-attack.png` (Frogs Fig 1) `:327` · `frogs-feature-b.png` (Frogs Fig 3b) `:360` · `badnets-mnist-triggers.png` (Gu Fig 3) `:405` · `badnets-trigger.png` (Gu Fig 7) `:416` · `badnets-error-vs-poison.png` (Gu Fig 6) `:434` · `badnets-confusion.png` (Gu Fig 4) `:451` · `badnets-real-stopsign.png` (Gu Fig 8) `:469` · `carlini-cost.png` (Carlini Fig 1) `:549` · `carlini-wiki-cdf.png` (Carlini Fig 6) `:592` · `carlini-datasets-table.png` (Carlini Table 1) `:613` · `glaze-results.png` (Glaze Fig 8) `:649` · `nightshade-outputs.png` (Nightshade Fig 7) `:666` · `wan-trigger-phrases.png` (Wan Fig 5) `:710` · `wan-overview.png` (Wan Fig 1) `:726` · `souly-overview.png` (Souly Fig 1) `:751` · `souly-constant-count.png` (Souly Fig 2) `:766` · `sleeper-setup.png` (Hubinger Fig 1) `:784` · `sleeper-code-vuln.png` (Hubinger Fig 2) `:801` · `spectral-pipeline.png` (Tran Fig 3) `:881` · `spectral-histograms.png` (Tran Fig 1) `:913` · `actclust-pca.png` (Chen Fig 2) `:930` · `cleanse-illustration.png` (Wang Fig 1) `:946` · `finepr-activations.png` (Liu Fig 4) `:962` · `tramer-extraction.png` (Tramèr Fig 1) `:1030`.
Inline SVG (23): two places `:95` · inference-time `:113` · train-time `:131` · pipeline cracks `:143` · hard to catch `:190` · two goals `:215` · boundary tilt `:261` · targeted `:291` · feature collision `:338` · backdoor idea `:387` · subtle triggers `:486` · why it works `:504` · where big data `:531` · split-view `:560` · no insider `:631` · tuning target `:692` · LLMs exposed `:818` · two lines `:843` · defending pipeline `:862` · spectral outlier `:893` · demo `:982` · never final `:1012` · frontier `:1046`. Citations use
`.cite-left`. Page number: bold `.slide-num` only.

**2026-09 figure pass (61→65):** 27 new cited crops (figure numbers checked against each PDF; `carlini-cost.png` re-cropped) and 16 new inline SVGs; the hand-drawn poison-count sketch on 250 Documents replaced by Souly Fig 2. Added 4 slides: Collision, Measured (Frogs Fig 3b), Few Datasets Ship a Hash (Carlini Table 1, split out of Tiny Fraction to avoid cite overlap), The Two Experiments (Souly Fig 1, split out of How Much Poison), The Signature, Measured (Tran Fig 1). the uncropped full-Fig-3 file frogs-feature-space.png removed. Note file: +4 articles, 44 "Slide figure" lines.

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
**2026-08 note enrichment:** `lec09-poisoning-note.html` upgraded from speaker script
(383 lines) to Script &amp; Companion Notes (677 lines; 61 entries unchanged): per-entry
`.detail` blocks with rigorous definitions (poisoning threat model, poison budget α,
availability/targeted/backdoor taxonomy, clean vs dirty label, x⊕t trigger operator,
CA/ASR, split-view & frontrunning mechanics, ε-spectral separability Def 3.1, Neural
Cleanse A(x,m,Δ) + MAD index, fine-pruning), theorems with proofs or labeled verified
sketches (Biggio bilevel/KKT gradient vs arXiv 1206.6389; Poison Frogs Eq 1 +
forward-backward splitting vs arXiv 1804.00792; BadNets λ-blend + numbers vs arXiv
1708.06733; Tran Lemmas 3.1–3.3 Chebyshev sketch vs arXiv 1811.00636; Souly 250-doc
numbers vs arXiv 2510.07192 + Anthropic blog; Tramèr d+1 equation-solving vs arXiv
1609.02943; general bilevel form, 40,000-image arithmetic, defense-evasion synthesis
labeled course notes), and 16 verified links (all 200; Neural Cleanse PDF via Internet
Archive; Tay via Microsoft blog).

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

### Sections (60 slides, ~90 min — content-revised 2026-08 from 54; figure pass 2026-09 from 57, all citations source-verified)

| Section | Slides | Divider line | Notable slides |
|---|---|---|---|
| Title / Contents | 1–2 | `:32`, `:44` | |
| **01 — Safety Training** | 3–12 | `:81` | raw model (SVG) `:89` · two goals (SVG) `:126` · instruction tuning (Ouyang Fig 2) `:155` · RLHF (SVG, Ouyang) `:175` · **InstructGPT, Measured (Ouyang Fig 1 win rate; added 2026-09)** `:203` · optimize against reward (SVG) `:224` · Constitutional AI (Bai Fig 1) `:258` · refusal behavior (SVG) `:274` · it mostly works (SVG) `:306` |
| **02 — Why It Is Fragile** | 13–20 | `:341` | thin layer (SVG) `:349` · Shallow Alignment (Qi ICLR 2025) `:384` · **Shallow, Measured (Qi Fig 1 per-token KL; added 2026-09)** `:408` · Two Failure Modes (Wei Fig 1 capture) `:429` · competing objectives (SVG) `:444` · mismatched generalization (SVG) `:479` · Refusal Is a Direction (Arditi Fig 1) `:500` |
| **03 — Manual Jailbreaks** | 21–26 | `:522` | what a jailbreak is (SVG) `:530` · persona play (SVG) `:571` · fake authority (SVG) `:607` · obfuscation (SVG) `:642` · manual is brittle (SVG) `:685` |
| **04 — Automated Jailbreaks** | 27–34 | `:730` | from art to optimization (SVG) `:738` · the target (SVG) `:781` · GCG (Zou Fig 2 ASR panel; 99/100 on Vicuna-7B) `:821` · search loop (SVG) `:842` · Search in Token Space (GCG Fig 1 capture) `:883` · It Transfers (Zou Fig 3; 84% GPT-3.5/4, 66% PaLM-2, ~2% Claude) `:894` · PAIR (Chao Fig 2, <20 queries) `:915` |
| **05 — Scaling the Attack** | 35–41 | `:936` | many-shot (SVG, Anil) `:944` · Power-Law Curve (MSJ Fig 1 capture) `:988` · Low-Resource Languages (Yong Fig 1; ~79% on GPT-4) `:1000` · **Which Languages Break Through (Yong Table 1; added 2026-09)** `:1017` · cipher prompts (CipherChat Fig 2; cite added 2026-09) `:1038` · Fine-Tuning Removes Safety (Qi ICLR 2024 Fig 1) `:1059` |
| **06 — One Unifying View** | 42–46 | `:1080` | adversarial examples (Szegedy Fig 5) `:1088` · same idea in text (SVG) `:1108` · crossing the boundary (SVG) `:1145` · the hard lesson (SVG) `:1167` |
| **07 — Defenses & Frontier** | 47–58 | `:1209` | Red-Teaming: Attack to Defend (Ganguli Fig 1) `:1217` · Red-Teaming at Scale (Perez Fig 1) `:1233` · defense in layers (SVG) `:1254` · filters (SVG) `:1289` · system-prompt hardening (SVG) `:1330` · Constitutional Classifiers (Sharma Fig 1) `:1366` · Circuit Breakers (Zou NeurIPS 2024 Fig 1) `:1387` · demo (SVG) `:1408` · cat-and-mouse (SVG) `:1450` · not solved (SVG) `:1471` · Frontier 2025-26 (Hughes BoN Fig 3) `:1504` |
| Takeaways / Closer | 59–60 | — | key takeaways `:1526` · closer `:1539` |

**Key definitions / citations (all source-verified 2026-08; cite-line pointers 2026-09):**
- InstructGPT (instruction tuning + RLHF) — `:171`, `:199`, `:220` — Ouyang et al., NeurIPS 2022 (Fig 2 pipeline, Fig 1 win rate).
- Constitutional AI (AI feedback, self-critique) — `:270` — Bai et al., 2022 (arXiv 2212.08073; Fig 1).
- Shallow safety alignment ("first few output tokens") — `:404`, `:425` — Qi et al., "Safety
  Alignment Should Be Made More Than Just a Few Tokens Deep", ICLR 2025 (Outstanding Paper; Fig 1 per-token KL).
- Two failure modes (competing objectives; mismatched generalization) — `:440`, `:475`,
  `:496` — Wei, Haghtalab, Steinhardt, "Jailbroken: How Does LLM Safety Training Fail?",
  NeurIPS 2023 (Fig 1: GPT-4 competing-objectives, Claude v1.3 base64 mismatched-gen).
- Refusal is a one-dimensional direction (13 models ≤72B) — `:517` — Arditi et al.,
  "Refusal in Language Models Is Mediated by a Single Direction", NeurIPS 2024 (Fig 1).
- GCG (universal + transferable; 99/100 harmful behaviors Vicuna-7B, 88% Harmful
  Strings; transfer 84% GPT-3.5/GPT-4, 66% PaLM-2, ~2.1% Claude) — `:838`, `:879`, `:890`,
  `:911` — Zou et al., "Universal and Transferable Adversarial Attacks on Aligned
  Language Models", 2023 (arXiv 2307.15043; Fig 1 = ChatGPT/Claude/Bard/Llama-2; Fig 2 optimizer comparison; Fig 3 transfer).
- PAIR (jailbreak in <20 queries) — `:931` — Chao et al., 2023 (arXiv 2310.08419; Fig 2).
- Many-shot jailbreaking (power-law in shots; more effective on larger models) — `:984`,
  `:996` — Anil et al., NeurIPS 2024 (Fig 1 = the three-panel plot capture).
- Low-resource-language jailbreak (~79% on GPT-4; Table 1 by resource level) — `:1013`, `:1034` — Yong, Menghini, Bach, 2023
  (arXiv 2310.02446).
- Cipher/CipherChat (~100% bypass in some domains) — `:1055` — Yuan et al., "GPT-4 Is Too Smart To Be Safe", ICLR 2024
  (Fig 2; cite added 2026-09).
- Fine-tuning compromises safety (10 examples, <$0.20 on GPT-3.5 Turbo; benign
  fine-tuning also degrades) — `:1075` — Qi et al., ICLR 2024 (arXiv 2310.03693, Oral; Fig 1).
- Adversarial examples origin — `:1104` — Szegedy et al., ICLR 2014 (Fig 5).
- Human red-teaming (38,961-attack dataset; RLHF harder to break with scale) — `:1229` —
  Ganguli et al., 2022 (arXiv 2209.07858; Fig 1).
- Automated red-teaming (LM attacks LM, tens of thousands of offensive replies) —
  `:1250` — Perez et al., EMNLP 2022 (Fig 1).
- Constitutional Classifiers (3,000+ red-team hrs, no universal jailbreak; +0.38%
  refusals, ~24% inference overhead) — `:1383` — Sharma et al. (Anthropic), 2025
  (arXiv 2501.18837; Fig 1).
- Circuit breakers / representation rerouting — `:1404` — Zou et al., "Improving
  Alignment and Robustness with Circuit Breakers", NeurIPS 2024 (arXiv 2406.04313; Fig 1).
- Best-of-N jailbreaking (power-law ASR; 89% GPT-4o, 78% Claude 3.5 Sonnet @ N=10k) —
  `:1522` — Hughes et al., 2024 (arXiv 2412.03556; Fig 3).

**Figures (21 real, 28 inline SVG):** `figs/ouyang-3steps.png` (Ouyang Fig 2) `:155`;
`figs/ouyang-winrate.png` (Ouyang Fig 1) `:203`; `figs/bai-cai.png` (Bai Fig 1) `:258`;
`figs/qishallow-kl.png` (Qi ICLR 2025 Fig 1) `:408`; `figs/wei-jailbroken.png` (Wei Fig 1) `:429`;
`figs/arditi-refusal.png` (Arditi Fig 1) `:500`; `figs/gcg-asr.png` (Zou Fig 2, ASR panel) `:821`;
`figs/gcg-schematic.png` (Zou Fig 1) `:883`; `figs/gcg-transfer.png` (Zou Fig 3) `:894`;
`figs/pair-schematic.png` (Chao Fig 2) `:915`; `figs/msj-powerlaw.png` (Anil Fig 1) `:988`;
`figs/yong-translate.png` (Yong Fig 1) `:1000`; `figs/yong-table.png` (Yong Table 1) `:1017`;
`figs/cipher-overview.png` (Yuan Fig 2) `:1038`; `figs/qift-overview.png` (Qi ICLR 2024 Fig 1) `:1059`;
`figs/szegedy-ostrich.png` (Szegedy Fig 5) `:1088`; `figs/ganguli-success.png` (Ganguli Fig 1) `:1217`;
`figs/perez-overview.png` (Perez Fig 1) `:1233`; `figs/sharma-overview.png` (Sharma Fig 1) `:1366`;
`figs/cb-overview.png` (Zou CB Fig 1) `:1387`; `figs/bon-powerlaw.png` (Hughes Fig 3) `:1504`.
Inline SVG: raw model `:89`, two goals `:126`, RLHF loop `:175`, reward + KL leash `:224`,
refusal chat `:274`, unsafe-output bars `:306`, thin layer `:349`, shallow first-token `:384`,
competing scale `:444`, capability⊃safety Venn `:479`, jailbreak rows `:530`, persona `:571`,
fake authority `:607`, obfuscation pipeline `:642`, trick→patched `:685`, hand vs search `:738`,
suffix target `:781`, search loop `:842`, many-shot context `:944`, image/prompt recipe `:1108`,
decision boundary + suffix `:1145`, broken-defenses timeline `:1167`, defense pipeline `:1254`,
filter bypass `:1289`, stacked context `:1330`, demo rows `:1408`, cat-and-mouse `:1450`,
staircase `:1471`. Citations use `.cite-left`.

**2026-09 figure pass (57→60):** added 18 cited figure crops (Ouyang ×2, Bai, Qi ICLR 2025,
Arditi, Zou GCG Fig 2 + Fig 3, Chao PAIR, Yong ×2, Yuan CipherChat, Qi ICLR 2024, Szegedy,
Ganguli, Perez, Sharma, Zou CB, Hughes BoN) and 23 inline SVGs on formerly text-only slides;
added 3 slides: InstructGPT, Measured (§01), Shallow, Measured (§02), Which Languages Break
Through (§05); added the CipherChat citation; Many-Shot cite normalized to Anil et al. NeurIPS
2024. 60-dpi render check of all edited slides. Note synced (60 articles incl. closer, order
matches; Slide-figure lines on every figure slide).

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
  reported via HackerOne, no CVE (GitHub-rated CVSS 9.6), Legit Security, Oct 2025;
  Invariant Labs, May 2025.
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

**2026-08 note enrichment:** `lec11-prompt-injection-note.html` upgraded from speaker
script to **script + companion notes** (395→736 lines; 63 entries unchanged). Per-entry
`.detail` blocks: prompt injection formalized (f over one token stream, x = τ(s,u,d),
agent loop x_{t+1} = x_t ∥ a_t ∥ o_t, injection success as unauthorized action — all
labeled course notes); control/data-plane and confused-deputy (Hardy 1988) definitions
expanded from lec11tech; full Greshake et al. taxonomy (4 injection methods × 6 threat
types) stated from arXiv 2302.12173; defense formalisms (spotlighting variants,
instruction hierarchy, taint/IFC lattice, dual-LLM invariant, CaMeL capabilities,
Saltzer–Schroeder least privilege); the "no clean escape / unsolvable by prompting
alone" argument given as a labeled 5-step informal argument (not a theorem), empirically
anchored to Zhan et al. 2025. Incident backgrounds + 24 verified links (all fetched:
arXiv ×7, Willison ×3, Brave ×2, CVE.org/MSRC/Aim, Legit/Register/Invariant,
embracethered, Ars, OWASP ×2, MIT Hardy, MIT Saltzer, dblp). Note and deck both
corrected 2026-08-19: CamoLeak has NO CVE — the previously cited "CVE-2025-59145"
is an unrelated npm color-name malware record.

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

**2026-08 note enrichment:** `lec12-watermark-note.html` upgraded from speaker script (376 lines) to Script &amp; Companion Notes (772 lines; 58 entries unchanged): per-entry `.detail` blocks with rigorous definitions (soft watermark, spike entropy, distortion-free generation, CGZ soundness/completeness/undetectability, TV/AUROC, C2PA), full proofs (KGW Thm 4.2 four-step, Thm 4.3 in corrected form + explicit misprint warning, green-mass boost Prop, Gumbel-max + Aaronson equivalence, exponential-minimum sampling, Zhao Unigram Thm 3.7 sketch, Sadasivan Thm 1, Berry–Esseen FP bound, Hoeffding tail), and 30 verified links — all consistent with `courses/privacy/lectures/06-watermark/`.

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

**2026-08 note enrichment:** `lec13-fairness-defs-note.html` upgraded from speaker script (365 lines) to Script &amp; Companion Notes (708 lines; 58 entries unchanged): per-entry `.detail` blocks with rigorous definitions (setup A/Y/Ŝ/Ŷ, per-group confusion quantities, demographic parity + EEOC four-fifths rule verbatim, equalized odds / equal opportunity (Hardt Defs 2.1/2.2), calibration / test fairness / predictive parity (Chouldechova Def 2.1), independence–separation–sufficiency trichotomy, Dwork (D,d)-Lipschitz Def 2.1, SCM + counterfactual fairness Def 5), full proofs (Chouldechova base-rate identity + impossibility corollary, KMR Theorem 1.1 four-step linear-system proof verified against §2 + Thm 1.2 approximate version, forced-FPR-ratio corollary ≈1.63 on COMPAS base rates, fully worked calibrated two-value-score wedge matching lec13tech), and 23 verified links (ProPublica exact rates 44.85/23.45 + 27.99/47.72, Northpointe rebuttal via DocumentCloud, eCFR §1607.4(D), Obermeyer, BBQ, LL144 + SB24-205 litigation timeline).

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

**2026-08 note enrichment:** `lec14-fairness-mitigation-note.html` upgraded from speaker
script (383 lines) to Script &amp; Companion Notes (695 lines; 61 entries unchanged):
per-entry `.detail` blocks with rigorous definitions (fairness-gap functionals, derived
predictor Def 4.1, discrimination score, first-person fairness), proofs (reweighing
independence, massaging flip count, reductions Thm 1/3 sketch, adversarial Props 2–3
with entropy proofs, Hardt LP + ROC geometry + Prop 5.2/Cor 5.3, DP error lower bound),
and 23 verified links — consistent with `lec14tech.html` and the lec13 note (impossibility
proofs referenced, not duplicated).

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
tier bullets de-dashed; still 6 sl). Note file synced (66 entries, order matches; 67 after the 2026-09 figure pass).

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
