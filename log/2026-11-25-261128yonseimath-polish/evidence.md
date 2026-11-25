# Evidence register — append-only

Cutoff: 2026-11-25. This is a focused update to the approved draft, not a survey of all current AI mathematics. Versions/claims below are bounded to the cited source; no implied current community consensus. Figures not yet built are explicitly proposed. Slides records final assets, parameters and code paths in its work report; reviewer appends verification here.

## E01 — Author, baseline and scope
- Label: illustrative example / author-supplied intent.
- Sources: requests C01–C19; inherited original-job requests C24–C27 at baseline37757bb. Frozen main and note: talks/261128yonseimath/261128yonseimath.html and 261128yonseimath-note.html, 24 paired IDs. Existing leaf outline and root quick-lookup inspected.
- Claim: 25-minute Korean graduation talk, advanced middle-school audience, speaker an alumnus/current professor; authentic reflection emphasizes understanding mathematics verbally and intuitively. No invented incident or claim that AM–GM changed Albert's own life.
- Reuse: privacy/lectures/06-watermark/OUTLINE.md §§01–02 and trustworthy-ai lec11 S15–S20 already cover the formal mechanism; adapt concepts, do not import a technical lecture. AM–GM is assumed known; reuse log-concavity geometry, not elementary rectangle teaching. No new prerequisite or tech supplement.

## E02 — IMO 2025
- Label: published result (official developer report).
- Source: Thang Luong and Edward Lockhart, “Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad,” Google DeepMind, 2025-07-21, section “Breakthrough Performance at IMO 2025 with Gemini Deep Think.” https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
- Verified claim: advanced Gemini Deep Think, 35/42 points, five of six problems, gold-medal standard under IMO coordinator grading. C02's requested heading is “IMO 2025 Gold Medal”; keep “금메달 수준 · Gemini Deep Think” with the score so it is not an award claim about every chatbot. No solved/unsolved grid.

## E03 — Navier–Stokes announcement and original vortex image
- Label: published result (dated announcement); source illustration, not independently measured flow or a proof.
- Sources: OpenAI, “On the Navier–Stokes Millennium Prize Problem,” 2026-09-08, opening/result and vortex illustration: https://openai.com/index/navier-stokes-solution/ . Clay Mathematics Institute, “Navier-Stokes Announcement,” 2026-09-11, concluding paragraphs: https://www.claymath.org/news/navier-stokes-announcement/ . Both reopened Nov25.
- Claim: Navier–Stokes is a Millennium Prize Problem; OpenAI announced an AI-produced solution. Say “OpenAI의 해법 발표” rather than an invented prize award. Forced variants C/D and prize procedure are optional note context, not a verification diagram or a repeated caution on the main slide.
- Exact original light-mode asset, downloaded and visually inspected: https://images.ctfassets.net/kftzwdyauwt9/75EbpsuBOy5LbUgCppWXD1/88da8c19dcf76d6f4f8fd7485dcb6346/navier-stokes-light-master.png . 1254×1254, swirling blue/orange vortex, embedded labels “inward spiral” and “axial stretching.” This is a static source image, not an animation. Dark-mode alternative is not needed. Proposed local asset: talks/261128yonseimath/figs/navier-stokes-vortex.png.
- Do not redraw/animate a speculative solution, substitute an unrelated simulation, or revive the deleted verification flow. Citation identifies OpenAI and the date; retain image aspect ratio.

## E04 — Terence Tao: research exceeds problem solving
- Label: published result (author's expressed viewpoint, not an empirical theorem).
- Primary source: Terence Tao, “Math 2.0,” Caltech public lecture 2026-10-09, posted 2026-10-10. https://terrytao.wordpress.com/2026/10/10/math-2-0/ ; author's slides https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf . Physical PDF p16 (“Beyond problem-solving”), p18 (understanding links pure/applied problems), p25 (“Examples of ‘Math 2.0’ usage of AI”).
- Supported paraphrase: research is not exhausted by solving open problems; the surrounding concepts, insights, explanations and connections matter. AI can also help improve exposition and identify principles/methods/insights. Use a Korean paraphrase labelled “Tao의 관점 요약,” not quotation marks suggesting verbatim wording.
- Additional primary reference: “Mathematics in the age of AI,” ICM public lecture 2026-07-24, PDF pp19 and23 (goals beyond problem solving and complementary theory building), https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf . No need to add both citations to the main.
- Author's three questions in C04 are Albert's framing, not a three-item verbatim Tao quotation. Do not cite the guest essay “After Math” as if Tao authored it; it is by Silvia De Toffoli and Eamon Duede. No assertion that AI cannot research or invent ideas.

## E05 — ChatGPT / autoregressive next-token modelling
- Label: published result (provider's explanation and primary research).
- Source: OpenAI, “How ChatGPT and our foundation models are developed,” section “What is ChatGPT and how does it work?”, checked Nov25 (page says updated28 days ago). https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-foundation-models-are-developed . Supports learning contextual patterns from large datasets and predicting continuations; tokens may be whole words, parts, or punctuation.
- Primary research context: Brown et al., “Language Models are Few-Shot Learners,” NeurIPS 2020, abstract and §2, https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf . GPT-3 is autoregressive. Do not identify it as the current ChatGPT model or describe this as the entirety of post-training/tool use.
- Main wording: “ChatGPT 같은 LLM은 문맥에 맞는 다음 단어의 확률분포를 예측한다”; “대량의 글에서 문맥과 단어의 통계적 패턴을 배운다.” Explain actual token granularity briefly in the note. In open-ended continuation there is no single prescribed correct next word, not “all factual questions lack answers.” “세상의 모든 글” is not literally a complete training corpus, nor is the model a frequency lookup table.

## E06 — Soft green-list watermark and its motivation
- Label: published result; specific demo probabilities are illustrative examples.
- Source: Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein, “A Watermark for Large Language Models,” ICML2023, PMLR202:17061–17084, introduction, §2, §3.1 Algorithm2 and quality discussion. https://proceedings.mlr.press/v202/kirchenbauer23a.html ; https://proceedings.mlr.press/v202/kirchenbauer23a/kirchenbauer23a.pdf .
- Claim: pseudorandom context-dependent candidate partition; gently upweight green candidates, normalize and sample, rather than ban all red tokens. Detection reconstructs groups and counts selected green tokens. Always forcing green can exclude the contextually appropriate token and hurt quality; soft bias reduces this problem, not guarantees zero quality loss.
- Scope: a generation-time scheme, not a detector of every AI model. Half the vocabulary is not necessarily half the probability mass at every context. Colour is our explanatory overlay, absent from emitted text. The partition must be reproducible from context/rule, not new private randomness unrecoverable by the detector. Do not imply a secret key is part of this specific original algorithm.
- Intro motivation: undisclosed/uncritical AI use in contexts expecting human writing; cheating/spam/disinformation are discussed in the paper. Our 과제/후기/기사 examples are hypothetical, not sourced incidents/statistics. No legal-compliance discussion needed.
- Toy distribution retained if used: four candidates .40,.30,.20,.10, first/fourth green. Multiplying green weights by1.5 then dividing all by1.25 yields .48,.24,.16,.12. Green mass .50→.60, red remains positive. Any alternate values require reported calculation, not live-model claims.

## E07 — DGmark site as animation reference, not method attribution
- Label: published source illustration / proposed original teaching adaptation.
- Primary project site: Hong and No, dgMARK: Decoding-Guided Watermarking for Diffusion Language Models, ICML2026, https://dgmark-watermarking.github.io/ , “Decoding-guided Watermarking for dLLMs” / “Existing Watermarking Schemes.”
- Inspected actual GIF frames: https://dgmark-watermarking.github.io/static/images/existing_wm.gif (35 frames) and https://dgmark-watermarking.github.io/static/images/dgmark.gif (290 frames). First shows prefix → hash → red/green candidates → bias/selection; second shows an accumulating coloured-text comparison with arbitrary unmasking order.
- Adapt the large token/word visual and accumulating sentence, but generate strictly left-to-right using E06. Do not copy the diffusion order, its “without altering probabilities” claim, whole-word tokenization as a real ChatGPT trace, or its simplified +/-delta probability labels as the exact algorithm.
- Proposed original demo source: talks/261128yonseimath/figs/watermark-demo.js (or equivalent deck-local implementation reported in work-r1). Record sentence, candidate tables, context partition, probability weights and deterministic demonstration schedule/seed. A short Korean sentence such as “오늘 나는 친구와 공원에서 산책을 했다.” is suitable; natural sentence choice remains slides' judgment.
- Main must show repeated candidate grouping and slight upweighting, selected tokens including at least one red example, accumulation, completion hold and restart. Any short output is a staged mechanism illustration, not a statistical detection experiment or a claimed sampled ChatGPT response. Loop during this slide only, with pause/restart and a representative static print/reduced-motion fallback. Verify at least two cycles and re-entry. Author C11 expressly permits this local loop.

## E08 — Invisible image-parity teaching example
- Label: our calculation / illustrative example; not a deployed robust watermark or a natural-image probability theorem.
- Proposed source image: NASA Goddard Space Flight Center, Blue Marble2002, source page https://svs.gsfc.nasa.gov/30614 (published2015-07-21, updated2024-10-10), image download “blue_marble_modis_north_america_print.jpg”,1024×574. It is a satellite-observation composite, not a single photograph. Credit NASA GSFC and identify our grayscale/parity processing.
- Setup: prepare one 8-bit grayscale image at the final stored dimensions, then copy it and replace every even intensity x by x+1; odd values unchanged. For x∈{0,…,255}, the result is odd and stays in range; maximum difference1. Save losslessly. Do not resize, JPEG-recompress, or re-quantize the stored marked image after applying parity. Normal browser scaling is presentation only, not the object whose parity is counted.
- Exhibit compares these two images at identical size. Report actual before/after odd fraction and maximum difference from file bytes; do not assume the original fraction is exactly50%. Main point: a change can be visually subtle yet leave a machine-readable pattern.
- “All pixels odd” is possible in unmarked/computer-generated images; it is not logically impossible or proof of AI authorship. Under an ideal independent unbiased parity model, all-odd over N pixels has probability2^-N, but natural image pixels need not satisfy that model. Keep this modelling qualification in optional notes rather than an advanced probability digression.
- It is fragile to ordinary editing and easy to remove if known; it illustrates invisibility, not security, robust provenance or guaranteed imperceptibility for every image/viewer. No production watermark claim.
- Proposed generator: talks/261128yonseimath/figs/generate-figures.py (existing deck-local generator, extended by slides); proposed outputs image-original-gray.png and image-all-odd.png. Record input asset URL/hash, conversion rule and stored dimensions in work-r1; test oddness, max difference and visual similarity. If the selected source cannot be used, return a concrete equivalent with provenance rather than an unsourced screenshot.

## E09 — Coin example and link to detection
- Label: our calculation, inherited and rechecked analytically from original evidenceE05/E21.
- Independent Bernoulli(1/2),100 trials; K≥70 upper tail, not “exactly70.” sum(comb(100,k),k=70…100)/2^100 =0.00003925069822796835, or0.003925069822796835%. Keep 0.0039% on the plot. The question asks if70 can occur; answer yes, but rare, on the following slide.
- Existing code: talks/261128yonseimath/figs/generate-figures.py, coins-100.svg (70filled/30hollow) and binom-pmf.svg (exact PMF). Plot source parameters and invariant unchanged unless recorded.
- This is a simplified fair-independent coin analogy, not an exact calibration theorem for arbitrary text or a posterior probability that a text is AI-written. Real-text context repetition/dependence belongs in optional note detail; do not restore the deleted limitation slide.

## E10 — AM–GM growth interpretation and log/Jensen
- Label: published mathematical result plus our illustrative interpretation/calculation.
- Source: Boyd and Vandenberghe, Convex Optimization,2004, §3.1.8–3.1.9, printedpp77–78: Jensen's inequality and log-derived geometric/arithmetic mean inequality. Author PDF https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . Source was directly checked in original draft evidenceE18; same result, no new theorem.
- Familiar multiplicative-growth interpretation: take two positive growth factors a,b from the same starting size; replace both by m=(a+b)/2. Original final factor ab is at most m². At fixed arithmetic mean, more unequal factors lower the product. For a=m-d,b=m+d and |d|<m, ab=m²-d². This is a two-step deterministic comparison, not investment advice or a general recommendation to remove every kind of uncertainty.
- Main does not reteach AM–GM or use numeric rectangles; symbolic two-step growth paths make the practical meaning visible. Candidate natural wording: “평균 성장배율이 같아도, 들쭉날쭉하면 덜 성장한다.” Keep the fixed-average/two-positive-factors setup visible. No claim about historical origin or an attributed famous quotation.
- Follow directly with log((a+b)/2) ≥ (1/2)log a+(1/2)log b for a,b>0. Call log “concave.” Curve/chord picture has symbolic labels a,b,(a+b)/2; no on-slide2,8,4,5. Internal illustrative geometry may retain a=2,b=8 on[1,9]: chord midpoint ln4 below curve ln5, with f''(x)=-1/x²<0 throughout. Cite as schematic geometry, not data.
- Existing generator generate-figures.py / log-chord.svg may be adapted. Do not introduce a full Jensen theorem, proof chain, expectation notation or another formula lesson. One spoken connection via monotonicity/product rule suffices in notes.

## E11 — Speaker's closing perspective
- Label: author-supplied viewpoint / illustrative teaching synthesis, not measured research finding.
- Sources: inherited original C24–C27 and current C06,C16–C19. Mathematical meaning/intuition mattered in Albert's life; techniques were useful too. Now end with understanding mathematics intuitively and applying that intuition to real problems. AI may contribute ideas as well as implementation; avoid the “AI only computes, humans alone understand” dichotomy.
- Explicitly deleted autobiographical phrase need not be retained as mandatory speech. Keep warmth and congratulations; do not fabricate childhood stories, private achievements or exact dates of attendance.
