# Deep Learning Math, Lecture 5: Concentration Inequalities and the Law of Large Numbers

**About this file.** Screen-reader edition of the Lecture 5 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob05-concentration-note.html`). The three comparison tables are
written out as lists, one row per bullet. Nothing else is needed to read it.

**Convention.** Earlier notes in this series fixed all random variables to
finitely many values; this lecture needs Gaussians, so that restriction is
relaxed. A random variable may be discrete (pmf $p_X$, expectations are sums) or
continuous (pdf $f_X$, expectations are integrals), and every statement below
holds in both readings with sums and integrals interchanged. Where a claim
genuinely requires more care in the continuous case (differentiating under an
expectation, MGF uniqueness), the gap is flagged rather than papered over.

**Notation.** $\bar X_n = \frac1n \sum_{i=1}^n X_i$ is the sample mean,
$S_n = n \bar X_n$ the sum, $\mu = \mathbb{E}[X]$,
$\sigma^2 = \mathrm{Var}(X)$, and $\mathbf{1}\{A\}$ the indicator of the event
$A$. $M_X(t) = \mathbb{E}[e^{tX}]$ is the moment generating function (MGF).
$X \perp Y$ means $X$ and $Y$ are independent. $\Phi$ is the standard normal CDF
and $Q(\alpha) = 1 - \Phi(\alpha)$ its upper tail. $D(P \Vert Q)$ is the KL
divergence, in nats here. "a.s." means with probability 1.

**Background used.** Expectation, LOTUS and Jensen's inequality from Lecture 1;
KL divergence from Lecture 2; independence and factorization from Lecture 3.
These are cited, not re-proved.

**Contents.**

1. Why averages?
2. Warm-up: mean, variance, independence
3. Markov's inequality
4. Chebyshev's inequality
5. Law of large numbers
6. Moment generating functions
7. Chernoff bound
8. Three bounds head-to-head
9. Central limit theorem
10. References

## 1. Why Averages?

Every number a working AI pipeline reports is a *sample mean* standing in for an
expectation: a minibatch loss for the population loss, a test accuracy (the mean
of 0/1 correctness indicators) for the true accuracy, a Monte Carlo average for
an integral. The computable object and the wanted object are different in kind:

$$ \bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i \quad \text{(computable, random)},
   \qquad \mu = \mathbb{E}[X] \quad \text{(wanted, fixed)}. $$

The engineering question is quantitative: how large must $n$ be so that
$\Pr(|\bar{X}_n - \mu| \geq 0.01) \leq 0.05$, that is accuracy within plus or
minus 1 percent at 95 percent confidence? It is answered twice below: Chebyshev
gives the safe answer $n \geq 50{,}000$ (Section 4.7), Chernoff the much cheaper
$n \geq 18{,}444$ (Section 7.6).

One structural claim is worth stating as a slogan and then earning: **there is
only one inequality in this lecture**, Markov's. Chebyshev is Markov applied to
the transformed variable $(X-\mu)^2$; Chernoff is Markov applied to $e^{tX}$.
Each transform feeds more distributional knowledge into the same engine (mean
only, then mean and variance, then the whole MGF) and buys a faster tail decay
($1/\alpha$, then $1/\alpha^2$, then $e^{-c\alpha}$). The proofs below are
written so that this reuse is literal, not metaphorical.

One running example carries all numerics: $X_1, \dots, X_n$ i.i.d. fair coins,
Bernoulli($\frac12$), and the tail question $\Pr(\bar{X}_n \geq \frac34)$.

## 2. Warm-Up: Mean, Variance, Independence

### 2.1 Expectation, and the two properties that do today's work

From Lecture 1 (definitions and LOTUS proved there):
$\mathbb{E}[X] = \sum_x x\, p_X(x)$, and for any function $g$,
$\mathbb{E}[g(X)] = \sum_x g(x)\, p_X(x)$, the law of the unconscious
statistician; in the continuous case the same with $f_X\,dx$. Two consequences
are used constantly today. **Linearity**,
$\mathbb{E}[aX + bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y]$ with no independence
needed, is proved in the Lecture 1 note. **Monotonicity** is proved here.

**Lemma 2.1 (monotonicity of expectation).** (i) If $Z \geq 0$ for every
outcome, then $\mathbb{E}[Z] \geq 0$. (ii) If $X \leq Y$ pointwise and both have
finite expectations, then $\mathbb{E}[X] \leq \mathbb{E}[Y]$.

*Proof.* (i) $\mathbb{E}[Z] = \sum_z z\, p_Z(z)$ ranges only over values
$z \geq 0$ with weights $p_Z(z) \geq 0$; a sum (or integral) of non-negative
terms is non-negative. (ii) Apply (i) to $Z = Y - X \geq 0$ and use linearity:
$0 \leq \mathbb{E}[Y - X] = \mathbb{E}[Y] - \mathbb{E}[X]$. **End of proof.**

Monotonicity does the heavy lifting all lecture: it is the single step that
converts each pointwise domination -- $a\mathbf{1}\{X \geq a\} \leq X$ in
Section 3, and its squared and exponentiated cousins -- into an inequality
between numbers.

### 2.2 Variance

With $\mu = \mathbb{E}[X]$ assumed finite, the variance is
$\mathrm{Var}(X) = \mathbb{E}[(X-\mu)^2]$ whenever $\mathbb{E}[X^2]$ is finite,
and $\sigma = \sqrt{\mathrm{Var}(X)}$. The alternative form and the scaling rule,
with their one-line proofs:

$$ \mathbb{E}[(X-\mu)^2] = \mathbb{E}[X^2 - 2\mu X + \mu^2]
   = \mathbb{E}[X^2] - 2\mu\,\mathbb{E}[X] + \mu^2
   = \mathbb{E}[X^2] - \mu^2 $$

by linearity, $\mu$ being a constant, and

$$ \mathrm{Var}(aX) = \mathbb{E}[(aX - a\mu)^2]
   = a^2\, \mathbb{E}[(X-\mu)^2] = a^2 \mathrm{Var}(X). $$

Also $\mathrm{Var}(X + c) = \mathrm{Var}(X)$ for constant $c$, since centering
removes $c$.

**Bernoulli($p$).** $X^2 = X$, both values 0 and 1 being idempotent, so
$\mathbb{E}[X^2] = \mathbb{E}[X] = p$ and $\mathrm{Var}(X) = p - p^2 = p(1-p)$.
The fair coin has the largest variance a coin can have, which is the elementary
bound $p(1-p) \leq \frac14$: indeed
$\frac14 - p(1-p) = (p - \frac12)^2 \geq 0$, with equality if and only if
$p = \frac12$. So $\mathrm{Var} = \frac14$ at $p = \frac12$, and every numeric
below that uses $\sigma^2 = \frac14$ is also the worst case over all coins.

### 2.3 Independence and the product rule

From Lecture 3: $X \perp Y$ if and only if
$p_{X,Y}(x,y) = p_X(x)\,p_Y(y)$ for all $x,y$, densities factorizing in the
continuous case. The consequence the lecture needs:

**Lemma 2.2 (product rule).** If $X \perp Y$ and $g, h$ are functions with
$\mathbb{E}|g(X)| < \infty$ and $\mathbb{E}|h(Y)| < \infty$, then

$$ \mathbb{E}[g(X)\, h(Y)] = \mathbb{E}[g(X)]\; \mathbb{E}[h(Y)]. $$

*Proof.* LOTUS for the pair $(X,Y)$, then factorization, then separation of the
double sum:

$$ \sum_{x,y} g(x)h(y)\, p_{X,Y}(x,y)
   = \sum_{x,y} g(x)h(y)\, p_X(x) p_Y(y)
   = \Big(\sum_x g(x) p_X(x)\Big)\Big(\sum_y h(y) p_Y(y)\Big), $$

the last step because each summand is a product of an $x$-only and a $y$-only
factor, so summing over $y$ first pulls the $x$-factor out of the inner sum. For
infinite alphabets or densities the rearrangement is justified by absolute
convergence, which is what the integrability hypotheses are for; with finite sums
they are not needed. **End of proof.**

**Extension used silently later.** For $X_1, \dots, X_n$ mutually independent,
$\mathbb{E}\big[\prod_i g_i(X_i)\big] = \prod_i \mathbb{E}[g_i(X_i)]$, by
induction on $n$, using that $(X_1, \dots, X_{n-1})$ is jointly independent of
$X_n$ so that Lemma 2.2 applies with $g = \prod_{i < n} g_i$ treated as one
function of the first block. This $n$-fold version is exactly what turns the MGF
of a sum into a product of $n$ factors in Sections 6.7 and 9.

### 2.4 Variance adds under independence

**Lemma 2.3.** If $X \perp Y$, both with finite variances, then
$\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$.

*Proof.* Center: $\tilde{X} = X - \mu_X$ and $\tilde{Y} = Y - \mu_Y$, both of
mean 0, with $X + Y - \mathbb{E}[X+Y] = \tilde X + \tilde Y$. Expand the square
and use linearity:

$$ \mathrm{Var}(X+Y) = \mathbb{E}\big[(\tilde{X}+\tilde{Y})^2\big]
   = \mathbb{E}[\tilde{X}^2] + 2\,\mathbb{E}[\tilde{X}\tilde{Y}]
   + \mathbb{E}[\tilde{Y}^2]. $$

For the cross term, $\tilde X$ is a function of $X$ and $\tilde Y$ of $Y$, so
Lemma 2.2 gives
$\mathbb{E}[\tilde{X}\tilde{Y}]
= \mathbb{E}[\tilde{X}]\,\mathbb{E}[\tilde{Y}] = 0 \cdot 0 = 0$. The outer terms
are the two variances. **End of proof.**

**Fine print worth knowing.** The proof used only
$\mathbb{E}[\tilde X \tilde Y] = 0$, that is *uncorrelatedness*, which is weaker
than independence; and by induction, for $X_1, \dots, X_n$ pairwise uncorrelated,
in particular i.i.d.,
$\mathrm{Var}(\sum_i X_i) = \sum_i \mathrm{Var}(X_i)$, the cross terms vanishing
pairwise. This is the form used for $\bar X_n$ in Section 4.5.

### 2.5 The running example, and why "just compute it" is not an option

For the fair-coin average, linearity gives
$\mathbb{E}[\bar X_n] = \frac1n \sum_i \mathbb{E}[X_i]
= \frac1n \cdot n \cdot \frac12 = \frac12$. The tail question has an exact
answer, since $S_n = n \bar X_n \sim \mathrm{Bin}(n, \frac12)$:

$$ \Pr\!\big(\bar{X}_n \geq \tfrac34\big)
   = \Pr\!\big(S_n \geq \tfrac{3n}{4}\big)
   = \sum_{k = \lceil 3n/4 \rceil}^{n} \binom{n}{k} 2^{-n}, $$

the ceiling making the summation limit explicit for $n$ not divisible by 4. This
formula is used below to *grade* the bounds -- but it exists only because the
coin's full distribution is known. For a real loss or accuracy the distribution
is unknown, and the entire point of the lecture is bounds that consume only
partial knowledge: a mean (Markov), a mean and a variance (Chebyshev), an MGF
(Chernoff).

## 3. Markov's Inequality

### 3.1 Indicators: events as random variables

For an event $A$, the indicator $\mathbf{1}\{A\}$ equals 1 if $A$ happens and 0
otherwise. Its expectation is the probability, by direct computation over its two
values:

$$ \mathbb{E}\big[\mathbf{1}\{A\}\big]
   = 1 \cdot \Pr(A) + 0 \cdot \Pr(A^c) = \Pr(A). $$

So bounding a probability is the same task as bounding the mean of a
$\{0,1\}$-valued variable, which monotonicity (Lemma 2.1) knows how to do from a
pointwise domination.

### 3.2 Statement, both forms, all conditions

**Theorem 1 (Markov's inequality).** Let $X$ be a random variable with
$X \geq 0$ with probability 1 and $\mathbb{E}[X] < \infty$. Then:

*Threshold form.* For every $a > 0$,

$$ \Pr(X \geq a) \;\leq\; \frac{\mathbb{E}[X]}{a}. $$

*Relative form.* If moreover $\mathbb{E}[X] > 0$, then for every $\alpha > 0$,

$$ \Pr\!\big(X \geq \alpha\,\mathbb{E}[X]\big) \;\leq\; \frac{1}{\alpha}. $$

Conditions unpacked. (i) *Non-negativity* is essential -- see the counterexample
in 3.6 -- and is used exactly once in the proof. (ii) The threshold form is the
primitive one; the relative form is the substitution
$a = \alpha\,\mathbb{E}[X]$, which requires $\mathbb{E}[X] > 0$ so that $a > 0$;
if $\mathbb{E}[X] = 0$ then $X = 0$ a.s. and $\Pr(X \geq a) = 0$ anyway, so
nothing is lost. (iii) If $\mathbb{E}[X] = \infty$ the threshold form is
trivially true but empty. (iv) The bound is informative only for
$a > \mathbb{E}[X]$, equivalently $\alpha > 1$; otherwise the right-hand side is
at least 1 and says nothing a probability did not already satisfy.

### 3.3 Proof, with the skipped justifications restored

**Step 1 (dominate).** Claim: for every outcome,
$a\,\mathbf{1}\{X \geq a\} \leq X$. Case $X \geq a$: the left side is
$a \cdot 1 = a \leq X$ by the very event being indicated. Case $X < a$: the left
side is $a \cdot 0 = 0 \leq X$ -- and *this* step is where non-negativity of $X$
enters, and the only place it is used.

**Step 2 (average).** A pointwise inequality between random variables passes to
expectations by Lemma 2.1(ii), and the constant $a$ exits by linearity:

$$ a\, \mathbb{E}\big[\mathbf{1}\{X \geq a\}\big]
   = \mathbb{E}\big[a\,\mathbf{1}\{X \geq a\}\big] \;\leq\; \mathbb{E}[X]. $$

**Step 3 (read off).** The indicator's mean is the probability (Section 3.1), so
$a \Pr(X \geq a) \leq \mathbb{E}[X]$; divide by $a > 0$, which preserves the
inequality:

$$ \Pr(X \geq a) \leq \frac{\mathbb{E}[X]}{a}, $$

and with $a = \alpha\,\mathbb{E}[X]$,

$$ \Pr\big(X \geq \alpha\,\mathbb{E}[X]\big)
   \leq \frac{\mathbb{E}[X]}{\alpha\,\mathbb{E}[X]} = \frac1\alpha. $$

**End of proof.**

### 3.4 Coin answer, verified

$\bar X_n \geq 0$, being an average of 0s and 1s, with
$\mathbb{E}[\bar X_n] = \frac12$; the threshold $\frac34$ is
$\alpha = \frac{3/4}{1/2} = \frac32$ means, so

$$ \Pr\!\big(\bar{X}_n \geq \tfrac34\big) \;\leq\; \frac{1/2}{3/4}
   = \frac{2}{3} \approx 0.67. $$

The bound is valid for every $n$ and *independent of* $n$: Markov consumes only
the mean, and $\mathbb{E}[\bar X_n] = \frac12$ does not change with $n$. Markov
is structurally blind to averaging.

### 3.5 Tightness: the two-point distribution, and the equality condition

Knowing only the mean, Markov cannot be improved. Fix $\mu > 0$ and a threshold
$a \geq \mu$ and let $X = a$ with probability $\mu/a$ and $X = 0$ with
probability $1 - \mu/a$. The condition $a \geq \mu$ makes
$\mu/a \in (0, 1]$ a legitimate probability. Check:
$\mathbb{E}[X] = a \cdot \frac{\mu}{a} + 0 = \mu$, and
$\Pr(X \geq a) = \Pr(X = a) = \frac{\mu}{a}$, exactly Markov's bound. So among
all non-negative variables with mean $\mu$, the supremum of $\Pr(X \geq a)$
*equals* $\mu/a$: any improvement must feed in more than the mean.

**Equality analysis.** Equality in Theorem 1 forces both inequalities in the
proof to be equalities, that is
$\mathbb{E}[X - a\mathbf{1}\{X \geq a\}] = 0$ with a non-negative integrand, so
$X = a\mathbf{1}\{X \geq a\}$ a.s.: $X$ takes only the values 0 and $a$. The
two-point example is the *only* shape achieving equality. Conversely this
diagnoses when Markov is loose: any mass strictly between 0 and $a$, or above
$a$, is thrown away. For $\bar X_n$, whose mass piles up near $\frac12$, almost
everything is thrown away -- hence the uselessly constant $\frac23$.

### 3.6 Non-negativity is essential; how Markov is actually used

Counterexample, checked: $X = \pm 1$ with probability $\frac12$ each has
$\mathbb{E}[X] = 0$, so the illegal threshold form at $a = 1$ would claim
$\Pr(X \geq 1) \leq 0/1 = 0$; the truth is $\Pr(X \geq 1) = \frac12$. The failure
is in proof Step 1: on the branch $X < a$ the step function's value 0 no longer
sits below $X$ when $X$ can be negative. In practice Markov is rarely applied
raw; it is the *engine*. Sections 4 and 7 apply it to $(X-\mu)^2$ and $e^{tX}$,
both non-negative *by construction* -- which is precisely why those transforms
are chosen.

## 4. Chebyshev's Inequality

### 4.1 Statement, both forms, all conditions

**Theorem 2 (Chebyshev's inequality).** Let $X$ have finite mean $\mu$ and
finite variance $\sigma^2$, that is $\mathbb{E}[X^2] < \infty$, with no sign or
boundedness assumption on $X$. Then:

*Relative form.* If $\sigma > 0$, for every $\alpha > 0$,

$$ \Pr\!\big(|X - \mu| \geq \alpha\sigma\big) \;\leq\; \frac{1}{\alpha^2}. $$

*Absolute form.* For every $\epsilon > 0$,

$$ \Pr\!\big(|X - \mu| \geq \epsilon\big) \;\leq\; \frac{\sigma^2}{\epsilon^2}. $$

Conditions unpacked. (i) Existence of the variance is the real hypothesis: for a
heavy-tailed $X$ with $\mathbb{E}[X^2] = \infty$ the $\epsilon$-form is vacuous
and the $\alpha\sigma$-form is not even well posed. (ii) The two forms translate
via $\epsilon = \alpha\sigma$, which needs $\sigma > 0$; if $\sigma = 0$ then
$X = \mu$ a.s. and the $\epsilon$-form gives the correct 0. (iii) The bound is
two-sided, controlling $|X-\mu|$ and hence both tails at once, and is informative
only for $\alpha > 1$.

### 4.2 Proof: Markov on the squared deviation

**Step 1 (square the event).** For $c > 0$, the map $u \mapsto u^2$ is strictly
increasing on $u \geq 0$, so for the non-negative quantity $|X - \mu|$,

$$ |X-\mu| \geq c \iff (X-\mu)^2 \geq c^2. $$

These are the *same event* described twice, hence have the same probability. Set
$Y = (X-\mu)^2$ and check Markov's entry ticket: $Y \geq 0$, being a square, and
$\mathbb{E}[Y] = \sigma^2 < \infty$ by the variance hypothesis -- the definition
of variance, no computation needed.

**Step 2 (Markov).** Theorem 1, threshold form, on $Y$ at level $c^2$:

$$ \Pr\!\big(|X - \mu| \geq c\big) = \Pr\!\big(Y \geq c^2\big)
   \;\leq\; \frac{\mathbb{E}[Y]}{c^2} = \frac{\sigma^2}{c^2}. $$

With $c = \epsilon$ this is the $\epsilon$-form; with $c = \alpha\sigma$ the
$\sigma^2$ cancels, $\sigma^2/(\alpha^2\sigma^2) = 1/\alpha^2$.
**End of proof.**

Note what squaring bought, beyond the $1/\alpha^2$ decay: *two-sidedness*.
Markov alone can only see one tail of a non-negative variable; the square folds
both tails of $X$ into one tail of $Y$.

### 4.3 Tightness: a three-point distribution achieving equality

Chebyshev, like Markov, cannot be improved from its inputs alone. The witness,
for any $\alpha \geq 1$: let $X = \mu + \alpha\sigma$ with probability
$\frac{1}{2\alpha^2}$, $X = \mu$ with probability $1 - \frac{1}{\alpha^2}$, and
$X = \mu - \alpha\sigma$ with probability $\frac{1}{2\alpha^2}$. Check:
$\mathbb{E}[X] = \mu$ by symmetry;
$\mathrm{Var}(X) = (\alpha\sigma)^2 \cdot \frac{1}{2\alpha^2} \cdot 2
= \sigma^2$; and
$\Pr(|X - \mu| \geq \alpha\sigma)
= \frac{1}{2\alpha^2} + \frac{1}{2\alpha^2} = \frac{1}{\alpha^2}$, equality. The
condition $\alpha \geq 1$ keeps the middle probability non-negative. So the
$\alpha\sigma$-rule is exactly the worst case; distributions with light tails,
next subsection, sit far below it.

### 4.4 The $\alpha\sigma$-rule, re-derived

Chebyshev's guarantee is $1/\alpha^2$; the Gaussian truth is the two-sided tail
$2Q(\alpha)$. Three deviation levels, each giving Chebyshev's bound and then the
Gaussian value:

- $\alpha = 2$: Chebyshev $\frac14 = 25$ percent; Gaussian
  $2Q(2) = 0.0455$, about 4.6 percent.
- $\alpha = 3$: Chebyshev $\frac19 \approx 11.1$ percent; Gaussian
  $2Q(3) = 0.0027$, that is 0.27 percent.
- $\alpha = 5$: Chebyshev $\frac1{25} = 4$ percent; Gaussian
  $2Q(5) = 5.73 \times 10^{-7}$, about 0.00006 percent.

The lesson is the loose-versus-tight diagnostic for Chebyshev: it is *tight* for
the adversarial three-point shape of 4.3, and *loose by orders of magnitude* --
a factor of roughly 70,000 at five standard deviations -- for light-tailed
distributions, because two numbers, $\mu$ and $\sigma^2$, cannot see tail
lightness. Chernoff's whole purpose is to feed that missing information in.

### 4.5 The key computation: the variance of the sample mean

**Lemma 4.1.** For $X_1, \dots, X_n$ i.i.d., pairwise uncorrelated being enough,
with variance $\sigma^2$:

$$ \mathrm{Var}(\bar{X}_n)
   = \mathrm{Var}\!\Big(\frac1n \sum_{i=1}^n X_i\Big)
   = \frac{1}{n^2}\,\mathrm{Var}\!\Big(\sum_{i=1}^n X_i\Big)
   = \frac{1}{n^2} \cdot n\sigma^2
   = \frac{\sigma^2}{n}. $$

The second equality is the scaling rule of 2.2 with $a = \frac1n$; the third is
the pairwise-uncorrelated induction noted after Lemma 2.3. **End of proof.**

This single identity powers everything that follows: the coin bound $4/n$, the
weak law of large numbers, error bars, and the variance argument for minibatching
reused by name in opt04.

### 4.6 Coin answer, verified

Fair coin: $\mathrm{Var}(\bar X_n) = \frac{1/4}{n} = \frac{1}{4n}$. The one-sided
tail sits inside the two-sided event, since $\bar X_n \geq \frac34$ implies
$|\bar X_n - \frac12| \geq \frac14$, so the first event's probability is at most
the second's by monotonicity of probability under set inclusion:

$$ \Pr\!\big(\bar{X}_n \geq \tfrac34\big)
   \;\leq\; \Pr\!\big(|\bar{X}_n - \tfrac12| \geq \tfrac14\big)
   \;\leq\; \frac{1/(4n)}{(1/4)^2} = \frac{16}{4n} = \frac{4}{n}, $$

the last step by the $\epsilon$-form. Numerically: $n = 16$ gives
$4/16 = 0.25$; $n = 100$ gives $0.04$; $n = 400$ gives $0.01$. This is the first
bound that improves with $n$ -- because variance, unlike the mean, sees
averaging.

### 4.7 Sample-size answer: 50,000, verified

Demand $\Pr(|\bar X_n - \mu| \geq \epsilon) \leq \delta$. The $\epsilon$-form
applied to $\bar X_n$, which has mean $\mu$ and variance $\sigma^2/n$ by
Lemma 4.1, delivers this as soon as $\frac{\sigma^2}{n\epsilon^2} \leq \delta$,
that is $n \geq \frac{\sigma^2}{\epsilon^2\delta}$. With the Section 1 demand,
taking $\sigma^2 = \frac14$ for a coin, the worst case by 2.2 and so
distribution-safe over all coins, and $\epsilon = 0.01$, $\delta = 0.05$:

$$ n \;\geq\; \frac{1/4}{(0.01)^2 \cdot 0.05}
   = \frac{0.25}{10^{-4} \cdot 0.05}
   = \frac{0.25}{5 \times 10^{-6}} = 50{,}000. $$

Note the scaling this encodes: $n \propto 1/\delta$. Halving the failure
probability doubles the samples, a cost polynomial in $1/\delta$. Chernoff will
make this logarithmic in $1/\delta$ (Section 7.7).

### 4.8 Omitted refinement: the one-sided (Cantelli) inequality

Folding a one-sided question into a two-sided bound costs a little. The one-sided
analogue of Chebyshev is a two-line illustration of "choose the transform".

**Cantelli's inequality.** For $X$ with mean $\mu$, variance $\sigma^2$, and any
$a > 0$:

$$ \Pr(X - \mu \geq a) \leq \frac{\sigma^2}{\sigma^2 + a^2}. $$

*Proof.* For any $\lambda \geq 0$, the event $\{X - \mu \geq a\}$ is contained in
$\{(X - \mu + \lambda)^2 \geq (a+\lambda)^2\}$: on the event,
$X - \mu + \lambda \geq a + \lambda > 0$, and then square. Markov on the
non-negative $(X-\mu+\lambda)^2$, whose mean is $\sigma^2 + \lambda^2$ -- expand;
the cross term has mean 0 -- gives

$$ \Pr(X - \mu \geq a) \;\leq\; \frac{\sigma^2 + \lambda^2}{(a+\lambda)^2}, $$

minimized at $\lambda = \frac{\sigma^2}{a}$, which yields
$\frac{\sigma^2}{\sigma^2 + a^2}$. **End of proof.**

For the coin,
$\Pr(\bar X_n \geq \frac34)
\leq \frac{1/(4n)}{1/(4n) + 1/16} = \frac{4}{n + 4}$: a hair better than $4/n$,
and a preview of Chernoff's structure -- introduce a free parameter, optimize it
at the end.

## 5. Law of Large Numbers

### 5.1 Convergence in probability, stated precisely

**Definition.** Random variables $Z_n$ converge *in probability* to the constant
$c$, written $Z_n \xrightarrow{p} c$, if for *every* $\epsilon > 0$,

$$ \lim_{n\to\infty} \Pr\big(|Z_n - c| > \epsilon\big) = 0. $$

Quantifier order matters: the tolerance $\epsilon$ is fixed *before* $n$ grows,
and the statement must hold for every fixed band, however narrow. Whether one
writes $> \epsilon$ or $\geq \epsilon$ inside is immaterial: the $\geq \epsilon$
event contains the $> \epsilon$ event and is contained in the $> \epsilon/2$
event, so the two formulations define the same notion. The definition extends
verbatim to a random limit $Z$ in place of $c$; today only constant limits
appear.

### 5.2 The weak law of large numbers, with proof and rate

**Theorem 3 (weak law of large numbers).** Let $X_1, X_2, \dots$ be i.i.d. with
finite mean $\mu$ and finite variance $\sigma^2$. Then
$\bar{X}_n \xrightarrow{p} \mu$.

*Proof.* Fix $\epsilon > 0$. The average $\bar X_n$ has mean $\mu$ by linearity
and variance $\sigma^2/n$ by Lemma 4.1. Chebyshev's $\epsilon$-form applied to
the random variable $\bar X_n$:

$$ \Pr\big(|\bar{X}_n - \mu| > \epsilon\big)
   \;\leq\; \Pr\big(|\bar{X}_n - \mu| \geq \epsilon\big)
   \;\leq\; \frac{\mathrm{Var}(\bar X_n)}{\epsilon^2}
   = \frac{\sigma^2}{n\epsilon^2}. $$

With $\epsilon$ and $\sigma$ fixed, the right side tends to 0 as
$n \to \infty$. Since $\epsilon > 0$ was arbitrary, this is convergence in
probability. **End of proof.**

The proof gives more than convergence: an explicit *rate*,
$\sigma^2/(n\epsilon^2)$. This is what "estimate by sampling" recipes actually
invoke -- test accuracy, minibatch gradients (per coordinate, the batch-mean
standard deviation shrinks like $1/\sqrt{B}$ since the variance shrinks like
$1/B$), Monte Carlo. Each is Theorem 3 applied to a different choice of $X_i$,
not a new theorem.

### 5.3 The strong law and the hierarchy of convergence modes

**Strong law of large numbers (Kolmogorov; stated, not proved).** If
$X_1, X_2, \dots$ are i.i.d. with $\mathbb{E}|X_1| < \infty$ and mean $\mu$,
then

$$ \Pr\Big( \lim_{n\to\infty} \bar{X}_n = \mu \Big) = 1, $$

almost-sure convergence, written $\bar X_n \xrightarrow{a.s.} \mu$.

Two upgrades over Theorem 3 at once. The *mode* is stronger: almost-sure
convergence means the single random sequence $n \mapsto \bar X_n(\omega)$
converges for all outcomes but a probability-zero set, whereas convergence in
probability only controls each time $n$ separately. And the *hypothesis* is
weaker: a finite mean suffices, with no variance needed. The proof is genuinely
harder; see [5, Thm. 2.4.1] or Etemadi's elementary proof [7]. The general
hierarchy, for the record: almost-sure convergence implies convergence in
probability, which implies convergence in distribution (Section 9.1), and none of
the arrows reverses in general; for a *constant* limit the last arrow does
reverse. See [5, Ch. 2-3].

### 5.4 The law-of-large-numbers numerics, audited

A simulated sample path, with a fixed seed, passes through
$\bar X_{10} = 0.30$ and $\bar X_{200} = 0.49$ -- illustrative, not
re-derivable, and plausible: at $n = 200$ the standard deviation of $\bar X_n$ is
$\frac{1}{2\sqrt{200}} \approx 0.035$, so 0.49 is well within one standard
deviation of $\frac12$.

The vanishing of the tails is exact and re-computable:

$$ \Pr\big(|\bar X_n - \tfrac12| \geq \tfrac14\big)
   = \Pr\big(S_n \leq \tfrac{n}{4}\big) + \Pr\big(S_n \geq \tfrac{3n}{4}\big),
   \qquad S_n \sim \mathrm{Bin}(n,\tfrac12), $$

giving, at $n = 4, 8, 12, 16, 20, 24$ respectively,

$$ 0.6250, \quad 0.2891, \quad 0.1460, \quad 0.0768, \quad 0.0414,
   \quad 0.0227, $$

which rounds to $0.63, 0.29, 0.15, 0.08, 0.04, 0.02$. Sample computation at
$n = 8$: $2\sum_{k=0}^{2}\binom{8}{k} 2^{-8}
= 2(1 + 8 + 28)/256 = 74/256 = 0.2891$, the factor 2 being the tail symmetry of
$\mathrm{Bin}(n,\frac12)$.

The size of the Chebyshev gap at $n = 16$:

$$ \Pr(\bar X_{16} \geq \tfrac34) = \Pr(S_{16} \geq 12)
   = \frac{\binom{16}{12} + \binom{16}{13} + \binom{16}{14}
     + \binom{16}{15} + \binom{16}{16}}{65536} $$

$$ = \frac{1820 + 560 + 120 + 16 + 1}{65536} = \frac{2517}{65536} = 0.0384, $$

so Chebyshev's 0.25 is off by a factor $0.25/0.0384 = 6.5$ -- and the gap grows
without bound in $n$, since the truth decays exponentially (Section 8) while
$4/n$ decays polynomially.

### 5.5 Source-notes discrepancies, for the record

The LaTeX source's remark on the law of large numbers contains two slips, both
confirmed against the correct derivation above: (i) it declares that "$Z_n$ is a
random variable with mean 0 and variance $\sigma^2/n$" -- the mean of
$Z_n = \bar X_n$ is $\mu$, not 0; (ii) its final Chebyshev bound reads
$\frac{\sigma^2}{n\epsilon}$, whereas the denominator must be $n\epsilon^2$, the
$\epsilon$-form with $\epsilon$ squared, as in Theorem 3's proof. A third, minor:
the source's Gaussian-sum exercise sentence is truncated mid-sentence, reading
"Show that the sum of independent Gaussian $X \sim \mathcal{N}(\mu_1,
\sigma_1^2)$"; it is completed as the worked example verified in Section 6.7
below.

## 6. Moment Generating Functions

### 6.1 Definition, domain, and finiteness: the fine print

**Definition (moment generating function).** For a random variable $X$,

$$ M_X(t) = \mathbb{E}\big[e^{tX}\big] \in (0, \infty],
   \qquad t \in \mathbb{R}. $$

Because $e^{tX} > 0$, the expectation always makes sense as a number in
$(0, \infty]$ -- but it may be $+\infty$. Fine print behind "finite at the $t$
used": (i) $M_X(0) = \mathbb{E}[1] = 1$ always. (ii) The *effective domain*
$\{t : M_X(t) < \infty\}$ is an interval containing 0, by convexity of $M_X$,
which follows from convexity of $t \mapsto e^{tx}$ for each fixed $x$; it may be
all of $\mathbb{R}$ (bounded variables, Gaussians), a half-line, or the
degenerate $\{0\}$. (iii) Existence of all moments does *not* guarantee a
nondegenerate domain: a random variable with density proportional to
$(1+|x|)^{-4}$ has finite mean and variance yet $M_X(t) = \infty$ for every
$t \neq 0$, since $e^{tx}$ outruns any polynomial decay. This is exactly the gap
that makes the central-limit sketch of Section 9 non-rigorous under the stated
hypotheses. (iv) For every variable in this lecture -- Bernoulli and its sums,
which are bounded, and Gaussians -- $M_X$ is finite on all of $\mathbb{R}$, so
the fine print never bites in the worked examples.

### 6.2 The moment machine: derivatives at zero are moments

Differentiate under the expectation:

$$ M_X'(t) = \mathbb{E}\Big[\tfrac{\partial}{\partial t} e^{tX}\Big]
   = \mathbb{E}\big[X e^{tX}\big], \qquad
   M_X''(t) = \mathbb{E}\big[X^2 e^{tX}\big], $$

and at $t = 0$, where $e^{0 \cdot X} = 1$: $M_X'(0) = \mathbb{E}[X]$ and
$M_X''(0) = \mathbb{E}[X^2]$; iterating,
$M_X^{(k)}(0) = \mathbb{E}[X^k]$ for every $k \geq 1$.

**Justifying the swap.** For a finite-valued $X$ the expectation is a finite sum
and differentiating termwise is elementary calculus -- nothing to check, and this
covers the Bernoulli and coin computations. In general the swap is legitimate
whenever $M_X$ is finite on an open interval $(-t_0, t_0)$ around 0: then $M_X$
is infinitely differentiable there and the formula holds, by a
dominated-convergence argument [4, Sec. 21; 5, Sec. 2.3 exercises]. We state this
and use it; the proof belongs to a measure-theory course. Combined with
$\mathrm{Var}(X) = \mathbb{E}[X^2] - \mu^2$ from 2.2, the first two derivatives
at 0 already recover mean and variance -- the fact the central-limit sketch runs
on.

### 6.3 The Taylor view

Expanding $e^{tX} = \sum_{k \geq 0} (tX)^k / k!$ and taking expectations
termwise,

$$ M_X(t) = 1 + \mathbb{E}[X]\,t + \frac{\mathbb{E}[X^2]}{2}\,t^2
   + \frac{\mathbb{E}[X^3]}{6}\,t^3 + \cdots, $$

so the moments are the Taylor coefficients, times $k!$, hence the name "moment
generating". Termwise expectation is again automatic for finite-valued $X$; in
general it is valid inside the interval of finiteness [4, Sec. 21]. The behavior
of $M_X$ *near $t = 0$* is governed by the low moments, and this locality is what
makes the central limit theorem universal: after standardization, all
distributions share the same expansion $1 + t^2/2 + \cdots$ to second order, and
the $1/\sqrt{n}$ scaling pushes everything into that shared neighborhood.

### 6.4 Bernoulli MGF, verified

For $X \sim \text{Bernoulli}(p)$,

$$ M_X(t) = (1-p)\,e^{t\cdot 0} + p\, e^{t \cdot 1} = 1 - p + p e^t. $$

Sanity against 6.2: $M_X'(t) = p e^t$, so $M_X'(0) = p = \mathbb{E}[X]$; and
$M_X''(0) = p = \mathbb{E}[X^2]$, correct since $X^2 = X$, giving
$\mathrm{Var} = p - p^2 = p(1-p)$, agreeing with 2.2. For the fair coin,
$M_X(t) = \frac{1 + e^t}{2}$.

### 6.5 Gaussian MGF: the exercise solved in full

Claim: $X \sim \mathcal{N}(\mu, \sigma^2)$, with density
$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
\exp\big({-\frac{(x-\mu)^2}{2\sigma^2}}\big)$, has

$$ M_X(t) = \exp\!\Big( \frac{t^2\sigma^2}{2} + t\mu \Big)
   \qquad \text{for all } t \in \mathbb{R}. $$

*Step 1 (set up).* By LOTUS, merging the two exponentials,

$$ M_X(t) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}}
   \exp\!\Big( tx - \frac{(x-\mu)^2}{2\sigma^2} \Big)\, dx. $$

*Step 2 (complete the square).* Work on the exponent as a quadratic in $x$:

$$ tx - \frac{(x-\mu)^2}{2\sigma^2}
   = \frac{2\sigma^2 t x - x^2 + 2\mu x - \mu^2}{2\sigma^2}
   = -\frac{x^2 - 2(\mu + \sigma^2 t)x + \mu^2}{2\sigma^2}. $$

With $m = \mu + \sigma^2 t$, the numerator is
$x^2 - 2mx + \mu^2 = (x-m)^2 - m^2 + \mu^2$, so the exponent equals

$$ -\frac{(x-m)^2}{2\sigma^2} + \frac{m^2 - \mu^2}{2\sigma^2}, $$

where

$$ \frac{m^2 - \mu^2}{2\sigma^2} = \frac{(\mu + \sigma^2 t)^2 - \mu^2}{2\sigma^2}
   = \frac{2\mu\sigma^2 t + \sigma^4 t^2}{2\sigma^2}
   = \mu t + \frac{\sigma^2 t^2}{2}. $$

*Step 3 (read off).* The part constant in $x$ exits the integral; what remains
under the integral is exactly the $\mathcal{N}(m, \sigma^2)$ density, which
integrates to 1:

$$ M_X(t) = e^{\mu t + \sigma^2 t^2/2}
   \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}}
   e^{-\frac{(x-m)^2}{2\sigma^2}}\, dx
   = \exp\!\Big( \frac{t^2\sigma^2}{2} + t\mu \Big). $$

**End of proof.**

Sanity via 6.2: $M_X'(t) = (\mu + \sigma^2 t) M_X(t)$, so $M_X'(0) = \mu$; and
$M_X''(t) = \big(\sigma^2 + (\mu + \sigma^2 t)^2\big) M_X(t)$, so
$M_X''(0) = \sigma^2 + \mu^2 = \mathbb{E}[X^2]$. For the standard normal,
$\mu = 0$ and $\sigma = 1$, giving $M(t) = e^{t^2/2}$ -- the target the
central-limit sketch aims at.

### 6.6 Uniqueness (Theorem 4): precise statement, and a subtlety

**Theorem 4 (MGF uniqueness; stated, not proved).** If
$M_X(t) = M_Y(t) < \infty$ for all $t$ in some open interval $(-t_0, t_0)$
around 0, then $X$ and $Y$ have the same distribution:
$F_X(x) = F_Y(x)$ for all $x$.

Notes. (i) The compact phrase "for all $t$" tacitly includes *finiteness*; the
honest hypothesis is finiteness plus agreement on a neighborhood of 0, since
agreement only at points where both are $+\infty$ carries no information.
(ii) The proof is genuinely out of scope: the standard route shows a
finite-MGF distribution is determined by its moments via analytic continuation of
the Laplace transform, or passes through characteristic functions
[4, Sec. 30; 5, Sec. 3.3]. (iii) A subtlety worth recording, since it explains
why finiteness is not decoration: *moments alone do not determine a
distribution*. The lognormal distribution has all moments finite, yet there are
infinitely many other distributions with exactly the same moment sequence
[4, Sec. 30, Heyde's example]. There is no contradiction with Theorem 4 -- the
lognormal's MGF is infinite for every $t > 0$, so the theorem never applies to
it. The MGF-as-fingerprint usage pattern (compute, recognize, conclude) is valid
precisely when the computed MGF is finite near 0, which is true in both uses
below, Gaussian sums and the central-limit sketch.

### 6.7 Sums become products; the two worked examples verified

**Proposition (independence makes the MGF factorize).** If $X \perp Y$ and
$Z = X + Y$, then for every $t$,

$$ M_Z(t) = \mathbb{E}\big[e^{t(X+Y)}\big] = \mathbb{E}\big[e^{tX} e^{tY}\big]
   = \mathbb{E}\big[e^{tX}\big]\,\mathbb{E}\big[e^{tY}\big]
   = M_X(t)\, M_Y(t), $$

the middle step being the product rule (Lemma 2.2) with $g(x) = e^{tx}$ and
$h(y) = e^{ty}$. For unbounded variables both sides may be $+\infty$; the
identity holds in $(0,\infty]$ because the product rule for *non-negative*
functions needs no integrability, both sides being sums or integrals of
non-negative terms with the same rearrangement. By the $n$-fold extension in
2.3: for $X_1, \dots, X_n$ independent,
$M_{X_1 + \cdots + X_n}(t) = \prod_i M_{X_i}(t)$. **End of proof.**

**Scaling companion**, used in the central-limit step and recalled by prob06 as
one of the MGF rules:

$$ M_{aX}(t) = \mathbb{E}[e^{t(aX)}] = \mathbb{E}[e^{(at)X}] = M_X(at), $$

pure substitution, no independence involved.

**Sum of independent Gaussians, verified.** For
$X \sim \mathcal{N}(\mu_1, \sigma_1^2)$ independent of
$Y \sim \mathcal{N}(\mu_2, \sigma_2^2)$,

$$ M_{X+Y}(t) = e^{\mu_1 t + \sigma_1^2 t^2/2}\, e^{\mu_2 t + \sigma_2^2 t^2/2}
   = e^{(\mu_1 + \mu_2)t + (\sigma_1^2 + \sigma_2^2)t^2/2}, $$

which is the MGF of
$\mathcal{N}(\mu_1 + \mu_2,\, \sigma_1^2 + \sigma_2^2)$, everywhere finite; so
Theorem 4 applies and identifies the distribution of $X + Y$ as exactly that
Gaussian. Consistency check: the mean adds by linearity and the variance adds by
Lemma 2.3 -- the MGF route additionally proves the *shape* is Gaussian, which no
moment bookkeeping could.

**Coin sum, verified.** For $S_n = X_1 + \cdots + X_n$ with i.i.d. fair coins,
$M_{S_n}(t) = \big(\frac{1+e^t}{2}\big)^n$ by the $n$-fold product with 6.4's
factor. The exponent $n$ sitting on the MGF is, one section later, the seed of
the exponential tail bound.

## 7. Chernoff Bound

### 7.1 Statement, conditions, and the lower-tail twin

**Theorem 5 (Chernoff bound).** Let $X$ have MGF
$M(t) = \mathbb{E}[e^{tX}]$. For any $\alpha \in \mathbb{R}$ and any $t > 0$
with $M(t) < \infty$,

$$ \Pr(X \geq \alpha) \;\leq\; M(t)\, e^{-t\alpha}. $$

Since each $t$ gives a valid bound, so does the best one:
$\Pr(X \geq \alpha) \leq \inf_{t > 0} M(t)e^{-t\alpha}$.

Conditions unpacked. (i) The only hypothesis is finiteness of $M$ at the $t$
actually used: no non-negativity, since $e^{tX}$ supplies it, and no variance
assumption. If $M(t) = \infty$ for all $t > 0$ the bound is vacuous, never wrong.
(ii) $\alpha$ needs no sign restriction, but the bound is useful only for
$\alpha$ above the mean: for $\alpha \leq \mathbb{E}[X]$, Jensen's inequality
(Lecture 1) gives
$M(t) = \mathbb{E}[e^{tX}] \geq e^{t\mathbb{E}[X]} \geq e^{t\alpha}$, so the
right-hand side is at least 1. (iii) *Lower tail:* the mirror statement
$\Pr(X \leq \alpha) \leq M(t)e^{-t\alpha}$ holds for every $t < 0$, by the same
proof with the decreasing map $x \mapsto e^{tx}$ flipping the event;
equivalently, apply Theorem 5 to $-X$ at level $-\alpha$. This twin is what the
two-sided factor 2 in 7.6 quietly uses.

### 7.2 Proof: Markov on the exponentiated variable

**Step 1 (exponentiate the event).** Fix $t > 0$. The map $x \mapsto e^{tx}$ is
strictly increasing, so

$$ X \geq \alpha \iff e^{tX} \geq e^{t\alpha}, $$

the same event, hence the same probability. Set $W = e^{tX}$ and check Markov's
entry ticket: $W > 0$, exponentials being positive -- note this holds regardless
of the sign of $X$, which is why no centering was needed -- and
$\mathbb{E}[W] = M(t) < \infty$ by hypothesis.

**Step 2 (Markov).** Theorem 1, threshold form, on $W$ at level
$e^{t\alpha} > 0$:

$$ \Pr(X \geq \alpha) = \Pr\big(W \geq e^{t\alpha}\big)
   \;\leq\; \frac{\mathbb{E}[W]}{e^{t\alpha}} = M(t)\, e^{-t\alpha}. $$

**End of proof.**

This is Chebyshev's proof with the square swapped for an exponential -- the "one
engine, three fuels" claim is now fully cashed. The new feature is the *free
parameter*: the transform is tunable, and the tuning happens after the inequality
is proved, at zero logical cost, because every $t$ yields a true statement.

### 7.3 Coin flips: the three-step optimization, every step verified

**Step 1 (plug in).** $\bar X_n \geq \frac34$ if and only if
$S_n \geq \frac{3n}{4}$, multiplying by $n > 0$. Chernoff on $S_n$ with
$M_{S_n}(t) = \big(\frac{1+e^t}{2}\big)^n$ from 6.7:

$$ \Pr\!\Big(S_n \geq \frac{3n}{4}\Big)
   \;\leq\; e^{-3nt/4} \Big(\frac{1+e^t}{2}\Big)^{\!n}
   = \Big[ e^{-3t/4}\, \frac{1+e^t}{2} \Big]^{n} = e^{n g(t)}, $$

where $g(t) = -\frac{3t}{4} + \ln\frac{1+e^t}{2}$.

**Step 2 (optimize $t$).** Minimizing the bound over $t > 0$ is the same as
minimizing $g$, since $u \mapsto e^{nu}$ is increasing, so the log of the minimum
is the minimum of the log. Differentiate:

$$ g'(t) = -\frac34 + \frac{e^t}{1+e^t} = 0
   \iff \frac{e^t}{1+e^t} = \frac34
   \iff e^t = 3
   \iff t^\star = \ln 3 > 0, $$

solving $4e^t = 3 + 3e^t$. This critical point is the unique minimizer:
$\frac{e^t}{1+e^t}$ is strictly increasing in $t$, being the logistic function,
climbing from $\frac12$ at $t = 0$ toward 1, so $g'$ is negative before
$t^\star$ and positive after; equivalently
$g''(t) = \frac{e^t}{(1+e^t)^2} > 0$, so $g$ is strictly convex.

**Step 3 (evaluate).** At $t^\star = \ln 3$ we have $e^{t^\star} = 3$, so
$\frac{1+e^{t^\star}}{2} = 2$ and

$$ g(t^\star) = -\frac34 \ln 3 + \ln 2
   = -0.823959\ldots + 0.693147\ldots = -0.130812\ldots, $$

$$ \Pr\!\big(\bar X_n \geq \tfrac34\big) \;\leq\; e^{-0.1308\, n}. $$

Numerically: $n = 16$ gives $e^{-2.0930} = 0.1233$, about 0.12; $n = 100$ gives
$e^{-13.081} = 2.08 \times 10^{-6}$; $n = 400$ gives
$e^{-52.325} = 1.89 \times 10^{-23}$. Against Chebyshev's 0.01 at $n = 400$ that
is twenty-one orders of magnitude.

### 7.4 The optimized exponent is a KL divergence

Run the same three steps at a general level $a$ with $\frac12 < a < 1$:
$g_a(t) = -at + \ln\frac{1+e^t}{2}$, and $g_a'(t) = 0$ gives
$\frac{e^t}{1+e^t} = a$, that is $e^{t^\star} = \frac{a}{1-a}$ and
$t^\star = \ln\frac{a}{1-a} > 0$. Substituting back, with
$\frac{1 + e^{t^\star}}{2} = \frac{1}{2(1-a)}$:

$$ g_a(t^\star) = -a \ln\frac{a}{1-a} + \ln\frac{1}{2(1-a)}
   = -a\ln a + a \ln(1-a) - \ln 2 - \ln(1-a) $$

$$ = -\big[ a \ln(2a) + (1-a)\ln(2(1-a)) \big]
   = -\Big[ a \ln\frac{a}{1/2} + (1-a)\ln\frac{1-a}{1/2} \Big] $$

$$ = -\,D\big(\mathrm{Bern}(a)\,\Vert\,\mathrm{Bern}(\tfrac12)\big), $$

the KL divergence of Lecture 2, in nats. Hence

$$ \Pr(\bar X_n \geq a)
   \leq e^{-n D(\mathrm{Bern}(a) \Vert \mathrm{Bern}(1/2))}. $$

Check at $a = \frac34$:
$D = \frac34\ln\frac{3/4}{1/2} + \frac14\ln\frac{1/4}{1/2}
= \frac34\ln\frac32 + \frac14\ln\frac12 = 0.304099 - 0.173287 = 0.130812$ nats,
identical to $-g(t^\star)$ from 7.3, as it must be. The optimized Chernoff bound
rediscovers, mechanically, information theory's cost of pretending $a$-biased
data came from a fair coin; Section 8 shows this exponent is not just an upper
bound but the *true* decay rate.

### 7.5 The quadratic approximation of the divergence

Claim: $D(\mathrm{Bern}(\frac12 + \epsilon) \Vert \mathrm{Bern}(\frac12))
\approx 2\epsilon^2$. Write

$$ h(\epsilon) = D\big(\mathrm{Bern}(\tfrac12+\epsilon) \Vert
   \mathrm{Bern}(\tfrac12)\big)
   = (\tfrac12+\epsilon)\ln(1+2\epsilon) + (\tfrac12-\epsilon)\ln(1-2\epsilon). $$

Then $h(0) = 0$; differentiating,
$h'(\epsilon) = \ln(1+2\epsilon) - \ln(1-2\epsilon)$, so $h'(0) = 0$; and
$h''(\epsilon) = \frac{2}{1+2\epsilon} + \frac{2}{1-2\epsilon}$, so
$h''(0) = 4$. Taylor:
$h(\epsilon) = \frac{4}{2}\epsilon^2 + O(\epsilon^3)
= 2\epsilon^2 + O(\epsilon^3)$. Check at $\epsilon = 0.01$:
$2\epsilon^2 = 2 \times 10^{-4}$, while the exact value is
$0.51\ln\frac{0.51}{0.5} + 0.49\ln\frac{0.49}{0.5} = 0.000200013$ -- accurate to
five significant figures already. This $2\epsilon^2$ is exactly the exponent of
prob06's Hoeffding inequality specialized to coins.

### 7.6 Sample-size revisited: 18,444, verified

The Section 1 demand for a fair coin is
$\Pr(|\bar X_n - \frac12| \geq 0.01) \leq 0.05$. The deviation event splits into
two tails, $\{\bar X_n \geq 0.51\}$ and $\{\bar X_n \leq 0.49\}$; the union bound
-- the probability of a union is at most the sum -- plus the upper-tail bound of
7.4 and its lower-tail twin from 7.1(iii), equal by the symmetry
$D(\mathrm{Bern}(0.49) \Vert \mathrm{Bern}(0.5))
= D(\mathrm{Bern}(0.51) \Vert \mathrm{Bern}(0.5))$ for a fair reference coin,
give

$$ \Pr\big(|\bar X_n - \tfrac12| \geq 0.01\big)
   \;\leq\; 2\, e^{-n D(\mathrm{Bern}(0.51) \Vert \mathrm{Bern}(0.5))}
   = 2\,e^{-n \cdot 0.000200013}. $$

Requiring $2e^{-nD} \leq 0.05$ gives $n \geq \frac{\ln 40}{D}$. With the rounded
$D \approx 0.0002$: $n \geq \frac{3.68888}{0.0002} = 18{,}444.4$. With the exact
$D = 0.000200013$: $n \geq 18{,}443.2$. So the integer requirement is
$n \geq 18{,}444$ either way, and the rounding is harmless. Against Chebyshev's
50,000 from 4.7 that is a saving by a factor 2.7, from the same data and the same
failure budget, purchased entirely by knowing the MGF instead of only the
variance.

### 7.7 Exponential versus polynomial: the scaling in the failure probability

Fix the coin question $\Pr(\bar X_n \geq \frac34) \leq \delta$ and solve each
bound for $n$. Chebyshev requires $n \geq 4/\delta$; Chernoff requires
$n \geq \ln(1/\delta)/0.1308$. Three targets, each with the Chebyshev
requirement then the Chernoff requirement:

- $\delta = 10^{-2}$: Chebyshev $n \geq 400$; Chernoff $n \geq 36$.
- $\delta = 10^{-6}$: Chebyshev $n \geq 4{,}000{,}000$; Chernoff
  $n \geq 106$, since $\ln(10^6) = 13.816$ and $13.816/0.1308 = 105.6$.
- $\delta = 10^{-9}$: Chebyshev $n \geq 4 \times 10^{9}$; Chernoff
  $n \geq 159$, since $\ln(10^9) = 20.72$ and $20.72/0.1308 = 158.4$.

Polynomial bounds pay $1/\delta$; exponential bounds pay $\ln(1/\delta)$. This is
why moderate sample sizes give strong guarantees in machine-learning theory:
pushing the failure probability from $10^{-2}$ to $10^{-9}$ costs Chernoff a
factor 4.4 in samples and costs Chebyshev a factor $10^{7}$.

## 8. Three Bounds Head-to-Head

The escalation needs no new mathematics -- each bound was proved above. For the
coin question $\Pr(\bar X_n \geq \frac34)$, the three bounds are Markov
$= \frac23$, Chebyshev $= 4/n$, and Chernoff $= e^{-0.130812 n}$, and the exact
value is $\Pr(S_n \geq \lceil 3n/4 \rceil)$. Three sample sizes, each with
Markov, Chebyshev, Chernoff, then the exact value:

- $n = 16$: Markov 0.67; Chebyshev 0.25; Chernoff 0.1233; exact
  $2517/65536 = 0.0384$.
- $n = 100$: Markov 0.67; Chebyshev 0.04; Chernoff
  $2.08 \times 10^{-6}$; exact $2.82 \times 10^{-7}$.
- $n = 400$: Markov 0.67; Chebyshev 0.01; Chernoff
  $1.89 \times 10^{-23}$; exact $1.30 \times 10^{-24}$.

The exact column is $\sum_{k \geq 3n/4} \binom{n}{k} 2^{-n}$ evaluated directly:
$n = 16$ was expanded coefficient by coefficient in 5.4, and $n = 100, 400$ are
the same finite sums, machine-evaluated as $2.8181 \times 10^{-7}$ and
$1.2959 \times 10^{-24}$.

**Why Chernoff tracks the truth's exponent.** On a logarithmic scale the exact
tail and the Chernoff bound are parallel lines: at $n = 400$,
$\frac1n \ln(1/\text{exact}) = 0.13758$ against the Chernoff exponent
$0.13081$. The residual gap is subexponential. Cramer's large-deviations theorem
[5, Sec. 2.7] says the true exponent equals the optimized Chernoff exponent,

$$ \lim_{n\to\infty} \frac1n \ln \Pr(\bar X_n \geq a)
   = -D\big(\mathrm{Bern}(a) \Vert \mathrm{Bern}(\tfrac12)\big), $$

and the remaining polynomial factor, of order $1/\sqrt{n}$, the Bahadur-Rao
correction, is why the exact numbers sit one order of magnitude below the bound
while decaying at the same rate. So Chernoff is not merely the best of the three
bounds -- at the exponential scale it is *unimprovable*. Chebyshev, by contrast,
is off by the unbounded factor $(4/n)e^{+0.1308 n}$, and Markov by a constant
that never moves. Diagnosis in one sentence: each bound is exactly as good as the
information it eats.

## 9. Central Limit Theorem

### 9.1 Convergence in distribution, stated precisely

**Definition.** $Z_n \to Z$ *in distribution*, written
$Z_n \xrightarrow{(d)} Z$, if $F_{Z_n}(x) \to F_Z(x)$ at every point $x$ where
$F_Z$ is continuous.

The continuity-point restriction is a real part of the definition that the
informal gloss "the CDF of $Z_n$ approaches the Gaussian CDF" can afford to drop
*only because* the limit here is $\mathcal{N}(0,1)$, whose CDF $\Phi$ is
continuous everywhere -- so in this lecture the convergence really is at every
$x$. Why the restriction exists in general: let $Z_n = \frac1n$
deterministically; then $Z_n \to 0$ in every reasonable sense, yet
$F_{Z_n}(0) = 0$ for all $n$ while $F_0(0) = 1$, so convergence fails exactly at
the limit CDF's jump. In the hierarchy of 5.3 this is the weakest mode: it
constrains only the distributions, not the random variables jointly.

### 9.2 Statement, and the standardization that feeds it

**Theorem 6 (central limit theorem, Lindeberg-Levy).** Let
$X_1, X_2, \dots$ be i.i.d. with mean $\mu$ and variance
$\sigma^2 \in (0, \infty)$. Then

$$ Z_n = \sum_{i=1}^{n} \frac{X_i - \mu}{\sqrt{n}\,\sigma}
   \;\xrightarrow{(d)}\; \mathcal{N}(0,1). $$

Equivalent bookkeeping: with $Y_i = (X_i - \mu)/\sigma$, so that
$\mathbb{E}[Y] = 0$ and $\mathbb{E}[Y^2] = \mathrm{Var}(Y) = 1$, hence
$M_Y(0) = 1$, $M_Y'(0) = 0$, $M_Y''(0) = 1$ by 6.2, we have
$Z_n = \frac{1}{\sqrt n}\sum_i Y_i$; and
$Z_n = \frac{\bar X_n - \mu}{\sigma/\sqrt n}$, the sample mean centered and
rescaled by its own standard deviation $\sigma/\sqrt{n}$ (Lemma 4.1). The
theorem's full hypotheses are exactly as stated -- finite variance, i.i.d. --
and note that it needs *no* MGF assumption. That mismatch between the theorem's
hypotheses and the sketch's tools is precisely what makes the proof below a
sketch.

### 9.3 What the sketch omits: the honest list

- **Gap 1: the MGF may not exist.** The sketch manipulates $M_Y(t)$, but finite
  variance does not give a finite MGF; the $(1+|x|)^{-4}$-density example of 6.1
  satisfies Theorem 6's hypotheses while $M_Y(t) = \infty$ for all
  $t \neq 0$. So the sketch cannot even be *started* for some distributions the
  theorem covers.
- **Gap 2: pointwise MGF convergence must imply convergence in distribution.**
  This is true but nontrivial: if $M_{Z_n}(t) \to M_Z(t) < \infty$ for all $t$ in
  an open interval around 0, then $Z_n \xrightarrow{(d)} Z$, which is Curtiss's
  theorem [8]. It is the "fingerprint, in the limit" taken on faith.
- **Gap 3: the Taylor step needs error control.** Writing
  $M_Y(s) \approx 1 + s^2/2$ hides a remainder; one must know the remainder is
  $o(s^2)$ and track it through the $n$-th power. Under Gap 1's assumption this
  is genuinely fine, and it is made rigorous in 9.4.

**The real proof** replaces the MGF by the characteristic function
$\varphi_X(t) = \mathbb{E}[e^{itX}]$, which exists for *every* random variable
since $|e^{itX}| = 1$, satisfies the same product and scale rules, has
$\varphi_Y(s) = 1 - s^2/2 + o(s^2)$ under finite variance, and comes with Levy's
continuity theorem in place of Curtiss's. The argument is then *formally
identical* to the sketch below with $t$ replaced by $it$; see [5, Sec. 3.4] or
[4, Sec. 27]. So the sketch is not a wrong proof -- it is the right proof run on
the wrong transform, and presenting it is a fair trade of complex analysis for
honesty about the gaps.

### 9.4 The sketch, made precise at statement level

**Standing assumption for this subsection (Gap 1 granted):** $M_Y$ is finite on
an open interval around 0. Then each step is a genuine lemma.

**Step 1 (product; exact, no approximation).** By the $n$-fold product rule of
6.7 and the scale rule with $a = \frac{1}{\sqrt n}$,

$$ M_{Z_n}(t)
   = \mathbb{E}\Big[ e^{\frac{t}{\sqrt n}\sum_i Y_i} \Big]
   = \prod_{i=1}^{n} \mathbb{E}\Big[ e^{\frac{t}{\sqrt n} Y_i} \Big]
   = M_Y\!\Big(\frac{t}{\sqrt n}\Big)^{\! n}, $$

using independence for the product and identical distribution to collapse it to a
power. This identity is exact for every $n$ and every $t$ with $t/\sqrt{n}$ in
the finiteness interval.

**Step 2 (Taylor, with the remainder stated).** By 6.2, $M_Y$ is twice
differentiable at 0 with $M_Y(0) = 1$, $M_Y'(0) = 0$, $M_Y''(0) = 1$; Taylor's
theorem with Peano remainder gives, as $s \to 0$,

$$ M_Y(s) = 1 + \frac{s^2}{2} + r(s), \qquad r(s) = o(s^2). $$

At $s = t/\sqrt{n}$ with $t$ fixed:
$M_Y(t/\sqrt n) = 1 + \frac{t^2}{2n} + r_n$ where $n\, r_n \to 0$.
Standardization is what killed the linear term; without it the expansion would
carry a term at scale $\mu t \sqrt{n}$ that ruins the limit.

**Step 3 (limit lemma, proved).** *If $c_n \to 0$ with $n\,c_n \to x$, then
$(1 + c_n)^n \to e^x$.* Proof: for $n$ large, $|c_n| < 1$ and
$\ln(1 + c_n) = c_n + O(c_n^2)$, the Taylor expansion of $\ln$ at 1, so
$n \ln(1 + c_n) = n c_n + n \cdot O(c_n^2) \to x + 0$, since
$n c_n^2 = (n c_n) \cdot c_n \to x \cdot 0 = 0$; exponentiate, using continuity
of $\exp$. Applying it with $c_n = \frac{t^2}{2n} + r_n$, so that
$n c_n \to \frac{t^2}{2}$:

$$ M_{Z_n}(t) = \Big(1 + \frac{t^2}{2n} + r_n\Big)^{\! n}
   \;\longrightarrow\; e^{t^2/2} \qquad \text{for every fixed } t. $$

**Step 4 (recognize and conclude).** $e^{t^2/2}$ is the $\mathcal{N}(0,1)$ MGF,
by 6.5 with $\mu = 0$ and $\sigma = 1$, finite everywhere; by Curtiss's theorem
(Gap 2, cited not proved), $Z_n \xrightarrow{(d)} \mathcal{N}(0,1)$.
**End of proof**, modulo Gap 2 and under the extra assumption of Gap 1.

Note the division of labor: Steps 1 to 3 are fully proved here; the entire
remaining debt of the sketch is Gap 1, an added hypothesis, and Gap 2, one cited
theorem. The universality mechanism is visible in Step 2: after standardization,
*only* $M_Y''(0) = 1$ survives into the limit -- every higher moment of $Y$ is
buried in $r_n$ and crushed by the $1/\sqrt{n}$ scaling. Coins, dice, and losses
genuinely become indistinguishable in the limit.

### 9.5 The compound-interest limit's numeric check

At $x = 1$: $(1 + \frac{1}{10})^{10} = 1.1^{10} = 2.5937$;
$(1 + \frac{1}{100})^{100} = 1.01^{100} = 2.7048$; and the limit is
$e = 2.71828\ldots$.

### 9.6 The binomial-versus-Gaussian comparison at $n = 16$

Compare the standardized pmf of $S_{16} \sim \mathrm{Bin}(16, \frac12)$ with the
$\mathcal{N}(0,1)$ density. To compare a pmf with a density, each probability
mass is divided by the lattice spacing of the standardized values: adjacent
values of $S_{16}$ sit $\Delta z = 1/\sigma_{S_{16}} = \frac12$ apart, since
$\sigma_{S_{16}} = \sqrt{16 \cdot \frac14} = 2$. So the height at the center is

$$ \frac{\Pr(S_{16} = 8)}{\Delta z} = \binom{16}{8} 2^{-16} \times 2
   = \frac{12870}{65536} \times 2 = 0.19638 \times 2 = 0.3928, $$

against the Gaussian peak $\frac{1}{\sqrt{2\pi}} = 0.3989$: agreement to
1.5 percent at $n$ as small as 16.

**What the central limit theorem buys:** the *shape* of typical fluctuations --
error bars $\mu \pm z\,\sigma/\sqrt n$, and the universality of the Gaussian
noise model, pairing with Lecture 3's maximum-entropy characterization.
Quantitatively, the Berry-Esseen theorem [5, Sec. 3.4.4] bounds the CDF error by
$C\,\mathbb{E}|Y|^3/\sqrt{n}$ for an absolute constant $C$, a $1/\sqrt n$
convergence rate.

**What it does not buy: guarantees.** The central limit theorem is a limit
statement about the *center* of the distribution; it comes with no error bound in
the far tails at fixed $n$, which is exactly the concentration inequalities' job.
An instructive coincidence on today's coin: the normal approximation to
$\Pr(\bar X_{100} \geq \frac34)$ is $Q(5) = 2.87 \times 10^{-7}$, the threshold
being $z = \frac{0.75 - 0.5}{0.5/10} = 5$ standard deviations, remarkably close
to the exact $2.82 \times 10^{-7}$ -- but this accuracy is luck, not law, since
nothing certifies it in advance, whereas Chernoff's $2.08 \times 10^{-6}$ is a
*proved ceiling*. Use the central limit theorem to describe fluctuations, and
concentration bounds to certify them. That division -- description versus
certification -- is the bridge to Lecture 6, where certification is extended from
one average to a whole hypothesis class via Hoeffding's inequality plus the union
bound.

## 10. References

1. S. Boucheron, G. Lugosi and P. Massart, *Concentration Inequalities: A
   Nonasymptotic Theory of Independence*, Oxford University Press, 2013. DOI
   10.1093/acprof:oso/9780199535255.001.0001
   (https://doi.org/10.1093/acprof:oso/9780199535255.001.0001). Chapter 2 has the
   Cramer-Chernoff method, that is Sections 7 and 8's optimization done in full
   generality; the standard modern reference for everything this lecture opens.
2. R. Vershynin, *High-Dimensional Probability: An Introduction with
   Applications in Data Science*, Cambridge University Press, 2018. DOI
   10.1017/9781108231596 (https://doi.org/10.1017/9781108231596); free copy on
   the author's page. Chapters 1 and 2 cover Markov, Chebyshev, Chernoff and
   sub-Gaussian variables, the road Lecture 6 takes.
3. H. Chernoff, "A Measure of Asymptotic Efficiency for Tests of a Hypothesis
   Based on the Sum of Observations," *Annals of Mathematical Statistics*,
   vol. 23, no. 4, pp. 493-507, 1952. DOI 10.1214/aoms/1177729330
   (https://doi.org/10.1214/aoms/1177729330). The original exponential bound; the
   KL form of the exponent in Section 7.4 is already here.
4. P. Billingsley, *Probability and Measure*, 3rd ed., Wiley, 1995. Section 21 has
   differentiation under the expectation and the moment expansions used in 6.2
   and 6.3; Section 30 the moment problem, MGF determinacy and Heyde's lognormal
   example cited in 6.6; Section 27 the characteristic-function proof of the
   central limit theorem.
5. R. Durrett, *Probability: Theory and Examples*, 5th ed., Cambridge University
   Press, 2019. DOI 10.1017/9781108591034
   (https://doi.org/10.1017/9781108591034). Theorem 2.4.1 is the strong law;
   Section 2.7 has large deviations and Cramer's theorem behind Section 8;
   Section 3.4 the rigorous central limit theorem and Berry-Esseen.
6. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 11 has the method of types, the
   KL exponent of Section 7.4 as the exact large-deviations rate; the course's
   standing reference for KL divergence.
7. N. Etemadi, "An Elementary Proof of the Strong Law of Large Numbers,"
   *Zeitschrift fur Wahrscheinlichkeitstheorie und verwandte Gebiete*, vol. 55,
   pp. 119-122, 1981. The most accessible proof of the theorem stated in 5.3.
8. J. H. Curtiss, "A Note on the Theory of Moment Generating Functions," *Annals
   of Mathematical Statistics*, vol. 13, no. 4, pp. 430-433, 1942. MGF
   convergence implies convergence in distribution, which is Gap 2 of
   Section 9.3.
