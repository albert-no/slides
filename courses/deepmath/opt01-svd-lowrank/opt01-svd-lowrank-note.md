# Deep Learning Math 10: SVD and Low-Rank Approximation -- Notes

**About this file.** This is the linear-text edition of the companion note for lecture 10 of Deep Learning Math, covering the singular value decomposition and low-rank approximation. It carries the full mathematical content of that note: every definition, theorem, proof, worked number and reference. Figures and tables have been replaced by prose descriptions placed where they occurred, matrices are written out entry by entry in text, and cross-references to the accompanying presentation have been removed. Section numbering matches the original note, so a reference such as "Section 7.4" points to the same material here. Nothing else is needed to read it.

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

## 1 Why the optimization half

### 1.1 The argmin that was never solved

The probability half of the course built estimators and bounded their errors, and each one ended in an optimization problem left unsolved: maximum likelihood is $\arg\max_\theta \sum_i \log p_\theta(x_i)$ (lecture 7); empirical risk minimization is $\arg\min_{f \in \mathcal{F}} \hat R(f)$ (lecture 6); the minimum-mean-squared-error estimator is the minimizer of a squared loss over all measurable functions (lecture 7). This half of the course solves those problems. The order of the four lectures is **object** (lecture 10, this one: what is being optimized -- matrices, and what their internal structure is), **problem** (lecture 11: least squares and empirical risk minimization, which have closed-form solutions), **algorithm** (lecture 12: convexity and gradient descent, for when they do not), and **practice** (lecture 13: stochastic gradients, which is what actually runs).

### 1.2 Why a linear-algebra lecture belongs in a deep-learning course

Every learnable parameter in a modern network sits in a matrix: a dense layer is $x \mapsto Wx + b$; an embedding table is $|\mathcal{V}| \times d$; attention is three projections $W_Q, W_K, W_V$ plus an output projection. The singular value decomposition is the only factorization that exists for *every* such matrix, and Sections 5 through 7 show that the three questions one actually asks about a weight matrix -- can it be inverted, how big is it, can it be compressed -- all have answers written directly in its singular values.

The lecture's empirical claim, which the mathematics does not prove and cannot, is that on real weight matrices, embedding tables and rating matrices the singular values decay fast. The mathematics supplies the conditional statement (Theorem 8): *if* they decay fast, truncation is not merely a reasonable heuristic but the provably optimal rank-$k$ approximation.

## 2 Background: subspaces, dimension, rank

The lecture opens with span, rank and null space as recalled objects and states Theorems 1 through 3 without proof. This section supplies the whole chain. Nothing here is deep, but the proof of Theorem 8 rests entirely on it, and the one genuinely non-obvious ingredient -- the dimension formula of Section 2.3 -- is exactly the technique review the lecture flags as its second recalled tool.

### 2.1 Span, independence, basis; dimension is well defined

**Definitions.** For $v_1, \dots, v_k \in \mathbb{R}^n$, $\operatorname{span}\{v_1, \dots, v_k\} = \{\sum_i \alpha_i v_i : \alpha_i \in \mathbb{R}\}$. The list is *linearly independent* if $\sum_i \alpha_i v_i = 0$ forces every $\alpha_i = 0$. A *subspace* $W \subseteq \mathbb{R}^n$ is a nonempty set closed under addition and scalar multiplication. A *basis* of $W$ is an independent list spanning $W$, and $\dim W$ is the length of a basis.

That last definition needs a theorem to be legitimate: two bases of the same subspace could a priori have different lengths.

**Lemma 2.1 (Steinitz exchange).** If $w_1, \dots, w_p$ are linearly independent and all lie in $\operatorname{span}\{v_1, \dots, v_q\}$, then $p \leq q$.

*Proof.* Induct on $p$, exchanging one vector at a time. Suppose after $j$ steps we have a spanning list consisting of $w_1, \dots, w_j$ together with $q - j$ of the $v$'s; this is true for $j = 0$. If $j < p$, write $w_{j+1}$ in that spanning list:

$$ w_{j+1} = \sum_{i \leq j} \alpha_i w_i + \sum_{\ell} \beta_\ell v_{i_\ell} . $$

Not every $\beta_\ell$ can vanish, or $w_{j+1}$ would be a combination of $w_1, \dots, w_j$, contradicting independence; in particular the list of remaining $v$'s is nonempty, which already forces $q - j \geq 1$, that is, $j < q$. Pick $\ell$ with $\beta_\ell \neq 0$, solve for $v_{i_\ell}$, and swap it out for $w_{j+1}$: the new list still spans. After $p$ steps we have used $p$ distinct $v$'s, so $p \leq q$. **End of proof.**

Applying the lemma in both directions to two bases of $W$ gives equal lengths, so $\dim W$ is well defined. The same lemma gives the two facts used repeatedly below: any independent list in $W$ has at most $\dim W$ elements and extends to a basis of $W$, and any spanning list contains a basis.

### 2.2 Range, null space, rank

**Definitions.** For $A \in \mathbb{R}^{m \times n}$ with columns $a_1, \dots, a_n$: $\operatorname{range}(A) = \{Ax : x \in \mathbb{R}^n\} = \operatorname{span}\{a_1, \dots, a_n\} \subseteq \mathbb{R}^m$, using $Ax = \sum_i x_i a_i$; $\operatorname{null}(A) = \{x \in \mathbb{R}^n : Ax = 0\} \subseteq \mathbb{R}^n$; $\operatorname{row}(A) = \operatorname{range}(A^\top) \subseteq \mathbb{R}^n$; and $\operatorname{rank}(A) = \dim \operatorname{range}(A)$. Both $\operatorname{range}(A)$ and $\operatorname{null}(A)$ are subspaces, immediately from linearity of $x \mapsto Ax$.

The parenthetical remark "row rank $=$ column rank" is a real theorem; here is the two-line proof.

**Proposition 2.2.** $\operatorname{rank}(A^\top) = \operatorname{rank}(A)$.

*Proof.* Let $r = \operatorname{rank}(A)$ and let $u_1, \dots, u_r$ be a basis of $\operatorname{range}(A)$; write $U_0 = [u_1 \cdots u_r] \in \mathbb{R}^{m \times r}$. Each column $a_j$ lies in $\operatorname{range}(A)$, so $a_j = U_0 c_j$ for some $c_j \in \mathbb{R}^r$; stacking these, $A = U_0 C$ with $C = [c_1 \cdots c_n] \in \mathbb{R}^{r \times n}$. Then $A^\top = C^\top U_0^\top$, so every column of $A^\top$ is a combination of the $r$ columns of $C^\top$, giving $\operatorname{rank}(A^\top) \leq r$. Applying the same bound to $A^\top$ in place of $A$ gives $\operatorname{rank}(A) \leq \operatorname{rank}(A^\top)$. **End of proof.**

The factorization $A = U_0 C$ produced in that proof is worth naming: **every rank-$r$ matrix is a product of an $m \times r$ and an $r \times n$ matrix**, that is, a sum of $r$ rank-one matrices. That is the abstract form of the recommender factorization $R = TG$ of Section 8, and the reason a rank-$r$ matrix costs $r(m+n)$ numbers rather than $mn$.

### 2.3 The dimension formula, proved

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

### 2.4 Theorem 1 (rank-nullity), proved

**Theorem 1.** For $A \in \mathbb{R}^{m \times n}$, $\operatorname{rank}(A) + \dim \operatorname{null}(A) = n$, the number of *columns*.

*Proof.* Let $x_1, \dots, x_t$ be a basis of $\operatorname{null}(A)$ and extend it to a basis $x_1, \dots, x_t, y_1, \dots, y_s$ of $\mathbb{R}^n$, so $t + s = n$. It suffices to show that $Ay_1, \dots, Ay_s$ is a basis of $\operatorname{range}(A)$.

*Spanning.* Any $Ax$ with $x = \sum_i \alpha_i x_i + \sum_j \beta_j y_j$ satisfies $Ax = \sum_j \beta_j A y_j$, because $Ax_i = 0$.

*Independence.* If $\sum_j \beta_j A y_j = 0$ then $A(\sum_j \beta_j y_j) = 0$, so $\sum_j \beta_j y_j \in \operatorname{null}(A)$ and thus equals $\sum_i \alpha_i x_i$ for some $\alpha$. Then $\sum_j \beta_j y_j - \sum_i \alpha_i x_i = 0$ is a relation among basis vectors of $\mathbb{R}^n$, so every $\beta_j = 0$. Hence $\operatorname{rank}(A) = s = n - t$. **End of proof.**

The intuitive reading -- every input dimension either survives or dies, and the budget is exactly $n$ -- is literally the proof: the $y_j$ directions survive, their images forming a basis of the range, and the $x_i$ directions die. Note the asymmetry: the $n$ on the right is the column count, so nullity is measured in the *input* space.

The sanity check on the two running matrices: $A$ has rank $2$ and nullity $0$; $C$ has rank $1$ and nullity $1$, the null space being $\operatorname{span}\{(1,-1)\}$ since $Cx = 0$ if and only if $x_1 + x_2 = 0$; the $2 \times 2$ zero matrix has rank $0$ and nullity $2$.

### 2.5 Orthogonality, Gram-Schmidt, and Theorem 2

Write $\langle x, y \rangle = x^\top y$. Orthonormal lists are automatically independent: if $\sum_i \alpha_i q_i = 0$ with $\langle q_i, q_j \rangle = \delta_{ij}$, taking the inner product with $q_j$ gives $\alpha_j = 0$.

**Lemma 2.5 (Gram-Schmidt).** Every subspace $W \subseteq \mathbb{R}^n$ with $\dim W = d \geq 1$ has an orthonormal basis.

*Proof.* Take any basis $w_1, \dots, w_d$ and define recursively

$$ \tilde q_j = w_j - \sum_{i < j} \langle q_i, w_j \rangle q_i , \qquad q_j = \tilde q_j / \|\tilde q_j\| . $$

Each $\tilde q_j \neq 0$, since otherwise $w_j \in \operatorname{span}\{w_1, \dots, w_{j-1}\}$, contradicting independence; and $\langle q_i, \tilde q_j \rangle = \langle q_i, w_j \rangle - \langle q_i, w_j \rangle = 0$ for $i < j$ by induction. The spans agree at every stage. **End of proof.**

**Theorem 2 (orthogonal decomposition).** Let $W \subseteq \mathbb{R}^n$ be a subspace and $W^\perp = \{v : v^\top w = 0 \text{ for all } w \in W\}$. Then every $x \in \mathbb{R}^n$ has a *unique* decomposition $x = x_1 + x_2$ with $x_1 \in W$ and $x_2 \in W^\perp$; moreover $\dim W + \dim W^\perp = n$ and $(W^\perp)^\perp = W$.

*Proof.* $W^\perp$ is a subspace, being an intersection of kernels of the linear functionals $v \mapsto v^\top w$.

*Existence.* Take an orthonormal basis $q_1, \dots, q_d$ of $W$ by Lemma 2.5, taking $x_1 = 0$ if $d = 0$, and set $x_1 = \sum_{i=1}^d \langle q_i, x \rangle q_i$ and $x_2 = x - x_1$. Then $x_1 \in W$ and $\langle q_j, x_2 \rangle = \langle q_j, x \rangle - \langle q_j, x \rangle = 0$ for each $j$, so $x_2$ is orthogonal to $\operatorname{span}\{q_j\} = W$.

*Uniqueness.* If $x_1 + x_2 = x_1' + x_2'$ then $x_1 - x_1' = x_2' - x_2 \in W \cap W^\perp$, and any $v \in W \cap W^\perp$ satisfies $v^\top v = 0$, hence $v = 0$.

*Dimensions.* Extend $q_1, \dots, q_d$ to an orthonormal basis of $\mathbb{R}^n$ -- apply Lemma 2.5 to any extension to a basis of $\mathbb{R}^n$, noting the first $d$ vectors are unchanged. This exhibits $q_{d+1}, \dots, q_n$ as a basis of $W^\perp$: they lie in $W^\perp$, and any $v \in W^\perp$ expands as $\sum_i \langle q_i, v \rangle q_i$ with the first $d$ coefficients zero. Finally $W \subseteq (W^\perp)^\perp$ is immediate, and both have dimension $d$ by applying the count twice, so they are equal. **End of proof.**

The map $x \mapsto x_1$ is the **orthogonal projection** onto $W$; in matrix form, with $Q = [q_1 \cdots q_d]$, it is $x \mapsto QQ^\top x$. Section 5.3 and the normal equations of lecture 11 both come back to exactly this matrix.

### 2.6 Theorem 3: the four fundamental subspaces

**Theorem 3.** For $A \in \mathbb{R}^{m \times n}$: $(\operatorname{row}(A))^\perp = \operatorname{null}(A)$ and $(\operatorname{range}(A))^\perp = \operatorname{null}(A^\top)$.

*Proof.* Write $\alpha_1^\top, \dots, \alpha_m^\top$ for the rows of $A$. Then $Ax = (\alpha_1^\top x, \dots, \alpha_m^\top x)$, so $Ax = 0$ if and only if $x$ is orthogonal to every $\alpha_i$, if and only if $x$ is orthogonal to $\operatorname{span}\{\alpha_i\} = \operatorname{row}(A)$, since orthogonality to a spanning set gives orthogonality to the span by linearity. That is the first identity. The second is the first applied to $A^\top$, since $\operatorname{row}(A^\top) = \operatorname{range}(A)$. **End of proof.**

Combining with Theorem 2 and Proposition 2.2 gives the full picture: $\mathbb{R}^n = \operatorname{row}(A) \oplus \operatorname{null}(A)$ with dimensions $r$ and $n - r$, and $\mathbb{R}^m = \operatorname{range}(A) \oplus \operatorname{null}(A^\top)$ with dimensions $r$ and $m - r$. Moreover $A$ restricted to $\operatorname{row}(A)$ is a bijection onto $\operatorname{range}(A)$: it is injective, since $\operatorname{row}(A) \cap \operatorname{null}(A) = \{0\}$, and both spaces have dimension $r$. That bijection is precisely what the pseudo-inverse of Section 5 inverts. Strang's article [7] is the classic exposition of this diagram.

## 3 Norms and orthogonal matrices

### 3.1 The axioms, and what follows from them

**Definition.** A function $\|\cdot\| : \mathbb{R}^n \to \mathbb{R}$ is a *norm* if for all $x, y$ and all $\alpha \in \mathbb{R}$:

- (N1) $\|x + y\| \leq \|x\| + \|y\|$;
- (N2) $\|\alpha x\| = |\alpha| \, \|x\|$;
- (N3) $\|x\| = 0$ if and only if $x = 0$.

Nonnegativity is not an extra axiom -- it follows: $0 = \|x + (-x)\| \leq \|x\| + \|-x\| = 2\|x\|$ by (N1) and (N2). Two consequences are used later. The *reverse triangle inequality* $\big|\, \|x\| - \|y\| \,\big| \leq \|x - y\|$, obtained by applying (N1) to $x = (x - y) + y$ and symmetrically. And the fact that every norm on $\mathbb{R}^n$ is a continuous function, immediate from the reverse triangle inequality together with $\|x\| \leq \sum_i |x_i| \, \|e_i\|$. Continuity is what makes the maximum in the induced-norm definition of Section 6.1 attained rather than merely a supremum.

### 3.2 The $\ell_p$ family is a family of norms, for $p \geq 1$

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

### 3.3 Why $p \geq 1$: an explicit failure at $p < 1$

The lecture states the restriction; here is the witness. Take $p = \tfrac12$ and the vectors $x = (1,0)$ and $y = (0,1)$ in $\mathbb{R}^2$. Then $\|x\|_{1/2} = \|y\|_{1/2} = 1$, but $\|x + y\|_{1/2} = (1 + 1)^2 = 4 > 2$. So (N1) fails, decisively.

The quantity $\|x\|_0 := \#\{i : x_i \neq 0\}$, used in Sections 6 and 8 in the identity "rank $= \|\sigma\|_0$", is not a norm either: it violates (N2), since $\|2x\|_0 = \|x\|_0 \neq 2\|x\|_0$ in general. Calling these "the $\ell_{1/2}$ norm" and "the $\ell_0$ norm" is standard abuse of language. The passage from $\|\sigma\|_0$ to $\|\sigma\|_1$ in Section 8 is precisely the move from a non-norm to the nearest convex norm.

### 3.4 $\ell_\infty$ as a limit, and the ordering

**Proposition 3.4.** $\|x\|_p \to \max_i |x_i| =: \|x\|_\infty$ as $p \to \infty$, and for every $x \in \mathbb{R}^n$,

$$ \|x\|_\infty \;\leq\; \|x\|_2 \;\leq\; \|x\|_1 \;\leq\; \sqrt{n}\, \|x\|_2 \;\leq\; n \, \|x\|_\infty . $$

*Proof.* Let $M = \|x\|_\infty$. Then $M^p \leq \sum_i |x_i|^p \leq n M^p$, so $M \leq \|x\|_p \leq n^{1/p} M$, and $n^{1/p} \to 1$. For the chain: $\|x\|_\infty^2 = \max_i x_i^2 \leq \sum_i x_i^2$ gives the first inequality; squaring $\|x\|_1$ gives $\sum_i x_i^2 + \sum_{i \neq j} |x_i||x_j| \geq \|x\|_2^2$, the second; Cauchy-Schwarz against the all-ones vector, $\sum_i |x_i| \cdot 1 \leq \sqrt n \|x\|_2$, the third; and $\|x\|_2^2 \leq n \|x\|_\infty^2$ the fourth. **End of proof.**

The worked example is $x = (3,4)$: $\|x\|_1 = 7$, $\|x\|_2 = 5$, $\|x\|_\infty = 4$, consistent with $4 \leq 5 \leq 7$. The same ordering reappears in Section 6.5 applied to the vector of singular values, where it becomes $\|A\|_2 \leq \|A\|_F \leq \|A\|_*$.

### 3.5 Orthogonal matrices: the equivalent characterizations

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

**Theorem 4.** If $U$ is orthogonal then $\|Ux\|_2 = \|x\|_2$ for all $x$. Conversely, a square $U$ preserving the $\ell_2$ norm is orthogonal.

*Proof.* Both directions are the equivalence of statements 1 and 5 in Proposition 3.5. **End of proof.**

The converse is worth stating because it explains why orthogonal invariance is the master trick of this lecture: the orthogonal matrices are *exactly* the linear maps under which the $\ell_2$ geometry is invisible, which is why $U$ and $V$ can be peeled off in Theorems 6, 7 and 8. Note that this is special to $p = 2$. Rotations do change $\|x\|_1$: rotating $(1,0)$ by $45$ degrees sends its $\ell_1$ norm from $1$ to $\sqrt2$.

## 4 The singular value decomposition

### 4.1 The one imported black box

**Spectral theorem (imported).** Every symmetric $S \in \mathbb{R}^{n \times n}$ can be written $S = Q \Lambda Q^\top$ with $Q$ orthogonal and $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ real. If moreover $S$ is positive semidefinite, meaning $x^\top S x \geq 0$ for all $x$, then every $\lambda_i \geq 0$.

This is the single result these notes do not prove. It was used in the lecture-8 note for covariance matrices and is proved in any of [5, 6, 8]. A sketch, for orientation: the maximum of the continuous function $x \mapsto x^\top S x$ on the compact unit sphere is attained at some $q_1$, which is an eigenvector by a Lagrange-multiplier or first-order argument; $S$ maps the orthogonal complement of $q_1$ into itself by symmetry, so one inducts on dimension. The positive-semidefinite claim is one line: $\lambda_i = q_i^\top S q_i \geq 0$. Everything else below is proved.

### 4.2 Theorem 5: existence of the SVD, proved

**Theorem 5.** Every $A \in \mathbb{R}^{m \times n}$ with $\operatorname{rank}(A) = r$ admits a factorization $A = U \Sigma V^\top$ with $U \in \mathbb{R}^{m \times m}$ and $V \in \mathbb{R}^{n \times n}$ orthogonal, and $\Sigma \in \mathbb{R}^{m \times n}$ diagonal in the sense that $\Sigma_{ij} = 0$ for $i \neq j$, with diagonal entries $\sigma_1 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$.

*Proof.* The matrix $S = A^\top A \in \mathbb{R}^{n \times n}$ is symmetric, since $S^\top = A^\top A$, and positive semidefinite, since $x^\top S x = \|Ax\|_2^2 \geq 0$. By the spectral theorem write $S = V \Lambda V^\top$ with $V = [v_1 \cdots v_n]$ orthogonal and $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0$, reordering the columns of $V$ to sort $\Lambda$, which preserves orthogonality.

*Step 1: the number of positive eigenvalues is $r$.* We have $\|Av_i\|_2^2 = v_i^\top S v_i = \lambda_i$, so $Av_i = 0$ exactly when $\lambda_i = 0$. Hence $\operatorname{null}(A) \supseteq \operatorname{span}\{v_i : \lambda_i = 0\}$. Conversely $Ax = 0$ implies $Sx = 0$, and $Sx = 0$ with $x = \sum_i c_i v_i$ gives $\sum_i c_i \lambda_i v_i = 0$, so $c_i = 0$ whenever $\lambda_i \neq 0$. Thus $\operatorname{null}(A) = \operatorname{span}\{v_i : \lambda_i = 0\}$, and by Theorem 1 the count of positive $\lambda_i$ is $n - \dim\operatorname{null}(A) = r$. So $\lambda_1 \geq \cdots \geq \lambda_r > 0 = \lambda_{r+1} = \cdots = \lambda_n$.

*Step 2: define $\sigma_i$ and $u_i$.* For $i \leq r$ set $\sigma_i = \sqrt{\lambda_i} > 0$ and $u_i = Av_i / \sigma_i \in \mathbb{R}^m$. These are orthonormal:

$$ u_i^\top u_j = \frac{v_i^\top A^\top A v_j}{\sigma_i \sigma_j} = \frac{v_i^\top(\lambda_j v_j)}{\sigma_i \sigma_j} = \frac{\lambda_j \, \delta_{ij}}{\sigma_i \sigma_j} = \delta_{ij} . $$

Since $r \leq m$, extend $u_1, \dots, u_r$ to an orthonormal basis $u_1, \dots, u_m$ of $\mathbb{R}^m$, by Lemma 2.5 applied to a completion to a basis, and set $U = [u_1 \cdots u_m]$, which is orthogonal by Proposition 3.5.

*Step 3: verify $AV = U\Sigma$.* Let $\Sigma \in \mathbb{R}^{m \times n}$ have $\Sigma_{ii} = \sigma_i$ for $i \leq r$ and zeros elsewhere. Column $i$ of $AV$ is $Av_i$, which equals $\sigma_i u_i$ for $i \leq r$ by the definition of $u_i$, and $0$ for $i > r$ by Step 1. Column $i$ of $U\Sigma$ is $\sum_j u_j \Sigma_{ji} = \sigma_i u_i$ for $i \leq r$ and $0$ otherwise. The columns agree, so $AV = U\Sigma$, and right-multiplying by $V^\top$ gives $A = U\Sigma V^\top$. **End of proof.**

Two remarks on this "$A^\top A$ route." First, the proof is *constructive*, and is exactly the by-hand recipe of the lecture: form $A^\top A$, eigendecompose, take square roots, push through $A$. Second, it is a terrible *numerical* recipe: forming $A^\top A$ squares the condition number, so library implementations, which use Golub-Kahan bidiagonalization [8, ch. 8], never do this. The hand computation is for understanding, not for code -- in practice one calls the library routine `numpy.linalg.svd`.

### 4.3 What is unique and what is not

**Proposition 4.1.** The singular values are unique: they are the square roots of the eigenvalues of $A^\top A$, sorted. The singular *vectors* are not unique.

*Proof of the first claim.* If $A = U\Sigma V^\top$ then $A^\top A = V \Sigma^\top \Sigma V^\top$, an eigendecomposition with eigenvalues $\sigma_i^2$; the eigenvalues of a fixed matrix are the roots of its characteristic polynomial, hence determined by $A$ alone. **End of proof.**

Non-uniqueness of the vectors has two sources. *Signs:* replacing the pair $(u_i, v_i)$ by $(-u_i, -v_i)$ changes nothing, since $\sigma_i(-u_i)(-v_i)^\top = \sigma_i u_i v_i^\top$. *Repeated singular values:* if $\sigma_i = \sigma_j$ for $i \neq j$, any rotation within the corresponding two-dimensional eigenspace of $A^\top A$ yields another valid SVD -- for $A = I_2$ every orthogonal $V$ works, with $U = V$. Additionally, the columns $u_{r+1}, \dots, u_m$ are constrained only to complete an orthonormal basis.

This is why the lecture drops the source's uniqueness claim for the *minimizer* in Theorem 8: non-uniqueness enters here, at the level of the decomposition itself, and Section 7.6 shows it survives into the approximation problem.

### 4.4 Thin SVD, the rank-one expansion, and the four subspaces again

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

### 4.5 Relations worth having

All of the following are immediate from $A = U\Sigma V^\top$.

- The singular values of $A^\top$ are those of $A$: transpose the decomposition, swapping the roles of $U$ and $V$.
- $A^\top A$ and $AA^\top$ have the same nonzero eigenvalues $\sigma_1^2, \dots, \sigma_r^2$.
- If $A$ is square and invertible then $\sigma_i(A^{-1}) = 1/\sigma_{n+1-i}(A)$, so the *condition number* $\kappa(A) = \sigma_1/\sigma_n = \|A\|_2 \|A^{-1}\|_2$ measures how badly $A$ distorts the unit sphere.
- If $A$ is symmetric positive semidefinite then its eigendecomposition *is* an SVD, with $\sigma_i = \lambda_i$.
- If $A$ is symmetric but indefinite, $\sigma_i = |\lambda_i|$ after sorting, absorbing the signs into $U$.

### 4.6 The running example, recomputed

Every step of the hand computation for $A$, the matrix with first row $(3, 0)$ and second row $(4, 5)$, verified independently.

*Step 1.* $A^\top$ has first row $(3, 4)$ and second row $(0, 5)$. The product $A^\top A$ has first row $(9 + 16, 20) = (25, 20)$ and second row $(20, 25)$. Checked.

*Step 2.* $\det(A^\top A - \lambda I) = (25 - \lambda)^2 - 400$, so $25 - \lambda = \pm 20$, giving $\lambda_1 = 45$ and $\lambda_2 = 5$. Checked. Two consistency tests: the trace, $45 + 5 = 50 = 25 + 25$; and the determinant, $45 \cdot 5 = 225 = 625 - 400$.

For eigenvectors: $A^\top A - 45I$ has first row $(-20, 20)$ and second row $(20, -20)$, and solving $(A^\top A - 45I)v = 0$ gives $v_1$ proportional to $(1,1)$. Likewise $A^\top A - 5I$ has both rows equal to $(20, 20)$, and solving gives $v_2$ proportional to $(-1, 1)$. Normalized and orthogonal. Checked.

*Step 3.* $\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.7082$ and $\sigma_2 = \sqrt5 \approx 2.2361$. Checked. Then $Av_1 = \tfrac{1}{\sqrt2}(3, 9)$ with $\|Av_1\| = \tfrac{1}{\sqrt2}\sqrt{90} = \sqrt{45} = \sigma_1$ (checked), so

$$ u_1 = \frac{Av_1}{\sigma_1} = \frac{(3,9)}{\sqrt2 \cdot 3\sqrt5} = \frac{(1,3)}{\sqrt{10}} . $$

Checked. Similarly $Av_2 = \tfrac{1}{\sqrt2}(-3, 1)$ with $\|Av_2\| = \tfrac{\sqrt{10}}{\sqrt2} = \sqrt5 = \sigma_2$ (checked), so $u_2 = (-3, 1)/\sqrt{10}$. Checked.

*Step 4: the two rank-one layers.* The first layer is

$$ \sigma_1 u_1 v_1^\top = 3\sqrt5 \cdot \frac{1}{\sqrt{10}} \cdot \frac{1}{\sqrt2} \, (1,3)^\top (1,1) = \frac{3\sqrt5}{\sqrt{20}} \cdot M_1 = \tfrac32 M_1 , $$

where $M_1$ is the matrix with first row $(1,1)$ and second row $(3,3)$, using $3\sqrt5/\sqrt{20} = 3\sqrt5/(2\sqrt5) = 3/2$. So the first layer has first row $(1.5, 1.5)$ and second row $(4.5, 4.5)$. Checked.

Similarly the second layer is $\sigma_2 u_2 v_2^\top = \sqrt5 \cdot \tfrac{1}{\sqrt{20}} \cdot M_2 = \tfrac12 M_2$, where $M_2$ is the matrix with first row $(3, -3)$ and second row $(-1, 1)$; so the second layer has first row $(1.5, -1.5)$ and second row $(-0.5, 0.5)$. Checked. The two layers sum entry by entry to $(1.5 + 1.5, 1.5 - 1.5) = (3, 0)$ and $(4.5 - 0.5, 4.5 + 0.5) = (4, 5)$, which is $A$. Checked.

The coincidence that $V$ is the same $45$-degree rotation met earlier in the lecture is not an accident of exposition but of the example: $A^\top A$ has equal diagonal entries, and any symmetric matrix with first row $(a, b)$ and second row $(b, a)$ has eigenvectors $(1,1)$ and $(-1,1)$ regardless of $a$ and $b$.

### 4.7 Eigenvalues versus singular values

For the running matrix, which is lower triangular, the eigenvalues are the diagonal entries $3$ and $5$; the singular values are $6.708$ and $2.236$. Not equal, not even close. But the products agree: $3 \cdot 5 = 15 = |\det A| = \sigma_1 \sigma_2 = 3\sqrt5 \cdot \sqrt5$, and that is general.

**Proposition 4.2.** For square $A$: (a) $\prod_i \sigma_i = |\det A| = \prod_i |\lambda_i|$; (b) $\max_i |\lambda_i| \leq \sigma_1$, with equality for all $i$ simultaneously if and only if $A$ is normal, meaning $A^\top A = AA^\top$, which in the real case includes in particular every symmetric $A$.

*Proof of (a) and of the inequality in (b).* (a) $\det A = \det U \det \Sigma \det V^\top = \pm \prod_i \sigma_i$. (b) If $Ax = \lambda x$ with $\|x\| = 1$ then $|\lambda| = \|Ax\|_2 \leq \max_{\|y\| = 1} \|Ay\|_2 = \sigma_1$ by Theorem 6. The equality characterization is standard and imported, from [6, ch. 3]. **End of proof.**

The conceptual difference is this: eigenvectors are directions $A$ preserves, while right singular vectors are directions $A$ stretches most. That is why singular values are the right notion here -- eigenvalues need not exist over $\mathbb{R}$, as a $90$-degree rotation has none, and eigenvectors need not be orthogonal or even span the space, whereas the singular values and both singular bases always exist.

### 4.8 The geometry: sphere to ellipsoid

**Proposition 4.3.** $A$ maps the unit sphere $\{x : \|x\|_2 = 1\}$ onto the ellipsoid $\{\sum_{i \leq r} c_i u_i : \sum_{i \leq r} c_i^2/\sigma_i^2 \leq 1\}$, degenerating to a filled ellipsoid inside $\operatorname{range}(A)$ when $r < n$, with semi-axes $\sigma_i u_i$.

*Proof.* With $y = V^\top x$, so that $\|y\| = 1$ by Theorem 4, we have $Ax = U\Sigma y = \sum_{i \leq r} \sigma_i y_i u_i$, that is, $c_i = \sigma_i y_i$ where $\sum_{i \leq n} y_i^2 = 1$. If $r = n$ this says exactly $\sum_i c_i^2/\sigma_i^2 = 1$. If $r < n$ the coordinates $y_{r+1}, \dots, y_n$ are free, so $\sum_{i \leq r} y_i^2$ takes every value in $[0,1]$ and the image is the solid ellipsoid. **End of proof.**

This is the standard four-panel picture read algebraically: $V^\top$ rotates the sphere to itself, $\Sigma$ stretches axis $i$ by $\sigma_i$, and $U$ rotates the resulting ellipsoid into the output space. It also makes Theorem 6 geometrically obvious in advance -- the longest semi-axis has length $\sigma_1$.

## 5 The Moore-Penrose pseudo-inverse

### 5.1 The problem it solves

The inverse $A^{-1}$ exists only for square invertible $A$. For every other $A$ -- tall, wide, or rank-deficient -- the equation $Ax = b$ is either over- or under-determined, and the question is what should play the role of "solve". The SVD answers it by inverting what is invertible and leaving the rest alone: $A$ restricted to $\operatorname{row}(A)$ is a bijection onto $\operatorname{range}(A)$ by Section 2.6, so invert *that* map and extend by zero on $\operatorname{range}(A)^\perp$.

### 5.2 Definition and well-definedness

**Definition.** With the thin SVD $A = U_c \Sigma_c V_c^\top$, set

$$ A^\dagger := V_c \Sigma_c^{-1} U_c^\top = \sum_{i=1}^{r} \frac{1}{\sigma_i} v_i u_i^\top \;\in\; \mathbb{R}^{n \times m} . $$

Equivalently, $A^\dagger = V \Sigma^\dagger U^\top$ where $\Sigma^\dagger \in \mathbb{R}^{n \times m}$ transposes $\Sigma$ and inverts its nonzero entries -- the "flip and reciprocate" rule. The definition passes through a chosen SVD, which by Section 4.3 is not unique, so well-definedness needs an argument. The clean one is Penrose's.

**Theorem 5.1 (Penrose, 1955 [4]).** For each $A$ there is exactly one $X \in \mathbb{R}^{n \times m}$ satisfying the four equations

$$ \text{(P1)}\ AXA = A, \qquad \text{(P2)}\ XAX = X, \qquad \text{(P3)}\ (AX)^\top = AX, \qquad \text{(P4)}\ (XA)^\top = XA, $$

and it equals $V_c \Sigma_c^{-1} U_c^\top$ for every SVD of $A$. Consequently $A^\dagger$ does not depend on the SVD chosen.

*Existence.* Put $X = V_c \Sigma_c^{-1} U_c^\top$ and use $U_c^\top U_c = V_c^\top V_c = I_r$. Then $AX = U_c \Sigma_c V_c^\top V_c \Sigma_c^{-1} U_c^\top = U_c U_c^\top$, which is symmetric, giving (P3); symmetrically $XA = V_c V_c^\top$, giving (P4). Then $AXA = U_c U_c^\top U_c \Sigma_c V_c^\top = U_c \Sigma_c V_c^\top = A$, which is (P1), and $XAX = V_c V_c^\top V_c \Sigma_c^{-1} U_c^\top = X$, which is (P2).

*Uniqueness.* Let $X$ and $Y$ both satisfy (P1) through (P4). Then

$$ X = XAX = X(AX)^\top = XX^\top A^\top = XX^\top (AYA)^\top = XX^\top A^\top (AY)^\top = X(AX)^\top AY = XAXAY = XAY , $$

and symmetrically $Y = XAY$, running the same chain from $Y = YAY$ using (P4) and $A = AXA$. Hence $X = Y$. **End of proof.**

### 5.3 $AA^\dagger$ and $A^\dagger A$ are projections

The proof just computed the two products: $AA^\dagger = U_c U_c^\top$ and $A^\dagger A = V_c V_c^\top$. By the projection formula in Theorem 2 these are the orthogonal projections onto $\operatorname{range}(A)$ and $\operatorname{row}(A)$ respectively -- symmetric, idempotent, since $(U_c U_c^\top)^2 = U_c (U_c^\top U_c) U_c^\top = U_c U_c^\top$, and with the stated ranges by Section 4.4.

So the slogan "$A^\dagger$ is an inverse only where inversion is possible" is literally true: $A^\dagger A = I_n$ if and only if $r = n$ (full column rank); $AA^\dagger = I_m$ if and only if $r = m$ (full row rank); and both hold if and only if $A$ is invertible, in which case $A^\dagger = A^{-1}$, by uniqueness in Theorem 5.1, since $X = A^{-1}$ satisfies (P1) through (P4).

Two closed forms follow, used constantly in lecture 11. If $A$ has full column rank then $A^\top A$ is invertible and $A^\dagger = (A^\top A)^{-1}A^\top$. If $A$ has full row rank then $A^\dagger = A^\top(AA^\top)^{-1}$.

*Proof of the first.* $A^\top A = V_c \Sigma_c^2 V_c^\top$ with $V_c$ square orthogonal when $r = n$, so $(A^\top A)^{-1}A^\top = V_c \Sigma_c^{-2} V_c^\top V_c \Sigma_c U_c^\top = V_c \Sigma_c^{-1} U_c^\top = A^\dagger$. The second is the transpose statement, using $(A^\dagger)^\top = (A^\top)^\dagger$, which follows by transposing the definition.

### 5.4 The two worked examples, verified

**Invertible case: $A$, with rows $(3,0)$ and $(4,5)$.** Here $\det A = 15 \neq 0$, so $A^\dagger = A^{-1} = \tfrac{1}{15} N$, where $N$ has first row $(5, 0)$ and second row $(-4, 3)$. Check: the product $AN$ has first row $(15, 0)$ and second row $(20 - 20, 15) = (0, 15)$, so $\tfrac{1}{15}AN = I$. Checked. Its singular values are $1/\sigma_2 = 1/\sqrt5$ and $1/\sigma_1 = 1/(3\sqrt5)$, consistent with Section 4.5.

**Singular case: $C$, with both rows proportional, namely $(1,1)$ and $(2,2)$.** Here $\operatorname{rank} C = 1$ and $C = \sigma_1 u_1 v_1^\top$ with $v_1 = \tfrac{1}{\sqrt2}(1,1)$, $u_1 = \tfrac{1}{\sqrt5}(1,2)$ and $\sigma_1 = \sqrt{10}$, since $C^\top C$ has both rows equal to $(5,5)$ and therefore eigenvalues $10$ and $0$. Hence

$$ C^\dagger = \frac{1}{\sigma_1} v_1 u_1^\top = \frac{1}{\sqrt{10}} \cdot \frac{1}{\sqrt{10}} \, (1,1)^\top (1,2) = \frac{1}{10} P , $$

where $P$ has first row $(1, 2)$ and second row $(1, 2)$; this matches the lecture.

The two products. First, $CC^\dagger = \tfrac{1}{10}$ times the product of $C$ and $P$, which has first row $(2, 4)$ and second row $(4, 8)$; so $CC^\dagger = \tfrac15$ times the matrix with rows $(1,2)$ and $(2,4)$, which is $u_1 u_1^\top$. Checked -- symmetric, idempotent, rank one, projecting onto $\operatorname{span}\{(1,2)\} = \operatorname{range}(C)$. Second, $C^\dagger C = \tfrac{1}{10}$ times the product of $P$ and $C$, which has both rows equal to $(5,5)$; so $C^\dagger C = \tfrac12$ times the all-ones $2 \times 2$ matrix, which is $v_1 v_1^\top$. Checked. Neither product is the identity: $C$ is not invertible, and the pseudo-inverse recovers only the row-space component.

### 5.5 What $A^\dagger b$ actually optimizes

The lecture defers the variational meaning to lecture 11; it is stated here because it is what makes the pseudo-inverse more than a formal gadget.

**Theorem 5.2.** For any $A \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$, the vector $x^\star = A^\dagger b$ is a minimizer of $\|Ax - b\|_2$, and among all minimizers it is the unique one of smallest $\|x\|_2$.

*Proof.* Write $b = AA^\dagger b + (I - AA^\dagger)b =: b_\parallel + b_\perp$, an orthogonal split by Section 5.3 with $b_\parallel \in \operatorname{range}(A)$. For any $x$, $Ax - b = (Ax - b_\parallel) - b_\perp$ with the two terms orthogonal, so

$$ \|Ax - b\|_2^2 = \|Ax - b_\parallel\|_2^2 + \|b_\perp\|_2^2 \;\geq\; \|b_\perp\|_2^2 , $$

with equality if and only if $Ax = b_\parallel$. And $Ax^\star = AA^\dagger b = b_\parallel$, so $x^\star$ attains it.

The full minimizer set is $x^\star + \operatorname{null}(A)$. Since $x^\star = V_c \Sigma_c^{-1} U_c^\top b \in \operatorname{row}(A) = \operatorname{null}(A)^\perp$, Pythagoras gives $\|x^\star + z\|_2^2 = \|x^\star\|_2^2 + \|z\|_2^2$ for $z \in \operatorname{null}(A)$, minimized uniquely at $z = 0$. **End of proof.**

So $A^\dagger$ is simultaneously the least-squares solver -- the normal equations of lecture 11, in the full-column-rank case $A^\dagger = (A^\top A)^{-1}A^\top$ -- and the minimum-norm solver, the implicit regularizer that reappears in lecture 13 as the bias of gradient descent started from zero initialization.

### 5.6 A caution: the map $A \mapsto A^\dagger$ is discontinuous

Let $A_\varepsilon = \operatorname{diag}(1, \varepsilon)$. Then $A_\varepsilon^\dagger = \operatorname{diag}(1, 1/\varepsilon)$, which blows up as $\varepsilon \to 0^+$, while $A_0 = \operatorname{diag}(1,0)$ has $A_0^\dagger = \operatorname{diag}(1,0)$. So $A_\varepsilon \to A_0$ but $A_\varepsilon^\dagger$ does not converge to $A_0^\dagger$.

This is why numerical software never tests $\sigma_i = 0$ exactly but truncates at a tolerance, typically $\max(m,n) \cdot \varepsilon_{\text{mach}} \cdot \sigma_1$, and why the rank-$k$ truncation of Section 7 is the numerically stable object while "the rank" is not.

## 6 Matrix norms

### 6.1 Induced norms: definition, attainment, submultiplicativity

**Definition.** For a vector norm $\|\cdot\|_p$, the induced (operator) norm is

$$ \|A\|_p := \max_{\|x\|_p = 1} \|Ax\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p} . $$

The maximum is attained, not merely approached: $x \mapsto \|Ax\|_p$ is continuous by Section 3.1 and the unit sphere is compact. The two expressions agree by homogeneity, $\|A(x/\|x\|)\| = \|Ax\|/\|x\|$.

Induced norms satisfy the norm axioms -- (N1) from $\|(A+B)x\| \leq \|Ax\| + \|Bx\|$ pointwise, then maximizing; (N3) because $\|A\| = 0$ forces $Ae_i = 0$ for all $i$ -- and additionally the two properties that make them useful for error analysis:

$$ \|Ax\|_p \leq \|A\|_p \|x\|_p \quad \text{(consistency)}, \qquad \|AB\|_p \leq \|A\|_p \|B\|_p \quad \text{(submultiplicativity)}. $$

Consistency is the definition rescaled; submultiplicativity follows by applying it twice, $\|ABx\| \leq \|A\| \|Bx\| \leq \|A\| \|B\| \|x\|$, then maximizing over $\|x\| = 1$. Also $\|I\|_p = 1$ for every induced norm -- a property the Frobenius norm lacks, since $\|I_n\|_F = \sqrt n$, which is the first sign that $\|\cdot\|_F$ is not induced by any vector norm for $n > 1$.

### 6.2 The $p = 1$ and $p = \infty$ formulas

Not covered in the lecture but standard, and useful as a contrast to how much harder $p = 2$ is:

$$ \|A\|_1 = \max_j \sum_i |a_{ij}| \quad \text{(largest absolute column sum)}, \qquad \|A\|_\infty = \max_i \sum_j |a_{ij}| \quad \text{(largest absolute row sum)}. $$

*Proof of the first.* $\|Ax\|_1 = \sum_i |\sum_j a_{ij}x_j| \leq \sum_j |x_j| \sum_i |a_{ij}| \leq (\max_j \sum_i |a_{ij}|)\|x\|_1$, with equality at $x = e_{j^\star}$ for the maximizing column. The second is the same argument transposed.

Both are read off the entries in $O(mn)$ time, whereas $\|A\|_2$ requires the SVD, which is $O(mn\min(m,n))$ -- the practical reason the Frobenius norm is often used as a cheap proxy.

### 6.3 Theorem 6: the spectral norm is $\sigma_1$

**Theorem 6.** $\|A\|_2 = \sigma_1(A)$, attained at $x = v_1$.

*Proof.* Let $A = U\Sigma V^\top$ and let $\|x\|_2 = 1$. Put $y = V^\top x$, so $\|y\|_2 = 1$ by Theorem 4. Then, again by Theorem 4 applied to $U$,

$$ \|Ax\|_2^2 = \|U\Sigma y\|_2^2 = \|\Sigma y\|_2^2 = \sum_{i \leq r} \sigma_i^2 y_i^2 \;\leq\; \sigma_1^2 \sum_i y_i^2 = \sigma_1^2 . $$

So $\|A\|_2 \leq \sigma_1$. For the reverse, $x = v_1$ gives $y = e_1$ and $\|Av_1\|_2 = \sigma_1$. **End of proof.**

The two-line structure -- peel off $U$ and $V$ by orthogonal invariance, reduce to a diagonal problem, read off the answer -- is the master trick of this lecture, and Theorems 7 and 8 are the same trick twice more.

### 6.4 The Frobenius norm and Theorem 7

Define $\|A\|_F := (\sum_{i,j} a_{ij}^2)^{1/2}$: the Euclidean norm of the matrix read as a vector in $\mathbb{R}^{mn}$. Hence it is a norm for free, being $\ell_2$ under that identification, and it comes with an inner product $\langle A, B \rangle = \operatorname{tr}(A^\top B) = \sum_{i,j} a_{ij}b_{ij}$, so that $\|A\|_F^2 = \operatorname{tr}(A^\top A)$.

**Theorem 7.** $\|A\|_F = (\sum_{i=1}^{r}\sigma_i^2)^{1/2}$, and more generally $\|UAV\|_F = \|A\|_F$ for orthogonal $U$ and $V$.

*Proof.* Using $\operatorname{tr}(XY) = \operatorname{tr}(YX)$:

$$ \|UAV\|_F^2 = \operatorname{tr}(V^\top A^\top U^\top U A V) = \operatorname{tr}(V^\top A^\top A V) = \operatorname{tr}(A^\top A V V^\top) = \operatorname{tr}(A^\top A) = \|A\|_F^2 . $$

Applying this with the SVD, $\|A\|_F = \|U^\top A V\|_F = \|\Sigma\|_F = (\sum_i \sigma_i^2)^{1/2}$. **End of proof.**

Check on the running example: $\|A\|_F = \sqrt{9 + 0 + 16 + 25} = \sqrt{50} = 5\sqrt2 \approx 7.07$, and $\sqrt{\sigma_1^2 + \sigma_2^2} = \sqrt{45 + 5} = \sqrt{50}$. Checked. The identity $\sum_i \sigma_i^2 = \sum_{i,j} a_{ij}^2$ is the "energy" bookkeeping used in Section 7.5: it lets a truncation error be quoted as a fraction of total energy.

### 6.5 The nuclear norm is a norm

Define $\|A\|_* := \sum_{i=1}^{r}\sigma_i$. Axioms (N2) and (N3) are easy -- $\sigma_i(\alpha A) = |\alpha|\sigma_i(A)$ from the SVD, and $\|A\|_* = 0$ forces $r = 0$ -- but (N1) is not obvious, because singular values of a sum are not sums of singular values. The efficient route is a variational formula, which also gives the duality used in Section 8.

**Proposition 6.1.** $\displaystyle \|A\|_* = \max_{\|Z\|_2 \leq 1} \operatorname{tr}(Z^\top A)$.

*Proof, direction "at least".* Take $Z = U_c V_c^\top$, which has all its nonzero singular values equal to $1$, so $\|Z\|_2 = 1$; then

$$ \operatorname{tr}(Z^\top A) = \operatorname{tr}(V_c U_c^\top U_c \Sigma_c V_c^\top) = \operatorname{tr}(\Sigma_c V_c^\top V_c) = \operatorname{tr}(\Sigma_c) = \sum_i \sigma_i . $$

*Direction "at most".* For any $Z$ with $\|Z\|_2 \leq 1$, write $A = \sum_i \sigma_i u_i v_i^\top$ and use linearity of the trace:

$$ \operatorname{tr}(Z^\top A) = \sum_i \sigma_i \operatorname{tr}(Z^\top u_i v_i^\top) = \sum_i \sigma_i \, v_i^\top Z^\top u_i \;\leq\; \sum_i \sigma_i \|Zv_i\|_2 \|u_i\|_2 \;\leq\; \sum_i \sigma_i , $$

by Cauchy-Schwarz and consistency. **End of proof.**

**Corollary 6.2.** The nuclear norm satisfies the triangle inequality, hence is a norm.

*Proof.* For any admissible $Z$, $\operatorname{tr}(Z^\top(A+B)) = \operatorname{tr}(Z^\top A) + \operatorname{tr}(Z^\top B) \leq \|A\|_* + \|B\|_*$; now maximize the left side over $Z$. **End of proof.**

The same argument shows $\|\cdot\|_*$ is convex, being a pointwise maximum of linear functions of $A$ -- exactly the property Section 8 needs, and the reason the proof was routed through the variational formula rather than through Weyl-type inequalities.

Proposition 6.1 says $\|\cdot\|_*$ and $\|\cdot\|_2$ are *dual norms* with respect to the trace inner product; the Frobenius norm is self-dual. In the language of Section 3, applying the vector chain $\|\sigma\|_\infty \leq \|\sigma\|_2 \leq \|\sigma\|_1$ to the singular-value vector gives

$$ \|A\|_2 \;\leq\; \|A\|_F \;\leq\; \|A\|_* \;\leq\; \sqrt{r}\, \|A\|_F \;\leq\; r \, \|A\|_2 . $$

Running example: $\|A\|_2 = 6.71 \leq \|A\|_F = 7.07 \leq \|A\|_* = 3\sqrt5 + \sqrt5 = 4\sqrt5 \approx 8.94$. Checked.

### 6.6 The three norms as $\ell_p$ norms of the singular-value vector

The punchline -- spectral $= \|\sigma\|_\infty$, Frobenius $= \|\sigma\|_2$, nuclear $= \|\sigma\|_1$, rank $= \|\sigma\|_0$ -- is the organizing fact of the rest of the lecture. All three norms are *unitarily invariant*, meaning $\|UAV\| = \|A\|$ for orthogonal $U, V$, because they depend on $A$ only through $\sigma$. Von Neumann's theorem states the converse: every unitarily invariant matrix norm is a symmetric gauge function of $\sigma$. That is the setting of Mirsky's version of Eckart-Young in Section 7.5, which is why one proof covers all three.

The rank/nuclear pairing is the matrix analogue of the sparsity/$\ell_1$ pairing in compressed sensing: $\|\sigma\|_0$ counts, while $\|\sigma\|_1$ is the tightest convex function that under-approximates it on a bounded set. Fazel [12] made this precise.

**Theorem 6.3 (Fazel, 2002).** On the set $\{X : \|X\|_2 \leq 1\}$, the convex envelope of $X \mapsto \operatorname{rank}(X)$ is $X \mapsto \|X\|_*$.

The convex envelope is the largest convex function lying below the target; the proof computes the biconjugate using Proposition 6.1. It is stated without proof here; see [12] and the exposition in [13]. On the set $\{\|X\|_2 \leq \tau\}$ the envelope is $\|X\|_*/\tau$, so the scale matters -- a point elided when the relaxation is written down casually.

The one-line intuition: rank is blind to the size of the singular values and only counts them, so it is flat and non-convex; the nuclear norm pays proportionally, which is convex, and driving a singular value to zero is rewarded continuously rather than only in the limit.

## 7 Low-rank approximation: Eckart-Young-Mirsky

### 7.1 The problem and the candidate

Fix $A \in \mathbb{R}^{m \times n}$ of rank $r$ and an integer $k < r$. The problem is

$$ \min_{B \,:\, \operatorname{rank}(B) \,\leq\, k} \ \|A - B\| $$

for a unitarily invariant norm. The feasible set is *not* convex: $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$ both have rank $1$, but their midpoint $\tfrac12 I_2$ has rank $2$. So nothing from convex optimization applies, and yet the problem has a clean closed-form solution. That is the surprise.

The candidate is the **truncated SVD**

$$ A_k \;:=\; \sum_{i=1}^{k}\sigma_i u_i v_i^\top \;=\; U\Sigma_k V^\top, \qquad \Sigma_k = \operatorname{diag}(\sigma_1, \dots, \sigma_k, 0, \dots, 0), $$

which has rank exactly $k$, its nonzero singular values being $\sigma_1, \dots, \sigma_k$. Its errors are read off immediately from Theorems 6 and 7 applied to $A - A_k = \sum_{i > k}\sigma_i u_i v_i^\top$:

$$ \|A - A_k\|_2 = \sigma_{k+1}, \qquad \|A - A_k\|_F = \Big(\sum_{i > k}\sigma_i^2\Big)^{1/2}, \qquad \|A - A_k\|_* = \sum_{i > k}\sigma_i . $$

The theorem is that no other matrix of rank at most $k$ does better, in any of the three norms.

### 7.2 Courant-Fischer for singular values

Both proofs below rest on a variational characterization; it is proved here rather than cited because everything downstream is a two-line consequence of it.

**Lemma 7.1 (min-max and max-min).** For $1 \leq i \leq \min(m,n)$,

$$ \sigma_i(A) \;=\; \max_{\substack{S \subseteq \mathbb{R}^n \\ \dim S = i}} \ \min_{\substack{x \in S \\ \|x\|_2 = 1}} \|Ax\|_2 \;=\; \min_{\substack{T \subseteq \mathbb{R}^n \\ \dim T = n-i+1}} \ \max_{\substack{x \in T \\ \|x\|_2 = 1}} \|Ax\|_2 . $$

*Proof of the first equality; the second is analogous.*

For the lower bound on the outer maximum, take $S_0 = \operatorname{span}\{v_1, \dots, v_i\}$. For unit $x \in S_0$ we have $x = \sum_{j \leq i} c_j v_j$ with $\sum_j c_j^2 = 1$, and $\|Ax\|_2^2 = \sum_{j \leq i}\sigma_j^2 c_j^2 \geq \sigma_i^2$, since $\sigma_j \geq \sigma_i$ for $j \leq i$. So the inner minimum over $S_0$ is at least $\sigma_i$, and in fact equals it, at $x = v_i$.

For the upper bound over every $S$, let $\dim S = i$ and put $W = \operatorname{span}\{v_i, v_{i+1}, \dots, v_n\}$, of dimension $n - i + 1$. By the dimension count in Corollary 2.4, $\dim(S \cap W) \geq \dim S + \dim W - n = 1$, so there is a unit vector $x \in S \cap W$. Writing $x = \sum_{j \geq i} c_j v_j$ gives $\|Ax\|_2^2 = \sum_{j \geq i}\sigma_j^2 c_j^2 \leq \sigma_i^2$. Hence the inner minimum over $S$ is at most $\sigma_i$. **End of proof.**

Note the mechanism: a dimension count forces two subspaces to intersect. That single idea drives Theorem 8, Lemma 7.3 and Theorem 9 alike.

### 7.3 Theorem 8: the spectral-norm case, proved

**Theorem 8 (Eckart-Young, spectral norm).** For every $B$ with $\operatorname{rank}(B) \leq k$, $\|A - B\|_2 \geq \sigma_{k+1} = \|A - A_k\|_2$.

*Proof.* By Theorem 1, $\dim\operatorname{null}(B) \geq n - k$. Let $W = \operatorname{span}\{v_1, \dots, v_{k+1}\}$, of dimension $k+1$. Then

$$ \dim\big(\operatorname{null}(B) \cap W\big) \;\geq\; (n-k) + (k+1) - n \;=\; 1 , $$

so choose a unit vector $x \in \operatorname{null}(B) \cap W$. Since $Bx = 0$,

$$ \|A - B\|_2^2 \;\geq\; \|(A-B)x\|_2^2 \;=\; \|Ax\|_2^2 \;=\; \Big\|\sum_{i \leq k+1}\sigma_i (v_i^\top x)\, u_i\Big\|_2^2 \;=\; \sum_{i \leq k+1}\sigma_i^2 (v_i^\top x)^2 \;\geq\; \sigma_{k+1}^2 , $$

using $x \in W$, so that $v_i^\top x = 0$ for $i > k+1$; orthonormality of the $u_i$; and $\sum_{i \leq k+1}(v_i^\top x)^2 = \|x\|_2^2 = 1$ with $\sigma_i \geq \sigma_{k+1}$ throughout. Since $A_k$ attains $\sigma_{k+1}$, it is optimal. **End of proof.**

The result is usually attributed to Eckart and Young [1], who proved the Frobenius case in 1936; Mirsky [2] gave the general unitarily-invariant statement in 1960, and Erhard Schmidt [3] had proved the analogous theorem for integral operators already in 1907. See [9] for the tangled history of who proved what.

### 7.4 The Frobenius case, proved

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

### 7.5 Energy accounting and the running example

Theorem 7 licenses reporting truncation quality as a fraction of "energy": $\|A_k\|_F^2 / \|A\|_F^2 = \sum_{i \leq k}\sigma_i^2 / \sum_{i \leq r}\sigma_i^2$. For the running $A$, the rank-one truncation captures $\sigma_1^2/(\sigma_1^2 + \sigma_2^2) = 45/50 = 90\%$, with $A_1$ having first row $(1.5, 1.5)$ and second row $(4.5, 4.5)$, and the residual $A - A_1$ having first row $(1.5, -1.5)$ and second row $(-0.5, 0.5)$, so that

$$ \|A - A_1\|_2 = \|A - A_1\|_F = \sigma_2 = \sqrt5 . $$

The coincidence that the two norms agree here is not general; it holds because $A - A_1$ has rank one, so its singular-value vector has a single nonzero entry and all $\ell_p$ norms of it agree. Check independently: $\|A - A_1\|_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$. Checked.

Two standard consequences.

*Storage.* Keeping $A_k$ costs $k(m+n)$ numbers, or $k(m+n+1)$ with the $\sigma_i$ stored separately, versus $mn$ for the full matrix -- a win as soon as $k < mn/(m+n)$.

*Principal component analysis.* If the rows of $A$ are mean-centred data points, then $A^\top A$ is proportional to the sample covariance, the $v_i$ are the principal directions, the quantities $\sigma_i^2/(m-1)$ are the explained variances, and Theorem 8F says that projecting onto the top $k$ principal directions is the rank-$k$ projection of least squared reconstruction error. The "90 percent of variance explained" convention is the energy ratio above.

### 7.6 Uniqueness: the claim the lecture drops

The source asserts that $A_k$ is *the* minimizer. As stated for the spectral norm that is false, and the lecture is right to omit it.

Counterexample: $A = \operatorname{diag}(2,1)$ and $k = 1$, so $\sigma_2 = 1$ and the optimal value is $1$. Take $B_a = \operatorname{diag}(a, 0)$ for any $a \in [1,3]$. Then $A - B_a = \operatorname{diag}(2-a, 1)$, whose singular values are $|2-a| \leq 1$ and $1$, so $\|A - B_a\|_2 = 1$, which is optimal -- while $A_1 = \operatorname{diag}(2,0)$ is only the case $a = 2$. A whole interval of minimizers.

**Proposition 7.4.** In the Frobenius norm the minimizer is unique if and only if $\sigma_k > \sigma_{k+1}$.

*Sketch.* The proof of Theorem 8F is tight only when $\sigma_i(A-B) = \sigma_{i+k}(A)$ for all $i$, which forces $B$ to be a truncation at a spectral gap. If $\sigma_k = \sigma_{k+1}$ the corresponding singular subspace has dimension greater than $1$, and any $k$-dimensional subspace of it gives another minimizer -- as for $A = I_2$ with $k = 1$, where every $vv^\top$ with $\|v\| = 1$ is optimal. In the spectral norm uniqueness fails even with a strict gap, by the counterexample above.

## 8 Matrix completion and the nuclear-norm relaxation

### 8.1 The recommender toy example, unpacked

The lecture's $5 \times 4$ user-by-movie rating matrix has five users -- Alice, Bob, Carol, Dave, Eve -- rating four films, the first two of which are action films and the last two dramas. Alice and Bob rate the action films $5$ and the dramas $1$; Carol and Dave do the reverse; Eve's row is $(4, 4, 2, 2)$.

The exhibited factorization is $R = TG$, where the taste matrix $T \in \mathbb{R}^{5 \times 2}$ has rows $(1, 0)$, $(1, 0)$, $(0, 1)$, $(0, 1)$ and $(0.75, 0.25)$, and the genre matrix $G \in \mathbb{R}^{2 \times 4}$ has first row $(5, 5, 1, 1)$ and second row $(1, 1, 5, 5)$.

Eve's row is then $0.75 \cdot (5,5,1,1) + 0.25 \cdot (1,1,5,5) = (4,4,2,2)$. Checked. So $\operatorname{rank}(R) = 2$, and the storage claim is $5 \cdot 2 + 2 \cdot 4 = 18$ numbers against $20$ -- a deliberately unimpressive ratio at this size, which becomes $500{,}000 \cdot 50 + 50 \cdot 20{,}000 = 26$ million against $10$ billion at the scale of a real streaming service.

The two latent columns are not labelled "action" and "drama" by the algorithm. The factorization is determined only up to $T \mapsto TM$ and $G \mapsto M^{-1}G$ for invertible $M$, so any interpretation of individual factors is imposed by the reader, not recovered. This non-identifiability is the honest version of the "taste vectors" story.

### 8.2 The completion problem, and why Section 7 does not apply

In practice one observes $R_{ij}$ only for $(i,j) \in \Omega$ -- for the Netflix data, about $1\%$ of entries -- and wants

$$ \min_{X} \ \operatorname{rank}(X) \quad \text{subject to} \quad X_{ij} = R_{ij} \ \text{ for all } (i,j) \in \Omega , $$

or its noisy variant, minimizing $\operatorname{rank}(X)$ subject to $\sum_{(i,j) \in \Omega}(X_{ij} - R_{ij})^2 \leq \delta$.

Eckart-Young does not solve this. Theorem 8 answers the question "what is the best rank-$k$ approximation to a *fully known* $A$"; here most of $A$ is missing, and the truncated SVD of a matrix with holes is not defined. Worse, the problem is genuinely hard.

**Theorem 9 (hardness, imported).** Deciding whether there is a completion of rank at most $k$ is NP-hard in general; the case $k = 3$ already encodes graph colourability. Even the weaker task of approximating the minimum rank within a constant factor is hard under standard assumptions [15].

So the exact problem is out of reach, and a relaxation is not a convenience but a necessity.

### 8.3 The relaxation

Replace the objective by its convex envelope, using Theorem 6.3:

$$ \min_{X} \ \|X\|_* \quad \text{subject to} \quad X_{ij} = R_{ij} \ \text{ for all } (i,j) \in \Omega , $$

or, in penalized form, minimize $\tfrac12\sum_{(i,j) \in \Omega}(X_{ij} - R_{ij})^2 + \lambda\|X\|_*$.

This is a convex program -- a semidefinite program, in fact, via the identity $\|X\|_* = \min\{\tfrac12(\operatorname{tr}W_1 + \operatorname{tr}W_2)\}$ over all $W_1, W_2$ for which the block matrix with first block row $(W_1, X)$ and second block row $(X^\top, W_2)$ is positive semidefinite [13] -- and hence solvable to global optimality. The nontrivial question is whether its solution is the matrix one actually wanted.

**Theorem 10 (Candes-Recht 2009; Candes-Tao 2010; Recht 2011).** Let $R$ be $n_1 \times n_2$ of rank $r$ satisfying a standard *incoherence* condition, meaning its singular vectors are not concentrated on few coordinates, and let $\Omega$ be a uniformly random set of $|\Omega|$ entries. If $|\Omega|$ is at least of order $\mu\, r\, n \log^2 n$ with $n = \max(n_1, n_2)$, then with high probability $R$ is the *unique* solution of the nuclear-norm program.

Stated without proof; see [10, 11, 14]. Two caveats the headline hides. First, incoherence genuinely excludes matrices like $e_1 e_1^\top$, which no sampling scheme can recover, since almost every observed entry is $0$ and carries no information about the one nonzero entry. Second, "uniformly random $\Omega$" is false for ratings data, where missingness correlates with the rating itself -- people watch what they expect to like. The theory explains why the method works at all, not why it works on real ratings data.

### 8.4 How it is solved, in one paragraph

The workhorse for the penalized form is *singular value thresholding* [14]: the proximal operator of $\lambda\|\cdot\|_*$ is soft-thresholding of the singular values,

$$ \operatorname{prox}_{\lambda\|\cdot\|_*}(Y) \;=\; \arg\min_X \ \tfrac12\|X - Y\|_F^2 + \lambda\|X\|_* \;=\; U \operatorname{diag}\big((\sigma_i - \lambda)_{+}\big) V^\top , $$

which follows from unitary invariance -- Theorem 7 -- reducing the problem to the diagonal case, and then to $n$ independent scalar problems $\min_x \tfrac12(x - \sigma)^2 + \lambda|x|$. Iterating a gradient step on the data-fit term with this proximal operator is proximal gradient descent, exactly the algorithm class of lecture 12, and gives the singular value thresholding algorithm.

At industrial scale the SVD per iteration is itself too expensive, so production systems instead parametrize $X = TG^\top$ with $T$ and $G$ tall and run alternating least squares or stochastic gradient descent on the factors [17]. That is non-convex, has no recovery guarantee of the above kind, and works well anyway. The winning Netflix Prize entry was an ensemble built around exactly such latent-factor models [17].

### 8.5 Historical footnote

Netflix announced its one-million-dollar prize in October 2006, for a $10\%$ improvement in root-mean-square error over its in-house Cinematch predictor on a held-out set. The prize was awarded in September 2009 to the team BellKor's Pragmatic Chaos, at a $10.06\%$ improvement. The contest is the reason matrix factorization became standard practice in recommender systems, and it is a fair characterization that its most durable legacy was methodological rather than deployed -- Netflix reported never putting the winning ensemble into production, as its engineering cost outweighed the accuracy gain.

### 8.6 Where this goes next

The same low-rank idea reappears throughout the second half of the course and beyond it.

*Compression:* replacing a weight matrix $W$ by $W_k$ costs $k(m+n)$ parameters.

*Low-rank adaptation (LoRA) [18]:* freeze $W$ and train an additive low-rank update $W + BA$ with $B \in \mathbb{R}^{m \times k}$ and $A \in \mathbb{R}^{k \times n}$, with $k$ in the single or double digits -- the dominant fine-tuning method for large models, and a direct application of the principle that the interesting part of a matrix is often low-rank.

*Embeddings:* word and item embeddings are low-rank factorizations of co-occurrence matrices.

In each case Section 7 supplies the guarantee that truncation is optimal, and Section 8 the machinery for when the matrix is only partly observed.

## 9 What the lecture leaves out

- **The spectral theorem** is used, in Theorem 5, and not proved, either here or in the lecture. It is the only imported ingredient; Section 4.1 sketches it and [5, 6, 8] prove it.
- **Complex matrices.** Everything above is stated over $\mathbb{R}$, with transposes and the word "orthogonal". Over $\mathbb{C}$, replace the transpose by the conjugate transpose $A^*$ and "orthogonal" by "unitary"; every statement and proof carries over verbatim, and this is why the literature says "unitarily invariant norm".
- **Numerical computation of the SVD.** The $A^\top A$ route proved in Section 4.2 is a proof technique, not an algorithm; production code uses Golub-Kahan bidiagonalization plus an implicit QR sweep [8, ch. 8], and randomized sketching [19] for the large-$k$-truncation case. Section 5.6 explains why the exact-rank test never appears in code.
- **Convergence rates for singular value thresholding and proximal gradient methods.** Deferred to lecture 12, where convexity and gradient descent are developed.
- **Proof of Theorem 6.3** (convex envelope) and of Theorem 10 (exact recovery). Both are cited, not proved; they are the subject of [12] and of [10, 11] respectively.
- **Von Neumann's characterization** of unitarily invariant norms as symmetric gauge functions, used to state Theorem 8M in full generality; see [6, ch. 3].
- **The source's uniqueness claim** for the low-rank minimizer is dropped by the lecture and refuted in Section 7.6; the correct statement is Proposition 7.4.

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
