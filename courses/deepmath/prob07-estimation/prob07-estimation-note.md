# Deep Learning Math 7: Estimation - MLE, MAP and Fundamental Limits

**About this file.** This is the accessible Markdown edition of the companion
note for Lecture 7. It carries the full content of the lecture: every formal
statement with the conditions the lecture abbreviates, every proof with its
skipped steps restored, and every worked number re-derived. It is written to be
read straight through by a screen reader: plain text, all mathematics in LaTeX,
no figures, no references to anything visual. Nothing else is needed to read it.

**Convention.** Statements are written for discrete variables (probability mass
functions, sums); the continuous reading (densities, integrals) holds verbatim
with sums replaced by integrals. The one genuinely delicate continuous point,
conditioning on the probability-zero event $\{Y = y\}$, is flagged where it
arises rather than papered over. As in Lectures 1 to 3, $\log$ is base $2$ and
entropies are in bits; natural logarithms are written $\ln$.

**Notation.**

- $X$: the observed sample (an input: an image, a height, a sentence).
- $Y$: the hidden label. $\mathcal{Y}$: the label set, $|\mathcal{Y}|$ its size.
- $p_{X|Y}(x \mid y)$, $f_{X|Y}(x \mid y)$: the model, the conditional pmf or
  density of the observation given the label. Assumed known in Sections 3 to 6.
- $p_Y$: the prior on labels. $p_{Y|X}$: the posterior.
- $\hat{y}(x)$, $\hat{Y}(X)$: an estimator, a function of the observation only.
- $L_x(y)$: the likelihood function, the model read as a function of the
  candidate $y$ with the data $x$ held fixed.
- $\theta$: an unknown parameter; $\ell(\theta)$ the log-likelihood;
  $\hat{\theta}_n$ an estimator of it from $n$ samples.
- $h_2(p) = p \log \frac{1}{p} + (1-p) \log \frac{1}{1-p}$: the binary entropy
  function, in bits. $P_e = \Pr(Y \neq \hat{Y})$: the error probability.
- $\mathbf{1}\{A\}$: the indicator of the event $A$, equal to $1$ when $A$
  happens and $0$ otherwise.
- $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$: the sample mean.

**Background used.** From Lecture 1: linearity of expectation, the law of the
unconscious statistician (LOTUS), and the entropy ceiling
$H(Y) \le \log|\mathcal{Y}|$ with equality if and only if $Y$ is uniform. From
Lecture 2: the mismatch theorem $H(P, Q) = H(P) + D(P \| Q)$. From Lecture 3:
conditional entropy, the chain rule, and the data-processing inequality. From
Lecture 5: the variance of an average, $\mathrm{Var}(\bar{X}_n) = \sigma^2/n$,
and the law of large numbers. From Lecture 6: Hoeffding's inequality and the
fact that the mean minimizes a quadratic. Each import is cited by section
number where it is used and is not re-proved here.

**Contents.**

1. Why estimation?
2. Conditional expectation
3. The estimation problem
4. Maximum likelihood
5. Maximum a posteriori
6. Fano's inequality
7. Parameter estimation
8. Naive Bayes
9. Bias and variance
10. MMSE estimation
11. References

---

## 1 Why Estimation?

### 1.1 Deep learning through the estimation lens

Three connections, each proved later in this note.

*Training.* A network with weights $\theta$ defines a model distribution
$q_\theta$. Training on cross-entropy loss selects the $\theta$ that maximizes
the likelihood of the data. That this is literally maximum likelihood
estimation is theorem-level content, proved in Section 7.5.

*Regularization.* Weight decay adds $\lambda \|\theta\|^2$ to the loss.
Section 5.5 shows this is exactly maximum a posteriori estimation with a
Gaussian prior on the weights.

*Fundamental limits.* No matter the architecture or the optimizer, the error
probability of *any* classifier is floored by Fano's inequality (Section 6) -
a statement about the joint distribution of input and label, not about the
model class.

### 1.2 The question Lecture 6 left open

Lecture 6's finite-class theorem certified the empirical-risk-minimization
pick: $R(\hat{h}) \le R(h^*) + 2\epsilon$ with high probability when
$n \gg \ln|\mathcal{H}|$ (Lecture 6 note, Sections 7.3 to 7.4). That is a
statement about *whatever* hypothesis empirical risk minimization returns. It
never says how a hypothesis should be scored in the first place, nor why low
empirical loss is the right thing to minimize. This lecture supplies the
principle (likelihood), the correction for base rates (the prior), the
fundamental limit (Fano), and the exact error accounting for the squared-error
view (bias and variance, MMSE).

### 1.3 Two faces of one problem

Two estimation problems alternate through the lecture, sharing one recipe.

- *Inference.* The model $p_{X|Y}$ is known, a label $y$ is hidden, an input
  $x$ is observed; estimate $y$. Sections 3 to 6 and 8.
- *Learning.* The model family $p_{X|\theta}$ is known up to a parameter,
  independent and identically distributed samples $x_1, \dots, x_n$ are
  observed; estimate $\theta$. Sections 7 and 9.

In both cases an *estimator* is a function of the observation only, a rule
fixed before the data arrive. The recipe is: maximize a likelihood, optionally
weighted by a prior.

---

## 2 Conditional Expectation

### 2.1 Definition, with its conditions

**Definition (conditional expectation given $Y = y$).** For jointly
distributed $X, Y$ and any $y$ with $p_Y(y) > 0$,

$$ \mathbb{E}[X \mid Y = y] \;=\; \sum_{x} x \, p_{X|Y}(x \mid y), \qquad
   p_{X|Y}(x \mid y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}, $$

provided the sum converges absolutely. Continuous case:
$\mathbb{E}[X \mid Y = y] = \int x \, f_{X|Y}(x \mid y) \, dx$ with
$f_{X|Y}(x \mid y) = f_{X,Y}(x,y) / f_Y(y)$ wherever $f_Y(y) > 0$.

Fine print, four items.

1. The conditional pmf $p_{X|Y}(\cdot \mid y)$ is a genuine pmf in $x$ for each
   *fixed* $y$: it is non-negative and sums to $p_Y(y)/p_Y(y) = 1$. So the
   conditional expectation is an *ordinary* expectation under a different
   distribution, and every rule from Lecture 1 (linearity, LOTUS, monotonicity)
   applies to it verbatim.
2. It is defined only for $y$ in the support of $Y$. Values off the support
   never enter any expectation and may be set arbitrarily.
3. The absolute-convergence proviso is automatic when
   $\mathbb{E}|X| < \infty$, since
   $\sum_x |x| \, p_{X|Y}(x \mid y) \le \mathbb{E}|X| / p_Y(y)$.
4. *Continuous flag.* For continuous $Y$ the event $\{Y = y\}$ has probability
   zero, so "conditioning on it" cannot mean an elementary conditional
   probability. The density formula above is the honest calculus-level
   definition (a limit of conditioning on $\{y \le Y \le y + \delta\}$), and
   the measure-theoretic construction that makes it canonical is beyond this
   course. Everything below is proved in the discrete setting, where no such
   subtlety exists.

### 2.2 Worked: the running joint distribution, all four conditionals

The joint distribution returns from Lecture 3. Written out cell by cell, with
the margins recomputed here:

- $p_{X,Y}(0,0) = 1/4$ and $p_{X,Y}(0,1) = 1/4$, so the row margin is
  $p_X(0) = 1/2$.
- $p_{X,Y}(1,0) = 1/2$ and $p_{X,Y}(1,1) = 0$, so the row margin is
  $p_X(1) = 1/2$.
- Column margins: $p_Y(0) = 1/4 + 1/2 = 3/4$ and
  $p_Y(1) = 1/4 + 0 = 1/4$. Total mass $1$.

Conditioning on $Y = 0$ (mass $3/4$):

$$ p_{X|Y}(1 \mid 0) = \frac{1/2}{3/4} = \frac{2}{3}, \qquad
   p_{X|Y}(0 \mid 0) = \frac{1/4}{3/4} = \frac{1}{3}, $$

which sums to $1$ as it must. Conditioning on $Y = 1$ (mass $1/4$):

$$ p_{X|Y}(1 \mid 1) = \frac{0}{1/4} = 0, \qquad
   p_{X|Y}(0 \mid 1) = \frac{1/4}{1/4} = 1. $$

Hence the two conditional means

$$ \mathbb{E}[X \mid Y = 0] = 0 \cdot \tfrac{1}{3} + 1 \cdot \tfrac{2}{3}
   = \tfrac{2}{3}, \qquad
   \mathbb{E}[X \mid Y = 1] = 0 \cdot 1 + 1 \cdot 0 = 0, $$

against the unconditional $\mathbb{E}[X] = p_X(1) = \tfrac{1}{2}$. Seeing
$Y = 1$ *forces* $X = 0$, because the cell $(1,1)$ carries zero mass.

### 2.3 $\mathbb{E}[X \mid Y]$ is a random variable

Define $g(y) = \mathbb{E}[X \mid Y = y]$ on the support of $Y$: an ordinary,
non-random function. Then $\mathbb{E}[X \mid Y]$ *means* the composition
$g(Y)$, which is a random variable because $Y$ is. In the example above,
$g(0) = \tfrac{2}{3}$ and $g(1) = 0$, so $\mathbb{E}[X \mid Y]$ takes the value
$\tfrac{2}{3}$ with probability $\tfrac{3}{4}$ and the value $0$ with
probability $\tfrac{1}{4}$. It has a pmf, hence an expectation of its own,
which is exactly the quantity the tower property computes.

Keeping the two readings separate - $g(y)$ is a number per scenario, $g(Y)$ is
a random variable - is what makes the proofs in Sections 5.4 and 10
one-liners rather than mysteries.

### 2.4 Theorem 1: the tower property, full proof

**Theorem 1 (tower property, or law of iterated expectations).** If
$\mathbb{E}|X| < \infty$, then

$$ \mathbb{E}\big[ \mathbb{E}[X \mid Y] \big] = \mathbb{E}[X]. $$

**Proof.** $\mathbb{E}[X \mid Y] = g(Y)$ is a function of $Y$, so LOTUS
(Lecture 1 note, Section 3) evaluates its expectation against $p_Y$:

$$ \mathbb{E}\big[ g(Y) \big] = \sum_y g(y) \, p_Y(y)
   = \sum_y p_Y(y) \sum_x x \, p_{X|Y}(x \mid y). $$

Substitute the definition $p_{X|Y}(x \mid y) = p_{X,Y}(x,y) / p_Y(y)$. The
factor $p_Y(y)$ cancels, legitimately: the outer sum only visits $y$ with
$p_Y(y) > 0$. This leaves

$$ \mathbb{E}\big[ g(Y) \big] = \sum_y \sum_x x \, p_{X,Y}(x,y). $$

Now swap the two sums. This is the step the lecture performs without
justification, and it is where the finite-mean hypothesis is used: a double
series may be reordered when it converges absolutely, and here
$\sum_y \sum_x |x| \, p_{X,Y}(x,y) = \mathbb{E}|X| < \infty$. After the swap,
the inner sum over $y$ marginalizes the joint pmf (Lecture 3 note, Section 2):

$$ \sum_x x \sum_y p_{X,Y}(x,y) = \sum_x x \, p_X(x) = \mathbb{E}[X]. $$

**End of proof.**

*Worked check.* On the running distribution,
$\mathbb{E}[\mathbb{E}[X \mid Y]] = \tfrac{3}{4} \cdot \tfrac{2}{3}
+ \tfrac{1}{4} \cdot 0 = \tfrac{2}{4} = \tfrac{1}{2} = \mathbb{E}[X]$.

The reading to keep: a hard expectation may be computed as *scenario averages,
weighted by scenario probabilities*, without ever assembling the joint
distribution.

### 2.5 The pull-out property

The lecture states $\mathbb{E}[h(Y) X] = \mathbb{E}[h(Y) \, \mathbb{E}[X \mid Y]]$
with no proof. It deserves one, since it alone kills the MMSE cross term in
Section 10.

**Lemma 2.1 (taking out what is known).** For any function $h$ with
$\mathbb{E}|h(Y) X| < \infty$,

$$ \mathbb{E}\big[ h(Y) \, X \big] \;=\;
   \mathbb{E}\big[ h(Y) \, \mathbb{E}[X \mid Y] \big]. $$

**Proof.** Expand the left side over the joint pmf, factor it through the
conditional, and pull $h(y)$ - constant in $x$ - out of the inner sum:

$$ \sum_y \sum_x h(y) \, x \, p_{X,Y}(x,y)
   = \sum_y p_Y(y) \, h(y) \sum_x x \, p_{X|Y}(x \mid y)
   = \sum_y p_Y(y) \, h(y) \, g(y), $$

and the right-hand sum is $\mathbb{E}[h(Y) \, g(Y)]$ by LOTUS on the pair.
Reordering is again licensed by absolute convergence. **End of proof.**

Equivalent slogan: *inside* a conditional expectation given $Y$, anything that
depends only on $Y$ is a constant and slides out,

$$ \mathbb{E}[h(Y) X \mid Y] = h(Y) \, \mathbb{E}[X \mid Y]. $$

Lemma 2.1 is this slogan followed by the tower property.

---

## 3 The Estimation Problem

### 3.1 Setup

$X$ is the observed *sample* (an input: an image, a height, a sentence); $Y$ is
the hidden *label*. The standing assumption of Sections 3 to 6: the conditional
model $p_{X|Y}(x \mid y)$, or the density $f_{X|Y}$, is *known exactly* for
every $y$. Nature draws $Y$, then draws $X$ from the known conditional, and we
see only $X = x$. An estimator is a function $\hat{y}(x)$ of the observation.
How the model itself gets known - estimated from data - is deliberately
postponed to Section 7; Section 8 then runs the full pipeline (fit the model,
then classify) end to end.

**Running example (two nationalities).** Heights from nationality A follow
$\mathcal{N}(170, 10^2)$, from nationality B follow $\mathcal{N}(180, 15^2)$,
in centimetres. Label $Y = 0$ for A, $Y = 1$ for B; the observation $X$ is the
height. Given $X = 176$: which nationality?

### 3.2 Likelihood versus probability

Fix the observation $x$ and read the model backwards. The **likelihood
function** is $L_x(y) = f_{X|Y}(x \mid y)$, a function of the *candidate* $y$
with the data $x$ frozen. Three things it is not.

1. It is not a probability distribution over $y$: summed or integrated over $y$
   it need not give $1$. At $x = 176$ below, the two values sum to
   $0.0333 + 0.0257 = 0.0590$.
2. Its individual values are not probabilities of anything when $X$ is
   continuous - a density value can exceed $1$.
3. Comparing $L_x(y)$ across $y$ is nonetheless meaningful. For continuous
   $X$, $\Pr(x \le X \le x + \delta \mid Y = y) \approx f_{X|Y}(x \mid y) \delta$
   for small $\delta$, so ratios of densities are ratios of probabilities of
   the same small window. That is precisely why an argmax over $y$ makes sense.

"Probability" answers *forward* questions (data unknown, parameter fixed);
"likelihood" ranks *backward* candidates (data fixed, parameter unknown).

### 3.3 Two questions, two estimators

"On which $y$ is the observed $x$ most likely?" ranks $f_{X|Y}(x \mid y)$ over
$y$ - the maximum likelihood estimator, needing only the model. "Given $x$,
which $y$ is most probable?" ranks the posterior $p_{Y|X}(y \mid x)$ - the
maximum a posteriori estimator, needing additionally a prior $p_Y$. The two
answers coincide under a uniform prior (Section 5.2) and genuinely differ
otherwise (Section 5.3, at $x = 185$).

---

## 4 Maximum Likelihood

### 4.1 Definition

**Definition (maximum likelihood estimator, MLE).**

$$ \hat{y}_{\mathrm{MLE}}(x) = \operatorname*{argmax}_y f_{X|Y}(x \mid y), $$

with the pmf $p_{X|Y}$ in place of the density for discrete $X$. If several $y$
tie, any fixed tie-breaking rule may be used; if the supremum is not attained,
the MLE does not exist. Examples of both pathologies are in Section 4.5.

### 4.2 Worked: the heights, all four density values from scratch

The decision rule is "pick A if and only if
$f_{X|Y}(x \mid 0) > f_{X|Y}(x \mid 1)$", with the Gaussian densities. The
normalizing constants are $\frac{1}{10\sqrt{2\pi}} = 0.0398942$ and
$\frac{1}{15\sqrt{2\pi}} = 0.0265962$.

**At $x = 176$.** The exponents are $-(176-170)^2/200 = -36/200 = -0.18$ and
$-(176-180)^2/450 = -16/450 = -0.035556$, so

$$ f(176 \mid 0) = 0.0398942 \times e^{-0.18}
   = 0.0398942 \times 0.835270 = 0.033322, $$

$$ f(176 \mid 1) = 0.0265962 \times e^{-0.035556}
   = 0.0265962 \times 0.965069 = 0.025667. $$

Since $0.0333 > 0.0257$, the MLE is $\hat{y} = 0$, nationality A. Note that
B's mean is *closer* to the observation ($|176 - 180| = 4$ against
$|176 - 170| = 6$), yet A wins: A's smaller spread concentrates more density
near its mean, so the taller, narrower curve is still on top at $176$.

**At $x = 185$.** The exponents are $-225/200 = -1.125$ and
$-25/450 = -0.055556$, so

$$ f(185 \mid 0) = 0.0398942 \times 0.324652 = 0.012952, $$

$$ f(185 \mid 1) = 0.0265962 \times 0.945959 = 0.025159. $$

Since $0.0130 < 0.0252$, the MLE is $\hat{y} = 1$, nationality B.

### 4.3 The decision boundary, solved exactly

The lecture reports boundaries at approximately $179$ and $145$ without
derivation. Equate the two densities and take natural logarithms:

$$ -\ln 10 - \frac{(x-170)^2}{200}
   \;=\; -\ln 15 - \frac{(x-180)^2}{450}. $$

Rearrange and multiply by $1800$:

$$ 4(x-180)^2 - 9(x-170)^2 = -1800 \ln \tfrac{15}{10} = -729.837. $$

Expanding,

$$ -5x^2 + 1620x - 130500 = -729.837
   \quad\Longleftrightarrow\quad x^2 - 324x + 25954.03 = 0, $$

with discriminant $324^2 - 4 \times 25954.03 = 1159.87$ and
$\sqrt{1159.87} = 34.06$, so

$$ x = \frac{324 \pm 34.06}{2} = 179.03 \quad\text{or}\quad 145.03. $$

Both reported boundaries check out.

Why *two* crossings: unequal variances make the log-density difference a
genuine quadratic in $x$, opening downward for the wider curve. B's
$\sigma = 15$ beats A not only above $179$ but also below $145$ - extreme
heights in either direction are better explained by the wide distribution.
Equal variances would cancel the $x^2$ terms and leave a single linear
boundary.

### 4.4 What MLE ignores

The likelihood question never asks how *common* each label is. If $99\%$ of the
population is from A, then even at $185$ centimetres most such people are tall
A-nationals, simply because there are so many more of them. Base-rate
information is a distribution on $Y$ - a prior - and folding it in is
Section 5. The classic failure mode of ignoring it is rare-disease testing,
where a positive result on an accurate test is still usually a false positive.

### 4.5 Omitted edge cases: non-uniqueness and non-existence

The argmax notation hides two possible pathologies, both standard
[2, Ch. 7] and both absent from today's well-behaved examples.

**Non-uniqueness.** Let $X_1, \dots, X_n$ be independent and uniform on
$[\theta, \theta + 1]$. The likelihood of $\theta$ is $1$ if
$\max_i x_i - 1 \le \theta \le \min_i x_i$ and $0$ otherwise: an entire
*interval* of maximizers. Any point of it is "the" MLE, so the definition needs
a tie-break. Ties also occur in classification whenever two class-conditional
densities cross exactly at the observed $x$, for instance at $x = 179.03$
above.

**Non-existence.** Three cases worth knowing.

1. $X_1, \dots, X_n$ independent and uniform on the *open* interval
   $(0, \theta)$: the likelihood
   $\theta^{-n} \mathbf{1}\{\theta > \max_i x_i\}$ increases as
   $\theta$ decreases toward $\max_i x_i$, but is $0$ at the limit - the
   supremum is not attained.
2. A two-component Gaussian mixture with both means and variances free: setting
   one component's mean at $x_1$ and letting its variance go to $0$ drives the
   likelihood to $+\infty$, so no maximizer exists over the full parameter
   space. Deep-learning moral: an unpenalized likelihood over a too-flexible
   family can be degenerate, and priors or regularization (Section 5.5) are
   one cure.
3. Boundary maxima are not pathological but need care. Bernoulli with all heads
   puts the MLE at $\hat{p} = 1$, an endpoint where no interior
   zero-derivative condition holds. See Section 7.2.

---

## 5 Maximum a Posteriori

### 5.1 Definition and Bayes' rule

**Definition (maximum a posteriori estimator, MAP).**

$$ \hat{y}_{\mathrm{MAP}}(x) = \operatorname*{argmax}_y p_{Y|X}(y \mid x). $$

This requires the prior $p_Y(y)$ for all $y$ in addition to the model; for
continuous $Y$, replace pmfs by densities.

The posterior is not given directly - the model runs in the direction
$Y \to X$. Flip it with two applications of the conditional-pmf definition.
This *is* Bayes' rule; nothing new is assumed:

$$ p_{Y|X}(y \mid x) = \frac{p_{X,Y}(x,y)}{p_X(x)}
   = \frac{p_{X|Y}(x \mid y) \, p_Y(y)}{p_X(x)}, \qquad
   p_X(x) = \sum_{y'} p_{X|Y}(x \mid y') \, p_Y(y'). $$

### 5.2 The evidence drops out

The denominator $p_X(x)$, called the *evidence*, is the same positive number
for every candidate $y$, and an argmax is invariant under multiplication by a
positive constant. Hence

$$ \hat{y}_{\mathrm{MAP}}(x)
   = \operatorname*{argmax}_y \; p_{X|Y}(x \mid y) \, p_Y(y)
   = \operatorname*{argmax}_y \; \big[ \text{likelihood} \times \text{prior} \big]. $$

Immediate corollary: if $p_Y$ is uniform over a finite label set, the prior
factor is constant and **MAP equals MLE**. So MLE is the special case "no
preference among labels", and every difference between the two estimators is
driven entirely by the prior.

### 5.3 Worked: the heights with a nine-to-one prior

Take $p_Y(0) = \tfrac{9}{10}$ and $p_Y(1) = \tfrac{1}{10}$, and use
Section 4.2's density values.

**At $x = 176$.** The scores are $0.033322 \times 0.9 = 0.029990 \approx 0.0300$
for A against $0.025667 \times 0.1 = 0.002567 \approx 0.0026$ for B: the same
verdict as MLE, with a wider margin. As a posterior,

$$ \Pr(Y = 0 \mid X = 176) = \frac{0.029990}{0.029990 + 0.002567} = 0.921. $$

**At $x = 185$.** The scores are $0.012952 \times 0.9 = 0.011657 \approx 0.0117$
for A against $0.025159 \times 0.1 = 0.002516 \approx 0.0025$ for B. Here the
two estimators disagree: MLE says B, because $0.0130 < 0.0252$; MAP says A. The
likelihood favors B by a factor of about $1.94$, a two-to-one likelihood edge,
but the prior favors A by nine to one, so the product favors A by about
$4.6$ to $1$:

$$ \Pr(Y = 0 \mid X = 185) = \frac{0.011657}{0.011657 + 0.002516} = 0.822. $$

Tall people from A still outnumber people from B.

**The shifted boundary, solved exactly.** The lecture reports a MAP boundary
near $195$. The boundary condition multiplies Section 4.3's equation by the
prior ratio, which adds $\ln 9 = 2.19722$ to the log balance:

$$ \frac{(x-180)^2}{450} - \frac{(x-170)^2}{200}
   = -\ln \tfrac{15}{10} - \ln 9 = -2.60269, $$

which after the same algebra becomes $x^2 - 324x + 25163.03 = 0$, with
discriminant $4323.87$, square root $65.76$, and roots

$$ x = 194.88 \quad\text{and}\quad x = 129.12. $$

Both check out, including the summary: the pick-B threshold moves
$194.88 - 179.03 = 15.85 \approx 16$ centimetres to the right.

### 5.4 Theorem 2: MAP is Bayes optimal, full proof

**Theorem 2 (Bayes optimality of MAP).** Among all estimators $\hat{Y}(X)$,
that is all functions of $X$ into the label set, the MAP rule minimizes the
error probability $\Pr(\hat{Y}(X) \neq Y)$.

**Proof.** Minimizing the error probability is the same as maximizing the
success probability
$\Pr(\hat{Y}(X) = Y) = 1 - \Pr(\hat{Y}(X) \neq Y)$. Fix any rule
$\hat{Y}(\cdot)$. Write the success probability as the expectation of an
indicator and condition on $X$ via the tower property (Theorem 1, applied to
the bounded variable $\mathbf{1}\{Y = \hat{Y}(X)\}$, whose mean is trivially
finite):

$$ \Pr\big( \hat{Y}(X) = Y \big)
   = \mathbb{E}\big[ \mathbf{1}\{Y = \hat{Y}(X)\} \big]
   = \mathbb{E}\Big[ \mathbb{E}\big[ \mathbf{1}\{Y = \hat{Y}(X)\}
     \,\big|\, X \big] \Big]. $$

Given $X = x$, the guess $\hat{Y}(x)$ is a fixed label, so the inner
conditional expectation is the posterior mass at that label:
$\mathbb{E}[\mathbf{1}\{Y = \hat{Y}(x)\} \mid X = x]
= p_{Y|X}(\hat{Y}(x) \mid x)$. LOTUS over $X$ then gives

$$ \Pr\big( \hat{Y}(X) = Y \big)
   = \sum_x p_X(x) \; p_{Y|X}\big( \hat{Y}(x) \,\big|\, x \big). $$

Here is the pointwise-optimization step, made precise: the sum is over disjoint
choices - the value $\hat{Y}(x)$ chosen at one $x$ appears in exactly one term
and constrains no other term. Bounding each term separately,

$$ \sum_x p_X(x) \, p_{Y|X}(\hat{Y}(x) \mid x)
   \;\le\; \sum_x p_X(x) \, \max_y \, p_{Y|X}(y \mid x), $$

with equality if and only if
$\hat{Y}(x) \in \operatorname*{argmax}_y p_{Y|X}(y \mid x)$ for every $x$ with
$p_X(x) > 0$, which is exactly the MAP rule (any tie-break attains the same
optimum). Since the upper bound is a fixed number independent of the rule, and
MAP attains it, MAP maximizes the success probability, hence minimizes the
error probability. **End of proof.**

Three remarks the lecture has no room for.

1. *Continuous inputs.* Replace $\sum_x p_X(x)$ by $\int f_X(x) \, dx$; the
   argument is untouched.
2. *Randomized rules do not help.* A randomized estimator is a probability
   mixture over deterministic rules, and its success probability is the
   corresponding mixture of theirs, hence at most the maximum. MAP remains
   optimal in the wider class.
3. *Optimality is loss-specific.* "Bayes optimal" here means optimal for the
   zero-one loss. Under squared error the optimum is a different functional of
   the same posterior, the conditional mean (Theorem 5, Section 10). The
   posterior is the sufficient object; the loss picks which summary of it to
   report.

*Source note.* The LaTeX source `probability25.tex` (line 1661) states the MAP rule as
$\operatorname*{argmax}_y p_{X|Y}(x \mid y)$, dropping the prior factor. The
correct statement is the posterior argmax, which is what is proved above.

### 5.5 MAP becomes regularization: Gaussian prior is ridge, Laplace prior is lasso

For a continuous parameter $\theta$ with prior density $f_\Theta$, take
logarithms of likelihood times prior (logarithms preserve the argmax;
Section 7.1):

$$ \hat{\theta}_{\mathrm{MAP}}
   = \operatorname*{argmax}_\theta
     \big[ \log f(x \mid \theta) + \log f_\Theta(\theta) \big]
   = \operatorname*{argmin}_\theta
     \big[ -\log f(x \mid \theta) - \log f_\Theta(\theta) \big], $$

where the first term is the training loss and the second is the penalty.

**Gaussian prior.** $f_\Theta(\theta) \propto e^{-\|\theta\|^2 / 2\tau^2}$
gives the penalty $\frac{1}{2\tau^2}\|\theta\|^2$ plus a constant: **$L_2$
regularization**, called *weight decay* in deep learning and *ridge regression*
in statistics. The strength is $\lambda = \frac{1}{2\tau^2}$, so a tighter
prior (small $\tau$) is a stronger pull toward $0$.

**Laplace prior**, the natural companion, omitted by the lecture:
$f_\Theta(\theta) \propto e^{-\|\theta\|_1 / b}$ gives the penalty
$\frac{1}{b}\|\theta\|_1$: **$L_1$ regularization**, the *lasso*. The Laplace
density's kink at $0$ is why $L_1$-regularized solutions have exact zeros
(sparse weights), while the smooth Gaussian prior only shrinks them.

*Caveat: improper priors.* "Uniform prior implies MAP equals MLE" is exact on a
finite label set or a bounded parameter set. On an unbounded parameter space
(all of $\mathbb{R}^d$), a uniform "prior" has infinite total mass - it is
*improper*, not a probability density. The recipe "maximize likelihood times
one" still produces the MLE, and posteriors can remain well defined if the
likelihood decays fast enough, but statements like Theorem 2 no longer have a
probabilistic interpretation until a proper prior is put back. MLE as flat MAP
is a useful mnemonic, not a theorem, in the unbounded case.

---

## 6 Fano's Inequality

### 6.1 The question, and the imported toolkit

Theorem 2 crowned MAP the best possible rule for error probability. Fano's
inequality answers the next question - how good can the best possibly be? -
with a floor that binds *every* estimator $\hat{Y}(X)$, MAP included, in terms
of the joint distribution of $(X, Y)$ alone. Throughout, the error probability
is $P_e = \Pr(Y \neq \hat{Y}(X))$.

Four facts are imported. The first three are stated and proved in the earlier
companion notes and only re-stated here; the fourth is derived below, because
the form the lecture uses is one step away from the cited one.

- **Conditional entropy** (Lecture 3 note, Section 3):
  $H(Y \mid X) = \sum_x p_X(x) H(Y \mid X = x)$, the average leftover
  uncertainty, with $0 \le H(Y \mid X) \le H(Y)$.
- **Uniform ceiling** (Lecture 1 note, Section 5): a variable supported on at
  most $m$ values has entropy at most $\log m$, with equality if and only if it
  is uniform. In particular a binary variable has
  $H(E) = h_2(p) \le \log 2 = 1$ bit.
- **Conditioning never hurts** (Lecture 3 note, Section 4, from
  $I \ge 0$): $H(A \mid C) \le H(A)$, and more generally
  $H(A \mid B, C) \le H(A \mid C)$.
- **Data-processing inequality** (Lecture 3 note, Section 5): if
  $\hat{Y} = g(X)$ then $Y - X - \hat{Y}$ is a Markov chain and
  $I(Y; \hat{Y}) \le I(Y; X)$.

**Data-processing inequality, entropy form (derived).** Write both mutual
informations as entropy drops, $I(Y; \hat{Y}) = H(Y) - H(Y \mid \hat{Y})$ and
$I(Y; X) = H(Y) - H(Y \mid X)$. The inequality
$I(Y; \hat{Y}) \le I(Y; X)$ becomes, after cancelling $H(Y)$ and flipping the
sign,

$$ H\big( Y \mid \hat{Y}(X) \big) \;\ge\; H(Y \mid X). $$

Processing the input can only lose information about the label: the guess never
knows more than the input it was computed from.

Two small lemmas the proof leans on, used by the lecture without proof.

**Lemma 6.1 (conditional chain rule).**
$H(A, B \mid C) = H(A \mid C) + H(B \mid A, C)$, in either order of $A$ and
$B$. *Proof.* Factor the conditional pmf,
$p(a, b \mid c) = p(a \mid c) \, p(b \mid a, c)$, take $\log \frac{1}{\cdot}$
of both sides, and average over the joint distribution of $(A, B, C)$: the left
side averages to $H(A, B \mid C)$, and the two right-side terms to
$H(A \mid C)$ and $H(B \mid A, C)$. The other order swaps the roles of $a$ and
$b$. **End of proof of Lemma 6.1.**

**Lemma 6.2 (functions carry no conditional entropy).** If $Z = g(W)$ then
$H(Z \mid W) = 0$; more generally $H(Z \mid W, V) = 0$. *Proof.* Given
$W = w$, the conditional pmf of $Z$ puts mass $1$ on the single point $g(w)$,
and the entropy of a point mass is $1 \cdot \log 1 = 0$; average over $w$, and
over $v$ in the general case. **End of proof of Lemma 6.2.**

### 6.2 The theorem: sharp form and the lecture's form

**Theorem 3 (Fano's inequality [1, Thm. 2.10.1]).** Let $Y \in \mathcal{Y}$
with $2 \le |\mathcal{Y}| < \infty$, let $\hat{Y} = \hat{Y}(X) \in \mathcal{Y}$
be any estimator, and let $P_e = \Pr(Y \neq \hat{Y})$. Then, in the sharp form,

$$ h_2(P_e) + P_e \log\big( |\mathcal{Y}| - 1 \big) \;\ge\; H(Y \mid X), $$

and consequently, weakening $h_2(P_e) \le 1$ and
$\log(|\mathcal{Y}| - 1) \le \log|\mathcal{Y}|$, in the lecture's form,

$$ P_e \;\ge\; \frac{H(Y \mid X) - 1}{\log |\mathcal{Y}|}. $$

The lecture proves the weak form directly; this note proves the sharp form -
the same nine steps, keeping two quantities the lecture rounds up - and then
coarsens. This costs nothing and pays off twice: the sharp form is the citable
standard, and it is the only version that says anything for binary labels
(Section 6.5).

### 6.3 The proof, every step justified

**Step 1 (error flag).** Define $E = \mathbf{1}\{\hat{Y} \neq Y\}$: binary,
with $p_E(1) = P_e$ and $p_E(0) = 1 - P_e$, and $E$ is a deterministic function
of the pair $(Y, \hat{Y})$. The quantity to be computed twice is
$H(E, Y \mid \hat{Y})$.

**Step 2 (first expansion, $Y$ before $E$).** Lemma 6.1 with $A = Y$,
$B = E$, $C = \hat{Y}$:

$$ H(E, Y \mid \hat{Y}) = H(Y \mid \hat{Y}) + H(E \mid Y, \hat{Y})
   = H(Y \mid \hat{Y}), $$

the second term vanishing by Lemma 6.2, since $E$ is a function of
$(Y, \hat{Y})$. The flag is *free*: attaching it costs no entropy in this
order.

**Step 3 (data processing).** By the entropy form of the data-processing
inequality (Section 6.1), since $\hat{Y}$ is a function of $X$,

$$ H(E, Y \mid \hat{Y}) = H(Y \mid \hat{Y}) \;\ge\; H(Y \mid X). $$

This is the only step where "any estimator" enters: nothing about $\hat{Y}$ is
used except that it is computed from $X$. The lower bound is done.

**Step 4 (second expansion, $E$ before $Y$).** Lemma 6.1 in the other order:

$$ H(E, Y \mid \hat{Y}) = H(E \mid \hat{Y}) + H(Y \mid E, \hat{Y}). $$

**Step 5 (flag term).** Conditioning never hurts, then the binary ceiling:

$$ H(E \mid \hat{Y}) \;\le\; H(E) = h_2(P_e) \;\le\; 1 \text{ bit}. $$

The sharp form keeps $h_2(P_e)$; the lecture rounds to $1$ here, and that is
where its $-1$ comes from.

**Step 6 (label term, split by the flag).** By definition of conditional
entropy, conditioning on the pair $(E, \hat{Y})$ averages over the values of
$E$ first:

$$ H(Y \mid E, \hat{Y}) = (1 - P_e) \, H(Y \mid E = 0, \hat{Y})
   + P_e \, H(Y \mid E = 1, \hat{Y}), $$

where
$H(Y \mid E = e, \hat{Y})
= \sum_{\hat{y}} p_{\hat{Y}|E}(\hat{y} \mid e) \, H(Y \mid E = e, \hat{Y} = \hat{y})$
is itself an average over the guess within each scenario.

**Step 7 (both scenarios bounded).** *Correct scenario:* given $E = 0$ and
$\hat{Y} = \hat{y}$, the label is determined, $Y = \hat{y}$, so every
$H(Y \mid E = 0, \hat{Y} = \hat{y})$ is $0$ and the average is $0$. *Error
scenario:* given $E = 1$ and $\hat{Y} = \hat{y}$, the label satisfies
$Y \neq \hat{y}$, so $Y$ is supported on at most the $|\mathcal{Y}| - 1$
remaining labels; by the uniform ceiling,
$H(Y \mid E = 1, \hat{Y} = \hat{y}) \le \log(|\mathcal{Y}| - 1)$ for every
$\hat{y}$, hence also after averaging. The lecture rounds this to
$\log|\mathcal{Y}|$ - the second coarsening.

**Step 8 (assemble the upper bound).** Steps 4 to 7 give

$$ H(E, Y \mid \hat{Y}) \;\le\; h_2(P_e) + (1 - P_e) \cdot 0
   + P_e \log(|\mathcal{Y}| - 1). $$

**Step 9 (close the sandwich).** Chain Steps 3 and 8 through the common middle
quantity:

$$ H(Y \mid X) \;\le\; H(E, Y \mid \hat{Y})
   \;\le\; h_2(P_e) + P_e \log(|\mathcal{Y}| - 1), $$

which is the sharp form. Weakening via $h_2(P_e) \le 1$ and
$\log(|\mathcal{Y}| - 1) \le \log|\mathcal{Y}|$ gives
$H(Y \mid X) \le 1 + P_e \log|\mathcal{Y}|$, and solving for $P_e$ (dividing by
$\log|\mathcal{Y}| > 0$) gives the lecture's bound. **End of proof.**

The proof in one sentence: one quantity, $H(E, Y \mid \hat{Y})$, is expanded by
the chain rule in two orders - the $Y$-first order plus data processing makes it
at least the leftover uncertainty $H(Y \mid X)$, and the $E$-first order makes
it at most "one flag plus, on errors, one label among the wrong ones" - and the
two readings sandwich $P_e$.

### 6.4 Worked: the eight-class example, both forms

Take $|\mathcal{Y}| = 8$, so $\log 8 = 3$ bits, and suppose noisy labels leave
$H(Y \mid X) = 2.5$ bits. The lecture's form gives

$$ P_e \;\ge\; \frac{2.5 - 1}{3} = \frac{1.5}{3} = 0.5. $$

The sharp form asks for $h_2(P_e) + P_e \log 7 \ge 2.5$ with
$\log 7 = 2.807$. The left side is increasing in $P_e$ on the relevant range,
and numerically it equals $2.5$ at $P_e \approx 0.536$: at $P_e = 0.53$ it is
$0.997 + 1.488 = 2.485 < 2.5$, and at $P_e = 0.55$ it is
$0.993 + 1.544 = 2.537 > 2.5$. So the honest floor is about $53.6\%$ error, and
the lecture's $50\%$ is a slightly generous round-down, as a weakened bound
must be. No architecture, dataset size, or training trick evades either number:
the floor depends only on the joint distribution of $(X, Y)$.

### 6.5 Edge cases: when the lecture's form is vacuous, and binary labels

**Vacuous regime.** If $H(Y \mid X) \le 1$ bit, the lecture's numerator is at
most $0$ and the bound says $P_e \ge (\text{something} \le 0)$: true and
useless. Fano is a *lower-bound* tool for genuinely uncertain problems; it
never certifies that a problem is easy.

**Binary labels, $|\mathcal{Y}| = 2$.** The lecture's form has
$\log|\mathcal{Y}| = 1$ and never bites, since its floor is
$H(Y \mid X) - 1 \le H(Y) - 1 \le 0$. The sharp form, by contrast, has
$\log(|\mathcal{Y}| - 1) = \log 1 = 0$, leaving

$$ h_2(P_e) \;\ge\; H(Y \mid X)
   \qquad\Longrightarrow\qquad P_e \;\ge\; h_2^{-1}\big( H(Y \mid X) \big), $$

where $h_2^{-1}$ is the inverse of $h_2$ on $[0, \tfrac{1}{2}]$. This is a real
constraint: for example $H(Y \mid X) = 0.5$ bits forces $P_e \ge 0.110$, and
the check is
$h_2(0.110) = 0.110 \times 3.184 + 0.890 \times 0.168 = 0.500$. This is exactly
the sharper variant the lecture alludes to with "replace the $1$ by $H(E)$":
keep $h_2(P_e)$ unrounded in Step 5 and keep $|\mathcal{Y}| - 1$ in Step 7, and
the same nine steps deliver it.

### 6.6 What Fano buys

*Label-noise ceiling.* Mislabeled training data is randomness in $Y$ that no
feature can remove; it inflates $H(Y \mid X)$ and caps achievable accuracy
before any model is chosen.

*Feature audit.* Since $H(Y \mid X) = H(Y) - I(X; Y)$, features carrying little
mutual information about the label leave $H(Y \mid X)$ large - the task is
certifiably hopeless with those features, a diagnosis available before
training.

*Theory workhorse.* Minimax lower bounds in statistics and learning theory
routinely run Fano over a carefully built finite family of hard distributions
[1, Ch. 2; 6, Ch. 15].

Direction matters: Fano converts uncertainty into an error *floor*; it says
nothing about achievability, and that side belongs to the estimators of
Sections 4 and 5.

---

## 7 Parameter Estimation

### 7.1 Setup, and why the logarithm is legitimate

Let $X_1, \dots, X_n$ be independent and identically distributed from a
distribution $p_{X|\theta}$ known up to the parameter $\theta$, with observed
values $x_1, \dots, x_n$. No distribution is assumed on $\theta$, so MAP is
unavailable and MLE is the tool. By independence the sample likelihood
factorizes, and the MLE is

$$ \hat{\theta}_{\mathrm{MLE}}
   = \operatorname*{argmax}_\theta \prod_{i=1}^n p_{X|\theta}(x_i \mid \theta)
   = \operatorname*{argmax}_\theta \sum_{i=1}^n
     \log p_{X|\theta}(x_i \mid \theta), $$

where the sum is called the log-likelihood and written $\ell(\theta)$.

**Why the second equality holds.** If $\phi$ is strictly increasing then it
preserves order, so $L(\theta^*) \ge L(\theta)$ for all $\theta$ if and only if
$\phi(L(\theta^*)) \ge \phi(L(\theta))$ for all $\theta$: the argmax sets of
$L$ and $\phi \circ L$ coincide. Apply this with $\phi = \log$, strictly
increasing on $(0, \infty)$; candidates with $L = 0$ are never maximizers when
any positive value is attainable. The practical payoff: a product of $n$ tiny
numbers becomes a sum of $n$ manageable ones, differentiable term by term, and
numerically stable.

### 7.2 Bernoulli MLE, with the second-order check

**Example.** $X_i$ independent Bernoulli($p$), $\theta = p \in (0,1)$. The
exponent trick writes the pmf in one formula,
$p_X(x) = p^x (1-p)^{1-x}$, which equals $p$ at $x = 1$ and $1 - p$ at
$x = 0$. With $k = \sum_i x_i$ heads,

$$ \ell(p) = \sum_{i=1}^n \log\big[ p^{x_i} (1-p)^{1-x_i} \big]
   = k \log p + (n - k) \log(1 - p). $$

Only two statistics survive: the heads count $k$ and the tails count $n - k$.
Differentiate on $(0,1)$ and set to zero:

$$ \ell'(p) = \frac{k}{p} - \frac{n-k}{1-p} = 0
   \;\Longleftrightarrow\; k(1-p) = (n-k)p
   \;\Longleftrightarrow\; k = np
   \;\Longleftrightarrow\; \hat{p} = \frac{k}{n}. $$

Cross-multiplying is safe because $p$ and $1-p$ are positive in the interior,
and the $-kp$ terms cancel on both sides.

**Second-order check, omitted by the lecture:**

$$ \ell''(p) = -\frac{k}{p^2} - \frac{n-k}{(1-p)^2} < 0
   \qquad \text{for every } p \in (0,1), $$

since both terms are at most $0$ and at least one is strictly negative for
$n \ge 1$. So $\ell$ is strictly concave and the critical point is the unique
global maximum. This is what the lecture's phrase "concave, so the
zero-derivative point is the unique maximum" asserts.

**Boundary cases.** If $k = 0$ then $\ell(p) = n \log(1-p)$ is strictly
decreasing and $\ell'$ never vanishes in the interior; the maximum over
$[0,1]$ sits at the endpoint $\hat{p} = 0$, consistent with $k/n$.
Symmetrically, $k = n$ gives $\hat{p} = 1$. Interior calculus finds the MLE
only when $0 < k < n$; the formula $\hat{p} = k/n$ happens to cover all three
cases. Estimating $\hat{p} \in \{0, 1\}$ from finite data is exactly the
zero-count pathology that ambushes naive Bayes in Section 8.5.

**Sanity chain.** Since $\hat{p} = \bar{X}_n$, Lecture 5's law of large numbers
gives $\hat{p} \to p$ in probability, and Lecture 6's Hoeffding inequality
gives

$$ \Pr\big( |\hat{p} - p| \ge \epsilon \big) \le 2e^{-2n\epsilon^2}. $$

The principled recipe agrees with the obvious one, and concentration certifies
it.

### 7.3 Worked: ten flips, seven heads

With $n = 10$ and $k = 7$, the estimate is $\hat{p} = 0.7$. The likelihood
$L(p) = p^7 (1-p)^3$ at three candidates:

$$ L(0.5) = 0.5^{10} = \frac{1}{1024} = 0.000977 \approx 0.00098, $$

$$ L(0.7) = 0.7^7 \times 0.3^3 = 0.0823543 \times 0.027 = 0.002224
   \approx 0.00222, $$

$$ L(0.9) = 0.9^7 \times 0.1^3 = 0.4782969 \times 0.001 = 0.000478
   \approx 0.00048. $$

All three values check out, and $L(0.7)/L(0.5) = 2.28$, the lecture's "$2.3$
times likelier than a fair coin". Note that the absolute values are tiny, since
every specific ten-flip sequence is unlikely; only the *ratios* matter, which
is likelihood thinking in miniature (Section 3.2).

### 7.4 Gaussian MLE, both parameters, with the checks

**Example.** $X_i$ independent $\mathcal{N}(\mu, \sigma^2)$, with
$\theta = (\mu, \sigma^2)$. The log-likelihood, dropping nothing, is

$$ \ell(\mu, \sigma^2) = \sum_{i=1}^n
   \left[ -\frac{(x_i - \mu)^2}{2\sigma^2}
   - \frac{1}{2} \log 2\pi\sigma^2 \right]. $$

**Solve for $\mu$** with $\sigma^2$ fixed:

$$ \frac{\partial \ell}{\partial \mu}
   = \sum_i \frac{x_i - \mu}{\sigma^2} = 0
   \;\Longleftrightarrow\; \sum_i x_i = n\mu
   \;\Longleftrightarrow\; \hat{\mu} = \frac{1}{n} \sum_i x_i, $$

and $\frac{\partial^2 \ell}{\partial \mu^2} = -\frac{n}{\sigma^2} < 0$, so this
is a maximum in $\mu$ for *every* fixed $\sigma^2$ - which is why $\sigma^2$
cancels entirely: the optimal $\mu$ does not depend on it. Equivalently, the
sample mean minimizes $\sum_i (x_i - \mu)^2$, the mean-minimizes-the-quadratic
fact proved in the Lecture 6 note, Lemma 3.1 Step A.

**Solve for $\sigma^2$.** Substitute $t = \sigma^2$ and
$S = \sum_i (x_i - \hat{\mu})^2$, so that
$\ell(t) = -\frac{S}{2t} - \frac{n}{2} \log(2\pi t)$:

$$ \ell'(t) = \frac{S}{2t^2} - \frac{n}{2t} = 0
   \;\Longleftrightarrow\; t = \frac{S}{n}
   \;\Longleftrightarrow\; \widehat{\sigma^2}
   = \frac{1}{n} \sum_{i=1}^n (x_i - \hat{\mu})^2. $$

**Second-order check.** $\ell''(t) = -\frac{S}{t^3} + \frac{n}{2t^2}$, and at
$\hat{t} = S/n$,

$$ \ell''(\hat{t}) = -\frac{n^3}{S^2} + \frac{n^3}{2S^2}
   = -\frac{n^3}{2S^2} < 0 $$

for $S > 0$, that is unless all samples are identical: a genuine maximum. Since
$\ell(t) \to -\infty$ both as $t$ decreases to $0$ (from the $-S/2t$ term) and
as $t \to \infty$ (from the $-\log t$ term), the unique critical point is the
global maximum.

*Source note.* The LaTeX source `probability25.tex` (line 1749) writes
$\widehat{\sigma^2} = \frac{1}{n} \sum (x_i - \mu)^2$ with the unknown $\mu$;
the correct version plugs in $\hat{\mu}$, as above.

**Omitted detail worth knowing: the MLE of the variance is biased.** Use the
identity

$$ \sum_i (x_i - \bar{x})^2 = \sum_i (x_i - \mu)^2 - n(\bar{x} - \mu)^2, $$

which follows by expanding the square around $\mu$: the cross term is
$-2(\bar{x} - \mu) \sum_i (x_i - \mu) = -2n(\bar{x} - \mu)^2$, which combines
with the $+n(\bar{x} - \mu)^2$ from the last term. Taking expectations,

$$ \mathbb{E}\Big[ \sum_i (X_i - \bar{X})^2 \Big]
   = n\sigma^2 - n \cdot \frac{\sigma^2}{n} = (n-1)\sigma^2, $$

so

$$ \mathbb{E}\big[ \widehat{\sigma^2} \big] = \frac{n-1}{n} \sigma^2,
   \qquad
   \mathrm{Bias}\big( \widehat{\sigma^2} \big) = -\frac{\sigma^2}{n}. $$

The MLE systematically underestimates the variance, because it measures spread
around the *fitted* center, which hugs the data; dividing by $n - 1$ instead of
$n$ removes the bias. This is a live example, one section early, that maximum
likelihood does not imply unbiasedness. Section 9's vocabulary makes the
trade-off precise.

### 7.5 The promised proof: cross-entropy training is MLE

**Claim (from Section 1, proved here in full).** For a model family $q_\theta$
over a finite alphabet and samples $x_1, \dots, x_n$, maximizing the likelihood
is minimizing the cross-entropy loss, which is minimizing a KL divergence:

$$ \operatorname*{argmax}_\theta \sum_{i=1}^n \log q_\theta(x_i)
   = \operatorname*{argmin}_\theta H(\hat{p}_n, q_\theta)
   = \operatorname*{argmin}_\theta D(\hat{p}_n \,\|\, q_\theta). $$

**Step 1 (regroup by value - the skipped step).** Let
$N_x = \#\{i : x_i = x\}$ and let $\hat{p}_n(x) = N_x / n$ be the *empirical
distribution*: non-negative, and summing to $\sum_x N_x / n = 1$, so a genuine
pmf. Grouping the $n$ terms of the loss by which symbol they evaluate,

$$ \frac{1}{n} \sum_{i=1}^n \log \frac{1}{q_\theta(x_i)}
   = \frac{1}{n} \sum_x N_x \log \frac{1}{q_\theta(x)}
   = \sum_x \hat{p}_n(x) \log \frac{1}{q_\theta(x)}
   = H(\hat{p}_n, q_\theta), $$

the cross-entropy of the pair $(\hat{p}_n, q_\theta)$ exactly as defined in
Lecture 2. Since
$\frac{1}{n} \sum_i \log \frac{1}{q_\theta(x_i)} = -\frac{1}{n} \ell(\theta)$,
maximizing $\ell$ is minimizing $H(\hat{p}_n, q_\theta)$, which is the first
equality of the claim - dividing by the constant $n > 0$ and negating flips
argmax to argmin, by Section 7.1's monotone-map argument with
$\phi(u) = -u/n$.

**Step 2 (split off the constant).** By Lecture 2's mismatch theorem
(Lecture 2 note, Section 3), $H(P, Q) = H(P) + D(P \| Q)$. With
$P = \hat{p}_n$ fixed by the data and $Q = q_\theta$ the only
$\theta$-dependent piece, $H(\hat{p}_n)$ is an additive constant in $\theta$,
so the argmin transfers to the KL term. **End of proof.**

Three names, one computation: every cross-entropy training run is maximum
likelihood estimation, and equivalently a KL *projection* of the empirical
distribution onto the model class $\{q_\theta\}$. If the class contains
$\hat{p}_n$ itself, the projection lands on it exactly, with $D = 0$. The
Bernoulli case of Section 7.2 is the one-parameter instance, where $q_p$ can
match any empirical frequency and the MLE $\hat{p} = k/n$ *is* the empirical
distribution. For classifiers the same regrouping runs on pairs
$(x_i, y_i)$ with conditional models $q_\theta(y \mid x)$; the bookkeeping is
identical. The Lecture 2 loop closes: the loss defined there for coding reasons
was MLE all along.

---

## 8 Naive Bayes

### 8.1 The parameter blow-up, counted exactly

Let the features be $X^n = (X_1, \dots, X_n)$, each binary, and let the label
$Y$ be binary. To run Section 5's MAP classifier one needs the
class-conditional model $p_{X^n|Y}(\cdot \mid y)$ for each $y$: a pmf on
$\{0,1\}^n$, that is $2^n$ numbers summing to $1$, hence $2^n - 1$ free
parameters *per class*. For seven-by-seven binarized images, $n = 49$, and

$$ 2^{49} = 562{,}949{,}953{,}421{,}312 \approx 5.63 \times 10^{14}, $$

confirming the lecture's $5.6 \times 10^{14}$. No dataset fills that table, so
an assumption must cut it down.

### 8.2 The assumption, and what it actually says

**Assumption (conditional independence).** Given the label, the features are
mutually independent:

$$ p_{X^n|Y}(x^n \mid y) = \prod_{i=1}^n p_{X_i|Y}(x_i \mid y), $$

equivalently, in the logarithmic form the lecture displays,

$$ \log p_{X^n|Y}(x^n \mid y)
   = \sum_{i=1}^n \log p_{X_i|Y}(x_i \mid y). $$

The two displays are equivalent by taking logarithms or exponentiating. The
count drops from $2^n - 1$ to $n$ Bernoulli parameters per class, where
$p_{i|y} = \Pr(X_i = 1 \mid Y = y)$, plus one prior parameter: $2n + 1$ numbers
in total for binary labels.

Note precisely what is assumed: independence *given the class*, not marginal
independence. In a spam filter, "free" and "winner" are certainly correlated
across all mail, since both flag spam; the assumption says that *within* the
spam pile, seeing one tells you nothing further about the other. That is still
false in general (Section 8.7, wrong but useful), but it is a much weaker
falsehood than marginal independence.

### 8.3 Fitting: why counting is exactly MLE

The lecture asserts the counting formulas; here is why they are the MLE. Given
training data $\{(\mathbf{x}^{(j)}, y^{(j)})\}_{j=1}^N$, the full
log-likelihood under the naive Bayes model with prior parameter $p_y$ is

$$ \sum_{j=1}^N \log p_Y(y^{(j)})
   \;+\; \sum_{i=1}^n \sum_{j :\, y^{(j)} = 1}
     \log p_{X_i|Y}(x^{(j)}_i \mid 1)
   \;+\; \sum_{i=1}^n \sum_{j :\, y^{(j)} = 0}
     \log p_{X_i|Y}(x^{(j)}_i \mid 0). $$

The three groups share no parameters, and within the feature groups each pair
$(i, y)$ has its own parameter $p_{i|y}$ appearing in its own inner sum only.
So the joint maximization *separates* into $2n + 1$ independent
one-dimensional Bernoulli MLE problems, each solved by Section 7.2's
count-and-divide:

$$ p_{i|y} = \frac{\#\{j : x^{(j)}_i = 1 \text{ and } y^{(j)} = y\}}
   {\#\{j : y^{(j)} = y\}}, $$

read as "among class-$y$ mails, the fraction containing word $i$", and

$$ p_y = \Pr(Y = 1) \text{ estimated by }
   \frac{1}{N} \#\{j : y^{(j)} = 1\}, $$

the fraction of spam in the training set.

*Source note.* The LaTeX source `probability25.tex` (line 1791) writes the
prior estimate with $\mathbf{1}\{y^{(j)} = 0\}$ while calling it
$\Pr(Y = 1)$; the correct version counts $y^{(j)} = 1$, as above.

With the fitted model and prior, Section 5's MAP posterior is computable by
Bayes' rule with the products factorized: every ingredient is a count.

### 8.4 Worked: the ten-mail training set, every number re-derived

Take $N = 10$: four spam, six ham. The prior is $p_Y(1) = \tfrac{4}{10}
= \tfrac{2}{5}$ and $p_Y(0) = \tfrac{3}{5}$. The counts: "free" appears in $3$
of the $4$ spam and $1$ of the $6$ ham; "meeting" appears in $1$ of the $4$
spam and $4$ of the $6$ ham. Hence the four fitted parameters

$$ p_{\text{free}|1} = \tfrac{3}{4}, \quad
   p_{\text{free}|0} = \tfrac{1}{6}, \quad
   p_{\text{meet}|1} = \tfrac{1}{4}, \quad
   p_{\text{meet}|0} = \tfrac{4}{6} = \tfrac{2}{3}. $$

**Classify a new mail** containing "free" but not "meeting", so $x = (1, 0)$.
Under conditional independence the class scores, which are the numerators of
Bayes' rule, are

$$ \text{spam:} \quad p_{\text{free}|1} \cdot (1 - p_{\text{meet}|1})
   \cdot p_Y(1) = \tfrac{3}{4} \cdot \tfrac{3}{4} \cdot \tfrac{2}{5}
   = \tfrac{9}{40} = 0.225, $$

$$ \text{ham:} \quad p_{\text{free}|0} \cdot (1 - p_{\text{meet}|0})
   \cdot p_Y(0) = \tfrac{1}{6} \cdot \tfrac{1}{3} \cdot \tfrac{3}{5}
   = \tfrac{1}{30} = 0.0333. $$

Note the $1 - p$ factors: the mail *lacks* "meeting", so the Bernoulli pmf
contributes $1 - p_{\text{meet}|y}$, which is where the factors $\tfrac{3}{4}$
and $\tfrac{1}{3}$ come from. The posterior, exactly: over the common
denominator $120$, $\tfrac{9}{40} = \tfrac{27}{120}$ and
$\tfrac{1}{30} = \tfrac{4}{120}$, so

$$ p_{Y|X^2}(1 \mid 1, 0) = \frac{27}{27 + 4} = \frac{27}{31}
   = 0.871 \approx 0.87, $$

and the verdict is spam.

### 8.5 The zero-count veto

Add the word "winner": present in $2$ of the $4$ spam but $0$ of the $6$ ham,
so the MLE sets $p_{\text{winner}|0} = \tfrac{0}{6} = 0$. Then *any* mail
containing "winner" has ham score
$\prod_i p_{X_i|Y}(x_i \mid 0) = 0$ exactly: a single unseen word-and-class
combination vetoes the entire class, no matter how ham-like the other ten
thousand words are. This is the boundary MLE $\hat{p} \in \{0, 1\}$ of
Section 7.2 doing real damage. With rare words and finite $N$, some counts
*will* be zero - the same finite-sample fluctuation Lecture 5 quantified - so
the failure is guaranteed in practice, not exotic.

### 8.6 Laplace smoothing, and its Bayesian reading

**Laplace smoothing.** Start every count from $1$:

$$ p_{i|y} = \frac{1 + \#\{j : x^{(j)}_i = 1, \; y^{(j)} = y\}}
   {2 + \#\{j : y^{(j)} = y\}}. $$

This is one pretend mail with the word and one without, per class. Estimates
are pulled toward $\tfrac{1}{2}$, and zeros - and ones - become impossible,
since the numerator is at least $1$ and at most the denominator minus $1$.

**Worked, the ham column,** with the unsmoothed MLE for comparison:

- "free", $1$ of $6$: smoothed $\frac{1+1}{2+6} = \tfrac{2}{8} = 0.25$, against
  MLE $\tfrac{1}{6} = 0.167$.
- "meeting", $4$ of $6$: smoothed $\tfrac{5}{8} = 0.625$, against MLE
  $\tfrac{2}{3} = 0.667$.
- "winner", $0$ of $6$: smoothed $\tfrac{1}{8} = 0.125$, against MLE $0$ - the
  veto becomes a strong but finite vote that enough contrary evidence can
  outweigh.

**Where the plus-one and plus-two come from,** omitted by the lecture: put a
Beta prior on the Bernoulli parameter. With $k$ successes in $m$ trials and
prior density proportional to $p^{\alpha - 1}(1-p)^{\beta - 1}$, the posterior
is Beta($\alpha + k$, $\beta + m - k$). The smoothed estimate
$\frac{k+1}{m+2}$ is the *posterior mean* under the uniform prior
$\alpha = \beta = 1$, known as Laplace's rule of succession, and equally the
*MAP* estimate under Beta($2, 2$). Either way, smoothing is Section 5 applied
to the parameters themselves: a prior belief - no word is impossible in either
class - folded into estimation. It deliberately biases the estimate toward
$\tfrac{1}{2}$ to kill the wild variance of small-count MLEs, which is the
exact trade Section 9 prices.

### 8.7 Why wrong but useful

The independence assumption is plainly false - strokes in a digit are
correlated, spam words co-occur - so the fitted $p_{X^n|Y}$ is the wrong
distribution, and the posterior $0.87$ above should not be read as a calibrated
probability. Why does classification still work? Because the classifier reports
only an **argmax**: it is correct whenever the true and modeled score
*rankings* agree at the observed $x$, which is far weaker than the
distributions agreeing.

Two structural reasons the ranking survives.

1. Double-counting correlated evidence typically inflates *both* class scores,
   moving posteriors toward $0$ or $1$ - overconfidence - more than it flips
   their order.
2. In log space naive Bayes is a linear classifier, since
   $\log \frac{\text{score}(1)}{\text{score}(0)}$ is a sum of per-feature
   weights plus a bias, and linear decision boundaries are often adequate even
   when the generative story behind them is wrong.

The cost side is equally instructive: fitting is counting, one pass, no
gradients, $O(nN)$ work. The model is the assumption, and the assumption is the
price of tractability. Discussion in [3, Sec. 8.2.2], with the estimation side
in [2, Ch. 7].

---

## 9 Bias and Variance

### 9.1 The estimator is a random variable

An estimator of a real parameter $\theta \in \Omega \subset \mathbb{R}$ is a
function of the sample, $\hat{\theta}_n = \hat{\theta}(X_1, \dots, X_n)$:
random inputs, hence a random output with a distribution of its own. Two
subtleties the lecture states quickly. First, that distribution depends on the
*true* $\theta$, since the sample was drawn under it, so every expectation
below is "under $\theta$", written $\mathbb{E}$ with $\theta$ fixed. Second,
quality must therefore be a property of the *distribution* of
$\hat{\theta}_n$: a new dataset gives a new estimate, and single realizations
are not gradeable.

### 9.2 The three definitions, with fine print

**Definitions.** For an estimator $\hat{\theta}_n$ of $\theta$, with all
expectations under the true $\theta$ and $\mathbb{E}[\hat{\theta}_n^2] < \infty$
standing,

$$ \mathrm{Bias}(\hat{\theta}_n) = \mathbb{E}[\hat{\theta}_n] - \theta,
   \qquad
   \mathrm{Var}(\hat{\theta}_n)
   = \mathbb{E}\big[ (\hat{\theta}_n - \mathbb{E}[\hat{\theta}_n])^2 \big], $$

$$ \mathrm{MSE}(\hat{\theta}_n)
   = \mathbb{E}\big[ (\hat{\theta}_n - \theta)^2 \big]. $$

Readings: bias is the systematic error, where the estimates *center* versus the
truth; variance is scatter around the estimator's *own* center, not around
$\theta$; mean squared error is the risk under squared-error loss, the distance
to the *truth*, where both failure modes hurt.

"Unbiased" means $\mathbb{E}[\hat{\theta}_n] = \theta$ *for all possible
$\theta$* - the quantifier matters: the constant estimator
$\hat{\theta} \equiv 5$ satisfies the equation at the single point
$\theta = 5$ but is not unbiased. All three quantities are functions of the
unknown $\theta$ in general, and the worked example in Section 9.5 shows the
winner between two estimators genuinely changing with $\theta$.

### 9.3 Theorem 4: the decomposition, line by line

**Theorem 4 (bias-variance decomposition).** If
$\mathbb{E}[\hat{\theta}_n^2] < \infty$, then, exactly,

$$ \mathrm{MSE}(\hat{\theta}_n)
   = \mathrm{Bias}(\hat{\theta}_n)^2 + \mathrm{Var}(\hat{\theta}_n). $$

**Proof.** Write $m = \mathbb{E}[\hat{\theta}_n]$, a constant once $\theta$ is
fixed. Add and subtract it inside the square, the same move as Lecture 5's
completing the square and Section 10's proof:

$$ (\hat{\theta}_n - \theta)^2
   = \big( (\hat{\theta}_n - m) + (m - \theta) \big)^2
   = (\hat{\theta}_n - m)^2 + 2(\hat{\theta}_n - m)(m - \theta)
   + (m - \theta)^2. $$

Take expectations term by term, using linearity (Lecture 1). The first term is
$\mathrm{Var}(\hat{\theta}_n)$ by definition. The third term, $(m-\theta)^2$,
is a constant - expectation does nothing - and equals $\mathrm{Bias}^2$ by
definition. For the cross term, $(m - \theta)$ is constant, so it pulls out:

$$ 2(m - \theta) \, \mathbb{E}\big[ \hat{\theta}_n - m \big]
   = 2(m - \theta)\big( \mathbb{E}[\hat{\theta}_n] - m \big)
   = 2(m - \theta) \cdot 0 = 0, $$

since $m$ *is* $\mathbb{E}[\hat{\theta}_n]$: deviations from one's own mean
average to zero by construction. **End of proof.**

This is an identity, not an inequality: nothing was bounded, and no assumption
was made beyond a finite second moment. Immediate corollary: for an unbiased
estimator, mean squared error equals variance. And the moral the lecture builds
toward: since only the *sum* is the score, deliberately accepting bias to cut
variance can lower the mean squared error - unbiasedness is not sacred.

### 9.4 Example: the sample mean

Take an independent sample with mean $\mu$ and variance $\sigma^2 < \infty$,
and the estimator $\bar{X}_n = \frac{1}{n} \sum_i X_i$. It is unbiased for
every $\mu$, since $\mathbb{E}[\bar{X}_n] = \mu$ by linearity, and its variance
is $\mathrm{Var}(\bar{X}_n) = \sigma^2/n$ by independence (Lecture 5 note,
Section 2). Hence $\mathrm{MSE} = 0^2 + \sigma^2/n \to 0$: the sample mean is
*consistent*, converging to $\mu$ in probability by Chebyshev applied to the
vanishing mean squared error. This is precisely Lecture 5's law-of-large-numbers
argument retold in estimation vocabulary.

### 9.5 Worked: can bias help? The smoothed coin, in full

**Setup.** Coin bias $p$, $n = 10$ flips, $S = \sum_i X_i$ Binomial($10, p$),
so $\mathbb{E}[S] = 10p$ and $\mathrm{Var}(S) = 10p(1-p)$. Two estimators: the
MLE $\hat{p} = S/10$ and the Laplace-smoothed
$\tilde{p} = \frac{S+1}{12}$, which is Section 8.6's rule with $m = 10$.

**Moments of $\hat{p}$.** $\mathbb{E}[\hat{p}] = p$, so it is unbiased, and

$$ \mathrm{Var}(\hat{p}) = \frac{10p(1-p)}{100} = \frac{p(1-p)}{10}
   = \mathrm{MSE}(\hat{p}). $$

**Moments of $\tilde{p}$.** $\mathbb{E}[\tilde{p}] = \frac{10p + 1}{12}$, so

$$ \mathrm{Bias}(\tilde{p}) = \frac{10p + 1}{12} - p
   = \frac{10p + 1 - 12p}{12} = \frac{1 - 2p}{12}, \qquad
   \mathrm{Var}(\tilde{p}) = \frac{\mathrm{Var}(S)}{144}
   = \frac{10 \, p(1-p)}{144}. $$

Both formulas check out. Note $\frac{10}{144} = 0.069 < 0.100 = \frac{1}{10}$,
so the smoothed estimator has $31\%$ less variance at *every* $p$: shrinking
toward $\tfrac{1}{2}$ compresses the scatter. By Theorem 4,

$$ \mathrm{MSE}(\tilde{p}) = \frac{(1-2p)^2}{144} + \frac{10p(1-p)}{144}. $$

**The numbers, re-derived.** Two values of $p$, each with both estimators:

- At $p = 0.5$: $\mathrm{MSE}(\hat{p}) = \frac{0.25}{10} = 0.0250$, while
  $\mathrm{MSE}(\tilde{p}) = \frac{0 + 2.5}{144} = 0.01736 \approx 0.0174$. The
  smoothed estimator wins - its bias is exactly zero there, and it keeps the
  variance cut.
- At $p = 0.9$: $\mathrm{MSE}(\hat{p}) = \frac{0.09}{10} = 0.0090$, while
  $\mathrm{MSE}(\tilde{p}) = \frac{0.64 + 0.9}{144} = 0.01069 \approx 0.0107$,
  where $0.64 = (-0.8)^2$ comes from $144 \times (-0.8/12)^2$. The unbiased
  estimator wins - near the edge, shrinking toward $\tfrac{1}{2}$ is shrinking
  in the wrong direction.

All four entries check out.

**The crossings, solved exactly.** The lecture reports them as roughly $0.14$
and $0.86$. Set the two mean squared errors equal, writing $q = p(1-p)$ and
noting $(1-2p)^2 = 1 - 4q$:

$$ \frac{144 \, q}{10} = (1 - 4q) + 10q
   \;\Longleftrightarrow\; 14.4 \, q - 10 \, q = 1 - 4q
   \;\Longleftrightarrow\; 8.4 \, q = 1
   \;\Longleftrightarrow\; q = \frac{5}{42}. $$

Then $p^2 - p + \frac{5}{42} = 0$ gives

$$ p = \frac{1 \pm \sqrt{11/21}}{2} = \frac{1 \pm 0.7237}{2},
   \qquad\text{that is}\qquad p = 0.138 \ \text{ and } \ p = 0.862. $$

So the biased estimator wins on the middle $72\%$ of the parameter range.

**The regularization trade, named.** Weight decay (Section 5.5) and Laplace
smoothing (Section 8.6) are the same move: accept a controlled pull toward a
default - zero weights, a fair coin - in exchange for a large cut in
sensitivity to the sample. The decomposition makes it an accounting identity
rather than folklore, and it connects to Lecture 6's U-shaped risk curve, which
is the same bias-variance tension with model-class size as the knob.

---

## 10 MMSE Estimation

### 10.1 Setup

Now *both* $X$, the source, and $Y$, the noisy measurement, are random with
known joint distribution, and the score is mean squared error: find, among
**all** functions $\hat{X}(\cdot)$ of the measurement, the minimizer of
$\mathbb{E}[(X - \hat{X}(Y))^2]$. The standing assumption is
$\mathbb{E}[X^2] < \infty$, since otherwise every estimator has infinite mean
squared error and the question is empty. Competitors may be restricted to those
with $\mathbb{E}[\hat{X}(Y)^2] < \infty$, since any other has infinite mean
squared error by the triangle inequality and can be discarded.

### 10.2 Theorem 5, with the orthogonality argument

**Lemma 10.1 (orthogonality of the residual).** For every function $g$ with
$\mathbb{E}|g(Y)(X - \mathbb{E}[X \mid Y])| < \infty$,

$$ \mathbb{E}\Big[ \big( X - \mathbb{E}[X \mid Y] \big) \, g(Y) \Big] = 0. $$

**Proof.** Split by linearity into
$\mathbb{E}[g(Y) X] - \mathbb{E}[g(Y) \, \mathbb{E}[X \mid Y]]$, and the two
terms are equal by Lemma 2.1, the pull-out property. Equivalently, in the
conditioned form,
$\mathbb{E}[X - \mathbb{E}[X \mid Y] \mid Y]
= \mathbb{E}[X \mid Y] - \mathbb{E}[X \mid Y] = 0$, so multiplying by the
$Y$-measurable $g(Y)$ and towering gives $0$. **End of proof of Lemma 10.1.**

The residual $X - \mathbb{E}[X \mid Y]$ is *orthogonal to every function of
$Y$*: the estimation error left after the conditional mean cannot be predicted
any further from $Y$, linearly or nonlinearly. Geometric reading: in the space
of finite-second-moment random variables with inner product
$\langle U, V \rangle = \mathbb{E}[UV]$, the functions of $Y$ form a subspace,
and $\mathbb{E}[X \mid Y]$ is the orthogonal projection of $X$ onto it. The
theorem below is the Pythagorean theorem for this projection.

**Theorem 5 (the MMSE estimator is the conditional mean).** For any function
$\hat{X}(\cdot)$,

$$ \mathbb{E}\big[ (X - \hat{X}(Y))^2 \big]
   \;\ge\; \mathbb{E}\big[ (X - \mathbb{E}[X \mid Y])^2 \big], $$

with equality if and only if $\hat{X}(Y) = \mathbb{E}[X \mid Y]$ with
probability $1$.

**Proof.** *Step 1 (insert and expand).* Add and subtract
$\mathbb{E}[X \mid Y]$ - the add-and-subtract move for the third time in this
lecture - and square out:

$$ \mathbb{E}\big[ (X - \hat{X}(Y))^2 \big]
   = \mathbb{E}\big[ (X - \mathbb{E}[X \mid Y])^2 \big]
   + \mathrm{cross}
   + \mathbb{E}\big[ (\mathbb{E}[X \mid Y] - \hat{X}(Y))^2 \big], $$

where

$$ \mathrm{cross} = 2 \, \mathbb{E}\Big[ \big( X - \mathbb{E}[X \mid Y] \big)
   \big( \mathbb{E}[X \mid Y] - \hat{X}(Y) \big) \Big]. $$

*Steps 2 and 3 (the cross term dies).* The second factor is a function of $Y$
alone; call it $g(Y) = \mathbb{E}[X \mid Y] - \hat{X}(Y)$. Lemma 10.1 applies
verbatim, so $\mathrm{cross} = 2 \cdot 0 = 0$. Spelled out with the tower, as
the lecture does: condition on $Y$; given $Y$, $g(Y)$ is a constant and slides
out of the inner expectation, whose remaining factor is
$\mathbb{E}[X - \mathbb{E}[X \mid Y] \mid Y] = 0$; the outer expectation of
$2 g(Y) \cdot 0$ is $0$. This is why the *random* center needs the tower where
Theorem 4's constant center needed only linearity.

*Step 4 (read off the minimizer).* What remains is a fixed number, in which
$\hat{X}$ appears nowhere, plus a non-negative penalty:

$$ \mathbb{E}\big[ (X - \hat{X}(Y))^2 \big]
   = \mathbb{E}\big[ (X - \mathbb{E}[X \mid Y])^2 \big]
   + \mathbb{E}\big[ (\mathbb{E}[X \mid Y] - \hat{X}(Y))^2 \big]. $$

The penalty is at least $0$, and is $0$ if and only if
$\hat{X}(Y) = \mathbb{E}[X \mid Y]$ with probability $1$. Dropping it gives the
inequality; its vanishing condition settles both the minimizer and its
uniqueness. **End of proof.**

The achieved optimum has a name and a formula:

$$ \mathrm{MMSE} = \mathbb{E}\big[ (X - \mathbb{E}[X \mid Y])^2 \big]
   = \mathbb{E}\big[ \mathrm{Var}(X \mid Y) \big], $$

obtained by towering the square and noting that given $Y$ the inner expectation
is precisely the conditional variance. It is the average *leftover* spread
after seeing the measurement - the squared-error analogue of Fano's
$H(Y \mid X)$.

### 10.3 Worked: the running distribution, with a cross-check

On Section 2's joint distribution, the optimal estimator is
$\hat{X}(0) = \mathbb{E}[X \mid Y = 0] = \tfrac{2}{3}$ and
$\hat{X}(1) = 0$. Sum the squared error over the three cells carrying mass:
the cell $(x,y) = (0,0)$ contributes
$\tfrac{1}{4}(0 - \tfrac{2}{3})^2$, the cell $(1,0)$ contributes
$\tfrac{1}{2}(1 - \tfrac{2}{3})^2$, and the cell $(0,1)$ contributes
$\tfrac{1}{4}(0 - 0)^2$, so

$$ \mathrm{MMSE} = \tfrac{1}{4} \cdot \tfrac{4}{9}
   + \tfrac{1}{2} \cdot \tfrac{1}{9} + 0
   = \tfrac{1}{9} + \tfrac{1}{18} = \tfrac{3}{18} = \tfrac{1}{6}. $$

**Cross-check via conditional variances.** Given $Y = 0$, $X$ is
Bernoulli($\tfrac{2}{3}$) with variance
$\tfrac{2}{3} \cdot \tfrac{1}{3} = \tfrac{2}{9}$; given $Y = 1$, $X$ is
identically $0$ with variance $0$. So

$$ \mathbb{E}\big[ \mathrm{Var}(X \mid Y) \big]
   = \tfrac{3}{4} \cdot \tfrac{2}{9} + \tfrac{1}{4} \cdot 0 = \tfrac{1}{6}, $$

the same answer, by the formula at the end of Section 10.2.

**Against the best constant.** The best $Y$-blind guess is the constant
minimizing $\mathbb{E}[(X - c)^2]$, which is $c = \mathbb{E}[X] = \tfrac{1}{2}$
with mean squared error
$\mathrm{Var}(X) = \tfrac{1}{2} - \tfrac{1}{4} = \tfrac{1}{4}$, by
mean-minimizes-the-quadratic (Lecture 6 note, Lemma 3.1 Step A). Since
$\tfrac{1}{6} < \tfrac{1}{4}$, watching $Y$ removes a third of the error. The
gap is exactly the *law of total variance*,

$$ \mathrm{Var}(X) = \mathbb{E}\big[ \mathrm{Var}(X \mid Y) \big]
   + \mathrm{Var}\big( \mathbb{E}[X \mid Y] \big), $$

and indeed
$\mathrm{Var}(\mathbb{E}[X \mid Y])
= \tfrac{3}{4} \cdot (\tfrac{2}{3})^2 - (\tfrac{1}{2})^2
= \tfrac{1}{3} - \tfrac{1}{4} = \tfrac{1}{12}
= \tfrac{1}{4} - \tfrac{1}{6}$. What observation buys is precisely the variance
*of* the conditional mean.

### 10.4 The loss picks the estimator

Regression with mean-squared-error loss aims, by Theorem 5, at the conditional
mean $\mathbb{E}[Y_{\text{label}} \mid \text{input}]$: the network is a
parameterized guess at that function, and training pushes it toward the target
the theorem names. Lecture 4's diffusion teaser is the same statement: the
ideal denoiser trained with squared error outputs
$\mathbb{E}[\text{clean} \mid \text{noisy}]$. Estimation theory names the
target, optimization approximates it; Lecture 8 computes it in closed form for
the Gaussian channel, where it becomes linear.

The lecture's closing summary, completed with one row the lecture omits:

- Zero-one loss gives the posterior mode - MAP, Theorem 2.
- Squared loss gives the conditional mean - Theorem 5.
- Absolute loss gives the conditional *median*, by the same
  insert-and-compare proof pattern run on the absolute value instead of the
  square.

The posterior is the object; the loss chooses which of its summaries to
report.

---

## 11 References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI: 10.1002/047174882X, at
   https://doi.org/10.1002/047174882X. Section 2.10 has Fano's inequality in
   the sharp form of Section 6.2, with the same error-flag proof; this is the
   standard modern source for the result, which originates in Robert M. Fano's
   early-1950s MIT information-theory course - Fano himself never published it
   in a journal, and citing Cover and Thomas is the accepted attribution.
   Chapter 2 has the entropy toolkit recalled from Lectures 1 to 3.
2. G. Casella and R. L. Berger, *Statistical Inference*, 2nd ed., Duxbury and
   Thomson Learning, 2002. Chapters 6 and 7: likelihood, MLE including the
   non-existence and non-uniqueness pathologies of Section 4.5, and Bayes
   estimators. Section 7.3: bias, mean squared error, and the bias-variance
   decomposition. Section 7.2.2: the Gaussian MLE and the $(n-1)/n$ bias of
   Section 7.4.
3. C. M. Bishop, *Pattern Recognition and Machine Learning*, Springer, 2006.
   Free PDF at the publisher-authorized Microsoft Research page,
   https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/.
   Sections 1.2.5 to 3.1: MLE, MAP, and the Gaussian-prior and regularization
   correspondence of Section 5.5. Sections 2.1 to 2.2: the Beta-Bernoulli
   conjugacy behind Laplace smoothing. Section 8.2.2: conditional independence
   and naive Bayes. Sections 1.5.5 and 3.2: squared loss, the conditional mean,
   and bias-variance.
4. E. L. Lehmann and G. Casella, *Theory of Point Estimation*, 2nd ed.,
   Springer, 1998. DOI: 10.1007/b98854, at https://doi.org/10.1007/b98854.
   Chapters 1 and 2: estimators, unbiasedness, mean squared error and the
   decomposition at full rigor. Chapter 4: Bayes and MMSE estimation, and
   conditional expectation as the $L_2$ projection of Section 10.2.
5. The Lecture 1 to Lecture 6 companion notes in this repository, which state
   and prove every imported lemma cited by section number in the text:
   Lecture 1 (LOTUS, the entropy ceiling), Lecture 2 (the mismatch theorem
   $H(P,Q) = H(P) + D(P \| Q)$ used in Section 7.5), Lecture 3 (conditional
   entropy, the chain rule, the data-processing inequality), Lecture 5 (the
   variance of averages, the law of large numbers), and Lecture 6 (Hoeffding,
   the ERM corollary, mean-minimizes-the-quadratic). The accessible editions
   are the files `prob01-foundations-note.md` through
   `prob06-generalization-note.md`, each in its own lecture folder.
6. M. J. Wainwright, *High-Dimensional Statistics: A Non-Asymptotic
   Viewpoint*, Cambridge University Press, 2019. DOI: 10.1017/9781108627771,
   at https://doi.org/10.1017/9781108627771. Chapter 15: minimax lower bounds,
   where Fano's inequality is run over a packing of hard distributions - the
   theory-workhorse use mentioned in Section 6.6.
