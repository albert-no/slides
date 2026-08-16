# privacy/lectures/04-mia/ — Membership inference attacks (5 lectures)

5-lecture series, paired `<deck>.html` + `<deck>-note.html`. Lectures 4 and 5 also have single-page `<deck>-overview.html` summaries. Plus legacy `old/MIA.html` (single-file deck superseded by mia1+mia2). Notes contain extra proof detail and tables.

## Files

| Deck | Note | Overview | Topic |
|---|---|---|---|
| `mia1-foundations.html` | `mia1-foundations-note.html` | — | Foundations (2008–2019): Homer, MI game, DP bounds, evaluation |
| `mia2-shadow.html` | `mia2-shadow-note.html` | — | Shadow models as Monte-Carlo estimation of the two conditionals: Shokri, per-class models, LOGAN (GANs), Hisamoto (seq2seq) and calibration |
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

**Revised 2026-08** (math-detail pass, 33 → 114 slides, 6 sections). Every assumption/lemma/
proposition/theorem/corollary below is stated **and proved on the slides**; the note holds only
proof bookkeeping, full result tables, and factual corrections. Continues `mia1-foundations.html`
(MI game, advantage, Neyman–Pearson, TV, DP bounds, ROC/AUC) — refers back, never redefines.

| Part | Topic | Line |
|---|---|---|
| **01** — From optimal test to estimation problem | | `:95-515` |
| | Recall (optimal attack) card; notation table for this lecture | `:102, :120` |
| | **Definition** member/non-member laws $P_1, P_0$ | `:134` |
| | Two densities the attacker cannot write down (figure); why the ratio is not computable | `:147, :168` |
| | **Key trick** sample what you cannot integrate | `:184` |
| | The shadow recipe; Monte-Carlo picture (figure) | `:201, :217` |
| | **Assumption S** (faithful shadows) | `:266` |
| | **Proposition 1** shadows simulate the two laws exactly (+ proof) | `:280, :292` |
| | **Theorem 1** log-loss minimiser $= \Lambda/(1+\Lambda)$: shadow training recovers the ratio | `:321` |
| | Proof of Theorem 1: outline, condition, minimise, invert, recap | `:332-395` |
| | What Theorem 1 buys; two gaps (statistical vs specification) | `:396, :412` |
| | **Corollary 1** mis-specification costs at most $2\,\mathrm{TV}$ (+ proof, reading) | `:437, :449, :466` |
| | The shift that breaks a threshold (figure) | `:482` |
| **02** — The Shokri paradigm | | `:516-809` |
| | Shokri et al. setting; instantiating the observable | `:523, :538` |
| | **Attack architecture — training pipeline** (SVG) | `:551` |
| | **Attack architecture — inference** (SVG) | `:598` |
| | The pipeline in the theory's language | `:631` |
| | Three ways to get shadow data; model-based synthesis; what synthesis estimates | `:645, :661, :677` |
| | Collecting the attack training set | `:688` |
| | Pseudocode (split: build+train, then attack) | `:702, :720` |
| | Results: Google Prediction API; Amazon ML and beyond | `:733, :746` |
| | Why more classes leak more; overfitting is the engine; limitations | `:760, :772, :792` |
| **03** — Per-class models and the threshold baseline | | `:810-1079` |
| | **Per-class attack models** $A_c$; class-conditional laws | `:817, :828` |
| | **Lemma 1** pooled ratio is a $\pi_c$-weighted average of class ratios (+ proof) | `:839, :851` |
| | **Corollary 2** pooling pulls the ratio toward 1 (mediant bound) | `:865` |
| | Why a pooled score blurs (figure) | `:876` |
| | **Proposition 2** conditioning never hurts (+ 3 proof slides) | `:907, :924-960` |
| | **Key trick** mixing is data processing (TV never increases under a channel) | `:961` |
| | Per-class models in practice; the confidence-threshold baseline | `:974, :990` |
| | **Assumption MLR** (monotone likelihood ratio) | `:1002` |
| | **Proposition 3** the baseline is the NP test among tests of $s$ (+ proof) | `:1013, :1024` |
| | What the baseline gives up; one axis, not two recipes (figure) | `:1037, :1050` |
| **04** — LOGAN: generative models | | `:1080-1389` |
| | LOGAN setting; GAN setup; **the game, drawn** (SVG) | `:1087, :1102, :1115` |
| | **Theorem 2** optimal discriminator $D^\star = p_{\text{data}}/(p_{\text{data}}+p_g)$ (+ 2 proof slides) | `:1152, :1163-1185` |
| | **Theorem 3** value of the game $= 2\,\mathrm{JSD}(p_{\text{data}}\|p_g) - \log 4$ (+ 2 proof slides) | `:1186, :1196-1220` |
| | **Proposition 4** $D^\star$ is the logistic of the log density ratio (+ proof) | `:1221, :1232` |
| | Ratio, seen (figure); why this makes an attack; the discriminator attack | `:1244, :1268, :1279` |
| | Black box: only samples | `:1291` |
| | **Proposition 5** reconstruction distance bounds the smoothed generator density (+ proof) | `:1303, :1314` |
| | What reconstruction is missing; shadow GANs restore the denominator | `:1328, :1342` |
| | LOGAN reported results; mode collapse raises the ratio | `:1357, :1370` |
| **05** — Sequence models and calibration | | `:1390-1705` |
| | The sequence challenge; **perplexity** defined | `:1397, :1412` |
| | **Proposition 6** an unnormalised perplexity threshold is a degenerate LRT (+ proof) | `:1423, :1435` |
| | Optimal only within a difficulty class; what a global threshold sees (figure) | `:1448, :1462` |
| | A two-group (easy/hard) model | `:1488` |
| | **Proposition 7** pooling costs half the population, $\mathrm{TPR} \to \tfrac12\Phi(\cdot) \le \tfrac12$ | `:1500` |
| | Proof of Proposition 7: part (i), size, power | `:1514-1551` |
| | The gap, numerically (Φ arithmetic, illustrative) | `:1552` |
| | Length is a second nuisance; variance shrinks with length (figure) | `:1564, :1576` |
| | Hisamoto et al. protocol (Alice/Bob/Carol); Bob's actual features (BLEU, **not** perplexity) | `:1602, :1617` |
| | Sentence-level result: chance; where signal does appear; group probes | `:1632, :1646, :1661` |
| | **Corollary 1, in the wild** (shadow BLEU gap as measured mis-specification) | `:1675` |
| | What is missing is a null | `:1688` |
| **06** — Synthesis | | `:1706-1786` |
| | Every attack names the same two densities (6-row table) | `:1713` |
| | The argument in three lines (chain: Prop 1 → Thm 1 → Cor 1) | `:1727` |
| | What to carry forward; two open threads (relaxation → mia3, calibration → mia4/mia5) | `:1751, :1767` |

**Key results, all proved on slides:** Assumption S `:266`; **Prop 1** `:280`; **Thm 1** `:321`;
**Cor 1** `:437`; **Lemma 1** `:839`; **Cor 2** `:865`; **Prop 2** `:907`; Assumption MLR `:1002`;
**Prop 3** `:1013`; **Thm 2** `:1152`; **Thm 3** `:1186`; **Prop 4** `:1221`; **Prop 5** `:1303`;
**Prop 6** `:1423`; **Prop 7** `:1500`.

Deck-local figure family: prefix `m2-` (`.m2-fig` + `.lab` overlays, `.m2-algo`, `.m2-chain`,
`.m2-tight`), defined in the deck's own `<style>` block. Original SVG figures: two-density picture
`:147`, Monte-Carlo picture `:217`, distribution shift `:482`, training pipeline `:551`, inference
pipeline `:598`, pooled-vs-conditional densities `:876`, threshold axis `:1050`, GAN game `:1115`,
density-ratio curve `:1244`, difficulty mixture `:1462`, per-length variance `:1576`.

**Note (`mia2-shadow-note.html`):** Google/Texas-100 full table `:39-50`; proof bookkeeping for
Prop 1 and Cor 1 (Glivenko–Cantelli, $O_p(k^{-1/2})$, pointwise ROC form) `:52-60`; non-saturating
GAN surrogate `:62-68`; **Hisamoto correction** — Bob uses n-gram precisions + sentence BLEU, not
perplexity; Table 2/4/5/6 numbers with the degenerate always-"out" caveat; shadow BLEU 38.6 vs
Alice 42.6 `:70-86`; provenance of the "Gap, Numerically" arithmetic `:88-94`; seq2seq → LLM
calibration bridge `:96-102`.

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
