# privacy/lectures/04-mia/ — Membership inference attacks (5 lectures)

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

104 slides, 6 sections. Every theorem/proposition below is stated **and proved on the slides**;
the note holds only caveats, tightness and numeric provenance.

| Part | Topic | Line |
|---|---|---|
| **01** — Why MIA matters | central question, notation, threat model, road map | `:93-217` |
| | Notation table (D, M, θ, z, A, α/β/π) | `:118` |
| | When membership is itself the secret (timeline figure) | `:147` |
| | Loss-histogram picture behind every attack | `:176` |
| **02** — Homer et al. 2008 | full statistical development of the genomic attack | `:218-660` |
| | Per-SNP probabilistic model (Y_ij, M_j, p_j) | `:286` |
| | Signed distance statistic D_j | `:300` |
| | **Key trick** \|Y−a\| = a + Y(1−2a) removes the absolute value | `:313` |
| | **Lemma 1** non-member has zero mean (+ proof) | `:331` |
| | **Lemma 2** member has mean −2p(1−p)/n (+ 2 proof slides) | `:347` |
| | Sign-flip figure (the attack in one picture) | `:392` |
| | **Proposition 1** per-SNP variance ≈ p(1−p)/n (+ proof) | `:416` |
| | CLT aggregation figure | `:446` |
| | **Theorem 1** power π = Φ(μ − z_{1−α}), μ = 2√(m v̄/n) | `:495` |
| | Proof of Theorem 1: outline, steps 1–4, recap chain | `:509-560` |
| | **Corollary 1** loci needed m ≥ n(z_{1−α}+z_{1−β})²/(4v̄) + numbers | `:575-603` |
| | What the model idealizes / what the paper reported | `:604-641` |
| | NIH database closure | `:642` |
| **03** — Reconstruction → distinguishability | | `:661-843` |
| | Genomics → ML translation table | `:683` |
| | Sampling-mechanism counterexample (defeats reconstruction, destroys privacy) | `:712-744` |
| | IND-CPA precedent (figure) | `:745` |
| | Attack-surface spectrum + two axes of adversary knowledge | `:787-826` |
| **04** — The MI game and the optimal attack | | `:844-1203` |
| | **MI game** (5-step challenger/adversary box) + game-flow figure | `:851-902` |
| | **Definition** MI advantage | `:918` |
| | **Proposition 2** Adv = \|TPR − FPR\| = 2Pr[b̂=b] − 1 (+ proof) | `:932` |
| | **Proposition 3** sup_A Adv = TV(P₁,P₀) (+ upper bound, achievability) | `:960-1002` |
| | Hypothesis-testing dictionary; what the adversary computes | `:1003-1030` |
| | Why loss is the natural statistic (Sablayrolles ICML 2019) | `:1031` |
| | **Theorem 2** Neyman–Pearson lemma, randomized at the boundary | `:1057` |
| | Proof of Theorem 2: outline, calibration, **sign trick**, integrate, size constraint, recap | `:1072-1151` |
| | Rejection-region figure | `:1152` |
| | **Corollary 2** every optimal attack is a likelihood-ratio test | `:1175` |
| **05** — DP as an upper bound | | `:1204-1422` |
| | Recall (ε,δ)-DP; recasting DP as a testing constraint | `:1211-1236` |
| | **Theorem 3** α + e^ε β ≥ 1−δ and β + e^ε α ≥ 1−δ (+ 2 proof slides) | `:1237-1281` |
| | **Corollary 3** ROC cap TPR ≤ e^ε FPR + δ | `:1282` |
| | DP wedge figure (achievable region shaded) | `:1296` |
| | **Corollary 4** Adv ≤ e^ε − 1 + δ (+ proof; migrated from the note) | `:1327` |
| | Numeric tables: advantage bound; ROC cap at FPR 10⁻³ | `:1342-1370` |
| | What the bound does *not* say (scope, direction) | `:1371-1392` |
| | Both directions: DP caps attacks; attacks certify ε ≥ log((TPR−δ)/FPR) | `:1393-1422` |
| **06** — Evaluating membership inference | | `:1423-1674` |
| | ROC as a curve, not a number; ROC-plane figure | `:1430-1465` |
| | AUC in two forms | `:1466` |
| | **Proposition 4** AUC = Pr[T⁺ > T⁻] (+ 2 proof slides) | `:1476-1515` |
| | **Proposition 5** AUC is an average-case statistic | `:1516` |
| | Two-attack counterexample (√FPR vs min(2FPR,1)) + linear/log-log figure | `:1529-1568` |
| | Why AUC misses MIA risk; TPR at low FPR (Carlini S&P 2022) | `:1569-1597` |
| | Metrics comparison; reading metric tables critically; benchmarks | `:1598-1637` |
| | The argument in one chain; what to carry forward | `:1638-1674` |

Deck-local figure family: prefix `m1-` (`.m1-fig` + `.lab` overlays, `.m1-algo`, `.m1-chain`, `.m1-tight`), defined in the deck's own `<style>` block.

**Note (`mia1-foundations-note.html`):** TPR-at-low-FPR rationale and metric pitfalls `:39-54`;
DP caveats — why the table values, tightness (Kairouz–Oh–Viswanath), sources of slack, auditing confidence intervals `:56-74`;
Homer model provenance and the √m vs 1/√n reading `:76-80`.

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
