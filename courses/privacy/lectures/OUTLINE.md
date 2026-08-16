# privacy/lectures/ — Privacy lecture series

Master-level series on privacy, copyright, and provenance in generative models. Folders are numbered in reading order (`01-`…`06-`); deck filenames keep their intra-topic numbering (`dp1-…`, `diffusion1-…`, `mia1-…`). Several decks have a paired `<deck>-note.html` companion (notes hold full derivations and proof detail; decks hold rigorous statements + intuition).

Exams live one level up in `../exam/`.

## Subfolders

- **`01-dp/`** — Differential privacy (8 decks). `dp1`–`dp7` build foundations: reconstruction attacks → pure DP → properties → approximate DP → DP-SGD → RDP → DP in ML / PATE. `dp8-fl.html` is the capstone applied talk (NeurIPS 2023). Source LaTeX in `tex/dp.tex`. See `01-dp/OUTLINE.md`.
- **`02-generative/`** — Generative-model review. **Diffusion** (5 lectures, from-scratch Bayes-route, SDE, DDIM, guidance, discrete) and **LLM** (1 brief deck: tokens, decoder-only transformer, NLL pretraining, sampling, privacy hooks). Companion notes: `diffusion3-sde-score-note.html` and `note/2_difffusion.tex` (LaTeX). See `02-generative/OUTLINE.md`.
- **`03-memorization/`** — Memorization in generative models. **Two decks (split 2026-05)**: `memorization-diffusion.html` (intro + lawsuits + Bartz/Anthropic, three formal definitions, diffusion detection, SAIL, CLIP-pad, LLM bridge; math-detail revision 2026-08 — 101 slides, theorem/lemma cards with on-slide proofs, companion `memorization-diffusion-note.html`) and `memorization-llm.html` (canary→ACR). Captured paper figures in `figs/`. See `03-memorization/OUTLINE.md`.
- **`04-mia/`** — Membership inference attacks (5 lectures, paired notes). Plus legacy `old/MIA.html`. See `04-mia/OUTLINE.md`.
- **`05-unlearning/`** — Machine unlearning. Definitions, classification methods, LLM methods, benchmarks, lab work. See `05-unlearning/OUTLINE.md`.
- **`06-watermark/`** — LLM watermarking (single deck). Green-list, distortion-free, undetectable, robustness, radioactivity. See `06-watermark/OUTLINE.md`.

## Reading order

1. **`01-dp/`** — differential privacy: the formal privacy backbone (reconstruction → ε-DP → (ε,δ)-DP → DP-SGD → RDP → PATE → DP-FL capstone).
2. **`02-generative/`** — generative-model review (diffusion + LLM); pins down the score, sampling, and per-token loss that every downstream attack plugs into.
3. **`03-memorization/`** — what generative models retain; the *signal* unlearning removes and MIA detects.
4. **`04-mia/`** — membership inference; the detection lens, with DP as its formal bound.
5. **`05-unlearning/`** — machine unlearning; certified/Newton theory reuses DP, evaluation reuses MIA.
6. **`06-watermark/`** — provenance by construction; the opposite direction from memorization.

## Theme connections

- **generative review ↔ everything downstream**: `02-generative/` pins down score, sampling, discrete-space generation; `llm.html` pins down $p_\theta(\cdot\mid x_{<t})$, per-token loss $\ell_t$, the sampling step. MIA / memorization / watermarking / unlearning each plug into one of those pieces (LLM 4-card map at `02-generative/llm.html:1101`).
- **diffusion ↔ llm (within `02-generative/`)**: parallel reviews. Diffusion = continuous score-based generation; LLM = discrete autoregressive counterpart. Privacy attacks differ in mechanism but share targets (training-data leakage, provenance, removal).
- **diffusion ↔ MIA**: diffusion-model MIA is a research frontier — `04-mia/mia4-modern.html:731-789` covers it. The diffusion-models theory in `02-generative/` provides the substrate.
- **DP ↔ MIA**: `04-mia/mia1-foundations.html:601-617` shows DP as MIA bound (`Adv ≤ e^ε−1+δ`); `01-dp/dp8-fl.html` builds the DP machinery. DP-SGD is referenced from `04-mia/mia4-modern.html:117`.
- **DP ↔ unlearning**: certified $(\varepsilon,\delta)$-unlearning reuses the DP definition from `01-dp/dp8-fl.html:375` — same bound, different distribution comparison.
- **memorization ↔ unlearning ↔ MIA**: memorization is the *signal* unlearning aims to remove and MIA aims to detect. `03-memorization/memorization-diffusion.html` + `memorization-llm.html` motivate the other two; defenses slide flows directly into `05-unlearning/`. `05-unlearning/unlearning1-foundations.html:487` reuses the SALUN MIA-Efficacy column.
- **memorization ↔ watermark**: both about provenance under copyright pressure, but opposite directions — memorization detects unintended retention, watermarking adds intended traceability. Same lawsuits motivate both.
- **dgMARK ↔ watermark**: lab thread for diffusion LLMs — full context in `talks/kics260521dllm/kics260521dllm.html:524-569`, broader watermark survey in `06-watermark/`.
- **Theoretical diffusion (`courses/infotheory/lectures/07-diffusion/`) vs from-scratch (`02-generative/`)**: same math, different presentation. The infotheory series uses information-theoretic / hierarchical-VAE framing (cleaner for theory students); the privacy series uses the Bayes-+-Taylor route and goes further (5 lectures including SDE, DDIM, CFG, discrete).

## Quick lookup — cross-deck pointers

| Topic | Where | Lines |
|---|---|---|
| Reconstruction attack (Dinur–Nissim) | `01-dp/dp1-reconstruction.html` | `:181-244` |
| Randomized response + sample complexity | `01-dp/dp2-pure-dp.html` | `:78-148` |
| **$\varepsilon$-DP definition + Laplace mechanism + proof** | `01-dp/dp2-pure-dp.html` | `:172, :275-298` |
| Exponential mechanism + Noisy Max (with proofs) | `01-dp/dp2-pure-dp.html` | `:349-450` |
| Composition + post-processing + group privacy | `01-dp/dp3-properties.html` | `:84-194` |
| **Subsampling amplification proof** | `01-dp/dp3-properties.html` | `:205-273` |
| Why additive DP fails (counterexamples) | `01-dp/dp3-properties.html` | `:296-340` |
| DP $k$-means + privacy proof | `01-dp/dp3-properties.html` | `:354-415` |
| **$(\varepsilon,\delta)$-DP + privacy-loss RV** | `01-dp/dp4-approximate-dp.html` | `:84-128` |
| **Gaussian mechanism + 1-D / multi-D proofs** | `01-dp/dp4-approximate-dp.html` | `:172-244` |
| DP-ERM via exponential mechanism + utility proof | `01-dp/dp5-erm.html` | `:113-160` |
| Advanced composition ($\sqrt k$) | `01-dp/dp5-erm.html` | `:171-201` |
| **DP-SGD algorithm + privacy + utility** | `01-dp/dp5-erm.html` | `:254-315` |
| **Rényi DP definition + Gaussian via RDP proof** | `01-dp/dp6-rdp.html` | `:138-285` |
| Input / Inference / Model DP paradigms | `01-dp/dp7-ml-paradigms.html` | `:78-141` |
| **PATE three-phase architecture** | `01-dp/dp7-ml-paradigms.html` | `:151-220` |
| (ε,δ)-DP definition (capstone restatement) | `01-dp/dp8-fl.html` | `:375-395` |
| Local DP minimax rate | `01-dp/dp8-fl.html` | `:483` |
| PrivUnit mechanism | `01-dp/dp8-fl.html` | `:523` |
| **RRSC + k-closest exact-optimality (NeurIPS 2023)** | `01-dp/dp8-fl.html` | `:571-822` |
| DP-Diffusion / DP-RDM | `01-dp/dp8-fl.html` | `:852-1004` |
| Bayes-route reverse derivation | `02-generative/diffusion1-foundations.html` | `:377-663` |
| Inverse-transform sampling proposition | `02-generative/diffusion1-foundations.html` | `:164` |
| MMSE = conditional mean (+ proof) | `02-generative/diffusion1-foundations.html` | `:620-655` |
| Tweedie's formula (+ proof) | `02-generative/diffusion1-foundations.html` | `:692-753` |
| DDPM VP forward + VLB + ε-loss | `02-generative/diffusion2-ddpm.html` | `:123-915` |
| Fokker–Planck + Anderson reverse SDE | `02-generative/diffusion3-sde-score.html` | `:135-315` |
| Score-matching theorem | `02-generative/diffusion3-sde-score.html` | `:339` |
| DDIM (deterministic, ODE, inversion) | `02-generative/diffusion4-ddim.html` | `:134-281` |
| Classifier-free guidance | `02-generative/diffusion5-guidance-discrete.html` | `:202-282` |
| Discrete diffusion + score-entropy loss | `02-generative/diffusion5-guidance-discrete.html` | `:287-425` |
| LLM overview (tokens, transformer, NLL, post-training, sampling) | `02-generative/llm.html` | `:214, :329, :369` |
| Cross-entropy = entropy + KL; perplexity | `02-generative/llm.html` | `:564, :609, :621` |
| KL-regularized RLHF optimum → DPO (+ NPO preview) | `02-generative/llm.html` | `:822, :929, :951` |
| LLM privacy-hook map (per-token loss / verbatim / sampling / conditional) | `02-generative/llm.html` | `:1101` |
| **Bartz v. Anthropic $1.5B settlement** (Reuters) | `03-memorization/memorization-diffusion.html` | `:162` |
| **Three formal definitions** — extraction / SSCD similarity / Webster taxonomy | `03-memorization/memorization-diffusion.html` | `:269, :426, :518` |
| Diffusion memorization — Carlini 2023 / Somepalli / Webster / Wen / Ross | `03-memorization/memorization-diffusion.html` | `:215-891` |
| **Carlini 2023 — Fig 4 precision + Fig 5 duplicates** | `03-memorization/memorization-diffusion.html` | `:390` |
| **Somepalli 2023 — Fig 5 similarity histograms** | `03-memorization/memorization-diffusion.html` | `:475` |
| **Wen's statistic = implicit classifier gradient** (proposition + proof) | `03-memorization/memorization-diffusion.html` | `:647, :659` |
| **Wen 2024 — Fig 2 magnitude plots** | `03-memorization/memorization-diffusion.html` | `:761` |
| **LID — small-ball definition + Levina–Bickel MLE** | `03-memorization/memorization-diffusion.html` | `:815, :855` |
| **Ross 2024 — LID schematic (Fig 1)** | `03-memorization/memorization-diffusion.html` | `:868` |
| **Theorem — smoothed thin support ($D-k$ eigenvalues at $-\sigma^{-2}$)** | `03-memorization/memorization-diffusion.html` | `:941-1012` |
| **SAIL — sharpness Lemmas 4.1–4.3 + proofs + objective** | `03-memorization/memorization-diffusion.html` | `:892-1421` |
| **SAIL — eigenvalue distribution figure (Fig 3 left)** | `03-memorization/memorization-diffusion.html` | `:1076` |
| **SAIL — Pareto plot (Fig 6 left)** | `03-memorization/memorization-diffusion.html` | `:1398` |
| **CLIP padding-embedding memorization** (Kim & No, CVPR 2026 Findings) | `03-memorization/memorization-diffusion.html` | `:1423-1620` |
| **CLIP-pad attention drop bar chart (Fig 8)** | `03-memorization/memorization-diffusion.html` | `:1558` |
| Secret Sharer canary + exposure null | `03-memorization/memorization-llm.html` | `:105-142` |
| Counterfactual + long-tail (Feldman) | `03-memorization/memorization-llm.html` | `:144` |
| Carlini scaling laws + repetition formal | `03-memorization/memorization-llm.html` | `:204-229` |
| Min-K% / Min-K%++ probes | `03-memorization/memorization-llm.html` | `:259, :274` |
| **Adversarial Compression Ratio (ACR)** | `03-memorization/memorization-llm.html` | `:313-368` |
| Cooper book extraction | `03-memorization/memorization-llm.html` | `:384` |
| Yeom overfitting bound | `04-mia/mia3-theory.html` | `:143` |
| Sablayrolles BB≈WB | `04-mia/mia3-theory.html` | `:436` |
| LiRA | `04-mia/mia4-modern.html` | `:264-503` |
| RMIA | `04-mia/mia4-modern.html` | `:647-720` |
| InfoRMIA (LLM token-level) | `04-mia/mia5-llm.html` | `:427-590` |
| Certified $(\varepsilon,\delta)$ unlearning | `05-unlearning/unlearning1-foundations.html` | `:160` |
| Influence function (leads into Newton) | `05-unlearning/unlearning1-foundations.html` | `:174` |
| Newton-step (8-slide) / Sekhari capacity theorems | `05-unlearning/unlearning1-foundations.html` | `:191-312` |
| MIA optimal test + DP cap + Yeom gap (HW4 woven in) | `05-unlearning/unlearning1-foundations.html` | `:472` |
| SCRUB / SalUn / $\ell_1$-sparse | `05-unlearning/unlearning1-foundations.html` | `:367-431` |
| IDI / COLA (lab) | `05-unlearning/unlearning1-foundations.html` | `:502-533` |
| GA collapse + NPO bounded + SimNPO | `05-unlearning/unlearning2-llm.html` | `:103-165` |
| TOFU / WMDP / RWKU / MUSE benchmarks (main-figure images) | `05-unlearning/unlearning2-llm.html` | `:250-302` |
| Benign + syntactic relearning | `05-unlearning/unlearning2-llm.html` | `:303-328` |
| Kirchenbauer green-list + entropy bound | `06-watermark/watermark.html` | `:164-222` |
| Gumbel-max trick + proof | `06-watermark/watermark.html` | `:252-295` |
| Aaronson distortion-free proof | `06-watermark/watermark.html` | `:325` |
| Edit-distance robustness theorem | `06-watermark/watermark.html` | `:356` |
| Christ–Gunn–Zamir undetectable + construction | `06-watermark/watermark.html` | `:386-419` |
| Adaptive / WaterMax | `06-watermark/watermark.html` | `:486-516` |
| SynthID-Text production | `06-watermark/watermark.html` | `:542` |

## Pairing convention

Decks in the DP, generative (diffusion), and MIA series have `-note.html` companions. The note generally contains full derivations of theorems stated in the deck, pitfalls / comparison tables, and forward/backward references to other lectures. When in doubt: deck = "what is true"; note = "why and how to apply".
