# infotheory/lectures/05-mi/ — Mutual-information estimation (2 lectures)

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
| Title / Contents | | `:19, :31` |
| **01 — Setup** | Motivation, why hard, what is computable, density ratio | `:63-121` |
| | Why estimate MI? (CLIP, SSL, IB) | `:71` |
| | MI as KL | `:83` |
| | Why is it hard? (density ratio without densities) | `:90` |
| | What we can — and cannot — compute | `:102` |
| | Density-ratio framing | `:117` |
| **02 — Barber–Agakov** | Variational LB via q(x\|y) | `:125-168` |
| | **Theorem (BA bound)** | `:133, :137` |
| | Proof — add and subtract log q (full substitution shown) | `:144` |
| | BA in practice → MLE | `:155` |
| **03 — Donsker–Varadhan** | Dual KL representation, MINE | `:171-219` |
| | **Theorem (DV representation)** | `:179, :183` |
| | DV bound on MI | `:189` |
| | Proof — tilt Q by e^T (full $D_{KL}(P\|G)$ expansion) | `:196` |
| | MINE — neural DV estimator (Monte Carlo) | `:207` |
| **04 — NWJ** | Linear-surrogate variant | `:221-263` |
| | From DV to NWJ (log inequality, full substitution + reparam) | `:229` |
| | **Theorem (Nguyen, Wainwright, Jordan 2010)** | `:236, :239` |
| | NWJ vs DV variance trade | `:250` |
| **05 — Tradeoffs & unification** | High MI barrier; $f$-divergence variational view | `:265-343` |
| | High-MI barrier (McAllester–Stratos, variance derivation shown) | `:273, :274` |
| | Three bounds side-by-side | `:285` |
| | Choosing your bound | `:298` |
| | One machine — KL is the tip (Fenchel dual + conjugate derivation) | `:308` |
| | Forward pointer to Divergence Lectures (table to div1 §02–04, div2) | `:318` |
| | Recap (now includes $f$-divergence framing) | `:333` |

**Key theorems:** BA bound `:137`, proof `:144-152`; DV representation `:183`, proof `:196-205`; DV→MI bound `:191`; NWJ bound `:239`, derivation from DV `:229-234`; McAllester–Stratos variance bound `:274`, mechanism sketch `:275-278`; $f$-divergence Fenchel dual + DV/NWJ as KL instances `:308-315` (machinery deferred to `divergence/div1`).

### Note (`mi1-bounds-note.html`)
- Density ratio as unifying view `:25`
- MINE estimator bias `:31`
- McAllester–Stratos lower bound — estimator-agnostic two-sample-testing argument, complementary to the deck's DV-specific AEP/delta-method derivation (§05) `:37`
- Toy bivariate Gaussian detail `:43`
- f-divergences and f-GAN connection — Fenchel-conjugate unification now derived on the deck (§05); note trimmed to a pointer plus the f-GAN generative-modeling link and forward pointer to `divergence/` `:55`
- Why CLIP/InfoNCE is different from these `:62`

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
- InfoNCE proof + log K saturation — now a short pointer to the deck's §01 ("Proof Sketch", "Optimal Critic") which derives both in full; note keeps only the original-references pointer (Oord 2018, Poole 2019) `:25`
- Temperature τ in CLIP `:30`
- Why symmetric loss `:37`
- CLIP zero-shot recipe `:44`
- Robustness / other zero-shot capabilities `:55`
- What CLIP doesn't do well `:61`
