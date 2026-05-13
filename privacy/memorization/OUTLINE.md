# privacy/memorization/ — Memorization in generative models

Two decks (split 2026-05): **Part I** covers diffusion memorization end-to-end with an LLM bridge; **Part II** is LLM-only. Diffusion half builds Carlini → Somepalli → Webster → Wen → Ross, then **SAIL** (ICML 2025) and **CLIP-pad** (CVPR 2026 Findings). LLM half: Secret Sharer / exposure / Feldman, scaling laws, Min-K, **ACR**.

## Files

| Deck | Topic |
|---|---|
| `memorization-diffusion.html` | Intro (lawsuits + Bartz v. Anthropic) · diffusion detection (Carlini→Wen, Ross/LID) · **SAIL** · **CLIP-pad** · bridge to LLM |
| `memorization-llm.html` | Defining (canary→long-tail) · extraction (GPT-2→Nasr→Min-K) · **ACR** · books · defenses |
| `figs/` | 8 captured scientific plots/schematics: Carlini Fig 4/5, Somepalli Fig 5, Wen Fig 2, Ross LID schematic, SAIL eigenvalues + Pareto, CLIP-pad attention bar chart |

---

## memorization-diffusion.html

| Part | Topic | Line |
|---|---|---|
| Title / Contents | | `:18-79` |
| **01** — Why memorization matters | lawsuits, **Anthropic settlement**, copyright vs privacy | `:80-195` |
| | Central question | `:91` |
| | Three stakeholders | `:103` |
| | Live lawsuits 2023–2026 (Anthropic first) | `:126` |
| | **Bartz v. Anthropic — $1.5B** (Reuters cite) | `:141` |
| | Two lenses: copyright vs privacy (4 bullets/lens) | `:163` |
| **02** — Detection in diffusion | Carlini, Somepalli, Webster, Wen, Ross | `:197-535` |
| | Diffusion recap | `:203` |
| | **Carlini 2023 #1** overview + Ann Graham Lotz | `:214` |
| | **Carlini visual** verbatim (Lotz) vs diverse (Obama) | `:230` |
| | **Carlini 2023 #2** extraction pipeline | `:253` |
| | **Carlini 2023 #3** results — Fig 4 + Fig 5 (cite-right) | `:280` |
| | **Carlini gallery** more memorized examples (calrini3) | `:300` |
| | **Somepalli visual** SSCD defined + replication examples | `:316` |
| | **Somepalli histograms** similarity distribution (Fig 5) | `:331` |
| | Webster — MV / RV / TV taxonomy schematic | `:346` |
| | **Wen seed (image)** same-seed comparison | `:374` |
| | **Wen seed (analysis)** reading the plot | `:385` |
| | **Wen #1** score-norm metric | `:399` |
| | **Wen verbatim** wen-1 | `:413` |
| | **Wen partial** wen-2 | `:428` |
| | **Wen regular** wen-3 | `:443` |
| | **Wen aggregate (Fig 2)** | `:458` |
| | **Wen findings** three empirical findings | `:472` |
| | **Wen mitigation (image)** wen-mitigate | `:486` |
| | **Wen mitigation (analysis)** what changes | `:497` |
| | **Ross 2024 LID** schematic (smaller, more bullet room) | `:512` |
| **03** — Our Method: SAIL | sharpness theory + noise optimization | `:536-760` |
| | **Sharpness in landscape** sail-sharpness image | `:546` |
| | Sharpness definition (Hessian, eigenvalues) | `:557` |
| | **Eigen concentration (SD)** sail-eigen | `:573` |
| | Reading the SD eigen plots | `:583` |
| | **Eigen concentration (MNIST)** sail-eigen-mnist | `:598` |
| | **Lemma 4.1** — score norm $= -\mathrm{tr}(H)$ | `:609` |
| | **Lemma 4.2** — Wen's metric = squared eigenvalue gap | `:622` |
| | **Lemma 4.3** — Hessian-score product $= -\mathrm{tr}(H^3)$ | `:635` |
| | **Proposed metric** $\|H^\Delta s^\Delta\|^2$ | `:648` |
| | **Theory vs practice** sail-vs-wen | `:659` |
| | Detection Results (SD v1.4 / v2.0) | `:670` |
| | SAIL — mitigation by initialization | `:690` |
| | Taylor approximation | `:702` |
| | Final SAIL objective | `:712` |
| | **Visual mitigation examples** sail-example | `:726` |
| | **Quality vs memorization** sail-tradeoff (Pareto) | `:737` |
| **04** — CLIP Embeddings Drive Memorization | padding-token cause + mitigations | `:761-866` |
| | Tokenize / encode / attend (kim-token) | `:770` |
| | **Padding embedding ≈ EoT embedding** | `:785` |
| | **Attention drop bar chart (CLIP-pad Fig 8)** | `:801` |
| | **CLIP-pad mitigation example (kim-1)** | `:821` |
| | Mitigation I — replace pad + mask EoT | `:837` |
| | Mitigation II — partial padding mask | `:851` |
| **05** — Bridge to LLM | why LLMs need their own framework | `:867-920` |
| | Diffusion vs autoregressive | `:874` |
| | What's in Part II | `:897` |
| | Takeaways (diffusion) | `:911` |

**Key formulas:** Sharpness Hessian `:561`; Lemma 4.1 `:614`; Lemma 4.2 `:627`; Lemma 4.3 `:640`; Proposed $\|H^\Delta s^\Delta\|^2$ `:653`; Padding ≈ EoT `:790`.

**Key theorems / lemmas:** Lemmas 4.1 / 4.2 / 4.3 (Jeon-Kim-No 2025) `:614, :627, :640`.

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
| Title / Contents / Recall | | `:18-79` |
| **Training objective** — next-token prediction + why it memorizes | `:82-104` |
| | Autoregressive factorization + NLL loss | `:82` |
| | Why this objective memorizes | `:93` |
| **01** — Defining LLM memorization | Zhang, Carlini 2019, exposure, Feldman | `:110-231` |
| | Zhang 2017 — random labels | `:118` |
| | **Carlini 2019** — Secret Sharer (canary, R = 10^9 example) | `:133` |
| | Exposure — calibrated memorization score | `:147` |
| | Null distribution tail $\Pr[\mathrm{exp}\ge t]\le 2^{-t}$ (derivation) | `:160` |
| | Long-tail intuition | `:176` |
| | Counterfactual memorization (definition) | `:191` |
| | **Feldman 2020** — long-tail theorem | `:204` |
| | Implication — memorization is necessary | `:217` |
| **02** — Extraction attacks | Carlini 2021, scaling, dedup, Nasr, Min-K | `:233-442` |
| | **Carlini 2021** — $k$-extractable, $k$-eidetic, GPT-2 | `:241` |
| | $f_\theta(\mathrm{greedy}, p)$ diagram | `:255` |
| | Extraction pipeline | `:285` |
| | $p_{\text{ref}}$ reference-model variants | `:308` |
| | **Carlini 2022** — three scaling laws | `:323` |
| | Repetition empirical law | `:339` |
| | Term-by-term ($p_0$, $N_\theta$, $L_{\text{ctx}}$, rarity) | `:350` |
| | Lee 2022 — deduplication | `:366` |
| | Nasr 2023 — divergence attack | `:380` |
| | What came out (PII, code, copyrighted text) | `:397` |
| | **Min-K% Prob** (Shi 2024) — lowest-$K\%$ tokens | `:413` |
| | **Min-K%++** (Zhang 2025) | `:427` |
| **03** — Adversarial compression and beyond | ACR, books, defenses | `:444-770` |
| | Why a new definition (Zhang et al. 2023 counterfactual cited) | `:452` |
| | Retraining cost — counterfactual is infeasible | `:467` |
| | **ACR formal definition** (Schwarzschild 2024) | `:483` |
| | Reading ACR — compression as storage | `:497` |
| | GCG primer (Zou 2023) | `:511` |
| | GCG one iteration | `:525` |
| | MiniPrompt — search by GCG | `:552` |
| | ACR — what it reveals | `:580` |
| | Hayes 2024 — probabilistic extraction $(n,q)$-extractable | `:595` |
| | Approximate match — LCS variant (longest common substring) | `:606` |
| | Cooper 2025 — books from open-weight LLMs (setup) | `:620` |
| | Cooper 2025 — headline results (Llama 3.1 70B, HP1, 1984) | `:634` |
| | Cooper 2025 — lawsuit discourse implications | `:648` |
| | Aerni 2024 — non-adversarial reproduction (benign prompts) | `:663` |
| | Aerni 2024 — findings (15% avg, 100% worst-case) | `:677` |
| | Defenses (dedup / DP / unlearning) | `:692` |
| | Memorization vs MIA | `:718` |
| | Open problems — measurement | `:739` |
| | Open problems — scope | `:750` |
| | Open problems — theory and defense | `:762` |
| | Takeaways (LLMs) | `:774` |

**Key formulas:** Next-token NLL `:88`; Exposure `:152`; Null tail derivation `:165`; Counterfactual mem `:196`; Long-tail theorem `:210`; $k$-extractable `:246`; Repetition law `:343`; Min-K% `:418`; Min-K%++ `:432`; ACR `:489`; Probabilistic extraction `:600`; LCS variant `:611`.

**Key theorems / lemmas:** Long-tail (Feldman 2020) `:210`; ACR definition (Schwarzschild 2024) `:489`; Counterfactual memorization (Zhang et al. 2023) `:472`.

---

## Cross-references

- **Diffusion preliminaries** at `memorization-diffusion.html:195` reuse score-based notation from `privacy/generative/diffusion3-sde-score.html`. No re-derivation here — pointer only.
- **SAIL** (Jeon, Kim, No 2025) is the lab's main contribution and motivates the diffusion sharpness framing. Detection metric extends Wen 2024 via the Hessian-score product (Lemma 4.3 cubic amplification). Mitigation is inference-time noise optimization, leaving prompt and weights untouched.
- **CLIP-pad mitigation** (Kim, No 2026 CVPR Findings, arXiv 2605.02908) is a complementary inference-time fix — different mechanism, same target prompt set.
- **Carlini 2021** extraction also appears in `privacy/mia/mia5-llm.html:166` (perplexity baseline).
- **Cooper 2025** book extraction motivates the unlearning lectures — see `privacy/unlearning/unlearning.html:108`.
- **ACR** is referenced as the audit benchmark in `privacy/unlearning/unlearning.html` (compliance theatre slide).
- **Memorization vs MIA** comparison links to `privacy/mia/mia1-foundations.html`; Min-K%/Min-K%++ are explicit bridges.
- **Bartz v. Anthropic** is the new copyright anchor (replaces NYT-only framing). Reuters Dec 4 2025 article cited.
- **Defenses → unlearning** flows directly into `privacy/unlearning/unlearning.html`.
