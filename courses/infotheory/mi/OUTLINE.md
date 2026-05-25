# infotheory/mi/ — Mutual-information estimation (2 lectures)

Variational MI bounds → contrastive learning (InfoNCE/CLIP). Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `mi1-bounds.html` | `mi1-bounds-note.html` | Variational lower bounds on MI (BA, DV, NWJ, MINE) |
| `mi2-infonce-clip.html` | `mi2-infonce-clip-note.html` | InfoNCE and CLIP |

---

## mi1-bounds.html — Variational lower bounds on MI

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :30` |
| **01 — Setup** | Motivation, why hard, what is computable, density ratio | `:63-124` |
| | Why estimate MI? (CLIP, SSL, IB) | `:71` |
| | MI as KL | `:83` |
| | Why is it hard? (density ratio without densities) | `:90` |
| | What we can — and cannot — compute | `:102` |
| | Density-ratio framing | `:117` |
| **02 — Barber–Agakov** | Variational LB via q(x\|y) | `:126-167` |
| | **Theorem (BA bound)** | `:133, :135` |
| | Proof — add and subtract log q | `:144` |
| | BA in practice → MLE | `:151` |
| **03 — Donsker–Varadhan** | Dual KL representation, MINE | `:169-212` |
| | **Theorem (DV representation)** | `:176, :178` |
| | DV bound on MI | `:186` |
| | Proof — tilt Q by e^T | `:193` |
| | MINE — neural DV estimator (Monte Carlo) | `:200` |
| **04 — NWJ** | Linear-surrogate variant | `:214-253` |
| | From DV to NWJ (log inequality) | `:221` |
| | **Theorem (Nguyen, Wainwright, Jordan 2010)** | `:228, :231` |
| | NWJ vs DV variance trade | `:238` |
| **05 — Tradeoffs & unification** | High MI barrier; $f$-divergence variational view | `:254-325` |
| | High-MI barrier (McAllester–Stratos) | `:262, :264` |
| | Three bounds side-by-side | `:270` |
| | Choosing your bound | `:283` |
| | One machine — KL is the tip (DV/NWJ as $f$-divergence instances) | `:293` |
| | Forward pointer to Divergence Lectures (table to div1 §02–04, div2) | `:300` |
| | Recap (now includes $f$-divergence framing) | `:315` |

**Key theorems:** BA bound `:137`; DV representation `:179`; DV→MI bound `:187`; NWJ bound `:231`; McAllester–Stratos variance bound `:264`; $f$-divergence Fenchel dual + DV/NWJ as KL instances `:293` (machinery deferred to `divergence/div1`).

### Note (`mi1-bounds-note.html`)
- Density ratio as unifying view `:25`
- MINE estimator bias `:31`
- McAllester–Stratos lower bound `:37`
- Toy bivariate Gaussian detail `:43`
- f-divergences and f-GAN connection (with forward pointer to `divergence/`) `:55`
- Why CLIP/InfoNCE is different from these `:67`

---

## mi2-infonce-clip.html — InfoNCE and CLIP

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:34, :45` |
| Motivation (preamble) | Why another bound? What we want from it | `:73, :84` |
| **01 — InfoNCE** | K-class softmax bounded by log K | `:96-143` |
| | Setup — 1 positive, K−1 negatives | `:104` |
| | **Theorem (InfoNCE bound)** | `:112, :114` |
| | Proof sketch | `:124` |
| | Optimal critic = log-density-ratio | `:133, :135` |
| **02 — CLIP architecture** | InfoNCE at web scale | `:145-225` |
| | Two encoders, one space | `:153` |
| | Separable critic + symmetric loss | `:173` |
| | Is separable enough? (Mercer / UAT) | `:182` |
| | Why we live with the restriction | `:193` |
| | N×N similarity matrix (encoder + matmul) | `:203` |
| **03 — Zero-shot classification** | Reusing the contrastive head | `:227-267` |
| | CLIP as classifier | `:234` |
| | Why it works — InfoNCE ≈ MAP | `:246` |
| | Prompt engineering | `:254` |
| **04 — Practice** | Bias, variance, batch size | `:269-311` |
| | Four bounds side-by-side | `:276` |
| | Why batch size matters | `:290` |

**Key:** InfoNCE bound `:116`; optimal critic = log-ratio `:135`; log K saturation `:119`; separable-critic justification (Mercer) `:182`; encoder evaluation $S_{ij} = g_i^\top h_j / \tau$ `:203`.

### Note (`mi2-infonce-clip-note.html`)
- Full InfoNCE proof detail `:25`
- Why exactly log K saturation `:42`
- Temperature τ in CLIP `:48`
- Why symmetric loss `:55`
- CLIP zero-shot recipe `:62`
- Robustness / other zero-shot capabilities `:73`
- What CLIP doesn't do well `:79`
