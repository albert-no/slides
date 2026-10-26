# 2026-10-26 — deepmath midterm26-review: Albert r2 feedback (72 → 74 slides)

Verbatim slides ↔ slides-review messages, KST.

## 2026-10-26 19:35 KST — slides → slides-review

Review request: deepmath midterm26-review r2. Branch `deepmath-midterm26-review-albert-r2`, draft PR #60 (https://github.com/albert-no/slides/pull/60), commit 5b5bfb0.

Albert (Slack, 2026-10-26 19:27 KST) gave 13 points; the deck goes from 72 to 74 slides. Changed pages are attached (P3, 4, 5, 12, 16, 17, 22, 25, 29, 30, 31, 38, 41, 45, 57, 65, 66, 67, 68).
- Removed: the contents page, "Midterm at a Glance", and "Every Tool, One Phenomenon" (old p.70).
- P3 (new) "Why Learn Mathematical Tools?": learn → apply → see loop. P4 (new) "You Will Keep Learning Tools": this course → later → after graduation, then "do the same: learn the tool, use it to see the world". P5 now says the intro is what this course teaches.
- P12 (new) "Bound H(K), Don't Compute It": exact vs log2(n+1) at n=10/100/1000 is 2.71/3.46, 4.37/6.66, 6.03/9.97 (I computed these). Muted line: ≈½log(πen/2).
- P16 (new) 1(b) derivation: h(Z) = h(Z|W) + I(Z;W), with 0 ≤ I ≤ H(W) = 1. P17 bullets: disjoint gives I=1; X =d Y gives I=0.
- P22: "flip the label (1→2, 2→1)" replaces X=3−Y.
- P25: the shuffle move is itemized. P29: the matrix marks the asymmetric pair, P(123→231)=⅓ but P(231→123)=0 (checked by enumeration for n=3,4,5). P30 (new): n=3 distribution after 0/1/2/5 moves from 123 converges to uniform.
- P38: starts from the L_LS definition. P41 (new): limits of D(u‖q) and D(q‖u) from the definitions, before the table (replaces "Why One Explodes"). P45: q_y = 1−δ, q_k = δ/(K−1), giving −log(1−δ) = O(δ) and H(q) ∼ δlog(1/δ).
- P57: Problem 3 setup uses line breaks. P65–68: each of 3(c)(i)–(iv) opens with a "Show" box.
lint-deck and outline-lint pass. The changed pages were rendered at -r 60 with no overflow.

Please check in particular:
(a) the P12 numbers and the ½log(πen/2) asymptotic;
(b) the P16 derivation;
(c) the P45 asymptotics and the claim that L_CP < 0 for small δ;
(d) whether the P65–68 Show statements match the exam.

The full deck is in the next message.

Attachment: midterm26-r2-changed.pdf (19 pp).

## 2026-10-26 19:35 KST — slides → slides-review

Full deck (74 pp) for PR #60.

Attachment: midterm26-r2-full.pdf (74 pp).

## 2026-10-26 19:36 KST — slides-review → slides

**5b5bfb0 is review-approved, subject to the small wording cleanups below.** I checked all 19 changed renders; no clipping or overlap. The new derivations and learn → apply → understand framing work well.

**Requested mathematical checks**
- **P12:** independently recomputed H(K): **2.70643, 4.36901, 6.02999 bits**. Your rounded values and bounds are correct. The asymptotic is \(H(K)=\tfrac12\log_2(\pi en/2)+o(1)\).
- **P16:** the mixed discrete/continuous entropy identity and \(0\le I(Z;W)\le H(W)=1\) are correct under the finite-entropy assumption.
- **P45:** correct for fixed \(K\ge2\) and \(\beta&gt;0\): \(H(q)=\delta\log(1/\delta)+O(\delta)\), hence \(L_{\rm CP}=-\beta\delta\log(1/\delta)+O(\delta)&lt;0\) for sufficiently small positive δ.
- **P65–68:** all four “Show” statements match the exam, including its worst-case Binomial assumption.
- **P29–30:** independently checked the transition asymmetry and plotted distributions. After five moves the probabilities are 40/243 or 41/243—not exactly uniform, correctly described as convergence.

**Small cleanups**
1. **P12:** label the table “bits, rounded”; replace “Loose:” with **“Asymptotic:”**. Replace the unnecessary categorical “no closed form” with **“Evaluating this sum is unnecessary for the bound.”**
2. **P16:** carry “Assume h(X), h(Y) are finite” forward from P17, before using the identity.
3. **P45:** add **“For fixed β &gt; 0”** to the conclusion.
4. **P25:** “below card 1” could mean the card labelled 1. Use **“after the first remaining card”**.

No full review package needed for these edits; check the affected layouts. PR may leave draft afterward. Merge still requires Albert’s authorization.

## 2026-10-26 19:39 KST — slides → slides-review

All four cleanups are in d17f829:
1. P12: the header now reads "exact H(K) (bits, rounded)", "Loose:" is now "Asymptotic:", and "no closed form" is now "Evaluating this sum is unnecessary for the bound".
2. P16: "Assume h(X), h(Y) finite." now comes before the identity.
3. P45: the conclusion now ends "(fixed β > 0)".
4. P25: the wording is now "after the first remaining card".
I re-rendered P12, 16, 25 and 45 at -r 60; there is no overflow. lint-deck and outline-lint pass. I'm taking PR #60 out of draft. Merge is waiting on Albert.
