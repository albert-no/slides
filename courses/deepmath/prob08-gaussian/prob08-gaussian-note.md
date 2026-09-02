# Deep Learning Math 8: The Multivariate Gaussian

**About this file.** This is the accessible edition of the Lecture 8 companion
notes, written to be read straight through with a screen reader or a braille
display. It is plain text with all mathematics in LaTeX: inline math sits
between single dollar signs, displayed math on its own line between dollar
signs. Every figure is replaced by a verbal description of what it shows, and
every wide table is rewritten as a list of items. Section numbers match the
other editions of these notes, so a section reference in class points to the
same place here. Nothing else is needed to read it.

**Convention.** Vectors are columns. $X$ denotes a random vector in
$\mathbb{R}^n$ and $x$ a point of $\mathbb{R}^n$. Following the source, the
general theory of Sections 4 to 6 writes $V$ for the covariance matrix, while
the two-dimensional warm-up of Section 2 and the discriminant analysis of
Section 9 write $\Sigma$; they mean the same object. The statement
$W \sim \mathcal N(0, I_n)$ always means $n$ independent standard normal
scalars stacked into a column. $\log$ is the natural logarithm throughout.
$A^{\mathsf T}$ is the transpose of $A$, and $\operatorname{tr}$ the trace.

**Notation.**

- $\mu$, $V$: mean vector and covariance matrix of a Gaussian; $\Sigma$ is the
  same matrix in Sections 2 and 9.
- $A \succeq 0$: $A$ is symmetric positive semidefinite; $A \succ 0$:
  symmetric positive definite.
- $A^{1/2}$: the positive semidefinite square root of $A$; $A^{-1/2}$ its
  inverse.
- $\operatorname{Cov}(X, Y)$: the cross-covariance matrix; $\operatorname{Cov}(X)$
  is $\operatorname{Cov}(X, X)$.
- $V_{XX}$, $V_{XY}$, $V_{YX}$, $V_{YY}$: the four blocks of the joint
  covariance of a stacked pair $(X, Y)$.
- $M_X(s) = \mathbb E[e^{s^{\mathsf T} X}]$: the moment generating function
  (MGF) of the random vector $X$, a function of a vector argument $s$.
- $D$: the matrix that builds a Gaussian out of white noise, as in
  $X = DW + \mu$; $d_i^{\mathsf T}$ is its $i$-th row.
- $\beta$, $\alpha = 1 - \beta$, $\bar\alpha_n = \prod_{i \le n}\alpha_i$: the
  diffusion noise schedule of Section 8.
- $\pi_y$, $\mu_y$, $\Sigma_y$: the prior, mean and covariance of class $y$ in
  Section 9; $\Phi = \Sigma^{-1}$ is the precision matrix and $S$ the scatter
  matrix.
- $\blacksquare$ in the other editions marks the end of a proof; here each
  proof ends with the words "End of proof."

**Background used.** From Lecture 3: the one-dimensional Gaussian
normalization $\int e^{-y^2/(2\lambda)}\,dy = \sqrt{2\pi\lambda}$, and the
maximum-entropy characterization of the Gaussian. From Lecture 4: independence
as the product rule for densities, and Markov chains. From Lecture 5: the
scalar MGF $e^{mt + vt^2/2}$ of $\mathcal N(m, v)$, the statement of scalar MGF
uniqueness, the fact that a normal has finite moments of all orders, the sum
rule for independent normals, and the central limit theorem. From Lecture 7:
conditional expectation, the orthogonality principle and the minimum
mean-squared-error theorem, the maximum-likelihood recipe, the Bayes
optimality of the maximum-a-posteriori rule, and the notion of bias. Two
facts are imported from linear algebra without proof: the spectral theorem for
symmetric matrices, and the multivariate change-of-variables formula. Exactly
one probabilistic black box is imported, stated with a citation in Section
4.3: multivariate MGF uniqueness.

**What this edition adds.** Relative to the lecture itself: full formal
statements of the three definitions of the multivariate normal with every
condition explicit, all seven parts of the properties theorem proved with
their skipped steps restored, the equivalence of the three definitions closed
in both directions, the conditional-distribution formula derived twice, the
exact reverse posterior of a diffusion chain that the lecture only
approximates, and both matrix-calculus identities of Section 9 proved. Every
worked number in the lecture has been re-derived from scratch, and all of them
check out. Four slips in the LaTeX source that the lecture corrects silently
are confirmed and flagged where they occur, in Sections 2.1, 2.4, 2.5 and 8.3;
one imprecise intermediate line is flagged in Section 8.8, whose headline
result is nevertheless correct.

**Contents.**

1. Why Gaussians?
2. Warm-up: two dimensions
3. Positive semidefinite matrices
4. Three definitions
5. Vector means and covariances
6. The properties theorem
7. The Gaussian channel
8. Gaussian diffusion
9. Gaussian discriminant analysis
10. References

## 1 Why Gaussians?

### 1.1 Three loads carried by one family

One distribution family carries three separate loads in deep learning.

*Generative models.* A diffusion model's forward process is repeated Gaussian
corruption, and its generator is a chain of Gaussian sampling steps. Section 8
builds this from the one-step recursion up to the standard notation of Ho,
Jain and Abbeel [2].

*Classification.* Modelling each class's features as a Gaussian and inverting
by Bayes' rule gives Gaussian discriminant analysis. That is Section 9, which
is also the first genuinely multivariate maximum-likelihood computation of the
course.

*Inference under noise.* Observing a Gaussian signal through additive Gaussian
noise leaves a Gaussian posterior whose mean is a shrunken version of the
observation. That is Section 7, which delivers the closed-form minimum
mean-squared-error estimator that Lecture 7 promised but could not compute.

### 1.2 Why this family and not another

Three earlier results make the Gaussian the default rather than a convenient
choice. From Lecture 3: among all densities on $\mathbb{R}$ with a fixed mean
and variance, the Gaussian has maximum differential entropy [5, Ch. 8], so it
is the least-committed noise model. From Lecture 5: the central limit theorem
makes sums of many small independent effects approximately Gaussian regardless
of the ingredients' own distributions. And, the content of this lecture, the
family is *closed* under everything one wants to do to it: affine maps,
marginalization, conditioning and convolution all return Gaussians (Theorem
2). That closure is why every computation in Sections 7 to 9 terminates in a
formula rather than in an integral.

## 2 Warm-Up: Two Dimensions

### 2.1 Definition and the joint density

**Definition (bivariate normal, nondegenerate).** The pair $(X_1, X_2)$ is
bivariate normal with means $\mu_1, \mu_2$, variances $\sigma_1^2, \sigma_2^2 > 0$
and correlation $\rho \in (-1, 1)$ if its joint density is

$$ f(x_1, x_2) = \frac{1}{2\pi \sqrt{\det \Sigma}}
   \exp\Big( -\tfrac{1}{2} (x - \mu)^{\mathsf T} \Sigma^{-1} (x - \mu) \Big), $$

where the covariance matrix has entries $\Sigma_{11} = \sigma_1^2$,
$\Sigma_{22} = \sigma_2^2$ and $\Sigma_{12} = \Sigma_{21} = \rho\sigma_1\sigma_2$.

The conditions matter. The requirements $\sigma_i > 0$ and $|\rho| < 1$ are
exactly what make $\Sigma$ invertible, since
$\det \Sigma = \sigma_1^2\sigma_2^2(1 - \rho^2) > 0$, so the formula is well
defined. The boundary cases $|\rho| = 1$ are the two-dimensional degenerate
Gaussians of Section 4.2: all the mass sits on a line and there is no joint
density.

Explicitly, the inverse of a two-by-two matrix with entries $a, b$ on the
first row and $c, d$ on the second is $1/(ad - bc)$ times the matrix with
entries $d, -b$ on the first row and $-c, a$ on the second. Hence
$\Sigma^{-1}$ is $\frac{1}{1 - \rho^2}$ times the matrix whose diagonal
entries are $1/\sigma_1^2$ and $1/\sigma_2^2$ and whose two off-diagonal
entries are both $-\rho/(\sigma_1\sigma_2)$. Written out, the exponent is the
classical form

$$ -\frac{1}{2(1-\rho^2)} \left[ \frac{(x_1-\mu_1)^2}{\sigma_1^2}
   - \frac{2\rho (x_1-\mu_1)(x_2-\mu_2)}{\sigma_1 \sigma_2}
   + \frac{(x_2-\mu_2)^2}{\sigma_2^2} \right]. $$

*Source note.* The LaTeX source `probability25.tex` writes this exponent
without the transpose, as $(x - \mu)\,\Sigma^{-1}(x - \mu)$. That does not
typecheck: a two-by-one column cannot left-multiply a two-by-two matrix. The
form above, with $(x-\mu)^{\mathsf T}$, is the correct one.

### 2.2 The running example

Throughout Sections 2 and 6 the running example is $\mu = 0$,
$\sigma_1 = \sigma_2 = 1$, $\rho = 0.6$, so that $\Sigma$ has diagonal entries
$1$ and $1$ and off-diagonal entries $0.6$ and $0.6$. Then
$\det \Sigma = 1 - 0.36 = 0.64$, and $\Sigma^{-1}$ is $1/0.64$ times the
matrix with diagonal entries $1, 1$ and off-diagonal entries $-0.6, -0.6$.

Eigenstructure: for any matrix with diagonal entries $1, 1$ and off-diagonal
entries $\rho, \rho$, the vectors $(1,1)^{\mathsf T}$ and $(1,-1)^{\mathsf T}$
are eigenvectors, with eigenvalues $1 + \rho$ and $1 - \rho$. Here
$\lambda_1 = 1.6$ along $\tfrac{1}{\sqrt2}(1,1)^{\mathsf T}$ and
$\lambda_2 = 0.4$ along $\tfrac{1}{\sqrt2}(1,-1)^{\mathsf T}$.

### 2.3 Geometry: why the level sets are ellipses

A level set $\{x : x^{\mathsf T} \Sigma^{-1} x = c\}$ is best read in the
eigenbasis. Write $\Sigma = Q \Lambda Q^{\mathsf T}$ with orthonormal
eigenvector columns $q_i$ and $\Lambda = \operatorname{diag}(\lambda_1, \lambda_2)$,
as in Section 3.3, and substitute $y = Q^{\mathsf T} x$, which is a rotation:

$$ x^{\mathsf T} \Sigma^{-1} x = y^{\mathsf T} \Lambda^{-1} y
   = \frac{y_1^2}{\lambda_1} + \frac{y_2^2}{\lambda_2} = c . $$

Dividing by $c$ puts this in standard form: it is equivalent to

$$ \frac{y_1^2}{(\sqrt{c\lambda_1})^2} + \frac{y_2^2}{(\sqrt{c\lambda_2})^2} = 1, $$

an ellipse with semi-axes $\sqrt{c\lambda_i}$ along the eigenvectors $q_i$.

For the running example the one-sigma ellipse, $c = 1$, has semi-axis
$\sqrt{1.6} \approx 1.265$ along the direction $(1,1)$ and semi-axis
$\sqrt{0.4} \approx 0.632$ along the direction $(1,-1)$: an ellipse of aspect
ratio two to one, tilted at 45 degrees, its long axis pointing up and to the
right.

The gallery over $\rho$ follows from the same two eigenvalues. At $\rho = 0$
the two eigenvalues coincide and the ellipse is a circle. As $\rho$ approaches
$+1$ or $-1$, the smaller eigenvalue $1 - |\rho|$ approaches zero and the
ellipse collapses toward the line $x_2 = x_1$ or the line $x_2 = -x_1$
respectively.

### 2.4 Theorem 1: slicing

**Theorem 1 (two-dimensional conditional).** Let $(X_1, X_2)$ be bivariate
normal with mean $(\mu_1, \mu_2)$ and covariance entries
$\sigma_{ij} = \operatorname{Cov}(X_i, X_j)$, with $\sigma_{22} > 0$ and
$|\rho| < 1$. Then for every $x_2 \in \mathbb{R}$,

$$ X_1 \mid X_2 = x_2 \;\sim\;
   \mathcal N\Big( \mu_1 + \frac{\sigma_{12}}{\sigma_{22}} (x_2 - \mu_2),\;\;
   \sigma_{11} - \frac{\sigma_{12}\sigma_{21}}{\sigma_{22}} \Big). $$

In the $(\sigma_1, \sigma_2, \rho)$ parameters the mean is
$\mu_1 + \rho \tfrac{\sigma_1}{\sigma_2}(x_2 - \mu_2)$ and the variance is
$\sigma_1^2 (1 - \rho^2)$.

*Source note.* The LaTeX source `probability25.tex` states the conditional
variance as $\sigma_{22} - \sigma_{12}\sigma_{21}/\sigma_{22}$, which is
wrong. For the running example it happens to give the same number by symmetry,
but for $\sigma_1 \neq \sigma_2$ it fails, and it does not even reduce to
$\operatorname{Var}(X_1)$ when $\sigma_{12} = 0$. The correct leading term is
$\sigma_{11}$.

Two structural facts are worth naming before the proof. First, the conditional
variance does not depend on the observed value $x_2$: every slice has the same
width. Second, it is strictly smaller than the marginal variance whenever
$\sigma_{12} \neq 0$, so conditioning on correlated information always helps.
Both facts survive verbatim in $n$ dimensions; see Section 6.9.

### 2.5 Proof of Theorem 1 by completing the square

*Proof.* Take $\mu = 0$ and unit variances, restoring them at the end by the
substitution $X_i \mapsto \mu_i + \sigma_i X_i$. The conditional density is
$f(x_1 \mid x_2) = f(x_1, x_2)/f(x_2)$; as a function of $x_1$ with $x_2$
held fixed, only the exponent matters. Group the Section 2.1 exponent in
$x_1$:

$$ \frac{x_1^2 - 2\rho x_1 x_2 + x_2^2}{1 - \rho^2}
   = \frac{(x_1 - \rho x_2)^2 + (1 - \rho^2) x_2^2}{1 - \rho^2}
   = \frac{(x_1 - \rho x_2)^2}{1 - \rho^2} + x_2^2 . $$

The middle step is one completed square:
$x_1^2 - 2\rho x_1 x_2 = (x_1 - \rho x_2)^2 - \rho^2 x_2^2$, and then
$-\rho^2 x_2^2 + x_2^2 = (1-\rho^2)x_2^2$. Hence the joint density factors as
$f(x_1, x_2) = f(x_1 \mid x_2)\, f(x_2)$ with

$$ f(x_1 \mid x_2) = \frac{1}{\sqrt{2\pi(1-\rho^2)}}
   \exp\Big( -\frac{(x_1 - \rho x_2)^2}{2(1-\rho^2)} \Big),
   \qquad
   f(x_2) = \frac{1}{\sqrt{2\pi}}\, e^{-x_2^2/2} . $$

The first factor is, for each fixed $x_2$, exactly the
$\mathcal N(\rho x_2,\, 1 - \rho^2)$ density. Integrating over $x_1$ confirms
that the second factor is the $X_2$ marginal, so $X_2 \sim \mathcal N(0,1)$:
this is the two-dimensional case of the statement that marginals of a Gaussian
are Gaussian. Restoring means and scales gives the theorem. **End of proof.**

**Worked slice.** In the running example, condition on $X_2 = 1$. The mean is
$\rho x_2 = 0.6 \cdot 1 = 0.6$ and the variance is
$1 - \rho^2 = 1 - 0.36 = 0.64$, so
$X_1 \mid X_2 = 1 \sim \mathcal N(0.6,\, 0.64)$, a normal with standard
deviation $0.8$. Geometrically: the horizontal line at height $x_2 = 1$ cuts
the density surface, and the resulting cross-section is a normal bump whose
peak sits at $x_1 = 0.6$, shifted right of the origin and slightly narrower
than the marginal.

*Source note.* The deeper reason the completed square works falls out of the
general machinery, and Section 6.9 re-derives Theorem 1 as the
one-plus-one-dimensional case of the general conditional formula. In that
passage the LaTeX source labels the density as belonging to "Definition 2";
in the source's own numbering the density is Definition 1, and this edition
uses the corrected label consistently with Section 4.

## 3 Positive Semidefinite Matrices

### 3.1 Definitions, and the eigenvalue characterization

**Definition.** A *symmetric* matrix $A \in \mathbb{R}^{n\times n}$ is
*positive semidefinite*, written $A \succeq 0$, if $x^{\mathsf T} A x \geq 0$
for all $x \in \mathbb{R}^n$; and *positive definite*, written $A \succ 0$, if
$x^{\mathsf T} A x > 0$ for all $x \neq 0$.

Symmetry is part of the definition here, following the source's convention.
For a symmetric matrix the *spectral theorem*, imported from linear algebra
and not re-proved, supplies real eigenvalues $\lambda_1, \dots, \lambda_n$ and
an orthonormal eigenbasis $z_1, \dots, z_n$, so that
$A = Q\Lambda Q^{\mathsf T} = \sum_{i=1}^n \lambda_i z_i z_i^{\mathsf T}$ with
$Q^{\mathsf T} Q = I$.

**Lemma 3.1.** $A \succeq 0$ if and only if all $\lambda_i \geq 0$; and
$A \succ 0$ if and only if all $\lambda_i > 0$.

*Proof.* For the forward direction, test the definition on an eigenvector:
$z_i^{\mathsf T} A z_i = \lambda_i \|z_i\|^2 = \lambda_i$, so the sign
condition on the quadratic form forces the same sign condition on each
eigenvalue. For the converse, expand an arbitrary $x$ in the eigenbasis as
$x = \sum_i c_i z_i$ with $c_i = z_i^{\mathsf T} x$. By orthonormality,

$$ x^{\mathsf T} A x = \sum_i \lambda_i (z_i^{\mathsf T} x)^2 = \sum_i \lambda_i c_i^2, $$

which is a nonnegative combination when every $\lambda_i \geq 0$, and is
strictly positive for $x \neq 0$ when every $\lambda_i > 0$, since then some
$c_i \neq 0$. **End of proof.**

### 3.2 The workbench matrix

Let $A$ be the two-by-two matrix with diagonal entries $2, 2$ and off-diagonal
entries $1, 1$.

*Positive-definiteness certificate.*
$x^{\mathsf T} A x = 2x_1^2 + 2x_1x_2 + 2x_2^2 = x_1^2 + x_2^2 + (x_1 + x_2)^2$.
Expanding the right-hand side gives
$x_1^2 + x_2^2 + x_1^2 + 2x_1x_2 + x_2^2 = 2x_1^2 + 2x_1x_2 + 2x_2^2$, which
matches. It is a sum of squares that vanishes only at $x = 0$, so $A \succ 0$
with no eigenvalue computation at all.

*Eigenpairs.* $A(1,1)^{\mathsf T} = (3,3)^{\mathsf T}$ and
$A(1,-1)^{\mathsf T} = (1,-1)^{\mathsf T}$, so $\lambda = 3$ at
$\tfrac{1}{\sqrt2}(1,1)^{\mathsf T}$ and $\lambda = 1$ at
$\tfrac{1}{\sqrt2}(1,-1)^{\mathsf T}$. Cross-checks: the trace is
$4 = 3 + 1$ and the determinant is $3 = 3 \cdot 1$.

### 3.3 Functions of a positive semidefinite matrix

**Lemma 3.2 (square root).** If $A = \sum_i \lambda_i z_i z_i^{\mathsf T} \succeq 0$,
then the matrix $A^{1/2} := \sum_i \sqrt{\lambda_i}\, z_i z_i^{\mathsf T}$ is
symmetric positive semidefinite and satisfies $(A^{1/2})^2 = A$.

*Proof.* Symmetry and positive semidefiniteness are immediate from the form:
each $z_i z_i^{\mathsf T}$ is symmetric positive semidefinite and each
$\sqrt{\lambda_i} \geq 0$. On squaring, the cross terms die by
orthonormality, since
$z_i z_i^{\mathsf T} z_j z_j^{\mathsf T} = (z_i^{\mathsf T} z_j)\, z_i z_j^{\mathsf T}
= \delta_{ij}\, z_i z_i^{\mathsf T}$:

$$ \Big( \sum_i \sqrt{\lambda_i}\, z_i z_i^{\mathsf T} \Big)^2
   = \sum_{i,j} \sqrt{\lambda_i \lambda_j}\, z_i z_i^{\mathsf T} z_j z_j^{\mathsf T}
   = \sum_i \lambda_i z_i z_i^{\mathsf T} = A. $$

**End of proof.**

*Remark.* $A^{1/2}$ is in fact the unique positive semidefinite square root.
Uniqueness is a standard linear-algebra fact and is not needed below: any $B$
with $BB^{\mathsf T} = A$ serves for the constructions of Section 4. Likewise,
if $A \succ 0$ then $A^{-1} = \sum_i \lambda_i^{-1} z_i z_i^{\mathsf T}$;
multiply and use the same orthonormality collapse, together with
$\sum_i z_i z_i^{\mathsf T} = QQ^{\mathsf T} = I$.

**Worked square root.** For the workbench matrix $A$ of Section 3.2,
$A^{1/2} = \sqrt3 \cdot \tfrac12 J_+ + 1 \cdot \tfrac12 J_-$, where $J_+$ has
all four entries equal to $1$ and $J_-$ has diagonal entries $1, 1$ and
off-diagonal entries $-1, -1$. The result is the symmetric matrix with
diagonal entries $(\sqrt3+1)/2 \approx 1.366$ and off-diagonal entries
$(\sqrt3-1)/2 \approx 0.366$. Direct check that $B^2 = A$ for
$B = A^{1/2}$: the diagonal entry of $B^2$ is
$\tfrac{(\sqrt3+1)^2 + (\sqrt3-1)^2}{4} = \tfrac{(4 + 2\sqrt3) + (4 - 2\sqrt3)}{4}
= \tfrac84 = 2$, and the off-diagonal entry is
$\tfrac{2(\sqrt3+1)(\sqrt3-1)}{4} = \tfrac{2(3-1)}{4} = 1$. Both match $A$.

### 3.4 Positive semidefinite if and only if Gram

**Lemma 3.3.** A symmetric matrix $A$ is positive semidefinite if and only if
$A = B^{\mathsf T} B$ for some matrix $B$.

*Proof.* For the "if" direction,
$x^{\mathsf T} B^{\mathsf T} B x = (Bx)^{\mathsf T}(Bx) = \|Bx\|^2 \geq 0$ for
every $x$, and $(B^{\mathsf T} B)^{\mathsf T} = B^{\mathsf T} B$ gives
symmetry. For the "only if" direction, take $B = A^{1/2}$ from Lemma 3.2:
then $B^{\mathsf T} B = A^{1/2} A^{1/2} = A$. **End of proof.**

Read forward, this says that covariance matrices will turn out to be *exactly*
the positive semidefinite matrices: Section 5.2 shows every covariance is
positive semidefinite, and Section 6.2, through the identity
$\operatorname{Cov}(DW + \mu) = DD^{\mathsf T}$, shows every positive
semidefinite matrix is a covariance.

### 3.5 Why positive definiteness buys a density

**Claim.** If $V \succ 0$ then

$$ \int_{\mathbb{R}^n} \exp\big(-\tfrac12 x^{\mathsf T} V^{-1} x\big)\, dx
   = (2\pi)^{n/2} (\det V)^{1/2}, $$

so the Definition-1 density of Section 4.1 normalizes, and positive
definiteness is exactly what makes the integral finite.

*Proof.* Write $V = Q\Lambda Q^{\mathsf T}$ and rotate by $x = Qy$; the
Jacobian factor is $|\det Q| = 1$ because $Q$ is orthogonal. Then

$$ \int e^{-\frac12 x^{\mathsf T} V^{-1} x}\, dx
   = \int e^{-\frac12 \sum_i y_i^2 / \lambda_i}\, dy
   = \prod_{i=1}^n \int_{-\infty}^{\infty} e^{-y_i^2 / (2\lambda_i)}\, dy_i
   = \prod_{i=1}^n \sqrt{2\pi \lambda_i}, $$

each one-dimensional factor being the $\mathcal N(0, \lambda_i)$
normalization from Lecture 3, finite precisely because every
$\lambda_i > 0$. The product is
$(2\pi)^{n/2} \big(\prod_i \lambda_i\big)^{1/2} = (2\pi)^{n/2}(\det V)^{1/2}$.
If instead some $\lambda_i = 0$, then along the direction $z_i$ the integrand
is constantly equal to $1$, interpreting $V^{-1}$ on the complement, and the
integral diverges. So a singular $V$ admits no density on $\mathbb{R}^n$,
which is why Definition 1 must require $V \succ 0$. **End of proof.**

## 4 Three Definitions

### 4.1 The three definitions, in full

**Definition 1 (density).** Let $\mu \in \mathbb{R}^n$ and let
$V \in \mathbb{R}^{n\times n}$ be symmetric with $V \succ 0$. Then
$X \sim \mathcal N(\mu, V)$ if $X$ has joint density

$$ f_X(x) = \frac{1}{(2\pi)^{n/2} (\det V)^{1/2}}
   \exp\Big( -\tfrac12 (x - \mu)^{\mathsf T} V^{-1} (x - \mu) \Big),
   \qquad x \in \mathbb{R}^n . $$

Section 3.5 verified that this integrates to $1$; it requires $V$ invertible.

**Definition 2 (construction).** $X$ is multivariate normal if
$X = DW + \mu$ for some matrix $D \in \mathbb{R}^{n \times m}$, some
$\mu \in \mathbb{R}^n$, and $W \sim \mathcal N(0, I_m)$, that is, with
$W_1, \dots, W_m$ independent standard normal. The joint density of $W$ is the
product $f_W(w) = (2\pi)^{-m/2} e^{-\|w\|^2/2}$, by Lecture 4's product rule
for independence.

**Definition 3 (projections).** $X$ is multivariate normal if for *every*
$a \in \mathbb{R}^n$ the scalar $a^{\mathsf T} X = \sum_i a_i X_i$ is normal,
where constants count as degenerate normals $\mathcal N(c, 0)$.

The quantifier in Definition 3 is "for all $a$", and the convention on
constants is not cosmetic: it is what lets $a = 0$, and more generally any $a$
annihilating a degenerate direction, pass the test. Note also that
Definition 3 makes no moment assumption at all; finiteness of every moment is
a *consequence*, established in Section 4.4.

### 4.2 Definitions 2 and 3 do more: the degenerate case

Take $n = 2$, $D = (1, 1)^{\mathsf T}$, that is, a single noise source with
$m = 1$, and $\mu = 0$. Then $X = (W_1, W_1)^{\mathsf T}$ puts all of its mass
on the line $x_1 = x_2$. Its covariance is $V = DD^{\mathsf T}$, the matrix
with all four entries equal to $1$, which is singular: its determinant is $0$
and its eigenvalues are $2$ and $0$. So by Section 3.5 there is no joint
density and Definition 1 cannot apply.

But Definition 2 applies by construction, and Definition 3 applies too:
$a^{\mathsf T} X = (a_1 + a_2) W_1 \sim \mathcal N(0, (a_1 + a_2)^2)$, a
genuine normal, or the constant $0$ when $a_1 = -a_2$, which is where the
convention on constants earns its keep.

In general a Definition-2 vector lives on the affine subspace
$\mu + \operatorname{range}(D)$, and
$\operatorname{range}(DD^{\mathsf T}) = \operatorname{range}(D)$, so the
support is $\mu + \operatorname{range}(V)$: the singular directions of the
covariance are exactly the deterministic directions of the vector. Degenerate
Gaussians are not pathologies. They appear whenever data sits on, or near, a
low-dimensional subspace, which is the normal state of affairs for learned
representations.

### 4.3 The equivalence, stated precisely

**Theorem (equivalence).**

(a) *Nondegenerate case.* For a random vector $X$ on $\mathbb{R}^n$ the
following three statements are equivalent: (i) $X$ satisfies Definition 1 for
some $\mu$ and some $V \succ 0$; (ii) $X = DW + \mu$ with $D$ square and
invertible; (iii) $X$ satisfies Definition 3 and $\operatorname{Cov}(X) \succ 0$.

(b) *In general.* Definitions 2 and 3 are equivalent, with matching
parameters $\mu = \mathbb E[X]$ and
$V = \operatorname{Cov}(X) = DD^{\mathsf T}$; and each is equivalent to
Definition 1 precisely when the covariance is invertible.

Two of the four implications are the ones the lecture proves: Definition 2
implies Definition 1 when $D$ is invertible, proved as part 4 of Theorem 2 in
Section 6.4; and Definition 2 implies Definition 3, which is part 3 followed
by part 1, in Section 6.3. The two reverse implications are stated in the
source but not proved in class. They are proved next.

One tool is imported. *Multivariate MGF uniqueness*: if
$M_X(s) = \mathbb E[e^{s^{\mathsf T} X}]$ and $M_Y(s)$ are finite and equal
for all $s$ in a neighborhood of $0$, then $X$ and $Y$ have the same
distribution. Lecture 5 stated the scalar version, also without proof, since
it needs complex analysis by way of characteristic functions. The multivariate
version is Section 4.10 of the MIT OpenCourseWare 6.436J notes [1] and rests
on the same machinery; equivalently, it follows from the Cramer-Wold device.
Everything else below is self-contained.

### 4.4 Closing the two remaining implications

**Proposition (Definition 1 implies Definition 2).** If $X$ has the
Definition-1 density with parameters $(\mu, V)$ and $V \succ 0$, then $X$ has
the same distribution as $V^{1/2} W + \mu$ with $W \sim \mathcal N(0, I_n)$.

*Proof.* Let $Y = V^{1/2} W + \mu$, a Definition-2 vector with
$D = V^{1/2}$ invertible by Lemma 3.2, since its eigenvalues
$\sqrt{\lambda_i}$ are all strictly positive. By part 4 of Theorem 2, proved
in Section 6.4 from Definition 2 alone so that there is no circularity, $Y$
has the Definition-1 density with mean $\mu$ and covariance
$DD^{\mathsf T} = V^{1/2}V^{1/2} = V$: the same density as $X$. Two random
vectors with the same density have the same distribution. **End of proof.**

**Proposition (Definition 3 implies Definition 2).** If every
$a^{\mathsf T} X$ is normal, then $X$ has the same distribution as
$V^{1/2} W + \mu$, where $\mu = \mathbb E[X]$ and $V = \operatorname{Cov}(X)$.

*Proof.* Step 1, the moments exist. Each coordinate
$X_i = e_i^{\mathsf T} X$ is normal, hence has finite moments of all orders by
Lecture 5, so $\mu$ and $V$ are well defined; and $V \succeq 0$ by Section 5.2.

Step 2, identify each projection's parameters. For fixed $s$ the scalar
$s^{\mathsf T} X$ is normal by hypothesis. Its mean and variance need no
Gaussianity, only linearity and bilinearity from Section 5:
$\mathbb E[s^{\mathsf T} X] = s^{\mathsf T}\mu$ and
$\operatorname{Var}(s^{\mathsf T} X) = s^{\mathsf T} V s$. So
$s^{\mathsf T} X \sim \mathcal N(s^{\mathsf T}\mu,\, s^{\mathsf T} V s)$.

Step 3, compute the MGF. A normal's scalar MGF is finite everywhere: Lecture 5
gives $\mathbb E[e^{tZ}] = e^{mt + v t^2/2}$ for $Z \sim \mathcal N(m, v)$,
and $e^{c t}$ in the degenerate case $v = 0$. Evaluating at $t = 1$,

$$ M_X(s) = \mathbb E\big[e^{s^{\mathsf T} X}\big]
   = M_{s^{\mathsf T} X}(1)
   = \exp\big( s^{\mathsf T}\mu + \tfrac12 s^{\mathsf T} V s \big)
   \qquad \text{for all } s \in \mathbb{R}^n . $$

Step 4, match. Part 5 of Theorem 2, in Section 6.5, proved from Definition 2
alone, shows that $Y = V^{1/2}W + \mu$ has exactly this MGF. Both MGFs are
finite everywhere, so multivariate MGF uniqueness [1, Section 4.10] gives that
$X$ and $Y$ have the same distribution. **End of proof.**

This closes the loop: Definition 1 implies Definition 2 implies Definition 3
implies Definition 2, and Definition 2 implies Definition 1 whenever the
covariance is invertible. Honest accounting: the only unproved ingredient in
this whole set of notes is MGF uniqueness, flagged above.

*Source note.* In two places the LaTeX source `probability25.tex` refers to
"the density in Definition 2"; in the source's own numbering the density
belongs to Definition 1, and this edition uses the corrected label.

A useful byproduct of the proof: a multivariate Gaussian's distribution is
completely determined by the pair $(\mu, V)$. This is used repeatedly below.

### 4.5 Whitening

The map of Section 4.4 inverts. If $X \sim \mathcal N(\mu, V)$ with
$V \succ 0$, then $W = V^{-1/2}(X - \mu)$ satisfies
$W \sim \mathcal N(0, I_n)$: by part 3 of Theorem 2 it is Gaussian, with mean
$V^{-1/2}(\mu - \mu) = 0$ and covariance $V^{-1/2} V V^{-1/2} = I$, using
symmetry of $V^{1/2}$, and a Gaussian is determined by its parameters. So
every nondegenerate Gaussian is a linear reshaping of white noise, and can be
linearly whitened back. This is the standing trick behind Sections 3.5 and
6.4, and behind every step of the form "reduce to the standard normal".

## 5 Vector Means and Covariances

### 5.1 Definitions and the transformation rules

**Definition.** For random vectors $X \in \mathbb{R}^n$ and
$Y \in \mathbb{R}^m$ with finite second moments, the mean is taken entrywise,
$\mathbb E[X] = (\mathbb E[X_1], \dots, \mathbb E[X_n])^{\mathsf T}$, and the
*cross-covariance matrix* is

$$ \operatorname{Cov}(X, Y) = \mathbb E\big[ (X - \mathbb E[X])(Y - \mathbb E[Y])^{\mathsf T} \big]
   \in \mathbb{R}^{n \times m},
   \qquad \operatorname{Cov}(X, Y)_{ij} = \operatorname{Cov}(X_i, Y_j). $$

Write $\operatorname{Cov}(X) := \operatorname{Cov}(X, X)$. Its diagonal holds
the variances, and $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)^{\mathsf T}$.

**Lemma 5.1 (affine rules).** $\mathbb E[AX + b] = A\,\mathbb E[X] + b$, and

$$ \operatorname{Cov}(AX + b,\; CY + d) = A \operatorname{Cov}(X, Y)\, C^{\mathsf T}. $$

*Proof.* The mean rule is linearity of expectation applied entrywise. For the
covariance rule, the shifts $b$ and $d$ cancel inside the centred factors, so
with $\tilde X = X - \mathbb E X$ and $\tilde Y = Y - \mathbb E Y$,

$$ \operatorname{Cov}(AX+b,\, CY+d)
   = \mathbb E[(A\tilde X)(C\tilde Y)^{\mathsf T}]
   = A\, \mathbb E[\tilde X \tilde Y^{\mathsf T}]\, C^{\mathsf T}, $$

pulling the constant matrices out of the entrywise expectations. **End of
proof.**

Two special cases are used constantly:
$\operatorname{Cov}(AX + b) = A\operatorname{Cov}(X)A^{\mathsf T}$, and
$\operatorname{Var}(a^{\mathsf T} X) = a^{\mathsf T} \operatorname{Cov}(X)\, a$.

### 5.2 Every covariance matrix is positive semidefinite

**Claim.** $\operatorname{Cov}(X) \succeq 0$ for every $X$ with finite second
moments.

*Proof.* For any $a \in \mathbb{R}^n$, by the last special case of Lemma 5.1,
$a^{\mathsf T} \operatorname{Cov}(X)\, a = \operatorname{Var}(a^{\mathsf T} X) \geq 0$,
being a scalar variance. Symmetry is visible from the definition. **End of
proof.**

Moreover $\operatorname{Cov}(X) \succ 0$ fails exactly when
$\operatorname{Var}(a^{\mathsf T} X) = 0$ for some $a \neq 0$, that is, when
$X$ has a deterministic direction, which ties back to Section 4.2. Combined
with Section 6.2, the covariance matrices are *exactly* the positive
semidefinite matrices.

### 5.3 Correlation, and the bound on it

Define $\rho_{ij} = \operatorname{Cov}(X_i, X_j) / (\sigma_i \sigma_j)$
whenever $\sigma_i, \sigma_j > 0$. That $|\rho_{ij}| \leq 1$ is the
Cauchy-Schwarz inequality: for centred $U = X_i - \mu_i$ and
$T = X_j - \mu_j$ and every $t \in \mathbb{R}$,

$$ 0 \leq \mathbb E[(U - tT)^2] = \mathbb E[U^2] - 2t\,\mathbb E[UT] + t^2 \mathbb E[T^2]. $$

A quadratic in $t$ that is never negative has discriminant at most zero, so
$\mathbb E[UT]^2 \leq \mathbb E[U^2]\,\mathbb E[T^2]$, which after dividing by
$\sigma_i^2\sigma_j^2$ is $|\rho_{ij}| \leq 1$.

Running-example check: $\operatorname{Cov}(X_1, X_2) = 0.6$ and
$\sigma_1 = \sigma_2 = 1$, so $\rho_{12} = 0.6$. More generally, for the
two-dimensional parameterization of Section 2 the off-diagonal entry
$\rho\sigma_1\sigma_2$ divided by $\sigma_1\sigma_2$ returns $\rho$, so the
symbol $\rho$ in the density really is the correlation.

## 6 The Properties Theorem

Throughout this section $X = DW + \mu$ is a Definition-2 Gaussian with
$W \sim \mathcal N(0, I_m)$, and $d_i^{\mathsf T}$ denotes the $i$-th row of
$D$.

**Theorem 2.** With $V = DD^{\mathsf T}$:

1. Each $X_i$ is normal; more generally $a^{\mathsf T} X$ is normal for every
   $a$.
2. $\mathbb E[X] = \mu$ and $\operatorname{Cov}(X) = DD^{\mathsf T}$.
3. $AX + b$ is again multivariate normal, with mean $A\mu + b$ and covariance
   $A\,DD^{\mathsf T} A^{\mathsf T}$.
4. If $D$ is square and invertible, $X$ has the Definition-1 density with
   $V = DD^{\mathsf T}$.
5. $M_X(s) = \exp(s^{\mathsf T}\mu + \tfrac12 s^{\mathsf T} V s)$, and the
   pair $(\mu, V)$ determines the distribution.
6. If $X$ is jointly Gaussian, its components are independent if and only if
   they are uncorrelated, that is, if and only if $V$ is diagonal; there is a
   blockwise version for subvectors.
7. If $(X, Y)$ are jointly Gaussian with $V_{YY} \succ 0$, then
   $\mathbb E[X \mid Y] = \mu_X + V_{XY} V_{YY}^{-1} (Y - \mu_Y)$, the
   residual is independent of $Y$, and
   $X \mid Y = y \sim \mathcal N\big(\mu_X + V_{XY}V_{YY}^{-1}(y - \mu_Y),\;
   V_{XX} - V_{XY} V_{YY}^{-1} V_{YX}\big)$.

### 6.1 Part 1: projections are normal

**Recalled tool (Lecture 5).** If $U \sim \mathcal N(m_1, v_1)$ and
$T \sim \mathcal N(m_2, v_2)$ are independent, then
$U + T \sim \mathcal N(m_1 + m_2, v_1 + v_2)$. Reason: MGFs multiply under
independence, and
$e^{m_1 t + v_1 t^2/2} \cdot e^{m_2 t + v_2 t^2/2} = e^{(m_1+m_2)t + (v_1+v_2)t^2/2}$
is again a normal MGF; conclude by scalar MGF uniqueness. By induction the
same holds for any finite independent sum, with degenerate summands allowed.

*Proof of part 1.* Write

$$ a^{\mathsf T} X = a^{\mathsf T} D W + a^{\mathsf T}\mu
   = \sum_{k=1}^m (a^{\mathsf T} D)_k\, W_k + a^{\mathsf T}\mu . $$

This is a finite sum of independent normals
$(a^{\mathsf T} D)_k W_k \sim \mathcal N(0, (a^{\mathsf T} D)_k^2)$ plus a
constant, hence normal, and specifically
$a^{\mathsf T} X \sim \mathcal N(a^{\mathsf T}\mu,\; \|D^{\mathsf T} a\|^2)$.
Taking $a = e_i$ gives $X_i \sim \mathcal N(\mu_i, \|d_i\|^2)$. **End of
proof.**

This is the implication from Definition 2 to Definition 3.

### 6.2 Part 2: the parameters

$\mathbb E[X] = D\,\mathbb E[W] + \mu = \mu$; and by Lemma 5.1 with
$\operatorname{Cov}(W) = I_m$, which holds because the $W_k$ are independent
with unit variance,
$\operatorname{Cov}(X) = D\, I_m\, D^{\mathsf T} = DD^{\mathsf T}$.

Together with Lemma 3.3 this shows that every positive semidefinite matrix
arises as a Gaussian covariance: given $V \succeq 0$, take $D = V^{1/2}$.

### 6.3 Part 3: affine closure, and marginals

$AX + b = A(DW + \mu) + b = (AD)W + (A\mu + b)$ is again of Definition-2 form,
with matrix $AD$. That one-line proof is the reason Definition 2 is the
workhorse: the other two definitions make this closure invisible. The
parameters follow from part 2 and Lemma 5.1: mean $A\mu + b$, covariance
$(AD)(AD)^{\mathsf T} = A\,V A^{\mathsf T}$.

*Corollary (marginals).* Any subvector $(X_{i_1}, \dots, X_{i_k})$ equals
$A X$ for the selector matrix $A$ whose rows are
$e_{i_1}^{\mathsf T}, \dots, e_{i_k}^{\mathsf T}$, hence is Gaussian, with
mean and covariance the corresponding sub-blocks of $\mu$ and $V$.
Marginalizing a Gaussian is *deleting rows and columns*; no integral is ever
computed.

### 6.4 Part 4: the density, by change of variables

**Recalled tool (multivariate change of variables, stated).** If $Y = g(Z)$
with $g$ an invertible differentiable map, then
$f_Y(y) = f_Z(g^{-1}(y))\, |\det J_{g^{-1}}(y)|$. For the affine map
$g(w) = Dw + \mu$ one has $g^{-1}(x) = D^{-1}(x - \mu)$, with the constant
Jacobian determinant $\det D^{-1} = 1/\det D$.

*Proof of part 4.* With $f_W(w) = (2\pi)^{-n/2} e^{-\|w\|^2/2}$ and
$w = D^{-1}(x-\mu)$,

$$ f_X(x) = \frac{1}{(2\pi)^{n/2} |\det D|}
   \exp\Big( -\tfrac12 \big\|D^{-1}(x - \mu)\big\|^2 \Big), $$

and the exponent rearranges into the $V^{-1}$ quadratic form, with
$V = DD^{\mathsf T}$:

$$ \|D^{-1}(x-\mu)\|^2 = (x-\mu)^{\mathsf T} (D^{-1})^{\mathsf T} D^{-1} (x-\mu)
   = (x-\mu)^{\mathsf T} (DD^{\mathsf T})^{-1} (x-\mu), $$

since $(D^{-1})^{\mathsf T} D^{-1} = (D^{\mathsf T})^{-1}D^{-1} = (DD^{\mathsf T})^{-1}$.
Finally
$|\det D| = (\det D \cdot \det D^{\mathsf T})^{1/2} = (\det V)^{1/2}$, which
gives exactly the Definition-1 density. **End of proof.**

This is the implication from Definition 2 to Definition 1. Note that
$V = DD^{\mathsf T} \succ 0$ automatically when $D$ is invertible, since
$\|D^{\mathsf T} a\|^2 = 0$ then forces $a = 0$.

### 6.5 Part 5: the moment generating function

*Proof.* By part 1, $s^{\mathsf T} X \sim \mathcal N(s^{\mathsf T}\mu,\, s^{\mathsf T} V s)$.
Evaluate its scalar MGF, from Lecture 5, at $t = 1$:

$$ M_X(s) = \mathbb E\big[e^{s^{\mathsf T} X}\big] = M_{s^{\mathsf T} X}(1)
   = \exp\big( s^{\mathsf T} \mu + \tfrac12\, s^{\mathsf T} V s \big),
   \qquad s \in \mathbb{R}^n, $$

finite for every $s$. Since this MGF depends on $(\mu, V)$ only, MGF
uniqueness, the single imported black box of Section 4.3, gives the following:
two multivariate Gaussians with the same mean and covariance are identically
distributed, regardless of which $D$ built them. **End of proof.**

For example $D$ and $DR$ give the same distribution for any orthogonal $R$,
because $DR(DR)^{\mathsf T} = DD^{\mathsf T}$. The construction is
many-to-one; the distribution is not.

### 6.6 Part 6: independence and zero covariance, both directions

*Proof.* Forward direction, needing no Gaussianity: independent $X_i$ and
$X_j$ with finite second moments satisfy
$\mathbb E[X_iX_j] = \mathbb E[X_i]\mathbb E[X_j]$ by Lecture 4, so
$\operatorname{Cov}(X_i, X_j) = 0$.

Reverse direction, the Gaussian miracle. Suppose $X \sim \mathcal N(\mu, V)$
with $V = \operatorname{diag}(v_1, \dots, v_n)$. Build an
independent-by-construction comparison vector: set
$Y_i = \mu_i + \sqrt{v_i}\, W_i$ with $W \sim \mathcal N(0, I_n)$, that is,
$Y = \operatorname{diag}(\sqrt{v_i})\, W + \mu$, a Definition-2 Gaussian whose
components are independent because the $W_i$ are. Its mean is $\mu$ and its
covariance is
$\operatorname{diag}(\sqrt{v_i})\, I \operatorname{diag}(\sqrt{v_i}) = V$. By
part 5, $X$ and $Y$ have the same distribution; and independence is a property
of the joint distribution, so the components of $X$ are independent. **End of
proof.**

*Blockwise version,* used in Sections 6.9 and 7: if $(X, Y)$ are jointly
Gaussian with $\operatorname{Cov}(X, Y) = 0$, the same matching argument with
a block-diagonal $V$ shows the subvectors $X$ and $Y$ are independent.

**Counterexample: joint Gaussianity cannot be dropped.** Let
$X \sim \mathcal N(0,1)$ and let $S$ be an independent random sign with
$\mathbb P(S = 1) = \mathbb P(S = -1) = \tfrac12$; set $Y = SX$.

(i) $Y$ *is* standard normal:
$\mathbb P(Y \leq t) = \tfrac12 \mathbb P(X \leq t) + \tfrac12 \mathbb P(-X \leq t) = \Phi(t)$,
using the symmetry of $X$.

(ii) $X$ and $Y$ are uncorrelated:
$\operatorname{Cov}(X, Y) = \mathbb E[S X^2] = \mathbb E[S]\,\mathbb E[X^2] = 0 \cdot 1 = 0$,
by independence of $S$ and $X$.

(iii) Yet they are *not* independent: $|Y| = |X|$ always, so for instance
$\mathbb P(|X| \leq 1,\; |Y| > 1) = 0 \neq \mathbb P(|X| \leq 1)\,\mathbb P(|Y| > 1)$.

The escape hatch is that $(X, Y)$ is *not jointly Gaussian*: the sum
$X + Y = (1 + S)X$ equals $0$ with probability $\tfrac12$ and is
$\mathcal N(0,4)$-distributed otherwise, a mixture with an atom, which is
neither a normal nor a constant, so Definition 3 fails at
$a = (1,1)^{\mathsf T}$. The hypothesis "jointly Gaussian" in part 6 is doing
real work: two marginally Gaussian, uncorrelated variables need not be
independent.

### 6.7 Part 7, step 1: the orthogonality characterization

**Lemma 6.1.** $\mathbb E[X \mid Y]$ is the unique, up to almost-sure
equality, function $h(Y)$ with finite second moment satisfying
$\mathbb E[(X - h(Y))\, g(Y)] = 0$ for every bounded measurable $g$;
entrywise for vectors.

*Proof.* That $h = \mathbb E[X|Y]$ passes the test is Lecture 7's
orthogonality principle, by the tower property:

$$ \mathbb E[(X - \mathbb E[X|Y])g(Y)]
   = \mathbb E\big[ g(Y)\, \mathbb E[X - \mathbb E[X|Y] \mid Y] \big] = 0 . $$

Conversely, if $h$ passes the test, set $d(Y) = \mathbb E[X|Y] - h(Y)$;
subtracting the two orthogonality statements gives
$\mathbb E[d(Y) g(Y)] = 0$ for all $g$, and choosing $g = d$, truncated if
unbounded and then letting the truncation grow, yields
$\mathbb E[d(Y)^2] = 0$, so $h(Y) = \mathbb E[X|Y]$ almost surely. **End of
proof.**

### 6.8 Part 7, step 2: guess linear, verify orthogonality

*Proof.* Centre everything: replace $X$ and $Y$ by $X - \mu_X$ and
$Y - \mu_Y$, restoring the means at the end. Guess $\hat X = A Y$ with
$A = V_{XY} V_{YY}^{-1}$, and let $\tilde X = X - \hat X$ be the residual.

*The residual is uncorrelated with $Y$:*

$$ \operatorname{Cov}(\tilde X, Y) = \operatorname{Cov}(X, Y) - A \operatorname{Cov}(Y, Y)
   = V_{XY} - V_{XY} V_{YY}^{-1} V_{YY} = 0, $$

using linearity of the covariance in its first slot, Lemma 5.1.

*Uncorrelated upgrades to independent:* the stacked vector
$(\tilde X, Y)$ is an affine image of the jointly Gaussian $(X, Y)$, namely
the image under the block matrix whose first block row is $(I, -A)$ and whose
second block row is $(0, I)$. Hence it is jointly Gaussian by part 3, so part
6 in its blockwise form makes $\tilde X$ independent of $Y$.

*Orthogonality test:* for any $g$,
$\mathbb E[\tilde X\, g(Y)] = \mathbb E[\tilde X]\, \mathbb E[g(Y)] = 0$,
since $\mathbb E[\tilde X] = 0$. By Lemma 6.1, $\hat X = \mathbb E[X \mid Y]$.
Restoring the means,

$$ \mathbb E[X \mid Y] = \mu_X + V_{XY} V_{YY}^{-1} (Y - \mu_Y). $$

**End of proof.**

*Why the guess is legitimate:* nothing is assumed, because the verification is
unconditional. The Gaussian structure is used exactly once, at the step
"uncorrelated implies independent". For non-Gaussian $(X,Y)$ the same
$\hat X$ is still the best *linear* estimator, Lecture 7's linear minimum
mean-squared-error estimator, but it need not equal $\mathbb E[X|Y]$.

### 6.9 Part 7, step 3: the full conditional distribution

*Proof.* Decompose $X = \hat X + \tilde X$ with $\tilde X$ independent of $Y$.
Conditioning on $Y = y$ freezes $\hat X$ at the constant
$\mu_X + V_{XY}V_{YY}^{-1}(y - \mu_Y)$ and, by independence, leaves the
distribution of $\tilde X$ untouched. Now $\tilde X$ is Gaussian, being an
affine image, by part 3, with mean $0$ and covariance

$$ \operatorname{Cov}(\tilde X) = \operatorname{Cov}(X - AY, \; X - AY)
   = V_{XX} - A V_{YX} - V_{XY} A^{\mathsf T} + A V_{YY} A^{\mathsf T}, $$

and with $A = V_{XY}V_{YY}^{-1}$ the last two terms cancel, since
$A V_{YY} A^{\mathsf T} = V_{XY} V_{YY}^{-1} V_{YX} = V_{XY} A^{\mathsf T}$,
leaving

$$ \operatorname{Cov}(\tilde X) = V_{XX} - V_{XY} V_{YY}^{-1} V_{YX} . $$

Hence

$$ X \mid Y = y \;\sim\; \mathcal N\big( \mu_X + V_{XY}V_{YY}^{-1}(y - \mu_Y),\;\;
   V_{XX} - V_{XY}V_{YY}^{-1}V_{YX} \big) . $$

Gaussian in, Gaussian out; the conditional covariance is free of $y$, so all
slices are congruent; and the covariance is *reduced* by the positive
semidefinite matrix $V_{XY}V_{YY}^{-1}V_{YX}$. **End of proof.**

**Theorem 1 recovered.** Take scalar blocks $X = X_1$ and $Y = X_2$: the mean
is $\mu_1 + \tfrac{\sigma_{12}}{\sigma_{22}}(x_2 - \mu_2)$ and the variance is
$\sigma_{11} - \tfrac{\sigma_{12}\sigma_{21}}{\sigma_{22}}$, exactly Section
2.4, now with the deeper reason on display: slicing is projection onto the
residual. Running-example recheck: $0 + \tfrac{0.6}{1}(1 - 0) = 0.6$ and
$1 - \tfrac{0.36}{1} = 0.64$, matching Section 2.5.

### 6.10 New tools: completing the square in matrix form, and the density route

The lecture derives part 7 without ever touching the density. For
completeness, and because Section 8.7 needs the scalar version, here is the
density route, which Bishop [4, Ch. 2.3] runs the same way, with its two
lemmas proved.

**Lemma 6.2 (matrix completing the square).** For symmetric $P \succ 0$ and
any $b$,

$$ x^{\mathsf T} P x - 2 b^{\mathsf T} x = (x - P^{-1}b)^{\mathsf T} P\, (x - P^{-1}b) - b^{\mathsf T} P^{-1} b. $$

*Proof.* Expand the right-hand side:

$$ x^{\mathsf T} P x - x^{\mathsf T} P P^{-1} b - b^{\mathsf T} P^{-1} P x
   + b^{\mathsf T} P^{-1} P P^{-1} b - b^{\mathsf T} P^{-1} b
   = x^{\mathsf T} P x - 2b^{\mathsf T} x, $$

using symmetry of $P$ and of $P^{-1}$ to merge the two middle terms and to
cancel the last two. **End of proof.**

Read off the consequence that gets used again and again: a density
proportional to $\exp(-\tfrac12 x^{\mathsf T} P x + b^{\mathsf T} x)$ is the
$\mathcal N(P^{-1}b,\, P^{-1})$ density. In words, the coefficient matrix of
the quadratic term is the inverse covariance, and the mean is the point where
the quadratic is minimized.

**Lemma 6.3 (block factorization, or Schur complement).** Let $V$ be the
symmetric block matrix with blocks $V_{XX}$, $V_{XY}$ on the first block row
and $V_{YX}$, $V_{YY}$ on the second, with $V \succ 0$, so that also
$V_{YY} \succ 0$. Put $A = V_{XY}V_{YY}^{-1}$ and
$S = V_{XX} - V_{XY}V_{YY}^{-1}V_{YX}$, the *Schur complement* of $V_{YY}$.
Then $V = L\, \operatorname{blockdiag}(S,\, V_{YY})\, L^{\mathsf T}$, where $L$
is the block upper-triangular matrix with block rows $(I, A)$ and $(0, I)$;
consequently $\det V = \det S \cdot \det V_{YY}$, and for $u = x - \mu_X$,
$v = y - \mu_Y$ the joint quadratic form splits as

$$ \begin{pmatrix} u \\ v \end{pmatrix}^{\mathsf T} V^{-1} \begin{pmatrix} u \\ v \end{pmatrix}
   = (u - Av)^{\mathsf T} S^{-1} (u - Av) \; + \; v^{\mathsf T} V_{YY}^{-1} v. $$

*Proof.* Multiply the three factors. The product's blocks are
$S + AV_{YY}A^{\mathsf T}$ and $AV_{YY}$ on the first block row, and
$V_{YY}A^{\mathsf T}$ and $V_{YY}$ on the second. Now $A V_{YY} = V_{XY}$ and
$AV_{YY}A^{\mathsf T} = V_{XY}V_{YY}^{-1}V_{YX} = V_{XX} - S$, so the product
is $V$. Determinants multiply, and the two triangular factors have
determinant $1$. Inverting the factorization is easy factor by factor, since a
block-triangular factor inverts by flipping the sign of $A$:
$V^{-1} = L_-^{\mathsf T}\, \operatorname{blockdiag}(S^{-1},\, V_{YY}^{-1})\, L_-$,
where $L_-$ has block rows $(I, -A)$ and $(0, I)$. Sandwiching with $(u, v)$
gives the quadratic-form split, since $L_-$ applied to the stacked
$(u, v)$ returns the stacked $(u - Av,\, v)$. **End of proof.**

**The density route to part 7.** Insert the split into the Definition-1 joint
density. Using $\det V = \det S \det V_{YY}$ to split the normalizer, it
factors as $f(x, y) = f(x \mid y)\, f(y)$ with

$$ f(x \mid y) = \frac{\exp\big(-\tfrac12 (u - Av)^{\mathsf T} S^{-1} (u - Av)\big)}
   {(2\pi)^{n_X/2}(\det S)^{1/2}},
   \qquad
   f(y) = \frac{\exp\big(-\tfrac12 v^{\mathsf T} V_{YY}^{-1} v\big)}
   {(2\pi)^{n_Y/2}(\det V_{YY})^{1/2}} . $$

The second factor is the $Y$ marginal, consistent with Section 6.3, and the
first, for fixed $y$, is the $\mathcal N(\mu_X + A(y - \mu_Y),\, S)$ density:
the same answer as Section 6.9, of which Section 2.5 is the scalar
one-plus-one case. The conditional covariance *is* the Schur complement; that
name is the standard one in the linear-algebra literature.

## 7 The Gaussian Channel

The additive-noise model of this section is the scalar Gaussian channel of
information theory [5, Ch. 9]; only its posterior is needed here, not its
capacity.

### 7.1 Setup and the joint covariance

Let $Y = X + Z$ with $X \sim \mathcal N(0, \sigma_x^2)$ and
$Z \sim \mathcal N(0, \sigma_z^2)$ independent and
$\sigma_x^2, \sigma_z^2 > 0$. The pair $(X, Y)$ is jointly Gaussian: it is the
affine image of the pair $(X, Z)$, which is jointly Gaussian because it is
independent, under the two-by-two matrix with rows $(1, 0)$ and $(1, 1)$.
Its second moments are

$$ \operatorname{Cov}(X, Y) = \operatorname{Cov}(X, X) + \operatorname{Cov}(X, Z)
   = \sigma_x^2 + 0, \qquad
   \operatorname{Var}(Y) = \sigma_x^2 + \sigma_z^2, $$

so the joint covariance matrix has diagonal entries $\sigma_x^2$ and
$\sigma_x^2 + \sigma_z^2$ and both off-diagonal entries equal to $\sigma_x^2$.

### 7.2 The posterior

*Proof.* Apply part 7 of Theorem 2 with $V_{XY} = \sigma_x^2$,
$V_{YY} = \sigma_x^2 + \sigma_z^2$, $V_{XX} = \sigma_x^2$ and zero means:

$$ X \mid Y = y \;\sim\; \mathcal N\left( \frac{\sigma_x^2}{\sigma_x^2 + \sigma_z^2}\, y,\;\;
   \frac{\sigma_x^2 \sigma_z^2}{\sigma_x^2 + \sigma_z^2} \right), $$

the variance coming from

$$ \sigma_x^2 - \frac{(\sigma_x^2)^2}{\sigma_x^2 + \sigma_z^2}
   = \frac{\sigma_x^2(\sigma_x^2 + \sigma_z^2) - \sigma_x^4}{\sigma_x^2 + \sigma_z^2}
   = \frac{\sigma_x^2\sigma_z^2}{\sigma_x^2 + \sigma_z^2} . $$

By Lecture 7's minimum mean-squared-error theorem, the posterior mean
$\hat X = \tfrac{\sigma_x^2}{\sigma_x^2+\sigma_z^2} Y$ is the
minimum-mean-squared-error estimate: the closed form Lecture 7 promised.
**End of proof.**

*Shrinkage reading.* The slope $\tfrac{\sigma_x^2}{\sigma_x^2 + \sigma_z^2}$
always lies strictly between $0$ and $1$, so the estimate pulls the
observation toward the prior mean $0$, by exactly the signal's share of the
total variance.

*Precision form.* The posterior variance satisfies

$$ \frac{1}{\operatorname{Var}(X \mid Y)} = \frac{\sigma_x^2 + \sigma_z^2}{\sigma_x^2\sigma_z^2}
   = \frac{1}{\sigma_x^2} + \frac{1}{\sigma_z^2} . $$

Precisions add: prior information plus channel information. In particular the
posterior variance is below $\min(\sigma_x^2, \sigma_z^2)$, so observing
through even terrible noise strictly helps.

### 7.3 Worked numbers and extremes

Take $\sigma_x^2 = 1$ and $\sigma_z^2 = \tfrac13$. The slope is
$\tfrac{1}{1 + 1/3} = \tfrac{1}{4/3} = \tfrac34$, so $\hat X = \tfrac34 y$;
the variance is $\tfrac{1 \cdot 1/3}{4/3} = \tfrac14$, which the precision
form confirms as $1 + 3 = 4$.

Three extremes:

- $\sigma_z^2 \to 0$: the slope tends to $1$ and the variance to $0$; trust
  the observation.
- $\sigma_z^2 \to \infty$: the slope tends to $0$ and the variance to
  $\sigma_x^2$; fall back on the prior.
- $\sigma_z^2 = \sigma_x^2$: the slope is $\tfrac12$ and the variance is
  $\tfrac{\sigma_x^2}{2}$; split the difference.

### 7.4 Two sampling orderings, and why the second matters

**Claim.** The following two procedures produce the same joint distribution of
$(X, Y)$.

- *Forward.* Sample $X \sim \mathcal N(0, \sigma_x^2)$, then set $Y = X + Z$
  with fresh $Z \sim \mathcal N(0, \sigma_z^2)$.
- *Observation first.* Sample $Y \sim \mathcal N(0, \sigma_x^2 + \sigma_z^2)$,
  then sample
  $X \sim \mathcal N\big(\tfrac{\sigma_x^2}{\sigma_x^2+\sigma_z^2}Y,\;
  \tfrac{\sigma_x^2\sigma_z^2}{\sigma_x^2+\sigma_z^2}\big)$.

*Proof.* Both procedures produce a jointly Gaussian pair: the first by Section
7.1; the second because $(Y, X) = (Y,\; aY + \tilde Z)$ with
$a = \tfrac{\sigma_x^2}{\sigma_x^2+\sigma_z^2}$ and $\tilde Z$ independent of
$Y$, an affine image of independent Gaussians. So by part 5 of Theorem 2 it
suffices to match means and covariances. All means are zero, since
$\mathbb E[X] = a\,\mathbb E[Y] = 0$. For the second procedure,
$\operatorname{Var}(Y) = \sigma_x^2 + \sigma_z^2$;
$\operatorname{Cov}(X, Y) = a \operatorname{Var}(Y) = \sigma_x^2$; and

$$ \operatorname{Var}(X) = a^2 \operatorname{Var}(Y) + \operatorname{Var}(\tilde Z)
   = \frac{\sigma_x^4}{\sigma_x^2 + \sigma_z^2} + \frac{\sigma_x^2\sigma_z^2}{\sigma_x^2+\sigma_z^2}
   = \sigma_x^2 . $$

Same $(\mu, V)$, same distribution. **End of proof.**

The forward ordering is how nature, or a diffusion forward pass, generates
data. The observation-first ordering is how a *generator* must run: it holds
$y$ and needs a coherent sample of the cleaner variable. Section 8.8 uses
exactly this reversal, one diffusion step at a time.

## 8 Gaussian Diffusion

### 8.1 The forward recursion and its kernel

Fix $\beta \in (0, 1)$. Given $X_0$, any starting distribution whose MGF is
finite near $0$, define

$$ X_n = \sqrt{1 - \beta}\; X_{n-1} + \sqrt{\beta}\; Z_n, $$

with $Z_n \sim \mathcal N(0, 1)$ independent and identically distributed and
independent of the past. This is a Markov chain, in the sense of Lecture 4, on
$\mathbb{R}$, with Gaussian transition kernel
$X_n \mid X_{n-1} = x \sim \mathcal N(\sqrt{1-\beta}\,x,\; \beta)$: shrink
toward $0$, then add a fixed dose of noise.

### 8.2 Variance preserving, and contracting

**Claim.** $\mathbb E[X_n] = (1-\beta)^{n/2}\, \mathbb E[X_0] \to 0$, and
$\operatorname{Var}(X_n) - 1 = (1-\beta)^n \big( \operatorname{Var}(X_0) - 1 \big) \to 0$.
In particular if $X_0 \sim \mathcal N(0,1)$ then $X_n \sim \mathcal N(0, 1)$
for every $n$: the standard normal is a fixed point.

*Proof.* Means: $\mathbb E[X_n] = \sqrt{1-\beta}\,\mathbb E[X_{n-1}]$; iterate.
Variances, using independence of $Z_n$ from $X_{n-1}$:
$\operatorname{Var}(X_n) = (1-\beta)\operatorname{Var}(X_{n-1}) + \beta$, so

$$ \operatorname{Var}(X_n) - 1 = (1-\beta)\big(\operatorname{Var}(X_{n-1}) - 1\big), $$

a contraction with factor $1 - \beta < 1$; iterate. For the fixed-point claim,
with $X_0 \sim \mathcal N(0,1)$ each $X_n$ is a linear combination of
independent Gaussians, hence Gaussian by the tool recalled in Section 6.1,
with mean $0$ and variance $1$ by the two recursions. **End of proof.**

### 8.3 The MGF telescope, by full induction

**Claim.** For every $n \geq 0$ and every $t$ where the MGFs are defined,

$$ M_{X_n}(t) = M_{X_0}\big( (1-\beta)^{n/2}\, t \big) \cdot
   \exp\Big( \tfrac{t^2}{2}\, \big(1 - (1-\beta)^n\big) \Big). $$

*Proof.* One step, by independence of $X_{n-1}$ and $Z_n$ and the
standard-normal MGF $e^{t^2/2}$ from Lecture 5:

$$ M_{X_n}(t) = \mathbb E\big[ e^{t\sqrt{1-\beta}X_{n-1}} \big] \,
   \mathbb E\big[ e^{t\sqrt{\beta}Z_n} \big]
   = M_{X_{n-1}}\big(\sqrt{1-\beta}\, t\big)\, e^{\beta t^2 / 2}. $$

Now induct on $n$. The base case $n = 0$ is trivial, since
$1 - (1-\beta)^0 = 0$. Assuming the claim at $n - 1$ and applying the one-step
identity at argument $\sqrt{1-\beta}\,t$,

$$ M_{X_n}(t) = M_{X_0}\big( (1-\beta)^{(n-1)/2} \sqrt{1-\beta}\, t \big)
   \exp\Big( \tfrac{(1-\beta)t^2}{2} \big( 1 - (1-\beta)^{n-1} \big) \Big) e^{\beta t^2/2}, $$

and the exponents combine, since
$(1-\beta)\big(1 - (1-\beta)^{n-1}\big) + \beta = 1 - (1-\beta)^n$. **End of
proof.**

*Two-step sanity check.* At $n = 2$ the noise coefficient is
$1 - (1-\beta)^2 = \beta + (1-\beta)\beta = \beta(2 - \beta)$.

*Source note.* The LaTeX source `probability25.tex` writes this two-step
exponent as $1 - (1-\beta)$; the geometric sum gives $1 - (1-\beta)^2$, as the
lecture itself notes and as the numerical check confirms: at $\beta = 0.02$,
$\beta + (1-\beta)\beta = 0.0396 = 1 - 0.98^2$.

### 8.4 Theorem 3: convergence to the standard normal

**Theorem 3.** For any $X_0$ whose MGF is finite in a neighborhood of $0$,
$X_n \to \mathcal N(0, 1)$ in distribution as $n \to \infty$.

*Proof.* Fix $t$. Since $(1-\beta)^{n/2} t \to 0$, and $M_{X_0}$ is finite
near $0$ and continuous there with $M_{X_0}(0) = 1$, the first factor of
Section 8.3 tends to $1$; the second tends to $e^{t^2/2}$. So
$M_{X_n}(t) \to e^{t^2/2}$, the $\mathcal N(0,1)$ MGF, for all $t$ in a
neighborhood of $0$; and MGF convergence on a neighborhood of $0$ implies
convergence in distribution, by the continuity theorem cited alongside MGF
uniqueness in Lecture 5 and in [1]. **End of proof.**

The striking part is that the limit is the same for *every* starting
distribution. The forward process is a data destroyer by design, and its
destination is exactly the fixed point of Section 8.2.

### 8.5 The closed form for $X_n$ given $X_0$, two ways

**Claim.** Conditionally on $X_0 = x_0$,

$$ X_n \mid X_0 = x_0 \;\sim\; \mathcal N\Big( (1-\beta)^{n/2}\, x_0, \;\; 1 - (1-\beta)^n \Big). $$

*Way 1, from the telescope.* Condition the telescope of Section 8.3 on
$X_0 = x_0$, that is, replace $M_{X_0}(s)$ by $e^{s x_0}$:

$$ M_{X_n \mid X_0 = x_0}(t)
   = \exp\big( (1-\beta)^{n/2} x_0\, t + \tfrac{t^2}{2}(1 - (1-\beta)^n) \big), $$

the MGF of the claimed normal; conclude by MGF uniqueness.

*Way 2, unrolling, as an independent check.* Iterate the recursion:

$$ X_n = (1-\beta)^{n/2} x_0 \; + \; \sqrt{\beta} \sum_{k=1}^{n} (1-\beta)^{(n-k)/2}\, Z_k, $$

a constant plus a linear combination of independent standard normals, hence
Gaussian, with mean $(1-\beta)^{n/2}x_0$ and variance

$$ \beta \sum_{k=1}^n (1-\beta)^{n-k}
   = \beta \cdot \frac{1 - (1-\beta)^n}{1 - (1-\beta)} = 1 - (1-\beta)^n $$

by the geometric sum. Same answer. **End of proof.**

So the whole $n$-step corruption collapses to *one* Gaussian sample. That is
the property which makes diffusion training practical: draw a random $n$ and
jump straight to $X_n$, with no simulation of the chain.

### 8.6 The standard notation, and the schedule numbers

Ho, Jain and Abbeel [2] write $\alpha_n = 1 - \beta_n$ and
$\bar\alpha_n = \prod_{i=1}^n \alpha_i$, which allows a step-dependent
schedule $\beta_n$. The closed form generalizes verbatim, by the same
unrolling with products replacing powers, to

$$ X_n \mid X_0 = x_0 \sim \mathcal N\big( \sqrt{\bar\alpha_n}\, x_0,\; 1 - \bar\alpha_n \big), $$

which for the constant schedule used here is $\bar\alpha_n = (1-\beta)^n$:
amplitude $\sqrt{\bar\alpha_n} = (1-\beta)^{n/2}$ and noise variance
$1 - (1-\beta)^n$, the Section 8.5 formula in the standard notation.

**Worked schedule.** With $\beta = 0.02$ and $n = 100$,

$$ \bar\alpha_{100} = 0.98^{100} = e^{100 \ln 0.98} \approx e^{-2.0203} \approx 0.1326, $$

so the lecture's value $\approx 0.133$ is right, and the noise variance is
$\approx 0.8674$. A second point on the same curve: $0.98^{25} \approx 0.6035$,
so about 60 percent of the signal's variance survives 25 steps.

One clarifying remark. The number $0.133$ is the *variance share*
$\bar\alpha_n$ of the signal; the signal's *amplitude* multiplier is
$\sqrt{\bar\alpha_{100}} = 0.98^{50} \approx 0.364$. Either way, at $n = 100$
the sample is mostly noise.

### 8.7 The exact reverse posterior

**Claim** (Ho, Jain and Abbeel [2], equations (6) and (7); the constant
schedule is shown, and the general schedule is identical with $\alpha_n$ and
$\bar\alpha_n$). With $\alpha = 1 - \beta$ and $\bar\alpha_k = (1-\beta)^k$,

$$ X_{n-1} \mid (X_n = x_n, X_0 = x_0) \;\sim\;
   \mathcal N\big( \tilde\mu_n(x_n, x_0),\; \tilde\beta_n \big), $$

where

$$ \tilde\mu_n = \frac{\sqrt{\alpha}\,(1 - \bar\alpha_{n-1})\, x_n
   + \sqrt{\bar\alpha_{n-1}}\,\beta\, x_0}{1 - \bar\alpha_n},
   \qquad
   \tilde\beta_n = \frac{\beta\, (1 - \bar\alpha_{n-1})}{1 - \bar\alpha_n} . $$

*Proof, by completing the square.* By the Markov property,
$q(x_{n-1} \mid x_n, x_0) \propto q(x_n \mid x_{n-1})\, q(x_{n-1} \mid x_0)$ as
a function of $x_{n-1}$, by Bayes' rule with $x_0$ carried along. Both factors
are known Gaussians, the kernel of Section 8.1 and the closed form of Section
8.5 at step $n-1$, so the log-posterior is, up to constants in $x_{n-1}$,

$$ -\frac{(x_n - \sqrt{\alpha}\, x_{n-1})^2}{2\beta}
   \; - \; \frac{(x_{n-1} - \sqrt{\bar\alpha_{n-1}}\, x_0)^2}{2 (1 - \bar\alpha_{n-1})} . $$

Collect the quadratic and linear coefficients of $x_{n-1}$, using Lemma 6.2 in
one dimension: the coefficient of $x_{n-1}^2$ is the posterior precision, and
the precision times the mean is the linear coefficient. The precision is

$$ \frac{\alpha}{\beta} + \frac{1}{1 - \bar\alpha_{n-1}}
   = \frac{\alpha(1 - \bar\alpha_{n-1}) + \beta}{\beta(1 - \bar\alpha_{n-1})}
   = \frac{1 - \bar\alpha_n}{\beta(1 - \bar\alpha_{n-1})}, $$

using $\alpha(1 - \bar\alpha_{n-1}) + \beta = \alpha - \bar\alpha_n + 1 - \alpha
= 1 - \bar\alpha_n$, so $\tilde\beta_n$ is its reciprocal, as claimed. The
linear coefficient is
$\tfrac{\sqrt\alpha}{\beta} x_n + \tfrac{\sqrt{\bar\alpha_{n-1}}}{1-\bar\alpha_{n-1}} x_0$;
multiplying it by $\tilde\beta_n$,

$$ \tilde\mu_n = \frac{\beta(1-\bar\alpha_{n-1})}{1-\bar\alpha_n}
   \left( \frac{\sqrt\alpha}{\beta}\, x_n
   + \frac{\sqrt{\bar\alpha_{n-1}}}{1-\bar\alpha_{n-1}}\, x_0 \right)
   = \frac{\sqrt\alpha (1-\bar\alpha_{n-1})\, x_n
   + \sqrt{\bar\alpha_{n-1}}\,\beta\, x_0}{1-\bar\alpha_n} . $$

**End of proof.**

*Sanity checks.*

- At $n = 1$: $\bar\alpha_0 = 1$ gives $\tilde\beta_1 = 0$ and
  $\tilde\mu_1 = x_0$. Conditioning on both endpoints of a one-step chain pins
  $X_0$ exactly.
- The coefficients of $x_n$ and of $x_0$ in $\tilde\mu_n$ sum to
  $\tfrac{\sqrt\alpha(1-\bar\alpha_{n-1}) + \sqrt{\bar\alpha_{n-1}}\beta}{1-\bar\alpha_n}$,
  which tends to $1$ as $\alpha \to 1$: a convex-combination flavour.
- $\tilde\beta_n < \beta$: the reverse step, once told $x_0$, is *less* noisy
  than the forward kernel.

This exact posterior is what diffusion training actually regresses against;
its mean, reparameterized through the noise, is the target of the
$\epsilon_\theta$ network in [2]. At generation time $x_0$ is unknown, and the
network's prediction stands in for it. The lecture deliberately stops at the
approximation of Section 8.8, and this subsection is the missing rigorous step
between the two.

### 8.8 The lecture's approximation: one reverse step via the channel

**Claim (stationary regime).** If $X_{n-1} \sim \mathcal N(0,1)$, which holds
late in the chain and is justified by Theorem 3 and the fixed point of Section
8.2, then *exactly*

$$ X_{n-1} \mid X_n = x_n \;\sim\; \mathcal N\big( \sqrt{1-\beta}\; x_n, \;\; \beta \big). $$

*Proof.* The pair $(X_{n-1}, X_n)$ is jointly Gaussian with
$\operatorname{Var}(X_{n-1}) = 1$,
$\operatorname{Var}(X_n) = (1-\beta) + \beta = 1$ and
$\operatorname{Cov}(X_{n-1}, X_n) = \sqrt{1-\beta}\, \operatorname{Var}(X_{n-1}) = \sqrt{1-\beta}$.
By part 7 of Theorem 2 the mean is
$\tfrac{\sqrt{1-\beta}}{1} x_n = \sqrt{1-\beta}\, x_n$ and the variance is
$1 - \tfrac{(\sqrt{1-\beta})^2}{1} = 1 - (1-\beta) = \beta$. **End of proof.**

*Flag on one intermediate line.* The lecture's headline result
$\mathcal N(\sqrt{1-\beta}\,x_n,\, \beta)$ is exactly right, but its
derivation records the intermediate step as
"variance $(1-\beta)\beta/1 = (1-\beta)\beta \approx \beta$". That
intermediate is the Section-7 posterior variance of the *scaled signal*
$\sqrt{1-\beta}\,X_{n-1}$: a channel with $\sigma_x^2 = 1-\beta$ and
$\sigma_z^2 = \beta$ gives $\tfrac{(1-\beta)\beta}{1}$. Dividing by the square
of the scale, $1-\beta$, recovers the variance of $X_{n-1}$ itself as exactly
$\beta$, with no small-$\beta$ approximation needed at that step. The genuine
approximation is elsewhere, and is honestly labelled: it is the use of the
stationary $\mathcal N(0,1)$ for $X_{n-1}$, which is only asymptotically true
early in the chain. Consistency check against Section 8.7: averaging the exact
posterior over the conditional distribution of $x_0$ given $x_n$ at
stationarity indeed returns $\mathcal N(\sqrt{\alpha}\,x_n, \beta)$, which
matches.

### 8.9 Vectors, and the generation skeleton

Everything above is coordinatewise independent, so it lifts to $\mathbb{R}^d$
verbatim: $X_n = \sqrt{1-\beta}\,X_{n-1} + \sqrt{\beta}\,Z_n$ with
$Z_n \sim \mathcal N(0, I_d)$, closed form
$X_n \mid X_0 = x_0 \sim \mathcal N(\sqrt{\bar\alpha_n}\, x_0,\; (1 - \bar\alpha_n) I_d)$,
and limit $\mathcal N(0, I_d)$. All covariances stay multiples of $I_d$, since
the recursion never mixes coordinates.

The sampler is Algorithm 2 of [2]: draw $x_T \sim \mathcal N(0, I_d)$; for
$n = T, T-1, \dots, 1$ sample
$x_{n-1} \sim \mathcal N(\mu_\theta(x_n, n),\, \beta I_d)$; return $x_0$. Every
line is a Gaussian sample, and all the learning is hidden in the mean function
$\mu_\theta$, the network's stand-in for the exact $\tilde\mu_n$ of Section
8.7, whose dependence on $x_0$ is what must be learned.

*Scope.* What this lecture does not cover, namely the variational training
objective, its decomposition into Kullback-Leibler terms, score matching, and
continuous-time limits, is the subject of Sohl-Dickstein and coauthors [3] and
Ho and coauthors [2]. These notes stay, like the lecture, at the probability
layer that those papers build on.

## 9 Gaussian Discriminant Analysis

### 9.1 The model and the decision rule

Labels $Y \in \{0, 1, \dots\}$ carry priors $\pi_y = \mathbb P(Y = y)$, and the
class-conditional features are
$X \mid Y = y \sim \mathcal N(\mu_y, \Sigma_y)$ on $\mathbb{R}^n$, each
$\Sigma_y \succ 0$. Classification is Lecture 7's maximum-a-posteriori rule,
with the density standing in for the likelihood:

$$ \hat y(x) = \arg\max_y \; \pi_y \, f(x \mid \mu_y, \Sigma_y)
   = \arg\max_y \Big[ \log \pi_y - \tfrac12 \log \det \Sigma_y
   - \tfrac12 (x - \mu_y)^{\mathsf T} \Sigma_y^{-1} (x - \mu_y) \Big], $$

taking logarithms, which is monotone, and dropping the shared term
$-\tfrac n2 \log 2\pi$. By Lecture 7's Bayes-optimality theorem, if the model
is correct then this rule minimizes the probability of error among *all*
classifiers.

### 9.2 The boundary: quadratic in general, linear for a shared covariance

*Derivation, two classes.* The boundary is the set where the two bracketed
scores tie. Their difference is

$$ \tfrac12 (x-\mu_1)^{\mathsf T}\Sigma_1^{-1}(x-\mu_1)
   - \tfrac12 (x-\mu_0)^{\mathsf T}\Sigma_0^{-1}(x-\mu_0)
   + \tfrac12 \log\frac{\det\Sigma_1}{\det\Sigma_0}
   + \log\frac{\pi_0}{\pi_1} = 0, $$

whose quadratic part in $x$ is
$\tfrac12 x^{\mathsf T}(\Sigma_1^{-1} - \Sigma_0^{-1})x$: a genuine quadric
surface whenever $\Sigma_0 \neq \Sigma_1$. Geometrically the boundary is then a
curve that bends around the class with the tighter covariance.

If $\Sigma_0 = \Sigma_1 = \Sigma$, the quadratic terms cancel. Expanding
$(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)
= x^{\mathsf T}\Sigma^{-1}x - 2\mu^{\mathsf T}\Sigma^{-1}x + \mu^{\mathsf T}\Sigma^{-1}\mu$
for both classes, the difference collapses to the *linear* equation

$$ (\mu_0 - \mu_1)^{\mathsf T} \Sigma^{-1} x =
   \tfrac12\big( \mu_0^{\mathsf T}\Sigma^{-1}\mu_0 - \mu_1^{\mathsf T}\Sigma^{-1}\mu_1 \big)
   + \log\frac{\pi_1}{\pi_0}, $$

a hyperplane with normal vector $w = \Sigma^{-1}(\mu_0 - \mu_1)$. That is
linear discriminant analysis [4, Ch. 4.2] and, one sigmoid away, the
functional form of logistic regression. **End of proof.**

### 9.3 The likelihood, assembled

Estimation decouples across classes, since each sample's log-likelihood
involves only its own class's parameters. So fix one class, with samples
$x^{(1)}, \dots, x^{(N)}$ independent and identically distributed
$\mathcal N(\mu, \Sigma)$. From Definition 1 and independence, the
log-likelihood is

$$ \ell(\mu, \Sigma) = -\frac{Nn}{2}\log 2\pi \; - \; \frac N2 \log\det\Sigma
   \; - \; \frac12 \sum_{i=1}^N (x^{(i)} - \mu)^{\mathsf T} \Sigma^{-1} (x^{(i)} - \mu), $$

which is Lecture 7's recipe, the logarithm of a product of densities.

### 9.4 Maximizing over the mean

**Lemma 9.1 (gradient of a quadratic form).** For symmetric $M$,
$\nabla_\mu\, (x - \mu)^{\mathsf T} M (x - \mu) = -2M(x - \mu)$.

*Proof.* Expand:
$(x-\mu)^{\mathsf T}M(x-\mu) = x^{\mathsf T}Mx - 2\mu^{\mathsf T}Mx + \mu^{\mathsf T}M\mu$,
merging the two cross terms by symmetry. Taking gradients in $\mu$ gives
$0 - 2Mx + 2M\mu = -2M(x - \mu)$, using
$\nabla_\mu (\mu^{\mathsf T} a) = a$ and
$\nabla_\mu(\mu^{\mathsf T}M\mu) = 2M\mu$ for symmetric $M$, both of which
follow from the entrywise definition of the gradient. **End of proof.**

*Derivation.* With $M = \Sigma^{-1}$, symmetric because $\Sigma$ is,

$$ \nabla_\mu \ell = \Sigma^{-1} \sum_{i=1}^N (x^{(i)} - \mu)
   = \Sigma^{-1}\Big( \sum_i x^{(i)} - N\mu \Big), $$

and setting this to zero gives $\hat\mu = \frac1N \sum_{i=1}^N x^{(i)}$, since
$\Sigma^{-1}$ is invertible. It is a maximum in $\mu$, because $\ell$ is a
concave quadratic in $\mu$, with Hessian $-N\Sigma^{-1} \prec 0$. The answer is
the sample mean: the same as Lecture 7's one-dimensional Gaussian
maximum-likelihood estimate, now in vector form. **End of proof.**

### 9.5 Reparameterizing in the precision, and the trace trick

Maximizing over $\Sigma$ directly puts the variable inside an inverse *and* a
determinant. The move is to optimize over the precision $\Phi = \Sigma^{-1}$
instead, a bijection of the positive definite matrices under which
$\log\det\Sigma = -\log\det\Phi$, and to flatten the quadratic forms with the
**trace trick**.

**Lemma 9.2.** $v^{\mathsf T} \Phi v = \operatorname{tr}(v v^{\mathsf T} \Phi)$
for any vector $v$ and any square $\Phi$.

*Proof.* $v^{\mathsf T}\Phi v$ is a scalar, hence equals its own trace; and
$\operatorname{tr}(AB) = \operatorname{tr}(BA)$, since both equal
$\sum_{i,j} A_{ij}B_{ji}$. Taking $A = v^{\mathsf T}$ and $B = \Phi v$ gives
$\operatorname{tr}(v^{\mathsf T} \cdot \Phi v)
= \operatorname{tr}(\Phi v \cdot v^{\mathsf T}) = \operatorname{tr}(v v^{\mathsf T} \Phi)$.
**End of proof.**

Summing over samples at $\mu = \hat\mu$, and introducing the *scatter matrix*
$S = \sum_{i=1}^N (x^{(i)} - \hat\mu)(x^{(i)} - \hat\mu)^{\mathsf T}$, which is
all the data the likelihood ever sees about $\Sigma$,

$$ \ell(\hat\mu, \Phi) = \text{const} + \frac N2 \log\det\Phi
   - \frac12 \operatorname{tr}(S\,\Phi). $$

### 9.6 The two matrix-calculus identities

**Lemma 9.3.** $\nabla_X \operatorname{tr}(AX) = A^{\mathsf T}$, where
$(\nabla_X f)_{ij} = \partial f / \partial X_{ij}$ and the entries of $X$ are
treated as independent.

*Proof.* $\operatorname{tr}(AX) = \sum_k (AX)_{kk} = \sum_{k,l} A_{kl} X_{lk}$.
Each entry $X_{ij}$ appears exactly once, with coefficient $A_{ji}$, so
$\partial \operatorname{tr}(AX)/\partial X_{ij} = A_{ji}$, that is,
$\nabla_X \operatorname{tr}(AX) = A^{\mathsf T}$. **End of proof.**

**Lemma 9.4.** For invertible $X$ with $\det X > 0$,
$\nabla_X \log\det X = (X^{-1})^{\mathsf T}$.

*Proof.* Cofactor-expand along row $i$: $\det X = \sum_l X_{il} C_{il}$, where
the cofactor $C_{il}$, being $(-1)^{i+l}$ times the minor that deletes row $i$
and column $l$, contains no entry of row $i$. So
$\partial \det X / \partial X_{ij} = C_{ij}$, that is,
$\nabla_X \det X = C$. Cramer's adjugate identity
$X^{-1} = \operatorname{adj}(X)/\det X$ with
$\operatorname{adj}(X) = C^{\mathsf T}$ gives
$C = \det X \cdot (X^{-1})^{\mathsf T}$. By the chain rule,
$\nabla_X \log\det X = \tfrac{1}{\det X}\, C = (X^{-1})^{\mathsf T}$. **End of
proof.**

For symmetric positive definite $\Phi$ one has
$(\Phi^{-1})^{\mathsf T} = \Phi^{-1}$. The standard caveat, that treating the
symmetric entries as constrained changes the off-diagonal derivatives by a
factor of $2$, does not change the stationary point, because the unconstrained
critical point found next is already symmetric.

### 9.7 Solving for the covariance, and Theorem 4

*Derivation.* By Lemmas 9.3 and 9.4,

$$ \nabla_\Phi\, \ell = \frac N2 (\Phi^{-1})^{\mathsf T} - \frac12 S^{\mathsf T}
   = \frac N2 \Sigma - \frac12 S, $$

using symmetry of $\Phi^{-1} = \Sigma$ and of $S$ to drop the transposes.
Setting this to zero gives

$$ \hat\Sigma = \frac1N S
   = \frac1N \sum_{i=1}^N (x^{(i)} - \hat\mu)(x^{(i)} - \hat\mu)^{\mathsf T} . $$

That this is the global maximum and not a saddle: the map
$\Phi \mapsto \log\det\Phi$ is concave on the positive definite cone
(standard; Boyd and Vandenberghe [7, Section 3.1.5]) and
$\operatorname{tr}(S\Phi)$ is linear, so $\ell(\hat\mu, \cdot)$ is concave and
its unique critical point is the global maximizer. When $S \succ 0$, which
holds almost surely once $N > n$, the function tends to $-\infty$ on the
boundary and at infinity, so the maximum is attained. **End of proof.**

**Theorem 4 (Gaussian maximum likelihood).** For independent and identically
distributed $\mathcal N(\mu, \Sigma)$ samples, the maximum-likelihood
estimates are $\hat\mu = \tfrac1N\sum_i x^{(i)}$ and
$\hat\Sigma = \tfrac1N\sum_i (x^{(i)} - \hat\mu)(x^{(i)} - \hat\mu)^{\mathsf T}$.
In discriminant analysis they are applied per class, together with
$\hat\pi_y = N_y / N$, the count estimate, which is Lecture 7's
Bernoulli and multinomial maximum-likelihood estimate.

**Bias remark.** $\mathbb E[\hat\Sigma] = \tfrac{N-1}{N}\Sigma$. Writing
$\bar x = \hat\mu$,

$$ \sum_i (x^{(i)} - \bar x)(x^{(i)} - \bar x)^{\mathsf T}
   = \sum_i x^{(i)} x^{(i)\mathsf T} - N \bar x \bar x^{\mathsf T}, $$

by expanding and using $\sum_i x^{(i)} = N\bar x$. Take expectations with
$\mathbb E[x x^{\mathsf T}] = \Sigma + \mu\mu^{\mathsf T}$ and
$\mathbb E[\bar x \bar x^{\mathsf T}] = \tfrac1N \Sigma + \mu\mu^{\mathsf T}$,
the latter because $\operatorname{Cov}(\bar x) = \Sigma / N$ for independent
and identically distributed samples:

$$ N(\Sigma + \mu\mu^{\mathsf T}) - N\big(\tfrac1N\Sigma + \mu\mu^{\mathsf T}\big)
   = (N-1)\Sigma . $$

Divide by $N$. **End of proof.** This is the same factor $\tfrac{N-1}{N}$ of
shrinkage as in Lecture 7's one-dimensional variance estimate; it vanishes as
$N \to \infty$, so the estimator is asymptotically unbiased, and the dimension
$n$ plays no role in the factor.

*Pipeline check.* Fit $(\hat\pi_y, \hat\mu_y, \hat\Sigma_y)$ per class by
Theorem 4, then classify by the rule of Section 9.1. In one dimension with two
classes and a shared variance this collapses exactly to Lecture 7's
two-Gaussian height classifier, with the Section 9.2 boundary reducing to the
midpoint threshold shifted by the prior derived there.

## 10 References

1. MIT OpenCourseWare, *6.436J / 15.085J Fundamentals of Probability*, Fall
   2018. The source the lecture credits: the three definitions, their
   equivalence, and the properties theorem follow its Lecture 14, on
   multivariate normal distributions, and MGF uniqueness is its Section 4.10.
   Licensed CC BY-NC-SA 4.0.
   https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/
2. J. Ho, A. Jain, P. Abbeel, "Denoising Diffusion Probabilistic Models,"
   NeurIPS 2020. Source of the $\bar\alpha$ notation of Section 8.6, the exact
   reverse posterior of Section 8.7, its equations (6) and (7), and the sampler
   of Section 8.9, its Algorithm 2. arXiv:2006.11239
   https://arxiv.org/abs/2006.11239
3. J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, S. Ganguli, "Deep
   Unsupervised Learning using Nonequilibrium Thermodynamics," ICML 2015. The
   origin of the Gaussian-diffusion generative framework of Section 8.
   arXiv:1503.03585 https://arxiv.org/abs/1503.03585
4. C. M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006.
   Chapter 2.3 for Gaussian marginals and conditionals via completing the
   square, the Section 6.10 route; Chapter 4.2 for discriminant analysis.
   https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
5. T. M. Cover, J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley, 2006. Chapter 8 for the maximum-entropy characterization behind
   Section 1.2; Chapter 9 for the Gaussian channel of Section 7.
   DOI: 10.1002/047174882X https://doi.org/10.1002/047174882X
6. Companion notes in this series: Lecture 3 for maximum entropy and the
   one-dimensional Gaussian normalization, Lecture 4 for independence and
   Markov chains, Lecture 5 for MGFs, the uniqueness statement and the central
   limit theorem, Lecture 7 for conditional expectation, the
   orthogonality and minimum mean-squared-error machinery, the
   maximum-likelihood recipe, Bayes optimality and bias.
7. S. Boyd, L. Vandenberghe, *Convex Optimization*, Cambridge University
   Press, 2004. Section 3.1.5 for the concavity of $\log\det$ on the positive
   definite cone, the fact that makes the critical point of Section 9.7 the
   global maximizer. https://web.stanford.edu/~boyd/cvxbook/
