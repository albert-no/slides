job: 2026-11-23-opt01-opt03-four-hour-core
size: large
deck: courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html; courses/deepmath/opt02-convexity-gd/opt02-convexity-gd.html (renamed from opt03); matching notes and courses/deepmath/opt03-backup/
audience / mode / duration: junior undergraduate AI majors / rigorous but narrowly scoped / 240 minutes total
baseline: 99cf2a220a92c83e938167c05745af15d9bafe13
id commit: 01ba79c7b18bb7538c0c8bcd34f6141dd604d075
branch: 2026-11-23-opt01-opt03-four-hour-core
reviewed candidate: 1f220ef63a13fb45ee38350bc06d498c0e6b4872
relocation starting point: 3d427a6cc1a2e447179a58e8ce5d9442e947363d
pr: 80 — https://github.com/albert-no/slides/pull/80
state: in-work
round: 3 of 3
albert decisions:
  - 2026-11-23: requested restructure for remaining six lecture hours: prob09 two hours, SVD/low-rank and simplest GD four hours; final in week 15.
  - 2026-11-23 16:22 Asia/Seoul: Albert said "go ahead" (C11), approving stages 1–3, the 150+90-minute split, strong convexity retained, co-coercivity/PL backup-only, and corrected nonconvex stationarity target.
  - 2026-11-23: plan-v1.md complete; round-1 work order assigned to slides on the recorded branch.
  - 2026-11-23: review-r1 verdict revise on 19e8acfdcb736b6232d820324c0bb5d64cfe6259; F01–F09 blocking, F10 optional. Round-2 work order is review-r1.md; argument and 150+90-minute allocation unchanged.
  - 2026-11-23: review-r2 approved exact commit 1f220ef63a13fb45ee38350bc06d498c0e6b4872; F01–F10 closed. Await final log-only push before PR; no merge authorized.
  - 2026-11-23: final record commit 3d427a6cc1a2e447179a58e8ce5d9442e947363d verified pushed and log-only after the approved content SHA; all job copies match. PR #80 opened against main via GitHub REST API. Await Albert final check; not merged.
  - 2026-11-24 14:20 Asia/Seoul: Albert requested temporary consecutive opt01/opt02 folders and filenames, with all remaining optimization material physically in opt03-backup (C12–C14). Same PR #80; no merge order.
  - 2026-11-24: plan-v2.md is the round-3 work order from pushed SHA 3d427a6cc1a2e447179a58e8ce5d9442e947363d. Prior content approval remains historical; new packaging awaits review. Size stays large; bounded relocation, no new mathematical argument or teaching-time change.
  - Current execution specification: plan-v2.md plus unchanged plan-v1 slide specs; stage 1–3 text below is historical and its original-path constraints are superseded by C12–C14.

# Size and work boundary

Large because this changes the structure and teaching scope of two substantial decks, not because new literature is needed. Stage 1–3 proposal is complete; no implementation work order or full slide-level plan has been issued. Albert approves before slides builds. slides-review owns planning/review/PR; slides alone edits decks, notes, backups, outlines and scripts. Maximum three review rounds.

Confirmed mounts with findmnt on 2026-11-23: `/workspace/extra/slides` read-only; `/workspace/extra/slides-log` read-write. This working folder is untracked. Baseline is the exact commit above, not a moving branch.

# Stage 1 — Audience, scope, objectives and exclusions

## Audience and teaching mode

Reuse the course's junior-undergraduate mathematical mode. Keep clear intuition, statements with assumptions, and short complete proofs of the selected central results. Reduce the number of topics rather than shrinking type or making remaining proofs cryptic. No new activities or assigned exercises planned; worked examples are lecturer-led.

## Deliverables proposed for approval

1. Revised opt01 main deck: **SVD and Best Low-Rank Approximation**, 150 minutes.
2. Revised opt03 main deck: **Gradient Descent: Three Guarantees**, 90 minutes.
3. Matching HTML notes plus synchronized, standalone screen-reader Markdown editions for both, preserving the course's ASCII/LaTeX/verbal-figure/linearized-table accessibility contract.
4. Separate backup decks and companion notes preserving material removed from these mains. Existing opt02 and opt04 stay available as backup-only course material, without substantive rewriting. Their packaging/location will be specified in the full plan; no old material is silently deleted.
5. Updated course outline/navigation distinguishing this year's two active decks from backup-only material. Do not rename the whole series to lec01–lec11.

Use existing opt01/opt03 main paths to avoid unnecessary new numbering. All backup material is outside the 240-minute lecture path. No PDF delivery unless requested.

## Schedule proposal

- Week 13: prob09, 120 minutes (already uploaded; untouched), then first 60 minutes of opt01.
- Week 14: remaining 90 minutes of opt01, then opt03, 90 minutes.
- Week 15: final exam. No exam editing in this job.

These are allocations of Albert's six available lecture hours, including ordinary recap/questions; slide counts remain targets, not limits.

## Learning objectives

- Explain singular values through orthogonal changes of coordinates and rank-one components.
- Distinguish vector norms, spectral matrix norm and Frobenius matrix norm; measure what a low-rank approximation loses.
- State and interpret Eckart–Young–Mirsky in spectral and Frobenius forms, follow the spectral optimality proof, and compute a truncation/error example.
- Run deterministic GD with one fixed step, 1/L; understand why smoothness gives descent.
- Distinguish nonconvex stationarity, convex O(1/T) function-gap convergence, and strongly convex geometric convergence to the optimum.

## Scope decisions proposed [judgment]

- C04 means remove the existing “The Optimization Half” opening (baseline opt01 pp3–5), not remove the low-rank minimization problem needed to state EYM. Replace the multi-lecture roadmap with a direct approximation motivation.
- Keep rank, null space and the dimension argument only to the depth needed by SVD/EYM. Recall symmetric eigendecomposition and orthogonality from existing Gaussian work, rather than reteaching a separate linear-algebra course.
- Vector l1/l2/linfinity comparison remains brief; spectral and Frobenius are the main matrix norms. Nuclear norm and convex rank relaxation go to backup.
- SVD existence: constructive explanation via A^T A, one running worked example, full derivation in notes; no separate lengthy existence-proof lecture.
- EYM: full spectral proof in class, Frobenius exact statement and residual-energy explanation; complete Frobenius optimality derivation in notes/backup, clearly distinguished from achievability. General unitarily invariant norm theorem is backup.
- GD: keep strong convexity; remove co-coercivity, the standalone PL condition and their proof chains from the main deck. Use E07's shared descent/distance proof. No hidden need to study backup to follow a main theorem.
- Pseudoinverse, detailed four-subspace theory, matrix completion/Netflix relaxation, extra norm theory, extended GD step-size optimization, monotone-operator arguments, PL generalizations, least-squares/ridge and SGD stay backup-only.
- prob01–prob09 are untouched. No probability-topic pruning or future lec renumbering. No acceleration, adaptive optimization, saddle-escape survey or new research survey.
- Evidence cutoff: 2026-11-23, with textbook-level sources (evidence.md); no novelty claims required.

# Stage 2 — Evidence map and resolution of conflicting targets

| Teaching claim | Evidence | What the main deck must not imply |
|---|---|---|
| SVD exposes orthogonal directions and singular values | E02, E08 | eigenvalues and singular values coincide for all matrices |
| Spectral vs Frobenius quantify different residuals | E02–E03, E08 | both error formulas agree generally |
| Truncated SVD solves fully observed low-rank approximation | E03 | same theorem solves missing entries or guarantees denoising/prediction |
| Smoothness + fixed step gives descent | E06–E07 | differentiability alone supplies a safe step |
| Nonconvex best squared gradient O(1/T) | E06, E08 | convergence to local optimum; last-iterate O(1/T) gradient bound |
| Convex function gap O(1/T) | E04, E07 | geometric convergence from convexity alone |
| Strongly convex geometric convergence | E05, E07 | a separate PL or co-coercivity prerequisite is required |

## C09: mathematical correction requiring explicit approval

The requested learning progression is retained, but the wording must change:

- Strongly convex + L-smooth: **geometric/exponential convergence to the unique global optimum**, commonly called **linear convergence** in optimization.
- Convex + L-smooth + attained minimum: **O(1/T) function gap to the global optimum**, called **sublinear**, not linear.
- General nonconvex + L-smooth + lower bound: **O(1/T) best squared gradient norm**, hence approximate stationarity. This is not a rate to a local minimum and does not guarantee one.

No additional saddle-avoidance assumptions are smuggled in to make the original wording true. A single stationary-but-not-minimizing example makes the limit explicit (E08). If Albert wants a conditional local-minimum theorem, return to scope approval rather than silently adding a technical detour.

# Stage 3 — Argument, title sequence and time budget

## Argument

**Structure gives a closed-form best approximation; otherwise an iterative method earns only the guarantee justified by its assumptions.** SVD/EYM is the centerpiece. GD is a compact final mathematical tool, not the start of four more optimization lectures.

## opt01: SVD and Best Low-Rank Approximation — 150 minutes

| Block | Target title sequence (not a fixed slide count) | Minutes | Main/notes boundary |
|---|---|---:|---|
| 1. Why low rank? | A Smaller Matrix, Controlled Error → Rank Counts Independent Directions → A Competitor Can Miss Directions | 15 | short motivation and rank/nullity recall; full foundational proofs in notes/backup |
| 2. Measuring error | Different Norms, Different Questions → Rotations Preserve Euclidean Length → Worst Direction or Total Error? | 25 | l1/l2/linfinity orientation; define operator and Frobenius norms; their singular-value identities follow SVD |
| 3. Reading an SVD | Rotate, Stretch, Rotate → Singular Values from A^T A → A Sum of Rank-One Layers → One Matrix, Worked Through → Norms Read from Singular Values | 45 | one complete small example; compact/full dimensions clear; excess example variants in backup |
| 4. Best low-rank approximation | Keep the Largest Components → Eckart–Young–Mirsky → Every Competitor Has a Blind Spot → A Strong Direction Survives → Truncation Meets the Lower Bound → Discarded Energy Sets Frobenius Error | 55 | full spectral proof with prerequisite recall; Frobenius theorem and energy explanation; full second proof in notes/backup |
| 5. Read the answer | Choose Rank by Residual Error → What the Guarantee Covers | 10 | contrast spectral/Frobenius residual with a rank>1 residual example; one closing synthesis |

Natural week boundary after about 60 minutes: foundations and SVD geometry, then resume with a short content recall. No “next week” or numbered-deck dependency language on normal slides.

## opt03: Gradient Descent: Three Guarantees — 90 minutes

| Block | Target title sequence (not a fixed slide count) | Minutes | Main/notes boundary |
|---|---|---:|---|
| 1. One update | A Gradient Gives a Direction → One Fixed Step: 1/L → Smoothness Controls the Step | 15 | standalone objective and gradient recall; no dependency on opt02 |
| 2. One descent inequality | A Quadratic Upper Bound → The Step Decreases the Objective → One Quadratic, Worked Through | 15 | short descent-lemma proof and numeric illustration; arbitrary-step investigations backup |
| 3. Nonconvex guarantee | Small Gradient, Not Necessarily Minimum → Sum the Decreases → O(1/T) for Squared Gradient | 15 | lower bound and best-iterate quantifier on the theorem slide; counterexample on main |
| 4. Convex guarantee | A Tangent Lies Below → Distance Pays for Function Error → Telescope to O(1/T) | 20 | first-order convexity; distance identity; complete short proof, no co-coercivity |
| 5. Strongly convex guarantee | Add a Quadratic Floor → Distance Contracts Geometrically → Linear Means Geometric | 20 | same proof with extra curvature term; optimizer/function-gap distinction explicit, no PL theorem |
| 6. Close | Three Assumptions, Three Guarantees | 5 | one summary with target quantity and assumptions; no promise of an SGD lecture |

Timing includes explanation and ordinary questions. Do not add a second proof route merely because it existed in the baseline.

## Coverage / disposition table

| Comment | Baseline location / title | Planned disposition | Later package |
|---|---|---|---|
| C01–C03 | course outline; both deck openings | two active decks, 150+90 minutes; prob09 untouched | shared/course surfaces |
| C04 | opt01 pp3–5, “The Optimization Half”, “Where the Probability Half Stopped”, “The Optimization Half, in Four Steps” | replace in main; preserve old opening in full backup | P1 |
| C05 | opt01 pp10–54, pp64–104 | keep just EYM prerequisites, SVD/norms, spectral proof and both error formulas | P1–P3 |
| C06 | opt01 pp55–63, 76–78, 105–115 and other trimmed material | explicit backup coverage, including paired note detail | P5 |
| C07 | course-wide numbering; prob01–prob09 | no changes; future reorganization excluded | shared/course surfaces |
| C08 | opt03 pp9–47, 63–78, 79–129 | simplest complete deterministic GD path, three guarantee levels | P4 |
| C09 | opt03 pp48–62 co-coercivity; pp73–78 PL; pp89–129 convergence | co-coercivity/PL backup; strong convexity main; corrected rate targets awaiting approval | P4–P5 |
| C10 | opt01/opt03, plus opt02/opt04 as excluded teaching material | two revised mains, preserved backups; no substantive opt02/04 rewrite | all |

## Preliminary work boundaries (not a work order)

P1 foundations/motivation; P2 SVD/norm identities; P3 EYM; P4 simplest GD; P5 archival/backup preservation. slides will own shared Contents/dividers/counts/OUTLINE/navigation after its content work. Detailed ID-level specs and file allowlists will be written only after approval as `plan-v1.md`.

Baseline decks lack slide IDs. Their notes are section-oriented, not one article per slide. Before implementation, the full plan must specify a contract-compliant ID-only baseline step and separate semantic note migration; do not mislabel rewritten notes as an ID-only change. Stable IDs must be paired in final slide/note articles, including a reported mapping for splits/moves into backup.

# Approval gate

Await Albert's approval of the scope, evidence-based convergence correction, two-deck 150+90-minute argument and teaching sequence above. Then prepare the full slide-level plan and send slides the contract pointer. No branch/deck changes requested yet. No PR until review approval and pushed job record.

# Frozen baseline page manifest

Pages include all structural slides. These are exact baseline titles and source lines, not instructions to implement by line number. IDs are unassigned until slides' ID-only commit.

## courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html

| Page | Line | Baseline title |
|---:|---:|---|
| 1 | 43 | SVD & Low-Rank Approximation |
| 2 | 55 | Contents |
| 3 | 135 | The Optimization Half |
| 4 | 143 | Where the Probability Half Stopped |
| 5 | 157 | The Optimization Half, in Four Steps |
| 6 | 192 | Deep Learning Optimizes Matrices |
| 7 | 216 | SVD = the X-Ray |
| 8 | 230 | Low Rank Is Everywhere |
| 9 | 254 | Route Map |
| 10 | 293 | Rank, Range, Null Space |
| 11 | 301 | A Matrix, Column by Column |
| 12 | 314 | Definition — Span & Range |
| 13 | 326 | Worked — a Collapsing Matrix |
| 14 | 355 | Definition — Rank |
| 15 | 367 | Worked — Ranks by Inspection |
| 16 | 383 | Definition — Null Space |
| 17 | 397 | Worked — Null Space of $C$ |
| 18 | 410 | Theorem 1 — Rank–Nullity |
| 19 | 423 | Rank–Nullity — Sanity Checks |
| 20 | 438 | Rank–Nullity — the Picture |
| 21 | 475 | Definition — Orthogonal Complement |
| 22 | 487 | Theorem 2 — Split Any Vector |
| 23 | 528 | Theorem 3 — the Four Subspaces |
| 24 | 544 | Why AI Cares About Rank |
| 25 | 558 | Norms & Orthogonal Matrices |
| 26 | 566 | How Long Is a Vector? |
| 27 | 578 | Definition — Norm |
| 28 | 592 | The $\ell_p$ Family |
| 29 | 605 | Worked — One Vector, Three Norms |
| 30 | 619 | Unit Balls — the Norms as Shapes |
| 31 | 645 | Definition — Orthogonal Matrix |
| 32 | 658 | Example — Rotation by 45° |
| 33 | 672 | Theorem 4 — Orthogonal Maps Preserve Length |
| 34 | 686 | Implication — Rotations Are Free |
| 35 | 700 | The Singular Value Decomposition |
| 36 | 708 | Recall — Eigendecomposition |
| 37 | 722 | Technique Review — Eigen vs Singular |
| 38 | 745 | Theorem 5 — the SVD Exists |
| 39 | 759 | Reading the Shapes (Full SVD) |
| 40 | 789 | What Each Factor Does |
| 41 | 802 | Technique Review — the Outer-Product View |
| 42 | 829 | Thin (Compact) SVD |
| 43 | 856 | Thin Factors Are Not Orthogonal Matrices |
| 44 | 869 | Worked — SVD by Hand: the Plan |
| 45 | 883 | Worked — Step 1: Form $A^{\top}A$ |
| 46 | 896 | Worked — Step 2: Eigenvalues |
| 47 | 906 | Worked — Step 2: Eigenvectors |
| 48 | 922 | Worked — Step 3: Sigmas and $u_i$ |
| 49 | 936 | Worked — Step 4: Assemble |
| 50 | 947 | Worked — Verify via Rank-1 Layers |
| 51 | 959 | Eigenvalues $\neq$ Singular Values |
| 52 | 973 | Circle to Ellipse — Rotate First |
| 53 | 1015 | Circle to Ellipse — Stretch, Then Rotate Back |
| 54 | 1057 | SVD — What to Remember |
| 55 | 1071 | The Pseudo-Inverse |
| 56 | 1079 | When $A^{-1}$ Doesn't Exist |
| 57 | 1093 | Definition — Moore–Penrose Pseudo-Inverse |
| 58 | 1108 | Worked — $A^{\dagger}$ for the Running Matrix |
| 59 | 1120 | Worked — $A^{\dagger}$, Finished |
| 60 | 1134 | Worked — the Rank-Deficient Case |
| 61 | 1147 | Sanity Check — $A A^{\dagger} A = A$ |
| 62 | 1163 | $AA^{\dagger}$ and $A^{\dagger}A$ Are Projections |
| 63 | 1176 | Teaser — Solving the Unsolvable |
| 64 | 1189 | Matrix Norms |
| 65 | 1197 | Two Ways to Measure a Matrix |
| 66 | 1218 | Definition — Induced (Operator) Norm |
| 67 | 1234 | The Inequality It's Built For |
| 68 | 1246 | Theorem 6 — Spectral Norm $=$ Top Sigma |
| 69 | 1258 | Proof (Thm 6) — No Vector Beats $\sigma_1$ |
| 70 | 1272 | Proof (Thm 6) — And $v_1$ Achieves It |
| 71 | 1285 | Worked — Max Stretch of $A$ |
| 72 | 1295 | Definition — Frobenius Norm |
| 73 | 1310 | Theorem 7 — Frobenius via Sigmas |
| 74 | 1321 | Proof (Thm 7) — One Trace Chain |
| 75 | 1333 | Worked — $\\|A\\|_F$ Two Ways |
| 76 | 1342 | Definition — Nuclear Norm |
| 77 | 1354 | One Vector, Three Norms |
| 78 | 1368 | Nuclear Norm $\approx$ Convex Rank |
| 79 | 1382 | Best Low-Rank Approximation |
| 80 | 1390 | The Compression Question |
| 81 | 1403 | The Candidate — Truncated SVD |
| 82 | 1416 | Worked — $A_1$ for the Running Matrix |
| 83 | 1429 | Worked — the Error of $A_1$ |
| 84 | 1440 | The Claim |
| 85 | 1453 | Technique Review 1 — Rank–Nullity |
| 86 | 1468 | Technique Review 2 — Big Subspaces Must Meet |
| 87 | 1482 | Picture — Two Planes in $\mathbb{R}^3$ |
| 88 | 1499 | Technique Review 3 — Bounding a Max From Below |
| 89 | 1511 | Technique Review 4 — $\\|Aw\\|^2$ in the $v$-Basis |
| 90 | 1522 | Theorem 8 — Eckart–Young–Mirsky |
| 91 | 1537 | Reading the Statement |
| 92 | 1549 | Proof Overview (Spectral Case) |
| 93 | 1562 | Step 1 — Every Competitor Has a Blind Spot |
| 94 | 1575 | Step 2 — Where $A$ Is Still Strong |
| 95 | 1587 | Step 3 — The Two Subspaces Collide |
| 96 | 1599 | Step 4 — The Witness Bound |
| 97 | 1612 | Step 4, Finished — $A$ Is Strong at $w$ |
| 98 | 1624 | Step 5 — Truncation Hits the Floor |
| 99 | 1638 | Proof Summary — the Skeleton |
| 100 | 1657 | The Key Trick, Named |
| 101 | 1672 | The Frobenius Case |
| 102 | 1686 | Worked — EYM on the Running Matrix |
| 103 | 1697 | How Much Did $A_1$ Keep? |
| 104 | 1725 | Implication — the License to Truncate |
| 105 | 1739 | Netflix & Matrix Completion |
| 106 | 1747 | The Recommendation Problem |
| 107 | 1761 | Worked — a Tiny Ratings Matrix |
| 108 | 1776 | Only Two Taste Patterns |
| 109 | 1788 | Rank 2 $=$ Tastes $\times$ Genres |
| 110 | 1801 | Worked — Fill In the Blanks |
| 111 | 1811 | Formalizing — the Observed Set $\Omega$ |
| 112 | 1822 | The Ideal Program — and Its Problem |
| 113 | 1835 | The Convex Relaxation |
| 114 | 1846 | Why the Relaxation Is a Win |
| 115 | 1858 | The Same Shape, Everywhere in AI |
| 116 | 1873 | Closing |
| 117 | 1881 | Every Tool, One Line Each |
| 118 | 1897 | Next — Least Squares |
| 119 | 1911 | (closer without heading) |

## courses/deepmath/opt03-convexity-gd/opt03-convexity-gd.html

| Page | Line | Baseline title |
|---:|---:|---|
| 1 | 50 | Convexity & Gradient Descent |
| 2 | 62 | Contents |
| 3 | 142 | Why Convexity? |
| 4 | 150 | When the Formula Runs Out |
| 5 | 165 | Three Questions About One Update |
| 6 | 188 | Today's Three Results |
| 7 | 206 | The Constants Are Learning-Rate Theory |
| 8 | 220 | Route Map |
| 9 | 269 | Convexity |
| 10 | 277 | Definition — Convex Function |
| 11 | 292 | Chord Above the Graph |
| 12 | 320 | Convex vs. Nonconvex |
| 13 | 349 | Why AI Cares |
| 14 | 363 | The Gradient, Recalled |
| 15 | 379 | First-Order Characterization |
| 16 | 394 | Tangent Below the Graph |
| 17 | 415 | Why — the 1D Picture |
| 18 | 430 | The Hessian, Recalled |
| 19 | 445 | Recall — PSD |
| 20 | 460 | Theorem 1 — Second-Order Characterization |
| 21 | 473 | Worked — Is It Convex? |
| 22 | 485 | Worked — a Saddle Is Not Convex |
| 23 | 498 | The Running Example |
| 24 | 514 | Running Example — Contours |
| 25 | 540 | Smoothness |
| 26 | 548 | Lipschitz Continuity |
| 27 | 563 | Definition — $L$-Smooth |
| 28 | 578 | Theorem 2 — Bounded Hessian |
| 29 | 593 | Proof Sketch — as in the Notes |
| 30 | 607 | Running Example — $L = 4$ |
| 31 | 620 | Technique Review — Restrict to a Segment |
| 32 | 635 | Technique Review — Cauchy–Schwarz |
| 33 | 649 | Lemma 1 — the Descent Lemma |
| 34 | 661 | The Picture — a Parabola Lid |
| 35 | 687 | Descent Lemma — Proof Overview |
| 36 | 700 | Step 1 — Set Up $g$ |
| 37 | 712 | Step 2 — Bound the Slope Drift |
| 38 | 724 | Step 3 — Integrate |
| 39 | 736 | Proof Summary — the Skeleton |
| 40 | 749 | What the Descent Lemma Buys |
| 41 | 763 | Theorem 3 — the Smoothness Sandwich |
| 42 | 775 | Reading the Statement |
| 43 | 787 | Proof — Right Side |
| 44 | 801 | Proof — Left Side, the Idea |
| 45 | 814 | Proof — Left Side, Minimize the Lid |
| 46 | 825 | Proof — Left Side, Best Direction |
| 47 | 836 | Sandwich, Checked on the Running Example |
| 48 | 849 | Smooth and Convex |
| 49 | 857 | Two Bounds Meet |
| 50 | 871 | Lemma 2 — Co-coercivity |
| 51 | 884 | What Co-coercivity Says |
| 52 | 898 | Proof of (i) — Overview |
| 53 | 912 | Proof of (i) — One Point, Two Bounds |
| 54 | 925 | Proof of (i) — Chain and Rearrange |
| 55 | 937 | Proof of (i) — the Best $z$ |
| 56 | 949 | Proof of (ii) — Overview |
| 57 | 963 | Proof of (ii) — the Tilted Function |
| 58 | 977 | Proof of (ii) — Apply the Sandwich |
| 59 | 989 | Proof of (ii) — Symmetrize |
| 60 | 1000 | Proof of (ii) — Add Them |
| 61 | 1013 | Proof Summary — Co-coercivity |
| 62 | 1024 | Co-coercivity, Checked on the Running Example |
| 63 | 1036 | Strong Convexity |
| 64 | 1044 | Definition — $\mu$-Strongly Convex |
| 65 | 1059 | The Two-Parabola Sandwich |
| 66 | 1085 | Theorem 4 — Hessian Floor |
| 67 | 1101 | Recall — Ridge Buys $\mu$ |
| 68 | 1115 | Theorem 5 — Gradient Monotonicity |
| 69 | 1130 | Proof — Add Two Floors |
| 70 | 1143 | Theorem 6 — Strong Monotonicity |
| 71 | 1157 | Proof — Same Trick, Stronger Floors |
| 72 | 1170 | Technique Review — Completing the Square |
| 73 | 1185 | Lemma 3 — the PL Condition |
| 74 | 1197 | Reading PL — Gradient Norm Measures the Gap |
| 75 | 1210 | Proof of PL — Rearrange the Floor |
| 76 | 1221 | Proof of PL — Complete the Square |
| 77 | 1234 | PL, Checked on the Running Example |
| 78 | 1246 | PL as an Assumption of Its Own |
| 79 | 1260 | Gradient Descent |
| 80 | 1268 | The Problem |
| 81 | 1280 | The Algorithm |
| 82 | 1298 | 1D Intuition — the Sign Does the Steering |
| 83 | 1327 | Running Example — GD, Set Up by Hand |
| 84 | 1339 | Four Iterations by Hand ($\alpha = 1/4$) |
| 85 | 1357 | The Path on the Contours ($\alpha = 1/4$) |
| 86 | 1387 | Bigger Step — Zigzag ($\alpha = 0.45$) |
| 87 | 1417 | Too Big — Divergence ($\alpha = 0.6 \gt 2/L$) |
| 88 | 1445 | Three Step Sizes, One Lesson |
| 89 | 1464 | Theorem 7 — GD Converges (Smooth Case) |
| 90 | 1478 | Proof — One Step Through the Lid |
| 91 | 1491 | Proof — Monotone and Bounded |
| 92 | 1504 | Proof — Gradients Must Vanish |
| 93 | 1517 | Reading the Theorem |
| 94 | 1531 | Rate I — $O(1/T)$ |
| 95 | 1539 | Assumptions and Goal |
| 96 | 1551 | Theorem 8 — $O(1/T)$ Convergence |
| 97 | 1564 | Proof Overview |
| 98 | 1577 | Step 1 — Guaranteed Decrease |
| 99 | 1591 | Step 2 — Bring In the Optimum |
| 100 | 1602 | Technique Review — the Square, Completed Again |
| 101 | 1617 | Step 3 — the Distance Identity |
| 102 | 1631 | Corollary — the Distance Also Shrinks |
| 103 | 1643 | Technique Review — Telescoping Sums |
| 104 | 1657 | Step 4 — Telescope |
| 105 | 1671 | Step 5 — From Sum to Last Iterate |
| 106 | 1684 | Proof Summary — the Skeleton |
| 107 | 1697 | Corollary — Iteration Complexity $O(1/\varepsilon)$ |
| 108 | 1710 | Bound vs. Reality on the Running Example |
| 109 | 1730 | Rate II — Linear |
| 110 | 1738 | The Goal — From $1/T$ to $c^{\,T}$ |
| 111 | 1751 | Theorem 9 — Subtract the Floor |
| 112 | 1765 | What $h$ Knows About $f$ |
| 113 | 1778 | Co-coercivity, Applied to $h$ |
| 114 | 1791 | Unpack — Expand the Square |
| 115 | 1802 | Unpack — Collect Terms |
| 116 | 1816 | Theorem 10 — Linear Convergence |
| 117 | 1831 | Proof Overview |
| 118 | 1844 | Step 1 — Expand the Square |
| 119 | 1857 | Step 2 — Co-coercivity at the Optimum |
| 120 | 1869 | Step 3 — Group; Kill the Gradient Term |
| 121 | 1882 | Technique Review — Unrolling a Recursion |
| 122 | 1895 | Step 4 — Unroll |
| 123 | 1907 | Step 5 — Function Values Follow |
| 124 | 1919 | Proof Summary — the Skeleton |
| 125 | 1933 | Remark — $O(\log(1/\varepsilon))$ Iterations |
| 126 | 1946 | Running Example — Contraction, Measured |
| 127 | 1965 | Geometric Shrinkage, Drawn |
| 128 | 2006 | Bonus — PL Alone Gives the Linear Rate |
| 129 | 2018 | Bonus — Unroll the PL Rate |
| 130 | 2030 | Closing |
| 131 | 2038 | Every Tool, One Line Each |
| 132 | 2058 | The Constants You Now Own |
| 133 | 2072 | Next — Stochastic Gradients |
| 134 | 2087 | $x^{+} = x - \alpha\, \nabla f(x)$ |
