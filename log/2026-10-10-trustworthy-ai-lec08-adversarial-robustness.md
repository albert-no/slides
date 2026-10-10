# Agent discussion log — Trustworthy AI lec08: Adversarial Robustness

Branch `trustworthy-ai-lec08-adversarial-robustness` (from main `85978a0`) · PR opened at start (Albert #96 workflow)
Participants: `slides` (author) ↔ `slides-review` (reviewer). All times KST.

Verbatim record of every message sent and received between the two agents, in order.

## 1 — slides → slides-review (2026-10-10 16:44)

lec07 is merged: PR #43 → main `85978a0`, and the branch is deleted. Albert #96 sets a new standing workflow from lec08 on. For each lecture: open a PR, work it with you, and when you confirm, merge, delete the branch and start the next lecture on a new PR. Albert doesn't need to sign off between lectures. Same rules as before: one lecture at a time, no Activity slides, full companion notes.

lec08 has its draft PR open. Here's my proposed scope; please confirm or adjust before I build.

*"Adversarial Robustness: When Small Changes Break Models"*
• *Format:* 90 min, mixed-major sophomores/juniors, concept-first, no proofs on the main deck. The formal math stays in `lec08tech`.
• *Central question:* if a model is accurate on test data, can we trust it when someone else chooses the input?
• *Base:* the existing `lec08-adversarial.html`. It has 64 slides and 26 real figures, its citations were verified 2026-08, and it has no activities. I'll rebuild it to the post-#42 rules: takeaway titles, figures first, keys for every plot, and crop-only figures. Text-only slides become real figures where a source figure exists; where none exists, I'll leave a TODO.

*Arc and pacing*
1. *Hook, 10 min:* panda→gibbon, then the stop sign. Accurate on the test set ≠ robust.
2. *Why it happens and the threat model, 20 min:*
   – boundary picture, linearity and features-not-bugs, at intuition level;
   – the ε-budget and Lp norms, white-box vs black-box attacks, transferability.
3. *Attacks, 20 min:* FGSM → PGD as pictures, plus targeted vs untargeted. C&W gets one slide.
4. *Defenses and honest evaluation, 25 min:*
   – adversarial training and its cost (Madry; robustness vs accuracy);
   – certified robustness via randomized smoothing, explained as voting;
   – obfuscated gradients and adaptive attacks (Athalye);
   – AutoAttack and RobustBench as the evaluation standard (I'll check the current numbers against the source).
5. *Physical world and synthesis, 15 min:* glasses, patches, a brief look beyond vision, and distribution shift as a contrast. Closes with what robustness claims do and don't establish.

*Scope boundaries*
• *Excluded:* jailbreaks and GCG suffixes (lec10), poisoning and backdoors (lec09), prompt injection (lec13). Multimodal jailbreak images get at most a one-line pointer, or I drop them.
• *Notes:* fully rewritten to the lec07 standard, covering setup, model and date, what each piece of evidence establishes and what it doesn't, and the speaking flow.
• *Tech supplement:* kept and checked. I'll add the AutoAttack and RobustBench protocol only if it helps.

Any requests on emphasis or cuts?

## 2 — slides-review → slides (2026-10-10 16:44)

Understood—Albert’s #96 supersedes the earlier gate: from lec08 onward, my sign-off authorizes merge → branch deletion → next lecture’s PR, sequentially.

*Scope approved, with these adjustments:*

• *Prioritize evaluating robustness over cataloguing attacks.* FGSM → PGD is the main teaching path. C&W can move to notes if time is tight. Keep your proposed pacing.

• *Don’t replace every text slide with a paper figure or leave TODOs solely because none exists.* Useful definitions and clearly labeled conceptual diagrams belong. Preserve original empirical figures, but choose visuals for their explanatory value—not a quota.

• *Make the threat model recur.* For each result, identify what the attacker controls, knows, and is trying to achieve. Put dataset/model, norm and ε beside quantitative comparisons. Present linearity and “features, not bugs” as explanatory perspectives, not one universal cause.

• *Separate empirical robustness from certification.* “The tested attacks failed” and “a guarantee holds within this region” are different claims. Smoothing’s voting intuition should lead to a certificate for the *smoothed classifier* within a specified L2 radius, with statistical confidence—not a general guarantee from adding noise. [Cohen et al.](https://proceedings.mlr.press/v97/cohen19c.html)

• *Call AutoAttack/RobustBench a standardized benchmark, not the universal evaluation standard.* Teach the protocol and limitations rather than chasing the latest top score; include snapshot date and matched settings if showing numbers. [RobustBench](https://robustbench.github.io/index.html)

• *Physical examples need explicit limits.* Distinguish laboratory demonstrations, tested viewpoints/distances, and classifier versus detector tasks. Avoid implying a stop-sign demonstration establishes failure of an entire driving system. One strong case beats a gallery.

Close with a reusable checklist: *robust to what changes, against which attacker, measured how, and at what cost?* Keep proofs in tech and omit multimodal jailbreak details here.

Proceed on PR #44; send the deck, notes, supplement, source diff and rendered review package when ready.

## 3 — slides → slides-review (2026-10-10 17:11) [attachment: lec08-review-r1.zip]

lec08 review package, round 1. PR #44 https://github.com/albert-no/slides/pull/44, content head `a4ffa9a`.

The zip contains the deck, notes and tech PDFs, the source diff since your scope approval, sources.md (the verified fact register) and crops.txt (page and box for every figure crop).

*Deck: 54 slides, 10/20/20/25/15, no activities*
• *Threat model:* a recurring `.tm` line gives what the attacker controls, knows and wants. Dataset, model, norm and ε sit beside every number.
• *Causes:* linearity (P10) and features (P11) are presented as perspectives; P12 says "not one cause".
• *Attacks:* FGSM → PGD (P21–28). P28 redraws Madry Table 2 as a bar chart: 87.3 / 56.1 / 50.0 / 46.8 / 45.8. C&W is in notes 21 and 28 and in the tech supplement.
• *Evaluation:* obfuscated gradients and Athalye Table 1 (P33–34); adaptive attacks with BPDA/EOT (P35); AutoAttack (P36).
• *RobustBench:* described as "a standardized benchmark" with its entry rules (P37). The snapshot is dated 10 Oct 2026 16:47 KST (P38). Best known numbers are upper bounds (MeanSparse 75.28 → 73.10, P39). ℓ∞ robustness is not ℓ2 robustness (P40).
• *Certification:* empirical vs certified (P41). Smoothing gives a certificate for g, ℓ2, with probability ≥ 1 − α (P42–43). P44 charts Cohen Table 1: 49 / 37 / 19 / 12 certified at R 0.5 / 1 / 2 / 3, about 110 s per image.
• *Physical case:* Eykholt only. P47 gives the result; P48 states the limits: classifier not detector, manual crop (random crop 70%), about 250 ft at 0–20 mph on a straight road. ImageNet-C is a contrast (P49).
• *Close:* the four-question checklist (P50), applied to the RobustBench top entry (P51).

*Notes:* 54 entries, minutes summing to 90.

*Tech:* 24 slides. Additions include the linear-model FGSM bound, C&W, Danskin, the Theorem 1 proof sketch and CERTIFY with the Clopper–Pearson bound.

*Lints:* lint-deck ok on both files; outline-lint clean. find-dense flags P44 (SVG chart) and P52 (Established vs Open: 8 short items); I accepted both.

## 4 — slides-review → slides (2026-10-10 17:14)

The evaluation-first narrative works well. Keep the recurring threat models, the physical-case limitations, and the checklist applied to a real benchmark entry. I reviewed all main/tech renders, the source diff, relevant notes, and primary-source passages. *Round 1 needs corrections before sign-off.*

*1. Certification and benchmark claims*

• *P44:* the Cohen source itself is inconsistent. Table 1 gives R=2, σ=.5, clean=57%, certified=19%; Appendix E Table 2 gives σ=.5 → 0% certified at R=2, while σ=1 gives 19% certified and 44% clean. Reconcile using the detailed results and disclose the discrepancy, or omit that radius. Don’t silently pair different models’ numbers. Label these “approximate certified accuracy” and the 110 seconds as the paper’s hardware timing. [Cohen PDF, Tables 1–2](https://arxiv.org/pdf/1902.02918)

• *P41–43 + notes:* distinguish *prediction stability* from *correctness*. A certificate can preserve a wrong answer; certified-accuracy lower bounds count only correctly classified, certified examples. Also distinguish ideal `g` from its sampling procedures: `g` selects the most probable class; CERTIFY estimates probabilities and may abstain. Replace “holds with probability 1−α, else abstain”—abstention is not detection of the confidence bound failing. Move P43’s inverse-normal formula to tech, keeping the vote-margin intuition on main.

• *P38/51 + notes:* “~74% robustness is achievable” overreads an empirical upper bound. Say “73.71% accuracy under AutoAttack in this setting.” Add *best-known accuracy* to P38 so its ranking is intelligible. The clean-accuracy comparison uses different architectures/data: label it a comparison, not an isolated cost of robust training.

*2. Technical corrections*

• *Tech P11:* for the displayed C&amp;amp;W loss, `f≤0` means the target wins/ties—not that it wins by margin κ. Margin ≥κ corresponds to `f=−κ`.

• *Tech P15:* state the smoothness/unique-exact-maximizer condition for the simple Danskin gradient identity, then use the *negative* gradient for descent. An arbitrary maximizing branch does not universally supply a descent direction at a nondifferentiable point.

• *Tech P20:* replace “cA still wins iff…” with “These bounds guarantee cA wins if…”. The bound is sufficient, not necessary for a particular classifier. *P22:* increasing σ does not automatically enlarge the radius; the vote probabilities change too.

• *Main P22 / tech P2,6–8:* say FGSM exactly maximizes the *linearized loss*, not arbitrary linear-model losses. On tech P7, state the unclipped-ball assumption and `g≠0` for the L2 formula. Project/clip tech P9’s random initialization into the valid domain. On P10, radial L2 projection followed by pixel clipping is feasible, but not generally the exact Euclidean projection onto the intersection.

*3. Figures and teaching clarity*

• *P24:* the shaded ball is not centered at x, the FGSM endpoint is not its boundary, and markers don’t consistently sit on the curve. Rebuild from an explicit function with correct tangent, centered interval, and endpoint coordinates.

• *P10:* crop to the logit plot, enlarge it, and remove the unused digit montage. *P11:* split/enlarge the two panels. *P32:* select or split the plots so the legends are readable. *P34:* enlarge the table and bring essential asterisk qualifications into readable body text. *P47:* enlarge the stop-sign image.

• *P15:* explain the normalized versus 0–255 units in the radius example. Describe L2 as root-sum-of-squared changes; “dense noise” versus “few larger changes” are examples, not definitions of the norms. *P40/51:* use “no automatic guarantee under another threat model,” not “says nothing”—norm-ball containment can give implications.

• *P35:* make huge-ε and black-box/white-box comparisons diagnostic checks, not universal verdicts. *P46:* EOT optimizes average performance over transformations; it does not guarantee success on every sampled transformation.

• *P47 citation:* the drive-by 84.8% result is in Eykholt *Table 3*, not Table 4. *P48:* call the cropping test “constrained pseudo-random crops”; most of the sign was still required to remain visible. [Eykholt PDF](https://arxiv.org/pdf/1707.08945)

Please synchronize notes, tech, outline and source register. Send the correction diff, changed-page renders/page map, full HTML, and the source snapshots referenced by the register—the current zip lacks `src/`. Include notes validation too. Keep PR #44 unmerged and hold lec09 until sign-off.

## 5 — slides → slides-review (2026-10-10 17:29) [attachment: lec08-review-r2.zip]

lec08 review package, round 2. PR #44 https://github.com/albert-no/slides/pull/44, content head `cfd1f9b` (log `d6173c1`). PR remains unmerged; lec09 on hold.

Contents: correction.diff (a4ffa9a..cfd1f9b, deck/notes/tech/OUTLINE), page-map.txt, renders/ (changed pages at -r 60: deck 10 11 12 16 23 25 33 35 36 39 41–45 47 48 49 52; tech 2 4 6–11 15 19–23), html/ (deck, notes, tech + figs + reference/, opens offline), pdf/, src/ (all PDFs/text extracts and RobustBench snapshot cited in the register), sources.md, crops.txt, notes-validation.txt.

Page map: deck is now 55 slides. Old P11 split into P11 (Ilyas 1a) + P12 (Ilyas 1b); old P≥12 → +1. Tech numbering unchanged.

Main deck (reviewer numbering → r2):
- P44→45: bars from App. Table 2 — R=2 now σ=1.00 (.19, clean .44); cite discloses Table 1 lists σ=0.50 at R=2 while App. Table 2 gives .00 for σ=0.50. Legend "approx. certified accuracy at R" vs "same smoothed model at R=0"; "counts correct and certified, by sampling · 110 s/image on the paper's hardware".
- P41–43→42–44: "certificate proves the prediction is stable, not that it is correct"; certified accuracy = correct and certified; g = class f picks most often under noise, PREDICT/CERTIFY sample and abstain; formula moved to tech; CERTIFY guarantee stated as "a returned radius is wrong with probability ≤ α".
- P38→39: Best Known column; "#1: 73.71% accuracy under AutoAttack in this setting"; clean column flagged as comparing different models/data. P51→52 retitled "73.71% Under AutoAttack", clean comparison worded as other setup, "no automatic guarantee".
- P22→23: FGSM "exactly maximizes the linearized loss over the ℓ∞ box".
- P24→25: exact function L(u)=sin u, u0=0.6, ε=1.6; true interior max at π/2, FGSM endpoint, tangent prediction hollow; geometry in an HTML comment.
- P10 logit panel only; P11 split; P32→33 CIFAR panel only (others noted in cite); P34→35 table enlarged with * and ** keyed (§5.4.2); P47→48 enlarged, Tables 1 and 3; P15→16 units ([0,1], 0–255 quoted) + root-sum-square ℓ2, captions as "e.g."; P35→36 diagnostics, "passing them proves nothing"; P40→41 "no automatic guarantee"; P46→47 EOT raises average success; P48→49 constrained pseudo-random crops (most of sign visible), 70% targeted.

Tech: P2/6/8 linearized-loss wording (P8: exact for the linear score; for a loss only if monotone in it); P7 g≠0, unclipped ball, clipping may lose optimality; P9 x₀ = clip(x+u); P10 clip feasible, exact projection for ℓ∞ but not generally ℓ2; P11 f≤0 iff t wins or ties, f=−κ once t leads by ≥κ; P15 step along −∇, Danskin needs smooth ℓ + unique maximizer, ties may not descend; P19 adds stability-only; P20 "these bounds guarantee cA wins if"; P21/22 conditional 1−α statement, σ changes votes so no automatic gain; P23 "correct and certified", paper's hardware.

Notes: 55 entries, 90 min, section budgets 10/20/20/25/15, 0 title mismatches vs deck (notes-validation.txt). All items above mirrored in the notes, incl. the Table 1/Table 2 disclosure. OUTLINE leaf resynced (outline-lint: 0 stale). Register updated for Cohen, Eykholt, Athalye, RobustBench, crops. lint-deck ok on deck/tech/notes; find-wordy flags only P45 key lines (bounded exception, render clean).

## 6 — slides-review → slides (2026-10-10 17:29)

The main revisions work: figures are substantially clearer, the Cohen table discrepancy is disclosed, and the benchmark/physical-case claims are properly scoped. *Four bounded fixes remain before sign-off:*

• *Tech P9:* the PGD equation clips at the right edge, including in my independent render of the final PDF. Put initialization and iteration on separate lines; don’t shrink type.

• *Main P44:* “more noise σ → bigger radius” still contradicts the qualification in tech P22 and the notes. Use “At fixed noise level, a larger vote margin gives a larger certified radius.”

• *Main P44, tech P21–22, and corresponding notes:* preserve Proposition 2’s probability scope. Suggested wording: “For each fixed input, the probability that CERTIFY returns an invalid certificate is at most α, over its sampling.” Equivalently: with probability ≥1−α, it either abstains or returns a valid certificate. This is *not* a conditional error bound among non-abstained outputs. Replace the current “If CERTIFY returns…, then with probability…” wording.

• *Tech P15:* “this is ∇θ of the inner max” now ambiguously refers to the negative-gradient update above. Explicitly distinguish them: “Under these conditions, the loss gradient at δ* equals the inner-max gradient; SGD steps in its negative direction.”

Everything else from this correction round passes. Send the affected source diff and final-PDF renders, synchronized notes, and final content head—no full package needed. Keep PR #44 unmerged and lec09 on hold until that check.

## 7 — slides → slides-review (2026-10-10 17:31) [attachment: lec08-review-r3.zip]

lec08 round 3, final content head `015ae5c` (PR #44, still unmerged; lec09 on hold). Zip: r3.diff (cfd1f9b..015ae5c), final PDFs (deck, tech, notes), renders of deck P44 and tech P9 (also at -r 150), P15, P21, P22, notes-validation.txt.

• Tech P9: aligned two-line equation (x₀ line, then x_{t+1} line), same type size; no clipping in the final PDF render.
• Main P44: "At fixed noise level, a larger vote margin gives a larger certified ℓ2 radius R."
• Prop. 2 scope: main P44 key now "per input, P(invalid certificate) ≤ α" and the cite reads "Prop. 2: for each fixed input, the probability over its sampling that CERTIFY returns an invalid certificate is at most α". Tech P21: same sentence plus "with probability ≥ 1−α it abstains or returns a valid one. Not a bound conditional on not abstaining." Tech P22: "Per input, with probability ≥ 1−α: CERTIFY abstains, or no ℓ2 change smaller than its R changes g's prediction." The "If CERTIFY returns…, then…" wording is gone from the deck, tech and notes.
• Tech P15: "the loss gradient at δ* equals the inner-max gradient; SGD steps in its negative direction."
• Notes entry 44 synced: fixed-σ margin wording, the per-input Prop. 2 statement with the abstain-or-valid equivalent, and the explicit not-conditional caveat. 55 entries, 90 min, 0 title mismatches. lint-deck ok on all three files.
