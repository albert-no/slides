# privacy/mia/ — Membership inference attacks (5 lectures)

5-lecture series, paired `<deck>.html` + `<deck>-note.html`. Lectures 4 and 5 also have single-page `<deck>-overview.html` summaries. Plus legacy `old/MIA.html` (single-file deck superseded by mia1+mia2). Notes contain extra proof detail and tables.

## Files

| Deck | Note | Overview | Topic |
|---|---|---|---|
| `mia1-foundations.html` | `mia1-foundations-note.html` | — | Foundations (2008–2019): Homer, MI game, DP bounds, evaluation |
| `mia2-shadow.html` | `mia2-shadow-note.html` | — | Shadow models: Shokri, LOGAN (GANs), Hisamoto (seq2seq) |
| `mia3-theory.html` | `mia3-theory-note.html` | — | Theory: Yeom (overfitting), Sablayrolles (BB≈WB), Salem (relaxed), Nasr (FL) |
| `mia4-modern.html` | `mia4-modern-note.html` | `mia4-overview.html` | Modern: LiRA, Ye hierarchy, RMIA, label-only, defenses |
| `mia5-llm.html` | `mia5-llm-note.html` | `mia5-overview.html` | LLMs (high-level): calibration strategies, **empirical wall** (Hayes 2025), fine-tuning, extraction |
| `old/MIA.html` | — | — | Legacy consolidated deck (Lectures 1–2 era) |

---

## mia1-foundations.html

| Part | Topic | Line |
|---|---|---|
| **01** — Why MIA matters | central question, IND-CPA analogy, real-world stakes | `:78-141` |
| | Inline notation table (M, D, x, θ, f_θ, ℓ) | `:91` |
| | IND-CPA defined inline | `:115` |
| **02** — Homer et al. 2008 | motivation, GWAS aggregates, MIA framing | `:142-310` |
| | "Why this paper existed" (GWAS publication norms) | `:149` |
| | **Homer attack in MIA language** (mapping table) | `:166` |
| | **Genomics in 60 seconds** (SNP, allele, frequencies) | `:184` |
| | Three ingredients (`Y_i`, `M_j`, `Pop_j`) with descriptions | `:198` |
| | Distance `D(Y_{i,j}) = \|Y_{i,j}-M_j\|-\|Y_{i,j}-Pop_j\|` | `:228` |
| | Aggregation t-test | `:257` |
| | NIH database closure | `:296` |
| **03** — Reconstruction → distinguishability | | `:311-476` |
| | IND-CPA cryptographic analogy (full) | `:412` |
| | Privacy = indistinguishability → MIA | `:454` |
| **04** — The MI game | challenger, adversary, neighboring DBs | `:477-687` |
| | **MI game** (with `A` defined inline) | `:483` |
| | **Neighboring DBs** `D_1=D∪{x}, D_0=D\{x}` | `:500` |
| | **Advantage** `\|Pr[A=1\|b=1]-Pr[A=1\|b=0]\|` | `:517` |
| | HT connection (refers back to DP2 HT interpretation) | `:545` |
| | **Neyman–Pearson setup** (size, power, level) | `:584` |
| | **Neyman–Pearson statement** `Λ(T) = p_1/p_0 ≷ τ` | `:605` |
| | **NP proof** (one-line sign-trick argument) | `:623` |
| | **NP → MIA**: every optimal MIA is a likelihood-ratio test | `:641` |
| | Error types (FPR, FNR) | `:663` |
| **05** — DP, MI, taxonomy | | `:688-1029` |
| | **HT interpretation of DP** (from DP2) `1≤α+βe^ε` | `:693` |
| | **DP caps the MIA ROC** `TPR ≤ e^ε FPR + δ` | `:707` |
| | **Corollary: Advantage bound** `Adv ≤ e^ε−1+δ` (with numerical table) | `:723` |
| | MI as auditing tool | `:740` |
| | Privacy attack taxonomy (membership/attribute/extraction/inversion, each defined) | `:788` |
| | Threat model spectrum | `:817` |
| | **Sablayrolles 2019** (dedicated slide): BB ≈ WB, loss is sufficient | `:832` |
| | **ROC curve — definition** (full-width equations) | `:848` |
| | **ROC curve — large diagram** (perfect / attack / random) | `:863` |
| | **AUC — formulas** (integral + probabilistic) | `:897` |
| | **AUC — diagram + reference values** | `:911` |
| | **Why AUC misses MIA risk** + Attack A vs B diagram | `:948` |
| | **TPR @ low FPR (Carlini critique)** + log-log ROC diagram | `:984` |
| | Metrics comparison table | `:1020` |
| | Standard benchmarks (CIFAR, Purchase, Texas, WikiMIA) | `:1035` |

**Note (`mia1-foundations-note.html`):** DP→MI bound full proof `:57-72`; why log-log ROC matters `:45`; metric pitfalls `:49-53`.

---

## mia2-shadow.html

| Part | Topic | Line |
|---|---|---|
| **01** — Shokri et al. 2017 | shadow model paradigm | `:62-481` |
| | **Attack architecture — training pipeline** (SVG: D_jˢ → Shadow j → labeled dataset → A_c) | `:94` |
| | **Attack architecture — inference** (SVG: x → f_θ → σ → A_c → IN/OUT) | `:166` |
| | Detailed pipeline (numbered steps) | `:215` |
| | Shadow data strategies | `:258` |
| | **Attack data collection** (Member/Non-member grid + labeled dataset card) | `:282` |
| | **Per-class attack models** `A_c: R^\|C\| → {0,1}` | `:311` |
| | Attack inference | `:327` |
| | Results: 93% precision, 91% recall (Purchase-100) | `:344` |
| | Pseudocode (split: build+train, then attack) | `:417, :436` |
| | Confidence-threshold baseline `1[max_c f(x)_c > τ]` | `:449` |
| **02** — LOGAN (Hayes et al.): MIA on GANs | | `:482-619` |
| | LOGAN overview | `:487` |
| | **GAN refresher** (G, D, minimax, SVG diagram) | `:504` |
| | Discriminator + reconstruction-based attacks | `:561` |
| | Results: MNIST DCGAN ~74%, CIFAR ~69% | `:601` |
| **03** — Seq2seq (Hisamoto et al.): MT models | | `:620-737` |
| | **Perplexity** `PPL(x,y)=exp(-1/T Σ log p(y_t\|y_{<t},x))` | `:632, :659` |
| | seq2seq vs LLM MIA comparison | `:675` |

**Note (`mia2-shadow-note.html`):** Full Google results table including Texas-100 `:42-50`; calibration for LLMs vs seq2seq `:53-63`.

---

## mia3-theory.html

Lightened from 45 → 28 slides: Yeom 3-part proof, redundant intuition slides, and individual Salem relaxation slides folded into single takeaway/summary slides. Full Yeom proof lives in `mia3-theory-note.html`.

| Part | Topic | Line |
|---|---|---|
| **01** — Yeom et al. 2018 (overfitting) | | `:78-216` |
| | **Generalization gap** `Δ = R_pop − R_train` | `:104` |
| | **Threshold attack** `A(z) = 1[ℓ(f,z) ≤ τ]`, `τ = R_pop` | `:118` |
| | **Theorem: Adv_MI ≤ Δ** (proof in note) | `:137` |
| | Loss-distribution intuition (members vs non-members) | `:147` |
| | Takeaway (what works / where it falls short) | `:187` |
| **02** — Sablayrolles et al. 2019 (BB vs WB) | | `:217-322` |
| | **Bayes-optimal MI** `Λ(z) = p(Φ\|z∈D)/p(Φ\|z∉D)` | `:240` |
| | White-box features (loss, gradients, activations) | `:276` |
| | **Theorem: Λ_BB → Λ_WB** with merged intuition | `:291` |
| | Experimental validation (BB-WB gap < 1% AUC) | `:306` |
| **03** — Salem et al. (ML-Leaks) — single consolidated slide + results | | `:323-368` |
| | Three relaxations (different arch / different distribution / no shadows) | `:329` |
| | Graceful degradation (~5% drop) | `:353` |
| **04** — Nasr et al. 2019 (white-box + FL) | | `:369-460` |
| | Per-layer gradients as features | `:395` |
| | FL vulnerability: shared Δθ exposes WB info | `:416` |
| | Passive vs active attacks in FL | `:438` |
| **05** — Synthesis | timeline 2008–2019 | `:461-525` |

**Key theorems:** Yeom bound `:137`; Bayes-optimal `:240`; BB→WB convergence `:291`.

**Note (`mia3-theory-note.html`):** Full Yeom proof `:40-61` (moved off slides as part of lightening); per-sample vulnerability `:64-68`; bound tightness `:78-87`; ML-Leaks results table `:90-100`; Sablayrolles validation `:103-113`.

---

## mia4-modern.html

| Part | Topic | Line |
|---|---|---|
| **01** — Defenses recap | DP-SGD, comparison, broken adaptive defenses | `:86-181` |
| | **DP-SGD update** `g̃_t = (1/B)(Σ clip(g_i,C) + N(0,σ²C²I))` | `:122` |
| | Defenses broken by adaptive attacks (MemGuard, label smoothing, etc.) | `:168` |
| **02** — Why early evaluations misled | label-only MIA | `:182-256` |
| | Label-only (Choquette-Choo 2020) — boundary distance, ~100 queries | `:207-244` |
| **03** — LiRA: Carlini et al. 2022 | | `:257-524` |
| | **Likelihood ratio** `Λ(z) = p(ℓ\|z∈D)/p(ℓ\|z∉D)` | `:285` |
| | Estimating distributions (N/2 IN, N/2 OUT, fit Gaussians) | `:299` |
| | **LiRA formula** Gaussian PDFs | `:324` |
| | **Per-example calibration** `(μ_in,σ_in,μ_out,σ_out)` per z | `:339` |
| | Online vs offline | `:355` |
| | Computational cost (256 models for CIFAR-10) | `:376` |
| | TPR@0.01% FPR is 10–50× higher than prior | `:432` |
| | Evaluation revolution | `:449` |
| | Offline algorithm pseudocode | `:487` |
| **04** — Unified view (Ye et al. 2022) | | `:525-646` |
| | **Attack power hierarchy: LiRA ≥ Reference ≥ Population ≥ Threshold** | `:600` |
| | Privacy Meter (open-source tool) | `:629` |
| **05** — RMIA: Zarifzadeh et al. 2023 | | `:647-730` |
| | **Formula** `Λ(z) = p_θ(z) / (1/R Σ p_{θ_r}(z))` | `:674` |
| | Population ranking | `:689` |
| | RMIA TPR@0.1%: ~11% with 2–8 models (vs LiRA's 256) | `:704` |
| **06** — Beyond classification | diffusion model MIA | `:731-913` |
| | Reconstruction-loss timestep analysis | `:742, :764` |
| | LR paradigm universal | `:799` |

**Key formulas:** DP-SGD `:122`; LiRA LR `:285, :324`; RMIA LR `:674`; attack hierarchy `:600`.

**Note (`mia4-modern-note.html`):** Side-by-side pseudocode threshold/LiRA/RMIA `:43-74`; defense comparison table `:78-87`; cost-vs-power table `:92-103`.

---

## mia5-llm.html

**Restructured 2026-05** to ~38 slides — high-level overview rather than per-paper deep dive. New §03 "Empirical wall" featuring Hayes et al. 2025 limits-of-strong-attacks paper, Duan et al. 2024, and Maini et al. blind baselines. Detailed per-paper material now lives in `mia5-llm-note.html`.

| Part | Topic | Line |
|---|---|---|
| **01** — What makes LLM MIA hard | | `:82-198` |
| | From classifiers to LLMs (one-pass, no shadows, unknown data) | `:90` |
| | Three threat models (pre-train/FT/context) | `:116` |
| | **Perplexity baseline** `PPL(x) = exp(-1/T Σ log p_θ(x_t\|x_{<t}))` | `:140` |
| | The calibration challenge (need a per-example null) | `:155` |
| | Two knobs: **signal × reference** | `:175` |
| **02** — Calibration strategies | | `:199-325` |
| | Reference model (Carlini 2021) — smaller LM as null | `:206` |
| | **Neighbourhood** (Mattern 2023) — paraphrase null | `:221` |
| | **SPV-MIA** (Fu 2023) — self-prompted null | `:236` |
| | **Context-aware** (Chang 2024) — `s(x) = Var_c[log p_θ(x\|c)]` | `:253` |
| | Token-level: which tokens carry signal (visualization) | `:269` |
| | **Min-K% / InfoRMIA** — token-weighted log-ratio | `:293` |
| | Calibration zoo summary table | `:306` |
| **03** — The empirical wall (NEW) | | `:326-441` |
| | The headline question (gap vs classifier MIA) | `:333` |
| | **Duan et al. 2024** — MIA barely beats random on Pythia/Pile | `:348` |
| | **Hayes et al. 2025** — scaled LiRA on GPT-2: AUC < 0.7 ceiling | `:364` |
| | Per-record instability (training-seed noise > membership signal) | `:378` |
| | **Maini et al. 2024** — blind baselines beat published MIAs | `:395` |
| | Why pre-training MIA is structurally hard (4 reasons) | `:411` |
| **04** — Where the signal still lives | | `:442-563` |
| | Fine-tuning MIA works (multi-epoch, small data) | `:449` |
| | Extractable vs. inferable memorization | `:471` |
| | MIA as extraction's ranker (generate → rank → verify) | `:491` |
| | Defenses (DP-FT, dedup, curation) | `:509` |
| | Legal landscape (GDPR, NYT v OpenAI) | `:537` |
| **05** — Synthesis | | `:564-655` |
| | Unified LR template `Λ(z) = p(signal\|in)/p(signal\|out)` | `:571` |
| | Instances table (Homer 2008 → InfoRMIA 2025) | `:582` |
| | Four eras (2008–2017, 2018–2019, 2020–2023, 2023–2025) | `:597` |
| | Key takeaways + open problems | `:610, :625` |
| | Essential reading (Hayes et al. featured) | `:640` |

**Key formulas:** Perplexity `:147`; Neighbourhood score `:228`; Context-aware variance `:259`; InfoRMIA `:300`; Unified LR `:575`.

**Featured limitations papers (§03):** Duan 2024 `:348`; **Hayes 2025** `:364, :378`; Maini 2024 `:395`.

**Note (`mia5-llm-note.html`):** Side-by-side pseudocode perplexity/neighbourhood/InfoRMIA `:43-72`; full calibration zoo with InfoRMIA row `:74-79`. (Per-paper deep-dive material — InfoRMIA token-selection strategies, SPV self-prompting strategies, full results tables — was moved out of the slides in the 2026-05 restructure and now belongs in the note.)

---

## old/MIA.html

Legacy consolidated deck (~`:45` title) covering the foundational material now spread across mia1 + mia2 (Homer, indistinguishability, DP connection, evaluation, Shokri shadow models). Newer 5-lecture series supersedes it. Reference paths in this file are off by one level (broken before and after the recent reorg) — not actively used.
