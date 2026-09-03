# Deep Learning Math, Lecture 6: From Concentration to Generalization

**About this file.** Screen-reader edition of the Lecture 6 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob06-generalization-note.html`). The two tables of sample-size
numbers are written out as lists, one bullet per row. Nothing else is needed to
read it.

**Convention.** As in the Lecture 5 note, a random variable may be discrete
(pmf $p_X$, expectations are sums) or continuous (pdf $f_X$, expectations are
integrals); every statement holds in both readings with sums and integrals
interchanged. The one place where the continuous case needs genuine extra care --
differentiating an MGF under the expectation -- is flagged, not papered over.

**Notation.** $\mathcal{D}$ is the unknown data distribution over an example
space $\mathcal{Z}$; $\ell(h, z) \in [0,1]$ is the loss of hypothesis $h$ on
example $z$; $R(h)$ is the true risk, $\hat R_n(h)$ the empirical risk,
$\hat h$ the empirical risk minimizer, $\mathcal{H}$ the hypothesis class.
$M_X(t) = \mathbb{E}[e^{tX}]$ is the moment generating function (MGF) and
$\psi(t) = \log M_X(t)$ the log-MGF. $\bar X_n = \frac1n \sum_i X_i$.
$\mathbf{1}\{A\}$ is the indicator of the event $A$. $\mathbb{E}_t$ and
$\mathrm{Var}_t$ are mean and variance under the tilted distribution $p_t$.

**Background used.** From Lecture 5: Markov's and Chernoff's inequalities, MGF
calculus, the Gaussian MGF, monotonicity of expectation (its Lemma 2.1), the
variance of a sample mean (its Lemma 4.1), and the fair coin's exact and
optimal-Chernoff tails. From Lecture 3: independence and the fact that functions
of independent variables are independent. From Lecture 1: $\log M$ as the
information in a choice among $M$ alternatives. These are cited, not re-proved.

**Contents.**

1. Why generalization?
2. Recall: the Lecture 5 toolkit
3. Hoeffding's lemma
4. Sub-Gaussian variables
5. Hoeffding's inequality
6. The union bound
7. The generalization theorem
8. Why ERM works
9. References

## 1. Why Generalization?

### 1.1 The statistical learning setup, in full

Everything in this lecture lives in one probabilistic model, so it deserves a
complete statement. There is an unknown distribution $\mathcal{D}$ over an
example space $\mathcal{Z}$; for supervised learning
$\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$ and an example is a pair
$z = (x, y)$. The *sample* is

$$ Z_1, \dots, Z_n \ \overset{\text{i.i.d.}}{\sim}\ \mathcal{D}, $$

meaning two separate things, both used later: each $Z_i$ has marginal
distribution $\mathcal{D}$, that is *identically distributed*; and the joint
distribution factorizes, $p_{Z_1,\dots,Z_n} = \prod_i p_{Z_i}$, that is
*mutually independent*. A *hypothesis* $h$ is a candidate model -- a function
$\mathcal{X} \to \mathcal{Y}$, or more abstractly any object that a *loss
function* can grade: $\ell(h, z) \in [0, 1]$ measures how badly $h$ handles the
single example $z$. Boundedness of $\ell$ is a standing assumption of the whole
lecture; it is what feeds Hoeffding's lemma in Section 3. The interval $[0,1]$ is
a normalization: any loss bounded in $[0, c]$ rescales, and Section 4.2 tracks
the constant $c$ explicitly. The canonical example is the 0/1 loss
$\ell(h, (x,y)) = \mathbf{1}\{h(x) \neq y\}$, whose expectation is an error rate.

### 1.2 True risk, empirical risk, ERM, gap -- the four definitions

**Definitions.** For a hypothesis $h$ and the sample $Z_1, \dots, Z_n$:

$$ R(h) = \mathbb{E}_{Z \sim \mathcal{D}}\big[\ell(h, Z)\big], \qquad
   \hat{R}_n(h) = \frac{1}{n} \sum_{i=1}^{n} \ell(h, Z_i), $$

$$ \hat{h} = \operatorname*{argmin}_{h \in \mathcal{H}} \hat{R}_n(h)
   \quad \text{(ERM over a class } \mathcal{H}\text{)}, \qquad
   \mathrm{gap}(h) = R(h) - \hat{R}_n(h). $$

Reading the types carefully is the source of every subtlety later. $R(h)$ is a
*fixed number* for each $h$, an expectation over a fresh $Z$ independent of the
sample; it depends on the unknown $\mathcal{D}$, so it is not computable.
$\hat{R}_n(h)$ is a *random variable*, a function of the sample; for each *fixed*
$h$ it is exactly the sample mean $\bar X_n$ of Lecture 5 with
$X_i = \ell(h, Z_i)$. The ERM output $\hat h$ is a *random hypothesis*, a
function of the sample, and that single fact is what breaks the naive application
of concentration (Section 1.4). If several $h$ tie for the minimum, $\hat h$ is
any fixed tie-breaking choice; nothing below depends on which. Training loss and
test-set accuracy are both instances of $\hat R_n$ computed on different samples;
"generalization" is the claim that $\mathrm{gap}(\hat h)$ is small with high
probability -- a theorem, not a hope.

### 1.3 Worked example: the memorizer, verified

The extreme case, with its hypotheses made explicit. Let the inputs $X_i$ be
distinct with probability 1 -- for instance $X$ has a continuous distribution, so
a repeat has probability 0, a condition left implicit in the source -- and let
the labels be independent fair coins carrying *no information* about $x$:
$Y \sim \mathrm{Bernoulli}(\frac12)$ independent of $X$. The memorizer is the
lookup table $h_{\text{mem}}(x) = Y_i$ if $x = X_i$ for some training index $i$,
and 0 otherwise. Then:

**Training loss.** On each training point,
$h_{\text{mem}}(X_i) = Y_i$ by construction, the $X_i$ being distinct so that the
lookup is unambiguous; hence every 0/1 loss term is 0 and
$\hat R_n(h_{\text{mem}}) = 0$.

**True risk.** A fresh $(X, Y) \sim \mathcal{D}$ misses the lookup table with
probability 1, by continuity, so $h_{\text{mem}}(X) = 0$; the fresh label is an
independent fair coin, so
$\Pr(h_{\text{mem}}(X) \neq Y) = \Pr(Y = 1) = \frac12$. Hence
$R(h_{\text{mem}}) = \frac12$ and $\mathrm{gap} = \frac12 - 0 = \frac12$.

Note what the example proves: *without* restricting the hypothesis class, the gap
of a data-dependent hypothesis can be as large as the loss range allows, at every
$n$. Any generalization theorem must therefore charge for the size of
$\mathcal{H}$ somewhere -- the memorizer's class, all lookup tables, is
effectively infinite, and Theorem 5's $\ln|\mathcal{H}|$ price on it is
$\infty$: the bound correctly refuses to certify it.

### 1.4 Why Lecture 5 is not enough: fixed versus chosen

Lecture 5's inequalities bound $\Pr(|\bar X_n - \mu| \geq \epsilon)$ for a sample
mean of i.i.d. terms. For a *fixed* $h$ -- chosen before the sample is drawn, so
that the terms $\ell(h, Z_i)$ are honest i.i.d. draws -- this applies verbatim,
and Section 7.2 does it. For $\hat h$ it does not: the event "$\hat h = h$"
depends on the whole sample, so conditional on the choice, the losses
$\ell(\hat h, Z_i)$ are no longer i.i.d. draws with mean $R(\hat h)$. ERM
*selected* a hypothesis precisely because its empirical losses came out low; that
is, it hunts for the downward fluctuations that concentration says are rare *per
hypothesis* but that become likely when many hypotheses are searched, which
Section 6.3 quantifies exactly with the model farm.

The fix is not to bound the chosen one but to bound **every $h$ at once** --
*uniform convergence* -- so that whatever the algorithm picks, it lands inside an
already-certified event. The route: Hoeffding's lemma (bounded implies
Gaussian-like MGF, Section 3), then Hoeffding's inequality (exponential tail for
one $h$, Section 5), then the union bound (pay for many looks, Section 6), then
the finite-class theorem and its ERM corollary (Section 7).

## 2. Recall: the Lecture 5 Toolkit

Three results are imported by name; all are stated and proved in the Lecture 5
companion note, cited here with their fine print.

### 2.1 Chernoff bound

For any random variable $X$, any threshold $\alpha$, and any $t > 0$ with
$M_X(t) = \mathbb{E}[e^{tX}] < \infty$:

$$ \Pr(X \geq \alpha) \;\leq\; e^{-t\alpha}\, M_X(t). $$

Engine: Markov's inequality applied to the non-negative variable $e^{tX}$, using
that $x \mapsto e^{tx}$ is strictly increasing for $t > 0$, so that
$\{X \geq \alpha\} = \{e^{tX} \geq e^{t\alpha}\}$ is the same event. The
parameter $t$ is free and is optimized at the end; see Lecture 5 note
Section 7. The finiteness proviso never bites today: every variable in this
lecture is bounded, so $M_X$ is finite for all $t$, the expectation of a bounded
positive variable being finite.

### 2.2 MGF calculus

For independent $X, Y$ and constant $c$: $M_{X+Y}(t) = M_X(t)\,M_Y(t)$ and
$M_{cX}(t) = M_X(ct)$. The product rule is the independence product rule
$\mathbb{E}[g(X)h(Y)] = \mathbb{E}[g(X)]\,\mathbb{E}[h(Y)]$ applied to
$g = h = \exp(t\,\cdot)$; the $n$-fold version
$\mathbb{E}\big[\prod_i e^{tX_i}\big] = \prod_i \mathbb{E}[e^{tX_i}]$ for
mutually independent $X_1, \dots, X_n$ follows by the induction spelled out in
Lecture 5 note Section 2.3, and is the exact form used in Sections 4.5 and 5
below. The scale rule is the substitution $e^{t(cX)} = e^{(tc)X}$.

### 2.3 Gaussian MGF

For $X \sim \mathcal{N}(\mu, \sigma^2)$:
$\mathbb{E}[e^{t(X-\mu)}] = e^{t^2\sigma^2/2}$ for all $t \in \mathbb{R}$, proved
by completing the square (Lecture 5 note Section 6.5). This exact shape,
$\exp(t^2 \cdot \text{constant}/2)$, is today's yardstick: Section 3 shows every
bounded variable's MGF sits under such an envelope, and Section 4 names the class
of variables that do.

### 2.4 What is genuinely new

Lecture 5's Chernoff computation for the coin used the coin's *exact* MGF. For a
loss $\ell(h, Z)$ the distribution -- hence the MGF -- is unknown, depending on
$\mathcal{D}$ and on $h$; all that is known structurally is $\ell \in [0,1]$.
Today's first job is therefore an MGF *bound* from boundedness alone. That is
Hoeffding's lemma.

## 3. Hoeffding's Lemma

### 3.1 Technique 1: variance of a bounded variable

**Lemma 3.1 (bounded variance).** If $Y \in [a, b]$ with probability 1 -- the
variance automatically exists since $Y$ is bounded -- then
$\mathrm{Var}(Y) \leq \frac{(b-a)^2}{4}$.

*Proof.* Two steps, each with its own sub-lemma.

*Step A (the mean minimizes the quadratic).* For any constant $c$, expand around
the mean $\mu_Y = \mathbb{E}[Y]$:

$$ \mathbb{E}\big[(Y - c)^2\big]
   = \mathbb{E}\big[\big((Y - \mu_Y) + (\mu_Y - c)\big)^2\big]
   = \mathrm{Var}(Y) + (\mu_Y - c)^2, $$

because the cross term $2(\mu_Y - c)\,\mathbb{E}[Y - \mu_Y] = 0$ by linearity. So
$c \mapsto \mathbb{E}[(Y-c)^2]$ is $\mathrm{Var}(Y)$ plus a non-negative
parabola, minimized exactly at $c = \mu_Y$; in particular, for the midpoint
$m = \frac{a+b}{2}$,

$$ \mathrm{Var}(Y) \;\leq\; \mathbb{E}\big[(Y - m)^2\big]. $$

*Step B (deviations from the midpoint).* Since $a \leq Y \leq b$ pointwise,
$Y - m \in \big[-\frac{b-a}{2},\, \frac{b-a}{2}\big]$, so
$(Y - m)^2 \leq \big(\frac{b-a}{2}\big)^2$ pointwise; monotonicity of expectation
(Lecture 5 note Lemma 2.1) gives

$$ \mathbb{E}\big[(Y - m)^2\big]
   \;\leq\; \Big(\frac{b-a}{2}\Big)^{\!2} = \frac{(b-a)^2}{4}. $$

**End of proof.**

**Tightness, checked.** $Y = a$ or $b$ with probability $\frac12$ each has mean
$m$ and $\mathrm{Var}(Y) = \mathbb{E}[(Y - m)^2] = \big(\frac{b-a}{2}\big)^2$
exactly -- both proof inequalities are equalities. For $[a,b] = [0,1]$ this is
the fair coin, whose variance $\frac14$ Lecture 5 already identified as the
largest any coin can have; Lemma 3.1 is the same fact for arbitrary bounded
variables.

### 3.2 Technique 2: tilted distributions

**Definition (exponential tilting).** Let $X$ have pmf $p_X$ -- for a density,
the same formulas with $f_X$ -- and $M_X(t) = \mathbb{E}[e^{tX}] < \infty$. The
*tilted distribution* at parameter $t$ is

$$ p_t(x) \;=\; \frac{e^{tx}\, p_X(x)}{M_X(t)}. $$

**Well-definedness, checked.** The numerator is non-negative always;
$M_X(t) > 0$ because $e^{tX} > 0$ pointwise -- indeed
$M_X(t) \geq e^{t\mu}$ by Jensen, though positivity is all that is needed -- and
the total mass is
$\sum_x p_t(x) = \frac{1}{M_X(t)} \sum_x e^{tx} p_X(x)
= \frac{M_X(t)}{M_X(t)} = 1$. So $p_t$ is a genuine probability distribution for
every $t$ in the finiteness domain, with $p_0 = p_X$.

Two facts about tilting carry the whole proof. (i) *Direction:* for $t > 0$ the
reweighting factor $e^{tx}$ grows in $x$, so mass shifts toward large values;
this is intuition, not used formally. (ii) *Support preservation*, which *is*
used formally: $p_t(x) > 0$ exactly where $p_X(x) > 0$, because $e^{tx}$ is
strictly positive everywhere -- tilting can move weight along the support but can
never create mass outside it. In particular, if $X \in [a,b]$ with probability 1,
then a random variable distributed as $p_t$ is also in $[a,b]$ with probability
1, for *every* $t$. Write $\mathbb{E}_t$ and $\mathrm{Var}_t$ for mean and
variance under $p_t$. (Aside for orientation: tilted families are exactly the
exponential families of statistics, and $p_t$ is the Gibbs reweighting of
statistical mechanics; nothing below uses this.)

### 3.3 Technique 3: Taylor with Lagrange remainder

The calculus fact, stated with its hypotheses: if $f$ is twice differentiable on
an interval containing 0 and $t$, then there exists $\xi$ strictly between 0 and
$t$ with

$$ f(t) = f(0) + f'(0)\, t + \frac{f''(\xi)}{2}\, t^2. $$

This is an *exact equality* -- the unknown point $\xi$ absorbs the entire error --
so a uniform bound on $f''$ over the interval becomes a bound on $f$ with no
approximation loss. The standard proof goes via Rolle's theorem and the mean
value theorem; any calculus text, or [2, App. A] for the form used in
concentration arguments. Lecture 5's central-limit sketch used Taylor
asymptotically near 0; here the remainder form does the work at every fixed $t$.

### 3.4 Theorem 1, with the full proof

**Theorem 1 (Hoeffding's lemma [1], 1963).** If $X \in [a, b]$ with probability 1
and $\mathbb{E}[X] = 0$, then for all $t \in \mathbb{R}$:

$$ \mathbb{E}\big[e^{tX}\big] \;\leq\; \exp\!\Big( \frac{t^2 (b-a)^2}{8} \Big). $$

Note $a \leq 0 \leq b$ is forced: a variable confined to $[a,b]$ has its mean in
$[a,b]$. The target is the log-MGF $\psi(t) = \log M(t)$ with
$M(t) = \mathbb{E}[e^{tX}]$, and the claim
$\psi(t) \leq \frac{t^2(b-a)^2}{8}$. Since $X$ is bounded, $M(t)$ is finite for
all $t$, and it is twice differentiable with

$$ M'(t) = \mathbb{E}\big[X e^{tX}\big], \qquad
   M''(t) = \mathbb{E}\big[X^2 e^{tX}\big]. $$

For a finite-valued $X$ this is termwise differentiation of a finite sum,
elementary; for a general bounded $X$ the swap of derivative and expectation is
justified by dominated convergence, with the bound
$|X|e^{tX} \leq \max(|a|,|b|)\, e^{|t|\max(|a|,|b|)}$ doing the domination --
the same caveat, flagged the same way, as Lecture 5 note Section 6.2. Since
$M > 0$, $\psi$ is also twice differentiable, and Technique 3 applies. The four
steps:

**Step 1 (start flat).** $\psi(0) = \log M(0) = \log \mathbb{E}[e^0]
= \log 1 = 0$. By the chain rule $\psi'(t) = M'(t)/M(t)$, so

$$ \psi'(0) = \frac{M'(0)}{M(0)} = \frac{\mathbb{E}[X]}{1} = 0, $$

using $M'(0) = \mathbb{E}[X e^{0}] = \mathbb{E}[X] = 0$: the zero-mean hypothesis
kills the linear term.

**Step 2 (identify the derivatives as tilted moments).** First derivative:

$$ \psi'(t) = \frac{M'(t)}{M(t)} = \frac{\mathbb{E}[X e^{tX}]}{M(t)}
   = \sum_x x\, \frac{e^{tx} p_X(x)}{M(t)} = \sum_x x\, p_t(x)
   = \mathbb{E}_t[X], $$

the mean under the tilted distribution. Second derivative, by the quotient rule
on $\psi' = M'/M$:

$$ \psi''(t) = \frac{M''(t)\,M(t) - M'(t)^2}{M(t)^2}
   = \frac{M''(t)}{M(t)} - \Big(\frac{M'(t)}{M(t)}\Big)^{\!2}
   = \mathbb{E}_t[X^2] - \big(\mathbb{E}_t[X]\big)^2 = \mathrm{Var}_t(X), $$

where $M''(t)/M(t) = \sum_x x^2 p_t(x) = \mathbb{E}_t[X^2]$ by the same
computation as for $\psi'$. The curvature of the log-MGF *is* a variance -- in
particular $\psi$ is convex, and more importantly the variance is with respect to
a distribution we know something about.

**Step 3 (cap the curvature).** By support preservation (Section 3.2), the tilted
distribution lives on $[a, b]$ for every $t$; by Lemma 3.1 applied under $p_t$:

$$ \psi''(t) = \mathrm{Var}_t(X) \;\leq\; \frac{(b-a)^2}{4}
   \qquad \text{for every } t \in \mathbb{R}. $$

This is the only place boundedness is used -- and it is used through the tilted
variable, which is why support preservation had to be checked.

**Step 4 (integrate the cap).** Taylor with Lagrange remainder at 0
(Technique 3), for some $\xi$ between 0 and $t$, with $\psi(0) = 0$ and
$\psi'(0) = 0$ from Step 1:

$$ \psi(t) = 0 + 0 \cdot t + \frac{\psi''(\xi)}{2}\, t^2
   \;\leq\; \frac{1}{2}\cdot\frac{(b-a)^2}{4}\, t^2 = \frac{t^2 (b-a)^2}{8}. $$

Exponentiate, $\exp$ being increasing:
$\mathbb{E}[e^{tX}] = e^{\psi(t)} \leq \exp\big(\frac{t^2(b-a)^2}{8}\big)$.
**End of proof.**

The one-line summary chain is Steps 4, 2 and 3 read backwards: by Taylor
$\psi(t) = \frac{\psi''(\xi)}{2}t^2$; by $\psi'' = \mathrm{Var}$ this is
$\frac{\mathrm{Var}_\xi(X)}{2}t^2$; by support preservation this is at most
$\frac{(b-a)^2}{8}t^2$. Zero distribution knowledge entered -- only the interval.

### 3.5 Sanity check: fair signs, with the skipped inequality proved

Let $X = \pm 1$ with probability $\frac12$ each, a *Rademacher* variable: mean 0,
$[a,b] = [-1,1]$. Direct computation, expanding both exponentials in series and
noting the odd terms cancel:

$$ \mathbb{E}\big[e^{tX}\big] = \frac{e^t + e^{-t}}{2} = \cosh t
   = \sum_{k=0}^{\infty} \frac{t^{2k}}{(2k)!}. $$

**Claim (stated without proof in the source):** $(2k)! \geq 2^k\, k!$ for all
$k \geq 0$, hence $\cosh t \leq e^{t^2/2}$.

*Proof.* Write $(2k)! = k! \cdot (k+1)(k+2)\cdots(2k)$. Each of the $k$ trailing
factors satisfies $k + i \geq 2i$, equivalent to $k \geq i$, true for
$i = 1, \dots, k$; so their product is at least $\prod_{i=1}^{k} 2i = 2^k k!$.
Hence $(2k)! \geq 2^k (k!)^2 \geq 2^k k!$ -- the claim holds with room to spare.
Termwise in the series, which converges absolutely everywhere:

$$ \cosh t = \sum_{k=0}^\infty \frac{t^{2k}}{(2k)!}
   \;\leq\; \sum_{k=0}^\infty \frac{t^{2k}}{2^k k!}
   = \sum_{k=0}^\infty \frac{(t^2/2)^k}{k!} = e^{t^2/2}. $$

**End of proof.**

The lemma's promise for $[-1,1]$ is
$\exp\big(\frac{t^2 \cdot 2^2}{8}\big) = e^{t^2/2}$ -- the same answer,
confirming the constant 8.

**Unimprovability of the constant, made precise.** Suppose some envelope
$\mathbb{E}[e^{tX}] \leq e^{ct^2}$ held for all $t$ for every mean-zero
$X \in [a,b]$. Taking logs and Taylor-expanding both sides at $t = 0$ -- Step 2
gives $\psi(t) = \frac{\mathrm{Var}(X)}{2}t^2 + o(t^2)$ -- the inequality at
small $t$ forces $c \geq \frac{\mathrm{Var}(X)}{2}$ for every admissible $X$; the
two-point variable of Section 3.1 has $\mathrm{Var} = \frac{(b-a)^2}{4}$, forcing
$c \geq \frac{(b-a)^2}{8}$. So no smaller constant works for the whole class.

### 3.6 Corollary: any mean, same width

For $X \in [a,b]$ with arbitrary mean $\mu$: the centered variable $X - \mu$ has
mean 0 and lies in $[a - \mu,\, b - \mu]$, an interval of the *same width*
$b - a$. Theorem 1 applied to it gives, for all $t$,

$$ \mathbb{E}\big[e^{t(X - \mu)}\big]
   \;\leq\; \exp\!\Big( \frac{t^2 (b-a)^2}{8} \Big), $$

the form used from now on. What the lemma buys: every bounded variable has its
MGF under a *Gaussian envelope* with variance parameter $\frac{(b-a)^2}{4}$ --
for losses in $[0,1]$, the envelope $e^{t^2/8}$ -- so Chernoff becomes usable
with zero knowledge of the distribution. Variables admitting such an envelope
deserve a name.

## 4. Sub-Gaussian Variables

### 4.1 Definition, with the fine print

**Definition (sub-Gaussian with variance proxy $\sigma^2$).** A random variable
$X$ with finite mean $\mu$ is *$\sigma^2$-sub-Gaussian* if

$$ \mathbb{E}\big[e^{t(X - \mu)}\big] \;\leq\; \exp\!\Big( \frac{t^2 \sigma^2}{2} \Big)
   \qquad \text{for all } t \in \mathbb{R}. $$

Fine print. (i) The quantifier is *every* real $t$, both signs -- that is what
makes the two-sided tail bound of Section 4.3 come for free. (ii) $\sigma^2$ is a
*proxy*, not the variance: it is any constant making the envelope valid, and it
is not unique -- if $\sigma^2$ works, every larger constant works. One can show a
valid proxy always satisfies $\sigma^2 \geq \mathrm{Var}(X)$, by the small-$t$
Taylor comparison of Section 3.5, so the best proxy is at least the variance and
may be strictly larger. (iii) "Sub-Gaussian with parameter $\sigma$" in other
texts, for instance [3], sometimes means a norm-based definition; all versions
agree up to absolute constants, and Section 4.4 proves the direction that
connects them. (iv) The definition implicitly requires $M_{X-\mu}(t)$ finite for
all $t$ -- part of the condition, satisfied automatically by bounded variables
and Gaussians.

### 4.2 The two canonical examples, and every bounded variable

**Gaussian.** $X \sim \mathcal{N}(\mu, \sigma^2)$ has
$\mathbb{E}[e^{t(X-\mu)}] = e^{t^2\sigma^2/2}$ with *equality* for every $t$
(Section 2.3): the Gaussian is $\sigma^2$-sub-Gaussian with its own variance as
proxy, the tightest possible by (ii) above. The definition is calibrated so its
eponym passes exactly.

**Rademacher.** $X = \pm 1$ equiprobably: Section 3.5 showed
$\mathbb{E}[e^{tX}] = \cosh t \leq e^{t^2/2}$, so it is 1-sub-Gaussian -- again
with proxy equal to its variance, $\mathrm{Var} = 1$, hence unimprovable.
Gaussian and Rademacher are the two benchmark members of the class: one
continuous and unbounded, one two-valued; both sit exactly on their envelopes
near $t = 0$.

**Every bounded variable.** This is the answer to "why does bounded imply
sub-Gaussian with $\sigma = \frac{b-a}{2}$": Theorem 1 in the centered form of
Section 3.6 says $X \in [a,b]$ satisfies the definition with
$\frac{t^2\sigma^2}{2} = \frac{t^2(b-a)^2}{8}$, that is proxy
$\sigma^2 = \frac{(b-a)^2}{4}$, that is $\sigma = \frac{b-a}{2}$ -- *half the
width* of the support, the largest standard deviation the support permits
(Lemma 3.1), regardless of the distribution on it. Three instances, checked:

- plus-or-minus-1 signs: width 2, proxy $\frac{2^2}{4} = 1$;
- coin flip or 0/1 loss: width 1, proxy $\frac14$;
- loss clipped to $[0,c]$: width $c$, proxy $\frac{c^2}{4}$.

All three verified. Bounded losses -- the machine-learning case -- are
automatically sub-Gaussian.

### 4.3 Theorem 2: the tail bound, full proof

**Theorem 2 (sub-Gaussian tails).** If $X$ is $\sigma^2$-sub-Gaussian with mean
$\mu$ and $\sigma > 0$, then for every $\epsilon > 0$:

$$ \Pr\big( X - \mu \geq \epsilon \big)
   \;\leq\; \exp\!\Big( -\frac{\epsilon^2}{2\sigma^2} \Big),
   \qquad
   \Pr\big( |X - \mu| \geq \epsilon \big)
   \;\leq\; 2\exp\!\Big( -\frac{\epsilon^2}{2\sigma^2} \Big). $$

*Proof.* *Steps 1 and 2 (Chernoff, then envelope).* For any $t > 0$, Chernoff
(Section 2.1) applied to $X - \mu$ at threshold $\epsilon$, then the definition:

$$ \Pr(X - \mu \geq \epsilon) \;\leq\; e^{-t\epsilon}\,
   \mathbb{E}\big[e^{t(X-\mu)}\big]
   \;\leq\; \exp\!\Big( \frac{t^2\sigma^2}{2} - t\epsilon \Big). $$

The unknown distribution has left the argument: only $\sigma^2$ remains.

*Step 3 (optimize the free $t$).* The exponent
$g(t) = \frac{\sigma^2}{2}t^2 - \epsilon t$ is an upward parabola;
$g'(t) = \sigma^2 t - \epsilon = 0$ at $t^\star = \frac{\epsilon}{\sigma^2}$,
which is admissible since $\epsilon, \sigma^2 > 0$ make $t^\star > 0$, and

$$ g(t^\star) = \frac{\sigma^2}{2}\cdot\frac{\epsilon^2}{\sigma^4}
   - \epsilon\cdot\frac{\epsilon}{\sigma^2}
   = \frac{\epsilon^2}{2\sigma^2} - \frac{\epsilon^2}{\sigma^2}
   = -\frac{\epsilon^2}{2\sigma^2}. $$

Since the bound holds for every $t > 0$, it holds at $t^\star$:
$\Pr(X - \mu \geq \epsilon) \leq e^{-\epsilon^2/(2\sigma^2)}$.

*Lower tail:* $-X$, of mean $-\mu$, satisfies
$\mathbb{E}[e^{t(-X+\mu)}] = \mathbb{E}[e^{(-t)(X-\mu)}]
\leq e^{(-t)^2\sigma^2/2} = e^{t^2\sigma^2/2}$ -- the envelope is even in $t$, so
$-X$ is $\sigma^2$-sub-Gaussian too, and the one-sided bound applies to it:
$\Pr(X - \mu \leq -\epsilon) = \Pr((-X) - (-\mu) \geq \epsilon)
\leq e^{-\epsilon^2/(2\sigma^2)}$. The two-sided event is the union of the two
one-sided events; add the bounds -- this is already a two-event union bound,
ahead of Section 6. **End of proof.**

This is exactly Lecture 5's Chernoff routine with one substitution: the envelope
stands in for the true MGF. The content in words: sub-Gaussian means the true
tail never pokes above the Gaussian envelope $e^{-\epsilon^2/(2\sigma^2)}$ -- and
for a bounded variable the true tail in fact drops to 0 at the support edge,
strictly below the envelope, which never reaches 0.

### 4.4 Omitted detail: the reverse direction (tails imply an MGF envelope)

Theorem 2 is one direction of an equivalence: Gaussian-type tails also imply a
sub-Gaussian MGF envelope, with a worse constant. Here is the statement and a
proof at the level of this course -- one exponential-comparison lemma plus one
integral. It is what justifies treating "sub-Gaussian" as a property of tails
rather than of the MGF.

**Proposition (tail implies envelope).** Suppose $Y$ has mean 0 and
$\Pr(|Y| \geq \epsilon) \leq 2e^{-\epsilon^2/(2\sigma^2)}$ for all
$\epsilon > 0$. Then $\mathbb{E}[e^{\lambda Y}] \leq e^{8\lambda^2\sigma^2}$ for
all $\lambda \in \mathbb{R}$, that is, $Y$ is $16\sigma^2$-sub-Gaussian. The
constant 16 is convenient, not optimal.

**Lemma A.** $e^x \leq x + e^{x^2}$ for all real $x$.

*Proof.* Three ranges. For $x \geq 1$: $x^2 \geq x$ so $e^{x^2} \geq e^x$, and
adding $x > 0$ only helps. For $x \leq 0$: the standard bound
$e^x \leq 1 + x + \frac{x^2}{2}$ holds there -- the function
$h(x) = 1 + x + \frac{x^2}{2} - e^x$ has $h(0) = 0$ and
$h'(x) = 1 + x - e^x \leq 0$ everywhere, so $h$ is non-increasing and
$h \geq 0$ on $x \leq 0$ -- and $1 + \frac{x^2}{2} \leq e^{x^2}$ since
$e^u \geq 1 + u$. For $0 \leq x \leq 1$:
$e^x = 1 + x + x^2\sum_{k \geq 2} \frac{x^{k-2}}{k!}
\leq 1 + x + x^2(e - 2) \leq 1 + x + x^2 \leq x + e^{x^2}$, again by
$e^u \geq 1 + u$. **End of proof of Lemma A.**

**Lemma B (squared-exponential moment).** For
$0 < s \leq \frac{1}{4\sigma^2}$, write the expectation of a non-negative
variable through its tail -- the layer-cake identity
$\mathbb{E}[g(V)] = g(0) + \int_0^\infty g'(u)\Pr(V \geq u)\,du$ for increasing
differentiable $g \geq 0$, here $g(u) = e^{su}$ and $V = Y^2$:

$$ \mathbb{E}\big[e^{sY^2}\big]
   = 1 + \int_0^\infty s\,e^{su}\, \Pr(Y^2 \geq u)\, du
   \;\leq\; 1 + 2s \int_0^\infty e^{su}\, e^{-u/(2\sigma^2)}\, du
   = 1 + \frac{2s}{\frac{1}{2\sigma^2} - s}, $$

the integral converging because $s < \frac{1}{2\sigma^2}$. For
$s \leq \frac{1}{4\sigma^2}$ the denominator is at least
$\frac{1}{4\sigma^2}$, so
$\mathbb{E}[e^{sY^2}] \leq 1 + 8s\sigma^2 \leq e^{8s\sigma^2}$.
**End of proof of Lemma B.**

*Proof of the Proposition.* *Small $\lambda$*, meaning
$\lambda^2 \leq \frac{1}{4\sigma^2}$: Lemma A pointwise at $x = \lambda Y$, then
expectations, then $\mathbb{E}[Y] = 0$ and Lemma B at $s = \lambda^2$:

$$ \mathbb{E}\big[e^{\lambda Y}\big] \;\leq\; \lambda\,\mathbb{E}[Y]
   + \mathbb{E}\big[e^{\lambda^2 Y^2}\big]
   \;\leq\; e^{8\lambda^2\sigma^2}. $$

*Large $\lambda$*, meaning $\lambda^2 > \frac{1}{4\sigma^2}$: by Young's
inequality $uv \leq \frac{u^2 + v^2}{2}$ with $u = \sqrt{2}\,\lambda\sigma$ and
$v = \frac{Y}{\sqrt{2}\,\sigma}$, pointwise
$\lambda Y \leq \lambda^2\sigma^2 + \frac{Y^2}{4\sigma^2}$, so
$\mathbb{E}[e^{\lambda Y}] \leq e^{\lambda^2\sigma^2}\,
\mathbb{E}[e^{Y^2/(4\sigma^2)}] \leq e^{\lambda^2\sigma^2} \cdot 3$, using
Lemma B at $s = \frac{1}{4\sigma^2}$ whose bound is $1 + 2 = 3$. Since
$3 = e^{\ln 3} \leq e^{1.1}$ and $1.1 \leq 4.4\,\lambda^2\sigma^2$ in this range,
where $\lambda^2\sigma^2 > \frac14$, this gives
$\mathbb{E}[e^{\lambda Y}] \leq e^{5.4\lambda^2\sigma^2}
\leq e^{8\lambda^2\sigma^2}$. **End of proof.**

Together with Theorem 2, this says the MGF envelope and the Gaussian tail bound
are the *same property* up to the value of the constant -- a factor 16 here;
sharper arguments bring it down, see [3, Prop. 2.5.2] for the full list of five
equivalent characterizations, including moment growth
$\mathbb{E}|Y|^k \leq (C\sigma\sqrt{k})^k$. None of the lecture's results need
the reverse direction; it is included because "sub-Gaussian" is used tail-first
in most of the literature this lecture points to.

### 4.5 Closure rules, with full proofs

**Rule 1 (scaling).** If $X$ is $\sigma^2$-sub-Gaussian with mean $\mu$ and
$c \in \mathbb{R}$, then $cX$, of mean $c\mu$, is $c^2\sigma^2$-sub-Gaussian.

*Proof.* For any $t$:
$\mathbb{E}[e^{t(cX - c\mu)}] = \mathbb{E}[e^{(tc)(X-\mu)}]
\leq e^{(tc)^2\sigma^2/2} = e^{t^2(c^2\sigma^2)/2}$, using the definition at the
still arbitrary real argument $tc$. The case $c = 0$ is trivial.
**End of proof.**

**Rule 2 (independent sums).** If $X_1, \dots, X_n$ are mutually independent and
$X_i$ is $\sigma_i^2$-sub-Gaussian with mean $\mu_i$, then $\sum_i X_i$, of mean
$\sum_i \mu_i$, is $\big(\sum_i \sigma_i^2\big)$-sub-Gaussian.

*Proof.* For any $t$, the $n$-fold product rule (Section 2.2, applied to the
functions $e^{t(x_i - \mu_i)}$ of independent variables), then each envelope:

$$ \mathbb{E}\Big[ e^{t \sum_i (X_i - \mu_i)} \Big]
   = \prod_{i=1}^n \mathbb{E}\big[ e^{t(X_i - \mu_i)} \big]
   \;\leq\; \prod_{i=1}^n e^{t^2\sigma_i^2/2}
   = \exp\!\Big( \frac{t^2}{2} \sum_{i=1}^n \sigma_i^2 \Big). $$

**End of proof.**

**Consequence (averages).** For $X_i$ i.i.d., each $\sigma^2$-sub-Gaussian:
Rule 2 gives $\sum_i X_i$ proxy $n\sigma^2$; Rule 1 with $c = \frac1n$ gives
$\bar X_n = \frac1n \sum_i X_i$ proxy
$\frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$. Averaging shrinks the proxy by $n$
-- the sub-Gaussian analogue of $\mathrm{Var}(\bar X_n) = \sigma^2/n$
(Lecture 5 note Lemma 4.1).

**Where independence is needed.** Rule 2's product step is the only use. Without
independence, proxies do *not* add -- but sub-Gaussianity survives with the worse
constant $\big(\sum_i \sigma_i\big)^2$, provable with Holder's inequality; the
extreme case $X_1 = X_2 = \cdots$ shows this is the right order, since then the
sum is $nX_1$ with proxy $n^2\sigma^2$ by Rule 1. Today every sum is a sum of
independent losses, so the clean additive rule applies.

## 5. Hoeffding's Inequality

### 5.1 Theorem 3, assembled

**Theorem 3 (Hoeffding's inequality [1], 1963).** Let $X_1, \dots, X_n$ be
independent with $X_i \in [a, b]$ with probability 1 and common mean $\mu$; let
$\epsilon > 0$. Then

$$ \Pr\big( \bar{X}_n - \mu \geq \epsilon \big)
   \;\leq\; \exp\!\Big( -\frac{2 n \epsilon^2}{(b-a)^2} \Big),
   \qquad
   \Pr\big( |\bar{X}_n - \mu| \geq \epsilon \big)
   \;\leq\; 2\exp\!\Big( -\frac{2 n \epsilon^2}{(b-a)^2} \Big). $$

*Proof.* Pure assembly.

*Step 1:* each $X_i - \mu \in [a - \mu, b - \mu]$, of width $b - a$ and mean 0;
Theorem 1, via Section 3.6, makes each $X_i$ $\frac{(b-a)^2}{4}$-sub-Gaussian.
Identical distributions are *not* needed -- only the shared range and mean.

*Step 2:* Rule 2 then Rule 1 (Section 4.5): $\bar X_n$ has mean $\mu$ by
linearity and proxy

$$ \frac{1}{n^2} \cdot n \cdot \frac{(b-a)^2}{4} = \frac{(b-a)^2}{4n}. $$

*Step 3:* Theorem 2 with this proxy:
$\Pr(\bar X_n - \mu \geq \epsilon)
\leq \exp\big(-\frac{\epsilon^2}{2 (b-a)^2/(4n)}\big)
= \exp\big(-\frac{2n\epsilon^2}{(b-a)^2}\big)$. Two-sided: each
$-X_i \in [-b, -a]$, same width, mean $-\mu$, so the one-sided bound applies to
the lower tail identically; add. **End of proof.**

The Chernoff-first re-derivation, since it is the route usually written: for
$t > 0$,

$$ \Pr(\bar X_n - \mu \geq \epsilon)
   \leq e^{-t\epsilon}\,\mathbb{E}[e^{t(\bar X_n - \mu)}]
   = e^{-t\epsilon} \prod_i \mathbb{E}\big[e^{\frac tn (X_i - \mu)}\big] $$

by the scale rule inside the product rule, which is at most

$$ e^{-t\epsilon}\, e^{n \cdot \frac{(t/n)^2 (b-a)^2}{8}}
   = e^{\frac{t^2(b-a)^2}{8n} - t\epsilon}; $$

minimizing over $t$ -- a parabola, minimized at
$t^\star = \frac{4n\epsilon}{(b-a)^2}$ -- gives exponent
$-\frac{2n\epsilon^2}{(b-a)^2}$, the same constant. So the 2 upstairs in
Theorem 3 and the 8 in the lemma are one constant moved around.

**Omitted generalization** (Hoeffding's own statement [1]): with different ranges
$X_i \in [a_i, b_i]$, the same assembly gives

$$ \Pr\Big(\sum_i (X_i - \mathbb{E}X_i) \geq \epsilon\Big)
   \leq \exp\Big(-\frac{2\epsilon^2}{\sum_i (b_i - a_i)^2}\Big), $$

nothing new being needed, only Rule 2 with unequal proxies.

### 5.2 The coin returns: all three numbers verified

Fair coin, $[a,b] = [0,1]$, $\mu = \frac12$, $\epsilon = \frac14$, $n = 100$:

$$ \Pr\big( \bar{X}_{100} \geq \tfrac34 \big)
   \;\leq\; e^{-2 \cdot 100 \cdot (1/4)^2} = e^{-200/16} = e^{-12.5}
   = 3.7266\ldots \times 10^{-6}, $$

that is $3.7 \times 10^{-6}$. The comparison rows: Lecture 5's optimal Chernoff
bound is $e^{-100\,\mathrm{KL}(3/4\,\Vert\,1/2)}$ with
$\mathrm{KL}(\frac34\Vert\frac12) = \frac34\ln\frac32 + \frac14\ln\frac12
= 0.130812$, giving $e^{-13.0812} = 2.084 \times 10^{-6}$, about
$2.1 \times 10^{-6}$ -- verified. The exact tail
$\Pr(S_{100} \geq 75) = \sum_{k=75}^{100}\binom{100}{k}2^{-100}
= 2.818 \times 10^{-7}$, about $2.8 \times 10^{-7}$ -- recomputed from scratch,
matching the Lecture 5 note. The exponents: Hoeffding
$2\epsilon^2 = 2 \cdot \frac{1}{16} = 0.125$ per flip versus optimal $0.1308$;
the price of knowing only the range is
$\frac{0.1308 - 0.125}{0.1308} = 4.4$ percent of the exponent, so the source's
"about 4 percent" is fair, the exact figure being 4.4 percent. Near-optimal
tails, zero distribution knowledge.

### 5.3 Worked example: plus-or-minus 2 percent at 95 percent, the inversion in full

Demand $\Pr(|\bar X_n - \mu| \geq 0.02) \leq 0.05$ for losses in $[0,1]$.
Two-sided Hoeffding gives the bound $2e^{-2n(0.02)^2}$; set it at most 0.05 and
solve, step by step:

$$ 2e^{-2n(0.02)^2} \leq 0.05
   \iff e^{2n \cdot 0.0004} \geq \frac{2}{0.05} = 40
   \iff n \geq \frac{\ln 40}{0.0008}. $$

Since $\ln 40 = 3.68888$, this is $n \geq 4611.10$, that is $n \geq 4612$
samples by the integer ceiling. Chebyshev on the same question (Lecture 5 note
Section 4.7, worst-case coin variance $\frac14$):
$\frac{1}{4n\epsilon^2} \leq 0.05
\iff n \geq \frac{1}{4 \cdot 0.0004 \cdot 0.05} = 12{,}500$ -- verified; the
ratio $\frac{12500}{4612} = 2.71$ is the claimed "one 2.7th of the data". At
$\delta = 0.001$: Chebyshev
$\frac{1}{4 \cdot 0.0004 \cdot 0.001} = 625{,}000$; Hoeffding
$\frac{\ln 2000}{0.0008} = 9501.13$, so $9{,}502$ -- both verified. The scaling
behind the widening gap: Chebyshev's $n \propto \frac{1}{\delta}$ versus
Hoeffding's $n \propto \ln\frac{1}{\delta}$.

What Hoeffding buys, with the dependencies explicit:
$n \geq \frac{\ln(2/\delta)}{2\epsilon^2}$ -- distribution-free, since only the
range enters; *logarithmic* in $\frac1\delta$, so confidence is cheap; quadratic
in $\frac1\epsilon$, so precision is expensive. One fixed hypothesis is now fully
handled; ERM searches many.

## 6. The Union Bound

### 6.1 Theorem 4, with the one-line proof expanded

**Theorem 4 (union bound, Boole's inequality).** For any events
$A_1, \dots, A_m$ -- no independence, no disjointness, no structure whatsoever:

$$ \Pr\!\Big( \bigcup_{j=1}^m A_j \Big) \;\leq\; \sum_{j=1}^m \Pr(A_j). $$

*Proof.* Pointwise indicator inequality first: for every outcome $\omega$,

$$ \mathbf{1}\Big\{ \bigcup_j A_j \Big\}(\omega)
   \;\leq\; \sum_{j=1}^m \mathbf{1}\{A_j\}(\omega). $$

Check by cases: if $\omega$ lies in none of the $A_j$, both sides are 0; if
$\omega$ lies in at least one, the left side is 1 while the right side counts the
number of $A_j$ containing $\omega$, which is at least 1. Take expectations, by
monotonicity and linearity (Lecture 5 note Lemma 2.1), and use
$\mathbb{E}[\mathbf{1}\{A\}] = \Pr(A)$ on every term. **End of proof.**

The proof also delivers the equality condition: the pointwise gap is the number
of memberships minus one on the union, so equality holds if and only if outcomes
lying in two or more $A_j$ have total probability 0 -- equality iff essentially
disjoint; overlap is double-counted. The bound extends verbatim to countably many
events, with a sum on the right and the same proof using monotone convergence;
not needed today, where $m = |\mathcal{H}|$ is finite.

### 6.2 Omitted detail: how loose is it?

Exact inclusion-exclusion for two events,
$\Pr(A_1 \cup A_2) = \Pr(A_1) + \Pr(A_2) - \Pr(A_1 \cap A_2)$, shows the slack is
precisely the overlap mass. Two regimes matter in practice. (i) *Small individual
probabilities:* for independent events with $\Pr(A_j) = p$, the truth is
$1 - (1-p)^m \approx mp - \binom{m}{2}p^2$, and the bound $mp$ overshoots by
$O(m^2p^2)$ -- negligible when $mp \ll 1$. For the model farm of Section 6.3: the
bound is 3.727 percent, and the exact value if the events were independent is
$1 - (1 - 3.7266\times10^{-6})^{10^4} = 3.658$ percent, so the union bound gives
away almost nothing. (ii) *Large total:* once $\sum_j \Pr(A_j) > 1$ the bound is
vacuous while the truth is still a probability; the $n = 25$ farm below is
exactly this regime.

Deeper looseness in the generalization application: the events $B_h$ for similar
hypotheses $h$ are strongly overlapping -- similar classifiers err together --
and the union bound charges them as if disjoint. This, not Hoeffding, is the
slack that VC and Rademacher theory (Section 7.8) recovers.

### 6.3 The model farm, verified

Take $m = 10^4$ useless models, each of true accuracy 50 percent, that is each a
fixed hypothesis with $R = \frac12$, all shown on the same $n = 100$ test points;
let $A_j$ be the event "model $j$ shows at least 75 percent". Per model,
Hoeffding (Section 5.2) gives
$\Pr(A_j) \leq e^{-12.5} = 3.7266 \times 10^{-6}$ -- note this holds for *each
fixed* $j$ regardless of how the models relate, since each $A_j$ concerns one
fixed hypothesis. Union:

$$ \Pr\Big( \bigcup_{j=1}^{10^4} A_j \Big)
   \;\leq\; 10^4 \times 3.7266 \times 10^{-6} = 0.0373 = 3.7\ \text{percent}, $$

verified at 3.73 percent: with probability at least 96 percent, no guesser fakes
75 percent.

Shrink the test set to $n = 25$: per model
$e^{-2 \cdot 25 \cdot (1/4)^2} = e^{-3.125} = 0.04394$, about 0.044, and the
union bound gives $10^4 \times 0.0439 = 439.4$, about 440 -- vacuous, verified.
And rightly vacuous: the *expected number* of faking guessers is
$10^4 \times 0.0439 \approx 439$, which is what the sum of probabilities
literally is, by linearity over indicators; so several *will* fake 75 percent. If
the models' test scores were independent, the probability that at least one fakes
would be $1 - (1 - 0.0439)^{10^4} \approx 1$ to machine precision. The exponent
must beat the head count: $e^{-2n\epsilon^2} \cdot m \leq \delta$ requires
$n \geq \frac{\ln m + \ln(1/\delta)}{2\epsilon^2}$, so $n$ grows with $\ln m$.

### 6.4 Budgeting: the Bonferroni split

To keep the total failure probability at most $\delta$ over $m$ events, give each
event a budget of $\delta/m$: if $\Pr(A_j) \leq \frac{\delta}{m}$ for each $j$,
then $\Pr(\bigcup_j A_j) \leq m \cdot \frac{\delta}{m} = \delta$. In statistics
this is the Bonferroni correction for multiple comparisons. The reason it is
affordable with exponential tails: pushing a per-event Hoeffding budget from
$\delta$ down to $\delta/m$ requires
$e^{-2n\epsilon^2} \leq \frac{\delta}{m}$ instead of $\leq \delta$, that is an
additive $+\ln m$ inside the exponent's requirement -- a factor $m$ in
probability is only $\ln m$ in samples. This one accounting rule, applied to
$\mathcal{H}$, is the next section.

## 7. The Generalization Theorem

### 7.1 Finite hypothesis classes

Let $\mathcal{H} = \{h_1, \dots, h_{|\mathcal{H}|}\}$ be finite. Two examples,
unpacked. *Decision stumps on 8-bit images:* a stump thresholds a single pixel;
choosing which of $d$ pixels and which of the 256 possible 8-bit threshold values
gives $|\mathcal{H}| = 256\,d$, counting one orientation of the decision --
allowing both "at least the threshold predicts 1" and "at least the threshold
predicts 0" doubles it, and only one is counted here. *Quantized nets:* any
architecture whose weights are stored in $k$ bits total takes at most $2^k$
distinct configurations, so $|\mathcal{H}| = 2^k$. The second example is the
important one: **every model that fits in a finite file is a member of a finite
class**, with $\ln|\mathcal{H}| = k \ln 2$ proportional to its description length
in bits -- the reading developed in Section 7.5.

### 7.2 The key observation: a fixed hypothesis is a coin

**Lemma 7.1.** Fix $h$ before the sample and set $W_i = \ell(h, Z_i)$. Then
$W_1, \dots, W_n$ are i.i.d., $W_i \in [0,1]$, $\mathbb{E}[W_i] = R(h)$, and
$\hat R_n(h) = \bar W_n$. Consequently, by two-sided Hoeffding (Theorem 3 with
$[a,b] = [0,1]$):

$$ \Pr\big( |\hat{R}_n(h) - R(h)| \geq \epsilon \big) \;\leq\; 2 e^{-2n\epsilon^2}. $$

*Proof.* Each $W_i$ is the *same fixed function* $z \mapsto \ell(h, z)$ applied
to $Z_i$; identical functions of identically distributed inputs are identically
distributed, and functions of independent inputs are independent -- the
factorization of the joint law is preserved under coordinatewise maps, as in the
Lecture 3 note. $W_i \in [0,1]$ since $\ell$ is;
$\mathbb{E}[W_i] = \mathbb{E}[\ell(h, Z_i)]
= \mathbb{E}_{Z\sim\mathcal{D}}[\ell(h,Z)] = R(h)$ since $Z_i \sim \mathcal{D}$;
and $\hat R_n(h) = \frac1n\sum_i W_i$ by definition. **End of proof.**

**The trap, stated precisely.** The lemma's proof uses that $h$ is the same fixed
function for every $i$, chosen without reference to the sample. Substituting
$h = \hat h$ breaks the very first step: $\hat h$ is itself a function of
$(Z_1, \dots, Z_n)$, so $\ell(\hat h, Z_i)$ is a function of the *whole* sample,
not of $Z_i$ alone -- the terms are neither independent nor of mean
$R(\hat h)$, and Theorem 3's hypotheses fail. This is not pedantry: ERM actively
*selects for* hypotheses whose empirical losses fluctuated low, and Section 6.3's
farm showed that the best of $10^4$ fixed hypotheses violating its own
per-hypothesis bound is routine at small $n$.

The fix: bound all hypotheses *simultaneously*, so the certificate exists before
any selection happens. Define the uniform convergence event

$$ G_\epsilon \;=\; \big\{ \, |\hat{R}_n(h) - R(h)| \leq \epsilon
   \ \text{ for all } h \in \mathcal{H} \, \big\}. $$

On $G_\epsilon$, *whatever* $h$ any algorithm picks -- ERM, SGD, a human staring
at the data -- its gap is at most $\epsilon$, because the guarantee quantifies
over all of $\mathcal{H}$ in advance. Data-dependence of the choice becomes
irrelevant. For finite $\mathcal{H}$, $G_\epsilon$ is a finite intersection of
events, so there are no measurability subtleties.

### 7.3 Theorem 5, with the full three-step proof

**Theorem 5 (uniform convergence, finite class).** Let $\mathcal{H}$ be finite,
$Z_1, \dots, Z_n$ i.i.d. from $\mathcal{D}$, $\ell \in [0,1]$, and
$\delta \in (0,1)$. With probability at least $1 - \delta$,

$$ \sup_{h \in \mathcal{H}} \big| R(h) - \hat{R}_n(h) \big|
   \;\leq\; \sqrt{ \frac{ \ln\!\big( 2 |\mathcal{H}| / \delta \big) }{ 2n } }. $$

*Proof.* Fix $\epsilon > 0$, to be chosen in Step 3.

*Step 1 (one hypothesis).* For each fixed $h \in \mathcal{H}$, let
$B_h = \{ |\hat R_n(h) - R(h)| > \epsilon \}$. Lemma 7.1 gives
$\Pr(B_h) \leq 2e^{-2n\epsilon^2}$.

*Step 2 (union over the class).* The failure event "some hypothesis deviates" is
exactly $\bigcup_{h \in \mathcal{H}} B_h$, whose complement is $G_\epsilon$ up to
the boundary case of equality, which only helps. Theorem 4 applies -- and its
total indifference to how the $B_h$ overlap and depend on each other is precisely
what is needed, since they are heavily dependent, all built from one sample:

$$ \Pr\Big( \bigcup_{h \in \mathcal{H}} B_h \Big)
   \;\leq\; \sum_{h \in \mathcal{H}} \Pr(B_h)
   \;\leq\; 2\, |\mathcal{H}|\, e^{-2n\epsilon^2}. $$

*Step 3 (invert).* Set the right side equal to the budget $\delta$ and solve for
$\epsilon$, each step reversible:

$$ 2 |\mathcal{H}|\, e^{-2n\epsilon^2} = \delta
   \iff e^{2n\epsilon^2} = \frac{2|\mathcal{H}|}{\delta}
   \iff 2n\epsilon^2 = \ln\frac{2|\mathcal{H}|}{\delta}
   \iff \epsilon = \sqrt{ \frac{\ln(2|\mathcal{H}|/\delta)}{2n} }, $$

the log being positive since $2|\mathcal{H}| \geq 2 > \delta$, so the square root
is real. With this $\epsilon$:
$\Pr\big( \sup_h |R - \hat R_n| > \epsilon \big) \leq \delta$, that is, the
displayed bound holds with probability at least $1 - \delta$. For finite
$\mathcal{H}$ the supremum is a maximum over finitely many values, so no analytic
care is needed. **End of proof.**

Reading: one sample, one guarantee, every hypothesis. The trick is to pay for the
search *before* it happens; the exponential tail beats the head count because
$|\mathcal{H}|$ enters only through a logarithm.

### 7.4 The ERM corollary, three hops in full

**Corollary (ERM guarantee).** Let $\hat h$ be any empirical risk minimizer and
$h^\star \in \operatorname{argmin}_{h \in \mathcal{H}} R(h)$ a true-risk
minimizer -- both exist, the class being finite. On the event of Theorem 5, of
probability at least $1 - \delta$, with
$\epsilon = \sqrt{\frac{\ln(2|\mathcal{H}|/\delta)}{2n}}$:

$$ R(\hat{h}) \;\leq\; \min_{h \in \mathcal{H}} R(h) + 2\epsilon. $$

*Proof.* On $G_\epsilon$, every $h$ satisfies both
$R(h) \leq \hat R_n(h) + \epsilon$ and $\hat R_n(h) \leq R(h) + \epsilon$. Chain
three inequalities: by the tube at $\hat h$,

$$ R(\hat{h}) \;\leq\; \hat{R}_n(\hat{h}) + \epsilon; $$

by the definition of ERM, $\hat R_n(\hat h) \leq \hat R_n(h^\star)$, so this is

$$ \leq\; \hat{R}_n(h^\star) + \epsilon; $$

and by the tube at $h^\star$, $\hat R_n(h^\star) \leq R(h^\star) + \epsilon$, so
altogether

$$ R(\hat h) \;\leq\; \big(R(h^\star) + \epsilon\big) + \epsilon
   = R(h^\star) + 2\epsilon. $$

**End of proof.**

Anatomy of the three hops, since each uses a different resource. Hop 1 is the
*upper* half of the tube at the random $\hat h$ -- legitimate because
$G_\epsilon$ covers every hypothesis, including whichever one $\hat h$ turns out
to be. The middle hop is the *definition* of ERM, $\hat h$ minimizing
$\hat R_n$, so its empirical risk is at most that of $h^\star$ -- no probability
at all. Hop 3 is the *lower* half of the tube at the fixed $h^\star$. The tube is
crossed twice, once at each hypothesis, hence $2\epsilon$ rather than $\epsilon$.
Both tube directions were genuinely used, which is why Theorem 5 had to be
two-sided.

### 7.5 Reading the rate: $\ln|\mathcal{H}|$ is bits

For the class of all models describable in $k$ bits, $|\mathcal{H}| = 2^k$ and

$$ \epsilon \;=\; \sqrt{ \frac{\ln(2 \cdot 2^k/\delta)}{2n} }
   \;=\; \sqrt{ \frac{k \ln 2 + \ln(2/\delta)}{2n} }, $$

by $\ln(2^k) = k\ln 2$ -- description length enters *linearly* in the numerator.
Complexity is measured in bits needed to write the model down, an echo of
Lecture 1's $\log M$ as the information in a choice among $M$ alternatives.
Inverting for $n$, by the same algebra as Step 3, the gap is at most $\epsilon$
with confidence $1 - \delta$ as soon as

$$ n \;\geq\; \frac{ \ln|\mathcal{H}| + \ln(2/\delta) }{ 2 \epsilon^2 }. $$

Per bit of model, the marginal cost is $\frac{\ln 2}{2\epsilon^2}$ samples
$= \frac{0.6931}{2 \cdot 0.0025} = 138.6$, about 139, at $\epsilon = 0.05$ --
verified. Precision dominates: halving $\epsilon$ quadruples $n$; confidence is
nearly free, entering through the logarithm of $\frac1\delta$.

### 7.6 The sample-size numbers, re-derived (one rounding slip found)

Setting $\epsilon = 0.05$ and $\delta = 0.05$ gives
$n \geq 200\big(\ln|\mathcal{H}| + \ln 40\big)$ with $\ln 40 = 3.6889$. Row by
row -- class size, then $\ln|\mathcal{H}|$, then
$200(\ln|\mathcal{H}| + 3.6889)$, then the integer sample size needed by
ceiling, then the value shown in the source deck:

- $|\mathcal{H}| = 10$: $\ln = 2.3026$; $1198.29$; need $1{,}199$; source
  $1{,}199$ -- agrees.
- $|\mathcal{H}| = 10^3$: $\ln = 6.9078$; $2119.33$; need $2{,}120$; source
  $2{,}120$ -- agrees.
- $|\mathcal{H}| = 10^6$: $\ln = 13.8155$; $3500.88$; need $3{,}501$; source
  $3{,}501$ -- agrees.
- $|\mathcal{H}| = 2^{100}$: $\ln = 69.3147$; $14600.72$; need $14{,}601$;
  source $14{,}600$ -- off by one.

**Discrepancy, for the record:** the last row's requirement is
$n \geq 14{,}600.72$, so the smallest integer sample size is $14{,}601$; the
source's $14{,}600$ rounds down instead of up. The qualitative claim is
untouched: a million hypotheses cost only
$\frac{3501}{1199} \approx 2.9$ times the data of ten -- logarithms are kind.

### 7.7 The bits-versus-samples line and the confidence numbers (same slip pattern)

The line is $n = 200\ln 40 + (200\ln 2)\,k = 737.78 + 138.63\,k$. The source's
caption "$n \approx 739 + 139\,k$" rounds each coefficient up-ish; the honest
rounding of the intercept is 738. Its plotted points, exactly -- bit budget $k$,
then the raw value, then the ceiling, then the value shown:

- $k = 10$: $2124.07$; ceiling $2{,}125$; source $2{,}124$.
- $k = 50$: $7669.25$; ceiling $7{,}670$; source $7{,}669$.
- $k = 100$: $14600.72$; ceiling $14{,}601$; source $14{,}600$.

So all three labels round the raw value down instead of taking the ceiling --
each off by one sample, immaterial at this scale but noted.

Confidence numbers at $\epsilon = 0.05$, where the extra samples over the
95-percent baseline are $200\big(\ln(2/\delta) - \ln 40\big)$: at 99.9 percent,
$200(\ln 2000 - \ln 40) = 200\ln 50 = 782.4$, shown as $+782$, rounded down;
ceiling against ceiling gives $+783$. At $1 - 10^{-9}$,
$\ln(2 \times 10^9) = 21.416$ and the extra is $3545.5$, shown as $+3{,}545$,
same rounding. The headline stands: from 95 percent to one-in-a-billion failure
costs a few thousand samples -- confidence is nearly free.

### 7.8 What breaks for infinite classes, and the road ahead

All linear classifiers in $\mathbb{R}^d$ form an uncountable class:
$|\mathcal{H}| = \infty$, $\ln|\mathcal{H}| = \infty$, and Theorem 5 says nothing
-- the union bound charged every member separately, and infinitely many members
cost infinitely much. But the charge was too crude: on any *fixed* $n$ sample
points, infinitely many linear classifiers produce only finitely many distinct
labelings, at most $O(n^d)$ of them, so "different hypotheses" that behave
identically on the data were each billed separately for the same event.

**VC dimension** replaces $\ln|\mathcal{H}|$ by the logarithm of the number of
achievable *behaviors on $n$ points*, via the growth function and the
symmetrization argument. **Rademacher complexity** replaces it by a direct
measurement of how well $\mathcal{H}$ can correlate with random plus-or-minus-1
signs on the sample. Both yield bounds of the same
$\sqrt{\text{complexity}/n}$ shape, with the Hoeffding-plus-union skeleton
surviving inside the proofs. Developed properly in [4, Ch. 6-26 selections] and
[5, Ch. 3]; this lecture names them and stops, and so does this note.

## 8. Why ERM Works

### 8.1 The license to train, and the trade-off

Theorem 5 certifies the proxy that ERM minimizes: when $n \gg \ln|\mathcal{H}|$,
$\hat R_n \approx R$ everywhere on $\mathcal{H}$, so minimizing the computable
$\hat R_n$ is nearly minimizing the wanted $R$ -- training loss becomes a
certified preview of test loss, which is what "learning is possible" means in
this framework. The corollary splits the achievable risk into two competing
terms, an *approximation* term and an *estimation* term:

$$ R(\hat{h}) \;\leq\; \underbrace{\min_{h \in \mathcal{H}} R(h)}_{\text{approximation}}
   \;+\; \underbrace{2\sqrt{ \tfrac{\ln(2|\mathcal{H}|/\delta)}{2n} }}_{\text{estimation}}. $$

Growing $\mathcal{H}$ shrinks the approximation term -- a richer class contains
better hypotheses, the minimum over a superset being no larger -- and grows the
estimation term, through $\ln|\mathcal{H}|$ in the numerator. Their sum is the
U-shaped overfitting curve, now derived rather than drawn; more data pushes the
estimation curve down, so the optimal class size grows with the dataset.
Lecture 7 and the optimization track pick up this decomposition by name.

### 8.2 Honest accounting: deep nets break this bound -- numbers verified

ResNet-50 has $25.6 \times 10^6$ parameters at 32 bits each, that is
$8.192 \times 10^8$ bits, so
$\ln|\mathcal{H}| = 8.192\times10^8 \ln 2 = 5.678 \times 10^8$, about
$5.7 \times 10^8$ -- verified. With $n = 1.28 \times 10^6$, the ImageNet training
set size, and dropping the negligible $\ln(2/\delta)$:

$$ \epsilon \;=\; \sqrt{ \frac{5.678 \times 10^8}{2 \times 1.28 \times 10^6} }
   \;=\; \sqrt{221.8} \;=\; 14.9, $$

verified at $14.89$; the displayed fraction
$\frac{5.7\times10^8}{2.56\times10^6}$ is the same computation with $2n$
evaluated. A certified gap of 14.9 on a loss bounded by 1 is vacuous by a factor
of about 15; the observed gap is a few percent.

The right reading, itemized: the bound is *sufficient, not necessary* -- its
failure certifies nothing about failure to generalize; the culprit is uniformity,
which pays for all $2^{8\times10^8}$ weight settings while SGD only ever visits a
vanishing sliver of them; and closing the factor -- explaining why heavily
overparameterized nets generalize -- is open research, with entry points in the
implicit bias of SGD and in margin, PAC-Bayes and compression bounds; see
[4, Ch. 26 notes] and the literature. The theory in this lecture is not wrong at
scale -- it is loose at scale, and honestly so.

### 8.3 What survives at deep-learning scale

Three direct survivors, each an instance of today's theorems with a small
effective $|\mathcal{H}|$.

(i) *The test-set bound.* A held-out test set is fresh data, and the single
trained model is one fixed hypothesis with respect to it: $|\mathcal{H}| = 1$,
Hoeffding applies exactly, and the Section 5.3 computation says $4{,}612$ test
samples certify plus-or-minus 2 percent at 95 percent confidence
*unconditionally, whatever the model is*.

(ii) *Validation and early stopping.* Comparing $m$ candidate checkpoints on a
validation set is a union bound over $m$ fixed hypotheses; $m$ is small, tens,
so the $+\ln m$ price is trivial.

(iii) *Leaderboard overfitting, explained.* A public leaderboard evaluated on one
fixed test set is the model farm of Section 6.3 -- thousands of submissions
selecting on the same sample's fluctuations -- and the theory predicts exactly
the observed effect: the top of the leaderboard is biased upward, increasingly so
as submissions grow and the test set stays fixed. Concentration versus selection
pressure is the whole story, on both sides of the ledger.

**The chain, end to end.** Bounded implies sub-Gaussian (Theorem 1, Section 3),
which implies an exponential tail for one average (Theorems 2 and 3,
Sections 4 and 5), which becomes simultaneous over $\mathcal{H}$ (Theorem 4,
Section 6), which gives the uniform $\epsilon$-tube (Theorem 5, Section 7.3),
which gives $R(\hat h) \leq R(h^\star) + 2\epsilon$ (the corollary,
Section 7.4). One engine, Chernoff; one lemma, the bounded-MGF envelope; one
accounting rule, the union bound. What the lecture leaves open -- how to *choose*
$\hat h$, rather than certify whatever was chosen -- is Lecture 7's subject:
likelihood, maximum likelihood and maximum a posteriori estimation, and the
bias-variance decomposition.

## 9. References

1. W. Hoeffding, "Probability Inequalities for Sums of Bounded Random
   Variables," *Journal of the American Statistical Association*, vol. 58,
   no. 301, pp. 13-30, 1963. DOI 10.1080/01621459.1963.10500830
   (https://doi.org/10.1080/01621459.1963.10500830). The original: Theorem 1 here
   is his Lemma; Theorem 3 with per-variable ranges $[a_i, b_i]$ is his
   Theorem 2.
2. S. Boucheron, G. Lugosi and P. Massart, *Concentration Inequalities: A
   Nonasymptotic Theory of Independence*, Oxford University Press, 2013. DOI
   10.1093/acprof:oso/9780199535255.001.0001
   (https://doi.org/10.1093/acprof:oso/9780199535255.001.0001). Sections 2.3 to
   2.6 cover sub-Gaussian variables and Hoeffding's lemma and inequality in the
   tilted-log-MGF style of Section 3.
3. R. Vershynin, *High-Dimensional Probability: An Introduction with
   Applications in Data Science*, Cambridge University Press, 2018. DOI
   10.1017/9781108231596 (https://doi.org/10.1017/9781108231596); free copy on
   the author's page. Proposition 2.5.2 is the five equivalent characterizations
   of sub-Gaussian behind Section 4.4; Chapter 2 has Hoeffding.
4. S. Shalev-Shwartz and S. Ben-David, *Understanding Machine Learning: From
   Theory to Algorithms*, Cambridge University Press, 2014. Free PDF at the
   authors' Cambridge-authorized page,
   https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/. Chapters 2 to
   4 have finite classes, uniform convergence and the ERM corollary exactly as in
   Sections 7.3 and 7.4; Chapter 6 has VC dimension.
5. M. Mohri, A. Rostamizadeh and A. Talwalkar, *Foundations of Machine
   Learning*, 2nd ed., MIT Press, 2018. Book page https://cs.nyu.edu/~mohri/mlbook/.
   Chapter 2 has the finite-class PAC bounds; Chapter 3 Rademacher complexity and
   VC dimension; Appendix D concentration inequalities.
