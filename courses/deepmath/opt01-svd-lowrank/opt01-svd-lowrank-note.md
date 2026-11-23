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
### 4. The Compression Question [S80]

#### 7.1 The problem and the candidate

Fix $A \in \mathbb{R}^{m \times n}$ of rank $r$ and an integer $k < r$. The problem is

$$ \min_{B \,:\, \operatorname{rank}(B) \,\leq\, k} \ \|A - B\| $$

for a unitarily invariant norm. The feasible set is *not* convex: $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$ both have rank $1$, but their midpoint $\tfrac12 I_2$ has rank $2$. So nothing from convex optimization applies, and yet the problem has a clean closed-form solution. That is the surprise.

The candidate is the **truncated SVD**

$$ A_k \;:=\; \sum_{i=1}^{k}\sigma_i u_i v_i^\top \;=\; U\Sigma_k V^\top, \qquad \Sigma_k = \operatorname{diag}(\sigma_1, \dots, \sigma_k, 0, \dots, 0), $$

which has rank exactly $k$, its nonzero singular values being $\sigma_1, \dots, \sigma_k$. Its errors are read off immediately from Theorems 6 and 7 applied to $A - A_k = \sum_{i > k}\sigma_i u_i v_i^\top$:

$$ \|A - A_k\|_2 = \sigma_{k+1}, \qquad \|A - A_k\|_F = \Big(\sum_{i > k}\sigma_i^2\Big)^{1/2}, \qquad \|A - A_k\|_* = \sum_{i > k}\sigma_i . $$

The theorem is that no other matrix of rank at most $k$ does better, in any of the three norms.
<!-- END S80 -->

<!-- BEGIN S12 -->
### 5. Definition -- Span & Range [S12]

#### 2.1 Span, independence, basis; dimension is well defined

**Definitions.** For $v_1, \dots, v_k \in \mathbb{R}^n$, $\operatorname{span}\{v_1, \dots, v_k\} = \{\sum_i \alpha_i v_i : \alpha_i \in \mathbb{R}\}$. The list is *linearly independent* if $\sum_i \alpha_i v_i = 0$ forces every $\alpha_i = 0$. A *subspace* $W \subseteq \mathbb{R}^n$ is a nonempty set closed under addition and scalar multiplication. A *basis* of $W$ is an independent list spanning $W$, and $\dim W$ is the length of a basis.

That last definition needs a theorem to be legitimate: two bases of the same subspace could a priori have different lengths.

**Lemma 2.1 (Steinitz exchange).** If $w_1, \dots, w_p$ are linearly independent and all lie in $\operatorname{span}\{v_1, \dots, v_q\}$, then $p \leq q$.

*Proof.* Induct on $p$, exchanging one vector at a time. Suppose after $j$ steps we have a spanning list consisting of $w_1, \dots, w_j$ together with $q - j$ of the $v$'s; this is true for $j = 0$. If $j < p$, write $w_{j+1}$ in that spanning list:

$$ w_{j+1} = \sum_{i \leq j} \alpha_i w_i + \sum_{\ell} \beta_\ell v_{i_\ell} . $$

Not every $\beta_\ell$ can vanish, or $w_{j+1}$ would be a combination of $w_1, \dots, w_j$, contradicting independence; in particular the list of remaining $v$'s is nonempty, which already forces $q - j \geq 1$, that is, $j < q$. Pick $\ell$ with $\beta_\ell \neq 0$, solve for $v_{i_\ell}$, and swap it out for $w_{j+1}$: the new list still spans. After $p$ steps we have used $p$ distinct $v$'s, so $p \leq q$. **End of proof.**

Applying the lemma in both directions to two bases of $W$ gives equal lengths, so $\dim W$ is well defined. The same lemma gives the two facts used repeatedly below: any independent list in $W$ has at most $\dim W$ elements and extends to a basis of $W$, and any spanning list contains a basis.

#### 2.2 Range, null space, rank

**Definitions.** For $A \in \mathbb{R}^{m \times n}$ with columns $a_1, \dots, a_n$: $\operatorname{range}(A) = \{Ax : x \in \mathbb{R}^n\} = \operatorname{span}\{a_1, \dots, a_n\} \subseteq \mathbb{R}^m$, using $Ax = \sum_i x_i a_i$; $\operatorname{null}(A) = \{x \in \mathbb{R}^n : Ax = 0\} \subseteq \mathbb{R}^n$; $\operatorname{row}(A) = \operatorname{range}(A^\top) \subseteq \mathbb{R}^n$; and $\operatorname{rank}(A) = \dim \operatorname{range}(A)$. Both $\operatorname{range}(A)$ and $\operatorname{null}(A)$ are subspaces, immediately from linearity of $x \mapsto Ax$.
<!-- END S12 -->

<!-- BEGIN S14 -->
### 6. Definition -- Rank [S14]

#### 2.2 Range, null space, rank (continued)

The parenthetical remark "row rank $=$ column rank" is a real theorem; here is the two-line proof.

**Proposition 2.2.** $\operatorname{rank}(A^\top) = \operatorname{rank}(A)$.

*Proof.* Let $r = \operatorname{rank}(A)$ and let $u_1, \dots, u_r$ be a basis of $\operatorname{range}(A)$; write $U_0 = [u_1 \cdots u_r] \in \mathbb{R}^{m \times r}$. Each column $a_j$ lies in $\operatorname{range}(A)$, so $a_j = U_0 c_j$ for some $c_j \in \mathbb{R}^r$; stacking these, $A = U_0 C$ with $C = [c_1 \cdots c_n] \in \mathbb{R}^{r \times n}$. Then $A^\top = C^\top U_0^\top$, so every column of $A^\top$ is a combination of the $r$ columns of $C^\top$, giving $\operatorname{rank}(A^\top) \leq r$. Applying the same bound to $A^\top$ in place of $A$ gives $\operatorname{rank}(A) \leq \operatorname{rank}(A^\top)$. **End of proof.**

The factorization $A = U_0 C$ produced in that proof is worth naming: **every rank-$r$ matrix is a product of an $m \times r$ and an $r \times n$ matrix**, that is, a sum of $r$ rank-one matrices. That is the abstract form of the recommender factorization $R = TG$ of Section 8, and the reason a rank-$r$ matrix costs $r(m+n)$ numbers rather than $mn$.
<!-- END S14 -->

<!-- BEGIN S13 -->
### 7. Worked -- a Collapsing Matrix [S13]
<!-- END S13 -->

<!-- BEGIN S16 -->
### 8. Definition -- Null Space [S16]
<!-- END S16 -->

<!-- BEGIN S18 -->
### 9. Theorem 1 -- Rank-Nullity [S18]

#### 2.4 Theorem 1 (rank-nullity), proved

**Theorem 1.** For $A \in \mathbb{R}^{m \times n}$, $\operatorname{rank}(A) + \dim \operatorname{null}(A) = n$, the number of *columns*.

*Proof.* Let $x_1, \dots, x_t$ be a basis of $\operatorname{null}(A)$ and extend it to a basis $x_1, \dots, x_t, y_1, \dots, y_s$ of $\mathbb{R}^n$, so $t + s = n$. It suffices to show that $Ay_1, \dots, Ay_s$ is a basis of $\operatorname{range}(A)$.

*Spanning.* Any $Ax$ with $x = \sum_i \alpha_i x_i + \sum_j \beta_j y_j$ satisfies $Ax = \sum_j \beta_j A y_j$, because $Ax_i = 0$.

*Independence.* If $\sum_j \beta_j A y_j = 0$ then $A(\sum_j \beta_j y_j) = 0$, so $\sum_j \beta_j y_j \in \operatorname{null}(A)$ and thus equals $\sum_i \alpha_i x_i$ for some $\alpha$. Then $\sum_j \beta_j y_j - \sum_i \alpha_i x_i = 0$ is a relation among basis vectors of $\mathbb{R}^n$, so every $\beta_j = 0$. Hence $\operatorname{rank}(A) = s = n - t$. **End of proof.**
<!-- END S18 -->

<!-- REGION P1a END -->

<!-- REGION P1b BEGIN -->

<!-- BEGIN S25 -->
### 10. Part 2: Measuring Error [S25]

**Message.** Part 2 chooses how to measure the size of the error matrix: worst-case stretch or total energy.
<!-- END S25 -->

<!-- BEGIN S27 -->
### 11. Definition -- Norm [S27]

#### 3.1 The axioms, and what follows from them

**Definition.** A function $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}$ is a *norm* if for all $x, y$ and all $\alpha \in \mathbb{R}$:

- (N1) $\|x + y\| \leq \|x\| + \|y\|$;
- (N2) $\|\alpha x\| = |\alpha| \, \|x\|$;
- (N3) $\|x\| = 0$ if and only if $x = 0$.

Nonnegativity is not an extra axiom -- it follows: $0 = \|x + (-x)\| \leq \|x\| + \|-x\| = 2\|x\|$ by (N1) and (N2). Two consequences are used later. The *reverse triangle inequality* $\big|\, \|x\| - \|y\| \,\big| \leq \|x - y\|$, obtained by applying (N1) to $x = (x - y) + y$ and symmetrically. And the fact that every norm on $\mathbb{R}^n$ is a continuous function, immediate from the reverse triangle inequality together with $\|x\| \leq \sum_i |x_i| \, \|e_i\|$. Continuity is what makes the maximum in the induced-norm definition of Section 6.1 attained rather than merely a supremum.
<!-- END S27 -->

<!-- BEGIN S28 -->
### 12. The $\ell_p$ Family [S28]

#### 3.2 The $\ell_p$ family is a family of norms, for $p \geq 1$

For $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$, axioms (N2) and (N3) are obvious. Axiom (N1), Minkowski's inequality, is not, and its standard proof runs through Holder's inequality, which is worth having explicitly because the Cauchy-Schwarz argument of lecture 11 is the case $p = 2$.

**Lemma 3.1 (Young).** For $a, b \geq 0$ and conjugate exponents $p, q > 1$ with $\tfrac1p + \tfrac1q = 1$,

$$ ab \leq \frac{a^p}{p} + \frac{b^q}{q} . $$

*Proof.* For $a, b > 0$ apply concavity of the logarithm -- Jensen's inequality from the lecture-1 note [20], at two points with weights $\tfrac1p$ and $\tfrac1q$ summing to $1$:

$$ \log\Big(\tfrac1p a^p + \tfrac1q b^q\Big) \geq \tfrac1p \log a^p + \tfrac1q \log b^q = \log(ab) ; $$

now exponentiate. If $a$ or $b$ is $0$ the inequality is trivial. **End of proof.**

**Lemma 3.2 (Holder).** $\sum_i |x_i y_i| \leq \|x\|_p \|y\|_q$ for conjugate $p, q$. For $p = q = 2$ this is Cauchy-Schwarz.

*Proof.* If either factor is $0$ both sides vanish. Otherwise put $a_i = |x_i| / \|x\|_p$ and $b_i = |y_i| / \|y\|_q$, and sum Young's inequality over $i$:

$$ \sum_i a_i b_i \leq \tfrac1p \sum_i a_i^p + \tfrac1q \sum_i b_i^q = \tfrac1p + \tfrac1q = 1 . $$

Multiply through by $\|x\|_p \|y\|_q$. **End of proof.**

**Lemma 3.3 (Minkowski).** $\|x + y\|_p \leq \|x\|_p + \|y\|_p$ for $p \geq 1$.

*Proof.* The case $p = 1$ is the scalar triangle inequality summed. For $p > 1$, with $q = p/(p-1)$,

$$ \|x+y\|_p^p \;\leq\; \sum_i |x_i| \, |x_i + y_i|^{p-1} + \sum_i |y_i| \, |x_i + y_i|^{p-1} , $$

and applying Holder to each of the two sums bounds this by

$$ \big(\|x\|_p + \|y\|_p\big) \Big( \sum_i |x_i + y_i|^{(p-1)q} \Big)^{1/q} . $$

Since $(p-1)q = p$, the last factor is $\|x+y\|_p^{p/q}$. If $\|x+y\|_p = 0$ we are done; otherwise divide by it and use $p - p/q = 1$. **End of proof.**

#### 3.3 Why $p \geq 1$: an explicit failure at $p < 1$

The lecture states the restriction; here is the witness. Take $p = \tfrac12$ and the vectors $x = (1,0)$ and $y = (0,1)$ in $\mathbb{R}^2$. Then $\|x\|_{1/2} = \|y\|_{1/2} = 1$, but $\|x + y\|_{1/2} = (1 + 1)^2 = 4 > 2$. So (N1) fails, decisively.

The quantity $\|x\|_0 := \#\{i : x_i \neq 0\}$, used in Sections 6 and 8 in the identity "rank $= \|\sigma\|_0$", is not a norm either: it violates (N2), since $\|2x\|_0 = \|x\|_0 \neq 2\|x\|_0$ in general. Calling these "the $\ell_{1/2}$ norm" and "the $\ell_0$ norm" is standard abuse of language. The passage from $\|\sigma\|_0$ to $\|\sigma\|_1$ in Section 8 is precisely the move from a non-norm to the nearest convex norm.

#### 3.4 $\ell_\infty$ as a limit, and the ordering

**Proposition 3.4.** $\|x\|_p \to \max_i |x_i| =: \|x\|_\infty$ as $p \to \infty$, and for every $x \in \mathbb{R}^n$,

$$ \|x\|_\infty \;\leq\; \|x\|_2 \;\leq\; \|x\|_1 \;\leq\; \sqrt{n}\, \|x\|_2 \;\leq\; n \, \|x\|_\infty . $$

*Proof.* Let $M = \|x\|_\infty$. Then $M^p \leq \sum_i |x_i|^p \leq n M^p$, so $M \leq \|x\|_p \leq n^{1/p} M$, and $n^{1/p} \to 1$. For the chain: $\|x\|_\infty^2 = \max_i x_i^2 \leq \sum_i x_i^2$ gives the first inequality; squaring $\|x\|_1$ gives $\sum_i x_i^2 + \sum_{i \neq j} |x_i||x_j| \geq \|x\|_2^2$, the second; Cauchy-Schwarz against the all-ones vector, $\sum_i |x_i| \cdot 1 \leq \sqrt n \|x\|_2$, the third; and $\|x\|_2^2 \leq n \|x\|_\infty^2$ the fourth. **End of proof.**
<!-- END S28 -->

<!-- BEGIN S29 -->
### 13. Worked -- One Vector, Three Norms [S29]

#### 3.4 $\ell_\infty$ as a limit, and the ordering (continued)

The worked example is $x = (3,4)$: $\|x\|_1 = 7$, $\|x\|_2 = 5$, $\|x\|_\infty = 4$, consistent with $4 \leq 5 \leq 7$. The same ordering reappears in Section 6.5 applied to the vector of singular values, where it becomes $\|A\|_2 \leq \|A\|_F \leq \|A\|_*$.
<!-- END S29 -->

<!-- BEGIN S30 -->
### 14. Unit Balls -- the Norms as Shapes [S30]
<!-- END S30 -->

<!-- BEGIN S31 -->
### 15. Definition -- Orthogonal Matrix [S31]

#### 3.5 Orthogonal matrices: the equivalent characterizations

**Proposition 3.5.** For *square* $U \in \mathbb{R}^{n \times n}$ the following are equivalent:

1. $U^\top U = I$;
2. $UU^\top = I$;
3. the columns of $U$ are orthonormal;
4. the rows of $U$ are orthonormal;
5. $\|Ux\|_2 = \|x\|_2$ for all $x$;
6. $(Ux)^\top(Uy) = x^\top y$ for all $x, y$.

*Proof.* Statement 1 is equivalent to statement 3 by the entry-wise reading of $U^\top U$, whose $(i,j)$ entry is $u_i^\top u_j$; likewise 2 is equivalent to 4.

For 1 implies 2: $U^\top U = I$ means $U^\top$ is a left inverse of the square matrix $U$; a square matrix with a left inverse is invertible, being injective and hence surjective by Theorem 1, and then $U^\top = U^\top(UU^{-1}) = (U^\top U)U^{-1} = U^{-1}$, so $UU^\top = I$. Symmetrically, 2 implies 1.

For 1 implies 6: $(Ux)^\top(Uy) = x^\top U^\top U y = x^\top y$. For 6 implies 5: take $y = x$. For 5 implies 6: use polarization, $x^\top y = \tfrac12(\|x+y\|^2 - \|x\|^2 - \|y\|^2)$. For 6 implies 1: $x^\top(U^\top U - I)y = 0$ for all $x, y$ forces the matrix $U^\top U - I$ to be $0$, taking $x = e_i$ and $y = e_j$. **End of proof.**

Squareness is essential, and the lecture flags why: the thin factor $U_c \in \mathbb{R}^{m \times r}$ of Section 4.4 satisfies $U_c^\top U_c = I_r$ but not $U_c U_c^\top = I_m$ when $r < m$ -- the proof that 1 implies 2 used a left inverse of a *square* matrix.

Two further standard facts. Orthogonal matrices form a group under multiplication: if $U^\top U = V^\top V = I$ then $(UV)^\top(UV) = V^\top U^\top U V = I$. And $\det U = \pm 1$, from $1 = \det I = \det(U^\top U) = (\det U)^2$; the value $+1$ is a rotation, and $-1$ a rotation composed with a reflection. The matrix $V$ appearing in the running example is $\tfrac{1}{\sqrt2}$ times the matrix with first row $(1, -1)$ and second row $(1, 1)$; its determinant is $\tfrac12(1 + 1) = 1$, so it is a genuine rotation, by $45$ degrees.
<!-- END S31 -->

<!-- BEGIN S33 -->
### 16. Theorem 4 -- Orthogonal Maps Preserve Length [S33]

#### 3.5 Orthogonal matrices: the equivalent characterizations (continued)

**Theorem 4.** If $U$ is orthogonal then $\|Ux\|_2 = \|x\|_2$ for all $x$. Conversely, a square $U$ preserving the $\ell_2$ norm is orthogonal.

*Proof.* Both directions are the equivalence of statements 1 and 5 in Proposition 3.5. **End of proof.**
<!-- END S33 -->

<!-- BEGIN S66 -->
### 17. Definition -- Induced (Operator) Norm [S66]

#### 6.1 Induced norms: definition, attainment, submultiplicativity

**Definition.** For a vector norm $\|\cdot\|_p$, the induced (operator) norm is

$$ \|A\|_p := \max_{\|x\|_p = 1} \|Ax\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p} . $$

The maximum is attained, not merely approached: $x \mapsto \|Ax\|_p$ is continuous by Section 3.1 and the unit sphere is compact. The two expressions agree by homogeneity, $\|A(x/\|x\|)\| = \|Ax\|/\|x\|$.

Induced norms satisfy the norm axioms -- (N1) from $\|(A+B)x\| \leq \|Ax\| + \|Bx\|$ pointwise, then maximizing; (N3) because $\|A\| = 0$ forces $Ae_i = 0$ for all $i$ -- and additionally the two properties that make them useful for error analysis:

$$ \|Ax\|_p \leq \|A\|_p \|x\|_p \quad \text{(consistency)}, \qquad \|AB\|_p \leq \|A\|_p \|B\|_p \quad \text{(submultiplicativity)}. $$

Consistency is the definition rescaled; submultiplicativity follows by applying it twice, $\|ABx\| \leq \|A\| \|Bx\| \leq \|A\| \|B\| \|x\|$, then maximizing over $\|x\| = 1$. Also $\|I\|_p = 1$ for every induced norm -- a property the Frobenius norm lacks, since $\|I_n\|_F = \sqrt n$, which is the first sign that $\|\cdot\|_F$ is not induced by any vector norm for $n > 1$.

#### 6.2 The $p = 1$ and $p = \infty$ formulas

Not covered in the lecture but standard, and useful as a contrast to how much harder $p = 2$ is:

$$ \|A\|_1 = \max_j \sum_i |a_{ij}| \quad \text{(largest absolute column sum)}, \qquad \|A\|_\infty = \max_i \sum_j |a_{ij}| \quad \text{(largest absolute row sum)}. $$

*Proof of the first.* $\|Ax\|_1 = \sum_i |\sum_j a_{ij}x_j| \leq \sum_j |x_j| \sum_i |a_{ij}| \leq (\max_j \sum_i |a_{ij}|)\|x\|_1$, with equality at $x = e_{j^\star}$ for the maximizing column. The second is the same argument transposed.

Both are read off the entries in $O(mn)$ time, whereas $\|A\|_2$ requires the SVD, which is $O(mn\min(m,n))$ -- the practical reason the Frobenius norm is often used as a cheap proxy.
<!-- END S66 -->

<!-- BEGIN S72 -->
### 18. Definition -- Frobenius Norm [S72]

#### 6.4 The Frobenius norm and Theorem 7

Define $\|A\|_F := (\sum_{i,j} a_{ij}^2)^{1/2}$: the Euclidean norm of the matrix read as a vector in $\mathbb{R}^{mn}$. Hence it is a norm for free, being $\ell_2$ under that identification, and it comes with an inner product $\langle A, B \rangle = \operatorname{tr}(A^\top B) = \sum_{i,j} a_{ij}b_{ij}$, so that $\|A\|_F^2 = \operatorname{tr}(A^\top A)$.
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
### 42. Candidate: Keep the $k$ Largest Layers [S81]

**Message.** Sort the singular values and keep the $k$ largest rank-one layers; this truncation $A_k$ is the natural candidate, not yet a proven optimum.

The SVD writes $A = \sum_{i=1}^r \sigma_i u_i v_i^\top$ as a sum of $r$ rank-one layers, each scaled by a singular value. Under a rank budget $k$ the obvious move is to keep the $k$ layers with the largest singular values and drop the rest. That gives $A_k = \sum_{i=1}^k \sigma_i u_i v_i^\top$.

The slide's display writes $A$ as one long sum. A brace under the first $k$ terms labels them as $A_k$, the kept part. A second brace under the remaining terms, printed in grey, labels them as discarded.

The layers $u_i v_i^\top$ are linearly independent, so $A_k$ has rank exactly $k$ and is inside the budget $\operatorname{rank} \leq k$. Whether some other rank-$k$ matrix does better is the question the rest of the part answers.

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

A recall box restates the SVD data of the worked matrix $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$: $\sigma_1 = 3\sqrt5$, $\sigma_2 = \sqrt5$, $u_1 = (1,3)^\top/\sqrt{10}$ and $v_1 = (1,1)^\top/\sqrt2$. Multiplying out the top layer gives $A_1$.

Both columns of $A_1$ are the same multiple of $u_1$, which is what rank one looks like on paper.

**Details.**

Multiplication:

$$A_1 = \sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}\sqrt2} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} = \frac{3\sqrt5}{\sqrt{20}} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} = \frac{3}{2} \begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} = \begin{bmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{bmatrix},$$

since $\sqrt{20} = 2\sqrt5$. Check: $\|A_1\|_F^2 = 2(1.5^2) + 2(4.5^2) = 4.5 + 40.5 = 45 = \sigma_1^2$.

Retained directions: $A_1$ maps $v_1$ to $\sigma_1 u_1$ and kills $v_2 = (-1,1)^\top/\sqrt2$. Its range is the line through $u_1$.

**Sources.**

Worked example and its SVD as computed earlier in this deck (Part 3); arithmetic checked above.
<!-- END S82 -->

<!-- BEGIN S83 -->
### 44. Worked: $A_1$'s Error Is the Discarded Layer [S83]

**Message.** The residual $A - A_1$ is exactly the dropped layer $\sigma_2 u_2 v_2^\top$, so its error is $\sqrt5$ in both norms; this computes one candidate's error and proves nothing about other candidates.

Subtracting $A_1$ from $A$ leaves the second layer alone. That residual has rank one, so its only singular value is $\sigma_2 = \sqrt5$, and the spectral norm (largest singular value) equals $\sqrt5$. The Frobenius norm, computed entry by entry, is also $\sqrt5$.

The two norms agree here only because the residual has rank one. A residual with two or more nonzero singular values separates them, as a later example shows.

Nothing on this slide compares $A_1$ with other rank-one matrices. That comparison is the theorem.

**Details.**

With $u_2 = (-3,1)^\top/\sqrt{10}$ and $v_2 = (-1,1)^\top/\sqrt2$:

$$\sigma_2 u_2 v_2^\top = \frac{\sqrt5}{\sqrt{20}} \begin{bmatrix} 3 & -3 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{bmatrix} = A - A_1 .$$

Direct check: $A - A_1 = \begin{bmatrix} 3 - 1.5 & 0 - 1.5 \\ 4 - 4.5 & 5 - 4.5 \end{bmatrix}$, the same matrix. Frobenius: $2.25 + 2.25 + 0.25 + 0.25 = 5$. Spectral: the spectral-norm identity $\|M\|_2 = \sigma_1(M)$ applied to $M = A - A_1$, whose SVD is the single layer above.

**Sources.**

Spectral and Frobenius norms via singular values: Wilkinson [16], Section 3.5.1, Propositions 3.10 and 3.11; arithmetic checked above.
<!-- END S83 -->

<!-- BEGIN S90 -->
### 45. Eckart--Young--Mirsky: Spectral Error [S90]

**Message.** In the spectral norm, no matrix of rank at most $k$ gets closer to $A$ than $\sigma_{k+1}$, and $A_k$ achieves exactly $\sigma_{k+1}$.

The theorem box states the setting in full: a real $m \times n$ matrix of rank $r$, sorted positive singular values, and a budget $0 \leq k \lt r$. The minimum of $\|A - B\|_2$ over every $m \times n$ matrix $B$ of rank at most $k$ equals $\sigma_{k+1}$, and $B = A_k$ attains it.

The quantifier is the point. The minimum runs over all rank-$\leq k$ matrices, not only over truncations of the SVD. The Frobenius version is a separate theorem with a separate proof, stated later.

**Details.**

Scope. The theorem concerns a fully observed matrix and the unweighted spectral error. It says nothing about uniqueness; in the spectral norm the minimizer is in general not unique (see the next article).

*7.3 The spectral-norm case, proved (compact form).*

**Theorem (Eckart--Young--Mirsky, spectral norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$.

*Proof.* By rank--nullity, $\dim\operatorname{null}(B) \geq n - k$. Let $W = \operatorname{span}\{v_1,\dots,v_{k+1}\}$, of dimension $k+1$. Then $\dim(\operatorname{null}(B) \cap W) \geq (n-k) + (k+1) - n = 1$, so choose a unit vector $x \in \operatorname{null}(B) \cap W$. Since $Bx = 0$,

$$\|A - B\|_2^2 \geq \|(A-B)x\|_2^2 = \|Ax\|_2^2 = \Big\|\sum_{i \leq k+1} \sigma_i (v_i^\top x)\, u_i\Big\|_2^2 = \sum_{i \leq k+1} \sigma_i^2 (v_i^\top x)^2 \geq \sigma_{k+1}^2,$$

using $x \in W$ (so $v_i^\top x = 0$ for $i \gt k+1$), orthonormality of the $u_i$, and $\sum_{i \leq k+1} (v_i^\top x)^2 = \|x\|_2^2 = 1$ with $\sigma_i \geq \sigma_{k+1}$ throughout. Since $A_k$ attains $\sigma_{k+1}$, it is optimal. $\blacksquare$

The slides that follow unpack this proof step by step.

History. The result is usually attributed to Eckart and Young [1], who proved the Frobenius case in 1936; Mirsky [2] gave the general unitarily invariant statement in 1960, and Erhard Schmidt [3] had proved the analogous theorem for integral operators already in 1907. See [9] for the history of who proved what.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

M. P. Deisenroth, A. A. Faisal and C. S. Ong, *Mathematics for Machine Learning*, Cambridge University Press, 2020, Section 4.6, Theorem 4.25 (Eckart--Young).

Historical attributions: [1], [2], [3], [9].
<!-- END S90 -->

<!-- BEGIN S91 -->
### 46. Optimal: a Floor for All, Met by One [S91]

**Message.** Optimality has two halves: a lower bound that holds for every competitor, and one competitor that meets it.

The figure is a schematic number line of spectral errors $\|A - B\|_2$, starting at $0$ on the left. A dashed red vertical line marks the floor $\sigma_{k+1}$. The region left of the floor is shaded and labelled as containing no rank-$\leq k$ matrix. A dark blue dot sits exactly on the floor and is labelled $A_k$. Grey dots to the right stand for other rank-$\leq k$ matrices; their positions are illustrative, not computed.

Computing one candidate's error, as the worked example did, gives only the blue dot. The proof has to establish the shaded region: no competitor whatsoever lands there.

**Details.**

What the statement does not claim. It does not say $A_k$ is the only minimizer, and it does not address missing entries, prediction, or noise.

*7.6 Uniqueness.*

A common phrasing calls $A_k$ *the* minimizer. For the spectral norm that is false. Counterexample: $A = \operatorname{diag}(2,1)$, $k = 1$, so $\sigma_2 = 1$ and the optimal value is $1$. Take $B_a = \operatorname{diag}(a, 0)$ for any $a \in [1,3]$; then $A - B_a = \operatorname{diag}(2-a, 1)$, whose singular values are $|2-a| \leq 1$ and $1$, so $\|A - B_a\|_2 = 1$, which is optimal, while $A_1 = \operatorname{diag}(2,0)$ is only the case $a = 2$. A whole interval of minimizers.

**Proposition 7.4.** In the Frobenius norm the minimizer is unique if and only if $\sigma_k \gt \sigma_{k+1}$. *Sketch:* the Frobenius proof (article for the Frobenius theorem below) is tight only when $\sigma_i(A-B) = \sigma_{i+k}(A)$ for all $i$, which forces $B$ to be a truncation at a spectral gap; if $\sigma_k = \sigma_{k+1}$ the corresponding singular subspace has dimension greater than $1$ and any $k$-dimensional subspace of it gives another minimizer (as for $A = I_2$, $k = 1$: every $vv^\top$ with $\|v\| = 1$ is optimal). In the spectral norm uniqueness fails even with a strict gap, by the counterexample above.

**Sources.**

Schematic drawn for this deck; no data. Counterexample checked above. Proposition 7.4 is carried over from the earlier note; not independently sourced here (see Horn and Johnson [6] for the singular-value inequalities it rests on).
<!-- END S91 -->

<!-- BEGIN S85 -->
### 47. Recall: Low Rank Forces a Big Null Space [S85]

**Message.** Rank--nullity turns a rank budget into a large null space: if $\operatorname{rank}(B) \leq k$ then $B$ sends at least an $(n-k)$-dimensional subspace of inputs to zero.

A recall box restates rank--nullity for $B \in \mathbb{R}^{m \times n}$: $\dim\operatorname{null}(B) = n - \operatorname{rank}(B)$. With the budget $\operatorname{rank}(B) \leq k$ this gives $\dim\operatorname{null}(B) \geq n - k$.

Here $n$ is the number of columns, the input dimension, and the null space lives in $\mathbb{R}^n$. Every low-rank competitor is blind on a large set of inputs. That blind spot is where the proof will catch it.

**Details.**

Rank--nullity is the statement $\dim\operatorname{null}(B) + \dim\operatorname{range}(B) = n$ for a linear map $\mathbb{R}^n \to \mathbb{R}^m$, with $\dim\operatorname{range}(B) = \operatorname{rank}(B)$. It was established in Part 1 of this deck.

**Sources.**

Rank--nullity as established in Part 1 of this deck.
<!-- END S85 -->

<!-- BEGIN S86 -->
### 48. Large Subspaces Must Intersect [S86]

**Message.** Two subspaces of $\mathbb{R}^n$ whose dimensions add up to more than $n$ must share a nonzero vector.

The fact box states the bound $\dim(S_1 \cap S_2) \geq \dim S_1 + \dim S_2 - n$ for subspaces of $\mathbb{R}^n$. The reason in one line: the sum $S_1 + S_2$ sits inside $\mathbb{R}^n$, so its dimension is at most $n$, and the dimension formula below converts that into the bound.

The application on the slide uses the two dimensions the proof will need, $n - k$ and $k + 1$. They add to $n + 1$, so the intersection has dimension at least one and contains a nonzero vector.

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

The figure shows two planes through the origin in three dimensions. One, shaded blue and labelled $S_1$, is nearly horizontal. The other, shaded amber and labelled $S_2$, is tilted steeply and cuts through it. Their intersection is drawn as a dashed red line through the origin, and a solid red arrow labelled $w$ points along that line from the origin. Because $w$ lies on the red line, it lies in both planes.

The caption gives the count, $\dim(S_1 \cap S_2) \geq 2 + 2 - 3 = 1$. The picture is in $\mathbb{R}^3$ only because that can be drawn; the same count works in any dimension, which is how the proof uses it.

**Details.**

The geometry is exact, not sketched. $S_1 = \{z = 0\}$, and $S_2 = \operatorname{span}\{d, e\}$ with $d = (1, 0.3, 0)$ and $e = (0, -0.6, 1)$. Then $S_1 \cap S_2 = \operatorname{span}\{d\}$, since a point $t d + s e$ has $z$-coordinate $s$, which vanishes only for $s = 0$. The arrow is $w = 0.8\, d / \|d\|$. The drawing uses a fixed oblique projection; the generator script asserts that the red line and $w$ lie in both planes.

**Sources.**

Figure computed for this deck (generator script `gen/o1c_planes.py`).
<!-- END S87 -->

<!-- BEGIN S88 -->
### 50. One Unit Witness Bounds the Maximum [S88]

**Message.** To show a maximum is at least some value, it is enough to exhibit one admissible input that reaches it; for the spectral norm the input must be a unit vector.

The display recalls $\|M\|_2 = \max_{\|x\|_2 = 1} \|Mx\|_2$. Any particular unit vector $w$ is one of the candidates in that maximum, so $\|M\|_2 \geq \|Mw\|_2$.

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

Each $\sigma_i$ with $i \leq k+1$ is at least $\sigma_{k+1}$ because the values are sorted, so the sum is at least $\sigma_{k+1}^2 \sum c_i^2 = \sigma_{k+1}^2$. The slide shows this as one two-row chain, each step labelled by the fact it uses.

**Details.**

The two orthonormality facts play different roles: orthonormal $v_i$ give the coefficient identity $\sum c_i^2 = 1$; orthonormal $u_i$ give the Pythagorean identity for $\|Aw\|_2^2$. Sortedness gives the final inequality. The bound is tight at $w = v_{k+1}$.

This is one half of the min--max characterization of singular values (Courant--Fischer), which the Frobenius proof uses in full; it is stated and proved in the article for the Frobenius theorem.

**Sources.**

Standard; Horn and Johnson [6], ch. 3 (variational characterization of singular values).
<!-- END S89 -->

<!-- BEGIN S92 -->
### 52. Proof Plan: Find One Witness [S92]

**Message.** The spectral proof fixes any competitor $B$, finds one unit vector where $B$ is blind and $A$ is strong, and then checks that $A_k$ meets the resulting bound.

The target, shown at the top, is that every $B$ with $\operatorname{rank}(B) \leq k$ satisfies $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$. A numbered list gives the five steps: the blind spot $\operatorname{null}(B)$ is large; the subspace $W$ spanned by the top $k+1$ right singular vectors is where $A$ is strong; the two must intersect in a unit vector $w$; that witness bounds $\|A - B\|_2$ below by $\sigma_{k+1}$; and $A_k$ attains $\sigma_{k+1}$.

Steps 1 to 4 give the lower bound for every competitor. Step 5 gives the matching competitor.

**Details.**

Each step uses one fact recalled in the preceding slides: rank--nullity (Step 1), orthonormality and sorting (Steps 2 and 4), the intersection count (Step 3), the witness bound for a maximum (Step 4), and the spectral-norm identity $\|M\|_2 = \sigma_1(M)$ (Step 5).

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S92 -->

<!-- BEGIN S93 -->
### 53. Step 1: Every Competitor Has a Blind Spot [S93]

**Message.** Any rank-$\leq k$ competitor $B$ has a null space of dimension at least $n - k$, and on that null space the residual $A - B$ acts exactly like $A$.

Fix $B$ arbitrary, subject only to the rank budget. Rank--nullity gives $\dim\operatorname{null}(B) = n - \operatorname{rank}(B) \geq n - k$.

For any $x$ with $Bx = 0$, $(A - B)x = Ax$: the competitor contributes nothing there. The slide stresses that $B$ is arbitrary, not $A_k$, because the bound has to hold for all competitors at once.

**Details.**

Nothing about the structure of $B$ beyond its rank is used, so the argument covers every competitor, including ones unrelated to the SVD of $A$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S93 -->

<!-- BEGIN S94 -->
### 54. Step 2: $A$ Stays Strong on $W$ [S94]

**Message.** The span $W$ of the top $k+1$ right singular vectors is a $(k+1)$-dimensional subspace of inputs on which $A$ stretches every unit vector by at least $\sigma_{k+1}$.

$W = \operatorname{span}\{v_1, \dots, v_{k+1}\}$ lives in the input space $\mathbb{R}^n$, the same space as $\operatorname{null}(B)$. Its dimension is $k + 1$ because orthonormal vectors are linearly independent.

The assumption $k \lt r$ is used here: it guarantees that $v_{k+1}$ exists with $\sigma_{k+1} \gt 0$. The last bullet recalls the top-directions bound: every unit $w \in W$ has $\|Aw\|_2 \geq \sigma_{k+1}$.

**Details.**

If $k \geq r$ the theorem is trivial, since $A_k = A$ has error zero, which is why the statement restricts to $0 \leq k \lt r$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S94 -->

<!-- BEGIN S95 -->
### 55. Step 3: The Two Subspaces Share a Unit $w$ [S95]

**Message.** The blind spot and the strong subspace have dimensions adding to more than $n$, so they share a nonzero vector, which can be scaled to a unit vector $w$.

The first display adds the dimensions: $(n - k) + (k + 1) = n + 1 \gt n$. The intersection bound then gives $\dim(\operatorname{null}(B) \cap W) \geq 1$.

Take any nonzero $z$ in the intersection and set $w = z / \|z\|_2$. Scaling keeps $w$ in both subspaces, so $w$ is a unit vector that $B$ kills and that lies in $W$.

**Details.**

This is the picture of two planes in $\mathbb{R}^3$ again, with $\operatorname{null}(B)$ and $W$ in place of the planes.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S95 -->

<!-- BEGIN S96 -->
### 56. Step 4: Along $w$, the Residual Is $A$ [S96]

**Message.** Because $w$ is a unit vector killed by $B$, the residual's spectral norm is at least $\|Aw\|_2$.

The chain on the slide has two labelled steps. The first, labelled "$w$ unit", is the witness bound for a maximum: $\|A - B\|_2 \geq \|(A - B)w\|_2$. The second, labelled "$Bw = 0$", removes the competitor: $\|Aw - Bw\|_2 = \|Aw\|_2$.

No maximum is computed; one input is enough for a lower bound. What remains is to show $\|Aw\|_2$ cannot be small.

**Details.**

Both facts about $w$ come from Step 3: unit length from the normalisation, $Bw = 0$ from membership in the null space.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S96 -->

<!-- BEGIN S97 -->
### 57. Step 4 (continued): The Witness Is Not Small [S97]

**Message.** Since $w$ lies in $W$, $\|Aw\|_2 \geq \sigma_{k+1}$, and therefore $\|A - B\|_2 \geq \sigma_{k+1}$ for every competitor $B$.

A recap line restates what is known about $w$: it lies in $W$ and has unit length, so $w = \sum_{i \leq k+1} c_i v_i$ with $\sum c_i^2 = 1$. The top-directions computation gives $\|Aw\|_2^2 = \sum \sigma_i^2 c_i^2 \geq \sigma_{k+1}^2$.

Both sides are nonnegative, so taking square roots preserves the inequality. Combined with the previous step this gives the lower bound $\|A - B\|_2 \geq \sigma_{k+1}$, valid for every $B$ with rank at most $k$, because $B$ was arbitrary.

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

The first row records the existence step: the dimensions of $\operatorname{null}(B)$ and $W$ add to more than $n$ (steps 1 and 2), so step 3 supplies a unit $w$ in both. The second row is the inequality chain from $\|A - B\|_2$ to $\|A - A_k\|_2$, each relation labelled by the step or fact that justifies it.

Reading the chain end to end: every rank-$\leq k$ matrix has spectral error at least $\sigma_{k+1}$, and $A_k$ has exactly that error, so $\min_{\operatorname{rank}(B) \leq k} \|A - B\|_2 = \sigma_{k+1}$.

**Details.**

The compact written proof is in the article for the spectral theorem (Section 7.3).

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).
<!-- END S99 -->

<!-- BEGIN S101 -->
### 60. Eckart--Young--Mirsky: Frobenius Error [S101]

**Message.** In the Frobenius norm the best rank-$\leq k$ squared error is $\sum_{i > k} \sigma_i^2$, again attained by $A_k$; this is a separate theorem, stated here and proved only in this note.

The theorem box repeats the same setup and states $\min_{\operatorname{rank}(B) \leq k} \|A - B\|_F^2 = \sum_{i = k+1}^r \sigma_i^2$, attained by $B = A_k$.

The spectral proof does not give this. It bounds only the largest singular value of $A - B$, whereas the Frobenius norm sums all of them. The proof below needs Weyl's inequality for singular values, which rests on the min--max characterization. The lecture uses the statement only.

**Details.**

*7.2 Courant--Fischer for singular values.*

**Lemma 7.1 (min--max / max--min).** For $1 \leq i \leq \min(m,n)$,

$$\sigma_i(A) = \max_{\substack{S \subseteq \mathbb{R}^n \\ \dim S = i}} \ \min_{\substack{x \in S \\ \|x\|_2 = 1}} \|Ax\|_2 = \min_{\substack{T \subseteq \mathbb{R}^n \\ \dim T = n-i+1}} \ \max_{\substack{x \in T \\ \|x\|_2 = 1}} \|Ax\|_2 .$$

*Proof (first equality; the second is analogous).* (At least $\sigma_i$ for the max.) Take $S_0 = \operatorname{span}\{v_1, \dots, v_i\}$. For unit $x \in S_0$, $x = \sum_{j \leq i} c_j v_j$ with $\sum c_j^2 = 1$, and $\|Ax\|_2^2 = \sum_{j \leq i} \sigma_j^2 c_j^2 \geq \sigma_i^2$. So the inner min over $S_0$ is at least $\sigma_i$ (indeed equal, at $x = v_i$). (At most $\sigma_i$ for every $S$.) Let $\dim S = i$ and $W' = \operatorname{span}\{v_i, v_{i+1}, \dots, v_n\}$, completing the $v$'s to an orthonormal basis of $\mathbb{R}^n$ with $\sigma_j := 0$ beyond the rank; $\dim W' = n - i + 1$. By the intersection count, $\dim(S \cap W') \geq 1$, so there is a unit $x \in S \cap W'$. Writing $x = \sum_{j \geq i} c_j v_j$, $\|Ax\|_2^2 = \sum_{j \geq i} \sigma_j^2 c_j^2 \leq \sigma_i^2$. Hence the inner min over $S$ is at most $\sigma_i$. $\blacksquare$

*7.4 The Frobenius case, proved.*

**Lemma 7.2 (Weyl, additive).** For $X, Y \in \mathbb{R}^{m \times n}$ and $i, j \geq 1$ with $i + j - 1 \leq \min(m,n)$: $\sigma_{i+j-1}(X + Y) \leq \sigma_i(X) + \sigma_j(Y)$.

*Proof.* By the min--max form of Lemma 7.1 there are subspaces $T_X$ of dimension $n - i + 1$ and $T_Y$ of dimension $n - j + 1$ with $\max_{x \in T_X, \|x\| = 1} \|Xx\|_2 = \sigma_i(X)$ and likewise for $Y$. Put $T = T_X \cap T_Y$, so $\dim T \geq (n-i+1) + (n-j+1) - n = n - (i+j-1) + 1$. Applying the min--max characterization at index $i + j - 1$ (whose minimum runs over subspaces of exactly that dimension, and any larger subspace contains one) gives $\sigma_{i+j-1}(X+Y) \leq \max_{x \in T, \|x\| = 1} \|(X+Y)x\|_2 \leq \max_{x \in T, \|x\| = 1} (\|Xx\|_2 + \|Yx\|_2) \leq \sigma_i(X) + \sigma_j(Y)$. $\blacksquare$

**Lemma 7.3.** If $\operatorname{rank}(B) \leq k$ then $\sigma_{i+k}(A) \leq \sigma_i(A - B)$ for all $i \geq 1$ (with $\sigma_j := 0$ beyond $\min(m,n)$). *Proof.* Apply Lemma 7.2 with $X = A - B$, $Y = B$, indices $i$ and $k+1$: $\sigma_{i+k}(A) \leq \sigma_i(A - B) + \sigma_{k+1}(B)$, and $\operatorname{rank}(B) \leq k$ means $\sigma_{k+1}(B) = 0$. $\blacksquare$

**Theorem (Eckart--Young--Mirsky, Frobenius norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_F^2 \geq \sum_{i > k} \sigma_i(A)^2 = \|A - A_k\|_F^2$. *Proof.* By the Frobenius identity $\|M\|_F^2 = \sum_i \sigma_i(M)^2$ and Lemma 7.3, $\|A - B\|_F^2 = \sum_{i \geq 1} \sigma_i(A - B)^2 \geq \sum_{i \geq 1} \sigma_{i+k}(A)^2 = \sum_{j > k} \sigma_j(A)^2$, which is $\|A - A_k\|_F^2$ by the next article. $\blacksquare$

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

The display subtracts the kept layers: $A - A_k = \sum_{i = k+1}^r \sigma_i u_i v_i^\top$, which is an SVD with singular values $\sigma_{k+1}, \dots, \sigma_r$. The Frobenius identity $\|M\|_F^2 = \sum_i \sigma_i(M)^2$ then gives the squared error.

A highlighted box separates the two claims. This calculation computes the error of one candidate. The statement that no other rank-$\leq k$ matrix does better is the Frobenius theorem, which this calculation does not prove.

**Details.**

The same structure appeared in the spectral case: Step 5 computed $\|A - A_k\|_2 = \sigma_{k+1}$, and Steps 1 to 4 supplied the bound for every competitor. In the Frobenius case the bound for every competitor is Lemma 7.3 in the previous article.

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

Applying both theorems with $k = 1$ and $\sigma_2 = \sqrt5$: the minimum spectral error is $\sqrt5$ and the minimum squared Frobenius error is $5$. The second display recalls $A_1$ and its errors, both $\sqrt5$, matching the floors.

The two errors coincide because the residual has rank one. The earlier calculation showed only that $A_1$ achieves $\sqrt5$; the theorems add that nothing does better. Both theorems are proved independently of this example, so the argument is not circular.

**Details.**

*7.5 Energy accounting and the worked example.*

$$A_1 = \begin{bmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{bmatrix}, \qquad A - A_1 = \begin{bmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{bmatrix}, \qquad \|A - A_1\|_2 = \|A - A_1\|_F = \sigma_2 = \sqrt5 .$$

The equality of the two norms is not general. It holds because $A - A_1$ has rank one, so its singular-value vector has a single nonzero entry and all $\ell_p$ norms of it agree. Independent check: $\|A - A_1\|_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

Worked example: arithmetic checked above.
<!-- END S102 -->

<!-- BEGIN S103 -->
### 64. One Layer Keeps 90% of the Energy [S103]

**Message.** The rank-one truncation keeps $45$ of the $50$ units of squared Frobenius norm, $90\%$ of the energy.

Define the energy kept by $A_k$ as $\|A_k\|_F^2 / \|A\|_F^2 = \sum_{i \leq k} \sigma_i^2 / \sum_{i \leq r} \sigma_i^2$. For the worked matrix with $k = 1$ this is $45 / (45 + 5) = 90\%$.

The figure is a single horizontal bar whose total length represents $\|A\|_F^2 = 9 + 16 + 25 = 50$. The dark blue part, $45$ units long, is $\sigma_1^2$, the part kept by $A_1$. The light blue end piece, $5$ units, is $\sigma_2^2$, the part discarded. A thin vertical line marks the split.

Energy share is not prediction accuracy. It is called explained variance only when the rows or columns of the data matrix have been centered.

**Details.**

The bar is drawn to scale: $18$ pixels per unit, so $810$ pixels for $45$ and $90$ for $5$.

Squared Frobenius norm from the entries: $3^2 + 0^2 + 4^2 + 5^2 = 50$; from the singular values: $45 + 5 = 50$. The kept energy $\|A_1\|_F^2 = 45$ was checked in the article for $A_1$.

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

A three-box flow reads left to right: given every entry of $A$, choose a rank budget $k$, get $A_k$ with optimal error. The optimal error is $\sigma_{k+1}$ in the spectral norm and $\sum_{i > k} \sigma_i^2$ in squared Frobenius norm, and every entry counts equally.

A box below lists what the theorem does not cover: matrices with missing entries, the downstream accuracy of a model built on $A_k$, and statistically optimal denoising of a noisy matrix. Each of these changes the problem, so the closed-form answer no longer applies as stated.

**Details.**

Other limits of this lecture, for the record: the existence of the SVD rests on the spectral theorem, which was not proved here; everything was over the real numbers (the complex case is parallel, with conjugate transposes); and how the SVD is computed numerically is a separate subject (Golub and Van Loan [8], ch. 8).

Weighted errors, where some entries count more than others, and observing only some entries, both break the closed form: the minimizer is no longer obtained by truncating an SVD.

**Sources.**

R. D. Wilkinson, MATH3030 lecture notes, Section 3.5 "Low-rank approximation" [16]: Section 3.5.2, Theorem 3.1 (Eckart--Young--Mirsky) states the result for the 2-norm and the Frobenius norm and proves the 2-norm case on the page; Section 3.5.1 gives $\|A\|_F^2 = \sum_i \sigma_i^2$ (Proposition 3.10) and $\|A\|_2 = \sigma_1$ (Proposition 3.11).

Numerical computation: Golub and Van Loan [8].
<!-- END S123 -->

<!-- BEGIN S117 -->
### 67. From Directions to the Optimal Error [S117]

**Message.** The lecture's chain: measure error through singular values, decompose $A$ into layers, truncate, and read the optimal error off the discarded singular values.

Four boxes form one chain. Measure: $\|A\|_2 = \sigma_1$ and $\|A\|_F^2 = \sum \sigma_i^2$. Decompose: $A = \sum \sigma_i u_i v_i^\top$. Truncate: keep $k$ layers to get $A_k$. Read off: the optimal errors $\sigma_{k+1}$ and $\sum_{i > k} \sigma_i^2$.

The line below summarises the payoff: the SVD gives the best rank-$k$ approximation in closed form, for both error measures.

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
