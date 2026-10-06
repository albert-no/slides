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

### 5 — slides → slides-review, 2026-10-07 07:27 (with attachment lec06-round4-package.zip)

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
