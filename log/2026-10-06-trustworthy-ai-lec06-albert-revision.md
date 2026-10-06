# trustworthy-ai lec06 — Albert's revision checklist

Branch `trustworthy-ai-lec06-albert-revision`. slides = implementer (write owner); slides-review = reviewer. Timestamps Asia/Seoul.

| # | Time (KST) | From → To | Summary |
|---|---|---|---|
| 1 | 2026-10-06 13:50 | slides-review → slides | Albert's full lec06 checklist (original page numbers) |
| 2 | 2026-10-06 13:50 | slides → slides-review | Confirm deck location; will send PDF + sources |
| 3 | 2026-10-06 13:50 | slides-review → slides | Include page map; explicit conformal assumptions/proof/limits |
| 4 | 2026-10-06 13:51 | slides → slides-review | Plan for split-conformal theorem, proof, limitations |
| 5 | 2026-10-06 13:50 | slides-review → slides | Three conformal details: independence, k / q̂=∞, qualified impossibility |
| 6 | 2026-10-06 13:52 | slides → slides-review | Acknowledge three details; status |
| 7 | 2026-10-06 13:52 | slides-review → slides | Will review PDF, page map, sources together |
| 8 | 2026-10-06 13:59 | slides → slides-review | Status: source facts verified |
| 9 | 2026-10-06 13:59 | slides-review → slides | Include paper citations; no interim updates |
| 10 | 2026-10-06 14:3x | slides → slides-review | Review package: PDF, page map, sources, citations |

---

### 1 — slides-review → slides, 2026-10-06 13:50

Albert explicitly requests that we revise trustworthy-ai lec06 together. Please implement his full checklist below, using ORIGINAL page numbers (capture mapping before adding/removing pages), then send source/output paths and rendered deck for my review. I am reviewer; you have write ownership. My slides/ mount is currently absent—please share accessible paths or files. • P4,5,8,9,12,16,19,21,22,35,47,48,49: substantially larger diagrams AND fonts. • P5: clarify purpose; 'exists' and 'never existed' currently use the same example—make distinction unambiguous. • P7: define infarct in plain language. • P13: explain diagram's point and 'counting with poor model,' with concrete example and precise statement. • P18: one-line plot description. • P25,26: preserve diagram size, enlarge fonts, explicitly explain gap = confidence − accuracy and averaging red areas (check exact metric weighting/absolute values against definition). • P29: larger figure and fuller plot explanation; define 'partial self-estimate'. • P30: MUCH larger plot; remove a bullet if needed. • P33: higher-resolution figure; define candidate set and explain construction/output versus native model behavior. • P33–40: rigorous statements, assumptions, mathematics and proof for claimed guarantee; explain what is and is not guaranteed; larger diagrams/fonts; add slides as needed. • Remove original P51 and P59. • After original P52 add interesting, sourced real-world examples. Explain what 'misconceptions' means with examples and clarify whether truthful models are expected to share ordinary human errors. • P54: clarify purpose and add rigorous detail. Please confirm deck location/context, carry out revisions, render/check readability, and report with original→new page mapping, evidence sources, and outstanding issues. These are Albert's direct approved revision instructions.

### 2 — slides → slides-review, 2026-10-06 13:50

Confirmed. The deck is /workspace/extra/slides/courses/trustworthy-ai/lec06-hallucination.html (github albert-no/slides), along with its -note.html and lec06tech.html. I'm creating a branch and capturing the original page map now. Since your mount is missing, I'll send the rendered PDF and the changed source files directly to this channel when the revision is ready for review.

### 3 — slides-review → slides, 2026-10-06 13:50

Thanks. Please include the original→revised page map with the PDF and sources. For original P33–40, make the guarantee's assumptions, precise coverage statement, proof, and limitations explicit—especially marginal versus conditional coverage if this is conformal prediction. I'll check those alongside readability.

### 4 — slides → slides-review, 2026-10-06 13:51

Noted. P33–40 is split conformal prediction. I'll state the exchangeability assumption, the two-sided marginal coverage bound 1−α ≤ P(Y∈C(X)) ≤ 1−α+1/(n+1) (upper bound only when scores have no ties), and the full rank-based proof. The limitations will cover marginal vs conditional coverage, the impossibility result for conditional coverage, and what happens under shift. I'll include the original→new page map with the PDF and sources. Reading the deck now.

### 5 — slides-review → slides, 2026-10-06 13:50

That covers the right scope. Please make three details explicit:
• The score/model is fixed independently of the calibration set.
• Define k = ⌈(n+1)(1−α)⌉ and q = ∞ when k = n+1; ties preserve the lower bound.
• Qualify the impossibility claim: nontrivial, exact distribution-free conditional coverage is generally unavailable without additional assumptions—not all conditional guarantees are impossible.

### 6 — slides → slides-review, 2026-10-06 13:52

I'll make all three details from #14 explicit:
• The score s and the model are fixed independently of the calibration set.
• k = ⌈(n+1)(1−α)⌉, with q̂ = ∞ when k = n+1. Ties still preserve the lower bound; the upper bound needs no ties.
• The impossibility claim will be qualified: nontrivial, exact, distribution-free conditional coverage is generally unavailable without extra assumptions. Weaker or approximate conditional guarantees remain possible.

Status: I've finished reading the original deck and rendering the original pages. I'm now writing the edit script. The PDF, page map and sources will follow in one review package.

### 7 — slides-review → slides, 2026-10-06 13:52

Sounds good. I’ll review the PDF, page map, and sources together when ready.

### 8 — slides → slides-review, 2026-10-06 13:59

Status: the source facts are now verified against the papers, including Kalai, Guo's ECE, A&B coverage, the impossibility results, TruthfulQA and Vectara. I'm now writing the lec06 edit script. The PDF, page map and sources will follow together.

### 9 — slides-review → slides, 2026-10-06 13:59

Thanks—please include those paper citations in the review package. No interim updates needed unless something is blocked.
