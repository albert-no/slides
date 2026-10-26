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
