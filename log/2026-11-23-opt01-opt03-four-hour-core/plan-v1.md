# plan-v1 — Four-hour SVD/EYM and GD core

## 1. Approved brief and boundaries

**Job:** `2026-11-23-opt01-opt03-four-hour-core`. **Baseline:** `99cf2a220a92c83e938167c05745af15d9bafe13`. **Branch:** same as job ID. Albert approved stages 1–3 with “go ahead” on 2026-11-23 at 16:22 Asia/Seoul (C11). This is the full work order, replacing the preliminary/not-yet-authorized status in the historical body of job.md. No merge authorization.

**Audience/mode:** junior undergraduate AI majors; rigorous but narrowly scoped. **Duration:** opt01 150 minutes, opt03 90 minutes. Two main decks at existing paths. Scope is reduced by removing topics, not removing essential reasoning or shrinking type. Detailed sources E01–E09 are in evidence.md; original requests C01–C11 in requests.md. job.md contains the exact baseline page/title/line map and approved schedule.

**Argument:** structure yields a best low-rank approximation in closed form; when using iteration, assumptions determine which convergence guarantee is earned. SVD/EYM is the centerpiece. GD uses only step 1/L and one shared descent/distance argument. Keep strong convexity. Co-coercivity and the independent PL condition stay in backup. Nonconvex means approximate stationarity, not a local-minimum guarantee.

**Deliverables:** revised main HTML deck + per-slide HTML note + accessible Markdown note for each of opt01/opt03; full extended backup editions preserving all baseline content; updated course/root outlines plus a backup index. Existing opt02 and opt04 are marked backup-only in course navigation, kept at their existing paths and not substantively edited. No prob01–prob09 edits, no exam changes, no whole-series renaming, no new activities, no new optimization methods. No PDF delivery to Albert.

**Read-side completed:** PLANNER_BRIEF; DS §§1,2,4,5,6,8,9,10; root topic map; `courses/deepmath/OUTLINE.md` (the applicable leaf—no separate per-opt-folder OUTLINE exists at baseline); math exemplar `courses/privacy/lectures/02-generative/diffusion2-ddpm.html`. The current design system overrides layout/count targets here. Do not copy a legacy formatting violation from an exemplar or backup into the new mains.

### Priority and interpretation

- All required points, assumptions, preservation obligations and proof dependencies are **must**.
- Proposed titles, exhibits and pacing are **prefer [judgment]** unless their mathematical content is marked must; slides may improve them while retaining the approved argument/time/scope. Suggested components are vocabulary only, not markup instructions.
- Splits, layout and moving secondary algebra into notes are **slides decides [judgment]**. Report them in the mapping. Do not move the theorem's assumptions, the answer to Albert's question, or a missing proof step off the main path merely to meet a page count.
- If the proof/argument should change, report a plan issue before departing. New evidence or scope needs a new plan version; the archived old plan is not authority against a better explanation.

## 2. IDs, preparation and archival integrity

1. **Assign baseline IDs by baseline page**, independently per deck: opt01 page 1->S01 through page 119->S119; opt03 page 1->S01 through page 134->S134. Always qualify IDs by deck in the work report. Existing IDs are not renumbered after reordering. New IDs below are reservations; report additional next-free IDs or suffix splits.
2. **Legacy notes require preparation.** Both are section-oriented, not per-slide articles. First make a separately identified note-structure preparation commit: align existing note material into one article per baseline slide, using the baseline title as heading; partition or duplicate relevant existing paragraphs as needed. Preserve every baseline substantive paragraph, equation, citation and figure description, including material not spoken on the slides. Do not change mathematical wording or claims in this preparation, and do not invent filler. Structural headings may change and redundant navigation may adapt. Keep all detail accessible. Report the old note section -> baseline slide-article mapping. Refresh accessible Markdown only as needed for this structural alignment; no content loss.
3. **Then make the ID-only commit:** add matching slide/article `data-slide-id` values to both decks and their notes; this commit changes IDs only, not wording/layout/content. Report both preparation SHA and ID-only SHA. If the mechanical note migration is not feasible without semantic change, flag that precise issue rather than calling a semantic rewrite “ID-only”.
4. **Archive the extended material before trimming.** From the prepared/ID-tagged baseline, create full backup deck + HTML note + Markdown note under each opt folder's `backup/` (paths below). Preserve all 119/134 baseline slides and all baseline note content. Adjust only resource paths, backup identification and necessary local navigation. Report any indispensable corrections separately. These are visibly marked extended/archive material, outside this year's lecture path. Do not treat preservation as an independent scientific reapproval of every legacy claim.
5. **Now implement revised main decks and per-slide notes.** Stable IDs move with content. New main material must not leak into the frozen full-original backup in place of its original content. Final note articles match final main slide IDs and order. All omitted details remain in the full backups and/or appropriate revised note. The removal manifest below makes this testable.

The baseline SHA remains unchanged. Review compares baseline, preparation, ID-only, and named content commit separately so that structural note migration does not hide content changes.

## 3. Coverage table

| Request | Baseline page / title | Target IDs / disposition | Package |
|---|---|---|---|
| C01–C03 | course outline and both openings | opt01 S01/S02; opt03 S01/S02; 150+90 minutes; prob09 unchanged | shared, P1–P4 |
| C04 | opt01 pp3–5, The Optimization Half / Where the Probability Half Stopped / The Optimization Half, in Four Steps | archive S03–S05; new S120 plus repurposed S80 starts main motivation | P1, P5 |
| C05 | opt01 pp10–54 and pp64–104, foundations/norms/SVD/EYM | selected S12–S103 and new S121–S123 below | P1–P3 |
| C06 | both extended baseline decks and notes | complete full-original backups; every excluded ID retained | P5 |
| C07 | series naming and probability sequence | deliberately untouched; no future renumbering | shared |
| C08 | opt03 pp79–129 convergence | S80/S81/S89/S96/S116 + proof rows below | P4 |
| C09 | opt03 pp48–78 and pp109–129 | co-coercivity/PL archive-only; S64/S116 strong convexity; S89/S93/S136 honest nonconvex target; S110/S131/S140 distinctions | P4, P5 |
| C10 | opt01/opt03 and remaining opt material | two main decks; full extended backups; opt02/04 registered backup-only | all |
| C11 | approval of stage 1–3 proposal | full execution of this plan; not a merge | all |

## 4. Global slide and companion acceptance

- One idea and one exhibit per content slide. Finding/example title states the result; otherwise state the point briefly. Necessary qualifiers remain visible. No dense shrink-to-fit text, tiny diagrams, illegible math or footer collision.
- The proof path remains understandable at instructor pace. For 4+ proof steps use setup -> outline -> steps -> one local equation-chain recap. Do not add redundant outlines/recaps for shorter derivations. One global recap per deck.
- Every theorem states domain, norm, assumptions, quantity and quantifier that make it true. Citation points to E02–E06 with exact section/theorem; E07–E09 examples are clearly our derivation/illustration, not empirical benchmarks.
- Main notes: one matching article per slide, ordered message -> explanation -> details/sources. Include extended algebra needed to teach without reconstruction. All examples and qualifiers agree with main figures and formulas. Plain-English figure narration covers axes/units/encodings/meaning. Full Frobenius optimality proof remains available, but do not make the 150-minute lecture depend on its min-max/Weyl machinery.
- Accessible Markdown: standalone prose, plain ASCII, LaTeX math, verbal figure descriptions, tables linearized with clear keys; matches revised HTML note order/content. No “see the slide” dependency. Legacy content removed from current-course notes is preserved in the backup note editions.
- Figure preference: existing mathematically correct diagrams or worked-math blocks. No new decorative/empirical case studies. If reusing a paper/book figure, keep provenance and necessary qualifier. If generating a figure, record code path and inputs in work-r1 for addition to evidence; check algebraic invariants, not just sampled visual plausibility. New or modified figure code may live only under the scoped opt folders.
- Prerequisites: recall symmetric eigendecomposition, Euclidean inner product and orthogonality in place; adapt baseline rank/nullity and norms; defer pseudoinverse, full four-subspace theory, ridge, co-coercivity, PL and SGD. opt03 is self-contained and must not assume the deferred regression deck.

## 5. Reading order and pacing

The detailed spec rows below are the target sequence, not the baseline order. Structural slides are listed separately and inserted around the specified blocks. Per-row minutes include transitions and ordinary explanation; structural time is absorbed into adjacent rows, not additional. Small timing adjustments are slides' call within the approved totals; scope expansion returns for decision.

### opt01 structural surfaces (shared editor)

- S01 title: **SVD and Best Low-Rank Approximation**. Point: a smaller matrix with a quantified approximation error. Evidence E02–E03. Title-slide component; no new schedule/series-number promise.
- S02 Contents: exactly **Why Low Rank? / Measuring Error / Reading an SVD / Best Low-Rank Approximation / Read the Answer**.
- New S120 before S80: **Why Low Rank?**, section divider 01.
- S25 before S27: **Measuring Error**, divider 02.
- S35 before S36: **Reading an SVD**, divider 03.
- S79 before S81: **Best Low-Rank Approximation**, divider 04.
- S116 before S102: **Read the Answer**, divider 05.
- S119 closer follows S117; no future least-squares promise.
- All structural notes are brief and match ID/title. These slides introduce no independent factual claim; evidence and acceptance inherited from adjacent block.

### opt03 structural surfaces (shared editor)

- S01 title: **Gradient Descent: Three Guarantees**. Point: distinguish what assumptions earn, not three different algorithms. E04–E07.
- S02 Contents: **One Update / One Descent Inequality / Nonconvex: Stationarity / Convex: Optimality / Strongly Convex: Geometric Decay / Three Guarantees**.
- S79 before S80: **One Update**, divider 01.
- S25 before S33: **One Descent Inequality**, divider 02.
- New S135 before S89: **Nonconvex: Stationarity**, divider 03.
- S09 before S10: **Convex: Optimality**, divider 04.
- S63 before S64: **Strongly Convex: Geometric Decay**, divider 05.
- S130 before S131: **Three Guarantees**, divider 06.
- S134 closer after new S140; remove promise of an upcoming SGD lecture.
- Structural note acceptance is the same as opt01.

### Per-slide specification key

Each item supplies the point, required content/exhibit, off-slide destination, evidence, suggested component and time, and an observable acceptance check. Titles/components are prefer [judgment]; mathematical point/qualifiers/check are must. All baseline titles/pages/lines for the ID are recoverable from job.md's page manifest (Snn=baseline page nn). New IDs include their insertion position.

### P1a — opt01: Why Low Rank? (15 minutes)

#### S80 — A Smaller Matrix, Controlled Error
- **Point (must):** Approximation trades representation size for a measurable residual.
- **Required / exhibit (must; presentation [judgment]):** Start with a generic matrix approximation question and rank-k candidate; exhibit A -> A_k plus residual, not the old four-lecture optimization agenda. Do not claim that every low-rank representation saves storage.
- **Note / backup:** Explain full-observation setting and difference from completion; save advanced applications for backup.
- **Evidence:** E02,E03. **Prefer:** diagram-flow. **Time target:** 4 min.
- **Acceptance (must):** Audience can state what is being approximated and how quality will be judged before hearing a theorem.

#### S12 — Recall: Span and Range
- **Point (must):** A matrix output lies in the span of its columns.
- **Required / exhibit (must; presentation [judgment]):** Recall range(A) as column span; show Ax=sum_j x_j a_j with dimensions. Only the span/basis facts needed later.
- **Note / backup:** Full linear independence and dimension foundations remain in note/backup.
- **Evidence:** E02,E01. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Range definition and dimensions are explicit; no unexplained appeal to a prior deck.

#### S14 — Rank Counts Independent Directions
- **Point (must):** Rank measures output-space dimension.
- **Required / exhibit (must; presentation [judgment]):** Define rank(A)=dim range(A); show a rank-r factorization/direction picture without asserting parameter counts.
- **Note / backup:** Keep row-rank equality and full four-subspace treatment in backup.
- **Evidence:** E02,E01. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Rank is not described as the number of nonzero entries or columns.

#### S13 — Two Inputs Collapse to One Direction
- **Point (must):** A concrete rank-one map makes lost directions visible.
- **Required / exhibit (must; presentation [judgment]):** Use C=[[1,1],[2,2]] and Cx=(x_1+x_2)(1,2); exhibit inputs mapped onto a line.
- **Note / backup:** Work through image/kernel calculation; keep other rank examples in backup.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Map and highlighted output line agree algebraically.

#### S16 — Null Space Means Lost Directions
- **Point (must):** The null space records inputs sent to zero.
- **Required / exhibit (must; presentation [judgment]):** Define null(A)={x:Ax=0}; for C use span((1,-1)); coordinate picture or compact worked block.
- **Note / backup:** Explain subspace closure if useful, no new theorem chain on main.
- **Evidence:** E09,E02. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** The null vector is an input direction, not an output vector in the range.

#### S18 — Rank and Nullity Add Up
- **Point (must):** Low rank leaves a large null space.
- **Required / exhibit (must; presentation [judgment]):** State rank(A)+dim null(A)=n for A in R^(m by n); connect the C example (1+1=2). This is the prerequisite later used for arbitrary competitors B.
- **Note / backup:** Full rank-nullity proof in note/backup; main may state this foundation with explanation.
- **Evidence:** E02,E01. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Column dimension n is used, including rectangular matrices.

### P1b — opt01: Measuring Error (25 minutes)

#### S27 — What Makes a Norm?
- **Point (must):** A norm measures size consistently.
- **Required / exhibit (must; presentation [judgment]):** Give nonnegativity/zero condition, homogeneity, triangle inequality in one compact definition exhibit; this is a brief foundation, not a norm-theory lecture.
- **Note / backup:** Explain norm versus squared norm and that squared l2 is not a norm.
- **Evidence:** E02. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Definitions have the absolute scalar in homogeneity and zero iff zero.

#### S28 — Three Familiar Vector Norms
- **Point (must):** Different norms measure different aspects of the same vector.
- **Required / exhibit (must; presentation [judgment]):** Define l1, l2 and linfinity, using finite coordinate vectors; omit general p proof.
- **Note / backup:** General lp, p>=1 and failure for p<1 remain backup.
- **Evidence:** E02. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No conflation of Euclidean length with the sum of absolute coordinates.

#### S29 — One Vector, Three Answers
- **Point (must):** The metric changes the reported size.
- **Required / exhibit (must; presentation [judgment]):** Use v=(3,4): norms 7,5,4; show one worked exhibit tied to the three definitions.
- **Note / backup:** Give arithmetic and interpretation; avoid a second unmotivated example.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Values are correct and each is labelled by its norm.

#### S30 — Unit Balls Reveal the Metric
- **Point (must):** A unit ball is the set of vectors judged no longer than one.
- **Required / exhibit (must; presentation [judgment]):** Use the existing l1/l2/linfinity boundary comparison; identify which shape belongs to which norm.
- **Note / backup:** Verbal descriptions of diamond, circle and square; no dependence on color alone.
- **Evidence:** E02,E09. **Prefer:** grid-3. **Time target:** 3 min.
- **Acceptance (must):** Boundary points actually satisfy the named norm=1 and labels are readable.

#### S31 — Orthogonal Maps Preserve Geometry
- **Point (must):** Orthogonal coordinates change orientation without changing Euclidean length.
- **Required / exhibit (must; presentation [judgment]):** Recall square Q with Q^T Q=I and a rotated vector; distinguish orthogonal matrix from merely orthogonal columns of a rectangular matrix.
- **Note / backup:** Equivalent characterizations and Gram-Schmidt are backup.
- **Evidence:** E02. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** No claim that every norm is invariant under arbitrary rotations.

#### S33 — Why Length Is Preserved
- **Point (must):** The identity Q^T Q=I proves Euclidean invariance.
- **Required / exhibit (must; presentation [judgment]):** One proof block: norm(Qx)^2=x^T Q^T Qx=norm(x)^2; state Euclidean norm.
- **Note / backup:** Detailed inner-product algebra in notes.
- **Evidence:** E02. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Proof uses Euclidean norm and square orthogonal Q; one short chain, not extra proof-outline slides.

#### S66 — Spectral Norm: Worst Stretch
- **Point (must):** Operator norm asks for the worst unit input direction.
- **Required / exhibit (must; presentation [judgment]):** Define norm(A)_2=max_{norm(x)_2=1} norm(Ax)_2 with finite-matrix dimensions; show unit ball becoming an ellipsoid only as concept intuition, not yet a singular-value identity.
- **Note / backup:** General induced p norms and submultiplicativity are backup.
- **Evidence:** E02,E03. **Prefer:** card. **Time target:** 4 min.
- **Acceptance (must):** Distinguish matrix spectral norm from vector l2 and from entrywise l2.

#### S72 — Frobenius Norm: Total Energy
- **Point (must):** Frobenius norm measures all entrywise squared error.
- **Required / exhibit (must; presentation [judgment]):** Define norm(A)_F^2=sum_ij a_ij^2 and interpret norm(A-B)_F^2; one matrix/residual exhibit.
- **Note / backup:** Explain square root for norm and squared norm for energy; trace form optional in notes.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 4 min.
- **Acceptance (must):** No claim that spectral and Frobenius norms agree generally; qualifiers for total squared error are explicit.

### P2 — opt01: Reading an SVD (45 minutes)

#### S36 — Recall: Symmetric Eigendecomposition
- **Point (must):** A^T A supplies orthogonal input directions.
- **Required / exhibit (must; presentation [judgment]):** Recall real symmetric eigendecomposition; A^T A is positive semidefinite since x^T A^T Ax=norm(Ax)^2. This is content recall, not a reference to a lecture number.
- **Note / backup:** Full spectral theorem is a prerequisite and is not reproved here.
- **Evidence:** E02. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Positive semidefiniteness is justified and dimensional role is clear.

#### S38 — Every Matrix Has an SVD
- **Point (must):** Orthogonal factors separate direction from nonnegative stretch.
- **Required / exhibit (must; presentation [judgment]):** State A=U Sigma V^T for real m by n A with square orthogonal U,V and rectangular nonnegative diagonal Sigma; ordered singular values. Explain construction route A^T A, not a complete long existence proof.
- **Note / backup:** Full construction including zero singular values and basis completion in notes.
- **Evidence:** E02. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Does not restrict SVD to symmetric or invertible matrices.

#### S39 — Read the Factor Shapes
- **Point (must):** Compatible dimensions make the decomposition meaningful.
- **Required / exhibit (must; presentation [judgment]):** Show m by m, m by n and n by n factors; distinguish rank r and zero slots.
- **Note / backup:** Add rectangular examples and edge cases in notes.
- **Evidence:** E02. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** All displayed products are dimensionally correct.

#### S40 — Rotate, Stretch, Rotate
- **Point (must):** Each SVD factor has a geometric job.
- **Required / exhibit (must; presentation [judgment]):** Show x -> V^T x -> Sigma V^T x -> U Sigma V^T x in that order; orthogonal maps may include reflections, so do not insist that all factors are proper rotations.
- **Note / backup:** Explain the reflection caveat and rectangular stretch map.
- **Evidence:** E02. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Arrow order matches actual multiplication, and non-square Sigma is not called a rotation.

#### S52 — First Change the Input Coordinates
- **Point (must):** Right singular vectors define the input basis.
- **Required / exhibit (must; presentation [judgment]):** Adapt the existing circle/axes exhibit: V^T first, with a correctly oriented vector or circle.
- **Note / backup:** Describe what does and does not change in this stage.
- **Evidence:** E02,E09. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** A rotation/reflection does not stretch the Euclidean circle.

#### S53 — Then Stretch and Reorient
- **Point (must):** Singular values set the ellipse axes.
- **Required / exhibit (must; presentation [judgment]):** Complete the same geometry with Sigma then U; match role/color/label order to S40.
- **Note / backup:** Ellipse semiaxes and transformation sequence in verbal notes.
- **Evidence:** E02,E09. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** The displayed elongations match the singular values, not A's eigenvalues.

#### S41 — A Sum of Rank-One Layers
- **Point (must):** SVD also separates a matrix into weighted components.
- **Required / exhibit (must; presentation [judgment]):** State A=sum_{i=1}^r sigma_i u_i v_i^T; one stacked-component exhibit with outer-product dimensions.
- **Note / backup:** Explain how diagonal Sigma yields this expansion.
- **Evidence:** E02. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Each term is rank one when sigma_i>0 and all terms reconstruct A.

#### S42 — Compact SVD Keeps Active Directions
- **Point (must):** Only nonzero singular components are needed to reconstruct A.
- **Required / exhibit (must; presentation [judgment]):** State A=U_r Sigma_r V_r^T with m by r, r by r, n by r factors and U_r^T U_r=V_r^T V_r=I_r.
- **Note / backup:** Full-versus-compact terminology; rectangular thin factors are not square orthogonal matrices.
- **Evidence:** E02. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** No false U_r U_r^T=I_m assertion when r<m.

#### S44 — One Matrix, One Construction
- **Point (must):** A small example makes all three factors checkable.
- **Required / exhibit (must; presentation [judgment]):** Introduce A=[[3,0],[4,5]] and the route A^T A -> eigenpairs -> singular values -> left vectors. Keep its values stable through later truncation.
- **Note / backup:** List exact input and explain sign choices; no extra example family.
- **Evidence:** E08,E09. **Prefer:** diagram-flow. **Time target:** 1 min.
- **Acceptance (must):** Every later factor calculation refers to this same A.

#### S45 — Build the Symmetric Matrix
- **Point (must):** A^T A converts the SVD problem into an eigenproblem.
- **Required / exhibit (must; presentation [judgment]):** Compute [[25,20],[20,25]]; no need for a new covariance digression.
- **Note / backup:** Show multiplication entry by entry.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** The off-diagonal value is 20 and dimensions match.

#### S46 — The Eigenvalues Are 45 and 5
- **Point (must):** Eigenvalues of A^T A determine squared stretches.
- **Required / exhibit (must; presentation [judgment]):** Factor the small characteristic polynomial and obtain 45,5.
- **Note / backup:** Full arithmetic and ordering in notes.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** These are identified as eigenvalues of A^T A, not A.

#### S47 — Orthonormal Input Directions
- **Point (must):** Eigenvectors identify the right singular vectors.
- **Required / exhibit (must; presentation [judgment]):** Use v1=(1,1)/sqrt(2), v2=(-1,1)/sqrt(2); check one orthogonality relation.
- **Note / backup:** Solve both eigenvector equations and explain sign nonuniqueness.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Both vectors normalized; subsequent U uses the same signs.

#### S48 — Recover Stretches and Output Directions
- **Point (must):** For each nonzero sigma, u_i=Av_i/sigma_i.
- **Required / exhibit (must; presentation [judgment]):** Obtain sigmas 3sqrt(5),sqrt(5) and u1=(1,3)/sqrt(10),u2=(-3,1)/sqrt(10). Split this ID with suffixes if the two computations cannot fit naturally.
- **Note / backup:** Give full algebra for both vectors and rounded values only when useful.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 4 min.
- **Acceptance (must):** No overflow and no division by a zero singular value; factors agree with S47.

#### S49 — The Factors Reconstruct A
- **Point (must):** The worked decomposition is an equality, not an analogy.
- **Required / exhibit (must; presentation [judgment]):** Assemble exact U Sigma V^T; one factorization exhibit.
- **Note / backup:** Verify multiplication in notes and explain that signs must change in paired vectors.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Product equals original A.

#### S50 — The First Layer Carries Most Energy
- **Point (must):** Two rank-one components sum to the example.
- **Required / exhibit (must; presentation [judgment]):** Show A1=[[1.5,1.5],[4.5,4.5]] and residual [[1.5,-1.5],[-0.5,0.5]] summing to A; postpone the formal optimality claim until EYM.
- **Note / backup:** Arithmetic and component energy are expanded in notes.
- **Evidence:** E08,E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Do not infer best approximation merely from this example's successful reconstruction.

#### S51 — Eigenvalues Are Not Singular Values
- **Point (must):** A nonsymmetric matrix can have different spectral quantities.
- **Required / exhibit (must; presentation [judgment]):** For A contrast eigenvalues 3,5 with singular values sqrt(45),sqrt(5), clearly labelled.
- **Note / backup:** Explain PSD symmetric special case if needed, not a new theorem arc.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 1 min.
- **Acceptance (must):** No false general identification of eigenvalues and singular values.

#### S68 — Largest Singular Value, Largest Stretch
- **Point (must):** Spectral norm equals the leading singular value.
- **Required / exhibit (must; presentation [judgment]):** State norm(A)_2=sigma1 and the two proof tasks: upper bound and achieving direction.
- **Note / backup:** Zero matrix case in notes.
- **Evidence:** E02,E03. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** The result follows from the norm definition, not from a visual alone.

#### S69 — No Direction Beats the Largest Stretch
- **Point (must):** Orthogonal invariance gives the upper bound.
- **Required / exhibit (must; presentation [judgment]):** Use norm(Ax)=norm(Sigma V^T x)<=sigma1 norm(x), with one short expansion if needed.
- **Note / backup:** Detail the singular-basis sum.
- **Evidence:** E02. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Every unit vector is covered, not just coordinate directions.

#### S70 — The First Singular Vector Attains It
- **Point (must):** The upper bound is sharp.
- **Required / exhibit (must; presentation [judgment]):** Substitute x=v1 and use Av1=sigma1 u1, norm(u1)=1.
- **Note / backup:** Handle zero/rank-zero edge case separately in notes.
- **Evidence:** E02. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Upper bound plus witness completes equality.

#### S73 — Frobenius Energy Sums Squared Stretches
- **Point (must):** Total energy is the squared singular-value sum.
- **Required / exhibit (must; presentation [judgment]):** State norm(A)_F^2=sum_i sigma_i^2 and connect to total energy rather than worst direction.
- **Note / backup:** Trace formulation optional, not required background.
- **Evidence:** E03. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Norm versus squared norm is unambiguous.

#### S74 — Orthogonal Coordinates Preserve Total Energy
- **Point (must):** Frobenius invariance proves the identity.
- **Required / exhibit (must; presentation [judgment]):** Use column/row Euclidean invariance to get norm(A)_F=norm(U^T A V)_F=norm(Sigma)_F; avoid relying on an unexplained trace trick.
- **Note / backup:** Prove left/right Frobenius invariance and optionally show the trace proof.
- **Evidence:** E02,E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** The proof ends with the squared singular-value sum and uses only taught invariance.

### P3a — opt01: Best Low-Rank Approximation (55 minutes)

#### S81 — Keep the Largest Components
- **Point (must):** Truncated SVD is a natural candidate, not yet proven best.
- **Required / exhibit (must; presentation [judgment]):** Define A_k=sum_{i=1}^k sigma_i u_i v_i^T for ordered positive singular values, k<r; diagram shows retained versus discarded components.
- **Note / backup:** Endpoint k=0 and k>=r conventions in notes.
- **Evidence:** E02,E03. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Candidate rank is at most k and order is explicit.

#### S82 — Truncate the Worked Matrix
- **Point (must):** Rank-one truncation is concrete.
- **Required / exhibit (must; presentation [judgment]):** Recall the exact first layer A1 from S50 as the candidate; do not redo the entire SVD.
- **Note / backup:** Full multiplication, retained input/output directions.
- **Evidence:** E08,E09. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Candidate has rank one and is the correct first component.

#### S83 — Read the Candidate's Error
- **Point (must):** The discarded component determines this residual.
- **Required / exhibit (must; presentation [judgment]):** Compute residual from E08; both norms equal sqrt(5) here because the residual has rank one. This is an error computation, not optimality proof.
- **Note / backup:** Make the rank-one caveat explicit in explanation.
- **Evidence:** E08. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No general claim that spectral error equals Frobenius error.

#### S90 — Eckart–Young–Mirsky: Spectral Error
- **Point (must):** No rank-k competitor beats the next singular value.
- **Required / exhibit (must; presentation [judgment]):** State for A in R^(m by n), rank r, ordered positive sigmas and 0<=k<r: min_{rank(B)<=k} norm(A-B)_2=sigma_(k+1), attained by A_k. Spectral form only here; Frobenius form has its own later slide S101.
- **Note / backup:** State no uniqueness is asserted; fully observed, unweighted approximation.
- **Evidence:** E03. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Competitors are all rank-at-most-k matrices, not only truncated SVDs.

#### S91 — Optimal Means Every Competitor
- **Point (must):** EYM proves more than a convenient construction.
- **Required / exhibit (must; presentation [judgment]):** Explain universal lower bound plus one attaining candidate; use a bound-and-witness diagram.
- **Note / backup:** No claims about exact completion, predictive error or uniqueness.
- **Evidence:** E03. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Audience can distinguish candidate error from proven minimum.

#### S85 — Recall: A Competitor Has a Kernel
- **Point (must):** The rank constraint forces at least n-k null directions.
- **Required / exhibit (must; presentation [judgment]):** Recall rank-nullity for B in R^(m by n): dim null(B)>=n-k.
- **Note / backup:** Expand why rank at most k yields an inequality.
- **Evidence:** E02,E03. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Uses input dimension n consistently.

#### S86 — Large Subspaces Must Intersect
- **Point (must):** A dimension count guarantees a shared nonzero vector.
- **Required / exhibit (must; presentation [judgment]):** State dim(U intersect V)>=dim U+dim V-n and explain its consequence for dimensions n-k and k+1.
- **Note / backup:** Full dimension-formula derivation in notes; only the needed bound on main.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 4 min.
- **Acceptance (must):** Subspaces are both in R^n and the conclusion is at least one dimension.

#### S87 — Two Planes Share a Direction
- **Point (must):** A geometric case makes the dimension argument visible.
- **Required / exhibit (must; presentation [judgment]):** Two planes through the origin in R^3 share a line or larger subspace; show the common direction without pretending every ambient-dimensional proof is 3D.
- **Note / backup:** Verbal description and generalization to R^n.
- **Evidence:** E03. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Planes are linear subspaces through zero and the marked vector lies in both.

#### S88 — One Witness Bounds a Maximum
- **Point (must):** A single unit input can lower-bound the operator norm.
- **Required / exhibit (must; presentation [judgment]):** Recall norm(A-B)_2>=norm((A-B)w)_2 for any unit w.
- **Note / backup:** Explain why a lower bound needs a chosen witness rather than all inputs.
- **Evidence:** E02,E03. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Unit-length requirement is stated.

#### S89 — Leading Directions Stay Strong
- **Point (must):** A vector in the top k+1 singular subspace cannot be stretched less than sigma_(k+1).
- **Required / exhibit (must; presentation [judgment]):** Expand w=sum_{i<=k+1} c_i v_i, sum c_i^2=1, then norm(Aw)^2=sum sigma_i^2 c_i^2>=sigma_(k+1)^2.
- **Note / backup:** Expand orthonormality step and explain sorted values.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Coefficient normalization and index ranges are correct.

#### S92 — Proof Plan: Find One Witness
- **Point (must):** The spectral proof combines a blind spot with a strong direction.
- **Required / exhibit (must; presentation [judgment]):** Preview target norm(A-B)_2>=sigma_(k+1); steps kernel -> strong subspace -> intersection -> witness -> attainment.
- **Note / backup:** Explain each step's job without repeating the whole derivation.
- **Evidence:** E03. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Overview predicts the actual subsequent proof order.

#### S93 — Every Competitor Has a Blind Spot
- **Point (must):** Any admissible B kills a large input subspace.
- **Required / exhibit (must; presentation [judgment]):** Fix an arbitrary B with rank(B)<=k; its null space has dimension >=n-k.
- **Note / backup:** Quantifiers and rectangular setup expanded.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** B is arbitrary, not the proposed A_k.

#### S94 — A Remains Strong Here
- **Point (must):** Top singular directions form a k+1 dimensional subspace.
- **Required / exhibit (must; presentation [judgment]):** Set W=span(v1,...,v_(k+1)); explain linear independence and dimension.
- **Note / backup:** Recall why these v_i are orthonormal.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** W lives in the input space and has dimension k+1.

#### S95 — The Two Subspaces Intersect
- **Point (must):** There is a unit direction B kills but A cannot shrink too much.
- **Required / exhibit (must; presentation [judgment]):** Use the dimension bound to choose unit w in null(B) intersect W.
- **Note / backup:** Normalization of a nonzero intersection vector.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** The same w satisfies both requirements.

#### S96 — The Residual Exposes That Direction
- **Point (must):** Along w the residual equals A itself.
- **Required / exhibit (must; presentation [judgment]):** Show norm(A-B)_2>=norm((A-B)w)=norm(Aw) since Bw=0.
- **Note / backup:** One-line reminder of w and its origin.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No switch from upper bound to lower bound or inconsistent witness.

#### S97 — The Witness Cannot Be Too Small
- **Point (must):** The strong subspace supplies sigma_(k+1).
- **Required / exhibit (must; presentation [judgment]):** Apply S89's expansion to the chosen w; conclude norm(Aw)>=sigma_(k+1).
- **Note / backup:** Full coefficient details repeated if needed for self-contained teaching.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Square roots and nonnegativity handled correctly.

#### S98 — Truncation Meets the Lower Bound
- **Point (must):** The candidate attains the universal lower bound.
- **Required / exhibit (must; presentation [judgment]):** A-A_k has largest singular value sigma_(k+1); use spectral-norm theorem to match the bound.
- **Note / backup:** Explain remaining singular spectrum.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Equality follows from both directions; not merely an inequality for one candidate.

#### S99 — One Chain Completes the Proof
- **Point (must):** Kernel, intersection and singular values establish optimality.
- **Required / exhibit (must; presentation [judgment]):** One recap inequality chain from arbitrary B through w to sigma_(k+1)=norm(A-A_k)_2; each non-obvious step has a short reason.
- **Note / backup:** Expanded chain and links to the local proof steps.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Recap is a mathematical chain, not a second bulleted overview.

#### S101 — Eckart–Young–Mirsky: Frobenius Error
- **Point (must):** The same truncation minimizes total squared residual energy.
- **Required / exhibit (must; presentation [judgment]):** State min_{rank(B)<=k} norm(A-B)_F^2=sum_{i>k} sigma_i^2, attained by A_k, with the same setup as S90. Use squared error for a short formula; note may give its square root. State that spectral proof did not prove this second norm's optimality.
- **Note / backup:** Full Frobenius optimality proof from baseline note §7.4 with its min-max/Weyl prerequisites; keep details in notes/backup.
- **Evidence:** E03. **Prefer:** card. **Time target:** 4 min.
- **Acceptance (must):** The theorem is distinguished from its easier achievability calculation; no unjustified proof claim.

#### S121 (new, after S101) — Discarded Components Set the Energy
- **Point (must):** Frobenius identity computes the candidate's error.
- **Required / exhibit (must; presentation [judgment]):** Use the residual's singular values to obtain norm(A-A_k)_F^2=sum_{i>k} sigma_i^2. Briefly distinguish computing this error from proving no other B does better.
- **Note / backup:** Full derivation and theorem-versus-achievability distinction.
- **Evidence:** E03. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No presentation of this calculation alone as a complete optimality proof.

### P3b — opt01: Read the Answer (10 minutes)

#### S102 — The Best Rank-One Error Is sqrt(5)
- **Point (must):** The worked error now has an optimality certificate.
- **Required / exhibit (must; presentation [judgment]):** Apply EYM to A's sigma2; state both norms equal sqrt(5) in this rank-one residual case.
- **Note / backup:** Complete arithmetic; avoid a third SVD calculation.
- **Evidence:** E08,E03. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Example conclusion follows the theorem and is not circular.

#### S103 — One Component Keeps 90% of Energy
- **Point (must):** Squared singular values quantify retained energy.
- **Required / exhibit (must; presentation [judgment]):** Use 45/(45+5)=90%, with an energy partition exhibit. Define retained energy as norm(A1)_F^2/norm(A)_F^2; 90% is not accuracy or explained variance without a centered-data setup.
- **Note / backup:** Storage trade-offs and PCA interpretation are optional backup, not a new main topic.
- **Evidence:** E08. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Labels say energy; denominator is total squared Frobenius norm.

#### S122 (new, after S103) — Worst Error and Total Error Differ
- **Point (must):** Discarding several components separates the two norms.
- **Required / exhibit (must; presentation [judgment]):** Use diag(5,3,1), k=1: residual diag(0,3,1), spectral norm 3, Frobenius norm sqrt(10); one worked comparison.
- **Note / backup:** Explain why the prior 2 by 2 example had equal norms.
- **Evidence:** E08. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No ambiguity between sqrt(10) and squared error 10.

#### S123 (new, after S122) — What the Guarantee Covers
- **Point (must):** EYM solves a specific approximation problem.
- **Required / exhibit (must; presentation [judgment]):** Show full known matrix -> chosen rank -> optimal spectral/Frobenius residual. Explicit qualifier: not a missing-data recovery or downstream accuracy guarantee.
- **Note / backup:** Matrix completion and applications preserved in full backup.
- **Evidence:** E03. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** No implication that truncated SVD automatically solves Netflix or denoises optimally statistically.

#### S117 — From Directions to Optimal Error
- **Point (must):** One synthesis links norms, SVD and truncation.
- **Required / exhibit (must; presentation [judgment]):** One closing chain or compact tool summary: measure error -> expose singular directions -> truncate -> read exact optimum. No second global recap.
- **Note / backup:** Explain the chain and point to backup topics in instructor notes only.
- **Evidence:** E02,E03. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No leftover optimization-half or least-squares agenda on main.

### P4a — opt03: One Update (15 minutes)

#### S80 — Minimize a Differentiable Objective
- **Point (must):** GD is an iterative method for one unconstrained objective.
- **Required / exhibit (must; presentation [judgment]):** Define f:R^d->R and the goal; do not assume a minimizer in the nonconvex case. One objective-landscape exhibit.
- **Note / backup:** Relate to empirical loss briefly without relying on opt02 or rederiving ERM.
- **Evidence:** E04,E06. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Domain and full-gradient deterministic setting clear.

#### S14 — Recall: The Gradient
- **Point (must):** The gradient encodes first-order change.
- **Required / exhibit (must; presentation [judgment]):** Recall f(x+h) approximately f(x)+<grad f(x),h> for small h and gradient as partial derivatives.
- **Note / backup:** Directional derivative details.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Approximation is local, not a finite-step decrease guarantee.

#### S82 — Move Against the Gradient
- **Point (must):** The negative gradient points downhill locally.
- **Required / exhibit (must; presentation [judgment]):** Simple one-dimensional sign example or vector-direction diagram; finite step needs smoothness next.
- **Note / backup:** Zero gradient need not mean a minimum.
- **Evidence:** E06,E08. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Does not assert every step length decreases the objective.

#### S27 — Smoothness Controls Gradient Change
- **Point (must):** L bounds how fast the gradient changes.
- **Required / exhibit (must; presentation [judgment]):** Define global Euclidean L-smoothness: norm(grad f(x)-grad f(y))<=L norm(x-y), L>0.
- **Note / backup:** Differentiate function Lipschitzness from gradient Lipschitzness; no general Hessian equivalence lecture.
- **Evidence:** E06. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** The assumption is on the gradient, not on f itself.

#### S81 — One Fixed Step
- **Point (must):** Use the same update in all three guarantees.
- **Required / exhibit (must; presentation [judgment]):** State x_(t+1)=x_t-(1/L)grad f(x_t), t=0,1,..., arbitrary x0. No line search, optimized 2/(L+mu), stochastic gradient or adaptive method.
- **Note / backup:** Known usable upper bound L is assumed for this elementary theory; practical estimation is outside scope.
- **Evidence:** E04,E06,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** All later formulas use precisely this fixed step.

#### S30 — A Quadratic Gives L=4
- **Point (must):** The running example makes the smoothness constant concrete.
- **Required / exhibit (must; presentation [judgment]):** Introduce f(x)=2x_1^2+(1/2)x_2^2 and grad f=(4x_1,x_2); show gradient Lipschitz bound via diag(4,1), hence choose L=4.
- **Note / backup:** Exact bound and attaining direction from E09; strong convexity saved for its section.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Example is defined before the hand iterations, and L=4 is justified.

### P4b — opt03: One Descent Inequality (15 minutes)

#### S33 — A Quadratic Upper Bound
- **Point (must):** Smoothness bounds a finite-step change.
- **Required / exhibit (must; presentation [judgment]):** State f(y)<=f(x)+<grad f(x),y-x>+(L/2)norm(y-x)^2 under L-smoothness; theorem exhibit.
- **Note / backup:** Explain no convexity needed; complete proof in matching notes.
- **Evidence:** E06. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** The inequality points upward and retains its quadratic coefficient.

#### S34 — The Upper Bound Touches Locally
- **Point (must):** The smoothness bound is tangent at the starting point.
- **Required / exhibit (must; presentation [judgment]):** Reuse a verified parabola-lid geometry; match f, tangent and upper quadratic, with exact functions/parameters in provenance.
- **Note / backup:** Algebraically verify lid>=f over displayed domain; explain tangent contact.
- **Evidence:** E06,E09. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** No lid crossing below f; labels do not rely only on color.

#### S36 — Proof: Follow the Segment
- **Point (must):** A multidimensional difference becomes a one-dimensional integral.
- **Required / exhibit (must; presentation [judgment]):** Set h=y-x and rho(s)=f(x+sh), s in [0,1]; use rho'(s)=<grad f(x+sh),h>.
- **Note / backup:** State chain rule and fundamental theorem carefully.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 1 min.
- **Acceptance (must):** Parameter s is not the GD iteration index.

#### S37 — Proof: Bound the Drift
- **Point (must):** L-smoothness controls the integral remainder.
- **Required / exhibit (must; presentation [judgment]):** After subtracting <grad f(x),h>, use Cauchy-Schwarz and norm(grad f(x+sh)-grad f(x))<=Ls norm(h).
- **Note / backup:** Expanded integrand derivation.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** The bound is Ls norm(h)^2, not L norm(h) or Ls^2 norm(h)^2.

#### S38 — Proof: Integrate the Bound
- **Point (must):** The factor one half comes from integrating s.
- **Required / exhibit (must; presentation [judgment]):** Integrate s from zero to one and conclude the descent lemma; no extra outline or recap for this short proof.
- **Note / backup:** Carry complete chain in notes.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 1 min.
- **Acceptance (must):** All terms and coefficient match S33.

#### S90 — The Fixed Step Decreases f
- **Point (must):** Substitution turns smoothness into guaranteed progress.
- **Required / exhibit (must; presentation [judgment]):** With g_t=grad f(x_t), show f(x_(t+1))<=f(x_t)-norm(g_t)^2/(2L). Explicitly no convexity needed.
- **Note / backup:** One-step substitution expanded; explain equality possible at a stationary point.
- **Evidence:** E06,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Uses 1/L, not a new step-size interval; statement is nonincrease with strict decrease if g_t is nonzero.

#### S83 — One Direction Finishes Immediately
- **Point (must):** The example's update has two simple coordinate factors.
- **Required / exhibit (must; presentation [judgment]):** For E09 quadratic and step1/4, x+=(0,(3/4)x2).
- **Note / backup:** Relate factors to the two curvatures; no optimized-step detour.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** The first coordinate becomes zero, rather than merely shrinking.

#### S84 — Two Steps Reduce the Objective
- **Point (must):** Hand calculations check the abstract update.
- **Required / exhibit (must; presentation [judgment]):** Use x0=(2,2), x1=(0,3/2), x2=(0,9/8) and function values 10,9/8,81/128. One small worked sequence; further iterations in notes/full backup.
- **Note / backup:** Squared distances and exact arithmetic provided in notes.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Values agree with the update; table/sequence is not overloaded by extra columns.

### P4c — opt03: Nonconvex Stationarity (15 minutes)

#### S89 — Nonconvex: Small Squared Gradient
- **Point (must):** Smoothness and a lower bound guarantee approximate stationarity.
- **Required / exhibit (must; presentation [judgment]):** For f>=f_low, L-smooth, T>=1, step1/L, state min_{0<=t<T} norm(grad f(x_t))^2 <=2L(f(x0)-f_low)/T. Display best squared gradient, not a local-optimum gap.
- **Note / backup:** Full quantifiers; no assumption the lower bound is attained. Distinguish infimum from attained minimum.
- **Evidence:** E06. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Assumptions, min, square and index range all visible.

#### S91 — Sum the Decreases
- **Point (must):** A finite objective budget bounds accumulated gradient energy.
- **Required / exhibit (must; presentation [judgment]):** Sum S90 from t=0 to T-1 and telescope to f(x0)-f(xT)<=f(x0)-f_low.
- **Note / backup:** Explain boundedness below is essential.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No use of a nonexistent optimizer in the proof.

#### S92 — Minimum Is at Most Average
- **Point (must):** One of the first T gradients must be small.
- **Required / exhibit (must; presentation [judgment]):** Divide the squared-gradient sum by T and use minimum<=average.
- **Note / backup:** Qualitative gradients-to-zero follows from summability but iterate convergence does not; keep this in notes.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** The selected index range has T terms and the conclusion is not a last-iterate rate.

#### S93 — Stationary Does Not Mean Minimum
- **Point (must):** The guarantee is weaker than local optimality.
- **Required / exhibit (must; presentation [judgment]):** Brief explicit answer: smooth nonconvex GD does not generally guarantee convergence to a local minimum. One target hierarchy exhibit: small gradient is not a minimum certificate.
- **Note / backup:** No silent random-initialization/saddle-escape theorem. A convergent subsequence, if any, has stationary limit by continuity; no generic iterate-limit assertion.
- **Evidence:** E06. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Answers Albert's original wording directly on main, with its scope.

#### S136 (new, after S93) — GD Can Stay at a Maximum
- **Point (must):** Zero gradient can trap deterministic GD at a non-minimizer.
- **Required / exhibit (must; presentation [judgment]):** Use f(x)=1-cos(x), x0=pi; f'=sin(x), f''(pi)=-1; show x_t=pi for every t. State illustrative exact initialization, not typical behavior.
- **Note / backup:** Explain f>=0 and global L=1, so it satisfies the theorem's assumptions.
- **Evidence:** E08. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** Counterexample obeys smoothness/lower-bound assumptions and is labelled an existence counterexample.

#### S137 (new, after S136) — The Square Changes the Rate
- **Point (must):** O(1/T) squared gradient means O(1/sqrt(T)) gradient norm.
- **Required / exhibit (must; presentation [judgment]):** Read S89 as a bound on norm squared; a norm tolerance epsilon needs T of order epsilon^-2, with problem-dependent constants.
- **Note / backup:** Full constant from E06 and best-iterate caveat.
- **Evidence:** E06. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No O(1/T) gradient-norm or local-minimum claim.

### P4d — opt03: Convex Optimality (20 minutes)

#### S10 — Convexity Puts Chords Above
- **Point (must):** Convexity rules out nonglobal local minima in this unconstrained setting.
- **Required / exhibit (must; presentation [judgment]):** Define convex f by chord inequality and one geometric exhibit; do not introduce unrelated convex-analysis properties.
- **Note / backup:** Give definition for all x,y and mixing parameter in [0,1].
- **Evidence:** E04. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Graph obeys the chord inequality; not a strict-convexity claim.

#### S15 — The Tangent Lies Below
- **Point (must):** Differentiable convexity supplies the global lower bound.
- **Required / exhibit (must; presentation [judgment]):** State f(y)>=f(x)+<grad f(x),y-x>.
- **Note / backup:** Short derivation from the chord definition; distinguish this lower bound from smoothness's upper bound.
- **Evidence:** E04,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No missing differentiability or reversed inequality.

#### S95 — Assume an Optimum Exists
- **Point (must):** Function-gap convergence needs an attained target here.
- **Required / exhibit (must; presentation [judgment]):** Assume x* in argmin f; define f*=f(x*), Delta_t=f(x_t)-f*, D_t=norm(x_t-x*)^2 as needed, not a dense notation glossary.
- **Note / backup:** Explain f* is different from the mere lower bound used in nonconvex proof.
- **Evidence:** E04. **Prefer:** card. **Time target:** 1 min.
- **Acceptance (must):** No uniqueness assumption for merely convex f.

#### S96 — Convex: O(1/T) Function Gap
- **Point (must):** The last objective value approaches the global optimum sublinearly.
- **Required / exhibit (must; presentation [judgment]):** State f(x_T)-f* <= L norm(x0-x*)^2/(2T), T>=1, under convexity, L-smoothness, attained minimum, step1/L.
- **Note / backup:** Spell out function-value gap, not iterate distance or geometric convergence.
- **Evidence:** E04. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** All essential assumptions and measured quantity on main.

#### S97 — Proof Plan: Spend Distance
- **Point (must):** The distance identity converts descent into a telescoping budget.
- **Required / exhibit (must; presentation [judgment]):** Target gap bound; outline descent -> tangent bound -> distance identity -> telescope -> last iterate.
- **Note / backup:** No co-coercivity/PL condition added to proof dependencies.
- **Evidence:** E07. **Prefer:** diagram-flow. **Time target:** 1 min.
- **Acceptance (must):** Sequence matches subsequent steps.

#### S98 — Recall: One-Step Decrease
- **Point (must):** Smoothness supplies the same progress bound.
- **Required / exhibit (must; presentation [judgment]):** Recall f(x_(t+1))<=f(x_t)-norm(g_t)^2/(2L), defining g_t locally if needed.
- **Note / backup:** Keep assumption recall brief and accurate.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 1 min.
- **Acceptance (must):** Exactly the inequality already established, not a strengthened result.

#### S99 — Use the Tangent at x_t
- **Point (must):** Convexity relates gradient direction to function gap.
- **Required / exhibit (must; presentation [judgment]):** Set y=x* in S15 to obtain Delta_t<=<g_t,x_t-x*>.
- **Note / backup:** Walk through sign rearrangement.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** This step does not assume strong convexity.

#### S101 — Expand the Squared Distance
- **Point (must):** The cross term and gradient square match the progress bound.
- **Required / exhibit (must; presentation [judgment]):** Expand D_(t+1)=D_t-(2/L)<g_t,x_t-x*>+norm(g_t)^2/L^2; identify Delta_(t+1)<=(L/2)(D_t-D_(t+1)). Split with suffix if needed.
- **Note / backup:** Complete algebra and substitution, no hidden co-coercivity lemma.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Coefficient L/2 and t+1 on gap are correct.

#### S104 — Distances Telescope
- **Point (must):** Total suboptimality is bounded by initial distance.
- **Required / exhibit (must; presentation [judgment]):** Sum Delta_(t+1)<=(L/2)(D_t-D_(t+1)) for t=0,...,T-1; drop nonnegative D_T.
- **Note / backup:** Explain why lower/upper indices yield Delta_1 through Delta_T.
- **Evidence:** E04,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** No off-by-one in the sum.

#### S105 — The Last Gap Is Smallest
- **Point (must):** Monotone objective values turn an average bound into the last-iterate bound.
- **Required / exhibit (must; presentation [judgment]):** Use T Delta_T <=sum_{t=1}^T Delta_t<=L D0/2; divide by T.
- **Note / backup:** Distinguish this last-objective guarantee from the nonconvex best-gradient guarantee.
- **Evidence:** E04,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Monotonicity is justified by descent, not convexity alone.

#### S106 — The Convex Proof in One Chain
- **Point (must):** Descent and the tangent bound spend a finite distance budget.
- **Required / exhibit (must; presentation [judgment]):** Recap the actual inequality chain, ending in the theorem. State sublinear, not linear, in a brief takeaway.
- **Note / backup:** Expanded proof in notes; avoid a second tool-list recap.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No independent smoothness sandwich, co-coercivity or PL theorem is required.

### P4e — opt03: Strongly Convex Geometric Decay (20 minutes)

#### S64 — Add a Quadratic Floor
- **Point (must):** Strong convexity strengthens the tangent lower bound.
- **Required / exhibit (must; presentation [judgment]):** Define f(y)>=f(x)+<grad f(x),y-x>+(mu/2)norm(y-x)^2, mu>0. Continue with 0<mu<=L.
- **Note / backup:** Existence/uniqueness on R^d explained in notes; current theorem may explicitly retain the optimizer setup.
- **Evidence:** E05,E07. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Strong convexity is not merely a unique minimizer or a positive Hessian at one point.

#### S65 — Curvature Is Bounded Below
- **Point (must):** The lower quadratic explains stronger progress.
- **Required / exhibit (must; presentation [judgment]):** Illustrate the strong-convexity floor and smoothness upper bound without adding a new general Hessian-test lecture. Use the same example with mu=1, L=4 if visualized.
- **Note / backup:** Verify inequalities algebraically over domain; explain definition-based calculation from E09.
- **Evidence:** E05,E09. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Floor never crosses above f; upper/lower roles clear.

#### S116 — Strongly Convex: Geometric Convergence
- **Point (must):** Squared distance contracts by a fixed factor.
- **Required / exhibit (must; presentation [judgment]):** State D_T <=(1-mu/L)^T D0 for T>=1, fixed step1/L, L-smooth mu-strong convex f; unique x*. Explain q in [0,1), with q=0 meaning one-step arrival.
- **Note / backup:** Equivalent exponential upper bound and condition number interpretation optional in notes; no optimized-step theorem.
- **Evidence:** E05,E07. **Prefer:** card. **Time target:** 2 min.
- **Acceptance (must):** Do not retain baseline's 2/(L+mu) step or sharper co-coercivity proof as the main theorem.

#### S138 (new, after S116) — Keep the Extra Curvature Term
- **Point (must):** The previous proof gains a negative distance term.
- **Required / exhibit (must; presentation [judgment]):** From strong convexity, Delta_t<=<g_t,x_t-x*>-(mu/2)D_t. Combine with descent/distance to obtain Delta_(t+1)<=(L/2)(D_t-D_(t+1))-(mu/2)D_t.
- **Note / backup:** Expanded derivation uses E07 exactly; split into suffix steps if needed.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 3 min.
- **Acceptance (must):** No PL inequality is invoked, even under a renamed lemma.

#### S139 (new, after S138) — Nonnegative Gap Forces Contraction
- **Point (must):** The function gap cannot consume negative budget.
- **Required / exhibit (must; presentation [judgment]):** Use Delta_(t+1)>=0 in S138 and rearrange to D_(t+1)<=(1-mu/L)D_t.
- **Note / backup:** State why f* is globally minimal and coefficients positive.
- **Evidence:** E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Contraction is for squared distance with q=1-mu/L.

#### S122 — Repeat the Same Contraction
- **Point (must):** Unrolling gives a geometric sequence.
- **Required / exhibit (must; presentation [judgment]):** D_T<=q^T D0; handle q=0 separately in explanation, avoiding 0^0 ambiguities.
- **Note / backup:** Brief induction and q^T<=exp(-mu T/L) for 0<mu<L, optional in notes.
- **Evidence:** E05,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** T counts iterations and q does not change across them.

#### S123 — Function Values Follow Distance
- **Point (must):** Smoothness converts iterate convergence into objective convergence.
- **Required / exhibit (must; presentation [judgment]):** At x*, grad f(x*)=0, so Delta_T<=(L/2)D_T<=(L/2)q^T D0. This explicitly answers convergence to optimum, not merely stationary points.
- **Note / backup:** Unique optimizer; do not replace prefactor (L/2)D0 by Delta0 without a different proof.
- **Evidence:** E05,E07. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Main conclusion is geometric function gap with the justified prefactor.

#### S110 — Linear Means Geometric
- **Point (must):** Optimization terminology names fixed-factor error reduction linear convergence.
- **Required / exhibit (must; presentation [judgment]):** Compare q^T with 1/T conceptually; label the former linear/geometric/exponential and the latter sublinear. No unsourced timing benchmark.
- **Note / backup:** Explain exponential in iteration count versus linear convergence nomenclature.
- **Evidence:** E04,E05. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Does not call 1/T linear or conflate error with iteration complexity.

#### S126 — The Example Beats Its Bound
- **Point (must):** A generic guarantee need not equal an example's exact rate.
- **Required / exhibit (must; presentation [judgment]):** For f=2x1^2+(1/2)x2^2, mu=1,L=4: bound q=3/4 on squared distance, actual later ratio 9/16. Use a compact exact calculation, noting first step differs.
- **Note / backup:** Include D0=8,D1=9/4,D2=81/64 and distinction between distance and squared distance.
- **Evidence:** E09. **Prefer:** math-block. **Time target:** 2 min.
- **Acceptance (must):** Measured/derived example rate is not presented as the theorem's universal factor.

### P4f — opt03: Three Guarantees (5 minutes)

#### S131 — Three Assumptions, Three Guarantees
- **Point (must):** The same algorithm earns different conclusions as assumptions strengthen.
- **Required / exhibit (must; presentation [judgment]):** One global summary: smooth+lower bound -> best squared gradient O(1/T); add convexity+attained optimum -> last function gap O(1/T); strong convexity -> squared distance and function gap geometric. Step1/L shared. Avoid one dense table full of constants.
- **Note / backup:** Record exact bounds/quantifiers from the theorem slides in notes.
- **Evidence:** E04,E05,E06. **Prefer:** card. **Time target:** 3 min.
- **Acceptance (must):** Target quantity and assumptions accompany every rate; no local-minimum claim.

#### S140 (new, after S131) — No Extra Conditions Needed
- **Point (must):** These elementary results do not require co-coercivity or an independent PL assumption.
- **Required / exhibit (must; presentation [judgment]):** Explicit short answer to Albert: keep strong convexity for the geometric rate; co-coercivity/PL are not prerequisites for this proof route. Exhibit descent -> distance identity -> curvature term rather than another rate recap.
- **Note / backup:** Optional reading/backup pointers in notes; do not reintroduce definitions or proofs of deferred conditions.
- **Evidence:** E07. **Prefer:** diagram-flow. **Time target:** 2 min.
- **Acceptance (must):** Answers the question without suggesting co-coercivity or PL are false or useless generally.

## 6. Packages and allowed files

Paths are repo-relative. slides owns implementation and integration; these are disjoint content responsibilities, not a requirement to create additional agents.

| Package | ID scope and dependencies | Allowed content surfaces |
|---|---|---|
| P0 preparation | both baseline decks/notes; before P1–P5 | ID assignment and separate legacy-note normalization described in §2, with no mathematical rewrite |
| P1 foundations | opt01 sequence S80,S12,S14,S13,S16,S18; S27,S28,S29,S30,S31,S33,S66,S72 | these slides and paired revised notes; original note §§1–3 and norm definitions; local supporting visuals |
| P2 SVD | opt01 S36,S38,S39,S40,S52,S53,S41,S42,S44–S51,S68–S70,S73–S74 | these slides and notes; original note §4 and spectral/Frobenius norm portions of §6; depends on P1 invariance/norm vocabulary and shared A from E08/E09 |
| P3 EYM/interpretation | opt01 S81–S83,S90–S91,S85–S89,S92–S99,S101,new S121,S102–S103,new S122–S123,S117 | these slides and notes, original note §7 including full Frobenius proof; depends on P1 rank/nullity and P2 SVD/norm identities |
| P4 GD | all opt03 content IDs specified in §5 | revised opt03 deck/HTML note/Markdown note and local visuals; may reuse only agreed generic notation, no dependency on opt02; depends on E07 proof route and E09 arithmetic |
| P5 backup preservation | every baseline ID and every baseline note subsection, including all IDs excluded below | full backup editions and backup inventory; capture prepared baseline before trimming, then independent of main rewrites |
| Shared integration | structural IDs in §5, titles, Contents/dividers, counts, naming, citations, navigation and outlines | slides integrates after packages, with one editor responsible for shared surfaces |

### Main files

- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank.html`
- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.html`
- `courses/deepmath/opt01-svd-lowrank/opt01-svd-lowrank-note.md`
- `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd.html`
- `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.html`
- `courses/deepmath/opt03-convexity-gd/opt03-convexity-gd-note.md`

### Full original / extended backups

Follow the existing prob06 full-backup naming convention:

- `courses/deepmath/opt01-svd-lowrank/backup/opt01-svd-lowrank-full.html`
- `courses/deepmath/opt01-svd-lowrank/backup/opt01-svd-lowrank-full-note.html`
- `courses/deepmath/opt01-svd-lowrank/backup/opt01-svd-lowrank-full-note.md`
- `courses/deepmath/opt03-convexity-gd/backup/opt03-convexity-gd-full.html`
- `courses/deepmath/opt03-convexity-gd/backup/opt03-convexity-gd-full-note.html`
- `courses/deepmath/opt03-convexity-gd/backup/opt03-convexity-gd-full-note.md`

These intentionally preserve the complete extended editions, not only disconnected clipped pages, so deferred proofs remain intelligible. They are not required reading for the revised mains. Old teaching-sequence promises belong only to clearly identified archival content, not the active course outline. Do not expand backups with a new survey.

### Shared surfaces and optional local assets

- `courses/deepmath/OUTLINE.md`: current-year teaching path, revised deck section ranges and named-theorem locations, paired-note summaries, all four slide-count surfaces, explicit backup-only opt02 and opt04. Preserve original source numbering for file discovery; do not globally rename.
- `OUTLINE.md`: update only the deepmath description/map to distinguish the active final block from extended backups and reflect additional note editions accurately.
- `courses/deepmath/backup/OUTLINE.md` (new): a concise backup index linking both new full extended backups and existing opt02/opt04 deck + note paths. This is navigation; do not copy or relocate opt02/opt04 content merely to put it under a folder named backup.
- Optional generated/local assets only under `courses/deepmath/opt01-svd-lowrank/figs/` and `courses/deepmath/opt03-convexity-gd/figs/`. Regeneration scripts, if needed, stay in those local folders and are reported with exact inputs. Preserve or repair relative asset paths when a full deck is copied one folder deeper.
- `log/2026-11-23-opt01-opt03-four-hour-core/`: slides copies this plan and the living job files unchanged and writes work-rN there. slides-review never writes the tracked record.

**Do not edit:** `reference/`, global scripts, design rules, source LaTeX, prob01–prob09, exams, substantive opt02/opt04 content, or unrelated decks. If a required tooling/design problem truly needs one of those, report it as a plan issue first.

## 7. Preservation manifest and per-slide backup specs

**Universal backup spec (must):** retain the baseline slide's point/content/qualifiers and associated note detail in the corresponding full extended backup at the same stable ID. Preserve original evidence/citations; E01 is only inventory authority. Layout/resource plumbing may adapt to make the copied deck work, never to silently remove a claim. The exhibit stays the original exhibit. Main teaching time is zero. Preferred component is the original. Acceptance: the source slide and its supporting note material are discoverable by ID/title, all original equations/paragraphs survive, and local links/assets render. Report any necessary correctness repair explicitly, with source and reason.

The tables below give every excluded baseline ID this complete inherited preservation spec, rather than silently deleting it. Retained main IDs are also present in the full backups; trimming their main detail must not lose it from both note editions.

### opt01-svd-lowrank — excluded from current main, retained in full backup

| ID / baseline page | Baseline title | Disposition |
|---|---|---|
| S03 / 3 | The Optimization Half | Full-backup preservation spec; 0 main minutes |
| S04 / 4 | Where the Probability Half Stopped | Full-backup preservation spec; 0 main minutes |
| S05 / 5 | The Optimization Half, in Four Steps | Full-backup preservation spec; 0 main minutes |
| S06 / 6 | Deep Learning Optimizes Matrices | Full-backup preservation spec; 0 main minutes |
| S07 / 7 | SVD = the X-Ray | Full-backup preservation spec; 0 main minutes |
| S08 / 8 | Low Rank Is Everywhere | Full-backup preservation spec; 0 main minutes |
| S09 / 9 | Route Map | Full-backup preservation spec; 0 main minutes |
| S10 / 10 | Rank, Range, Null Space | Full-backup preservation spec; 0 main minutes |
| S11 / 11 | A Matrix, Column by Column | Full-backup preservation spec; 0 main minutes |
| S15 / 15 | Worked — Ranks by Inspection | Full-backup preservation spec; 0 main minutes |
| S17 / 17 | Worked — Null Space of $C$ | Full-backup preservation spec; 0 main minutes |
| S19 / 19 | Rank–Nullity — Sanity Checks | Full-backup preservation spec; 0 main minutes |
| S20 / 20 | Rank–Nullity — the Picture | Full-backup preservation spec; 0 main minutes |
| S21 / 21 | Definition — Orthogonal Complement | Full-backup preservation spec; 0 main minutes |
| S22 / 22 | Theorem 2 — Split Any Vector | Full-backup preservation spec; 0 main minutes |
| S23 / 23 | Theorem 3 — the Four Subspaces | Full-backup preservation spec; 0 main minutes |
| S24 / 24 | Why AI Cares About Rank | Full-backup preservation spec; 0 main minutes |
| S26 / 26 | How Long Is a Vector? | Full-backup preservation spec; 0 main minutes |
| S32 / 32 | Example — Rotation by 45° | Full-backup preservation spec; 0 main minutes |
| S34 / 34 | Implication — Rotations Are Free | Full-backup preservation spec; 0 main minutes |
| S37 / 37 | Technique Review — Eigen vs Singular | Full-backup preservation spec; 0 main minutes |
| S43 / 43 | Thin Factors Are Not Orthogonal Matrices | Full-backup preservation spec; 0 main minutes |
| S54 / 54 | SVD — What to Remember | Full-backup preservation spec; 0 main minutes |
| S55 / 55 | The Pseudo-Inverse | Full-backup preservation spec; 0 main minutes |
| S56 / 56 | When $A^{-1}$ Doesn't Exist | Full-backup preservation spec; 0 main minutes |
| S57 / 57 | Definition — Moore–Penrose Pseudo-Inverse | Full-backup preservation spec; 0 main minutes |
| S58 / 58 | Worked — $A^{\dagger}$ for the Running Matrix | Full-backup preservation spec; 0 main minutes |
| S59 / 59 | Worked — $A^{\dagger}$, Finished | Full-backup preservation spec; 0 main minutes |
| S60 / 60 | Worked — the Rank-Deficient Case | Full-backup preservation spec; 0 main minutes |
| S61 / 61 | Sanity Check — $A A^{\dagger} A = A$ | Full-backup preservation spec; 0 main minutes |
| S62 / 62 | $AA^{\dagger}$ and $A^{\dagger}A$ Are Projections | Full-backup preservation spec; 0 main minutes |
| S63 / 63 | Teaser — Solving the Unsolvable | Full-backup preservation spec; 0 main minutes |
| S64 / 64 | Matrix Norms | Full-backup preservation spec; 0 main minutes |
| S65 / 65 | Two Ways to Measure a Matrix | Full-backup preservation spec; 0 main minutes |
| S67 / 67 | The Inequality It's Built For | Full-backup preservation spec; 0 main minutes |
| S71 / 71 | Worked — Max Stretch of $A$ | Full-backup preservation spec; 0 main minutes |
| S75 / 75 | Worked — $\\|A\\|_F$ Two Ways | Full-backup preservation spec; 0 main minutes |
| S76 / 76 | Definition — Nuclear Norm | Full-backup preservation spec; 0 main minutes |
| S77 / 77 | One Vector, Three Norms | Full-backup preservation spec; 0 main minutes |
| S78 / 78 | Nuclear Norm $\approx$ Convex Rank | Full-backup preservation spec; 0 main minutes |
| S84 / 84 | The Claim | Full-backup preservation spec; 0 main minutes |
| S100 / 100 | The Key Trick, Named | Full-backup preservation spec; 0 main minutes |
| S104 / 104 | Implication — the License to Truncate | Full-backup preservation spec; 0 main minutes |
| S105 / 105 | Netflix & Matrix Completion | Full-backup preservation spec; 0 main minutes |
| S106 / 106 | The Recommendation Problem | Full-backup preservation spec; 0 main minutes |
| S107 / 107 | Worked — a Tiny Ratings Matrix | Full-backup preservation spec; 0 main minutes |
| S108 / 108 | Only Two Taste Patterns | Full-backup preservation spec; 0 main minutes |
| S109 / 109 | Rank 2 $=$ Tastes $\times$ Genres | Full-backup preservation spec; 0 main minutes |
| S110 / 110 | Worked — Fill In the Blanks | Full-backup preservation spec; 0 main minutes |
| S111 / 111 | Formalizing — the Observed Set $\Omega$ | Full-backup preservation spec; 0 main minutes |
| S112 / 112 | The Ideal Program — and Its Problem | Full-backup preservation spec; 0 main minutes |
| S113 / 113 | The Convex Relaxation | Full-backup preservation spec; 0 main minutes |
| S114 / 114 | Why the Relaxation Is a Win | Full-backup preservation spec; 0 main minutes |
| S115 / 115 | The Same Shape, Everywhere in AI | Full-backup preservation spec; 0 main minutes |
| S118 / 118 | Next — Least Squares | Full-backup preservation spec; 0 main minutes |

### opt03-convexity-gd — excluded from current main, retained in full backup

| ID / baseline page | Baseline title | Disposition |
|---|---|---|
| S03 / 3 | Why Convexity? | Full-backup preservation spec; 0 main minutes |
| S04 / 4 | When the Formula Runs Out | Full-backup preservation spec; 0 main minutes |
| S05 / 5 | Three Questions About One Update | Full-backup preservation spec; 0 main minutes |
| S06 / 6 | Today's Three Results | Full-backup preservation spec; 0 main minutes |
| S07 / 7 | The Constants Are Learning-Rate Theory | Full-backup preservation spec; 0 main minutes |
| S08 / 8 | Route Map | Full-backup preservation spec; 0 main minutes |
| S11 / 11 | Chord Above the Graph | Full-backup preservation spec; 0 main minutes |
| S12 / 12 | Convex vs. Nonconvex | Full-backup preservation spec; 0 main minutes |
| S13 / 13 | Why AI Cares | Full-backup preservation spec; 0 main minutes |
| S16 / 16 | Tangent Below the Graph | Full-backup preservation spec; 0 main minutes |
| S17 / 17 | Why — the 1D Picture | Full-backup preservation spec; 0 main minutes |
| S18 / 18 | The Hessian, Recalled | Full-backup preservation spec; 0 main minutes |
| S19 / 19 | Recall — PSD | Full-backup preservation spec; 0 main minutes |
| S20 / 20 | Theorem 1 — Second-Order Characterization | Full-backup preservation spec; 0 main minutes |
| S21 / 21 | Worked — Is It Convex? | Full-backup preservation spec; 0 main minutes |
| S22 / 22 | Worked — a Saddle Is Not Convex | Full-backup preservation spec; 0 main minutes |
| S23 / 23 | The Running Example | Full-backup preservation spec; 0 main minutes |
| S24 / 24 | Running Example — Contours | Full-backup preservation spec; 0 main minutes |
| S26 / 26 | Lipschitz Continuity | Full-backup preservation spec; 0 main minutes |
| S28 / 28 | Theorem 2 — Bounded Hessian | Full-backup preservation spec; 0 main minutes |
| S29 / 29 | Proof Sketch — as in the Notes | Full-backup preservation spec; 0 main minutes |
| S31 / 31 | Technique Review — Restrict to a Segment | Full-backup preservation spec; 0 main minutes |
| S32 / 32 | Technique Review — Cauchy–Schwarz | Full-backup preservation spec; 0 main minutes |
| S35 / 35 | Descent Lemma — Proof Overview | Full-backup preservation spec; 0 main minutes |
| S39 / 39 | Proof Summary — the Skeleton | Full-backup preservation spec; 0 main minutes |
| S40 / 40 | What the Descent Lemma Buys | Full-backup preservation spec; 0 main minutes |
| S41 / 41 | Theorem 3 — the Smoothness Sandwich | Full-backup preservation spec; 0 main minutes |
| S42 / 42 | Reading the Statement | Full-backup preservation spec; 0 main minutes |
| S43 / 43 | Proof — Right Side | Full-backup preservation spec; 0 main minutes |
| S44 / 44 | Proof — Left Side, the Idea | Full-backup preservation spec; 0 main minutes |
| S45 / 45 | Proof — Left Side, Minimize the Lid | Full-backup preservation spec; 0 main minutes |
| S46 / 46 | Proof — Left Side, Best Direction | Full-backup preservation spec; 0 main minutes |
| S47 / 47 | Sandwich, Checked on the Running Example | Full-backup preservation spec; 0 main minutes |
| S48 / 48 | Smooth and Convex | Full-backup preservation spec; 0 main minutes |
| S49 / 49 | Two Bounds Meet | Full-backup preservation spec; 0 main minutes |
| S50 / 50 | Lemma 2 — Co-coercivity | Full-backup preservation spec; 0 main minutes |
| S51 / 51 | What Co-coercivity Says | Full-backup preservation spec; 0 main minutes |
| S52 / 52 | Proof of (i) — Overview | Full-backup preservation spec; 0 main minutes |
| S53 / 53 | Proof of (i) — One Point, Two Bounds | Full-backup preservation spec; 0 main minutes |
| S54 / 54 | Proof of (i) — Chain and Rearrange | Full-backup preservation spec; 0 main minutes |
| S55 / 55 | Proof of (i) — the Best $z$ | Full-backup preservation spec; 0 main minutes |
| S56 / 56 | Proof of (ii) — Overview | Full-backup preservation spec; 0 main minutes |
| S57 / 57 | Proof of (ii) — the Tilted Function | Full-backup preservation spec; 0 main minutes |
| S58 / 58 | Proof of (ii) — Apply the Sandwich | Full-backup preservation spec; 0 main minutes |
| S59 / 59 | Proof of (ii) — Symmetrize | Full-backup preservation spec; 0 main minutes |
| S60 / 60 | Proof of (ii) — Add Them | Full-backup preservation spec; 0 main minutes |
| S61 / 61 | Proof Summary — Co-coercivity | Full-backup preservation spec; 0 main minutes |
| S62 / 62 | Co-coercivity, Checked on the Running Example | Full-backup preservation spec; 0 main minutes |
| S66 / 66 | Theorem 4 — Hessian Floor | Full-backup preservation spec; 0 main minutes |
| S67 / 67 | Recall — Ridge Buys $\mu$ | Full-backup preservation spec; 0 main minutes |
| S68 / 68 | Theorem 5 — Gradient Monotonicity | Full-backup preservation spec; 0 main minutes |
| S69 / 69 | Proof — Add Two Floors | Full-backup preservation spec; 0 main minutes |
| S70 / 70 | Theorem 6 — Strong Monotonicity | Full-backup preservation spec; 0 main minutes |
| S71 / 71 | Proof — Same Trick, Stronger Floors | Full-backup preservation spec; 0 main minutes |
| S72 / 72 | Technique Review — Completing the Square | Full-backup preservation spec; 0 main minutes |
| S73 / 73 | Lemma 3 — the PL Condition | Full-backup preservation spec; 0 main minutes |
| S74 / 74 | Reading PL — Gradient Norm Measures the Gap | Full-backup preservation spec; 0 main minutes |
| S75 / 75 | Proof of PL — Rearrange the Floor | Full-backup preservation spec; 0 main minutes |
| S76 / 76 | Proof of PL — Complete the Square | Full-backup preservation spec; 0 main minutes |
| S77 / 77 | PL, Checked on the Running Example | Full-backup preservation spec; 0 main minutes |
| S78 / 78 | PL as an Assumption of Its Own | Full-backup preservation spec; 0 main minutes |
| S85 / 85 | The Path on the Contours ($\alpha = 1/4$) | Full-backup preservation spec; 0 main minutes |
| S86 / 86 | Bigger Step — Zigzag ($\alpha = 0.45$) | Full-backup preservation spec; 0 main minutes |
| S87 / 87 | Too Big — Divergence ($\alpha = 0.6 \gt 2/L$) | Full-backup preservation spec; 0 main minutes |
| S88 / 88 | Three Step Sizes, One Lesson | Full-backup preservation spec; 0 main minutes |
| S94 / 94 | Rate I — $O(1/T)$ | Full-backup preservation spec; 0 main minutes |
| S100 / 100 | Technique Review — the Square, Completed Again | Full-backup preservation spec; 0 main minutes |
| S102 / 102 | Corollary — the Distance Also Shrinks | Full-backup preservation spec; 0 main minutes |
| S103 / 103 | Technique Review — Telescoping Sums | Full-backup preservation spec; 0 main minutes |
| S107 / 107 | Corollary — Iteration Complexity $O(1/\varepsilon)$ | Full-backup preservation spec; 0 main minutes |
| S108 / 108 | Bound vs. Reality on the Running Example | Full-backup preservation spec; 0 main minutes |
| S109 / 109 | Rate II — Linear | Full-backup preservation spec; 0 main minutes |
| S111 / 111 | Theorem 9 — Subtract the Floor | Full-backup preservation spec; 0 main minutes |
| S112 / 112 | What $h$ Knows About $f$ | Full-backup preservation spec; 0 main minutes |
| S113 / 113 | Co-coercivity, Applied to $h$ | Full-backup preservation spec; 0 main minutes |
| S114 / 114 | Unpack — Expand the Square | Full-backup preservation spec; 0 main minutes |
| S115 / 115 | Unpack — Collect Terms | Full-backup preservation spec; 0 main minutes |
| S117 / 117 | Proof Overview | Full-backup preservation spec; 0 main minutes |
| S118 / 118 | Step 1 — Expand the Square | Full-backup preservation spec; 0 main minutes |
| S119 / 119 | Step 2 — Co-coercivity at the Optimum | Full-backup preservation spec; 0 main minutes |
| S120 / 120 | Step 3 — Group; Kill the Gradient Term | Full-backup preservation spec; 0 main minutes |
| S121 / 121 | Technique Review — Unrolling a Recursion | Full-backup preservation spec; 0 main minutes |
| S124 / 124 | Proof Summary — the Skeleton | Full-backup preservation spec; 0 main minutes |
| S125 / 125 | Remark — $O(\log(1/\varepsilon))$ Iterations | Full-backup preservation spec; 0 main minutes |
| S127 / 127 | Geometric Shrinkage, Drawn | Full-backup preservation spec; 0 main minutes |
| S128 / 128 | Bonus — PL Alone Gives the Linear Rate | Full-backup preservation spec; 0 main minutes |
| S129 / 129 | Bonus — Unroll the PL Rate | Full-backup preservation spec; 0 main minutes |
| S132 / 132 | The Constants You Now Own | Full-backup preservation spec; 0 main minutes |
| S133 / 133 | Next — Stochastic Gradients | Full-backup preservation spec; 0 main minutes |

## 8. Work report and review gate

In `work-r1.md`, supply:

1. Branch, preparation SHA, ID-only SHA, exact reviewed content/report SHA, and the immutable baseline above. Do not offer the working tree as review target.
2. Per-package summary; all deviations and plan issues separated from routine layout decisions.
3. Complete deck-qualified `ID | baseline page/title | new page/title | retained/moved/split/new/archive-only` map. For archives also record retained slide count and any changed wrappers/resource links. Never reuse a deleted ID for unrelated material.
4. Note mapping and loss check: every original subsection/equation/citation is either retained in current notes or the full archived notes (usually both). Explain structural preparation separately from semantic rewriting. Confirm paired final articles and accessibility Markdown in both delivery paths.
5. Pace check against 150+90 minutes: outline of where the lecturer spends time, including questions/recall. Final counts may differ from the approximate 68/51 target if density requires it; more pages must not silently add more teaching time or topics.
6. Mathematical checks: EYM competitor quantifier, spectral/Frobenius distinction and proof status; no PL/co-coercivity dependency in main; nonconvex minimum/squared-norm/index/lower-bound qualifier; convex last-gap bound; strongly convex q and prefactor; E08/E09 arithmetic.
7. Design/functional checks: repository lint on affected files, no font reduction, no overflow, no duplicate page counters, source links, valid resource paths; updated outline pointers/counts; no unresolved TODOs introduced in core content.
8. Render-check every new or substantively changed main slide at final presentation size. Pay particular attention to vector/matrix norm labels, SVD factor shapes, worked factorization, EYM witness proof, theorem assumptions, main rate formulas and the final summary. For backups, render representative first/middle/last pages and all repaired path/assets. Verify math rendering, not just HTML validity.
9. Notes checks at desktop and narrow viewport: long math does not force horizontal overflow; messages, explanations, details and sources agree. Plain-ASCII Markdown check and explicit verbal descriptions of each figure/table.
10. Inventory generated figures with repo code paths, inputs, parameter choices and exact algebraic invariants. Flag any unsourced legacy fact copied into new main; do not repair from memory.

Send only the contract pointer naming work-r1 and exact SHA. slides-review will review Albert's request, the evidence, design rules, then this plan. Only blocking findings cause another round (maximum three). After approved, copy final review and refresh living records before pushing; subsequent changes must be log-only before slides-review opens the PR. No merge without Albert's direct order for that PR.
