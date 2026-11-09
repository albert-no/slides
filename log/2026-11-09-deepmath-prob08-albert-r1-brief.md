# prob08 — complete revision brief for slides

**From:** slides-review  
**For:** slides, implementing Albert's comments  
**Date:** 2026-11-09, KST  
**Deliverable:** ONE PR covering the complete prob08 revision, including sections 08–09 and the closing slides. Do not merge without Albert's authorization.

## 0. Scope, baseline, and review findings

Albert's 20:40 instruction, “do all at once and ask slides to open up a single PR for prob08,” supersedes the earlier instruction to revise only through original p94 first. His 20:43 instruction requests this complete brief as a Markdown file because ordinary messages truncate. Do not split the work into first-half/second-half PRs, and do not wait for an intermediate p94 approval before working on the remainder.

Inspected baseline:
- Repository HEAD: `85fb3a4b73f6b0bb90fcdc8bbaac48c43b2e8ece`.
- Main deck: `courses/deepmath/prob08-gaussian/prob08-gaussian.html`, **130 slides**.
- Paired notes: `prob08-gaussian-note.md` and `prob08-gaussian-note.html` in that directory.
- Index: `courses/deepmath/OUTLINE.md`, prob08 leaf begins at baseline line 430.
- Deck SHA-256: `f9dd7d8041eba3e0704dbdad500f3604deb5608ec8dcbee05ac62ed2c322598d`.
- Every page number below means the ORIGINAL 130-slide deck. Use titles/section boundaries to locate it after insertion/deletion. Do not apply later requests to newly shifted page numbers.

I read all 130 slides' text, relevant companion-note sections, the current prob07 continuity material, and rendered the baseline in Chromium. I visually inspected the targeted geometry, equivalence, and layout pages. This is a revision plan, not approval of a revised deck, and not a claim that every baseline page received a full visual audit. I have not edited the slides repository.

### Three priorities

1. **Make the theorem teachable:** Definition 2 is the common starting point; introduce each part immediately before its proof, then end with actual statements of all seven parts. The current opening dumps parts 1–7 before any proof.
2. **Expose the missing mathematical bridges:** a density slice must be normalized; the determinant measures volume; conditional expectation projects onto functions of the observation, not merely the observation vector. These are mathematical clarity/correctness requirements, not taste.
3. **Reconnect applications to prob07:** diffusion is a continuation of the already-discussed learning problem; GDA is a new likelihood model for the same spam classification problem. Define Mahalanobis distance and motivate trace algebra before using them.

**Keep:** the shared covariance example `[[1,0.6],[0.6,1]]`, the separate matrix workbench `[[2,1],[1,2]]`, the construction-first proof spine, the Gaussian-channel shrinkage example, and the distinction between jointly Gaussian and merely Gaussian marginals. These give the lecture continuity; do not replace them with unrelated examples.

**Classification:** Albert's requests and the mathematical guards below are required. Proposed titles, the exact number of split slides, and the recommended visual compositions are implementation recommendations. Preserve their learning objective if choosing a different layout.

## 1. Albert's comments — verbatim and complete

### 20:01 message

> I am revising prob08 slides of Deepmath
> Check the current slides and provide the detailed revision plan for slides agent based on my comment.
> The description should be detailed enough so that the slides agent can call multiple subagents and edit slides in parallel.
> Revise up to page 94 (chapter 07) first
>
> • Remove page 8 route map
> • Page 14, Show both Eigen values and Eigen vectors
> • Page 16, show 3d illustration of joint density and its horizontal slice at x_2=1
> • Explain why page 21 is true. Use non trivial x and add one line of intuition
> • Before page24, show the Eigen value decomposition in matrix form then show spectral decomposition in page 24.
> • Section 04 should name “multivariate normal” (or at least at page 33, we need to specify what we want to define)
> • Page 41, mention all three definitions are equivalent (in some sense). We will show direction from 2->1 2->3 only. Do not mention source. Mention reverses are true (specify condition if needed)
> • Page 50, mention that we are using definition 2!
> • Starting from page 50, state each part then prove it (instead of state all theorem2 part 1-7 then prove one by one). So state part 1, prove part 1, state part 2, prove part 2, etc.
> • Page 55, isn’t this trivial if we are following definition 2? (If so mention definition 2)
> • Page 59, show the selection matrix (3 by 5 matrix that selects row 1, 4, 5 as an example)
> • Page 61-62, can we prove this from pure definition without using change of variables relation? (I do not want to use it). If you need to use change of variables relation for densities, provide intuition why determinant appears here (because I haven’t introduced it before but do not want to provide formal proof)
> • Do we have elementary proof for orthogonal property characterizes E[X|Y] in page 78? If not, provide intuition behind.
> • We can say conditional expectation E[X|Y] is simply the projection of X to the space of Y (to explain X-E[X|Y] and Y are orthogonal)
> • Remove page 85, but show all part 1-7 statement as a summary
> • Page 93, the box sizes are broken, resize it

### 20:25 message

> if you are working on it, here are the comments for remainders:
>
> Starting from section 08,
>
> • In the beginning of section 08, mention that “as we briefly discussed in prob07”. Also emphasize the connection at page 112
> • What is mahalanobis distance?
> • Connect GDA to spam mail case in prob07
> • Page 121, explain why trace trick is required (for covariance matrix estimation). This is multi dimensional extension of MLE for multivariate Gaussian
> • Resize boxes in page 126
> • Remove page 128
> • Page 129, what is antiderivative?

### Subsequent scope/delivery instructions

> do all at once and ask slides to open up a single PR for prob08

> use md file to send message to slides. (normal message cuts off). add all the details

### Comment-by-comment baseline crosswalk (23/23)

The IDs below refer to bullet order within the two verbatim messages above: **16 at 20:01 + 7 at 20:25**. All page and source-line references are frozen to **main `85fb3a4`, 130 slides**. Lines refer to `courses/deepmath/prob08-gaussian/prob08-gaussian.html`. For comments without an explicit page, the mapped location is the implementation anchor, not an extra page number attributed to Albert. Detailed change instructions and constraints follow under the indicated package item.

| Original comment | Baseline page/title/source anchor | Required change | Detailed instructions |
|---|---|---|---|
| 20:01 #1 | p8 **Route Map** (L215–252) | Delete the entire route-map slide; retain Contents. | A1 |
| 20:01 #2 | p14 **The Running Example, Drawn** (L332–350) | Add both eigenvalues and both normalized eigenvectors for the existing covariance; distinguish variance from axis length. | A2 |
| 20:01 #3 | p16 **Conditioning = Slicing the Ellipse** (L365–385) | Replace the ambiguous contour overlay with a 3D joint-density surface and the x₂=1 slice; show normalization. | A3 |
| 20:01 #4 | p21 **Picture — Bowl vs. Trough** (L441–462) | Supply explicit matrices and a nonzero null-direction witness; add the one-line trough intuition. | A4 |
| 20:01 #5 | Insert immediately before p24 **Spectral Decomposition** (L493–503) | Introduce A=QΛQᵀ first, then expand it into the spectral sum on the existing slide. | A5 |
| 20:01 #6 | p32 **Three Definitions** (L598–603); p33 **Three Roads to One Object** (L606–627) | Name the object “Multivariate Normal” in the section and definition introduction; synchronize TOC/notes. | A6 |
| 20:01 #7 | p41 **Equivalence — What We Actually Prove** (L766–794) | State the equivalence with nondegeneracy qualifications, the two taught arrows, and the true reverse directions; remove source narration here. | A6 |
| 20:01 #8 | p50 **Theorem 2 — Parts 1–3** (L895–908) | Make Definition 2 the explicit standing assumption at the theorem opening. | B1 |
| 20:01 #9 | p50–85: opening statement slides p50–52, roadmap p53, proofs p54–84, recap p85 | Interleave each of parts 1–7 with its own proof; remove the all-parts opening dump and stale roadmap. | B1, C1, C4 |
| 20:01 #10 | p55 **Part 1 — Proof** (L975–989) | Identify scalar normality as a direct Definition-2 consequence plus closure of independent Gaussian sums. | B2 |
| 20:01 #11 | p59 **Corollary — All Marginals Are Gaussian** (L1036–1046) | Show the exact 3×5 selector for indices 1,4,5, its selected vector, and selected covariance block. | B3 |
| 20:01 #12 | p61 **Part 4 — Technique: Change of Variables** (L1063–1073); p62 **Part 4 — Proof, Step 1** (L1076–1085); dependent proof p63–65 | Answer the proof question explicitly; use the permitted determinant-volume intuition instead of an unexplained transformation theorem. | B4 |
| 20:01 #13 | p78 **Part 7, Step 3 — Naming the Guess** (L1298–1309) (following residual independence on p77) | Add the elementary tower-property orthogonality proof and uniqueness argument on the slides. | C2 |
| 20:01 #14 | p78 and its p76–79 residual/conditional-expectation context; no page specified in the original comment | Explain projection onto all square-integrable functions of Y; distinguish it from an affine/linear predictor. | C3 |
| 20:01 #15 | p85 **Theorem 2 — Recap** (L1406–1420) | Remove the existing payoff-only recap and replace it with readable complete statements of parts 1–7 after the proofs. | C4 |
| 20:01 #16 | p93 **Two Ways to Sample the Same Pair** (L1531–1551) | Use a content-sized local layout; keep math readable and independence assumptions visible. | C5 |
| 20:25 #1 | p95 **Gaussian Diffusion** (L1566–1570) / p96 **The Diffusion Teaser, Cashed In** (L1572–1584); p112 **Scope — Today vs. the Full Story** (L1823–1839) | Add the explicit prob07 callback at the section opening and explain the learning/probability connection at the scope slide. | D1–D3 |
| 20:25 #2 | p115 **The Decision Rule** (L1862–1873) (first use; insert definition before it) | Define distance and squared distance, illustrate whitening, and preserve prior/determinant terms in GDA. | E2 |
| 20:25 #3 | p113–117 GDA opening, especially p114 **Setup — One Gaussian per Class** (L1848–1860) and p116 **Picture — Two Classes, One Boundary** (L1875–1897) | Connect the Bayes rule to prob07 spam classification while explicitly changing from binary to continuous features. | E1 |
| 20:25 #4 | p121 **Technique — the Trace Trick** (L1953–1964) within p117–124 covariance-MLE derivation | Explain trace as exposing the unknown matrix and collecting residual outer products; connect scalar variance MLE to covariance MLE. | E3 |
| 20:25 #5 | p126 **Exercises (from the source)** (L2028–2043) | Resize the two exercise boxes locally without shrinking type or changing global CSS. | E4 |
| 20:25 #6 | p128 **Recap — Every Tool, One Job** (L2060–2075) | Delete the global every-tool recap; do not recreate it elsewhere. | E5 |
| 20:25 #7 | p129 **Bridge — When Closed Form Runs Out** (L2077–2088) | Define antiderivative with a tiny example; describe the real obstacle as lack of convenient closed-form evaluation and bridge to sampling. | E6 |

## 2. Work packages and integration contract

The following packages are independently specified so they can be delegated without rediscovering the entire conversation. Slides has flagged the current repo's **one editing agent per series** policy. Honor that policy: parallelize read-only research/proof checks/visual specifications, and serialize edits to the canonical deck. Separate work packages do not authorize simultaneous writes to the same HTML or notes. Parallel editing worktrees require resolving that policy with Albert; this should not block proceeding serially now.

| Package | Baseline ownership | Companion-note ownership | Main output |
|---|---|---|---|
| A — geometry/definitions | p1–41, sections 01–04 | §§1–4 | Deletions, eigenpairs, true density surface/slice, PSD explanation, EVD, equivalence |
| B — properties 1–6 | p42–73, sections 05 and first part of 06 | §§5, 6.1–6.6 and theorem preamble | Definition-2 setup, interleaved statements/proofs, selector, density derivation |
| C — conditional expectation/channel | p74–94, rest of 06 and 07 | §§6.7–6.10, 7 | Elementary orthogonality proof/projection visual, theorem summary, channel layout |
| D — diffusion continuity | p95–112, section 08 | §8 | prob07 bridge, exact-versus-model distinction, matching scope slide |
| E — GDA/MLE/closing | p113–130, section 09 and close | §9, relevant reference/closing text | Spam connection, Mahalanobis, trace motivation, boxes, antiderivative |
| Integrator — slides | TOC, shared styles/assets, numbering, cross-references, outlines, log | all cross-section consistency | One coherent branch and PR; final QA |

Each editing handoff must include:
1. Exact baseline titles replaced/deleted and new titles inserted.
2. Updated HTML and BOTH note formats for its owned sections.
3. Any asset paths, with a package-specific prefix such as `p8-slice-*`.
4. Proof assumptions and numerical checks, plus lint and affected-page renders.
5. Any unresolved issue; never silently claim a missing proof was completed.

Do not let every worker independently renumber the deck, edit the TOC, rewrite the outline, or touch shared `reference/deck.css`. The integrator does those once after integration. Do not edit prob07 itself: use it as a read-only continuity reference.

Freeze these interfaces before editing:
- Definition 1 = density, Definition 2 = `X = DW + μ`, Definition 3 = all scalar projections normal.
- Use `W ∈ R^m`, `D ∈ R^{n×m}` in the general construction; sum over `j=1,...,m`, not automatically `n`.
- `V = DD^T` throughout the properties theorem; `Σ` can remain in the warm-up and GDA if explicitly connected.
- Part numbering 1–7 remains unchanged.
- Package B supplies the final parts 1–6 statements to C; C's summary must reproduce those statements, not paraphrase away assumptions.
- A's equivalence arrows must match B's actual proof locations. The direct projection argument belongs to part 1 in the recommended order, not an unchanged stale “part 3” label.
- Albert explicitly requests prob07 references. Include them despite the generic design rule against lecture-number callbacks; make the referenced concept self-contained too.

## 3. Package A — original p1–41

### A1. p8 “Route Map” — delete

Delete the slide, not merely its heading or figure. Retain p2 Contents. Update counts/outline centrally; no replacement navigation slide.

### A2. p14 “The Running Example, Drawn” — show both eigenpairs

Current issue: the figure labels only the long-axis eigenvalue and does not show either eigenvector. The caption mentions the second eigenvalue but gives no geometric direction.

Use the existing covariance, not the separate p25 workbench:

\[
\Sigma=\begin{bmatrix}1&0.6\\0.6&1\end{bmatrix},\quad
\lambda_1=1.6,\ z_1=\frac1{\sqrt2}\binom11,\quad
\lambda_2=0.4,\ z_2=\frac1{\sqrt2}\binom1{-1}.
\]

Draw/label both perpendicular eigenvector directions through the origin. Match the label colors to the axes. Suggested title: **“Eigenvectors orient; eigenvalues set spread.”**

One explanatory line: “Variance along `z_i` is `λ_i`; standard deviation is `sqrt(λ_i)`.” The ellipse semi-axis lengths are proportional to square roots, NOT to eigenvalues. At Mahalanobis radius 1 they are approximately 1.265 and 0.632. If keeping “1σ/2σ” labels, clarify these are directional-standard-deviation/Mahalanobis-radius contours, not 68%/95% probability regions in two dimensions.

Acceptance: both `Σz_i = λ_i z_i` checks hold; vectors normalized and orthogonal; long axis follows `(1,1)`; labels not overlaid on the curve.

### A3. p16 “Conditioning = Slicing the Ellipse” — replace with actual 3D density

Current issue: the 2D contour picture places a bell curve on the `x_2=1` line, mixing coordinate height with density height; it also skips normalization.

Use a quantitatively generated surface with coordinates `x_1`, `x_2`, and height `f_{X_1,X_2}`:

\[
f(x_1,x_2)=\frac1{2\pi\sqrt{0.64}}
\exp\left[-\frac{x_1^2-1.2x_1x_2+x_2^2}{2(0.64)}\right].
\]

Show the fixed-coordinate slice `x_2=1`, highlight its intersection with the surface, and show the corresponding 1D curve alongside or on the following slide. Geometrically this is a **vertical cutting plane** in a density-height plot; its trace in the base plane is the requested horizontal `x_2=1` line. Do not use a constant-density-height plane.

Essential on-slide distinction:

\[
f_{X_1\mid X_2=1}(x_1)=\frac{f(x_1,1)}{f_{X_2}(1)}
=\frac{f(x_1,1)}{\phi(1)}.
\]

- Raw slice: same bell shape, area `φ(1) ≈ 0.24197`.
- Conditional density: rescale to area 1; mean 0.6 and variance 0.64.
- These are different vertical scales; label them honestly.

Suggested title: **“Fix x₂, then normalize the slice.”** Keep p17 as the numerical conclusion rather than repeating its entire calculation here. Build a reproducible mathematical plot, not an AI-generated approximate surface. Give the figure most of the slide; split surface and normalization if labels become small.

### A4. p21 “Picture — Bowl vs. Trough” — explain the nonzero flat direction

Current issue: “some `x^T A x=0`” is vacuous if `x=0` is allowed. The picture provides no matrix/vector witness.

Concrete comparison:

\[
A=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad
B=\begin{bmatrix}1&1\\1&1\end{bmatrix},\quad
x=\binom1{-1}\ne0.
\]

Then `x^T A x=2>0`, while `Bx=0` and `x^T Bx=0`. More strongly, `q_B(tx)=0` for every real `t`, whereas `q_A(tx)=2t²`.

Use the same directions in the picture; B's flat trough follows `(1,-1)`. One-line intuition: **“A nonzero null direction lets you move without climbing.”** Label the right side **“PSD and singular”**, not an unqualified claim that every singular matrix has a nonnegative bowl. A single test vector is a witness for B's failure of PD, not a proof that A is PD; p22 supplies A's all-vectors sum-of-squares proof.

### A5. Before p24 “Spectral Decomposition” — insert matrix EVD

Show the matrix construction first:

\[
Q=[z_1\ \cdots\ z_n],\quad \Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad AQ=Q\Lambda,
\qquad A=Q\Lambda Q^T,\quad Q^TQ=I.
\]

Use a visual “change to eigenbasis → scale → change back” chain; explain that columns of Q are eigenvectors. Then retain p24 and explicitly expand:

\[
Q\Lambda Q^T=\sum_i\lambda_i z_i z_i^T.
\]

Connect the two expressions rather than presenting them as unrelated decompositions. Keep p25's concrete eigenpairs for `A=[[2,1],[1,2]]` (eigenvalues 3 and 1), clearly distinct from the covariance example (1.6 and 0.4).

Small correctness repair while here: p31's “tails die, therefore integral finite” is not true for arbitrary functions. Use `x^T A x ≥ λ_min ||x||²` with `λ_min>0`, so the exponential is bounded by an integrable Gaussian. One line is enough; fuller justification in the note.

### A6. p32–33 and p41 — name the object, qualify equivalence

Rename section 04 **“Multivariate Normal”** with subtitle **“Three equivalent definitions”**; update TOC and note heading. Suggested p33 title: **“Three Definitions of a Multivariate Normal.”** Remove “the source states...” from p33 and p41. Keep existing licensing/attribution elsewhere; this request does not require deleting the credit on p9 or the references.

p41 must say explicitly:
- **Positive-definite covariance:** Definitions 1, 2, and 3 are equivalent.
- **Possibly singular covariance:** Definitions 2 and 3 remain equivalent; Definition 1's ordinary n-dimensional density is unavailable when covariance is singular.
- **Today:** prove `2 → 1` in the square-invertible construction case and `2 → 3`.
- **Reverse directions are also true**, but not proved in the main slides.

For the construction, the intrinsic nondegeneracy condition is `DD^T ≻ 0` (D has full row rank). The simple part-4 proof may state square invertible D; do not incorrectly imply rectangular full-row-rank D produces a degenerate law. The existing notes already discuss equivalent representations.

Use real returning arrows or a compact equivalence diagram, with “proved here” versus “true, not proved here.” Do not send dashed arrows to a text blob that merely says “source.” Normal distributions in Definition 3 must include variance-zero constants (including the projection `a=0`). Notes §§4.3–4.4 already have the precise statements and reverse proofs; retain these as optional reading, but align the main-slide scope text.

## 4. Package B — original p42–73

### B1. Restructure the entire theorem, not just p50's title

At the start of section 06, explicitly state **“Throughout, we use Definition 2: X=DW+μ, with independent standard-normal coordinates in W.”**

Replace the opening p50–52 bulk statement with this sequence:

1. **Part 1 statement → p54–55 proof/recall.**
2. **Part 2 statement → p56–57 proof.**
3. **Part 3 statement → p58 proof → p59 selector → p60 applications.**
4. **Part 4 statement, including invertibility → determinant intuition → p62–65 revised proof.**
5. **Part 5 statement → p66–67 MGF proof → p68 consequence.**
6. **Part 6 statement → p69–72 proof(s) → p73 consequence.**
7. **Part 7 statement moves to C's opening, immediately before p74's proof sequence.**

Delete or absorb p53's all-parts roadmap; do not preserve another front-loaded seven-part synopsis immediately after removing the first one. A short local roadmap within a long part is fine. Reuse existing statement content instead of duplicating all the old slides. A statement may share its slide with a short proof only if it visibly comes first and the layout remains readable.

### B2. p55 — explicitly recognize the direct Definition-2 consequence

Albert is right that this is immediate once the standard fact about linear combinations of independent Gaussians is available. Say so; do not imply scalar normality is an unexplained additional axiom of Definition 2.

\[
X_i=\mu_i+\sum_{j=1}^m d_{ij}W_j
\sim\mathcal N\left(\mu_i,\sum_{j=1}^m d_{ij}^2\right).
\]

One line: **“Direct from Definition 2 and closure of independent Gaussian sums.”** Condense p54's review if needed. Then explain `a^T X = a^T μ + (D^T a)^T W` is likewise normal; this proves `2 → 3`. Do not use the yet-to-be-proved covariance formula as the only justification of the scalar variance. Avoid the current incomplete notation `N(μ_i, ·)` in the statement.

### B3. p59 — show the requested 3×5 selector

\[
C=\begin{bmatrix}
1&0&0&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{bmatrix},\qquad
CX=\begin{bmatrix}X_1\\X_4\\X_5\end{bmatrix}.
\]

Then show `Cμ=(μ_1,μ_4,μ_5)^T` and

\[
CVC^T=\begin{bmatrix}
V_{11}&V_{14}&V_{15}\\
V_{41}&V_{44}&V_{45}\\
V_{51}&V_{54}&V_{55}
\end{bmatrix}.
\]

Highlight selected indices consistently. The point is “marginal = selected mean and covariance block, with no integration.” Split into a selector slide and a covariance-block slide if putting all three objects together is dense.

### B4. p61–65 — do not invoke an unintroduced change-of-variables theorem

**Answer to Albert:** a proof avoiding the multivariable change-of-variables theorem exists, via triangular constructions and conditional densities, but adds new linear-algebra/probability machinery. A density cannot be obtained by just substituting `X=DW+μ` into a formula without accounting for probability per unit volume. The least disruptive implementation is Albert's explicitly permitted fallback: derive the linear-map density rule through elementary probability/volume intuition, without stating or formally proving the general Jacobian theorem.

**Recommended main-slide implementation:**

1. Replace p61's “Technique: Change of Variables” with **“Stretch the volume, spread the density.”** Start in 1D: `X=2W` stretches a small interval by 2, preserves its probability, and halves its density.
2. Show a unit square and its image parallelogram under
   \[
   D=\begin{bmatrix}2&1\\0&1\end{bmatrix}.
   \]
   Image edge vectors are `(2,0)` and `(1,1)`; area is 2. Stretching changes area; shearing tilts without changing it. State the n-dimensional analogue: linear volume multiplier `|det D|`. Reflections need the absolute value.
3. Explain mass conservation for a tiny region around `w` and its image around `x=Dw+μ`:
   \[
   f_W(w)\,\Delta v\ \approx\ f_X(x)\,|\det D|\,\Delta v.
   \]
   Thus the density at x is the original density at `D^{-1}(x-μ)`, divided by `|det D|`. This is a geometric derivation of the linear rule, not a claim that no change-of-volume reasoning is being used. No formal Jacobian proof required.
4. Now substitute the independent white-noise density. Keep p63's exponent algebra and p64's normalization:
   \[
   \|D^{-1}(x-\mu)\|^2=(x-\mu)^T(DD^T)^{-1}(x-\mu),
   \quad |\det D|=\sqrt{\det(DD^T)}.
   \]
5. End with Definition 1 and the meaning: **“The determinant normalizes the volume stretch.”** Keep square invertible D explicit. Mark singular covariance as outside this ordinary-density argument.

Fix the current p61 wording “in its 1D version”: the displayed D/determinant formula is multivariate, not a 1D recall. Do not claim the density was derived “from scratch” if the geometric volume fact was stated without proof; state what is assumed.

**Optional note-only alternative, if a Jacobian-free proof is desired:** for square invertible D, row Gram–Schmidt gives `D=LQ`, with L lower triangular and positive diagonal, Q orthogonal. Let `U=QW`. Its joint MGF is `exp(||t||²/2)=∏exp(t_i²/2)`, so MGF uniqueness makes its coordinates independent standard normals. This lemma is proved directly from independent W; do not cite the later part 6 or assume part 5. Given earlier coordinates, each `X_i` has mean `μ_i+∑_{j<i}l_ij u_j` and variance `l_ii²`, with the previous u-values recovered by forward substitution. Multiply these scalar conditional densities: denominator `∏l_ii=|det D|`, exponent `||L^{-1}(x-μ)||²`. This proves the result without the multivariable density-transform theorem, but introduces triangular factorization and joint-MGF uniqueness earlier. Do not teach both full routes on the main slides; the geometric route is the recommendation for this revision.

### B5. Preserve proof dependency and block independence

Parts 5 and 6 remain MGF/matching-based; the density-factorization proof is an optional second check only when covariance is invertible. For C's residual proof, explicitly state the block form of part 6: **jointly Gaussian subvectors with zero cross-covariance are independent**. Individual coordinates inside a block need not be independent. The block-diagonal matching proof uses the same part-5 argument, and covers singular blocks.

## 5. Package C — original p74–94

### C1. Bring the full part 7 statement here

Move the content of old p52 directly before p74. State joint Gaussianity, the block covariance, and `V_YY ≻ 0`. Restore nonzero means in the statement. Use centered variables for the proof only with an explicit announcement. Do not silently strengthen the assumption to a nonsingular full joint covariance; singular conditional covariances are allowed.

### C2. p78 — elementary proof exists; put the missing reason on slides

The current companion note §6.7 already contains an elementary proof using the tower property. Promote its short version instead of saying “this property characterizes...” without explanation.

Let `m(Y)=E[X|Y]`, with finite second moments. For every square-integrable scalar `g(Y)` (coordinatewise for vector X),

\[
E[(X-m(Y))g(Y)]
=E[g(Y)E[X-m(Y)\mid Y]]=0.
\]

Conversely, suppose `h(Y)` is square-integrable and passes the same orthogonality test for every square-integrable function of Y. Subtract the two tests and choose `g(Y)=h(Y)-m(Y)` in the scalar case:

\[
E[(h(Y)-m(Y))^2]=0
\quad\Longrightarrow\quad h(Y)=m(Y)\text{ almost surely}.
\]

For vector X do this coordinatewise, or use the squared norm and an inner product. Use “every square-integrable function” consistently so the choice of g is permitted; if choosing the bounded-functions version instead, its truncation step belongs in the note.

Recommended split:
- Slide: conditional expectation makes the residual orthogonal (tower calculation).
- Slide: this identifies it uniquely (difference/squared-error argument).
- Slide or integrated visual: the projection interpretation.

An even shorter direct ending for the Gaussian proof, after p77 has established independent residual `R=X−Xhat` with zero mean, is

\[
E[X\mid Y]=E[\widehat X(Y)+R\mid Y]
=\widehat X(Y)+E[R]=\widehat X(Y).
\]

Use this to close the Gaussian calculation; keep the elementary orthogonality explanation because Albert explicitly asked for it, not only in notes.

### C3. Projection — say precisely what “space of Y” means

Suggested title: **“Conditional Expectation Is a Projection.”**

Plain-language line: **“Project X onto the space of all square-integrable functions of Y.”** Write `L²(σ(Y))` only after this explanation; Hilbert-space terminology is optional.

Draw a schematic plane/subspace labelled “functions of Y”; place `E[X|Y]` on it, and show `X−E[X|Y]` perpendicular to it. Define the inner product as `⟨U,V⟩=E[UV]` (coordinatewise for vectors). This is a geometry of random variables, not an ordinary scatterplot of data points.

Necessary guard: orthogonality to Y alone does not characterize the conditional expectation. Within the affine-predictor class, residual orthogonality to both the constant 1 and each coordinate of Y characterizes the best affine predictor (the best linear predictor for centered variables). For jointly Gaussian variables, the conditional expectation is affine in Y, so the full projection happens to lie in `span{1,Y_1,...,Y_m}`. Only in the centered case should it be called linear.

A note-only counterexample helps: take `Y~N(0,1)` and `X=Y²`. Their covariance is zero, yet `E[X|Y]=Y²`, not a constant. Orthogonality does not imply independence in general. The Gaussian residual's independence is the special extra conclusion of part 6.

Keep p76 → p77's actual logical chain: zero cross-covariance, joint Gaussianity of `(R,Y)`, then independence. It is not enough merely to draw a right angle.

### C4. p85 — delete the current payoff table; replace with all seven statements

Albert's “remove p85” and “show all part 1–7 statement as a summary” mean replace the current vague recap, not omit the requested summary. Use 2–3 readable summary slides after the proofs, not seven dense equations crammed into one. A sensible grouping is parts 1–3, parts 4–6, and part 7.

Required mathematical content, matching B's finalized statements:
1. Scalar coordinates/projections are normal; give their means and variances.
2. `E[X]=μ`, `Cov(X)=V=DD^T`.
3. `CX+d ~ N(Cμ+d, CVC^T)`.
4. Square invertible D gives the Definition-1 density with `V=DD^T`; display that density rather than only “density exists.”
5. `M_X(s)=exp(s^Tμ + ½s^TVs)`; mean and covariance determine the Gaussian law.
6. Jointly Gaussian: diagonal covariance iff independent coordinates; block cross-covariance zero iff independent blocks.
7. Joint Gaussian `(X,Y)`, `V_YY≻0`:
   \[
   m(y)=\mu_X+V_{XY}V_{YY}^{-1}(y-\mu_Y),\quad
   S=V_{XX}-V_{XY}V_{YY}^{-1}V_{YX},
   \]
   `X|Y=y ~ N(m(y),S)`, `R=X−m(Y)` independent of Y, and `Cov(R)=S`.

Keep shared assumptions visible. The final summary must not reintroduce an unqualified “uncorrelated = independent.”

### C5. p93 “Two Ways to Sample the Same Pair” — fix actual layout cause

Verified from source and render: `.cols` has `flex:1; align-items:stretch` in canonical CSS, so short `.card` elements stretch into large hollow boxes. Merely setting a smaller font or shrinking the formula is the wrong fix.

Replace this local `.cols` layout with content-sized `.grid-2`, or a local class with no flex growth. Keep global `reference/deck.css` unchanged. Provide a deliberate gap between the panels and the concluding independence line. If the observation-first formula is too wide, stack two compact rows or introduce

\[
k=\frac{\sigma_x^2}{\sigma_x^2+\sigma_z^2},\qquad
s^2=\frac{\sigma_x^2\sigma_z^2}{\sigma_x^2+\sigma_z^2},
\]

then write `X=kY+sW`. Define them visibly, not only in notes. State independence inside the corresponding sampling order: forward `Z ⟂ X`; observation-first `W ⟂ Y`. Preserve the claim of identical joint law and p94's “conditional mean + fresh noise” takeaway.

Check the neighboring channel wording while touched: p89's variance is one-half the harmonic mean of the two variances, not literally the harmonic mean; safer to say “precisions add,” `1/s²=1/σ_x²+1/σ_z²` for positive variances. Describe the noncentered conditional mean as affine, not universally linear.

## 6. Package D — original p95–112

### D1. Section 08 opening — explicitly reconnect to prob07

At the first content slide after the divider, include Albert's requested wording:

**“As we briefly discussed in prob07, diffusion learns to reverse a Gaussian noising process.”**

Then state today's added value: **“Now derive the Gaussian identities behind that construction.”** The existing p96 only recalls prob04's Markov-chain teaser; make prob07 the primary bridge, with prob04 at most a secondary reminder.

Read-only reference: current `prob07-estimation.html` has “Diffusion — an Auxiliary Forward Process,” “DDPM — Learn the Backward Steps,” “Each Backward Step Is a Gaussian MLE,” and “The Full ELBO Is Path-Likelihood Training.” It already discusses fixed-variance Gaussian regression, conditional means, the full bound, and the simplified loss. Do not describe all those topics as entirely new or absent from the course.

### D2. p112 — explain the connection, not just repeat the lecture number

Replace “Today vs. the Full Story” with **“prob07's Learning View, Now Explained.”** A compact paired layout can show:
- prob07: learn a backward conditional mean with squared loss.
- prob08: Gaussian construction, conditional formulas, exact forward noising, and the Gaussian-channel intuition.

Include the bridge `μ*(x_t,t)=E[X_{t-1}|X_t=x_t,t]` as the ideal squared-error predictor (over unrestricted functions); do not claim a trained finite network always achieves it.

The current “Beyond today (learning)” card must become “Learning connection from prob07” or equivalent. Do not re-teach the full ELBO derivation in this deck unless Albert asks. Keep scope honest: Gaussian probability alone does not solve the learned reverse dynamics.

### D3. Correctness guards while revising this section

These are important because the current p112 places “Gaussian reverse steps” under “Exact forward process,” and p108–109 can sound stronger than the proof supports.

- Exact: `q(x_t|x_0)` is Gaussian for fixed x0.
- For `t≥2`, exact training posterior: `q(x_{t-1}|x_t,x_0)` is Gaussian in this forward process.
- Generally not exactly Gaussian: `q(x_{t-1}|x_t)` with unknown, non-Gaussian initial data.
- Learned `p_θ(x_{t-1}|x_t)` is the Gaussian reverse MODEL. Exact under a Gaussian prior; otherwise model/approximation, not a consequence of part 7 for arbitrary data. These distinctions are supported by [DDPM equations (1), (4), (6)–(7)](https://arxiv.org/html/2006.11239#S2).

p109's `N(sqrt(1−β)x_n,β)` is exact if `X_{n-1}` is exactly standard normal; approaching stationarity does not make the finite-time distribution exactly normal or give a pointwise posterior-approximation bound by itself. Say “stationary Gaussian benchmark,” not a universal reverse-kernel derivation. Fix the corresponding note §8.8, which currently claims the exact stationary assumption “holds late in the chain” and later says “early” where the intended regime is late.

At p111 label the generation procedure a simplified Gaussian reverse sampler. Do not promise that any arbitrary learned mean produces the data distribution, or identify its fixed-β skeleton verbatim with the full original DDPM algorithm.

For the MGF argument p101–104, retain the assumption that the initial MGF is finite near zero and that fresh noises are independent of `X_0`. Do not extend that particular proof to every distribution. If retaining an unrestricted “any starting distribution” headline, a short optional note can instead use
`X_n = a_n X_0 + sqrt(1−a_n²)Z` in distribution, `a_n→0`, and convergence in probability plus Slutsky. Otherwise qualify the headline to match the displayed theorem. Do not label finite `n=200` as literally “pure noise”; use “noise-dominated.”

## 7. Package E — original p113–130

### E1. p113–117 — connect GDA to the actual prob07 spam example

Introduce the same target `Y ∈ {spam, non-spam}` and the same Bayes decision structure:

\[
\widehat y=\arg\max_y \pi_y p(x\mid y).
\]

Then show what changes:
- prob07 Bernoulli Naive Bayes: binary word-presence features such as “free,” “meeting,” “winner”; class-conditional product of Bernoulli probabilities.
- Here GDA: continuous mail features, for example log email length and a continuous link/word-frequency feature; one Gaussian mean/covariance per class, allowing within-class correlations.

Do not silently claim the original binary indicators are exactly Gaussian. Label the Gaussian fit as a model for continuous features, not an empirical fact about real spam data. Any illustrative feature cloud or parameter values are synthetic and should say so.

Use a spam/non-spam scatterplot with mean markers and covariance ellipses; connect its prior-and-density comparison to the same Bayes rule students already used. The heights example can remain as a short scalar analogy, but must not be the only continuity bridge.

If showing shared covariance, identify a linear discriminant boundary; separate class covariances allow a quadratic boundary. Full covariance differs from conditional-independence Naive Bayes; diagonal Gaussian covariance recovers a Gaussian Naive Bayes variant, not the same Bernoulli model.

### E2. Before p115's first “Mahalanobis distance” — define it

Suggested title: **“Distance Measured in Standard Deviations.”**

For positive-definite Σ,

\[
d_\Sigma(x,\mu)=\sqrt{(x-\mu)^T\Sigma^{-1}(x-\mu)}
=\|\Sigma^{-1/2}(x-\mu)\|_2.
\]

Plain-language explanation: **“Euclidean distance after removing scale and correlation.”** Connect whitening to earlier p60, and label the quadratic form in the Gaussian exponent as the **squared** Mahalanobis distance.

Concrete visual: `Σ=diag(4,1)`, mean zero. `(2,0)` and `(0,2)` have the same Euclidean distance, but Mahalanobis distances 1 and 2. The wide direction tolerates a bigger displacement. Equal-distance contours are ellipses.

Then the GDA score is

\[
\log\pi_y-\tfrac12\log\det\Sigma_y-\tfrac12d_{\Sigma_y}(x,\mu_y)^2
\]

up to a class-independent constant. “Pick the nearest Mahalanobis mean” alone is justified when priors and covariance determinants are equal; otherwise prior and volume terms matter too. Use natural logs in this likelihood section and say so once.

### E3. p117–124, especially p121 — motivate the trace trick

Current issue: trace is introduced as an isolated algebraic convenience, and the current phrase “turns ... into a linear function” can hide that the expression was already linear in Φ. Trace makes that dependence easy to see and differentiate; it is not the only possible way to do MLE.

Start with the task: **“Extend scalar Gaussian MLE from a variance to a covariance matrix.”** Connect prob07's `σhat²=(1/N)∑(x_i−xbar)²` to the desired matrix analogue with outer products.

At p120: set precision `Φ=Σ^{-1}` to isolate the unknown matrix. At p121 show the calculation with its goal visible:

\[
v_i=x^{(i)}-\widehat\mu,\quad
v_i^T\Phi v_i=\operatorname{tr}(\Phi v_iv_i^T),\quad
\sum_i v_i^T\Phi v_i=\operatorname{tr}(\Phi S),\quad
S=\sum_i v_iv_i^T.
\]

One-line intuition: **“Collect all data into S; expose the matrix parameter Φ.”** A flow diagram `N residual vectors → one scatter matrix → derivative` is more useful than a generic technique card.

Then keep the objective/derivative sequence readable:

\[
\ell(\Phi)=\text{const}+\frac N2\log\det\Phi-\frac12\operatorname{tr}(\Phi S),
\qquad \nabla_\Phi\ell=\frac N2\Phi^{-T}-\frac12S^T.
\]

Stationarity gives `Σhat=S/N`. Distinguish scatter S from covariance S/N. Use `μhat` once the mean has been optimized, or explicitly label `S(μ)` if keeping a variable mean. Trace cyclicity is not arbitrary reordering of matrix products.

Keep the existing nonsingular-centered-scatter requirement in Theorem 4. For unrestricted positive-definite covariance, singular centered scatter does not yield a valid positive-definite MLE. Concavity of log determinant makes the positive-definite stationary solution a maximum; one sentence in notes suffices. Do not replace `N` with `N−1` in the MLE; explain the unbiased alternative separately.

### E4. p126 — resize exercises, preserve font sizes

Same source/render diagnosis as p93: `.cols` flex growth stretches two short cards almost to the footer. Use a content-sized grid or two compact stacked exercise blocks. Keep each statement next to its hint; no forced full-height panels. It is fine for the bottom of the slide to be empty; do not fill the boxes with padding or redundant text.

Retain the mathematical domain for the log-determinant derivative: positive-definite X in this covariance context (or an explicitly specified determinant-positive/invertible domain); `|X|` here means determinant, not entrywise absolute value. If the second exercise needs extra explanation, split rather than reduce type.

### E5. p128 — delete

Remove “Recap — Every Tool, One Job.” Do not recreate an equivalent global tools table under another title. The requested local seven-property summary stays after the properties theorem, not at the end of the applications.

### E6. p129 — explain antiderivative without making a false claim

Current wording “E[g(X)] with no antiderivative” is imprecise: an expectation is a number; antiderivatives refer to an integrand. Continuous integrands have antiderivatives, even if no elementary expression is available.

Use a short definition:

**“An antiderivative of h is a function H with H′=h.”**

Concrete example: `h(x)=2x`, `H(x)=x²`; hence `∫_a^b 2x dx=H(b)−H(a)`. Then state the actual difficulty: **“Many expectation integrals have no convenient closed-form evaluation.”** In high dimensions, the issue goes beyond finding a scalar antiderivative.

Suggested bridge:

\[
E[g(X)]=\int g(x)f_X(x)\,dx
\quad\leadsto\quad
\frac1N\sum_{i=1}^N g(X^{(i)}).
\]

Label the right side a Monte Carlo estimate using samples from the target distribution, not an equality for finite N. Split the vocabulary example and the bridge if necessary. Replace “Everything today was exact because everything was Gaussian”: the diffusion reverse-model discussion includes approximations and the data distribution need not be Gaussian. Safer: **“Gaussian models gave us closed-form answers; more general models may require sampling.”**

## 8. Integration and acceptance criteria

### Required editorial checks

- All original comments in §1 mapped to a changed/deleted/inserted slide in the PR description.
- No old p8 route map, p85 payoff-only recap, or p128 global tools recap remains.
- Section 04, TOC, notes, and outline use consistent multivariate-normal terminology.
- Each theorem part is stated before its own proof; the final summary contains all seven complete results.
- No backward/forward reference points to a removed slide number or stale proof location.
- No “source says” on p33/p41 equivalents; existing legitimate attribution remains elsewhere.
- Every conceptual question Albert asked has an explicit short answer ON the slides, not only in notes or the PR.
- Current prob07 callbacks are accurate; no claim that its learning material was never discussed.

### Mathematical/visual test cases

1. Eigenpairs for `[[1,.6],[.6,1]]`: eigenvalues 1.6/.4, orthonormal vectors `(1,±1)/sqrt2`.
2. Fixed `x2=1` slice: raw area `φ(1)≈.2419707`; normalized conditional `N(.6,.64)`. Surface and 1D curve agree.
3. PSD example: nonzero `(1,−1)` is a null direction of B; A's positive definiteness justified for all nonzero vectors, not by one example.
4. Selection C is exactly 3×5 and returns indices 1,4,5 in that order; covariance rows AND columns selected.
5. Determinant picture: square→parallelogram multiplier 2; density divides by 2, not multiplies. General normalizer uses absolute determinant, then square root of det V.
6. Projection uniqueness: h is a function of Y with finite second moment; test is against all square-integrable functions, not only Y. Gaussian independence claim has joint-Gaussian hypothesis.
7. p93 and p126 replacements: no hollow full-height cards, no clipped fractions, no crowding against footer. Inspect at native 1280×720 and in print.
8. Mahalanobis example distances 1 and 2; squared/unsquared terminology consistent. Class scoring retains determinant/prior terms when unequal.
9. MLE: centered scatter, denominator N, positive-definite condition, natural log convention.
10. Diffusion: fixed-x0 forward exact; learned reverse not presented as exact for arbitrary data; stationary benchmark honestly labelled.

### Repository/QA responsibilities

- Preserve canonical fonts and body sizes. Split overfull slides; never solve density by shrinking type.
- Keep CSS fixes scoped to prob08; do not change shared `.cols` globally.
- Update BOTH companion-note formats, including figure verbal descriptions, theorem order, assumptions, changed proof explanations, and continuity text.
- Update `courses/deepmath/OUTLINE.md` with new section names, counts, accurate line pointers, and proof descriptions. Update other prob08 count references only where relevant. Do not rewrite unrelated lecture entries.
- Update deck pagination/navigation totals; rebuild bundled artifacts only through the established process and do not commit generated standalone/PDF artifacts contrary to repo policy.
- Run `lint-deck.py`, `find-wordy.py`, `find-dense.py`, and `outline-lint.py`; review density warnings in context, fix structural/font/overflow failures.
- Render and inspect every added or materially changed slide plus neighboring transitions, after KaTeX and fonts load. Check figure labels and math, not only text extraction. Existing internal review PDF need not be sent to Albert.
- PR includes a baseline-page→new-page map, requirement checklist, proof decisions, numeric checks, and QA results. Include the required verbatim reviewer/implementer discussion log, and archive this Markdown brief so its untruncated detail is recoverable.
- Open **one prob08 PR**, provide its URL and commit hash to Albert and slides-review, and request review. Opening the PR is authorized; merging it is not.

## 9. Reference boundary

The existing prob08 notes are the first implementation resource: §§2.2–2.4 (eigenstructure/slicing), §§4.3–4.4 (equivalence), §6.7 (orthogonality proof), §8.7 (exact conditioned diffusion posterior), and §9.5 (trace/MLE). The direct numerical examples and proposed pedagogical derivations above have been checked against the displayed formulas.

For external confirmation of the nondegenerate/degenerate distinction, consult [MIT OCW Lecture 14](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/ceb423b6a703abd60429367b733f45bf_MIT6_436JF18_lec14.pdf); note that its definition numbering differs from this deck's. For the diffusion model-versus-exact-posterior distinction, use the [original DDPM paper, equations (1), (4), (6)–(7)](https://arxiv.org/html/2006.11239#S2). These are verification resources, not text to paste wholesale onto p41.
