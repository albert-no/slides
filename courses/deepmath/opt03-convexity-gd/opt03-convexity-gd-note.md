# Deep Learning Math 12. Convexity, Smoothness and Gradient Descent

**About this file.** This is the accessible Markdown edition of the lecture note for Lecture 12 (opt03), written to be read linearly by a screen reader or a braille display. Every figure and every table of the original has been replaced by prose carrying the same information, every matrix is written out row by row, and all mathematics is in LaTeX. The section numbering matches the original note exactly, so a reference to "Section 6.2" means the same thing in both. Nothing else is needed to read it.

**Convention.** $f:\mathbb{R}^n\to\mathbb{R}$ is differentiable unless stated otherwise; $\|\cdot\|$ is the Euclidean norm and $\langle\cdot,\cdot\rangle$ the standard inner product. The phrase "$L$-smooth" always means *the gradient $\nabla f$ is $L$-Lipschitz*, never "$f$ is $L$-Lipschitz"; these are different conditions and Section 3.1 separates them. $x^\star$ denotes a global minimizer and $f^\star = f(x^\star)$. For symmetric matrices, $P\succeq Q$ means $P-Q$ is positive semidefinite. Gradient descent is the iteration $x_{i+1}=x_i-\alpha\nabla f(x_i)$ with a constant step $\alpha>0$.

**The running example.** Throughout,

$ f(x)=2x_1^2+\tfrac12 x_2^2,\qquad \nabla f(x)=(4x_1,\;x_2), $

and the Hessian $\nabla^2 f$ is the constant matrix with first row $(4,0)$ and second row $(0,1)$, that is $\operatorname{diag}(4,1)$. So $L=4$, $\mu=1$, $x^\star=0$, $f^\star=0$, and the condition number is $\kappa=L/\mu=4$.

**Notation.**

- $\nabla f$, $\nabla^2 f$: gradient and Hessian.
- $L$: smoothness constant; $\mu$: strong-convexity constant; $\kappa = L/\mu$: condition number.
- $\alpha$: step size; $x_i$: the $i$-th gradient-descent iterate; $T$: number of iterations.
- $\|M\|_2$: spectral norm of a matrix, the largest absolute eigenvalue for symmetric $M$.
- $\operatorname{diag}(a,b)$: the diagonal matrix with those diagonal entries.
- $e_1$, $e_2$: the standard basis vectors.
- $\varphi_{x,d}(t)=f(x+td)$: the restriction of $f$ to the line through $x$ in direction $d$.
- PL: the Polyak-Lojasiewicz inequality of Section 5.5.
- $I$: identity matrix; $P\succ 0$: positive definite.

**Background used.** Multivariable calculus: the chain rule, the fundamental theorem of calculus along a segment, the mean value theorem, Taylor's theorem, and Fermat's rule that a differentiable local minimizer is stationary. From linear algebra: symmetric matrices, eigenvalues, the spectral norm, and the positive semidefinite order, all as set up in Lecture 10 (opt01). From Lecture 11 (opt02): the least-squares objective $\tfrac12\|A\theta-B\|^2$, which is the convex objective this lecture optimizes. No probability is used until Section 9.6.

**What this edition adds.** Nothing mathematical. The only changes are linearization: the three-tier rate table of Section 1 and the iterate table of Section 6.3 turned into bullet lists, matrices written out row by row, boxed statements turned into bold-labelled paragraphs.

**Contents.**

1. What this lecture actually claims
2. Convexity
3. Smoothness
4. Smooth and convex: co-coercivity
5. Strong convexity
6. Gradient descent
7. Rate I: the $O(1/T)$ rate for smooth convex $f$
8. Rate II: linear convergence under strong convexity
9. What the lecture leaves out
10. References

**Summary of what is proved here.** Proposition 2.1, that a local minimizer of a convex function is global; Theorem 2.2, the first-order (tangent-floor) characterization, in both directions; Corollary 2.3, that stationary implies global for convex $f$; Lemma 2.4, restriction to a line, and Lemma 2.5, the scalar Hessian test, combining into Theorem 1 (the Hessian test); Lemma 3.1, the descent lemma, in its two-sided form; Theorem 3.2, that $L$-smoothness is equivalent to a spectral-norm bound on the Hessian, in both directions; Theorem 3, the sandwich inequality; Theorem 4 of the lecture, co-coercivity, both parts, and the four-way equivalence of Section 4.4; Theorem 4 on strong convexity and the Hessian; existence and uniqueness of $x^\star$ under strong convexity; Lemma 3, the Polyak-Lojasiewicz inequality, and the fact that strong convexity implies it; Theorems 5 and 6, monotonicity of the gradient; the exact spectral analysis of gradient descent on a quadratic, showing the step-size cliff at $2/L$ is sharp; Theorem 7 and its nonconvex corollary; Theorem 8, the $O(1/T)$ rate, with Fejer monotonicity upgrading it to iterate convergence; Theorem 9, extended co-coercivity, including the isotropic case the original derivation divides away; and Theorem 10, linear convergence, with the optimal step size $\alpha=2/(\mu+L)$.

**How to use.** One article per baseline slide, in slide order, headed by slide number and title. Section references (Section N, Section N.M) point to the original section headings, kept as subheadings inside the article where that material now sits.

<!-- REGION Opening BEGIN -->

<!-- BEGIN S01 -->
### 1. Gradient Descent: Three Guarantees [S01]

**Message.** One algorithm, gradient descent with step $1/L$; three assumptions give three different guarantees.

Lecture 12 of Deep Learning Math (90 minutes). It studies one algorithm, gradient descent with the fixed step $1/L$, and asks what can be guaranteed about it. Smoothness alone gives approximate stationarity; adding convexity gives an $O(1/T)$ function gap; adding strong convexity gives geometric decay of the distance to the minimizer.
<!-- END S01 -->

<!-- BEGIN S02 -->
### 2. Contents [S02]

**Message.** Six parts: the update, the one inequality every proof uses, then one guarantee per assumption, then the comparison.

1. One Update: Step against the gradient.
2. One Descent Inequality: Smoothness bounds every step.
3. Nonconvex: Stationarity: Small gradients, not minima.
4. Convex: Optimality: Function gap at rate 1/T.
5. Strongly Convex: Geometric Decay: Distance shrinks every step.
6. Three Guarantees: Same step, different assumptions.
<!-- END S02 -->

<!-- REGION Opening END -->

<!-- REGION P4a BEGIN -->

<!-- BEGIN S79 -->
### 3. Part 1: One Update [S79]

**Message.** Part 1 fixes the algorithm: gradient descent with step $1/L$, where $L$ bounds how fast the gradient changes.
<!-- END S79 -->

<!-- BEGIN S80 -->
### 4. Goal: Minimize One Differentiable $f$ [S80]

**Message.** The whole lecture studies one problem: minimize a differentiable $f:\mathbb{R}^n\to\mathbb{R}$ using its exact gradient.

The problem is unconstrained: $x$ ranges over all of $\mathbb{R}^n$ and $f$ is differentiable. The algorithm is deterministic: at every step it uses the exact gradient $\nabla f(x)$, with no sampling noise. Stochastic gradients are not part of this lecture.

The figure is a schematic one-dimensional slice of a nonconvex $f$. The horizontal axis is the input, the vertical axis is $f$. Starting from the left, the curve falls into a local minimum (blue dot), rises to a local maximum (grey dot), then falls and flattens toward a dashed horizontal line labelled $f_{\text{low}}$. The tail approaches that line but never reaches it.

The picture fixes two words for the nonconvex part of the lecture. First, $f$ may have several stationary points, and not all of them are minima. Second, a lower bound $f_{\text{low}}$ with $f(x)\ge f_{\text{low}}$ for all $x$ can hold even when no minimizer exists. The nonconvex guarantee later assumes only such a lower bound; the convex results add the assumption that a minimizer $x^\star$ exists.

**Details.**

The schematic curve is $f(u)=1.5/(1+e^{2(u-2)})-0.8\,e^{-(u+1)^2}$ for $u\in[-3,5]$. Numerically, its local minimum is near $u\approx-0.995$ with $f\approx0.696$, and its local maximum is near $u\approx0.645$ with $f\approx1.353$ (our calculation). As $u\to\infty$ both terms tend to $0$ and $f$ stays positive, so the infimum $0$ is not attained; the dashed line is drawn at $f_{\text{low}}=0$. The curve is an illustration of the vocabulary, not a function used in any later calculation.

**Sources.**

Problem setup: plan-v1 shared notation. Curve: our illustration (formula above, our calculation).
<!-- END S80 -->

<!-- BEGIN S14 -->
### 5. Recall: The Gradient Gives First-Order Change [S14]

**Message.** The gradient gives the first-order change of $f$, which is a statement about small steps only.

The gradient collects the partial derivatives, $\nabla f(x)=(\partial f/\partial x_1(x),\dots,\partial f/\partial x_n(x))\in\mathbb{R}^n$. Differentiability means $f(x+h)=f(x)+\langle\nabla f(x),h\rangle+o(\|h\|)$ as $h\to0$: near $x$, $f$ is its linear model plus an error that is small compared with $\|h\|$.

Taking $h=sv$ and letting $s\to0$ gives the rate of change along a direction $v$: $\langle\nabla f(x),v\rangle$. This is the only fact the next slide needs to say that moving against the gradient lowers $f$.

The qualifier matters. The $o(\|h\|)$ term says nothing about a fixed, finite step: it only promises that the error becomes negligible as the step shrinks. To control one real step of an algorithm we need a quantitative bound on the error, which is what $L$-smoothness will provide.

**Details.**

For a unit direction $v$, Cauchy-Schwarz gives $\langle\nabla f(x),v\rangle\ge-\|\nabla f(x)\|$, with equality at $v=-\nabla f(x)/\|\nabla f(x)\|$ when $\nabla f(x)\ne0$. So the negative gradient is the direction of fastest first-order decrease.

**Sources.**

Standard definition of the (Frechet) derivative; recalled, not new material.
<!-- END S14 -->

<!-- BEGIN S82 -->
### 6. Small Steps Against the Gradient Go Downhill [S82]

**Message.** A small enough step against the gradient lowers $f$, but a long step in the same direction can raise it.

The figure plots the parabola $f(u)=u^2$. The current point $x$ (dark blue dot, right branch) has $f'(x)>0$, so the negative gradient points left. Two steps go in that same direction. The short step (solid green arrow) lands lower on the curve: $f$ drops. The long step (dashed red arrow) overshoots the bottom and lands high on the left branch: $f$ rises.

So the direction alone does not guarantee progress; the step length matters too. The first-order picture from the previous slide only covers small enough steps. How far is safe is decided by how fast the gradient can change, measured by the smoothness constant $L$ defined next.

**Details.**

Numbers (our calculation): start at $u=1.5$, where $f=2.25$ and $f'(u)=3$. The short step goes to $u=0.9$ (step length $0.2$ times the gradient), and $f$ falls to $0.81$. The long step goes to $u=-1.8$ (step length $1.1$ times the gradient), and $f$ rises to $3.24$. For this $f$, $f'(u)=2u$ is $2$-Lipschitz, so $L=2$ and the step $1/L=1/2$ would land exactly at the minimizer $u=0$.

**Sources.**

Illustration: our calculation.
<!-- END S82 -->

<!-- BEGIN S27 -->
### 7. $L$-Smoothness Bounds Gradient Change [S27]

**Message.** A differentiable $f$ is $L$-smooth when its gradient is $L$-Lipschitz; this limits how fast the slope can change, not $f$ itself.

Definition: a differentiable $f:\mathbb{R}^n\to\mathbb{R}$ is $L$-smooth, for a constant $L>0$, if $\|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|$ for all $x,y\in\mathbb{R}^n$, with the Euclidean norm.

The condition is on the gradient. The function itself may grow without bound: $f(x)=\tfrac12x^2$ has gradient $x$, which is $1$-Lipschitz, so $f$ is $1$-smooth; but $f$ itself is not Lipschitz, because its slope $x$ is unbounded.

Smoothness says nothing about convexity. The nonconvex curve of the opening slide, and the function $1-\cos x$ used later, are smooth and not convex. The first guarantee of the lecture uses smoothness alone.

**Details.**

If $f$ is $L$-smooth it is also $L'$-smooth for every $L'\ge L$; "the" smoothness constant usually means the smallest valid $L$. For a twice-differentiable $f$ that smallest value is $\sup_x\|\nabla^2f(x)\|_2$, the largest spectral norm of the Hessian; the running example on slide 9 checks $L=4$ directly from the definition instead.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Lipschitz continuous gradient assumption (or the L-smoothness assumption)", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06). Example $\tfrac12x^2$: our calculation.
<!-- END S27 -->

<!-- BEGIN S81 -->
### 8. One Fixed Step: $1/L$ [S81]

**Message.** Gradient descent in this lecture uses the single fixed step $1/L$, and the same update appears in all three guarantees.

The algorithm box has three lines. Input: the smoothness constant $L$ and any start $x_0\in\mathbb{R}^n$. Loop: for $t=0,1,\dots,T-1$, set $x_{t+1}=x_t-\tfrac1L\nabla f(x_t)$. Output: the iterates $x_0,x_1,\dots,x_T$.

Fixing one step size keeps the lecture to one proof route: the nonconvex, convex and strongly convex guarantees all analyze exactly this update. $T$ counts gradient evaluations: $T$ steps use the gradients at $x_0,\dots,x_{T-1}$.

$L$ is assumed known. Line search, adaptive steps and other constant steps are deliberately left out.

**Details.**

The source states its results for any constant step $\alpha$ with $\alpha L\le1$; this lecture specializes to $\alpha=1/L$, which gives the cleanest constants. How to estimate $L$ in practice is out of scope here.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06), specialized to $\alpha=1/L$.
<!-- END S81 -->

<!-- BEGIN S30 -->
### 9. Running Example: $L = 4$ [S30]

**Message.** For $f(x)=2x_1^2+\tfrac12x_2^2$ the smoothness constant is exactly $L=4$, so the step is $1/4$.

The running example is $f(x)=2x_1^2+\tfrac12x_2^2$ on $\mathbb{R}^2$, with gradient $\nabla f(x)=(4x_1,x_2)$.

Write $z=x-y$. Then $\nabla f(x)-\nabla f(y)=(4z_1,z_2)$, whose norm is $\sqrt{16z_1^2+z_2^2}$. Since $16z_1^2+z_2^2\le16(z_1^2+z_2^2)$, the norm is at most $4\|z\|$, so $f$ is $4$-smooth.

At $z=(1,0)$ both sides equal $4$, so no smaller constant works: $L=4$ exactly, and gradient descent uses step $1/L=1/4$.

**Details.**

The two coordinates have curvatures $4$ and $1$ (the diagonal of the Hessian $\mathrm{diag}(4,1)$). $L$ is the larger curvature. The smaller one, $\mu=1$, returns in the strongly convex part of the lecture.

**Sources.**

Our calculation (illustrative example; evidence E08, E09).
<!-- END S30 -->

<!-- REGION P4a END -->

<!-- REGION P4b BEGIN -->

<!-- BEGIN S25 -->
### 10. Part 2: One Descent Inequality [S25]

**Message.** Part 2 proves the one inequality that every later guarantee uses: each step lowers $f$ by at least $\frac{1}{2L}\|\nabla f\|^2$.
<!-- END S25 -->

<!-- BEGIN S33 -->
### 11. Smoothness Gives a Quadratic Upper Bound [S33]

**Message.** An $L$-smooth function lies below its linear model plus $\tfrac L2\|y-x\|^2$, for every pair of points.

Lemma (descent lemma). If $f:\mathbb{R}^n\to\mathbb{R}$ is differentiable and $L$-smooth, then for all $x,y\in\mathbb{R}^n$: $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac L2\|y-x\|^2$.

The right side is the linear model of $f$ at $x$ plus a quadratic penalty. Unlike the $o(\|h\|)$ statement of slide 5, this is valid for every finite step, which is exactly what is needed to analyze one step of an algorithm.

No convexity is used. The bound is one-sided: it limits how far $f$ can rise above its linear model, not how far it can fall below it.

**Details.**

The proof follows on the next slides in three steps: restrict $f$ to the segment from $x$ to $y$, bound the change of the slope along it by smoothness, and integrate.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07 step 1).
<!-- END S33 -->

<!-- BEGIN S34 -->
### 12. The Upper Bound Touches $f$ at $x$ [S34]

**Message.** The quadratic upper bound touches $f$ at $x$ and lies above it everywhere else.

The figure shows one variable. The solid black curve is $f$. The dashed blue curve is the upper bound from the lemma, built at the marked point $x$. The thin grey line is the tangent at $x$. All three meet at $x$; the dashed curve stays on or above the solid curve everywhere, and the solid curve bends upward away from the tangent.

Equality holds at $y=x$: there the penalty $\tfrac L2\|y-x\|^2$ is zero and the linear model equals $f(x)$. Away from $x$ the penalty grows quadratically and keeps the bound above $f$.

**Details.**

The drawing uses $f(u)=u^2$, the point $x=-0.6$ and $L=3$ (our drawing). Since $f'(u)=2u$ is $2$-Lipschitz, $f$ is $2$-smooth and hence also $3$-smooth, so $L=3$ is valid. The upper bound minus $f$ equals $\tfrac32(u+0.6)^2-(u+0.6)^2=\tfrac12(u+0.6)^2\ge0$ (our calculation), which is zero only at $u=x$. With $L=2$ the bound would coincide with $f$; $L=3$ was chosen so the two curves are visibly different.

**Sources.**

Illustration: our drawing and calculation (parameters above).
<!-- END S34 -->

<!-- BEGIN S36 -->
### 13. Proof Step 1: Follow the Segment [S36]

**Message.** Restricting $f$ to the segment from $x$ to $y$ turns the lemma into a one-variable calculus statement.

Set $h=y-x$ and $\rho(s)=f(x+sh)$ for $s\in[0,1]$, so $\rho(0)=f(x)$ and $\rho(1)=f(y)$. By the chain rule, $\rho'(s)=\langle\nabla f(x+sh),h\rangle$.

The fundamental theorem of calculus then gives $f(y)-f(x)=\rho(1)-\rho(0)=\int_0^1\rho'(s)\,ds$.

Here $s$ marks a point on the segment; it is not the iteration index $t$.

**Details.**

The fundamental theorem applies because $\rho'$ is continuous: $\nabla f$ is Lipschitz, hence continuous, and $s\mapsto x+sh$ is continuous, so $s\mapsto\langle\nabla f(x+sh),h\rangle$ is continuous on $[0,1]$.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S36 -->

<!-- BEGIN S37 -->
### 14. Proof Step 2: Smoothness Bounds the Drift [S37]

**Message.** Smoothness bounds how far the slope $\rho'(s)$ can drift from $\rho'(0)$: by at most $Ls\|h\|^2$.

Compare the slope at $s$ with the slope at $0$: $\rho'(s)-\rho'(0)=\langle\nabla f(x+sh)-\nabla f(x),h\rangle$.

Cauchy-Schwarz bounds this by $\|\nabla f(x+sh)-\nabla f(x)\|\,\|h\|$. Smoothness bounds the gradient difference by $L$ times the distance between the points, which is $\|sh\|=s\|h\|$. Together: $\rho'(s)-\rho'(0)\le Ls\|h\|^2$.

**Details.**

Only an upper bound is needed, so only one side of Cauchy-Schwarz is used. The same argument with the sign flipped gives $\rho'(s)-\rho'(0)\ge-Ls\|h\|^2$, which would yield a matching lower bound on $f$; the lecture does not need it.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S37 -->

<!-- BEGIN S38 -->
### 15. Proof Step 3: Integrating $s$ Gives $\tfrac{1}{2}$ [S38]

**Message.** Integrating the drift bound over $s\in[0,1]$ produces the factor $\tfrac L2$ and finishes the lemma.

Start from Step 1: $f(y)=f(x)+\int_0^1\rho'(s)\,ds$. Replace $\rho'(s)$ by its Step 2 bound $\rho'(0)+Ls\|h\|^2$. Since $\rho'(0)=\langle\nabla f(x),y-x\rangle$ does not depend on $s$ and $\int_0^1Ls\,ds=\tfrac L2$, the result is $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac L2\|y-x\|^2$.

So the $\tfrac12$ in the lemma is just the average of $s$ over the segment.

**Details.**

Full chain: $f(y)=f(x)+\int_0^1\rho'(s)\,ds\le f(x)+\int_0^1(\rho'(0)+Ls\|h\|^2)\,ds=f(x)+\rho'(0)+\tfrac L2\|h\|^2$, with $h=y-x$.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S38 -->

<!-- BEGIN S90 -->
### 16. The Step $1/L$ Decreases $f$ [S90]

**Message.** Plugging the step $1/L$ into the lemma gives the descent inequality $f(x_{t+1})\le f(x_t)-\tfrac1{2L}\|\nabla f(x_t)\|^2$.

Write $g_t=\nabla f(x_t)$ and apply the lemma with $x=x_t$ and $y=x_{t+1}=x_t-\tfrac1Lg_t$. The linear term is $\langle g_t,-\tfrac1Lg_t\rangle=-\tfrac1L\|g_t\|^2$ and the penalty is $\tfrac L2\|\tfrac1Lg_t\|^2=\tfrac1{2L}\|g_t\|^2$. Adding them gives $f(x_{t+1})\le f(x_t)-\tfrac1{2L}\|g_t\|^2$.

No convexity is used. Every step either keeps $f$ the same (only when $g_t=0$) or strictly lowers it. This single inequality drives all three guarantees in the lecture.

**Details.**

Among steps of the form $x_t-\alpha g_t$, the lemma gives $f(x_{t+1})\le f(x_t)-\alpha(1-\tfrac{L\alpha}2)\|g_t\|^2$, and $\alpha=1/L$ maximizes $\alpha(1-\tfrac{L\alpha}2)$, with value $\tfrac1{2L}$ (our calculation). This explains the choice of step; other step sizes are not used in the lecture.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07 step 1), with $\alpha=1/L$.
<!-- END S90 -->

<!-- BEGIN S83 -->
### 17. One Step Zeroes the Stiff Coordinate [S83]

**Message.** On the running example, one step $1/4$ sets the stiff coordinate to zero and shrinks the flat one by $\tfrac34$.

With $\nabla f(x)=(4x_1,x_2)$ and step $1/4$: $x^+=x-\tfrac14(4x_1,x_2)=((1-\tfrac44)x_1,(1-\tfrac14)x_2)=(0,\tfrac34x_2)$.

Each coordinate is multiplied by $1-(\text{curvature})/L$. The stiff coordinate has curvature $4=L$, so its factor is $0$ and it is exactly zero after one step. The flat coordinate has curvature $1$, so its factor is $\tfrac34$ at every step.

**Details.**

This is special to a diagonal quadratic: the coordinates decouple, so the step acts on each separately. In general the step $1/L$ is tuned to the stiffest direction, and flatter directions move more slowly.

**Sources.**

Our calculation (illustrative example; evidence E08).
<!-- END S83 -->

<!-- BEGIN S84 -->
### 18. Two Steps: $f$ Falls From $10$ to $81/128$ [S84]

**Message.** Two steps from $x_0=(2,2)$ take $f$ from $10$ to $9/8$ to $81/128$, each value below the descent bound.

The table has columns step $t$, iterate $x_t$, value $f(x_t)$, and the descent bound $f(x_{t-1})-\tfrac18\|\nabla f(x_{t-1})\|^2$ (here $\tfrac1{2L}=\tfrac18$). Row $t=0$: $x_0=(2,2)$, $f=10$, no bound. Row $t=1$: $x_1=(0,\tfrac32)$, $f=\tfrac98$, bound $10-\tfrac{68}8=\tfrac32$. Row $t=2$: $x_2=(0,\tfrac98)$, $f=\tfrac{81}{128}$, bound $\tfrac98-\tfrac{9/4}8=\tfrac{27}{32}$.

Each actual value sits below its bound, as the descent inequality promises. The bound is not tight here: the example decreases faster than the generic guarantee.

**Details.**

Gradients: $g_0=(8,2)$ with $\|g_0\|^2=68$; $g_1=(0,\tfrac32)$ with $\|g_1\|^2=\tfrac94$. Values: $f(x_0)=2\cdot4+\tfrac12\cdot4=10$; $f(x_1)=\tfrac12\cdot\tfrac94=\tfrac98$; $f(x_2)=\tfrac12\cdot\tfrac{81}{64}=\tfrac{81}{128}$. Checks: $\tfrac98\le\tfrac32$ and $\tfrac{81}{128}\le\tfrac{27}{32}=\tfrac{108}{128}$.

Squared distances to the minimizer $x^\star=0$ are $8$, $\tfrac94$, $\tfrac{81}{64}$. The first step behaves differently from later ones because it zeroes the stiff coordinate; from $t=1$ on only the second coordinate remains, so both the squared distance and $f$ shrink by exactly $(\tfrac34)^2=\tfrac9{16}$ per step, e.g. $\tfrac{81/128}{9/8}=\tfrac9{16}$. These exact ratios belong to this example, not to a general bound. The baseline table with more iterations is in the backup note.

**Sources.**

Our calculation (illustrative example; evidence E09).
<!-- END S84 -->

<!-- REGION P4b END -->

<!-- REGION P4c BEGIN -->

<!-- BEGIN S135 -->
### 19. Part 3: Nonconvex: Stationarity [S135]

**Message.** Part 3 uses smoothness alone: the smallest gradient seen shrinks, which certifies approximate stationarity, not a minimum.
<!-- END S135 -->

<!-- BEGIN S89 -->
### 20. Nonconvex Guarantee: Small Squared Gradient [S89]

**Message.** For any $L$-smooth $f$ bounded below, $T$ steps of size $1/L$ make the smallest squared gradient at most $2L(f(x_0)-f_{\text{low}})/T$.

Theorem (nonconvex, step $1/L$). Let $f:\mathbb{R}^n\to\mathbb{R}$ be differentiable and $L$-smooth with $f(x)\ge f_{\text{low}}$ for all $x$. For any $x_0$ and every $T\ge1$, the iterates satisfy $\min_{0\le t\le T-1}\|\nabla f(x_t)\|^2\le 2L(f(x_0)-f_{\text{low}})/T$.

The bound concerns the best of the $T$ squared gradients at $x_0,\dots,x_{T-1}$. It is not a bound on a gap $f(x_t)-f^\star$, and it does not say which iterate is best.

Only a lower bound is assumed: $f_{\text{low}}$ need not be attained, and no minimizer is assumed. Convexity is not assumed either.

**Details.**

Indexing: the source states the bound with $f^*$, step $\alpha$ with $\alpha L\le1$, and a minimum over $t\in\{0,\dots,T\}$, i.e. $\min\|\nabla f(w_t)\|^2\le2(f(w_0)-f^*)/(\alpha T)$. Here we use exactly $T$ gradients indexed $0$ to $T-1$, which is what summing $T$ descent inequalities gives (next slides), and replace $f^*$ by any lower bound, which the telescoping proof allows. With $\alpha=1/L$ the constants agree.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06), specialized to $\alpha=1/L$ and a lower bound $f_{\text{low}}$.
<!-- END S89 -->

<!-- BEGIN S91 -->
### 21. Proof Step 1: Sum the Decreases [S91]

**Message.** Adding the descent inequality over $T$ steps telescopes, so the total squared gradient is capped by the finite budget $f(x_0)-f_{\text{low}}$.

Rearrange the descent inequality as $\tfrac1{2L}\|\nabla f(x_t)\|^2\le f(x_t)-f(x_{t+1})$ and add it for $t=0,\dots,T-1$. On the right, consecutive terms cancel and only $f(x_0)-f(x_T)$ remains. Since $f(x_T)\ge f_{\text{low}}$, this is at most $f(x_0)-f_{\text{low}}$.

Result: $\tfrac1{2L}\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2\le f(x_0)-f_{\text{low}}$. The only place the lower bound enters is $f(x_T)\ge f_{\text{low}}$; no minimizer is needed.

**Details.**

Telescoping written out: $\sum_{t=0}^{T-1}(f(x_t)-f(x_{t+1}))=(f(x_0)-f(x_1))+(f(x_1)-f(x_2))+\dots+(f(x_{T-1})-f(x_T))=f(x_0)-f(x_T)$.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07).
<!-- END S91 -->

<!-- BEGIN S92 -->
### 22. Proof Step 2: Minimum at Most Average [S92]

**Message.** The smallest of $T$ numbers is at most their average, which turns the summed bound into the theorem.

$\min_{0\le t\le T-1}\|\nabla f(x_t)\|^2\le\tfrac1T\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2\le\tfrac{2L(f(x_0)-f_{\text{low}})}T$, where the second inequality is Step 1 multiplied by $2L/T$.

The guarantee is about the best iterate among the first $T$, not the last one. The proof gives no bound on $\|\nabla f(x_{T-1})\|$ itself beyond what the descent inequality says.

**Details.**

The same argument bounds the average squared gradient, which is a slightly stronger statement than the minimum.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S92 -->

<!-- BEGIN S93 -->
### 23. Stationary Does Not Mean Minimum [S93]

**Message.** Nonconvex gradient descent gets a $1/T$ rate only for the smallest squared gradient, not for reaching a local optimum.

Q: Does nonconvex GD reach a local optimum at rate $1/T$ (asked as "linear convergence to local optimum")? A: No. The $1/T$ rate is for $\min_t\|\nabla f(x_t)\|^2$ only. Under these assumptions there is no guarantee of a local minimum, and the rate $1/T$ is sublinear, not linear.

The figure is four nested boxes. The outer box is the set of $\varepsilon$-stationary points, $\|\nabla f(x)\|\le\varepsilon$: this is what the theorem delivers. Inside it is the set of stationary points, $\nabla f(x)=0$, which also contains local maxima and saddle points. Inside that, in a dashed box, are local minima, which are not guaranteed. Innermost, also dashed, are global minima.

Scope: $L$-smooth, bounded below, step $1/L$, and no further assumptions. The next slide shows a concrete function where gradient descent stays at a maximum.

**Details.**

From Step 1 of the proof, $\sum_{t\ge0}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})$ for every $T$, so the series converges and $\|\nabla f(x_t)\|\to0$. This alone does not imply that the iterates converge. If a subsequence of iterates converges to some $\bar x$, continuity of $\nabla f$ gives $\nabla f(\bar x)=0$: the limit is stationary, but it may be a maximum or a saddle.

Stronger conclusions, such as avoiding saddle points from almost every start, need further assumptions and are outside this lecture.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD" and the following discussion, which says the limit "can even be a local maximum or saddle point", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S93 -->

<!-- BEGIN S136 -->
### 24. GD Can Stay at a Maximum [S136]

**Message.** For $f(x)=1-\cos x$, gradient descent started at $x_0=\pi$ never moves, so the theorem's assumptions do not force a local minimum.

The figure plots $f(x)=1-\cos x$ over a little more than one period. It is a smooth wave: minima (green dots, labelled "min") at $x=0$ and $x=2\pi$ with $f=0$, and a maximum (red dot) at $x=\pi$ with $f=2$, labelled $f'(\pi)=0$ and $f''(\pi)=-1$.

The assumptions hold: $f\ge0$, so $f_{\text{low}}=0$, and $f$ is $1$-smooth. With step $1/L=1$ the update is $x_{t+1}=x_t-\sin x_t$. Since $\sin\pi=0$, starting at $x_0=\pi$ gives $x_t=\pi$ for all $t$: every iterate is a strict local maximum, and the gradient is exactly zero, so the theorem is satisfied.

This is an existence counterexample. It uses an exact start at the maximum; it does not describe what happens from a typical start.

**Details.**

$L=1$: $f'(x)=\sin x$ and $|\sin x-\sin y|\le|x-y|$ by the mean value theorem, because $|\cos|\le1$; and $f''(0)=1$, so no smaller constant works. $f''(\pi)=\cos\pi=-1\lt0$, so $\pi$ is a strict local maximum; $f(\pi)=2$ is in fact the global maximum.

The theorem's bound here reads $\min_t|f'(x_t)|^2=0\le2\cdot1\cdot(2-0)/T$, true for every $T$.

**Sources.**

Our calculation (illustrative example; evidence E08). Plot: inline SVG drawn from the formula.
<!-- END S136 -->

<!-- BEGIN S137 -->
### 25. The Square Changes the Rate [S137]

**Message.** Taking square roots, the gradient norm itself falls only like $O(1/\sqrt T)$, so tolerance $\varepsilon$ costs on the order of $1/\varepsilon^2$ iterations.

Square-rooting the theorem gives $\min_{0\le t\le T-1}\|\nabla f(x_t)\|\le\sqrt{2L(f(x_0)-f_{\text{low}})/T}=O(1/\sqrt T)$. Solving for $T$: if $T\ge2L(f(x_0)-f_{\text{low}})/\varepsilon^2$, then some $t\le T-1$ has $\|\nabla f(x_t)\|\le\varepsilon$.

So asking for tolerance $\varepsilon/10$ instead of $\varepsilon$ multiplies this iteration bound by $100$. The constants $L$ and $f(x_0)-f_{\text{low}}$ depend on the problem.

Again, this is a best-iterate statement: there is no $O(1/T)$ rate for the gradient norm, and no local-minimum guarantee.

**Details.**

Full constant: $T\ge\lceil2L(f(x_0)-f_{\text{low}})/\varepsilon^2\rceil$ suffices. Arithmetic illustration with the running example's constants $L=4$, $f(x_0)=10$, $f_{\text{low}}=0$: the bound is $80/\varepsilon^2$, e.g. $8000$ for $\varepsilon=0.1$ (our calculation). This is the worst-case guarantee; the running example itself converges much faster.

The source gives the squared-gradient bound; the square root and the iteration count are our derivation from it.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06: $O(\varepsilon^{-2})$ iterations). Square root and $T$ count: our derivation.
<!-- END S137 -->

<!-- REGION P4c END -->

<!-- REGION P4d BEGIN -->

<!-- BEGIN S09 -->
### 26. Part 4: Convex: Optimality [S09]

**Message.** Part 4 adds convexity: the function gap to the optimum shrinks at rate $O(1/T)$.
<!-- END S09 -->

<!-- BEGIN S10 -->
### 27. Definition -- Convex Function [S10]

#### 2.1 Convex sets and convex functions

A set $C\subseteq\mathbb{R}^n$ is **convex** if for all $x,y\in C$ and $t\in[0,1]$ we have $tx+(1-t)y\in C$: the segment joining any two points of $C$ stays in $C$. A function $f:C\to\mathbb{R}$ on a convex domain is **convex** if

$ f\bigl(tx+(1-t)y\bigr)\;\le\;t f(x)+(1-t)f(y)\qquad\text{for all }x,y\in C,\;t\in[0,1]. \tag{2.1} $

This is the **chord** definition: the graph lies below or on every chord. It is **strictly convex** if the inequality is strict for $x\ne y$ and $t\in(0,1)$. Note that (2.1) requires *no* differentiability; it is the definition of record, and every other characterization below is a theorem relative to it.

The domain matters, and the lecture suppresses it. Convexity of $f$ is a statement about a convex domain; $f(x)=1/x$ is convex on $(0,\infty)$ and concave on $(-\infty,0)$, and the union of those two intervals is not convex, so "$1/x$ is convex" is only true once you name the domain. Throughout, when no domain is named, it is $\mathbb{R}^n$.
<!-- END S10 -->

<!-- BEGIN S15 -->
### 28. First-Order Characterization [S15]

#### 2.4 First-order characterization (tangent floor)

The lecture states that for differentiable $f$, convexity is equivalent to the graph lying above every tangent plane, and says it "follows directly from the chord definition." It does, but the argument runs in two directions and only one of them is a one-liner. Here is the full statement and proof.

**Theorem 2.2 (first-order characterization).** Let $f$ be differentiable on $\mathbb{R}^n$. Then $f$ is convex if and only if

$ f(y)\;\ge\;f(x)+\langle\nabla f(x),\,y-x\rangle\qquad\text{for all }x,y. \tag{2.2} $

*Proof, forward direction.* Assume $f$ convex, fix $x,y$, and let $t\in(0,1]$. By (2.1) with the roles arranged so that the increment sits at $x$,

$ f\bigl(x+t(y-x)\bigr)\;=\;f\bigl((1-t)x+ty\bigr)\;\le\;(1-t)f(x)+tf(y). $

Subtract $f(x)$ and divide by $t>0$:

$ \frac{f\bigl(x+t(y-x)\bigr)-f(x)}{t}\;\le\;f(y)-f(x). $

The left side is a difference quotient of the one-dimensional function $t\mapsto f(x+t(y-x))$, whose derivative at $t=0$ is $\langle\nabla f(x),y-x\rangle$ by the chain rule. Letting $t\to0^+$ gives (2.2). The limit exists because $f$ is differentiable; convexity additionally makes the quotient *nondecreasing* in $t$, so the limit is also an infimum, a fact used repeatedly below.

*Proof, converse direction.* Assume (2.2). Fix $x,y$ and $t\in[0,1]$, and set $z=tx+(1-t)y$. Apply (2.2) twice, anchored at $z$:

$ f(x)\;\ge\;f(z)+\langle\nabla f(z),x-z\rangle,\qquad f(y)\;\ge\;f(z)+\langle\nabla f(z),y-z\rangle. $

Multiply the first by $t\ge0$, the second by $1-t\ge0$, and add:

$ tf(x)+(1-t)f(y)\;\ge\;f(z)+\bigl\langle\nabla f(z),\;t x+(1-t)y-z\bigr\rangle\;=\;f(z)+\langle\nabla f(z),0\rangle\;=\;f(z), $

because $tx+(1-t)y=z$ exactly. This is (2.1). **End of proof.**

The "anchor at the intermediate point and add two copies" move in the converse direction is the single most reused trick in this lecture: it reappears in the proof of monotonicity (Theorem 5, Section 5.6 here) and in co-coercivity. It is worth internalizing as a pattern rather than re-deriving it each time.

**Corollary 2.3 (stationary implies global, for convex $f$).** If $f$ is convex and differentiable and $\nabla f(x)=0$, then $x$ is a global minimizer.

*Proof.* Put this $x$ into (2.2): $f(y)\ge f(x)+\langle 0,y-x\rangle=f(x)$ for every $y$. **End of proof.**

This corollary is the formal content of the slogan "for convex functions, stationary is enough." Note how much weaker the proof is than Proposition 2.1's, one substitution, and note that it requires differentiability, which Proposition 2.1 does not.
<!-- END S15 -->

<!-- BEGIN S95 -->
### 29. Assumptions and Goal [S95]
<!-- END S95 -->

<!-- BEGIN S96 -->
### 30. Theorem 8 -- $O(1/T)$ Convergence [S96]

#### 7.1 Theorem 8, proved

**Theorem 8 (Theorem 7.1 in this numbering).** Let $f$ be convex and $L$-smooth with a global minimizer $x^\star$, and run gradient descent with $0<\alpha\le 1/L$. Then for every $T\ge1$,

$ f(x_T)-f^\star\;\le\;\frac{\|x_0-x^\star\|^2}{2\alpha T}. \tag{7.1} $

*Proof.* **Step 1, per-step decrease.** The lid of Lemma 3.1 at $x_i$ with $\delta=-\alpha\nabla f(x_i)$ gives, as in Theorem 6.2(a),

$ f(x_{i+1})\;\le\;f(x_i)-\alpha\Bigl(1-\tfrac{\alpha L}{2}\Bigr)\|\nabla f(x_i)\|^2\;\le\;f(x_i)-\frac{\alpha}{2}\|\nabla f(x_i)\|^2, $

where the last step uses that $\alpha\le1/L$ forces $\alpha L/2\le\tfrac12$ and hence $1-\tfrac{\alpha L}{2}\ge\tfrac12$. This is the only place the restriction $\alpha\le1/L$, rather than $\alpha<2/L$, is used.

**Step 2, bring in the optimum, via convexity.** The tangent floor (2.2) with the pair $(x_i,x^\star)$ reads $f^\star\ge f(x_i)+\langle\nabla f(x_i),x^\star-x_i\rangle$, that is,

$ f(x_i)-f^\star\;\le\;\langle\nabla f(x_i),\,x_i-x^\star\rangle. $

This is the step that fails without convexity; it is what ties the value gap to a quantity the algorithm can control.

**Step 3, combine and complete the square.** Chaining Steps 1 and 2,

$ f(x_{i+1})-f^\star\;\le\;\langle\nabla f(x_i),x_i-x^\star\rangle-\frac{\alpha}{2}\|\nabla f(x_i)\|^2. $

Now recognize the right-hand side as a telescoping difference. Writing $g_i=\nabla f(x_i)$, expanding $\|x_i-x^\star-\alpha g_i\|^2=\|x_i-x^\star\|^2-2\alpha\langle g_i,x_i-x^\star\rangle+\alpha^2\|g_i\|^2$ and using $x_{i+1}-x^\star=x_i-x^\star-\alpha g_i$,

$ \frac{1}{2\alpha}\Bigl(\|x_i-x^\star\|^2-\|x_{i+1}-x^\star\|^2\Bigr)\;=\;\langle g_i,x_i-x^\star\rangle-\frac{\alpha}{2}\|g_i\|^2. $

The two sides of the previous display therefore match exactly:

$ f(x_{i+1})-f^\star\;\le\;\frac{1}{2\alpha}\Bigl(\|x_i-x^\star\|^2-\|x_{i+1}-x^\star\|^2\Bigr). \tag{7.2} $

**Step 4, telescope.** Sum (7.2) for $i=0,\dots,T-1$; the right side collapses:

$ \sum_{i=1}^{T}\bigl(f(x_i)-f^\star\bigr)\;\le\;\frac{1}{2\alpha}\Bigl(\|x_0-x^\star\|^2-\|x_T-x^\star\|^2\Bigr)\;\le\;\frac{\|x_0-x^\star\|^2}{2\alpha}. $

**Step 5, use monotonicity of the values.** By Step 1 the sequence $f(x_i)$ is nonincreasing, so $f(x_T)-f^\star\le f(x_i)-f^\star$ for every $i\le T$, hence $T\bigl(f(x_T)-f^\star\bigr)\le\sum_{i=1}^{T}(f(x_i)-f^\star)$. Divide by $T$. **End of proof.**
<!-- END S96 -->

<!-- BEGIN S97 -->
### 31. Proof Overview [S97]
<!-- END S97 -->

<!-- BEGIN S98 -->
### 32. Step 1 -- Guaranteed Decrease [S98]
<!-- END S98 -->

<!-- BEGIN S99 -->
### 33. Step 2 -- Bring In the Optimum [S99]
<!-- END S99 -->

<!-- BEGIN S101 -->
### 34. Step 3 -- the Distance Identity [S101]
<!-- END S101 -->

<!-- BEGIN S104 -->
### 35. Step 4 -- Telescope [S104]
<!-- END S104 -->

<!-- BEGIN S105 -->
### 36. Step 5 -- From Sum to Last Iterate [S105]

Step 5 is worth pausing on. The telescoping in Step 4 naturally bounds the *sum*, which controls the *average* or the *best* iterate; getting the bound for the *last* iterate $x_T$ requires the monotonicity from Step 1. In stochastic gradient descent, where per-step monotonicity fails, this is exactly why guarantees are stated for the averaged iterate $\bar x_T=\tfrac1T\sum x_i$, a point the next lecture returns to.
<!-- END S105 -->

<!-- BEGIN S106 -->
### 37. Proof Summary -- the Skeleton [S106]
<!-- END S106 -->

<!-- REGION P4d END -->

<!-- REGION P4e BEGIN -->

<!-- BEGIN S63 -->
### 38. Part 5: Strongly Convex: Geometric Decay [S63]

**Message.** Part 5 adds strong convexity: the distance to the minimizer shrinks by a fixed factor every step.
<!-- END S63 -->

<!-- BEGIN S64 -->
### 39. Definition -- $\mu$-Strongly Convex [S64]

#### 5.1 Definition and equivalent forms

$f$ is **$\mu$-strongly convex** (with $\mu>0$) if

$ f(y)\;\ge\;f(x)+\langle\nabla f(x),\,y-x\rangle+\frac{\mu}{2}\|y-x\|^2\qquad\text{for all }x,y. \tag{5.1} $

Compare the tangent floor (2.2): convexity puts the graph above the tangent *plane*; strong convexity puts it above a tangent *paraboloid* of curvature $\mu$. Equivalently, and this is the formulation that makes several proofs trivial, $f$ is $\mu$-strongly convex if and only if

$ h(x)\;:=\;f(x)-\tfrac{\mu}{2}\|x\|^2\quad\text{is convex.} \tag{5.2} $

*Proof that (5.1) and (5.2) are equivalent.* We have $\nabla h(x)=\nabla f(x)-\mu x$. Apply the first-order characterization (Theorem 2.2) to $h$: $h$ is convex if and only if $h(y)\ge h(x)+\langle\nabla f(x)-\mu x,\,y-x\rangle$ for all $x,y$, that is,

$ f(y)-\tfrac\mu2\|y\|^2\;\ge\;f(x)-\tfrac\mu2\|x\|^2+\langle\nabla f(x),y-x\rangle-\mu\langle x,y-x\rangle. $

Collect the quadratic terms: $-\tfrac\mu2\|y\|^2+\tfrac\mu2\|x\|^2+\mu\langle x,y-x\rangle=-\tfrac\mu2\bigl(\|y\|^2-2\langle x,y\rangle+\|x\|^2\bigr)=-\tfrac\mu2\|y-x\|^2$, and moving it across gives exactly (5.1). **End of proof.**

Strong convexity is a strictly stronger condition than strict convexity: $f(x)=x^4$ is strictly convex but not $\mu$-strongly convex for any $\mu>0$, since near the origin its curvature vanishes, so no fixed paraboloid fits underneath. It is also stronger than convexity by a quantitative margin, and that margin is precisely what turns the $O(1/T)$ rate into a linear one.
<!-- END S64 -->

<!-- BEGIN S65 -->
### 40. The Two-Parabola Sandwich [S65]

Note also that a $\mu$-strongly convex, $L$-smooth function necessarily has $\mu\le L$: inequality (5.1) and the lid of Lemma 3.1 sandwich the quantity $f(y)-f(x)-\langle\nabla f(x),y-x\rangle$ between $\tfrac\mu2\|y-x\|^2$ and $\tfrac L2\|y-x\|^2$, so $\mu\le L$. The ratio $\kappa=L/\mu\ge1$ is the **condition number** and it governs everything in Section 8.

#### 5.4 What strong convexity buys, geometrically

Under both hypotheses, $f$ is trapped between two paraboloids of curvature $\mu$ and $L$ anchored at every point of its graph. That is a very rigid picture: the function is a quadratic up to a factor $\kappa$ in curvature. Gradient descent is exactly optimal on an isotropic quadratic, where $\kappa=1$ and one step with $\alpha=1/L$ reaches the minimum, and $\kappa$ measures how far a problem is from that ideal. All of the preconditioning, feature-normalization and adaptive-step-size machinery of practical deep learning is, in this language, an attempt to reduce an effective $\kappa$.
<!-- END S65 -->

<!-- BEGIN S116 -->
### 41. Theorem 10 -- Linear Convergence [S116]

#### 8.3 Theorem 10, proved, with the optimal step size

**Theorem 10 (Theorem 8.2 in this numbering).** Let $f$ be $\mu$-strongly convex and $L$-smooth with minimizer $x^\star$, unique by Proposition 5.2, and run gradient descent with $0<\alpha\le\dfrac{2}{\mu+L}$. Then

$ \|x_{i+1}-x^\star\|^2\;\le\;c\,\|x_i-x^\star\|^2,\qquad c\;=\;1-\frac{2\alpha\mu L}{\mu+L}\;\in[0,1), $

hence $\|x_T-x^\star\|^2\le c^T\|x_0-x^\star\|^2$ and the error decays **geometrically**.

*Proof.* **Step 1.** Since $\nabla f(x^\star)=0$, the update can be written relative to $x^\star$: $x_{i+1}-x^\star=(x_i-x^\star)-\alpha\bigl(\nabla f(x_i)-\nabla f(x^\star)\bigr)$. Put $\Delta x=x_i-x^\star$ and $\Delta g=\nabla f(x_i)-\nabla f(x^\star)$.

**Step 2, expand.** $\|x_{i+1}-x^\star\|^2=\|\Delta x\|^2-2\alpha\langle\Delta g,\Delta x\rangle+\alpha^2\|\Delta g\|^2$.

**Step 3, apply Theorem 9.** Since $-2\alpha<0$, substituting the lower bound (8.1) gives an upper bound:

$ \|x_{i+1}-x^\star\|^2\;\le\;\|\Delta x\|^2-\frac{2\alpha}{L+\mu}\|\Delta g\|^2-\frac{2\alpha\mu L}{L+\mu}\|\Delta x\|^2+\alpha^2\|\Delta g\|^2. $

**Step 4, group.** The coefficient of $\|\Delta x\|^2$ is $c=1-\frac{2\alpha\mu L}{\mu+L}$, and the remaining terms collect into a multiple of $\|\Delta g\|^2$:

$ \|x_{i+1}-x^\star\|^2\;\le\;c\,\|\Delta x\|^2\;+\;\alpha\Bigl(\alpha-\frac{2}{L+\mu}\Bigr)\|\Delta g\|^2. $

**Step 5, discard.** The hypothesis $\alpha\le\tfrac{2}{\mu+L}$ makes the bracket $\alpha-\tfrac{2}{L+\mu}$ nonpositive, so the second term is at most $0$ and may be dropped. Iterating the resulting contraction $T$ times gives the stated bound. Finally $c<1$ because $\alpha,\mu,L>0$, and $c\ge0$ because $\alpha\le\tfrac{2}{\mu+L}$ gives $c\ge1-\tfrac{4\mu L}{(\mu+L)^2}=\bigl(\tfrac{L-\mu}{L+\mu}\bigr)^2\ge0$. **End of proof.**

**Optimal step size.** The factor $c$ is decreasing in $\alpha$ on the admissible range, so the best allowed choice is the endpoint

$ \alpha^\star=\frac{2}{\mu+L},\qquad c^\star=1-\frac{4\mu L}{(\mu+L)^2}=\Bigl(\frac{L-\mu}{L+\mu}\Bigr)^2=\Bigl(\frac{\kappa-1}{\kappa+1}\Bigr)^2,\qquad \kappa=\frac{L}{\mu}. $

This is exactly the square of the contraction factor $\rho(\alpha^\star)$ computed independently in Proposition 6.1 for quadratics, as it must be, since Theorem 8.2 measures squared distance. The agreement is a useful check that neither bound is lossy at the optimum: **Theorem 10 is tight, and quadratics are the worst case.**
<!-- END S116 -->

<!-- BEGIN S138 -->
### 42. S138 (new) [S138]
<!-- END S138 -->

<!-- BEGIN S139 -->
### 43. S139 (new) [S139]
<!-- END S139 -->

<!-- BEGIN S122 -->
### 44. Step 4 -- Unroll [S122]
<!-- END S122 -->

<!-- BEGIN S123 -->
### 45. Step 5 -- Function Values Follow [S123]
<!-- END S123 -->

<!-- BEGIN S110 -->
### 46. The Goal -- From $1/T$ to $c^{\,T}$ [S110]
<!-- END S110 -->

<!-- BEGIN S126 -->
### 47. Running Example -- Contraction, Measured [S126]

#### 8.4 The running example, verified, including a tightness bonus

With $\mu=1$, $L=4$ and $\alpha=\tfrac14$: the admissible range is $\alpha\le\tfrac{2}{5}=0.4$, which is satisfied, and

$ c\;=\;1-\frac{2\cdot\tfrac14\cdot1\cdot4}{1+4}\;=\;1-\frac{2}{5}\;=\;0.6. $

Four iterations, each given as: index $i$; the bound $c^i\cdot8$; the actual squared distance $\|x_i-x^\star\|^2$.

- $i=1$; bound $4.8$; actual $2.25$.
- $i=2$; bound $2.88$; actual $1.2656$.
- $i=3$; bound $1.728$; actual $0.7119$.
- $i=4$; bound $1.0368$; actual $0.4004$.

All four bound values reproduce, and the observed per-step ratio from $i\ge1$ is $\bigl(\tfrac34\bigr)^2=0.5625\le0.6$. Checked. It is close to the bound but not equal, because $\alpha=\tfrac14$ is not the optimal step for this problem.

**Bonus the lecture misses.** Rerun at the optimal $\alpha^\star=\tfrac25$. Theorem 10 then predicts $c^\star=\bigl(\tfrac{4-1}{4+1}\bigr)^2=\bigl(\tfrac35\bigr)^2=0.36$. The actual iteration sends $x_1$ to $(1-4\cdot\tfrac25)x_1=-\tfrac35x_1$ and $x_2$ to $(1-\tfrac25)x_2=\tfrac35x_2$, so *both* coordinates contract by exactly $\tfrac35$ in magnitude and the squared distance contracts by exactly $0.36=c^\star$ at every step, from every starting point. So on this example, at the optimal step size, Theorem 10 holds with **equality**: the bound is not merely correct but exact. This is the concrete face of the tightness claim in Section 8.3, and it is a good sanity check that the constant $\tfrac{2\alpha\mu L}{\mu+L}$ has not been derived too generously.
<!-- END S126 -->

<!-- REGION P4e END -->

<!-- REGION P4f BEGIN -->

<!-- BEGIN S130 -->
### 48. Part 6: Three Guarantees [S130]

**Message.** Part 6 compares the three guarantees side by side.
<!-- END S130 -->

<!-- BEGIN S131 -->
### 49. Every Tool, One Line Each [S131]

#### 9.1 Acceleration, and the lower bounds that make it optimal

The most consequential omission. Gradient descent's $O(1/T)$ and $O(\kappa\log\tfrac1\varepsilon)$ are *not* the best a first-order method can do. Nesterov's accelerated gradient method [14] adds one momentum term,

$ y_{i+1}=x_i-\tfrac1L\nabla f(x_i),\qquad x_{i+1}=y_{i+1}+\beta_i\,(y_{i+1}-y_i), $

and attains $f(x_T)-f^\star=O\bigl(L\|x_0-x^\star\|^2/T^2\bigr)$ for smooth convex $f$, and $O\bigl(\exp(-T/\sqrt\kappa)\bigr)$ with $\beta_i=\tfrac{\sqrt\kappa-1}{\sqrt\kappa+1}$ for strongly convex $f$. The improvements are $\kappa\to\sqrt\kappa$ and $1/T\to1/T^2$; for $\kappa=10^4$ that is a hundredfold reduction in iterations, from the same gradient oracle. Nemirovski and Yudin [15] proved matching lower bounds, $\Omega(1/T^2)$ and $\Omega(\exp(-T/\sqrt\kappa))$, for any method whose iterates lie in the span of observed gradients, so acceleration is optimal, not merely better. See [3, Chapter 2] for the standard treatment. Momentum in deep learning is the practical descendant of this idea, though the theory transfers only loosely to the stochastic nonconvex setting.

#### 9.3 Nonsmooth objectives

$L$-smoothness fails for the $\ell_1$ penalty, the hinge loss, and ReLU networks, that is, for much of what one actually optimizes. Two replacements. **Subgradient descent** replaces $\nabla f(x)$ by any element $g$ of the subdifferential $\partial f(x)=\{g:f(y)\ge f(x)+\langle g,y-x\rangle\text{ for all }y\}$; with $G$-Lipschitz $f$ and a decaying step it achieves $O(1/\sqrt T)$, genuinely slower, and no descent lemma is available, so the values are not monotone. **Proximal gradient** handles $f=\ell+r$ with $\ell$ smooth and $r$ simple by iterating $x_{i+1}=\operatorname{prox}_{\alpha r}(x_i-\alpha\nabla \ell(x_i))$, and recovers the full $O(1/T)$ and linear rates; for $r=\lambda\|\cdot\|_1$ the prox is soft-thresholding and the method is ISTA, accelerated to FISTA. Beck [5] is the reference; Rockafellar [2] is the source for subdifferential calculus.

#### 9.4 Constraints

Minimizing over a convex set $C$ replaces the update with **projected gradient descent**, $x_{i+1}=\Pi_C\bigl(x_i-\alpha\nabla f(x_i)\bigr)$. Because $\Pi_C$ is nonexpansive, every proof in Sections 7 and 8 survives essentially verbatim: the projection can only shrink distances to a point of $C$, and $x^\star\in C$. The optimality condition changes from $\nabla f(x^\star)=0$ to the variational inequality $\langle\nabla f(x^\star),y-x^\star\rangle\ge0$ for all $y\in C$. The unconstrained framing of the lecture hides that these are the same theorems. See [1, Chapter 4] and [16].
<!-- END S131 -->

<!-- BEGIN S140 -->
### 50. S140 (new) [S140]
<!-- END S140 -->

<!-- REGION P4f END -->

<!-- REGION Closing BEGIN -->

<!-- BEGIN S134 -->
### 51. Closing: One Update [S134]

**Message.** The update never changes; what we may conclude about it depends only on the assumptions on $f$.

The closing slide repeats the update $x_{t+1} = x_t - \tfrac{1}{L}\nabla f(x_t)$ and opens questions.
<!-- END S134 -->

<!-- REGION Closing END -->

## 10 References

1. S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004. Free PDF: https://web.stanford.edu/~boyd/cvxbook/. Chapter 3 is the standard reference for the convexity-preserving operations of Section 2.3; Chapter 9 for unconstrained descent methods and line search.
2. R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970. The source for subdifferentials, conjugacy, and the nonsmooth theory referenced in Section 9.3.
3. Y. Nesterov, *Lectures on Convex Optimization*, 2nd edition, Springer, 2018. doi:10.1007/978-3-319-91578-4. The canonical treatment of everything in this lecture: smoothness classes, the $O(1/T)$ and linear rates, acceleration, and the lower bounds.
4. S. Bubeck, "Convex Optimization: Algorithms and Complexity," *Foundations and Trends in Machine Learning* 8(3-4), 2015. arXiv:1405.4980, https://arxiv.org/abs/1405.4980. A compact modern account; its Section 3 gives the proofs of Theorems 8 and 10 in essentially the form used here.
5. A. Beck, *First-Order Methods in Optimization*, SIAM, 2017. doi:10.1137/1.9781611974997. Proximal and projected gradient methods (Sections 9.3 and 9.4), with the descent lemma developed in full generality.
6. A.-L. Cauchy, "Methode generale pour la resolution des systemes d'equations simultanees," *Comptes Rendus de l'Academie des Sciences* 25, 536-538, 1847. The two-page note that introduced gradient descent.
7. J.-B. Baillon and G. Haddad, "Quelques proprietes des operateurs angle-bornes et $n$-cycliquement monotones," *Israel Journal of Mathematics* 26, 137-150, 1977. doi:10.1007/BF03007664. The theorem behind the equivalence list of Section 4.4: for convex $f$, Lipschitz gradient and co-coercivity are the same condition.
8. H. Karimi, J. Nutini and M. Schmidt, "Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Lojasiewicz Condition," ECML-PKDD 2016. arXiv:1608.04636, https://arxiv.org/abs/1608.04636. The modern reference for Sections 5.5 and 8.5, including the nonconvex example $x^2+3\sin^2x$ and the comparison of PL with error bounds and quadratic growth.
9. B. T. Polyak, "Gradient methods for the minimisation of functionals," *USSR Computational Mathematics and Mathematical Physics* 3(4), 864-878, 1963. doi:10.1016/0041-5553(63)90382-3. Where inequality (5.4) first appears as a convergence hypothesis.
10. S. Lojasiewicz, "Une propriete topologique des sous-ensembles analytiques reels," in *Les Equations aux Derivees Partielles*, CNRS, 87-89, 1963. The independent, more general gradient inequality, with exponent $\theta$, for analytic functions; PL is the case $\theta=\tfrac12$.
11. J. D. Lee, M. Simchowitz, M. I. Jordan and B. Recht, "Gradient Descent Only Converges to Minimizers," COLT 2016. arXiv:1602.04915, https://arxiv.org/abs/1602.04915. The measure-zero statement quoted in Section 6.4.
12. Y. Carmon, J. C. Duchi, O. Hinder and A. Sidford, "Lower Bounds for Finding Stationary Points I," *Mathematical Programming* 184, 71-120, 2020. arXiv:1710.11606, https://arxiv.org/abs/1710.11606. Shows the $O(\varepsilon^{-2})$ of Corollary 6.3 is optimal for smooth nonconvex problems.
13. Y. Drori and M. Teboulle, "Performance of first-order methods for smooth convex minimization: a novel approach," *Mathematical Programming* 145, 451-482, 2014. arXiv:1206.3209, https://arxiv.org/abs/1206.3209. The exact worst-case constant $L\|x_0-x^\star\|^2/(4T+2)$ quoted in Section 7.3.
14. Y. Nesterov, "A method of solving a convex programming problem with convergence rate $O(1/k^2)$," *Soviet Mathematics Doklady* 27(2), 372-376, 1983. Acceleration (Section 9.1).
15. A. S. Nemirovski and D. B. Yudin, *Problem Complexity and Method Efficiency in Optimization*, Wiley, 1983. The oracle-complexity lower bounds that make acceleration optimal.
16. H. H. Bauschke and P. L. Combettes, *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd edition, Springer, 2017. doi:10.1007/978-3-319-48311-5. Fejer monotonicity (Section 7.4), nonexpansive operators, and the operator-theoretic reading of Section 5.6.
17. L. Bottou, F. E. Curtis and J. Nocedal, "Optimization Methods for Large-Scale Machine Learning," *SIAM Review* 60(2), 223-311, 2018. arXiv:1606.04838, https://arxiv.org/abs/1606.04838. The survey bridging Sections 9.2 and 9.6 with practice.
18. J. Nocedal and S. J. Wright, *Numerical Optimization*, 2nd edition, Springer, 2006. doi:10.1007/978-0-387-40065-5. Line search (Section 9.2), Newton and quasi-Newton methods (Section 9.5).
19. S. Ghadimi and G. Lan, "Stochastic First- and Zeroth-order Methods for Nonconvex Stochastic Programming," *SIAM Journal on Optimization* 23(4), 2341-2368, 2013. arXiv:1309.5549, https://arxiv.org/abs/1309.5549. The stochastic analogue of Corollary 6.3, and the reference point for the next lecture.
20. Companion notes in this series, in the same accessible Markdown edition: `../opt01-svd-lowrank/opt01-svd-lowrank-note.md` (SVD, pseudoinverse, low-rank approximation), `../opt02-regression-erm/opt02-regression-erm-note.md` (least squares, ERM, ridge, where the convex objective $\tfrac12\|A\theta-B\|^2$ optimized here comes from), and `../opt04-sgd/opt04-sgd-note.md` (stochastic gradient descent, the sequel to Section 9.6). The probability half of the course is covered by prob01 through prob09.
