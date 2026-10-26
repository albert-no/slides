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
