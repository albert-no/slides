# infotheory/divergence/ — Divergence families (2 lectures)

Two-lecture series on the divergences that drive modern generative training. Lecture 1 develops the $f$-divergence family (KL, JS, $\chi^2$, TV, hockey-stick) and the GAN-as-JS-minimization theorem. Lecture 2 covers Fisher divergence and Vincent's denoising score matching theorem. The diffusion-specific equivalence ELBO $\equiv$ DSM is proved in the next series (`diffusion/diff3-parameterizations.html`), citing this lecture for Fisher and DSM.

## Files

| Deck | Note | Topic |
|---|---|---|
| `div1-fdivergence-gan.html` | `div1-fdivergence-gan-note.html` | $f$-divergences, properties, GAN $\equiv$ JS minimization |
| `div2-fisher-score.html` | `div2-fisher-score-note.html` | Fisher divergence and denoising score matching |

---

## div1-fdivergence-gan.html — $f$-Divergence and GAN

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Beyond KL** | Why a broader family | `:63-110` |
| | Recall — ML as KL minimization | `:71` |
| | Pathology 1 — high likelihood, bad samples (Theis et al.) | `:83` |
| | Pathology 2 — overfit gives $-\infty$ likelihood | `:93` |
| | Plan — family of divergences | `:101` |
| **02 — $f$-Divergence definition + examples** | | `:113-208` |
| | **Definition** | `:121` |
| | Reading the definition (3 conventions, asymmetry partner) | `:132` |
| | Example 1 — KL ($f(t)=t\log t$) | `:143` |
| | Example 2 — Reverse KL ($f=-\log t$), TV ($f=\tfrac12\lvert t-1\rvert$) | `:150` |
| | Example 3 — $\chi^2$ ($f=(t-1)^2$) | `:158` |
| | Example 4 — Hockey-stick ($f=[t-\gamma]_+$, DP connection) | `:166` |
| | Example 5 — Jensen–Shannon (compound definition) | `:174` |
| | JS as $f$-divergence (proof) | `:182` |
| | Worked example — two Bernoullis (numerical table) | `:194` |
| **03 — Properties** | DPI and info inequality from one Jensen | `:209-300` |
| | Overview — four properties at once | `:217` |
| | **Theorem (Csiszár, 1967)** — four parts | `:229` |
| | Proof Part 1 — joint via product conditional | `:244` |
| | Proof Part 2 — joint $\ge$ marginal (Jensen on $q(y\lvert x)$) | `:256` |
| | Proof Part 3 — DPI (combines Parts 1 and 2) | `:269` |
| | Proof Part 4 — info inequality | `:281` |
| | Recap — Jensen-on-$f$ drives all four | `:288` |
| **04 — GAN $\equiv$ JS** | Minimax over $f$-divergence | `:301-410` |
| | Setup — generator, discriminator, minimax value | `:309` |
| | Overview — the JS theorem | `:321` |
| | **Theorem (Goodfellow et al., 2014)** — max value $=2D_{\mathrm{JS}}-2\log 2$ | `:330` |
| | Proof Step 1 — optimal $d^*(x) = p_{\mathrm{data}}/(p_{\mathrm{data}}+p_\theta)$ | `:341` |
| | Proof Step 2 — substitute back, identify two KL terms as JS | `:350` |
| | Recap — three labelled steps | `:362` |
| | Training algorithm (alternating ascent/descent) | `:377` |
| | Beyond JS — $f$-GAN via Fenchel dual (+ back-pointer to mi1 DV/NWJ) | `:402` |
| **05 — Recap** | | `:411-441` |
| | Catalogue table — KL/rev-KL/TV/$\chi^2$/hockey/JS | `:419` |
| | Where this lecture sits; pointer to div2 | `:433` |

**Key theorems and definitions:** $f$-divergence definition `:121`; Csiszár properties theorem `:229`; DPI proof `:269`; info inequality `:281`; GAN $\equiv$ $2D_{\mathrm{JS}}$ theorem `:330`; optimal discriminator `:341`; $f$-GAN variational form `:402`.

### Note (`div1-fdivergence-gan-note.html`)
- Why both pathologies matter (Theis et al. discussion)
- Conventions $0\cdot f(0/0)$, $f(0)$, $0\cdot f(a/0)$ — when $D_f$ blows up
- Asymmetry partner $\widetilde f(t) = t\,f(1/t)$
- Pinsker chain: $\mathrm{TV} \le \sqrt{\tfrac12 D_{\mathrm{KL}}} \le \sqrt{\tfrac12 \chi^2}$ (verified on Bernoulli example)
- Hockey-stick and $(\varepsilon,\delta)$-DP — pointer to `privacy/dp/dp8-fl.html`
- Why $D_{\mathrm{JS}} \le 2\log 2$
- $f$-GAN minimax for KL, $\chi^2$, JS (conjugate worked out)
- Wasserstein motivation (out of family, mentioned briefly)
- Forward connection to Lecture 2

---

## div2-fisher-score.html — Fisher Divergence and Score Matching

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Beyond $f$-divergence** | Energy models, score function | `:58-103` |
| | Why another divergence? | `:65` |
| | **Definition (energy-based pdf)** | `:74` |
| | **Definition (score function)** — gradient kills $Z$ | `:85` |
| | Example — Gaussian score | `:95` |
| **02 — Fisher divergence** | Score-based distance | `:104-166` |
| | Overview — where we are going (4 steps) | `:112` |
| | **Lemma** — score identifies the density | `:123` |
| | **Definition (Hyvärinen, 2005)** — Fisher divergence | `:133` |
| | **Theorem** — non-neg, asymmetric, scaling, Gaussian comparator | `:144` |
| | Proof — non-negativity and scaling | `:158` |
| **03 — Denoising score matching** | Gaussian smoothing makes it tractable | `:167-247` |
| | Problem — direct score matching is intractable | `:175` |
| | Setup — $\mathbf{Y} = \mathbf{X} + \mathbf{Z}$ | `:183` |
| | **Theorem (Vincent, 2011)** — DSM equivalence | `:192` |
| | Proof Step 1 — expand the square | `:203` |
| | Proof Step 2 — rewrite cross term using $\nabla_{\mathbf{y}}\mathcal{N}$ | `:215` |
| | Proof Step 3 — assemble | `:227` |
| | Recap — conditional MSE on $\mathbf{x}-\mathbf{y}$ | `:237` |
| **04 — Recap** | Three divergence families | `:248-278` |
| | Three families table ($f$, Fisher, Wasserstein) | `:256` |
| | Where this lecture sits | `:268` |

**Key theorems and definitions:** energy-based pdf `:74`; score function `:85`; score-determines-pdf lemma `:123`; Fisher divergence `:133`; properties theorem `:144`; Vincent DSM theorem `:192`.

The diffusion-specific equivalence (per-step ELBO MSE $\equiv$ DSM at noise level $1-\bar\alpha_t$) is proved in `diffusion/diff3-parameterizations.html` Section 05, citing this lecture for the Fisher and DSM machinery.

### Note (`div2-fisher-score-note.html`)
- Why $f$-divergences fail on energy-based models
- Hyvärinen's original (non-denoising) score matching via integration by parts
- Why Gaussian smoothing is the kernel that gives a closed form
- Sampling from a score model = Langevin dynamics (Fokker–Planck)
- Comparison: $f$ / Fisher / Wasserstein
- Closing thread — pointer forward to diffusion lectures where DSM is applied

---

## Pairing convention

Same as the rest of the series: deck = rigorous statement + intuition; note = expanded derivation + edge cases + cross-references.

## Cross-deck pointers

| Topic | Other folder | Line |
|---|---|---|
| Variational MI bounds (DV, NWJ as KL-instances) — *previous lecture* | `infotheory/mi/mi1-bounds.html` | `:176, :221` (DV/NWJ); `:293` (unifying slide); `:300` (forward-pointer table) |
| Tweedie's formula — *next lecture (Diff 3) uses + proves it* | `infotheory/diffusion/diff3-parameterizations.html` | `:125` (statement), `:136` (proof) |
| Diffusion ELBO $\equiv$ DSM theorem — *Diff 3 capstone (cites Vincent from this lecture)* | `infotheory/diffusion/diff3-parameterizations.html` | `:256` |
| ELBO + diffusion training | `infotheory/diffusion/diff2-diffusion.html` | `:153-212` |
| Hockey-stick and $(\varepsilon,\delta)$-DP | `privacy/dp/dp8-fl.html` | — |
| SDE / Langevin sampling view of score | `privacy/generative/diffusion3-sde-score.html` | `:339` |
