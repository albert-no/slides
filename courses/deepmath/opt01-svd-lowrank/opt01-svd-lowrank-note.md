# Deep Learning Math 10: SVD and Low-Rank Approximation -- Notes

**About this file.** This is the text-only, screen-reader-friendly edition of the Lecture 10 companion note. It has one numbered section per topic, each headed by its number, title and an ID in brackets; the slide deck `opt01-svd-lowrank.html` and the HTML note `opt01-svd-lowrank-note.html` use the same numbering and IDs. Every figure and table is described in words or linearized into lists, and all mathematics is written in LaTeX. Nothing else is needed to read it.

The lecture has 68 sections and runs 150 minutes. Audience: junior undergraduate AI majors who know matrix multiplication, the Euclidean inner product and the eigendecomposition of a symmetric matrix. Each section opens with a one-sentence message, then explains the idea, then gives details (derivations, worked numbers, figure provenance) and sources.

**What the lecture does.** Five parts: why a low-rank matrix is useful (sections 3-9); two ways to measure the error of an approximation, the spectral and Frobenius norms (sections 10-18); reading an SVD as rotate, stretch, rotate (sections 19-40); the Eckart-Young-Mirsky theorem, which says the truncated SVD is the best rank-k approximation in both norms (sections 41-61); and reading every number off one worked matrix (sections 62-67).

**Conventions.** $A \in \mathbb{R}^{m \times n}$ is a real matrix of rank $r$, with singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(m,n)} \geq 0$ and $\sigma_i = 0$ for $i > r$. $Q$ denotes an orthogonal matrix, $A = U\Sigma V^\top$ the full SVD and $A = U_r \Sigma_r V_r^\top$ the compact one. $A_k = \sum_{i \leq k} \sigma_i u_i v_i^\top$ is the rank-$k$ truncated SVD and $B$ a competing matrix of rank at most $k$. $\|\cdot\|_2$ is the Euclidean vector norm or the spectral matrix norm; $\|\cdot\|_F$ is the Frobenius norm. Results are cited by name, not number. The running example is $A$ with first row $(3, 0)$ and second row $(4, 5)$.

**Extended edition.** The pre-2026-11 lecture (119 sections: pseudo-inverse, four fundamental subspaces, nuclear norm, matrix completion, and the full set of background proofs) is archived with the same IDs as `backup/opt01-svd-lowrank-full.html`, with notes `backup/opt01-svd-lowrank-full-note.html` and `backup/opt01-svd-lowrank-full-note.md`.

<!-- REGION Opening BEGIN -->

<!-- BEGIN S01 -->
### 1. SVD and Best Low-Rank Approximation [S01]

**Message.** Replace a matrix by one of lower rank, and say exactly how much is lost.

Lecture 10 of Deep Learning Math (150 minutes). The lecture asks one question: given a matrix, which matrix of rank at most $k$ is closest to it, and how close is it? The singular value decomposition answers it in closed form, and the Eckart-Young-Mirsky theorem proves that the answer cannot be beaten.
<!-- END S01 -->

<!-- BEGIN S02 -->
### 2. Contents [S02]

**Message.** Five parts: the question, the error measures, the decomposition, the theorem, and the worked answer.

1. Why Low Rank?: Fewer directions, measured loss.
2. Measuring Error: Two sizes for a residual.
3. Reading an SVD: Rotate, stretch, rotate.
4. Best Low-Rank Approximation: Eckart-Young-Mirsky.
5. Read the Answer: One matrix, every number.
<!-- END S02 -->

<!-- REGION Opening END -->

<!-- REGION P1a BEGIN -->

<!-- BEGIN S120 -->
### 3. Part 1: Why Low Rank? [S120]

**Message.** Part 1 poses the question: replace a matrix by one with fewer independent directions, and measure what is lost.
<!-- END S120 -->

<!-- BEGIN S80 -->
### 4. A Smaller Matrix, Controlled Error [S80]

**Message.** Low-rank approximation replaces a fully observed matrix $A$ by a matrix $B$ of rank at most $k$ and judges the result by the size of the residual $A - B$.

The setting: $A \in \mathbb{R}^{m\times n}$ is given and every entry is observed; we choose $B$ with $\operatorname{rank}(B) \le k$. Consider one equation with three matrices: the data $A = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right]$, of rank 2, equals a rank-1 candidate $B = \left[\begin{smallmatrix}1.5 & 1.5\\ 4.5 & 4.5\end{smallmatrix}\right]$ plus the residual $A - B = \left[\begin{smallmatrix}1.5 & -1.5\\ -0.5 & 0.5\end{smallmatrix}\right]$. The decomposition $A = B + (A - B)$ holds for any $B$; what changes from one candidate to another is how big the residual is, and that size will be measured by a matrix norm (Part 2). This sets up the two questions for the lecture: which rank-$k$ matrix is closest, and how small can the error be. At this point $B$ is just one candidate; nothing yet says it is the best one.

Storage is a reason to want low rank, but not automatically a saving: a rank-$k$ matrix can be stored as two factors with $k(m+n)$ numbers, which beats the $mn$ entries of $A$ only when $k(m+n) \lt mn$. For the $2\times 2$ example with $k = 1$ both counts are $4$, so there is no saving at all; the gain appears for large matrices and small $k$.

**Details.** **Full observation versus completion.** Here every entry of $A$ is known and the residual is computed over all entries. Matrix completion is a different problem: only some entries are observed, the fit is measured on those, and the low-rank assumption fills in the rest. The methods of this lecture do not directly solve completion.

**Why the problem is not convex.** The feasible set $\{B : \operatorname{rank}(B) \le k\}$ is not convex: $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$ both have rank 1, but their midpoint $\tfrac12 I_2$ has rank 2. So convex-optimization guarantees do not apply; the lecture still reaches an exact answer through the SVD.

**Check of the example.** $B + (A - B) = \left[\begin{smallmatrix}1.5+1.5 & 1.5-1.5\\ 4.5-0.5 & 4.5+0.5\end{smallmatrix}\right] = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right] = A$. Both columns of $B$ equal $(1.5, 4.5)$, so $\operatorname{rank}(B) = 1$.

**Sources.** Problem statement: Wilkinson, *Multivariate Statistics* (MATH3030 notes), Section 3.5 "Low-rank approximation". The matrices $A$, $B$ and $A - B$ are our illustration (evidence E08); the storage count $k(m+n)$ is our arithmetic.
<!-- END S80 -->

<!-- BEGIN S12 -->
### 5. Recall: Span and Range [S12]

**Message.** Every output $Ax$ is a linear combination of the columns of $A$, so the set of all outputs is the span of those columns.

Write $A = [\,a_1 \cdots a_n\,] \in \mathbb{R}^{m\times n}$ with columns $a_j \in \mathbb{R}^m$, and take an input $x \in \mathbb{R}^n$. Multiplying out gives $Ax = x_1a_1 + \cdots + x_na_n$, a vector in $\mathbb{R}^m$: the entries of $x$ are the weights on the columns. The range (column space) collects every possible output, $\operatorname{range}(A) = \{Ax : x \in \mathbb{R}^n\} = \operatorname{span}\{a_1, \dots, a_n\}$, a subspace of the output space $\mathbb{R}^m$. For example, take $m = n = 2$ with columns $a_1 = (2,1)$ and $a_2 = (1,2)$. For $x = (1,1)$ the output $Ax = a_1 + a_2 = (3,3)$ is the diagonal of the parallelogram spanned by $a_1$ and $a_2$.

**Details.** The span of $v_1, \dots, v_k$ is the set of all combinations $\sum_i \alpha_i v_i$. A subspace is a nonempty set closed under addition and scalar multiplication; $\operatorname{range}(A)$ is one because $Ax + Ay = A(x+y)$ and $\alpha Ax = A(\alpha x)$. A basis is a linearly independent spanning list, and the dimension is its length (well defined by the Steinitz exchange lemma, proved in the backup note).

**Sources.** Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* (CUP 2020), Section 2.7.3, Definition 2.23 and eq. (2.124): $\operatorname{Im}(A) = \{Ax\} = \operatorname{span}[a_1, \dots, a_n] \subseteq \mathbb{R}^m$. Figure: our illustration.
<!-- END S12 -->

<!-- BEGIN S14 -->
### 6. Rank Counts Independent Directions [S14]

**Message.** The rank of $A$ is the dimension of its range: the number of independent output directions.

Definition: $\operatorname{rank}(A) = \dim \operatorname{range}(A)$, the number of vectors in any basis of the range. This determines a factorization of $A$: if $r = \operatorname{rank}(A)$ and $u_1, \dots, u_r$ is a basis of the range, then the $m\times n$ matrix $A$ factors as $U$, an $m\times r$ matrix whose columns are the $u_i$, times $C$, an $r\times n$ matrix. Column $j$ of $C$ holds the coordinates of $a_j$ in that basis. When $r$ is small, $U$ is tall and thin and $C$ is short and wide. Rank is not the number of nonzero entries and not the number of columns: $\left[\begin{smallmatrix}1 & 1\\ 2 & 2\end{smallmatrix}\right]$ has four nonzero entries and two columns, yet both columns point along $(1,2)$, so its rank is 1.

**Details.** **The factorization.** Each column $a_j$ lies in $\operatorname{range}(A)$, so $a_j = Uc_j$ for a unique $c_j \in \mathbb{R}^r$. Stacking the columns gives $A = UC$ with $C = [c_1 \cdots c_n]$. Equivalently $A = \sum_{i=1}^r u_i \tilde c_i^\top$, a sum of $r$ rank-one matrices, where $\tilde c_i^\top$ is row $i$ of $C$.

Row rank equals column rank ($\operatorname{rank}(A^\top) = \operatorname{rank}(A)$) follows from the same factorization; the proof and the four-subspace picture are in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 2.6.2 (rank as the number of linearly independent columns) and Section 2.7.3, eq. (2.124) ($\operatorname{rk}(A) = \dim \operatorname{Im}(A)$). The factorization $A = UC$ is our derivation from the definition.
<!-- END S14 -->

<!-- BEGIN S13 -->
### 7. Two Inputs Collapse to One Direction [S13]

**Message.** The matrix $C = \left[\begin{smallmatrix}1 & 1\\ 2 & 2\end{smallmatrix}\right]$ sends every input onto the single line through $(1,2)$, so its rank is 1.

Both columns of $C$ equal $(1,2)$, so $Cx = x_1(1,2) + x_2(1,2) = (x_1 + x_2)(1,2)$: whatever the input, the output is a multiple of $(1,2)$. Follow three inputs through $C$. The range is the line through the origin with slope 2 in the output plane. The inputs $e_1$ and $e_2$ both land on the same point $(1,2)$, and $(1,1)$ lands on $(2,4)$, further out on the same line. Two independent inputs produce only one output direction: $\operatorname{range}(C) = \operatorname{span}\{(1,2)\}$ and $\operatorname{rank}(C) = 1$.

**Details.** Image calculation: $Ce_1 = (1,2)$, $Ce_2 = (1,2)$, $C(1,1) = (2,4) = 2\cdot(1,2)$. Since every output is $(x_1 + x_2)(1,2)$ and $x_1 + x_2$ can be any real number, the range is the whole line $\operatorname{span}\{(1,2)\}$, not just a segment. A basis of the range is $\{(1,2)\}$, so the dimension is 1.

**Sources.** Our worked example (evidence E09).
<!-- END S13 -->

<!-- BEGIN S16 -->
### 8. Null Space Means Lost Directions [S16]

**Message.** The null space collects the input directions that $A$ sends to zero; for $C$ it is the line spanned by $(1,-1)$.

Definition: $\operatorname{null}(A) = \{x \in \mathbb{R}^n : Ax = 0\}$, a set of inputs. For $C$, $Cx = (x_1 + x_2)(1,2)$ vanishes exactly when $x_1 + x_2 = 0$, so $\operatorname{null}(C) = \operatorname{span}\{(1,-1)\}$. In the input plane the null space is the line of slope $-1$ through the origin. The vector from $e_2$ to $e_1$ is $e_1 - e_2 = (1,-1)$, which lies along that line. In the output plane $C(1,-1) = 0$ is the origin, and $Ce_1 = Ce_2$ is a single point on the range line. So $e_1$ and $e_2$ differ by a null vector, and $C$ cannot tell them apart. The null space lives in the input space $\mathbb{R}^n$; it is not a set of outputs and not part of the range.

**Details.** $\operatorname{null}(A)$ is a subspace: if $Ax = 0$ and $Ay = 0$ then $A(x + y) = 0$ and $A(\alpha x) = 0$. Inputs differing by a null vector give the same output: $A(x + z) = Ax$ when $z \in \operatorname{null}(A)$. For $C$, solving $x_1 + x_2 = 0$ gives $x = t(1,-1)$, $t \in \mathbb{R}$; one free parameter, so $\dim \operatorname{null}(C) = 1$.

**Sources.** Definition: Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 2.7.3, Definition 2.23 (kernel/null space). Example: our calculation (evidence E09).
<!-- END S16 -->

<!-- BEGIN S18 -->
### 9. Rank and Nullity Add Up [S18]

**Message.** For any $A \in \mathbb{R}^{m\times n}$ the kept directions and the lost directions add up to the number of columns $n$, so low rank forces a large null space.

Rank-nullity theorem: for every $A \in \mathbb{R}^{m\times n}$, square or rectangular, $\operatorname{rank}(A) + \dim \operatorname{null}(A) = n$. The count is over columns, i.e. input dimensions, not rows. Think of the $n$ input dimensions as split into two parts: the rank counts the dimensions that are kept, the nullity those that are lost. Check on $C$: rank 1 plus nullity 1 equals 2 columns. For a wide matrix $A \in \mathbb{R}^{2\times 3}$ the rank is at most 2 (the range sits inside $\mathbb{R}^2$), so the nullity is at least 1: some nonzero input is always lost. This is the fact used later for an arbitrary competitor $B$: if $\operatorname{rank}(B) \le k$ then $\dim \operatorname{null}(B) \ge n - k$.

**Details.** **Proof.** Let $x_1, \dots, x_t$ be a basis of $\operatorname{null}(A)$ and extend it to a basis $x_1, \dots, x_t, y_1, \dots, y_s$ of $\mathbb{R}^n$, so $t + s = n$. It suffices to show that $Ay_1, \dots, Ay_s$ is a basis of $\operatorname{range}(A)$. Spanning: any $x = \sum_i \alpha_i x_i + \sum_j \beta_j y_j$ has $Ax = \sum_j \beta_j Ay_j$, because $Ax_i = 0$. Independence: if $\sum_j \beta_j Ay_j = 0$ then $\sum_j \beta_j y_j \in \operatorname{null}(A)$, so it equals some $\sum_i \alpha_i x_i$; this is a linear relation among basis vectors of $\mathbb{R}^n$, so every $\beta_j = 0$. Hence $\operatorname{rank}(A) = s = n - t$. $\blacksquare$

**Corollary used later.** $\operatorname{rank}(B) \le k$ gives $\dim \operatorname{null}(B) = n - \operatorname{rank}(B) \ge n - k$.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 2.7.3, Theorem 2.24 (rank-nullity, stated for a linear map $V \to W$: $\dim \ker + \dim \operatorname{Im} = \dim V$; here $V = \mathbb{R}^n$ and the map is $x \mapsto Ax$). Proof: standard basis-extension argument, retained from the previous version of this note.
<!-- END S18 -->
<!-- REGION P1a END -->

<!-- REGION P1b BEGIN -->

<!-- BEGIN S25 -->
### 10. Part 2: Measuring Error [S25]

**Message.** Part 2 chooses how to measure the size of the error matrix: worst-case stretch or total energy.
<!-- END S25 -->

<!-- BEGIN S27 -->
### 11. What Makes a Norm? [S27]

**Message.** A norm is a size function that is zero only at zero, scales with $|\alpha|$, and obeys the triangle inequality.

Definition: a norm on $\mathbb{R}^n$ is a function $\|\cdot\| : \mathbb{R}^n \to [0,\infty)$ such that for all $x, y \in \mathbb{R}^n$ and $\alpha \in \mathbb{R}$: $\|x\| = 0$ if and only if $x = 0$; $\|\alpha x\| = |\alpha|\,\|x\|$ (the absolute value means flipping the sign does not change the size); and $\|x + y\| \le \|x\| + \|y\|$. Geometrically, the triangle inequality compares two routes: following $x$ and then $y$ is a detour, while $x + y$ goes directly from the start of $x$ to the end of $y$. The direct route is never longer than the detour. These three rules are all we need in this lecture; we use norms to measure residuals, not to study them for their own sake.

**Details.** **Norm versus squared norm.** The squared Euclidean norm $\|x\|_2^2$ is not a norm. It fails homogeneity, since $\|2x\|_2^2 = 4\|x\|_2^2$ rather than $2\|x\|_2^2$, and it fails the triangle inequality: for $x = y = e_1$, $\|x + y\|_2^2 = 4 \gt 2 = \|x\|_2^2 + \|y\|_2^2$. Squared Euclidean and Frobenius norms are still useful as objectives: they are smooth, and squaring a nonnegative quantity does not move its minimizers, which is why the Frobenius "energy" is often written squared later.

**Nonnegativity follows from the other rules:** $0 = \|x + (-x)\| \le \|x\| + \|-x\| = 2\|x\|$. A consequence used for continuity arguments is the reverse triangle inequality $\big|\|x\| - \|y\|\big| \le \|x - y\|$.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.1, Definition 3.1 (absolutely homogeneous, triangle inequality, positive definite). Squared-norm counterexample: our calculation.
<!-- END S27 -->

<!-- BEGIN S28 -->
### 12. Three Familiar Vector Norms [S28]

**Message.** The $\ell_1$, $\ell_2$ and $\ell_\infty$ norms measure different aspects of the same coordinate vector.

For $x = (x_1, \dots, x_n) \in \mathbb{R}^n$ there are three common norms. $\ell_1$, the absolute sum $\|x\|_1 = \sum_i |x_i|$: the distance walked along the coordinate axes. $\ell_2$, the Euclidean norm $\|x\|_2 = (\sum_i x_i^2)^{1/2}$: the straight-line length. $\ell_\infty$, the maximum $\|x\|_\infty = \max_i |x_i|$: the largest single coordinate. $\ell_2$ is Euclidean (straight-line) length; all three are norms. Do not confuse it with the sum of absolute coordinates: $x = (1,1)$ has $\|x\|_1 = 2$ but $\|x\|_2 = \sqrt{2}$.

**Details.** These are three members of the $\ell_p$ family $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$ for $p \ge 1$, with $\ell_\infty$ the limit as $p \to \infty$. For $p \lt 1$ the formula is not a norm: with $p = \tfrac12$, $x = (1,0)$, $y = (0,1)$ we get $\|x\|_{1/2} = \|y\|_{1/2} = 1$ but $\|x+y\|_{1/2} = (1+1)^2 = 4 \gt 2$. The proof that $\ell_p$ is a norm for $p \ge 1$ (Young, Holder, Minkowski) is in the backup note.

**Sources.** $\ell_1$ (Manhattan) and $\ell_2$ (Euclidean): Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.1, Examples 3.1 and 3.2. $\ell_p$: Wilkinson, MATH3030 notes, Section 2.3.1, Definition 2.9. $\ell_\infty = \max_i |x_i|$: Boyd and Vandenberghe, *Convex Optimization* (CUP 2004), Appendix A.1.3, p. 635, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf. The $(1,1)$ and $p = \tfrac12$ numbers: our calculation.
<!-- END S28 -->

<!-- BEGIN S29 -->
### 13. One Vector, Three Answers: 7, 5, 4 [S29]

**Message.** For $x = (3,4)$ the three norms report three different sizes, 7, 5 and 4, so the choice of norm is part of the question.

Arithmetic: $\|x\|_1 = |3| + |4| = 7$; $\|x\|_2 = \sqrt{9 + 16} = 5$; $\|x\|_\infty = \max(3, 4) = 4$. Geometrically, on a grid from the origin to the point $x = (3,4)$: the path that walks 3 to the right and then 4 up has total length $3 + 4 = 7$, which is $\ell_1$. The straight diagonal from the origin to $x$ has length 5, which is $\ell_2$. The longer of the two legs, 4, is $\ell_\infty$. For every vector, $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$, here $4 \le 5 \le 7$.

**Details.** **Why the ordering always holds.** $\|x\|_\infty^2 = \max_i x_i^2 \le \sum_i x_i^2 = \|x\|_2^2$. And $\|x\|_1^2 = \sum_i x_i^2 + \sum_{i \ne j} |x_i||x_j| \ge \|x\|_2^2$. Taking square roots of nonnegative quantities gives $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$.

Interpretation: $\ell_1$ adds up every coordinate, $\ell_\infty$ looks only at the worst one, and $\ell_2$ sits between them. The same contrast between "worst case" and "total" reappears for matrices as spectral norm versus Frobenius norm.

**Sources.** Our worked example (evidence E09: 7, 5, 4). Ordering proof: our derivation.
<!-- END S29 -->

<!-- BEGIN S30 -->
### 14. Unit Balls Reveal the Metric [S30]

**Message.** The unit ball $\{x : \|x\| \le 1\}$ is the set of vectors a norm calls at most 1, and its shape shows how the norm measures.

In the plane the three unit balls have three shapes. The $\ell_1$ ball is a diamond with corners on the axes at $(\pm1, 0)$ and $(0, \pm1)$. The $\ell_2$ ball is a round disc of radius 1. The $\ell_\infty$ ball is a square with corners at $(\pm1, \pm1)$. One boundary point of each: $(1,0)$ on the diamond ($|1| + |0| = 1$), $(\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2})$ on the circle ($\tfrac12 + \tfrac12 = 1$ under the square root), and the corner $(1,1)$ on the square ($\max(1,1) = 1$). Each of these points has norm exactly 1 in its own norm. The shapes are nested: diamond inside circle inside square.

**Details.** **Nesting.** From $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$: if $\|x\|_1 \le 1$ then $\|x\|_2 \le 1$, and if $\|x\|_2 \le 1$ then $\|x\|_\infty \le 1$. So the $\ell_1$ ball lies inside the $\ell_2$ ball, which lies inside the $\ell_\infty$ ball. The point $(1,1)$ is in the square but not in the circle ($\|(1,1)\|_2 = \sqrt2 \gt 1$).

**Sources.** Our illustration, drawn to scale (evidence E09 for the norms used). The unit-ball shapes follow directly from the definitions in sections 11 and 12.
<!-- END S30 -->

<!-- BEGIN S31 -->
### 15. Orthogonal Maps Preserve Geometry [S31]

**Message.** A square matrix $Q$ with $Q^\top Q = I$ turns vectors without changing their Euclidean length.

Definition: $Q \in \mathbb{R}^{n\times n}$ is orthogonal if $Q^\top Q = I = QQ^\top$; equivalently its columns are orthonormal, and $Q^{-1} = Q^\top$. Example: the $45^\circ$ rotation $Q = \tfrac{1}{\sqrt2}\left[\begin{smallmatrix}1 & -1\\ 1 & 1\end{smallmatrix}\right]$ sends $e_1$ to $Qe_1 = (\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2})$, at a $45^\circ$ angle from $e_1$. Both vectors lie on the unit circle: the direction changed, the Euclidean length stayed 1. Squareness matters. The tall matrix $W = [e_1\; e_2] \in \mathbb{R}^{3\times 2}$ has orthonormal columns, so $W^\top W = I_2$, but $WW^\top = \operatorname{diag}(1,1,0) \ne I_3$; it is not an orthogonal matrix. And the protection is for $\ell_2$ only, not every norm (section 16).

**Details.** For square $Q$, $Q^\top Q = I$ already implies $QQ^\top = I$ (a square matrix with a left inverse is invertible, and the inverse is that left inverse). Further equivalent characterizations, orthonormal rows, $\det Q = \pm1$, and Gram-Schmidt are in the backup note. Check of the example: the columns $\tfrac{1}{\sqrt2}(1,1)$ and $\tfrac{1}{\sqrt2}(-1,1)$ each have length 1 and dot product $\tfrac12(-1+1) = 0$.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.4, Definition 3.8 (orthogonal matrix: square, $AA^\top = I = A^\top A$). Rotation and $W$ examples: our illustration.
<!-- END S31 -->

<!-- BEGIN S33 -->
### 16. Why Length Is Preserved [S33]

**Message.** One line of algebra using $Q^\top Q = I$ shows that a square orthogonal $Q$ preserves the Euclidean norm of every vector.

Claim: for square $Q \in \mathbb{R}^{n\times n}$ with $Q^\top Q = I$ and every $x \in \mathbb{R}^n$, $\|Qx\|_2 = \|x\|_2$. Proof: $\|Qx\|_2^2 = (Qx)^\top(Qx) = x^\top Q^\top Q x = x^\top x = \|x\|_2^2$, where the middle step uses $Q^\top Q = I$; both norms are nonnegative, so taking square roots gives the claim. The same step with two vectors gives $(Qx)^\top(Qy) = x^\top y$, so inner products, and hence angles, are preserved too. The protection is specific to the Euclidean norm: for the $45^\circ$ rotation, $\|Qe_1\|_1 = \tfrac{1}{\sqrt2} + \tfrac{1}{\sqrt2} = \sqrt2$, while $\|e_1\|_1 = 1$.

**Details.** The proof uses only $Q^\top Q = I$, not squareness, so it also shows that a tall matrix with orthonormal columns (like $W$ in section 15) preserves Euclidean length. Squareness is needed for the converse direction and for $QQ^\top = I$. Conversely, a square $Q$ with $\|Qx\|_2 = \|x\|_2$ for all $x$ is orthogonal, by the polarization identity $x^\top y = \tfrac12(\|x+y\|_2^2 - \|x\|_2^2 - \|y\|_2^2)$; details in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.4, Definition 3.8 and eqs. (3.31) (length preserved) and (3.32) (angles preserved). $\ell_1$ counterexample: our calculation.
<!-- END S33 -->

<!-- BEGIN S66 -->
### 17. Spectral Norm: Worst Stretch [S66]

**Message.** The spectral norm of a matrix is the largest factor by which it stretches any unit-length input.

Definition: for $A \in \mathbb{R}^{m\times n}$, $\|A\|_2 = \max_{x \in \mathbb{R}^n,\ \|x\|_2 = 1} \|Ax\|_2$. It is one number for the whole matrix. Take the running example $A = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right]$. It maps the input unit circle to a tall, tilted ellipse. One input $x^\star$ on the circle is mapped to the farthest point of the ellipse; that longest image $Ax^\star$ has length $\|A\|_2$. This picture is only intuition for "worst direction"; how to compute that length comes later in the lecture. Keep three things apart: $\|A\|_2$ is a matrix norm; $\|x\|_2$ is the length of a vector; and the $\ell_2$ norm of all entries of $A$ is a different matrix norm, the Frobenius norm (section 18).

**Details.** **Figure geometry.** The ellipse is the exact image $\{A(\cos t, \sin t)\} = \{(3\cos t,\ 4\cos t + 5\sin t)\}$. The marked input is $x^\star = (1,1)/\sqrt2$, and $Ax^\star = (3, 9)/\sqrt2$; a numerical scan of $t$ confirms this is where $\|A(\cos t, \sin t)\|_2$ is largest. The numerical value is deliberately not stated here; it is derived with the singular values later.

The maximum is attained because $x \mapsto \|Ax\|_2$ is continuous and the unit sphere is compact. Equivalently $\|A\|_2 = \max_{x \ne 0} \|Ax\|_2 / \|x\|_2$, by homogeneity. Other induced norms ($p = 1, \infty$) and submultiplicativity $\|AB\|_2 \le \|A\|_2\|B\|_2$ are in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 4.6, Definition 4.23 (spectral norm, eq. (4.93)); Wilkinson, MATH3030 notes, Section 3.5.1, Definition 3.2 (matrix $p$-norms, here $p = 2$). Figure: our running example (evidence E08), computed exactly.
<!-- END S66 -->

<!-- BEGIN S72 -->
### 18. Frobenius Norm: Total Energy [S72]

**Message.** The squared Frobenius norm adds up every squared entry, so $\|A - B\|_F^2$ is the total squared error over all entries.

Definition: $\|A\|_F = (\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2)^{1/2}$, and for a residual $\|A - B\|_F^2 = \sum_{i,j} (a_{ij} - b_{ij})^2$. Square each entry of the residual $A - B$ from the opening example: the first row gives $1.5^2 = 2.25$ and $(-1.5)^2 = 2.25$, the second row gives $(-0.5)^2 = 0.25$ and $0.5^2 = 0.25$. The first row contributes far more. The sum is $5$, so $\|A - B\|_F = \sqrt5$. Qualifiers: every entry is observed and counts equally (no weights), and the Frobenius norm is not the spectral norm in general. For the identity $I_2$, $\|I_2\|_2 = 1$ (it stretches nothing) but $\|I_2\|_F = \sqrt2$.

**Details.** **Square root versus square.** The norm is the square root, which makes it a norm (it is the Euclidean norm of the matrix read as a vector of $mn$ numbers). The squared version is the "energy": it is additive over entries, which is why least-squares objectives use it.

**Trace form (optional).** $\|A\|_F^2 = \operatorname{tr}(A^\top A)$, since the diagonal entries of $A^\top A$ are the squared column lengths.

**Arithmetic.** $2.25 + 2.25 + 0.25 + 0.25 = 5$; $\sqrt5 \approx 2.236$.

**Sources.** Wilkinson, MATH3030 notes, Section 3.5.1, Definition 3.1 ($\|A\|_F = (\sum_{i,j} |a_{ij}|^2)^{1/2} = (\operatorname{tr} A^\top A)^{1/2}$). Residual numbers: our calculation on the running example (evidence E08).
<!-- END S72 -->
<!-- REGION P1b END -->

<!-- REGION P2 BEGIN -->

<!-- BEGIN S35 -->
### 19. Part 3: Reading an SVD [S35]

**Message.** Part 3 builds the singular value decomposition and reads every factor on one worked matrix.
<!-- END S35 -->

<!-- BEGIN S36 -->
### 20. Recall: Symmetric Eigendecomposition [S36]

**Message.** The SVD is built from one imported fact: a symmetric matrix has an orthonormal eigenbasis, and for $A^\top A$ every eigenvalue is nonnegative.

Recall: every symmetric $S \in \mathbb R^{n\times n}$ factors as $S = Q\Lambda Q^\top$ with $Q$ orthogonal and $\Lambda$ real diagonal. Apply this to $A^\top A$, which is symmetric and $n \times n$, so it acts on input vectors $x \in \mathbb R^n$. This gives $A^\top A = Q\Lambda Q^\top$ and $\lambda_i = q_i^\top A^\top A q_i = \|Aq_i\|_2^2 \ge 0$. The payoff: $A^\top A$ supplies orthonormal input directions $q_1, \dots, q_n$ in $\mathbb R^n$.

**Details.**

**Why the eigenvalues are nonnegative.** For a unit eigenvector $q_i$, $\lambda_i = q_i^\top (\lambda_i q_i) = q_i^\top A^\top A q_i = (Aq_i)^\top (Aq_i) = \|Aq_i\|_2^2 \ge 0$. More generally $x^\top A^\top A x = \|Ax\|_2^2 \ge 0$ for every $x$, so $A^\top A$ is positive semidefinite.

**What is imported.** The spectral theorem itself is not proved in this lecture; it is the one black box. Everything else in Part 3 is derived from it.

**Why input space.** $A^\top A$ is $n \times n$, the same size as the input dimension of $A$. Its eigenvectors will become the right singular vectors $v_i$ in sections 21-23.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.2, Theorem 4.14 ($A^\top A$ symmetric positive semidefinite) and Theorem 4.15 (spectral theorem).
<!-- END S36 -->

<!-- BEGIN S38 -->
### 21. Every Matrix Has an SVD [S38]

**Message.** Every real matrix, of any shape and rank, factors as an orthogonal matrix times a nonnegative diagonal stretch times an orthogonal matrix.

SVD theorem. Every $A \in \mathbb R^{m\times n}$ of rank $r$, with no assumption of squareness, symmetry or invertibility, factors as $A = U\Sigma V^\top$ with $U \in \mathbb R^{m\times m}$ and $V \in \mathbb R^{n\times n}$ orthogonal. Here $\Sigma \in \mathbb R^{m\times n}$ has $\Sigma_{ii} = \sigma_i$, zeros off the diagonal, $\sigma_1 \ge \dots \ge \sigma_r \gt 0$, and the remaining diagonal slots equal to $0$. The construction: eigenvectors of $A^\top A$ give $V$, then $u_i = Av_i/\sigma_i$ for $\sigma_i \gt 0$.

**Details.**

**Construction sketch.** Take the eigendecomposition $A^\top A = V\Lambda V^\top$ with eigenvalues in decreasing order and set $\sigma_i = \sqrt{\lambda_i}$. Exactly $r$ of them are positive because $\operatorname{rank}(A^\top A) = \operatorname{rank}(A) = r$. For $i \le r$ put $u_i = Av_i/\sigma_i$; these are orthonormal because $u_i^\top u_j = v_i^\top A^\top A v_j/(\sigma_i\sigma_j) = \lambda_j v_i^\top v_j/(\sigma_i\sigma_j) = \delta_{ij}$. Extend $u_1, \dots, u_r$ to an orthonormal basis of $\mathbb R^m$. Then $AV = U\Sigma$ column by column (for $i \gt r$, $\|Av_i\|_2^2 = \lambda_i = 0$), so $A = U\Sigma V^\top$.

**Uniqueness.** The singular values are unique. The vectors are unique up to sign when the $\sigma_i$ are distinct and positive; repeated values allow any orthonormal basis of the shared subspace. The full existence and uniqueness proof is kept in the archived full note.

**Naming.** The lecture cites its results by name, not number: the SVD theorem here, then the spectral-norm and Frobenius-norm identities read off $\Sigma$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5, Theorem 4.22 (SVD theorem); Section 4.5.2, eq. (4.78), $u_i = Av_i/\sigma_i$.
<!-- END S38 -->

<!-- BEGIN S39 -->
### 22. Read the Factor Shapes [S39]

**Message.** The factor shapes $(m\times m)(m\times n)(n\times n)$ multiply to $m \times n$, and only the first $r$ diagonal slots of $\Sigma$ are nonzero.

Take a tall matrix, $m \gt n$. Then $A$ ($m \times n$) equals a square orthogonal $U$ ($m \times m$), times $\Sigma$ ($m \times n$, tall like $A$), times a smaller square orthogonal $V^\top$ ($n \times n$). The shapes multiply as $(m\times m)(m\times n)(n\times n) = m \times n$. The diagonal of $\Sigma$ starts with the positive values $\sigma_1, \dots, \sigma_r \gt 0$ and continues with zeros in the remaining diagonal slots; the last $m - n$ rows of $\Sigma$ are entirely zero.

**Details.**

**Names.** The columns $u_i$ of $U$ are the left singular vectors (in output space $\mathbb R^m$); the columns $v_i$ of $V$ are the right singular vectors (in input space $\mathbb R^n$).

**Other shapes.** For $m \lt n$ the zero block of $\Sigma$ is a set of columns on the right instead of rows at the bottom. For square $A$ there is no zero block, only zero diagonal entries when $r \lt n$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5, eq. (4.64) and the shape discussion after Theorem 4.22.
<!-- END S39 -->

<!-- BEGIN S40 -->
### 23. Rotate, Stretch, Rotate [S40]

**Message.** Multiplying by $A = U\Sigma V^\top$ is three steps: an orthogonal change of input coordinates, a stretch by the singular values, and an orthogonal change of output coordinates.

The input passes through four stages: $x$ in $\mathbb R^n$, then $V^\top x$ in $\mathbb R^n$ (apply $V^\top$, orthogonal), then $\Sigma V^\top x$ in $\mathbb R^m$ (apply $\Sigma$, a stretch), then $Ax$ in $\mathbb R^m$ (apply $U$, orthogonal). In one formula, $Ax = U(\Sigma(V^\top x))$: the rightmost factor acts first. The roles: $V^\top$ and $U$ are rotations or reflections that keep lengths; $\Sigma$, of size $m \times n$, multiplies coordinate $i$ by $\sigma_i$ and is not a rotation.

**Details.**

**Why lengths are kept.** For orthogonal $Q$, $\|Qx\|_2^2 = x^\top Q^\top Q x = \|x\|_2^2$. This orthogonal invariance was proved earlier in the lecture and is used again in the norm proofs below.

**Change of space.** $\Sigma$ is the only step that can change dimension: it maps $\mathbb R^n$ to $\mathbb R^m$, dropping coordinates when $m \lt n$ and padding with zeros when $m \gt n$.

**Rotation or reflection.** An orthogonal matrix has determinant $\pm 1$; with determinant $-1$ it includes a reflection. In the worked example below both $U$ and $V$ have determinant $1$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.1 and Figure 4.8 (basis change, scaling, basis change).
<!-- END S40 -->

<!-- BEGIN S52 -->
### 24. First Change the Input Coordinates [S52]

**Message.** The first step $V^\top$ only changes coordinates: the unit circle stays a circle and the right singular vectors become the coordinate axes.

Follow the unit circle of inputs through $V^\top$, for the worked matrix used later, with $v_1 = (1,1)/\sqrt2$ and $v_2 = (-1,1)/\sqrt2$. Before the step, $v_1$ points up and to the right at $45$ degrees and $v_2$ points up and to the left. After $V^\top$ the circle is the same circle, with $v_1$ now along the horizontal axis as $e_1$ and $v_2$ along the vertical axis as $e_2$. $V^\top$ is orthogonal, so lengths are kept and nothing is stretched.

**Details.**

**Check.** $V^\top v_1 = e_1$ and $V^\top v_2 = e_2$ because the rows of $V^\top$ are $v_1^\top, v_2^\top$ and these are orthonormal. Here $V = \frac{1}{\sqrt2}\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ has determinant $1$, so $V^\top$ is a rotation by $-45$ degrees.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.1, Figure 4.8. Vectors: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S52 -->

<!-- BEGIN S53 -->
### 25. Then Stretch and Reorient [S53]

**Message.** $\Sigma$ stretches the axes by $\sigma_1$ and $\sigma_2$, and $U$ turns them into the output directions: the image of the unit circle is an ellipse with semi-axes $\sigma_1 u_1$ and $\sigma_2 u_2$.

Continue the sequence. After $\Sigma$, the circle becomes an axis-aligned ellipse three times as wide as it is tall, with semi-axes $\sigma_1 e_1$ along the horizontal axis and $\sigma_2 e_2$ along the vertical axis. After $U$, the same ellipse is tilted steeply up and to the right, with the long semi-axis $\sigma_1 u_1$ pointing along $(1,3)$ and the short one $\sigma_2 u_2$ pointing along $(-3,1)$; this ellipse is the set of all $Ax$ for unit $x$. The semi-axis lengths are the singular values $\sigma_1 = 3\sqrt5 \approx 6.71$ and $\sigma_2 = \sqrt5 \approx 2.24$. These are not the eigenvalues $3$ and $5$ of $A$. The axis ratio is exactly $3:1$.

**Details.**

**Why an ellipse.** After $V^\top$ the input is a unit vector $y$; $\Sigma y = (\sigma_1 y_1, \sigma_2 y_2)$ satisfies $(z_1/\sigma_1)^2 + (z_2/\sigma_2)^2 = 1$, an axis-aligned ellipse. $U$ is orthogonal, so it moves the ellipse rigidly.

**Drawing scale.** In the lecture's figure the semi-axes are $120$ and $40$ units, ratio $3 = \sigma_1/\sigma_2$; the tilt is $\arctan 3 \approx 71.57$ degrees, the direction of $u_1 = (1,3)/\sqrt{10}$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.1, Figure 4.8. Numbers: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S53 -->

<!-- BEGIN S41 -->
### 26. A Sum of Rank-One Layers [S41]

**Message.** Expanding $U\Sigma V^\top$ writes $A$ as a sum of $r$ rank-one layers $\sigma_i u_i v_i^\top$, ordered by weight.

Expand: $A = U\Sigma V^\top = \sum_{i=1}^r \sigma_i u_i v_i^\top$, where $u_i$ is $m \times 1$ and $v_i^\top$ is $1 \times n$. Three facts follow: each $u_i v_i^\top$ is $m \times n$ with every column a multiple of $u_i$; when $\sigma_i \gt 0$ the term has rank one; and all $r$ terms together give $A$ exactly. Think of $A$ as layer $1 + \dots +$ layer $r$, stacked like sheets: the first layer $\sigma_1 u_1 v_1^\top$ has the largest weight, and later layers carry smaller $\sigma_i$.

**Details.**

**Derivation.** The columns of $U\Sigma$ are $\sigma_i u_i$ for $i \le r$ and zero otherwise. Multiplying by $V^\top$, whose rows are $v_i^\top$, gives $U\Sigma V^\top = \sum_{i=1}^r (\sigma_i u_i) v_i^\top$ by the column-times-row form of matrix multiplication.

**Rank one.** Column $j$ of $u_i v_i^\top$ is $(v_i)_j u_i$, a multiple of $u_i$, and $v_i \ne 0$, so the column space is exactly the span of $u_i$.

**Forward pointer.** The partial sum of the first $k$ layers is written $A_k = \sum_{i \le k}\sigma_i u_i v_i^\top$. Whether $A_k$ is the best rank-$k$ approximation is a separate theorem, proved later in the lecture.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6 (matrix approximation as a sum of rank-one matrices).
<!-- END S41 -->

<!-- BEGIN S42 -->
### 27. Compact SVD Keeps Active Directions [S42]

**Message.** Dropping the zero singular values leaves the compact SVD $A = U_r\Sigma_r V_r^\top$, which is still exact; its factors $U_r$ and $V_r$ have orthonormal columns but need not be square orthogonal matrices.

The $m \times n$ matrix $A$ equals a thin tall $U_r$ ($m \times r$), times a small square $\Sigma_r$ ($r \times r$) with a full diagonal, times a short wide $V_r^\top$ ($r \times n$); only the $r$ nonzero $\sigma_i$ are kept. In formulas, $A = U_r\Sigma_r V_r^\top$, $\Sigma_r = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$, $U_r^\top U_r = V_r^\top V_r = I_r$. When $r \lt m$, $U_r U_r^\top \ne I_m$: the thin factors have orthonormal columns but are not square orthogonal matrices.

**Details.**

**Why it is exact.** The rank-one expansion uses only $i \le r$, and $U_r\Sigma_r V_r^\top$ is exactly that sum. The discarded columns of $U$ and $V$ only ever multiply zeros of $\Sigma$.

**What $U_r U_r^\top$ is.** It is the orthogonal projector onto the column space of $A$; it equals $I_m$ only when $r = m$. Likewise $V_r V_r^\top$ projects onto the row space.

**Notation.** This revision writes the compact factors with subscript $r$ ($U_r, \Sigma_r, V_r$), matching the rank.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5 (reduced SVD discussion).
<!-- END S42 -->

<!-- BEGIN S44 -->
### 28. One Matrix, One Construction [S44]

**Message.** One non-symmetric $2\times 2$ matrix carries the whole construction: form $A^\top A$, take eigenpairs, take square roots, and divide to get the outputs.

The worked example is introduced as $A = \begin{bmatrix}3 & 0\\ 4 & 5\end{bmatrix}$, not symmetric, used to the end of the lecture. Substitute the SVD into $A^\top A$: $A^\top A = V\Sigma^\top U^\top U\Sigma V^\top = V\Sigma^\top\Sigma V^\top$ because $U^\top U = I$, so the eigenvalues of $A^\top A$ are the $\sigma_i^2$. The route has four steps:

1. Form $A^\top A$.
2. Find its eigenpairs $\lambda_i, v_i$.
3. Take the stretches $\sigma_i = \sqrt{\lambda_i}$.
4. Compute the outputs $u_i = Av_i/\sigma_i$.

**Details.**

**Why the route works.** $V\Sigma^\top\Sigma V^\top$ is an eigendecomposition: $\Sigma^\top\Sigma$ is $n \times n$ diagonal with entries $\sigma_i^2$ (and zeros), and $V$ is orthogonal. So the right singular vectors are eigenvectors of $A^\top A$, and the eigenvalues are the squared stretches.

**Step 4.** Dividing by $\sigma_i$ is allowed only when $\sigma_i \gt 0$; the zero singular values give no $u_i$ this way, and the remaining columns of $U$ are filled in by any orthonormal completion.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.2 (construction of the SVD). Example: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S44 -->

<!-- BEGIN S45 -->
### 29. Build the Symmetric Matrix $A^\top A$ [S45]

**Message.** For the worked example, $A^\top A = \begin{bmatrix}25 & 20\\ 20 & 25\end{bmatrix}$, and each entry is a dot product of two columns of $A$.

Multiply $A^\top = \begin{bmatrix}3 & 4\\ 0 & 5\end{bmatrix}$ by $A$ to get $\begin{bmatrix}25 & 20\\ 20 & 25\end{bmatrix}$. Entry $(i,j)$ is column $i$ of $A$ dotted with column $j$; the three distinct dot products are $3^2 + 4^2 = 25$, $3\cdot 0 + 4\cdot 5 = 20$, and $0^2 + 5^2 = 25$. The result is $2\times 2$, symmetric and positive semidefinite, ready for an eigenproblem.

**Details.**

**Columns of $A$.** Column 1 is $(3,4)$ and column 2 is $(0,5)$. Their squared lengths $25$ and $25$ sit on the diagonal; their dot product $20$ sits off the diagonal.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S45 -->

<!-- BEGIN S46 -->
### 30. The Eigenvalues Are 45 and 5 [S46]

**Message.** The eigenvalues of $A^\top A$ are $45$ and $5$; they are the squared singular values, not eigenvalues of $A$.

Factor the characteristic polynomial as a difference of squares: $\det(A^\top A - \lambda I) = (25-\lambda)^2 - 20^2 = (25-\lambda-20)(25-\lambda+20) = (5-\lambda)(45-\lambda)$. So $\lambda_1 = 45 \ge \lambda_2 = 5$, with two checks: the sum $50$ equals the trace $25+25$, and the product $225$ equals the determinant $25^2 - 20^2$. These are eigenvalues of $A^\top A$, the squared stretches $\sigma_i^2$, not eigenvalues of $A$.

**Details.**

**Arithmetic.** $25^2 - 20^2 = 625 - 400 = 225 = 45 \cdot 5$. Also $\det(A^\top A) = (\det A)^2 = 15^2 = 225$.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S46 -->

<!-- BEGIN S47 -->
### 31. Orthonormal Input Directions [S47]

**Message.** Solving the two null-space problems gives $v_1 = (1,1)/\sqrt2$ and $v_2 = (-1,1)/\sqrt2$: orthonormal input directions.

Solve $(A^\top A - \lambda I)v = 0$ for each eigenvalue. For $\lambda_1 = 45$ the matrix is $\begin{bmatrix}-20 & 20\\ 20 & -20\end{bmatrix}$, whose null space is spanned by $(1,1)$, so $v_1 = (1,1)/\sqrt2$. For $\lambda_2 = 5$ the matrix is $\begin{bmatrix}20 & 20\\ 20 & 20\end{bmatrix}$, giving $v_2 = (-1,1)/\sqrt2$. Check: $v_1^\top v_2 = \frac12(-1+1) = 0$ and both vectors have length $1$. The sign is a choice: $-v_i$ also works, provided $u_i$ flips with it.

**Details.**

**Sign convention.** Replacing $v_i$ by $-v_i$ replaces $u_i = Av_i/\sigma_i$ by $-u_i$, and $\sigma_i u_i v_i^\top$ is unchanged. The lecture fixes the signs above.

**Geometry.** $V = [v_1\ v_2] = \frac{1}{\sqrt2}\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ is the rotation by $45$ degrees (determinant $1$).

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S47 -->

<!-- BEGIN S48 -->
### 32. Recover Stretches and Output Directions [S48]

**Message.** Square roots give $\sigma_1 = 3\sqrt5$ and $\sigma_2 = \sqrt5$, and $u_i = Av_i/\sigma_i$ gives $u_1 = (1,3)/\sqrt{10}$ and $u_2 = (-3,1)/\sqrt{10}$.

Square roots give $\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.71$ and $\sigma_2 = \sqrt5 \approx 2.24$. Then compute $Av_1 = (3,9)/\sqrt2$ and divides by $3\sqrt5$ to get $u_1 = (1,3)/\sqrt{10}$, and compute $Av_2 = (-3,1)/\sqrt2$ and divides by $\sqrt5$ to get $u_2 = (-3,1)/\sqrt{10}$. Check: $u_1^\top u_2 = \frac{1}{10}(-3+3) = 0$, both of length $1$, and both $\sigma_i \gt 0$ so the divisions are allowed.

**Details.**

**Arithmetic.** $Av_1 = \frac{1}{\sqrt2}(3\cdot1 + 0\cdot1,\ 4\cdot1 + 5\cdot1) = (3,9)/\sqrt2$; dividing by $3\sqrt5$ gives $(1,3)/\sqrt{10}$ since $\sqrt2\cdot\sqrt5 = \sqrt{10}$. $Av_2 = \frac{1}{\sqrt2}(-3,\ -4+5) = (-3,1)/\sqrt2$. Lengths: $(1+9)/10 = 1$ for both.

**Geometry.** $U = \frac{1}{\sqrt{10}}\begin{bmatrix}1 & -3\\ 3 & 1\end{bmatrix}$ has determinant $(1+9)/10 = 1$, a rotation by $\arctan 3 \approx 71.57$ degrees.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S48 -->

<!-- BEGIN S49 -->
### 33. The Factors Reconstruct $A$ [S49]

**Message.** Multiplying the three computed factors gives back $A$ exactly.

Write $A$ as the product of $U = \frac{1}{\sqrt{10}}\begin{bmatrix}1 & -3\\ 3 & 1\end{bmatrix}$, $\Sigma = \operatorname{diag}(3\sqrt5, \sqrt5)$ and $V^\top = \frac{1}{\sqrt2}\begin{bmatrix}1 & 1\\ -1 & 1\end{bmatrix}$. Multiply in two steps: $U\Sigma = \frac{1}{\sqrt2}\begin{bmatrix}3 & -3\\ 9 & 1\end{bmatrix}$, then $(U\Sigma)V^\top = \frac12\begin{bmatrix}6 & 0\\ 8 & 10\end{bmatrix} = A$, as required. Recall that the columns of $U$ are $u_1, u_2$ and the rows of $V^\top$ are $v_1^\top, v_2^\top$.

**Details.**

**Arithmetic.** $U\Sigma$: column 1 is $3\sqrt5\,(1,3)/\sqrt{10} = (3,9)/\sqrt2$ and column 2 is $\sqrt5\,(-3,1)/\sqrt{10} = (-3,1)/\sqrt2$. Then row 1 of $(U\Sigma)V^\top$ is $\frac12(3\cdot1 + (-3)(-1),\ 3\cdot1 + (-3)\cdot1) = \frac12(6, 0)$ and row 2 is $\frac12(9 - 1,\ 9 + 1) = \frac12(8, 10)$.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S49 -->

<!-- BEGIN S50 -->
### 34. The First Layer Carries Most Energy [S50]

**Message.** The first rank-one layer $A_1$ carries $45$ of the total energy $50$, that is $90\%$; this is a reconstruction fact, not yet an optimality claim.

Split $A$ into its two layers: $A_1 = \sigma_1 u_1 v_1^\top = \begin{bmatrix}1.5 & 1.5\\ 4.5 & 4.5\end{bmatrix}$ plus $\sigma_2 u_2 v_2^\top = \begin{bmatrix}1.5 & -1.5\\ -0.5 & 0.5\end{bmatrix}$. The energies, squared Frobenius norms, satisfy $50 = 45 + 5$, so the first layer's share is $45/50 = 90\%$. This is reconstruction, not optimality: it does not yet show $A_1$ is the best rank-one approximation.

**Details.**

**Arithmetic.** $\sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}}(1,3) \cdot \frac{1}{\sqrt2}(1,1)^\top = \frac{3}{2}\begin{bmatrix}1 & 1\\ 3 & 3\end{bmatrix}$, entries summing in squares to $\frac94(1+1+9+9) = 45$. $\sigma_2 u_2 v_2^\top = \sqrt5 \cdot \frac{1}{\sqrt{10}}(-3,1) \cdot \frac{1}{\sqrt2}(-1,1)^\top = \frac12\begin{bmatrix}3 & -3\\ -1 & 1\end{bmatrix}$, squared entries $\frac14(9+9+1+1) = 5$. The two layers add to $A$ entry by entry. $\|A\|_F^2 = 9 + 0 + 16 + 25 = 50$.

**Why the energies add.** The layers are orthogonal in the Frobenius inner product because $u_1 \perp u_2$; the Frobenius-norm identity (section 39) states the general identity $\|A\|_F^2 = \sum_i \sigma_i^2$.

**Forward pointer.** That $A_1$ is the best rank-one approximation, in both the spectral and Frobenius norms, is the Eckart-Young-Mirsky theorem, later in the lecture.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S50 -->

<!-- BEGIN S51 -->
### 35. Eigenvalues Are Not Singular Values [S51]

**Message.** For a non-symmetric matrix the eigenvalues and the singular values are different lists; the eigenvalues of $A^\top A$ are the squared singular values.

Compare two lists for the same $A = \begin{bmatrix}3 & 0\\ 4 & 5\end{bmatrix}$. The eigenvalues of $A$ are $3$ and $5$, read from the diagonal of a triangular matrix; an eigenvector keeps its direction, $Ax = \lambda x$. The singular values are $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$; a singular pair satisfies $Av_i = \sigma_i u_i$, so the direction may turn. The link: $45$ and $5$ are eigenvalues of $A^\top A$, the squares $\sigma_i^2$. The two lists coincide for symmetric positive semidefinite $A$ but differ in general.

**Details.**

**Eigenvectors of $A$.** $\det(A - \lambda I) = (3-\lambda)(5-\lambda)$. For $\lambda = 3$, $(1,-2)$ works: $A(1,-2) = (3, -6)$. For $\lambda = 5$, $(0,1)$ works: $A(0,1) = (0,5)$. These are not orthogonal: $(1,-2)\cdot(0,1) = -2$.

**One shared quantity.** Both products equal $|\det A| = 15$: $3 \cdot 5 = 15$ and $3\sqrt5 \cdot \sqrt5 = 15$.

**Symmetric case.** For symmetric $A = Q\Lambda Q^\top$ the singular values are $|\lambda_i|$; they equal the eigenvalues only when all $\lambda_i \ge 0$. A symmetric matrix with a negative eigenvalue has eigendecomposition and SVD that differ by signs. Note: MML Section 4.5.3 states the symmetric case without the positive semidefinite condition.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.3 (eigenvalue decomposition vs SVD). Example: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S51 -->

<!-- BEGIN S68 -->
### 36. Largest Singular Value, Largest Stretch [S68]

**Message.** The spectral norm, the largest stretch of any unit vector, equals the largest singular value $\sigma_1$; the proof needs an upper bound and a witness.

Spectral-norm identity. For every $A \in \mathbb R^{m\times n}$ with largest singular value $\sigma_1$, $\|A\|_2 = \max_{\|x\|_2 = 1}\|Ax\|_2 = \sigma_1$. The proof has two tasks:

1. An upper bound: $\|Ax\|_2 \le \sigma_1$ for every unit $x$.
2. A witness: one unit $x$ with $\|Ax\|_2 = \sigma_1$.

**Details.**

**Why two tasks.** A maximum equals $\sigma_1$ exactly when nothing exceeds $\sigma_1$ and something reaches it. Sections 37 and 38 do the two tasks.

**Geometry.** In the ellipse picture of section 25, $\sigma_1$ is the longest semi-axis of the image of the unit circle.

**Definition.** $\|\cdot\|_2$ as the worst stretch was defined earlier in the lecture.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Definition 4.23 and Theorem 4.24 (proof left as an exercise there). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html, Proposition 3.11.
<!-- END S68 -->

<!-- BEGIN S69 -->
### 37. No Direction Beats the Largest Stretch [S69]

**Message.** After the orthogonal change of coordinates $y = V^\top x$, every unit input is stretched by at most $\sigma_1$.

Take any unit $x \in \mathbb R^n$ and set $y = V^\top x$, which is also a unit vector by orthogonal invariance. Then $\|Ax\|_2^2 = \|U\Sigma y\|_2^2 = \|\Sigma y\|_2^2$ (since $U$ is orthogonal) $= \sum_{i=1}^r \sigma_i^2 y_i^2 \le \sigma_1^2\sum_{i=1}^n y_i^2 = \sigma_1^2\|y\|_2^2 = \sigma_1^2$ (since every $\sigma_i \le \sigma_1$). As $x$ runs over all unit vectors so does $y$, so no direction is skipped.

**Details.**

**The inequality step.** Each term $\sigma_i^2 y_i^2 \le \sigma_1^2 y_i^2$, and extending the sum from $r$ to $n$ only adds nonnegative terms $\sigma_1^2 y_i^2$.

**Coverage.** $V^\top$ is invertible with inverse $V$, so $x \mapsto V^\top x$ is a bijection of the unit sphere onto itself; bounding over all unit $y$ is the same as bounding over all unit $x$.

**Shape.** $\Sigma y$ lies in $\mathbb R^m$ and its only nonzero coordinates are $\sigma_i y_i$ for $i \le r$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Theorem 4.24 (exercise). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html, Proposition 3.11.
<!-- END S69 -->

<!-- BEGIN S70 -->
### 38. The First Singular Vector Attains It [S70]

**Message.** The input $x = v_1$ is stretched by exactly $\sigma_1$, so together with the upper bound $\|A\|_2 = \sigma_1$.

Take the unit witness $x = v_1$. Compute $Av_1 = U\Sigma V^\top v_1 = U\Sigma e_1 = \sigma_1 u_1$, so $\|Av_1\|_2 = \sigma_1$ because $u_1$ is a unit vector. This closes the argument: $\sigma_1 = \|Av_1\|_2 \le \|A\|_2 \le \sigma_1$ by the upper bound, hence $\|A\|_2 = \sigma_1$, end of proof. Geometrically, $\sigma_1 u_1$ is the longest semi-axis of the image ellipse.

**Details.**

**Step $V^\top v_1 = e_1$.** The rows of $V^\top$ are $v_1^\top, \dots, v_n^\top$, and $v_j^\top v_1 = \delta_{j1}$.

**Edge case $A = 0$.** Then $r = 0$, every $\sigma_i = 0$ and $\|A\|_2 = 0$; the identity still holds with any unit $v_1$, since $Av_1 = 0 = \sigma_1 u_1$.

**Worked example.** $\|A\|_2 = 3\sqrt5 \approx 6.71$, attained at $v_1 = (1,1)/\sqrt2$ with $Av_1 = (3,9)/\sqrt2$, whose length is $\sqrt{90/2} = \sqrt{45}$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Theorem 4.24 (exercise). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html, Proposition 3.11.
<!-- END S70 -->

<!-- BEGIN S73 -->
### 39. Frobenius Energy Sums Squared Stretches [S73]

**Message.** The total energy $\|A\|_F^2$, the sum of all squared entries, equals the sum of all squared singular values.

Frobenius-norm identity. For every $A \in \mathbb R^{m\times n}$ of rank $r$: $\|A\|_F^2 = \sum_{i,j} a_{ij}^2 = \sum_{i=1}^r \sigma_i^2$. Contrast: $\|A\|_2 = \sigma_1$ measures the worst single direction while $\|A\|_F^2$ measures total energy (the norm itself is its square root $\|A\|_F$). Check on the worked example: $\|A\|_F^2 = 9 + 0 + 16 + 25 = 50 = 45 + 5$.

**Details.**

**Consequence.** $\|A\|_2 = \sigma_1 \le \|A\|_F \le \sqrt r\,\sigma_1$, since the sum has $r$ terms each at most $\sigma_1^2$. In the example, $\sqrt{45} \approx 6.71 \le \sqrt{50} \approx 7.07$.

**Definition.** $\|\cdot\|_F$ was defined earlier in the lecture; its square $\|\cdot\|_F^2$ is the total energy.

**Sources.**

R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html, Proposition 3.10.
<!-- END S73 -->

<!-- BEGIN S74 -->
### 40. Orthogonal Coordinates Preserve Total Energy [S74]

**Message.** Orthogonal matrices on either side do not change the Frobenius norm, so $\|A\|_F = \|U^\top A V\|_F = \|\Sigma\|_F$.

Fix orthogonal $Q$ and $W$ and a matrix $B$ with columns $b_j$. Prove invariance on each side. Columns: $\|QB\|_F^2 = \sum_j\|Qb_j\|_2^2 = \sum_j\|b_j\|_2^2 = \|B\|_F^2$, using vector invariance column by column. Rows, via the transpose: $\|BW\|_F = \|W^\top B^\top\|_F = \|B^\top\|_F = \|B\|_F$. Apply both with $Q = U^\top$ and $W = V$: $\|A\|_F^2 = \|U^\top A V\|_F^2 = \|\Sigma\|_F^2 = \sum_{i=1}^r\sigma_i^2$, end of proof.

**Details.**

**Transposition.** $\|B^\top\|_F = \|B\|_F$ because both sum the same squared entries.

**Alternative trace proof.** $\|A\|_F^2 = \operatorname{tr}(A^\top A) = \operatorname{tr}(V\Sigma^\top\Sigma V^\top) = \operatorname{tr}(\Sigma^\top\Sigma V^\top V) = \operatorname{tr}(\Sigma^\top\Sigma) = \sum_i\sigma_i^2$, using the cyclic property of the trace.

**Why $U^\top A V = \Sigma$.** Multiply $A = U\Sigma V^\top$ on the left by $U^\top$ and on the right by $V$.

**Sources.**

R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html, Proposition 3.10 (proof via $\|U^\top A V\|_F = \|\Sigma\|_F$).
<!-- END S74 -->

<!-- REGION P2 END -->

<!-- REGION P3a BEGIN -->

<!-- BEGIN S79 -->
### 41. Part 4: Best Low-Rank Approximation [S79]

**Message.** Part 4 states and proves that truncating the SVD gives the best rank-$k$ approximation.
<!-- END S79 -->

<!-- BEGIN S81 -->
### 42. Candidate: Keep the $k$ Largest Layers [S81]

**Message.** Sort the singular values and keep the $k$ largest rank-one layers; this truncation $A_k$ is the natural candidate, not yet a proven optimum.

The SVD writes $A = \sum_{i=1}^r \sigma_i u_i v_i^\top$ as a sum of $r$ rank-one layers, each scaled by a singular value. Under a rank budget $k$ the obvious move is to keep the $k$ layers with the largest singular values and drop the rest. That gives $A_k = \sum_{i=1}^k \sigma_i u_i v_i^\top$.

Write $A$ as one long sum and split it in two: the first $k$ terms form $A_k$, the kept part, and the remaining terms $\sigma_{k+1} u_{k+1} v_{k+1}^\top + \cdots + \sigma_r u_r v_r^\top$ are discarded.

For $i \leq k$, $A_k v_i = \sigma_i u_i$, so the range of $A_k$ contains the $k$ independent vectors $\sigma_1 u_1, \dots, \sigma_k u_k$; it also lies in their span, because every column of $A_k$ is a combination of $u_1, \dots, u_k$. So $A_k$ has rank exactly $k$ and is inside the budget $\operatorname{rank} \leq k$. Whether some other rank-$k$ matrix does better is the question the rest of the part answers.

**Details.**

The singular values are sorted, $\sigma_1 \geq \cdots \geq \sigma_r \gt 0$. When there are ties, $A_k$ depends on which singular vectors are chosen, but its error does not.

Edge cases. For $k = 0$ the empty sum gives $A_0 = 0$, with error $\|A\|$ in either norm. For $k \geq r$ we have $A_k = A$ and the error is zero, so the interesting range is $0 \leq k \lt r$, the range the theorems use.

In matrix form $A_k = U \Sigma_k V^\top$, where $\Sigma_k$ keeps the first $k$ diagonal entries of $\Sigma$ and zeroes the rest.

**Sources.**

Truncation $A_k$ as in Wilkinson [16], Section 3.5.2, Theorem 3.1.
<!-- END S81 -->

<!-- BEGIN S82 -->
### 43. Worked: $A_1$ Is the Top Layer of $A$ [S82]

**Message.** For the worked matrix, the top layer $\sigma_1 u_1 v_1^\top$ is the rank-one matrix with both columns equal to $1.5\,(1,3)^\top$.

Recall the SVD data of the worked matrix $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$: $\sigma_1 = 3\sqrt5$, $\sigma_2 = \sqrt5$, $u_1 = (1,3)^\top/\sqrt{10}$ and $v_1 = (1,1)^\top/\sqrt2$. Multiplying out the top layer gives $A_1$.

Both columns of $A_1$ are the same multiple of $u_1$, which is what rank one looks like on paper.

**Details.**

Multiplication:

$$\begin{aligned} A_1 &= \sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}\sqrt2} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} \\ &= \frac{3\sqrt5}{\sqrt{20}} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} = \frac{3}{2} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} \\ &= \begin{bmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{bmatrix},\end{aligned}$$

since $\sqrt{20} = 2\sqrt5$. Check: $\|A_1\|_F^2 = 2(1.5^2) + 2(4.5^2) = 4.5 + 40.5 = 45 = \sigma_1^2$.

Retained directions: $A_1$ maps $v_1$ to $\sigma_1 u_1$ and kills $v_2 = (-1,1)^\top/\sqrt2$. Its range is the line through $u_1$.

**Sources.**

Worked example and its SVD as computed earlier in this lecture (Part 3); arithmetic checked above.
<!-- END S82 -->

<!-- BEGIN S83 -->
### 44. Worked: $A_1$'s Error Is the Discarded Layer [S83]

**Message.** The residual $A - A_1$ is exactly the dropped layer $\sigma_2 u_2 v_2^\top$, so its error is $\sqrt5$ in both norms; this computes one candidate's error and proves nothing about other candidates.

Subtracting $A_1$ from $A$ leaves the second layer alone. That residual has rank one, so its only singular value is $\sigma_2 = \sqrt5$, and the spectral norm (largest singular value) equals $\sqrt5$. The Frobenius norm, computed entry by entry, is also $\sqrt5$.

The two norms agree here only because the residual has rank one. A residual with two or more nonzero singular values separates them, as section 65, Worst Error and Total Error Can Differ, illustrates.

This calculation does not compare $A_1$ with other rank-one matrices. That comparison is the theorem.

**Details.**

With $u_2 = (-3,1)^\top/\sqrt{10}$ and $v_2 = (-1,1)^\top/\sqrt2$:

$$\begin{aligned} \sigma_2 u_2 v_2^\top &= \frac{\sqrt5}{\sqrt{20}} \begin{bmatrix} 3 & -3 \\ -1 & 1 \end{bmatrix} \\ &= \begin{bmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{bmatrix} = A - A_1 .\end{aligned}$$

Direct check: $A - A_1 = \begin{bmatrix} 3 - 1.5 & 0 - 1.5 \\ 4 - 4.5 & 5 - 4.5 \end{bmatrix}$, the same matrix. Frobenius: $2.25 + 2.25 + 0.25 + 0.25 = 5$. Spectral: the spectral-norm identity $\|M\|_2 = \sigma_1(M)$ applied to $M = A - A_1$, whose SVD is the single layer above.

**Sources.**

Spectral and Frobenius norms via singular values: Wilkinson [16], Section 3.5.1, Propositions 3.10 and 3.11; arithmetic checked above.
<!-- END S83 -->

<!-- BEGIN S90 -->
### 45. Eckart--Young--Mirsky: Spectral Error [S90]

**Message.** In the spectral norm, no matrix of rank at most $k$ gets closer to $A$ than $\sigma_{k+1}$, and $A_k$ achieves exactly $\sigma_{k+1}$.

Eckart-Young-Mirsky theorem, spectral norm. Setting: a real $m \times n$ matrix of rank $r$, sorted positive singular values, and a budget $0 \leq k \lt r$. The minimum of $\|A - B\|_2$ over every $m \times n$ matrix $B$ of rank at most $k$ equals $\sigma_{k+1}$, and $B = A_k$ attains it.

The quantifier is the point. The minimum runs over all rank-$\leq k$ matrices, not only over truncations of the SVD. The Frobenius version is a separate theorem with a separate proof, stated later.

**Details.**

Scope. The theorem concerns a fully observed matrix and the unweighted spectral error. It says nothing about uniqueness; in the spectral norm the minimizer is in general not unique (see section 46, Optimal: a Floor for All, Met by One).

*7.3 The spectral-norm case, proved (compact form).*

**Theorem (Eckart--Young--Mirsky, spectral norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$.

*Proof.* By rank--nullity, $\dim\operatorname{null}(B) \geq n - k$. Let $W = \operatorname{span}\{v_1,\dots,v_{k+1}\}$, of dimension $k+1$. Then $\dim(\operatorname{null}(B) \cap W) \geq (n-k) + (k+1) - n = 1$, so choose a unit vector $x \in \operatorname{null}(B) \cap W$. Since $Bx = 0$,

$$\begin{aligned} \|A - B\|_2^2 &\geq \|(A-B)x\|_2^2 = \|Ax\|_2^2 \\ &= \Big\|\sum_{i \leq k+1} \sigma_i (v_i^\top x)\, u_i\Big\|_2^2 \\ &= \sum_{i \leq k+1} \sigma_i^2 (v_i^\top x)^2 \geq \sigma_{k+1}^2,\end{aligned}$$

using $x \in W$ (so $v_i^\top x = 0$ for $i \gt k+1$), orthonormality of the $u_i$, and $\sum_{i \leq k+1} (v_i^\top x)^2 = \|x\|_2^2 = 1$ with $\sigma_i \geq \sigma_{k+1}$ throughout. Since $A_k$ attains $\sigma_{k+1}$, it is optimal. $\blacksquare$

Sections 47 to 59 unpack this proof step by step.

History. The result is usually attributed to Eckart and Young [1], who proved the Frobenius case in 1936; Mirsky [2] gave the general unitarily invariant statement in 1960, and Erhard Schmidt [3] had proved the analogous theorem for integral operators already in 1907. See [9] for the history of who proved what.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

M. P. Deisenroth, A. A. Faisal and C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020, Section 4.6, Theorem 4.25 (Eckart--Young).

Historical attributions: [1], [2], [3], [9].
<!-- END S90 -->

<!-- BEGIN S91 -->
### 46. Optimal: a Floor for All, Met by One [S91]

**Message.** Optimality has two halves: a lower bound that holds for every competitor, and one competitor that meets it.

Picture the spectral errors $\|A - B\|_2$ on a number line starting at $0$. The floor $\sigma_{k+1}$ splits it. Below the floor, between $0$ and $\sigma_{k+1}$, there is no rank-$\leq k$ matrix at all. The truncation $A_k$ sits exactly on the floor. Every other rank-$\leq k$ matrix sits on the floor or above it; this is a schematic, and no positions of other matrices are computed.

Computing one candidate's error, as the worked example did, only locates $A_k$ on the floor. The proof has to establish the empty region below the floor: no competitor whatsoever lands there.

**Details.**

What the statement does not claim. It does not say $A_k$ is the only minimizer, and it does not address missing entries, prediction, or noise.

*7.6 Uniqueness.*

A common phrasing calls $A_k$ *the* minimizer. For the spectral norm that is false. Counterexample: $A = \operatorname{diag}(2,1)$, $k = 1$, so $\sigma_2 = 1$ and the optimal value is $1$. Take $B_a = \operatorname{diag}(a, 0)$ for any $a \in [1,3]$; then $A - B_a = \operatorname{diag}(2-a, 1)$, whose singular values are $|2-a| \leq 1$ and $1$, so $\|A - B_a\|_2 = 1$, which is optimal, while $A_1 = \operatorname{diag}(2,0)$ is only the case $a = 2$. A whole interval of minimizers.

**Sources.**

Schematic drawn for this deck; no data. Counterexample checked above.
<!-- END S91 -->

<!-- BEGIN S85 -->
### 47. Recall: Low Rank Forces a Big Null Space [S85]

**Message.** Rank--nullity turns a rank budget into a large null space: if $\operatorname{rank}(B) \leq k$ then $B$ sends at least an $(n-k)$-dimensional subspace of inputs to zero.

Recall rank--nullity for $B \in \mathbb{R}^{m \times n}$: $\dim\operatorname{null}(B) = n - \operatorname{rank}(B)$. With the budget $\operatorname{rank}(B) \leq k$ this gives $\dim\operatorname{null}(B) \geq n - k$.

Here $n$ is the number of columns, the input dimension, and the null space lives in $\mathbb{R}^n$. Every low-rank competitor is blind on a large set of inputs. That blind spot is where the proof will catch it.

**Details.**

Rank--nullity is the statement $\dim\operatorname{null}(B) + \dim\operatorname{range}(B) = n$ for a linear map $\mathbb{R}^n \to \mathbb{R}^m$, with $\dim\operatorname{range}(B) = \operatorname{rank}(B)$. It was established in Part 1 of this lecture.

**Sources.**

Rank--nullity as established in Part 1 of this lecture.
<!-- END S85 -->

<!-- BEGIN S86 -->
### 48. Large Subspaces Must Intersect [S86]

**Message.** Two subspaces of $\mathbb{R}^n$ whose dimensions add up to more than $n$ must share a nonzero vector.

Intersection bound: $\dim(S_1 \cap S_2) \geq \dim S_1 + \dim S_2 - n$ for subspaces of $\mathbb{R}^n$. The reason in one line: the sum $S_1 + S_2$ sits inside $\mathbb{R}^n$, so its dimension is at most $n$, and the dimension formula below converts that into the bound.

Apply it with the two dimensions the proof will need, $n - k$ and $k + 1$. They add to $n + 1$, so the intersection has dimension at least one and contains a nonzero vector.

**Details.**

*2.3 The dimension formula, proved.*

**Theorem 2.3.** For subspaces $W_1, W_2 \subseteq \mathbb{R}^n$, $\dim(W_1 + W_2) + \dim(W_1 \cap W_2) = \dim W_1 + \dim W_2$, where $W_1 + W_2 = \{w_1 + w_2 : w_i \in W_i\}$.

*Proof.* Let $z_1, \dots, z_t$ be a basis of $W_1 \cap W_2$. Extend it to a basis $z_1, \dots, z_t, x_1, \dots, x_p$ of $W_1$ and to a basis $z_1, \dots, z_t, y_1, \dots, y_q$ of $W_2$, so $\dim W_1 = t + p$, $\dim W_2 = t + q$. The combined list spans $W_1 + W_2$; we claim it is independent. Suppose $\sum \gamma_i z_i + \sum \alpha_j x_j + \sum \beta_\ell y_\ell = 0$. Then $v := \sum_\ell \beta_\ell y_\ell = -\sum \gamma_i z_i - \sum \alpha_j x_j$ lies in $W_1$ and in $W_2$, hence in $W_1 \cap W_2$, so $v = \sum_i \delta_i z_i$ for some $\delta$. But $\sum_\ell \beta_\ell y_\ell - \sum_i \delta_i z_i = 0$ with the $z$'s and $y$'s independent forces all $\beta_\ell = 0$ (and all $\delta_i = 0$). The relation collapses to $\sum \gamma_i z_i + \sum \alpha_j x_j = 0$, and independence in $W_1$ kills the rest. Hence $\dim(W_1 + W_2) = t + p + q$, and $(t+p+q) + t = (t+p) + (t+q)$. $\blacksquare$

**Corollary 2.4.** $\dim(W_1 \cap W_2) \geq \dim W_1 + \dim W_2 - n$. In particular, if $\dim W_1 + \dim W_2 \gt n$ then $W_1 \cap W_2$ contains a nonzero vector. *Proof.* $W_1 + W_2 \subseteq \mathbb{R}^n$ gives $\dim(W_1 + W_2) \leq n$; substitute into Theorem 2.3. $\blacksquare$

This count is the engine of the spectral proof: it converts "$B$ has low rank" into "$B$ is blind at a specific place where $A$ is strong".

**Sources.**

Standard linear algebra; proof given in full above. See also Horn and Johnson [6].
<!-- END S86 -->

<!-- BEGIN S87 -->
### 49. Two Planes in $\mathbb{R}^3$ Share a Line [S87]

**Message.** Two planes through the origin in $\mathbb{R}^3$ always share at least a line, because $2 + 2 - 3 = 1$.

Picture two planes through the origin in three dimensions. One, $S_1$, is horizontal. The other, $S_2$, is tilted steeply and cuts through it. Their intersection is a line through the origin, and a vector $w$ pointing along that line from the origin lies in both planes.

The count is $\dim(S_1 \cap S_2) \geq 2 + 2 - 3 = 1$. The example is in $\mathbb{R}^3$ only because that can be pictured; the same count works in any dimension, which is how the proof uses it.

**Details.**

The geometry is exact, not sketched. $S_1 = \{z = 0\}$, and $S_2 = \operatorname{span}\{d, e\}$ with $d = (1, 0.3, 0)$ and $e = (0, -0.6, 1)$. Then $S_1 \cap S_2 = \operatorname{span}\{d\}$, since a point $t d + s e$ has $z$-coordinate $s$, which vanishes only for $s = 0$. In the drawing, $w = 0.8\, d / \|d\|$. The lecture's drawing uses a fixed oblique projection; its generator script asserts that the intersection line and $w$ lie in both planes.

**Sources.**

Figure computed for this deck (generator script `figs/o1c_planes.py`).
<!-- END S87 -->

<!-- BEGIN S88 -->
### 50. One Unit Witness Bounds the Maximum [S88]

**Message.** To show a maximum is at least some value, it is enough to exhibit one admissible input that reaches it; for the spectral norm the input must be a unit vector.

Recall $\|M\|_2 = \max_{\|x\|_2 = 1} \|Mx\|_2$. Any particular unit vector $w$ is one of the candidates in that maximum, so $\|M\|_2 \geq \|Mw\|_2$.

The unit-length condition is not decoration. Doubling $w$ doubles $\|Mw\|_2$, so without normalisation the bound would be meaningless. The plan for the proof is to find one unit vector where $\|(A - B)w\|_2$ is forced to be large.

**Details.**

For a nonzero $z$ the same idea reads $\|M\|_2 \geq \|Mz\|_2 / \|z\|_2$, which is the normalised version used when $z$ comes out of an intersection argument with arbitrary length.

**Sources.**

Definition of the spectral norm as the operator 2-norm; Wilkinson [16], Section 3.5.1.
<!-- END S88 -->

<!-- BEGIN S89 -->
### 51. Top $k{+}1$ Directions Stretch by $\geq \sigma_{k+1}$ [S89]

**Message.** Every unit vector in the span of the top $k+1$ right singular vectors is stretched by $A$ by at least $\sigma_{k+1}$.

Write a unit $w$ in that span as $w = \sum_{i \leq k+1} c_i v_i$. Because the $v_i$ are orthonormal, $\sum c_i^2 = \|w\|_2^2 = 1$. Applying $A$ sends each $v_i$ to $\sigma_i u_i$, and because the $u_i$ are orthonormal the squared length is $\sum \sigma_i^2 c_i^2$.

Each $\sigma_i$ with $i \leq k+1$ is at least $\sigma_{k+1}$ because the values are sorted, so the sum is at least $\sigma_{k+1}^2 \sum c_i^2 = \sigma_{k+1}^2$. As one chain, with the fact used at each step:

$$\begin{aligned} \|Aw\|_2^2 &= \sum_{i \leq k+1} \sigma_i^2 c_i^2 && \text{(orthonormal } u_i\text{)} \\ &\geq \sigma_{k+1}^2 \sum_{i \leq k+1} c_i^2 && \text{(sorted } \sigma_i\text{)} \\ &= \sigma_{k+1}^2 && \text{(orthonormal } v_i\text{)}. \end{aligned}$$

**Details.**

The two orthonormality facts play different roles: orthonormal $v_i$ give the coefficient identity $\sum c_i^2 = 1$; orthonormal $u_i$ give the Pythagorean identity for $\|Aw\|_2^2$. Sortedness gives the final inequality. The bound is tight at $w = v_{k+1}$.

This is one half of the min--max characterization of singular values (Courant--Fischer), which the Frobenius proof uses in full; it is stated and proved in section 60, Eckart-Young-Mirsky: Frobenius Error.

**Sources.**

Standard; Horn and Johnson [6], ch. 3 (variational characterization of singular values).
<!-- END S89 -->

<!-- BEGIN S92 -->
### 52. Proof Plan: Find One Witness [S92]

**Message.** The spectral proof fixes any competitor $B$, finds one unit vector where $B$ is blind and $A$ is strong, and then checks that $A_k$ meets the resulting bound.

The target is that every $B$ with $\operatorname{rank}(B) \leq k$ satisfies $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$. The proof has five steps:

1. The blind spot $\operatorname{null}(B)$ is large.
2. The subspace $W$ spanned by the top $k+1$ right singular vectors is where $A$ is strong.
3. The two must intersect in a unit vector $w$.
4. That witness bounds $\|A - B\|_2$ below by $\sigma_{k+1}$.
5. $A_k$ attains $\sigma_{k+1}$.

Steps 1 to 4 give the lower bound for every competitor. Step 5 gives the matching competitor.

**Details.**

Each step uses one fact recalled in sections 47 to 51: rank--nullity (Step 1), orthonormality and sorting (Steps 2 and 4), the intersection count (Step 3), the witness bound for a maximum (Step 4), and the spectral-norm identity $\|M\|_2 = \sigma_1(M)$ (Step 5).

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S92 -->

<!-- BEGIN S93 -->
### 53. Step 1: Every Competitor Has a Blind Spot [S93]

**Message.** Any rank-$\leq k$ competitor $B$ has a null space of dimension at least $n - k$, and on that null space the residual $A - B$ acts exactly like $A$.

Fix $B$ arbitrary, subject only to the rank budget. Rank--nullity gives $\dim\operatorname{null}(B) = n - \operatorname{rank}(B) \geq n - k$.

For any $x$ with $Bx = 0$, $(A - B)x = Ax$: the competitor contributes nothing there. Note that $B$ is arbitrary, not $A_k$, because the bound has to hold for all competitors at once.

**Details.**

Nothing about the structure of $B$ beyond its rank is used, so the argument covers every competitor, including ones unrelated to the SVD of $A$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S93 -->

<!-- BEGIN S94 -->
### 54. Step 2: $A$ Stays Strong on $W$ [S94]

**Message.** The span $W$ of the top $k+1$ right singular vectors is a $(k+1)$-dimensional subspace of inputs on which $A$ stretches every unit vector by at least $\sigma_{k+1}$.

$W = \operatorname{span}\{v_1, \dots, v_{k+1}\}$ lives in the input space $\mathbb{R}^n$, the same space as $\operatorname{null}(B)$. Its dimension is $k + 1$ because orthonormal vectors are linearly independent.

The assumption $k \lt r$ is used here: it guarantees that $v_{k+1}$ exists with $\sigma_{k+1} \gt 0$. Recall the top-directions bound (section 51): every unit $w \in W$ has $\|Aw\|_2 \geq \sigma_{k+1}$.

**Details.**

If $k \geq r$ the theorem is trivial, since $A_k = A$ has error zero, which is why the statement restricts to $0 \leq k \lt r$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S94 -->

<!-- BEGIN S95 -->
### 55. Step 3: The Two Subspaces Share a Unit $w$ [S95]

**Message.** The blind spot and the strong subspace have dimensions adding to more than $n$, so they share a nonzero vector, which can be scaled to a unit vector $w$.

Add the dimensions: $(n - k) + (k + 1) = n + 1 \gt n$. The intersection bound then gives $\dim(\operatorname{null}(B) \cap W) \geq 1$.

Take any nonzero $z$ in the intersection and set $w = z / \|z\|_2$. Scaling keeps $w$ in both subspaces, so $w$ is a unit vector that $B$ kills and that lies in $W$.

**Details.**

This is the example of two planes in $\mathbb{R}^3$ (section 49) again, with $\operatorname{null}(B)$ and $W$ in place of the planes.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S95 -->

<!-- BEGIN S96 -->
### 56. Step 4: Along $w$, the Residual Is $A$ [S96]

**Message.** Because $w$ is a unit vector killed by $B$, the residual's spectral norm is at least $\|Aw\|_2$.

The chain has two steps. The first uses that $w$ is a unit vector; it is the witness bound for a maximum: $\|A - B\|_2 \geq \|(A - B)w\|_2$. The second uses $Bw = 0$ and removes the competitor: $\|Aw - Bw\|_2 = \|Aw\|_2$.

No maximum is computed; one input is enough for a lower bound. What remains is to show $\|Aw\|_2$ cannot be small.

**Details.**

Both facts about $w$ come from Step 3: unit length from the normalisation, $Bw = 0$ from membership in the null space.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S96 -->

<!-- BEGIN S97 -->
### 57. Step 4 (continued): The Witness Is Not Small [S97]

**Message.** Since $w$ lies in $W$, $\|Aw\|_2 \geq \sigma_{k+1}$, and therefore $\|A - B\|_2 \geq \sigma_{k+1}$ for every competitor $B$.

Recall what is known about $w$: it lies in $W$ and has unit length, so $w = \sum_{i \leq k+1} c_i v_i$ with $\sum c_i^2 = 1$. The top-directions computation gives $\|Aw\|_2^2 = \sum \sigma_i^2 c_i^2 \geq \sigma_{k+1}^2$.

Both sides are nonnegative, so taking square roots preserves the inequality. Combined with Step 4 (section 56) this gives the lower bound $\|A - B\|_2 \geq \sigma_{k+1}$, valid for every $B$ with rank at most $k$, because $B$ was arbitrary.

**Details.**

This completes the lower-bound half of the theorem. Optimality also needs a competitor that achieves the bound.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S97 -->

<!-- BEGIN S98 -->
### 58. Step 5: Truncation Meets the Bound [S98]

**Message.** The residual $A - A_k$ is itself an SVD with largest singular value $\sigma_{k+1}$, so $A_k$ achieves the lower bound and the minimum is exactly $\sigma_{k+1}$.

Subtracting the first $k$ layers leaves $A - A_k = \sum_{i = k+1}^r \sigma_i u_i v_i^\top$. This sum is already a valid SVD: the $u_i$ are orthonormal, the $v_i$ are orthonormal, and the $\sigma_i$ are positive and sorted. Its largest singular value is $\sigma_{k+1}$.

The spectral-norm identity $\|M\|_2 = \sigma_1(M)$ then gives $\|A - A_k\|_2 = \sigma_{k+1}$. A lower bound for every competitor plus one competitor on the bound means the minimum equals $\sigma_{k+1}$, which completes the proof.

**Details.**

The step uses a subset of an orthonormal family, which is still orthonormal, so no new decomposition has to be computed.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S98 -->

<!-- BEGIN S99 -->
### 59. One Chain Proves the Spectral Theorem [S99]

**Message.** The whole spectral proof fits in one chain: its left end is an arbitrary competitor and its right end is the truncation $A_k$.

First the existence step: the dimensions of $\operatorname{null}(B)$ and $W$ add to more than $n$ (steps 1 and 2), so step 3 supplies a unit $w$ in both. Then the inequality chain from $\|A - B\|_2$ to $\|A - A_k\|_2$, with the step or fact that justifies each relation:

$$\begin{aligned} \|A - B\|_2 &\geq \|(A - B)w\|_2 && \text{(} w \text{ unit)} \\ &= \|Aw\|_2 && (Bw = 0) \\ &\geq \sigma_{k+1} && \text{(} w \in W \text{, step 4)} \\ &= \|A - A_k\|_2 && \text{(step 5)}. \end{aligned}$$

Reading the chain end to end: every rank-$\leq k$ matrix has spectral error at least $\sigma_{k+1}$, and $A_k$ has exactly that error, so $\min_{\operatorname{rank}(B) \leq k} \|A - B\|_2 = \sigma_{k+1}$.

**Details.**

The compact written proof is in section 45, Eckart-Young-Mirsky: Spectral Error.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S99 -->

<!-- BEGIN S101 -->
### 60. Eckart--Young--Mirsky: Frobenius Error [S101]

**Message.** In the Frobenius norm the best rank-$\leq k$ squared error is $\sum_{i > k} \sigma_i^2$, again attained by $A_k$; this is a separate theorem, stated here and proved only in this note.

Eckart-Young-Mirsky theorem, Frobenius norm. In the same setup, $\min_{\operatorname{rank}(B) \leq k} \|A - B\|_F^2 = \sum_{i = k+1}^r \sigma_i^2$, attained by $B = A_k$.

The spectral proof does not give this. It bounds only the largest singular value of $A - B$, whereas the Frobenius norm sums all of them. The proof below needs Weyl's inequality for singular values, which rests on the min--max characterization. The lecture uses the statement only.

**Details.**

*7.2 Courant--Fischer for singular values.*

**Lemma 7.1 (min--max / max--min).** For $1 \leq i \leq \min(m,n)$,

$$\begin{aligned} \sigma_i(A) &= \max_{\substack{S \subseteq \mathbb{R}^n \\ \dim S = i}} \ \min_{\substack{x \in S \\ \|x\|_2 = 1}} \|Ax\|_2 \\ &= \min_{\substack{T \subseteq \mathbb{R}^n \\ \dim T = n-i+1}} \ \max_{\substack{x \in T \\ \|x\|_2 = 1}} \|Ax\|_2 .\end{aligned}$$

*Proof (first equality; the second is analogous).* (At least $\sigma_i$ for the max.) Take $S_0 = \operatorname{span}\{v_1, \dots, v_i\}$. For unit $x \in S_0$, $x = \sum_{j \leq i} c_j v_j$ with $\sum c_j^2 = 1$, and $\|Ax\|_2^2 = \sum_{j \leq i} \sigma_j^2 c_j^2 \geq \sigma_i^2$. So the inner min over $S_0$ is at least $\sigma_i$ (indeed equal, at $x = v_i$). (At most $\sigma_i$ for every $S$.) Let $\dim S = i$ and $W' = \operatorname{span}\{v_i, v_{i+1}, \dots, v_n\}$, completing the $v$'s to an orthonormal basis of $\mathbb{R}^n$ with $\sigma_j := 0$ beyond the rank; $\dim W' = n - i + 1$. By the intersection count, $\dim(S \cap W') \geq 1$, so there is a unit $x \in S \cap W'$. Writing $x = \sum_{j \geq i} c_j v_j$, $\|Ax\|_2^2 = \sum_{j \geq i} \sigma_j^2 c_j^2 \leq \sigma_i^2$. Hence the inner min over $S$ is at most $\sigma_i$. $\blacksquare$

*7.4 The Frobenius case, proved.*

**Lemma 7.2 (Weyl, additive).** For $X, Y \in \mathbb{R}^{m \times n}$ and $i, j \geq 1$ with $i + j - 1 \leq \min(m,n)$: $\sigma_{i+j-1}(X + Y) \leq \sigma_i(X) + \sigma_j(Y)$.

*Proof.* By the min--max form of Lemma 7.1 there are subspaces $T_X$ of dimension $n - i + 1$ and $T_Y$ of dimension $n - j + 1$ with $\max_{x \in T_X, \|x\| = 1} \|Xx\|_2 = \sigma_i(X)$ and likewise for $Y$. Put $T = T_X \cap T_Y$, so $\dim T \geq (n-i+1) + (n-j+1) - n = n - (i+j-1) + 1$. Applying the min--max characterization at index $i + j - 1$ (whose minimum runs over subspaces of exactly that dimension, and any larger subspace contains one) gives $\sigma_{i+j-1}(X+Y) \leq \max_{x \in T, \|x\| = 1} \|(X+Y)x\|_2 \leq \max_{x \in T, \|x\| = 1} (\|Xx\|_2 + \|Yx\|_2) \leq \sigma_i(X) + \sigma_j(Y)$. $\blacksquare$

**Lemma 7.3.** If $\operatorname{rank}(B) \leq k$ then $\sigma_{i+k}(A) \leq \sigma_i(A - B)$ for all $i \geq 1$ (with $\sigma_j := 0$ beyond $\min(m,n)$). *Proof.* Apply Lemma 7.2 with $X = A - B$, $Y = B$, indices $i$ and $k+1$: $\sigma_{i+k}(A) \leq \sigma_i(A - B) + \sigma_{k+1}(B)$, and $\operatorname{rank}(B) \leq k$ means $\sigma_{k+1}(B) = 0$. $\blacksquare$

**Theorem (Eckart--Young--Mirsky, Frobenius norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_F^2 \geq \sum_{i > k} \sigma_i(A)^2 = \|A - A_k\|_F^2$. *Proof.* By the Frobenius identity $\|M\|_F^2 = \sum_i \sigma_i(M)^2$ and Lemma 7.3, $\|A - B\|_F^2 = \sum_{i \geq 1} \sigma_i(A - B)^2 \geq \sum_{i \geq 1} \sigma_{i+k}(A)^2 = \sum_{j > k} \sigma_j(A)^2$, which is $\|A - A_k\|_F^2$ by section 61, $A_k$'s Error Is the Discarded Energy. $\blacksquare$

The same two lines prove the nuclear-norm case, $\|A - B\|_* = \sum_i \sigma_i(A - B) \geq \sum_{i > k} \sigma_i(A) = \|A - A_k\|_*$, and, since Lemma 7.3 controls the whole singular-value vector entrywise, Mirsky's general statement:

**Theorem 8M (Mirsky, 1960).** For every unitarily invariant norm, $A_k$ minimizes $\|A - B\|$ over $\operatorname{rank}(B) \leq k$. *Reason:* such a norm is a symmetric gauge function of the singular-value vector (von Neumann), hence monotone in it, and Lemma 7.3 gives $\sigma(A - B) \geq \sigma(A - A_k)$ entrywise after sorting.

So one matrix, $A_k$, is simultaneously optimal for the spectral, Frobenius and nuclear errors. That is unusual: the $\ell_1$ and $\ell_2$ minimizers of an ordinary regression problem do not coincide in general.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11). The Frobenius case is stated there but not proved on the page.

M. P. Deisenroth, A. A. Faisal and C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020, Section 4.6, Theorem 4.25 (Eckart--Young).

Weyl's inequality and the min--max characterization: Horn and Johnson [6], ch. 3. Mirsky's theorem: [2].
<!-- END S101 -->

<!-- BEGIN S121 -->
### 61. $A_k$'s Error Is the Discarded Energy [S121]

**Message.** The Frobenius error of the truncation is the energy in the discarded layers, $\|A - A_k\|_F^2 = \sum_{i > k} \sigma_i^2$; this is achievability for one candidate, not optimality.

Subtract the kept layers: $A - A_k = \sum_{i = k+1}^r \sigma_i u_i v_i^\top$, which is an SVD with singular values $\sigma_{k+1}, \dots, \sigma_r$. The Frobenius identity $\|M\|_F^2 = \sum_i \sigma_i(M)^2$ then gives the squared error.

Keep the two claims apart. This calculation computes the error of one candidate. The statement that no other rank-$\leq k$ matrix does better is the Frobenius theorem, which this calculation does not prove.

**Details.**

The same structure appeared in the spectral case: Step 5 computed $\|A - A_k\|_2 = \sigma_{k+1}$, and Steps 1 to 4 supplied the bound for every competitor. In the Frobenius case the bound for every competitor is Lemma 7.3 in section 60.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S121 -->

<!-- REGION P3a END -->

<!-- REGION P3b BEGIN -->

<!-- BEGIN S116 -->
### 62. Part 5: Read the Answer [S116]

**Message.** Part 5 reads the theorem's answer on concrete matrices and states what it does and does not cover.
<!-- END S116 -->

<!-- BEGIN S102 -->
### 63. The Best Rank-One Error Is $\sqrt5$ [S102]

**Message.** For the worked matrix with $k = 1$, the theorems certify that no matrix of rank at most one is closer than $\sqrt5$, in either norm, and $A_1$ attains it.

Applying both theorems with $k = 1$ and $\sigma_2 = \sqrt5$: the minimum spectral error is $\sqrt5$ and the minimum squared Frobenius error is $5$. Recall $A_1$ and its errors, both $\sqrt5$, matching the floors.

The two errors coincide because the residual has rank one. The earlier calculation showed only that $A_1$ achieves $\sqrt5$; the theorems add that nothing does better. Both theorems are proved independently of this example, so the argument is not circular.

**Details.**

*7.5 Energy accounting and the worked example.*

$$\begin{gathered} A_1 = \begin{bmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{bmatrix}, \\ A - A_1 = \begin{bmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{bmatrix}, \\ \|A - A_1\|_2 = \|A - A_1\|_F = \sigma_2 = \sqrt5 .\end{gathered}$$

The equality of the two norms is not general. It holds because $A - A_1$ has rank one, so its singular-value vector has a single nonzero entry and all $\ell_p$ norms of it agree. Independent check: $\|A - A_1\|_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

Worked example: arithmetic checked above.
<!-- END S102 -->

<!-- BEGIN S103 -->
### 64. One Layer Keeps 90% of the Energy [S103]

**Message.** The rank-one truncation keeps $45$ of the $50$ units of squared Frobenius norm, $90\%$ of the energy.

Define the energy kept by $A_k$ as $\|A_k\|_F^2 / \|A\|_F^2 = \sum_{i \leq k} \sigma_i^2 / \sum_{i \leq r} \sigma_i^2$. For the worked matrix with $k = 1$ this is $45 / (45 + 5) = 90\%$.

Picture the total energy $\|A\|_F^2 = 9 + 16 + 25 = 50$ as a bar of 50 units, split into two pieces: $45$ units for $\sigma_1^2$, the part kept by $A_1$, and $5$ units for $\sigma_2^2$, the part discarded.

Energy share is not prediction accuracy. It is called explained variance only when the rows or columns of the data matrix have been centered.

**Details.**

In the lecture's figure the bar is drawn to scale: $18$ pixels per unit, so $810$ pixels for $45$ and $90$ for $5$.

Squared Frobenius norm from the entries: $3^2 + 0^2 + 4^2 + 5^2 = 50$; from the singular values: $45 + 5 = 50$. The kept energy $\|A_1\|_F^2 = 45$ was checked in section 43, Worked: $A_1$ Is the Top Layer of $A$.

The ratio is a property of this matrix. How fast singular values decay in real data depends on the data and is not claimed here.

**Sources.**

Frobenius identity: Wilkinson [16], Section 3.5.1, Proposition 3.10. Arithmetic checked above.
<!-- END S103 -->

<!-- BEGIN S122 -->
### 65. Worst Error and Total Error Can Differ [S122]

**Message.** With a residual of rank two, the spectral and Frobenius errors separate: for $\operatorname{diag}(5,3,1)$ truncated to rank one they are $3$ and $\sqrt{10}$.

Take the diagonal matrix $D = \operatorname{diag}(5, 3, 1)$, whose singular values are $5, 3, 1$ with standard basis vectors as singular vectors. Keeping the top layer gives $D_1 = \operatorname{diag}(5, 0, 0)$, and the residual is $\operatorname{diag}(0, 3, 1)$.

The spectral error is the largest dropped singular value, $3$, the worst-case stretch. The Frobenius error counts all dropped values, $\sqrt{3^2 + 1^2} = \sqrt{10} \approx 3.16$. A rank-two residual has two nonzero singular values, so the two norms measure different things.

**Details.**

In the $2 \times 2$ worked example the residual had one nonzero singular value, so the two errors matched. In general $\|M\|_2 \leq \|M\|_F \leq \sqrt{\operatorname{rank}(M)}\, \|M\|_2$, with equality on the left exactly when $M$ has rank at most one.

Both numbers are optimal for their own norm by the two theorems with $k = 1$.

**Sources.**

Arithmetic checked above; norm identities as in Wilkinson [16], Section 3.5.1.
<!-- END S122 -->

<!-- BEGIN S123 -->
### 66. What the Guarantee Covers [S123]

**Message.** The theorems answer one precise question: given every entry of $A$ and a rank budget $k$, which rank-$\leq k$ matrix is closest in unweighted spectral or Frobenius error.

The setting has three steps: given every entry of $A$, choose a rank budget $k$, and get $A_k$ with optimal error. The optimal error is $\sigma_{k+1}$ in the spectral norm and $\sum_{i > k} \sigma_i^2$ in squared Frobenius norm, and every entry counts equally.

The theorem does not cover:

- matrices with missing entries;
- the downstream accuracy of a model built on $A_k$;
- statistically optimal denoising of a noisy matrix.

Each of these changes the problem, so the closed-form answer no longer applies as stated.

**Details.**

Other limits of this lecture, for the record: the existence of the SVD rests on the spectral theorem, which was not proved here; everything was over the real numbers (the complex case is parallel, with conjugate transposes); and how the SVD is computed numerically is a separate subject (Golub and Van Loan [8], ch. 8).

Weighted errors, where some entries count more than others, and observing only some entries, are not covered: the unweighted Eckart-Young-Mirsky guarantee does not apply to general weighted or missing-entry objectives, and truncating the given matrix's SVD is not generally guaranteed to solve them.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

Numerical computation: Golub and Van Loan [8].
<!-- END S123 -->

<!-- BEGIN S117 -->
### 67. From Directions to the Optimal Error [S117]

**Message.** The lecture's chain: measure error through singular values, decompose $A$ into layers, truncate, and read the optimal error off the discarded singular values.

The chain has four links:

1. Measure: $\|A\|_2 = \sigma_1$ and $\|A\|_F^2 = \sum \sigma_i^2$.
2. Decompose: $A = \sum \sigma_i u_i v_i^\top$.
3. Truncate: keep $k$ layers to get $A_k$.
4. Read off: the optimal errors $\sigma_{k+1}$ and $\sum_{i > k} \sigma_i^2$.

The payoff: the SVD gives the best rank-$k$ approximation in closed form, for both error measures.

**Details.**

The chain uses each part of the lecture once: the two norms from Part 2, the decomposition from Part 3, the truncation and the optimality theorems from Part 4, and the worked answers from Part 5.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

M. P. Deisenroth, A. A. Faisal and C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020, Section 4.6, Theorem 4.25 (Eckart--Young).
<!-- END S117 -->

<!-- REGION P3b END -->

<!-- REGION Closing BEGIN -->

<!-- BEGIN S119 -->
### 68. Closing: $A = \sum_i \sigma_i u_i v_i^{\top}$ [S119]

**Message.** Every matrix is a sum of rank-one layers $\sigma_i u_i v_i^{\top}$; keeping the largest $k$ is the best rank-$k$ approximation.

The lecture closes on the SVD written as a sum of rank-one layers, $A = \sum_i \sigma_i u_i v_i^{\top}$, and opens the floor to questions.
<!-- END S119 -->

<!-- REGION Closing END -->

## 10 References

Theorem and section numbers in the annotations below (Theorem 5.1, Theorem 6.3) refer to the extended edition's note, `backup/opt01-svd-lowrank-full-note.md`.

1. C. Eckart and G. Young. "The approximation of one matrix by another of lower rank." *Psychometrika* 1(3):211-218, 1936. doi:10.1007/BF02288367 -- https://doi.org/10.1007/BF02288367
2. L. Mirsky. "Symmetric gauge functions and unitarily invariant norms." *Quarterly Journal of Mathematics* 11(1):50-59, 1960. doi:10.1093/qmath/11.1.50 -- https://doi.org/10.1093/qmath/11.1.50
3. E. Schmidt. "Zur Theorie der linearen und nichtlinearen Integralgleichungen." *Mathematische Annalen* 63:433-476, 1907. doi:10.1007/BF01449770 -- https://doi.org/10.1007/BF01449770. The rank-$k$ approximation result in its original, integral-operator form, three decades before Eckart-Young.
4. R. Penrose. "A generalized inverse for matrices." *Mathematical Proceedings of the Cambridge Philosophical Society* 51(3):406-413, 1955. doi:10.1017/S0305004100030401 -- https://doi.org/10.1017/S0305004100030401. The four equations of Theorem 5.1.
5. L. N. Trefethen and D. Bau III. *Numerical Linear Algebra.* SIAM, 1997. Lectures 4 and 5 for the SVD, lecture 11 for least squares; the cleanest short treatment.
6. R. A. Horn and C. R. Johnson. *Matrix Analysis*, 2nd edition. Cambridge University Press, 2013. Chapter 3 for singular values, Weyl-type inequalities, and unitarily invariant norms.
7. G. Strang. "The fundamental theorem of linear algebra." *American Mathematical Monthly* 100(9):848-855, 1993. doi:10.2307/2324660 -- https://doi.org/10.2307/2324660. The four-subspace picture of Theorem 3.
8. G. H. Golub and C. F. Van Loan. *Matrix Computations*, 4th edition. Johns Hopkins University Press, 2013. Chapter 8 for how the SVD is actually computed.
9. G. W. Stewart. "On the early history of the singular value decomposition." *SIAM Review* 35(4):551-566, 1993. doi:10.1137/1035134 -- https://doi.org/10.1137/1035134
10. E. J. Candes and B. Recht. "Exact matrix completion via convex optimization." *Foundations of Computational Mathematics* 9:717-772, 2009. arXiv:0805.4471 -- https://arxiv.org/abs/0805.4471
11. E. J. Candes and T. Tao. "The power of convex relaxation: near-optimal matrix completion." *IEEE Transactions on Information Theory* 56(5):2053-2080, 2010. arXiv:0903.1476 -- https://arxiv.org/abs/0903.1476
12. M. Fazel. *Matrix Rank Minimization with Applications.* PhD thesis, Stanford University, 2002. The convex-envelope result, Theorem 6.3.
13. B. Recht, M. Fazel, and P. A. Parrilo. "Guaranteed minimum-rank solutions of linear matrix equations via nuclear norm minimization." *SIAM Review* 52(3):471-501, 2010. arXiv:0706.4138 -- https://arxiv.org/abs/0706.4138. Includes the semidefinite-program formulation quoted in Section 8.3.
14. J.-F. Cai, E. J. Candes, and Z. Shen. "A singular value thresholding algorithm for matrix completion." *SIAM Journal on Optimization* 20(4):1956-1982, 2010. arXiv:0810.3286 -- https://arxiv.org/abs/0810.3286
15. M. Hardt, R. Meka, P. Raghavendra, and B. Weitz. "Computational limits for matrix completion." *COLT* 2014. arXiv:1402.2331 -- https://arxiv.org/abs/1402.2331. The hardness statement of Theorem 9.
16. R. D. Wilkinson. MATH3030 lecture notes, section 3.5, "Low-rank approximation." https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html. The proof reference cited in the source; the Frobenius case is proved independently in Section 7.4 above.
17. Y. Koren, R. Bell, and C. Volinsky. "Matrix factorization techniques for recommender systems." *IEEE Computer* 42(8):30-37, 2009. doi:10.1109/MC.2009.263 -- https://doi.org/10.1109/MC.2009.263. By the Netflix Prize winners; the practical counterpart to the matrix-completion slides of the extended edition (`backup/opt01-svd-lowrank-full.html`).
18. E. J. Hu et al. "LoRA: Low-Rank Adaptation of Large Language Models." *ICLR* 2022. arXiv:2106.09685 -- https://arxiv.org/abs/2106.09685
19. N. Halko, P. G. Martinsson, and J. A. Tropp. "Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions." *SIAM Review* 53(2):217-288, 2011. arXiv:0909.4061 -- https://arxiv.org/abs/0909.4061
20. Companion notes in this series: prob01 through prob09 cover the probability half (lectures 1 through 9); the covariance eigendecomposition, the symmetric positive-semidefinite special case of the SVD, is in prob08. The opt03 note covers gradient descent. The regression and SGD notes (opt02, opt04) are extended material, listed in `../backup/OUTLINE.md`. Each lives at `../<name>/<name>-note.md` in this accessible edition, or `-note.html` in the original.
