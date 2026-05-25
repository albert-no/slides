# privacy/ — Privacy series

Six sub-tracks: a unified generative-model review (`generative/` — diffusion + LLM) followed by the privacy stack — DP (8-deck lecture series ending in the NeurIPS 2023 DP-FL talk), MIA (5-lecture series with paired notes), plus three single-deck topics (memorization, unlearning, watermarking). Together they form the privacy / copyright / provenance stack.

## Subfolders

- **`generative/`** — Generative-model review. **Diffusion** (5 lectures, from-scratch Bayes-route, SDE, DDIM, guidance, discrete) and **LLM** (1 brief deck: tokens, decoder-only transformer, NLL pretraining, sampling, privacy hooks). Companion notes: `diffusion3-sde-score-note.html` and `note/2_difffusion.tex` (LaTeX). See `generative/OUTLINE.md`.
- **`dp/`** — Differential privacy lecture series (8 decks). `dp1`–`dp7` build foundations: reconstruction attacks → pure DP → properties → approximate DP → DP-SGD → RDP → DP in ML / PATE. `dp8-fl.html` is the capstone applied talk (NeurIPS 2023). Source LaTeX in `tex/dp.tex`. See `dp/OUTLINE.md`.
- **`mia/`** — Membership inference attacks (5 lectures, paired notes). Plus legacy `old/MIA.html`. See `mia/OUTLINE.md`.
- **`memorization/`** — Memorization in generative models. **Two decks (split 2026-05)**: `memorization-diffusion.html` (intro + lawsuits + Bartz/Anthropic, diffusion detection, SAIL, CLIP-pad, LLM bridge) and `memorization-llm.html` (canary→ACR). Captured paper figures in `figs/`. See `memorization/OUTLINE.md`.
- **`unlearning/`** — Machine unlearning (single comprehensive deck). Definitions, classification methods, LLM methods, benchmarks, lab work. Source: `slide.pdf` (the talk Albert gave on this topic). See `unlearning/OUTLINE.md`.
- **`watermark/`** — LLM watermarking (single deck). Green-list, distortion-free, undetectable, robustness, radioactivity. See `watermark/OUTLINE.md`.

## Quick lookup

| Topic | Where | Lines |
|---|---|---|
| Bayes-route reverse derivation | `generative/diffusion1-foundations.html` | `:194-345` |
| Tweedie's formula | `generative/diffusion1-foundations.html` | `:374` |
| DDPM VP forward + VLB + ε-loss | `generative/diffusion2-ddpm.html` | `:90-333` |
| Fokker–Planck + Anderson reverse SDE | `generative/diffusion3-sde-score.html` | `:135-315` |
| Score-matching theorem | `generative/diffusion3-sde-score.html` | `:339` |
| DDIM (deterministic, ODE, inversion) | `generative/diffusion4-ddim.html` | `:134-281` |
| Classifier-free guidance | `generative/diffusion5-guidance-discrete.html` | `:202-282` |
| Discrete diffusion + score-entropy loss | `generative/diffusion5-guidance-discrete.html` | `:287-425` |
| LLM brief overview (tokens, transformer, NLL, sampling) | `generative/llm.html` | `:72-296` |
| LLM privacy-hook map (per-token loss / verbatim / sampling / conditional) | `generative/llm.html` | `:258-281` |
| Reconstruction attack (Dinur–Nissim) | `dp/dp1-reconstruction.html` | `:181-244` |
| Randomized response + sample complexity | `dp/dp2-pure-dp.html` | `:78-148` |
| **$\varepsilon$-DP definition + Laplace mechanism + proof** | `dp/dp2-pure-dp.html` | `:172, :275-298` |
| Exponential mechanism + Noisy Max (with proofs) | `dp/dp2-pure-dp.html` | `:349-450` |
| Composition + post-processing + group privacy | `dp/dp3-properties.html` | `:84-194` |
| **Subsampling amplification proof** | `dp/dp3-properties.html` | `:205-273` |
| Why additive DP fails (counterexamples) | `dp/dp3-properties.html` | `:296-340` |
| DP $k$-means + privacy proof | `dp/dp3-properties.html` | `:354-415` |
| **$(\varepsilon,\delta)$-DP + privacy-loss RV** | `dp/dp4-approximate-dp.html` | `:84-128` |
| **Gaussian mechanism + 1-D / multi-D proofs** | `dp/dp4-approximate-dp.html` | `:172-244` |
| DP-ERM via exponential mechanism + utility proof | `dp/dp5-erm.html` | `:113-160` |
| Advanced composition ($\sqrt k$) | `dp/dp5-erm.html` | `:171-201` |
| **DP-SGD algorithm + privacy + utility** | `dp/dp5-erm.html` | `:254-315` |
| **Rényi DP definition + Gaussian via RDP proof** | `dp/dp6-rdp.html` | `:138-285` |
| Input / Inference / Model DP paradigms | `dp/dp7-ml-paradigms.html` | `:78-141` |
| **PATE three-phase architecture** | `dp/dp7-ml-paradigms.html` | `:151-220` |
| (ε,δ)-DP definition (capstone restatement) | `dp/dp8-fl.html` | `:375-395` |
| Local DP minimax rate | `dp/dp8-fl.html` | `:483` |
| PrivUnit mechanism | `dp/dp8-fl.html` | `:523` |
| **RRSC + k-closest exact-optimality (NeurIPS 2023)** | `dp/dp8-fl.html` | `:571-822` |
| DP-Diffusion / DP-RDM | `dp/dp8-fl.html` | `:852-1004` |
| Yeom overfitting bound | `mia/mia3-theory.html` | `:143` |
| Sablayrolles BB≈WB | `mia/mia3-theory.html` | `:436` |
| LiRA | `mia/mia4-modern.html` | `:264-503` |
| RMIA | `mia/mia4-modern.html` | `:647-720` |
| InfoRMIA (LLM token-level) | `mia/mia5-llm.html` | `:427-590` |
| **Bartz v. Anthropic $1.5B settlement** (Reuters) | `memorization/memorization-diffusion.html` | `:140` |
| Diffusion memorization — Carlini 2023 / Somepalli / Webster / Wen / Ross | `memorization/memorization-diffusion.html` | `:206-365` |
| **Carlini 2023 — Fig 4 precision + Fig 5 duplicates** | `memorization/memorization-diffusion.html` | `:249` |
| **Somepalli 2023 — Fig 5 similarity histograms** | `memorization/memorization-diffusion.html` | `:269` |
| **Wen 2024 — Fig 2 magnitude plots** | `memorization/memorization-diffusion.html` | `:317` |
| **Ross 2024 — LID schematic (Fig 1)** | `memorization/memorization-diffusion.html` | `:345` |
| **SAIL — sharpness Lemmas 4.1–4.3 + objective** | `memorization/memorization-diffusion.html` | `:377-540` |
| **SAIL — eigenvalue distribution figure (Fig 3 left)** | `memorization/memorization-diffusion.html` | `:393` |
| **SAIL — Pareto plot (Fig 6 left)** | `memorization/memorization-diffusion.html` | `:520` |
| **CLIP padding-embedding memorization** (Kim & No, CVPR 2026 Findings) | `memorization/memorization-diffusion.html` | `:543-653` |
| **CLIP-pad attention drop bar chart (Fig 8)** | `memorization/memorization-diffusion.html` | `:594` |
| Secret Sharer canary + exposure null | `memorization/memorization-llm.html` | `:105-142` |
| Counterfactual + long-tail (Feldman) | `memorization/memorization-llm.html` | `:144` |
| Carlini scaling laws + repetition formal | `memorization/memorization-llm.html` | `:204-229` |
| Min-K% / Min-K%++ probes | `memorization/memorization-llm.html` | `:259, :274` |
| **Adversarial Compression Ratio (ACR)** | `memorization/memorization-llm.html` | `:313-368` |
| Cooper book extraction | `memorization/memorization-llm.html` | `:384` |
| Certified $(\varepsilon,\delta)$ unlearning | `unlearning/unlearning.html` | `:175` |
| Newton-step / Sekhari capacity theorems | `unlearning/unlearning.html` | `:189-216` |
| Influence function | `unlearning/unlearning.html` | `:259` |
| SCRUB / SalUn / $\ell_1$-sparse | `unlearning/unlearning.html` | `:276-318` |
| IDI / COLA (lab) | `unlearning/unlearning.html` | `:396-424` |
| GA collapse + NPO bounded + SimNPO | `unlearning/unlearning.html` | `:479-538` |
| TOFU / WMDP / RWKU / MUSE benchmarks | `unlearning/unlearning.html` | `:648-702` |
| Benign + syntactic relearning | `unlearning/unlearning.html` | `:705-728` |
| Pawelczyk verification hardness | `unlearning/unlearning.html` | `:748` |
| Kirchenbauer green-list + entropy bound | `watermark/watermark.html` | `:164-222` |
| Gumbel-max trick + proof | `watermark/watermark.html` | `:252-295` |
| Aaronson distortion-free proof | `watermark/watermark.html` | `:325` |
| Edit-distance robustness theorem | `watermark/watermark.html` | `:356` |
| Christ–Gunn–Zamir undetectable + construction | `watermark/watermark.html` | `:386-419` |
| Adaptive / WaterMax | `watermark/watermark.html` | `:486-516` |
| SynthID-Text production | `watermark/watermark.html` | `:542` |

## Theme connections

- **generative review ↔ everything downstream**: `generative/` is the unified review opener for the privacy series. Diffusion lectures pin down score, sampling, discrete-space generation; `llm.html` pins down $p_\theta(\cdot\mid x_{<t})$, per-token loss $\ell_t$, the sampling step. MIA / memorization / watermarking / unlearning each plug into one of those pieces (LLM 4-card map at `generative/llm.html:258-281`).
- **diffusion ↔ llm (within `generative/`)**: parallel reviews. Diffusion = continuous score-based generation; LLM = discrete autoregressive counterpart. Privacy attacks differ in mechanism but share targets (training-data leakage, provenance, removal).
- **diffusion ↔ MIA**: diffusion-model MIA is a research frontier — `mia/mia4-modern.html:731-789` covers it. The diffusion-models theory in `privacy/generative/` provides the substrate.
- **DP ↔ MIA**: `mia/mia1-foundations.html:601-617` shows DP as MIA bound (`Adv ≤ e^ε−1+δ`); `dp/dp8-fl.html` builds the DP machinery. DP-SGD is referenced from `mia/mia4-modern.html:117`.
- **DP ↔ unlearning**: certified $(\varepsilon,\delta)$-unlearning reuses the DP definition from `dp/dp8-fl.html:375` — same bound, different distribution comparison.
- **memorization ↔ unlearning ↔ MIA**: memorization is the *signal* unlearning aims to remove and MIA aims to detect. `memorization/memorization-diffusion.html` + `memorization-llm.html` motivate the other two; defenses slide flows directly into `unlearning/`. `unlearning/unlearning.html:317` reuses the SALUN MIA-Efficacy column.
- **memorization ↔ watermark**: both about provenance under copyright pressure, but opposite directions — memorization detects unintended retention, watermarking adds intended traceability. Same lawsuits motivate both.
- **dgMARK ↔ watermark**: lab thread for diffusion LLMs — full context in `talks/dllm/dllm.html:524-569`, broader watermark survey here.
- **Theoretical diffusion (`courses/infotheory/diffusion/`) vs from-scratch (`courses/privacy/generative/`)**: same math, different presentation. The infotheory series uses information-theoretic / hierarchical-VAE framing (cleaner for theory students); the privacy series uses the Bayes-+-Taylor route and goes further (5 lectures including SDE, DDIM, CFG, discrete).
