# infotheory/ — Information-theory lecture series

Master-level series with paired `<deck>.html` + `<deck>-note.html`. Notes hold full derivations and proof detail; decks hold the rigorous statements + intuition.

## Subfolders

- **`entropy/`** — Foundations: entropy and basic information-theoretic quantities (2 lectures): entropy + KL → joint, conditional, MI, Fano. See `entropy/OUTLINE.md`.
- **`lossless/`** — Lossless compression (3 lectures): codes/Kraft/Huffman → AEP/arithmetic → Markov/universal/LZ. See `lossless/OUTLINE.md`.
- **`diffentropy/`** — Differential entropy and continuous-domain MI (3 lectures): foundations → MaxEnt/Gaussian/EPI → MI/AWGN/water-filling/I-MMSE. See `diffentropy/OUTLINE.md`.
- **`lossy/`** — Rate–distortion theory + modern LLM compression (4 lectures): foundations → Gaussian/Laplacian + pruning + CROM → lattice codes & QUIP# → TURBOQUANT. See `lossy/OUTLINE.md`.
- **`mi/`** — Mutual-information estimation (2 lectures): variational lower bounds (BA, DV, NWJ, MINE) → InfoNCE & CLIP; closes with $f$-divergence unification. See `mi/OUTLINE.md`.
- **`divergence/`** — Divergence families behind modern generative training (2 lectures): $f$-divergence + GAN $\equiv$ JS minimization → Fisher divergence + denoising score matching. See `divergence/OUTLINE.md`.
- **`diffusion/`** — Diffusion through the information-theory lens (3 lectures): VAE/ELBO → hierarchical VAE → parameterizations + Tweedie; closes by showing diffusion ELBO $\equiv$ score matching (using machinery from `divergence/`). See `diffusion/OUTLINE.md`.
- **`ib/`** — Information Bottleneck (2 lectures): IB Lagrangian + self-consistent equations → Variational IB + deep learning. Connects MI bounds from `mi/`, rate-distortion from `lossy/`, DPI from `entropy/`. See `ib/OUTLINE.md`.

## Reading order (suggested for a full master's course)

1. **`entropy/`** — discrete entropy, KL, MI, DPI, Fano. Foundation.
2. **`lossless/`** — entropy as the operational compression limit; Kraft, AEP, arithmetic, LZ.
3. **`diffentropy/`** — continuous-domain analogue; Gaussian as MaxEnt; AWGN capacity.
4. **`lossy/`** — rate–distortion theory; classical R(D) and modern LLM compression.
5. **`mi/`** — variational MI bounds; InfoNCE/CLIP.
6. **`divergence/`** — $f$-divergence + GAN, Fisher + denoising score matching.
7. **`diffusion/`** — generative modeling through the info-theoretic lens; closes the loop by showing diffusion ELBO $\equiv$ score matching.
8. **`ib/`** — the information bottleneck: compression for relevance; connects MI, R(D), and deep learning.

## Themes

- **entropy / lossless / diffentropy** establish the discrete- and continuous-domain toolkits.
- **lossy** ramps from classical R(D) to **applied compression of LLM weights and KV caches** (QUIP#, TURBOQUANT).
- **mi** culminates in the MI view of CLIP — the bridge between variational-bound theory and contrastive learning.
- **divergence** synthesizes the divergence families: $f$-divergences unify MI/GAN; Fisher + DSM sets up the score-based view.
- **diffusion** is the *theoretical* side of diffusion (see `privacy/generative/` for the from-scratch Bayes-route version); closes by showing diffusion ELBO $\equiv$ DSM, using `divergence/` machinery.
- **ib** bridges information theory and deep learning: IB Lagrangian reuses MI from `entropy/` and rate-distortion from `lossy/`; the information plane gives a diagnostic lens for DNN representations.

## Cross-deck pointers

| Topic | Lecture | Line |
|---|---|---|
| Entropy definition | `entropy/entropy1-entropy-kl.html` | `:97` |
| Gibbs inequality | `entropy/entropy1-entropy-kl.html` | `:379` |
| Log-sum inequality | `entropy/entropy1-entropy-kl.html` | `:437` |
| Chain rule (entropy) | `entropy/entropy2-joint-mi-fano.html` | `:118` |
| Conditioning reduces entropy | `entropy/entropy2-joint-mi-fano.html` | `:158` |
| Mutual information definition | `entropy/entropy2-joint-mi-fano.html` | `:227` |
| Data processing inequality | `entropy/entropy2-joint-mi-fano.html` | `:368` |
| Fano's inequality | `entropy/entropy2-joint-mi-fano.html` | `:438` |
| Kraft inequality | `lossless/lossless1-codes.html` | `:157` |
| Kraft–McMillan | `lossless/lossless1-codes.html` | `:198` |
| Shannon code (entropy bound) | `lossless/lossless1-codes.html` | `:268` |
| Huffman optimality | `lossless/lossless1-codes.html` | `:413` |
| AEP | `lossless/lossless2-aep-arithmetic.html` | `:84` |
| Source coding theorem | `lossless/lossless2-aep-arithmetic.html` | `:204` |
| Arithmetic coding bound | `lossless/lossless2-aep-arithmetic.html` | `:405` |
| Markov entropy rate | `lossless/lossless3-markov-universal.html` | `:188` |
| LZ78 optimality | `lossless/lossless3-markov-universal.html` | `:355` |
| Differential entropy definition | `diffentropy/diffentropy1-foundations.html` | `:84` |
| Bin discretization bridge | `diffentropy/diffentropy1-foundations.html` | `:96` |
| MI invariance under scaling | `diffentropy/diffentropy1-foundations.html` | `:386` |
| Gaussian MaxEnt | `diffentropy/diffentropy2-maxent-gaussian.html` | `:165` |
| Hadamard's inequality | `diffentropy/diffentropy2-maxent-gaussian.html` | `:248` |
| EPI | `diffentropy/diffentropy2-maxent-gaussian.html` | `:367` |
| Shannon–Hartley | `diffentropy/diffentropy3-mi-awgn.html` | `:177` |
| Water-filling | `diffentropy/diffentropy3-mi-awgn.html` | `:293` |
| I-MMSE | `diffentropy/diffentropy3-mi-awgn.html` | `:385` |
| ELBO definition | `diffusion/diff1-vae-elbo.html` | `:101` |
| Reparameterization trick (lemma) | `diffusion/diff1-vae-elbo.html` | `:198` |
| q(x_t\|x_0) closed form | `diffusion/diff2-diffusion.html` | `:76` |
| Tweedie's formula (theorem + proof) | `diffusion/diff3-parameterizations.html` | `:121` (statement), `:130` (proof) |
| Shannon's R(D) theorem | `lossy/lossy1-foundations.html` | `:270` |
| Gaussian R(D) achievability + converse | `lossy/lossy2-gaussian-laplacian.html` | `:71-160` |
| Layer-wise telescoping (pruning) | `lossy/lossy2-gaussian-laplacian.html` | `:215` |
| Lattice packing gain | `lossy/lossy3-lattice-quip.html` | `:119` |
| QUIP# Hadamard step | `lossy/lossy3-lattice-quip.html` | `:180` |
| TURBOQUANT_mse theorem | `lossy/lossy4-turboquant.html` | `:154` |
| QJL lemma | `lossy/lossy4-turboquant.html` | `:233` |
| Barber–Agakov bound | `mi/mi1-bounds.html` | `:107` |
| Donsker–Varadhan representation | `mi/mi1-bounds.html` | `:151` |
| $f$-divergence variational view (DV, NWJ as KL instances) | `mi/mi1-bounds.html` | `:261, :270` |
| InfoNCE bound | `mi/mi2-infonce-clip.html` | `:91` |
| $f$-divergence definition | `divergence/div1-fdivergence-gan.html` | `:121` |
| $f$-divergence properties theorem (DPI, info inequality) | `divergence/div1-fdivergence-gan.html` | `:229` |
| GAN $\equiv$ Jensen–Shannon theorem | `divergence/div1-fdivergence-gan.html` | `:330` |
| Energy-based pdf + score function | `divergence/div2-fisher-score.html` | `:80, :91` |
| Fisher divergence definition (Hyvärinen) | `divergence/div2-fisher-score.html` | `:141` |
| Denoising score matching theorem (Vincent) | `divergence/div2-fisher-score.html` | `:200` |
| Diffusion ELBO $\equiv$ DSM theorem | `diffusion/diff3-parameterizations.html` | `:256` |
| IB Lagrangian (definition) | `ib/ib1-foundations.html` | `:112` |
| IB optimal encoder (Gibbs form) | `ib/ib1-foundations.html` | `:182` |
| Relevance decomposition lemma | `ib/ib1-foundations.html` | `:261` |
| IB $\equiv$ R(D) with log-loss | `ib/ib1-foundations.html` | `:284` |
| Information plane definition | `ib/ib1-foundations.html` | `:315` |
| VIB definition | `ib/ib2-deep-learning.html` | `:225` |
| Rate upper bound (variational) | `ib/ib2-deep-learning.html` | `:200` |

## Pairing convention

Every deck has a `-note.html` companion. The note generally contains:
- Full derivations of theorems stated in the deck.
- Pitfalls, edge cases, comparison tables.
- Forward/backward references to other lectures in the series.
- Connection to the *next* lecture (often at the bottom of the note).

When in doubt: deck = "what is true"; note = "why and how to apply".
