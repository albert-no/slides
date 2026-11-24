job: 2026-11-24-opt01-opt02-polish
size: medium
deck: courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html; courses/deepmath/opt02-convexity-gd/opt02-convexity-gd.html; matching HTML and Markdown notes
audience / mode / duration: junior undergraduate AI majors / rigorous core with fewer worked calculations / existing 150-minute opt01 + 90-minute opt02 allocations, 240 minutes total
baseline: 9fdba016e02405c96fa9d8a9c7224f4612361d16
id commit: inherited 01ba79c7b18bb7538c0c8bcd34f6141dd604d075 from parent job; no new ID-only pass
branch: 2026-11-24-opt01-opt02-polish
pr: 80 — https://github.com/albert-no/slides/pull/80 (existing PR; no second PR)
pr head branch: 2026-11-23-opt01-opt03-four-hour-core
state: in-work
round: 2 of 2
review commit: 2244aea04c44369d216d928c9e70b5341cddca2e
albert decisions:
  - 2026-11-24 22:10 Asia/Seoul: additional opt01 comments C01–C13 authorize spacing, splitting, figure readability, removal of worked arithmetic, retained illustration/energy argument, explicit Frobenius-proof scope and brief LLM weight-compression application.
  - 2026-11-24 22:20 Asia/Seoul: opt02 C14–C20 authorize removal of running examples and pages 24/47, optional animation, an elementary descent argument, clarification of vanishing gradients and rate, and reference verification. Both batches combined before plan-v1 announcement.
  - No merge, PDF, probability rewrite or overall teaching-time change requested.
  - 2026-11-24: plan-v1.md complete and issued as the first work order for this medium follow-up; C01–C20 mapped to frozen deck-qualified IDs. New job branch from baseline; retain existing PR #80 for approved delivery.

  - 2026-11-24 22:33 Asia/Seoul: slides acknowledged plan-v1 and reported branch setup from 9fdba01.

review decisions:
  - 2026-11-24: round1 exact commit 2244aea04c44369d216d928c9e70b5341cddca2e reviewed; verdict revise. Main decks answer the requests; blocking F01 covers narrow-note math reflow and F02 covers nonconvex summary qualifiers. F03/F04 are nonblocking.
  - review-r1.md issued for final round2; notes/necessary metadata only, no main-deck redesign or plan change. E10 resolves the flagged Golub–Van Loan citation. Existing PR80 head remains unchanged until approval.

# Size and relationship to the approved work

Medium: many localized comments and deletions, but the argument remains norms/rank → SVD → spectral EYM proof → Frobenius statement and energy → application/limits. The GD argument also remains one update → descent → three convergence guarantees. Targeted verification supports the LLM use and GD attribution question; no literature survey or new course design is needed. Two review rounds maximum for this new author-feedback batch.

The parent job `2026-11-23-opt01-opt03-four-hour-core` completed its three review rounds and remains a historical approved record. This is not an automatic fourth correction round or a reset of unresolved findings: all prior findings were closed, and Albert has now supplied new comments. Use this separate job record and branch, preserving the parent record.

GitHub verified PR #80 open/unmerged at the exact baseline on 2026-11-24. Work on the new job-named branch from that SHA. Keep the existing PR head branch unchanged while this follow-up is being reviewed. After approval and copying/pushing the final job record, slides may fast-forward the existing PR head branch to that exact reviewed/log-only descendant. This preserves the commit identity, the job-named branch convention and the single existing PR. No force push, new PR, main push, merge or branch deletion. If the PR head independently advances, report it before integrating; never overwrite another change.

Mounts reconfirmed with findmnt: repo read-only, `/workspace/extra/slides-log` read-write. Reviewer writes only job-owned files here; slides implements all source/note/outline work. Baseline page numbers below include structural slides. Page-to-ID mapping is frozen; future feedback uses IDs after deletions/splits.

# Resolved scope choices

1. Keep the main argument and full spectral EYM proof; reduce repetitive numerical construction, not conceptual prerequisites. Existing 150-minute allocation is a ceiling/teaching slot, not a demand to refill deleted examples.
2. Page 5 explicitly keeps an example as the second half of the requested split. Page 34 remains the one self-contained SVD layer illustration. The deletion requests do not mean remove every example from the deck.
3. Page 35 means eigenvalues and singular values are different notions and generally differ, not that they can never coincide. Symmetric positive-semidefinite matrices are a legitimate exception; the corrected qualifier belongs on-slide.
4. Page 60's Frobenius optimality proof is beyond this lecture. Keep its theorem and the simpler discarded-energy calculation; label the long note proof optional/beyond scope rather than imply it is assigned core reading. This changes presentation scope, not the truth of the theorem or exam policy.
5. Pages 63–65 lose their worked calculations; retain and generalize the energy-ratio argument at S103. The 90% example on retained page 34 is permitted and must not be duplicated as a second exercise.
6. Replace page 46's puzzling diagram with the two explicit proof obligations, not a new arbitrary plot. Answer its purpose on-slide: optimality needs a bound for every competitor and a candidate attaining it.
7. Brief LLM application: low-rank weight factors can save storage when k(m+n)<mn; EYM's matrix-error guarantee does not guarantee preserved language-model quality. One high-level slide, no SVD-LLM method tutorial or performance numbers.
8. Deleted arithmetic remains discoverable in the existing full-original opt01 archive and notes. Verify actual coverage. Any unique removed detail not there is retained as optional material in an appropriate surviving main-note article, not silently lost or kept as an orphan slide/article. No archive rewrite is needed for this batch.

# Opt01 baseline page manifest

| Baseline page | ID | Source line | Title |
|---:|---|---:|---|
| 1 | S01 | 100 | SVD and Best Low-Rank Approximation |
| 2 | S02 | 111 | Contents |
| 3 | S120 | 161 | Why Low Rank? |
| 4 | S80 | 168 | A Smaller Matrix, Controlled Error |
| 5 | S12 | 185 | Recall: Span and Range |
| 6 | S14 | 222 | Rank Counts Independent Directions |
| 7 | S13 | 246 | Two Inputs Collapse to One Direction |
| 8 | S16 | 283 | Null Space Means Lost Directions |
| 9 | S18 | 322 | Rank and Nullity Add Up |
| 10 | S25 | 349 | Measuring Error |
| 11 | S27 | 356 | What Makes a Norm? |
| 12 | S28 | 387 | Three Familiar Vector Norms |
| 13 | S29 | 412 | One Vector, Three Answers: 7, 5, 4 |
| 14 | S30 | 446 | Unit Balls Reveal the Metric |
| 15 | S31 | 478 | Orthogonal Maps Preserve Geometry |
| 16 | S33 | 513 | Why Length Is Preserved |
| 17 | S66 | 526 | Spectral Norm: Worst Stretch |
| 18 | S72 | 563 | Frobenius Norm: Total Energy |
| 19 | S35 | 588 | Reading an SVD |
| 20 | S36 | 595 | Recall: Symmetric Eigendecomposition |
| 21 | S38 | 605 | Every Matrix Has an SVD |
| 22 | S39 | 619 | Read the Factor Shapes |
| 23 | S40 | 653 | Rotate, Stretch, Rotate |
| 24 | S52 | 671 | First Change the Input Coordinates |
| 25 | S53 | 714 | Then Stretch and Reorient |
| 26 | S41 | 757 | A Sum of Rank-One Layers |
| 27 | S42 | 782 | Compact SVD Keeps Active Directions |
| 28 | S44 | 810 | One Matrix, One Construction |
| 29 | S45 | 828 | Build the Symmetric Matrix $A^{\top}A$ |
| 30 | S46 | 840 | The Eigenvalues Are 45 and 5 |
| 31 | S47 | 853 | Orthonormal Input Directions |
| 32 | S48 | 867 | Recover Stretches and Output Directions |
| 33 | S49 | 881 | The Factors Reconstruct $A$ |
| 34 | S50 | 895 | The First Layer Carries Most Energy |
| 35 | S51 | 907 | Eigenvalues Are Not Singular Values |
| 36 | S68 | 930 | Largest Singular Value, Largest Stretch |
| 37 | S69 | 951 | No Direction Beats the Largest Stretch |
| 38 | S70 | 966 | The First Singular Vector Attains It |
| 39 | S73 | 978 | Frobenius Energy Sums Squared Stretches |
| 40 | S74 | 991 | Orthogonal Coordinates Preserve Total Energy |
| 41 | S79 | 1006 | Best Low-Rank Approximation |
| 42 | S81 | 1013 | Candidate: Keep the $k$ Largest Layers |
| 43 | S82 | 1023 | Worked: $A_1$ Is the Top Layer of $A$ |
| 44 | S83 | 1038 | Worked: $A_1$'s Error Is the Discarded Layer |
| 45 | S90 | 1049 | Eckart–Young–Mirsky: Spectral Error |
| 46 | S91 | 1063 | Optimal: a Floor for All, Met by One |
| 47 | S85 | 1094 | Recall: Low Rank Forces a Big Null Space |
| 48 | S86 | 1106 | Large Subspaces Must Intersect |
| 49 | S87 | 1119 | Two Planes in $\mathbb{R}^3$ Share a Line |
| 50 | S88 | 1142 | One Unit Witness Bounds the Maximum |
| 51 | S89 | 1154 | Top $k{+}1$ Directions Stretch by $\geq \sigma_{k+1}$ |
| 52 | S92 | 1166 | Proof Plan: Find One Witness |
| 53 | S93 | 1181 | Step 1: Every Competitor Has a Blind Spot |
| 54 | S94 | 1191 | Step 2: $A$ Stays Strong on $W$ |
| 55 | S95 | 1204 | Step 3: The Two Subspaces Share a Unit $w$ |
| 56 | S96 | 1213 | Step 4: Along $w$, the Residual Is $A$ |
| 57 | S97 | 1227 | Step 4 (continued): The Witness Is Not Small |
| 58 | S98 | 1237 | Step 5: Truncation Meets the Bound |
| 59 | S99 | 1247 | One Chain Proves the Spectral Theorem |
| 60 | S101 | 1263 | Eckart–Young–Mirsky: Frobenius Error |
| 61 | S121 | 1277 | $A_k$'s Error Is the Discarded Energy |
| 62 | S116 | 1293 | Read the Answer |
| 63 | S102 | 1300 | The Best Rank-One Error Is $\sqrt{5}$ |
| 64 | S103 | 1313 | One Layer Keeps 90% of the Energy |
| 65 | S122 | 1333 | Worst Error and Total Error Can Differ |
| 66 | S123 | 1345 | What the Guarantee Covers |
| 67 | S117 | 1367 | From Directions to the Optimal Error |
| 68 | S119 | 1385 | (closer) |

# Additional resolved opt02 choices

9. Remove the two-dimensional quadratic running example and repeated tables: S30/S83/S84/S126. Generalize S65 and remove running-example references throughout core notes. Generic concept pictures remain. C18 separately deletes S136 (baseline page 24).
10. C15 permits animation: use an instructor-advanced build of the upper model and GD step. No auto-play, numerical iteration table or new library. Static print/export and verbal notes must remain complete.
11. C16: state the standard smooth quadratic upper bound as a lemma, then derive the step by completing a square and establish decrease by substitution. This is an elementary GD argument, not a proof of the lemma. The formal integral derivation becomes optional detail. Do not silently strengthen L-smoothness to twice differentiability.
12. C17: yes, globally L-smooth, bounded-below f with step 1/L gives convergence of the entire gradient-norm sequence to zero, by summability of squared norms. O(1/T) is for the best squared gradient or its average; the best unsquared norm is O(1/sqrt(T)). No last-iterate O(1/T), iterate convergence or local-minimum guarantee. A finite lower bound suffices, without an attained objective minimum. Distinguish the minimum over iterates from an objective minimizer.
13. C19: Garrigos & Gower correctly exposes both formulas but did not originate them. Keep it for the precise bounds and add Nesterov (2004) as an earlier standard reference. Remove author/year attribution from theorem headings. Earliest historical priority for either exact formulation is not established by this limited check; do not invent an original-author claim.
14. Keep simplest fixed-step proofs, strong convexity and q=0 edge case. No co-coercivity or PL in the core. Do not refill removed arithmetic to hit a page quota.

# Opt02 baseline page manifest

IDs below belong to opt02, not opt01.

| Baseline page | ID | Source line | Title |
|---:|---|---:|---|
| 1 | S01 | 66 | Gradient Descent:Three Guarantees |
| 2 | S02 | 77 | Contents |
| 3 | S79 | 135 | One Update |
| 4 | S80 | 142 | Goal: Minimize One Differentiable $f$ |
| 5 | S14 | 167 | Recall: The Gradient Gives First-Order Change |
| 6 | S82 | 178 | Small Steps Against the Gradient Go Downhill |
| 7 | S27 | 212 | $L$-Smoothness Bounds Gradient Change |
| 8 | S81 | 226 | One Fixed Step: $1/L$ |
| 9 | S30 | 242 | Running Example: $L = 4$ |
| 10 | S25 | 258 | One Descent Inequality |
| 11 | S33 | 265 | Smoothness Gives a Quadratic Upper Bound |
| 12 | S34 | 278 | The Upper Bound Touches $f$ at $x$ |
| 13 | S36 | 305 | Proof Step 1: Follow the Segment |
| 14 | S37 | 318 | Proof Step 2: Smoothness Bounds the Drift |
| 15 | S38 | 331 | Proof Step 3: Integrating $s$ Gives $\tfrac{1}{2}$ |
| 16 | S90 | 343 | The Step $1/L$ Decreases $f$ |
| 17 | S83 | 356 | One Step Zeroes the Stiff Coordinate |
| 18 | S84 | 369 | Two Steps: $f$ Falls From $10$ to $81/128$ |
| 19 | S135 | 390 | Nonconvex: Stationarity |
| 20 | S89 | 397 | Nonconvex Guarantee: Small Squared Gradient |
| 21 | S91 | 410 | Proof Step 1: Sum the Decreases |
| 22 | S92 | 423 | Proof Step 2: Minimum at Most Average |
| 23 | S93 | 435 | Stationary Does Not Mean Minimum |
| 24 | S136 | 458 | GD Can Stay at a Maximum |
| 25 | S137 | 482 | The Square Changes the Rate |
| 26 | S09 | 498 | Convex: Optimality |
| 27 | S10 | 505 | Convexity Puts Chords Above |
| 28 | S15 | 539 | The Tangent Lies Below |
| 29 | S95 | 568 | Assume an Optimum Exists |
| 30 | S96 | 602 | Convex: $O(1/T)$ Function Gap |
| 31 | S97 | 616 | Proof Plan: Spend Distance |
| 32 | S98 | 631 | Recall: One-Step Decrease |
| 33 | S99 | 640 | Use the Tangent at $x_t$ |
| 34 | S101 | 650 | Expand the Squared Distance |
| 35 | S104 | 662 | Distances Telescope |
| 36 | S105 | 675 | The Last Gap Is Smallest |
| 37 | S106 | 685 | The Convex Proof in One Chain |
| 38 | S63 | 701 | Strongly Convex: Geometric Decay |
| 39 | S64 | 708 | Add a Quadratic Floor |
| 40 | S65 | 720 | Curvature Is Bounded Below |
| 41 | S116 | 750 | Strongly Convex: Geometric Convergence |
| 42 | S138 | 764 | Keep the Extra Curvature Term |
| 43 | S139 | 776 | Nonnegative Gap Forces Contraction |
| 44 | S122 | 786 | Repeat the Same Contraction |
| 45 | S123 | 796 | Function Values Follow Distance |
| 46 | S110 | 806 | Linear Means Geometric |
| 47 | S126 | 842 | The Example Beats Its Bound |
| 48 | S130 | 859 | Three Guarantees |
| 49 | S131 | 866 | Three Assumptions, Three Guarantees |
| 50 | S140 | 879 | No Extra Conditions Needed |
| 51 | S134 | 905 | $x_{t+1} = x_t - \tfrac{1}{L}\, \nabla f(x_t)$ |
