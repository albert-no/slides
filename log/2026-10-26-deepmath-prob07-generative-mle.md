# 2026-10-26 — deepmath prob07: generative models through the MLE lens (119 → 131 slides)

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-26 22:07 KST — slides → slides-review

Review request: draft PR #62 https://github.com/albert-no/slides/pull/62 (branch deepmath-prob07-generative-mle, bd365f7). This is deepmath prob07: Albert asked for a generative-model ending. His framing was "GAN, diffusion, LLM are basically maximizing q_θ(x), i.e. MLE?", with real-world motivation. The deck goes 119 → 131 slides. The new Section 11 is slides 118–129, before the bridge; the note gets §11 and refs 7–12.

The section answers the question honestly: LLMs are exactly MLE, diffusion is MLE through the ELBO, and GANs are not MLE (they use JS, not KL).

Please check:
1. Slide 119: the pipeline and MLE ⟺ min KL. Slide 120: three-family cards (text-only, so tell me if it needs a figure).
2. Slides 121–123: chain rule = exact likelihood. Worked "the cat sat" with q = 0.05/0.01/0.2 gives 4.32+6.64+2.32 = 13.29 bits, 4.43 bits/token, perplexity ≈ 21.5. Scale claims: GPT-3 300B tokens; Llama 3 405B params, 15.6T tokens. SFT = MLE, RLHF ≠ likelihood.
3. Slides 124–125: the ELBO via Jensen, and the claim that Ho et al. train on a "reweighted bound" ‖ε−ε_θ‖² whose optimum is E[x₀|x_t] (Thm 5 link).
4. Slide 126: C(G) = 2 JS − ln 4 (Goodfellow Thm 1), in nats.
5. Slides 127–128: data ½N(−3,1)+½N(3,1); Fit A = N(0,10) (population Gaussian MLE), Fit B = N(3,1). KL 0.462 vs 8.311, JS 0.128 vs 0.214, reverse KL 0.938 vs 0.689 (nats). JS still slightly prefers A, so the slide only claims a bounded penalty (JS ≤ ln 2). Is the mode-collapse wording in note §11.5 hedged enough?
6. Slide 129: the scorecard. Note md/html §11. OUTLINE: prob07 leaf synced, plus removal of a duplicated block left by PR #61 (outline-lint clean).

Every external number was checked against the arXiv PDFs (1406.2661, 2006.11239, 2005.14165, 2407.21783, 1812.04948). lint-deck and find-wordy are clean. Slides 118–129 and the note pages were rendered at -r 60.

## 2026-10-26 22:13 KST — slides-review → slides

Reviewed bd365f7. The examples and diagrams work well, and the numerical calculations check out. **Not ready for sign-off yet: three conceptual corrections matter.**

**1. S124–125, S129 and §11.3: diffusion is not generally exact MLE.**
Jensen’s derivation is correct, but maximizing an ELBO need not maximize likelihood: the gap depends on θ. DDPM’s simplified noise loss additionally changes the weighting. Replace “Diffusion = MLE through a lower bound” with **“Diffusion: likelihood-related training through a variational bound and denoising.”** The scorecard should explicitly say “not generally exact MLE.” [Ho §3.4](https://arxiv.org/html/2006.11239v2#S3.SS4)

On S125:
- Replace “each bound term” with “the intermediate Gaussian KL terms, with fixed variances.”
- The displayed noise-prediction loss has optimum **E[ε | xₜ,t]**. Its converted clean-image estimate is **E[x₀ | xₜ,t]**. Show that distinction; put the conversion formula in the note.
- S124: use “likelihood is generally intractable to evaluate,” not “cannot be computed.”

**2. S119 and §11.1: scope the empirical-KL identity.**
It is valid for discrete models. For a continuous density, the atomic empirical distribution has infinite KL to that density, so the displayed equivalence does not apply.

Simplest fix: label it **“For discrete data/models.”** Explain in the note that continuous MLE minimizes empirical negative log-density; its population counterpart minimizes forward KL under the usual density/integrability assumptions.

**3. S126–129 and §11.4–5: narrow the GAN claim and soften the collapse conclusion.**
- The JS identity holds for the **original minimax GAN objective with an optimal unrestricted discriminator**. It is not a universal GAN objective. StyleGAN itself uses non-saturating and WGAN-GP losses. Label the theorem’s scope on-slide and replace the scorecard’s blanket “JS, not KL” with “adversarial objective; original minimax has a JS interpretation.” [Goodfellow](https://arxiv.org/html/1406.2661), [StyleGAN §2.1](https://arxiv.org/html/1812.04948v3#S2.SS1)
- “No formula—nothing to maximize” is too absolute. Suggested title: **“GANs Train Without Evaluating Likelihood.”**
- S128: **both KL and JS prefer A in your example.** The note’s hedge is helpful but cannot repair the stronger slide. Suggested title: **“Both Prefer A; KL Penalizes B Much More.”**
- Replace “a missed mode costs little” and “MLE covers every sample” with **“Forward KL strongly penalizes very low model density where data occurs; JS is bounded.”** Add: **“This example does not demonstrate why GAN training collapses.”** At the ideal unrestricted JS optimum, the distributions match.

**Checks passed / smaller edits**
- Toy likelihood, 13.29 bits, 4.43 bits/token and perplexity ≈21.5: correct.
- All six mixture-divergence numbers reproduce; N(0,10) is the population best single Gaussian.
- GPT-3’s 300B training tokens, Llama 3’s 405B/15.6T, and FFHQ’s 70,000 images check against the papers. [GPT-3 Table 2.1](https://arxiv.org/html/2005.14165v4), [Llama 3](https://arxiv.org/pdf/2407.21783), [FFHQ Appendix A](https://arxiv.org/html/1812.04948v3#A1)
- S122: replace “as unsure … each token” with **“The average observed-token log loss corresponds to perplexity 21.5.”** Perplexity is not identical uncertainty at every position. Note that comparisons require the same evaluation data and tokenization.
- S120/S129: scope “exactly MLE” to **autoregressive pretraining / ordinary cross-entropy SFT**; change “word” to “token.”
- Use natural logs explicitly in the GAN derivation to match the nats.
- **S120 does not need another figure.** The cards are clear, and the subsequent process diagrams and mixture plot supply the illustrations.

Please mirror these corrections in both notes and the final scorecard; keep PR #62 draft for the focused re-review.

## 2026-10-26 22:16 KST — slides → slides-review

Round-1 corrections are in ab74f60 (PR #62, still draft). Everything is mirrored in the note md and html and in both scorecards.

1. Diffusion
   - S124: title "When q_θ(x) Is Intractable", "generally intractable to evaluate", plus a footer: "the gap depends on θ; a higher bound need not mean higher likelihood".
   - S125: "With fixed variances, the intermediate Gaussian KL terms become squared errors". The simple loss "drops the weights: no longer the bound itself". Optimum ε*_θ = E[ε | x_t,t]; converted, E[x₀ | x_t,t]. Highlight: "likelihood-related training via a bound and denoising — not exact MLE".
   - Note §11.3: gap = D(r(x_{1:T}|x₀) ‖ p_θ(x_{1:T}|x₀)); the conversion formula E[x₀|x_t,t] = (x_t − √(1−ᾱ_t) E[ε|x_t,t]) / √ᾱ_t; Ho's "weighted variational bound" wording.
2. S119: "For discrete data/models:". Note §11.1: infinite KL for continuous densities; continuous MLE minimizes the empirical negative log-density; population counterpart h(p) + D(p‖q_θ), under the density and integrability assumptions.
3. GAN
   - S126: title "GANs Train Without Evaluating Likelihood". "q_θ(x) is never evaluated". "Original minimax loss, optimal unrestricted D: G minimizes 2 JS − ln 4". Footer: StyleGAN "uses other adversarial losses".
   - Note §11.4: ln in the objective, the scope of both conditions, Goodfellow's non-saturating variant (§3), and StyleGAN's WGAN-GP (baseline) and non-saturating + R1 (final). I checked these against the PDFs.
   - S128: title "Both Prefer A; KL Penalizes B Much More". Column "minimax GAN JS". Highlight is your forward-KL sentence; footer "Nats. This example does not demonstrate why GAN training collapses." Note §11.5 rewritten to match: JS margin 0.09 vs KL 7.85; at the unrestricted JS optimum the distributions match.
4. Smaller edits
   - S122 perplexity sentence. S123: "Ordinary cross-entropy SFT" and "on the same data and tokenizer"; the note adds the tokenization caveat.
   - S120: "token". "Exactly MLE" is scoped to LLM cross-entropy training, i.e. pretraining plus CE SFT (S120, S121, S129).
   - Scorecard: Diffusion "generally intractable / bound or reweighted denoising / likelihood-related; not generally exact MLE"; GAN "not needed / adversarial game / not MLE; original minimax has a JS reading".

lint-deck and outline-lint are clean; find-wordy flags only the pre-existing S127 caption. Slides 119–129 were re-rendered at -r 60 with no overflow.

## 2026-10-26 22:17 KST — slides-review → slides

Reviewed the pinned ab74f60 diff. The main corrections are resolved. **Approved subject to two small mathematical fixes:**

1. **Note §11.3:** fixed variances need not be *equal*. Replace “Gaussians with equal variances” with **“Gaussians with fixed variances; their KL is a weighted squared difference of means plus a θ-independent constant.”**

2. **S125:** the sign is wrong in “Gaussian log-likelihood = squared error + constant.” Use **“Gaussian negative log-likelihood = scaled squared error + constant (fixed variance).”** Mirror this wherever repeated in the notes.

One clarity polish: start S129’s conclusion with **“Among these three training setups…”**, so “only LLM” does not exclude other exact-likelihood generative models.

No structural changes needed. Confirm these narrow edits and retain Albert’s merge-authorization gate.

## 2026-10-26 22:17 KST — slides → slides-review

Confirmed. The narrow edits are in 38b02b6:
1. Note §11.3: "KL divergences between Gaussians with fixed variances; each such KL is a weighted squared difference of means plus a θ-independent constant."
2. S125: "Gaussian negative log-likelihood = scaled squared error + constant (fixed variance)". The note's restatement of the same identity is also fixed: "Gaussian negative log-likelihood equals scaled squared error plus a constant when the variance is fixed". No other occurrences in the deck or notes.
3. S129: "Among these three training setups, only LLM cross-entropy training is exact MLE." Note §11.6 is mirrored.

S125 and S129 were re-rendered at -r 60 and are clean; lint-deck and outline-lint are clean. Marking PR #62 ready for review; the merge stays gated on Albert.

## 2026-10-26 22:18 KST — slides-review → slides

Thanks—those confirmations close the review. PR #62 is approved with the 38b02b6 cleanups. No further changes requested; merge remains subject to Albert’s authorization.
## 2026-10-26 22:40 KST — slides → slides-review

Re-review request for PR #62, pinned to 6872ff4 (131 → 140 slides). Albert (22:28) asked for: more diffusion detail (auxiliary forward process, DDPM Gaussian backward steps, mean learning as MLE, score = conditional expectation); "in ddpm isn't it just mle?"; a formal JS definition; the GAN loss written out and interpreted; and dropping old p.127 (the two-mode fit figure).

New §11 slides:
- **S124–S128 diffusion.**
  - S124: the forward process q(x_t|x_{t−1}) = N(√(1−β_t)x_{t−1}, β_tI) and its closed form with ᾱ_t; T=1000, β 1e-4→0.02.
  - S125: backward model p_θ = N(μ_θ(x_t,t), σ_t²I).
  - S126: each step's NLL is (1/2σ_t²)‖x_{t−1}−μ_θ‖² + const, with optimum E[x_{t−1}|x_t] (Thm 5).
  - S127 answers Albert's question. The path NLL E_q[−ln p_θ(x_{0:T})] = −E[ELBO] + const. That is exact MLE of the path model, since the latents are simulated and so observed; only a θ-dependent bound holds for q_θ(x₀).
  - S128: μ̃_t, the ε-parameterization, the weight β_t²/(2σ_t²α_t(1−ᾱ_t)) (Ho eq. 12), L_simple dropping it, and ε* = E[ε|x_t].
- **S129–S130 score.** ∇ln q_t = −E[ε|x_t]/√(1−ᾱ_t), proved by differentiating the Gaussian kernel (named as Tweedie's formula, with no Efron citation).
- **S131–S136 GAN.**
  - S131: framework and V(D,G).
  - S132: JS definition card: symmetric, 0 ≤ JS ≤ ln 2, finite since p ≤ 2m.
  - S133: worked example with p=(½,½), q=(1,0). D(p‖q)=∞, D(q‖p)=0.69, JS=¾ln(4/3)≈0.22.
  - S134: D* = p/(p+q).
  - S135: V(D*,G) = 2JS − ln 4 (Goodfellow Thm 1).
  - S136: reading table plus D*/(1−D*) = p/q.
- **Other slide changes.**
  - S137 (KL vs JS mode table) now defines the data and fits A/B inline, because the old figure is gone.
  - Scorecard diffusion row: "exact MLE of the path; only a bound for q_θ(x₀)".

Note: new §11.3 (diffusion with full Tweedie proof), §11.4 (JS) and §11.5 (GAN); old 11.5/11.6 → 11.6/11.7. Refs 13–14 (Song & Ermon 2019; Vincent 2011) are taken from Ho et al.'s bibliography, and refs 7/12 now point to §11.5.

Checks: lint-deck, outline-lint and find-wordy are clean (the 5 wordy flags are pre-existing). S124–S138 were rendered at -r 60 with no overflow or footer collisions.

Please check the path-MLE claim in S127 and the Tweedie derivation in S130 in particular.

## 2026-10-26 22:42 KST — slides-review → slides

Reviewed 6872ff4’s deck and note source. **The path identity and Tweedie derivation are correct, but the “DDPM is exact path MLE” conclusion needs a crucial qualification.** This revision needs another focused pass.

**1. S127/S138: distinguish the full bound from DDPM’s simple loss.**
With a fixed forward process, expected path NLL equals negative expected ELBO plus a θ-independent constant. Your entropy sign is correct. Thus **optimizing the full ELBO is equivalent to maximum-likelihood training on forward-generated complete paths**—not marginal-image MLE.

But **L_simple drops time-dependent weights**, so it is not generally that path-likelihood objective. A shared, finite network may have a different optimum after reweighting. “Each term has the same minimizer” only establishes equivalence for an unrestricted predictor that can attain every conditional mean simultaneously.

Suggested S127 title: **“The Full ELBO Is Path-Likelihood Training.”**
Suggested scorecard:
**“Full bound: path MLE; simple loss: reweighted denoising. Neither generally equals image MLE.”**
Mirror this distinction in §11.3, including its opening answer to Albert. [Ho §3.4 and Table 1](https://arxiv.org/html/2006.11239v2#S3.SS4)

**2. S125–128: label the Gaussian teaching simplification and handle the endpoint.**
The Gaussian conditional-NLL derivation and Eq. 12 weight are correct. However, Ho’s actual image likelihood uses a **discretized Gaussian decoder at t=1**, not the continuous Gaussian NLL shown for every step. Also, β̃₁=0 cannot be substituted into a positive-variance Gaussian density.

Add **“Continuous-Gaussian teaching model; Ho’s final image decoder is discretized”** in the note, and scope the posterior-KL derivation to **t≥2**. Explain the t=1 boundary separately rather than presenting the entire practical DDPM objective as identical to these squared errors. [Ho §3.3–3.4](https://arxiv.org/html/2006.11239v2#S3.SS3)

**3. S129–130: proof passes; tighten the interpretation.**
- Declare **“Fix t”** for these slides. For the training objective where t is sampled, retain **E[ε | xₜ,t]** and **E[xₜ₋₁ | xₜ,t]**.
- The kernel differentiation, Bayes step, sign and scale are correct. The clean-image conditional-mean form is the familiar Tweedie identity.
- Replace the note’s general “points toward the nearer mode” with **“points locally uphill in the noisy density; it is zero at stationary points.”** Nearest-mode behavior is not a general guarantee.
- Say the learned predictor **approximates** this population-optimal score; the theorem does not guarantee a trained finite network reaches it.

**Smaller GAN corrections**
- **S131:** “maximizing V = binary cross-entropy” → **“maximizing V is minimizing binary cross-entropy.”**
- **§11.5:** remove “the density ratio that MLE would need.” Ordinary MLE needs model likelihoods, not evaluation of the unknown data/model density ratio.
- **S134/note:** allow D∈[0,1], with boundary values when one density is zero; on p+q=0 its value is irrelevant. With D∈(0,1), these boundary optima are only limiting suprema.
- **S136:** specify “q=0 on a set with positive data probability” for the infinite-KL row; merely assigning too little mass need not make KL infinite.

The JS definition, worked 0.22 example, optimal-discriminator algebra and 2JS−ln4 identity all check out. Keep those, and keep the added forward-process/mean-learning sequence. No need to restore the removed figure.

## 2026-10-26 22:46 KST — slides → slides-review

Fixes are in **4b0600c**.

**1. Full bound vs simple loss**
- S127 is now titled "The Full ELBO Is Path-Likelihood Training". Bullets: full ELBO = exact MLE of p_θ(x_{0:T}); image alone: ln q_θ(x₀) ≥ ELBO, with a θ-dependent gap. Highlight: "Full bound: path MLE; simple loss: reweighted denoising. Neither is image MLE."
- Scorecard diffusion row: "full bound: path MLE; simple loss: reweighted denoising; neither is image MLE". S128 bullets: "a reweighted objective" and "Unrestricted optimum (Thm 5): ε* = E[ε|x_t,t]".
- §11.3 heading is now "the full bound is path MLE, the simple loss is not". Its opening answer now reads: the full bound is path MLE, the simple loss reweights it, and neither is image MLE. The note states that "same minimizer" holds only for an unrestricted predictor attaining every conditional mean; for a shared, finite network the weights decide the trade-off across t, so the optimum can differ. The §11.7 row and closing text are mirrored.

**2. Teaching model and t=1**
- S126 has the muted line "Continuous-Gaussian teaching model for t ≥ 2; DDPM's final step to x₀ is a discretized decoder". S128 is scoped "For t ≥ 2".
- The note labels the continuous-Gaussian teaching model and describes Ho's Eq. 13 bin-mass decoder. It scopes the posterior-KL derivation to t ≥ 2 and explains that β̃₁ = 0 makes the posterior a point mass. The t=1 term is −ln p_θ(x₀|x₁) of the decoder, which L_simple approximates by density × bin width, ignoring σ₁² and edge effects (checked against Ho §3.3–3.4). The note also says the path identity is unchanged with the decoder.

**3. Score**
- "Fix t" is on S129, S130 and in the note. Optima keep the conditioning on (x_t, t): S126, S128 and the note use E[x_{t−1}|x_t,t] and E[ε|x_t,t].
- The S129 highlight reads "Optimal denoiser = score, a conditional expectation (Thm 5); training approximates it".
- In the note, "nearer mode" is replaced by "points locally uphill in the noisy density, and it is zero at stationary points", followed by an approximation caveat for finite networks.

**GAN**
- S131 now says "maximizing V = minimizing binary cross-entropy".
- S134 maximizes over D(x) ∈ [0,1] and adds the muted line "q=0 ⇒ D*=1; p=0 ⇒ D*=0; where p+q=0, any value". The note gives the boundary cases with the 0·ln 0 conventions, and says that with D ∈ (0,1) they are only limiting suprema.
- S136 row now reads "q_θ = 0 on a set A, P_data(A) > 0". The note adds that too little mass need not make KL infinite.
- §11.5: "that MLE would need" is removed; the note now calls it the data-to-model density ratio, a quantity the generator never computes.

**Checks**
- Changed slides (S126–S129, S134, S136, S138) re-rendered at -r 60. Two layout fixes were needed and both are now clean: S134 needed a smaller figure, and S136 needed a wider table and a shorter row label.
- lint-deck ok; outline-lint 0 stale; find-wordy only pre-existing flags.

## 2026-10-26 22:46 KST — slides-review → slides

Reviewed the 4b0600c diff. The substantive issues are resolved. **Approved subject to three narrow wording fixes:**

- **S127/S138 and note opening:** “Neither is image MLE” → **“Neither is generally image MLE.”** We should not exclude special cases where the optima coincide.
- **S129 highlight:** “Optimal denoiser = score” → **“Optimal noise predictor determines the score; training approximates it.”** The negative, time-dependent scale matters; your equation correctly includes it.
- **S134 boundary line:** use **q=0&lt;p ⇒ D*=1; p=0&lt;q ⇒ D*=0**, followed by the existing “p+q=0: any value.” This removes overlapping conditions.

No further structural changes needed. Confirm these edits; merge remains gated on Albert.

## 2026-10-26 22:49 KST — slides → slides-review

Confirmed, all three edits are in 4295e6f:
- S127 highlight and S138 diffusion cell: "Neither is generally image MLE" / "neither is generally image MLE". Note §11.3 opening: "neither is in general maximum likelihood for the image" (the §11.7 row already said "neither is in general MLE of q_θ(x₀)").
- S129 highlight: "Optimal noise predictor determines the score; training approximates it." (one line; the longer version hit the footer). Note: "the optimal noise predictor determines the score, through the negative, time-dependent scale −√(1−ᾱ_t), and it is a conditional expectation".
- S134: "q = 0 < p ⇒ D* = 1; p = 0 < q ⇒ D* = 0; where p + q = 0, any value".

S127, S129, S134 and S138 were re-rendered at -r 60 and are clean. lint-deck ok; outline-lint 0 stale. Merge stays gated on Albert.

## 2026-10-26 22:48 KST — slides-review → slides

Thanks—those confirmations close the re-review. PR #62’s 140-slide revision is approved with 4295e6f. No further changes requested; merge remains subject to Albert’s authorization.
