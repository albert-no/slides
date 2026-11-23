# Deep Learning Math 10: SVD and Low-Rank Approximation -- Notes

**About this file.** This is the linear-text edition of the companion note for lecture 10 of Deep Learning Math, covering the singular value decomposition and low-rank approximation. It carries the full mathematical content of that note: every definition, theorem, proof, worked number and reference. Figures and tables have been replaced by prose descriptions placed where they occurred, matrices are written out entry by entry in text, and cross-references to the accompanying presentation have been removed. Section numbering matches the original note, so a reference such as "Section 7.4" points to the same material here. Nothing else is needed to read it.

**How to use it.** There is one section per baseline slide, in slide order, each headed by the slide number and baseline title. The former section and subsection numbers are kept in the subsection headings (a subsection split across slides is marked "continued"), so a reference such as "Section 7.4" still finds its material; the References list follows the last slide section.

**Convention.** Throughout, $A \in \mathbb{R}^{m \times n}$ is a real matrix with $\operatorname{rank}(A) = r$. Its singular values are written $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(m,n)} \geq 0$, with $\sigma_i = 0$ for $i > r$. Everything is stated over the real numbers; the complex case requires only the replacements "orthogonal" to "unitary" and transpose ${}^\top$ to conjugate transpose ${}^*$. A norm bar with no subscript, $\|\cdot\|$, means the Euclidean norm $\|\cdot\|_2$.

**The running example.** One $2 \times 2$ matrix recurs from Section 4.6 onward. It is called $A$ and has first row $(3, 0)$ and second row $(4, 5)$. A second, singular, matrix called $C$ has first row $(1, 1)$ and second row $(2, 2)$.

**Notation.**

- $\operatorname{span}\{v_1, \dots, v_k\}$: the set of all linear combinations of $v_1, \dots, v_k$.
- $\operatorname{range}(A) = \{Ax : x \in \mathbb{R}^n\} \subseteq \mathbb{R}^m$, the column space.
- $\operatorname{null}(A) = \{x : Ax = 0\} \subseteq \mathbb{R}^n$, the null space or kernel.
- $\operatorname{row}(A) = \operatorname{range}(A^\top) \subseteq \mathbb{R}^n$, the row space.
- $\operatorname{rank}(A) = \dim \operatorname{range}(A)$.
- $W^\perp$: the orthogonal complement of a subspace $W$.
- $\langle x, y \rangle = x^\top y$; $\delta_{ij}$ is $1$ if $i = j$ and $0$ otherwise.
- $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$; $\|x\|_\infty = \max_i |x_i|$; $\|x\|_0 = \#\{i : x_i \neq 0\}$.
- $\|A\|_2 = \sigma_1$ (spectral norm), $\|A\|_F = (\sum_{i,j} a_{ij}^2)^{1/2}$ (Frobenius norm), $\|A\|_* = \sum_i \sigma_i$ (nuclear norm).
- $A^\dagger$: the Moore-Penrose pseudo-inverse.
- $A_k = \sum_{i \leq k} \sigma_i u_i v_i^\top$: the rank-$k$ truncated SVD.
- $U_c, \Sigma_c, V_c$: the thin (compact) SVD factors, of sizes $m \times r$, $r \times r$, $n \times r$.
- $\operatorname{tr}(X)$: the trace; $\operatorname{diag}(\dots)$: the diagonal matrix with the listed entries.
- $\succeq 0$ after a matrix: positive semidefinite.

**Background used.** This is Lecture 10 (opt01), the first of the four optimization lectures: opt01, opt02, opt03, opt04 are lectures 10 through 13. From the probability half of the course: Jensen's inequality (Lecture 1, prob01), used once in Lemma 3.1; the eigendecomposition of a covariance matrix (Lecture 8, prob08), which is the symmetric positive-semidefinite special case of Section 4.5. Maximum likelihood and the minimum-mean-squared-error estimator (Lecture 7, prob07) and empirical risk minimization (Lecture 6, prob06) are the problems this half of the course solves. The only mathematical result imported without proof is the **spectral theorem** for real symmetric matrices (Section 4.1); two further results are cited rather than proved because their proofs are outside the lecture's scope (the convex-envelope theorem of Fazel, Theorem 6.3, and the exact-recovery theorem for matrix completion, Theorem 10).

**What this edition adds.** Nothing mathematical: the content is that of the original companion note, which already proves everything the lecture states without proof. What is added is linearization. The two matrix displays that were laid out as grids, and the four-row table of fundamental subspaces in Section 4.4, are given as bullet lists. Small matrices that appeared inline as $2 \times 2$ arrays are written as "first row ..., second row ...". A tick mark used in the original to signal "this number was checked" is rendered as the word *checked* at the end of the sentence.

**Contents.**

1. Why the optimization half
2. Background: subspaces, dimension, rank
3. Norms and orthogonal matrices
4. The singular value decomposition
5. The Moore-Penrose pseudo-inverse
6. Matrix norms
7. Low-rank approximation: Eckart-Young-Mirsky
8. Matrix completion and the nuclear-norm relaxation
9. What the lecture leaves out
10. References

**Summary of what is proved here.** The linear-algebra background the lecture assumes -- that dimension is well defined, the dimension formula $\dim(W_1 + W_2) + \dim(W_1 \cap W_2) = \dim W_1 + \dim W_2$, and row rank $=$ column rank -- is proved from scratch in Section 2. Theorem 1 (rank-nullity), Theorem 2 (orthogonal decomposition, with uniqueness), Theorem 3 (the four fundamental subspaces) and Theorem 5 (existence of the SVD), all four of which the lecture states without proof, are proved in Sections 2 and 4. The $\ell_p$ norm axioms are verified through Young's, Holder's and Minkowski's inequalities in Section 3.2, with an explicit counterexample showing the triangle inequality fails for $p < 1$. The Moore-Penrose pseudo-inverse is shown well defined and characterized by Penrose's four equations in Section 5, together with the discontinuity of the map $A \mapsto A^\dagger$ that the clean $2 \times 2$ examples hide. The nuclear norm is *proved* to be a norm, via the variational identity $\|A\|_* = \max_{\|Z\|_2 \leq 1} \operatorname{tr}(Z^\top A)$, in Section 6.5. The Frobenius case of Eckart-Young-Mirsky -- the one real gap in the lecture, where the source gives only a sketch -- is proved in full in Section 7.4, via Courant-Fischer for singular values and Weyl's additive inequality, both proved first in Sections 7.2 and 7.4. Section 7.6 settles the uniqueness question: with $A = \operatorname{diag}(2,1)$ and $k = 1$, *every* $B = \operatorname{diag}(a, 0)$ with $a \in [1,3]$ is a spectral-norm minimizer, so the source's uniqueness claim is false as stated; in the Frobenius norm the minimizer is unique exactly when $\sigma_k > \sigma_{k+1}$. Every number in the lecture has been recomputed from scratch -- $A^\top A$ with rows $(25, 20)$ and $(20, 25)$, eigenvalues $45$ and $5$, singular values $3\sqrt5$ and $\sqrt5$, the pseudo-inverse $\tfrac{1}{15}$ times the matrix with rows $(5, 0)$ and $(-4, 3)$, $\|A\|_F = 5\sqrt2$, $\|A\|_* = 4\sqrt5$, the $90\%$ energy figure, the recommender toy example's count of $18$ against $20$ -- and all of them check out.

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

The setting: $A \in \mathbb{R}^{m\times n}$ is given and every entry is observed; we choose $B$ with $\operatorname{rank}(B) \le k$. The slide shows one equation drawn as three boxed matrices: the data $A = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right]$ (rank 2, grey box) equals a rank-1 candidate $B = \left[\begin{smallmatrix}1.5 & 1.5\\ 4.5 & 4.5\end{smallmatrix}\right]$ (blue box) plus the residual $A - B = \left[\begin{smallmatrix}1.5 & -1.5\\ -0.5 & 0.5\end{smallmatrix}\right]$ (red dashed box). The decomposition $A = B + (A - B)$ holds for any $B$; what changes from one candidate to another is how big the residual is, and that size will be measured by a matrix norm (Part 2). This sets up the two questions for the lecture: which rank-$k$ matrix is closest, and how small can the error be. At this point $B$ is just one candidate; nothing yet says it is the best one.

Storage is a reason to want low rank, but not automatically a saving: a rank-$k$ matrix can be stored as two factors with $k(m+n)$ numbers, which beats the $mn$ entries of $A$ only when $k(m+n) \lt mn$. For the $2\times 2$ example with $k = 1$ both counts are $4$, so there is no saving at all; the gain appears for large matrices and small $k$.

**Details.** **Full observation versus completion.** Here every entry of $A$ is known and the residual is computed over all entries. Matrix completion is a different problem: only some entries are observed, the fit is measured on those, and the low-rank assumption fills in the rest. The methods of this lecture do not directly solve completion.

**Why the problem is not convex.** The feasible set $\{B : \operatorname{rank}(B) \le k\}$ is not convex: $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$ both have rank 1, but their midpoint $\tfrac12 I_2$ has rank 2. So convex-optimization guarantees do not apply; the lecture still reaches an exact answer through the SVD.

**Check of the example.** $B + (A - B) = \left[\begin{smallmatrix}1.5+1.5 & 1.5-1.5\\ 4.5-0.5 & 4.5+0.5\end{smallmatrix}\right] = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right] = A$. Both columns of $B$ equal $(1.5, 4.5)$, so $\operatorname{rank}(B) = 1$.

**Sources.** Problem statement: Wilkinson, *Multivariate Statistics* (MATH3030 notes), Section 3.5 "Low-rank approximation". The matrices $A$, $B$ and $A - B$ are our illustration (evidence E08); the storage count $k(m+n)$ is our arithmetic.
<!-- END S80 -->

<!-- BEGIN S12 -->
### 5. Recall: Span and Range [S12]

**Message.** Every output $Ax$ is a linear combination of the columns of $A$, so the set of all outputs is the span of those columns.

Write $A = [\,a_1 \cdots a_n\,] \in \mathbb{R}^{m\times n}$ with columns $a_j \in \mathbb{R}^m$, and take an input $x \in \mathbb{R}^n$. Multiplying out gives $Ax = x_1a_1 + \cdots + x_na_n$, a vector in $\mathbb{R}^m$: the entries of $x$ are the weights on the columns. The range (column space) collects every possible output, $\operatorname{range}(A) = \{Ax : x \in \mathbb{R}^n\} = \operatorname{span}\{a_1, \dots, a_n\}$, a subspace of the output space $\mathbb{R}^m$. The figure shows the case $m = n = 2$ with $a_1 = (2,1)$ and $a_2 = (1,2)$ as two blue arrows from the origin; the amber arrow is $Ax$ for $x = (1,1)$, the diagonal of the dashed parallelogram spanned by $a_1$ and $a_2$, i.e. $a_1 + a_2 = (3,3)$.

**Details.** The span of $v_1, \dots, v_k$ is the set of all combinations $\sum_i \alpha_i v_i$. A subspace is a nonempty set closed under addition and scalar multiplication; $\operatorname{range}(A)$ is one because $Ax + Ay = A(x+y)$ and $\alpha Ax = A(\alpha x)$. A basis is a linearly independent spanning list, and the dimension is its length (well defined by the Steinitz exchange lemma, proved in the backup note).

**Sources.** Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* (CUP 2020), Section 2.7.3, Definition 2.23 and eq. (2.124): $\operatorname{Im}(A) = \{Ax\} = \operatorname{span}[a_1, \dots, a_n] \subseteq \mathbb{R}^m$. Figure: our illustration.
<!-- END S12 -->

<!-- BEGIN S14 -->
### 6. Rank Counts Independent Directions [S14]

**Message.** The rank of $A$ is the dimension of its range: the number of independent output directions.

Definition: $\operatorname{rank}(A) = \dim \operatorname{range}(A)$, the number of vectors in any basis of the range. The block diagram shows what this means for the shape of $A$: if $r = \operatorname{rank}(A)$ and $u_1, \dots, u_r$ is a basis of the range, then $A$ (a wide grey $m\times n$ block) factors as $U$ (a tall thin blue $m\times r$ block whose columns are the $u_i$) times $C$ (a short amber $r\times n$ block). Column $j$ of $C$ holds the coordinates of $a_j$ in that basis. The block sizes are schematic, not to scale. Rank is not the number of nonzero entries and not the number of columns: $\left[\begin{smallmatrix}1 & 1\\ 2 & 2\end{smallmatrix}\right]$ has four nonzero entries and two columns, yet both columns point along $(1,2)$, so its rank is 1.

**Details.** **The factorization.** Each column $a_j$ lies in $\operatorname{range}(A)$, so $a_j = Uc_j$ for a unique $c_j \in \mathbb{R}^r$. Stacking the columns gives $A = UC$ with $C = [c_1 \cdots c_n]$. Equivalently $A = \sum_{i=1}^r u_i \tilde c_i^\top$, a sum of $r$ rank-one matrices, where $\tilde c_i^\top$ is row $i$ of $C$.

Row rank equals column rank ($\operatorname{rank}(A^\top) = \operatorname{rank}(A)$) follows from the same factorization; the proof and the four-subspace picture are in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 2.6.2 (rank as the number of linearly independent columns) and Section 2.7.3, eq. (2.124) ($\operatorname{rk}(A) = \dim \operatorname{Im}(A)$). The factorization $A = UC$ is our derivation from the definition.
<!-- END S14 -->

<!-- BEGIN S13 -->
### 7. Two Inputs Collapse to One Direction [S13]

**Message.** The matrix $C = \left[\begin{smallmatrix}1 & 1\\ 2 & 2\end{smallmatrix}\right]$ sends every input onto the single line through $(1,2)$, so its rank is 1.

Both columns of $C$ equal $(1,2)$, so $Cx = x_1(1,2) + x_2(1,2) = (x_1 + x_2)(1,2)$: whatever the input, the output is a multiple of $(1,2)$. The figure has two coordinate panels joined by an arrow labelled $C$. The left (input) panel marks $e_1$ and $e_2$ as blue dots and $(1,1)$ as an amber square. The right (output) panel shows the range as a dashed light-blue line through the origin with slope 2; $e_1$ and $e_2$ both land on the same blue dot $(1,2)$, and $(1,1)$ lands on the amber square $(2,4)$, further out on the same line. All points are drawn at their exact coordinates. Two independent inputs produce only one output direction: $\operatorname{range}(C) = \operatorname{span}\{(1,2)\}$ and $\operatorname{rank}(C) = 1$.

**Details.** Image calculation: $Ce_1 = (1,2)$, $Ce_2 = (1,2)$, $C(1,1) = (2,4) = 2\cdot(1,2)$. Since every output is $(x_1 + x_2)(1,2)$ and $x_1 + x_2$ can be any real number, the range is the whole line $\operatorname{span}\{(1,2)\}$, not just a segment. A basis of the range is $\{(1,2)\}$, so the dimension is 1.

**Sources.** Our worked example (evidence E09).
<!-- END S13 -->

<!-- BEGIN S16 -->
### 8. Null Space Means Lost Directions [S16]

**Message.** The null space collects the input directions that $A$ sends to zero; for $C$ it is the line spanned by $(1,-1)$.

Definition: $\operatorname{null}(A) = \{x \in \mathbb{R}^n : Ax = 0\}$, a set of inputs. For $C$, $Cx = (x_1 + x_2)(1,2)$ vanishes exactly when $x_1 + x_2 = 0$, so $\operatorname{null}(C) = \operatorname{span}\{(1,-1)\}$. The figure repeats the two panels of the previous slide. In the input panel a solid red line of slope $-1$ through the origin is the null space; a dashed red arrow from $e_2$ to $e_1$ is the vector $e_1 - e_2 = (1,-1)$, which lies along that line. In the output panel the origin is a red dot labelled $C(1,-1) = 0$, and $Ce_1 = Ce_2$ is a single blue dot on the dashed range line. The point: $e_1$ and $e_2$ differ by a null vector, so $C$ cannot tell them apart. The null space lives in the input space $\mathbb{R}^n$; it is not a set of outputs and not part of the range.

**Details.** $\operatorname{null}(A)$ is a subspace: if $Ax = 0$ and $Ay = 0$ then $A(x + y) = 0$ and $A(\alpha x) = 0$. Inputs differing by a null vector give the same output: $A(x + z) = Ax$ when $z \in \operatorname{null}(A)$. For $C$, solving $x_1 + x_2 = 0$ gives $x = t(1,-1)$, $t \in \mathbb{R}$; one free parameter, so $\dim \operatorname{null}(C) = 1$.

**Sources.** Definition: Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 2.7.3, Definition 2.23 (kernel/null space). Example: our calculation (evidence E09).
<!-- END S16 -->

<!-- BEGIN S18 -->
### 9. Rank and Nullity Add Up [S18]

**Message.** For any $A \in \mathbb{R}^{m\times n}$ the kept directions and the lost directions add up to the number of columns $n$, so low rank forces a large null space.

Rank-nullity theorem: for every $A \in \mathbb{R}^{m\times n}$, square or rectangular, $\operatorname{rank}(A) + \dim \operatorname{null}(A) = n$. The count is over columns, i.e. input dimensions, not rows. The bar below the theorem splits all $n$ input dimensions into a solid blue part labelled "rank: kept" and a dashed red part labelled "nullity: lost"; the widths are schematic. Check on $C$: rank 1 plus nullity 1 equals 2 columns. For a wide matrix $A \in \mathbb{R}^{2\times 3}$ the rank is at most 2 (the range sits inside $\mathbb{R}^2$), so the nullity is at least 1: some nonzero input is always lost. This is the fact used later for an arbitrary competitor $B$: if $\operatorname{rank}(B) \le k$ then $\dim \operatorname{null}(B) \ge n - k$.

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

Definition: a norm on $\mathbb{R}^n$ is a function $\|\cdot\| : \mathbb{R}^n \to [0,\infty)$ such that for all $x, y \in \mathbb{R}^n$ and $\alpha \in \mathbb{R}$: $\|x\| = 0$ if and only if $x = 0$; $\|\alpha x\| = |\alpha|\,\|x\|$ (the absolute value means flipping the sign does not change the size); and $\|x + y\| \le \|x\| + \|y\|$. The sketch shows the triangle inequality: a solid blue arrow $x$ followed by a solid blue arrow $y$ (the detour), and a dashed amber arrow $x + y$ from the start of $x$ to the tip of $y$ (the direct route). The direct route is never longer than the detour. These three rules are all we need in this lecture; we use norms to measure residuals, not to study them for their own sake.

**Details.** **Norm versus squared norm.** The squared Euclidean norm $\|x\|_2^2$ is not a norm. It fails homogeneity, since $\|2x\|_2^2 = 4\|x\|_2^2$ rather than $2\|x\|_2^2$, and it fails the triangle inequality: for $x = y = e_1$, $\|x + y\|_2^2 = 4 \gt 2 = \|x\|_2^2 + \|y\|_2^2$. Squared norms are still useful as objectives (they are smooth and minimized by the same point), which is why the Frobenius "energy" is often written squared later.

**Nonnegativity follows from the other rules:** $0 = \|x + (-x)\| \le \|x\| + \|-x\| = 2\|x\|$. A consequence used for continuity arguments is the reverse triangle inequality $\big|\|x\| - \|y\|\big| \le \|x - y\|$.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.1, Definition 3.1 (absolutely homogeneous, triangle inequality, positive definite). Squared-norm counterexample: our calculation.
<!-- END S27 -->

<!-- BEGIN S28 -->
### 12. Three Familiar Vector Norms [S28]

**Message.** The $\ell_1$, $\ell_2$ and $\ell_\infty$ norms measure different aspects of the same coordinate vector.

For $x = (x_1, \dots, x_n) \in \mathbb{R}^n$ the slide shows three side-by-side cards. $\ell_1$, the absolute sum $\|x\|_1 = \sum_i |x_i|$: the distance walked along the coordinate axes. $\ell_2$, the Euclidean norm $\|x\|_2 = (\sum_i x_i^2)^{1/2}$: the straight-line length. $\ell_\infty$, the maximum $\|x\|_\infty = \max_i |x_i|$: the largest single coordinate. Only $\ell_2$ is geometric length. Do not confuse it with the sum of absolute coordinates: $x = (1,1)$ has $\|x\|_1 = 2$ but $\|x\|_2 = \sqrt{2}$.

**Details.** These are three members of the $\ell_p$ family $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$ for $p \ge 1$, with $\ell_\infty$ the limit as $p \to \infty$. For $p \lt 1$ the formula is not a norm: with $p = \tfrac12$, $x = (1,0)$, $y = (0,1)$ we get $\|x\|_{1/2} = \|y\|_{1/2} = 1$ but $\|x+y\|_{1/2} = (1+1)^2 = 4 \gt 2$. The proof that $\ell_p$ is a norm for $p \ge 1$ (Young, Holder, Minkowski) is in the backup note.

**Sources.** $\ell_1$ (Manhattan) and $\ell_2$ (Euclidean): Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.1, Examples 3.1 and 3.2. $\ell_p$: Wilkinson, MATH3030 notes, Section 2.3.1, Definition 2.9. $\ell_\infty = \max_i |x_i|$: standard definition, not found in either evidence source (flagged). The $(1,1)$ and $p = \tfrac12$ numbers: our calculation.
<!-- END S28 -->

<!-- BEGIN S29 -->
### 13. One Vector, Three Answers: 7, 5, 4 [S29]

**Message.** For $x = (3,4)$ the three norms report three different sizes, 7, 5 and 4, so the choice of norm is part of the question.

Arithmetic: $\|x\|_1 = |3| + |4| = 7$; $\|x\|_2 = \sqrt{9 + 16} = 5$; $\|x\|_\infty = \max(3, 4) = 4$. The figure is drawn to scale on a grid with the origin at bottom left and the point $x = (3,4)$ marked. The amber dashed path walks 3 to the right and then 4 up: its total length, $3 + 4 = 7$, is $\ell_1$. The solid blue diagonal from the origin straight to $x$ has length 5: that is $\ell_2$. A red bracket beside the vertical leg marks the longer coordinate, 4: that is $\ell_\infty$. For every vector, $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$, here $4 \le 5 \le 7$.

**Details.** **Why the ordering always holds.** $\|x\|_\infty^2 = \max_i x_i^2 \le \sum_i x_i^2 = \|x\|_2^2$. And $\|x\|_1^2 = \sum_i x_i^2 + \sum_{i \ne j} |x_i||x_j| \ge \|x\|_2^2$. Taking square roots of nonnegative quantities gives $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$.

Interpretation: $\ell_1$ adds up every coordinate, $\ell_\infty$ looks only at the worst one, and $\ell_2$ sits between them. The same contrast between "worst case" and "total" reappears for matrices as spectral norm versus Frobenius norm.

**Sources.** Our worked example (evidence E09: 7, 5, 4). Ordering proof: our derivation.
<!-- END S29 -->

<!-- BEGIN S30 -->
### 14. Unit Balls Reveal the Metric [S30]

**Message.** The unit ball $\{x : \|x\| \le 1\}$ is the set of vectors a norm calls at most 1, and its shape shows how the norm measures.

The figure has three panels in the plane, all at the same scale with axes crossing at the centre. Left: the $\ell_1$ ball is a diamond with corners on the axes at $(\pm1, 0)$ and $(0, \pm1)$. Middle: the $\ell_2$ ball is a round disc of radius 1. Right: the $\ell_\infty$ ball is a square with corners at $(\pm1, \pm1)$. Each panel marks one boundary point with an amber dot: $(1,0)$ on the diamond ($|1| + |0| = 1$), $(\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2})$ on the circle ($\tfrac12 + \tfrac12 = 1$ under the square root), and the corner $(1,1)$ on the square ($\max(1,1) = 1$). Each marked point has norm exactly 1 in its own panel's norm. The shapes are nested: diamond inside circle inside square. The panels are labelled by shape name as well as by norm, so the identification does not rely on colour.

**Details.** **Nesting.** From $\|x\|_\infty \le \|x\|_2 \le \|x\|_1$: if $\|x\|_1 \le 1$ then $\|x\|_2 \le 1$, and if $\|x\|_2 \le 1$ then $\|x\|_\infty \le 1$. So the $\ell_1$ ball lies inside the $\ell_2$ ball, which lies inside the $\ell_\infty$ ball. The point $(1,1)$ is in the square but not in the circle ($\|(1,1)\|_2 = \sqrt2 \gt 1$).

**Sources.** Our illustration, drawn to scale (evidence E09 for the norms used). The unit-ball shapes follow directly from the definitions on the previous slides.
<!-- END S30 -->

<!-- BEGIN S31 -->
### 15. Orthogonal Maps Preserve Geometry [S31]

**Message.** A square matrix $Q$ with $Q^\top Q = I$ turns vectors without changing their Euclidean length.

Definition: $Q \in \mathbb{R}^{n\times n}$ is orthogonal if $Q^\top Q = I = QQ^\top$; equivalently its columns are orthonormal, and $Q^{-1} = Q^\top$. The figure shows a dashed grey unit circle. A blue arrow is $e_1$; an amber arrow is $Qe_1$ for the $45^\circ$ rotation $Q = \tfrac{1}{\sqrt2}\left[\begin{smallmatrix}1 & -1\\ 1 & 1\end{smallmatrix}\right]$, so $Qe_1 = (\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2})$; a small arc marks the $45^\circ$ angle between them. Both tips sit on the unit circle: the direction changed, the Euclidean length stayed 1. Squareness matters. The tall matrix $W = [e_1\; e_2] \in \mathbb{R}^{3\times 2}$ has orthonormal columns, so $W^\top W = I_2$, but $WW^\top = \operatorname{diag}(1,1,0) \ne I_3$; it is not an orthogonal matrix. And the protection is for $\ell_2$ only, not every norm (next slide).

**Details.** For square $Q$, $Q^\top Q = I$ already implies $QQ^\top = I$ (a square matrix with a left inverse is invertible, and the inverse is that left inverse). Further equivalent characterizations, orthonormal rows, $\det Q = \pm1$, and Gram-Schmidt are in the backup note. Check of the example: the columns $\tfrac{1}{\sqrt2}(1,1)$ and $\tfrac{1}{\sqrt2}(-1,1)$ each have length 1 and dot product $\tfrac12(-1+1) = 0$.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.4, Definition 3.8 (orthogonal matrix: square, $AA^\top = I = A^\top A$). Rotation and $W$ examples: our illustration.
<!-- END S31 -->

<!-- BEGIN S33 -->
### 16. Why Length Is Preserved [S33]

**Message.** One line of algebra using $Q^\top Q = I$ shows that a square orthogonal $Q$ preserves the Euclidean norm of every vector.

Claim: for square $Q \in \mathbb{R}^{n\times n}$ with $Q^\top Q = I$ and every $x \in \mathbb{R}^n$, $\|Qx\|_2 = \|x\|_2$. Proof: $\|Qx\|_2^2 = (Qx)^\top(Qx) = x^\top Q^\top Q x = x^\top x = \|x\|_2^2$, where the middle step uses $Q^\top Q = I$; both norms are nonnegative, so taking square roots gives the claim. The same step with two vectors gives $(Qx)^\top(Qy) = x^\top y$, so inner products, and hence angles, are preserved too. The protection is specific to the Euclidean norm: for the $45^\circ$ rotation, $\|Qe_1\|_1 = \tfrac{1}{\sqrt2} + \tfrac{1}{\sqrt2} = \sqrt2$, while $\|e_1\|_1 = 1$.

**Details.** The proof uses only $Q^\top Q = I$, not squareness, so it also shows that a tall matrix with orthonormal columns (like $W$ on the previous slide) preserves Euclidean length. Squareness is needed for the converse direction and for $QQ^\top = I$. Conversely, a square $Q$ with $\|Qx\|_2 = \|x\|_2$ for all $x$ is orthogonal, by the polarization identity $x^\top y = \tfrac12(\|x+y\|_2^2 - \|x\|_2^2 - \|y\|_2^2)$; details in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 3.4, Definition 3.8 and eqs. (3.31) (length preserved) and (3.32) (angles preserved). $\ell_1$ counterexample: our calculation.
<!-- END S33 -->

<!-- BEGIN S66 -->
### 17. Spectral Norm: Worst Stretch [S66]

**Message.** The spectral norm of a matrix is the largest factor by which it stretches any unit-length input.

Definition: for $A \in \mathbb{R}^{m\times n}$, $\|A\|_2 = \max_{x \in \mathbb{R}^n,\ \|x\|_2 = 1} \|Ax\|_2$. It is one number for the whole matrix. The figure uses the running example $A = \left[\begin{smallmatrix}3 & 0\\ 4 & 5\end{smallmatrix}\right]$. On the left is the input unit circle (drawn three times larger than the output scale so it is visible), with one input $x^\star$ marked by a blue radius. An arrow labelled $A$ leads to the right panel, where the image of the circle under $A$ is a tall, tilted ellipse drawn to scale. The red radius from the centre to the ellipse's farthest point is $Ax^\star$, the longest image: its length is $\|A\|_2$. The picture is only intuition for "worst direction"; how to compute that length comes later in the lecture. Keep three things apart: $\|A\|_2$ is a matrix norm; $\|x\|_2$ is the length of a vector; and the $\ell_2$ norm of all entries of $A$ is a different matrix norm, the Frobenius norm (next slide).

**Details.** **Figure geometry.** The ellipse is the exact image $\{A(\cos t, \sin t)\} = \{(3\cos t,\ 4\cos t + 5\sin t)\}$. The marked input is $x^\star = (1,1)/\sqrt2$, and $Ax^\star = (3, 9)/\sqrt2$; a numerical scan of $t$ confirms this is where $\|A(\cos t, \sin t)\|_2$ is largest. The numerical value is deliberately not stated on the slide; it is derived with the singular values later.

The maximum is attained because $x \mapsto \|Ax\|_2$ is continuous and the unit sphere is compact. Equivalently $\|A\|_2 = \max_{x \ne 0} \|Ax\|_2 / \|x\|_2$, by homogeneity. Other induced norms ($p = 1, \infty$) and submultiplicativity $\|AB\|_2 \le \|A\|_2\|B\|_2$ are in the backup note.

**Sources.** Deisenroth, Faisal & Ong, *MML* (CUP 2020), Section 4.6, Definition 4.23 (spectral norm, eq. (4.93)); Wilkinson, MATH3030 notes, Section 3.5.1, Definition 3.2 (matrix $p$-norms, here $p = 2$). Figure: our running example (evidence E08), computed exactly.
<!-- END S66 -->

<!-- BEGIN S72 -->
### 18. Frobenius Norm: Total Energy [S72]

**Message.** The Frobenius norm adds up every squared entry, so $\|A - B\|_F^2$ is the total squared error over all entries.

Definition: $\|A\|_F = (\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2)^{1/2}$, and for a residual $\|A - B\|_F^2 = \sum_{i,j} (a_{ij} - b_{ij})^2$. The figure is a $2\times 2$ grid of tiles, one per entry of the residual $A - B$ from the opening example, each showing its square: the top row $1.5^2 = 2.25$ and $(-1.5)^2 = 2.25$ in dark red solid tiles, the bottom row $(-0.5)^2 = 0.25$ and $0.5^2 = 0.25$ in pale red dashed tiles; darker means a larger contribution. The sum is $5$, so $\|A - B\|_F = \sqrt5$. Qualifiers: every entry is observed and counts equally (no weights), and the Frobenius norm is not the spectral norm in general. For the identity $I_2$, $\|I_2\|_2 = 1$ (it stretches nothing) but $\|I_2\|_F = \sqrt2$.

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
### 20. Recall -- Eigendecomposition [S36]

#### 4.1 The one imported black box

**Spectral theorem (imported).** Every symmetric $S \in \mathbb{R}^{n \times n}$ can be written $S = Q \Lambda Q^\top$ with $Q$ orthogonal and $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real. If moreover $S$ is positive semidefinite, meaning $x^\top S x \geq 0$ for all $x$, then every $\lambda_i \geq 0$.

This is the single result these notes do not prove. It was used in the lecture-8 note for covariance matrices and is proved in any of [5, 6, 8]. A sketch, for orientation: the maximum of the continuous function $x \mapsto x^\top S x$ on the compact unit sphere is attained at some $q_1$, which is an eigenvector by a Lagrange-multiplier or first-order argument; $S$ maps the orthogonal complement of $q_1$ into itself by symmetry, so one inducts on dimension. The positive-semidefinite claim is one line: $\lambda_i = q_i^\top S q_i \geq 0$. Everything else below is proved.
<!-- END S36 -->

<!-- BEGIN S38 -->
### 21. Theorem 5 -- the SVD Exists [S38]

#### 4.2 Theorem 5: existence of the SVD, proved

**Theorem 5.** Every $A \in \mathbb{R}^{m \times n}$ with $\operatorname{rank}(A) = r$ admits a factorization $A = U \Sigma V^\top$ with $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ orthogonal, and $\Sigma \in \mathbb{R}^{m \times n}$ diagonal in the sense that $\Sigma_{ij} = 0$ for $i \neq j$, with diagonal entries $\sigma_1 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$.

*Proof.* The matrix $S = A^\top A \in \mathbb{R}^{n \times n}$ is symmetric, since $S^\top = A^\top A$, and positive semidefinite, since $x^\top S x = \|Ax\|_2^2 \geq 0$. By the spectral theorem write $S = V \Lambda V^\top$ with $V = [v_1 \cdots v_n]$ orthogonal and $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0$, reordering the columns of $V$ to sort $\Lambda$, which preserves orthogonality.

*Step 1: the number of positive eigenvalues is $r$.* We have $\|Av_i\|_2^2 = v_i^\top S v_i = \lambda_i$, so $Av_i = 0$ exactly when $\lambda_i = 0$. Hence $\operatorname{null}(A) \supseteq \operatorname{span}\{v_i : \lambda_i = 0\}$. Conversely $Ax = 0$ implies $Sx = 0$, and $Sx = 0$ with $x = \sum_i c_i v_i$ gives $\sum_i c_i \lambda_i v_i = 0$, so $c_i = 0$ whenever $\lambda_i \neq 0$. Thus $\operatorname{null}(A) = \operatorname{span}\{v_i : \lambda_i = 0\}$, and by Theorem 1 the count of positive $\lambda_i$ is $n - \dim\operatorname{null}(A) = r$. So $\lambda_1 \geq \cdots \geq \lambda_r > 0 = \lambda_{r+1} = \cdots = \lambda_n$.

*Step 2: define $\sigma_i$ and $u_i$.* For $i \leq r$ set $\sigma_i = \sqrt{\lambda_i} > 0$ and $u_i = Av_i / \sigma_i \in \mathbb{R}^m$. These are orthonormal:

$$ u_i^\top u_j = \frac{v_i^\top A^\top A v_j}{\sigma_i \sigma_j} = \frac{v_i^\top(\lambda_j v_j)}{\sigma_i \sigma_j} = \frac{\lambda_j \, \delta_{ij}}{\sigma_i \sigma_j} = \delta_{ij} . $$

Since $r \leq m$, extend $u_1, \dots, u_r$ to an orthonormal basis $u_1, \dots, u_m$ of $\mathbb{R}^m$, by Lemma 2.5 applied to a completion to a basis, and set $U = [u_1 \cdots u_m]$, which is orthogonal by Proposition 3.5.

*Step 3: verify $AV = U\Sigma$.* Let $\Sigma \in \mathbb{R}^{m \times n}$ have $\Sigma_{ii} = \sigma_i$ for $i \leq r$ and zeros elsewhere. Column $i$ of $AV$ is $Av_i$, which equals $\sigma_i u_i$ for $i \leq r$ by the definition of $u_i$, and $0$ for $i > r$ by Step 1. Column $i$ of $U\Sigma$ is $\sum_j u_j \Sigma_{ji} = \sigma_i u_i$ for $i \leq r$ and $0$ otherwise. The columns agree, so $AV = U\Sigma$, and right-multiplying by $V^\top$ gives $A = U\Sigma V^\top$. **End of proof.**

Two remarks on this "$A^\top A$ route." First, the proof is *constructive*, and is exactly the by-hand recipe of the lecture: form $A^\top A$, eigendecompose, take square roots, push through $A$. Second, it is a terrible *numerical* recipe: forming $A^\top A$ squares the condition number, so library implementations, which use Golub-Kahan bidiagonalization [8, ch. 8], never do this. The hand computation is for understanding, not for code -- in practice one calls the library routine `numpy.linalg.svd`.

#### 4.3 What is unique and what is not

**Proposition 4.1.** The singular values are unique: they are the square roots of the eigenvalues of $A^\top A$, sorted. The singular *vectors* are not unique.

*Proof of the first claim.* If $A = U\Sigma V^\top$ then $A^\top A = V \Sigma^\top \Sigma V^\top$, an eigendecomposition with eigenvalues $\sigma_i^2$; the eigenvalues of a fixed matrix are the roots of its characteristic polynomial, hence determined by $A$ alone. **End of proof.**

Non-uniqueness of the vectors has two sources. *Signs:* replacing the pair $(u_i, v_i)$ by $(-u_i, -v_i)$ changes nothing, since $\sigma_i(-u_i)(-v_i)^\top = \sigma_i u_i v_i^\top$. *Repeated singular values:* if $\sigma_i = \sigma_j$ for $i \neq j$, any rotation within the corresponding two-dimensional eigenspace of $A^\top A$ yields another valid SVD -- for $A = I_2$ every orthogonal $V$ works, with $U = V$. Additionally, the columns $u_{r+1}, \dots, u_m$ are constrained only to complete an orthonormal basis.

This is why the lecture drops the source's uniqueness claim for the *minimizer* in Theorem 8: non-uniqueness enters here, at the level of the decomposition itself, and Section 7.6 shows it survives into the approximation problem.
<!-- END S38 -->

<!-- BEGIN S39 -->
### 22. Reading the Shapes (Full SVD) [S39]
<!-- END S39 -->

<!-- BEGIN S40 -->
### 23. What Each Factor Does [S40]
<!-- END S40 -->

<!-- BEGIN S52 -->
### 24. Circle to Ellipse -- Rotate First [S52]

#### 4.8 The geometry: sphere to ellipsoid

**Proposition 4.3.** $A$ maps the unit sphere $\{x : \|x\|_2 = 1\}$ onto the ellipsoid $\{\sum_{i \leq r} c_i u_i : \sum_{i \leq r} c_i^2/\sigma_i^2 \leq 1\}$, degenerating to a filled ellipsoid inside $\operatorname{range}(A)$ when $r < n$, with semi-axes $\sigma_i u_i$.

*Proof.* With $y = V^\top x$, so that $\|y\| = 1$ by Theorem 4, we have $Ax = U\Sigma y = \sum_{i \leq r} \sigma_i y_i u_i$, that is, $c_i = \sigma_i y_i$ where $\sum_{i \leq n} y_i^2 = 1$. If $r = n$ this says exactly $\sum_i c_i^2/\sigma_i^2 = 1$. If $r < n$ the coordinates $y_{r+1}, \dots, y_n$ are free, so $\sum_{i \leq r} y_i^2$ takes every value in $[0,1]$ and the image is the solid ellipsoid. **End of proof.**

This is the standard four-stage rotate-stretch-rotate picture read algebraically: $V^\top$ rotates the sphere to itself, $\Sigma$ stretches axis $i$ by $\sigma_i$, and $U$ rotates the resulting ellipsoid into the output space. It also makes Theorem 6 geometrically obvious in advance -- the longest semi-axis has length $\sigma_1$.
<!-- END S52 -->

<!-- BEGIN S53 -->
### 25. Circle to Ellipse -- Stretch, Then Rotate Back [S53]
<!-- END S53 -->

<!-- BEGIN S41 -->
### 26. Technique Review -- the Outer-Product View [S41]

#### 4.4 Thin SVD, the rank-one expansion, and the four subspaces again

Discarding the columns of $U$ and $V$ that meet only zeros in $\Sigma$ gives the **thin (compact) SVD** $A = U_c \Sigma_c V_c^\top$, with $U_c \in \mathbb{R}^{m \times r}$, $\Sigma_c = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$ invertible, and $V_c \in \mathbb{R}^{n \times r}$. Equivalently,

$$ A \;=\; \sum_{i=1}^{r} \sigma_i \, u_i v_i^\top , $$

since the $(j,k)$ entry of both sides is $\sum_i \sigma_i u_{ji} v_{ki}$. Each $u_i v_i^\top$ has rank one and acts as $x \mapsto u_i (v_i^\top x)$: measure the component of $x$ along $v_i$, emit it along $u_i$.

The SVD also hands back the subspaces of Theorem 3 explicitly. For each of the four, its basis drawn from the SVD factors and its dimension:

- $\operatorname{range}(A)$: basis $u_1, \dots, u_r$; dimension $r$.
- $\operatorname{null}(A^\top) = \operatorname{range}(A)^\perp$: basis $u_{r+1}, \dots, u_m$; dimension $m - r$.
- $\operatorname{row}(A)$: basis $v_1, \dots, v_r$; dimension $r$.
- $\operatorname{null}(A) = \operatorname{row}(A)^\perp$: basis $v_{r+1}, \dots, v_n$; dimension $n - r$.

For the first of these: $Ax = \sum_{i \leq r} \sigma_i (v_i^\top x) u_i$ ranges over $\operatorname{span}\{u_1, \dots, u_r\}$ as $x$ varies. The fourth was Step 1 of the proof of Theorem 5, and the other two follow by Theorem 3.

Note also that $\operatorname{rank}(A) = r$ is *defined* by the SVD as the number of nonzero singular values, which in floating-point arithmetic becomes the useful notion of *numerical rank*: the number of $\sigma_i$ above a tolerance. Section 5.6 explains why that is the only workable definition in practice.
<!-- END S41 -->

<!-- BEGIN S42 -->
### 27. Thin (Compact) SVD [S42]
<!-- END S42 -->

<!-- BEGIN S44 -->
### 28. Worked -- SVD by Hand: the Plan [S44]

#### 4.6 The running example, recomputed

Every step of the hand computation for $A$, the matrix with first row $(3, 0)$ and second row $(4, 5)$, verified independently.
<!-- END S44 -->

<!-- BEGIN S45 -->
### 29. Worked -- Step 1: Form $A^{\top}A$ [S45]

#### 4.6 The running example, recomputed (continued)

*Step 1.* $A^\top$ has first row $(3, 4)$ and second row $(0, 5)$. The product $A^\top A$ has first row $(9 + 16, 20) = (25, 20)$ and second row $(20, 25)$. Checked.
<!-- END S45 -->

<!-- BEGIN S46 -->
### 30. Worked -- Step 2: Eigenvalues [S46]

#### 4.6 The running example, recomputed (continued)

*Step 2.* $\det(A^\top A - \lambda I) = (25 - \lambda)^2 - 400$, so $25 - \lambda = \pm 20$, giving $\lambda_1 = 45$ and $\lambda_2 = 5$. Checked. Two consistency tests: the trace, $45 + 5 = 50 = 25 + 25$; and the determinant, $45 \cdot 5 = 225 = 625 - 400$.

For eigenvectors: $A^\top A - 45I$ has first row $(-20, 20)$ and second row $(20, -20)$, and solving $(A^\top A - 45I)v = 0$ gives $v_1$ proportional to $(1,1)$. Likewise $A^\top A - 5I$ has both rows equal to $(20, 20)$, and solving gives $v_2$ proportional to $(-1, 1)$. Normalized and orthogonal. Checked.
<!-- END S46 -->

<!-- BEGIN S47 -->
### 31. Worked -- Step 2: Eigenvectors [S47]

#### 4.6 The running example, recomputed (continued)

The coincidence that $V$ is the same $45$-degree rotation met earlier in the lecture is not an accident of exposition but of the example: $A^\top A$ has equal diagonal entries, and any symmetric matrix with first row $(a, b)$ and second row $(b, a)$ has eigenvectors $(1,1)$ and $(-1,1)$ regardless of $a$ and $b$.
<!-- END S47 -->

<!-- BEGIN S48 -->
### 32. Worked -- Step 3: Sigmas and $u_i$ [S48]

#### 4.6 The running example, recomputed (continued)

*Step 3.* $\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.7082$ and $\sigma_2 = \sqrt5 \approx 2.2361$. Checked. Then $Av_1 = \tfrac{1}{\sqrt2}(3, 9)$ with $\|Av_1\| = \tfrac{1}{\sqrt2}\sqrt{90} = \sqrt{45} = \sigma_1$ (checked), so

$$ u_1 = \frac{Av_1}{\sigma_1} = \frac{(3,9)}{\sqrt2 \cdot 3\sqrt5} = \frac{(1,3)}{\sqrt{10}} . $$

Checked. Similarly $Av_2 = \tfrac{1}{\sqrt2}(-3, 1)$ with $\|Av_2\| = \tfrac{\sqrt{10}}{\sqrt2} = \sqrt5 = \sigma_2$ (checked), so $u_2 = (-3, 1)/\sqrt{10}$. Checked.
<!-- END S48 -->

<!-- BEGIN S49 -->
### 33. Worked -- Step 4: Assemble [S49]
<!-- END S49 -->

<!-- BEGIN S50 -->
### 34. Worked -- Verify via Rank-1 Layers [S50]

#### 4.6 The running example, recomputed (continued)

*Step 4: the two rank-one layers.* The first layer is

$$ \sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}} \cdot \frac{1}{\sqrt2} \, (1,3)^\top (1,1) = \frac{3\sqrt5}{\sqrt{20}} \cdot M_1 = \tfrac32 M_1 , $$

where $M_1$ is the matrix with first row $(1,1)$ and second row $(3,3)$, using $3\sqrt5/\sqrt{20} = 3\sqrt5/(2\sqrt5) = 3/2$. So the first layer has first row $(1.5, 1.5)$ and second row $(4.5, 4.5)$. Checked.

Similarly the second layer is $\sigma_2 u_2 v_2^\top = \sqrt5 \cdot \tfrac{1}{\sqrt{20}} \cdot M_2 = \tfrac12 M_2$, where $M_2$ is the matrix with first row $(3, -3)$ and second row $(-1, 1)$; so the second layer has first row $(1.5, -1.5)$ and second row $(-0.5, 0.5)$. Checked. The two layers sum entry by entry to $(1.5 + 1.5, 1.5 - 1.5) = (3, 0)$ and $(4.5 - 0.5, 4.5 + 0.5) = (4, 5)$, which is $A$. Checked.
<!-- END S50 -->

<!-- BEGIN S51 -->
### 35. Eigenvalues $\neq$ Singular Values [S51]

#### 4.7 Eigenvalues versus singular values

For the running matrix, which is lower triangular, the eigenvalues are the diagonal entries $3$ and $5$; the singular values are $6.708$ and $2.236$. Not equal, not even close. But the products agree: $3 \cdot 5 = 15 = |\det A| = \sigma_1 \sigma_2 = 3\sqrt5 \cdot \sqrt5$, and that is general.

**Proposition 4.2.** For square $A$: (a) $\prod_i \sigma_i = |\det A| = \prod_i |\lambda_i|$; (b) $\max_i |\lambda_i| \leq \sigma_1$, with equality for all $i$ simultaneously if and only if $A$ is normal, meaning $A^\top A = AA^\top$, which in the real case includes in particular every symmetric $A$.

*Proof of (a) and of the inequality in (b).* (a) $\det A = \det U \det \Sigma \det V^\top = \pm \prod_i \sigma_i$. (b) If $Ax = \lambda x$ with $\|x\| = 1$ then $|\lambda| = \|Ax\|_2 \leq \max_{\|y\| = 1} \|Ay\|_2 = \sigma_1$ by Theorem 6. The equality characterization is standard and imported, from [6, ch. 3]. **End of proof.**

The conceptual difference is this: eigenvectors are directions $A$ preserves, while right singular vectors are directions $A$ stretches most. That is why singular values are the right notion here -- eigenvalues need not exist over $\mathbb{R}$, as a $90$-degree rotation has none, and eigenvectors need not be orthogonal or even span the space, whereas the singular values and both singular bases always exist.
<!-- END S51 -->

<!-- BEGIN S68 -->
### 36. Theorem 6 -- Spectral Norm $=$ Top Sigma [S68]

#### 6.3 Theorem 6: the spectral norm is $\sigma_1$

**Theorem 6.** $\|A\|_2 = \sigma_1(A)$, attained at $x = v_1$.

*Proof.* Let $A = U\Sigma V^\top$ and let $\|x\|_2 = 1$. Put $y = V^\top x$, so $\|y\|_2 = 1$ by Theorem 4. Then, again by Theorem 4 applied to $U$,

$$ \|Ax\|_2^2 = \|U\Sigma y\|_2^2 = \|\Sigma y\|_2^2 = \sum_{i \leq r} \sigma_i^2 y_i^2 \;\leq\; \sigma_1^2 \sum_i y_i^2 = \sigma_1^2 . $$

So $\|A\|_2 \leq \sigma_1$. For the reverse, $x = v_1$ gives $y = e_1$ and $\|Av_1\|_2 = \sigma_1$. **End of proof.**

The two-line structure -- peel off $U$ and $V$ by orthogonal invariance, reduce to a diagonal problem, read off the answer -- is the master trick of this lecture, and Theorems 7 and 8 are the same trick twice more.
<!-- END S68 -->

<!-- BEGIN S69 -->
### 37. Proof (Thm 6) -- No Vector Beats $\sigma_1$ [S69]
<!-- END S69 -->

<!-- BEGIN S70 -->
### 38. Proof (Thm 6) -- And $v_1$ Achieves It [S70]
<!-- END S70 -->

<!-- BEGIN S73 -->
### 39. Theorem 7 -- Frobenius via Sigmas [S73]

#### 6.4 The Frobenius norm and Theorem 7 (continued)

**Theorem 7.** $\|A\|_F = (\sum_{i=1}^{r}\sigma_i^2)^{1/2}$, and more generally $\|UAV\|_F = \|A\|_F$ for orthogonal $U$ and $V$.

*Proof.* Using $\operatorname{tr}(XY) = \operatorname{tr}(YX)$:

$$ \|UAV\|_F^2 = \operatorname{tr}(V^\top A^\top U^\top U A V) = \operatorname{tr}(V^\top A^\top A V) = \operatorname{tr}(A^\top A V V^\top) = \operatorname{tr}(A^\top A) = \|A\|_F^2 . $$

Applying this with the SVD, $\|A\|_F = \|U^\top A V\|_F = \|\Sigma\|_F = (\sum_i \sigma_i^2)^{1/2}$. **End of proof.**
<!-- END S73 -->

<!-- BEGIN S74 -->
### 40. Proof (Thm 7) -- One Trace Chain [S74]
<!-- END S74 -->

<!-- REGION P2 END -->

<!-- REGION P3a BEGIN -->

<!-- BEGIN S79 -->
### 41. Part 4: Best Low-Rank Approximation [S79]

**Message.** Part 4 states and proves that truncating the SVD gives the best rank-$k$ approximation.
<!-- END S79 -->

<!-- BEGIN S81 -->
### 42. The Candidate -- Truncated SVD [S81]
<!-- END S81 -->

<!-- BEGIN S82 -->
### 43. Worked -- $A_1$ for the Running Matrix [S82]
<!-- END S82 -->

<!-- BEGIN S83 -->
### 44. Worked -- the Error of $A_1$ [S83]
<!-- END S83 -->

<!-- BEGIN S90 -->
### 45. Theorem 8 -- Eckart-Young-Mirsky [S90]

#### 7.3 Theorem 8: the spectral-norm case, proved

**Theorem 8 (Eckart-Young, spectral norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$.

*Proof.* By Theorem 1, $\dim\operatorname{null}(B) \geq n - k$. Let $W = \operatorname{span}\{v_1, \dots, v_{k+1}\}$, of dimension $k+1$. Then

$$ \dim\big(\operatorname{null}(B) \cap W\big) \;\geq\; (n-k) + (k+1) - n \;=\; 1 , $$

so choose a unit vector $x \in \operatorname{null}(B) \cap W$. Since $Bx = 0$,

$$ \|A - B\|_2^2 \;\geq\; \|(A-B)x\|_2^2 \;=\; \|Ax\|_2^2 \;=\; \Big\|\sum_{i \leq k+1}\sigma_i (v_i^\top x)\, u_i\Big\|_2^2 \;=\; \sum_{i \leq k+1}\sigma_i^2 (v_i^\top x)^2 \;\geq\; \sigma_{k+1}^2 , $$

using $x \in W$, so that $v_i^\top x = 0$ for $i > k+1$; orthonormality of the $u_i$; and $\sum_{i \leq k+1}(v_i^\top x)^2 = \|x\|_2^2 = 1$ with $\sigma_i \geq \sigma_{k+1}$ throughout. Since $A_k$ attains $\sigma_{k+1}$, it is optimal. **End of proof.**

The result is usually attributed to Eckart and Young [1], who proved the Frobenius case in 1936; Mirsky [2] gave the general unitarily-invariant statement in 1960, and Erhard Schmidt [3] had proved the analogous theorem for integral operators already in 1907. See [9] for the tangled history of who proved what.
<!-- END S90 -->

<!-- BEGIN S91 -->
### 46. Reading the Statement [S91]

#### 7.6 Uniqueness: the claim the lecture drops

The source asserts that $A_k$ is *the* minimizer. As stated for the spectral norm that is false, and the lecture is right to omit it.

Counterexample: $A = \operatorname{diag}(2,1)$ and $k = 1$, so $\sigma_2 = 1$ and the optimal value is $1$. Take $B_a = \operatorname{diag}(a, 0)$ for any $a \in [1,3]$. Then $A - B_a = \operatorname{diag}(2-a, 1)$, whose singular values are $|2-a| \leq 1$ and $1$, so $\|A - B_a\|_2 = 1$, which is optimal -- while $A_1 = \operatorname{diag}(2,0)$ is only the case $a = 2$. A whole interval of minimizers.

**Proposition 7.4.** In the Frobenius norm the minimizer is unique if and only if $\sigma_k > \sigma_{k+1}$.

*Sketch.* The proof of Theorem 8F is tight only when $\sigma_i(A-B) = \sigma_{i+k}(A)$ for all $i$, which forces $B$ to be a truncation at a spectral gap. If $\sigma_k = \sigma_{k+1}$ the corresponding singular subspace has dimension greater than $1$, and any $k$-dimensional subspace of it gives another minimizer -- as for $A = I_2$ with $k = 1$, where every $vv^\top$ with $\|v\| = 1$ is optimal. In the spectral norm uniqueness fails even with a strict gap, by the counterexample above.
<!-- END S91 -->

<!-- BEGIN S85 -->
### 47. Technique Review 1 -- Rank-Nullity [S85]
<!-- END S85 -->

<!-- BEGIN S86 -->
### 48. Technique Review 2 -- Big Subspaces Must Meet [S86]

#### 2.3 The dimension formula, proved

**Theorem 2.3.** For subspaces $W_1, W_2 \subseteq \mathbb{R}^n$,

$$ \dim(W_1 + W_2) + \dim(W_1 \cap W_2) \;=\; \dim W_1 + \dim W_2 , $$

where $W_1 + W_2 = \{w_1 + w_2 : w_i \in W_i\}$.

*Proof.* Let $z_1, \dots, z_t$ be a basis of $W_1 \cap W_2$. Extend it to a basis $z_1, \dots, z_t, x_1, \dots, x_p$ of $W_1$ and to a basis $z_1, \dots, z_t, y_1, \dots, y_q$ of $W_2$, so $\dim W_1 = t + p$ and $\dim W_2 = t + q$. The combined list of $z$'s, $x$'s and $y$'s spans $W_1 + W_2$; the claim is that it is independent.

Suppose $\sum \gamma_i z_i + \sum \alpha_j x_j + \sum \beta_\ell y_\ell = 0$. Then

$$ v := \sum_\ell \beta_\ell y_\ell = -\sum_i \gamma_i z_i - \sum_j \alpha_j x_j $$

lies in $W_1$ and in $W_2$, hence in $W_1 \cap W_2$, so $v = \sum_i \delta_i z_i$ for some coefficients $\delta$. But $\sum_\ell \beta_\ell y_\ell - \sum_i \delta_i z_i = 0$ with the $z$'s and $y$'s independent forces all $\beta_\ell = 0$, and all $\delta_i = 0$. The relation collapses to $\sum \gamma_i z_i + \sum \alpha_j x_j = 0$, and independence in $W_1$ kills the rest. Hence $\dim(W_1 + W_2) = t + p + q$, and $(t + p + q) + t = (t + p) + (t + q)$. **End of proof.**

**Corollary 2.4.** $\dim(W_1 \cap W_2) \geq \dim W_1 + \dim W_2 - n$. In particular, if $\dim W_1 + \dim W_2 > n$ then $W_1 \cap W_2$ contains a nonzero vector.

*Proof.* $W_1 + W_2 \subseteq \mathbb{R}^n$ gives $\dim(W_1 + W_2) \leq n$; substitute into Theorem 2.3. **End of proof.**

This is the "two planes in $\mathbb{R}^3$ share a line" picture, and it is the entire engine of Theorem 8: it is what converts "$B$ has low rank" into "$B$ is blind at a specific place where $A$ is loud."
<!-- END S86 -->

<!-- BEGIN S87 -->
### 49. Picture -- Two Planes in $\mathbb{R}^3$ [S87]
<!-- END S87 -->

<!-- BEGIN S88 -->
### 50. Technique Review 3 -- Bounding a Max From Below [S88]
<!-- END S88 -->

<!-- BEGIN S89 -->
### 51. Technique Review 4 -- $\|Aw\|^2$ in the $v$-Basis [S89]

#### 7.2 Courant-Fischer for singular values

Both proofs below rest on a variational characterization; it is proved here rather than cited because everything downstream is a two-line consequence of it.

**Lemma 7.1 (min-max and max-min).** For $1 \leq i \leq \min(m,n)$,

$$ \sigma_i(A) \;=\; \max_{\substack{S \subseteq \mathbb{R}^n \\ \dim S = i}} \ \min_{\substack{x \in S \\ \|x\|_2 = 1}} \|Ax\|_2 \;=\; \min_{\substack{T \subseteq \mathbb{R}^n \\ \dim T = n-i+1}} \ \max_{\substack{x \in T \\ \|x\|_2 = 1}} \|Ax\|_2 . $$

*Proof of the first equality; the second is analogous.*

For the lower bound on the outer maximum, take $S_0 = \operatorname{span}\{v_1, \dots, v_i\}$. For unit $x \in S_0$ we have $x = \sum_{j \leq i} c_j v_j$ with $\sum_j c_j^2 = 1$, and $\|Ax\|_2^2 = \sum_{j \leq i}\sigma_j^2 c_j^2 \geq \sigma_i^2$, since $\sigma_j \geq \sigma_i$ for $j \leq i$. So the inner minimum over $S_0$ is at least $\sigma_i$, and in fact equals it, at $x = v_i$.

For the upper bound over every $S$, let $\dim S = i$ and put $W = \operatorname{span}\{v_i, v_{i+1}, \dots, v_n\}$, of dimension $n - i + 1$. By the dimension count in Corollary 2.4, $\dim(S \cap W) \geq \dim S + \dim W - n = 1$, so there is a unit vector $x \in S \cap W$. Writing $x = \sum_{j \geq i} c_j v_j$ gives $\|Ax\|_2^2 = \sum_{j \geq i}\sigma_j^2 c_j^2 \leq \sigma_i^2$. Hence the inner minimum over $S$ is at most $\sigma_i$. **End of proof.**

Note the mechanism: a dimension count forces two subspaces to intersect. That single idea drives Theorem 8, Lemma 7.3 and Theorem 9 alike.
<!-- END S89 -->

<!-- BEGIN S92 -->
### 52. Proof Overview (Spectral Case) [S92]
<!-- END S92 -->

<!-- BEGIN S93 -->
### 53. Step 1 -- Every Competitor Has a Blind Spot [S93]
<!-- END S93 -->

<!-- BEGIN S94 -->
### 54. Step 2 -- Where $A$ Is Still Strong [S94]
<!-- END S94 -->

<!-- BEGIN S95 -->
### 55. Step 3 -- The Two Subspaces Collide [S95]
<!-- END S95 -->

<!-- BEGIN S96 -->
### 56. Step 4 -- The Witness Bound [S96]
<!-- END S96 -->

<!-- BEGIN S97 -->
### 57. Step 4, Finished -- $A$ Is Strong at $w$ [S97]
<!-- END S97 -->

<!-- BEGIN S98 -->
### 58. Step 5 -- Truncation Hits the Floor [S98]
<!-- END S98 -->

<!-- BEGIN S99 -->
### 59. Proof Summary -- the Skeleton [S99]
<!-- END S99 -->

<!-- BEGIN S101 -->
### 60. The Frobenius Case [S101]

#### 7.4 The Frobenius case, proved

The lecture states this case and does not prove it; the source likewise defers to an external note [16]. It is proved here in full, because the Frobenius case -- not the spectral one -- is what principal component analysis, latent-factor recommenders and low-rank compression actually minimize. The route is Weyl's inequality for singular values.

**Lemma 7.2 (Weyl, additive).** For $X, Y \in \mathbb{R}^{m \times n}$ and indices $i, j \geq 1$ with $i + j - 1 \leq \min(m,n)$: $\sigma_{i+j-1}(X+Y) \leq \sigma_i(X) + \sigma_j(Y)$.

*Proof.* By the min-max form of Lemma 7.1 there are subspaces $T_X$ of dimension $n - i + 1$ and $T_Y$ of dimension $n - j + 1$ with $\max_{x \in T_X, \|x\|=1}\|Xx\|_2 = \sigma_i(X)$ and likewise for $Y$. Put $T = T_X \cap T_Y$, so that

$$ \dim T \;\geq\; (n - i + 1) + (n - j + 1) - n \;=\; n - (i + j - 1) + 1 . $$

Applying the min-max characterization at index $i + j - 1$, whose minimum runs over subspaces of exactly that dimension -- and any larger subspace contains one -- gives

$$ \sigma_{i+j-1}(X+Y) \leq \max_{x \in T, \|x\|=1}\|(X+Y)x\|_2 \leq \max_{x \in T, \|x\|=1}\big(\|Xx\|_2 + \|Yx\|_2\big) \leq \sigma_i(X) + \sigma_j(Y) . $$

**End of proof.**

**Lemma 7.3.** If $\operatorname{rank}(B) \leq k$ then $\sigma_{i+k}(A) \leq \sigma_i(A - B)$ for all $i \geq 1$, with the convention $\sigma_j := 0$ beyond $\min(m,n)$.

*Proof.* Apply Lemma 7.2 with $X = A - B$, $Y = B$, and indices $i$ and $k+1$:

$$ \sigma_{i+k}(A) = \sigma_{i + (k+1) - 1}\big((A-B) + B\big) \leq \sigma_i(A-B) + \sigma_{k+1}(B) . $$

But $\operatorname{rank}(B) \leq k$ means $\sigma_{k+1}(B) = 0$. **End of proof.**

**Theorem 8F (Eckart-Young, Frobenius norm).** For every $B$ with $\operatorname{rank}(B) \leq k$,

$$ \|A - B\|_F^2 \;\geq\; \sum_{i > k}\sigma_i(A)^2 \;=\; \|A - A_k\|_F^2 . $$

*Proof.* By Theorem 7 and Lemma 7.3,

$$ \|A-B\|_F^2 = \sum_{i \geq 1}\sigma_i(A-B)^2 \;\geq\; \sum_{i \geq 1}\sigma_{i+k}(A)^2 = \sum_{j > k}\sigma_j(A)^2 , $$

which is exactly $\|A - A_k\|_F^2$ by the display in Section 7.1. **End of proof.**

The same two lines prove the nuclear case, since $\|A-B\|_* = \sum_i \sigma_i(A-B) \geq \sum_{i > k}\sigma_i(A) = \|A - A_k\|_*$. And, since Lemma 7.3 controls the whole singular-value vector entry by entry, they prove Mirsky's general statement.

**Theorem 8M (Mirsky, 1960).** For *every* unitarily invariant norm, $A_k$ minimizes $\|A - B\|$ over all $B$ with $\operatorname{rank}(B) \leq k$. *Reason:* such a norm is a symmetric gauge function of the singular-value vector, by von Neumann's theorem, hence monotone in it, and Lemma 7.3 gives that $\sigma(A - B)$ dominates $\sigma(A - A_k)$ entry by entry after sorting.

This is why one can say that a single matrix, $A_k$, is simultaneously optimal for all three norms -- a genuinely unusual state of affairs; the $\ell_1$ and $\ell_2$ minimizers of an ordinary regression problem certainly do not coincide.
<!-- END S101 -->

<!-- BEGIN S121 -->
### 61. S121 (new) [S121]
<!-- END S121 -->

<!-- REGION P3a END -->

<!-- REGION P3b BEGIN -->

<!-- BEGIN S116 -->
### 62. Part 5: Read the Answer [S116]

**Message.** Part 5 reads the theorem's answer on concrete matrices and states what it does and does not cover.
<!-- END S116 -->

<!-- BEGIN S102 -->
### 63. Worked -- EYM on the Running Matrix [S102]

#### 7.5 Energy accounting and the running example

Theorem 7 licenses reporting truncation quality as a fraction of "energy": $\|A_k\|_F^2 / \|A\|_F^2 = \sum_{i \leq k}\sigma_i^2 / \sum_{i \leq r}\sigma_i^2$. For the running $A$, the rank-one truncation captures $\sigma_1^2/(\sigma_1^2 + \sigma_2^2) = 45/50 = 90\%$, with $A_1$ having first row $(1.5, 1.5)$ and second row $(4.5, 4.5)$, and the residual $A - A_1$ having first row $(1.5, -1.5)$ and second row $(-0.5, 0.5)$, so that

$$ \|A - A_1\|_2 = \|A - A_1\|_F = \sigma_2 = \sqrt5 . $$

The coincidence that the two norms agree here is not general; it holds because $A - A_1$ has rank one, so its singular-value vector has a single nonzero entry and all $\ell_p$ norms of it agree. Check independently: $\|A - A_1\|_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$. Checked.
<!-- END S102 -->

<!-- BEGIN S103 -->
### 64. How Much Did $A_1$ Keep? [S103]
<!-- END S103 -->

<!-- BEGIN S122 -->
### 65. S122 (new) [S122]
<!-- END S122 -->

<!-- BEGIN S123 -->
### 66. S123 (new) [S123]
<!-- END S123 -->

<!-- BEGIN S117 -->
### 67. Every Tool, One Line Each [S117]
<!-- END S117 -->

<!-- REGION P3b END -->

<!-- REGION Closing BEGIN -->

<!-- BEGIN S119 -->
### 68. Closing: $A = \sum_i \sigma_i u_i v_i^{\top}$ [S119]

**Message.** Every matrix is a sum of rank-one layers $\sigma_i u_i v_i^{\top}$; keeping the largest $k$ is the best rank-$k$ approximation.

The closing slide shows the SVD as a sum of rank-one layers and opens questions.
<!-- END S119 -->

<!-- REGION Closing END -->

## 10 References

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
16. R. D. Wilkinson. MATH3030 lecture notes, section 3.5, "Low-rank approximation." https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html. The proof reference cited in the source; the Frobenius case is proved independently in Section 7.4 above.
17. Y. Koren, R. Bell, and C. Volinsky. "Matrix factorization techniques for recommender systems." *IEEE Computer* 42(8):30-37, 2009. doi:10.1109/MC.2009.263 -- https://doi.org/10.1109/MC.2009.263. By the Netflix Prize winners; the practical counterpart to Section 8.4.
18. E. J. Hu et al. "LoRA: Low-Rank Adaptation of Large Language Models." *ICLR* 2022. arXiv:2106.09685 -- https://arxiv.org/abs/2106.09685
19. N. Halko, P. G. Martinsson, and J. A. Tropp. "Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions." *SIAM Review* 53(2):217-288, 2011. arXiv:0909.4061 -- https://arxiv.org/abs/0909.4061
20. Companion notes in this series: prob01 through prob09 cover the probability half (lectures 1 through 9). Jensen's inequality, used in Lemma 3.1, is in prob01; the covariance eigendecomposition, the symmetric positive-semidefinite special case of Section 4.5, is in prob08. The notes opt02, opt03 and opt04 (lectures 11 through 13) cover regression, convexity, and stochastic gradient methods. Each lives at `../<name>/<name>-note.md` in this accessible edition, or `-note.html` in the original.
