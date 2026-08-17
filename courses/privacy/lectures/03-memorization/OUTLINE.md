# privacy/lectures/03-memorization/ — Memorization in generative models

Two decks (split 2026-05): **Part I** covers diffusion memorization end-to-end with an LLM bridge; **Part II** is LLM-only. Diffusion half builds Carlini → Somepalli → Webster → Wen → Ross, then **SAIL** (ICML 2025) and **CLIP-pad** (CVPR 2026 Findings). LLM half (math-detail revision 2026-08, 55 → 128 slides): Secret Sharer / exposure theory / Feldman, scaling laws, alignment and Min-K, **ACR**, books, defenses.

## Files

| Deck | Topic |
|---|---|
| `memorization-diffusion.html` | Intro (lawsuits + Bartz v. Anthropic) · **three formal definitions** · diffusion detection (Carlini→Wen, Ross/LID) · **SAIL** (smoothing theorem + Lemmas 4.1/4.2/4.3 with proofs) · **CLIP-pad** · bridge to LLM |
| `memorization-diffusion-note.html` | **Companion note** for the deck: full derivations kept off-slide (Levina–Bickel MLE, smoothing-theorem proof, simultaneous diagonalization, moment ladder, IBP regularity, cross-attention algebra, finite-difference bias/variance, three-definitions contrast) |
| `memorization-llm.html` | Defining (**exposure theory** + Feldman long tail) · extraction (Carlini 2021 → scaling/dedup → alignment/Nasr → **Min-K%/++**) · **ACR** (counting bound + MiniPrompt) · books (Cooper) · **defenses with proofs** (dedup / DP / $n$-gram blocking) |
| `memorization-llm-note.html` | **Companion note** for the LLM deck: exposure caveats, Feldman model assumptions, Min-K assumptions and the MIA boundary, alignment gaps, ACR's load-bearing assumptions, defense fine print, the four objects by type |
| `figs/` | 8 captured scientific plots/schematics: Carlini Fig 4/5, Somepalli Fig 5, Wen Fig 2, Ross LID schematic, SAIL eigenvalues + Pareto, CLIP-pad attention bar chart |

---

## memorization-diffusion.html

101 slides. Math-detail revision 2026-08: three definitions given as separate formal objects, every SAIL lemma carried by a statement card + on-slide proof, plus a smoothing theorem that unifies LID and sharpness.

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:43-103` |
| **01** — Why memorization matters | lawsuits, **Anthropic settlement**, copyright vs privacy | `:104-214` |
| | Central question | `:112` |
| | Three stakeholders | `:124` |
| | Live lawsuits 2023–2026 (Anthropic first) | `:147` |
| | **Bartz v. Anthropic — $1.5B** (Reuters cite) | `:162` |
| | Two lenses: copyright vs privacy | `:184` |
| **02** — Defining and detecting memorization | three definitions, Carlini, Somepalli, Webster, Wen, Ross | `:215-891` |
| | Diffusion recap | `:223` |
| | What would count as memorization? | `:234` |
| | **Definition 1 — $(\ell,\delta)$-extractability** | `:269` |
| | **Definition 1b — $(k,\ell)$-eidetic memorization** | `:282` |
| | Reading the extraction definition (SVG ball) | `:296` |
| | **Carlini 2023** overview + Ann Graham Lotz | `:324` |
| | **Carlini visual** verbatim (Lotz) vs diverse (Obama) | `:340` |
| | **Carlini** extraction pipeline | `:363` |
| | **Carlini** results — Fig 4 + Fig 5 (cite-right) | `:390` |
| | **Carlini gallery** (calrini3) | `:410` |
| | **Definition 2 — SSCD replication at level $\tau$** | `:426` |
| | What the threshold test decides (SVG) | `:438` |
| | **Somepalli visual** replication examples | `:460` |
| | **Somepalli histograms** (Fig 5) | `:475` |
| | Webster 2023 — MV / RV / TV taxonomy | `:490` |
| | **Definition 3 — the taxonomy, formally** | `:518` |
| | Three ways to copy (SVG) | `:531` |
| | Three definitions, three objects | `:572` |
| | **Wen seed (image)** same-seed comparison | `:591` |
| | **Wen seed (analysis)** reading the plot | `:602` |
| | Recall — guidance and the score | `:616` |
| | **Definition — Wen's detection statistic** | `:631` |
| | **Proposition — gap is an implicit classifier** | `:647` |
| | Proof — Bayes at noise level $t$ | `:659` |
| | Why memorization inflates the gap | `:671` |
| | Guidance as a vector gap (SVG) | `:681` |
| | **Wen verbatim** wen-1 | `:716` |
| | **Wen partial** wen-2 | `:731` |
| | **Wen regular** wen-3 | `:746` |
| | **Wen aggregate (Fig 2)** | `:761` |
| | **Wen findings** three empirical findings | `:775` |
| | **Wen mitigation (image)** wen-mitigate | `:789` |
| | **Wen mitigation (analysis)** | `:800` |
| | **Definition — local intrinsic dimension** | `:815` |
| | Reading the exponent (SVG ladder) | `:827` |
| | **Levina–Bickel nearest-neighbour MLE** | `:855` |
| | **Ross 2024 LID** schematic | `:868` |
| **03** — Our Method: SAIL | smoothing theorem → sharpness → three lemmas → noise optimization | `:892-1421` |
| | From dimension to curvature (bridge) | `:900` |
| | Setup — a density on a $k$-plane | `:916` |
| | **Theorem — smoothing a thin support** | `:941` |
| | Proof outline (+ key trick) | `:954` |
| | Step 1 — split the convolution | `:968` |
| | Step 2 — logs, then two derivatives | `:977` |
| | Proof recap (`\stackrel` chain) | `:986` |
| | **Corollary 1 (LID read-off) / Corollary 2 ($\mathrm{tr}\,H=-D/\sigma^2$)** | `:999` |
| | Sharp spike vs broad basin (SVG) | `:1014` |
| | **Sharpness in landscape** sail-sharpness image | `:1033` |
| | Sharpness of $\log p_t$ — definition | `:1044` |
| | Why the Hessian measures sharpness | `:1060` |
| | **Eigen concentration (SD)** sail-eigen | `:1076` |
| | Reading the SD eigen plots | `:1086` |
| | **Eigen concentration (MNIST)** sail-eigen-mnist | `:1101` |
| | The local Gaussian toolkit (precision eigenvalues $\Lambda_i$) | `:1112` |
| | **Lemma A (quadratic form)** — one lemma powers all three | `:1122` |
| | **Lemma 4.1** — score norm $= -\mathrm{tr}(H)$ | `:1134` |
| | Proof of Lemma 4.1 | `:1147` |
| | **Proposition** — score norm $=$ negative Laplacian (beyond Gaussians) | `:1158` |
| | Setup — conditional vs unconditional | `:1171` |
| | **Lemma 4.2** — Wen's metric = squared eigenvalue gap | `:1181` |
| | Proof of Lemma 4.2 | `:1193` |
| | Why the gap is weak at the first step | `:1205` |
| | **Lemma 4.3** — Hessian-score product $= -\mathrm{tr}(H^3)$ | `:1230` |
| | Proof of Lemma 4.3 | `:1242` |
| | **Proposition (moment ladder)** — $m=0$ Wen, $m=1$ SAIL | `:1253` |
| | **Proposed metric** $\|H^\Delta s^\Delta\|^2$ | `:1266` |
| | What the metric sees (SVG bar chart) | `:1277` |
| | The three lemmas in one line | `:1305` |
| | **Theory vs practice** sail-vs-wen | `:1320` |
| | Detection Results (SD v1.4 / v2.0) | `:1331` |
| | SAIL — mitigation by initialization | `:1351` |
| | Taylor approximation (directional-derivative justification) | `:1363` |
| | Final SAIL objective | `:1373` |
| | **Visual mitigation examples** sail-example | `:1387` |
| | **Quality vs memorization** sail-tradeoff (Pareto) | `:1398` |
| **04** — CLIP Embeddings Drive Memorization | training + padding-token cause + mitigations | `:1423-1620` |
| | **How CLIP is trained** (contrastive image/text) | `:1431` |
| | **$\langle$EoT$\rangle$ is the only token CLIP optimizes** | `:1444` |
| | **Cross-attention in Stable Diffusion** | `:1459` |
| | Tokenize / encode / attend (kim-token) | `:1475` |
| | **Padding embedding ≈ EoT embedding** | `:1490` |
| | **Proposition (padding amplification)** $A_{\text{eot}}=(1+|\mathcal{G}|)a_{\text{eot}}$ | `:1506` |
| | Seventy-seven slots, one vector (SVG) | `:1519` |
| | **Attention drop bar chart (CLIP-pad Fig 8)** | `:1558` |
| | **CLIP-pad mitigation example (kim-1)** | `:1578` |
| | Mitigation I — replace pad + mask EoT | `:1592` |
| | Mitigation II — partial padding mask | `:1606` |
| **05** — Bridge to LLM | why LLMs need their own framework | `:1622-1678` |
| | Diffusion vs autoregressive | `:1630` |
| | What's in Part II | `:1653` |
| | Takeaways (diffusion) | `:1667` |

**Key formulas:** $(\ell,\delta)$-extractability `:275`; $(k,\ell)$-eidetic `:287`; SSCD replication `:432`; Webster MV/RV/TV `:522`; Wen statistic `:636`; implicit-classifier identity `:653`; LID small-ball `:821`; Levina–Bickel Hill estimator `:859`; smoothed-support Hessian `:947`; corollaries `:1004`; sharpness Hessian `:1048`; Gaussian sharpness intuition `:1064`; Lemma A `:1129`; Lemma 4.1 `:1141`; score norm $=$ $-\mathbb{E}[\mathrm{tr}\,H]$ `:1164`; Lemma 4.2 `:1187`; Lemma 4.3 `:1236`; moment ladder `:1259`; proposed $\|H^\Delta s^\Delta\|^2$ `:1270`; three lemmas in one line `:1308`; Taylor approximation `:1368`; SAIL objective `:1376`; CLIP contrastive loss `:1435`; CLIP EoT vector `:1448`; cross-attention `:1463`; padding ≈ EoT `:1494`; padding amplification `:1512`.

**Key theorems / lemmas (statement card + on-slide proof):**
- **Theorem (spectrum of a smoothed low-dimensional density)** `:945` — Gaussian smoothing of a density on a $k$-plane gives block-diagonal $\nabla^2\log p_\sigma$ with exactly $D-k$ eigenvalues at $-\sigma^{-2}$. Proof `:954-997`. Corollaries `:1003`, `:1007`.
- **Proposition (implicit classifier gradient)** `:651` — $s^\Delta=\nabla\log p_t(c\mid x_t)$. Proof `:659`.
- **Lemma A (quadratic form)** `:1126` — $\mathbb{E}\|Az\|^2=\mathrm{tr}(A\Sigma A^\top)$; the single engine behind 4.1/4.2/4.3.
- **Lemmas 4.1 / 4.2 / 4.3 (Jeon-Kim-No 2025)** `:1139`, `:1185`, `:1234`; proofs `:1147`, `:1193`, `:1242`.
- **Proposition (score norm = negative Laplacian)** `:1162` — non-Gaussian generalization of 4.1 via integration by parts.
- **Proposition (moment ladder)** `:1257` — $\mathbb{E}\|(H^\Delta)^m s^\Delta\|^2=\sum_i(\Lambda_i-\Lambda_{i,c})^{2m+2}/\Lambda_{i,c}$.
- **Proposition (padding amplification)** `:1510` — $A_{\text{eot}}=(1+|\mathcal{G}|)\,a_{\text{eot}}$.

**Deck-local SVG diagrams** (`md-fig` / `md-algo` / `md-chain`, KaTeX labels in `.lab` overlays): tolerance ball `:296`; threshold-test densities `:438`; three-ways-to-copy `:531`; guidance vector gap `:681`; LID exponent ladder `:827`; sharp spike vs broad basin `:1014`; metric bar chart `:1277`; seventy-seven slots `:1519`.

**Companion note** — `memorization-diffusion-note.html`, nine sections: §0 sign conventions and the precision spectrum; §1 Levina–Bickel MLE in full (cited from slide `:855`); §2 smoothing-theorem proof with both corollaries; §3 simultaneous diagonalization + $s^\Delta=H^\Delta(x-\mu)$; §4 Lemma A and the moment ladder; §5 regularity for the integration-by-parts identity; §6 cross-attention algebra behind the padding amplification; §7 finite-difference bias/variance for $H^\Delta s^\Delta$; §8 the three definitions — what not to conflate.

**Figures (in `figs/`)** — mix of methodology plots and user-captured visual examples placed per explicit instructions:

Methodology / data plots (captions cropped out):
- `carlini_precision.png` — Carlini 2023 Fig 4 (attack precision curve)
- `carlini_duplicates.png` — Carlini 2023 Fig 5 (LAION duplicate count histogram)
- `somepalli_histograms.png` — Somepalli 2023 Fig 5 (top-1 similarity histograms across training-set sizes)
- `wen_fig2.png` — Wen 2024 Fig 2 (aggregate magnitude line plot + dataset density histogram)
- `ross_lid_schematic.png` — Ross 2024 Fig 1 (LID geometric schematic, 6 panels)
- `clippad_attention.png` — Kim & No 2026 Fig 8 (attention score drop, prompt vs EoT/pad slots)

User-captured visual examples (placed per instruction):
- `calrini-ann.png` — Carlini Ann Graham Lotz verbatim (Training Set + Generated Image)
- `calrini-obama.png` — Carlini Obama diverse-generation counter-example
- `calrini3.png` — Carlini gallery row (Original vs Generated pairs)
- `somepali.png` — Somepalli verbatim replication examples (gen vs LAION top-1 match)
- `wen-seed.png` — Wen normal-vs-memorized prompt collapse under same seed
- `wen-1.png` — Wen verbatim memorization example with metric
- `wen-2.png` — Wen partial memorization example with metric
- `wen-3.png` — Wen non-memorized example with metric
- `wen-mitigate.png` — Wen mitigation by suppression
- `kim-1.png` — Kim & No CVPR 2026 illustrative example (Original vs Ours)
- `kim-token.png` — Kim & No tokenize + encode architecture (pad ≈ EoT duplication)
- `sail-sharpness.png` — SAIL sharpness in distribution landscape (intro)
- `sail-eigen.png` — SAIL eigenvalue concentration on Stable Diffusion (Fig 3)
- `sail-eigen-mnist.png` — SAIL eigenvalue concentration on MNIST (Fig 2)
- `sail-vs-wen.png` — SAIL empirical validation: $\|s\|^2 \approx -\mathrm{tr}(H)$ and $\|Hs\|^2 \approx -\mathrm{tr}(H^3)$
- `sail-example.png` — SAIL mitigation qualitative examples (Original / Ours / prior methods)
- `sail-tradeoff.png` — SAIL Pareto plot (SSCD vs CLIP, SD v1.4 + v2.0)

---

## memorization-llm.html

128 slides. Math-detail revision 2026-08 (was 55): every named result now carries a statement card plus an on-slide proof or proof sketch, and the four *mathematically distinct* memorization objects (reproduction / counterfactual / compression / membership) are kept apart throughout. Reuses the diffusion deck's definitions ($(\ell,\delta)$-extractability, $(k,\ell)$-eidetic) rather than restating them.

| Part | Topic | Line |
|---|---|---|
| Title / Contents / Recall | autoregressive factorization, surprisal, why the objective memorizes | `:43-147` |
| | Recall — autoregressive model $\prod_t p_\theta(x_t\mid x_{<t})$ | `:109` |
| | Recall — per-token surprisal $\ell_t$ and its sum | `:120` |
| | Why this objective memorizes | `:131` |
| **01** — Defining LLM memorization | Secret Sharer / exposure (full theory) → Feldman long tail | `:148-726` |
| | Three notions — preview | `:156` |
| | Generalization vs memorization | `:181` |
| | **Carlini 2019** — Secret Sharer, the canary | `:196` |
| | **Definition 1** — log-perplexity and rank | `:210` |
| | The rank picture (SVG) | `:225` |
| | **Definition 2** — exposure | `:248` |
| | Why rank, not perplexity? (order invariance) | `:263` |
| | **Theorem 1** — exposure is an extraction budget | `:277`, proof `:290` |
| | Corollary — reading the budget | `:307` |
| | The guessing budget (SVG) | `:321` |
| | **Proposition 2** — bits of guesswork | `:342`, reading `:357` |
| | **Theorem 2** — null distribution $\Pr[\mathrm{exposure}\ge t]\le 2^{-t}$ | `:371`, proof `:384` |
| | Corollary — the null is tight (Stirling) | `:400` |
| | **Proposition 3** — exposure without enumeration | `:414` |
| | The exposure estimator (algorithm) | `:426` |
| | Scope of the exposure framework | `:442` |
| | Long-tail intuition · where the mass lives (Zipf SVG) | `:461`, `:476` |
| | **Definition 3** — memorization score (Feldman) | `:511` |
| | **Definition 4** — influence | `:526` |
| | The counterfactual experiment (SVG) | `:541` |
| | The long-tail model | `:575` |
| | **Theorem 3** — memorization is necessary | `:588`; Corollary 2 `:601` |
| | Proof sketch — outline / steps 1-2 / steps 3-4 / recap | `:612`, `:628`, `:638`, `:648` |
| | Why singletons force storage (SVG) | `:661` |
| | Complements, not substitutes · three notions as formal objects | `:693`, `:707` |
| **02** — Extraction attacks | Carlini 2021 → scaling laws → dedup → alignment → Nasr → Min-K | `:727-1220` |
| | **Definition 5** — extractable, $(k,\ell)$-eidetic | `:735`; discrete-metric remark `:749` |
| | What $f_\theta(\mathrm{greedy},p)$ means (SVG) | `:762` |
| | **Definition 6** — discoverable vs extractable | `:792` |
| | The extraction pipeline (algorithm) | `:812` |
| | Why a ratio, not a likelihood? · what is $p_{\mathrm{ref}}$ | `:827`, `:841` |
| | **Carlini 2022** — three scaling laws | `:856`; empirical law `:872`; term-by-term `:883` |
| | **Corollary 3** — the dedup arithmetic | `:899`; Lee 2022 | `:911` |
| | Recall — alignment is a tilt | `:925` |
| | **Proposition 5** — flat reward ⇒ base model | `:937`; where alignment binds (SVG) `:951` |
| | **Nasr 2023** — divergence attack | `:973`; what came out `:989`; alignment is a filter `:1005` |
| | Detour — membership inference · why the mean fails | `:1019`, `:1038` |
| | **Definition 7** — Min-K% Prob (Shi 2024) | `:1052`; surprisal profile (SVG) `:1065` |
| | **Proposition 6** — tail sufficiency | `:1107`, proof `:1119`, reading `:1135`; the test `:1149` |
| | **Definition 8** — Min-K%++ (Zhang 2025) | `:1162` |
| | **Proposition 7** — what $\mu_t$ really is ($=-H_t$) | `:1175`; reading `:1187` |
| | Memorization vs membership inference | `:1200` |
| **03** — Adversarial compression | ACR, GCG/MiniPrompt, probabilistic extraction, books | `:1221-1716` |
| | Counterfactual at corpus scale · its cost · why a new definition | `:1229`, `:1239`, `:1254` |
| | **Definition 9** — adversarial compression ratio (Schwarzschild 2024) | `:1268`; well-definedness remark `:1281` |
| | Weights as decompressor (SVG) | `:1294` |
| | **Proposition 8** — no trivial attack | `:1320` |
| | **Theorem 4** — compression is rare (counting bound) | `:1334`; outline `:1346`; steps `:1362`, `:1373`; chain `:1382` |
| | Pigeonhole picture (SVG) · **Corollary 4** — a number | `:1395`, `:1423` |
| | Tool — GCG (Zou 2023): surrogate, one iteration | `:1435`, `:1449`, `:1462` |
| | MiniPrompt — searching for $x^\star$ | `:1478` |
| | **Proposition 9** — one-sided soundness | `:1494`, reading `:1506`; what ACR reveals `:1520` |
| | **Definition 10** — probabilistic extraction (Hayes 2024) | `:1535` |
| | **Proposition 10** — the threshold in $p_{\mathrm{ext}}$ | `:1548`, reading `:1560` |
| | Approximate match — LCS variant | `:1573` |
| | **Cooper 2025** — books from open-weight LLMs (setup) | `:1586` |
| | **Cooper Fig 3** — per-book rates | `:1599`; headline results `:1613` |
| | **Cooper Fig 2** — 1984 sliding window | `:1627`; **Fig 8** books × models `:1641` |
| | What this means for the lawsuits | `:1652` |
| | **Aerni 2024** — non-adversarial reproduction | `:1667`; prompt families `:1679`; findings `:1700` |
| **04** — Defenses and open problems | dedup / DP / decoding, with what each provably gives | `:1717-2010` |
| | Three levers (data / training / decoding) | `:1725` |
| | Deduplication — the guarantee | `:1749` |
| | Recall — differential privacy | `:1768` |
| | **Theorem 5** — DP bounds memorization | `:1780`, proof `:1792` |
| | **Corollary 5** — when the bound is vacuous | `:1807` |
| | **Proposition 11** — duplicates break DP (group privacy) | `:1818` |
| | **Definition 11** — $n$-gram blocking | `:1831` |
| | **Proposition 12** — what blocking guarantees | `:1843`; one blocked step (SVG) `:1854`; what it does not give `:1881` |
| | Unlearning — the open lever · defenses side by side | `:1896`, `:1910` |
| | Open problems — measurement / scope / theory / defense | `:1928`, `:1939`, `:1951`, `:1962` |
| | The four objects · Takeaways | `:1973`, `:1991` |

**Key formulas:** autoregressive factorization `:113`; surprisal + sum `:125`; $\mathrm{px}_\theta$ / $\mathrm{rank}_\theta$ `:216`; exposure `:253`; Theorem 1 budget `:284`; guessing-entropy reading `:346`; null tail $2^{-t}$ `:378`; Corollary 1 (1.44 bits) `:405`; $\mathrm{rank}=|\mathcal R|F$ `:420`; exposure estimator (algorithm) `:429`; $\mathrm{mem}(A,S,i)$ `:517`; $\mathrm{infl}$ `:531`; Feldman bound $\mathrm{err}\ge\mathrm{opt}+\Omega$ `:594`; contrapositive `:605`; $f_\theta(\mathrm{greedy},p)=s$ `:741`; extraction pipeline (algorithm) `:815`; $\Lambda(x)$ ratio `:819`; surprisal decomposition $H(x)+\Delta_\theta(x)$ `:831`; repetition law `:878`; dedup arithmetic `:903`; mean surprisal $=\log$ PPL `:1042`; Min-K% `:1058`; tail-sufficiency likelihood ratio `:1113`; Min-K%++ `:1168`; $\mu_t=-H_t$ `:1181`; $z_t$ `:1191`; ACR `:1274`; counting bound `:1340`; GCG surrogate (algorithm) `:1465`; MiniPrompt (algorithm) `:1481`; one-sided soundness `:1500`; $p_{\mathrm{ext}}$ `:1539`; Hayes inversion `:1553`; LCS `:1577`; DP definition `:1774`; DP memorization bound `:1786`; vacuity `:1811`; group privacy `:1824`; $n$-gram blocking `:1835`.

**Key theorems / propositions (statement card + on-slide proof):**
- **Theorem 1 (exposure is an extraction budget)** `:282` — a rank-ordering adversary with $N$ guesses succeeds iff exposure $\ge\log_2|\mathcal R|-\log_2 N$. Proof `:290`; corollary `:307`.
- **Proposition 2 (bits of guesswork)** `:346` — exposure read as guessing entropy; caveats in the note.
- **Theorem 2 (null distribution)** `:376` — $\Pr[\mathrm{exposure}\ge t]\le 2^{-t}$ under a uniform-rank null. Proof `:384`; tightness by Stirling `:404`.
- **Proposition 3 (exposure without enumeration)** `:419` — $\mathrm{rank}=|\mathcal R|\,F(\mathrm{px})$, so a fitted skew-normal replaces $|\mathcal R|$ scoring passes.
- **Theorem 3 (Feldman 2020, long tail — marked a sketch)** `:592` — singleton subpopulations force $\mathrm{err}\ge\mathrm{opt}+\Omega(\cdot)$ unless memorized. Sketch `:612-660`; key trick `:622`.
- **Proposition 5 (flat reward ⇒ base model)** `:941` — the KL-regularized alignment optimum collapses to $\pi_{\mathrm{ref}}$; explains why divergence attacks work.
- **Proposition 6 (tail sufficiency)** `:1112` — under tail-clipping the Neyman-Pearson ratio depends only on the $K\%$ most-surprising tokens. Proof `:1119`.
- **Proposition 7 ($\mu_t=-H_t$)** `:1179` — Min-K%++'s calibration term is the next-token entropy; this is the whole content of the ++.
- **Proposition 8 (no trivial attack)** `:1324` — a prompt cannot be shorter than the incompressible content it elicits.
- **Theorem 4 (compression is rare)** `:1338` — pigeonhole/counting bound on the fraction of strings with $\mathrm{ACR}>1$. Proof `:1346-1394`; key trick `:1356` (determinism makes witness selection injective); numeric corollary `:1423`.
- **Proposition 9 (one-sided soundness)** `:1498` — MiniPrompt's $\widehat{\mathrm{ACR}}$ under-estimates; ACR evidence is sound, never complete.
- **Proposition 10 (threshold in $p_{\mathrm{ext}}$)** `:1552` — Hayes' $(n,q)$-extractability inverted into a per-prompt probability threshold.
- **Theorem 5 (DP bounds memorization)** `:1784` — $\varepsilon$-DP gives a multiplicative bound on any extraction event. Proof `:1792`; **Corollary 5 (vacuity)** `:1811`; **Proposition 11 (duplicates break DP)** `:1822`.
- **Proposition 12 ($n$-gram blocking)** `:1847` — induction over decode steps: no $n$-gram of the blocked corpus is ever emitted; limits at `:1881`.

**Deck-local SVG diagrams** (`ml-fig` / `ml-algo` / `ml-chain`, KaTeX labels in `.lab` overlays): rank picture `:225`; guessing-budget bar `:321`; long-tail Zipf bars `:476`; leave-one-out counterfactual `:541`; singleton subpopulations `:661`; where alignment binds `:951`; surprisal profile, clipped vs spiking tails `:1065`; weights as decompressor `:1294`; pigeonhole `:1395`; one blocked decode step `:1854`.

**Companion note** — `memorization-llm-note.html`, eight sections: §0 notation and sign conventions; §1 exposure (why rank not probability, the tail bound, the Stirling check, skew-normal cautions, guessing-entropy/Jensen caveat); §2 Feldman (mixture-with-prior model, the $\tau_1$-vs-$n$ dependence, Step-3 exchangeability, coupling error, what the theorem does *not* license); §3 Min-K (independence and tail-clipping assumptions, why $K\approx20\%$, the ++ entropy correction and its logit access, boundary with the MIA lecture); §4 alignment tilt — three gaps; §5 ACR (Theorem 4's three load-bearing assumptions, the numeric corollary is arithmetic not measurement, one-sided guarantee); §6 defenses (multiplicative vs crude DP bound, group privacy, blocking induction, degenerate renormalization); §7 the four objects and their mathematical types.

**Cooper 2025 figures (in `figs/`, preserved from the pre-revision deck with their citations):** `cooper_rates.png` (Fig 3, per-book rates) `:1599`, `cooper_1984.png` (Fig 2, sliding-window) `:1627`, `cooper_heatmap.png` (Fig 8, books × models) `:1641`.

---

## Cross-references

- **Diffusion preliminaries** at `memorization-diffusion.html:223` reuse score-based notation from `privacy/lectures/02-generative/diffusion3-sde-score.html`. Self-contained "Recall" cards only (`:223`, `:616`), no re-derivation.
- **Classifier-free guidance** recalled at `memorization-diffusion.html:616` from `privacy/lectures/02-generative/diffusion5-guidance-discrete.html`; that deck is also the style model for the theorem/proof-step/recap pattern used throughout §03.
- **SAIL** (Jeon, Kim, No 2025) is the lab's main contribution and motivates the diffusion sharpness framing. Detection metric extends Wen 2024 via the Hessian-score product (Lemma 4.3 cubic amplification). Mitigation is inference-time noise optimization, leaving prompt and weights untouched.
- **CLIP-pad mitigation** (Kim, No 2026 CVPR Findings, arXiv 2605.02908) is a complementary inference-time fix — different mechanism, same target prompt set.
- **Carlini 2021** extraction also appears in `privacy/lectures/04-mia/mia5-llm.html:166` (perplexity baseline).
- **Cooper 2025** book extraction motivates the unlearning lectures — see `privacy/lectures/05-unlearning/unlearning1-foundations.html:91` ("Why Now").
- **ACR** is referenced as the audit benchmark in `privacy/lectures/05-unlearning/unlearning2-llm.html` (benchmarks/failures, Part II).
- **Memorization vs MIA** comparison links to `privacy/lectures/04-mia/mia1-foundations.html`; Min-K%/Min-K%++ are explicit bridges.
- **Bartz v. Anthropic** is the new copyright anchor (replaces NYT-only framing). Reuters Dec 4 2025 article cited.
- **Defenses → unlearning** flows directly into `privacy/lectures/05-unlearning/unlearning1-foundations.html` (Part I).
