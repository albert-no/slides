# infotheory/lectures/06-divergence/ — Divergence families (2 lectures)

Two-lecture series on the divergences that drive modern generative training. Lecture 1 develops the $f$-divergence family (KL, JS, $\chi^2$, TV, hockey-stick) and the GAN-as-JS-minimization theorem. Lecture 2 covers Fisher divergence and Vincent's denoising score matching theorem. The diffusion-specific equivalence ELBO $\equiv$ DSM is proved in the next series (`diffusion/diff3-parameterizations.html`), citing this lecture for Fisher and DSM.

## Files

| Deck | Note | Topic |
|---|---|---|
| `div1-fdivergence-gan.html` | `div1-fdivergence-gan-note.html` | $f$-divergences, properties, GAN $\equiv$ JS minimization |
| `div2-fisher-score.html` | `div2-fisher-score-note.html` | Fisher divergence and denoising score matching |

---

## div1-fdivergence-gan.html — $f$-Divergence and GAN (43 slides)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Beyond KL** | Why a broader family | `:63-112` |
| | Recall — ML as KL minimization | `:71` |
| | Pathology 1 — high likelihood, bad samples (Theis et al.) | `:83` |
| | Pathology 2 — overfit gives $-\infty$ likelihood | `:93` |
| | Plan — family of divergences | `:101` |
| **02 — $f$-Divergence definition + examples** | | `:113-233` |
| | **Definition** | `:121` |
| | Reading the definition (3 conventions, asymmetry partner) | `:132` |
| | The Generator Function $f$ (diagram — convex curve, tangent-below-curve Jensen picture) | `:143` |
| | Example 1 — KL ($f(t)=t\log t$) | `:169` |
| | Example 2 — Reverse KL ($f=-\log t$), TV ($f=\tfrac12\lvert t-1\rvert$) | `:176` |
| | Example 3 — $\chi^2$ ($f=(t-1)^2$) | `:184` |
| | Example 4 — Hockey-stick ($f=[t-\gamma]_+$, DP connection) | `:192` |
| | Example 5 — Jensen–Shannon (compound definition) | `:200` |
| | JS as $f$-divergence (proof) | `:208` |
| | Worked example — two Bernoullis (numerical table) | `:220` |
| **03 — Properties** | DPI and info inequality from one Jensen | `:235-326` |
| | Overview — four properties at once | `:243` |
| | **Theorem (Csiszár, 1967)** — four parts | `:255` |
| | Proof Part 1 — joint via product conditional | `:270` |
| | Proof Part 2 — joint $\ge$ marginal (Jensen on $q(y\lvert x)$) | `:282` |
| | Proof Part 3 — DPI (combines Parts 1 and 2) | `:295` |
| | Proof Part 4 — info inequality | `:307` |
| | Recap — Jensen-on-$f$ drives all four | `:314` |
| **04 — GAN $\equiv$ JS** | Minimax over $f$-divergence | `:328-520` |
| | Setup — generator, discriminator, minimax value | `:335` |
| | The Adversarial Game (GAN schematic — generator/discriminator dataflow, min/max annotation) | `:347` |
| | Reading the minimax — discriminator vs generator perspectives | `:385` |
| | Overview — the JS theorem | `:402` |
| | **Theorem (Goodfellow et al., 2014)** — max value $=2D_{\mathrm{JS}}-2\log 2$ | `:411` |
| | Proof Step 1 — optimal $d^*(x) = p_{\mathrm{data}}/(p_{\mathrm{data}}+p_\theta)$ | `:422` |
| | Proof Step 2 — substitute back, identify two KL terms as JS | `:431` |
| | Recap — three labelled steps | `:443` |
| | Why JS, Not KL (symmetric / bounded / sample-driven interpretation) | `:458` |
| | Training algorithm (alternating ascent/descent) | `:469` |
| | Beyond JS — $f$-GAN via Fenchel dual | `:494` |
| | Two Roads from One Machine (generative training vs MI estimation, back-pointer to mi1 DV/NWJ) | `:503` |
| **05 — Recap** | | `:522-551` |
| | Catalogue table — KL/rev-KL/TV/$\chi^2$/hockey/JS | `:530` |
| | Where this lecture sits; pointer to div2 | `:544` |

**Key theorems and definitions:** $f$-divergence definition `:121`; Csiszár properties theorem `:255`; DPI proof `:295`; info inequality `:307`; GAN $\equiv$ $2D_{\mathrm{JS}}$ theorem `:411`; optimal discriminator `:422`; $f$-GAN variational form `:494`.

### Note (`div1-fdivergence-gan-note.html`)
- Why both pathologies matter (Theis et al. discussion)
- Conventions $0\cdot f(0/0)$, $f(0)$, $0\cdot f(a/0)$ — when $D_f$ blows up
- Asymmetry partner $\widetilde f(t) = t\,f(1/t)$
- Pinsker chain: $\mathrm{TV} \le \sqrt{\tfrac12 D_{\mathrm{KL}}} \le \sqrt{\tfrac12 \chi^2}$ (verified on Bernoulli example)
- Hockey-stick and $(\varepsilon,\delta)$-DP — pointer to `courses/privacy/lectures/01-dp/dp8-fl.html`
- Why $D_{\mathrm{JS}} \le 2\log 2$
- $f$-GAN minimax for KL, $\chi^2$, JS (conjugate worked out)
- Wasserstein motivation (out of family, mentioned briefly)
- Forward connection to Lecture 2

---

## div2-fisher-score.html — Fisher Divergence and Score Matching (32 slides)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Beyond $f$-divergence** | Energy models, score function | `:58-146` |
| | Why another divergence? | `:66` |
| | **Definition (energy-based pdf)** | `:77` |
| | **Definition (score function)** — gradient kills $Z$ | `:88` |
| | Example — Gaussian score | `:96` |
| | Score as a Vector Field (intuition — score field points uphill toward modes) | `:104` |
| **02 — Fisher divergence** | Score-based distance | `:148-221` |
| | Overview — where we are going (4 steps) | `:156` |
| | **Lemma** — score identifies the density | `:167` |
| | **Definition (Hyvärinen, 2005)** — Fisher divergence | `:177` |
| | **Theorem** — non-neg, asymmetric, scaling, Gaussian comparator | `:188` |
| | Proof — Non-Negativity and Asymmetry (counterexample for (2)) | `:202` |
| | Proof — Scaling and Gaussian Comparator (change-of-variables algebra for (3), direct substitution for (4)) | `:210` |
| **03 — Denoising score matching** | Gaussian smoothing makes it tractable | `:223-381` |
| | Problem — direct score matching is intractable | `:231` |
| | Setup — $\mathbf{Y} = \mathbf{X} + \mathbf{Z}$ | `:239` |
| | The Denoising Setup, Pictured (schematic — clean $\mathbf{x}$, noisy $\mathbf{y}=\mathbf{x}+\mathbf{z}$, learned denoising arrow back) | `:248` |
| | **Theorem (Vincent, 2011)** — DSM equivalence | `:285` |
| | Intuition — the denoising direction (kernel score) | `:296` |
| | Intuition — Tweedie's bridge (marginal score = posterior mean) | `:304` |
| | Proof — Roadmap (3-step outline: expand, rewrite cross term, complete the square) | `:312` |
| | Proof Step 1 — expand the square | `:323` |
| | Proof Step 2a — kernel-score identity ($\nabla_{\mathbf{y}}\mathcal{N}=\frac{\mathbf{x}-\mathbf{y}}{\sigma^2}\mathcal{N}$, recall-before-use) | `:335` |
| | Proof Step 2b — rewrite cross term (applies the Step 2a identity) | `:343` |
| | Proof Step 3a — match the measures (marginalization rewrite so both terms share the joint measure) | `:355` |
| | Proof Step 3b — complete the square (full algebra) | `:362` |
| | Recap — conditional MSE on $\mathbf{x}-\mathbf{y}$ | `:372` |
| **04 — Recap** | Three divergence families | `:383-411` |
| | Three families table ($f$, Fisher, Wasserstein) | `:391` |
| | Where this lecture sits | `:403` |

**Key theorems and definitions:** energy-based pdf `:77`; score function `:88`; score-determines-pdf lemma `:167`; Fisher divergence `:177`; properties theorem `:188`; Vincent DSM theorem `:285`; Tweedie bridge intuition `:304`.

The diffusion-specific equivalence (per-step ELBO MSE $\equiv$ DSM at noise level $1-\bar\alpha_t$) is proved in `diffusion/diff3-parameterizations.html` Section 05, citing this lecture for the Fisher and DSM machinery.

### Note (`div2-fisher-score-note.html`)
- Why $f$-divergences fail on energy-based models
- Intuition section: pointer to the deck's kernel-score-identity/Tweedie derivation (now fully on-slide) + the one genuinely new piece — why MSE over data pairs recovers the marginal score (law of total expectation)
- Hyvärinen's original (non-denoising) score matching via integration by parts
- Why Gaussian *specifically* (not smoothing in general) gives a closed-form target — pointer to deck's Proof Step 2a (kernel-score identity) + the kernel-comparison argument
- Sampling from a score model = Langevin dynamics (Fokker–Planck)
- Comparison: $f$ / Fisher / Wasserstein
- Closing thread — pointer forward to diffusion lectures where DSM is applied

---

## Pairing convention

Same as the rest of the series: deck = rigorous statement + intuition; note = expanded derivation + edge cases + cross-references.

## Cross-deck pointers

| Topic | Other folder | Line |
|---|---|---|
| Variational MI bounds (DV, NWJ as KL-instances) — *previous lecture* | `infotheory/lectures/05-mi/mi1-bounds.html` | `:176, :221` (DV/NWJ); `:293` (unifying slide); `:300` (forward-pointer table) |
| Tweedie's formula — *next lecture (Diff 3) uses + proves it* | `infotheory/lectures/07-diffusion/diff3-parameterizations.html` | `:125` (statement), `:136` (proof) |
| Diffusion ELBO $\equiv$ DSM theorem — *Diff 3 capstone (cites Vincent from this lecture)* | `infotheory/lectures/07-diffusion/diff3-parameterizations.html` | `:256` |
| ELBO + diffusion training | `infotheory/lectures/07-diffusion/diff2-diffusion.html` | `:153-212` |
| Hockey-stick and $(\varepsilon,\delta)$-DP | `courses/privacy/lectures/01-dp/dp8-fl.html` | — |
| SDE / Langevin sampling view of score | `courses/privacy/lectures/02-generative/diffusion3-sde-score.html` | `:339` |
