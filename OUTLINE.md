# Talks repo — content outline

Slide decks for Yonsei talks (academic conferences + master-level lectures). Repo conventions in `CLAUDE.md`, design rules in `DESIGN_SYSTEM.md`, pitfalls in `GOTCHAS.md`.

Each topic folder has its own `OUTLINE.md`. Leaf subfolders have detailed per-deck outlines with slide and theorem line numbers. **For specific content, descend into the relevant folder's OUTLINE.md.**

## Folders

- **`icml2026/`** — ICML 2026 5-min SlidesLive recording for the position paper "The Term 'Machine Unlearning' Is Overused in LLMs" (Yoon, Jun, No). 10 slides. Poster ID 67198.
- **`dllm/`** — Diffusion LLMs: invited talk on masked-discrete diffusion (Rainbow Padding, A2D, dgMARK, Reversal Curse, DAPD). 1 deck, no notes.
- **`infotheory/`** — Information-theory lecture series (paired decks + `-note.html` companions):
  - `entropy/` — Foundations: entropy, KL, joint/conditional MI, DPI, Fano (2 lectures)
  - `lossless/` — Codes/Kraft/Huffman, AEP/arithmetic, Markov/LZ (3 lectures)
  - `diffentropy/` — Differential entropy, MaxEnt/Gaussian/EPI, AWGN/water-filling/I-MMSE (3 lectures)
  - `diffusion/` — Diffusion as hierarchical VAE; closes with score-matching equivalence (3 lectures)
  - `lossy/` — Rate–distortion + LLM compression (4 lectures)
  - `mi/` — Variational MI bounds, InfoNCE/CLIP (2 lectures); closes with $f$-divergence unification
  - `divergence/` — $f$-divergence + GAN ($\equiv$ JS), Fisher divergence + score matching ($\equiv$ diffusion) (2 lectures)
- **`privacy/`** — Privacy series:
  - `generative/` — Generative-model review opener: 5 diffusion lectures (Bayes-route, DDPM, SDE, DDIM, guidance + discrete) + 1 brief LLM deck. `note/2_difffusion.tex` is LaTeX source for Diffusion Lectures 1–2
  - `dp/` — Differential privacy + federated learning (1 NeurIPS 2023 talk: RRSC result)
  - `mia/` — Membership inference attacks (5 lectures, paired notes; legacy `old/MIA.html`)
  - `memorization/` — Memorization in generative models (2 decks split 2026-05: `memorization-diffusion.html` covers intro/lawsuits/Bartz, diffusion detection, SAIL, CLIP-pad; `memorization-llm.html` covers canary→ACR). Paper-figure assets in `figs/`
  - `unlearning/` — Machine unlearning (1 deck: definitions, classification, LLM, benchmarks, lab work; sourced from `slide.pdf`)
  - `watermark/` — LLM watermarking (1 deck: green-list, distortion-free, undetectable, robust, radioactivity)

## Quick lookup — where does X live?

| Topic | Location |
|---|---|
| Entropy definition / Gibbs / log-sum | `infotheory/entropy/entropy1-entropy-kl.html:97, :379, :437` |
| Chain rule / DPI / Fano | `infotheory/entropy/entropy2-joint-mi-fano.html:118, :368, :438` |
| Mutual information (discrete) | `infotheory/entropy/entropy2-joint-mi-fano.html:227` |
| Kraft / Kraft–McMillan / Shannon / Huffman | `infotheory/lossless/lossless1-codes.html:157, :198, :268, :413` |
| AEP / source coding theorem / arithmetic coding | `infotheory/lossless/lossless2-aep-arithmetic.html:84, :204, :405` |
| Markov entropy rate / LZ78 | `infotheory/lossless/lossless3-markov-universal.html:188, :355` |
| Differential entropy + bin discretization | `infotheory/diffentropy/diffentropy1-foundations.html:84, :96` |
| Gaussian MaxEnt / Hadamard / EPI | `infotheory/diffentropy/diffentropy2-maxent-gaussian.html:165, :248, :367` |
| Shannon–Hartley / water-filling / I-MMSE | `infotheory/diffentropy/diffentropy3-mi-awgn.html:177, :293, :385` |
| Score function / Tweedie's formula | `privacy/generative/diffusion1-foundations.html:362-425`; theorem at `infotheory/diffusion/diff3-parameterizations.html:121` |
| DDPM forward + VLB derivation | `privacy/generative/diffusion2-ddpm.html:189-333`; `infotheory/diffusion/diff2-diffusion.html:153-212` |
| SDE / Fokker–Planck / Anderson reverse | `privacy/generative/diffusion3-sde-score.html` (FP `:148`, Anderson `:234`, score matching `:339`) |
| DDIM (non-Markovian, deterministic, ODE) | `privacy/generative/diffusion4-ddim.html` (marginal invariance `:164`, predicted clean `:234`) |
| Classifier guidance + CFG | `privacy/generative/diffusion5-guidance-discrete.html:202-282` |
| Discrete diffusion / score-entropy loss | `privacy/generative/diffusion5-guidance-discrete.html:287-425`; `dllm/dllm.html:192-205` (SEDD) |
| LLM brief overview (autoregressive, transformer, NLL, sampling) | `privacy/generative/llm.html:72-296` |
| LLM privacy-hook map (loss / verbatim / sampling / conditional) | `privacy/generative/llm.html:258-281` |
| Rate–distortion theorem (Shannon) | `infotheory/lossy/lossy1-foundations.html:258-311` |
| Lloyd–Max / scalar quantization | `infotheory/lossy/lossy1-foundations.html:143-199` |
| Gaussian R(D), Shannon lower bound, pruning | `infotheory/lossy/lossy2-gaussian-laplacian.html:63-232` |
| Lattice / E8 / QUIP# | `infotheory/lossy/lossy3-lattice-quip.html` |
| TURBOQUANT (online VQ for KV cache) | `infotheory/lossy/lossy4-turboquant.html` |
| Variational MI lower bounds (BA, DV, NWJ, MINE) | `infotheory/mi/mi1-bounds.html` |
| $f$-divergence unification of MI bounds | `infotheory/mi/mi1-bounds.html:261-280` |
| InfoNCE / CLIP | `infotheory/mi/mi2-infonce-clip.html` |
| $f$-divergence definition + properties (DPI, info inequality) | `infotheory/divergence/div1-fdivergence-gan.html:121, :229` |
| GAN $\equiv$ Jensen–Shannon minimization (theorem + proof) | `infotheory/divergence/div1-fdivergence-gan.html:330, :341-350` |
| Hockey-stick divergence (DP connection) | `infotheory/divergence/div1-fdivergence-gan.html:166` |
| Fisher divergence + score function | `infotheory/divergence/div2-fisher-score.html:91, :141` |
| Denoising score matching theorem (Vincent 2011) | `infotheory/divergence/div2-fisher-score.html:200, :211-235` |
| Diffusion ELBO $\equiv$ DSM theorem | `infotheory/divergence/div2-fisher-score.html:315`; cross-ref `infotheory/diffusion/diff3-parameterizations.html:211` |
| MIA foundations (Homer, evaluation metrics) | `privacy/mia/mia1-foundations.html` |
| Shadow models (Shokri / LOGAN / seq2seq) | `privacy/mia/mia2-shadow.html` |
| MIA theory (Yeom / Sablayrolles / ML-Leaks / Nasr) | `privacy/mia/mia3-theory.html` |
| LiRA, RMIA, label-only, attack hierarchy | `privacy/mia/mia4-modern.html` |
| LLM MIA (perplexity, neighbourhood, SPV, InfoRMIA) | `privacy/mia/mia5-llm.html` |
| Bartz v. Anthropic $1.5B settlement (Reuters cite) | `privacy/memorization/memorization-diffusion.html:140` |
| Diffusion memorization — Carlini/Somepalli/Webster/Wen/Ross | `privacy/memorization/memorization-diffusion.html:206-365` |
| SAIL — Lemmas 4.1–4.3 + eigenvalue figure + objective | `privacy/memorization/memorization-diffusion.html:377-540` |
| CLIP padding-embedding memorization (Kim & No 2026) | `privacy/memorization/memorization-diffusion.html:542-631` |
| Memorization — canary entropy, exposure, $k$-extractable | `privacy/memorization/memorization-llm.html:105-142` |
| Counterfactual memorization + long-tail theorem (Feldman) | `privacy/memorization/memorization-llm.html:144` |
| Repetition scaling formal law | `privacy/memorization/memorization-llm.html:222` |
| Min-K%++ probe | `privacy/memorization/memorization-llm.html:274` |
| ACR (Schwarzschild 2024) + MiniPrompt | `privacy/memorization/memorization-llm.html:313-354` |
| Cooper book extraction (open-weight LLMs) | `privacy/memorization/memorization-llm.html:384` |
| Certified $(\varepsilon,\delta)$-unlearning | `privacy/unlearning/unlearning.html:175` |
| Newton-step + Sekhari capacity theorems | `privacy/unlearning/unlearning.html:189-216` |
| Influence function (IU) | `privacy/unlearning/unlearning.html:259` |
| SCRUB / SalUn / $\ell_1$-sparse classification unlearn | `privacy/unlearning/unlearning.html:276-318` |
| IDI / COLA (lab unlearning eval) | `privacy/unlearning/unlearning.html:396-424` |
| GA collapse + NPO bounded + SimNPO | `privacy/unlearning/unlearning.html:479-538` |
| ME+GD / IDK / LUNAR (LLM unlearn) | `privacy/unlearning/unlearning.html:542-639` |
| TOFU / WMDP / RWKU / MUSE benchmarks | `privacy/unlearning/unlearning.html:648-702` |
| Benign + syntactic relearning (lab) | `privacy/unlearning/unlearning.html:705-728` |
| Pawelczyk black-box verification hardness | `privacy/unlearning/unlearning.html:748` |
| Position: "Unlearning" overused in LLMs (5-min ICML talk) | `icml2026/icml2026.html` |
| Kirchenbauer green-list + z-test + entropy bound | `privacy/watermark/watermark.html:164-222` |
| Gumbel distribution + Gumbel-max trick + proof | `privacy/watermark/watermark.html:252-295` |
| Aaronson distortion-free + proof | `privacy/watermark/watermark.html:309-337` |
| Kuditipudi edit-distance robustness theorem | `privacy/watermark/watermark.html:356` |
| Christ–Gunn–Zamir undetectable + PRF construction | `privacy/watermark/watermark.html:386-419` |
| Adaptive watermark + WaterMax | `privacy/watermark/watermark.html:486-516` |
| SynthID-Text production watermark | `privacy/watermark/watermark.html:542` |
| **DP foundations series (dp1–dp7)** | `privacy/dp/dp1`…`dp7-ml-paradigms.html` |
| DP definition / LDP vs central / PrivUnit | `privacy/dp/dp8-fl.html:364-569` |
| RRSC + k-closest exact-optimality (NeurIPS 2023) | `privacy/dp/dp8-fl.html:571-822` |
| DP-SGD / DP-Diffusion / DP-RDM | `privacy/dp/dp8-fl.html:827-1004` |
| Continuous SDE diffusion at a glance (Song et al.) | `dllm/dllm.html:99` |
| Masked diffusion at a glance | `dllm/dllm.html:115` |
| Reverse process needs a ratio (concrete score) | `dllm/dllm.html:179` |
| Rainbow Padding (EOS overflow, ICLR 2026) | `dllm/dllm.html:319-461` |
| DAPD (attention dependency graph, ICML 2026) | `dllm/dllm.html:463-669` |
| Diffusion-LLM safety (A2D) | `dllm/dllm.html:694` |
| dgMARK (diffusion-LLM watermarking, ICML 2026) | `dllm/dllm.html:707` |
| Reversal curse in MDMs | `dllm/dllm.html:720` |

## Cross-references

Same topic, different decks (use the more recent / more detailed):
- **VAE / ELBO**: rigorous derivation `infotheory/diffusion/diff1-vae-elbo.html`
- **Hierarchical-VAE view of diffusion**: `infotheory/diffusion/diff2-diffusion.html` (information-theoretic, Markov rewrite)
- **Diffusion from-scratch (Bayes route)**: `privacy/generative/diffusion1-foundations.html` (Taylor + complete-square proof, less abstract)
- **Tweedie**: brief `privacy/generative/diffusion1-foundations.html:374`; with proof `infotheory/diffusion/diff3-parameterizations.html:135`
- **$f$-divergence variational dual**: brief in `infotheory/mi/mi1-bounds.html:261` (KL instances); full development in `infotheory/divergence/div1-fdivergence-gan.html:121-300`
- **Score matching $\equiv$ diffusion training**: brief cross-ref `infotheory/diffusion/diff3-parameterizations.html:211`; full proof `infotheory/divergence/div2-fisher-score.html:200-326`

## Companion notes pattern

`<deck>.html` is the deck. `<deck>-note.html` (where present) holds:
- Long-form proofs (theorem cited on slide → full derivation in notes)
- Intuition that doesn't fit on a slide
- Edge cases, comparison tables, references
- Look in the `-note.html` for "why does this hold" / "what's the precise statement" detail.

`infotheory/` has notes for every deck. `privacy/mia/` has notes for every deck. `privacy/generative/` has notes for every diffusion lecture (1–5); `llm.html` has no note. `dllm/` and `privacy/dp/` do **not** have companion notes — proof detail is in-deck or in `note/2_difffusion.tex` (under `privacy/generative/`).

## Authoring conventions

- Decks live at `<topic>/<deck>.html`.
- Reference assets in `reference/`: paths from depth-1 decks (`infotheory/foo.html`) use `../reference/`; depth-2 decks (`privacy/mia/foo.html`) use `../../reference/`.
- Build: `python3 scripts/bundle.py <path>/<deck>.html` → `<deck>.standalone.html` (gitignored).
- Lint: `python3 scripts/lint-deck.py --all`.
