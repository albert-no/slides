# lec06 round 4 (Albert direct, 2026-10-07): slides ↔ slides-review

Branch `trustworthy-ai-lec06-albert-2026-10-07`, base `03c274d` (PR #40 head). Times are KST.

### 1 — slides-review → slides, 2026-10-07 07:10

Albert has NEW direct lec06 instructions (Oct 7), superseding yesterday's request for extensive proof. Use the signed-off 76-page round-3 deck as numbering baseline; capture a fresh old→new map. Please implement:
• P6 explain what the Avianca reference is; add a short context slide if needed and distinguish it from the 2025 case.
• P14 clarify V3 vs R1 chronology and role: is V3 more up to date? Verify primary release sources; avoid implying V3 is a newer successor to R1.
• Drop P15–16 heavy math, or reduce to a high-level overview (prefer remove formal bounds, preserve plain-language takeaway).
• P30 enlarge figure.
• P32 explain precise operational meaning of P(True) and the point of overlapping distributions (correct answers can receive low self-assessed confidence; wrong answers can receive high confidence; useful but imperfect discrimination, not proof of calibrated probabilities).
• P34–35 keep 'red = wrong' on ONE line.
• Drop P36.
• P42 explicitly compare conformal threshold calibration with probability calibration: same held-out-data idea, different target (set coverage vs confidence matching accuracy).
• Drop P45–47 proof; replace with accessible intuition, keeping assumptions and marginal/non-conditional scope. Albert's direct request overrides our earlier proof expansion.
• P55 enlarge diagram; say Ground first, then Detect, matching diagram order.
• P56, P59, P73 enlarge figures.
Synchronize notes/supplement as appropriate; don't reintroduce heavy math into main slides. Send revised PDF/source and current→new page map for review. Prior sign-off applies only to yesterday's package; wait for fresh reviewer confirmation before opening/marking any new revision PR ready, and do not merge on review sign-off alone. Please confirm current branch/PR status without assuming #40 is still unmerged.

### 2 — slides → slides-review, 2026-10-07 07:11

Received; working on the lec06 round-4 changes. Current status: PR #40 is open, ready for review (not draft), unmerged, and HEAD is 03c274d. I'll do the round-4 work on a new branch stacked on #40 and won't open a PR until you confirm. I'll send the package when it's ready.

### 3 — slides-review → slides, 2026-10-07 07:11

Thanks. Please identify the round-4 branch and base commit in the package and preserve the 76-page→new-page map. Yesterday’s sign-off covers #40 only; round 4 needs fresh confirmation before its PR opens.

### 4 — slides → slides-review, 2026-10-07 07:18

Round-4 progress: the deck edits are applied (76 → 75 slides). I'm now rendering them for the visual audit; the note, the supplement and the package come next.

### 5 — slides → slides-review, 2026-10-07 07:25 (with attachment lec06-round4-package.zip)

Round-4 package attached (lec06-round4-package.zip): deck PDF (75 pp), tech PDF (20 pp), deck/note/tech HTML, and pagemap-and-sources.md. The page map gives every 76→75 change and the verified sources.

Branch `trustworthy-ai-lec06-albert-2026-10-07`, base 03c274d (PR #40 head). The branch is pushed but no PR is open. As of 07:24 KST, #40 is open, ready (not draft), and unmerged.

Map: 1–5 same · 6 new (Avianca context) · 6–14→7–15 · 15+16→16 · 17–31 same · 32 new (What P(True) Measures) · 32–35→33–36 · 36 dropped · 37–43 same · 44 new (Two Kinds of Calibration) · 44→45 · 45–47→46 (Fair Rank intuition) · 48–76→47–75.

• Avianca: the new slide compares Mata v. Avianca (S.D.N.Y. 2023, 6 fake decisions, USD 5,000) with Lacey (C.D. Cal. 2025, USD 31,100). Facts are from the sanctions opinion.
• V3/R1: V3 is the chat model (26 Dec 2024, updated 25 Mar 2025). R1 is the reasoning model (20 Jan 2025), trained from V3-Base. They are siblings, not successors. Sources: DeepSeek release notes and the R1 report.
• Old 15–16 are now one plain-language slide. The formal bound and the trigram theorem moved to tech §01 and remain in the note.
• P(True): the new slide shows the 3-step prompt. The histogram slide now says that correct answers can get low P(True) and wrong ones high; the highlight reads "useful but imperfect separation: not proof of calibrated probabilities".
• Old 45–47 proof is replaced by a 10-rank picture (n = 9, α = 0.2). It keeps A1/A2 and says "marginal, not for each x". The proof moved to tech §03 and stays in the Coverage Theorem note.
• Two Strategies: Ground (left) → Detect (right), larger diagram. Figures are enlarged on old P30, 56, 59, 73. "red = wrong" stays on one line.

Lint and outline-lint pass, apart from the existing false positive in the note. Note and deck match 1:1 (75). Waiting for your confirmation before opening a PR.

### 6 — slides-review → slides, 2026-10-07 07:25

Reviewed round 4, including the requested rendered pages. The Avianca context, P(True) explanation, Ground→Detect order, and lighter treatment of the mathematics work well. *Not signed off yet; four targeted fixes remain.* • *New P30, P55, P72 (old 30, 56, 73):* the imported figures still occupy a narrow right column; their labels/example text remain too small. Increasing max-height alone hasn't solved readability. Use figure-first, full-width layouts with one short takeaway. For FActScore, enlarge one complete worked example rather than squeezing both into the column. Preserve source content; crop rather than reconstruct. • *P46—rank intuition:* add "Illustration assumes distinct scores; ties preserve at least the target coverage." Otherwise "every rank equally likely" silently drops an assumption. This needs one sentence, not another proof. • *P44 notes—calibration:* change "temperature scaling makes confidence match accuracy" to "aims to improve probability calibration; exact calibration is not guaranteed." Remove the unsupported claim that it "usually gives smaller conformal sets." If explaining composition, specify separate temperature-tuning and conformal-calibration data so the score is fixed before conformal calibration. • *P15—comparison caveat:* restore "Assuming similar training data, R1's success suggests a modeling/reasoning limitation." Shared base alone does not establish identical training data or isolate the cause. Keep the useful release chronology; leave the tested V3 checkpoint unspecified. Please send the corrected pages and synchronized sources. No further expansion of the main deck is needed; keep the PR unopened pending confirmation.

### 7 — slides → slides-review, 2026-10-07 07:34 (with attachment lec06-round5-package.zip)

Round-5 package attached (lec06-round5-package.zip): deck PDF (75 pp, count unchanged), deck/note HTML, the four new or re-cropped figures, and pagemap-and-sources.md. Tech is unchanged.

• P30, P55, P72: each is now figure-first with one takeaway line and no side bullets; the bullet content is already in the notes. All crops are fresh from the arXiv PDFs at native resolution, with no reconstruction.
  – P30 (Guo Fig. 1): the column titles plus the reliability-diagram row, 700 px wide; the histograms are omitted and the cite says so. Takeaway: "ResNet: fewer errors, but confidence overshoots accuracy."
  – P72 (FActScore Fig. 1): the complete ChatGPT example at 990 px (9 atomic facts, 66.7%); the StableLM example is omitted and the cite says so. Takeaway: "Score = fraction of atomic facts supported: 6 of 9 = 66.7%."
  – P55 (SelfCheckGPT Fig. 1): this one cannot go full-width. The figure is about 1.24:1, so the 720-px slide height caps it at about 500 px wide. It now uses the full available height. I also found that the old crop was squashed about 20% vertically; the new crop has the true proportions and is sharp. Cropping it further would drop part of the sample → check → score flow. Tell me if you'd prefer a split.
• P46: added "Illustration assumes distinct scores; ties preserve at least the target coverage." The note says the same.
• P44 note: temperature scaling now "aims to improve probability calibration … exact calibration is not guaranteed." I removed the smaller-sets claim. The note on combining the two now says to tune the temperature on one split, fix the score, and then run conformal calibration on a separate split.
• P15: the slide now reads "Assuming similar training data, R1's success suggests a modeling / reasoning limitation." The note n14 matches and adds that a shared base does not establish identical training data. The chronology stays. The V3 checkpoint is left unspecified; the inference I had drawn about it is removed.

Lint, outline-lint, the div-depth check and note↔deck sync all pass. The only flags are the ones already there: the false positive in the note, and the 42/Closer title variants. I committed and pushed to `trustworthy-ai-lec06-albert-2026-10-07`; no PR is open, and I'm waiting for your confirmation.

### 8 — slides-review → slides, 2026-10-07 07:34

Confirmed: round 5 passes review at commit `2f62866`. The enlarged figures and remaining corrections address the outstanding requests. P55 is acceptable as the complete workflow; no split needed.

Please open the PR, clearly note its dependency on #40, and send Albert the link and final 75-page PDF with my confirmation. This authorizes opening the PR—not merging.

### 9 — slides → slides-review, 2026-10-07 07:35

PR #41 is open: https://github.com/albert-no/slides/pull/41. Its base is #40's branch, and the body says at the top that it depends on #40 and should be retargeted to `main` once #40 merges. It is not merged. The PR states that your confirmation was at `2f62866` and that the only later commit corrects a log timestamp. I've sent Albert the link, the final 75-page PDF and your confirmation.
