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
