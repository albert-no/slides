# Deep Learning Math 11: Gradient Descent -- Three Guarantees -- Notes

**About this file.** This is the text-only, screen-reader-friendly edition of the Lecture 11 companion note. It has 48 numbered sections, each headed by its number, title and an ID in brackets; the lecture's slide deck `opt02-convexity-gd.html` and the HTML note `opt02-convexity-gd-note.html` use the same section numbers and IDs. Every figure and table is described in words or linearized into lists, and all mathematics is written in LaTeX. Nothing else is needed to read it.

Companion to the slide deck `opt02-convexity-gd.html` (48 slides, 90 minutes). Audience: junior undergraduate AI majors who know gradients, Taylor's first-order approximation and the Euclidean inner product. The lecture is self-contained; it assumes nothing from the regression lecture. Each section opens with a one-sentence message, then explains it, then gives details (derivations, worked numbers, figure provenance) and sources. Cross-references name a section by its number, for example section 10, Smoothness Gives a Quadratic Upper Bound.

**What the lecture does.** One algorithm, gradient descent with the fixed step $1/L$, and three guarantees earned by three assumptions. The update and $L$-smoothness (sections 3-8); one descent inequality, $f(x_{t+1}) \leq f(x_t) - \frac{1}{2L}\|\nabla f(x_t)\|^2$, read as minimizing a quadratic upper model (sections 9-16); nonconvex $f$ bounded below: every gradient norm tends to zero and the smallest squared gradient is $O(1/T)$, which means approximate stationarity, not a local minimum (sections 17-23); convex $f$ with an attained minimum: function gap $O(1/T)$ (sections 24-35); $\mu$-strongly convex $f$: geometric (linear) decay of the distance and the function gap (sections 36-44); and the three results side by side (sections 45-47).

**Conventions.** $f:\mathbb{R}^n \to \mathbb{R}$ is differentiable and $L$-smooth; $x_{t+1} = x_t - \frac{1}{L}\nabla f(x_t)$. $f_{\text{low}}$ is a lower bound on $f$; when a minimizer $x^*$ exists, $f^* = f(x^*)$. $\mu > 0$ is the strong-convexity constant. $\|\cdot\|$ is the Euclidean norm. Results are cited by name, not number.

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
2. One Descent Inequality: An upper model and one square.
3. Nonconvex: Stationarity: Gradients vanish, minima not promised.
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

Smoothness says nothing about convexity. The nonconvex curve of section 4 is smooth and not convex. The nonconvex guarantee uses smoothness and boundedness below, but not convexity.

**Details.**

If $f$ is $L$-smooth it is also $L'$-smooth for every $L'\ge L$, so any valid $L$ can be used.

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

<!-- REGION P4a END -->

<!-- REGION P4b BEGIN -->

## Part 2: One Descent Inequality

<!-- BEGIN S25 -->
### 9. Part 2: One Descent Inequality [S25]

**Message.** Part 2 proves the one inequality that every later guarantee uses: each step lowers $f$ by at least $\frac{1}{2L}\|\nabla f\|^2$.
<!-- END S25 -->

<!-- BEGIN S33 -->
### 10. Smoothness Gives a Quadratic Upper Bound [S33]

**Message.** An $L$-smooth function lies below its linear model plus $\tfrac L2\|y-x\|^2$, for every pair of points; this standard lemma is the tool every later step uses.

Lemma (descent lemma). If $f:\mathbb{R}^n\to\mathbb{R}$ is differentiable and $L$-smooth, then for all $x,y\in\mathbb{R}^n$: $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac L2\|y-x\|^2$.

**Meaning.** The right side is the linear model of $f$ at $x$ plus a quadratic penalty. As a function of $y$ it is a round bowl that touches $f$ at $x$ with the same slope, and $f$ never rises above it. The bowl's curvature is $L$, the largest rate at which smoothness lets the gradient change.

**Role.** Unlike the $o(\|h\|)$ statement of section 5, the bound holds for every finite step, which is what is needed to analyze one step of an algorithm. Every later guarantee uses it only through the one-step decrease of section 16.

No convexity is used. The bound is one-sided: it limits how far $f$ can rise above its linear model, not how far it can fall below it.

This is a standard lemma, used here as a tool. The three pictures that follow illustrate it on one function; they do not prove it. A proof is given below as optional reading; nothing later depends on it.

**Details.**

**Optional formal derivation.** Not needed for the rest of the lecture. Fix $x,y$, set $h=y-x$ and $\rho(s)=f(x+sh)$ for $s\in[0,1]$, so $\rho(0)=f(x)$ and $\rho(1)=f(y)$. Here $s$ marks a point on the segment; it is not the iteration index $t$.

Step 1. By the chain rule $\rho'(s)=\langle\nabla f(x+sh),h\rangle$. This is continuous in $s$, because $\nabla f$ is Lipschitz and hence continuous. The fundamental theorem of calculus gives $f(y)-f(x)=\int_0^1\rho'(s)\,ds$.

Step 2. The slope drifts by at most $Ls\|h\|^2$: $\rho'(s)-\rho'(0)=\langle\nabla f(x+sh)-\nabla f(x),h\rangle\le\|\nabla f(x+sh)-\nabla f(x)\|\,\|h\|\le Ls\|h\|^2$, by Cauchy-Schwarz and then smoothness, since the two points are $\|sh\|=s\|h\|$ apart.

Step 3. Integrate: $f(y)=f(x)+\int_0^1\rho'(s)\,ds\le f(x)+\int_0^1(\rho'(0)+Ls\|h\|^2)\,ds=f(x)+\langle\nabla f(x),h\rangle+\tfrac L2\|h\|^2$, because $\rho'(0)=\langle\nabla f(x),h\rangle$ does not depend on $s$ and $\int_0^1Ls\,ds=\tfrac L2$. The $\tfrac12$ is the average of $s$ over the segment.

The derivation uses only differentiability and the Lipschitz gradient: no Hessian and no convexity. The earlier three-slide version of this proof (IDs S36, S37, S38) is archived in the extended edition, `../opt03-backup/opt03-convexity-gd-full.html` and its notes.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html. The optional derivation follows the same section.
<!-- END S33 -->

<!-- BEGIN S34a -->
### 11. Start at the Current Point [S34a]

**Message.** At the current point $x$, the tangent gives the local slope of $f$; it is not a safe upper bound and says nothing about how far to step.

This is the first of three frames built on one fixed picture of a function of one variable. The solid black curve is $f$, a bowl-shaped curve. A blue dot marks the current point $x$ on its left, descending side. A thin grey line through that dot is the tangent at $x$, the linear model $f(x)+\langle g,y-x\rangle$ with $g=\nabla f(x)$; it slopes downward to the right.

The tangent matches the value and the slope of $f$ at $x$, so it tells which way is downhill. It does not tell how far to go: a linear model keeps decreasing forever and has no minimizer, so following it alone would suggest an unlimited step.

**Details.**

**Frame parameters** (the source line under the figure gives $f$ and $x$). $f(u)=u^2$, current point $x=-0.6$, so $f(x)=0.36$ and $g=f'(x)=-1.2$; tangent $T(u)=0.36-1.2(u+0.6)$. All three frames use the same axes and curves, generated by `figs/gd_model_build.py` in this deck folder, which asserts the geometry (our drawing and calculation).

**Sources.**

Illustration: our drawing (`figs/gd_model_build.py`).
<!-- END S34a -->

<!-- BEGIN S34b -->
### 12. Smoothness Adds an Upper Model [S34b]

**Message.** Smoothness adds the upper model $Q_x$, a bowl that touches $f$ at $x$ and stays above it everywhere.

Same frame as section 11, with one curve added: a dashed blue curve labelled upper model $Q_x$, where $Q_x(y)=f(x)+\langle g,y-x\rangle+\tfrac L2\|y-x\|^2$ is the right side of the descent lemma, the tangent plus a quadratic penalty.

All three curves meet at $x$ with the same slope. The dashed blue model lies on or above the solid black $f$ everywhere and touches it only at $x$; it is narrower than $f$ here, so it rises faster on both sides.

The labels: black is the objective $f$; grey is the tangent, the first-order model; dashed blue is the safe upper model $Q_x$. Unlike the tangent, $Q_x$ has a lowest point, because of its quadratic term.

**Details.**

**Frame parameters.** With $f(u)=u^2$, $f'(u)=2u$ is $2$-Lipschitz, so $f$ is $2$-smooth and hence also $3$-smooth; the drawing uses $L=3$. Then $Q_x(u)=0.36-1.2(u+0.6)+1.5(u+0.6)^2$ and $Q_x(u)-f(u)=\tfrac32(u+0.6)^2-(u+0.6)^2=\tfrac12(u+0.6)^2\ge0$, zero only at $u=x$ (our calculation). With $L=2$ the model would coincide with $f$; $L=3$ keeps the two curves visibly apart. Curves are clipped at the top of the plot.

**Sources.**

- Inequality: the descent lemma, Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
- Illustration: our drawing and calculation (`figs/gd_model_build.py`).
<!-- END S34b -->

<!-- BEGIN S34c -->
### 13. Minimize the Model, Then Step [S34c]

**Message.** Gradient descent steps to the minimizer of the model, $x-g/L$; there $f$ lies below the model, and the new point need not be the minimizer of $f$.

Same frame as section 12, with the step added. Below the axis a horizontal arrow runs from $x$ to the point labelled $x-g/L$, to the right because the slope $g$ is negative here. Above that point, a hollow blue dot marks the lowest point of the dashed model $Q_x$, and a solid black dot directly below it marks $f$ at the same input. A short red vertical segment joins the two dots, labelled gap: $f\le Q_x$. Further right, a grey dot at the bottom of the black curve is labelled min of $f$.

Read it in two moves. Horizontally: the step goes to the minimizer of the model, not to the minimizer of $f$. Vertically: at the new point the value of $f$ is at most the model's lowest value, which is $f(x)-\tfrac{\|g\|^2}{2L}$ (section 15). So the step lowers $f$ by at least $\tfrac{\|g\|^2}{2L}$.

The next step builds a new model at the new point and repeats.

**Details.**

**Frame numbers**. $x-g/L=-0.6+1.2/3=-0.2$. Model minimum $Q_x(-0.2)=0.36-1.2(0.4)+1.5(0.4)^2=0.12$, equal to $f(x)-g^2/(2L)=0.36-1.44/6=0.12$. Objective $f(-0.2)=0.04$, so the red gap is $0.08=\tfrac12(0.4)^2$. The minimizer of $f$ is $0$, not $-0.2$ (our calculation).

**Checks.** `figs/gd_model_build.py` asserts the touching point, $Q_x\ge f$, the tangent below $f$, and the values above.

**Sources.**

- Descent inequality: Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
- Illustration: our drawing and calculation (`figs/gd_model_build.py`).
<!-- END S34c -->

<!-- BEGIN S36 -->
### 14. Minimize a Safe Upper Model [S36]

**Message.** Fix the base point $x$; the descent lemma says $f(y)\le Q_x(y)$ for every candidate $y$, so we choose the next point by minimizing $Q_x$, not $f$.

Write $g=\nabla f(x)$. The upper model at $x$ is

$$Q_x(y)=f(x)+\langle g,y-x\rangle+\frac L2\|y-x\|^2.$$

The descent lemma says that for every candidate $y$,

$$f(y)\;\le\;Q_x(y).$$

Two roles must be kept apart. The base point $x$ is fixed: it is the current iterate, and $f(x)$ and $g$ are known numbers. The candidate $y$ is the variable. As a function of $y$, $Q_x$ is a simple quadratic, a round bowl with curvature $L$ in every direction, while $f$ may be any smooth function and hard to minimize directly.

So instead of solving the whole problem, minimize the model. Because the model sits above $f$, wherever we move, $f$ is at most what the model predicts there. This explains the step; it is not a proof of the descent lemma, which was stated in Section 10.

**Details.**

**Model versus objective.** $Q_x$ depends on the base point: after a step there is a new model at the new point. At the base point the model is exact, $Q_x(x)=f(x)$. The phrase upper model and this minimize-the-model reading are our exposition; the inequality itself is the descent lemma.

**Sources.**

- Inequality: Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
- Model view: our exposition.
<!-- END S36 -->

<!-- BEGIN S37 -->
### 15. Completing the Square Gives GD [S37]

**Message.** Completing the square writes $Q_x(y)=f(x)-\tfrac{\|g\|^2}{2L}+\tfrac L2\|y-(x-g/L)\|^2$, so the minimizer of the model is the gradient step $x-g/L$.

The derivation takes two steps:

$$\begin{aligned}Q_x(y)&=f(x)+\frac L2\Big(\|y-x\|^2\\&\qquad\qquad+\frac2L\langle g,y-x\rangle\Big)\\&=f(x)-\frac{\|g\|^2}{2L}\\&\qquad+\frac L2\Big\|y-\Big(x-\frac gL\Big)\Big\|^2.\end{aligned}$$

The first line factors $\tfrac L2$ out of the two terms that depend on $y$. For the second, expand $\|a+b\|^2=\|a\|^2+2\langle a,b\rangle+\|b\|^2$ with $a=y-x$ and $b=g/L$: $\|y-x+g/L\|^2=\|y-x\|^2+\tfrac2L\langle g,y-x\rangle+\tfrac{\|g\|^2}{L^2}$. Hence $\|y-x\|^2+\tfrac2L\langle g,y-x\rangle=\|y-(x-g/L)\|^2-\tfrac{\|g\|^2}{L^2}$. Multiply by $\tfrac L2$ and add $f(x)$.

The square is nonnegative and vanishes only at $y=x-g/L$. So the model is smallest exactly at the gradient step, and its smallest value is $f(x)-\tfrac{\|g\|^2}{2L}$.

Only the expansion of $\|a+b\|^2$ is used: no integral, no Hessian, no convexity.

**Details.**

**One variable.** $Q_x(u)=f(x)+g(u-x)+\tfrac L2(u-x)^2$ is a parabola with vertex at $u=x-g/L$, the familiar vertex formula. **Check on the pictures.** With $x=-0.6$, $g=-1.2$, $L=3$: vertex $-0.2$ and minimum value $0.36-1.44/6=0.12$, matching section 13.

**Sources.**

Our calculation (completing the square). Descent lemma: Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Descent lemma: Lipschitz conitnuous gradient implies a global quadratic upper bound" (section title spelled as in the source), https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
<!-- END S37 -->

<!-- BEGIN S90 -->
### 16. The Step $1/L$ Decreases $f$ [S90]

**Message.** Plugging the step $1/L$ into the lemma gives the descent inequality $f(x_{t+1})\le f(x_t)-\tfrac1{2L}\|\nabla f(x_t)\|^2$.

Write $g_t=\nabla f(x_t)$ and apply the lemma with $x=x_t$ and $y=x_{t+1}=x_t-\tfrac1Lg_t$. The linear term is $\langle g_t,-\tfrac1Lg_t\rangle=-\tfrac1L\|g_t\|^2$ and the penalty is $\tfrac L2\|\tfrac1Lg_t\|^2=\tfrac1{2L}\|g_t\|^2$. Adding them gives $f(x_{t+1})\le f(x_t)-\tfrac1{2L}\|g_t\|^2$. The step $x_{t+1}$ is the minimizer of the upper model $Q_{x_t}$ (section 15), and the right side is the minimum value of $Q_{x_t}$.

No convexity is used. Every step either keeps $f$ the same (only when $g_t=0$) or strictly lowers it. This single inequality drives all three guarantees in the lecture.

**Details.**

Among steps of the form $x_t-\alpha g_t$, the lemma gives $f(x_{t+1})\le f(x_t)-\alpha(1-\tfrac{L\alpha}2)\|g_t\|^2$, and $\alpha=1/L$ maximizes $\alpha(1-\tfrac{L\alpha}2)$, with value $\tfrac1{2L}$ (our calculation). This explains the choice of step; other step sizes are not used in the lecture.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07 step 1), with $\alpha=1/L$.
<!-- END S90 -->

<!-- REGION P4b END -->

<!-- REGION P4c BEGIN -->

## Part 3: Nonconvex: Stationarity

<!-- BEGIN S135 -->
### 17. Part 3: Nonconvex: Stationarity [S135]

**Message.** Part 3 uses smoothness and boundedness below: the smallest gradient seen shrinks, which certifies approximate stationarity, not a minimum.
<!-- END S135 -->

<!-- BEGIN S89 -->
### 18. Nonconvex Guarantee: Small Squared Gradient [S89]

**Message.** For any $L$-smooth $f$ bounded below, $T$ steps of size $1/L$ make the smallest squared gradient at most $2L(f(x_0)-f_{\text{low}})/T$.

Theorem (nonconvex, step $1/L$). Let $f:\mathbb{R}^n\to\mathbb{R}$ be differentiable and $L$-smooth with $f(x)\ge f_{\text{low}}$ for all $x$. For any $x_0$ and every $T\ge1$, the iterates satisfy $\min_{0\le t\le T-1}\|\nabla f(x_t)\|^2\le 2L(f(x_0)-f_{\text{low}})/T$.

The bound concerns the best of the $T$ squared gradients at $x_0,\dots,x_{T-1}$. It is not a bound on a gap $f(x_t)-f^\star$, and it does not say which iterate is best. The $\min$ is over the iterates, not a minimum of $f$.

Only a lower bound is assumed: $f_{\text{low}}$ need not be attained, and no minimizer is assumed. Convexity is not assumed either.

**Details.**

Indexing: the source states the bound with $f^*$, step $\alpha$ with $\alpha L\le1$, and a minimum over $t\in\{0,\dots,T\}$, i.e. $\min\|\nabla f(w_t)\|^2\le2(f(w_0)-f^*)/(\alpha T)$. Here we use exactly $T$ gradients indexed $0$ to $T-1$, which is what summing $T$ descent inequalities gives (sections 19 and 20), and replace $f^*$ by any lower bound, which the telescoping proof allows. With $\alpha=1/L$ the constants agree.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06), specialized to $\alpha=1/L$ and a lower bound $f_{\text{low}}$.
<!-- END S89 -->

<!-- BEGIN S91 -->
### 19. Proof Step 1: Sum the Decreases [S91]

**Message.** Adding the descent inequality over $T$ steps telescopes, so the total squared gradient is capped by the finite budget $f(x_0)-f_{\text{low}}$.

Rearrange the descent inequality as $\tfrac1{2L}\|\nabla f(x_t)\|^2\le f(x_t)-f(x_{t+1})$ and add it for $t=0,\dots,T-1$. On the right, consecutive terms cancel and only $f(x_0)-f(x_T)$ remains. Since $f(x_T)\ge f_{\text{low}}$, this is at most $f(x_0)-f_{\text{low}}$.

Result: $\tfrac1{2L}\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2\le f(x_0)-f_{\text{low}}$. The only place the lower bound enters is $f(x_T)\ge f_{\text{low}}$; no minimizer is needed.

**Details.**

Telescoping written out: $\sum_{t=0}^{T-1}(f(x_t)-f(x_{t+1}))=(f(x_0)-f(x_1))+(f(x_1)-f(x_2))+\dots+(f(x_{T-1})-f(x_T))=f(x_0)-f(x_T)$.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06, E07).
<!-- END S91 -->

<!-- BEGIN S92 -->
### 20. Proof Step 2: Minimum at Most Average [S92]

**Message.** The smallest of $T$ numbers is at most their average, which turns the summed bound into the theorem.

$\min_{0\le t\le T-1}\|\nabla f(x_t)\|^2\le\tfrac1T\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2\le\tfrac{2L(f(x_0)-f_{\text{low}})}T$, where the second inequality is Step 1 multiplied by $2L/T$.

The guarantee is about the best iterate among the first $T$, not the last one. The proof gives no bound on $\|\nabla f(x_{T-1})\|$ itself beyond what the descent inequality says.

**Details.**

The same argument bounds the average squared gradient, which is a slightly stronger statement than the minimum.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06).
<!-- END S92 -->

<!-- BEGIN S141 -->
### 21. Every Gradient Norm Vanishes [S141]

**Message.** Under the nonconvex assumptions the whole sequence of gradient norms tends to zero, $\|\nabla f(x_t)\|\to0$, but with no rate for the last iterate and no claim about the iterates themselves.

Q: Does $\|\nabla f(x_t)\|\to0$ for nonconvex gradient descent? A: Yes, for the whole sequence, under the same assumptions: $f$ is $L$-smooth, $f\ge f_{\text{low}}$, and the step is $1/L$.

Write $B=2L(f(x_0)-f_{\text{low}})$, a fixed finite budget. Step 1 of the proof (section 19) gives, for every $T$,

$$\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2\;\le\;B.$$

The right side does not depend on $T$, and the partial sums only grow, so the infinite sum is finite:

$$\sum_{t\ge0}\|\nabla f(x_t)\|^2\;\le\;B\;\lt\;\infty.$$

Therefore

$$\|\nabla f(x_t)\|\to0.$$

The reason in one line: nonnegative terms with a finite sum must tend to zero.

What it does not say. It is an asymptotic statement about the whole sequence, not a rate: there is no $O(1/T)$ bound on the last gradient; the $O(1/T)$ rate of section 18 is for the best squared gradient. It also says nothing about whether $x_t$ converges, or to what (section 22).

**Details.**

**The $\varepsilon$ argument.** Suppose the gradient norms do not tend to zero. Then there is $\varepsilon\gt0$ with $\|\nabla f(x_t)\|\ge\varepsilon$ for infinitely many $t$. Each such $t$ adds at least $\varepsilon^2$ to the sum, so after $N$ of them the partial sum is at least $N\varepsilon^2$, which exceeds $2L(f(x_0)-f_{\text{low}})$ once $N\gt2L(f(x_0)-f_{\text{low}})/\varepsilon^2$: a contradiction. So for every $\varepsilon\gt0$ only finitely many $t$ have $\|\nabla f(x_t)\|\ge\varepsilon$, which is the definition of $\|\nabla f(x_t)\|\to0$.

**Why no rate.** The argument uses only that the series is summable, which by itself gives no bound on an individual term at a given $t$; nothing in it makes the gradient norms decrease monotonically.

**Assumptions.** Only a finite lower bound $f_{\text{low}}$ is needed; it need not be attained, and no minimizer is assumed. The iterates may fail to converge; the statement is about gradients only.

**Sources.**

- Summed bound for every $T$: Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
- The limit and the $\varepsilon$ argument: our deduction from that bound.
<!-- END S141 -->

<!-- BEGIN S93 -->
### 22. Stationary Does Not Mean Minimum [S93]

**Message.** Nonconvex gradient descent gets a $1/T$ rate only for the smallest squared gradient; vanishing gradients do not mean reaching a local optimum.

Q: Does nonconvex GD reach a local optimum at rate $1/T$ (asked as "linear convergence to local optimum")? A: No. The $1/T$ rate is for $\min_t\|\nabla f(x_t)\|^2$ only. Under these assumptions there is no guarantee of a local minimum, and the rate $1/T$ is sublinear, not linear.

The figure is four nested boxes. The outer box is the set of $\varepsilon$-stationary points, $\|\nabla f(x)\|\le\varepsilon$: this is what the theorem delivers. Inside it is the set of stationary points, $\nabla f(x)=0$, which also contains local maxima and saddle points. Inside that, in a dashed box, are local minima, which are not guaranteed. Innermost, also dashed, are global minima.

Scope: $L$-smooth, bounded below, step $1/L$, and no further assumptions. The gradients do vanish (section 21); what fails is the step from a vanishing gradient to a minimum.

**Details.**

section 21 showed $\|\nabla f(x_t)\|\to0$ for the whole sequence. That is a statement about gradients, not iterates: it does not imply that $x_t$ converges. If a subsequence of iterates converges to some $\bar x$, continuity of $\nabla f$ gives $\nabla f(\bar x)=0$: the limit is stationary, but it may be a maximum or a saddle.

**Optional example: gradient descent can stay at a maximum.** Take $f(x)=1-\cos x$ on $\mathbb{R}$. It satisfies the assumptions: $f\ge0$, so $f_{\text{low}}=0$; and $f$ is $1$-smooth, because $f'(x)=\sin x$ and $|\sin x-\sin y|\le|x-y|$ by the mean value theorem, since $|\cos|\le1$, while $f''(0)=1$ shows no smaller constant works. With step $1/L=1$ the update is $x_{t+1}=x_t-\sin x_t$. Start at $x_0=\pi$: since $\sin\pi=0$, $f'(\pi)=0$ and $x_t=\pi$ for all $t$. But $f''(\pi)=\cos\pi=-1\lt0$, so $\pi$ is a strict local maximum, and $f(\pi)=2$ is in fact the global maximum. The theorem still holds: $\min_t|f'(x_t)|^2=0\le2\cdot1\cdot(2-0)/T=4/T$ for every $T$. This uses an exact start at the maximum; it says nothing about a typical start.

Stronger conclusions, such as avoiding saddle points from almost every start, need further assumptions and are outside this lecture.

**Sources.**

- Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD" and the following discussion, which says the limit "can even be a local maximum or saddle point", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html.
- Optional example: our calculation (formerly slide ID S136, removed from the lecture).
<!-- END S93 -->

<!-- BEGIN S137 -->
### 23. The Square Changes the Rate [S137]

**Message.** The smallest gradient norm among the first $T$ iterates, $\min_{0\le t\le T-1}\|\nabla f(x_t)\|$, is bounded by $O(1/\sqrt T)$; $O(1/\varepsilon^2)$ steps suffice to find an iterate with $\|\nabla f(x_t)\|\le\varepsilon$.

Square-rooting the theorem gives $\min_{0\le t\le T-1}\|\nabla f(x_t)\|\le\sqrt{2L(f(x_0)-f_{\text{low}})/T}=O(1/\sqrt T)$. Solving for $T$: if $T\ge2L(f(x_0)-f_{\text{low}})/\varepsilon^2$, then some $t\le T-1$ has $\|\nabla f(x_t)\|\le\varepsilon$.

So asking for tolerance $\varepsilon/10$ instead of $\varepsilon$ multiplies this iteration bound by $100$. The constants $L$ and $f(x_0)-f_{\text{low}}$ depend on the problem.

Again, this is a best-iterate statement: there is no $O(1/T)$ rate for the gradient norm, and no local-minimum guarantee.

**Details.**

Full constant: $T\ge\lceil2L(f(x_0)-f_{\text{low}})/\varepsilon^2\rceil$ suffices. This is a worst-case guarantee for the best iterate. It is different from the limit of section 21: every gradient norm tends to zero, but with no rate for the last iterate.

The source gives the squared-gradient bound; the square root and the iteration count are our derivation from it.

**Sources.**

Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (evidence E06: $O(\varepsilon^{-2})$ iterations). Square root and $T$ count: our derivation.
<!-- END S137 -->

<!-- REGION P4c END -->

<!-- REGION P4d BEGIN -->

## Part 4: Convex: Optimality

<!-- BEGIN S09 -->
### 24. Part 4: Convex: Optimality [S09]

**Message.** Part 4 adds convexity: the function gap to the optimum shrinks at rate $O(1/T)$.
<!-- END S09 -->

<!-- BEGIN S10 -->
### 25. Convexity Puts Chords Above [S10]

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
### 26. The Tangent Lies Below [S15]

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
### 27. Assume an Optimum Exists [S95]

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
### 28. Convex: O(1/T) Function Gap [S96]

**Message.** For a convex $L$-smooth function with a minimizer, gradient descent with step $1/L$ has function gap at most $L\|x_0-x^\star\|^2/(2T)$ after $T$ steps.

Read the statement part by part. Domain: $f:\mathbb{R}^n\to\mathbb{R}$ with the Euclidean norm. Assumptions: $f$ differentiable, convex, $L$-smooth, and a minimizer $x^\star$ exists. Algorithm: $x_{t+1}=x_t-\tfrac1L\nabla f(x_t)$ from any $x_0$. Quantifier: for every $T\ge1$,

$$f(x_T)-f^\star\le\frac{L\|x_0-x^\star\|^2}{2T}.$$

The measured quantity is the function-value gap at the last iterate. The theorem says nothing directly about $\|x_T-x^\star\|$. The rate is sublinear: to reach gap $\varepsilon$ the bound needs $T\ge LD_0/(2\varepsilon)$, that is $O(1/\varepsilon)$ steps.

**Details.**

Sections 29 to 34 prove this theorem. The bound is stated for any minimizer $x^\star$; with several minimizers, use the one nearest $x_0$.

The earlier version of this lecture proved this result with co-coercivity; that proof is in the backup note. The route used now needs only the descent inequality and the tangent bound.

**Who proved it?** An earlier version of this lecture cited only Garrigos and Gower (2024) for this theorem. Their handbook is a correct reference for the exact statement and constant, but it is a modern exposition, not the original source: its bibliographic notes for this chapter refer to Nesterov's 2004 book for proofs. Nesterov (2004) is an earlier standard treatment; we have not verified who first published the result, so no discoverer is named. Theorem numbers from other editions or drafts of Nesterov's notes are deliberately not quoted.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. https://link.springer.com/book/10.1007/978-1-4419-8853-9 (an earlier standard treatment; not verified as the first publication).
- Garrigos and Gower, same handbook, Section 3.4, "Bibliographic notes", which refer to Nesterov (2004) for proofs. https://arxiv.org/abs/2301.11235v3
<!-- END S96 -->

<!-- BEGIN S97 -->
### 29. Proof Plan: Spend Distance [S97]

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
### 30. Recall: One-Step Decrease [S98]

**Message.** Smoothness alone gives the one-step decrease $\Delta_{t+1}\le\Delta_t-\tfrac1{2L}\|g_t\|^2$.

Write $g_t=\nabla f(x_t)$. The descent inequality, proved earlier in the lecture for any $L$-smooth $f$ and the step $1/L$, says

$$f(x_{t+1})\le f(x_t)-\frac1{2L}\|g_t\|^2.$$

Subtracting $f^\star$ from both sides rewrites it in terms of gaps. Nothing here uses convexity.

**Details.**

**Re-derivation.** The smoothness upper bound at $x=x_t$, $y=x_{t+1}=x_t-g_t/L$ gives $f(x_{t+1})\le f(x_t)-\tfrac1L\|g_t\|^2+\tfrac L2\cdot\tfrac1{L^2}\|g_t\|^2=f(x_t)-\tfrac1{2L}\|g_t\|^2$.

Two consequences are used later: the gaps are nonincreasing, $\Delta_{t+1}\le\Delta_t$ (section 34), and each step removes at least $\|g_t\|^2/(2L)$ of gap.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S98 -->

<!-- BEGIN S99 -->
### 31. Use the Tangent at x_t [S99]

**Message.** Convexity's tangent bound at $x_t$, evaluated at $x^\star$, bounds the gap by $\langle g_t,x_t-x^\star\rangle$.

Take the tangent bound with $x=x_t$ and $y=x^\star$: $f^\star\ge f(x_t)+\langle g_t,x^\star-x_t\rangle$. Moving terms gives $\Delta_t\le\langle g_t,x_t-x^\star\rangle$.

Put this into the descent step of section 30:

$$\Delta_{t+1}\le\langle g_t,x_t-x^\star\rangle-\frac1{2L}\|g_t\|^2.$$

This is the only use of convexity in the proof, and it is plain convexity, not strong convexity.

**Details.**

By Cauchy-Schwarz the same step gives $\Delta_t\le\|g_t\|\sqrt{D_t}$: a convex function cannot have a large gap where both the gradient and the distance to $x^\star$ are small.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S99 -->

<!-- BEGIN S101 -->
### 32. Expand the Squared Distance [S101]

**Message.** Expanding $\|x_{t+1}-x^\star\|^2$ shows that the right side of the last bound equals $\tfrac L2(D_t-D_{t+1})$, so $\Delta_{t+1}\le\tfrac L2(D_t-D_{t+1})$.

The update gives $x_{t+1}-x^\star=(x_t-x^\star)-\tfrac1Lg_t$. Expanding the square,

$$D_{t+1}=D_t-\frac2L\langle g_t,x_t-x^\star\rangle+\frac1{L^2}\|g_t\|^2.$$

Multiplying by $L/2$ and rearranging gives $\tfrac L2(D_t-D_{t+1})=\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2$, exactly the right side of the tangent-plus-descent bound. Therefore

$$\Delta_{t+1}\le\frac L2\big(D_t-D_{t+1}\big).$$

The gap after step $t$ is paid for by the drop in squared distance during step $t$.

**Details.**

**Index check.** The right side uses $g_t$, $D_t$ and $D_{t+1}$; the left side is the gap at $x_{t+1}$, one index ahead of the gradient.

**A by-product.** Because $\Delta_{t+1}\ge0$, the inequality forces $D_{t+1}\le D_t$: under convexity, the iterates never move away from any minimizer.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S101 -->

<!-- BEGIN S104 -->
### 33. Distances Telescope [S104]

**Message.** Summing the per-step bound over $t=0,\dots,T-1$ cancels the middle distances and leaves $\sum_{t=1}^T\Delta_t\le\tfrac L2D_0$.

Write the bound for $t=0,1,\dots,T-1$ and add the $T$ inequalities. The left sides add to $\Delta_1+\dots+\Delta_T$. On the right, each $D_t$ with $1\le t\le T-1$ appears once with a plus sign and once with a minus sign, so

$$\sum_{t=1}^T\Delta_t\le\frac L2\big(D_0-D_T\big)\le\frac L2D_0,$$

where the last step drops $D_T\ge0$.

**Details.**

**Off-by-one check.** There are $T$ inequalities, $T$ gaps $\Delta_1,\dots,\Delta_T$ on the left, and the distance terms run from $D_0$ to $D_T$. The gap $\Delta_0$ never appears.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S104 -->

<!-- BEGIN S105 -->
### 34. The Last Gap Is Smallest [S105]

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
### 35. The Convex Proof in One Chain [S106]

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
### 36. Part 5: Strongly Convex: Geometric Decay [S63]

**Message.** Part 5 adds strong convexity: the distance to the minimizer shrinks by a fixed factor every step.
<!-- END S63 -->

<!-- BEGIN S64 -->
### 37. Add a Quadratic Floor [S64]

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
### 38. Curvature Is Bounded Below [S65]

**Message.** Strong convexity and smoothness together trap the remainder above the tangent between $\tfrac\mu2\|y-x\|^2$ and $\tfrac L2\|y-x\|^2$.

Let $r(y)=f(y)-f(x)-\langle\nabla f(x),y-x\rangle$ be the height of $f$ above its tangent at $x$. Then

$$\frac\mu2\|y-x\|^2\le r(y)\le\frac L2\|y-x\|^2.$$

The curvature of $f$ is at least $\mu$ and at most $L$ in every direction.

The figure is a generic one-variable picture. The solid black curve is $f$, with a marked base point $x$ and a thin grey tangent line through it. A green curve labelled floor, curvature $\mu$, is the tangent plus $\tfrac\mu2(y-x)^2$; a dashed blue curve labelled upper, curvature $L$, is the tangent plus $\tfrac L2(y-x)^2$. All three curves and the tangent touch at $x$ with the same slope; the green floor stays below $f$ and the blue curve stays above it.

**Details.**

**Figure parameters** (illustrative; not the lecture's earlier example). $f(s)=s^2$, which has curvature $2$, with illustrative constants $\mu=1$ and $L=3$ and base point $s_0=-1$. The residual above the tangent is $r=(s+1)^2$; the floor adds $\tfrac12(s+1)^2$ and the upper curve $\tfrac32(s+1)^2$, and $\tfrac12h^2\le h^2\le\tfrac32h^2$ for $h=s+1$ because $1\lt2\lt3$ (our calculation).

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring). The script asserts $\tfrac\mu2h^2\le r\le\tfrac L2h^2$ on a fine grid; the upper curve is clipped at the top of the plot.

**Sources.**

Illustration: our drawing and calculation (`figs/o3b_figs.py`).
<!-- END S65 -->

<!-- BEGIN S116 -->
### 39. Strongly Convex: Geometric Convergence [S116]

**Message.** Under strong convexity and smoothness, gradient descent with step $1/L$ shrinks the squared distance to the minimizer by the factor $q=1-\mu/L$ every step.

Statement: $f:\mathbb{R}^n\to\mathbb{R}$ is $\mu$-strongly convex and $L$-smooth, $0\lt\mu\le L$, with unique minimizer $x^\star$ (it exists and is unique by strong convexity). Gradient descent uses step $1/L$ from any $x_0$. For every $T\ge1$,

$$\|x_T-x^\star\|^2\le\Big(1-\frac\mu L\Big)^T\|x_0-x^\star\|^2.$$

The factor $q=1-\mu/L$ lies in $[0,1)$. If $q=0$, that is $\mu=L$, a single step lands on $x^\star$. To get $D_T\le\varepsilon$ it suffices that $T\ge\tfrac L\mu\ln(D_0/\varepsilon)$.

The step is the same $1/L$ as in every other part of the lecture. Other step sizes give other theorems, not used here.

**Details.**

**The case $\mu=L$.** Then the remainder bounds coincide, $r(y)=\tfrac L2\|y-x\|^2$ exactly, so $f$ is a quadratic with Hessian $LI$ and $x_0-\tfrac1L\nabla f(x_0)$ is its minimizer.

**Iteration count.** $q^T\le e^{-\mu T/L}$ (section 42), and $e^{-\mu T/L}D_0\le\varepsilon$ when $T\ge\tfrac L\mu\ln(D_0/\varepsilon)$.

The earlier version of this lecture stated this result with step $2/(\mu+L)$ and a co-coercivity proof; see the backup note.

**Attribution.** As for the convex theorem, Garrigos and Gower (2024) is cited for the precise modern statement and Nesterov (2004) as an earlier standard treatment; neither is claimed as the first publication. The proof in Sections 40-43 is the elementary shared-distance argument with step $1/L$, not a source proof that needs co-coercivity or another step size.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
- Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. https://link.springer.com/book/10.1007/978-1-4419-8853-9 (an earlier standard treatment; not verified as the first publication).
<!-- END S116 -->

<!-- BEGIN S138 -->
### 40. Keep the Extra Curvature Term [S138]

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
### 41. Nonnegative Gap Forces Contraction [S139]

**Message.** Because the next gap is nonnegative, the per-step bound forces $D_{t+1}\le(1-\mu/L)D_t$.

Since $x^\star$ minimizes $f$, $\Delta_{t+1}\ge0$, so the per-step bound of section 40 gives

$$0\le\frac L2(D_t-D_{t+1})-\frac\mu2D_t.$$

Multiply by $2/L$: $0\le D_t-D_{t+1}-\tfrac\mu LD_t$, that is $D_{t+1}\le(1-\tfrac\mu L)D_t=qD_t$. Every step shrinks the squared distance by at least the factor $q$.

**Details.**

The argument throws away the gap $\Delta_{t+1}$ and keeps only distances; that is one reason the bound can be loose.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S139 -->

<!-- BEGIN S122 -->
### 42. Repeat the Same Contraction [S122]

**Message.** Applying the one-step contraction $T$ times gives $D_T\le q^TD_0$.

Chain the contraction: $D_T\le qD_{T-1}\le q^2D_{T-2}\le\dots\le q^TD_0$.

The statement is for $T\ge1$, which also covers $q=0$: then $D_1=0$, so $x_1=x^\star$ and all later iterates stay there, with no $0^0$ to interpret.

Since $1-u\le e^{-u}$ for every real $u$, $q^T\le e^{-\mu T/L}$: the error falls by a constant factor every step.

**Details.**

**Induction.** Base case $T=1$ is the contraction of section 41 at $t=0$. If $D_T\le q^TD_0$, then $D_{T+1}\le qD_T\le q^{T+1}D_0$; multiplying the inequality by $q$ is allowed because $q\ge0$, which holds since $\mu\le L$.

**The exponential bound.** $u\mapsto e^{-u}$ is convex with tangent $1-u$ at $u=0$, so the tangent bound gives $e^{-u}\ge1-u$. With $u=\mu/L$ and $q\ge0$, raising to the power $T$ gives $q^T\le e^{-\mu T/L}$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S122 -->

<!-- BEGIN S123 -->
### 43. Function Values Follow Distance [S123]

**Message.** Smoothness at the minimizer converts the distance bound into the function-gap bound $\Delta_T\le\tfrac L2q^TD_0$.

Use the smoothness upper bound at $x=x^\star$, where $\nabla f(x^\star)=0$, with $y=x_T$: $f(x_T)\le f^\star+\tfrac L2\|x_T-x^\star\|^2$. With the distance bound of section 42,

$$\begin{aligned}f(x_T)-f^\star&\le\frac L2\|x_T-x^\star\|^2\\
&\le\frac L2q^T\|x_0-x^\star\|^2.\end{aligned}$$

The iterates converge to the unique minimizer $x^\star$, and their function values converge to $f^\star$. Under the nonconvex assumptions, every gradient norm tends to zero, but convergence of $x_t$ to a minimizer is not guaranteed.

**Details.**

The prefactor is $\tfrac L2D_0$. A bound of the form $\Delta_T\le q^T\Delta_0$ would need a separate function-gap contraction argument, which this lecture does not prove.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
<!-- END S123 -->

<!-- BEGIN S110 -->
### 44. Linear Means Geometric [S110]

**Message.** In optimization, linear convergence means the error shrinks geometrically, like $q^T$ with $0\lt q\lt1$; the convex $O(1/T)$ rate is sublinear.

A rate is called linear when the error after $T$ steps is at most $Cq^T$ with $0\lt q\lt1$. The name comes from the log scale: $\log(Cq^T)=\log C+T\log q$ is a straight line in $T$. Geometric and exponential mean the same thing here.

A rate like $1/T$ is sublinear: on a log scale its curve flattens out. The convex rate $O(1/T)$ is sublinear, not linear; the strongly convex rate is linear.

The figure plots two curve shapes on a logarithmic vertical axis for $T=1,\dots,24$: grey $1/T$ and blue $q^T$ for one illustrative value $q=0.8$. The blue curve is a straight line falling to about $5\times10^{-3}$ at $T=24$; the grey curve flattens near $0.04$. For $T=2$ to $10$ the blue curve is higher; from $T=11$ on it is lower and the gap widens.

The plot shows shapes only, with an illustrative $q$: it is not output of gradient descent and does not say which bound is smaller for every $T$ or every constant. Each iteration is the same gradient step in both settings.

**Details.**

**Error versus iteration count.** These are two readings of one bound. Error after $T$ steps: $q^T$ against $1/T$. Steps needed for error $\varepsilon$: $O(\log(1/\varepsilon))$ against $O(1/\varepsilon)$. Keep them apart: a linear rate is an error statement, and $\log(1/\varepsilon)$ is the matching iteration count.

**Plot numbers.** $0.8^{24}=e^{24\ln0.8}\approx e^{-5.36}\approx4.7\times10^{-3}$; $1/24\approx0.042$. Crossing: $0.8^{10}\approx0.107\gt1/10$, $0.8^{11}\approx0.086\lt1/11\approx0.091$ (our calculation).

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring).

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3 (Remark 3.7 on the terminology)
- Plot: our calculation.
<!-- END S110 -->

<!-- REGION P4e END -->

<!-- REGION P4f BEGIN -->

## Part 6: Three Guarantees

<!-- BEGIN S130 -->
### 45. Part 6: Three Guarantees [S130]

**Message.** Part 6 compares the three guarantees side by side.
<!-- END S130 -->

<!-- BEGIN S131 -->
### 46. Three Assumptions, Three Guarantees [S131]

**Message.** One algorithm, three assumption levels, three guarantees: vanishing gradients with a best-iterate rate, then an $O(1/T)$ function gap, then geometric convergence to the minimizer.

All three rows use gradient descent with step $1/L$ on an $L$-smooth $f:\mathbb{R}^n\to\mathbb{R}$.

Nonconvex, with $f\ge f_{\text{low}}$: $\min_{t\lt T}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})/T$, a best-iterate $O(1/T)$ rate for the squared gradient. A line below the table adds that every $\|\nabla f(x_t)\|\to0$ and that there is no local-minimum guarantee; that limit comes with no rate.

Convex, with a minimizer: $\Delta_T\le LD_0/(2T)$, a sublinear $O(1/T)$ rate on the last function gap.

$\mu$-strongly convex: $D_T\le q^TD_0$ and $\Delta_T\le\tfrac L2q^TD_0$ with $q=1-\mu/L$, a linear, that is geometric, rate.

This is the lecture's one global recap; each row measures a different quantity, so compare what is guaranteed, not only the speed.

**Details.**

Three different statements, kept apart: (i) nonconvex, the whole sequence of gradient norms tends to zero (section 21), with an $O(1/T)$ rate only for the best squared gradient (section 18); (ii) convex, the objective gap at the last iterate is $O(1/T)$ (section 28); (iii) strongly convex, the distance and the gap shrink geometrically (section 39).

Constants and alternative step sizes are deliberately omitted from the table.

**Sources.**

- Nonconvex: Cornell CS4787/5777 (Fall 2026), Lecture 5, section "Convergence of GD", https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html. The limit: our deduction.
- Convex and strongly convex: Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. https://link.springer.com/book/10.1007/978-1-4419-8853-9 (an earlier standard treatment; not verified as the first publication).
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
<!-- END S131 -->

<!-- BEGIN S140 -->
### 47. No Extra Conditions Needed [S140]

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
### 48. Closing: One Update [S134]

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
21. Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. https://link.springer.com/book/10.1007/978-1-4419-8853-9. Cited on the convex and strongly convex theorems as an earlier standard treatment of the fixed-step rates; it is not claimed as the first publication.
