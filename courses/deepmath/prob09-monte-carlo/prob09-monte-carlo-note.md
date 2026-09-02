# Deep Learning Math 9 - Monte Carlo and Importance Sampling (Lecture Note)

**About this file.** This is a linear, screen-reader-friendly edition of the Lecture 9 companion note. It is text only: every figure, chart and table of the original has been replaced by a description or by a list that reads in order, and all mathematics is written in LaTeX. Section numbers match the original note, so a reference to "Section 7.6" means the same place in both editions. Nothing else is needed to read it.

**Convention.** Throughout, $p$ is the *target* distribution (the one whose expectation we want), $q$ is the *proposal* distribution (the one we can actually sample), and
$$ w(x) = \frac{p(x)}{q(x)} $$
is the *importance weight*. The quantity being estimated is always
$$ \mu = \mathbb{E}_p\big[f(X)\big]. $$
All logarithms are natural. Integrals are written for the continuous case; every argument here works verbatim for discrete distributions with sums replacing integrals, and the two places where the discrete case needs separate words say so.

**Notation.**

- $\mathbb{E}_p[\cdot]$: expectation when $X \sim p$. A bare $\mathbb{E}[\cdot]$ refers to whatever sampling distribution the surrounding paragraph has fixed.
- $\mathrm{Var}_q(\cdot)$, $\mathrm{Cov}_q(\cdot,\cdot)$: variance and covariance under $q$.
- $\hat\mu_n$: the plain Monte Carlo estimator of $\mu$ from $n$ samples.
- $\hat\mu_n^{\mathrm{IS}}$: the importance-sampling estimator.
- $\hat\mu_n^{\mathrm{SN}}$: the self-normalized importance-sampling estimator.
- $\sigma_f^2 = \mathrm{Var}_p(f(X))$: the variance of the integrand under the target.
- $\tilde p$: an unnormalized target, so that $p = \tilde p / Z$ with $Z = \int \tilde p$.
- $\tilde w = \tilde p / q = Z w$: the computable unnormalized weight.
- $\mathbf 1\{A\}$: the indicator of the event $A$, equal to $1$ when $A$ holds and $0$ otherwise.
- $n_{\mathrm{eff}}$: effective sample size (Section 7.6).
- $D(P \| Q)$: Kullback-Leibler divergence from $P$ to $Q$.
- $\pi_\theta$: a distribution parametrized by $\theta$ (a policy or generator); $\pi_b$ a behavior policy; $\pi_{\mathrm{ref}}$ a reference model.
- $s_\theta(x) = \nabla_\theta \log \pi_\theta(x)$: the *score*.
- $R$: a reward or return; $b$ a baseline; $J(\theta) = \mathbb{E}_{\pi_\theta}[R(X)]$.
- $\stackrel{\mathrm{i.i.d.}}{\sim}$: independent and identically distributed draws from the named distribution.

**Background used.** From Lecture 1 (prob01): the law of the unconscious statistician (LOTUS), the variance identity $\mathrm{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2$, linearity of expectation, Jensen's inequality, the Bernoulli variance $\rho(1-\rho)$, the mean of an exponential. From Lecture 2 (prob02): Kullback-Leibler divergence, its nonnegativity with equality only for identical distributions, and its additivity over product distributions. From Lecture 4 (prob04): the chain rule of probability for sequences. From Lecture 5 (prob05): Chebyshev's inequality, the law of large numbers, the central limit theorem. From Lecture 6 (prob06): Hoeffding's inequality and the inversion of a tail bound into a sample-size requirement. From Lecture 7 (prob07): the decomposition $\mathrm{MSE} = \mathrm{Bias}^2 + \mathrm{Variance}$ and the notion of estimator bias. From Lecture 8 (prob08): the Gaussian machinery, in particular $X = \mu + \Sigma^{1/2}\varepsilon$.

Two facts of real analysis are *imported without proof*, and they are the only such imports in the whole note: the **strong law of large numbers** (Section 2.2) and the **dominated convergence theorem** (Section 8.3).

**What this edition adds.** Nothing mathematical. Where the original cross-checks a number against the presentation it accompanies, this edition keeps the number and the check but drops the cross-reference, since a presentation is not something this reader can consult. Descriptions of the figures appear in prose at the point where each figure was placed.

**Contents.**

1. Why Sampling
2. Recall the Toolkit
3. The Monte Carlo Estimator
4. Error Scaling and Dimension
5. Importance Sampling
6. The Variance of Importance Sampling
7. Self-Normalized Importance Sampling
8. The Score-Function Gradient
9. Off-Policy Estimation and RLHF
10. What the Lecture Leaves Out
11. References

---

## 1 Why Sampling

### 1.1 The one number

Nearly every quantity a learning system needs is an expectation:
$$ \mu = \mathbb{E}_{X \sim p}\big[ f(X) \big] = \int f(x)\, p(x)\, dx . $$
Two standing assumptions run through the entire lecture: we can *draw samples* from $p$, and we can *evaluate* $f$ at a sample. Neither assumption gives us the integral.

Three examples where the integral is out of reach:

- A Bayesian posterior normalizer $Z = \int \tilde p(x)\, dx$, an integral over a parameter space of dimension in the millions.
- A reinforcement-learning return $\mathbb{E}_{\pi}[\sum_t r_t]$, an expectation over all trajectories a policy can generate.
- A language-model expectation over sequences, where a vocabulary of size $|\mathcal V|$ and length $T$ gives $|\mathcal V|^T$ terms.

### 1.2 What "uncomputable" means, and the thread of the lecture

None of these integrals is uncomputable in a logical sense; each is a finite sum or a well-defined integral. What fails is *enumeration*: the number of terms, or the dimension of the domain, puts exact evaluation permanently out of reach. Sampling replaces enumeration by a random probe, and the price is variance.

Variance accounting is the single thread of this lecture. Every theorem below is either a variance formula, a variance bound, or a device for making variance smaller. Unbiasedness is comparatively cheap; variance is what decides whether an estimator is usable.

## 2 Recall the Toolkit

### 2.1 From Lecture 1

- **LOTUS.** $\mathbb{E}[f(X)] = \int f(x)\, p(x)\, dx$: an expectation of a *function* of $X$ is computed against the density of $X$, with no need for the density of $f(X)$.
- **Variance identity.** $\mathrm{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2$.
- **Linearity.** $\mathbb{E}[aY + bZ] = a\mathbb{E}[Y] + b\mathbb{E}[Z]$, with no independence needed.
- **Jensen.** For convex $\varphi$, $\mathbb{E}[\varphi(Y)] \geq \varphi(\mathbb{E}[Y])$; the inequality reverses for concave $\varphi$.

### 2.2 From Lecture 5

**Chebyshev's inequality.** For $Y$ with finite variance,
$$ \Pr\big( |Y - \mathbb{E} Y| \geq \epsilon \big) \;\leq\; \frac{\mathrm{Var}(Y)}{\epsilon^2}, $$
so for an average of $n$ i.i.d. variables of variance $\sigma^2$ the bound is $\sigma^2/(n\epsilon^2)$.

**Weak versus strong law.** The *weak* law gives convergence in probability of the sample mean and follows from Chebyshev whenever the variance is finite. The *strong* law gives almost-sure convergence and needs only a finite first moment, $\mathbb{E}|Y| < \infty$. The strong law is **imported without proof** here; the distinction between the two becomes material in Section 6.6, where an estimator has a finite mean and an infinite variance.

### 2.3 From Lecture 6

**Hoeffding's inequality.** If $Y_1,\dots,Y_n$ are i.i.d. with $Y_i \in [a,b]$ almost surely, then
$$ \Pr\big( |\bar Y_n - \mathbb{E} Y| \geq \epsilon \big) \;\leq\; 2\exp\!\left( -\frac{2n\epsilon^2}{(b-a)^2} \right). $$

Chebyshev and Hoeffding are stated in *different currencies*: Chebyshev charges for variance and pays in a polynomial tail; Hoeffding charges for boundedness and pays in an exponential tail. Neither dominates the other in general, and Section 3.8 compares them on the same problem.

### 2.4 The new element

Lectures 1 to 8 treated the sampling distribution as given by the problem. From here on the sampler is a **design variable**: the same $\mu$ can be estimated by sampling many different distributions, and choosing which one is the subject of Sections 5 through 7.

## 3 The Monte Carlo Estimator

### 3.1 Definition

Let $X_1, \dots, X_n \stackrel{\mathrm{i.i.d.}}{\sim} p$ and set
$$ \hat\mu_n = \frac1n \sum_{i=1}^{n} f(X_i). $$

Two moment conditions are needed, and it is worth keeping them separate, because the results below need different ones:

- $\mathbb{E}_p[|f(X)|] < \infty$, which makes $\mu$ well defined and gives unbiasedness and consistency;
- $\sigma_f^2 = \mathrm{Var}_p(f(X)) < \infty$, which is needed for the variance formula and for every rate.

### 3.2 Theorem 1: unbiasedness

**Theorem 1.** If $\mathbb{E}_p[|f(X)|] < \infty$ then $\mathbb{E}[\hat\mu_n] = \mu$ for every $n \geq 1$.

*Proof.* By linearity of expectation,
$$ \mathbb{E}[\hat\mu_n] = \frac1n \sum_{i=1}^{n} \mathbb{E}[f(X_i)] = \frac1n \cdot n\mu = \mu . $$
**End of proof.**

Note what the proof did *not* use: independence. Identical distribution alone suffices for unbiasedness. Independence is what buys the variance formula next.

### 3.3 Theorem 2: variance

**Theorem 2.** If in addition $\sigma_f^2 < \infty$, then
$$ \mathrm{Var}(\hat\mu_n) = \frac{\sigma_f^2}{n}. $$

*Proof.* Expand the variance of the sum:
$$ \mathrm{Var}\Big( \frac1n \sum_i f(X_i) \Big) = \frac{1}{n^2} \Big( \sum_i \mathrm{Var}(f(X_i)) + \sum_{i \neq j} \mathrm{Cov}\big(f(X_i), f(X_j)\big) \Big). $$
Independence kills every covariance term, and each of the $n$ variance terms equals $\sigma_f^2$, so the bracket is $n\sigma_f^2$ and the whole expression is $\sigma_f^2/n$. **End of proof.**

### 3.4 Corollary: the error rate

Since the estimator is unbiased, its mean squared error is its variance, and
$$ \mathrm{RMSE}(\hat\mu_n) = \sqrt{\mathbb{E}\big[ (\hat\mu_n - \mu)^2 \big]} = \frac{\sigma_f}{\sqrt n}. $$
Every extra correct decimal digit therefore costs a hundredfold increase in $n$.

### 3.5 Guarantee I: Chebyshev and consistency

Applying Chebyshev to $\hat\mu_n$ with Theorem 2's variance,
$$ \Pr\big( |\hat\mu_n - \mu| \geq \epsilon \big) \;\leq\; \frac{\sigma_f^2}{n\,\epsilon^2} \;\xrightarrow[n \to \infty]{}\; 0 \quad \text{for every fixed } \epsilon > 0, $$
which is exactly convergence in probability $\hat\mu_n \to \mu$: the estimator is **consistent**. Under finite variance this is the weak law re-derived. Under the weaker hypothesis $\mathbb{E}_p|f| < \infty$ alone, consistency still holds by the imported strong law of Section 2.2, and that distinction is what saves the pathological example of Section 6.6.

### 3.6 Guarantee II: Hoeffding, with the inversion derived

If moreover $f(x) \in [a,b]$ for all $x$, Hoeffding applies to $Y_i = f(X_i)$:
$$ \Pr\big( |\hat\mu_n - \mu| \geq \epsilon \big) \;\leq\; 2\exp\!\left( -\frac{2n\epsilon^2}{(b-a)^2} \right). $$

**Inversion.** Demanding that the right side be at most $\delta$ and solving for $n$:
$$ 2 e^{-2n\epsilon^2/(b-a)^2} \leq \delta \iff \frac{2n\epsilon^2}{(b-a)^2} \geq \ln\frac{2}{\delta} \iff n \geq \frac{(b-a)^2 \ln(2/\delta)}{2\epsilon^2}. $$
That is: error at most $\epsilon$ with confidence $1 - \delta$ once $n$ crosses the threshold. This is the sample-complexity form used in the worked example below, and structurally the same inversion Lecture 6 performed for generalization bounds.

### 3.7 Worked example: estimating $\pi$ by throwing darts

**Setup.** Let $X = (x,y)$ be uniform on the square $[-1,1]^2$, whose density is the constant $\tfrac14$ on the square since the square has area $4$. Let $f(x,y) = \mathbf 1\{x^2 + y^2 \leq 1\}$, the indicator of the unit disk. By LOTUS,
$$ \mathbb{E}[f] = \tfrac14 \cdot \mathrm{area(disk)} = \tfrac14 \cdot \pi \cdot 1^2 = \frac{\pi}{4}, $$
which is the familiar area ratio. The estimator
$$ \hat\pi_n = 4 \cdot \frac{\#\text{hits}}{n} = \frac4n \sum_{i=1}^n f(X_i) $$
is unbiased for $\pi$ by Theorem 1 and linearity: $\mathbb{E}[\hat\pi_n] = 4 \cdot \pi/4 = \pi$.

**Six darts by hand.** Each entry gives the point, the value of $x^2 + y^2$, and the verdict:

- $(0.5, 0.5)$: $0.25 + 0.25 = 0.50$, inside.
- $(-0.9, 0.8)$: $0.81 + 0.64 = 1.45$, outside.
- $(0.2, -0.6)$: $0.04 + 0.36 = 0.40$, inside.
- $(-0.4, 0.1)$: $0.16 + 0.01 = 0.17$, inside.
- $(0.8, -0.7)$: $0.64 + 0.49 = 1.13$, outside.
- $(0.3, 0.9)$: $0.09 + 0.81 = 0.90$, inside.

Four inside, two outside, so $\hat\pi = 4 \cdot \tfrac46 = \tfrac83 \approx 2.67$. (The original note carries a dartboard figure at this point: a square with an inscribed circle, the four inside points drawn as filled marks within the circle and the two outside points as open marks in the corner regions, with the counts 4 and 2 labelled. It carries no information beyond the list above.) The estimate is badly noisy at $n = 6$, exactly as Theorem 2 predicts.

**Exact statistics.** Each $f(X_i)$ is Bernoulli with success probability $\rho = \pi/4 \approx 0.785398$, so by the Bernoulli variance of Lecture 1,
$$ \mathrm{Var}(f) = \rho(1-\rho) = \frac{\pi}{4}\Big( 1 - \frac{\pi}{4} \Big) \approx 0.785398 \times 0.214602 \approx 0.168548, $$
i.e. about $0.1685$. Since $\hat\pi_n$ is the average of the i.i.d. variables $4f(X_i)$, and $\mathrm{Var}(4f) = 16\,\mathrm{Var}(f) = \pi(4 - \pi) \approx 2.6968$,
$$ \mathrm{Var}(\hat\pi_n) = \frac{16\,\rho(1-\rho)}{n} \approx \frac{2.70}{n}, \qquad \mathrm{RMSE} \approx \frac{\sqrt{2.6968}}{\sqrt n} \approx \frac{1.64}{\sqrt n}, $$
using $\sqrt{2.6968} = 1.6422$. The darts-per-digit ledger follows by substitution: $n = 10^2, 10^4, 10^6$ give RMSE about $0.164$, $0.0164$, $0.00164$ respectively, i.e. roughly one, two and three correct digits, with each digit costing a hundred times the darts.

### 3.8 The same guarantee two ways, with a rounding note

Target: $|\hat\pi - \pi| \leq 0.01$ with confidence $95$ percent, so $\epsilon = 0.01$ and $\delta = 0.05$.

**Chebyshev.** The requirement is $n \geq \sigma^2/(\delta\,\epsilon^2)$ with $\sigma^2 = \mathrm{Var}(4f)$. Using the rounded variance $\sigma^2 = 16 \times 0.1685 = 2.696$,
$$ n \geq \frac{2.696}{0.05 \times 10^{-4}} = 539{,}200 . $$

*Rounding note.* Three slightly different numbers circulate for this requirement, and they come from three roundings of the same variance: $2.696$ gives $539{,}200$; the displayed $2.70$ gives $540{,}000$; the exact $\sigma^2 = \pi(4-\pi) = 2.69677$ gives $539{,}354$. They agree to two significant figures. The figure $539{,}200$ is internally consistent with the rounded variance $2.696$, so this is a rounding artifact and not an error, but a reader reproducing the arithmetic from $2.70$ will land on $540{,}000$.

**Hoeffding.** Here $4f \in [0,4]$, so $(b-a)^2 = 16$, and the Section 3.6 inversion with $\ln(2/0.05) = \ln 40 \approx 3.6889$ gives
$$ n \;\geq\; \frac{16 \ln 40}{2 \times 0.01^2} = \frac{16 \times 3.6889}{2 \times 10^{-4}} = \frac{59.022}{2 \times 10^{-4}} \approx 295{,}111 . $$

Hoeffding wins here by roughly a factor $1.8$: the exponential tail beats the polynomial one even after Chebyshev is handed the exact variance. Both are conservative. The actual RMSE at $n = 10^5$ is $1.6422/\sqrt{10^5} \approx 0.0052$, already half the target error, because tail *guarantees* pay for their worst-case validity.

### 3.9 What Monte Carlo never asked

The proofs above used exactly three things: the ability to sample $p$, the ability to evaluate $f$, and $\sigma_f^2 < \infty$. They never used smoothness of $f$ (in the $\pi$ example $f$ is an indicator, discontinuous on the circle), nor a formula for $p$, nor any geometry of the domain. This austerity is the method's robustness, and it sets up the next section: the one thing the theorems *also* never mentioned is the dimension.

## 4 Error Scaling and Dimension

### 4.1 The remarkable absence

Let $X \in \mathbb{R}^d$ for any $d$. Theorem 2's proof manipulated only the scalars $Y_i = f(X_i)$; the domain of $X$ never entered it. So $\mathrm{RMSE} = \sigma_f/\sqrt n$ holds verbatim in every dimension, with one honest caveat: the *constant* $\sigma_f$ is a property of $f$ and $p$ and can itself grow with $d$. The claim is that the *rate* in $n$ does not degrade, not that the error is dimension-free.

### 4.2 The competitor: grid integration, with the $h^2$ claim derived

**Lemma (composite midpoint rule).** Let $f \in C^2[0,1]$, partition $[0,1]$ into $m$ cells of width $h = 1/m$ with midpoints $c_k$. Then
$$ \left| \int_0^1 f(x)\, dx - h \sum_{k=1}^m f(c_k) \right| \;\leq\; \frac{h^2}{24}\, \max_{[0,1]} |f''| . $$

*Proof.* On one cell $[c_k - \tfrac h2,\, c_k + \tfrac h2]$, Taylor's theorem with Lagrange remainder gives
$$ f(x) = f(c_k) + f'(c_k)(x - c_k) + \tfrac12 f''(\xi_x)(x - c_k)^2 . $$
Integrate over the cell. The linear term integrates to $0$ by symmetry about $c_k$, and the remainder is bounded by
$$ \left| \int_{\mathrm{cell}} f - h f(c_k) \right| \leq \frac{\max|f''|}{2} \int_{-h/2}^{h/2} u^2\, du = \frac{\max|f''|}{2} \cdot \frac{h^3}{12} = \frac{\max|f''|\, h^3}{24}. $$
Summing over the $m = 1/h$ cells multiplies by $1/h$, giving a global bound proportional to $h^2$. **End of proof.**

On $[0,1]^d$, the product (tensor-grid) version of this rule with $m$ total points has spacing $h = m^{-1/d}$ per axis, so the error scales as
$$ C\,h^2 = C\, m^{-2/d} $$
for smooth $f$, with $C$ depending on second derivatives. Constants are suppressed, as flagged.

### 4.3 Cost of accuracy, both methods

**Grid.** Setting $m^{-2/d} = \epsilon$ and solving gives $m = \epsilon^{-d/2}$. At $\epsilon = 10^{-2}$ this is $m = 10^{d}$. Evaluating that single formula:

- $d = 1$: about $10$ points.
- $d = 6$: about $10^{6}$ points.
- $d = 20$: about $10^{20}$ points.
- $d = 100$: about $10^{100}$ points.

**Monte Carlo.** Setting $\sigma_f/\sqrt n = 10^{-2}$ gives $n = \sigma_f^2 \times 10^4$, for every $d$.

The exponential-in-$d$ blowup of the grid is the *curse of dimensionality*. Monte Carlo's escape is not cleverness: its error analysis, Theorem 2, simply never looked at the domain.

### 4.4 The crossover at $d = 4$

Per unit of work $N$ (grid points or samples), grid error scales as $N^{-2/d}$ and Monte Carlo error as $N^{-1/2}$. The grid wins when its exponent is larger:
$$ \frac2d > \frac12 \iff d < 4, $$
with equality at $d = 4$. (The original note plots error against work on log-log axes; the content of that chart is exactly these slopes: $-2$ for the $d = 1$ grid, $-1/2$ for Monte Carlo, and $-2/20 = -0.1$ for the $d = 20$ grid.)

### 4.5 Honest caveats

1. $\sigma_f$ can be enormous even in $d = 1$. The rare-event example of Section 5 is precisely this failure, and it motivates importance sampling rather than more samples.
2. For very smooth integrands in low dimension, higher-order quadrature beats both lines above; the comparison pitted Monte Carlo against a *second-order* rule only.
3. *Quasi-Monte Carlo*, meaning deterministic low-discrepancy point sets, achieves error $O((\log n)^d / n)$ for integrands of bounded variation, asymptotically better than $n^{-1/2}$. See Owen [1, ch. 15-17]. Monte Carlo's claim is robustness under minimal assumptions, not universal supremacy.

For the workloads this course cares about (images, trajectories, token sequences) $d$ is in the thousands or beyond, grids die by about $d = 10$, and every minibatch loss, every generation and every evaluation in the field is de facto a Monte Carlo estimate.

## 5 Importance Sampling

### 5.1 Two failure modes of vanilla Monte Carlo

(a) *Cannot sample $p$.* Bayesian posteriors are computable only up to the normalizer $Z$; this case is deferred to Section 7.

(b) *Rare events.* Here $p$ is samplable but $f$ lives where $p$ almost never goes, so almost every sample contributes $0$.

Both are cured by the same identity.

**The rare event by hand.** Let $X \sim \mathrm{Exp}(1)$, so $p(x) = e^{-x}$ on $x \geq 0$, and target
$$ \mu = \Pr(X > 10) = \int_{10}^{\infty} e^{-x}\, dx = e^{-10} \approx 4.54 \times 10^{-5} . $$
Since $e^5 \approx 148.41$ and $e^{10} = (e^5)^2 \approx 22{,}026$, this is about one hit per $22{,}026$ samples.

**Relative-error computation.** Here $f = \mathbf 1\{x > 10\}$ makes $f(X)$ Bernoulli with parameter $\mu$, so $\sigma_f^2 = \mu(1-\mu)$ and by Theorem 2
$$ \frac{\mathrm{RMSE}}{\mu} = \frac{\sqrt{\mu(1-\mu)}}{\mu\sqrt n} = \sqrt{\frac{1-\mu}{n\,\mu}} \approx \frac{1}{\sqrt{n\mu}} \qquad (\mu \text{ tiny}). $$
So $10$ percent relative error needs $n\mu \approx 100$, that is $n \approx 100\,e^{10} \approx 2.2 \times 10^6$ samples. The *absolute* error is tiny at any $n$; the *relative* error is the honest yardstick for a quantity of order $10^{-5}$, and vanilla Monte Carlo fails it, because virtually all the work is spent confirming that the event usually does not happen.

### 5.2 Theorem 3: the importance-sampling identity

**Theorem 3 (importance sampling identity).** Let $p$ and $q$ be densities (or mass functions) and $f$ a function with $\mathbb{E}_p[|f(X)|] < \infty$. Assume the *support condition*:
$$ q(x) > 0 \quad \text{for every } x \text{ with } f(x)\, p(x) \neq 0 . $$
Then, with $w(x) = p(x)/q(x)$ defined on $\{q > 0\}$,
$$ \mathbb{E}_p\big[ f(X) \big] \;=\; \mathbb{E}_q\big[ f(X)\, w(X) \big]. $$

*Proof (continuous case).* By LOTUS under $q$. The integrand $fw$ is only ever evaluated at samples from $q$, which land in $\{q > 0\}$ with probability $1$, so
$$ \mathbb{E}_q[f w] = \int_{\{q > 0\}} f(x)\, \frac{p(x)}{q(x)}\, q(x)\, dx = \int_{\{q > 0\}} f(x)\, p(x)\, dx . $$
The cancellation $\tfrac pq \cdot q = p$ is legitimate pointwise wherever $q(x) > 0$, which is the only place the integral looks. It remains to *patch* the missing region: on $\{q = 0\}$ the support condition forces $f(x)p(x) = 0$, so the integral over that region is $0$ and
$$ \int_{\{q > 0\}} f\,p\,dx = \int_{\{q > 0\}} f\,p\,dx + \int_{\{q = 0\}} f\,p\,dx = \int f\,p\,dx = \mathbb{E}_p[f]. $$
*Discrete case:* identical, with sums over $\{x : q(x) > 0\}$ and the same patch. **End of proof.**

**Reading the condition.** It is an *absolute-continuity* requirement restricted to where it matters: the measure $f\,p$ must vanish wherever $q$ does, equivalently $p$ restricted to $\{f \neq 0\}$ is absolutely continuous with respect to $q$. The proposal may freely ignore regions where $f = 0$, and the tailored rare-event proposal below does exactly that, legally. What it may never do is assign zero probability to a region where $fp$ is alive.

### 5.3 The counterexample, computed in full

**Why the support condition is real.** Let $p$ be uniform on $\{1,2,3,4\}$ and $f = \mathbf 1\{x = 4\}$, so $\mu = \tfrac14$. Take $q$ uniform on $\{1,2,3\}$. Then $q(4) = 0$ while $f(4)\,p(4) = \tfrac14 \neq 0$, so the condition is violated. On the support of $q$ the weight is the constant $w(x) = \tfrac{1/4}{1/3} = \tfrac34$, and
$$ \mathbb{E}_q[f\,w] = \sum_{x=1}^{3} q(x)\, f(x)\, w(x) = \sum_{x=1}^{3} \tfrac13 \cdot \mathbf 1\{x = 4\} \cdot \tfrac34 = 0 \;\neq\; \tfrac14 . $$

Every sample reports $0$, with zero empirical variance, forever: the estimator converges cleanly, to the wrong answer. There is *no warning sign in the data*, because the region carrying all of $\mu$ is simply never visited. Section 7.7 sharpens this: the effective-sample-size diagnostic reads a perfect $n_{\mathrm{eff}} = n$ here.

### 5.4 The importance-sampling estimator and its unbiasedness

**Definition (IS estimator).** Under the hypotheses of Theorem 3, for $X_1,\dots,X_n \stackrel{\mathrm{i.i.d.}}{\sim} q$:
$$ \hat\mu_n^{\mathrm{IS}} = \frac1n \sum_{i=1}^{n} w(X_i)\, f(X_i), \qquad w = \frac pq . $$

**Corollary (unbiased).** $\mathbb{E}\big[\hat\mu_n^{\mathrm{IS}}\big] = \mathbb{E}_q[f\,w] = \mu$.

*Proof.* The first equality is Theorem 1 applied under $q$ to the function $g = f \cdot w$; its $q$-expectation exists because $\mathbb{E}_q[|fw|] = \mathbb{E}_p[|f|] < \infty$ by Theorem 3 applied to $|f|$, which satisfies the same support condition since $|f|p \neq 0$ exactly when $fp \neq 0$. The second equality is Theorem 3. **End of proof.**

### 5.5 Weights are likelihood ratios, and one condition worth flagging

The weight $w(x) = p(x)/q(x)$ compares how likely $x$ is under the target versus the proposal: $w > 1$ where $q$ under-visits, so each such sample is counted extra, and $w < 1$ where $q$ over-visits.

The bookkeeping line "$\mathbb{E}_q[w] = \int p = 1$" deserves a precision note. Computing under the Theorem 3 condition only,
$$ \mathbb{E}_q[w] = \int_{\{q > 0\}} p(x)\, dx = \Pr_p\big( q(X) > 0 \big) \;\leq\; 1, $$
with equality if and only if $q > 0$ wherever $p > 0$, which is a *stronger* condition than Theorem 3's. The two coincide for proposals covering the whole target support, which is the usual case and the implicit setting of that line. But the tailored rare-event proposal of Section 5.6 separates them: with $q(x) = e^{-(x-10)}$ on $x \geq 10$,
$$ \mathbb{E}_q[w] = \int_{10}^{\infty} \frac{e^{-x}}{e^{-(x-10)}}\, e^{-(x-10)}\, dx = \int_{10}^{\infty} e^{-x}\, dx = e^{-10} \;\neq\; 1 . $$
Nothing is wrong: Theorem 3 needs only coverage of $fp$, and the estimator is exactly unbiased for $\mu$. But "weights average to one" is a fact about *full-support* proposals, not about all admissible ones. It becomes essential in Section 7, where the denominator of the self-normalized estimator estimates $\int \tilde p$ and full support of $q$ over $p$ is genuinely required.

### 5.6 The tailored proposal on the rare event

Target $\mu = \Pr(X > 10)$ under $p = \mathrm{Exp}(1)$. Take the shifted exponential $q(x) = e^{-(x-10)}$ for $x \geq 10$, and zero below. It is a genuine density, since $\int_{10}^{\infty} e^{-(x-10)}\,dx = \int_0^\infty e^{-u}\,du = 1$. Support condition: $fp \neq 0$ only on $(10,\infty)$, where $q > 0$, so it holds. For any sample $x \geq 10$, hence $f(x) = 1$,
$$ f(x)\, w(x) = 1 \cdot \frac{e^{-x}}{e^{-(x-10)}} = e^{-x + x - 10} = e^{-10} $$
for *every* such $x$. The weighted integrand is the constant $e^{-10}$, so $\hat\mu_n^{\mathrm{IS}} = e^{-10}$ exactly from $n = 1$ onward, and $\mathrm{Var}_q(fw) = 0$. Compare vanilla Monte Carlo's $2.2 \times 10^6$ samples for the same $10$ percent relative error.

This looks like luck. Theorem 4 shows it is the equality case of Jensen's inequality, available whenever $f \geq 0$, and Section 6.5 shows that this $q$ is precisely the optimal proposal $q^*$. The proposal is a dial: this end of it reads variance $0$, and Section 6.6 exhibits the other end.

## 6 The Variance of Importance Sampling

### 6.1 The variance formula

$\hat\mu_n^{\mathrm{IS}}$ is a plain Monte Carlo estimator under $q$ for the function $g = f \cdot w$, so Theorem 2 under $q$ gives, whenever $\mathbb{E}_q[(fw)^2] < \infty$,
$$ \mathrm{Var}\big( \hat\mu_n^{\mathrm{IS}} \big) = \frac{\mathrm{Var}_q(fw)}{n} = \frac1n \Big( \mathbb{E}_q\big[ (fw)^2 \big] - \mu^2 \Big), $$
using $\mathbb{E}_q[fw] = \mu$ from Theorem 3 in the variance identity. Since $\mu$ is fixed by the problem, the proposal moves only the second moment. That is the one object to watch.

### 6.2 The object to watch

By LOTUS under $q$, with the integral over $\{q > 0\}$ as always,
$$ \mathbb{E}_q\big[ (fw)^2 \big] = \int f(x)^2\, \frac{p(x)^2}{q(x)^2}\, q(x)\, dx = \int \frac{f(x)^2\, p(x)^2}{q(x)}\, dx . $$
The proposal sits *in the denominator*: wherever $|f|\,p$ is large and $q$ is small, the ratio explodes. And $q$ is a density, of total mass $1$, so enlarging it somewhere means shrinking it elsewhere. Proposal design is therefore a budget-allocation problem, and Theorem 4 solves it exactly.

### 6.3 Jensen recalled, with the equality case proved

**Recall (Lecture 1) plus the equality case.** The square is convex, so $\mathbb{E}[Y^2] \geq (\mathbb{E}[Y])^2$ for any $Y$ with finite mean, and equality holds if and only if $Y$ is almost surely constant.

*Proof of the equality case, for this convex function only.*
$$ \mathbb{E}[Y^2] - (\mathbb{E} Y)^2 = \mathrm{Var}(Y) = \mathbb{E}\big[ (Y - \mathbb{E} Y)^2 \big], $$
the expectation of a nonnegative variable; it is $0$ if and only if $(Y - \mathbb{E} Y)^2 = 0$ almost surely, that is, if and only if $Y = \mathbb{E}[Y]$ almost surely. **End of proof.**

Lecture 1 proved the general concave form. For Theorem 4 the square, with this self-contained equality analysis, is all that is needed, and the equality case is not a footnote here: it is the *design principle*.

### 6.4 Theorem 4: the optimal proposal

**Theorem 4 (optimal proposal).** Fix $f$ and $p$ with $c = \mathbb{E}_p[|f(X)|] \in (0,\infty)$. Call $q$ *admissible* if it is a density satisfying Theorem 3's support condition. Then for every admissible $q$,
$$ \mathrm{Var}_q(f\,w) \;\geq\; c^2 - \mu^2, $$
and equality holds for the admissible proposal
$$ q^*(x) = \frac{|f(x)|\, p(x)}{c}, $$
which is moreover the *unique* minimizer up to almost-everywhere equivalence. Consequently
$$ \min_q \mathrm{Var}\big( \hat\mu_n^{\mathrm{IS}} \big) = \frac{c^2 - \mu^2}{n}, $$
and if $f \geq 0$ then $c = \mu$ and the minimum variance is $0$.

*Proof, step 1 (the floor).* Let $Y = |f(X)|\,w(X)$ under $X \sim q$, a nonnegative variable with $Y^2 = (fw)^2$. By Jensen and then Theorem 3 applied to $|f|$ (admissibility covers $|f|$, since $|f|p \neq 0$ exactly when $fp \neq 0$),
$$ \mathbb{E}_q\big[ (fw)^2 \big] = \mathbb{E}_q[Y^2] \;\geq\; \big( \mathbb{E}_q[Y] \big)^2 = \big( \mathbb{E}_p[\,|f|\,] \big)^2 = c^2 , $$
the same floor for every admissible $q$; subtract $\mu^2$ using Section 6.1. The floor is never negative, because $c = \mathbb{E}_p|f| \geq |\mathbb{E}_p f| = |\mu|$ by the triangle inequality, so $c^2 - \mu^2 \geq 0$.

*Step 2 (attained).* First, $q^*$ is a density, since $\int |f|p/c = c/c = 1$, and it is admissible, since $q^* > 0$ exactly where $|f|p > 0$. Under it, for every $x$ with $q^*(x) > 0$,
$$ |f(x)|\, w^*(x) = \frac{|f(x)|\,p(x)}{q^*(x)} = \frac{|f(x)|\,p(x)\,c}{|f(x)|\,p(x)} = c , $$
so $Y \equiv c$ is constant, $\mathbb{E}_{q^*}[(fw^*)^2] = c^2$, and the floor is met.

*Step 3 (uniqueness).* Suppose an admissible $q$ meets the floor. Then Jensen holds with equality, so by Section 6.3 the variable $Y = |f|\,w$ is constant $q$-almost surely, and the constant must be $\mathbb{E}_q[Y] = c$. Hence $|f(x)|\,p(x) = c\,q(x)$ for $q$-almost every $x$, i.e. $q = |f|p/c$ almost everywhere on $\{q > 0\}$. Integrating over $\{q > 0\}$,
$$ 1 = \int_{\{q>0\}} q = \frac1c \int_{\{q>0\}} |f|\,p \;\leq\; \frac1c \int |f|\,p = 1, $$
which forces the inequality to be an equality, so $\{q > 0\}$ carries all of $\int |f|p$ and $q = q^*$ almost everywhere. **End of proof.**

Three readings of the theorem:

1. The optimal proposal follows $|f| \cdot p$, not $p$: sample where the *integrand* lives, not where the target lives.
2. For $f \geq 0$ the minimum is zero, so a perfect estimator exists in principle.
3. The equality analysis explains the apparent magic of Section 5.6 structurally: the design goal is to make $|f|\,w$ constant, killing Jensen's gap.

### 6.5 Zero variance verified on the rare event

Take Section 5's example: $f = \mathbf 1\{x > 10\} \geq 0$ and $p = e^{-x}$, so $c = \mathbb{E}_p[|f|] = \mu = e^{-10}$ and
$$ q^*(x) = \frac{\mathbf 1\{x > 10\}\, e^{-x}}{e^{-10}} = e^{-(x-10)} \quad \text{on } x > 10, $$
exactly the shifted exponential guessed in Section 5.6, with minimum variance $c^2 - \mu^2 = 0$.

**The catch.** Writing down $q^*$ required $c$, which for $f \geq 0$ *is* the answer $\mu$; and even for signed $f$, sampling $|f|p/c$ exactly is typically as hard as the original problem. Theorem 4 is a compass, not an algorithm: aim the proposal at $|f| \cdot p$ and expect the variance to degrade gracefully with the aim. What Theorem 4 conspicuously does *not* provide is any upper bound over admissible $q$, because none exists, as the next example proves.

### 6.6 The infinite-variance example, computed in full

**Setup.** Target $p = \mathrm{Exp}(1)$ and $f(x) = x$, so $\mu = \mathbb{E}_p[X] = 1$ by Lecture 1. Proposal $q = \mathrm{Exp}(2)$, that is $q(x) = 2e^{-2x}$, which has a *lighter* tail than the target. Support: $q > 0$ on all of $[0,\infty)$, so it is admissible. The weight is
$$ w(x) = \frac{e^{-x}}{2e^{-2x}} = \frac{e^{x}}{2}, $$
growing exponentially. That is the red flag.

**All four moments.** By LOTUS under $q$:
$$ \mathbb{E}_q[w] = \int_0^\infty \frac{e^x}{2} \cdot 2e^{-2x}\, dx = \int_0^\infty e^{-x}\, dx = 1 . $$
$$ \mathbb{E}_q[w^2] = \int_0^\infty \frac{e^{2x}}{4} \cdot 2e^{-2x}\, dx = \int_0^\infty \tfrac12\, dx = \infty . $$
$$ \mathbb{E}_q[X w] = \int_0^\infty x\, \frac{e^x}{2} \cdot 2e^{-2x}\, dx = \int_0^\infty x\, e^{-x}\, dx = 1 . $$
$$ \mathbb{E}_q\big[ (X w)^2 \big] = \int_0^\infty x^2\, \frac{e^{2x}}{4} \cdot 2e^{-2x}\, dx = \int_0^\infty \frac{x^2}{2}\, dx = \infty . $$
The third integral is $\Gamma(2) = 1$, the exponential mean of Lecture 1. So the estimator is exactly unbiased, since the mean integral converges absolutely, while its variance is $+\infty$: the exponential growth of $w^2$ precisely cancels the exponential decay of $q$, leaving a non-integrable constant, and for $f = x$ a non-integrable $x^2/2$.

**Consequences, spelled out.** Theorem 2's formula is vacuous. Chebyshev gives no rate. The RMSE is undefined. The central limit theorem of Lecture 5 does not apply, so there is no $1/\sqrt n$ error bar at any $n$. Consistency *survives*: $fw$ has a finite mean, so the imported strong law of Section 2.2 still forces $\hat\mu_n^{\mathrm{IS}} \to 1$ almost surely, but with no useful speed. The sample-path behavior is the signature of heavy tails: long quiet stretches that look converged, punctuated by catastrophic jumps when a sample lands deep in the tail and its weight $e^x/2$ detonates. An estimator can be unbiased, consistent and useless simultaneously.

**Generalization to every rate.** Keep $p = \mathrm{Exp}(1)$ and take $q = \mathrm{Exp}(\lambda)$, that is $q(x) = \lambda e^{-\lambda x}$. Then
$$ \mathbb{E}_q[w^2] = \int_0^\infty \frac{e^{-2x}}{\lambda e^{-\lambda x}}\, dx = \frac1\lambda \int_0^\infty e^{-(2-\lambda)x}\, dx, $$
which equals $\dfrac{1}{\lambda(2-\lambda)}$ for $0 < \lambda < 2$, and $\infty$ for $\lambda \geq 2$.

The boundary is exactly $\lambda = 2$, where the integrand is the constant $\tfrac12$: that is the case computed above. So any proposal whose tail is lighter than $e^{-2x}$, meaning it decays at more than *twice* the target's rate, has infinite weight variance. A heavier-tailed check is $\lambda = \tfrac12$: the formula gives $\mathbb{E}_q[w^2] = \frac{1}{\frac12 \cdot \frac32} = \frac43$, matching the direct computation $2\int_0^\infty e^{-3x/2}\,dx = 2 \cdot \frac23 = \frac43$. Minimizing $\frac{1}{\lambda(2-\lambda)}$ over $\lambda$ gives $\lambda = 1$, i.e. $q = p$ and $w \equiv 1$, which is consistent: for the *weights alone*, meaning $f \equiv 1$, the best proposal is the target itself.

The practical **tail rule** follows: use proposal tails at least as heavy as the target's, and with a safety margin, since "equally heavy with a bad rate constant" already fails.

### 6.7 Weight degeneracy: the finite-$n$ face

Consider five samples with weights $(0.1,\ 0.2,\ 0.1,\ 0.1,\ 9.5)$, totalling $10.0$. Their shares of the total are $1$ percent, $2$ percent, $1$ percent, $1$ percent and $95$ percent. (The original note shows this as a histogram of five bars, one towering over the rest; the numbers are the whole content.) The weighted average is then essentially $f$ evaluated at one point: a single noisy draw wearing the costume of a five-sample average.

This is not a different disease from infinite variance but its finite-sample symptom. When $\mathbb{E}_q[w^2]$ is huge or infinite, the weight distribution is so skewed that in any finite batch one weight dominates. The diagnostic that quantifies "how many samples am I effectively holding" is the effective sample size of Section 7.6, and this five-weight example returns $n_{\mathrm{eff}} \approx 1.11$ there.

## 7 Self-Normalized Importance Sampling

### 7.1 The missing constant and unnormalized weights

This is failure mode (a) from Section 5.1: the target is known only up to normalization, $p = \tilde p / Z$, with $\tilde p$ evaluable (prior times likelihood, or $e^{-\mathrm{energy}}$) and
$$ Z = \int \tilde p $$
the impossible integral itself. The true weight $w = p/q$ needs $Z$. What is computable is
$$ \tilde w(x) = \frac{\tilde p(x)}{q(x)} = Z\, w(x), $$
off from the truth by the *same* unknown factor at every sample, so any ratio of $\tilde w$-weighted sums cancels it. Symmetrically, $q$ may also be unnormalized; any constant in the denominator cancels the same way.

**Standing support condition for this section:** $q > 0$ wherever $p > 0$, the full-support version from Section 5.5. It is needed because the denominator below estimates $Z = \int \tilde p$, an integral of $\tilde p$ over its *whole* support; there $f \equiv 1$, so Theorem 3's condition specializes to exactly this.

### 7.2 The estimator defined

**Definition (self-normalized IS).** For $X_1,\dots,X_n \stackrel{\mathrm{i.i.d.}}{\sim} q$,
$$ \hat\mu_n^{\mathrm{SN}} \;=\; \frac{\sum_{i=1}^n \tilde w(X_i)\, f(X_i)}{\sum_{i=1}^n \tilde w(X_i)} . $$

Replacing $\tilde w$ by $c\,\tilde w$ multiplies numerator and denominator by $c$, so the estimator is scale-invariant in the weights and hence $Z$-free. Equivalently it is the weighted average $\sum_i \bar w_i f(X_i)$ with normalized weights $\bar w_i = \tilde w(X_i)/\sum_j \tilde w(X_j)$, which sum to $1$.

### 7.3 Two Monte Carlo estimators, one ratio

Divide top and bottom by $n$ and inspect each piece as a plain Monte Carlo estimator under $q$, using Theorem 1 and LOTUS:
$$ A_n := \frac1n \sum_i \tilde w(X_i)\, f(X_i), \qquad \mathbb{E}[A_n] = \mathbb{E}_q[\tilde w f] = Z\,\mathbb{E}_q[wf] = Z\mu , $$
$$ B_n := \frac1n \sum_i \tilde w(X_i), \qquad \mathbb{E}[B_n] = \mathbb{E}_q[\tilde w] = Z\,\mathbb{E}_q[w] = Z , $$
using Theorem 3 for $\mathbb{E}_q[wf] = \mu$ and the full-support condition for $\mathbb{E}_q[w] = 1$ (Section 5.5). So the numerator is an unbiased importance-sampling estimate of $Z\mu$ and the denominator one of $Z$: two good estimators whose *ratio* is the object of study.

### 7.4 Consistency

**Lemma (continuous mapping, almost-sure version).** If $U_n \to u$ and $V_n \to v$ almost surely and $g$ is continuous at $(u,v)$, then $g(U_n, V_n) \to g(u,v)$ almost surely.

*Proof.* On the probability-one event where both convergences hold, they hold as ordinary numerical sequences, and continuity of $g$ at $(u,v)$ gives $g(U_n(\omega), V_n(\omega)) \to g(u,v)$ pointwise on that event. **End of proof.**

The lecture flags this step as named rather than proved. For *almost-sure* convergence it is, as just shown, elementary; the delicacy the flag alludes to arises for convergence *in probability*, which we bypass by using the strong law.

**Proposition (self-normalized IS is consistent).** Assume the Section 7.1 support condition and $\mathbb{E}_p[|f|] < \infty$. Then $\hat\mu_n^{\mathrm{SN}} \to \mu$ almost surely.

*Proof.* By the strong law (imported, Section 2.2) applied to the i.i.d. sequences $\tilde w(X_i) f(X_i)$ and $\tilde w(X_i)$, both with finite means computed in Section 7.3, we get $A_n \to Z\mu$ and $B_n \to Z$ almost surely. The map $g(u,v) = u/v$ is continuous at $(Z\mu, Z)$ because $Z > 0$: any $\tilde p$ not identically zero has positive total mass. Apply the lemma:
$$ \hat\mu_n^{\mathrm{SN}} = \frac{A_n}{B_n} \to \frac{Z\mu}{Z} = \mu \quad \text{almost surely.} $$
**End of proof.**

### 7.5 Bias: the ratio-estimator argument

Unbiasedness fails because expectation does not pass through ratios: $\mathbb{E}[A/B] \neq \mathbb{E}[A]/\mathbb{E}[B]$ in general. A mini-example: let $A = 1$ be constant and $B$ uniform on $\{1,3\}$. Then
$$ \mathbb{E}\!\left[ \frac AB \right] = \frac12\Big( 1 + \frac13 \Big) = \frac23 \;\neq\; \frac{\mathbb{E}[A]}{\mathbb{E}[B]} = \frac12 . $$
The intuition: the reciprocal is a convex function of $B$, so Jensen pushes $\mathbb{E}[1/B]$ *above* $1/\mathbb{E}[B]$, and here $\tfrac23 > \tfrac12$.

For the self-normalized estimator itself the bias can be quantified.

**Second-order expansion (formal, flagged).** Write $a = \mathbb{E}[A_n] = Z\mu$ and $b = \mathbb{E}[B_n] = Z$, and Taylor-expand $g(A,B) = A/B$ to second order around $(a,b)$, where $g_{aa} = 0$, $g_{ab} = -1/b^2$ and $g_{bb} = 2a/b^3$. Taking expectations,
$$ \mathbb{E}\big[ \hat\mu_n^{\mathrm{SN}} \big] - \mu \;\approx\; -\frac{\mathrm{Cov}(A_n, B_n)}{b^2} + \frac{a\,\mathrm{Var}(B_n)}{b^3} . $$
With $\mathrm{Var}(B_n) = Z^2\,\mathrm{Var}_q(w)/n$ and $\mathrm{Cov}(A_n, B_n) = Z^2\,\mathrm{Cov}_q(wf, w)/n$ (i.i.d. samples, Theorem-2-style bookkeeping), the factors of $Z$ cancel, and using $\mathbb{E}_q[w] = 1$ and $\mathbb{E}_q[wf] = \mu$,
$$ \mathrm{bias} \approx \frac{\mu\,\mathrm{Var}_q(w) - \mathrm{Cov}_q(wf, w)}{n} = \frac{\mu\big( \mathbb{E}_q[w^2] - 1 \big) - \big( \mathbb{E}_q[w^2 f] - \mu \big)}{n}, $$
which simplifies to
$$ \mathrm{bias} \approx -\frac{\mathbb{E}_q\big[ w^2 (f - \mu) \big]}{n} . $$

*Honesty.* This is a formal delta-method expansion; making it rigorous requires moment and regularity conditions, for which see Owen [1, ch. 9]. Its message stands: the bias is $O(1/n)$, so it vanishes an order faster than the $O(1/\sqrt n)$ statistical error. That is why the trade is almost always accepted: a small transient bias buys a computable, $Z$-free and often *lower-variance* estimator. Biased at every finite $n$, consistent in the limit: the promised contrast with Theorem 1.

### 7.6 Effective sample size: the derivation, not just the definition

**Step 1 (delta-method variance, formal, same caveat as Section 7.5).** A first-order expansion of $A_n/B_n$ around $(Z\mu, Z)$ gives
$$ \hat\mu_n^{\mathrm{SN}} - \mu \approx \frac{A_n - Z\mu}{Z} - \frac{\mu(B_n - Z)}{Z} = \frac1Z\big( A_n - \mu B_n \big), $$
and $A_n - \mu B_n = \tfrac1n \sum_i \tilde w_i (f_i - \mu)$ is a centered Monte Carlo average, since $\mathbb{E}_q[w(f - \mu)] = \mu - \mu = 0$. So by Theorem 2,
$$ \mathrm{Var}\big( \hat\mu_n^{\mathrm{SN}} \big) \;\approx\; \frac{\mathbb{E}_q\big[ w^2 (f-\mu)^2 \big]}{n} . $$

**Step 2 (the decoupling heuristic).** This is where "theorem" ends and "heuristic" begins, and the lecture flags it as such. Rewrite one factor exactly, using $w^2 q = w p$, to get $\mathbb{E}_q[w^2 (f-\mu)^2] = \mathbb{E}_p[w(f-\mu)^2]$. Then *assume* that $w$ and $(f-\mu)^2$ are approximately uncorrelated under $p$:
$$ \mathbb{E}_p\big[ w (f-\mu)^2 \big] \;\approx\; \mathbb{E}_p[w]\; \mathbb{E}_p\big[ (f-\mu)^2 \big] = \mathbb{E}_q[w^2]\; \sigma_f^2, $$
using $\mathbb{E}_p[w] = \mathbb{E}_q[w^2]$, the same rewrite read backwards. Then
$$ \mathrm{Var}\big( \hat\mu_n^{\mathrm{SN}} \big) \approx \frac{\sigma_f^2}{\,n/\mathbb{E}_q[w^2]\,} = \frac{\sigma_f^2}{n_{\mathrm{eff}}^{\mathrm{pop}}}, \qquad n_{\mathrm{eff}}^{\mathrm{pop}} = \frac{n\,\mathbb{E}_q[w]^2}{\mathbb{E}_q[w^2]} , $$
that is, the self-normalized batch behaves like a *plain* Monte Carlo batch of $n_{\mathrm{eff}}$ samples drawn from $p$. The factor $\mathbb{E}_q[w]^2 = 1$ is inserted to make the expression scale-invariant.

**Step 3 (plug-in).** Estimate the two moments by their sample versions using the computable $\tilde w_i$; scale-invariance makes the unknown $Z$ irrelevant:
$$ n_{\mathrm{eff}} \;=\; \frac{\big( \sum_i \tilde w_i \big)^2}{\sum_i \tilde w_i^2} , $$
Kong's formula [4]. Every approximation in the chain is now visible: a first-order Taylor step, a decoupling assumption that simply ignores the correlation between $f$ and $w$, and a plug-in. That is why the effective sample size is a *diagnostic* and not a theorem.

**Bounds, proved.** For nonnegative weights, not all zero, $1 \leq n_{\mathrm{eff}} \leq n$.

*Proof.* Upper bound: Cauchy-Schwarz applied to the vectors $(\tilde w_i)$ and $(1,\dots,1)$ gives $\big( \sum_i \tilde w_i \big)^2 \leq n \sum_i \tilde w_i^2$, with equality if and only if all weights are equal. Lower bound:
$$ \Big( \sum_i \tilde w_i \Big)^2 = \sum_i \tilde w_i^2 + \sum_{i \neq j} \tilde w_i \tilde w_j \;\geq\; \sum_i \tilde w_i^2 $$
since the cross terms are nonnegative, with equality if and only if at most one weight is nonzero. **End of proof.**

The two equality cases are exactly the two sanity checks that follow.

**Sanity checks.** Equal weights $\tilde w_i = c$ give $n_{\mathrm{eff}} = (nc)^2/(nc^2) = n$, full strength. The degenerate five of Section 6.7, namely $(0.1, 0.2, 0.1, 0.1, 9.5)$, has sum $10.0$ and sum of squares $0.01 + 0.04 + 0.01 + 0.01 + 90.25 = 90.32$, so
$$ n_{\mathrm{eff}} = \frac{10.0^2}{90.32} = \frac{100}{90.32} \approx 1.107 \approx 1.11 : $$
five samples, effectively one, matching the $95$ percent share of that one weight.

### 7.7 What the effective sample size is not

Three limitations, each traceable to a specific gap in the derivation.

1. *It ignores $f$*, which was discarded wholesale in Step 2's decoupling. If $f$ is extreme exactly where the weights are moderate, the variance can be terrible at a healthy $n_{\mathrm{eff}}$.
2. *It sees only sampled weights.* A heavy-tailed weight distribution can produce batch after batch of comfortable-looking weights before the first detonation; the plug-in of Step 3 cannot know about weights it has not drawn.
3. *It cannot detect support violations.* In the sharpest form, take the counterexample of Section 5.3: there every sampled weight equals $\tfrac34$, all equal, so $n_{\mathrm{eff}} = n$, the diagnostic's *best possible* reading, while the estimator converges to $0$ instead of $\tfrac14$.

The effective sample size grades the weights you have; it says nothing about the mass you never see. The standard reading is therefore one-directional: $n_{\mathrm{eff}} \ll n$ reliably means *fix the proposal*, while $n_{\mathrm{eff}} \approx n$ does not certify health. Cheap, universal, imperfect: a dashboard light, not a gauge.

### 7.8 Where self-normalized IS runs

Posterior inference, where $Z$ is unknown by construction; particle filters, meaning sequential reweight-and-resample loops, mentioned by name only here (see Robert and Casella [2]); and off-policy evaluation, where logged data from an old policy must judge a new one, which is Section 9's subject.

## 8 The Score-Function Gradient

### 8.1 A new kind of problem

Everything so far estimated a fixed expectation. Now the distribution itself is parametrized and *ours to move*: a policy or generator $\pi_\theta$, and the objective
$$ J(\theta) = \mathbb{E}_{X \sim \pi_\theta}\big[ R(X) \big] \;\longrightarrow\; \max_\theta , $$
with $X$ a trajectory and $R$ its return in reinforcement learning, or $X$ a generated text and $R$ a reward score in language-model alignment.

Gradient ascent needs $\nabla_\theta J$, and plain Monte Carlo cannot deliver it, because $\theta$ sits inside the *sampler* and not inside the integrand. Sampling $X_i \sim \pi_\theta$ and averaging $R(X_i)$ estimates the number $J(\theta)$ at one $\theta$; the samples carry no derivative. Differentiating the samples with respect to $\theta$ is meaningless as stated, unless the sampling is reparametrized, which is the alternative route discussed in Section 10.2. What is needed is an identity rewriting $\nabla_\theta \mathbb{E}_{\pi_\theta}[\cdot]$ as $\mathbb{E}_{\pi_\theta}[\cdot]$ *of something computable*, after which Theorem 1 applies to that something.

### 8.2 The log-derivative trick

**Identity.** For $g(\theta) > 0$ differentiable, the chain rule gives $\nabla_\theta \log g = (\nabla_\theta g)/g$; read backwards,
$$ \nabla_\theta\, g(\theta) = g(\theta)\, \nabla_\theta \log g(\theta) . $$
Applied to $g = \pi_\theta(x)$ at fixed $x$, which requires $\pi_\theta(x) > 0$, it converts a bare $\nabla \pi_\theta$ into $\pi_\theta$ times $\nabla \log \pi_\theta$, and a factor of $\pi_\theta$ is exactly what a sum needs in order to be readable as an expectation. This is the same multiply-and-divide move as importance sampling, which inserts $\pi_\theta/\pi_\theta$, aimed at a derivative instead of at a change of sampler.

### 8.3 Theorem 5, proof in full (finite case)

**Theorem 5 (score-function or REINFORCE identity [3]).** Let $\mathcal X$ be finite, let $\pi_\theta(x) > 0$ for all $x \in \mathcal X$ and be differentiable in $\theta$, and let $R : \mathcal X \to \mathbb{R}$ be fixed, with no $\theta$-dependence. Then
$$ \nabla_\theta\, \mathbb{E}_{X \sim \pi_\theta}\big[ R(X) \big] = \mathbb{E}_{X \sim \pi_\theta}\big[ R(X)\, \nabla_\theta \log \pi_\theta(X) \big] . $$

*Proof.*

*Step 1 (expand).* By LOTUS, $J(\theta) = \sum_{x \in \mathcal X} \pi_\theta(x)\, R(x)$, a finite sum of differentiable functions of $\theta$, the $R(x)$ being constants.

*Step 2 (swap).* Differentiation is linear, so it passes through the finite sum term by term:
$$ \nabla_\theta J(\theta) = \sum_x R(x)\, \nabla_\theta \pi_\theta(x) . $$

*Step 3 (log-derivative, then reread).* By Section 8.2, using $\pi_\theta(x) > 0$,
$$ \sum_x R(x)\, \nabla_\theta \pi_\theta(x) = \sum_x \pi_\theta(x)\, R(x)\, \nabla_\theta \log \pi_\theta(x) = \mathbb{E}_{\pi_\theta}\big[ R(X)\, \nabla_\theta \log \pi_\theta(X) \big], $$
the last step being LOTUS read backwards, which is legitimate precisely because the inserted $\pi_\theta$ factor is there. **End of proof.**

The vector $s_\theta(x) = \nabla_\theta \log \pi_\theta(x)$ is the *score*. The identity says that the gradient of an expectation over a moving distribution is an ordinary expectation, of reward times score, under that same distribution.

**Continuous $\mathcal X$: the interchange condition, stated precisely.** For densities, Step 2 becomes
$$ \nabla_\theta \int R\, \pi_\theta\, dx = \int R\, \nabla_\theta \pi_\theta\, dx , $$
which is *not* automatic. A sufficient condition: for each $\theta_0$ there are a neighborhood $U \ni \theta_0$ and an integrable envelope $g$ with
$$ \sup_{\theta \in U} \big| R(x)\, \nabla_\theta \pi_\theta(x) \big| \;\leq\; g(x), \qquad \int g(x)\, dx < \infty . $$
Then the mean value theorem bounds the difference quotients by $g$, and the dominated convergence theorem, **imported without proof** as flagged, lets the limit pass inside the integral. Steps 1 and 3 are unchanged. This is the honest asterisk on every policy-gradient theorem over continuous action spaces.

### 8.4 The REINFORCE estimator and its unbiasedness

**Definition and corollary.** For $X_1,\dots,X_n \stackrel{\mathrm{i.i.d.}}{\sim} \pi_\theta$,
$$ \hat g_n = \frac1n \sum_{i=1}^{n} R(X_i)\, \nabla_\theta \log \pi_\theta(X_i) \qquad \text{satisfies} \qquad \mathbb{E}[\hat g_n] = \nabla_\theta J(\theta) . $$

*Proof.* Apply Theorem 1 under $\pi_\theta$, componentwise in $\theta$, to the function $h(x) = R(x)\, s_\theta(x)$, each component of which is a fixed real-valued function of $x$ at the current $\theta$. Its expectation is $\nabla_\theta J$ by Theorem 5. **End of proof.**

What is required: sample from $\pi_\theta$, evaluate $R$ at the samples, differentiate $\log \pi_\theta$. What is pointedly *not* required: differentiate $R$. Black-box simulators and human ratings are therefore admissible rewards, which is the trick's entire industrial significance.

### 8.5 Worked check: the two-action sigmoid policy

Actions $\{a, b\}$ with $\pi_\theta(a) = \sigma(\theta) = (1 + e^{-\theta})^{-1}$ and $\pi_\theta(b) = 1 - \sigma(\theta)$; rewards $R(a) = 1$ and $R(b) = 0$.

**Direct route.** $J(\theta) = \sigma(\theta)\cdot 1 + (1 - \sigma(\theta))\cdot 0 = \sigma(\theta)$. The sigmoid derivative, derived: with $\sigma = (1 + e^{-\theta})^{-1}$,
$$ \sigma'(\theta) = \frac{e^{-\theta}}{(1 + e^{-\theta})^2} = \frac{1}{1 + e^{-\theta}} \cdot \frac{e^{-\theta}}{1 + e^{-\theta}} = \sigma(\theta)\big( 1 - \sigma(\theta) \big), $$
so $\nabla_\theta J = \sigma(1 - \sigma)$.

**Identity route.** The scores are $\nabla \log \sigma = \sigma'/\sigma = 1 - \sigma$ and $\nabla \log(1 - \sigma) = -\sigma'/(1 - \sigma) = -\sigma$. Then
$$ \mathbb{E}\big[ R\, \nabla \log \pi_\theta \big] = \sigma \cdot 1 \cdot (1 - \sigma) + (1 - \sigma) \cdot 0 \cdot (-\sigma) = \sigma(1 - \sigma), $$
matching the direct route exactly, for every $\theta$. At $\theta = 0$: $\sigma = \tfrac12$ and both sides equal $\tfrac12 \cdot \tfrac12 = \tfrac14$.

### 8.6 The baseline lemma, with the variance computation

**Lemma (mean-zero score).** Under Theorem 5's hypotheses, $\mathbb{E}_{\pi_\theta}\big[ \nabla_\theta \log \pi_\theta(X) \big] = 0$.

*Proof.* By LOTUS and the log-derivative identity, then differentiating the normalization $\sum_x \pi_\theta(x) = 1$, which is a finite sum so the swap is free (the continuous case needs the same envelope condition as Section 8.3):
$$ \mathbb{E}_{\pi_\theta}\big[ \nabla \log \pi_\theta \big] = \sum_x \pi_\theta(x)\, \frac{\nabla \pi_\theta(x)}{\pi_\theta(x)} = \nabla_\theta \sum_x \pi_\theta(x) = \nabla_\theta\, 1 = 0 . $$
**End of proof.**

**Corollary (baseline invariance).** For any constant $b$ not depending on the sample $X$,
$$ \mathbb{E}_{\pi_\theta}\big[ (R(X) - b)\, \nabla_\theta \log \pi_\theta(X) \big] = \nabla_\theta J(\theta) - b \cdot 0 = \nabla_\theta J(\theta), $$
by linearity, Theorem 5 for the first term and the lemma for the second: subtracting a baseline costs *no bias whatsoever*. **End of proof.** In reinforcement-learning practice $b$ may depend on the state, or on anything the score is conditionally mean-zero against; see Sutton and Barto [8, ch. 13] for the state-value baseline and the actor-critic family it generates. The constant case is what is needed here.

**Variance of the baselined estimator, and the optimal $b$.** Take $\theta$ scalar for clarity. Write $s = \nabla_\theta \log \pi_\theta(X)$ and $g_b = (R - b)\,s$. Since $\mathbb{E}[g_b] = \nabla J$ for every $b$,
$$ \mathrm{Var}(g_b) = \mathbb{E}\big[ (R - b)^2 s^2 \big] - (\nabla J)^2 = \mathbb{E}[R^2 s^2] - 2b\,\mathbb{E}[R\,s^2] + b^2\,\mathbb{E}[s^2] - (\nabla J)^2 , $$
a convex quadratic in $b$, since the leading coefficient $\mathbb{E}[s^2]$ is positive. It is minimized where the derivative vanishes:
$$ b^* = \frac{\mathbb{E}\big[ R(X)\, s^2 \big]}{\mathbb{E}\big[ s^2 \big]} \qquad \text{(per component for vector } \theta). $$
Any $b$ strictly between $0$ and $2b^*$ strictly reduces variance relative to no baseline. The lecture itself does not state $b^*$, only demonstrating a good $b$; it is included here because it explains the toy example below. The common practical choice $b = \mathbb{E}[R]$, the average reward, is *not* optimal in general: it coincides with $b^*$ exactly when $s^2$ is uncorrelated with $R$.

**The toy example.** Two-action policy at $\theta = 0$, so $\sigma = \tfrac12$ and the scores are $s(a) = 1 - \sigma = \tfrac12$ and $s(b) = -\sigma = -\tfrac12$. Single-sample estimates are $g_b = (R - b)s$. With $b = 0$:

- sample $a$, probability $\tfrac12$: $g_0 = 1 \cdot \tfrac12 = \tfrac12$.
- sample $b$, probability $\tfrac12$: $g_0 = 0 \cdot (-\tfrac12) = 0$.
- mean: $\tfrac12 \cdot \tfrac12 + \tfrac12 \cdot 0 = \tfrac14$.
- variance: $\tfrac12 \cdot \tfrac14 + \tfrac12 \cdot 0 - \tfrac{1}{16} = \tfrac{1}{16}$.

With $b = \tfrac12$:

- sample $a$, probability $\tfrac12$: $g_b = (1 - \tfrac12)\tfrac12 = \tfrac14$.
- sample $b$, probability $\tfrac12$: $g_b = (0 - \tfrac12)(-\tfrac12) = \tfrac14$.
- mean: $\tfrac14$.
- variance: $0$, since the estimate is the same constant on both outcomes.

Both means equal the true gradient $\tfrac14$ from Section 8.5, which is baseline invariance in action, and the variance drops from $\tfrac{1}{16}$ to exactly $0$. Why *exactly* zero? Check against $b^*$: here $s^2 = \tfrac14$ for both actions, a constant, so
$$ b^* = \frac{\mathbb{E}[R s^2]}{\mathbb{E}[s^2]} = \mathbb{E}[R] = \tfrac12 , $$
so the chosen baseline is precisely the optimal one, and with only two outcomes the optimally-baselined estimator becomes constant. Generic problems have more outcomes than parameters, and there $b^*$ reduces the variance without killing it.

### 8.7 Reading the identity, and the training loop

Each sample's contribution $(R(X_i) - b)\,\nabla \log \pi_\theta(X_i)$ pushes the log-probability of $X_i$ *up* in proportion to its baselined reward: reward-weighted log-likelihood ascent on the policy's own samples. The loop, which the original note draws as a pipeline diagram, is:

1. Sample $n$ outputs from $\pi_\theta$.
2. Score each with the black-box reward $R$.
3. Average $(R - b) \times \nabla \log \mathrm{prob}$, which is Theorem 5 plus Theorem 1 plus the baseline lemma.
4. Take a gradient-ascent step in $\theta$.
5. Repeat.

The estimator's practical weakness is its *variance*: the score can be high-dimensional and $R$ noisy. That is why baselines are never optional in practice, and why the reparameterization alternative of Section 10.2 wins whenever it is available.

## 9 Off-Policy Estimation and RLHF

### 9.1 Off-policy is Theorem 3

The data on disk was sampled from $\pi_b$, yesterday's policy and its logged interactions; the expectation wanted is under today's $\pi_\theta$. That is verbatim the importance-sampling setting, with target $\pi_\theta$ and proposal $\pi_b$:
$$ \mathbb{E}_{\pi_\theta}\big[ R(X) \big] = \mathbb{E}_{\pi_b}\!\left[ \frac{\pi_\theta(X)}{\pi_b(X)}\, R(X) \right] , $$
valid under Theorem 3's support condition: $\pi_b(x) > 0$ wherever $\pi_\theta(x) R(x) \neq 0$. In words, the behavior policy must have been capable of doing anything reward-relevant that the new policy can do. Violation is the silent-bias failure of Section 5.3: behaviors $\pi_\theta$ has learned that $\pi_b$ could never produce are simply invisible in the logged data.

### 9.2 Sequences multiply weights

**Claim.** For autoregressive policies over length-$T$ sequences $x = (x_1,\dots,x_T)$,
$$ w(x) = \frac{\pi_\theta(x)}{\pi_b(x)} = \prod_{t=1}^{T} \frac{\pi_\theta(x_t \mid x_{<t})}{\pi_b(x_t \mid x_{<t})} . $$

*Proof.* The chain rule of probability (Lecture 4) factorizes any joint distribution over a sequence as $\pi(x) = \prod_{t=1}^{T} \pi(x_t \mid x_{<t})$, which is exactly the form in which autoregressive models, language models included, are *defined*. Divide the two factorizations term by term. **End of proof.**

One modest per-token ratio, $T$ of them, multiplied: small systematic drifts compound geometrically, in either direction.

### 9.3 Degeneracy grows with length

**Setup (a flagged caricature).** Pretend the per-token ratios $w_t$ are independent under $\pi_b$ with $\mathbb{E}[w_t] = 1$ and $\mathbb{E}[w_t^2] = 1.1$ each. Real tokens are neither independent nor homogeneous; the caricature isolates the multiplicative mechanism. Then, for $T = 100$,
$$ \mathbb{E}\big[ w^2 \big] = \mathbb{E}\Big[ \prod_t w_t^2 \Big] = \prod_{t=1}^{100} \mathbb{E}\big[ w_t^2 \big] = 1.1^{100} = e^{100 \ln 1.1} \approx e^{9.531} \approx 13{,}780 , $$
using $\ln 1.1 = 0.09531$, so roughly $13{,}800$. Via the population effective sample size of Section 7.6 with $\mathbb{E}[w] = 1$, namely $n_{\mathrm{eff}} \approx n / \mathbb{E}[w^2]$, a million logged samples yield
$$ n_{\mathrm{eff}} \approx \frac{10^6}{13{,}780} \approx 73 . $$

*And the growth is the rule, not an artifact of the number $1.1$.* Each factor obeys $\mathbb{E}[w_t^2] \geq (\mathbb{E}[w_t])^2 = 1$ by Jensen, with equality only if $w_t$ is almost surely constant, that is, only if the per-token conditionals agree exactly. Any genuine disagreement makes its factor strictly exceed $1$, and the product grows exponentially in $T$. **End of proof.** Section 10.1 upgrades this from caricature to theorem via the Kullback-Leibler divergence.

### 9.4 Keep the ratio near one

The operational lesson: off-policy weights are statistically safe only while $\pi_\theta \approx \pi_b$. Practical algorithms therefore *constrain* the per-step ratio. Proximal policy optimization [5] clips $\pi_\theta/\pi_b$ into $[1-\epsilon,\, 1+\epsilon]$ inside a surrogate objective, and trust-region methods bound the update by a Kullback-Leibler ball. Both are deliberate bias-for-variance trades, collected in Section 10.3; the lecture keeps them at name-only level, as does this note beyond the pointer.

What the question "how far have we drifted" needs is a principled divergence between the two policies, which Lecture 2 built.

### 9.5 Kullback-Leibler recalled, and one connection made explicit

**Recall (Lecture 2).** $D(P \| Q) = \sum_x P(x) \log \tfrac{P(x)}{Q(x)} \geq 0$, with equality if and only if $P = Q$, proved in Lecture 2 via Jensen. The connection to today's objects: with $w = P/Q$,
$$ D(P \| Q) = \mathbb{E}_P\big[ \log w(X) \big] , $$
the mean *log-weight under the target*. Small divergence is precisely "typical log-weights near zero", that is, typical weights near one. So the Kullback-Leibler divergence is the natural drift meter for exactly the quantity importance sampling needs controlled. Section 10.1 makes the effective-sample-size consequence quantitative.

### 9.6 The RLHF-shaped objective

Reward-tuning a language model $\pi_\theta$ against a learned reward $r$, itself fit to human preference data, while staying near a reference model $\pi_{\mathrm{ref}}$:
$$ \max_\theta \;\; \mathbb{E}_{X \sim \pi_\theta}\big[ r(X) \big] \;-\; \beta\, D\big( \pi_\theta \,\|\, \pi_{\mathrm{ref}} \big) . $$

Every ingredient is today's mathematics or an earlier lecture's. The first term is estimated by sampling and climbed by Theorem 5 with a baseline. Sample reuse across updates is Theorem 3 reweighting, with the effective sample size watched and the ratios constrained. The second term is Lecture 2's divergence, the leash whose strength $\beta$ dials between reward-chasing and drift.

The scope note is worth repeating: this is the *schematic objective family* of RLHF-style methods, with InstructGPT [6] instantiating it and using proximal policy optimization [5] as the optimizer. Neither the lecture nor this note makes claims about the internals of any specific algorithm. This is a pointer, nothing more.

## 10 What the Lecture Leaves Out

### 10.1 When importance sampling fails in high dimension: degeneracy as a theorem

**Proposition.** Let $q > 0$ wherever $p > 0$ and $w = p/q$. Then
$$ \mathbb{E}_q\big[ w^2 \big] \;\geq\; e^{\,D(p \,\|\, q)}, \qquad \text{hence} \qquad \frac{n_{\mathrm{eff}}^{\mathrm{pop}}}{n} \approx \frac{1}{\mathbb{E}_q[w^2]} \;\leq\; e^{-D(p \| q)} . $$

*Proof.* Two lines from the course's own tools. Rewrite the second moment under the target: $\mathbb{E}_q[w^2] = \int p^2/q = \mathbb{E}_p[w]$. Then apply Jensen (Lecture 1) to the concave logarithm under $p$:
$$ \log \mathbb{E}_p[w] \;\geq\; \mathbb{E}_p[\log w] = D(p \,\|\, q) , $$
the last equality being Section 9.5. **End of proof.**

For product-form distributions in dimension $d$, or sequences of length $T$, the divergence is additive: $D(p^{\otimes d} \| q^{\otimes d}) = d \cdot D(p \| q)$, by Lecture 2. So any fixed per-coordinate mismatch makes the effective sample fraction decay *exponentially in $d$*. This is the rigorous core behind the caricature of Section 9.3 and the weight-degeneracy example of Section 6.7: importance sampling between genuinely different high-dimensional distributions is hopeless without structure. One either keeps the two distributions close (Section 9.4), resamples sequentially (particle filters), or abandons plain importance sampling for Markov-chain methods. All three are beyond today's scope.

### 10.2 Reparameterization versus REINFORCE

Theorem 5 is one of *two* standard routes to $\nabla_\theta \mathbb{E}_{\pi_\theta}[R]$. If the sampling can be *reparametrized*, meaning $X = g_\theta(\varepsilon)$ with $\varepsilon$ drawn from a fixed, $\theta$-free distribution and $g_\theta$ differentiable, then, under an interchange condition of the Section 8.3 type,
$$ \nabla_\theta\, \mathbb{E}_{\pi_\theta}[R(X)] = \nabla_\theta\, \mathbb{E}_{\varepsilon}\big[ R(g_\theta(\varepsilon)) \big] = \mathbb{E}_{\varepsilon}\big[ \nabla_\theta R(g_\theta(\varepsilon)) \big] . $$
The Gaussian case of Lecture 8 is the standard instance: $X = \mu_\theta + \Sigma_\theta^{1/2}\varepsilon$ with $\varepsilon \sim \mathcal N(0, I)$. The expectation is now over a *fixed* distribution, so the gradient passes onto the integrand and ordinary backpropagation applies.

Comparison. Reparameterization requires a differentiable $R$ and a reparameterizable, typically continuous $\pi_\theta$, and in exchange usually delivers far lower variance, because it uses the local information in $\nabla R$ while REINFORCE only correlates rewards with scores. REINFORCE requires neither: discrete outputs, tokens above all, and black-box rewards such as human preference are fine. That is exactly why the RLHF pipeline of Section 9 runs on score-function gradients while variational autoencoders and diffusion training run on reparameterization (Kingma and Welling [7]). The two are complementary tools, split along the question: is the sampler differentiable in its noise, and is the reward differentiable in the sample?

### 10.3 The bias-variance trades, collected

The lecture's quiet running theme, stated once: *unbiasedness is a purchasable property, and it is sometimes right to sell it.*

- Plain Monte Carlo and importance sampling are exactly unbiased.
- Self-normalized importance sampling sells unbiasedness, taking on a bias of order $1/n$ (Section 7.5), to buy freedom from $Z$, and often lower variance too, since normalized weights are bounded by $1$ while raw weights are not.
- Ratio clipping of the proximal-policy-optimization kind (Section 9.4) sells even consistency of the gradient direction, to buy bounded weights and stable updates.
- Baselines (Section 8.6) are the rare free lunch: variance reduction at zero bias.

Reading estimators through Lecture 7's decomposition $\mathrm{MSE} = \mathrm{Bias}^2 + \mathrm{Var}$ makes each trade a comparison of two terms rather than a matter of principle.

### 10.4 Smaller pointers

*Quasi-Monte Carlo*, named only in the lecture: low-discrepancy sequences achieve $O((\log n)^d/n)$ error for suitable integrands. See Owen [1, ch. 15-17].

*Optimal proposal for self-normalized IS*: the variance-minimizing proposal is $q \propto |f - \mu|\,p$, not $|f|\,p$, and the minimal variance is generally *not* zero. See Owen [1, ch. 9]. Theorem 4 above is the plain-importance-sampling statement only.

*The two imported analysis facts* remain the strong law of large numbers and the dominated convergence theorem (Sections 2.2 and 8.3). Everything else above is self-contained given Lectures 1 through 8.

## 11 References

1. A. B. Owen, *Monte Carlo theory, methods and examples*, 2013 onward (in progress, free online). The canonical modern reference: ch. 2 for plain Monte Carlo and error analysis, ch. 9 for importance sampling (Theorem 4's optimal proposal, self-normalized IS, and the delta-method variance and bias expansions of Sections 7.5 and 7.6), ch. 15-17 for quasi-Monte Carlo. https://artowen.su.domains/mc/
2. C. P. Robert, G. Casella, *Monte Carlo Statistical Methods*, 2nd ed., Springer, 2004. Ch. 3 for Monte Carlo integration and importance sampling, including the infinite-variance pathologies; later chapters for the Markov-chain and particle methods this lecture stops short of. doi:10.1007/978-1-4757-4145-2, https://doi.org/10.1007/978-1-4757-4145-2
3. R. J. Williams, "Simple statistical gradient-following algorithms for connectionist reinforcement learning," *Machine Learning* 8:229-256, 1992. The REINFORCE paper: Theorem 5's estimator, the baseline, and the name. doi:10.1007/BF00992696, https://doi.org/10.1007/BF00992696
4. A. Kong, "A note on importance sampling using standardized weights," Technical Report 348, Department of Statistics, University of Chicago, 1992. The origin of the effective-sample-size formula of Section 7.6. (Technical report; no stable link. It is cited as commonly referenced in the importance-sampling literature, for instance by Owen [1, ch. 9].)
5. J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov, "Proximal Policy Optimization Algorithms," 2017. The ratio-clipping surrogate behind Section 9.4. arXiv:1707.06347, https://arxiv.org/abs/1707.06347
6. L. Ouyang et al., "Training language models to follow instructions with human feedback," NeurIPS 2022. InstructGPT: the RLHF pipeline whose schematic objective Section 9.6 states, with the divergence-to-reference term. arXiv:2203.02155, https://arxiv.org/abs/2203.02155
7. D. P. Kingma, M. Welling, "Auto-Encoding Variational Bayes," ICLR 2014. The reparameterization trick of Section 10.2. arXiv:1312.6114, https://arxiv.org/abs/1312.6114
8. R. S. Sutton, A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. Ch. 13 for policy-gradient methods and baselines in their native reinforcement-learning setting. http://incompleteideas.net/book/the-book.html
9. Companion notes in this series: prob01 (LOTUS, variance, Jensen with equality case), prob02 (Kullback-Leibler divergence, additivity, nonnegativity via Jensen), prob04 (chain rule of probability), prob05 (law of large numbers, Chebyshev, central limit theorem, moment generating functions), prob06 (Hoeffding), prob07 (mean-squared-error decomposition, estimator bias), prob08 (Gaussian machinery, the reparameterization substrate). Each lives at `../prob0N-<topic>/prob0N-<topic>-note.md` in this accessible edition, or `-note.html` in the original.
