# Talks repo — content outline

Slide decks for Yonsei talks (academic conferences + master-level lectures). Repo conventions in `CLAUDE.md`, design rules in `DESIGN_SYSTEM.md`, pitfalls in `GOTCHAS.md`.

Each topic folder has its own `OUTLINE.md`. Leaf subfolders have detailed per-deck outlines with slide and theorem line numbers. **For specific content, descend into the relevant folder's OUTLINE.md.**

## Folders

### `courses/` — semester-long lecture series

- **`courses/infotheory/`** — Information-theory lecture series (paired decks + `-note.html` companions):
  - `entropy/` — Foundations: entropy, KL, joint/conditional MI, DPI, Fano (2 lectures)
  - `lossless/` — Codes/Kraft/Huffman, AEP/arithmetic, Markov/LZ (3 lectures)
  - `diffentropy/` — Differential entropy, MaxEnt/Gaussian/EPI, AWGN/water-filling/I-MMSE (3 lectures)
  - `diffusion/` — Diffusion as hierarchical VAE; closes with score-matching equivalence (3 lectures)
  - `lossy/` — Rate–distortion + LLM compression (4 lectures)
  - `mi/` — Variational MI bounds, InfoNCE/CLIP (2 lectures); closes with $f$-divergence unification
  - `divergence/` — $f$-divergence + GAN ($\equiv$ JS), Fisher divergence + score matching ($\equiv$ diffusion) (2 lectures)
- **`courses/privacy/`** — Privacy series:
  - `generative/` — Generative-model review opener: 5 diffusion lectures (Bayes-route, DDPM, SDE, DDIM, guidance + discrete) + 1 brief LLM deck. `note/2_difffusion.tex` is LaTeX source for Diffusion Lectures 1–2
  - `dp/` — Differential privacy + federated learning (1 NeurIPS 2023 talk: RRSC result)
  - `mia/` — Membership inference attacks (5 lectures, paired notes; legacy `old/MIA.html`)
  - `memorization/` — Memorization in generative models (2 decks split 2026-05: `memorization-diffusion.html` covers intro/lawsuits/Bartz, diffusion detection, SAIL, CLIP-pad; `memorization-llm.html` covers canary→ACR). Paper-figure assets in `figs/`
  - `unlearning/` — Machine unlearning (1 deck: definitions, classification, LLM, benchmarks, lab work; sourced from `slide.pdf`)
  - `watermark/` — LLM watermarking (1 deck: green-list, distortion-free, undetectable, robust, radioactivity)

### `talks/` — standalone research presentations

- **`talks/icml2026/`** — ICML 2026 5-min SlidesLive recording for the position paper "The Term 'Machine Unlearning' Is Overused in LLMs" (Yoon, Jun, No). 10 slides. Poster ID 67198.
- **`talks/dllm/`** — Diffusion LLMs: invited talk on masked-discrete diffusion (Rainbow Padding, A2D, dgMARK, Reversal Curse, DAPD). 1 deck, no notes.
- **`talks/seoul/`** — Seoul AI governance talk.

## Quick lookup — where does X live?

| Topic | Location |
|---|---|
| Entropy definition / Gibbs / log-sum | `courses/infotheory/entropy/entropy1-entropy-kl.html:97, :379, :437` |
| Chain rule / DPI / Fano | `courses/infotheory/entropy/entropy2-joint-mi-fano.html:118, :368, :438` |
| Mutual information (discrete) | `courses/infotheory/entropy/entropy2-joint-mi-fano.html:227` |
| Kraft / Kraft–McMillan / Shannon / Huffman | `courses/infotheory/lossless/lossless1-codes.html:157, :198, :268, :413` |
| AEP / source coding theorem / arithmetic coding | `courses/infotheory/lossless/lossless2-aep-arithmetic.html:84, :204, :405` |
| Markov entropy rate / LZ78 | `courses/infotheory/lossless/lossless3-markov-universal.html:188, :355` |
| Differential entropy + bin discretization | `courses/infotheory/diffentropy/diffentropy1-foundations.html:84, :96` |
| Gaussian MaxEnt / Hadamard / EPI | `courses/infotheory/diffentropy/diffentropy2-maxent-gaussian.html:165, :248, :367` |
| Shannon–Hartley / water-filling / I-MMSE | `courses/infotheory/diffentropy/diffentropy3-mi-awgn.html:177, :293, :385` |
| Score function / Tweedie's formula | `courses/privacy/generative/diffusion1-foundations.html:362-425`; theorem at `courses/infotheory/diffusion/diff3-parameterizations.html:121` |
| DDPM forward + VLB derivation | `courses/privacy/generative/diffusion2-ddpm.html:189-333`; `courses/infotheory/diffusion/diff2-diffusion.html:153-212` |
| SDE / Fokker–Planck / Anderson reverse | `courses/privacy/generative/diffusion3-sde-score.html` (FP `:148`, Anderson `:234`, score matching `:339`) |
| DDIM (non-Markovian, deterministic, ODE) | `courses/privacy/generative/diffusion4-ddim.html` (marginal invariance `:164`, predicted clean `:234`) |
| Classifier guidance + CFG | `courses/privacy/generative/diffusion5-guidance-discrete.html:202-282` |
| Discrete diffusion / score-entropy loss | `courses/privacy/generative/diffusion5-guidance-discrete.html:287-425`; `talks/dllm/dllm.html:192-205` (SEDD) |
| LLM brief overview (autoregressive, transformer, NLL, sampling) | `courses/privacy/generative/llm.html:72-296` |
| LLM privacy-hook map (loss / verbatim / sampling / conditional) | `courses/privacy/generative/llm.html:258-281` |
| Rate–distortion theorem (Shannon) | `courses/infotheory/lossy/lossy1-foundations.html:258-311` |
| Lloyd–Max / scalar quantization | `courses/infotheory/lossy/lossy1-foundations.html:143-199` |
| Gaussian R(D), Shannon lower bound, pruning | `courses/infotheory/lossy/lossy2-gaussian-laplacian.html:63-232` |
| Lattice / E8 / QUIP# | `courses/infotheory/lossy/lossy3-lattice-quip.html` |
| TURBOQUANT (online VQ for KV cache) | `courses/infotheory/lossy/lossy4-turboquant.html` |
| Variational MI lower bounds (BA, DV, NWJ, MINE) | `courses/infotheory/mi/mi1-bounds.html` |
| $f$-divergence unification of MI bounds | `courses/infotheory/mi/mi1-bounds.html:261-280` |
| InfoNCE / CLIP | `courses/infotheory/mi/mi2-infonce-clip.html` |
| $f$-divergence definition + properties (DPI, info inequality) | `courses/infotheory/divergence/div1-fdivergence-gan.html:121, :229` |
| GAN $\equiv$ Jensen–Shannon minimization (theorem + proof) | `courses/infotheory/divergence/div1-fdivergence-gan.html:330, :341-350` |
| Hockey-stick divergence (DP connection) | `courses/infotheory/divergence/div1-fdivergence-gan.html:166` |
| Fisher divergence + score function | `courses/infotheory/divergence/div2-fisher-score.html:91, :141` |
| Denoising score matching theorem (Vincent 2011) | `courses/infotheory/divergence/div2-fisher-score.html:200, :211-235` |
| Diffusion ELBO $\equiv$ DSM theorem | `courses/infotheory/divergence/div2-fisher-score.html:315`; cross-ref `courses/infotheory/diffusion/diff3-parameterizations.html:211` |
| MIA foundations (Homer, evaluation metrics) | `courses/privacy/mia/mia1-foundations.html` |
| Shadow models (Shokri / LOGAN / seq2seq) | `courses/privacy/mia/mia2-shadow.html` |
| MIA theory (Yeom / Sablayrolles / ML-Leaks / Nasr) | `courses/privacy/mia/mia3-theory.html` |
| LiRA, RMIA, label-only, attack hierarchy | `courses/privacy/mia/mia4-modern.html` |
| LLM MIA (perplexity, neighbourhood, SPV, InfoRMIA) | `courses/privacy/mia/mia5-llm.html` |
| Bartz v. Anthropic $1.5B settlement (Reuters cite) | `courses/privacy/memorization/memorization-diffusion.html:140` |
| Diffusion memorization — Carlini/Somepalli/Webster/Wen/Ross | `courses/privacy/memorization/memorization-diffusion.html:206-365` |
| SAIL — Lemmas 4.1–4.3 + eigenvalue figure + objective | `courses/privacy/memorization/memorization-diffusion.html:377-540` |
| CLIP padding-embedding memorization (Kim & No 2026) | `courses/privacy/memorization/memorization-diffusion.html:542-631` |
| Memorization — canary entropy, exposure, $k$-extractable | `courses/privacy/memorization/memorization-llm.html:105-142` |
| Counterfactual memorization + long-tail theorem (Feldman) | `courses/privacy/memorization/memorization-llm.html:144` |
| Repetition scaling formal law | `courses/privacy/memorization/memorization-llm.html:222` |
| Min-K%++ probe | `courses/privacy/memorization/memorization-llm.html:274` |
| ACR (Schwarzschild 2024) + MiniPrompt | `courses/privacy/memorization/memorization-llm.html:313-354` |
| Cooper book extraction (open-weight LLMs) | `courses/privacy/memorization/memorization-llm.html:384` |
| Certified $(\varepsilon,\delta)$-unlearning | `courses/privacy/unlearning/unlearning.html:175` |
| Newton-step + Sekhari capacity theorems | `courses/privacy/unlearning/unlearning.html:189-216` |
| Influence function (IU) | `courses/privacy/unlearning/unlearning.html:259` |
| SCRUB / SalUn / $\ell_1$-sparse classification unlearn | `courses/privacy/unlearning/unlearning.html:276-318` |
| IDI / COLA (lab unlearning eval) | `courses/privacy/unlearning/unlearning.html:396-424` |
| GA collapse + NPO bounded + SimNPO | `courses/privacy/unlearning/unlearning.html:479-538` |
| ME+GD / IDK / LUNAR (LLM unlearn) | `courses/privacy/unlearning/unlearning.html:542-639` |
| TOFU / WMDP / RWKU / MUSE benchmarks | `courses/privacy/unlearning/unlearning.html:648-702` |
| Benign + syntactic relearning (lab) | `courses/privacy/unlearning/unlearning.html:705-728` |
| Pawelczyk black-box verification hardness | `courses/privacy/unlearning/unlearning.html:748` |
| Position: "Unlearning" overused in LLMs (5-min ICML talk) | `talks/icml2026/icml2026.html` |
| Kirchenbauer green-list + z-test + entropy bound | `courses/privacy/watermark/watermark.html:164-222` |
| Gumbel distribution + Gumbel-max trick + proof | `courses/privacy/watermark/watermark.html:252-295` |
| Aaronson distortion-free + proof | `courses/privacy/watermark/watermark.html:309-337` |
| Kuditipudi edit-distance robustness theorem | `courses/privacy/watermark/watermark.html:356` |
| Christ–Gunn–Zamir undetectable + PRF construction | `courses/privacy/watermark/watermark.html:386-419` |
| Adaptive watermark + WaterMax | `courses/privacy/watermark/watermark.html:486-516` |
| SynthID-Text production watermark | `courses/privacy/watermark/watermark.html:542` |
| **DP foundations series (dp1–dp7)** | `courses/privacy/dp/dp1`…`dp7-ml-paradigms.html` |
| DP definition / LDP vs central / PrivUnit | `courses/privacy/dp/dp8-fl.html:364-569` |
| RRSC + k-closest exact-optimality (NeurIPS 2023) | `courses/privacy/dp/dp8-fl.html:571-822` |
| DP-SGD / DP-Diffusion / DP-RDM | `courses/privacy/dp/dp8-fl.html:827-1004` |
| Continuous SDE diffusion at a glance (Song et al.) | `talks/dllm/dllm.html:99` |
| Masked diffusion at a glance | `talks/dllm/dllm.html:115` |
| Reverse process needs a ratio (concrete score) | `talks/dllm/dllm.html:179` |
| Rainbow Padding (EOS overflow, ICLR 2026) | `talks/dllm/dllm.html:319-461` |
| DAPD (attention dependency graph, ICML 2026) | `talks/dllm/dllm.html:463-669` |
| Diffusion-LLM safety (A2D) | `talks/dllm/dllm.html:694` |
| dgMARK (diffusion-LLM watermarking, ICML 2026) | `talks/dllm/dllm.html:707` |
| Reversal curse in MDMs | `talks/dllm/dllm.html:720` |

## Cross-references

Same topic, different decks (use the more recent / more detailed):
- **VAE / ELBO**: rigorous derivation `courses/infotheory/diffusion/diff1-vae-elbo.html`
- **Hierarchical-VAE view of diffusion**: `courses/infotheory/diffusion/diff2-diffusion.html` (information-theoretic, Markov rewrite)
- **Diffusion from-scratch (Bayes route)**: `courses/privacy/generative/diffusion1-foundations.html` (Taylor + complete-square proof, less abstract)
- **Tweedie**: brief `courses/privacy/generative/diffusion1-foundations.html:374`; with proof `courses/infotheory/diffusion/diff3-parameterizations.html:135`
- **$f$-divergence variational dual**: brief in `courses/infotheory/mi/mi1-bounds.html:261` (KL instances); full development in `courses/infotheory/divergence/div1-fdivergence-gan.html:121-300`
- **Score matching $\equiv$ diffusion training**: brief cross-ref `courses/infotheory/diffusion/diff3-parameterizations.html:211`; full proof `courses/infotheory/divergence/div2-fisher-score.html:200-326`

## Companion notes pattern

`<deck>.html` is the deck. `<deck>-note.html` (where present) holds:
- Long-form proofs (theorem cited on slide → full derivation in notes)
- Intuition that doesn't fit on a slide
- Edge cases, comparison tables, references
- Look in the `-note.html` for "why does this hold" / "what's the precise statement" detail.

`courses/infotheory/` has notes for every deck. `courses/privacy/mia/` has notes for every deck. `courses/privacy/generative/` has notes for every diffusion lecture (1–5); `llm.html` has no note. `talks/dllm/` and `courses/privacy/dp/` do **not** have companion notes — proof detail is in-deck or in `note/2_difffusion.tex` (under `courses/privacy/generative/`).

## Authoring conventions

- Course decks live at `courses/<course>/<topic>/<deck>.html` — reference path `../../../reference/`.
- Research talks live at `talks/<name>/<deck>.html` — reference path `../../reference/`.
- Build: `python3 scripts/bundle.py <path>/<deck>.html` → `<deck>.standalone.html` (gitignored).
- Lint: `python3 scripts/lint-deck.py --all`.
