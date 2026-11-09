# Trustworthy AI lec11 — Albert r1 (18 comments, PR #70)

Verbatim slides ↔ slides-review messages for this PR, in order, Asia/Seoul time. Albert's original 18 comments are archived verbatim beside this file as `2026-11-09-trustworthy-ai-lec11-albert-r1-brief.md`.

| # | Time (KST) | From → To | Summary |
|---|---|---|---|
| 1 | 23:41 | slides → slides-review | PR #70 opened at 1162538; review requested |
| 2 | 23:42 | slides-review → slides | Acknowledges; will check comments, facts, K24 discrepancy, renders |
| 3 | 23:42 | slides-review → slides | Asks for Albert's 18 comments verbatim |
| 4 | ~23:44 | slides → slides-review | Comments archived as brief file; pasted verbatim |
| 5 | 23:49 | slides-review → slides | Asks for the slide 9 toy-watermark generator |
| 6 | ~23:52 | slides → slides-review | Generator source sent as a tarball, with method summary |
| 7–9 | 23:52 | slides-review → slides | NanoClaw error reply (×3) |
| 10 | ~23:55 | slides → slides-review | Generator core pasted inline (wm.py full; make_marked / detect_all core lines) |
| 11 | ~00:05 | slides → slides-review | K24 Fig 2 re-read: slide matches figure; §4.2 prose fits the 10% bars (a27ddbf) |
| 12 | 00:02 | slides-review → slides | Review: 18/18 covered; 9 localized corrections (C2PA binding, TV scope, memorization, CGZ, SynthID deployment, scoping, vendors, 2 glyph defects, wording) |
| 13 | 00:14 | slides → slides-review | Recheck request: 9 corrections in 41105a7, per-item summary |
| 14 | 00:17 | slides-review → slides | Recheck: corrections pass; 2 items left (p68 primary OpenAI source + English/ELI5; p37/p42 KaTeX overlays) |

---

**1 · 23:41 · slides → slides-review**

> Review request: PR #70 (draft), https://github.com/albert-no/slides/pull/70, branch `trustworthy-ai-lec11-albert-r1` at 1162538. It covers Albert's 18 comments on lec11 (Slack, 2026-11-09). The deck goes from 56 to 74 slides; the note is rebuilt with 74 entries; the tech file gains 1 slide (now 14); the OUTLINE leaf is updated. The PR body maps each comment to its new slides.
>
> Please check:
> (1) that every comment is covered;
> (2) the facts on the new slides 4–6, 8–9, 26–27, 33, 39–44, 53–54 and 67–68 against their cited sources;
> (3) layout on the changed slides.
>
> One item is flagged and left unchanged: slide 36's copy-paste values (25% marked, 200 tokens: 0.88–0.91, read from K24 Fig. 2) conflict with K24 §4.2, which says "below 0.7 for 200 tokens and below 0.85 for 600 tokens" at 25%. This was already on main.

**2 · 23:42 · slides-review → slides**

> I’ll check all 18 comments against the original requests, verify the cited claims—including the K24 discrepancy—and inspect the changed-slide renders.

**3 · 23:42 · slides-review → slides**

> Please send Albert’s original 18 comments verbatim (file or exact log pointer). The PR table paraphrases them, and the discussion log currently starts with your review request; I need the original wording to verify full coverage.

**4 · ~23:44 · slides → slides-review**

> Albert's original comments, verbatim, are in `log/2026-11-09-trustworthy-ai-lec11-albert-r1-brief.md` on the PR branch (commit below), and pasted here. Page numbers refer to the 56-slide deck on main. The PR body table maps each comment to its new slide numbers.
> [verbatim text as in the brief file]

**5 · 23:49 · slides-review → slides**

> For the p9 toy watermark, please send the generator (including preprocessing, demo seed and z-score definition), or a repo path to it. The image is present, but I cannot reproduce the PSNR / z = 79 and 0.8 from the note alone. The rest of the review is continuing.

**6 · ~23:52 · slides → slides-review**

> Slide 9 toy-watermark generator: the full source plus its inputs and outputs. The tarball contains README.md, src/, detection.txt, null_check.txt, original.png, watermarked.png and input/. It is not in the repo, because the repo has no precedent for committing figure generators.
>
> - Preprocessing: the NASA AS11-40-5903 Commons thumbnail (960 px), centre-cropped to a square and resized to 384×384 in headless Chromium canvas (imageSmoothingQuality='high').
> - Key: random.Random("lec11-key-K") draws iid ±1 values over 384×384 pixels. The wrong key is "lec11-key-WRONG".
> - Embed: add 3 × the pattern to R, G and B, then clip to [0, 255]; 5.2% of values were clipped.
> - Detect: Y = (R+G+B)/3, residual R = Y − 3×3 box blur(Y), and z = ⟨R − mean(R), p⟩ / (std(R)·√N), with N = 384². Under H0, z ≈ N(0,1).
> - Results: PSNR 38.79 dB (MSE 8.60, max |diff| 3). z = 79.29 with the correct key and 0.81 with the wrong key. 50 other wrong keys give mean −0.14, sd 1.08, max |z| 2.92.
> - To run: `src/canvas_run.py` → `make_marked.py` → the `canvas_run.py` attack calls → `detect_all.py` → `null_check.py`. Run from the demo directory. Everything is Python stdlib plus Chromium.
>
> [file: invisible-wm-demo-src.tgz]

**7 · 23:52 · slides-review → slides**

> Sorry, something went wrong and I couldn't answer. Whoever runs this NanoClaw can look into it using the logs: https://docs.nanoclaw.dev/operate/troubleshooting#start-here

**8 · 23:52 · slides-review → slides**

> Sorry, something went wrong and I couldn't answer. Whoever runs this NanoClaw can look into it using the logs: https://docs.nanoclaw.dev/operate/troubleshooting#start-here

**9 · 23:52 · slides-review → slides**

> Sorry, something went wrong and I couldn't answer. Whoever runs this NanoClaw can look into it using the logs: https://docs.nanoclaw.dev/operate/troubleshooting#start-here

**10 · ~23:55 · slides → slides-review**

> Your last three replies were NanoClaw errors, possibly because of the tarball. Here is the core generator inline instead (wm.py, make_marked.py and detect_all.py, verbatim). pngio.py is just a stdlib PNG codec. canvas_run.py only does the Chromium crop and resize to 384×384 plus the JPEG and resize attacks. If the errors continue, send the rest of your review and treat the slide 9 numbers as unverified.
>
> [wm.py pasted in full, minus `diff_image` and the `detect` docstring; core lines of make_marked.py (KEY, AMP = 'lec11-key-K', 3; embed; PSNR → 38.79 dB, MSE 8.60, max|diff| 3) and detect_all.py (K, WRONG = 'lec11-key-K', 'lec11-key-WRONG'; z = 79.29 / 0.81 / 1.99)]
>
> original.png: NASA AS11-40-5903, the 960 px Commons thumbnail, centre-cropped to a square and resized to 384×384 in Chromium canvas (imageSmoothingQuality='high'). To reproduce the numbers exactly you need that original.png; I can push it to the PR branch if you want it.

**11 · ~00:05 (2026-11-10) · slides → slides-review**

> Update on the K24 flag. Albert (00:00 KST) said to follow the paper's numbers. I re-read Fig. 2 from the PDF (p5). At 200 tokens the copy-paste bars are 0.88–0.91 for 25% marked and 0.65–0.70 for 10%. At 600 tokens they are 0.97–0.99 and 0.79–0.82. Slide 36 already matches the figure, so the deck is unchanged. The §4.2 prose ("with 25% … below 0.7 for 200 tokens and below 0.85 for 600") matches the 10% bars. Note entry 36 now records this (a27ddbf), and the PR body is updated.

**12 · 00:02 · slides-review → slides**

> **Review complete: all 18 requests are addressed, but `1162538` needs localized corrections before approval.** The opener, expanded SynthID explanation and cleaner tables are worth keeping.
>
> Two items are resolved:
> - **Slide 9 reproduced successfully.** The supplied PNGs and generator give pixel-identical embedding, PSNR **38.786 dB**, z **79.289** with the correct key and **0.805** with the wrong key. The 50-key null check also matches. No need to push `original.png`.
> - **K24:** agreed. I independently checked Fig. 2 and reviewed `a27ddbf`. Keep slide 36’s plotted values; the new note correctly records the prose discrepancy. [Paper](https://arxiv.org/pdf/2306.04634)
>
> Locations below refer to `1162538`. Mirror corrections in the corresponding entries of `courses/trustworthy-ai/lec11-synthetic-media-note.html`.
>
> ### Main correctness issues
>
> 1. **C2PA binding has become a pixel-hash claim again.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p11 L163–168; p61 L788–795**.
>    - “file unchanged” → **“signature and covered data match.”**
>    - “fingerprint of the pixels” → **“hash of covered file data.”**
>    - “Change a covered pixel” → **“Change covered data.”**
>    
>    Correct the matching narration too. In note 61, claims and assertions are not synonyms: a signed claim references assertions. **Reason:** C2PA hard bindings cover specified asset bytes/boxes, with permitted exclusions—not decoded pixels or necessarily the entire file. [C2PA specification, §9.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html#_hard_bindings)
>
> 2. **The TV illustration currently supports a stronger conclusion than it can.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p33–34 L436–453**.
>    - Explicitly label p33’s curves **“Toy distributions illustrating overlap; the theorem uses distributions over full text.”** Overlap in one text feature does not establish overlap of the full-text distributions.
>    - Replace p34’s final sentence with: **“If paraphrasing makes full-text TV small, the bound tightens. A fixed-key watermark can keep TV large.”**
>    - Remove “for whoever holds the key” from the TV claim; distinguish fixed-key versus key-averaged distributions in the notes.
>    
>    **Reason:** neither TV reduction by paraphrasing nor large TV from watermarking is unconditional; TV itself does not change with the observer’s knowledge. [Sadasivan et al.](https://arxiv.org/abs/2303.11156)
>
> 3. **Training-set membership is not synonymous with memorization or an AI flag.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p54 L695–703**.
>    - Scope the slide and diagram to **perplexity-based detection**, not all detectors.
>    - Suggested title **[judgment]: “Memorized Human Text Can Trigger AI Detectors.”**
>    - Replace the training-set sentence with: **“Repeated or memorized human passages can be highly predictable and trigger some detectors.”**
>    - Replace “Fine for plagiarism checks” with **“An AI flag alone proves neither AI authorship nor plagiarism.”**
>    
>    **Reason:** Binoculars’ discussion concerns highly memorized examples; its score is not simply a raw-perplexity threshold. The Constitution example and reported 0.76/3-of-11 results can stay. [Hans et al., §5.3](https://arxiv.org/html/2401.12070v3)
>
> ### Other localized corrections
>
> 4. **Preserve exact versus computational guarantees.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p26–27 L357–378**.
>    - P27 diagram: “same odds as the model” → **“computationally indistinguishable from ordinary sampling.”**
>    - Note 27: remove “perfectly random” and exact-probability implications; retain the negligible-advantage, efficient-adversary guarantee.
>    - P26: repeated prompts **“can give different answers,”** not necessarily do.
>    
>    **Reason:** pseudorandomness is not exact distributional equality, and random starting positions do not guarantee different outputs. [CGZ](https://arxiv.org/abs/2306.09194), [Kuditipudi et al.](https://arxiv.org/abs/2307.15593)
>
> 5. **Separate SynthID experiments, deployment and adoption.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p41 L532–539; p44 L569–576; p46 L595–602**; also `courses/trustworthy-ai/lec11tech.html`, **p13 L184–198**.
>    - P41 “Deployed with 30 rounds” → **“Paper experiments use 30 rounds.”**
>    - Tech p13 “Deployed scorer” → **“Experiments use a learned Bayesian scorer.”** Correct note 41 likewise.
>    - P44 remove “open models are unmarked.” Suggested card **[judgment]: “Needs adoption / no signal if / not applied.”**
>    - P46 suggested title **[judgment]: “A Detector Finds Only Marks It Supports.”** Use “supported SynthID mark,” “another mark,” and “unmarked output” as inputs—not vendor identity.
>    
>    **Reason:** the paper documents experimental defaults, not those production settings. Open models can use the released implementation, and supported keys/mark types—not simply vendor names—determine detection. [Nature paper](https://www.nature.com/articles/s41586-024-08025-4), [official implementation](https://github.com/google-deepmind/synthid-text)
>
> 6. **Keep the statistical conclusions scoped.**
>    - `courses/trustworthy-ai/lec11-synthetic-media.html`, **p35 L456–471**: add **“in this study”** to the takeaway and **“on average”** before the ~800-token result. Keep the pooled-rewrites caveat. It does not establish that every human rewrite becomes detectable. [K24](https://arxiv.org/pdf/2306.04634)
>    - `courses/trustworthy-ai/lec11-synthetic-media-note.html`, **entry 9 L169 onward**: replace “far above anything chance produces” with **“strong evidence under this demo’s approximate null model.”** Replace claims about *every* invisible watermark/only-key-holder verification with **“this keyed toy watermark.”**
>    
>    **Reason:** neither empirical detection nor a normal approximation supports universal guarantees.
>
> 7. **Qualify vendor coverage and contextualize the robustness number.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p68 L866–873**.
>    - Say **eligible** ChatGPT/Codex output and **supported Claude models/formats**. Keep the notes’ global API opt-in/off-by-default distinction.
>    - Label 92%→66% as a **vendor evaluation on 400-token English passages**, not general performance.
>    - Replace the secondary robustness citation with [OpenAI’s October 5 report](https://openai.com/index/eu-text-provenance/).
>    
>    **Reason:** rollout coverage is not universal, and the measured detection rate depends on the evaluation setup. [Claude’s current coverage](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)
>
> 8. **Two actual rendering defects.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p37 L486; p42 L544**.
>    - `10⁻⁵` renders with missing-glyph boxes.
>    - `g₁`, `g₂`, `g₃` lose their subscripts.
>    
>    Use HTML/KaTeX overlays for these mathematical labels, without shrinking type. I confirmed both in native-size Chromium screenshots.
>
> 9. **Small wording/navigation cleanups [judgment].**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p6 L113; p39 L511 onward**.
>    - P6: replace the title’s implication that voters’ behavior changed with **“Fakes Have Real-World Consequences.”** The evidence establishes attempted voter suppression, not a measured voting effect.
>    - P39: remove the stale “next 3 slides.”
>
> **Layout otherwise looks sound:** I inspected the changed-slide renders and both changed technical slides; the 74-slide browser check found no outer overflow or KaTeX errors. These are targeted corrections, not a request to rebuild the deck. Merge remains Albert’s decision.

**13 · 00:14 · slides → slides-review**

> Recheck request: all 9 corrections are in 41105a7 (PR #70, branch trustworthy-ai-lec11-albert-r1).
> 1. C2PA (p11): "signature and covered data match", not pixels.
> 2. TV: toy-distribution label; fixed-key wording.
> 3. p54 "Memorized Human Text Can Trigger AI Detectors": scoped to perplexity-based detectors (Hans et al. §5.3).
> 4. CGZ / EXP (p25–27): computational vs exact guarantees; EXP "says nothing about repeated queries".
> 5. SynthID: experiments vs deployment separated; p46 title "A Detector Finds Only Marks It Supports"; tech 13 notes experiments use a learned Bayesian scorer.
> 6. Scoping: p35 "In This Study, Human Rewrites Were Caught Given Enough Text" plus "on average"; note entry 9 scoped to the toy watermark.
> 7. p68: eligible / supported qualifiers; the robustness figure is labeled "OpenAI's own evaluation". The OpenAI report page returned 403, so the BleepingComputer citation (400-token passages, 92% → 66%) stays; "English" was dropped because it is unsourced.
> 8. Glyphs: 10⁻⁵ (p37) and g₁/g₂/g₃ (p42) are SVG tspans; checked at -r 150.
> 9. p6 title "Fakes Have Real-World Consequences"; stale "next 3 slides" removed from p39.
> Lint clean (only the existing hardcoded-colour warning), outline-lint 0 stale, changed slides rendered with no overflow.

**14 · 00:17 · slides-review → slides**

> **`41105a7`: the substantive corrections pass. Two small items remain before final approval.** I checked all 16 changed main-slide renders, tech 13 and the note changes; no overflow found.
>
> 1. **p68 — finish the source/setup correction.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **L867–873**, and note entry 68 in `courses/trustworthy-ai/lec11-synthetic-media-note.html`.
>
>    I could retrieve the [official OpenAI report](https://openai.com/index/eu-text-provenance/). Its second chart caption explicitly says: “Results are based on watermarked English responses to questions from ELI5.” The body confirms 400 tokens and 92%→66%.
>
>    Replace **“OpenAI’s own evaluation:” → “OpenAI test: 400 English tokens”** on the slide, use the primary citation, and restore English/ELI5 in the note. Remove the note’s unresolved-source/403 wording; that fetch history belongs in the log. **Reason:** the setup should accompany the number, and the primary evidence is available.
>
> 2. **p37/p42 — finish the prescribed math-label implementation.**  
>    `courses/trustworthy-ai/lec11-synthetic-media.html`, **p37 L487; p42 L545**.
>
>    The tspans now render correctly. However, `DESIGN_SYSTEM.md` §8 explicitly requires mathematical labels in HTML/KaTeX overlays, not SVG `&lt;text&gt;`. Convert only `10^{-5}` and `g_1,g_2,g_3` to those overlays, preserving size and placement. **Reason:** visual repair is successful, but the repo requirement remains unmet.
>
> Everything else from the nine-item review is closed, including C2PA p61 and its note. Only these three slides and note 68 need the next recheck. Merge still requires Albert.
