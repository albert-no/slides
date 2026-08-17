# privacy/lectures/04-mia/ — Membership inference attacks (5 lectures)

Complete 5-lecture series (all five decks revised 2026-08 to full math-detail form: 104 / 114 / 139 / 147 / 123 slides). Paired `<deck>.html` + `<deck>-note.html`; decks 4 and 5 also have single-page `<deck>-overview.html` summaries. Plus legacy `old/MIA.html` (single-file deck superseded by mia1+mia2). Every definition, theorem, proposition, lemma and corollary listed below is stated **and proved on the slides**; the notes hold assumptions, provenance of reported numbers, corrections and speaker asides.

## Files

| Deck | Note | Overview | Topic |
|---|---|---|---|
| `mia1-foundations.html` | `mia1-foundations-note.html` | — | Foundations (2008–2019): Homer, MI game, DP bounds, evaluation |
| `mia2-shadow.html` | `mia2-shadow-note.html` | — | Shadow models as Monte-Carlo estimation of the two conditionals: Shokri, per-class models, LOGAN (GANs), Hisamoto (seq2seq) and calibration |
| `mia3-theory.html` | `mia3-theory-note.html` | — | Theory: Yeom (overfitting), Sablayrolles (BB≈WB), Salem (relaxed), Nasr (FL) |
| `mia4-modern.html` | `mia4-modern-note.html` | `mia4-overview.html` | Modern estimators of the likelihood ratio: LiRA (closed form, calibration, online/offline), Ye's nested-conditioning hierarchy, RMIA, label-only boundary distance, DP-SGD and the post-processing bound, diffusion MIA |
| `mia5-llm.html` | `mia5-llm-note.html` | `mia5-overview.html` | LLMs: the calibrated score $\log p_\theta(x)-\log q(x)$ and five estimators of its null; a model-based signal-to-noise account of why pre-training MIA is hard; the **empirical wall** (Duan 2024, Hayes 2025, blind baselines as a validity failure); fine-tuning, extraction, DP; series-wide synthesis |
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

Math-detail revision (28 → 139 slides): the Yeom argument is now stated, proved and
counter-exampled on the slides, Sablayrolles' two theorems are proved in full, Salem's three
relaxations are quantified against `mia2`'s mis-specification bound, and Nasr's white-box and
federated claims are turned into a rank-one gradient proposition and a data-processing
proposition. Class prefix `m3-`. Deck refers back to `mia1`/`mia2` through self-contained
"Recall" cards only.

| Part | Topic | Line |
|---|---|---|
| Front matter | Title; contents; **What We Already Have** (2 Recall cards); the question (SVG fan-in) | `:44, :55, :88, :113` |
| **01** — Yeom et al., CSF 2018 | | `:149-957` |
| | What Yeom actually proves; setup and notation (bit flipped to $b=1$ = member) | `:156, :172` |
| | **Experiment 1** membership experiment; **Definition 4** membership advantage | `:187, :205` |
| | Why non-members come from $\mathcal{D}$; **Definition 3** average generalisation error | `:220, :236` |
| | Average gap vs fixed-set gap | `:250` |
| | **The picture behind everything** (SVG: two loss densities, threshold, shaded errors) | `:273` |
| | Reading the picture; the bounded-loss assumption | `:305, :329` |
| | **Adversary 1** (loss-proportional coin); **Key trick** | `:349, :366` |
| | **Theorem 2** $\mathrm{Adv}^{\mathrm{M}}(\mathcal{A}_1) = R_{\text{gen}}/B = \Delta/B$ (an equality) | `:387` |
| | Proof of Theorem 2: outline, condition, linearity, identify, recap | `:402-484` |
| | What Theorem 2 buys; **Corollary** $\Delta/B \le \sup\mathrm{Adv} = \mathrm{TV}(P_1,P_0)$ (+ proof) | `:485, :508, :521` |
| | Which way the bound points (SVG number line); the folklore misstatement | `:535, :563` |
| | **Counterexample A** zero gap, full advantage (+ the attack) | `:584, :600` |
| | **Counterexample B** large gap, useless threshold (+ three attackers) | `:617, :633` |
| | Both counterexamples at a glance (SVG); moments vs distributions | `:649, :680` |
| | **Theorem 1** $\varepsilon$-DP $\Rightarrow \mathrm{Adv}^{\mathrm{M}} \le e^{\varepsilon}-1$ (+ 3 proof slides) | `:701, :716-764` |
| | Two bounds, two directions; **Adversary 2** (known error law) | `:765, :786` |
| | **Theorem 3** Gaussian errors (+ 2 proof slides); advantage vs $\rho$ (SVG erf curve) | `:803, :817-845, :846` |
| | Unknown standard error | `:870` |
| | **Theorem 4** overfitting is not necessary; the colluding construction; the two error terms | `:886, :901, :922` |
| | Section 01 takeaway | `:938` |
| **02** — Sablayrolles et al., ICML 2019 | | `:958-1607` |
| | Change of question; the generative story; why this posterior | `:965, :985, :1002` |
| | Temperature concentrates the posterior (SVG) | `:1017` |
| | **Definition** $\mathcal{M}(\theta,z_1) := P(m_1{=}1 \mid \theta,z_1)$, nuisance $\mathcal{T}$; notation $\sigma$, $t_\lambda$ | `:1040, :1054` |
| | **Theorem 5** membership as a sigmoid of a log-ratio (paper Thm 1) | `:1076` |
| | Proof of Theorem 5: outline, condition, Bayes, sigmoid identity, recap | `:1089-1161` |
| | Not yet useful; **the calibration constant** $\tau_p$; **the membership score** $s$ | `:1162, :1176, :1196` |
| | **Theorem 6** $\mathcal{M} = \mathbb{E}_{\mathcal{T}}[\sigma(s + t_\lambda)]$ (paper Thm 2) | `:1212` |
| | Proof of Theorem 6: outline, split off $z_1$, **cancel the nuisance**, take logs | `:1226-1283` |
| | **Corollary** the loss is a sufficient statistic; thresholding the loss is optimal | `:1284, :1299` |
| | Sufficient-statistic collapse (SVG: white-box features → loss → $\mathcal{M}$) | `:1313` |
| | Assumptions stated loudly; what breaks when they fail | `:1344, :1358` |
| | **Property 1** $P(m_1{=}1\mid\theta,z_1) \le \lambda + \varepsilon/4$ (+ proof, ¼-Lipschitz sigmoid) | `:1377, :1391` |
| | **Definition** $(\varepsilon,\delta)$-membership privacy; **Property 2** $\le \lambda + \varepsilon/(4T) + \delta$ (+ proof) | `:1407, :1422` |
| | Temperature as a privacy knob | `:1436` |
| | MALT / MAST / MATT; MATT's local quadratic model; MATT as an inner product | `:1456, :1471, :1490, :1504` |
| | Worked example: Gaussian mean; why the example matters | `:1523, :1536` |
| | Measured: CIFAR-10 (Table 2); ImageNet (Table 3); section takeaway | `:1559, :1574, :1589` |
| **03** — Salem et al., NDSS 2019 (ML-Leaks) | | `:1608-1863` |
| | The claim; **Recall** the mis-specification bound from the shadow-model deck | `:1615, :1627` |
| | **Lemma** total variation is a metric (+ proof) | `:1641` |
| | The three relaxations, formalised as surrogate laws $Q^{(1)},Q^{(2)},Q^{(3)}$ | `:1655` |
| | The relaxation staircase (SVG, $2\,\mathrm{TV}$ steps) | `:1670` |
| | Adversary 1 (fewer shadows); mismatched hyperparameters and algorithm | `:1700, :1714` |
| | Adversary 2 (wrong data distribution); Adversary 3 (no shadow model); the threshold | `:1729, :1745, :1760` |
| | Theory versus measurement; what predicts vulnerability; dropout; a real service | `:1780, :1801, :1816, :1830` |
| | Section 03 takeaway | `:1844` |
| **04** — Nasr, Shokri, Houmansadr, IEEE S&P 2019 | | `:1864-2264` |
| | Three observation models; why gradients should carry signal; the last layer set up | `:1871, :1887, :1906` |
| | **Proposition** $\partial\ell/\partial W = (p - e_y)a^{\top}$ is rank one (+ 2 proof slides) | `:1920, :1934-1960` |
| | Picture of the outer product (SVG) | `:1961` |
| | **Corollary** $\|\partial\ell/\partial W\|_F = \|p-e_y\|\,\|a\|$; why that limits the white-box gain | `:1986, :2002` |
| | Measured: layer outputs (Table III); parameter gradients (Table IV); total gain (Table VIII) | `:2022, :2037, :2053` |
| | The apparent tension with Section 02 | `:2070` |
| | **Lemma** data processing for total variation (+ proof) | `:2089` |
| | **Proposition** trajectories dominate snapshots (+ proof) | `:2104, :2118` |
| | Trajectory versus snapshot (SVG update chain); when is the gap strict | `:2132, :2161` |
| | The active attacker formalised; gradient ascent as a probe | `:2180, :2192` |
| | Measured: federated attacks (Table X); the isolating attacker; section takeaway | `:2209, :2225, :2245` |
| **05** — Synthesis | | `:2265-2440` |
| | **The single object** $\Lambda(z,O)$; the same three choices (6-row table); calibration | `:2272, :2286, :2301` |
| | The arc, as mathematics (chain); four bounds side by side | `:2317, :2346` |
| | What is actually settled; consequences for a defender; where the series goes next | `:2360, :2380, :2403` |

**Key results, all proved on slides:** **Thm 2** (exact advantage) `:387`; **Corollary**
$\Delta/B \le \mathrm{TV}$ `:508`; **Thm 1** (DP ceiling) `:701`; **Thm 3** (Gaussian) `:803`;
**Thm 4** (overfitting not necessary) `:886`; **Thm 5** (sigmoid form) `:1076`; **Thm 6**
(loss is sufficient) `:1212`; **Corollary** (sufficiency) `:1284`; **Property 1** `:1377`;
**Property 2** `:1422`; **Lemma** (TV is a metric) `:1641`; **Prop** (rank-one gradient) `:1920`;
**Lemma** (data processing) `:2089`; **Prop** (trajectories dominate) `:2104`.

**Counterexamples:** zero gap / full advantage `:584`; large gap / useless threshold `:617`.
Together they show the Yeom identity is one-directional, and kill the folklore reading
`Adv ≤ Δ` `:563`.

Deck-local figure family: prefix `m3-` (`.m3-fig` + `.lab` overlays, `.m3-algo`, `.m3-chain`,
`.m3-tight`), defined in the deck's own `<style>` block. Original SVG figures: attack fan-in
`:117`, member/non-member loss densities with threshold and shaded errors `:278`, gap-vs-advantage
number line `:540`, both counterexamples `:654`, advantage as a function of $\rho$ `:851`, Gibbs
posterior concentrating as $T \to 0$ `:1022`, sufficient-statistic collapse `:1318`, relaxation
staircase `:1675`, rank-one outer product `:1966`, trajectory versus snapshot `:2137`.

**Note (`mia3-theory-note.html`):** what moved onto the slides, including why the old
Markov-based "proof" was wrong `:39-45`; tightness and what the bounds do not say (per-record vs
population-average, slack in $\Delta/B \le \mathrm{TV}$, defences that shrink $\Delta$) `:47-59`;
Sablayrolles' assumptions (Gibbs vs real SGD, additive loss, one snapshot, MATT identifiability)
`:61-73`; Salem theory vs measurement `:75-79`; white-box feature dimensions table and measured
gains `:81-93`; speaker asides `:95-100`.

---

## mia4-modern.html

**Revised 2026-08** (53 → 147 slides, 8 sections). Every definition, theorem, proposition and
corollary below is stated **and proved on the slides**; the note holds only modelling caveats,
one secondary table and speaker asides.

| Part | Topic | Line |
|---|---|---|
| **01** — From optimal test to usable attack | | `:125-256` |
| | **Recall** cards: the MI game; every optimal attack is a ratio test; the loss carries the signal; data processing for TV | `:133, :152, :166, :179` |
| | The missing piece (nobody has the two densities); roadmap — one ratio, four estimators | `:193, :207` |
| | **Recall** where an attack must be measured (TPR at low FPR) | `:223` |
| | Log-log ROC that reset the field (Carlini Fig. 1) + how to read it | `:236, :245` |
| **02** — LiRA: a parametric per-example test | | `:259-816` |
| | **Definition 1** IN/OUT model distributions $\mathcal{Q}_{\mathrm{in}}(z), \mathcal{Q}_{\mathrm{out}}(z)$ | `:277` |
| | Why the honest ratio is unusable; why raw confidence is the wrong scalar | `:290, :301` |
| | **Definition 2** logit-scaled statistic $\phi(p)=\log\frac{p}{1-p}$ (+ SVG, + Carlini Fig. 4) | `:314, :327, :350` |
| | **Definition 3** the Gaussian LiRA statistic; what is assumed here | `:360, :373` |
| | **Theorem 1** closed form of $\log\Lambda$ (quadratic in $\ell$) + 3-step proof + recap | `:385, :398-451` |
| | **Corollary 1** equal variances ⟹ $\log\Lambda = dz - \tfrac12 d^2$ (+ proof, + two readings) | `:453, :466, :475` |
| | Per-example picture (SVG); one threshold, three examples (SVG) | `:487, :523` |
| | **Proposition 1** calibration dominates pooling (mixture + Jensen) + 3-step proof + recap | `:548, :561-616` |
| | Worked instance: pooled 0.9% vs calibrated 13.8% TPR at $10^{-3}$ | `:618` |
| | Per-example distributions really move (Carlini Fig. 3) | `:628` |
| | Online LiRA procedure (`.m4-algo`); **Definition 4** offline LiRA | `:650, :667` |
| | **Proposition 2** offline LiRA is a one-sided z-test, UMP by Karlin–Rubin (+ proof, + SVG) | `:680, :693, :704` |
| | Cost/power online vs offline; Carlini Table I @$10^{-3}$, @$10^{-5}$; balanced accuracy | `:729, :743, :759, :775` |
| **03** — The attack hierarchy: nested conditioning | | `:819-1102` |
| | The zoo of attacks; **Definition 5** one template for all of them | `:827, :840` |
| | **Lemma 1** (Ye 4.1) approximated LRT → loss threshold; the fine print (not optimality) | `:854, :867` |
| | **Definition 6** four conditioning sets S / P / R / D (Ye Table 1) | `:877` |
| | Population out-world; reference out-world; two ways to sweep (SVG); why it bites | `:892, :903, :914, :938` |
| | **Theorem 2** $V \subseteq V'$ ⟹ $\beta_V(\alpha) \le \beta_{V'}(\alpha)$ + 3-step proof (nesting → suprema → TV/DPI) + recap | `:951, :964-1019` |
| | **The ordering is partial, not total** (Hasse diagram SVG); what Theorem 2 does *not* say | `:1021, :1046` |
| | What Ye measured (S ≈ P; R beats S on 19.84% of inputs); auditing / Privacy Meter | `:1059, :1070, :1081` |
| **04** — RMIA: pairwise ratios, few models | | `:1105-1322` |
| | **Proposition 3** $\mathrm{Var}(\hat\sigma^2) = 2\sigma^4/(R-1)$, $\mathrm{sd}(\hat\sigma)/\sigma \approx 1/\sqrt{2(R-1)}$ (+ proof, + table) | `:1123, :1136, :1147` |
| | **Definition 7** $\mathrm{LR}_\theta(x,z) = \Pr(\theta\mid x)/\Pr(\theta\mid z)$; computable form; what $\Pr(x)$ is | `:1162, :1176, :1187` |
| | **Definition 8** $\mathrm{Score}(x;\theta) = \Pr_{z\sim\pi}[\mathrm{LR}_\theta(x,z) \ge \gamma]$; the score is a rank (SVG) | `:1200, :1213` |
| | Zarifzadeh Fig. 3 (AUC vs reference budget); Tables 2 and 3; the low-budget regime | `:1251, :1260, :1275, :1291` |
| | **A warning about cross-paper numbers** (their LiRA column is not Carlini's) | `:1302` |
| **05** — Label-only access | | `:1325-1484` |
| | **Definition 9** boundary distance as the attack statistic | `:1344` |
| | **Proposition 4** for a linear model $d(x) = \phi(h(x))/\|w\|_2$ (+ proof); **Corollary 2** nothing was hidden | `:1357, :1370, :1381` |
| | The geometry (SVG); beyond the linear case (proxy, not identity) | `:1393, :1416` |
| | Estimating $d$ from labels alone (boundary walk); reported query counts; Choquette-Choo Fig. 2(c) | `:1426, :1442, :1453` |
| **06** — Defenses | | `:1487-1714` |
| | Four families; the one question that sorts them (does it change the model?) | `:1495, :1508` |
| | **Definition 10** DP-SGD update `g̃_t = (1/B)(Σ clip(g_i,C) + N(0,σ²C²I))`; why those two operations; clip-then-blur (SVG) | `:1518, :1530, :1543` |
| | **Recall** the DP ROC cap; the cap at $\mathrm{FPR}=10^{-3}$ worked numerically; what DP-SGD does not give | `:1568, :1581, :1596` |
| | **Proposition 5** post-processing cannot increase TV (+ proof); **Corollary 3** the trap; channel diagram (SVG) | `:1609, :1621, :1632, :1645` |
| | MemGuard as predicted; defenses sorted by the right question; the evaluation standard | `:1668, :1679, :1694` |
| **07** — Beyond classification: diffusion models | | `:1717-1874` |
| | What breaks (no single loss); **Recall** the denoising objective | `:1725, :1735` |
| | **Definition 11** per-timestep statistic $\varphi_t(x_0) = \|\varepsilon - \varepsilon_\theta(\sqrt{\bar\alpha_t}x_0 + \sqrt{1-\bar\alpha_t}\varepsilon, t)\|_2^2$ | `:1747` |
| | Why fix $t$ rather than average; where the signal lives (SVG); the two endpoints (**intuition**) | `:1760, :1770, :1791` |
| | Matsumoto Fig. 4; the peak at $t=350$ cosine / $t=200$ linear, both $\bar\alpha_t = 0.7$; Table II; reading it honestly | `:1802, :1811, :1822, :1837` |
| | Porting the recipe | `:1847` |
| **08** — Synthesis | | `:1877-2002` |
| | **The template** $\hat\Lambda(z) = \hat p(\phi(z)\mid z \in D,\mathcal{C}) / \hat p(\phi(z)\mid z \notin D,\mathcal{C})$ | `:1885` |
| | What actually changed 2017→2024; attacks without / with reference models (2 tables) | `:1897, :1912, :1926` |
| | Proved in this lecture; **claimed, not proved**; if you have to run one; where the recipe runs out | `:1940, :1955, :1968, :1981` |

**Key results, all proved on slides:** **Thm 1** (closed form of the LiRA test) `:385`; **Cor 1**
(calibrated z-score) `:453`; **Prop 1** (calibration dominates pooling) `:548`; **Prop 2** (offline
is a one-sided UMP z-test) `:680`; **Lemma 1** (Ye's approximated LRT) `:854`; **Thm 2** (richer
conditioning cannot hurt) `:951`; **Prop 3** (variance of $\hat\sigma$) `:1123`; **Prop 4**
(distance is the logit) `:1357`; **Cor 2** (hiding scores hides nothing) `:1381`; **Prop 5**
(post-processing) `:1609`; **Cor 3** (output-side defenses cannot help) `:1632`.

**Definitions:** 1 IN/OUT worlds `:277`; 2 logit statistic `:314`; 3 LiRA statistic `:360`;
4 offline LiRA `:667`; 5 attack template `:840`; 6 four conditioning sets `:877`; 7 pairwise
likelihood ratio `:1162`; 8 RMIA score `:1200`; 9 boundary distance `:1344`; 10 DP-SGD update
`:1518`; 11 per-timestep statistic `:1747`.

Deck-local figure family: prefix `m4-` (`.m4-fig` + `.lab` overlays, `.m4-algo`, `.m4-chain`,
`.m4-tight`, `.m4-shot`), defined in the deck's own `<style>` block. Original SVG figures: logit
transform reshaping a skewed confidence density `:330`; per-example IN/OUT Gaussians with the
z-score arrow `:490`; one threshold against three examples `:526`; offline upper tail vs online
two-sided region `:707`; population sweep vs reference sweep `:917`; Hasse diagram of the partial
order `:1024`; RMIA population-rank axis `:1216`; boundary-distance geometry `:1396`; DP-SGD
clip-then-blur `:1546`; the post-processing channel `:1648`; diffusion signal against timestep
`:1773`.

Real paper figures (in `figs/`, all cropped from the arXiv PDFs): Carlini et al., IEEE S&P 2022
Fig. 1 `:238`, Fig. 4 `:352`, Fig. 3 `:630`; Zarifzadeh et al., ICML 2024 Fig. 3 `:1253`;
Choquette-Choo et al., ICML 2021 Fig. 2(c) `:1455`; Matsumoto et al. 2023 Fig. 4 — cited on the
measured-AUC slide `:1802`.

**Note (`mia4-modern-note.html`):** what moved onto the slides, the corrected monotonicity claim
(Ye's hierarchy is a design rationale, not a theorem) and the list of numbers deleted as
unverifiable `mia4-modern-note.html:40-44`; the Gaussian model as an assumption, the logit
transform, and where misspecification bites `:47-57`; what the hierarchy does not promise
(population level vs finite samples, per-record vs per-sample games, auditing asymmetry) `:60-70`;
reading RMIA's claims carefully `:73-77`; label-only cost model `:80-83`; DP-SGD honest scope
`:86-89`; diffusion measured vs intuited `:92-95`; fuller defense table `:98-110`; speaker asides
`:113-118`; open questions `:121-127`.

**Overview (`mia4-overview.html`):** single page, 8 sections matching the deck, plus the synthesis
table of statistic × conditioning × density estimator `:85-99` and three take-homes `:100`.

---

## mia5-llm.html

**Revised 2026-08** (37 → 123 slides, 5 sections). Every definition, theorem, proposition,
lemma and corollary below is stated **and proved on the slides**; the note holds assumptions,
provenance of every reported number, four corrections and speaker asides. Deck prefix `m5-`.

| Part | Topic | Line |
|---|---|---|
| **01** — Why LLM MIA is structurally hard | | `:112-537` |
| | **Recall** cards: the membership game; the modern per-example recipe | `:122, :137` |
| | What breaks at LLM scale; three threat models; the perplexity baseline; two confounds inside it | `:158, :182, :205, :220` |
| | **Model M1** (`.m5-algo`, A1–A4) — labelled *model-based, not a theorem about real LLMs* | `:243` |
| | **Proposition 1** membership shift $T^{\text{in}}-T^{\text{out}} = -\eta E\|g_x\|^2$ + proof | `:260, :277` |
| | **Proposition 2** $\mathrm{AUC}=\Phi(\rho/\sqrt2)$, $\sup\mathrm{Adv}=2\Phi(\rho/2)-1$, small-$\rho$ expansion + proof | `:295, :315` |
| | **Proposition 3** pooled $\rho \propto \eta E$ vs calibrated $\rho = \|g_x\|^2/\sqrt{N v_x}$ + two proof slides | `:331, :350, :366` |
| | Recap chain (`\stackrel`); the shift-against-spread SVG; reading Prop 3 | `:381, :402, :435` |
| | **Corollary 1** $\rho_{\text{cal}} \approx \sqrt{d_{\text{eff}}/N}$ under near-orthogonality (A5) | `:451` |
| | **What Model M1 does *not* say** (frozen gradients, no repetition, Gaussian scores) | `:466` |
| | Duan Fig. 2 (left) AUC vs steps + how to read it; Duan Fig. 2 (right) AUC vs epochs | `:481, :490, :504` |
| | Two knobs every attack turns (statistic × null) | `:513` |
| **02** — The calibration principle | | `:535-1187` |
| | **Definition 1** $s(x) = \log p_\theta(x) - \log q(x)$ | `:545` |
| | **Recall** why pooling loses (mixture + Jensen) | `:562` |
| | **Proposition 4** calibration helps iff $\sigma_\delta^2 \lt \sigma_a^2$ + proof; two failure modes of a null | `:577, :597, :614` |
| | One score, three nulls (SVG); what makes a good $q$ | `:635, :667` |
| | **Estimator 1** reference model (Carlini et al. 2021); where it breaks | `:682, :700` |
| | **Estimator 2** neighbourhood (Mattern et al. 2023) | `:718` |
| | **Lemma 1** exchangeable perturbations ⟹ exact level $1/(K+1)$ + proof + cloud SVG + failures | `:734, :751, :763, :791` |
| | **Estimator 3** SPV-MIA (Fu et al., NeurIPS 2024): self-generated reference; assumption + evidence | `:805, :826` |
| | **Estimator 4** context-aware (Chang et al., EMNLP 2025): cut-off loss and OLS slope | `:842, :857` |
| | CAMIA Fig. 3 (members descend faster); the rest of the family; what it buys (23.13% → 63.43% TPR@1%) | `:873, :881, :897` |
| | **Estimator 5** not all tokens are equal; **Recall** Min-K% (owned by 03-memorization) | `:913, :941` |
| | **Proposition 5** tail selection converges to a conditional tail expectation, not a calibrated LR + proof + SVG | `:956, :973, :988` |
| | InfoRMIA as a composite test (Tao & Shokri 2025) | `:1032` |
| | **Theorem 1** $\Lambda_{\text{Info}} = \log\frac{p(x\mid\theta)}{p(x)} + D_{\mathrm{KL}}(p(z)\|p(z\mid\theta))$ + proof | `:1054, :1071` |
| | **Corollary 2** it is Definition 1 again, with $q$ = population marginal | `:1089` |
| | Why the log average beats the count; token-level InfoRMIA (**proof of concept**); reported evidence | `:1104, :1120, :1136` |
| | The calibration zoo, then the same zoo read as assumptions | `:1152, :1167` |
| **03** — The empirical wall | | `:1185-1584` |
| | The headline question; **Duan et al., COLM 2024** — no attack above AUC 0.6 except GitHub | `:1195, :1210` |
| | Their diagnosis in Definition-1 notation (7-gram overlap 39.3% vs 13.9%) | `:1231` |
| | **Hayes et al., NeurIPS 2025** — give the attack everything (128 references); Fig. 2(a); the numbers | `:1247, :1264, :1273` |
| | Aggregate AUC is the wrong question | `:1292` |
| | **Proposition 6** $\mathrm{Var}(T)=\Delta^2/4+\sigma_{\text{run}}^2$, share $=\rho^2/(\rho^2+4)$ + proof + corollary + SVG | `:1306, :1323, :1339, :1356` |
| | Hayes Fig. 5 unstable member; how many records are coin flips (15.4%, 42.2%) | `:1380, :1389` |
| | **Das, Zhang & Tramèr, DATA-FM at ICLR 2025** — how the benchmarks were built | `:1403` |
| | **Proposition 7** different splits ⟹ $\sup\mathrm{Adv}=\mathrm{TV}(Q_1,Q_0)$, attained blind + proof + reading | `:1424, :1441, :1457` |
| | The blind-baseline confound (big SVG); Das Fig. 1 PCA; blind beats published, everywhere | `:1472, :1505, :1514` |
| | Corroboration from CAMIA (98.7% blind AUC on WikiMIA) | `:1529` |
| | **Corollary** what a valid split requires (random split ⟹ $\mathbb{E}[\mathrm{Adv}]=0$ blind); assembled argument | `:1545, :1563` |
| **04** — Where the signal still lives | | `:1582-1946` |
| | The regime change; **Corollary 3** reversal $\rho'_{\text{pool}}/\rho_{\text{pool}} = E'/E$, $\rho'_{\text{cal}}/\rho_{\text{cal}} = \sqrt{N/N'}$ + proof | `:1592, :1607, :1626` |
| | The two regimes on one plane (SVG); where this under-predicts; what the friendly regime delivers | `:1642, :1668, :1684` |
| | **Recall** three notions of memorization (owned by 03-memorization); extraction as a thresholded attack | `:1700, :1716` |
| | **Proposition 8** $\mathrm{FPR}(\mathcal{A}_{\text{ext}}) \le 2^{-h}$, $\mathrm{Adv}\ge\mathrm{TPR}-2^{-h}$ + proof | `:1733, :1751` |
| | The converse fails (counterexample); strict inclusions (SVG); MIA as extraction's ranker | `:1768, :1786, :1804` |
| | **Defense** DP fine-tuning; **Proposition 9** $\mathrm{AUC}\le 1-(1-\delta)^2/(2e^\varepsilon)$ + proof + numbers | `:1823, :1840, :1856, :1872` |
| | Defenses without a guarantee; why output filters do not help; why anyone outside asks (GDPR, NYT v. OpenAI) | `:1888, :1904, :1923` |
| **05** — Synthesis | | `:1944-2190` |
| | Every attack is one object; three choices, nothing else; the chain that runs through everything (SVG) | `:1954, :1968, :1991` |
| | Instances — the classical line; the language-model line | `:2021, :2037` |
| | Four eras; proved in this lecture (2 tables); claimed, not proved | `:2053, :2069, :2084, :2100` |
| | Key takeaways; the audit recipe (`.m5-algo`); open problems; where the recipe runs out; essential reading | `:2115, :2128, :2144, :2157, :2172` |

**Key results, all proved on slides:** **Prop 1** (membership shift) `:260`; **Prop 2** (ratio to
AUC and advantage) `:295`; **Prop 3** (pooled vs calibrated ceilings) `:331`; **Cor 1** (capacity
over data) `:451`; **Prop 4** (difficulty cancellation) `:577`; **Lemma 1** (exchangeability ⟹
valid rank test) `:734`; **Prop 5** (the selection effect) `:956`; **Thm 1** (InfoRMIA
decomposition) `:1054`; **Cor 2** (reduces to Definition 1) `:1089`; **Prop 6** (variance
decomposition, per-record instability) `:1306`; **Prop 7** (blind baselines as a validity failure)
`:1424`; **Cor 3** (the fine-tuning reversal) `:1607`; **Prop 8** (extraction implies inference)
`:1733`; **Prop 9** (DP AUC ceiling) `:1840`.

**Definition:** 1 calibrated score `:545` — the deck's organising object; every attack in §02 is
one estimator of its $q$.

Deck-local figure family: prefix `m5-` (`.m5-fig` + `.lab` overlays, `.m5-algo`, `.m5-chain`,
`.m5-tight`, `.m5-snug`, `.m5-shot`), defined in the deck's own `<style>` block. Original SVG
figures: shift-against-spread signal-to-noise panels `:405`; one score, three nulls `:638`; the
neighbourhood cloud `:766`; two surprisal profiles under the same tail rule `:991`; where the
variance goes (membership share bars) `:1359`; the blind-baseline confound `:1475`; the two
regimes on one plane `:1645`; strict inclusions (extractable ⊊ inferable ⊊ member) `:1789`; the
series-wide likelihood-ratio chain `:1994`.

Real paper figures (in `figs/`, cropped from the arXiv PDFs): Duan et al., COLM 2024 Fig. 2 left
`:484` and right `:507`; Chang et al., EMNLP 2025 Fig. 3 `:875`; Hayes et al., NeurIPS 2025
Fig. 2(a) `:1267` and Fig. 5 `:1383`; Das, Zhang & Tramèr, DATA-FM at ICLR 2025 Fig. 1 `:1508`.

**Note (`mia5-llm-note.html`):** what moved onto the slides, four corrections (CAMIA's statistic
and its direction; InfoRMIA's headline number and its true setting; 128 not 256 references; the
blind-baseline paper is Das/Zhang/Tramèr, not Maini) and the list of numbers deleted as
unverifiable `mia5-llm-note.html:42-68`; why LLMs break the classical toolkit `:72-89`;
perplexity and the direction of the calibration inequality `:93-104`; neighbourhood mechanics,
what Mattern actually claims, where it breaks `:108-121`; SPV-MIA mechanism and assumption
`:125-134`; CAMIA's six statistics and benchmark choice `:138-155`; InfoRMIA's composite null,
decomposition and per-setting results table `:159-178`; benchmarks and the empirical wall
`:182-195`; inference-to-extraction and the ownership note `:199-208`; defenses `:212-227`;
pseudocode for four attacks `:231-267`; open problems `:271`.

**Overview (`mia5-overview.html`):** single page, 5 sections matching the deck, the estimator
table `:65-73`, the take-home matrix `:98-106` and three take-homes `:108`. Every number in it
is quoted from a cited paper with its setting named.

---

## old/MIA.html

Legacy consolidated deck (~`:45` title) covering the foundational material now spread across mia1 + mia2 (Homer, indistinguishability, DP connection, evaluation, Shokri shadow models). Newer 5-lecture series supersedes it. Reference paths in this file are off by one level (broken before and after the recent reorg) — not actively used.
