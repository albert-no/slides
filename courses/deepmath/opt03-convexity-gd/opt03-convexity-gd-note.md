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

## 1 What This Lecture Actually Claims

The lecture answers one question, *when does gradient descent work, and how fast?*, by isolating the three structural assumptions that make the answer clean.

1. **Convexity** buys you that a stationary point is a global minimum. Without it, $\nabla f(x)=0$ tells you almost nothing: $x$ could be a maximum, a saddle, or a point on a flat ridge.
2. **Smoothness**, meaning an $L$-Lipschitz gradient, buys you a *quadratic upper lid* on $f$. This is what makes a fixed step size safe: it tells you how far you can trust the linear model $f(x)+\langle\nabla f(x),\delta\rangle$ before curvature can betray you. Everything about step-size choice traces back to this one lemma.
3. **Strong convexity** buys you a *quadratic lower floor*. Sandwiched between a floor and a lid, the function is within a constant factor of a quadratic, and gradient descent contracts geometrically.

The resulting three-tier picture is worth stating up front, because the rest of the lecture is just filling in the rows. Each entry below names the assumptions, the guarantee, and the number of iterations needed to reach accuracy $\varepsilon$.

- *$L$-smooth only.* Guarantee: $\min_{i<T}\|\nabla f(x_i)\|^2 \le \tfrac{2L(f(x_0)-f^\star)}{T}$ (Section 6.5). Iterations: $O(1/\varepsilon^2)$ to reach $\|\nabla f\|\le\varepsilon$.
- *$L$-smooth and convex.* Guarantee: $f(x_T)-f^\star \le \tfrac{\|x_0-x^\star\|^2}{2\alpha T}$ (Theorem 8). Iterations: $O(1/\varepsilon)$.
- *$L$-smooth and $\mu$-strongly convex.* Guarantee: $\|x_T-x^\star\|^2\le c^T\|x_0-x^\star\|^2$ with $c<1$ (Theorem 10). Iterations: $O(\kappa\log(1/\varepsilon))$.

Two honest caveats. First, *deep networks satisfy none of the convexity assumptions*; what survives into the nonconvex world is exactly the first row, plus the descent lemma, plus, where it happens to hold, the Polyak-Lojasiewicz inequality of Section 5.5, which delivers linear convergence *without* convexity. Second, the rates in rows two and three are not the best achievable by a first-order method; Section 9.1 gives the accelerated rates and the matching lower bounds, so that "$O(1/T)$" is not mistaken for "the truth about first-order optimization."

## 2 Convexity

### 2.1 Convex sets and convex functions

A set $C\subseteq\mathbb{R}^n$ is **convex** if for all $x,y\in C$ and $t\in[0,1]$ we have $tx+(1-t)y\in C$: the segment joining any two points of $C$ stays in $C$. A function $f:C\to\mathbb{R}$ on a convex domain is **convex** if

$ f\bigl(tx+(1-t)y\bigr)\;\le\;t f(x)+(1-t)f(y)\qquad\text{for all }x,y\in C,\;t\in[0,1]. \tag{2.1} $

This is the **chord** definition: the graph lies below or on every chord. It is **strictly convex** if the inequality is strict for $x\ne y$ and $t\in(0,1)$. Note that (2.1) requires *no* differentiability; it is the definition of record, and every other characterization below is a theorem relative to it.

The domain matters, and the lecture suppresses it. Convexity of $f$ is a statement about a convex domain; $f(x)=1/x$ is convex on $(0,\infty)$ and concave on $(-\infty,0)$, and the union of those two intervals is not convex, so "$1/x$ is convex" is only true once you name the domain. Throughout, when no domain is named, it is $\mathbb{R}^n$.

### 2.2 Why convexity is the right dividing line

The reason optimization theory pivots on convexity is a single proposition.

**Proposition 2.1 (local implies global).** Let $f$ be convex on a convex set $C$ and let $x^\star\in C$ be a local minimizer. Then $x^\star$ is a global minimizer. If $f$ is strictly convex, the global minimizer is unique when it exists.

*Proof.* Suppose $y\in C$ with $f(y)<f(x^\star)$. For $t\in(0,1]$ put $x_t=x^\star+t(y-x^\star)\in C$. By (2.1),

$ f(x_t)\;\le\;(1-t)f(x^\star)+t f(y)\;=\;f(x^\star)-t\bigl(f(x^\star)-f(y)\bigr)\;<\;f(x^\star). $

Since $x_t\to x^\star$ as $t\to 0^+$, every neighbourhood of $x^\star$ contains a point with strictly smaller value, contradicting local minimality. For uniqueness under strict convexity: if $x\ne y$ were both global minimizers with common value $m$, then $f\bigl(\tfrac{x+y}{2}\bigr)<\tfrac12 m+\tfrac12 m=m$, contradicting that $m$ is the minimum. **End of proof.**

This is what "no bad local minima" means, and it is the entire practical payoff of convexity. Everything else in the lecture, smoothness, strong convexity, rates, is about *speed*. Convexity is about *correctness*: it is the hypothesis under which a local search algorithm is solving the problem you asked it to solve.

A second structural fact, not in the lecture, explains why convexity interacts well with constraints: if $f$ is convex then every **sublevel set** $S_c=\{x: f(x)\le c\}$ is convex. Indeed if $f(x)\le c$ and $f(y)\le c$ then $f(tx+(1-t)y)\le tf(x)+(1-t)f(y)\le tc+(1-t)c=c$. The converse is false. Functions with all sublevel sets convex are called *quasiconvex*, and quasiconvex functions, for instance $f(x)=\sqrt{|x|}$, can have the flat plateaus and slow gradients that convexity rules out.

### 2.3 Operations that preserve convexity

The lecture verifies convexity Hessian by Hessian. In practice one almost never does that; one builds convex functions from a small kit. Each of the following is immediate from (2.1) and worth having explicitly.

- **Nonnegative combination.** If $f_1,f_2$ are convex and $a,b\ge0$, then $af_1+bf_2$ is convex.
- **Affine precomposition.** If $f$ is convex then $x\mapsto f(Ax+b)$ is convex. This is why $\theta\mapsto\tfrac12\|A\theta-B\|^2$ from the previous lecture is convex: $\|\cdot\|^2$ is convex and $\theta\mapsto A\theta-B$ is affine. *No Hessian computation needed.*
- **Pointwise supremum.** $f=\sup_{s\in S}f_s$ is convex whenever each $f_s$ is, for any index set $S$. This is how $\|x\|_\infty=\max_i|x_i|$ and the hinge loss $\max(0,1-y\hat y)$ are known to be convex.
- **Composition.** If $g$ is convex and nondecreasing and $h$ is convex, then $g\circ h$ is convex. The monotonicity hypothesis is essential: $h(x)=x^2$ is convex and $g(u)=-u$ is both convex and concave, and $g\circ h$ is concave.

Crucially, *the composition of two convex functions need not be convex*, which is precisely why a deep network, an alternating composition of affine maps and convex nonlinearities, is not convex in its parameters even though every layer is. The affine map's coefficients are themselves variables, so "affine precomposition" does not apply. Bilinearity, not the nonlinearity, is what breaks convexity.

### 2.4 First-order characterization (tangent floor)

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

### 2.5 Theorem 1: the Hessian test, proved

The lecture states Theorem 1, that for twice-differentiable $f$, convexity is equivalent to $\nabla^2 f(x)\succeq 0$ for all $x$, and moves on without proof. Since this is the test one actually applies, here it is in full. The proof technique, standard and set out in [1, Section 3.1.1], is **restriction to a line**: reduce the $n$-dimensional claim to a one-dimensional one, where Taylor's theorem is available.

**Lemma 2.4 (restriction to a line).** $f:\mathbb{R}^n\to\mathbb{R}$ is convex if and only if for every $x\in\mathbb{R}^n$ and $d\in\mathbb{R}^n$ the one-dimensional function $\varphi_{x,d}(t)=f(x+td)$ is convex on $\mathbb{R}$.

*Proof.* Forward: $t\mapsto x+td$ is affine, and convexity is preserved by affine precomposition (Section 2.3). Converse: given $u,v$ and $t\in[0,1]$, take $x=u$ and $d=v-u$; convexity of $\varphi_{u,v-u}$ at the points $0$ and $1$ gives $f(u+t(v-u))=\varphi(t)=\varphi((1-t)\cdot0+t\cdot1)\le(1-t)\varphi(0)+t\varphi(1)=(1-t)f(u)+tf(v)$. **End of proof.**

If $f$ is twice differentiable then $\varphi_{x,d}$ is twice differentiable with

$ \varphi_{x,d}'(t)=\langle\nabla f(x+td),\,d\rangle,\qquad \varphi_{x,d}''(t)=d^\top\nabla^2 f(x+td)\,d, \tag{2.3} $

by the chain rule. So the $n$-dimensional Hessian condition $\nabla^2 f\succeq0$ is *exactly* the statement that $\varphi_{x,d}''\ge0$ for every line, and Theorem 1 reduces to the scalar case.

**Lemma 2.5 (scalar case).** A twice-differentiable $\varphi:\mathbb{R}\to\mathbb{R}$ is convex if and only if $\varphi''(t)\ge0$ for all $t$.

*Proof.* Converse direction first: $\varphi''\ge0$ means $\varphi'$ is nondecreasing. Fix $s<t$. By the mean value theorem there is $\xi\in(s,t)$ with $\varphi(t)-\varphi(s)=\varphi'(\xi)(t-s)$, and since $\varphi'$ is nondecreasing, $\varphi'(s)\le\varphi'(\xi)$, so $\varphi(t)\ge\varphi(s)+\varphi'(s)(t-s)$. The same computation for $t<s$ gives the identical conclusion: both $\varphi'(\xi)\le\varphi'(s)$ and $t-s<0$ flip, and the inequality direction survives. So the one-dimensional version of (2.2) holds, and Theorem 2.2 gives convexity.

Forward direction: suppose $\varphi$ convex, so by Theorem 2.2, $\varphi(t)\ge\varphi(s)+\varphi'(s)(t-s)$ and $\varphi(s)\ge\varphi(t)+\varphi'(t)(s-t)$ for all $s,t$. Adding the two and rearranging gives $\bigl(\varphi'(t)-\varphi'(s)\bigr)(t-s)\ge0$, that is, $\varphi'$ is nondecreasing. Hence for $h>0$ we have $\bigl(\varphi'(t+h)-\varphi'(t)\bigr)/h\ge0$, and letting $h\to0^+$ yields $\varphi''(t)\ge0$. **End of proof.**

**Theorem 1 (Theorem 2.6 in this numbering).** Let $f$ be twice continuously differentiable on $\mathbb{R}^n$. Then $f$ is convex if and only if $\nabla^2 f(x)\succeq0$ for all $x$.

*Proof.* Combine the three equivalences: $f$ is convex if and only if every $\varphi_{x,d}$ is convex (Lemma 2.4), if and only if $\varphi_{x,d}''(t)\ge0$ for all $x,d,t$ (Lemma 2.5), if and only if $d^\top\nabla^2 f(y)d\ge0$ for all $y,d$ (by (2.3)), if and only if $\nabla^2 f(y)\succeq0$ for all $y$. The step from "all $x,d,t$" to "all $y,d$" uses that every $y$ is reachable as $x+td$, for instance with $t=0$ and $x=y$. **End of proof.**

**One-way warning.** $\nabla^2 f\succ0$, strictly positive definite everywhere, implies strict convexity, but *not* conversely: $f(x)=x^4$ is strictly convex on $\mathbb{R}$ with $f''(0)=0$. So the natural "strict" analogue of Theorem 1 is only an implication, and the lecture is right not to claim the equivalence. This asymmetry is exactly why strong convexity (Section 5), which *is* equivalent to a uniform Hessian bound, is the useful strengthening rather than strict convexity.

### 2.6 Running example and the standard non-example

For $f(x)=2x_1^2+\tfrac12x_2^2$ the Hessian is the constant matrix $\operatorname{diag}(4,1)$, with eigenvalues $4$ and $1$, both positive; so $f$ is convex, indeed strongly convex (Section 5). The contrasting example is the saddle $g(x)=x_1^2-x_2^2$, with $\nabla^2 g=\operatorname{diag}(2,-2)$: the eigenvalue $-2$ certifies non-convexity, and the origin is a stationary point that is a minimum along $e_1$ and a maximum along $e_2$. Along the line $x=t e_2$ the restriction is $\varphi(t)=-t^2$, which Lemma 2.4 already disqualifies; one bad line is enough. This is the concrete form of "$\nabla f(x)=0$ tells you nothing without convexity."

## 3 Smoothness

### 3.1 Two different Lipschitz conditions

Lipschitz continuity and $L$-smoothness are introduced on adjacent slides, and it is easy to conflate them. They are logically independent.

- $f$ is **$G$-Lipschitz** if $|f(x)-f(y)|\le G\|x-y\|$; equivalently, for differentiable $f$, if $\|\nabla f(x)\|\le G$ everywhere. This bounds the *slope*.
- $f$ is **$L$-smooth** if $\|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|$. This bounds the *curvature*.

Neither implies the other. $f(x)=|x|$ is $1$-Lipschitz but not $L$-smooth for any $L$, since its gradient jumps. $f(x)=x^2$ is $2$-smooth but not $G$-Lipschitz for any $G$, since its gradient is unbounded. The rest of the lecture uses only $L$-smoothness; $G$-Lipschitzness is the assumption behind *subgradient* methods, which converge at the slower rate $O(1/\sqrt{T})$ and which this lecture does not cover (Section 9.3).

Throughout, "$L$-smooth" is a statement about a specific $L$; a function that is $L$-smooth is also $L'$-smooth for any $L'\ge L$. The *smoothness constant* means the smallest such $L$, which by Theorem 3.2 below equals $\sup_x\|\nabla^2f(x)\|_2$.

### 3.2 The descent lemma (Lemma 1 of the lecture)

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

Two remarks. First, **no convexity is used**: Lemma 3.1 holds for the saddle, for a neural network, for anything with a Lipschitz gradient. This is why it is the workhorse of nonconvex analysis too (Section 6.5). Second, the *two-sided* form is genuinely two-sided: smoothness gives a lower quadratic bound as well, with the same constant but the opposite sign. The lower bound is much weaker than the strong-convexity floor of Section 5, whose constant is $+\mu$ rather than $-L$, but it is what forbids $f$ from dropping arbitrarily fast, and it is the reason $L$-smooth functions cannot have cusps pointing downward.

### 3.3 Theorem 2, proved rigorously, and its converse

The lecture states Theorem 2, that $f$ being $L$-smooth implies $\nabla^2 f(x)\preceq LI$, with a sketch, and the source file explicitly flags the rigorous version as an exercise. Here it is, in both directions, which is the more useful statement anyway because the converse is what one uses in practice: one computes $\|\nabla^2 f\|_2$ and concludes smoothness.

**Theorem 3.2.** Let $f$ be twice continuously differentiable. Then $f$ is $L$-smooth if and only if $-LI\preceq\nabla^2 f(x)\preceq LI$ for all $x$, if and only if $\|\nabla^2 f(x)\|_2\le L$ for all $x$, where $\|\cdot\|_2$ is the spectral norm. If in addition $f$ is convex, the condition collapses to the one-sided $0\preceq\nabla^2f(x)\preceq LI$ stated in the lecture.

*Proof, forward direction (the exercise).* Fix $x$ and a unit vector $d$. For $t\ne0$ apply $L$-smoothness to the pair $x+td$ and $x$:

$ \Bigl\|\frac{\nabla f(x+td)-\nabla f(x)}{t}\Bigr\|\;\le\;\frac{L\,\|td\|}{|t|}\;=\;L. $

As $t\to0$ the left-hand vector converges to the directional derivative of $\nabla f$ at $x$ along $d$, which is $\nabla^2f(x)\,d$; this is where continuity of the second derivative is used. Norms are continuous, so $\|\nabla^2 f(x)d\|\le L$ for every unit $d$, that is $\|\nabla^2 f(x)\|_2\le L$. Since $\nabla^2f(x)$ is symmetric its spectral norm is $\max_i|\lambda_i|$, so all eigenvalues lie in $[-L,L]$, which is exactly $-LI\preceq\nabla^2f(x)\preceq LI$.

*Proof, converse direction.* Suppose $\|\nabla^2 f(z)\|_2\le L$ for all $z$. Fix $x,y$ and apply the fundamental theorem of calculus to the *gradient* along the segment:

$ \nabla f(y)-\nabla f(x)\;=\;\int_0^1\nabla^2 f\bigl(x+t(y-x)\bigr)\,(y-x)\,dt. $

Taking norms and using $\|\nabla^2f(\cdot)(y-x)\|\le\|\nabla^2f(\cdot)\|_2\|y-x\|\le L\|y-x\|$ pointwise gives $\|\nabla f(y)-\nabla f(x)\|\le\int_0^1 L\|y-x\|\,dt=L\|y-x\|$. **End of proof.**

**Why the sketch is not yet a proof.** The lecture's argument divides the smoothness inequality by $\|td\|$ and passes to the limit, which is the right idea and is Step 1 above, but the honest version has to say *which* limit object appears, namely the directional derivative of the gradient map, and it has to invoke continuity of $\nabla^2f$ to identify it with $\nabla^2f(x)d$. Without $C^2$ the statement still holds almost everywhere by Rademacher's theorem, but the clean pointwise version needs the smoothness of the second derivative. This is exactly the kind of step that is easy to wave through and worth writing down once.

**Running example.** $\nabla^2f=\operatorname{diag}(4,1)$ has spectral norm $4$, so $f$ is $4$-smooth and not $L$-smooth for any $L<4$. The constant $L=4$ used throughout is the exact smoothness constant, not a loose bound. Concretely, the gradient map $x\mapsto(4x_1,x_2)$ stretches the $e_1$ direction by exactly $4$.

### 3.4 Theorem 3: the sandwich

Theorem 3 states, for $L$-smooth $f$ with a global minimizer $x^\star$,

$ \frac{1}{2L}\|\nabla f(z)\|^2\;\le\;f(z)-f(x^\star)\;\le\;\frac{L}{2}\|z-x^\star\|^2 \tag{3.2} $

for every $z$. Both halves deserve care, and the hypotheses differ between them.

*Proof of the right inequality.* Since $x^\star$ is a global minimizer of a differentiable $f$, it is in particular a local minimizer, so $\nabla f(x^\star)=0$ by Fermat's rule. Apply the *lid* of Lemma 3.1 at the base point $x^\star$ with $\delta=z-x^\star$; the inner-product term $\langle\nabla f(x^\star),z-x^\star\rangle$ is zero, so $f(z)\le f(x^\star)+\tfrac{L}{2}\|z-x^\star\|^2$. Rearrange. **End of proof.**

*Proof of the left inequality.* Fix $z$ and write $g=\nabla f(z)$; if $g=0$ the claim is trivial, so assume $g\ne0$. The lid at base point $z$ says that for every $y$,

$ f^\star\;\le\;f(y)\;\le\;f(z)+\langle g,\,y-z\rangle+\tfrac{L}{2}\|y-z\|^2. $

The first inequality is where global minimality of $x^\star$ enters: $f^\star$ is below *every* value of $f$, so we may minimize the right-hand side freely over $y$ without worrying whether the minimizer of the lid is anywhere near $x^\star$. Substituting $y=z-sg$ for $s\in\mathbb{R}$ turns the right side into the scalar quadratic

$ q(s)\;=\;f(z)-s\|g\|^2+\tfrac{L}{2}s^2\|g\|^2, $

minimized at $s=1/L$ with $q(1/L)=f(z)-\tfrac{1}{2L}\|g\|^2$. Hence $f^\star\le f(z)-\tfrac{1}{2L}\|g\|^2$, which is the left inequality. **End of proof.**

**What each half needs.** The right inequality needs $\nabla f(x^\star)=0$ and the lid, nothing else; it would hold at any stationary point, minimizer or not. The left inequality needs $f^\star$ to be a *global* lower bound; it is false if $f$ is unbounded below. Take $f(z)=-z$, which is $0$-smooth, and note the left side would claim $\|\nabla f\|^2/(2L)$ with $L=0$. **Neither half uses convexity**, which is worth stressing: the sandwich is a smoothness fact, and it is the reason the nonconvex rate of Section 6.5 exists.

**Reading.** The left inequality says a small gradient certifies near-optimality: $\|\nabla f(z)\|\le\varepsilon$ forces $f(z)-f^\star\le\varepsilon^2/(2L)$. This is the theoretical justification for the universal practice of using gradient norm as a stopping criterion. The right inequality says being close in $x$ guarantees being close in $f$: the value cannot blow up faster than quadratically as you leave the optimum.

**Numerical check, verified.** At $z=(2,2)$: $f(z)=2\cdot4+\tfrac12\cdot4=10$, $\nabla f(z)=(8,2)$, and $\|\nabla f(z)\|^2=64+4=68$. The left bound is $68/(2\cdot4)=8.5$; the right bound is $\tfrac42\|(2,2)\|^2=2\cdot8=16$. So $8.5\le 10\le16$: both inequalities hold with room to spare, and neither is tight, because the running example's curvature is $4$ in one direction and only $1$ in the other while $L=4$ is used for both.

## 4 Smooth and Convex: Co-coercivity

### 4.1 Statement

Lemma 2 of the lecture combines the two hypotheses and extracts two inequalities. For $f$ convex and $L$-smooth, and all $x,y$:

(i) $ f(y)\;\ge\;f(x)+\langle\nabla f(x),y-x\rangle+\frac{1}{2L}\|\nabla f(y)-\nabla f(x)\|^2. \tag{4.1} $

(ii) $ \bigl\langle \nabla f(x)-\nabla f(y),\,x-y\bigr\rangle\;\ge\;\frac{1}{L}\bigl\|\nabla f(x)-\nabla f(y)\bigr\|^2. \tag{4.2} $

Statement (ii) is called **co-coercivity** of the gradient; equivalently, $\nabla f$ is a $\tfrac1L$-cocoercive operator. It is strictly stronger than the plain monotonicity $\langle\nabla f(x)-\nabla f(y),x-y\rangle\ge0$ that convexity alone provides, and it is the exact inequality that makes the $O(1/T)$ rate work.

### 4.2 Proof of (i): the tilt trick

*Proof.* Fix $x$ and define the **tilted function**

$ g_x(z)\;=\;f(z)-\langle\nabla f(x),\,z\rangle. $

Three observations. (a) $g_x$ is convex, being $f$ minus a linear function. (b) $g_x$ is $L$-smooth, because $\nabla g_x(z)=\nabla f(z)-\nabla f(x)$ differs from $\nabla f$ by a constant, which does not change Lipschitz constants. (c) $\nabla g_x(x)=0$, so by Corollary 2.3 and convexity, $x$ is a *global minimizer* of $g_x$: this is the whole point of the tilt. The linear term was chosen precisely to move the minimum to $x$.

Now apply the left half of the sandwich (3.2) to $g_x$ at the point $z=y$, with minimizer $x$:

$ \frac{1}{2L}\|\nabla g_x(y)\|^2\;\le\;g_x(y)-g_x(x). $

Substituting the definitions, $\nabla g_x(y)=\nabla f(y)-\nabla f(x)$ and

$ g_x(y)-g_x(x)\;=\;f(y)-\langle\nabla f(x),y\rangle-f(x)+\langle\nabla f(x),x\rangle\;=\;f(y)-f(x)-\langle\nabla f(x),y-x\rangle, $

which rearranges to exactly (4.1). **End of proof.**

Note what (4.1) improves on: the plain tangent floor (2.2) says $f(y)-f(x)-\langle\nabla f(x),y-x\rangle\ge0$. Smoothness upgrades the $0$ to a positive quantity that measures how much the gradient moved. The chain of implications is worth tracking: convexity gives the tilt a global minimum, smoothness gives the sandwich, and the composition of the two gives a strictly better floor than either alone.

### 4.3 Proof of (ii)

*Proof.* Write (4.1) twice, once as stated and once with $x$ and $y$ exchanged:

$ f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\tfrac{1}{2L}\|\nabla f(y)-\nabla f(x)\|^2, $

$ f(x)\ge f(y)+\langle\nabla f(y),x-y\rangle+\tfrac{1}{2L}\|\nabla f(x)-\nabla f(y)\|^2. $

Add them. The $f(x)$ and $f(y)$ terms cancel completely, leaving

$ 0\;\ge\;\langle\nabla f(x)-\nabla f(y),\,y-x\rangle+\tfrac{1}{L}\|\nabla f(x)-\nabla f(y)\|^2, $

where the two inner products combined because $\langle\nabla f(x),y-x\rangle+\langle\nabla f(y),x-y\rangle=\langle\nabla f(x)-\nabla f(y),y-x\rangle$. Moving the inner product to the left and flipping its sign gives (4.2). **End of proof.**

The "write it twice and add" move here is the same one used in Lemma 2.5 and in the monotonicity proofs of Section 5.6. Whenever a symmetric conclusion is wanted from an asymmetric hypothesis, this is the move.

### 4.4 The equivalence the lecture does not state

Co-coercivity is not merely a consequence of "convex and smooth"; for convex $f$ it is *equivalent* to it. This is the **Baillon-Haddad theorem** [7]: for a convex differentiable $f$, the following five conditions are equivalent.

1. $\nabla f$ is $L$-Lipschitz.
2. $f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\tfrac{L}{2}\|y-x\|^2$ for all $x,y$, the lid.
3. $f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\tfrac{1}{2L}\|\nabla f(y)-\nabla f(x)\|^2$, that is (4.1).
4. $\langle\nabla f(x)-\nabla f(y),x-y\rangle\ge\tfrac1L\|\nabla f(x)-\nabla f(y)\|^2$, that is (4.2).
5. $\langle\nabla f(x)-\nabla f(y),x-y\rangle\le L\|x-y\|^2$.

We proved 1 implies 2 implies 3 implies 4 above. The loop closes because 4 implies 1 by Cauchy-Schwarz: writing $\Delta g=\nabla f(x)-\nabla f(y)$ and $\Delta x=x-y$, the chain $\tfrac1L\|\Delta g\|^2\le\langle\Delta g,\Delta x\rangle\le\|\Delta g\|\,\|\Delta x\|$ gives $\|\Delta g\|\le L\|\Delta x\|$. That one-line closure is worth noticing: co-coercivity looks much stronger than Lipschitzness, and for *general* operators it is, but convexity makes them the same condition. Convexity is doing real work here.

**Numerical check, verified.** With $x=(2,2)$ and $y=0$: $\nabla f(x)-\nabla f(y)=(8,2)-(0,0)=(8,2)$ and $x-y=(2,2)$. Left side of (4.2): $\langle(8,2),(2,2)\rangle=16+4=20$. Right side: $\tfrac14\cdot68=17$. So $20\ge17$. Checked. The slack is again the anisotropy $\mu=1$ against $L=4$: co-coercivity is tight only along the maximal-curvature direction, and here the displacement has equal components in both directions.

## 5 Strong Convexity

### 5.1 Definition and equivalent forms

$f$ is **$\mu$-strongly convex** (with $\mu>0$) if

$ f(y)\;\ge\;f(x)+\langle\nabla f(x),\,y-x\rangle+\frac{\mu}{2}\|y-x\|^2\qquad\text{for all }x,y. \tag{5.1} $

Compare the tangent floor (2.2): convexity puts the graph above the tangent *plane*; strong convexity puts it above a tangent *paraboloid* of curvature $\mu$. Equivalently, and this is the formulation that makes several proofs trivial, $f$ is $\mu$-strongly convex if and only if

$ h(x)\;:=\;f(x)-\tfrac{\mu}{2}\|x\|^2\quad\text{is convex.} \tag{5.2} $

*Proof that (5.1) and (5.2) are equivalent.* We have $\nabla h(x)=\nabla f(x)-\mu x$. Apply the first-order characterization (Theorem 2.2) to $h$: $h$ is convex if and only if $h(y)\ge h(x)+\langle\nabla f(x)-\mu x,\,y-x\rangle$ for all $x,y$, that is,

$ f(y)-\tfrac\mu2\|y\|^2\;\ge\;f(x)-\tfrac\mu2\|x\|^2+\langle\nabla f(x),y-x\rangle-\mu\langle x,y-x\rangle. $

Collect the quadratic terms: $-\tfrac\mu2\|y\|^2+\tfrac\mu2\|x\|^2+\mu\langle x,y-x\rangle=-\tfrac\mu2\bigl(\|y\|^2-2\langle x,y\rangle+\|x\|^2\bigr)=-\tfrac\mu2\|y-x\|^2$, and moving it across gives exactly (5.1). **End of proof.**

Strong convexity is a strictly stronger condition than strict convexity: $f(x)=x^4$ is strictly convex but not $\mu$-strongly convex for any $\mu>0$, since near the origin its curvature vanishes, so no fixed paraboloid fits underneath. It is also stronger than convexity by a quantitative margin, and that margin is precisely what turns the $O(1/T)$ rate into a linear one.

Note also that a $\mu$-strongly convex, $L$-smooth function necessarily has $\mu\le L$: inequality (5.1) and the lid of Lemma 3.1 sandwich the quantity $f(y)-f(x)-\langle\nabla f(x),y-x\rangle$ between $\tfrac\mu2\|y-x\|^2$ and $\tfrac L2\|y-x\|^2$, so $\mu\le L$. The ratio $\kappa=L/\mu\ge1$ is the **condition number** and it governs everything in Section 8.

### 5.2 Theorem 4, proved

The lecture asserts Theorem 4, that a twice-differentiable $f$ is $\mu$-strongly convex if and only if $\nabla^2f\succeq\mu I$, without proof. Given Section 2.5 and (5.2) it is now a two-line corollary.

**Theorem 4 (Theorem 5.1 in this numbering).** For $f\in C^2$: $f$ is $\mu$-strongly convex if and only if $\nabla^2 f(x)\succeq\mu I$ for all $x$.

*Proof.* By (5.2), $f$ is $\mu$-strongly convex if and only if $h=f-\tfrac\mu2\|\cdot\|^2$ is convex. Since the Hessian of $\tfrac\mu2\|x\|^2$ is $\mu I$, we have $\nabla^2h(x)=\nabla^2f(x)-\mu I$, and $h\in C^2$. Theorem 2.6 applied to $h$ says $h$ is convex if and only if $\nabla^2h(x)\succeq0$ for all $x$, that is $\nabla^2f(x)\succeq\mu I$. **End of proof.**

Concretely, $\nabla^2f(x)\succeq\mu I$ means the smallest eigenvalue of the Hessian is at least $\mu$ everywhere. For the running example $\nabla^2f=\operatorname{diag}(4,1)$ has smallest eigenvalue $1$, so $\mu=1$ is the exact strong-convexity constant, matching the lecture. Together with $L=4$ from Section 3.3, this gives $\kappa=4$: the running example is mildly ill-conditioned, enough to make the anisotropy visible in the iterate list of Section 6.3 without obscuring the pattern.

### 5.3 Existence and uniqueness of $x^\star$, an assumption the lecture leaves implicit

Every theorem from Section 6 onward writes $x^\star$ as though it obviously exists and is unique. For a merely convex $f$ neither is automatic: $f(x)=e^{-x}$ has no minimizer, and $f(x)=0$ has a continuum of them. Under strong convexity both are guaranteed, and the proof is short enough that there is no reason to leave it out.

**Proposition 5.2.** A $\mu$-strongly convex differentiable $f:\mathbb{R}^n\to\mathbb{R}$ has exactly one global minimizer $x^\star$, and it satisfies the **quadratic growth** bound

$ f(x)-f^\star\;\ge\;\frac{\mu}{2}\|x-x^\star\|^2\qquad\text{for all }x. \tag{5.3} $

*Proof, existence.* Apply (5.1) with $x=0$ fixed: $f(y)\ge f(0)+\langle\nabla f(0),y\rangle+\tfrac\mu2\|y\|^2\ge f(0)-\|\nabla f(0)\|\,\|y\|+\tfrac\mu2\|y\|^2$, which tends to $+\infty$ as $\|y\|\to\infty$. So $f$ is coercive, and its sublevel set $S=\{y:f(y)\le f(0)\}$ is bounded; it is closed by continuity, hence compact, and nonempty since $0\in S$. A continuous function on a compact set attains its minimum, at some $x^\star\in S$, and by construction $f(x^\star)\le f(0)\le f(y)$ for every $y\notin S$, so $x^\star$ is a global minimizer.

*Proof, uniqueness and (5.3).* At a minimizer $\nabla f(x^\star)=0$, so (5.1) with $x=x^\star$ reads $f(y)\ge f^\star+\tfrac\mu2\|y-x^\star\|^2$, which is (5.3). If $y$ is also a minimizer then the left side equals $f^\star$, forcing $\|y-x^\star\|=0$. **End of proof.**

Inequality (5.3) is the mirror image of the sandwich's right half (3.2): smoothness caps the value gap by $\tfrac L2\|x-x^\star\|^2$, strong convexity floors it by $\tfrac\mu2\|x-x^\star\|^2$. Together,

$ \frac{\mu}{2}\|x-x^\star\|^2\;\le\;f(x)-f^\star\;\le\;\frac{L}{2}\|x-x^\star\|^2, $

so distance-to-optimum and value gap are equivalent measures of progress up to the factor $\kappa$. This is why the theorem of Section 8 can be stated in distance and that of Section 7 in value without the two being different results.

### 5.4 What strong convexity buys, geometrically

Under both hypotheses, $f$ is trapped between two paraboloids of curvature $\mu$ and $L$ anchored at every point of its graph. That is a very rigid picture: the function is a quadratic up to a factor $\kappa$ in curvature. Gradient descent is exactly optimal on an isotropic quadratic, where $\kappa=1$ and one step with $\alpha=1/L$ reaches the minimum, and $\kappa$ measures how far a problem is from that ideal. All of the preconditioning, feature-normalization and adaptive-step-size machinery of practical deep learning is, in this language, an attempt to reduce an effective $\kappa$.

### 5.5 Lemma 3: the Polyak-Lojasiewicz inequality

**Lemma 5.3 (PL).** If $f$ is $\mu$-strongly convex with minimum value $f^\star$, then

$ \|\nabla f(x)\|^2\;\ge\;2\mu\bigl(f(x)-f^\star\bigr)\qquad\text{for all }x. \tag{5.4} $

*Proof.* Minimize both sides of (5.1) over $y$, holding $x$ fixed. The left side has minimum $f^\star$. The right side is a quadratic in $y$, namely $\psi(y)=f(x)+\langle\nabla f(x),y-x\rangle+\tfrac\mu2\|y-x\|^2$, whose gradient $\nabla\psi(y)=\nabla f(x)+\mu(y-x)$ vanishes at $y=x-\tfrac1\mu\nabla f(x)$, giving

$ \min_y\psi(y)\;=\;f(x)-\tfrac1\mu\|\nabla f(x)\|^2+\tfrac{\mu}{2}\cdot\tfrac{1}{\mu^2}\|\nabla f(x)\|^2\;=\;f(x)-\frac{1}{2\mu}\|\nabla f(x)\|^2. $

Since (5.1) holds for every $y$, in particular $f^\star=\min_y f(y)\ge\min_y\psi(y)$, that is $f^\star\ge f(x)-\tfrac{1}{2\mu}\|\nabla f(x)\|^2$. Rearranging gives (5.4). **End of proof.**

Compare with the left half of the sandwich (3.2), which reads $\|\nabla f(x)\|^2\le 2L(f(x)-f^\star)$. So under both hypotheses,

$ 2\mu\bigl(f(x)-f^\star\bigr)\;\le\;\|\nabla f(x)\|^2\;\le\;2L\bigl(f(x)-f^\star\bigr), $

a two-sided identification of gradient magnitude with value gap. The upper bound is the "a small gradient means you are nearly done" direction; the PL lower bound is the "if you are not done, the gradient is not small" direction, and it is the latter that forbids the long flat plateaus on which gradient descent stalls.

**Verification on the running example.** $\|\nabla f(x)\|^2=16x_1^2+x_2^2$ and $2\mu(f(x)-f^\star)=2\cdot1\cdot(2x_1^2+\tfrac12x_2^2)=4x_1^2+x_2^2$. Since $16x_1^2\ge4x_1^2$, inequality (5.4) holds, with equality exactly on the $x_2$-axis, the direction of minimal curvature, which is where $\mu$ is attained.

**PL is strictly weaker than strong convexity, and this matters.** The lecture derives PL *from* strong convexity, which can leave the impression that it is a mere corollary. It is not: (5.4) can hold for functions that are not convex at all. Karimi, Nutini and Schmidt [8] give the example $f(x)=x^2+3\sin^2 x$ on $\mathbb{R}$, which satisfies PL with $\mu=1/32$ yet is plainly nonconvex. What PL does give, without convexity:

- **Every stationary point is a global minimum.** If $\nabla f(x)=0$ then (5.4) forces $f(x)-f^\star\le0$. So PL rules out the spurious local minima and saddles that make nonconvex optimization hard, without requiring convexity.
- **Linear convergence of gradient descent**, at rate $(1-\mu/L)$ with $\alpha=1/L$; the lecture derives this as the bonus at the close, and Section 8.5 records it here.

PL is therefore the natural weakest hypothesis under which the fast rate survives, and it is the entry point into the literature on why over-parameterized networks sometimes train as if they were convex. The inequality goes back to Polyak [9] and, in a more general form with exponents, to Lojasiewicz [10], both in 1963; its revival for machine learning is due to [8].

### 5.6 Theorems 5 and 6: monotonicity of the gradient

Theorems 5 and 6 of the lecture state that convexity makes $\nabla f$ a monotone operator and strong convexity makes it strongly monotone. Both proofs are the "write it twice and add" move of Section 4.3.

**Theorem 5.4.** $f$ convex and differentiable if and only if $\langle\nabla f(x)-\nabla f(y),\,x-y\rangle\ge0$ for all $x,y$. And $f$ is $\mu$-strongly convex if and only if $\langle\nabla f(x)-\nabla f(y),\,x-y\rangle\ge\mu\|x-y\|^2$ for all $x,y$.

*Proof, forward direction, strong case.* Write (5.1) twice, swapping $x$ and $y$:

$ f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle+\tfrac\mu2\|y-x\|^2,\qquad f(x)\ge f(y)+\langle\nabla f(y),x-y\rangle+\tfrac\mu2\|x-y\|^2. $

Add; $f(x)$ and $f(y)$ cancel, leaving $0\ge\langle\nabla f(x)-\nabla f(y),\,y-x\rangle+\mu\|x-y\|^2$, which is the claim. The convex case is identical with $\mu=0$.

*Proof, converse direction, convex case.* Fix $x,y$ and let $\varphi(t)=f(x+t(y-x))$, so $\varphi'(t)=\langle\nabla f(x+t(y-x)),y-x\rangle$. For $s<t$, monotonicity applied to the points $x+t(y-x)$ and $x+s(y-x)$, whose difference is $(t-s)(y-x)$, gives $\bigl(\varphi'(t)-\varphi'(s)\bigr)(t-s)\ge0$, so $\varphi'$ is nondecreasing, so $\varphi$ is convex by Lemma 2.5, which needs only that $\varphi'$ is nondecreasing, not that $\varphi''$ exists. Lemma 2.4 lifts this to convexity of $f$. The strong case follows by applying this to $h=f-\tfrac\mu2\|\cdot\|^2$, whose gradient difference is $\nabla f(x)-\nabla f(y)-\mu(x-y)$. **End of proof.**

The operator-theoretic reading is worth a sentence, because it is how the convex-optimization literature is organized. Minimizing a convex $f$ is the problem $0\in\nabla f(x)$, that is, finding a zero of a monotone operator; gradient descent is one instance of a family of fixed-point iterations for monotone operators, and strong monotonicity is exactly the condition making the associated map a contraction. Everything in Section 8 is a contraction-mapping argument in disguise.

## 6 Gradient Descent

### 6.1 The algorithm and where it comes from

Gradient descent is $x_{i+1}=x_i-\alpha\nabla f(x_i)$, the method Cauchy proposed in a two-page note of 1847 [6], for solving systems of equations rather than for machine learning. The lecture presents the step as "move downhill"; the descent lemma gives the sharper derivation, and it is worth writing out because it explains the specific constant $1/L$ that appears everywhere. Minimizing the **lid** from Lemma 3.1 over the next iterate,

$ x_{i+1}\;=\;\arg\min_{y}\;\Bigl\{f(x_i)+\langle\nabla f(x_i),\,y-x_i\rangle+\frac{1}{2\alpha}\|y-x_i\|^2\Bigr\}\;=\;x_i-\alpha\nabla f(x_i), $

by setting the gradient of the quadratic to zero. So gradient descent *is* the exact minimization of a local quadratic model of $f$, with $1/\alpha$ playing the role of assumed curvature. Choosing $\alpha=1/L$ means "trust the model with the worst-case curvature"; choosing $\alpha$ larger means assuming less curvature than $f$ may actually have, which is exactly how divergence happens.

### 6.2 The exact story on a quadratic: the cliff at $2/L$ is sharp

Theorem 7 of the lecture says gradient descent behaves well for $\alpha\in(0,2/L)$, and the numerical example shows blow-up at $\alpha=0.6>2/L=0.5$. That is suggestive but it is one example; the following exact analysis, which the lecture omits, shows the threshold is a theorem and not a coincidence.

**Proposition 6.1 (exact quadratic analysis).** Let $f(x)=\tfrac12 x^\top Q x$ with $Q$ symmetric positive definite, with eigenvalues $0<\mu=\lambda_n\le\dots\le\lambda_1=L$. Then gradient descent from $x_0$ satisfies $x_i=(I-\alpha Q)^i x_0$, and $x_i\to0$ for every $x_0$ *if and only if* $|1-\alpha\lambda|<1$ for every eigenvalue $\lambda$, that is, if and only if

$ 0\;<\;\alpha\;<\;\frac{2}{L}. $

Moreover the asymptotic contraction factor per step is $\rho(\alpha)=\max_j|1-\alpha\lambda_j|=\max\{|1-\alpha\mu|,\,|1-\alpha L|\}$, minimized at $\alpha^\star=\dfrac{2}{\mu+L}$ with $\rho(\alpha^\star)=\dfrac{L-\mu}{L+\mu}=\dfrac{\kappa-1}{\kappa+1}$.

*Proof.* Here $\nabla f(x)=Qx$, so $x_{i+1}=x_i-\alpha Qx_i=(I-\alpha Q)x_i$ and the closed form follows by induction. Diagonalize $Q=U\Lambda U^\top$; in the eigenbasis the iteration decouples into $n$ scalar recursions $z_j^{(i+1)}=(1-\alpha\lambda_j)z_j^{(i)}$, each converging to $0$ from every start if and only if $|1-\alpha\lambda_j|<1$, that is $0<\alpha<2/\lambda_j$. Requiring this for all $j$ gives $\alpha<2/\lambda_1=2/L$. For the rate: the map $\alpha\mapsto|1-\alpha\mu|$ is decreasing then increasing with minimum at $1/\mu$, and $\alpha\mapsto|1-\alpha L|$ likewise at $1/L\le1/\mu$; on the relevant range the maximum is $1-\alpha\mu$ (decreasing) versus $\alpha L-1$ (increasing), and the minimum of the maximum is where they cross, so $1-\alpha\mu=\alpha L-1$ and $\alpha=\tfrac{2}{\mu+L}$, giving the stated value. **End of proof.**

So on quadratics the picture is complete and exact: convergence for $\alpha<2/L$, divergence for $\alpha>2/L$, oscillation without decay at $\alpha=2/L$ exactly. Since quadratics are a special case of "$\mu$-strongly convex and $L$-smooth", the $2/L$ threshold in Theorem 7 cannot be improved for the general class. The proof is not being lossy; the geometry really does forbid larger steps.

**The step-size comparison, re-derived.** For the running example $Q=\operatorname{diag}(4,1)$, the per-coordinate contraction factors are $1-4\alpha$ for $x_1$ and $1-\alpha$ for $x_2$. Five step sizes, each given as: $\alpha$; the factor $1-4\alpha$ on $x_1$; the factor $1-\alpha$ on $x_2$; then the behaviour.

- $\alpha=0.25=1/L$; factors $0$ and $0.75$: $x_1$ solved in one step, $x_2$ decays at $0.75$.
- $\alpha=0.4=2/(\mu+L)$; factors $-0.6$ and $0.6$: optimal, both magnitudes equal $0.6$.
- $\alpha=0.45$; factors $-0.8$ and $0.55$: converges, oscillating in $x_1$.
- $\alpha=0.5=2/L$; factors $-1$ and $0.5$: $x_1$ oscillates forever, never decays.
- $\alpha=0.6$; factors $-1.4$ and $0.4$: diverges, with $x_1$ running $2\to-2.8\to3.92\to-5.488\to\cdots$.

Every number here matches the lecture. The row at $\alpha=0.4$ is the one the lecture does not show, and it is the interesting one: the optimal step balances the two error modes so that both contract at the same rate $0.6$, which is exactly $\tfrac{\kappa-1}{\kappa+1}=\tfrac{3}{5}$. It also explains why $\alpha=1/L$, the safe choice used in most of the lecture's proofs, is *not* optimal here: it wastes the $x_1$ coordinate's already-finished progress on a conservative step for $x_2$.

### 6.3 The iterate sequence, verified

With $\alpha=1/4$ and $x_0=(2,2)$ the recursions are $x_1^{(i+1)}=(1-1)x_1^{(i)}=0$ and $x_2^{(i+1)}=0.75\,x_2^{(i)}$. Five iterations, each given as: index $i$; the iterate $x_i$; the value $f(x_i)$; the squared distance $\|x_i-x^\star\|^2$.

- $i=0$; $x_0=(2,\,2)$; $f=10$; squared distance $8$.
- $i=1$; $x_1=(0,\,1.5)$; $f=1.125$; squared distance $2.25$.
- $i=2$; $x_2=(0,\,1.125)$; $f=0.6328$; squared distance $1.2656$.
- $i=3$; $x_3=(0,\,0.8438)$; $f=0.3560$; squared distance $0.7119$.
- $i=4$; $x_4=(0,\,0.6328)$; $f=0.2002$; squared distance $0.4004$.

All values check: $f=\tfrac12x_2^2$ once $x_1=0$, and the ratio of consecutive values of $f$, and of consecutive squared distances, is $0.75^2=0.5625$ from step 1 onward. The single large drop from $i=0$ to $i=1$ is the $x_1$ coordinate being annihilated exactly; everything after is the slow $x_2$ mode, whose rate $0.75=1-\alpha\mu$ is what the theory predicts.

### 6.4 Theorem 7, stated honestly

The lecture source phrases Theorem 7 as "gradient descent converges to the local minimum" for $\alpha\in(0,2/L)$. That overstates what the proof delivers, and the presentation already softens it. For the record, here is what is actually true under $L$-smoothness alone, with no convexity, and what is not.

**Theorem 6.2.** Let $f$ be $L$-smooth and bounded below by $f^\star$, and let $0<\alpha<2/L$. Then gradient descent satisfies:

(a) $f(x_{i+1})\le f(x_i)-\alpha\bigl(1-\tfrac{\alpha L}{2}\bigr)\|\nabla f(x_i)\|^2$, so $f(x_i)$ is nonincreasing;

(b) $f(x_i)$ converges to some limit that is at least $f^\star$;

(c) $\sum_{i=0}^{\infty}\|\nabla f(x_i)\|^2<\infty$, hence $\|\nabla f(x_i)\|\to0$.

*Proof.* (a) Apply the lid of Lemma 3.1 with $x=x_i$ and $\delta=-\alpha\nabla f(x_i)$:

$ f(x_{i+1})\;\le\;f(x_i)-\alpha\|\nabla f(x_i)\|^2+\tfrac{L\alpha^2}{2}\|\nabla f(x_i)\|^2\;=\;f(x_i)-\alpha\Bigl(1-\tfrac{\alpha L}{2}\Bigr)\|\nabla f(x_i)\|^2. $

The constant $c_\alpha:=\alpha(1-\tfrac{\alpha L}{2})$ is strictly positive exactly when $0<\alpha<2/L$; this is where the threshold enters the proof. (b) A nonincreasing sequence bounded below converges. (c) Summing (a) from $0$ to $T-1$ telescopes: $c_\alpha\sum_{i<T}\|\nabla f(x_i)\|^2\le f(x_0)-f(x_T)\le f(x_0)-f^\star$, uniformly in $T$; let $T\to\infty$. A convergent series has terms tending to $0$. **End of proof.**

**What this does *not* say.** It does not say $x_i$ converges; it does not say the limit of $f(x_i)$ is a local minimum value; it does not say any limit point is a minimizer. All three can fail without further assumptions. For $f(x)=e^{-x}$, which is not $L$-smooth globally, but the phenomenon persists for smooth examples, the iterates run to infinity with $f(x_i)$ decreasing to $0$ and $\|\nabla f(x_i)\|\to0$, and there is no minimizer at all. For a smooth function with a saddle, gradient descent started exactly on the stable manifold converges *to the saddle*, a stationary point that is not a minimum. The honest content of Theorem 7 is: **the iterates approach stationarity**. Convexity (Section 7) is what upgrades stationarity to optimality; strong convexity (Section 8) is what upgrades it to a rate.

It is worth adding that the generic-initialization caveat has a clean modern answer: Lee, Simchowitz, Jordan and Recht [11] proved that gradient descent with a small constant step converges to a saddle only from a measure-zero set of initializations. So "converges to a local minimum" is *almost surely* true for random initialization under mild conditions, but that is a theorem the lecture does not prove and should not be assumed silently.

### 6.5 The nonconvex rate, which follows in two lines and is never stated

Part (c) of Theorem 6.2 is qualitative, but its proof already contains a quantitative bound. Since it is the single guarantee that survives into deep learning, it deserves to be written down.

**Corollary 6.3 (rate to stationarity).** Under the hypotheses of Theorem 6.2 with $\alpha=1/L$,

$ \min_{0\le i<T}\|\nabla f(x_i)\|^2\;\le\;\frac{1}{T}\sum_{i=0}^{T-1}\|\nabla f(x_i)\|^2\;\le\;\frac{2L\bigl(f(x_0)-f^\star\bigr)}{T}. $

Hence $\min_{i<T}\|\nabla f(x_i)\|\le\varepsilon$ after $T=O(\varepsilon^{-2})$ iterations.

*Proof.* With $\alpha=1/L$ we get $c_\alpha=\tfrac1L(1-\tfrac12)=\tfrac1{2L}$, and the telescoped bound of Theorem 6.2(c) reads $\tfrac{1}{2L}\sum_{i<T}\|\nabla f(x_i)\|^2\le f(x_0)-f^\star$. Divide by $T$ and use that a minimum is at most an average. **End of proof.**

No convexity, no minimizer, no $\mu$: just the descent lemma and boundedness below. This $O(1/\varepsilon^2)$ is known to be *optimal* for first-order methods on smooth nonconvex functions (Carmon, Duchi, Hinder and Sidford [12]), so unlike the convex rates of Section 7 it cannot be improved by acceleration. When people say "we have theory for nonconvex optimization," this corollary is very often all they mean.

## 7 Rate I: $O(1/T)$ for Smooth Convex $f$

### 7.1 Theorem 8, proved

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

Step 5 is worth pausing on. The telescoping in Step 4 naturally bounds the *sum*, which controls the *average* or the *best* iterate; getting the bound for the *last* iterate $x_T$ requires the monotonicity from Step 1. In stochastic gradient descent, where per-step monotonicity fails, this is exactly why guarantees are stated for the averaged iterate $\bar x_T=\tfrac1T\sum x_i$, a point the next lecture returns to.

### 7.2 Reading the bound

Rearranged: to reach $f(x_T)-f^\star\le\varepsilon$ it suffices to take $T\ge\dfrac{\|x_0-x^\star\|^2}{2\alpha\varepsilon}$, that is, $O(1/\varepsilon)$ iterations. With the standard choice $\alpha=1/L$ this is $T\ge\dfrac{L\|x_0-x^\star\|^2}{2\varepsilon}$: the iteration count is proportional to the smoothness constant and to the squared initial distance, and inversely proportional to the target accuracy. Note there is *no* $\mu$ and no logarithm; for merely convex $f$, one extra digit of accuracy costs a factor of $10$ in iterations, not a constant additive amount. That gap between $1/\varepsilon$ and $\log(1/\varepsilon)$ is the entire point of Section 8.

**Numerical check, verified.** Running example, $\alpha=1/4$, $x_0=(2,2)$, so $\|x_0-x^\star\|^2=8$ and the bound is $8/(2\cdot\tfrac14\cdot T)=16/T$. To get $\varepsilon=0.01$ the theorem demands $T\ge1600$. Against the actual values from Section 6.3, given as: $T$; the bound $16/T$; the actual gap $f(x_T)-f^\star$; the ratio between them.

- $T=1$; bound $16$; actual $1.125$; ratio about $14$ times.
- $T=2$; bound $8$; actual $0.6328$; ratio about $13$ times.
- $T=4$; bound $4$; actual $0.2002$; ratio about $20$ times.

The bound is correct but loose by more than an order of magnitude, and the looseness *grows*, because the true behaviour here is geometric, not $1/T$. That is not a defect of the proof; it is the price of discarding the strong convexity that this example happens to have. Theorem 8 is stated for all convex smooth $f$, including ones with $\mu=0$ for which $1/T$ is essentially the truth.

### 7.3 Is $O(1/T)$ tight?

Two separate questions, and the lecture conflates them by silence.

- **For gradient descent itself: essentially yes.** Drori and Teboulle [13] computed the exact worst case over all $L$-smooth convex $f$ and showed the sharp constant is $f(x_T)-f^\star\le\dfrac{L\|x_0-x^\star\|^2}{4T+2}$, attained by a specific piecewise-quadratic function. So (7.1) with $\alpha=1/L$ is off by only a factor of about $2$; the $1/T$ order cannot be improved for this algorithm. A streamlined derivation of both this rate and Theorem 10 is in Bubeck [4, Sections 3.2 to 3.4].
- **For first-order methods in general: no.** Nesterov's accelerated gradient method [14] attains $O(1/T^2)$ using only gradients, and Nemirovski and Yudin's lower bound [15] shows $\Omega(1/T^2)$ is optimal. Section 9.1 says more.

### 7.4 Fejer monotonicity: the iterates converge, not just the values

Theorem 8 bounds $f(x_T)-f^\star$ but says nothing about $x_T$ itself. Its proof already contains the missing piece, and it costs one line to extract.

**Proposition 7.2.** Under the hypotheses of Theorem 7.1, $\|x_{i+1}-x^\star\|\le\|x_i-x^\star\|$ for every minimizer $x^\star$ and every $i$, so the iterates are **Fejer monotone** with respect to the solution set, and $x_i$ converges to some minimizer of $f$.

*Proof.* The left side of (7.2) is $f(x_{i+1})-f^\star\ge0$, so the right side is too, giving $\|x_{i+1}-x^\star\|^2\le\|x_i-x^\star\|^2$. Consequently the sequence $(x_i)$ is bounded, so it has limit points; by Theorem 7.1, $f(x_i)\to f^\star$, so by continuity every limit point $\bar x$ satisfies $f(\bar x)=f^\star$ and is therefore a minimizer. Fejer monotonicity applied to that particular $\bar x$ makes $\|x_i-\bar x\|$ nonincreasing; since a subsequence tends to $0$, the whole sequence does. **End of proof.**

So for convex smooth $f$ the full statement is: the iterates converge to a minimizer, and the value gap decays like $1/T$. This is a strictly stronger conclusion than the assertion $\|\nabla f(x_i)\|\to0$ of Theorem 6.2, and the difference is entirely due to convexity. The pattern "non-expansiveness toward the solution set implies convergence" is the backbone of the whole fixed-point-theoretic treatment of convex optimization [16].

## 8 Rate II: Linear Convergence Under Strong Convexity

### 8.1 Theorem 9: extended co-coercivity

**Theorem 9 (Theorem 8.1 in this numbering).** Let $f$ be $\mu$-strongly convex and $L$-smooth. Then for all $x,y$, writing $\Delta g=\nabla f(x)-\nabla f(y)$ and $\Delta x=x-y$,

$ \langle\Delta g,\,\Delta x\rangle\;\ge\;\frac{1}{L+\mu}\|\Delta g\|^2+\frac{\mu L}{L+\mu}\|\Delta x\|^2. \tag{8.1} $

*Proof, case $\mu<L$.* Let $h(x)=f(x)-\tfrac\mu2\|x\|^2$, so $\nabla h(x)=\nabla f(x)-\mu x$ and $\nabla h(x)-\nabla h(y)=\Delta g-\mu\Delta x$. By (5.2), $h$ is convex, and by Section 8.2 below it is $(L-\mu)$-smooth. Apply co-coercivity (4.2) to $h$ with constant $L-\mu>0$:

$ \bigl\langle \Delta g-\mu\Delta x,\;\Delta x\bigr\rangle\;\ge\;\frac{1}{L-\mu}\bigl\|\Delta g-\mu\Delta x\bigr\|^2. $

Multiply by $L-\mu>0$ and expand both sides:

$ (L-\mu)\langle\Delta g,\Delta x\rangle-\mu(L-\mu)\|\Delta x\|^2\;\ge\;\|\Delta g\|^2-2\mu\langle\Delta g,\Delta x\rangle+\mu^2\|\Delta x\|^2. $

Collect the inner-product terms on the left, where $(L-\mu)+2\mu=L+\mu$, and the $\|\Delta x\|^2$ terms on the right, where $\mu^2+\mu(L-\mu)=\mu L$:

$ (L+\mu)\langle\Delta g,\Delta x\rangle\;\ge\;\|\Delta g\|^2+\mu L\|\Delta x\|^2. $

Divide by $L+\mu>0$. **End of proof.**

Inequality (8.1) is the union of the two things already known, co-coercivity (4.2), which contributes the $\|\Delta g\|^2$ term, and strong monotonicity (Theorem 5.4), which contributes the $\|\Delta x\|^2$ term, but with better constants than simply averaging them would give. That improvement is what buys the sharp step-size range in Theorem 10.

### 8.2 Two gaps in the derivation, closed

**Gap 1: why is $h$ $(L-\mu)$-smooth?** The lecture justifies this by Hessians: $\mu I\preceq\nabla^2f\preceq LI$ gives $0\preceq\nabla^2h\preceq(L-\mu)I$. That is correct but assumes $f\in C^2$, whereas Theorem 9 is used in settings where only the first-order definitions hold. Here is the argument without second derivatives. Since $h$ is convex, it suffices, by the chain of implications 5 to 2 to 3 to 4 to 1 in the equivalence list of Section 4.4, to check $\langle\nabla h(x)-\nabla h(y),x-y\rangle\le(L-\mu)\|x-y\|^2$, which follows from Cauchy-Schwarz and $L$-smoothness of $f$:

$ \langle\Delta g-\mu\Delta x,\Delta x\rangle=\langle\Delta g,\Delta x\rangle-\mu\|\Delta x\|^2\le\|\Delta g\|\,\|\Delta x\|-\mu\|\Delta x\|^2\le(L-\mu)\|\Delta x\|^2. $

The one implication of Section 4.4 not proved there is that 5 implies 2, so here it is. Given convex $g$ with $\langle\nabla g(x)-\nabla g(y),x-y\rangle\le M\|x-y\|^2$, set $\phi(x)=\tfrac M2\|x\|^2-g(x)$. Then $\langle\nabla\phi(x)-\nabla\phi(y),x-y\rangle=M\|\Delta x\|^2-\langle\nabla g(x)-\nabla g(y),\Delta x\rangle\ge0$, so $\phi$ is convex by Theorem 5.4, so $\phi(y)\ge\phi(x)+\langle\nabla\phi(x),y-x\rangle$; substituting $\phi=\tfrac M2\|\cdot\|^2-g$ and simplifying the quadratic terms exactly as in Section 5.1 yields $g(y)\le g(x)+\langle\nabla g(x),y-x\rangle+\tfrac M2\|y-x\|^2$, which is item 2. End of subproof.

**Gap 2: the isotropic case $\mu=L$.** The proof above divides by $L-\mu$, so it says nothing when $\mu=L$, which is not a pathological corner but precisely the perfectly conditioned case $\kappa=1$. The conclusion still holds, with equality. Indeed if $\mu=L$ then $h$ satisfies both $\langle\nabla h(x)-\nabla h(y),x-y\rangle\ge0$, by convexity, and $\le(L-\mu)\|\Delta x\|^2=0$, by the display above, so the inner product vanishes identically, forcing $\nabla h$ to be constant and $h$ affine, say $h(x)=\langle a,x\rangle+b$. Then $f(x)=\tfrac\mu2\|x\|^2+\langle a,x\rangle+b$ and $\Delta g=\mu\Delta x$, so the two sides of (8.1) are $\mu\|\Delta x\|^2$ and $\tfrac{1}{2\mu}\mu^2\|\Delta x\|^2+\tfrac{\mu^2}{2\mu}\|\Delta x\|^2=\mu\|\Delta x\|^2$, which are equal. So (8.1) holds for all $\mu\le L$, with the case $\mu=L$ being an identity rather than an inequality. This also identifies the equality case in general: (8.1) is tight exactly on isotropic quadratics.

### 8.3 Theorem 10, proved, with the optimal step size

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

**Iteration complexity.** From $\|x_T-x^\star\|^2\le c^T\|x_0-x^\star\|^2$, reaching $\varepsilon$ requires

$ T\;\ge\;\frac{\log\bigl(\|x_0-x^\star\|^2/\varepsilon\bigr)}{\log(1/c)}. $

At $\alpha=1/L$ we get $c=1-\tfrac{2\mu}{\mu+L}=\tfrac{L-\mu}{L+\mu}$, so $\log(1/c)\approx 2/\kappa$ for large $\kappa$ and $T=O\bigl(\kappa\log(1/\varepsilon)\bigr)$. Two readings: the $\log(1/\varepsilon)$ means each extra digit of accuracy costs a *constant* number of iterations, in contrast with Section 7.2, where it costs a factor of ten; the $\kappa$ means the constant is proportional to the condition number, so ill-conditioned problems are slow even though they are "linear". Both facts matter, and only the first is good news.

### 8.4 The running example, verified, including a tightness bonus

With $\mu=1$, $L=4$ and $\alpha=\tfrac14$: the admissible range is $\alpha\le\tfrac{2}{5}=0.4$, which is satisfied, and

$ c\;=\;1-\frac{2\cdot\tfrac14\cdot1\cdot4}{1+4}\;=\;1-\frac{2}{5}\;=\;0.6. $

Four iterations, each given as: index $i$; the bound $c^i\cdot8$; the actual squared distance $\|x_i-x^\star\|^2$.

- $i=1$; bound $4.8$; actual $2.25$.
- $i=2$; bound $2.88$; actual $1.2656$.
- $i=3$; bound $1.728$; actual $0.7119$.
- $i=4$; bound $1.0368$; actual $0.4004$.

All four bound values reproduce, and the observed per-step ratio from $i\ge1$ is $\bigl(\tfrac34\bigr)^2=0.5625\le0.6$. Checked. It is close to the bound but not equal, because $\alpha=\tfrac14$ is not the optimal step for this problem.

**Bonus the lecture misses.** Rerun at the optimal $\alpha^\star=\tfrac25$. Theorem 10 then predicts $c^\star=\bigl(\tfrac{4-1}{4+1}\bigr)^2=\bigl(\tfrac35\bigr)^2=0.36$. The actual iteration sends $x_1$ to $(1-4\cdot\tfrac25)x_1=-\tfrac35x_1$ and $x_2$ to $(1-\tfrac25)x_2=\tfrac35x_2$, so *both* coordinates contract by exactly $\tfrac35$ in magnitude and the squared distance contracts by exactly $0.36=c^\star$ at every step, from every starting point. So on this example, at the optimal step size, Theorem 10 holds with **equality**: the bound is not merely correct but exact. This is the concrete face of the tightness claim in Section 8.3, and it is a good sanity check that the constant $\tfrac{2\alpha\mu L}{\mu+L}$ has not been derived too generously.

**Linear against sublinear, numerically.** For $\varepsilon=10^{-6}$ with $\alpha=\tfrac14$, Theorem 10 needs $T\ge\log(8/10^{-6})/\log(1/0.6)=15.895/0.5108\approx31.1$, so $T=32$ iterations. Theorem 8's sublinear bound $\|x_0-x^\star\|^2/(2\alpha T)\le\varepsilon$ would demand $T\ge8/(2\cdot\tfrac14\cdot10^{-6})=1.6\times10^{7}$. Six orders of magnitude, on the same function with the same algorithm and the same step size; the only difference is which theorem you are allowed to invoke. That gap is the value of the extra hypothesis $\mu>0$.

### 8.5 Linear convergence from PL alone

The lecture closes with a bonus: convexity is not needed for a linear rate, since PL suffices.

**Proposition 8.3.** Let $f$ be $L$-smooth and satisfy the PL inequality (5.4) with constant $\mu>0$, with $f^\star=\inf f>-\infty$. Then gradient descent with $\alpha=1/L$ satisfies

$ f(x_{i+1})-f^\star\;\le\;\Bigl(1-\frac{\mu}{L}\Bigr)\bigl(f(x_i)-f^\star\bigr). $

*Proof.* Theorem 6.2(a) with $\alpha=1/L$ gives $f(x_{i+1})\le f(x_i)-\tfrac{1}{2L}\|\nabla f(x_i)\|^2$. Insert PL, that is $\|\nabla f(x_i)\|^2\ge2\mu(f(x_i)-f^\star)$:

$ f(x_{i+1})\;\le\;f(x_i)-\frac{2\mu}{2L}\bigl(f(x_i)-f^\star\bigr). $

Subtract $f^\star$ from both sides and factor. **End of proof.**

No convexity was used, only the descent lemma and PL. Note also that the conclusion is about *values*, not iterates, and it has to be: under PL alone the minimizer need not be unique, since the solution set can be a whole manifold, so "$x_i\to x^\star$" is not even a well-posed claim. Karimi, Nutini and Schmidt [8] show that PL is implied by, and strictly weaker than, several other conditions in common use (error bounds, quadratic growth, the restricted secant inequality), and that it extends to proximal and stochastic variants.

**Check on the running example.** With $\mu=1$ and $L=4$ the predicted factor is $1-\tfrac14=\tfrac34$; the observed ratio $f(x_{i+1})/f(x_i)=\bigl(\tfrac34\bigr)^2=\tfrac{9}{16}=0.5625\le0.75$. Checked. As always, the bound is honest but conservative because the worst-case direction is not the one the iterates actually travel after step one.

## 9 What the Lecture Leaves Out

### 9.1 Acceleration, and the lower bounds that make it optimal

The most consequential omission. Gradient descent's $O(1/T)$ and $O(\kappa\log\tfrac1\varepsilon)$ are *not* the best a first-order method can do. Nesterov's accelerated gradient method [14] adds one momentum term,

$ y_{i+1}=x_i-\tfrac1L\nabla f(x_i),\qquad x_{i+1}=y_{i+1}+\beta_i\,(y_{i+1}-y_i), $

and attains $f(x_T)-f^\star=O\bigl(L\|x_0-x^\star\|^2/T^2\bigr)$ for smooth convex $f$, and $O\bigl(\exp(-T/\sqrt\kappa)\bigr)$ with $\beta_i=\tfrac{\sqrt\kappa-1}{\sqrt\kappa+1}$ for strongly convex $f$. The improvements are $\kappa\to\sqrt\kappa$ and $1/T\to1/T^2$; for $\kappa=10^4$ that is a hundredfold reduction in iterations, from the same gradient oracle. Nemirovski and Yudin [15] proved matching lower bounds, $\Omega(1/T^2)$ and $\Omega(\exp(-T/\sqrt\kappa))$, for any method whose iterates lie in the span of observed gradients, so acceleration is optimal, not merely better. See [3, Chapter 2] for the standard treatment. Momentum in deep learning is the practical descendant of this idea, though the theory transfers only loosely to the stochastic nonconvex setting.

### 9.2 Choosing $\alpha$ without knowing $L$

Every theorem here is stated for a constant $\alpha$ calibrated to $L$, which in practice is unknown. The standard remedies, none of which the lecture mentions: **backtracking line search**, which starts from a generous $\alpha$ and halves it until the Armijo condition $f(x-\alpha\nabla f(x))\le f(x)-\tfrac{\alpha}{2}\|\nabla f(x)\|^2$ holds, this condition being precisely Step 1 of Theorem 7.1, so all the rates go through with $L$ replaced by the largest local curvature actually encountered; **exact line search**; the **Barzilai-Borwein** step $\alpha_i=\tfrac{\langle\Delta x,\Delta g\rangle}{\|\Delta g\|^2}$, which estimates $1/L$ from the last two iterates; and the adaptive per-coordinate schemes (AdaGrad, RMSProp, Adam) that dominate deep learning practice. See [18, Chapter 3] for line-search theory and [17] for the machine-learning perspective.

### 9.3 Nonsmooth objectives

$L$-smoothness fails for the $\ell_1$ penalty, the hinge loss, and ReLU networks, that is, for much of what one actually optimizes. Two replacements. **Subgradient descent** replaces $\nabla f(x)$ by any element $g$ of the subdifferential $\partial f(x)=\{g:f(y)\ge f(x)+\langle g,y-x\rangle\text{ for all }y\}$; with $G$-Lipschitz $f$ and a decaying step it achieves $O(1/\sqrt T)$, genuinely slower, and no descent lemma is available, so the values are not monotone. **Proximal gradient** handles $f=\ell+r$ with $\ell$ smooth and $r$ simple by iterating $x_{i+1}=\operatorname{prox}_{\alpha r}(x_i-\alpha\nabla \ell(x_i))$, and recovers the full $O(1/T)$ and linear rates; for $r=\lambda\|\cdot\|_1$ the prox is soft-thresholding and the method is ISTA, accelerated to FISTA. Beck [5] is the reference; Rockafellar [2] is the source for subdifferential calculus.

### 9.4 Constraints

Minimizing over a convex set $C$ replaces the update with **projected gradient descent**, $x_{i+1}=\Pi_C\bigl(x_i-\alpha\nabla f(x_i)\bigr)$. Because $\Pi_C$ is nonexpansive, every proof in Sections 7 and 8 survives essentially verbatim: the projection can only shrink distances to a point of $C$, and $x^\star\in C$. The optimality condition changes from $\nabla f(x^\star)=0$ to the variational inequality $\langle\nabla f(x^\star),y-x^\star\rangle\ge0$ for all $y\in C$. The unconstrained framing of the lecture hides that these are the same theorems. See [1, Chapter 4] and [16].

### 9.5 Second-order methods and the $\kappa$ that will not go away

Newton's method, $x_{i+1}=x_i-\bigl(\nabla^2f(x_i)\bigr)^{-1}\nabla f(x_i)$, converges quadratically near $x^\star$ and, crucially, its local rate does *not* depend on $\kappa$, because the Hessian inverse undoes the anisotropy that Section 6.2 showed is what slows gradient descent down. The price is $O(n^3)$ per step and $O(n^2)$ storage, which rules it out at deep-learning scale; quasi-Newton methods (BFGS, L-BFGS) build a low-rank approximation to the inverse Hessian from gradient differences at $O(n)$ cost per step. Conjugate gradient reaches the exact minimizer of a quadratic in $n$ steps and has a $\sqrt\kappa$ rate, the same as acceleration. Reference [18] covers all of these.

### 9.6 Stochastic gradients

Every rate here assumes the exact gradient, whose cost is $O(N)$ for an $N$-sample ERM objective. The next lecture replaces $\nabla f$ by a mini-batch estimate; the consequences are structural, not cosmetic. The descent lemma no longer gives monotone decrease, so Step 5 of Theorem 7.1 fails and guarantees move to averaged iterates; a constant step size converges only to a noise ball of radius $O(\alpha\sigma^2/\mu)$ rather than to $x^\star$; and the rates degrade to $O(1/\sqrt T)$ in the convex case and $O(1/T)$ in the strongly convex case, both dominated by variance rather than by curvature, so acceleration no longer helps in the same way. Reference [17] is the survey; [19] gives the nonconvex analysis; the companion note for that lecture is listed in [20].

### 9.7 What actually happens in deep learning

The honest position. Deep network training objectives are nonconvex, typically not globally $L$-smooth, and the theorems above do not apply as stated. What transfers: the descent lemma and the $O(1/\varepsilon^2)$ rate to stationarity of Corollary 6.3, which hold verbatim; the intuition that a step size larger than twice the reciprocal of the local smoothness constant diverges, which is exactly what a learning-rate sweep discovers empirically; and the condition-number picture, which explains why normalization layers and adaptive step sizes help. What does not transfer: the guarantee that stationary means optimal. The empirical observation that trained networks nonetheless reach near-zero loss has motivated searching for a hypothesis that is weaker than convexity but strong enough for a rate, and PL (Section 5.5) is the leading candidate, provable in some over-parameterized regimes. That is the honest state of the art, and the reason PL appears in a first course at all.

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
