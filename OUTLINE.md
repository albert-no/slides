# Talks repo — content outline

Slide decks for Yonsei talks (academic conferences + master-level lectures). Repo conventions in `CLAUDE.md`, design rules in `DESIGN_SYSTEM.md`, pitfalls in `GOTCHAS.md`.

Each topic folder has its own `OUTLINE.md`. Leaf subfolders have detailed per-deck outlines with slide and theorem line numbers. **For specific content, descend into the relevant folder's OUTLINE.md.**

## Folders

### `courses/` — semester-long lecture series

- **`courses/infotheory/`** — Information-theory course. Four artifact types: `lectures/` (slides), `notes/` (LaTeX notes), `exam/`, and `overleaf/` (frozen archive). See `courses/infotheory/OUTLINE.md`.
  - `lectures/` — slide series, 8 numbered topic folders (paired decks + `-note.html`):
    - `01-entropy/` — Foundations: entropy, KL, joint/conditional MI, DPI, Fano (2 lectures)
    - `02-lossless/` — Codes/Kraft/Huffman, AEP/arithmetic, Markov/LZ (3 lectures)
    - `03-diffentropy/` — Differential entropy, MaxEnt/Gaussian/EPI, AWGN/water-filling/I-MMSE (3 lectures)
    - `04-lossy/` — Rate–distortion + LLM compression (4 lectures)
    - `05-mi/` — Variational MI bounds, InfoNCE/CLIP (2 lectures); closes with $f$-divergence unification
    - `06-divergence/` — $f$-divergence + GAN ($\equiv$ JS), Fisher divergence + score matching ($\equiv$ diffusion) (2 lectures)
    - `07-diffusion/` — Diffusion as hierarchical VAE; closes with score-matching equivalence (3 lectures)
    - `08-ib/` — Information Bottleneck: IB Lagrangian, VIB, information plane (2 lectures)
  - `notes/` — canonical LaTeX notes (2026); `exam/` — finals 2024–26; `overleaf/` — frozen legacy source
- **`courses/privacy/`** — Privacy series. Three artifact types: `lectures/` (slides, 6 numbered topic folders), `exam/` (homework/midterm/final set), and `overleaf/` (frozen legacy source). See `courses/privacy/OUTLINE.md`.
  - `lectures/01-dp/` — Differential privacy: 8 decks, `dp1`–`dp7` foundations + `dp8-fl.html` capstone (NeurIPS 2023: RRSC result). LaTeX source in `tex/dp.tex`
  - `lectures/02-generative/` — Generative-model review: 5 diffusion lectures (Bayes-route, DDPM, SDE, DDIM, guidance + discrete) + 1 brief LLM deck. `note/2_difffusion.tex` is LaTeX source for Diffusion Lectures 1–2
  - `lectures/03-memorization/` — Memorization in generative models (2 decks split 2026-05: `memorization-diffusion.html` covers intro/lawsuits/Bartz, diffusion detection, SAIL, CLIP-pad; `memorization-llm.html` covers canary→ACR). Paper-figure assets in `figs/`
  - `lectures/04-mia/` — Membership inference attacks (5 lectures, paired notes; legacy `old/MIA.html`)
  - `lectures/05-unlearning/` — Machine unlearning (definitions, classification, LLM, benchmarks, lab work; sourced from `slide.pdf`)
  - `lectures/06-watermark/` — LLM watermarking (1 deck: green-list, distortion-free, undetectable, robust, radioactivity)
  - `exam/` — homework (HW1–4), midterms 2025–26, finals 2024–25 + 2026/27 drafts (`.tex`/`.pdf`/`.html`, shared style files)
  - `overleaf/` — frozen Overleaf archive: lecture-note `.tex` (`1_dp`/`2_difffusion`/`3_watermark`/`4_MIA`), `hw_exam/` (all HW + exams), `images/`, `old/` drafts, `.bib`/style files
- **`courses/trustworthy-ai/`** — Trustworthy AI course (**junior/senior undergrad**, mixed majors, 15 weeks × 1.5 hr). Concept-first: each lecture is motivation → foundational works → 2025–26 frontier, ≤1 intuitive formula per concept, no proofs, plus an optional Colab demo. Decks live flat (`lecNN-*.html`). Five modules: Foundations (Wk 1) · Privacy & Data (2–5) · Reliability (6–7) · Security (8–11) · Provenance & Fairness (12–14) · Synthesis (15). **All 15 lectures + 4 backups + 15 technical supplements (`lecNNtech.html`) — screenshot-audited, real cited paper figures embedded, lint-clean** (no figure-TODO markers remain). Each lecture has a `-note.html` speaker script; each has an optional `lecNNtech.html` holding the formal math the main deck keeps as a picture. Backups: sycophancy, copyright, agentic autonomy, model stealing. The light undergrad pass over topics treated rigorously in `courses/privacy/`. See `courses/trustworthy-ai/OUTLINE.md`.

### `talks/` — standalone research presentations

- **`talks/icml2026/`** — ICML 2026 5-min SlidesLive recording for the position paper "The Term 'Machine Unlearning' Is Overused in LLMs" (Yoon, Jun, No). 10 slides. Poster ID 67198.
- **`talks/kics260521dllm/`** — Diffusion LLMs (KICS, 2026-05-21): general-audience invited talk on masked-discrete diffusion (Rainbow Padding, A2D, dgMARK, Reversal Curse, DAPD). 1 deck, no notes.
- **`talks/math260624dllm/`** — Diffusion LLMs (math conference, June 2026): mathematician-facing variant of the KICS talk — more Gaussian SDE theory, deeper SEDD/RADD, formal DAPD problem, lab work compressed; adds Mercury/DiffusionGemma "in practice" slide. 1 deck, no notes.
- **`talks/postech260819/`** — POSTECH Ok-lab seminar (2026-08-19, 50 min, graduate AI audience): "Small Interventions, Large Effects" — REFT first-token diversification, SafePath 8-token safety primer, few-shot Benign DPO attack (GPT fine-tuning-service framing + TenBenign prior art), 3-slide unlearning-position close; high-level connections to SEAG/LSC/FedVPA-GP; lab-author photos on section dividers; 3 lab-publication slides (papers in the talk + other records since 2025: unlearning/safety, discrete diffusion) before the closer. 42 slides (incl. 4 NeurIPS-2026 rebuttal slides for REFT and Benign DPO), figures captured from papers, no notes.
- **`talks/seoul/`** — Seoul AI governance talk.

## Quick lookup — where does X live?

| Topic | Location |
|---|---|
| Entropy definition / Gibbs / log-sum | `courses/infotheory/lectures/01-entropy/entropy1-entropy-kl.html:131, :507, :582` |
| Chain rule / DPI / Fano | `courses/infotheory/lectures/01-entropy/entropy2-joint-mi-fano.html:111, :426, :518` |
| Mutual information (discrete) | `courses/infotheory/lectures/01-entropy/entropy2-joint-mi-fano.html:240` |
| Kraft / Kraft–McMillan / Shannon / Huffman | `courses/infotheory/lectures/02-lossless/lossless1-codes.html:213, :252, :293, :493` |
| AEP / source coding theorem / arithmetic coding | `courses/infotheory/lectures/02-lossless/lossless2-aep-arithmetic.html:98, :205, :413` |
| Markov entropy rate / LZ78 | `courses/infotheory/lectures/02-lossless/lossless3-markov-universal.html:156, :283` |
| Differential entropy + bin discretization | `courses/infotheory/lectures/03-diffentropy/diffentropy1-foundations.html:106, :117` |
| Gaussian MaxEnt / Hadamard / EPI | `courses/infotheory/lectures/03-diffentropy/diffentropy2-maxent-gaussian.html:143, :221, :332` |
| Shannon–Hartley / water-filling / I-MMSE | `courses/infotheory/lectures/03-diffentropy/diffentropy3-mi-awgn.html:161, :291, :389` |
| Score function / Tweedie's formula | `courses/privacy/lectures/02-generative/diffusion1-foundations.html:679, :695` (theorem + 3-slide proof); theorem at `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:121` |
| DDPM forward + VLB derivation | `courses/privacy/lectures/02-generative/diffusion2-ddpm.html:187-708`; `courses/infotheory/lectures/07-diffusion/diff2-diffusion.html:153-212` |
| SDE / Fokker–Planck / Anderson reverse | `courses/privacy/lectures/02-generative/diffusion3-sde-score.html` (FP `:148`, Anderson `:234`, score matching `:339`) |
| DDIM (non-Markovian, deterministic, ODE) | `courses/privacy/lectures/02-generative/diffusion4-ddim.html` (marginal invariance `:164`, predicted clean `:234`) |
| Classifier guidance + CFG | `courses/privacy/lectures/02-generative/diffusion5-guidance-discrete.html:202-282` |
| Discrete diffusion / score-entropy loss | `courses/privacy/lectures/02-generative/diffusion5-guidance-discrete.html:287-425`; `talks/kics260521dllm/kics260521dllm.html:192-205` (SEDD) |
| LLM brief overview (autoregressive, transformer, NLL, sampling) | `courses/privacy/lectures/02-generative/llm.html:72-296` |
| LLM privacy-hook map (loss / verbatim / sampling / conditional) | `courses/privacy/lectures/02-generative/llm.html:258-281` |
| Rate–distortion theorem (Shannon) | `courses/infotheory/lectures/04-lossy/lossy1-foundations.html:258-311` |
| Lloyd–Max / scalar quantization | `courses/infotheory/lectures/04-lossy/lossy1-foundations.html:143-199` |
| Gaussian R(D), Shannon lower bound, pruning | `courses/infotheory/lectures/04-lossy/lossy2-gaussian-laplacian.html:63-232` |
| Lattice / E8 / QUIP# | `courses/infotheory/lectures/04-lossy/lossy3-lattice-quip.html` |
| TURBOQUANT (online VQ for KV cache) | `courses/infotheory/lectures/04-lossy/lossy4-turboquant.html` |
| Variational MI lower bounds (BA, DV, NWJ, MINE) | `courses/infotheory/lectures/05-mi/mi1-bounds.html` |
| $f$-divergence unification of MI bounds | `courses/infotheory/lectures/05-mi/mi1-bounds.html:261-280` |
| InfoNCE / CLIP | `courses/infotheory/lectures/05-mi/mi2-infonce-clip.html` |
| $f$-divergence definition + properties (DPI, info inequality) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:121, :229` |
| GAN $\equiv$ Jensen–Shannon minimization (theorem + proof) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:330, :341-350` |
| Hockey-stick divergence (DP connection) | `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:166` |
| Fisher divergence + score function | `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:91, :141` |
| Denoising score matching theorem (Vincent 2011) | `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193, :220-253` |
| Diffusion ELBO $\equiv$ DSM theorem | `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:198` (capstone); cites Vincent from `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193` |
| MIA foundations (Homer, evaluation metrics) | `courses/privacy/lectures/04-mia/mia1-foundations.html` |
| Shadow models (Shokri / LOGAN / seq2seq) | `courses/privacy/lectures/04-mia/mia2-shadow.html` |
| MIA theory (Yeom / Sablayrolles / ML-Leaks / Nasr) | `courses/privacy/lectures/04-mia/mia3-theory.html` |
| LiRA, RMIA, label-only, attack hierarchy | `courses/privacy/lectures/04-mia/mia4-modern.html` |
| LLM MIA (perplexity, neighbourhood, SPV, InfoRMIA) | `courses/privacy/lectures/04-mia/mia5-llm.html` |
| Bartz v. Anthropic $1.5B settlement (Reuters cite) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:140` |
| Diffusion memorization — Carlini/Somepalli/Webster/Wen/Ross | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:206-365` |
| SAIL — Lemmas 4.1–4.3 + eigenvalue figure + objective | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:377-540` |
| CLIP padding-embedding memorization (Kim & No 2026) | `courses/privacy/lectures/03-memorization/memorization-diffusion.html:542-631` |
| Memorization — canary entropy, exposure, $k$-extractable | `courses/privacy/lectures/03-memorization/memorization-llm.html:105-142` |
| Counterfactual memorization + long-tail theorem (Feldman) | `courses/privacy/lectures/03-memorization/memorization-llm.html:144` |
| Repetition scaling formal law | `courses/privacy/lectures/03-memorization/memorization-llm.html:222` |
| Min-K%++ probe | `courses/privacy/lectures/03-memorization/memorization-llm.html:274` |
| ACR (Schwarzschild 2024) + MiniPrompt | `courses/privacy/lectures/03-memorization/memorization-llm.html:313-354` |
| Cooper book extraction (open-weight LLMs) | `courses/privacy/lectures/03-memorization/memorization-llm.html:384` |
| Certified $(\varepsilon,\delta)$-unlearning | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:160` |
| Influence function (IU) — leads into the Newton block | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:174` |
| Newton-step (8-slide derivation) + Sekhari capacity theorems | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:191-312` |
| MIA: optimal test + DP cap + Yeom gap (HW4 woven in) | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:472` |
| SCRUB / SalUn / $\ell_1$-sparse classification unlearn | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:367-431` |
| IDI / COLA (lab unlearning eval) | `courses/privacy/lectures/05-unlearning/unlearning1-foundations.html:502-533` |
| GA collapse + NPO bounded + SimNPO | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:103-165` |
| ME+GD / IDK / ELM / LUNAR (LLM unlearn) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:166-241` |
| TOFU / WMDP / RWKU / MUSE benchmarks (main-figure images) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:250-302` |
| Benign + syntactic relearning (lab) | `courses/privacy/lectures/05-unlearning/unlearning2-llm.html:303-328` |
| Position: "Unlearning" overused in LLMs (5-min ICML talk) | `talks/icml2026/icml2026.html` |
| REFT (first-token diversification for RLVR) | `talks/postech260819/postech260819.html:145-455` (rebuttal: 373-420) |
| SafePath (8-token safety primer for LRMs) | `talks/postech260819/postech260819.html:456-591` |
| Benign DPO attack + fine-tuning-as-a-service | `talks/postech260819/postech260819.html:592-798` (rebuttal: 696-746) |
| Kirchenbauer green-list + z-test + entropy bound | `courses/privacy/lectures/06-watermark/watermark.html:164-222` |
| Gumbel distribution + Gumbel-max trick + proof | `courses/privacy/lectures/06-watermark/watermark.html:252-295` |
| Aaronson distortion-free + proof | `courses/privacy/lectures/06-watermark/watermark.html:309-337` |
| Kuditipudi edit-distance robustness theorem | `courses/privacy/lectures/06-watermark/watermark.html:356` |
| Christ–Gunn–Zamir undetectable + PRF construction | `courses/privacy/lectures/06-watermark/watermark.html:386-419` |
| Adaptive watermark + WaterMax | `courses/privacy/lectures/06-watermark/watermark.html:486-516` |
| SynthID-Text production watermark | `courses/privacy/lectures/06-watermark/watermark.html:542` |
| **DP foundations series (dp1–dp7)** | `courses/privacy/lectures/01-dp/dp1`…`dp7-ml-paradigms.html` |
| DP definition / LDP vs central / PrivUnit | `courses/privacy/lectures/01-dp/dp8-fl.html:364-569` |
| RRSC + k-closest exact-optimality (NeurIPS 2023) | `courses/privacy/lectures/01-dp/dp8-fl.html:571-822` |
| DP-SGD / DP-Diffusion / DP-RDM | `courses/privacy/lectures/01-dp/dp8-fl.html:827-1004` |
| Continuous SDE diffusion at a glance (Song et al.) | `talks/kics260521dllm/kics260521dllm.html:99` |
| Masked diffusion at a glance | `talks/kics260521dllm/kics260521dllm.html:115` |
| Reverse process needs a ratio (concrete score) | `talks/kics260521dllm/kics260521dllm.html:179` |
| Rainbow Padding (EOS overflow, ICLR 2026) | `talks/kics260521dllm/kics260521dllm.html:319-461` |
| DAPD (attention dependency graph, ICML 2026) | `talks/kics260521dllm/kics260521dllm.html:463-669` |
| Diffusion-LLM safety (A2D) | `talks/kics260521dllm/kics260521dllm.html:694` |
| dgMARK (diffusion-LLM watermarking, ICML 2026) | `talks/kics260521dllm/kics260521dllm.html:707` |
| Reversal curse in MDMs | `talks/kics260521dllm/kics260521dllm.html:720` |
| Threat-model framing (knowledge × timing), trust dimensions | `courses/trustworthy-ai/lec01-introduction.html:333, :296` |
| $(\varepsilon,\delta)$-DP intuition (undergrad) / formal | `lec02-privacy-dp.html:457` · formal in `lec02tech.html` |
| Statistical indistinguishability (heights example, intuition) | `courses/trustworthy-ai/lec02-privacy-dp.html:581` |
| DP-SGD intuition (clip + noise) / formal algorithm | `lec02-privacy-dp.html:853` · formal in `lec02tech.html` |
| Formal math per lecture (definitions, derivations, algorithms) | `courses/trustworthy-ai/lecNNtech.html` (15 supplements) |

## Cross-references

Same topic, different decks (use the more recent / more detailed):
- **VAE / ELBO**: rigorous derivation `courses/infotheory/lectures/07-diffusion/diff1-vae-elbo.html`
- **Hierarchical-VAE view of diffusion**: `courses/infotheory/lectures/07-diffusion/diff2-diffusion.html` (information-theoretic, Markov rewrite)
- **Diffusion from-scratch (Bayes route)**: `courses/privacy/lectures/02-generative/diffusion1-foundations.html` (Taylor + complete-square proof, less abstract)
- **Tweedie**: convolution-derivative proof `courses/privacy/lectures/02-generative/diffusion1-foundations.html:692-753`; alternate proof `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:135`
- **$f$-divergence variational dual**: brief in `courses/infotheory/lectures/05-mi/mi1-bounds.html:261` (KL instances); full development in `courses/infotheory/lectures/06-divergence/div1-fdivergence-gan.html:121-300`
- **Score matching $\equiv$ diffusion training**: Vincent DSM theorem + proof `courses/infotheory/lectures/06-divergence/div2-fisher-score.html:193-253`; ELBO $\equiv$ DSM capstone `courses/infotheory/lectures/07-diffusion/diff3-parameterizations.html:156-209`

## Companion notes pattern

`<deck>.html` is the deck. `<deck>-note.html` (where present) holds:
- Long-form proofs (theorem cited on slide → full derivation in notes)
- Intuition that doesn't fit on a slide
- Edge cases, comparison tables, references
- Look in the `-note.html` for "why does this hold" / "what's the precise statement" detail.

`courses/infotheory/` has notes for every deck. `courses/privacy/lectures/04-mia/` has notes for every deck. `courses/privacy/lectures/02-generative/` has notes for every diffusion lecture (1–5); `llm.html` has no note. `talks/kics260521dllm/`, `talks/math260624dllm/`, and `courses/privacy/lectures/01-dp/` do **not** have companion notes — proof detail is in-deck or in `note/2_difffusion.tex` (under `courses/privacy/lectures/02-generative/`).

## Authoring conventions

- Course lecture decks live at `courses/<course>/lectures/<NN-topic>/<deck>.html` — reference path `../../../../reference/`.
- Research talks live at `talks/<name>/<deck>.html` — reference path `../../reference/`.
- Build: `python3 scripts/bundle.py <path>/<deck>.html` → `<deck>.standalone.html` (gitignored).
- Lint: `python3 scripts/lint-deck.py --all`.
- Outline pointers: `python3 scripts/outline-lint.py` verifies every `file:line` cited in any `OUTLINE.md` still exists and is within the file's length. Run it after edits that shift line numbers.
