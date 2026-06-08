# infotheory/lectures/ — Information-theory lecture series

Master-level series with paired `<deck>.html` + `<deck>-note.html`. Notes hold full derivations and proof detail; decks hold the rigorous statements + intuition. Folders are numbered in reading order (`01-`…`08-`); deck filenames keep their intra-topic numbering (`entropy1-…`, `lossless1-…`).

The companion LaTeX lecture notes live one level up in `../notes/`; exams in `../exam/`; the frozen legacy source in `../overleaf/`.

## Subfolders

- **`01-entropy/`** — Foundations: entropy and basic information-theoretic quantities (2 lectures): entropy + KL → joint, conditional, MI, Fano. See `01-entropy/OUTLINE.md`.
- **`02-lossless/`** — Lossless compression (3 lectures): codes/Kraft/Huffman → AEP/arithmetic → Markov/universal/LZ. See `02-lossless/OUTLINE.md`.
- **`03-diffentropy/`** — Differential entropy and continuous-domain MI (3 lectures): foundations → MaxEnt/Gaussian/EPI → MI/AWGN/water-filling/I-MMSE. See `03-diffentropy/OUTLINE.md`.
- **`04-lossy/`** — Rate–distortion theory + modern LLM compression (4 lectures): foundations → Gaussian/Laplacian + pruning + CROM → lattice codes & QUIP# → TURBOQUANT. See `04-lossy/OUTLINE.md`.
- **`05-mi/`** — Mutual-information estimation (2 lectures): variational lower bounds (BA, DV, NWJ, MINE) → InfoNCE & CLIP; closes with $f$-divergence unification. See `05-mi/OUTLINE.md`.
- **`06-divergence/`** — Divergence families behind modern generative training (2 lectures): $f$-divergence + GAN $\equiv$ JS minimization → Fisher divergence + denoising score matching. See `06-divergence/OUTLINE.md`.
- **`07-diffusion/`** — Diffusion through the information-theory lens (3 lectures): VAE/ELBO → hierarchical VAE → parameterizations + Tweedie; closes by showing diffusion ELBO $\equiv$ score matching (using machinery from `06-divergence/`). See `07-diffusion/OUTLINE.md`.
- **`08-ib/`** — Information Bottleneck (2 lectures): IB Lagrangian + self-consistent equations → Variational IB + deep learning. Connects MI bounds from `05-mi/`, rate-distortion from `04-lossy/`, DPI from `01-entropy/`. See `08-ib/OUTLINE.md`.

## Reading order (suggested for a full master's course)

1. **`01-entropy/`** — discrete entropy, KL, MI, DPI, Fano. Foundation.
2. **`02-lossless/`** — entropy as the operational compression limit; Kraft, AEP, arithmetic, LZ.
3. **`03-diffentropy/`** — continuous-domain analogue; Gaussian as MaxEnt; AWGN capacity.
4. **`04-lossy/`** — rate–distortion theory; classical R(D) and modern LLM compression.
5. **`05-mi/`** — variational MI bounds; InfoNCE/CLIP.
6. **`06-divergence/`** — $f$-divergence + GAN, Fisher + denoising score matching.
7. **`07-diffusion/`** — generative modeling through the info-theoretic lens; closes the loop by showing diffusion ELBO $\equiv$ score matching.
8. **`08-ib/`** — the information bottleneck: compression for relevance; connects MI, R(D), and deep learning.

## Themes

- **entropy / lossless / diffentropy** establish the discrete- and continuous-domain toolkits.
- **lossy** ramps from classical R(D) to **applied compression of LLM weights and KV caches** (QUIP#, TURBOQUANT).
- **mi** culminates in the MI view of CLIP — the bridge between variational-bound theory and contrastive learning.
- **divergence** synthesizes the divergence families: $f$-divergences unify MI/GAN; Fisher + DSM sets up the score-based view.
- **diffusion** is the *theoretical* side of diffusion (see `courses/privacy/lectures/02-generative/` for the from-scratch Bayes-route version); closes by showing diffusion ELBO $\equiv$ DSM, using `06-divergence/` machinery.
- **ib** bridges information theory and deep learning: IB Lagrangian reuses MI from `01-entropy/` and rate-distortion from `04-lossy/`; the information plane gives a diagnostic lens for DNN representations.

## Cross-deck pointers

| Topic | Lecture | Line |
|---|---|---|
| Entropy definition | `01-entropy/entropy1-entropy-kl.html` | `:97` |
| Gibbs inequality | `01-entropy/entropy1-entropy-kl.html` | `:379` |
| Log-sum inequality | `01-entropy/entropy1-entropy-kl.html` | `:437` |
| Chain rule (entropy) | `01-entropy/entropy2-joint-mi-fano.html` | `:118` |
| Conditioning reduces entropy | `01-entropy/entropy2-joint-mi-fano.html` | `:158` |
| Mutual information definition | `01-entropy/entropy2-joint-mi-fano.html` | `:227` |
| Data processing inequality | `01-entropy/entropy2-joint-mi-fano.html` | `:368` |
| Fano's inequality | `01-entropy/entropy2-joint-mi-fano.html` | `:438` |
| Kraft inequality | `02-lossless/lossless1-codes.html` | `:157` |
| Kraft–McMillan | `02-lossless/lossless1-codes.html` | `:198` |
| Shannon code (entropy bound) | `02-lossless/lossless1-codes.html` | `:268` |
| Huffman optimality | `02-lossless/lossless1-codes.html` | `:413` |
| AEP | `02-lossless/lossless2-aep-arithmetic.html` | `:84` |
| Source coding theorem | `02-lossless/lossless2-aep-arithmetic.html` | `:204` |
| Arithmetic coding bound | `02-lossless/lossless2-aep-arithmetic.html` | `:405` |
| Markov entropy rate | `02-lossless/lossless3-markov-universal.html` | `:188` |
| LZ78 optimality | `02-lossless/lossless3-markov-universal.html` | `:355` |
| Differential entropy definition | `03-diffentropy/diffentropy1-foundations.html` | `:84` |
| Bin discretization bridge | `03-diffentropy/diffentropy1-foundations.html` | `:96` |
| MI invariance under scaling | `03-diffentropy/diffentropy1-foundations.html` | `:386` |
| Gaussian MaxEnt | `03-diffentropy/diffentropy2-maxent-gaussian.html` | `:165` |
| Hadamard's inequality | `03-diffentropy/diffentropy2-maxent-gaussian.html` | `:248` |
| EPI | `03-diffentropy/diffentropy2-maxent-gaussian.html` | `:367` |
| Shannon–Hartley | `03-diffentropy/diffentropy3-mi-awgn.html` | `:177` |
| Water-filling | `03-diffentropy/diffentropy3-mi-awgn.html` | `:293` |
| I-MMSE | `03-diffentropy/diffentropy3-mi-awgn.html` | `:385` |
| ELBO definition | `07-diffusion/diff1-vae-elbo.html` | `:101` |
| Reparameterization trick (lemma) | `07-diffusion/diff1-vae-elbo.html` | `:198` |
| q(x_t\|x_0) closed form | `07-diffusion/diff2-diffusion.html` | `:76` |
| Tweedie's formula (theorem + proof) | `07-diffusion/diff3-parameterizations.html` | `:121` (statement), `:130` (proof) |
| Shannon's R(D) theorem | `04-lossy/lossy1-foundations.html` | `:270` |
| Gaussian R(D) achievability + converse | `04-lossy/lossy2-gaussian-laplacian.html` | `:71-160` |
| Layer-wise telescoping (pruning) | `04-lossy/lossy2-gaussian-laplacian.html` | `:215` |
| Lattice packing gain | `04-lossy/lossy3-lattice-quip.html` | `:119` |
| QUIP# Hadamard step | `04-lossy/lossy3-lattice-quip.html` | `:180` |
| TURBOQUANT_mse theorem | `04-lossy/lossy4-turboquant.html` | `:154` |
| QJL lemma | `04-lossy/lossy4-turboquant.html` | `:233` |
| Barber–Agakov bound | `05-mi/mi1-bounds.html` | `:107` |
| Donsker–Varadhan representation | `05-mi/mi1-bounds.html` | `:151` |
| $f$-divergence variational view (DV, NWJ as KL instances) | `05-mi/mi1-bounds.html` | `:261, :270` |
| InfoNCE bound | `05-mi/mi2-infonce-clip.html` | `:91` |
| $f$-divergence definition | `06-divergence/div1-fdivergence-gan.html` | `:121` |
| $f$-divergence properties theorem (DPI, info inequality) | `06-divergence/div1-fdivergence-gan.html` | `:229` |
| GAN $\equiv$ Jensen–Shannon theorem | `06-divergence/div1-fdivergence-gan.html` | `:330` |
| Energy-based pdf + score function | `06-divergence/div2-fisher-score.html` | `:80, :91` |
| Fisher divergence definition (Hyvärinen) | `06-divergence/div2-fisher-score.html` | `:141` |
| Denoising score matching theorem (Vincent) | `06-divergence/div2-fisher-score.html` | `:200` |
| Diffusion ELBO $\equiv$ DSM theorem | `07-diffusion/diff3-parameterizations.html` | `:256` |
| IB Lagrangian (definition) | `08-ib/ib1-foundations.html` | `:112` |
| IB optimal encoder (Gibbs form) | `08-ib/ib1-foundations.html` | `:182` |
| Relevance decomposition lemma | `08-ib/ib1-foundations.html` | `:261` |
| IB $\equiv$ R(D) with log-loss | `08-ib/ib1-foundations.html` | `:284` |
| Information plane definition | `08-ib/ib1-foundations.html` | `:315` |
| VIB definition | `08-ib/ib2-deep-learning.html` | `:225` |
| Rate upper bound (variational) | `08-ib/ib2-deep-learning.html` | `:200` |

## Pairing convention

Every deck has a `-note.html` companion. The note generally contains:
- Full derivations of theorems stated in the deck.
- Pitfalls, edge cases, comparison tables.
- Forward/backward references to other lectures in the series.
- Connection to the *next* lecture (often at the bottom of the note).

When in doubt: deck = "what is true"; note = "why and how to apply".
