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
### 4. The Problem [S80]
<!-- END S80 -->

<!-- BEGIN S14 -->
### 5. The Gradient, Recalled [S14]
<!-- END S14 -->

<!-- BEGIN S82 -->
### 6. 1D Intuition -- the Sign Does the Steering [S82]
<!-- END S82 -->

<!-- BEGIN S27 -->
### 7. Definition -- $L$-Smooth [S27]

Throughout, "$L$-smooth" is a statement about a specific $L$; a function that is $L$-smooth is also $L'$-smooth for any $L'\ge L$. The *smoothness constant* means the smallest such $L$, which by Theorem 3.2 below equals $\sup_x\|\nabla^2f(x)\|_2$.
<!-- END S27 -->

<!-- BEGIN S81 -->
### 8. The Algorithm [S81]

#### 6.1 The algorithm and where it comes from

Gradient descent is $x_{i+1}=x_i-\alpha\nabla f(x_i)$, the method Cauchy proposed in a two-page note of 1847 [6], for solving systems of equations rather than for machine learning. The lecture presents the step as "move downhill"; the descent lemma gives the sharper derivation, and it is worth writing out because it explains the specific constant $1/L$ that appears everywhere. Minimizing the **lid** from Lemma 3.1 over the next iterate,

$ x_{i+1}\;=\;\arg\min_{y}\;\Bigl\{f(x_i)+\langle\nabla f(x_i),\,y-x_i\rangle+\frac{1}{2\alpha}\|y-x_i\|^2\Bigr\}\;=\;x_i-\alpha\nabla f(x_i), $

by setting the gradient of the quadratic to zero. So gradient descent *is* the exact minimization of a local quadratic model of $f$, with $1/\alpha$ playing the role of assumed curvature. Choosing $\alpha=1/L$ means "trust the model with the worst-case curvature"; choosing $\alpha$ larger means assuming less curvature than $f$ may actually have, which is exactly how divergence happens.
<!-- END S81 -->

<!-- BEGIN S30 -->
### 9. Running Example -- $L = 4$ [S30]

**Running example.** $\nabla^2f=\operatorname{diag}(4,1)$ has spectral norm $4$, so $f$ is $4$-smooth and not $L$-smooth for any $L<4$. The constant $L=4$ used throughout is the exact smoothness constant, not a loose bound. Concretely, the gradient map $x\mapsto(4x_1,x_2)$ stretches the $e_1$ direction by exactly $4$.
<!-- END S30 -->

<!-- REGION P4a END -->

<!-- REGION P4b BEGIN -->

<!-- BEGIN S25 -->
### 10. Part 2: One Descent Inequality [S25]

**Message.** Part 2 proves the one inequality that every later guarantee uses: each step lowers $f$ by at least $\frac{1}{2L}\|\nabla f\|^2$.
<!-- END S25 -->

<!-- BEGIN S33 -->
### 11. Lemma 1 -- the Descent Lemma [S33]

#### 3.2 The descent lemma (Lemma 1 of the lecture)

This is the single most important consequence of smoothness. The lecture proves it in three steps; the proof below is the same argument with the fundamental-theorem-of-calculus step written out.

**Lemma 3.1 (descent lemma).** If $f$ is $L$-smooth then for all $x,\delta$,

$ \Bigl|\,f(x+\delta)-f(x)-\langle\nabla f(x),\delta\rangle\,\Bigr|\;\le\;\tfrac{L}{2}\|\delta\|^2. \tag{3.1} $

In particular the **upper lid** $f(x+\delta)\le f(x)+\langle\nabla f(x),\delta\rangle+\tfrac{L}{2}\|\delta\|^2$ holds, and so does the **lower floor** $f(x+\delta)\ge f(x)+\langle\nabla f(x),\delta\rangle-\tfrac{L}{2}\|\delta\|^2$.

*Proof.* **Step 1, fundamental theorem of calculus along the segment.** Let $\varphi(t)=f(x+t\delta)$ for $t\in[0,1]$. Then $\varphi'(t)=\langle\nabla f(x+t\delta),\delta\rangle$ and

$ f(x+\delta)-f(x)\;=\;\varphi(1)-\varphi(0)\;=\;\int_0^1\langle\nabla f(x+t\delta),\,\delta\rangle\,dt. $

**Step 2, subtract the linear model.** Since $\langle\nabla f(x),\delta\rangle=\int_0^1\langle\nabla f(x),\delta\rangle\,dt$,

$ f(x+\delta)-f(x)-\langle\nabla f(x),\delta\rangle \;=\;\int_0^1\bigl\langle\nabla f(x+t\delta)-\nabla f(x),\;\delta\bigr\rangle\,dt. $

**Step 3, bound the integrand.** By Cauchy-Schwarz and then $L$-smoothness applied to the two points $x+t\delta$ and $x$, whose separation is $\|t\delta\|=t\|\delta\|$,

$ \bigl|\langle\nabla f(x+t\delta)-\nabla f(x),\delta\rangle\bigr| \;\le\;\|\nabla f(x+t\delta)-\nabla f(x)\|\,\|\delta\|\;\le\;Lt\|\delta\|^2. $

Integrating, $\int_0^1 Lt\|\delta\|^2\,dt=L\|\delta\|^2\int_0^1t\,dt=\tfrac{L}{2}\|\delta\|^2$. Taking absolute values through the integral gives (3.1). **End of proof.**
<!-- END S33 -->

<!-- BEGIN S34 -->
### 12. The Picture -- a Parabola Lid [S34]
<!-- END S34 -->

<!-- BEGIN S36 -->
### 13. Step 1 -- Set Up $g$ [S36]
<!-- END S36 -->

<!-- BEGIN S37 -->
### 14. Step 2 -- Bound the Slope Drift [S37]
<!-- END S37 -->

<!-- BEGIN S38 -->
### 15. Step 3 -- Integrate [S38]
<!-- END S38 -->

<!-- BEGIN S90 -->
### 16. Proof -- One Step Through the Lid [S90]
<!-- END S90 -->

<!-- BEGIN S83 -->
### 17. Running Example -- GD, Set Up by Hand [S83]
<!-- END S83 -->

<!-- BEGIN S84 -->
### 18. Four Iterations by Hand ($\alpha = 1/4$) [S84]

#### 6.3 The iterate sequence, verified

With $\alpha=1/4$ and $x_0=(2,2)$ the recursions are $x_1^{(i+1)}=(1-1)x_1^{(i)}=0$ and $x_2^{(i+1)}=0.75\,x_2^{(i)}$. Five iterations, each given as: index $i$; the iterate $x_i$; the value $f(x_i)$; the squared distance $\|x_i-x^\star\|^2$.

- $i=0$; $x_0=(2,\,2)$; $f=10$; squared distance $8$.
- $i=1$; $x_1=(0,\,1.5)$; $f=1.125$; squared distance $2.25$.
- $i=2$; $x_2=(0,\,1.125)$; $f=0.6328$; squared distance $1.2656$.
- $i=3$; $x_3=(0,\,0.8438)$; $f=0.3560$; squared distance $0.7119$.
- $i=4$; $x_4=(0,\,0.6328)$; $f=0.2002$; squared distance $0.4004$.

All values check: $f=\tfrac12x_2^2$ once $x_1=0$, and the ratio of consecutive values of $f$, and of consecutive squared distances, is $0.75^2=0.5625$ from step 1 onward. The single large drop from $i=0$ to $i=1$ is the $x_1$ coordinate being annihilated exactly; everything after is the slow $x_2$ mode, whose rate $0.75=1-\alpha\mu$ is what the theory predicts.
<!-- END S84 -->

<!-- REGION P4b END -->

<!-- REGION P4c BEGIN -->

<!-- BEGIN S135 -->
### 19. Part 3: Nonconvex: Stationarity [S135]

**Message.** Part 3 uses smoothness alone: the smallest gradient seen shrinks, which certifies approximate stationarity, not a minimum.
<!-- END S135 -->

<!-- BEGIN S89 -->
### 20. Theorem 7 -- GD Converges (Smooth Case) [S89]

#### 6.4 Theorem 7, stated honestly

The lecture source phrases Theorem 7 as "gradient descent converges to the local minimum" for $\alpha\in(0,2/L)$. That overstates what the proof delivers, and the presentation already softens it. For the record, here is what is actually true under $L$-smoothness alone, with no convexity, and what is not.

**Theorem 6.2.** Let $f$ be $L$-smooth and bounded below by $f^\star$, and let $0<\alpha<2/L$. Then gradient descent satisfies:

(a) $f(x_{i+1})\le f(x_i)-\alpha\bigl(1-\tfrac{\alpha L}{2}\bigr)\|\nabla f(x_i)\|^2$, so $f(x_i)$ is nonincreasing;

(b) $f(x_i)$ converges to some limit that is at least $f^\star$;

(c) $\sum_{i=0}^{\infty}\|\nabla f(x_i)\|^2<\infty$, hence $\|\nabla f(x_i)\|\to0$.

*Proof.* (a) Apply the lid of Lemma 3.1 with $x=x_i$ and $\delta=-\alpha\nabla f(x_i)$:

$ f(x_{i+1})\;\le\;f(x_i)-\alpha\|\nabla f(x_i)\|^2+\tfrac{L\alpha^2}{2}\|\nabla f(x_i)\|^2\;=\;f(x_i)-\alpha\Bigl(1-\tfrac{\alpha L}{2}\Bigr)\|\nabla f(x_i)\|^2. $

The constant $c_\alpha:=\alpha(1-\tfrac{\alpha L}{2})$ is strictly positive exactly when $0<\alpha<2/L$; this is where the threshold enters the proof. (b) A nonincreasing sequence bounded below converges. (c) Summing (a) from $0$ to $T-1$ telescopes: $c_\alpha\sum_{i<T}\|\nabla f(x_i)\|^2\le f(x_0)-f(x_T)\le f(x_0)-f^\star$, uniformly in $T$; let $T\to\infty$. A convergent series has terms tending to $0$. **End of proof.**
<!-- END S89 -->

<!-- BEGIN S91 -->
### 21. Proof -- Monotone and Bounded [S91]
<!-- END S91 -->

<!-- BEGIN S92 -->
### 22. Proof -- Gradients Must Vanish [S92]
<!-- END S92 -->

<!-- BEGIN S93 -->
### 23. Reading the Theorem [S93]

**What this does *not* say.** It does not say $x_i$ converges; it does not say the limit of $f(x_i)$ is a local minimum value; it does not say any limit point is a minimizer. All three can fail without further assumptions. For $f(x)=e^{-x}$, which is not $L$-smooth globally, but the phenomenon persists for smooth examples, the iterates run to infinity with $f(x_i)$ decreasing to $0$ and $\|\nabla f(x_i)\|\to0$, and there is no minimizer at all. For a smooth function with a saddle, gradient descent started exactly on the stable manifold converges *to the saddle*, a stationary point that is not a minimum. The honest content of Theorem 7 is: **the iterates approach stationarity**. Convexity (Section 7) is what upgrades stationarity to optimality; strong convexity (Section 8) is what upgrades it to a rate.

It is worth adding that the generic-initialization caveat has a clean modern answer: Lee, Simchowitz, Jordan and Recht [11] proved that gradient descent with a small constant step converges to a saddle only from a measure-zero set of initializations. So "converges to a local minimum" is *almost surely* true for random initialization under mild conditions, but that is a theorem the lecture does not prove and should not be assumed silently.

#### 6.5 The nonconvex rate, which follows in two lines and is never stated

Part (c) of Theorem 6.2 is qualitative, but its proof already contains a quantitative bound. Since it is the single guarantee that survives into deep learning, it deserves to be written down.

**Corollary 6.3 (rate to stationarity).** Under the hypotheses of Theorem 6.2 with $\alpha=1/L$,

$ \min_{0\le i<T}\|\nabla f(x_i)\|^2\;\le\;\frac{1}{T}\sum_{i=0}^{T-1}\|\nabla f(x_i)\|^2\;\le\;\frac{2L\bigl(f(x_0)-f^\star\bigr)}{T}. $

Hence $\min_{i<T}\|\nabla f(x_i)\|\le\varepsilon$ after $T=O(\varepsilon^{-2})$ iterations.

*Proof.* With $\alpha=1/L$ we get $c_\alpha=\tfrac1L(1-\tfrac12)=\tfrac1{2L}$, and the telescoped bound of Theorem 6.2(c) reads $\tfrac{1}{2L}\sum_{i<T}\|\nabla f(x_i)\|^2\le f(x_0)-f^\star$. Divide by $T$ and use that a minimum is at most an average. **End of proof.**

No convexity, no minimizer, no $\mu$: just the descent lemma and boundedness below. This $O(1/\varepsilon^2)$ is known to be *optimal* for first-order methods on smooth nonconvex functions (Carmon, Duchi, Hinder and Sidford [12]), so unlike the convex rates of Section 7 it cannot be improved by acceleration. When people say "we have theory for nonconvex optimization," this corollary is very often all they mean.
<!-- END S93 -->

<!-- BEGIN S136 -->
### 24. S136 (new) [S136]
<!-- END S136 -->

<!-- BEGIN S137 -->
### 25. S137 (new) [S137]
<!-- END S137 -->

<!-- REGION P4c END -->

<!-- REGION P4d BEGIN -->

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

The figure draws the parabola $f(u)=u^2$, marks $y$ at $u=-1$ and $x$ at $u=3/2$, and joins them with a blue chord. At the midpoint $\theta=1/2$ (so $u=1/4$) a dashed vertical line connects the chord value $13/8$ above with the function value $1/16$ on the curve below.

The payoff is the one property the convex part of the lecture needs: a convex function has no bad local minima. The inequality is $\le$, not $\lt$, so flat pieces and many minimizers are allowed; linear functions are convex. This is not strict convexity.

**Details.**

**Local implies global.** Let $x$ be a local minimizer and suppose some $y$ has $f(y)\lt f(x)$. For every $\theta\in(0,1]$, convexity gives $f\big(x+\theta(y-x)\big)\le(1-\theta)f(x)+\theta f(y)\lt f(x)$. Taking $\theta$ small puts these points arbitrarily close to $x$, which contradicts local minimality. So no such $y$ exists.

**Strict convexity** asks for strict inequality whenever $x\ne y$ and $\theta\in(0,1)$; it rules out two distinct minimizers. The lecture never assumes it.

**Figure check.** The chord at $u=1/4$ has height $\tfrac12(1)+\tfrac12(9/4)=13/8$, and $f(1/4)=1/16$. The plot maps $X=320+130u$, $Y=280-60u^2$ (viewBox units), so the dots sit at $(352.5,182.5)$ and $(352.5,276.25)$.

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

The figure shows the parabola $f(u)=u^2$, a point $x$ at $u=-1$, and the blue tangent line there, $v=-1-2u$. The line touches the curve at $x$ and stays below it everywhere else.

**Details.**

**From the chord definition.** Fix $x,y$ and $\theta\in(0,1]$. Convexity gives $f\big(x+\theta(y-x)\big)\le(1-\theta)f(x)+\theta f(y)$. Subtract $f(x)$ and divide by $\theta\gt0$:

$$\frac{f\big(x+\theta(y-x)\big)-f(x)}{\theta}\le f(y)-f(x).$$

As $\theta\to0^+$ the left side tends to the directional derivative $\langle\nabla f(x),y-x\rangle$, which gives the tangent bound. The converse (tangent bound for all $x,y$ implies convexity) is proved in the backup note.

**Figure check.** $u^2-(-1-2u)=(u+1)^2\ge0$, with equality only at $u=-1$. With $X=320+130u$, $Y=280-60v$, the tangent runs from $(60,100)$ at $u=-2$ to $(320,340)$ at $u=0$.

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

The figure plots $f(u)=\max(|u|-1,0)^2$, which is convex and smooth and is minimized on the whole interval $[-1,1]$ (thick blue). The chosen minimizer $x^\star$ is the right end $u=1$. The iterate $x_t$ sits at $u=2.9$; a dashed vertical segment shows the gap $\Delta_t$ and a grey bracket on the axis shows the distance $\sqrt{D_t}$.

**Details.**

**Contrast with the nonconvex part.** There the guarantee used only a lower bound $f\ge f_{\text{low}}$; $f_{\text{low}}$ did not need to be attained or even to equal the infimum. Here the proof measures distance to an actual point $x^\star$, so attainment is needed.

**Example checks.** $\log(1+e^u)\gt0$ tends to $0$ as $u\to-\infty$; its second derivative is $\sigma(u)(1-\sigma(u))\le\tfrac14$ with $\sigma$ the logistic function. For the plotted $f$: it is $g(|u|-1)$ with $g(s)=\max(s,0)^2$ convex and nondecreasing, so $f$ is convex; $f'(u)=2\max(|u|-1,0)\,\mathrm{sign}(u)$ is $2$-Lipschitz. At $u=2.9$: $\Delta_t=1.9^2=3.61$ and $\sqrt{D_t}=1.9$.

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

The next six slides prove this theorem. The bound is stated for any minimizer $x^\star$; with several minimizers, use the one nearest $x_0$.

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

Two consequences are used later: the gaps are nonincreasing, $\Delta_{t+1}\le\Delta_t$ (slide 36), and each step removes at least $\|g_t\|^2/(2L)$ of gap.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S98 -->

<!-- BEGIN S99 -->
### 33. Use the Tangent at x_t [S99]

**Message.** Convexity's tangent bound at $x_t$, evaluated at $x^\star$, bounds the gap by $\langle g_t,x_t-x^\star\rangle$.

Take the tangent bound with $x=x_t$ and $y=x^\star$: $f^\star\ge f(x_t)+\langle g_t,x^\star-x_t\rangle$. Moving terms gives $\Delta_t\le\langle g_t,x_t-x^\star\rangle$.

Put this into the descent step from the previous slide:

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

$$T\Delta_T\le\sum_{t=1}^T\Delta_t\le\frac L2D_0,\qquad\text{so}\qquad f(x_T)-f^\star\le\frac{L\|x_0-x^\star\|^2}{2T}.$$

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

The recap chain, with each step labelled:

$$T\Delta_T\overset{\text{monotone}}{\le}\sum_{t=0}^{T-1}\Delta_{t+1}\overset{\text{descent+tangent}}{\le}\sum_{t=0}^{T-1}\Big(\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2\Big)\overset{\text{identity}}{=}\tfrac L2\sum_{t=0}^{T-1}(D_t-D_{t+1})\overset{\text{telescope}}{=}\tfrac L2(D_0-D_T)\le\tfrac L2D_0.$$

$O(1/T)$ is sublinear, not linear: doubling $T$ only halves the bound, and reaching gap $\varepsilon$ takes $O(1/\varepsilon)$ steps.

**Details.**

The proof uses no co-coercivity, no PL condition and no two-sided sandwich of $\nabla f$. The highlight box on the slide is the takeaway to say aloud.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
<!-- END S106 -->

<!-- REGION P4d END -->

<!-- REGION P4e BEGIN -->

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

The figure uses the running example $f=2x_1^2+\tfrac12x_2^2$ ($\mu=1$, $L=4$), restricted to the diagonal line $x=s(1,1)/\sqrt2$, where it becomes $1.25s^2$ (black). At the anchor $s=-1$ the green curve is the tangent plus $\tfrac12(s+1)^2$ (curvature $\mu=1$) and the dashed blue curve is the tangent plus $2(s+1)^2$ (curvature $L=4$). All three touch at the anchor; the green floor stays below $f$ and the blue curve stays above it.

**Details.**

**Example check.** For this quadratic $r=2h_1^2+\tfrac12h_2^2$ with $h=y-x$, and $\tfrac12\|h\|^2\le2h_1^2+\tfrac12h_2^2\le2\|h\|^2$, so $\mu=1$ and $L=4$. Along the diagonal, $f=2\cdot\tfrac{s^2}2+\tfrac12\cdot\tfrac{s^2}2=1.25s^2$, whose curvature $2.5$ lies between $1$ and $4$.

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring). The script asserts floor $\le f\le$ upper curve on a fine grid; the upper curve is clipped at the top of the plot.

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

**Iteration count.** $q^T\le e^{-\mu T/L}$ (slide 44), and $e^{-\mu T/L}D_0\le\varepsilon$ when $T\ge\tfrac L\mu\ln(D_0/\varepsilon)$.

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

$$\Delta_{t+1}\le\langle g_t,x_t-x^\star\rangle-\tfrac1{2L}\|g_t\|^2-\tfrac\mu2D_t=\tfrac L2(D_t-D_{t+1})-\tfrac\mu2D_t.$$

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

Since $x^\star$ minimizes $f$, $\Delta_{t+1}\ge0$, so the previous slide gives

$$0\le\frac L2(D_t-D_{t+1})-\frac\mu2D_t.$$

Multiply by $2/L$: $0\le D_t-D_{t+1}-\tfrac\mu LD_t$, that is $D_{t+1}\le(1-\tfrac\mu L)D_t=qD_t$. Every step shrinks the squared distance by at least the factor $q$.

**Details.**

The argument throws away the gap $\Delta_{t+1}$ and keeps only distances; that is one reason the bound can be loose (slide 47).

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

**Induction.** Base case $T=1$ is the previous slide at $t=0$. If $D_T\le q^TD_0$, then $D_{T+1}\le qD_T\le q^{T+1}D_0$; multiplying the inequality by $q$ is allowed because $q\ge0$, which holds since $\mu\le L$.

**The exponential bound.** $u\mapsto e^{-u}$ is convex with tangent $1-u$ at $u=0$, so the tangent bound gives $e^{-u}\ge1-u$. With $u=\mu/L$ and $q\ge0$, raising to the power $T$ gives $q^T\le e^{-\mu T/L}$.

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
- Our calculation.
<!-- END S122 -->

<!-- BEGIN S123 -->
### 45. Function Values Follow Distance [S123]

**Message.** Smoothness at the minimizer converts the distance bound into the function-gap bound $\Delta_T\le\tfrac L2q^TD_0$.

Use the smoothness upper bound at $x=x^\star$, where $\nabla f(x^\star)=0$, with $y=x_T$: $f(x_T)\le f^\star+\tfrac L2\|x_T-x^\star\|^2$. With the previous slide,

$$f(x_T)-f^\star\le\frac L2\|x_T-x^\star\|^2\le\frac L2q^T\|x_0-x^\star\|^2.$$

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

The figure plots the two bound shapes on a logarithmic vertical axis for $T=1,\dots,24$: grey $1/T$ and blue $(3/4)^T$, where $3/4$ is $q$ for the running example. The blue curve is a straight line falling to about $10^{-3}$ at $T=24$; the grey curve flattens near $0.04$. For $T=2$ to $6$ the blue curve is slightly higher; from $T=7$ on it is lower and the gap widens.

The plot shows bounds, not measured run times. Each iteration is the same gradient step in both settings.

**Details.**

**Error versus iteration count.** These are two readings of one bound. Error after $T$ steps: $q^T$ against $1/T$. Steps needed for error $\varepsilon$: $O(\log(1/\varepsilon))$ against $O(1/\varepsilon)$. Keep them apart: a linear rate is an error statement, and $\log(1/\varepsilon)$ is the matching iteration count.

**Plot numbers.** $(3/4)^{24}=e^{24\ln0.75}\approx e^{-6.90}\approx1.0\times10^{-3}$; $1/24\approx0.042$. Crossing: $(3/4)^6\approx0.178\gt1/6$, $(3/4)^7\approx0.133\lt1/7\approx0.143$.

Figure coordinates: `figs/o3b_figs.py` in this deck folder (exact inputs in its docstring).

**Sources.**

- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3 (Remark 3.7 on the terminology)
- Our calculation.
<!-- END S110 -->

<!-- BEGIN S126 -->
### 47. The Example Beats Its Bound [S126]

**Message.** On $f=2x_1^2+\tfrac12x_2^2$, the iterates beat the guarantee: after the first step the squared distance falls by $9/16$ per step, below the bound factor $q=3/4$.

Here $\nabla f=(4x_1,x_2)$, $L=4$, $\mu=1$, $q=3/4$, and the step $1/4$ maps $(x_1,x_2)$ to $(0,\tfrac34x_2)$. From $x_0=(2,2)$:

$x_0=(2,2)$, $D_0=8$; $x_1=(0,3/2)$, $D_1=9/4$, ratio $9/32$; $x_2=(0,9/8)$, $D_2=81/64$, ratio $9/16$. The bound $q^tD_0$ gives $8$, $6$, $9/2$.

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

<!-- BEGIN S130 -->
### 48. Part 6: Three Guarantees [S130]

**Message.** Part 6 compares the three guarantees side by side.
<!-- END S130 -->

<!-- BEGIN S131 -->
### 49. Three Assumptions, Three Guarantees [S131]

**Message.** One algorithm, three assumption levels, three guarantees: a small gradient, then an $O(1/T)$ function gap, then geometric convergence to the minimizer.

All three rows use gradient descent with step $1/L$ on an $L$-smooth $f:\mathbb{R}^n\to\mathbb{R}$.

Nonconvex, with $f\ge f_{\text{low}}$: $\min_{t\lt T}\|\nabla f(x_t)\|^2\le2L(f(x_0)-f_{\text{low}})/T$. This is stationarity only. It does not promise a local minimum: $f(u)=1-\cos u$ is $1$-smooth, and gradient descent started at $u=\pi$, a strict local maximum, never moves.

Convex, with a minimizer: $\Delta_T\le LD_0/(2T)$, a sublinear rate on the last function gap.

$\mu$-strongly convex: $D_T\le q^TD_0$ and $\Delta_T\le\tfrac L2q^TD_0$ with $q=1-\mu/L$, a linear, that is geometric, rate.

This is the lecture's one global recap; each row measures a different quantity, so compare what is guaranteed, not only the speed.

**Details.**

**Example check.** For $1-\cos u$: $f'(u)=\sin u$ is $1$-Lipschitz, $f'(\pi)=0$, $f''(\pi)=-1$.

Constants and alternative step sizes are deliberately left off the slide.

**Sources.**

- Cornell CS4787/5777, Fall 2026, Lecture 5 notes, section "Convergence of GD". https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html (checked 2026-11-23).
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.1, Theorem 3.4, eqs. (14)-(16). https://arxiv.org/abs/2301.11235v3
- Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, arXiv:2301.11235v3 (2024-03-09), Section 3.2, Theorem 3.6 and Remark 3.7. https://arxiv.org/abs/2301.11235v3
<!-- END S131 -->

<!-- BEGIN S140 -->
### 50. No Extra Conditions Needed [S140]

**Message.** The convex and strongly convex proofs need only the descent inequality, one distance identity and the tangent bound with its $\mu$ term: no co-coercivity and no PL condition.

The flow on the slide: descent inequality, then the distance identity, then the tangent bound with $-\tfrac\mu2D_t$. With $\mu=0$ the result telescopes to $O(1/T)$; with $\mu\gt0$ it contracts by $q$ each step.

The answers, explicitly. Co-coercivity of $\nabla f$: not needed. Polyak-Lojasiewicz (PL) condition: not needed. Strong convexity: kept, because it supplies the $\mu$ term that produces the contraction.

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
