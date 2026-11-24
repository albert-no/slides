# Deep Learning Math 11: Gradient Descent -- Three Guarantees -- Notes

**About this file.** This is the text-only, screen-reader-friendly edition of the Lecture 11 companion note. It has 51 numbered sections, each headed by its number, title and an ID in brackets; the lecture's slide deck `opt02-convexity-gd.html` and the HTML note `opt02-convexity-gd-note.html` use the same section numbers and IDs. Every figure and table is described in words or linearized into lists, and all mathematics is written in LaTeX. Nothing else is needed to read it.

Companion to the slide deck `opt02-convexity-gd.html` (51 slides, 90 minutes). Audience: junior undergraduate AI majors who know gradients, Taylor's first-order approximation and the Euclidean inner product. The lecture is self-contained; it assumes nothing from the regression lecture. Each section opens with a one-sentence message, then explains it, then gives details (derivations, worked numbers, figure provenance) and sources. Cross-references name a section by its number, for example section 9, Running Example: $L = 4$.

**What the lecture does.** One algorithm, gradient descent with the fixed step $1/L$, and three guarantees earned by three assumptions. The update and $L$-smoothness (sections 3-9); one descent inequality, $f(x_{t+1}) \leq f(x_t) - \frac{1}{2L}\|\nabla f(x_t)\|^2$ (sections 10-18); nonconvex $f$ bounded below: a small squared gradient at rate $O(1/T)$, which means approximate stationarity, not a local minimum (sections 19-25); convex $f$ with an attained minimum: function gap $O(1/T)$ (sections 26-37); $\mu$-strongly convex $f$: geometric (linear) decay of the distance and the function gap (sections 38-47); and the three results side by side (sections 48-50).

**Conventions.** $f:\mathbb{R}^n \to \mathbb{R}$ is differentiable and $L$-smooth; $x_{t+1} = x_t - \frac{1}{L}\nabla f(x_t)$. $f_{\text{low}}$ is a lower bound on $f$; when a minimizer $x^*$ exists, $f^* = f(x^*)$. $\mu > 0$ is the strong-convexity constant. $\|\cdot\|$ is the Euclidean norm. The running example is $f(x) = 2x_1^2 + \frac12 x_2^2$ on $\mathbb{R}^2$, with $L = 4$. Results are cited by name, not number.

**Extended edition.** The pre-2026-11 lecture (134 slides, with the Hessian tests, co-coercivity, the Polyak-Lojasiewicz condition, step sizes other than $1/L$ and the full legacy proofs) is archived with the same slide IDs as `../opt03-backup/opt03-convexity-gd-full.html`, with notes `../opt03-backup/opt03-convexity-gd-full-note.html` and `../opt03-backup/opt03-convexity-gd-full-note.md`.

<!-- REGION Opening BEGIN -->

## Opening

<!-- BEGIN S01 -->
### 1. Gradient Descent: Three Guarantees [S01]

**Message.** One algorithm, gradient descent with step $1/L$; three assumptions give three different guarantees.

Lecture 11 of Deep Learning Math (90 minutes). It studies one algorithm, gradient descent with the fixed step $1/L$, and asks what can be guaranteed about it. Smoothness and a lower bound on $f$ give approximate stationarity; adding convexity and an attained minimum gives an $O(1/T)$ function gap; adding strong convexity gives geometric decay of the distance to the minimizer.
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

## Part 1: One Update

<!-- BEGIN S79 -->
### 3. Part 1: One Update [S79]

**Message.** Part 1 fixes the algorithm: gradient descent with step $1/L$, where $L$ bounds how fast the gradient changes.
<!-- END S79 -->

<!-- BEGIN S80 -->
### 4. Goal: Minimize One Differentiable $f$ [S80]

**Message.** The whole lecture studies one problem: minimize a differentiable $f:\mathbb{R}^n\to\mathbb{R}$ using its exact gradient.

The problem is unconstrained: $x$ ranges over all of $\mathbb{R}^n$ and $f$ is differentiable. The algorithm is deterministic: at every step it uses the exact gradient $\nabla f(x)$, with no sampling noise. Stochastic gradients are not part of this lecture.

A schematic one-dimensional example of a nonconvex $f$: as the input increases, $f$ first falls into a local minimum, then rises to a local maximum, then falls again and flattens toward a constant level $f_{\text{low}}$. It approaches that level but never reaches it.

This example fixes two words for the nonconvex part of the lecture. First, $f$ may have several stationary points, and not all of them are minima. Second, a lower bound $f_{\text{low}}$ with $f(x)\ge f_{\text{low}}$ for all $x$ can hold even when no minimizer exists. The nonconvex guarantee later assumes only such a lower bound; the convex results add the assumption that a minimizer $x^\star$ exists.

**Details.**

The schematic curve is $f(u)=1.5/(1+e^{2(u-2)})-0.8\,e^{-(u+1)^2}$ for $u\in[-3,5]$. Numerically, its local minimum is near $u\approx-0.995$ with $f\approx0.696$, and its local maximum is near $u\approx0.645$ with $f\approx1.353$ (our calculation). As $u\to\infty$ both terms tend to $0$ and $f$ stays positive, so the infimum $0$ is not attained; the lower bound is $f_{\text{low}}=0$. The curve is an illustration of the vocabulary, not a function used in any later calculation.

**Sources.**

Problem setup: Cornell CS4787/5777 (Fall 2026), Lecture 5, https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06). Curve: our illustration (formula above, our calculation).
<!-- END S80 -->

<!-- BEGIN S14 -->
### 5. Recall: The Gradient Gives First-Order Change [S14]

**Message.** The gradient gives the first-order change of $f$, which is a statement about small steps only.

The gradient collects the partial derivatives, $\nabla f(x)=(\partial f/\partial x_1(x),\dots,\partial f/\partial x_n(x))\in\mathbb{R}^n$. Differentiability means $f(x+h)=f(x)+\langle\nabla f(x),h\rangle+o(\|h\|)$ as $h\to0$: near $x$, $f$ is its linear model plus an error that is small compared with $\|h\|$.

Taking $h=sv$ and letting $s\to0$ gives the rate of change along a direction $v$: $\langle\nabla f(x),v\rangle$. This is the only fact needed in section 6 to show that a small step against the gradient lowers $f$.

The qualifier matters. The $o(\|h\|)$ term says nothing about a fixed, finite step: it only promises that the error becomes negligible as the step shrinks. To control one real step of an algorithm we need a quantitative bound on the error, which is what $L$-smoothness will provide.

**Details.**

For a unit direction $v$, Cauchy-Schwarz gives $\langle\nabla f(x),v\rangle\ge-\|\nabla f(x)\|$, with equality at $v=-\nabla f(x)/\|\nabla f(x)\|$ when $\nabla f(x)\ne0$. So the negative gradient is the direction of fastest first-order decrease.

**Sources.**

Standard definition of the (Frechet) derivative; recalled, not new material.
<!-- END S14 -->

<!-- BEGIN S82 -->
### 6. Small Steps Against the Gradient Go Downhill [S82]

**Message.** A small enough step against the gradient lowers $f$, but a long step in the same direction can raise it.

Take the parabola $f(u)=u^2$ and a current point $x$ on its right branch, where $f'(x)>0$, so the negative gradient points toward smaller $u$. Consider two steps in that same direction. A short step lands lower on the parabola: $f$ drops. A long step overshoots the bottom and lands high on the other branch: $f$ rises.

So the direction alone does not guarantee progress; the step length matters too. The first-order statement of section 5 only covers small enough steps. How far is safe is decided by how fast the gradient can change, measured by the smoothness constant $L$ defined next.

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

Smoothness says nothing about convexity. The nonconvex curve of section 4, and the function $1-\cos x$ used later, are smooth and not convex. The nonconvex guarantee uses smoothness and boundedness below, but not convexity.

**Details.**

If $f$ is $L$-smooth it is also $L'$-smooth for every $L'\ge L$, so any valid $L$ can be used; the running example in section 9, Running Example: $L = 4$, checks $L=4$ directly from the definition.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Lipschitz continuous gradient assumption (or the L-smoothness assumption)", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06). Example $\tfrac12x^2$: our calculation.
<!-- END S27 -->

<!-- BEGIN S81 -->
### 8. One Fixed Step: $1/L$ [S81]

**Message.** Gradient descent in this lecture uses the single fixed step $1/L$, and the same update appears in all three guarantees.

The algorithm has an input, a loop and an output. Input: the smoothness constant $L$ and any start $x_0\in\mathbb{R}^n$. Loop: for $t=0,1,\dots,T-1$, set $x_{t+1}=x_t-\tfrac1L\nabla f(x_t)$. Output: the iterates $x_0,x_1,\dots,x_T$.

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

## Part 2: One Descent Inequality

<!-- BEGIN S25 -->
### 10. Part 2: One Descent Inequality [S25]

**Message.** Part 2 proves the one inequality that every later guarantee uses: each step lowers $f$ by at least $\frac{1}{2L}\|\nabla f\|^2$.
<!-- END S25 -->

<!-- BEGIN S33 -->
### 11. Smoothness Gives a Quadratic Upper Bound [S33]

**Message.** An $L$-smooth function lies below its linear model plus $\tfrac L2\|y-x\|^2$, for every pair of points.

Lemma (descent lemma). If $f:\mathbb{R}^n\to\mathbb{R}$ is differentiable and $L$-smooth, then for all $x,y\in\mathbb{R}^n$: $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac L2\|y-x\|^2$.

The right side is the linear model of $f$ at $x$ plus a quadratic penalty. Unlike the $o(\|h\|)$ statement of section 5, this is valid for every finite step, which is exactly what is needed to analyze one step of an algorithm.

No convexity is used. The bound is one-sided: it limits how far $f$ can rise above its linear model, not how far it can fall below it.

**Details.**

The proof follows in sections 13 to 15, in three steps: restrict $f$ to the segment from $x$ to $y$, bound the change of the slope along it by smoothness, and integrate.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07 step 1).
<!-- END S33 -->

<!-- BEGIN S34 -->
### 12. The Upper Bound Touches $f$ at $x$ [S34]

**Message.** The quadratic upper bound touches $f$ at $x$ and lies above it everywhere else.

In one variable, compare three graphs: $f$ itself, the upper bound from the lemma built at a point $x$, and the tangent line at $x$. All three meet at $x$. The upper bound stays on or above $f$ everywhere, and $f$ bends upward away from the tangent.

Equality holds at $y=x$: there the penalty $\tfrac L2\|y-x\|^2$ is zero and the linear model equals $f(x)$. Away from $x$ the penalty grows quadratically and keeps the bound above $f$.

**Details.**

The illustration uses $f(u)=u^2$, the point $x=-0.6$ and $L=3$ (our choice). Since $f'(u)=2u$ is $2$-Lipschitz, $f$ is $2$-smooth and hence also $3$-smooth, so $L=3$ is valid. The upper bound minus $f$ equals $\tfrac32(u+0.6)^2-(u+0.6)^2=\tfrac12(u+0.6)^2\ge0$ (our calculation), which is zero only at $u=x$. With $L=2$ the bound would coincide with $f$; $L=3$ was chosen so the two curves differ away from $x$.

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

The iterates, one bullet per step $t$. Each bullet gives the iterate $x_t$, the value $f(x_t)$, and the descent bound $f(x_{t-1})-\tfrac18\|\nabla f(x_{t-1})\|^2$ on that value (here $\tfrac1{2L}=\tfrac18$).

- Step $t=0$: $x_0=(2,2)$, $f=10$, no bound.
- Step $t=1$: $x_1=(0,\tfrac32)$, $f=\tfrac98$, bound $10-\tfrac{68}8=\tfrac32$.
- Step $t=2$: $x_2=(0,\tfrac98)$, $f=\tfrac{81}{128}$, bound $\tfrac98-\tfrac{9/4}8=\tfrac{27}{32}$.

Each actual value sits below its bound, as the descent inequality promises. The bound is not tight here: the example decreases faster than the generic guarantee.

**Details.**

Gradients: $g_0=(8,2)$ with $\|g_0\|^2=68$; $g_1=(0,\tfrac32)$ with $\|g_1\|^2=\tfrac94$. Values: $f(x_0)=2\cdot4+\tfrac12\cdot4=10$; $f(x_1)=\tfrac12\cdot\tfrac94=\tfrac98$; $f(x_2)=\tfrac12\cdot\tfrac{81}{64}=\tfrac{81}{128}$. Checks: $\tfrac98\le\tfrac32$ and $\tfrac{81}{128}\le\tfrac{27}{32}=\tfrac{108}{128}$.

Squared distances to the minimizer $x^\star=0$ are $8$, $\tfrac94$, $\tfrac{81}{64}$. The first step behaves differently from later ones because it zeroes the stiff coordinate; from $t=1$ on only the second coordinate remains, so both the squared distance and $f$ shrink by exactly $(\tfrac34)^2=\tfrac9{16}$ per step, e.g. $\tfrac{81/128}{9/8}=\tfrac9{16}$. These exact ratios belong to this example, not to a general bound. The baseline table with more iterations is in the backup note.

**Sources.**

Our calculation (illustrative example; evidence E09).
<!-- END S84 -->

<!-- REGION P4b END -->

<!-- REGION P4c BEGIN -->

## Part 3: Nonconvex: Stationarity

<!-- BEGIN S135 -->
### 19. Part 3: Nonconvex: Stationarity [S135]

**Message.** Part 3 uses smoothness and boundedness below: the smallest gradient seen shrinks, which certifies approximate stationarity, not a minimum.
<!-- END S135 -->

<!-- BEGIN S89 -->
### 20. Nonconvex Guarantee: Small Squared Gradient [S89]

**Message.** For any $L$-smooth $f$ bounded below, $T$ steps of size $1/L$ make the smallest squared gradient at most $2L(f(x_0)-f_{\text{low}})/T$.

Theorem (nonconvex, step $1/L$). Let $f:\mathbb{R}^n\to\mathbb{R}$ be differentiable and $L$-smooth with $f(x)\ge f_{\text{low}}$ for all $x$. For any $x_0$ and every $T\ge1$, the iterates satisfy $\min_{0\le t\le T-1}\|\nabla f(x_t)\|^2\le 2L(f(x_0)-f_{\text{low}})/T$.

The bound concerns the best of the $T$ squared gradients at $x_0,\dots,x_{T-1}$. It is not a bound on a gap $f(x_t)-f^\star$, and it does not say which iterate is best.

Only a lower bound is assumed: $f_{\text{low}}$ need not be attained, and no minimizer is assumed. Convexity is not assumed either.

**Details.**

Indexing: the source states the bound with $f^*$, step $\alpha$ with $\alpha L\le1$, and a minimum over $t\in\{0,\dots,T\}$, i.e. $\min\|\nabla f(w_t)\|^2\le2(f(w_0)-f^*)/(\alpha T)$. Here we use exactly $T$ gradients indexed $0$ to $T-1$, which is what summing $T$ descent inequalities gives (sections 21 and 22), and replace $f^*$ by any lower bound, which the telescoping proof allows. With $\alpha=1/L$ the constants agree.

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

Four sets are nested, from largest to smallest. The largest is the set of $\varepsilon$-stationary points, $\|\nabla f(x)\|\le\varepsilon$: this is what the theorem delivers. Inside it is the set of stationary points, $\nabla f(x)=0$, which also contains local maxima and saddle points. Inside that are local minima, which are not guaranteed. Innermost are global minima, also not guaranteed.

Scope: $L$-smooth, bounded below, step $1/L$, and no further assumptions. Section 24 gives a concrete function where gradient descent stays at a maximum.

**Details.**

From Step 1 of the proof, $\sum_{t\ge0}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})$ for every $T$, so the series converges and $\|\nabla f(x_t)\|\to0$. This alone does not imply that the iterates converge. If a subsequence of iterates converges to some $\bar x$, continuity of $\nabla f$ gives $\nabla f(\bar x)=0$: the limit is stationary, but it may be a maximum or a saddle.

Stronger conclusions, such as avoiding saddle points from almost every start, need further assumptions and are outside this lecture.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD" and the following discussion, which says the limit "can even be a local maximum or saddle point", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S93 -->

<!-- BEGIN S136 -->
### 24. GD Can Stay at a Maximum [S136]

**Message.** For $f(x)=1-\cos x$, gradient descent started at $x_0=\pi$ never moves, so the theorem's assumptions do not force a local minimum.

Over a little more than one period, $f(x)=1-\cos x$ is a smooth wave: it has minima at $x=0$ and $x=2\pi$, where $f=0$, and a maximum at $x=\pi$, where $f=2$, $f'(\pi)=0$ and $f''(\pi)=-1$.

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

## Part 4: Convex: Optimality

<!-- BEGIN S09 -->
### 26. Part 4: Convex: Optimality [S09]

**Message.** Part 4 adds convexity: the function gap to the optimum shrinks at rate $O(1/T)$.
<!-- END S09 -->

<!-- BEGIN S10 -->
### 27. Convexity Puts Chords Above [S10]

**Message.** A function is convex when its graph lies on or below every chord, and for such a function every local minimum is global.

The definition: $f:\mathbb{R}^n\to\mathbb{R}$ is convex if, for all $x,y\in\mathbb{R}^n$ and all $\theta\in[0,1]$,

$$f\big(\theta x+(1-\theta)y\big)\le\theta f(x)+(1-\theta)f(y).$$

The left side is $f$ at a point of the segment from $y$ to $x$; the right side is the height of the straight chord between $(y,f(y))$ and $(x,f(x))$ at that same point. The weight is called $\theta$ because $t$ counts iterations later in the lecture.

Example: take the parabola $f(u)=u^2$ with $y$ at $u=-1$ and $x$ at $u=3/2$. At the midpoint $\theta=1/2$ (so $u=1/4$) the chord has height $13/8$, while the function value is only $1/16$.

The payoff is the one property the convex part of the lecture needs: a convex function has no bad local minima. The inequality is $\le$, not $\lt$, so flat pieces and many minimizers are allowed; linear functions are convex. This is not strict convexity.

**Details.**

**Local implies global.** Let $x$ be a local minimizer and suppose some $y$ has $f(y)\lt f(x)$. For every $\theta\in(0,1]$, convexity gives $f\big(x+\theta(y-x)\big)\le(1-\theta)f(x)+\theta f(y)\lt f(x)$. Taking $\theta$ small puts these points arbitrarily close to $x$, which contradicts local minimality. So no such $y$ exists.

**Strict convexity** asks for strict inequality whenever $x\ne y$ and $\theta\in(0,1)$; it rules out two distinct minimizers. The lecture never assumes it.

**Figure check.** The chord at $u=1/4$ has height $\tfrac12(1)+\tfrac12(9/4)=13/8$, and $f(1/4)=1/16$. Drawing coordinates, for reproducing the illustration: the map $X=320+130u$, $Y=280-60u^2$ (SVG drawing units) puts these two points at $(352.5,182.5)$ and $(352.5,276.25)$.

The domain matters in general: convexity is a statement on a convex set. Here the domain is always $\mathbb{R}^n$. Convex sets, examples and operations that preserve convexity are in the backup note.

**Sources.**

- S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004, Chapter 3.
- Our calculation. Plot adapted from the earlier version of this deck.
<!-- END S10 -->

<!-- BEGIN S15 -->
### 28. The Tangent Lies Below [S15]

**Message.** For a differentiable convex function, the tangent plane at any point lies below the whole graph.

If $f$ is convex and differentiable, then for all $x,y\in\mathbb{R}^n$

$$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle.$$

One gradient, computed at one point, gives a lower bound on $f$ everywhere. Smoothness gave the opposite side: $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac L2\|y-x\|^2$. So a convex $L$-smooth function sits between its tangent plane and a quadratic above it. Setting $\nabla f(x)=0$ shows that a stationary point of a convex function is a global minimizer.

Example: for the parabola $f(u)=u^2$ at the point $x$ at $u=-1$, the tangent line is $v=-1-2u$. It touches the parabola at $x$ and lies below it everywhere else.

**Details.**

**From the chord definition.** Fix $x,y$ and $\theta\in(0,1]$. Convexity gives $f\big(x+\theta(y-x)\big)\le(1-\theta)f(x)+\theta f(y)$. Subtract $f(x)$ and divide by $\theta\gt0$:

$$\frac{f\big(x+\theta(y-x)\big)-f(x)}{\theta}\le f(y)-f(x).$$

As $\theta\to0^+$ the left side tends to the directional derivative $\langle\nabla f(x),y-x\rangle$, which gives the tangent bound. The converse (tangent bound for all $x,y$ implies convexity) is proved in the backup note.

**Figure check.** $u^2-(-1-2u)=(u+1)^2\ge0$, with equality only at $u=-1$. Drawing coordinates, for reproducing the illustration: with $X=320+130u$, $Y=280-60v$, the tangent runs from $(60,100)$ at $u=-2$ to $(320,340)$ at $u=0$.

**Sources.**

- S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004, Chapter 3.
- Our calculation. Plot adapted from the earlier version of this deck.
<!-- END S15 -->

<!-- BEGIN S95 -->
### 29. Assume an Optimum Exists [S95]

**Message.** The convex rate is measured from a minimizer, so we assume one exists; it does not have to be unique.

From here on, assume some $x^\star\in\arg\min f$ exists and write $f^\star=f(x^\star)$. Two quantities track the iterates: the function gap $\Delta_t=f(x_t)-f^\star\ge0$ and the squared distance $D_t=\|x_t-x^\star\|^2$.

Existence is a real assumption. The function $f(u)=\log(1+e^u)$ is convex and $\tfrac14$-smooth, and its infimum $0$ is never attained, so there is no $x^\star$ and no $D_0$.

Uniqueness is not assumed. If several minimizers exist, every one of them gives a valid bound; the one closest to $x_0$ gives the smallest $D_0$.

Example: $f(u)=\max(|u|-1,0)^2$ is convex and smooth and is minimized on the whole interval $[-1,1]$. Choose the minimizer $x^\star$ at the right end, $u=1$, and an iterate $x_t$ at $u=2.9$. The gap $\Delta_t$ is the height of $f$ at $x_t$ above $f^\star=0$, and the distance $\sqrt{D_t}$ is the length from $u=1$ to $u=2.9$ (values in the details).

**Details.**

**Contrast with the nonconvex part.** There the guarantee used only a lower bound $f\ge f_{\text{low}}$; $f_{\text{low}}$ did not need to be attained or even to equal the infimum. Here the proof measures distance to an actual point $x^\star$, so attainment is needed.

**Example checks.** $\log(1+e^u)\gt0$ tends to $0$ as $u\to-\infty$; its second derivative is $\sigma(u)(1-\sigma(u))\le\tfrac14$ with $\sigma$ the logistic function. For the example $f(u)=\max(|u|-1,0)^2$: it is $g(|u|-1)$ with $g(s)=\max(s,0)^2$ convex and nondecreasing, so $f$ is convex; $f'(u)=2\max(|u|-1,0)\,\mathrm{sign}(u)$ is $2$-Lipschitz. At $u=2.9$: $\Delta_t=1.9^2=3.61$ and $\sqrt{D_t}=1.9$.

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring).

**Sources.**

- Our calculation.
<!-- END S95 -->

<!-- BEGIN S96 -->
### 30. Convex: O(1/T) Function Gap [S96]

**Message.** For a convex $L$-smooth function with a minimizer, gradient descent with step $1/L$ has function gap at most $L\|x_0-x^\star\|^2/(2T)$ after $T$ steps.

Read the statement part by part. Domain: $f:\mathbb{R}^n\to\mathbb{R}$ with the Euclidean norm. Assumptions: $f$ differentiable, convex, $L$-smooth, and a minimizer $x^\star$ exists. Algorithm: $x_{t+1}=x_t-\tfrac1L\nabla f(x_t)$ from any $x_0$. Quantifier: for every $T\ge1$,

$$f(x_T)-f^\star\le\frac{L\|x_0-x^\star\|^2}{2T}.$$

The measured quantity is the function-value gap at the last iterate. The theorem says nothing directly about $\|x_T-x^\star\|$. The rate is sublinear: to reach gap $\varepsilon$ the bound needs $T\ge LD_0/(2\varepsilon)$, that is $O(1/\varepsilon)$ steps.

**Details.**

Sections 31 to 36 prove this theorem. The bound is stated for any minimizer $x^\star$; with several minimizers, use the one nearest $x_0$.

The earlier version of this lecture numbered this result Theorem 8 and proved it with co-coercivity; that proof is in the backup note. The route used now needs only the descent inequality and the tangent bound.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S96 -->

<!-- BEGIN S97 -->
### 31. Proof Plan: Spend Distance [S97]

**Message.** The proof pays for each step's function gap with a drop in squared distance, and the initial distance $D_0$ is the total budget.

Target: $\Delta_T\le LD_0/(2T)$. Five moves get there.

1. Descent: smoothness lowers $f$ by $\tfrac1{2L}\|\nabla f(x_t)\|^2$ each step. 2. Tangent at $x_t$: convexity bounds the gap $\Delta_t$ by an inner product with the gradient. 3. Distance identity: plain algebra of the update turns the two together into $\tfrac L2(D_t-D_{t+1})$. 4. Telescope over $t=0,\dots,T-1$. 5. Last iterate: gaps never increase, so the last one is at most the average.

Steps 1 and 5 use smoothness only; step 2 is the only place convexity enters; steps 3 and 4 are algebra.

**Details.**

No co-coercivity and no Polyak-Lojasiewicz (PL) condition is needed; both appear in other textbook proofs, but this route avoids them. The same five moves, with one extra term, prove the strongly convex rate in the next part.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Our calculation. (arrangement of the steps)
<!-- END S97 -->

<!-- BEGIN S98 -->
### 32. Recall: One-Step Decrease [S98]

**Message.** Smoothness alone gives the one-step decrease $\Delta_{t+1}\le\Delta_t-\tfrac1{2L}\|g_t\|^2$.

Write $g_t=\nabla f(x_t)$. The descent inequality, proved earlier in the lecture for any $L$-smooth $f$ and the step $1/L$, says

$$f(x_{t+1})\le f(x_t)-\frac1{2L}\|g_t\|^2.$$

Subtracting $f^\star$ from both sides rewrites it in terms of gaps. Nothing here uses convexity.

**Details.**

**Re-derivation.** The smoothness upper bound at $x=x_t$, $y=x_{t+1}=x_t-g_t/L$ gives $f(x_{t+1})\le f(x_t)-\tfrac1L\|g_t\|^2+\tfrac L2\cdot\tfrac1{L^2}\|g_t\|^2=f(x_t)-\tfrac1{2L}\|g_t\|^2$.

Two consequences are used later: the gaps are nonincreasing, $\Delta_{t+1}\le\Delta_t$ (section 36), and each step removes at least $\|g_t\|^2/(2L)$ of gap.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S98 -->

<!-- BEGIN S99 -->
### 33. Use the Tangent at x_t [S99]

**Message.** Convexity's tangent bound at $x_t$, evaluated at $x^\star$, bounds the gap by $\langle g_t,x_t-x^\star\rangle$.

Take the tangent bound with $x=x_t$ and $y=x^\star$: $f^\star\ge f(x_t)+\langle g_t,x^\star-x_t\rangle$. Moving terms gives $\Delta_t\le\langle g_t,x_t-x^\star\rangle$.

Put this into the descent step of section 32:

$$\Delta_{t+1}\le\langle g_t,x_t-x^\star\rangle-\frac1{2L}\|g_t\|^2.$$

This is the only use of convexity in the proof, and it is plain convexity, not strong convexity.

**Details.**

By Cauchy-Schwarz the same step gives $\Delta_t\le\|g_t\|\sqrt{D_t}$: a convex function cannot have a large gap where both the gradient and the distance to $x^\star$ are small.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S99 -->

<!-- BEGIN S101 -->
### 34. Expand the Squared Distance [S101]

**Message.** Expanding $\|x_{t+1}-x^\star\|^2$ shows that the right side of the last bound equals $\tfrac L2(D_t-D_{t+1})$, so $\Delta_{t+1}\le\tfrac L2(D_t-D_{t+1})$.

The update gives $x_{t+1}-x^\star=(x_t-x^\star)-\tfrac1Lg_t$. Expanding the square,

$$D_{t+1}=D_t-\frac2L\langle g_t,x_t-x^\star\rangle+\frac1{L^2}\|g_t\|^2.$$

Multiplying by $L/2$ and rearranging gives $\tfrac L2(D_t-D_{t+1})=\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2$, exactly the right side of the tangent-plus-descent bound. Therefore

$$\Delta_{t+1}\le\frac L2\big(D_t-D_{t+1}\big).$$

The gap after step $t$ is paid for by the drop in squared distance during step $t$.

**Details.**

**Index check.** The right side uses $g_t$, $D_t$ and $D_{t+1}$; the left side is the gap at $x_{t+1}$, one index ahead of the gradient.

**A by-product.** Because $\Delta_{t+1}\ge0$, the inequality forces $D_{t+1}\le D_t$: under convexity, the iterates never move away from any minimizer.

**Example.** For $f=2x_1^2+\tfrac12x_2^2$, $x_0=(2,2)$, $x_1=(0,3/2)$: $\Delta_1=9/8$ and $\tfrac L2(D_0-D_1)=2(8-9/4)=23/2$, consistent with the bound.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S101 -->

<!-- BEGIN S104 -->
### 35. Distances Telescope [S104]

**Message.** Summing the per-step bound over $t=0,\dots,T-1$ cancels the middle distances and leaves $\sum_{t=1}^T\Delta_t\le\tfrac L2D_0$.

Write the bound for $t=0,1,\dots,T-1$ and add the $T$ inequalities. The left sides add to $\Delta_1+\dots+\Delta_T$. On the right, each $D_t$ with $1\le t\le T-1$ appears once with a plus sign and once with a minus sign, so

$$\sum_{t=1}^T\Delta_t\le\frac L2\big(D_0-D_T\big)\le\frac L2D_0,$$

where the last step drops $D_T\ge0$.

**Details.**

**Off-by-one check.** There are $T$ inequalities, $T$ gaps $\Delta_1,\dots,\Delta_T$ on the left, and the distance terms run from $D_0$ to $D_T$. The gap $\Delta_0$ never appears.

**Example.** In the running quadratic with $T=2$: $\Delta_1+\Delta_2=9/8+81/128=225/128\approx1.76$, against $\tfrac L2D_0=16$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S104 -->

<!-- BEGIN S105 -->
### 36. The Last Gap Is Smallest [S105]

**Message.** Gaps never increase, so $T$ times the last gap is at most their sum, which proves the theorem.

The descent inequality gives $\Delta_{t+1}\le\Delta_t$, so $\Delta_T$ is the smallest of $\Delta_1,\dots,\Delta_T$. Hence

$$\begin{gathered}T\Delta_T\le\sum_{t=1}^T\Delta_t\le\frac L2D_0,\\
\text{so}\quad f(x_T)-f^\star\le\frac{L\|x_0-x^\star\|^2}{2T}.\end{gathered}$$

Monotonicity comes from the descent inequality, not from convexity. It is what lets the theorem speak about the last iterate.

**Details.**

**Contrast with the nonconvex guarantee.** Under smoothness and a lower bound alone, the guarantee is $\min_{0\le t\lt T}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})/T$: a bound on the smallest gradient among the first $T$ iterates, not on the last iterate and not on a function gap.

Without monotonicity the same sum would bound only the average or the best gap; that is the form stochastic methods usually get.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Cornell CS4787/5777, Fall 2026, Lecture 5 notes, section "Convergence of GD". https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (checked 2026-11-23).
<!-- END S105 -->

<!-- BEGIN S106 -->
### 37. The Convex Proof in One Chain [S106]

**Message.** The whole convex proof is one chain from $T\Delta_T$ to $\tfrac L2D_0$, using only the descent inequality and the tangent bound; the rate is sublinear.

The whole proof as one chain, each step labelled by its reason:

$$\begin{aligned}T\Delta_T&\overset{\text{monotone}}{\le}\sum_{t=0}^{T-1}\Delta_{t+1}\\
&\overset{\substack{\text{descent}\\\text{+ tangent}}}{\le}\sum_{t=0}^{T-1}\Big(\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2\Big)\\
&\overset{\text{identity}}{=}\tfrac L2\sum_{t=0}^{T-1}(D_t-D_{t+1})\\
&\overset{\text{telescope}}{=}\tfrac L2(D_0-D_T)\le\tfrac L2D_0.\end{aligned}$$

$O(1/T)$ is sublinear, not linear: doubling $T$ only halves the bound, and reaching gap $\varepsilon$ takes $O(1/\varepsilon)$ steps.

**Details.**

The proof uses no co-coercivity, no PL condition and no two-sided sandwich of $\nabla f$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S106 -->

<!-- REGION P4d END -->

<!-- REGION P4e BEGIN -->

## Part 5: Strongly Convex: Geometric Decay

<!-- BEGIN S63 -->
### 38. Part 5: Strongly Convex: Geometric Decay [S63]

**Message.** Part 5 adds strong convexity: the distance to the minimizer shrinks by a fixed factor every step.
<!-- END S63 -->

<!-- BEGIN S64 -->
### 39. Add a Quadratic Floor [S64]

**Message.** Strong convexity strengthens the tangent bound by a quadratic bowl $\tfrac\mu2\|y-x\|^2$.

A differentiable $f:\mathbb{R}^n\to\mathbb{R}$ is $\mu$-strongly convex, $\mu\gt0$, if for all $x,y$

$$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\frac\mu2\|y-x\|^2.$$

It is the tangent bound plus a quadratic of curvature $\mu$. If $f$ is also $L$-smooth, then $\mu\le L$, so from here on $0\lt\mu\le L$.

It is stronger than having a unique minimizer: $f(u)=u^4$ has the unique minimizer $0$, yet $u^4\ge\tfrac\mu2u^2$ fails for small $u$ whatever $\mu\gt0$ is. A positive second derivative at one point is not enough either; the bowl must hold at every $x$.

**Details.**

**Why $\mu\le L$.** For $y\ne x$, the remainder $r=f(y)-f(x)-\langle\nabla f(x),y-x\rangle$ satisfies $\tfrac\mu2\|y-x\|^2\le r\le\tfrac L2\|y-x\|^2$, which forces $\mu\le L$.

**Existence.** With $x=0$: $f(y)\ge f(0)+\langle\nabla f(0),y\rangle+\tfrac\mu2\|y\|^2\to\infty$ as $\|y\|\to\infty$. So a sublevel set is bounded and closed, and the continuous $f$ attains its minimum on it.

**Uniqueness.** If $x^\star$ and $y^\star$ are both minimizers, the bound at $x=x^\star$ (where $\nabla f(x^\star)=0$) gives $f(y^\star)\ge f(x^\star)+\tfrac\mu2\|y^\star-x^\star\|^2$, so $y^\star=x^\star$.

Equivalent forms and further examples are in the backup note.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S64 -->

<!-- BEGIN S65 -->
### 40. Curvature Is Bounded Below [S65]

**Message.** Strong convexity and smoothness together trap the remainder above the tangent between $\tfrac\mu2\|y-x\|^2$ and $\tfrac L2\|y-x\|^2$.

Let $r(y)=f(y)-f(x)-\langle\nabla f(x),y-x\rangle$ be the height of $f$ above its tangent at $x$. Then

$$\frac\mu2\|y-x\|^2\le r(y)\le\frac L2\|y-x\|^2.$$

The curvature of $f$ is at least $\mu$ and at most $L$ in every direction.

Example: restrict the running example $f=2x_1^2+\tfrac12x_2^2$ ($\mu=1$, $L=4$) to the diagonal line $x=s(1,1)/\sqrt2$, where it becomes $1.25s^2$. At the anchor $s=-1$, the lower curve is the tangent plus $\tfrac12(s+1)^2$ (curvature $\mu=1$) and the upper curve is the tangent plus $2(s+1)^2$ (curvature $L=4$). All three touch at the anchor; the lower curve stays below $f$ and the upper curve stays above it.

**Details.**

**Example check.** For this quadratic $r=2h_1^2+\tfrac12h_2^2$ with $h=y-x$, and $\tfrac12\|h\|^2\le2h_1^2+\tfrac12h_2^2\le2\|h\|^2$, so $\mu=1$ and $L=4$. Along the diagonal, $f=2\cdot\tfrac{s^2}2+\tfrac12\cdot\tfrac{s^2}2=1.25s^2$, whose curvature $2.5$ lies between $1$ and $4$.

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring). The script asserts lower curve $\le f\le$ upper curve on a fine grid.

**Sources.**

- Our calculation.
<!-- END S65 -->

<!-- BEGIN S116 -->
### 41. Strongly Convex: Geometric Convergence [S116]

**Message.** Under strong convexity and smoothness, gradient descent with step $1/L$ shrinks the squared distance to the minimizer by the factor $q=1-\mu/L$ every step.

Statement: $f:\mathbb{R}^n\to\mathbb{R}$ is $\mu$-strongly convex and $L$-smooth, $0\lt\mu\le L$, with unique minimizer $x^\star$ (it exists and is unique by strong convexity). Gradient descent uses step $1/L$ from any $x_0$. For every $T\ge1$,

$$\|x_T-x^\star\|^2\le\Big(1-\frac\mu L\Big)^T\|x_0-x^\star\|^2.$$

The factor $q=1-\mu/L$ lies in $[0,1)$. If $q=0$, that is $\mu=L$, a single step lands on $x^\star$. To get $D_T\le\varepsilon$ it suffices that $T\ge\tfrac L\mu\ln(D_0/\varepsilon)$.

The step is the same $1/L$ as in every other part of the lecture. Other step sizes give other theorems, not used here.

**Details.**

**The case $\mu=L$.** Then the remainder bounds coincide, $r(y)=\tfrac L2\|y-x\|^2$ exactly, so $f$ is a quadratic with Hessian $LI$ and $x_0-\tfrac1L\nabla f(x_0)$ is its minimizer.

**Iteration count.** $q^T\le e^{-\mu T/L}$ (section 44), and $e^{-\mu T/L}D_0\le\varepsilon$ when $T\ge\tfrac L\mu\ln(D_0/\varepsilon)$.

The earlier version of this lecture stated this as Theorem 10 with step $2/(\mu+L)$ and a co-coercivity proof; see the backup note.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S116 -->

<!-- BEGIN S138 -->
### 42. Keep the Extra Curvature Term [S138]

**Message.** With strong convexity the tangent step carries an extra $-\tfrac\mu2D_t$, and it survives into the per-step bound.

Strong convexity at $x=x_t$, $y=x^\star$ gives $f^\star\ge f(x_t)+\langle g_t,x^\star-x_t\rangle+\tfrac\mu2D_t$, so

$$\Delta_t\le\langle g_t,x_t-x^\star\rangle-\frac\mu2D_t.$$

The descent inequality and the distance identity are unchanged from the convex proof, so

$$\begin{aligned}\Delta_{t+1}&\le\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2-\tfrac\mu2D_t\\
&=\tfrac L2(D_t-D_{t+1})-\tfrac\mu2D_t.\end{aligned}$$

Setting $\mu=0$ gives back the convex step exactly.

**Details.**

No PL condition is used. PL is the inequality $\tfrac12\|\nabla f(x)\|^2\ge\mu(f(x)-f^\star)$, an assumption about gradients rather than a quadratic lower bound; it appears in other proofs of linear rates.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation. (derivation chain)
- H. Karimi, J. Nutini and M. Schmidt, "Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Lojasiewicz Condition," ECML-PKDD 2016, arXiv:1608.04636.
<!-- END S138 -->

<!-- BEGIN S139 -->
### 43. Nonnegative Gap Forces Contraction [S139]

**Message.** Because the next gap is nonnegative, the per-step bound forces $D_{t+1}\le(1-\mu/L)D_t$.

Since $x^\star$ minimizes $f$, $\Delta_{t+1}\ge0$, so the per-step bound of section 42 gives

$$0\le\frac L2(D_t-D_{t+1})-\frac\mu2D_t.$$

Multiply by $2/L$: $0\le D_t-D_{t+1}-\tfrac\mu LD_t$, that is $D_{t+1}\le(1-\tfrac\mu L)D_t=qD_t$. Every step shrinks the squared distance by at least the factor $q$.

**Details.**

The argument throws away the gap $\Delta_{t+1}$ and keeps only distances; that is one reason the bound can be loose (section 47).

**Example.** In the running quadratic, $D_1/D_0=(9/4)/8=9/32\le3/4$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S139 -->

<!-- BEGIN S122 -->
### 44. Repeat the Same Contraction [S122]

**Message.** Applying the one-step contraction $T$ times gives $D_T\le q^TD_0$.

Chain the contraction: $D_T\le qD_{T-1}\le q^2D_{T-2}\le\dots\le q^TD_0$.

The statement is for $T\ge1$, which also covers $q=0$: then $D_1=0$, so $x_1=x^\star$ and all later iterates stay there, with no $0^0$ to interpret.

Since $1-u\le e^{-u}$ for every real $u$, $q^T\le e^{-\mu T/L}$: the error falls by a constant factor every step.

**Details.**

**Induction.** Base case $T=1$ is the contraction of section 43 at $t=0$. If $D_T\le q^TD_0$, then $D_{T+1}\le qD_T\le q^{T+1}D_0$; multiplying the inequality by $q$ is allowed because $q\ge0$, which holds since $\mu\le L$.

**The exponential bound.** $u\mapsto e^{-u}$ is convex with tangent $1-u$ at $u=0$, so the tangent bound gives $e^{-u}\ge1-u$. With $u=\mu/L$ and $q\ge0$, raising to the power $T$ gives $q^T\le e^{-\mu T/L}$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S122 -->

<!-- BEGIN S123 -->
### 45. Function Values Follow Distance [S123]

**Message.** Smoothness at the minimizer converts the distance bound into the function-gap bound $\Delta_T\le\tfrac L2q^TD_0$.

Use the smoothness upper bound at $x=x^\star$, where $\nabla f(x^\star)=0$, with $y=x_T$: $f(x_T)\le f^\star+\tfrac L2\|x_T-x^\star\|^2$. With the distance bound of section 44,

$$\begin{aligned}f(x_T)-f^\star&\le\frac L2\|x_T-x^\star\|^2\\
&\le\frac L2q^T\|x_0-x^\star\|^2.\end{aligned}$$

Both the iterates and the function values converge to the optimum, the unique minimizer. This is much more than the nonconvex conclusion, which only finds a point with small gradient.

**Details.**

The prefactor is $\tfrac L2D_0$. A bound of the form $\Delta_T\le q^T\Delta_0$ would need a separate function-gap contraction argument, which this lecture does not prove.

**Example.** In the running quadratic, $\Delta_2=81/128\approx0.63$ against $\tfrac L2q^2D_0=2\cdot\tfrac9{16}\cdot8=9$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
<!-- END S123 -->

<!-- BEGIN S110 -->
### 46. Linear Means Geometric [S110]

**Message.** In optimization, linear convergence means the error shrinks geometrically, like $q^T$; the convex $O(1/T)$ rate is sublinear.

A rate is called linear when the error after $T$ steps is at most $Cq^T$ with $q\lt1$. The name comes from the log scale: $\log(Cq^T)=\log C+T\log q$ is a straight line in $T$. Geometric and exponential mean the same thing here.

A rate like $1/T$ is sublinear: on a log scale its curve flattens out. The convex rate $O(1/T)$ is sublinear, not linear; the strongly convex rate is linear.

Compare the two bound shapes $1/T$ and $(3/4)^T$ for $T=1,\dots,24$ on a logarithmic scale, where $3/4$ is $q$ for the running example. On that scale $(3/4)^T$ is a straight line, falling to about $10^{-3}$ at $T=24$, while $1/T$ flattens near $0.04$. For $T=2$ to $6$, $(3/4)^T$ is slightly larger; from $T=7$ on it is smaller and the gap widens.

These are bounds, not measured run times. Each iteration is the same gradient step in both settings.

**Details.**

**Error versus iteration count.** These are two readings of one bound. Error after $T$ steps: $q^T$ against $1/T$. Steps needed for error $\varepsilon$: $O(\log(1/\varepsilon))$ against $O(1/\varepsilon)$. Keep them apart: a linear rate is an error statement, and $\log(1/\varepsilon)$ is the matching iteration count.

**Numbers.** $(3/4)^{24}=e^{24\ln0.75}\approx e^{-6.90}\approx1.0\times10^{-3}$; $1/24\approx0.042$. Crossing: $(3/4)^6\approx0.178\gt1/6$, $(3/4)^7\approx0.133\lt1/7\approx0.143$.

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring).

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3 (Remark 3.7 on the terminology)
- Our calculation.
<!-- END S110 -->

<!-- BEGIN S126 -->
### 47. The Example Beats Its Bound [S126]

**Message.** On $f=2x_1^2+\tfrac12x_2^2$, the iterates beat the guarantee: after the first step the squared distance falls by $9/16$ per step, below the bound factor $q=3/4$.

Here $\nabla f=(4x_1,x_2)$, $L=4$, $\mu=1$, $q=3/4$, and the step $1/4$ maps $(x_1,x_2)$ to $(0,\tfrac34x_2)$. From $x_0=(2,2)$:

The iterates, one bullet per step $t$. Each bullet gives the iterate $x_t$, the squared distance $D_t$, and the ratio $D_t/D_{t-1}$ to the previous step.

- $t=0$: $x_0=(2,2)$, $D_0=8$.
- $t=1$: $x_1=(0,3/2)$, $D_1=9/4$, ratio $9/32$.
- $t=2$: $x_2=(0,9/8)$, $D_2=81/64$, ratio $9/16$.

The bound $q^tD_0$ gives $8$, $6$, $9/2$.

The first step is special: it zeroes the steep first coordinate at once. After that only the second coordinate is left; its distance shrinks by $3/4$ per step, so the squared distance shrinks by $(3/4)^2=9/16$.

The guarantee is a worst case over all such functions; one example can do better.

**Details.**

**Function values.** $f(x_0)=10$, $f(x_1)=9/8$, $f(x_2)=81/128$; later ratios are also $9/16$. The strongly convex bound $\tfrac L2q^tD_0=16(3/4)^t$ gives $12$ and $9$ at $t=1,2$; the convex bound $LD_0/(2T)=16/T$ gives $16$ and $8$.

**Distance versus squared distance.** The theorem bounds the squared distance by $q^t$, which corresponds to $\sqrt q$ per step for the distance. In this example the distance itself shrinks by $3/4=q$, so the squared distance shrinks by $q^2$: the bound is loose by a square here.

**Sources.**

- Our calculation.
<!-- END S126 -->

<!-- REGION P4e END -->

<!-- REGION P4f BEGIN -->

## Part 6: Three Guarantees

<!-- BEGIN S130 -->
### 48. Part 6: Three Guarantees [S130]

**Message.** Part 6 compares the three guarantees side by side.
<!-- END S130 -->

<!-- BEGIN S131 -->
### 49. Three Assumptions, Three Guarantees [S131]

**Message.** One algorithm, three assumption levels, three guarantees: a small gradient, then an $O(1/T)$ function gap, then geometric convergence to the minimizer.

All three guarantees use gradient descent with step $1/L$ on an $L$-smooth $f:\mathbb{R}^n\to\mathbb{R}$. One bullet per assumption level; each bullet gives the assumption, the guarantee and what it measures.

- Nonconvex, with $f\ge f_{\text{low}}$: $\min_{t\lt T}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})/T$. This is stationarity only. It does not promise a local minimum: $f(u)=1-\cos u$ is $1$-smooth, and gradient descent started at $u=\pi$, a strict local maximum, never moves.
- Convex, with a minimizer: $\Delta_T\le LD_0/(2T)$, a sublinear rate on the last function gap.
- $\mu$-strongly convex: $D_T\le q^TD_0$ and $\Delta_T\le\tfrac L2q^TD_0$ with $q=1-\mu/L$, a linear, that is geometric, rate.

This is the lecture's one global recap; each guarantee measures a different quantity, so compare what is guaranteed, not only the speed.

**Details.**

**Example check.** For $1-\cos u$: $f'(u)=\sin u$ is $1$-Lipschitz, $f'(\pi)=0$, $f''(\pi)=-1$.

Constants and alternative step sizes are deliberately left out of this summary.

**Sources.**

- Cornell CS4787/5777, Fall 2026, Lecture 5 notes, section "Convergence of GD". https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (checked 2026-11-23).
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
<!-- END S131 -->

<!-- BEGIN S140 -->
### 50. No Extra Conditions Needed [S140]

**Message.** The convex and strongly convex proofs need only the descent inequality, one distance identity and the tangent bound with its $\mu$ term: no co-coercivity and no PL condition.

The proof route: descent inequality, then the distance identity, then the tangent bound with $-\tfrac\mu2D_t$. With $\mu=0$ the result telescopes to $O(1/T)$; with $\mu\gt0$ it contracts by $q$ each step.

Which extra conditions are needed:

- Co-coercivity of $\nabla f$: not needed.
- Polyak-Lojasiewicz (PL) condition: not needed.
- Strong convexity: kept, because it supplies the $\mu$ term that produces the contraction.

Co-coercivity and PL are useful tools in other proofs and other settings. They are not prerequisites for the results in this lecture.

**Details.**

The earlier version of this lecture proved the convex rate through co-coercivity and listed PL among the conditions; that material is in the backup note.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- H. Karimi, J. Nutini and M. Schmidt, "Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Lojasiewicz Condition," ECML-PKDD 2016, arXiv:1608.04636.
<!-- END S140 -->

<!-- REGION P4f END -->

<!-- REGION Closing BEGIN -->

## Closing

<!-- BEGIN S134 -->
### 51. Closing: One Update [S134]

**Message.** The update never changes; what we may conclude about it depends only on the assumptions on $f$.

The update is the same throughout the lecture: $x_{t+1} = x_t - \tfrac{1}{L}\nabla f(x_t)$.
<!-- END S134 -->

<!-- REGION Closing END -->

## References

Section numbers and the theorem, corollary and lemma numbers in the annotations below (Theorems 8 and 10, Corollary 6.3) refer to the extended edition's note, `../opt03-backup/opt03-convexity-gd-full-note.md`.

1. S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004. Free PDF: https://web.stanford.edu/~boyd/cvxbook/. Chapter 3 is the standard reference for the convexity-preserving operations of Section 2.3; Chapter 9 for unconstrained descent methods and line search.
2. R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970. https://press.princeton.edu/books/paperback/9780691015866/convex-analysis. The source for subdifferentials, conjugacy, and the nonsmooth theory referenced in Section 9.3.
3. Y. Nesterov, *Lectures on Convex Optimization*, 2nd edition, Springer, 2018. doi:10.1007/978-3-319-91578-4, https://link.springer.com/book/10.1007/978-3-319-91578-4. The canonical treatment of everything in this lecture: smoothness classes, the $O(1/T)$ and linear rates, acceleration, and the lower bounds.
4. S. Bubeck, "Convex Optimization: Algorithms and Complexity," *Foundations and Trends in Machine Learning* 8(3-4), 2015. arXiv:1405.4980, https://arxiv.org/abs/1405.4980. A compact modern account; its Section 3 gives the proofs of Theorems 8 and 10 in essentially the form used here.
5. A. Beck, *First-Order Methods in Optimization*, SIAM, 2017. doi:10.1137/1.9781611974997, https://epubs.siam.org/doi/book/10.1137/1.9781611974997. Proximal and projected gradient methods (Sections 9.3 and 9.4), with the descent lemma developed in full generality.
6. A.-L. Cauchy, "Methode generale pour la resolution des systemes d'equations simultanees," *Comptes Rendus de l'Academie des Sciences* 25, 536-538, 1847. Original (PDF): https://www.academie-sciences.fr/pdf/dossiers/Cauchy/Cauchy_pdf/CR1847_t25_p536.pdf. The two-page note that introduced gradient descent.
7. J.-B. Baillon and G. Haddad, "Quelques proprietes des operateurs angle-bornes et $n$-cycliquement monotones," *Israel Journal of Mathematics* 26, 137-150, 1977. doi:10.1007/BF03007664, https://doi.org/10.1007/BF03007664. The theorem behind the equivalence list of Section 4.4: for convex $f$, Lipschitz gradient and co-coercivity are the same condition.
8. H. Karimi, J. Nutini and M. Schmidt, "Linear Convergence of Gradient and Proximal-Gradient Methods Under the Polyak-Lojasiewicz Condition," ECML-PKDD 2016. arXiv:1608.04636, https://arxiv.org/abs/1608.04636. The modern reference for Sections 5.5 and 8.5, including the nonconvex example $x^2+3\sin^2x$ and the comparison of PL with error bounds and quadratic growth.
9. B. T. Polyak, "Gradient methods for the minimisation of functionals," *USSR Computational Mathematics and Mathematical Physics* 3(4), 864-878, 1963. doi:10.1016/0041-5553(63)90382-3, https://doi.org/10.1016/0041-5553(63)90382-3. Where inequality (5.4) first appears as a convergence hypothesis.
10. S. Lojasiewicz, "Une propriete topologique des sous-ensembles analytiques reels," in *Les Equations aux Derivees Partielles*, CNRS, 87-89, 1963. The independent, more general gradient inequality, with exponent $\theta$, for analytic functions; PL is the case $\theta=\tfrac12$.
11. J. D. Lee, M. Simchowitz, M. I. Jordan and B. Recht, "Gradient Descent Only Converges to Minimizers," COLT 2016. arXiv:1602.04915, https://arxiv.org/abs/1602.04915. The measure-zero statement quoted in Section 6.4.
12. Y. Carmon, J. C. Duchi, O. Hinder and A. Sidford, "Lower Bounds for Finding Stationary Points I," *Mathematical Programming* 184, 71-120, 2020. arXiv:1710.11606, https://arxiv.org/abs/1710.11606. Shows the $O(\varepsilon^{-2})$ of Corollary 6.3 is optimal for smooth nonconvex problems.
13. Y. Drori and M. Teboulle, "Performance of first-order methods for smooth convex minimization: a novel approach," *Mathematical Programming* 145, 451-482, 2014. arXiv:1206.3209, https://arxiv.org/abs/1206.3209. The exact worst-case constant $L\|x_0-x^\star\|^2/(4T+2)$ quoted in Section 7.3.
14. Y. Nesterov, "A method of solving a convex programming problem with convergence rate $O(1/k^2)$," *Soviet Mathematics Doklady* 27(2), 372-376, 1983. https://www.mathnet.ru/eng/dan46009. Acceleration (Section 9.1).
15. A. S. Nemirovski and D. B. Yudin, *Problem Complexity and Method Efficiency in Optimization*, Wiley, 1983. The oracle-complexity lower bounds that make acceleration optimal.
16. H. H. Bauschke and P. L. Combettes, *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd edition, Springer, 2017. doi:10.1007/978-3-319-48311-5, https://link.springer.com/book/10.1007/978-3-319-48311-5. Fejer monotonicity (Section 7.4), nonexpansive operators, and the operator-theoretic reading of Section 5.6.
17. L. Bottou, F. E. Curtis and J. Nocedal, "Optimization Methods for Large-Scale Machine Learning," *SIAM Review* 60(2), 223-311, 2018. arXiv:1606.04838, https://arxiv.org/abs/1606.04838. The survey bridging Sections 9.2 and 9.6 with practice.
18. J. Nocedal and S. J. Wright, *Numerical Optimization*, 2nd edition, Springer, 2006. doi:10.1007/978-0-387-40065-5, https://doi.org/10.1007/978-0-387-40065-5. Line search (Section 9.2), Newton and quasi-Newton methods (Section 9.5).
19. S. Ghadimi and G. Lan, "Stochastic First- and Zeroth-order Methods for Nonconvex Stochastic Programming," *SIAM Journal on Optimization* 23(4), 2341-2368, 2013. arXiv:1309.5549, https://arxiv.org/abs/1309.5549. The stochastic analogue of Corollary 6.3, and the reference point for the next lecture.
20. Companion notes in this series, in the same accessible Markdown edition: `../opt01-svd-lowrank/opt01-svd-lowrank-note.md` (SVD and best low-rank approximation). The regression and SGD notes are extended material in `../opt03-backup/`, listed in `../opt03-backup/OUTLINE.md`. The probability half of the course is covered by prob01 through prob09.
