# Deep Learning Math 11. Linear Regression, ERM and Ridge

**About this file.** This is the accessible Markdown edition of the lecture note for Lecture 11 (opt02), written to be read linearly by a screen reader or a braille display. Every figure and every table of the original has been replaced by prose carrying the same information, every matrix is written out row by row, and all mathematics is in LaTeX. The section numbering matches the original note exactly, so a reference to "Section 9.4" means the same thing in both. Nothing else is needed to read it.

**Convention.** Throughout, $A \in \mathbb{R}^{N\times n}$ is the design matrix, its rows being the $N$ examples and its columns the $n$ features; $B \in \mathbb{R}^{N}$ is the label vector; $r = \operatorname{rank}(A)$. The compact SVD is $A = U_c\Sigma_cV_c^{\top}$ with $\Sigma_c = \operatorname{diag}(\sigma_1,\dots,\sigma_r)$ and every $\sigma_i > 0$. The least-squares objective is $J(\theta) = \tfrac12\|A\theta - B\|_2^2$. All references to opt01 are to the companion note for Lecture 10.

**The running example.** One data set is used throughout. Three points in one input variable: $x = -1, 0, 1$ with labels $y = 0, 1, 3$. With a dummy intercept feature the design matrix $A$ has first row $(1, -1)$, second row $(1, 0)$, third row $(1, 1)$, and $B = (0, 1, 3)$. Whenever the text says "the running example", this is the data.

**Notation.**

- $\theta \in \mathbb{R}^n$: parameter vector; $\theta^\star$ its least-squares optimum, $\theta^\star_\lambda$ its ridge optimum.
- $A^{\dagger}$: Moore-Penrose pseudo-inverse of $A$.
- $\operatorname{range}(A)$, $\operatorname{null}(A)$: column space and null space.
- $S^{\perp}$: orthogonal complement of the subspace $S$.
- $\|v\|_2$: Euclidean norm; $\|M\|_F$: Frobenius norm; $\|M\|_*$: nuclear norm.
- $\kappa_2(A) = \sigma_1/\sigma_n$: 2-norm condition number.
- $u_i$, $v_i$: the $i$-th left and right singular vectors of $A$.
- $\phi$: a feature map; $\Phi$ the resulting design matrix.
- $R[f]$, $\hat R[f]$: risk and empirical risk; $R^\star$ the Bayes risk.
- $\mathcal{F}$: hypothesis class; $\hat f$ the empirical risk minimizer.
- $\varepsilon$: noise vector; $\theta_0$ the true parameter; $\sigma^2$ the noise variance.
- $M \succeq 0$: $M$ is positive semidefinite; the Loewner order $M \succeq M'$ means $M - M' \succeq 0$.
- SSE, SST: sum of squared errors, total sum of squares.
- $\operatorname{diag}(a, b)$: the diagonal matrix with those diagonal entries.

**Background used.** Everything from Lecture 10 (opt01) is used freely: the compact SVD and the four fundamental subspaces (opt01 Section 4.4), orthogonal decomposition of a vector against a subspace (opt01 Theorem 2), Gram-Schmidt completion of an orthonormal set (opt01 Lemma 2.5), rank-nullity (opt01 Theorem 1), invariance of the Euclidean norm under orthogonal maps (opt01 Theorem 4), the pseudo-inverse and its projectors (opt01 Sections 5.3 and 5.5), and its discontinuity (opt01 Section 5.6). From the probability half, the conditional expectation machinery of Lecture 7 (prob07) is used in Section 8.2, and the Gaussian likelihood of Lecture 7 in Section 5.1. Two results are cited but not proved here: Rademacher complexity bounds (Section 8.4) and the double-descent phenomenon (Section 8.5).

**What this edition adds.** Nothing mathematical. The only changes are linearization: matrices spelled out row by row, verification tick marks turned into the word "checked", and the original note's boxed statements turned into bold-labelled paragraphs.

**Contents.**

1. What this lecture actually claims
2. Setup
3. Theorem 1: the optimum is $A^{\dagger}B$
4. Geometry and the normal equations
5. What kind of estimator is $\theta^\star$
6. Feature maps
7. Multiple outputs
8. Empirical risk minimization
9. Ridge regression
10. What the lecture leaves out
11. References

**Summary of what is proved here.** The two gradient rules of the technique review (Lemma 2.1); Theorem 1, that $J$ always attains its minimum, that the minimizer set is exactly $A^{\dagger}B + \operatorname{null}(A)$, and that $A^{\dagger}B$ is its unique least-norm element; Proposition 4.1, the projection theorem; Theorem 2, the normal equations, by exact expansion with no calculus; Proposition 4.2, that the normal equations are always consistent; Proposition 5.1, that least squares is the Gaussian maximum-likelihood estimate; the Gauss-Markov theorem; Proposition 6.1, that more features never increase training error, and Proposition 6.2, the Vandermonde determinant; Proposition 7.1, the multiple-output case; Theorem 8.1, the Bayes predictor for squared loss; Proposition 8.2, the two-supremum bound making empirical risk minimization sound; Lemma 9.1 and Theorem 3, existence and uniqueness of the ridge optimum; Proposition 9.2, ridge as singular-value shrinkage; Proposition 9.3, that the ridge path tends to $A^{\dagger}B$ as $\lambda \to 0^{+}$; the MAP correspondence with $\lambda = \sigma^2/\tau^2$; and Theorem 9.4, the Hoerl-Kennard theorem that some positive $\lambda$ always beats least squares in mean squared error.

## 1 What This Lecture Actually Claims

Lecture 10 ended on a teaser: $x = A^{\dagger}b$ "solves" systems that have no solution. That sentence is meaningless until "solves" is given a definition, and the definition is: *minimizes $\|A\theta - B\|_2$*. Once that is fixed, three questions have to be answered, and the lecture answers all three.

1. **Does a minimizer exist?** Not obvious. $\mathbb{R}^n$ is not compact and $J$ is not coercive when $\operatorname{null}(A) \neq \{0\}$. Theorem 1's proof settles it constructively.
2. **Is it unique, and if not, which one do we mean?** The minimizer set is an affine subspace; $A^{\dagger}B$ is singled out by least norm, and Section 9.5 shows that tie-break is not arbitrary.
3. **Is minimizing the training miss the right thing to do at all?** Section 8 says: only conditionally. Section 9 fixes the objective when it is not.

This is the one place in the course where a training problem closes in a formula. Everything from Lecture 12 (opt03) onward exists because that stops being true. Historically the formula is old: Legendre published the method in 1805 [1] and Gauss claimed use from 1795, publishing the Gaussian-error justification of Proposition 5.1 in 1809 [2]. The dispute is the first priority fight in mathematical statistics.

## 2 Setup

### 2.1 Data, model, design matrix

Data $(\mathbf{x}^{(1)},y^{(1)}),\dots,(\mathbf{x}^{(N)},y^{(N)})$ with $\mathbf{x}^{(i)}\in\mathbb{R}^n$ and $y^{(i)}\in\mathbb{R}$; model $f_\theta(\mathbf{x}) = \theta^{\top}\mathbf{x}$. Stacking the inputs as rows gives the *design matrix* $A\in\mathbb{R}^{N\times n}$ with $A_{ij} = x^{(i)}_j$, and the label vector $B \in \mathbb{R}^N$, so that $A\theta$ is the vector of all $N$ predictions and

$ \sum_{i=1}^{N}\big(\theta^{\top}\mathbf{x}^{(i)} - y^{(i)}\big)^2 \;=\; \|A\theta - B\|_2^2 . $

The *dummy feature* trick, prepending a constant $1$ to every $\mathbf{x}^{(i)}$, buys an intercept at the cost of nothing: the model stays linear in $\theta$, which is the only linearity Theorem 1 uses. It is worth being explicit that "linear model" in this lecture means *linear in the parameters*, never linear in the inputs. Section 6 exploits exactly that gap.

### 2.2 Harmless rescalings of the objective

The lecture drops the factor $\tfrac1N$ and inserts a factor $\tfrac12$ freely. Both are licensed by the same triviality, worth stating once: for $c > 0$ and any $g$, $\operatorname*{argmin}_\theta c\,g(\theta) = \operatorname*{argmin}_\theta g(\theta)$, and $\operatorname*{argmin}_\theta\,(g(\theta) + \text{const}) = \operatorname*{argmin}_\theta g(\theta)$. Both are used in Theorem 1's Step 3.

This is *not* true once a regularizer is present. Rescaling the fit term by $c$ while leaving $\lambda\|\theta\|^2$ alone is the same as dividing $\lambda$ by $c$, which is why the $\tfrac1N$ convention has to be fixed before quoting a numeric $\lambda$ (Section 9.8).

### 2.3 Why squared loss: the honest answer

The lecture motivates $(\hat y - y)^2$ as "zero if and only if exact, grows with the miss." So does $|\hat y - y|$, which is listed as the robust alternative. The real reasons squared loss is the default are three, and only the first is about the data.

- *Statistical.* It is the negative log-likelihood of Gaussian noise, up to constants (Proposition 5.1), so it is the right loss exactly when the residuals are Gaussian and homoscedastic.
- *Geometric.* It is the only loss for which minimizing is orthogonal projection, hence the only one giving a closed form (Sections 3 and 4). Regression under the $\ell_1$ loss has no formula; it is a linear program.
- *Decision-theoretic.* Its Bayes predictor is the conditional mean (Section 8.2), a quantity we know how to interpret. The $\ell_1$ Bayes predictor is the conditional *median*, a different and equally legitimate target.

Squared loss also has a real cost, flagged in one line: it punishes big misses quadratically, so a single outlier can move $\theta^\star$ arbitrarily far. The formula's convenience and its fragility have the same source.

### 2.4 The two gradient rules, derived

The technique review asserts $\nabla_\theta(b^{\top}\theta) = b$ and $\nabla_\theta(\theta^{\top}Q\theta) = 2Q\theta$ for symmetric $Q$, with the instruction "check entrywise." Here is the check.

**Lemma 2.1.** For $b \in \mathbb{R}^n$ and $Q\in\mathbb{R}^{n\times n}$: $\nabla_\theta (b^{\top}\theta) = b$, and $\nabla_\theta(\theta^{\top}Q\theta) = (Q + Q^{\top})\theta$, which is $2Q\theta$ when $Q = Q^{\top}$.

*Proof.* $b^{\top}\theta = \sum_j b_j\theta_j$, so the partial derivative in $\theta_k$ is $b_k$. For the quadratic, $\theta^{\top}Q\theta = \sum_{i,j}Q_{ij}\theta_i\theta_j$; differentiating in $\theta_k$, the terms with $i = k \neq j$ contribute $\sum_j Q_{kj}\theta_j$, those with $j = k\neq i$ contribute $\sum_i Q_{ik}\theta_i$, and the single term $i=j=k$ contributes $2Q_{kk}\theta_k$, which is exactly what the two sums give at $j=k$ and at $i=k$. So the $k$-th partial derivative is $(Q\theta)_k + (Q^{\top}\theta)_k$. **End of proof.**

Apply it to

$ J(\theta) = \tfrac12\theta^{\top}A^{\top}A\theta - (A^{\top}B)^{\top}\theta + \tfrac12\|B\|_2^2, $

which comes from expanding $\|A\theta-B\|_2^2 = \theta^{\top}A^{\top}A\theta - 2B^{\top}A\theta + B^{\top}B$ and using $\theta^{\top}A^{\top}B = B^{\top}A\theta$ since both are scalars. The result is

$ \nabla J(\theta) \;=\; A^{\top}A\theta - A^{\top}B \;=\; A^{\top}(A\theta - B), $

the symmetry hypothesis being satisfied because $A^{\top}A$ is symmetric. Note that Theorem 2's proof below does *not* actually need calculus: the exact expansion does all the work, which is why an if-and-only-if is available rather than a first-order necessary condition.

## 3 Theorem 1: the optimum is $A^{\dagger}B$

### 3.1 Statement

**Theorem 1.** Let $A\in\mathbb{R}^{N\times n}$ have rank $r$ and let $B\in\mathbb{R}^N$ be arbitrary. Then $J(\theta) = \tfrac12\|A\theta-B\|_2^2$ attains its minimum, the set of minimizers is the affine subspace $A^{\dagger}B + \operatorname{null}(A)$, and $A^{\dagger}B$ is the unique minimizer of smallest Euclidean norm. The minimizer is unique if and only if $r = n$.

No hypothesis on shape or rank. The five steps of the lecture's proof are reproduced below as a single argument, with three points filled in that the presentation passes over: the existence of the completion $\tilde U$, the block-norm identity, and the "all minimizers" claim.

### 3.2 Proof

*Step 1, SVD and completion.* Write $A = U_c\Sigma_cV_c^{\top}$ (opt01 Section 4.4). The columns of $U_c$ are $r$ orthonormal vectors in $\mathbb{R}^N$ and $r \leq N$, so by Gram-Schmidt applied to any completion to a basis (opt01 Lemma 2.5) there is $\tilde U \in \mathbb{R}^{N\times(N-r)}$ such that the matrix $U$ whose first $r$ columns are those of $U_c$ and whose remaining $N-r$ columns are those of $\tilde U$ is orthogonal. The bookkeeping identities $U_c^{\top}U_c = I_r$, $\tilde U^{\top}\tilde U = I_{N-r}$ and $\tilde U^{\top}U_c = 0$ are exactly the statement $U^{\top}U = I_N$ read blockwise.

*Step 2, rotate.* By orthogonal invariance (opt01 Theorem 4), $\|A\theta - B\|_2 = \|U^{\top}(A\theta - B)\|_2$. Read blockwise, $U^{\top}(A\theta - B)$ is the stacked vector whose top block is $\Sigma_cV_c^{\top}\theta - U_c^{\top}B$ (of length $r$) and whose bottom block is $-\,\tilde U^{\top}B$ (of length $N-r$), using $U_c^{\top}U_c = I_r$ in the top block and $\tilde U^{\top}U_c = 0$ in the bottom. For a stacked vector $z$ with blocks $z_1$ and $z_2$ one has $\|z\|_2^2 = \|z_1\|_2^2 + \|z_2\|_2^2$, the coordinates being simply partitioned, so

$ J(\theta) \;=\; \tfrac12\big\|\Sigma_cV_c^{\top}\theta - U_c^{\top}B\big\|_2^2 \;+\; \tfrac12\big\|\tilde U^{\top}B\big\|_2^2 . $

Call the first term $J_1(\theta)$; the second does not depend on $\theta$.

*Step 3, drop the constant.* By Section 2.2, $\operatorname{argmin} J = \operatorname{argmin} J_1$. The dropped constant is not noise: it equals $\tfrac12\|(I - U_cU_c^{\top})B\|_2^2$, the squared distance from $B$ to $\operatorname{range}(A)$, the error no $\theta$ can remove. Section 4 reads it geometrically.

*Step 4, split $\theta$.* By opt01 Theorem 2 applied to $S = \operatorname{range}(V_c)$, every $\theta$ decomposes uniquely as $\theta = \theta_1 + \theta_2$ with $\theta_1\in S$ and $\theta_2\in S^{\perp} = \operatorname{null}(V_c^{\top})$, and $\|\theta\|_2^2 = \|\theta_1\|_2^2+\|\theta_2\|_2^2$. Since $V_c^{\top}\theta_2 = 0$ we get $J_1(\theta) = J_1(\theta_1)$: the objective is blind to $\theta_2$. Note also $A\theta_2 = U_c\Sigma_c V_c^{\top}\theta_2 = 0$, so $S^{\perp} \subseteq \operatorname{null}(A)$; conversely $A\theta = 0$ implies $\Sigma_cV_c^{\top}\theta = U_c^{\top}A\theta = 0$, hence $V_c^{\top}\theta = 0$ because $\Sigma_c$ is invertible. So $\operatorname{null}(A) = \operatorname{range}(V_c)^{\perp}$ exactly.

*Step 5, solve.* Parametrize $\theta_1 = V_cc$ with $c\in\mathbb{R}^r$; then $V_c^{\top}\theta_1 = V_c^{\top}V_cc = c$ and $J_1 = \tfrac12\|\Sigma_cc - U_c^{\top}B\|_2^2 \geq 0$, with equality if and only if $c = c^\star := \Sigma_c^{-1}U_c^{\top}B$. That is possible because $\Sigma_c$ is invertible, and this is where positivity of the $\sigma_i$ is used. So the minimum of $J_1$ is $0$, attained precisely at $\theta_1 = V_c\Sigma_c^{-1}U_c^{\top}B = A^{\dagger}B$, which lies in $\operatorname{range}(V_c)$ as required, plus any $\theta_2\in\operatorname{null}(A)$. Existence and the minimizer set are both settled.

*Least norm.* $A^{\dagger}B \in \operatorname{range}(V_c)$, which is orthogonal to $\operatorname{null}(A)$, so for $\theta_2\in\operatorname{null}(A)$ we get $\|A^{\dagger}B + \theta_2\|_2^2 = \|A^{\dagger}B\|_2^2 + \|\theta_2\|_2^2 \geq \|A^{\dagger}B\|_2^2$, with equality if and only if $\theta_2 = 0$.

*Uniqueness.* The minimizer set is a single point if and only if $\operatorname{null}(A) = \{0\}$, if and only if $r = n$ (opt01 Theorem 1, rank-nullity). **End of proof.**

### 3.3 What the proof really used

Only three things: that rotations preserve $\ell_2$ length, that $\Sigma_c$ is invertible, and Pythagoras. The trick has a name, *rotate until the problem is diagonal*, and it is worth noticing that this is the same move as opt01's Theorems 6, 7 and 8. The reason it works here and nowhere later in the course is that the objective is a squared $\ell_2$ norm of an affine function of $\theta$; replace the norm (by $\ell_1$) or the affinity (by a neural network) and the rotation buys nothing.

### 3.4 The running example, recomputed

Recall $A$ has first row $(1, -1)$, second row $(1, 0)$, third row $(1, 1)$, and $B = (0,1,3)$.

First, the claim that no exact solution exists. Rows 1 and 2 give $\theta_0 - \theta_1 = 0$ and $\theta_0 = 1$, hence $\theta = (1,1)$, and row 3 then demands $\theta_0+\theta_1 = 2 = 3$. Checked: a contradiction, so $B \notin \operatorname{range}(A)$.

**SVD.** $A^{\top}A$ is the matrix with first row $(3, 0)$ and second row $(0, 2)$, that is $\operatorname{diag}(3,2)$. Checked: the off-diagonal entry is $\sum_i x_i = -1+0+1 = 0$, which is what "centered inputs" means. It is already diagonal, so $V_c = I_2$, $\sigma_1 = \sqrt3$ and $\sigma_2 = \sqrt2$. Checked. And

$ u_1 = \tfrac{Av_1}{\sigma_1} = \tfrac{1}{\sqrt3}(1,1,1), \qquad u_2 = \tfrac{Av_2}{\sigma_2} = \tfrac{1}{\sqrt2}(-1,0,1). $

Checked; they are orthonormal, since $u_1^{\top}u_2 = \tfrac{1}{\sqrt6}(-1+0+1) = 0$. Then $A^{\dagger} = V_c\Sigma_c^{-1}U_c^{\top}$ is the sum of $\tfrac13$ times the matrix with first row $(1,1,1)$ and second row $(0,0,0)$, and $\tfrac12$ times the matrix with first row $(0,0,0)$ and second row $(-1,0,1)$. So $A^{\dagger}$ is the two-by-three matrix with first row $(\tfrac13, \tfrac13, \tfrac13)$ and second row $(-\tfrac12, 0, \tfrac12)$. Checked. Hence

$ \theta^\star = A^{\dagger}B = \Big(\tfrac{0+1+3}{3},\ \tfrac{-0+3}{2}\Big) = \Big(\tfrac43, \tfrac32\Big). $

Checked. The reading given in the lecture is exact: row 1 of $A^{\dagger}$ averages the labels, and row 2 is the end-to-end difference quotient $\tfrac{y^{(3)}-y^{(1)}}{2}$, both consequences of $V_c = I$ and the symmetric design.

Fitted values and residuals: $\hat y = \tfrac43 + \tfrac32x$ gives $\hat y(-1) = -\tfrac16$, $\hat y(0) = \tfrac43$, $\hat y(1) = \tfrac{17}{6}$, so the residuals $y - \hat y$ are $\tfrac16, -\tfrac13, \tfrac16$ and $\mathrm{SSE} = \tfrac{1}{36}+\tfrac{4}{36}+\tfrac{1}{36} = \tfrac16$. Checked. (The objective carries a factor $\tfrac12$; the quoted $\tfrac16$ is the unhalved sum of squares, which is the standard reporting convention.) Two independent cross-checks not run in the lecture:

- *The fit passes through $(\bar x, \bar y)$.* Whenever an intercept column is present, the first normal equation reads $\sum_i(y^{(i)} - \hat y^{(i)}) = 0$, that is $\bar y = \theta_0 + \theta_1\bar x$. Here $\bar x = 0$ and $\bar y = \tfrac43 = \theta_0$. Checked.
- *The textbook slope formula.* $\theta_1 = \frac{\sum_i (x^{(i)}-\bar x)(y^{(i)}-\bar y)}{\sum_i(x^{(i)}-\bar x)^2} = \frac{(-1)(0-\tfrac43) + 0 + (1)(3-\tfrac43)}{2} = \frac{\tfrac43+\tfrac53}{2} = \tfrac32$. Checked.

For completeness, $\mathrm{SST} = \sum_i(y^{(i)}-\bar y)^2 = \tfrac{16}{9}+\tfrac19+\tfrac{25}{9} = \tfrac{14}{3}$, so $R^2 = 1 - \tfrac{\mathrm{SSE}}{\mathrm{SST}} = 1 - \tfrac{1/6}{14/3} = \tfrac{27}{28}\approx 0.964$.

## 4 Geometry and the Normal Equations

### 4.1 The projection picture

As $\theta$ ranges over $\mathbb{R}^n$, the vector $A\theta$ ranges over exactly $\operatorname{range}(A)$, a subspace of $\mathbb{R}^N$ of dimension $r$. So the problem "minimize $\|A\theta - B\|_2$" is, verbatim, "find the point of $\operatorname{range}(A)$ closest to $B$." The geometric content of the theorem is this: the closest point is the orthogonal projection, and the residual is perpendicular to the subspace. Formally:

**Proposition 4.1 (projection).** Let $S\subseteq\mathbb{R}^N$ be a subspace and $B \in \mathbb{R}^N$. There is a unique $\hat B \in S$ minimizing $\|B - s\|_2$ over $s\in S$, namely the $\hat B$ from the orthogonal decomposition $B = \hat B + (B-\hat B)$ with $\hat B \in S$ and $B - \hat B \in S^{\perp}$; and it is characterized by $B - \hat B$ being orthogonal to $S$.

*Proof.* Existence and uniqueness of the decomposition is opt01 Theorem 2. For any $s\in S$, write $B - s = (B-\hat B) + (\hat B - s)$ with the first term in $S^{\perp}$ and the second in $S$, so by Pythagoras $\|B-s\|_2^2 = \|B-\hat B\|_2^2 + \|\hat B - s\|_2^2 \geq \|B-\hat B\|_2^2$, with equality if and only if $s = \hat B$. Conversely if $B - \hat B$ is orthogonal to $S$ with $\hat B \in S$, the same computation shows $\hat B$ minimizes. **End of proof.**

Combining with Theorem 1: $\hat B = AA^{\dagger}B = U_cU_c^{\top}B$, which is the orthogonal projector onto $\operatorname{range}(A)$ (opt01 Section 5.3). The leftover constant discarded in Theorem 1's Step 3 was $\tfrac12\|B - \hat B\|_2^2$, the irreducible error. Nothing was thrown away; it was *named*.

### 4.2 Theorem 2 (normal equations)

**Theorem 2.** $\theta$ minimizes $J$ if and only if $A^{\top}(A\theta - B) = 0$, that is, $A^{\top}A\theta = A^{\top}B$.

*Proof (exact expansion, no calculus).* Fix $\theta$ and let $h\in\mathbb{R}^n$ be arbitrary. Then

$ J(\theta+h) = \tfrac12\|A\theta - B + Ah\|_2^2 = J(\theta) + h^{\top}A^{\top}(A\theta - B) + \tfrac12\|Ah\|_2^2 . $

For the "if" direction: if $A^{\top}(A\theta-B) = 0$ the middle term vanishes and $J(\theta+h) = J(\theta) + \tfrac12\|Ah\|_2^2\geq J(\theta)$ for every $h$, so $\theta$ is a global minimizer. For the "only if" direction: if $g := A^{\top}(A\theta - B)\neq 0$, take $h = -tg$ with $t > 0$; then $J(\theta+h) = J(\theta) - t\|g\|_2^2 + \tfrac{t^2}{2}\|Ag\|_2^2$, which is smaller than $J(\theta)$ for all small enough $t > 0$, specifically any $t < 2\|g\|_2^2/\|Ag\|_2^2$, with any $t>0$ working if $Ag = 0$. So $\theta$ is not a minimizer. **End of proof.**

Two remarks not made in the lecture. First, this proof is *exact*: the expansion has no remainder term, which is why a stationary point is automatically a global minimum. That is a property of quadratics, not a general fact, and it is the reason opt03 has to introduce convexity to recover it. Second, the equivalence is the algebraic form of Proposition 4.1: $A^{\top}(A\theta - B) = 0$ says the residual is orthogonal to every column of $A$, that is, to $\operatorname{range}(A)$.

### 4.3 The normal equations are always consistent

The lecture writes down $A^{\top}A\theta = A^{\top}B$ and moves on. But a linear system can be unsolvable, which is the entire premise of the lecture, so it is a genuine gap that this one never is. It follows from Theorem 1, since a minimizer exists and hence a solution exists, but the direct argument is worth having.

**Proposition 4.2.** $\operatorname{range}(A^{\top}A) = \operatorname{range}(A^{\top})$ and $\operatorname{null}(A^{\top}A) = \operatorname{null}(A)$. Consequently $A^{\top}A\theta = A^{\top}B$ is consistent for every $B$.

*Proof.* If $A\theta = 0$ then $A^{\top}A\theta = 0$. Conversely if $A^{\top}A\theta = 0$ then $\|A\theta\|_2^2 = \theta^{\top}A^{\top}A\theta = 0$, so $A\theta = 0$; the null spaces agree. By rank-nullity (opt01 Theorem 1), $\operatorname{rank}(A^{\top}A) = n - \dim\operatorname{null}(A) = \operatorname{rank}(A) = \operatorname{rank}(A^{\top})$. Since $\operatorname{range}(A^{\top}A)\subseteq\operatorname{range}(A^{\top})$ trivially and the dimensions match, they are equal. Finally $A^{\top}B\in\operatorname{range}(A^{\top}) = \operatorname{range}(A^{\top}A)$. **End of proof.**

### 4.4 When $A$ has full column rank

If $r = n$ then $\operatorname{null}(A^{\top}A) = \operatorname{null}(A) = \{0\}$ and $A^{\top}A\in\mathbb{R}^{n\times n}$ is invertible, giving the familiar $\theta^\star = (A^{\top}A)^{-1}A^{\top}B$. This agrees with Theorem 1 because $(A^{\top}A)^{-1}A^{\top} = A^{\dagger}$ in that case (opt01 Section 5.5): with $V_c$ square orthogonal, $A^{\top}A = V_c\Sigma_c^2V_c^{\top}$ and $(A^{\top}A)^{-1}A^{\top} = V_c\Sigma_c^{-2}V_c^{\top}V_c\Sigma_cU_c^{\top} = V_c\Sigma_c^{-1}U_c^{\top}$. On the running example $A^{\top}A = \operatorname{diag}(3,2)$ is invertible, so $\theta^\star = \operatorname{diag}(\tfrac13,\tfrac12)(4,3) = (\tfrac43,\tfrac32)$. Checked, and agreeing with the SVD route as it must.

Full column rank requires $N \geq n$: at least as many examples as features. When $N < n$, the overparametrized regime, which is the normal one in deep learning, $A^{\top}A$ is *never* invertible, infinitely many $\theta$ achieve zero training error, and $A^{\dagger}B$ is the minimum-norm interpolant. Section 9.5 and reference [13] pick that thread up.

### 4.5 A caution the lecture omits: never actually form $A^{\top}A$

The normal equations are the right *theory* and the wrong *algorithm*. For $A$ of full column rank the 2-norm condition number is $\kappa_2(A) = \sigma_1/\sigma_n$, and since the singular values of $A^{\top}A$ are the $\sigma_i^2$,

$ \kappa_2(A^{\top}A) = \kappa_2(A)^2 . $

Forming $A^{\top}A$ therefore squares the sensitivity to rounding: an $A$ with $\kappa_2 = 10^{8}$, unremarkable for polynomial or nearly collinear features, yields a Gram matrix numerically singular in double precision. The standard remedy is to work with $A$ directly: compute a thin QR factorization $A = QR$ and solve the triangular system $R\theta = Q^{\top}B$, whose error growth is governed by $\kappa_2(A)$ and not its square; or use the SVD, which additionally handles rank deficiency. Trefethen and Bau [15, Lectures 11, 18-19] give the full comparison. This is why library routines such as `numpy.linalg.lstsq` and LAPACK's `gelsd` call an SVD or QR rather than inverting a Gram matrix, and it is a second, purely numerical reason ridge helps: adding $\lambda I$ moves $\sigma_i^2$ to $\sigma_i^2+\lambda$, capping the condition number at $(\sigma_1^2+\lambda)/\lambda$.

## 5 What Kind of Estimator Is $\theta^\star$?

Least squares is treated in the lecture as a deterministic optimization problem, which it is. But every claim about "fitting well" presupposes a data-generating story, and two classical results say precisely how good $\theta^\star$ is under one. Both are omitted from the lecture; both are one paragraph.

Throughout this section: $B = A\theta_0 + \varepsilon$ with $A$ deterministic of full column rank, $\mathbb{E}[\varepsilon] = 0$ and $\operatorname{Cov}(\varepsilon) = \sigma^2I_N$.

### 5.1 Least squares is the Gaussian MLE

**Proposition 5.1.** If moreover $\varepsilon\sim\mathcal{N}(0,\sigma^2I_N)$, then the maximum-likelihood estimate of $\theta$ is exactly $\operatorname*{argmin}_\theta\|A\theta-B\|_2^2$.

*Proof.* The log-likelihood is $\log p(B\mid\theta) = -\tfrac{N}{2}\log(2\pi\sigma^2) - \tfrac{1}{2\sigma^2}\|B - A\theta\|_2^2$. Only the last term depends on $\theta$, and maximizing it is minimizing $\|A\theta - B\|_2^2$. **End of proof.**

So squared loss is not an aesthetic choice; it is a distributional assumption in disguise. Heavier-tailed noise makes a different loss the MLE: Laplace noise gives $\ell_1$, which is why $\ell_1$ regression is the robust one.

### 5.2 Gauss-Markov: $\theta^\star$ is BLUE

Unbiasedness first: $\mathbb{E}[\theta^\star] = (A^{\top}A)^{-1}A^{\top}\mathbb{E}[B] = (A^{\top}A)^{-1}A^{\top}A\theta_0 = \theta_0$, and $\operatorname{Cov}(\theta^\star) = \sigma^2(A^{\top}A)^{-1}$ by the rule $\operatorname{Cov}(CB) = C\operatorname{Cov}(B)C^{\top}$ with $C = (A^{\top}A)^{-1}A^{\top}$.

**Theorem (Gauss-Markov).** Among all estimators of the form $\tilde\theta = CB$ that are unbiased for every $\theta_0$, the least-squares estimator has the smallest covariance in the Loewner order: $\operatorname{Cov}(\tilde\theta) - \operatorname{Cov}(\theta^\star)\succeq 0$.

*Proof.* Unbiasedness for every $\theta_0$ means $CA\theta_0 = \theta_0$ for all $\theta_0$, that is $CA = I_n$. Write $C = (A^{\top}A)^{-1}A^{\top} + D$; then $CA = I + DA$, so $DA = 0$. Hence

$ \operatorname{Cov}(\tilde\theta) = \sigma^2CC^{\top} = \sigma^2\big[(A^{\top}A)^{-1} + (A^{\top}A)^{-1}A^{\top}D^{\top} + DA(A^{\top}A)^{-1} + DD^{\top}\big] = \sigma^2(A^{\top}A)^{-1} + \sigma^2DD^{\top}, $

the two cross terms vanishing because $DA = 0$ and its transpose $A^{\top}D^{\top} = 0$. Since $DD^{\top}\succeq0$ always, the difference is positive semidefinite. **End of proof.**

Read the hypotheses carefully, because Section 9 violates one of them on purpose. Gauss-Markov optimizes only over *linear* and *unbiased* estimators. Ridge is linear but biased, so it is not a competitor, and Hoerl-Kennard (Theorem 9.4) shows that dropping unbiasedness strictly improves mean squared error. The word "best" in BLUE is a statement about a restricted class, not about the problem.

## 6 Feature Maps: Nonlinear Fits from a Linear Solver

### 6.1 The move

Replace $\mathbf{x}$ by $\phi(\mathbf{x}) \in \mathbb{R}^d$ and fit $f_\theta(\mathbf{x}) = \theta^{\top}\phi(\mathbf{x})$. The design matrix becomes $\Phi$, whose $i$-th row is $\phi(\mathbf{x}^{(i)})^{\top}$, and *every result above applies verbatim* with $A$ replaced by $\Phi$, because not one of the proofs used any structure of $A$'s entries. The model is nonlinear in $\mathbf{x}$ and linear in $\theta$; the solver only ever sees the second. This is the single most-reused idea in the course: it is what makes kernel methods, polynomial regression, random features, and the final linear layer of a network all the same computation.

### 6.2 "More features never hurt", proved, and its catch

**Proposition 6.1.** Let $\Phi_1 \in\mathbb{R}^{N\times d_1}$ and let $\Phi_2$ be $\Phi_1$ with extra feature columns $\Psi$ appended on the right. Then $\min_{\theta}\|\Phi_2\theta - B\|_2^2 \leq \min_{\theta}\|\Phi_1\theta - B\|_2^2$.

*Proof.* $\operatorname{range}(\Phi_1)\subseteq\operatorname{range}(\Phi_2)$, since any $\Phi_1\theta$ equals $\Phi_2$ applied to the vector $\theta$ padded with zeros. A minimum over a larger set is no larger. **End of proof.**

So the *training* error is monotone non-increasing in the feature set. That is a theorem, not a heuristic. The catch, flagged in one line in the lecture and developed in Sections 8.5 and 9: *test* error is not monotone. Proposition 6.1 is exactly the statement that empirical risk minimization cannot be used to choose $d$; adding features always looks better by the criterion being optimized. This is the structural reason model selection needs a held-out set or a penalty.

### 6.3 The parabola example, and why it is exact

With $\phi(x) = (1,x,x^2)$ and the running data $x = -1,0,1$, $y = 0,1,3$, the design matrix $\Phi$ has first row $(1, -1, 1)$, second row $(1, 0, 0)$ and third row $(1, 1, 1)$, and its determinant is

$ \det\Phi = \prod_{i < j}(x_j - x_i) = (0-(-1))(1-(-1))(1-0) = 2 \neq 0 . $

Solving $\Phi\theta = B$ exactly: $\theta_0 = 1$ from row 2; rows 1 and 3 give $\theta_0 - \theta_1+\theta_2 = 0$ and $\theta_0+\theta_1+\theta_2 = 3$, so $\theta_1 = \tfrac32$ and $\theta_2 = \tfrac12$. Thus $f(x) = 1 + \tfrac32x+\tfrac12x^2$, and the fit is exact: $f(-1) = 1-\tfrac32+\tfrac12 = 0$, $f(0) = 1$, $f(1) = 1+\tfrac32+\tfrac12 = 3$. All checked. Zero training error, versus $\mathrm{SSE} = \tfrac16$ for the line.

The elimination makes this look like arithmetic luck. It is not.

**Proposition 6.2 (Vandermonde).** For nodes $x_1,\dots,x_m$, the $m\times m$ matrix with entries $V_{ij} = x_i^{\,j-1}$ has $\det V = \prod_{i < j}(x_j - x_i)$. Hence $V$ is invertible if and only if the nodes are distinct, and there is then exactly one polynomial of degree $m-1$ through any $m$ prescribed values.

*Proof sketch.* Regard $\det V$ as a polynomial in $x_m$ of degree $m-1$; it vanishes whenever $x_m = x_i$ for some $i < m$, because then two rows are equal, so it equals $c\prod_{i < m}(x_m-x_i)$ with $c$ the coefficient of $x_m^{m-1}$, which by cofactor expansion is the Vandermonde determinant on the first $m-1$ nodes. Induct. **End of proof.**

So a polynomial of degree $N-1$ *always* interpolates $N$ points with distinct $x$-values, and the exactness of this parabola is a fact about $N = 3$, not about this data. That is precisely why it is not evidence that the parabola is a better model, a point the lecture makes next and this proposition explains.

### 6.4 Where feature maps stop

Two limits noted in passing, worth naming. *Cost:* full degree-$p$ polynomial features in $n$ variables number $\binom{n+p}{p}$; for $n = 100$ and $p = 3$ that is $176{,}851$, and the map is exponential in $p$. Kernel methods dodge the explicit map by working with the $N\times N$ Gram matrix $K_{ij} = \langle\phi(\mathbf{x}^{(i)}),\phi(\mathbf{x}^{(j)})\rangle$, trading $\mathcal{O}(Nd^2)$ for $\mathcal{O}(N^3)$, which is good when $d \gg N$ and useless when $N$ is in the millions. *Design:* $\phi$ must still be chosen by hand. The one-sentence summary of why the rest of the course exists: deep learning replaces the hand-designed $\phi$ with a learned one, at the cost of every closed form in this lecture.

## 7 Multiple Outputs

With $y^{(i)}\in\mathbb{R}^m$, stack the labels into $B\in\mathbb{R}^{N\times m}$ and the parameters into $\Theta\in\mathbb{R}^{n\times m}$, and measure the miss in Frobenius norm.

**Proposition 7.1.** The problem $\operatorname*{argmin}_{\Theta}\|A\Theta - B\|_F^2$ has minimum-norm solution $\Theta^\star = A^{\dagger}B$, obtained column by column.

*Proof.* By definition of the Frobenius norm as the sum of squared entries, grouped by column, $\|A\Theta - B\|_F^2 = \sum_{k=1}^{m}\|A\Theta_{:,k} - B_{:,k}\|_2^2$. The $k$-th summand involves only the $k$-th column of $\Theta$, so the objective separates into $m$ independent least-squares problems; apply Theorem 1 to each, giving $\Theta^\star_{:,k} = A^{\dagger}B_{:,k}$, that is $\Theta^\star = A^{\dagger}B$. Minimality of $\|\Theta\|_F$ follows since each column is separately of least norm. **End of proof.**

The practical content: the expensive object is the factorization of $A$, and it does not depend on $B$. One SVD, or one QR, serves all $m$ outputs, and serves any future $B$ as well; refitting with new labels is a matrix multiply. Note also that the outputs do not interact at all under Frobenius loss. If you want them coupled, say by shared low-rank structure across tasks, you must change the objective, for instance by penalizing $\|\Theta\|_*$, which is opt01 Section 6.5 and the multi-task and LoRA connection.

## 8 Empirical Risk Minimization

### 8.1 The framework

Assume $(X,Y)\sim P$ independently and identically distributed, fix a loss $\ell$ and a function class $\mathcal{F}$. The *risk* and the *empirical risk* are

$ R[f] = \mathbb{E}_{(X,Y)\sim P}\big[\ell(f(X),Y)\big], \qquad \hat R[f] = \frac1N\sum_{i=1}^{N}\ell\big(f(\mathbf{x}^{(i)}),y^{(i)}\big), $

and empirical risk minimization returns $\hat f \in \operatorname*{argmin}_{f\in\mathcal{F}}\hat R[f]$. Least squares is the instance $\ell(\hat y,y) = (\hat y - y)^2$ with $\mathcal{F} = \{\theta^{\top}\mathbf{x}\}$, and the point is that this lecture has been doing empirical risk minimization all along, with a class so small that the argmin has a formula.

### 8.2 The Bayes predictor for squared loss

The lecture cites this to Lecture 7 (prob07); here is the proof, since the whole narrative rests on knowing what $R$ is trying to reach.

**Theorem 8.1.** Over *all* measurable $f$ with $\mathbb{E}[f(X)^2] < \infty$, the risk $R[f] = \mathbb{E}[(f(X)-Y)^2]$ is minimized by $f^\star(\mathbf{x}) = \mathbb{E}[Y\mid X=\mathbf{x}]$, and $R^\star = R[f^\star] = \mathbb{E}\big[\operatorname{Var}(Y\mid X)\big]$.

*Proof.* Condition on $X$ and add and subtract $f^\star(X)$:

$ \mathbb{E}\big[(f(X)-Y)^2\,\big|\,X\big] = \mathbb{E}\big[(Y - f^\star(X))^2\,\big|\,X\big] + 2\big(f^\star(X)-f(X)\big)\,\mathbb{E}\big[Y-f^\star(X)\,\big|\,X\big] + \big(f^\star(X)-f(X)\big)^2 . $

The cross term vanishes because $\mathbb{E}[Y\mid X] = f^\star(X)$ by definition, and $f$ and $f^\star$ are $X$-measurable so they factor out of the conditional expectation. Taking expectations, $R[f] = \mathbb{E}[\operatorname{Var}(Y\mid X)] + \mathbb{E}[(f^\star(X)-f(X))^2] \geq \mathbb{E}[\operatorname{Var}(Y\mid X)]$, with equality if and only if $f = f^\star$ almost surely. **End of proof.**

Two consequences. First, $R^\star > 0$ in general: the *noise floor* is not a modelling failure, and driving training error below it is by definition fitting noise. Second, the identity $R[f] = R^\star + \mathbb{E}[(f - f^\star)^2]$ says excess risk is exactly squared $L^2(P)$ distance to the conditional mean, the cleanest justification for the geometric language of Section 4.

### 8.3 Why $\hat R$ at all

$R$ is unavailable: it is an expectation under the unknown $P$. What we have is a sample, and for each *fixed* $f$ the strong law gives $\hat R[f]\to R[f]$ almost surely, with $\mathbb{E}[\hat R[f]] = R[f]$ exactly. So $\hat R$ is an unbiased and consistent estimate of $R$, per function.

### 8.4 The gap in "minimize $\hat R$ and hope $R$ follows"

That phrasing is honest but hides the actual difficulty, and it is worth being precise about it because it is the reason statistical learning theory exists. Pointwise convergence is *not enough*: $\hat f$ is chosen using the data, so $\hat R[\hat f]$ is *not* an unbiased estimate of $R[\hat f]$. The same sample that picks the function then grades it, and $\hat f$ is precisely the function that looks best on this sample. Concretely, with $\mathcal{F}$ all measurable functions, take $\hat f$ to be $y^{(i)}$ at each $\mathbf{x}^{(i)}$ and $0$ elsewhere: then $\hat R[\hat f] = 0$ while $R[\hat f]$ is as bad as it gets. Nothing in the law of large numbers is violated; the law was never applied to a data-dependent $f$.

What repairs it is *uniform* convergence over $\mathcal{F}$.

**Proposition 8.2.** Let $\Delta := \sup_{f\in\mathcal{F}}\big|\hat R[f]-R[f]\big|$ and let $\hat f$ minimize $\hat R$ over $\mathcal{F}$. Then

$ R[\hat f] \;-\; \inf_{f\in\mathcal{F}} R[f] \;\leq\; 2\Delta . $

*Proof.* Let $f_\varepsilon\in\mathcal{F}$ satisfy $R[f_\varepsilon]\leq\inf_{\mathcal F}R+\varepsilon$. Then $R[\hat f]\leq \hat R[\hat f]+\Delta \leq \hat R[f_\varepsilon]+\Delta\leq R[f_\varepsilon]+2\Delta \leq \inf_{\mathcal F}R + 2\Delta+\varepsilon$, the second inequality by optimality of $\hat f$ for $\hat R$. Let $\varepsilon$ decrease to $0$. **End of proof.**

So empirical risk minimization is sound exactly to the extent that $\Delta$ is small, and $\Delta$ is a property of $\mathcal{F}$, not of the algorithm. Bounding it is what VC dimension and Rademacher complexity do [8, 9]: for a class of Rademacher complexity $\mathfrak{R}_N(\mathcal{F})$ and bounded loss, $\mathbb{E}\Delta \leq 2\mathfrak{R}_N(\mathcal{F})$, which for linear predictors with $\|\theta\|\leq b$ and $\|\mathbf{x}\|\leq c$ is $\mathcal{O}(bc/\sqrt N)$. Note the norm bound, which is the theoretical shadow of ridge. Adding the approximation term gives the decomposition drawn in the lecture as two arrows:

$ R[\hat f]-R^\star \;=\; \Big(\inf_{f\in\mathcal{F}}R[f]-R^\star\Big) \;+\; \Big(R[\hat f]-\inf_{f\in\mathcal{F}}R[f]\Big) . $

The left-hand side is the excess risk. The first term on the right is the *approximation* error, large when $\mathcal{F}$ is too small; the second is the *estimation* error, bounded by $2\Delta$. Enlarging $\mathcal{F}$ drives the first term down and the second up. That trade-off is the whole of model selection, and it is why Proposition 6.1, "more features never hurt", is about the wrong quantity.

### 8.5 When ERM misleads, and the modern caveat

The failure list given in the lecture is right: too rich an $\mathcal{F}$ (memorization), tiny $N$, distribution shift (so that $\hat R$ estimates the wrong $R$), and a loss that is not what you care about (squared error under an outlier-ridden $P$, or accuracy optimized through cross-entropy). To these should be added the observation that classical uniform-convergence bounds are *vacuous* for modern networks: Zhang and coauthors [10] showed a standard architecture can fit random labels on CIFAR-10 to zero training error, so its capacity term admits no useful bound, and yet the same architecture generalizes on real labels. And the "more capacity is worse past the interpolation point" picture is itself incomplete: *double descent* [11] finds test error rising to a peak at $d\approx N$ and then *falling again* as $d$ grows past it, with the minimum-norm interpolant $A^{\dagger}B$, Theorem 1's own answer, as the object being analyzed [12, 13]. The classical U-shaped curve is the left half of the picture; it is correct as far as it goes, and the course-level honest statement is that a complete theory is not settled.

## 9 Ridge Regression

### 9.1 The objective

$ J_\lambda(\theta) \;=\; \tfrac12\|A\theta - B\|_2^2 \;+\; \tfrac{\lambda}{2}\|\theta\|_2^2, \qquad \lambda > 0 . $

Three separate motivations converge on this one formula, and it is worth keeping them distinct because they suggest different ways to choose $\lambda$.

- *Algebraic.* $A^{\top}A$ may be singular, or nearly so; adding $\lambda I$ makes it invertible and caps the condition number (Section 4.5). This is Tikhonov's motivation [3] and needs no probability at all.
- *Statistical.* Trading a little bias for a lot of variance strictly reduces mean squared error (Theorem 9.4).
- *Bayesian.* It is MAP estimation under a Gaussian prior, with $\lambda$ pinned to the noise-to-prior variance ratio (Section 9.6).

### 9.2 Theorem 3

**Lemma 9.1.** For $\lambda > 0$, the matrix $A^{\top}A + \lambda I$ is symmetric positive definite, hence invertible.

*Proof.* Symmetry is clear. For $\theta \neq 0$, $\theta^{\top}(A^{\top}A+\lambda I)\theta = \|A\theta\|_2^2 + \lambda\|\theta\|_2^2 \geq \lambda\|\theta\|_2^2 > 0$. A positive-definite matrix has trivial null space, since $M\theta = 0$ forces $\theta^{\top}M\theta = 0$ and hence $\theta = 0$, so it is invertible. Note this holds for *every* $A$, with no rank assumption. **End of proof.**

**Theorem 3.** For $\lambda > 0$, $J_\lambda$ has the unique minimizer $\theta^\star_\lambda = (A^{\top}A+\lambda I)^{-1}A^{\top}B$.

*Proof.* Write $M = A^{\top}A+\lambda I$. Expanding exactly as in Theorem 2, for any $\theta$ and $h$,

$ J_\lambda(\theta + h) \;=\; J_\lambda(\theta) \;+\; h^{\top}\big(M\theta - A^{\top}B\big) \;+\; \tfrac12 h^{\top}Mh . $

Take $\theta = \theta^\star_\lambda = M^{-1}A^{\top}B$, which exists by Lemma 9.1; the linear term vanishes and $J_\lambda(\theta^\star_\lambda + h) = J_\lambda(\theta^\star_\lambda) + \tfrac12h^{\top}Mh > J_\lambda(\theta^\star_\lambda)$ for every $h\neq0$, by positive definiteness. So $\theta^\star_\lambda$ is a minimizer and it is the only one. **End of proof.**

Compare with Theorem 1: uniqueness there needed $r = n$; here it is free for any $\lambda > 0$. The regularizer buys strict convexity, and strict convexity is exactly what makes the argmin a point rather than a set.

### 9.3 The running example

$A^{\top}A + \lambda I = \operatorname{diag}(3+\lambda,\,2+\lambda)$, so

$ \theta^\star_\lambda = \Big(\frac{4}{3+\lambda},\ \frac{3}{2+\lambda}\Big) . $

Check: $\lambda = 0$ gives $(\tfrac43,\tfrac32)$, Theorem 1's answer; $\lambda = 1$ gives $(1,1)$; $\lambda = 4$ gives $(\tfrac47,\tfrac12)$; and $\lambda\to\infty$ gives $(0,0)$, as it must. All checked. Both coordinates shrink monotonically, and the shrinkage is *relatively faster where the corresponding $\sigma_i$ is smaller*: here $\sigma_2^2 = 2 < 3 = \sigma_1^2$, so the slope coordinate is damped more aggressively at equal $\lambda$. At $\lambda = 1$ the slope has lost $\tfrac13$ of its value against $\tfrac14$ for the intercept. That is the general rule, and Proposition 9.2 is why.

### 9.4 What ridge does in the SVD basis

**Proposition 9.2 (shrinkage).** With $A = U_c\Sigma_cV_c^{\top}$ of rank $r$ and $\lambda > 0$,

$ \theta^\star_\lambda \;=\; \sum_{i=1}^{r}\frac{\sigma_i}{\sigma_i^2+\lambda}\,\big(u_i^{\top}B\big)\,v_i, $

to be compared with

$ A^{\dagger}B \;=\; \sum_{i=1}^{r}\frac{1}{\sigma_i}\big(u_i^{\top}B\big)\,v_i . $

*Proof.* Complete $V_c$ to an orthogonal $V \in\mathbb{R}^{n\times n}$ whose first $r$ columns are those of $V_c$ (Section 3.2, Step 1, applied on the other side). Then $A^{\top}A = V\Lambda V^{\top}$ with $\Lambda = \operatorname{diag}(\sigma_1^2,\dots,\sigma_r^2,0,\dots,0)$, so

$ (A^{\top}A+\lambda I)^{-1} = V(\Lambda + \lambda I)^{-1}V^{\top}, $

using $I = VV^{\top}$ and the fact that inverting a matrix conjugated by an orthogonal matrix inverts the middle factor. Multiply by $A^{\top} = V_c\Sigma_cU_c^{\top}$ and use that $V^{\top}V_c$ is the $n\times r$ matrix whose top $r\times r$ block is $I_r$ and whose remaining rows are zero, so that only the first $r$ diagonal entries survive:

$ (A^{\top}A+\lambda I)^{-1}A^{\top} = V_c\,\operatorname{diag}\!\Big(\tfrac{\sigma_i}{\sigma_i^2+\lambda}\Big)\,U_c^{\top}. $

Applying it to $B$ gives the stated sum. **End of proof.**

So ridge replaces the filter factor $1/\sigma_i$ by $\sigma_i/(\sigma_i^2+\lambda) = \tfrac{1}{\sigma_i}\cdot\tfrac{\sigma_i^2}{\sigma_i^2+\lambda}$. The correction factor lies in $(0,1)$, near $1$ when $\sigma_i^2 \gg \lambda$ and near $\sigma_i^2/\lambda \approx 0$ when $\sigma_i^2\ll\lambda$. In words: *directions the data measures well pass through nearly untouched; directions it barely measures are suppressed.* That is the precise sense in which ridge is a smooth version of truncating small singular values, and it explains the algebraic motivation quantitatively. The unregularized $1/\sigma_i$ amplifies whatever noise lands along $u_i$ by a factor that blows up as $\sigma_i\to0$, while $\sigma_i/(\sigma_i^2+\lambda)$ is bounded by $1/(2\sqrt\lambda)$ for every $\sigma_i$, by the arithmetic-geometric mean inequality.

It also gives the standard summary statistic, the *effective degrees of freedom* [7, Section 3.4.1]. The ridge fit is $\hat B = A\theta^\star_\lambda = HB$ with $H = U_c\operatorname{diag}(\sigma_i^2/(\sigma_i^2+\lambda))U_c^{\top}$, so

$ \mathrm{df}(\lambda) = \operatorname{tr}(H) = \sum_{i=1}^{r}\frac{\sigma_i^2}{\sigma_i^2+\lambda}, $

which decreases from $r$ at $\lambda = 0$ to $0$ as $\lambda\to\infty$: a continuous model-complexity dial, where subset selection offers only integers. On the running example $\mathrm{df}(1) = \tfrac34+\tfrac23 = \tfrac{17}{12}\approx1.42$ out of $2$.

### 9.5 The limit $\lambda\to0^{+}$

**Proposition 9.3.** $\lim_{\lambda\to0^{+}}\theta^\star_\lambda = A^{\dagger}B$, for every $A$, including rank-deficient $A$.

*Proof.* In Proposition 9.2 the sum runs over $i \leq r$ only, so every $\sigma_i > 0$ and $\sigma_i/(\sigma_i^2+\lambda)\to1/\sigma_i$ as $\lambda\to0^{+}$; the sum is finite, so the limit passes term by term. **End of proof.**

This is a genuinely informative fact, and the lecture states only the invertible case. Even when $J$ has infinitely many minimizers, the ridge path selects one particular point in the limit, and it is $A^{\dagger}B$, the *minimum-norm* one. The least-norm tie-break of Theorem 1 is therefore not an arbitrary convention: it is what vanishing $\ell_2$ regularization picks out. The same phenomenon reappears for gradient descent started from the origin (opt03) and is the object of study in the interpolation literature [12, 13]. Note also that the convergence is not uniform in $A$, consistent with the map $A\mapsto A^{\dagger}$ being discontinuous (opt01 Section 5.6).

### 9.6 Ridge as MAP estimation

**Proposition.** Let $B\mid\theta \sim \mathcal{N}(A\theta,\sigma^2I_N)$ and put the prior $\theta\sim\mathcal{N}(0,\tau^2I_n)$. Then the posterior mode is $\theta^\star_\lambda$ with $\lambda = \sigma^2/\tau^2$.

*Proof.* By Bayes, $-\log p(\theta\mid B) = \tfrac{1}{2\sigma^2}\|A\theta - B\|_2^2 + \tfrac{1}{2\tau^2}\|\theta\|_2^2 + \text{const}$. Multiplying by $\sigma^2 > 0$ (Section 2.2) leaves

$ \tfrac12\|A\theta-B\|_2^2 + \tfrac{\sigma^2}{2\tau^2}\|\theta\|_2^2 = J_\lambda(\theta), \qquad \lambda = \frac{\sigma^2}{\tau^2}. $

**End of proof.**

The constant is the point. $\lambda$ is not a free knob but a ratio: large noise or a tight prior means heavy regularization, and a diffuse prior, $\tau\to\infty$, recovers least squares. Since $\sigma^2$ and $\tau^2$ are unknown in practice, $\lambda$ is chosen by cross-validation. For ridge specifically there is a closed-form leave-one-out shortcut and its rotation-invariant cousin, generalized cross-validation [6], both computable from one SVD across the whole grid of $\lambda$ values, since Proposition 9.2 gives every $\theta^\star_\lambda$ from the same factorization.

Interpreting the same objective as a constrained problem, minimize $\|A\theta-B\|_2^2$ subject to $\|\theta\|_2 \leq t$, gives the geometric picture in which the round $\ell_2$ ball generically touches the elliptical contours of the objective at a point away from any axis. Swapping in the $\ell_1$ ball, whose corners lie on the axes, is the lasso [14], and that is what makes it select variables. Ridge never sets a coefficient exactly to zero, as Proposition 9.2 makes plain, since every filter factor is strictly positive.

### 9.7 Bias, variance, and a theorem the lecture states as a picture

Keep the model of Section 5. Ridge is biased: $\mathbb{E}[\theta^\star_\lambda] = (A^{\top}A+\lambda I)^{-1}A^{\top}A\,\theta_0 \neq \theta_0$ for $\lambda > 0$. Gauss-Markov therefore does not apply, and that is the opening rather than a defect.

Take $A$ of full column rank, write $a_i = v_i^{\top}\theta_0$ and $\eta_i = u_i^{\top}\varepsilon$, so that $u_i^{\top}B = \sigma_ia_i+\eta_i$ with $\mathbb{E}\eta_i = 0$, $\operatorname{Var}\eta_i = \sigma^2$, and the $\eta_i$ uncorrelated because the $u_i$ are orthonormal. By Proposition 9.2 the $i$-th coordinate of $\theta^\star_\lambda$ in the $v$-basis is $\sigma_i(\sigma_ia_i+\eta_i)/(\sigma_i^2+\lambda)$, so its bias is $-\lambda a_i/(\sigma_i^2+\lambda)$ and its variance is $\sigma^2\sigma_i^2/(\sigma_i^2+\lambda)^2$. Summing, by Parseval since the $v_i$ are orthonormal,

$ \mathrm{MSE}(\lambda) \;=\; \mathbb{E}\big\|\theta^\star_\lambda - \theta_0\big\|_2^2 \;=\; \sum_{i=1}^{n}\frac{\lambda^2a_i^2 \;+\; \sigma^2\sigma_i^2}{(\sigma_i^2+\lambda)^2} . $

The numerator displays the trade-off in one line: the first term is squared bias, increasing in $\lambda$ from $0$; the second is variance, and the denominator drives it down. At $\lambda = 0$ this is $\mathrm{MSE}(0) = \sigma^2\sum_i\sigma_i^{-2} = \sigma^2\operatorname{tr}((A^{\top}A)^{-1})$, the Gauss-Markov value, which is enormous when any $\sigma_i$ is small.

**Theorem 9.4 (Hoerl-Kennard, 1970 [4]).** For every $\theta_0$ and every $\sigma^2 > 0$, $\mathrm{MSE}(\lambda) < \mathrm{MSE}(0)$ for all $\lambda$ with $0 < \lambda < 2\sigma^2/\max_i a_i^2$. In particular there always exists a $\lambda > 0$ whose ridge estimator beats least squares in mean squared error.

*Proof.* Compare term by term. Fix $i$ and set

$ D_i(\lambda) := \frac{\lambda^2a_i^2+\sigma^2\sigma_i^2}{(\sigma_i^2+\lambda)^2} - \frac{\sigma^2}{\sigma_i^2}. $

Multiplying by the positive quantity $\sigma_i^2(\sigma_i^2+\lambda)^2$ turns the sign question into

$ \sigma_i^2\lambda^2a_i^2 + \sigma^2\sigma_i^4 - \sigma^2(\sigma_i^2+\lambda)^2 \;=\; \sigma_i^2\lambda^2a_i^2 - 2\sigma^2\sigma_i^2\lambda - \sigma^2\lambda^2 \;=\; \lambda\Big[\lambda\big(\sigma_i^2a_i^2 - \sigma^2\big) - 2\sigma^2\sigma_i^2\Big]. $

For $\lambda > 0$ this is negative as soon as $\lambda(\sigma_i^2a_i^2-\sigma^2) < 2\sigma^2\sigma_i^2$, for which $\lambda\,\sigma_i^2a_i^2 < 2\sigma^2\sigma_i^2$, that is $\lambda < 2\sigma^2/a_i^2$, is sufficient. Requiring it for every $i$ gives the stated range, which is a nonempty interval whenever $\sigma^2 > 0$. Summing the strictly negative $D_i$ proves the claim. Equivalently, differentiating gives $\mathrm{MSE}'(\lambda) = 2\sum_i\sigma_i^2(\lambda a_i^2-\sigma^2)/(\sigma_i^2+\lambda)^3$, so $\mathrm{MSE}'(0) = -2\sigma^2\sum_i\sigma_i^{-4} < 0$: the curve leaves $\lambda = 0$ strictly downhill. **End of proof.**

The U-shaped curve drawn in the lecture is a picture of this theorem, and the sharp part is that the descent at $\lambda = 0$ is *unconditional*. Unbiasedness is never optimal here. The catch is equally sharp: the useful range $2\sigma^2/\max_ia_i^2$ depends on the unknown $\theta_0$ and $\sigma^2$, so the theorem guarantees a good $\lambda$ exists without telling you which, hence cross-validation. This is the same phenomenon as Stein's paradox and the James-Stein estimator [5]: in dimension at least $3$, shrinking a natural unbiased estimator toward a point dominates it everywhere.

### 9.8 Two cautions not raised in the lecture

- **The intercept is being penalized.** Written as $\lambda\|\theta\|_2^2$ over all coordinates, ridge shrinks $\theta_0$ too, visible in the running example where the intercept goes $\tfrac43$, then $1$, then $\tfrac47$. Standard practice excludes it: center $B$ and the feature columns, fit the slopes with a penalty, and recover the intercept as $\bar y$. Penalizing the intercept makes the fit depend on where the origin of $y$ sits, which is not a modelling assumption anyone intends.
- **Ridge is not scale-equivariant.** Least squares is: rescaling a feature column by $c$ rescales its coefficient by $1/c$ and leaves the fit unchanged. Ridge does not commute with that rescaling, because $\|\theta\|_2^2$ weights all coordinates equally, so measuring a length in millimetres instead of metres changes the answer. Features are therefore standardized to unit variance before ridge, always. The same remark applies to the lasso.

## 10 What the Lecture Leaves Out

1. **Weighted and generalized least squares.** If $\operatorname{Cov}(\varepsilon) = \Sigma \neq \sigma^2I$, the efficient estimator minimizes $(A\theta-B)^{\top}\Sigma^{-1}(A\theta-B)$; substituting $\Sigma^{-1/2}$ into the data reduces it to the ordinary case. Gauss-Markov is stated for the homoscedastic case only.
2. **Lasso and the elastic net.** Swapping $\|\theta\|_2^2$ for $\|\theta\|_1$ gives sparse solutions and no closed form; it is a convex program [17] solved by coordinate descent or proximal methods. The $\ell_1$ story is the direct sibling of opt01's nuclear norm, a convex surrogate for a counting objective, and it connects to opt03's proximal machinery.
3. **Choosing $\lambda$ in practice.** $K$-fold cross-validation, leave-one-out with the closed-form hat-matrix shortcut, and generalized cross-validation [6]; also the whole regularization path, computable at the cost of one SVD.
4. **Inference.** Standard errors, $t$- and $F$-tests, confidence and prediction intervals: everything that makes least squares a statistical procedure rather than a curve fit. Note that ridge's biasedness makes naive intervals invalid.
5. **Diagnostics and robustness.** Leverage $h_{ii}$, Cook's distance, and the fact that a single high-leverage outlier can move $\theta^\star$ without bound; Huber loss and $\ell_1$ regression as the fixes.
6. **Iterative solvers.** For $N$ or $n$ in the millions, neither the SVD, at $\mathcal{O}(Nn^2)$, nor the normal equations are affordable; LSQR, conjugate gradients on the normal equations, and sketching methods are [16, Chapters 5-6]. This is the bridge to opt03 and opt04, where the closed form is abandoned entirely.
7. **Nonlinear least squares.** An $f_\theta$ nonlinear in $\theta$ destroys every result here; Gauss-Newton and Levenberg-Marquardt recover local versions, and Levenberg-Marquardt's damping term is literally ridge applied to the linearized subproblem.

## 11 References

1. A.-M. Legendre, *Nouvelles methodes pour la determination des orbites des cometes*, Paris, 1805. First publication of the method of least squares. https://archive.org/details/nouvellesmthod00lege
2. C. F. Gauss, *Theoria Motus Corporum Coelestium*, 1809. Least squares with the Gaussian error law, and the priority claim to 1795. https://archive.org/details/theoriamotuscor00gausgoog
3. A. N. Tikhonov, "Solution of incorrectly formulated problems and the regularization method," *Soviet Math. Dokl.* 4 (1963), 1035-1038. The $\lambda I$ term for ill-posed inverse problems.
4. A. E. Hoerl and R. W. Kennard, "Ridge regression: biased estimation for nonorthogonal problems," *Technometrics* 12(1) (1970), 55-67. Theorem 9.4. doi:10.1080/00401706.1970.10488634, https://doi.org/10.1080/00401706.1970.10488634
5. W. James and C. Stein, "Estimation with quadratic loss," *Proc. Fourth Berkeley Symp.* 1 (1961), 361-379. Shrinkage dominates the unbiased estimator in dimension at least 3. https://projecteuclid.org/euclid.bsmsp/1200512173
6. G. H. Golub, M. Heath and G. Wahba, "Generalized cross-validation as a method for choosing a good ridge parameter," *Technometrics* 21(2) (1979), 215-223. doi:10.1080/00401706.1979.10489751, https://doi.org/10.1080/00401706.1979.10489751
7. T. Hastie, R. Tibshirani and J. Friedman, *The Elements of Statistical Learning*, 2nd ed., Springer, 2009. Chapter 3 for ridge, lasso and effective degrees of freedom; Chapter 7 for the bias-variance decomposition. https://hastie.su.domains/ElemStatLearn/
8. V. N. Vapnik, *The Nature of Statistical Learning Theory*, 2nd ed., Springer, 2000. Empirical risk minimization, uniform convergence, VC dimension. doi:10.1007/978-1-4757-3264-1, https://doi.org/10.1007/978-1-4757-3264-1
9. P. L. Bartlett and S. Mendelson, "Rademacher and Gaussian complexities: risk bounds and structural results," *JMLR* 3 (2002), 463-482. The modern form of the $\Delta$ bound in Proposition 8.2. https://www.jmlr.org/papers/v3/bartlett02a.html
10. C. Zhang, S. Bengio, M. Hardt, B. Recht and O. Vinyals, "Understanding deep learning requires rethinking generalization," ICLR 2017. arXiv:1611.03530, https://arxiv.org/abs/1611.03530
11. M. Belkin, D. Hsu, S. Ma and S. Mandal, "Reconciling modern machine learning practice and the bias-variance trade-off," *PNAS* 116(32) (2019). Double descent. arXiv:1812.11118, https://arxiv.org/abs/1812.11118
12. T. Hastie, A. Montanari, S. Rosset and R. J. Tibshirani, "Surprises in high-dimensional ridgeless least squares interpolation," *Ann. Statist.* 50(2) (2022). The $\lambda\to0^{+}$ limit of Section 9.5, analyzed. arXiv:1903.08560, https://arxiv.org/abs/1903.08560
13. P. L. Bartlett, P. M. Long, G. Lugosi and A. Tsigler, "Benign overfitting in linear regression," *PNAS* 117(48) (2020). When the minimum-norm interpolant $A^{\dagger}B$ generalizes. arXiv:1906.11300, https://arxiv.org/abs/1906.11300
14. R. Tibshirani, "Regression shrinkage and selection via the lasso," *JRSS-B* 58(1) (1996), 267-288. doi:10.1111/j.2517-6161.1996.tb02080.x, https://doi.org/10.1111/j.2517-6161.1996.tb02080.x
15. L. N. Trefethen and D. Bau III, *Numerical Linear Algebra*, SIAM, 1997. Lectures 11 and 18-19 for the conditioning argument of Section 4.5 and the QR and SVD routes. doi:10.1137/1.9780898719574, https://doi.org/10.1137/1.9780898719574
16. G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th ed., Johns Hopkins, 2013. Chapter 5 for least-squares algorithms, Chapter 6 for modified and regularized problems.
17. S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge, 2004. Section 1.2 and Chapter 4 for least squares as the model tractable problem; picked up in opt03. https://web.stanford.edu/~boyd/cvxbook/
18. Companion notes in this series, accessible Markdown editions: `../opt01-svd-lowrank/opt01-svd-lowrank-note.md` for the SVD, the pseudo-inverse and Eckart-Young-Mirsky, that is every linear-algebra fact used above; `../prob07-estimation/prob07-estimation-note.md` for conditional expectation and the Bayes predictor of Section 8.2; and, in the sequel, `../opt03-convexity-gd/opt03-convexity-gd-note.md` for what replaces the closed form when there is none.
