# privacy/lectures/03-memorization/ — Memorization in generative models

Two decks (split 2026-05): **Part I** covers diffusion memorization end-to-end with an LLM bridge; **Part II** is LLM-only. Diffusion half builds Carlini → Somepalli → Webster → Wen → Ross, then **SAIL** (ICML 2025) and **CLIP-pad** (CVPR 2026 Findings). LLM half: Secret Sharer / exposure / Feldman, scaling laws, Min-K, **ACR**.

## Files

| Deck | Topic |
|---|---|
| `memorization-diffusion.html` | Intro (lawsuits + Bartz v. Anthropic) · **three formal definitions** · diffusion detection (Carlini→Wen, Ross/LID) · **SAIL** (smoothing theorem + Lemmas 4.1/4.2/4.3 with proofs) · **CLIP-pad** · bridge to LLM |
| `memorization-diffusion-note.html` | **Companion note** for the deck: full derivations kept off-slide (Levina–Bickel MLE, smoothing-theorem proof, simultaneous diagonalization, moment ladder, IBP regularity, cross-attention algebra, finite-difference bias/variance, three-definitions contrast) |
| `memorization-llm.html` | Defining (canary→long-tail) · extraction (GPT-2→Nasr→Min-K) · **ACR** · books · defenses |
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

| Part | Topic | Line |
|---|---|---|
| Title / Contents / Recall | | `:22-79` |
| **Training objective** — next-token prediction + why it memorizes | `:82-105` |
| | Autoregressive factorization + NLL loss | `:83` |
| | Why this objective memorizes | `:94` |
| **01** — Defining LLM memorization | Zhang, Carlini 2019, exposure, Feldman | `:110-226` |
| | Zhang 2017 — random labels | `:119` |
| | **Carlini 2019** — Secret Sharer (canary, R = 10^9 example) | `:134` |
| | Exposure — calibrated memorization score | `:148` |
| | Null distribution tail $\Pr[\mathrm{exp}\ge t]\le 2^{-t}$ (derivation) | `:161` |
| | Long-tail intuition | `:175` |
| | Counterfactual memorization (definition) | `:190` |
| | **Feldman 2020** — long-tail theorem | `:203` |
| | Implication — memorization is necessary | `:216` |
| **02** — Extraction attacks | Carlini 2021, scaling, dedup, Nasr, Min-K (MIA bridge) | `:228-462` |
| | **Carlini 2021** — $k$-extractable, $k$-eidetic, GPT-2 | `:240` |
| | $f_\theta(\mathrm{greedy}, p)$ diagram | `:254` |
| | Extraction pipeline | `:284` |
| | $p_{\text{ref}}$ reference-model variants | `:307` |
| | **Carlini 2022** — three scaling laws | `:322` |
| | Repetition empirical law | `:338` |
| | Term-by-term ($p_0$, $N_\theta$, $L_{\text{ctx}}$, rarity) | `:349` |
| | Lee 2022 — deduplication | `:365` |
| | **Nasr 2023** — divergence attack, takeaway lead | `:379` |
| | What came out (PII, code, copyrighted text) | `:397` |
| | **MIA teaser** — why Min-K% is MIA-flavored | `:413` |
| | **Min-K% Prob** (Shi 2024) — MIA probe | `:433` |
| | **Min-K%++** (Zhang 2025) — MIA probe | `:447` |
| **03** — Adversarial compression and beyond | ACR, books (3 visuals), defenses | `:463-790` |
| | **Counterfactual (Zhang 2023) — Recap + drawback** | `:472` |
| | Why a new definition | `:490` |
| | **ACR formal definition** (Schwarzschild 2024) | `:504` |
| | Reading ACR — compression as storage | `:518` |
| | GCG primer (Zou 2023) | `:532` |
| | **GCG — Gradient surrogate detail** | `:546` |
| | GCG one iteration | `:561` |
| | MiniPrompt — search by GCG | `:588` |
| | ACR — what it reveals | `:616` |
| | Hayes 2024 — probabilistic extraction $(n,q)$-extractable | `:631` |
| | Approximate match — LCS variant | `:642` |
| | Cooper 2025 — books from open-weight LLMs (setup) | `:656` |
| | **Cooper Fig 3** — bars + per-book table (HP vs Sandman Slim) | `:670` |
| | Cooper headline results (Llama 3.1 70B, HP1, 1984) | `:684` |
| | **Cooper Fig 2** — 1984 sliding-window heatmap | `:698` |
| | **Cooper Fig 8** — books × models memorization heatmap | `:712` |
| | Cooper — lawsuit discourse implications | `:723` |
| | **Aerni 2024** — non-adversarial reproduction (motivation lead) | `:738` |
| | Aerni — findings (15% avg, 100% worst-case) | `:755` |
| | Defenses (dedup / DP / unlearning) | `:770` |
| | Memorization vs MIA | `:796` |
| | Open problems — measurement | `:817` |
| | Open problems — scope | `:828` |
| | Open problems — theory and defense | `:840` |
| | Takeaways (LLMs) | `:852` |

**Key formulas:** Next-token NLL `:86`; Exposure `:151`; Null tail derivation `:164`; Counterfactual mem `:193`; Long-tail theorem `:208`; $k$-extractable `:245`; Repetition law `:343`; Counterfactual mem (recap) `:476`; Min-K% `:436`; Min-K%++ `:450`; ACR `:507`; GCG one-hot gradient `:551`; Probabilistic extraction `:635`; LCS variant `:646`.

**Key theorems / lemmas:** Long-tail (Feldman 2020) `:208`; ACR definition (Schwarzschild 2024) `:507`; Counterfactual memorization (Zhang et al. 2023) recap `:476`.

**Cooper 2025 figures (in `figs/`):** `cooper_rates.png` (Fig 3, bars + table), `cooper_1984.png` (Fig 2, sliding-window), `cooper_heatmap.png` (Fig 8, books × models).

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
