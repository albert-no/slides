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
### 20. Recall: Symmetric Eigendecomposition [S36]

**Message.** The SVD is built from one imported fact: a symmetric matrix has an orthonormal eigenbasis, and for $A^\top A$ every eigenvalue is nonnegative.

The slide opens with the recall line: every symmetric $S \in \mathbb R^{n\times n}$ factors as $S = Q\Lambda Q^\top$ with $Q$ orthogonal and $\Lambda$ real diagonal. It then applies this to $A^\top A$, which is symmetric and $n \times n$, so it acts on input vectors $x \in \mathbb R^n$. The display gives $A^\top A = Q\Lambda Q^\top$ and $\lambda_i = q_i^\top A^\top A q_i = \|Aq_i\|_2^2 \ge 0$. The highlighted line states the payoff: $A^\top A$ supplies orthonormal input directions $q_1, \dots, q_n$ in $\mathbb R^n$.

**Details.**

**Why the eigenvalues are nonnegative.** For a unit eigenvector $q_i$, $\lambda_i = q_i^\top (\lambda_i q_i) = q_i^\top A^\top A q_i = (Aq_i)^\top (Aq_i) = \|Aq_i\|_2^2 \ge 0$. More generally $x^\top A^\top A x = \|Ax\|_2^2 \ge 0$ for every $x$, so $A^\top A$ is positive semidefinite.

**What is imported.** The spectral theorem itself is not proved in this lecture; it is the one black box. Everything else in Part 3 is derived from it.

**Why input space.** $A^\top A$ is $n \times n$, the same size as the input dimension of $A$. Its eigenvectors will become the right singular vectors $v_i$ on the next slides.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.2, Theorem 4.14 ($A^\top A$ symmetric positive semidefinite) and Theorem 4.15 (spectral theorem).
<!-- END S36 -->

<!-- BEGIN S38 -->
### 21. Every Matrix Has an SVD [S38]

**Message.** Every real matrix, of any shape and rank, factors as an orthogonal matrix times a nonnegative diagonal stretch times an orthogonal matrix.

The theorem card states Theorem 5 for every $A \in \mathbb R^{m\times n}$ of rank $r$, with no assumption of squareness, symmetry or invertibility. The display reads $A = U\Sigma V^\top$ with $U \in \mathbb R^{m\times m}$ and $V \in \mathbb R^{n\times n}$ orthogonal. The last card line says $\Sigma \in \mathbb R^{m\times n}$ has $\Sigma_{ii} = \sigma_i$, zeros off the diagonal, $\sigma_1 \ge \dots \ge \sigma_r \gt 0$, and the remaining diagonal slots equal to $0$. A muted line under the card names the construction: eigenvectors of $A^\top A$ give $V$, then $u_i = Av_i/\sigma_i$.

**Details.**

**Construction sketch.** Take the eigendecomposition $A^\top A = V\Lambda V^\top$ with eigenvalues in decreasing order and set $\sigma_i = \sqrt{\lambda_i}$. Exactly $r$ of them are positive because $\operatorname{rank}(A^\top A) = \operatorname{rank}(A) = r$. For $i \le r$ put $u_i = Av_i/\sigma_i$; these are orthonormal because $u_i^\top u_j = v_i^\top A^\top A v_j/(\sigma_i\sigma_j) = \lambda_j v_i^\top v_j/(\sigma_i\sigma_j) = \delta_{ij}$. Extend $u_1, \dots, u_r$ to an orthonormal basis of $\mathbb R^m$. Then $AV = U\Sigma$ column by column (for $i \gt r$, $\|Av_i\|_2^2 = \lambda_i = 0$), so $A = U\Sigma V^\top$.

**Uniqueness.** The singular values are unique. The vectors are unique up to sign when the $\sigma_i$ are distinct and positive; repeated values allow any orthonormal basis of the shared subspace. The full existence and uniqueness proof is kept in the archived full note.

**Numbering.** This is Theorem 5 of the lecture; Theorems 6 and 7 below read the two norms off $\Sigma$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5, Theorem 4.22 (SVD theorem); Section 4.5.2, eq. (4.78), $u_i = Av_i/\sigma_i$.
<!-- END S38 -->

<!-- BEGIN S39 -->
### 22. Read the Factor Shapes [S39]

**Message.** The factor shapes $(m\times m)(m\times n)(n\times n)$ multiply to $m \times n$, and only the first $r$ diagonal slots of $\Sigma$ are nonzero.

The figure draws, left to right, a tall shaded block $A$ labelled $m \times n$, an equals sign, a square $U$ labelled $m \times m$ and orthogonal, a tall $\Sigma$ labelled $m \times n$, and a smaller square $V^\top$ labelled $n \times n$ and orthogonal. Inside $\Sigma$ the diagonal starts as a solid blue segment, labelled $\sigma_1, \dots, \sigma_r \gt 0$ above the block, and continues as a dashed gray segment for the zero diagonal slots. A gray band across the bottom of $\Sigma$ marks the zero rows. The figure is drawn for $m \gt n$. The key lines below give the shape product and decode solid, dashed and gray.

**Details.**

**Names.** The columns $u_i$ of $U$ are the left singular vectors (in output space $\mathbb R^m$); the columns $v_i$ of $V$ are the right singular vectors (in input space $\mathbb R^n$).

**Other shapes.** For $m \lt n$ the zero block of $\Sigma$ is a set of columns on the right instead of rows at the bottom. For square $A$ there is no zero block, only zero diagonal entries when $r \lt n$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5, eq. (4.64) and the shape discussion after Theorem 4.22.
<!-- END S39 -->

<!-- BEGIN S40 -->
### 23. Rotate, Stretch, Rotate [S40]

**Message.** Multiplying by $A = U\Sigma V^\top$ is three steps: an orthogonal change of input coordinates, a stretch by the singular values, and an orthogonal change of output coordinates.

A flow diagram runs left to right through four boxes: $x$ in $\mathbb R^n$, then $V^\top x$ in $\mathbb R^n$, then $\Sigma V^\top x$ in $\mathbb R^m$, then $Ax$ in $\mathbb R^m$. The three arrows are labelled $V^\top$ (orthogonal), $\Sigma$ (stretch) and $U$ (orthogonal). The display reads $Ax = U(\Sigma(V^\top x))$ and notes that the rightmost factor acts first. Two lines name the roles: $V^\top$ and $U$ are rotations or reflections that keep lengths; $\Sigma$, of size $m \times n$, multiplies coordinate $i$ by $\sigma_i$ and is not a rotation.

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

Two panels are joined by a gray arrow labelled $V^\top$. Panel 1 shows the unit circle of inputs with two arrows: $v_1$ pointing up and to the right at $45$ degrees and $v_2$ pointing up and to the left. Panel 2, after $V^\top$, shows the same circle with $v_1$ now along the horizontal axis as $e_1$ and $v_2$ along the vertical axis as $e_2$. The caption says $V^\top$ is orthogonal, so lengths are kept and nothing is stretched. A muted line notes that the picture is drawn for the worked matrix used later, with $v_1 = (1,1)/\sqrt2$ and $v_2 = (-1,1)/\sqrt2$.

**Details.**

**Check.** $V^\top v_1 = e_1$ and $V^\top v_2 = e_2$ because the rows of $V^\top$ are $v_1^\top, v_2^\top$ and these are orthonormal. Here $V = \frac{1}{\sqrt2}\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ has determinant $1$, so $V^\top$ is a rotation by $-45$ degrees.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.1, Figure 4.8. Vectors: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S52 -->

<!-- BEGIN S53 -->
### 25. Then Stretch and Reorient [S53]

**Message.** $\Sigma$ stretches the axes by $\sigma_1$ and $\sigma_2$, and $U$ turns them into the output directions: the image of the unit circle is an ellipse with semi-axes $\sigma_1 u_1$ and $\sigma_2 u_2$.

Two more panels continue the sequence, joined by an arrow labelled $U$. Panel 3, after $\Sigma$, shows an axis-aligned ellipse three times as wide as it is tall, with arrows $\sigma_1 e_1$ along the horizontal axis and $\sigma_2 e_2$ along the vertical axis. Panel 4, after $U$, shows the same ellipse tilted steeply up and to the right, with the long semi-axis $\sigma_1 u_1$ pointing along $(1,3)$ and the short one $\sigma_2 u_2$ pointing along $(-3,1)$; this ellipse is the set of all $Ax$ for unit $x$. The caption gives the semi-axis lengths as the singular values $\sigma_1 = 3\sqrt5 \approx 6.71$ and $\sigma_2 = \sqrt5 \approx 2.24$. The muted line warns that these are not the eigenvalues $3$ and $5$ of $A$ and that the drawing is shrunk with axis ratio exactly $3:1$.

**Details.**

**Why an ellipse.** After $V^\top$ the input is a unit vector $y$; $\Sigma y = (\sigma_1 y_1, \sigma_2 y_2)$ satisfies $(z_1/\sigma_1)^2 + (z_2/\sigma_2)^2 = 1$, an axis-aligned ellipse. $U$ is orthogonal, so it moves the ellipse rigidly.

**Drawing scale.** The drawn semi-axes are $120$ and $40$ units, ratio $3 = \sigma_1/\sigma_2$; the tilt is $\arctan 3 \approx 71.57$ degrees, the direction of $u_1 = (1,3)/\sqrt{10}$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.1, Figure 4.8. Numbers: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S53 -->

<!-- BEGIN S41 -->
### 26. A Sum of Rank-One Layers [S41]

**Message.** Expanding $U\Sigma V^\top$ writes $A$ as a sum of $r$ rank-one layers $\sigma_i u_i v_i^\top$, ordered by weight.

The left column shows $A = U\Sigma V^\top = \sum_{i=1}^r \sigma_i u_i v_i^\top$, with braces marking $u_i$ as $m \times 1$ and $v_i^\top$ as $1 \times n$. Three lines follow: each $u_i v_i^\top$ is $m \times n$ with every column a multiple of $u_i$; when $\sigma_i \gt 0$ the term has rank one; and all $r$ terms together give $A$ exactly. The right column shows three stacked translucent sheets; the front sheet is labelled $\sigma_1 u_1 v_1^\top$ with largest weight, the caption reads $A$ = layer $1 + \dots +$ layer $r$, and the back layers carry smaller $\sigma_i$.

**Details.**

**Derivation.** The columns of $U\Sigma$ are $\sigma_i u_i$ for $i \le r$ and zero otherwise. Multiplying by $V^\top$, whose rows are $v_i^\top$, gives $U\Sigma V^\top = \sum_{i=1}^r (\sigma_i u_i) v_i^\top$ by the column-times-row form of matrix multiplication.

**Rank one.** Column $j$ of $u_i v_i^\top$ is $(v_i)_j u_i$, a multiple of $u_i$, and $v_i \ne 0$, so the column space is exactly the span of $u_i$.

**Forward pointer.** The partial sum of the first $k$ layers is written $A_k = \sum_{i \le k}\sigma_i u_i v_i^\top$. Whether $A_k$ is the best rank-$k$ approximation is a separate theorem, proved later in the lecture.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6 (matrix approximation as a sum of rank-one matrices).
<!-- END S41 -->

<!-- BEGIN S42 -->
### 27. Compact SVD Keeps Active Directions [S42]

**Message.** Dropping the zero singular values leaves the compact SVD $A = U_r\Sigma_r V_r^\top$, which is still exact but whose thin factors are not orthogonal matrices.

The figure shows $A$ ($m \times n$) equal to a thin tall block $U_r$ ($m \times r$), a small square $\Sigma_r$ ($r \times r$) with a full diagonal, and a short wide block $V_r^\top$ ($r \times n$); a gray note says only the $r$ nonzero $\sigma_i$ are kept. The display reads $A = U_r\Sigma_r V_r^\top$, $\Sigma_r = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$, $U_r^\top U_r = V_r^\top V_r = I_r$. The muted qualifier says that when $r \lt m$, $U_r U_r^\top \ne I_m$: the thin factors have orthonormal columns but are not square orthogonal matrices.

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

The worked example is introduced as $A = \begin{bmatrix}3 & 0\\ 4 & 5\end{bmatrix}$, not symmetric, used to the end of the lecture. The display substitutes the SVD into $A^\top A$: $A^\top A = V\Sigma^\top U^\top U\Sigma V^\top = V\Sigma^\top\Sigma V^\top$ because $U^\top U = I$, so the eigenvalues of $A^\top A$ are the $\sigma_i^2$. A four-box chain shows the route: 1, form $A^\top A$; 2, eigenpairs $\lambda_i, v_i$; 3, stretches $\sigma_i = \sqrt{\lambda_i}$; 4, outputs $u_i = Av_i/\sigma_i$.

**Details.**

**Why the route works.** $V\Sigma^\top\Sigma V^\top$ is an eigendecomposition: $\Sigma^\top\Sigma$ is $n \times n$ diagonal with entries $\sigma_i^2$ (and zeros), and $V$ is orthogonal. So the right singular vectors are eigenvectors of $A^\top A$, and the eigenvalues are the squared stretches.

**Step 4.** Dividing by $\sigma_i$ is allowed only when $\sigma_i \gt 0$; the zero singular values give no $u_i$ this way, and the remaining columns of $U$ are filled in by any orthonormal completion.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.5.2 (construction of the SVD). Example: Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S44 -->

<!-- BEGIN S45 -->
### 29. Build the Symmetric Matrix $A^\top A$ [S45]

**Message.** For the worked example, $A^\top A = \begin{bmatrix}25 & 20\\ 20 & 25\end{bmatrix}$, and each entry is a dot product of two columns of $A$.

The first display multiplies $A^\top = \begin{bmatrix}3 & 4\\ 0 & 5\end{bmatrix}$ by $A$ to get $\begin{bmatrix}25 & 20\\ 20 & 25\end{bmatrix}$. The line below explains entry $(i,j)$ as column $i$ of $A$ dotted with column $j$, and the second display shows the three distinct dot products: $3^2 + 4^2 = 25$, $3\cdot 0 + 4\cdot 5 = 20$, and $0^2 + 5^2 = 25$. The muted line notes the result is $2\times 2$, symmetric and positive semidefinite, ready for an eigenproblem.

**Details.**

**Columns of $A$.** Column 1 is $(3,4)$ and column 2 is $(0,5)$. Their squared lengths $25$ and $25$ sit on the diagonal; their dot product $20$ sits off the diagonal.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S45 -->

<!-- BEGIN S46 -->
### 30. The Eigenvalues Are 45 and 5 [S46]

**Message.** The eigenvalues of $A^\top A$ are $45$ and $5$; they are the squared singular values, not eigenvalues of $A$.

The characteristic polynomial is factored as a difference of squares: $\det(A^\top A - \lambda I) = (25-\lambda)^2 - 20^2 = (25-\lambda-20)(25-\lambda+20) = (5-\lambda)(45-\lambda)$. The second display lists $\lambda_1 = 45 \ge \lambda_2 = 5$ with two checks: the sum $50$ equals the trace $25+25$, and the product $225$ equals the determinant $25^2 - 20^2$. The muted line repeats that these are eigenvalues of $A^\top A$, the squared stretches $\sigma_i^2$.

**Details.**

**Arithmetic.** $25^2 - 20^2 = 625 - 400 = 225 = 45 \cdot 5$. Also $\det(A^\top A) = (\det A)^2 = 15^2 = 225$.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S46 -->

<!-- BEGIN S47 -->
### 31. Orthonormal Input Directions [S47]

**Message.** Solving the two null-space problems gives $v_1 = (1,1)/\sqrt2$ and $v_2 = (-1,1)/\sqrt2$: orthonormal input directions.

The display solves $(A^\top A - \lambda I)v = 0$ for each eigenvalue. For $\lambda_1 = 45$ the matrix is $\begin{bmatrix}-20 & 20\\ 20 & -20\end{bmatrix}$, whose null space is spanned by $(1,1)$, so $v_1 = (1,1)/\sqrt2$. For $\lambda_2 = 5$ the matrix is $\begin{bmatrix}20 & 20\\ 20 & 20\end{bmatrix}$, giving $v_2 = (-1,1)/\sqrt2$. The check line shows $v_1^\top v_2 = \frac12(-1+1) = 0$ and both vectors have length $1$. The muted line notes that $-v_i$ also works, provided $u_i$ flips with it.

**Details.**

**Sign convention.** Replacing $v_i$ by $-v_i$ replaces $u_i = Av_i/\sigma_i$ by $-u_i$, and $\sigma_i u_i v_i^\top$ is unchanged. The lecture fixes the signs above.

**Geometry.** $V = [v_1\ v_2] = \frac{1}{\sqrt2}\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ is the rotation by $45$ degrees (determinant $1$).

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S47 -->

<!-- BEGIN S48 -->
### 32. Recover Stretches and Output Directions [S48]

**Message.** Square roots give $\sigma_1 = 3\sqrt5$ and $\sigma_2 = \sqrt5$, and $u_i = Av_i/\sigma_i$ gives $u_1 = (1,3)/\sqrt{10}$ and $u_2 = (-3,1)/\sqrt{10}$.

The first display gives $\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.71$ and $\sigma_2 = \sqrt5 \approx 2.24$. The second display computes $Av_1 = (3,9)/\sqrt2$ and divides by $3\sqrt5$ to get $u_1 = (1,3)/\sqrt{10}$, and computes $Av_2 = (-3,1)/\sqrt2$ and divides by $\sqrt5$ to get $u_2 = (-3,1)/\sqrt{10}$. The check line shows $u_1^\top u_2 = \frac{1}{10}(-3+3) = 0$, both of length $1$, and both $\sigma_i \gt 0$ so the divisions are allowed.

**Details.**

**Arithmetic.** $Av_1 = \frac{1}{\sqrt2}(3\cdot1 + 0\cdot1,\ 4\cdot1 + 5\cdot1) = (3,9)/\sqrt2$; dividing by $3\sqrt5$ gives $(1,3)/\sqrt{10}$ since $\sqrt2\cdot\sqrt5 = \sqrt{10}$. $Av_2 = \frac{1}{\sqrt2}(-3,\ -4+5) = (-3,1)/\sqrt2$. Lengths: $(1+9)/10 = 1$ for both.

**Geometry.** $U = \frac{1}{\sqrt{10}}\begin{bmatrix}1 & -3\\ 3 & 1\end{bmatrix}$ has determinant $(1+9)/10 = 1$, a rotation by $\arctan 3 \approx 71.57$ degrees.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S48 -->

<!-- BEGIN S49 -->
### 33. The Factors Reconstruct $A$ [S49]

**Message.** Multiplying the three computed factors gives back $A$ exactly.

The first display writes $A$ as the product of $U = \frac{1}{\sqrt{10}}\begin{bmatrix}1 & -3\\ 3 & 1\end{bmatrix}$, $\Sigma = \operatorname{diag}(3\sqrt5, \sqrt5)$ and $V^\top = \frac{1}{\sqrt2}\begin{bmatrix}1 & 1\\ -1 & 1\end{bmatrix}$, each labelled by a brace. The second display multiplies in two steps: $U\Sigma = \frac{1}{\sqrt2}\begin{bmatrix}3 & -3\\ 9 & 1\end{bmatrix}$, then $(U\Sigma)V^\top = \frac12\begin{bmatrix}6 & 0\\ 8 & 10\end{bmatrix} = A$, with a check mark. The muted line reminds that the columns of $U$ are $u_1, u_2$ and the rows of $V^\top$ are $v_1^\top, v_2^\top$.

**Details.**

**Arithmetic.** $U\Sigma$: column 1 is $3\sqrt5\,(1,3)/\sqrt{10} = (3,9)/\sqrt2$ and column 2 is $\sqrt5\,(-3,1)/\sqrt{10} = (-3,1)/\sqrt2$. Then row 1 of $(U\Sigma)V^\top$ is $\frac12(3\cdot1 + (-3)(-1),\ 3\cdot1 + (-3)\cdot1) = \frac12(6, 0)$ and row 2 is $\frac12(9 - 1,\ 9 + 1) = \frac12(8, 10)$.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S49 -->

<!-- BEGIN S50 -->
### 34. The First Layer Carries Most Energy [S50]

**Message.** The first rank-one layer $A_1$ carries $45$ of the total energy $50$, that is $90\%$; this is a reconstruction fact, not yet an optimality claim.

The first display splits $A$ into its two layers: $A_1 = \sigma_1 u_1 v_1^\top = \begin{bmatrix}1.5 & 1.5\\ 4.5 & 4.5\end{bmatrix}$ plus $\sigma_2 u_2 v_2^\top = \begin{bmatrix}1.5 & -1.5\\ -0.5 & 0.5\end{bmatrix}$. The second display gives the energies, squared Frobenius norms: $50 = 45 + 5$. The text line states the share $45/50 = 90\%$. The muted line warns that this is reconstruction, not optimality: it does not yet show $A_1$ is the best rank-one approximation.

**Details.**

**Arithmetic.** $\sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}}(1,3) \cdot \frac{1}{\sqrt2}(1,1)^\top = \frac{3}{2}\begin{bmatrix}1 & 1\\ 3 & 3\end{bmatrix}$, entries summing in squares to $\frac94(1+1+9+9) = 45$. $\sigma_2 u_2 v_2^\top = \sqrt5 \cdot \frac{1}{\sqrt{10}}(-3,1) \cdot \frac{1}{\sqrt2}(-1,1)^\top = \frac12\begin{bmatrix}3 & -3\\ -1 & 1\end{bmatrix}$, squared entries $\frac14(9+9+1+1) = 5$. The two layers add to $A$ entry by entry. $\|A\|_F^2 = 9 + 0 + 16 + 25 = 50$.

**Why the energies add.** The layers are orthogonal in the Frobenius inner product because $u_1 \perp u_2$; Theorem 7 below states the general identity $\|A\|_F^2 = \sum_i \sigma_i^2$.

**Forward pointer.** That $A_1$ is the best rank-one approximation, in both the spectral and Frobenius norms, is the Eckart-Young-Mirsky theorem, later in the lecture.

**Sources.**

Worked-example arithmetic: our calculation, recomputed for this revision.
<!-- END S50 -->

<!-- BEGIN S51 -->
### 35. Eigenvalues Are Not Singular Values [S51]

**Message.** For a non-symmetric matrix the eigenvalues and the singular values are different lists; the eigenvalues of $A^\top A$ are the squared singular values.

The slide shows the same $A = \begin{bmatrix}3 & 0\\ 4 & 5\end{bmatrix}$ in two columns. Left, the eigenvalues of $A$ are $3$ and $5$, read from the diagonal of a triangular matrix; an eigenvector keeps its direction, $Ax = \lambda x$. Right, the singular values are $3\sqrt5 \approx 6.71$ and $\sqrt5 \approx 2.24$; a singular pair satisfies $Av_i = \sigma_i u_i$, so the direction may turn. The highlight says $45$ and $5$ are eigenvalues of $A^\top A$, the squares $\sigma_i^2$, and that the lists coincide for symmetric positive semidefinite $A$ but differ in general.

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

The theorem card states Theorem 6 for every $A \in \mathbb R^{m\times n}$ with largest singular value $\sigma_1$: $\|A\|_2 = \max_{\|x\|_2 = 1}\|Ax\|_2 = \sigma_1$. Below, two columns name the proof tasks: 1, an upper bound $\|Ax\|_2 \le \sigma_1$ for every unit $x$; 2, a witness, one unit $x$ with $\|Ax\|_2 = \sigma_1$.

**Details.**

**Why two tasks.** A maximum equals $\sigma_1$ exactly when nothing exceeds $\sigma_1$ and something reaches it. The next two slides do the two tasks.

**Geometry.** On the ellipse picture, $\sigma_1$ is the longest semi-axis of the image of the unit circle.

**Definition.** $\|\cdot\|_2$ as the worst stretch was defined earlier in the lecture.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Definition 4.23 and Theorem 4.24 (proof left as an exercise there). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html, Proposition 3.11.
<!-- END S68 -->

<!-- BEGIN S69 -->
### 37. No Direction Beats the Largest Stretch [S69]

**Message.** After the orthogonal change of coordinates $y = V^\top x$, every unit input is stretched by at most $\sigma_1$.

The first line takes any unit $x \in \mathbb R^n$ and sets $y = V^\top x$, which is also a unit vector by orthogonal invariance. The two-line display chains $\|Ax\|_2^2 = \|U\Sigma y\|_2^2 = \|\Sigma y\|_2^2$ (since $U$ is orthogonal) $= \sum_{i=1}^r \sigma_i^2 y_i^2 \le \sigma_1^2\sum_{i=1}^n y_i^2 = \sigma_1^2\|y\|_2^2 = \sigma_1^2$ (since every $\sigma_i \le \sigma_1$). The muted line notes that as $x$ runs over all unit vectors so does $y$, so no direction is skipped.

**Details.**

**The inequality step.** Each term $\sigma_i^2 y_i^2 \le \sigma_1^2 y_i^2$, and extending the sum from $r$ to $n$ only adds nonnegative terms $\sigma_1^2 y_i^2$.

**Coverage.** $V^\top$ is invertible with inverse $V$, so $x \mapsto V^\top x$ is a bijection of the unit sphere onto itself; bounding over all unit $y$ is the same as bounding over all unit $x$.

**Shape.** $\Sigma y$ lies in $\mathbb R^m$ and its only nonzero coordinates are $\sigma_i y_i$ for $i \le r$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Theorem 4.24 (exercise). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html, Proposition 3.11.
<!-- END S69 -->

<!-- BEGIN S70 -->
### 38. The First Singular Vector Attains It [S70]

**Message.** The input $x = v_1$ is stretched by exactly $\sigma_1$, so together with the upper bound $\|A\|_2 = \sigma_1$.

The slide takes the unit witness $x = v_1$. The first display computes $Av_1 = U\Sigma V^\top v_1 = U\Sigma e_1 = \sigma_1 u_1$, so $\|Av_1\|_2 = \sigma_1$ because $u_1$ is a unit vector. The second display closes the argument: $\sigma_1 = \|Av_1\|_2 \le \|A\|_2 \le \sigma_1$ by the upper bound, hence $\|A\|_2 = \sigma_1$, end of proof. The muted line ties it to the picture: $\sigma_1 u_1$ is the ellipse's longest semi-axis.

**Details.**

**Step $V^\top v_1 = e_1$.** The rows of $V^\top$ are $v_1^\top, \dots, v_n^\top$, and $v_j^\top v_1 = \delta_{j1}$.

**Edge case $A = 0$.** Then $r = 0$, every $\sigma_i = 0$ and $\|A\|_2 = 0$; the identity still holds with any unit $v_1$, since $Av_1 = 0 = \sigma_1 u_1$.

**Worked example.** $\|A\|_2 = 3\sqrt5 \approx 6.71$, attained at $v_1 = (1,1)/\sqrt2$ with $Av_1 = (3,9)/\sqrt2$, whose length is $\sqrt{90/2} = \sqrt{45}$.

**Sources.**

Deisenroth, Faisal and Ong, *Mathematics for Machine Learning* (Cambridge University Press, 2020), https://mml-book.github.io/, Section 4.6, Theorem 4.24 (exercise). R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html, Proposition 3.11.
<!-- END S70 -->

<!-- BEGIN S73 -->
### 39. Frobenius Energy Sums Squared Stretches [S73]

**Message.** The total energy $\|A\|_F^2$, the sum of all squared entries, equals the sum of all squared singular values.

The theorem card states Theorem 7 for every $A \in \mathbb R^{m\times n}$ of rank $r$: $\|A\|_F^2 = \sum_{i,j} a_{ij}^2 = \sum_{i=1}^r \sigma_i^2$. A contrast line follows: $\|A\|_2 = \sigma_1$ measures the worst single direction while $\|A\|_F$ measures total energy. The muted line checks the worked example: $\|A\|_F^2 = 9 + 0 + 16 + 25 = 50 = 45 + 5$.

**Details.**

**Consequence.** $\|A\|_2 = \sigma_1 \le \|A\|_F \le \sqrt r\,\sigma_1$, since the sum has $r$ terms each at most $\sigma_1^2$. In the example, $\sqrt{45} \approx 6.71 \le \sqrt{50} \approx 7.07$.

**Definition.** $\|\cdot\|_F$ as total energy was defined earlier in the lecture.

**Sources.**

R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html, Proposition 3.10.
<!-- END S73 -->

<!-- BEGIN S74 -->
### 40. Orthogonal Coordinates Preserve Total Energy [S74]

**Message.** Orthogonal matrices on either side do not change the Frobenius norm, so $\|A\|_F = \|U^\top A V\|_F = \|\Sigma\|_F$.

The first line fixes orthogonal $Q$ and $W$ and a matrix $B$ with columns $b_j$. The two-line display proves invariance on each side. Columns: $\|QB\|_F^2 = \sum_j\|Qb_j\|_2^2 = \sum_j\|b_j\|_2^2 = \|B\|_F^2$, using vector invariance column by column. Rows, via the transpose: $\|BW\|_F = \|W^\top B^\top\|_F = \|B^\top\|_F = \|B\|_F$. The final display applies both with $Q = U^\top$ and $W = V$: $\|A\|_F^2 = \|U^\top A V\|_F^2 = \|\Sigma\|_F^2 = \sum_{i=1}^r\sigma_i^2$, end of proof.

**Details.**

**Transposition.** $\|B^\top\|_F = \|B\|_F$ because both sum the same squared entries.

**Alternative trace proof.** $\|A\|_F^2 = \operatorname{tr}(A^\top A) = \operatorname{tr}(V\Sigma^\top\Sigma V^\top) = \operatorname{tr}(\Sigma^\top\Sigma V^\top V) = \operatorname{tr}(\Sigma^\top\Sigma) = \sum_i\sigma_i^2$, using the cyclic property of the trace.

**Why $U^\top A V = \Sigma$.** Multiply $A = U\Sigma V^\top$ on the left by $U^\top$ and on the right by $V$.

**Sources.**

R. D. Wilkinson, MATH3030 *Multivariate Statistics* lecture notes, Section 3.5.1, https://rich-d-wilkinson.github.io/MATH3030/3.5-lowrank.html, Proposition 3.10 (proof via $\|U^\top A V\|_F = \|\Sigma\|_F$).
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
