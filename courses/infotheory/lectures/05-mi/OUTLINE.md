# infotheory/lectures/05-mi/ — Mutual-information estimation (2 lectures)

Variational MI bounds → contrastive learning (InfoNCE/CLIP). Each deck paired with `-note.html`.

## Files

| Deck | Note | Topic |
|---|---|---|
| `mi1-bounds.html` | `mi1-bounds-note.html` | Variational lower bounds on MI (BA, DV, NWJ, MINE) |
| `mi2-infonce-clip.html` | `mi2-infonce-clip-note.html` | InfoNCE and CLIP |

---

## mi1-bounds.html — Variational lower bounds on MI (36 slides)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:19, :31` |
| **01 — Setup** | Motivation, why hard, what is computable, density ratio, critic-as-classifier | `:63-153` |
| | Why estimate MI? (CLIP, SSL, IB) | `:71` |
| | MI as KL | `:83` |
| | Why is it hard? (density ratio without densities) | `:90` |
| | What we can — and cannot — compute | `:102` |
| | Density-ratio framing | `:117` |
| | The Critic Is a Classifier (new: joint-vs-product scatter + decision-boundary diagram) | `:125` |
| **02 — Barber–Agakov** | Variational LB via q(x\|y) | `:164-209` |
| | **Theorem (BA bound)** | `:165, :167` |
| | Proof — Add and Subtract log q (split 1/2: derives the KL-gap identity) | `:176` |
| | Proof — Drop the KL Term (split 2/2: substitutes back, drops KL, states bound) | `:183` |
| | BA in practice → MLE | `:193` |
| **03 — Donsker–Varadhan** | Dual KL representation, tilting intuition, MINE | `:217-285` |
| | **Theorem (DV representation)** | `:218, :220` |
| | DV bound on MI | `:228` |
| | Intuition — Tilting Reweights Q Toward P (new: Q / weight $e^T$ / tilted-G curve diagram) | `:235` |
| | Proof — Tilt Q by e^T (split 1/2: defines tilted measure G, expands $D_{KL}(P\|G)$) | `:256` |
| | Proof — Rearrange to the Bound (split 2/2: identifies first term as $D_{KL}(P\|Q)$, rearranges) | `:267` |
| | MINE — neural DV estimator (Monte Carlo) | `:276` |
| **04 — NWJ** | Linear-surrogate variant | `:289-334` |
| | From DV to NWJ (split 1/2: log-inequality substitution into the DV bound) | `:297` |
| | From DV to NWJ — Relabel (split 2/2: critic relabeling $T\to T-1$ to reach NWJ form) | `:305` |
| | **Theorem (Nguyen, Wainwright, Jordan 2010)** | `:312, :314` |
| | NWJ vs DV variance trade | `:322` |
| **05 — Tradeoffs & unification** | High MI barrier (why + cost); $f$-divergence variational view | `:338-457` |
| | The High-MI Barrier — Why (split 1/2: AEP-tail + delta-method variance derivation) | `:346` |
| | The High-MI Barrier — Cost (split 2/2: McAllester–Stratos citation + new variance-vs-MI diagram) | `:358` |
| | Three bounds side-by-side | `:388` |
| | Choosing your bound | `:401` |
| | One machine — KL is the tip (Fenchel dual + conjugate derivation) | `:411` |
| | NWJ and DV — Same Conjugate (new: shows NWJ as the bare conjugate, DV as the tightened sup over T) | `:422` |
| | Forward pointer to Divergence Lectures (table to div1 §02–04, div2) | `:433` |
| | Recap (now includes $f$-divergence framing) | `:448` |

**Key theorems:** BA bound `:167`, proof `:176-190` (split across "Add and Subtract log q" `:176-181` and "Drop the KL Term" `:183-190`); DV representation `:220`, proof `:256-273` (split across "Tilt Q by e^T" `:256-264` and "Rearrange to the Bound" `:266-273`); DV→MI bound `:229`; NWJ bound `:314`, derivation from DV `:297-309` (split across "From DV to NWJ" `:297-302` and "— Relabel" `:304-309`); McAllester–Stratos variance bound `:358`, mechanism/derivation `:346-355` ("The High-MI Barrier — Why"), cost/citation `:358-385` ("— Cost"); $f$-divergence Fenchel dual + DV/NWJ as KL instances `:411-430` (machinery on `:411-419`, DV/NWJ unification on `:421-430`; deferred to `divergence/div1`).

### Note (`mi1-bounds-note.html`)
- Density ratio as unifying view — now also illustrated on the deck via "The Critic Is a Classifier" (§01) `:25`
- MINE estimator bias `:31`
- McAllester–Stratos lower bound — estimator-agnostic two-sample-testing argument, complementary to the deck's DV-specific AEP/delta-method derivation, now split across "The High-MI Barrier — Why" and "— Cost" (§05) `:37`
- Toy bivariate Gaussian detail `:43`
- f-divergences and f-GAN connection — Fenchel-conjugate unification derived on the deck in "One Machine — KL Is the Tip of It" plus new "NWJ and DV — Same Conjugate" (§05); note trimmed to a pointer plus the f-GAN generative-modeling link and forward pointer to `divergence/` `:55`
- Why CLIP/InfoNCE is different from these `:62`

---

## mi2-infonce-clip.html — InfoNCE and CLIP (28 slides)

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:75, :86` |
| Motivation (preamble) | Why another bound? What we want from it | `:114, :125` |
| **01 — InfoNCE** | K-class softmax bounded by log K | `:144-193` |
| | Setup — 1 positive, K−1 negatives | `:145` |
| | **Theorem (InfoNCE bound)** | `:153, :155` |
| | Proof Sketch — Split the Loss (split 1/2: add/subtract log K, isolates term A/term B) | `:165` |
| | Proof Sketch — Bound Term A (split 2/2: Jensen bounds term A ≤ 0, concludes the bound) | `:174` |
| | Optimal critic = log-density-ratio | `:184, :186` |
| **02 — CLIP architecture** | InfoNCE at web scale | `:197-323` |
| | Two encoders, one space | `:205` |
| | Separable critic + symmetric loss | `:225` |
| | Positives on the Diagonal, Negatives Off (new: N×N CLIP grid diagram, diagonal=positive) | `:234` |
| | Each Row Is One InfoNCE Problem (new: row-softmax = one InfoNCE instance) | `:263` |
| | Is separable enough? (Mercer / UAT) | `:281` |
| | Why we live with the restriction | `:293` |
| | N×N similarity matrix (encoder + matmul) | `:303` |
| **03 — Zero-shot classification** | Reusing the contrastive head | `:327-374` |
| | CLIP as classifier | `:335` |
| | Why It Works — Score Is a Log-Ratio (split 1/2: $g^\top h \approx \log r$, drops the x-only constant) | `:347` |
| | Why It Works — Reduces to MAP (split 2/2: uniform prior ⇒ argmax reduces to MAP) | `:355` |
| | Prompt engineering | `:363` |
| **04 — Practice** | Bias, variance, batch size | `:377-419` |
| | Four bounds side-by-side | `:385` |
| | Why batch size matters | `:399` |

**Key:** InfoNCE bound `:157`; proof split across "Split the Loss" `:165-171` and "Bound Term A" `:174-181`; optimal critic = log-ratio `:186`; log K saturation `:158`; positives/negatives grid diagram `:234-260`; row-as-InfoNCE diagram `:263-278`; separable-critic justification (Mercer) `:284`; encoder evaluation $S_{ij} = g_i^\top h_j / \tau$ `:303`.

### Note (`mi2-infonce-clip-note.html`)
- InfoNCE proof + log K saturation — now a short pointer to the deck's §01 ("Proof Sketch — Split the Loss", "Proof Sketch — Bound Term A", "Optimal Critic = Log-Density-Ratio") which derives both in full across the split slides; note keeps only the original-references pointer (Oord 2018, Poole 2019) `:25`
- Temperature τ in CLIP `:30`
- Why symmetric loss `:37`
- CLIP zero-shot recipe — slide-side reasoning now split across "Why It Works — Score Is a Log-Ratio" and "— Reduces to MAP" (§03) `:44`
- Robustness / other zero-shot capabilities `:55`
- What CLIP doesn't do well `:61`
