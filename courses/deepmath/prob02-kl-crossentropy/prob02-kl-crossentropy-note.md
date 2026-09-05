# Deep Learning Math, Lecture 2: KL Divergence and Cross-Entropy Loss

**About this file.** Screen-reader edition of the Lecture 2 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob02-kl-crossentropy-note.html`, 2026-09 revision). Nothing else is needed to
read it.

**Notation.** $\log$ means logarithm base 2, and information is measured in bits;
$\ln$ is the natural logarithm. $P$, $Q$ are probability mass functions on a
finite alphabet $\mathcal{X}$ with $|\mathcal{X}| = M$; $p_X$ is the true pmf of
$X$. $D(P \Vert Q)$ is the KL divergence and $H(P,Q)$ the cross-entropy. The
double bar in $D(P \Vert Q)$ is written `\Vert`.

**Background used.** Entropy, LOTUS and Jensen's inequality from Lecture 1 are
quoted as lemmas in Section 2.1 rather than re-proved; their proofs are in the
Lecture 1 note, Sections 3.3, 4.3 and 5.3.

**Contents.**

1. Why cross-entropy
2. Recall and teaser
3. The mismatch theorem
4. KL divergence
5. Betting, coding, predicting
6. Cross-entropy loss
7. KL across deep learning
8. References

## 1. Why Cross-Entropy?

Every classification project contains one line of code: `nn.CrossEntropyLoss()`.
Write $f(x) = (f(x)_1, \dots, f(x)_M)$ for the model's predicted probability
vector over $M$ labels and $y$ for the true label. The loss on one sample is

$$ \ell(f(x), y) = \log \frac{1}{f(x)_y} = -\log f(x)_y. $$

Why this *particular* decreasing function of $f(x)_y$? Any decreasing function,
such as $1 - f(x)_y$ or $(1 - f(x)_y)^{2}$, rewards putting belief on the true
label; nothing in the phrase "penalize wrong answers" forces a logarithm or a
reciprocal.

The answer developed below: $\log (1/Q)$ is *surprisal* priced by a model pmf
$Q$; its expectation under the truth is the *cross-entropy* $H(P, Q)$; the excess
of that over the entropy $H(P)$ is exactly the *KL divergence* $D(P \Vert Q)$; so
minimizing cross-entropy is minimizing the KL divergence from the model to the
truth. The same quantity has an operational meaning with money attached
(Section 5): $D(P \Vert Q)$ is the exponential rate at which a gambler who
believes $Q$ loses wealth to a gambler who knows $P$.
Section 5 adds two more costumes, code length and next-token prediction
(perplexity); Section 6 asks why the *log* rather than any other decreasing
function (proper scoring rules, locality, the softmax gradient); and Section 7
tours where KL, in which direction, sits inside modern training objectives.

**A remark on units.** This note uses $\log_2$. PyTorch's `CrossEntropyLoss`
uses $\ln$, and takes raw logits, applying log-softmax internally. Since
$\log_2 t = \ln t / \ln 2$, the two losses differ by the constant factor
$1/\ln 2 \approx 1.4427$: same minimizer, same gradients up to scale. Every
theorem below is base-independent.

## 2. Recall and Teaser

### 2.1 What is imported from Lecture 1

Setting: $X$ is a discrete random variable with true pmf $p_X$ on a finite
alphabet $\mathcal{X}$ of size $M$. Three facts are used as lemmas.

**Surprisal and entropy.** $S(x) = \log \frac{1}{p_X(x)}$ and
$H(X) = \mathbb{E}[\log \frac{1}{p_X(X)}] = \sum_x p_X(x) \log \frac{1}{p_X(x)}$,
with the continuity convention $0 \log \frac{1}{0} = 0$; equivalently, sums run
over the support. Range: $0 \leq H(X) \leq \log M$.

**LOTUS.** $\mathbb{E}[f(X)] = \sum_x f(x) p_X(x)$ for any function $f$. This is
used silently every time an expectation is expanded as a sum below.

**Jensen's inequality.** If $f$ is concave and $Z$ takes finitely many values in
its domain then $\mathbb{E}[f(Z)] \leq f(\mathbb{E}[Z])$; if $f$ is *strictly*
concave, equality holds if and only if $Z$ is constant, that is, all mass on one
point. The key instance is $f = \log$, strictly concave on $(0,\infty)$ because
$(\log t)'' = -1/(t^{2} \ln 2) < 0$.

The proof pattern to remember from the maximum-entropy theorem of Lecture 1: trap
an expectation under a logarithm, use Jensen to move the logarithm outside, and
let the pmf weight $p_X(x)$ cancel whatever ratio sits inside. Both moves recur
verbatim in Theorem 1.

### 2.2 The teaser

Surprisal prices outcome $x$ by the *true* pmf. A learned model does not have
$p_X$; it has a guess $Q$. Outcomes still arrive with frequencies $p_X$, but the
model pays the bill $\log \frac{1}{Q(x)}$. How does the average mismatched bill

$$ \mathbb{E}\left[\log \frac{1}{Q(X)}\right] = \sum_x p_X(x) \log \frac{1}{Q(x)} $$

compare with the honest bill $H(X)$? A priori it could seem to go either way:
$Q$ might under-price some outcomes, since $Q(x) > p_X(x)$ makes that term
cheaper, and over-price others. The mismatch theorem says the savings can never
beat the losses; the true pmf is the unique cheapest pricing.

## 3. The Mismatch Theorem

### 3.1 Statement

**Theorem 1 (mismatch).** Let $X$ have pmf $p_X$ on a finite alphabet
$\mathcal{X}$, and let $Q$ be any pmf on $\mathcal{X}$, so $Q(x) \geq 0$ and
$\sum_{x} Q(x) = 1$. Then

$$ H(X) \leq \mathbb{E}\left[\log \frac{1}{Q(X)}\right]
   = \sum_{x} p_X(x) \log \frac{1}{Q(x)}, $$

with equality if and only if $Q = p_X$. Conventions: terms with $p_X(x) = 0$
contribute 0; and if $Q(x) = 0$ for some $x$ with $p_X(x) > 0$, the right-hand
side is $+\infty$ and the inequality holds trivially.

Both conventions are continuity statements: $t \log \frac{1}{t} \to 0$ as
$t \to 0^{+}$ (proved by l'Hopital in the Lecture 1 note, Section 4.3), while
$p \log \frac{1}{q} \to +\infty$ as $q \to 0^{+}$ for fixed $p > 0$. The second
is not a technicality: a model that declares an outcome *impossible* pays an
infinite bill the first time that outcome occurs. This is why classifiers end in
a softmax, which keeps every $Q(x)$ strictly positive.

### 3.2 Numeric example

Truth $P = (0.01, 0.99)$, model $Q = (0.1, 0.9)$. The mismatched bill:

$$ \mathbb{E}\left[\log \frac{1}{Q(X)}\right]
   = 0.01 \log \frac{1}{0.1} + 0.99 \log \frac{1}{0.9}
   = 0.01 \times 3.3219 + 0.99 \times 0.1520 \approx 0.1837 \text{ bits}. $$

The honest bill, computed in the Lecture 1 note, Section 4.4:

$$ H(X) = 0.01 \log \frac{1}{0.01} + 0.99 \log \frac{1}{0.99}
   \approx 0.0664 + 0.0144 \approx 0.0808 \text{ bits}. $$

The overpayment is $0.1837 - 0.0808 \approx 0.103$ bits per draw: the model pays
more than double the optimum. Section 4 identifies that gap as $D(P \Vert Q)$.

### 3.3 Proof in three steps

Assume for now that $p_X(x) > 0$ for all $x \in \mathcal{X}$, and that
$Q(x) > 0$ wherever needed; the general case is Section 3.4. The target is
$H(X) - \mathbb{E}[\log \frac{1}{Q(X)}] \leq 0$.

*Step 1: merge the gap.* Both terms are expectations of functions of $X$ under
the same pmf $p_X$, so linearity of expectation combines them, and
$\log a - \log b = \log \frac{a}{b}$ merges the logarithms:

$$ H(X) - \mathbb{E}\left[\log \frac{1}{Q(X)}\right]
   = \mathbb{E}\left[\log \frac{1}{p_X(X)} - \log \frac{1}{Q(X)}\right]
   = \mathbb{E}\left[\log \frac{Q(X)}{p_X(X)}\right]. $$

*Step 2: Jensen.* Apply Jensen's inequality with the strictly concave
$f = \log$ to the positive random variable $Z = Q(X)/p_X(X)$:

$$ \mathbb{E}\left[\log \frac{Q(X)}{p_X(X)}\right]
   \leq \log \mathbb{E}\left[\frac{Q(X)}{p_X(X)}\right]. $$

*Step 3: cancellation.* Expand the inner expectation by LOTUS. The weight
$p_X(x)$ cancels the denominator, and $Q$ is a pmf:

$$ \log \mathbb{E}\left[\frac{Q(X)}{p_X(X)}\right]
   = \log \sum_x p_X(x) \frac{Q(x)}{p_X(x)}
   = \log \sum_x Q(x) = \log 1 = 0. $$

Chaining the three displays gives
$H(X) - \mathbb{E}[\log \frac{1}{Q(X)}] \leq 0$. **End of proof.**

*Equality.* The only inequality used was Jensen with the strictly concave
logarithm, which is tight if and only if $Z = Q(X)/p_X(X)$ is constant, that is
$Q(x) = c \, p_X(x)$ for all $x$. Summing over $x$ gives $1 = c \cdot 1$, so
$c = 1$ and $Q = p_X$. Conversely $Q = p_X$ plainly gives equality.
**End of proof.**

### 3.4 The edge case, solved

The proof above divides by $p_X(x)$, which is illegal where $p_X(x) = 0$. Here is
the rigorous version.

**Rigorous proof of Theorem 1.** If $Q(x) = 0$ for some $x$ with $p_X(x) > 0$,
the right-hand side is $+\infty$ and there is nothing to prove; so assume
$Q(x) > 0$ whenever $p_X(x) > 0$. Let $\mathcal{S} = \{x : p_X(x) > 0\}$ be the
support. By the zero-mass convention, both $H(X)$ and the cross term are sums
over $\mathcal{S}$ only, so

$$ H(X) - \mathbb{E}\left[\log \frac{1}{Q(X)}\right]
   = \sum_{x \in \mathcal{S}} p_X(x) \log \frac{Q(x)}{p_X(x)}. $$

Every ratio $Q(x)/p_X(x)$ for $x \in \mathcal{S}$ is now well defined and
positive, and Jensen still applies, over the pmf $p_X$ restricted to
$\mathcal{S}$ where it sums to 1:

$$ \sum_{x \in \mathcal{S}} p_X(x) \log \frac{Q(x)}{p_X(x)}
   \leq \log \sum_{x \in \mathcal{S}} p_X(x) \frac{Q(x)}{p_X(x)}
   = \log \sum_{x \in \mathcal{S}} Q(x). $$

The final sum is *no longer necessarily* 1: it omits any mass $Q$ puts outside
the support of $p_X$. But it is at most 1, and the logarithm is increasing, so

$$ \log \sum_{x \in \mathcal{S}} Q(x) \leq \log 1 = 0, $$

and the theorem follows.

*Equality* now requires both inequalities to be tight: (i) Jensen is tight if and
only if $Q(x)/p_X(x) = c$ for all $x \in \mathcal{S}$; (ii)
$\sum_{x \in \mathcal{S}} Q(x) = 1$ if and only if $Q(x) = 0$ for every $x$
outside $\mathcal{S}$. Given (ii), summing (i) over $\mathcal{S}$ gives
$1 = c \cdot 1$, so $c = 1$ and $Q(x) = p_X(x)$ on $\mathcal{S}$; combined with
(ii), $Q = p_X$ everywhere. **End of proof.**

Note the asymmetry of the two ways of "putting zeros": $Q$ vanishing off the
support of $p_X$ costs nothing, since inequality (ii) can still be tight, while
$Q$ vanishing *on* the support costs everything, an infinite bill.

### 3.5 Cross-entropy, defined

**Definition (cross-entropy).** For pmfs $P$ and $Q$ on $\mathcal{X}$,

$$ H(P, Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{1}{Q(x)} \in [0, +\infty], $$

with the conventions of Theorem 1: $0 \cdot \log \frac{1}{Q(x)} = 0$ even when
$Q(x) = 0$, and $H(P,Q) = +\infty$ if $P(x) > 0 = Q(x)$ for some $x$.

It is the expected surprisal when outcomes are drawn from $P$ but priced by $Q$;
the two arguments are crossed, hence the name. In this notation Theorem 1 reads
$H(P, Q) \geq H(P, P) = H(P)$, with equality if and only if $Q = P$. Note that
$H(P,Q)$ is *not* symmetric in its arguments, and that $H(P,P) = H(P)$ recovers
ordinary entropy. Writing $H(X)$ and $H(p_X)$ interchangeably is a common abuse
of notation.

## 4. KL Divergence

### 4.1 Definition and conventions

**Definition (Kullback-Leibler divergence, also called relative entropy [3]).**
For pmfs $P$ and $Q$ on $\mathcal{X}$,

$$ D(P \Vert Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{P(x)}{Q(x)}
   \in [0, +\infty], $$

with conventions $0 \log \frac{0}{q} = 0$ for any $q \geq 0$, including
$0 \log \frac{0}{0} = 0$, and $p \log \frac{p}{0} = +\infty$ for $p > 0$.

Spelled out: $D(P \Vert Q)$ is finite only if $Q(x) = 0$ implies $P(x) = 0$, that
is, only if the support of $P$ is contained in the support of $Q$. For general
measures this containment is called absolute continuity, written $P \ll Q$.
Outcomes outside the support of $P$ never contribute. Equivalently,
$D(P \Vert Q)$ is the expected log-likelihood-ratio of truth to model, weighted
by the truth:

$$ D(P \Vert Q) = \mathbb{E}_{X \sim P}\left[\log \frac{P(X)}{Q(X)}\right]. $$

**Finiteness.** $D(P \Vert Q) < \infty$ if and only if $\operatorname{supp} P
\subseteq \operatorname{supp} Q$.

**Proof.** Every term with $P(x) = 0$ is $0$ by convention. If
$\operatorname{supp} P \subseteq \operatorname{supp} Q$, every remaining term
has $P(x), Q(x) > 0$ and is a finite real number, so the finite sum is finite.
Conversely, if some $x$ has $P(x) > 0 = Q(x)$, that term is $+\infty$ and no
finite term can cancel it. **End of proof.**

In words: the truth may be *narrower* than the model, never wider. Both
conventions are continuity statements, $t \log t \rightarrow 0$ as $t \downarrow
0$ and $p \log \tfrac{p}{q} \rightarrow +\infty$ as $q \downarrow 0$ for fixed
$p > 0$.

**Support in deep learning.** The cross-entropy loss on the true label $y$ is
$\log 1/Q(y)$ (Section 6), so $Q(y) = 0$ gives an infinite loss on a single
sample. Three consequences:

- A softmax output $e^{z_i} / \sum_j e^{z_j}$ is strictly positive for every
  finite logit vector, so every label keeps some mass and the loss stays finite.

- Label smoothing (Section 7.3) replaces the one-hot target $y^{(o)}$ by
  $(1-\varepsilon)\, y^{(o)} + \varepsilon / M$, which has full support: it
  *widens the truth* rather than narrowing the model.

- Forward KL $D(P \Vert Q)$ is infinite the moment the model rules out something
  the truth allows; this is the "zero-avoiding" behavior developed in Section
  7.1.

### 4.2 Worked example in both directions

Take $P = (0.5, 0.4, 0.1)$ and uniform $Q = (1/3, 1/3, 1/3)$. Forward direction,
term by term:

$$ D(P \Vert Q)
   = 0.5 \log \frac{0.5}{1/3} + 0.4 \log \frac{0.4}{1/3} + 0.1 \log \frac{0.1}{1/3}
   = 0.5 \log 1.5 + 0.4 \log 1.2 + 0.1 \log 0.3, $$

$$ D(P \Vert Q) \approx 0.2925 + 0.1052 - 0.1737 \approx 0.2240 \text{ bits}. $$

Individual terms may be negative, here the third one, because $P$ under-weights
outcome 3 relative to $Q$ so its log-ratio is negative. Only the *sum* is
guaranteed non-negative. Reverse direction:

$$ D(Q \Vert P)
   = \tfrac13 \log \frac{1/3}{0.5} + \tfrac13 \log \frac{1/3}{0.4}
   + \tfrac13 \log \frac{1/3}{0.1}
   \approx -0.1950 - 0.0877 + 0.5790 \approx 0.2963 \text{ bits}. $$

So $D(P \Vert Q) \approx 0.224$ differs from $D(Q \Vert P) \approx 0.296$.

**Uniform-$Q$ shortcut**, proved in one line: if $Q$ is uniform on $M$ symbols,

$$ D(P \Vert Q) = \sum_x P(x) \log (M P(x)) = \log M - H(P). $$

Check: $\log 3 - H(P) = 1.5850 - 1.3610 = 0.2240$, where
$H(P) = 0.5 \cdot 1 + 0.4 \log 2.5 + 0.1 \log 10 \approx 1.3610$. The
maximum-entropy theorem $H(P) \leq \log M$ from Lecture 1 is thus the special
case "$D(P \Vert \text{uniform}) \geq 0$" of Theorem 2 below.

**Asymmetry can be extreme.** Let $P = (1/2, 1/2)$ and $Q = (1, 0)$. Then

$$ D(P \Vert Q) = \tfrac12 \log \frac{1/2}{1} + \tfrac12 \log \frac{1/2}{0}
   = +\infty, $$

$$ D(Q \Vert P) = 1 \cdot \log \frac{1}{1/2} + 0 \cdot \log \frac{0}{1/2}
   = 1 \text{ bit}. $$

One direction is infinite and the other is one bit: believing an impossible thing
is possible is mildly wrong, while believing a possible thing is impossible is
infinitely wrong, because under the first argument's draws the "impossible"
outcome eventually happens. Keeping track of which argument holds the truth is
therefore not pedantry.

### 4.3 Divergence, not distance

$D$ fails two of the three metric axioms: it is not symmetric, as just computed,
and it does not satisfy the triangle inequality; it also need not be finite. It
does satisfy the separation axiom, namely $D(P \Vert Q) \geq 0$ with equality if
and only if $P = Q$ (Theorem 2), and that is exactly enough for its main use: a
quantity that is zero precisely at "model equals truth" and positive otherwise
can be *minimized* to drive a model toward the truth. Objects with separation but
without symmetry or the triangle inequality are called divergences.

### 4.4 Theorem 2: the information inequality

**Theorem 2 (information inequality).** For any pmfs $P$ and $Q$ on
$\mathcal{X}$, $D(P \Vert Q) \geq 0$, with equality if and only if $P = Q$.

*Proof.* This is Theorem 1 re-read. Take $X \sim P$ in Theorem 1 (rigorous
version, Section 3.4); its two sides differ by exactly $-D(P \Vert Q)$:

$$ -D(P \Vert Q) = \sum_{x \,:\, P(x) > 0} P(x) \log \frac{Q(x)}{P(x)}
   = H(P) - H(P, Q) \leq 0, $$

with equality if and only if $Q = P$, by the equality analysis already done.
**End of proof.**

Theorem 2 as proved above inherits the support bookkeeping of Section 3.4. The
next subsection gives a second proof that handles every zero-mass case by a
single lemma, which then also delivers the convexity of $D$ (Theorem 3).

### 4.5 Technique: $t \log t$, the log-sum inequality, and Theorem 2 with zeros

The function behind everything in this section is $f(t) = t \log t$ on $(0,
\infty)$, extended by $f(0) = 0$. It is *strictly convex*: $f'(t) = \log t +
\tfrac{1}{\ln 2}$ and $f''(t) = \tfrac{1}{t \ln 2} > 0$. Landmarks: $f(1) = 0$; the minimum is at $f'(t) = 0$, i.e. $t = 1/e$, with value
$f(1/e) = -\tfrac{\log e}{e} = -\tfrac{1.4427}{2.7183} \approx -0.531$ bits; and
$f(3) = 3 \log 3 \approx 4.755$. Jensen's inequality for a *convex* $f$ runs the
other way from Section 2.1: $\mathbb{E}[f(Z)] \geq f(\mathbb{E}[Z])$, with
equality iff $Z$ is constant when $f$ is strictly convex.

**Lemma (log-sum inequality [1, Thm 2.7.1]).** For $a_1, \dots, a_n \geq 0$ and
$b_1, \dots, b_n > 0$,

$$ \sum_{i=1}^{n} a_i \log \frac{a_i}{b_i} \;\geq\; \Bigl(\sum_i a_i\Bigr) \log \frac{\sum_i a_i}{\sum_i b_i}, $$

with $0 \log 0 = 0$; equality iff $a_i / b_i$ is the same for all $i$. ("Merging
terms can only lower the sum.")

**Proof.** Put $B = \sum_j b_j$, weights $w_i = b_i / B$ (a pmf on $\{1, \dots,
n\}$), points $t_i = a_i / b_i \geq 0$. Then $a_i \log \tfrac{a_i}{b_i} = b_i\,
t_i \log t_i = B\, w_i f(t_i)$, so

$$ \sum_i a_i \log \frac{a_i}{b_i}
   = B \sum_i w_i\, f(t_i)
   \;\overset{(\text{Jensen})}{\geq}\; B\, f\Bigl(\sum_i w_i t_i\Bigr)
   = B\, f\Bigl(\frac{\sum_i a_i}{B}\Bigr)
   = \Bigl(\sum_i a_i\Bigr) \log \frac{\sum_i a_i}{\sum_j b_j}, $$

using $\sum_i w_i t_i = \sum_i a_i / B$ in the middle. Strict convexity of $f$
makes Jensen tight iff all $t_i$ coincide. **End of proof.**

(If some $b_i = 0$ with $a_i > 0$ the left side is $+\infty$ and the inequality
is trivial; indices with $a_i = b_i = 0$ can be discarded. So the hypothesis
$b_i > 0$ costs no generality.)

**Corollary (Theorem 2, zeros included).** Take $a_x = P(x)$, $b_x = Q(x)$ over
$x \in \operatorname{supp} P$. If some $Q(x) = 0$ there, $D(P \Vert Q) = +\infty
\geq 0$ and there is nothing to prove. Otherwise

$$ D(P \,\Vert\, Q)
   \;\overset{(\text{log-sum})}{\geq}\; 1 \cdot \log \frac{1}{\sum_{x \in \operatorname{supp} P} Q(x)}
   \;\overset{(\text{sub-sum} \,\leq\, 1)}{\geq}\; \log 1 = 0. \qquad \text{(end of proof)} $$

**Equality** needs both steps tight: $P(x)/Q(x)$ constant on
$\operatorname{supp} P$ (log-sum) and $\sum_{\operatorname{supp} P} Q(x) = 1$,
i.e. no $Q$-mass off the support. Together they force $P = Q$. The convention $0
\log 0 = 0$ handled every $P(x) = 0$ term for free.

### 4.6 Theorem 3: KL is convex in the pair

**Theorem 3 (convexity of KL [1, Thm 2.7.2]).** For pmfs $(P_1, Q_1)$, $(P_2,
Q_2)$ on $\mathcal{X}$ and $\lambda \in [0, 1]$,

$$ D\bigl(\lambda P_1 + (1-\lambda) P_2 \,\Vert\, \lambda Q_1 + (1-\lambda) Q_2\bigr)
   \;\leq\; \lambda\, D(P_1 \,\Vert\, Q_1) + (1-\lambda)\, D(P_2 \,\Vert\, Q_2). $$

**Proof.** Fix $x$ and apply the two-term log-sum inequality with $a_1 = \lambda
P_1(x)$, $a_2 = (1-\lambda) P_2(x)$, $b_1 = \lambda Q_1(x)$, $b_2 = (1-\lambda)
Q_2(x)$ (read the lemma right-to-left):

$$ (a_1 + a_2) \log \frac{a_1 + a_2}{b_1 + b_2}
   \;\leq\; a_1 \log \frac{a_1}{b_1} + a_2 \log \frac{a_2}{b_2}
   = \lambda P_1(x) \log \frac{P_1(x)}{Q_1(x)} + (1-\lambda) P_2(x) \log \frac{P_2(x)}{Q_2(x)}, $$

because the factors $\lambda$ and $1-\lambda$ cancel inside each log. The left
side is the $x$-th term of the mixture divergence; sum over $x$. (Terms where a
$b_i = 0$ with $a_i > 0$ make the right side $+\infty$, where the inequality is
trivial.) **End of proof.**

Mixing truths and models together never increases the divergence. In particular
$D$ is convex in $Q$ for fixed $P$ (take $P_1 = P_2$), the property that makes
"minimize $D(P \Vert Q_\theta)$" a convex problem when $Q_\theta$ is linear in
$\theta$. Two later uses: the data-processing inequality
(prob03) and variational bounds (Section 7).

### 4.7 Theorem 4: cross-entropy = entropy + KL

**Theorem 4 (cross-entropy decomposition).** For pmfs $P, Q$ on $\mathcal{X}$
with $\operatorname{supp} P \subseteq \operatorname{supp} Q$,

$$ H(P, Q) \;=\; H(P) + D(P \,\Vert\, Q). $$

(Without the support hypothesis both sides are $+\infty$ and the identity still
holds formally.)

**Proof.** Split the log-ratio inside $D$; sums run over $\operatorname{supp}
P$, where every term is finite:

$$ D(P \,\Vert\, Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}
   = \underbrace{\sum_x P(x) \log P(x)}_{-H(P)}
   + \underbrace{\sum_x P(x) \log \frac{1}{Q(x)}}_{H(P,\,Q)}, $$

i.e. $D = -H(P) + H(P, Q)$. Rearranging gives the claim. **End of proof.**

The mismatch overpayment of Theorem 1 *is* the KL divergence: Theorem 1 is now
an exact identity plus Theorem 2. In the Section 3.2 example, $D(P \Vert Q) =
0.1837 - 0.0808 \approx 0.103$ bits (direct computation: $0.01 \log
\tfrac{0.01}{0.1} + 0.99 \log \tfrac{0.99}{0.9} \approx 0.1029$). Since $H(P)$
contains no $Q$, minimizing $H(P, Q)$ over $Q$ is minimizing $D(P \Vert Q)$;
that one sentence is the whole of Section 6. (The source notes' displayed
derivation of this identity drops a $p_X(x)$ factor in one intermediate line, a
typo, and the version above is the corrected computation.)

### 4.8 Theorem 5: KL adds over independent samples

**Theorem 5 (additivity).** Let $P^n(x_1, \dots, x_n) = \prod_{i=1}^n P(x_i)$
and $Q^n$ likewise be the pmfs of $n$ i.i.d. draws on $\mathcal{X}^n$. Then

$$ D(P^n \,\Vert\, Q^n) = n \cdot D(P \,\Vert\, Q), \qquad H(P^n, Q^n) = n \cdot H(P, Q). $$

**Proof.** Write $X^n = (X_1, \dots, X_n) \sim P^n$, so each $X_i \sim P$. The
log of a product is a sum of logs, and expectation is linear:

$$ D(P^n \,\Vert\, Q^n)
   = \mathbb{E}_{P^n}\Bigl[\log \prod_{i=1}^n \frac{P(X_i)}{Q(X_i)}\Bigr]
   = \sum_{i=1}^n \mathbb{E}\Bigl[\log \frac{P(X_i)}{Q(X_i)}\Bigr]
   = n \cdot D(P \,\Vert\, Q), $$

since each summand is the same expectation under $X_i \sim P$ (independence is
used only through the product form of $P^n$ and $Q^n$). The same computation
with $\log \tfrac{1}{Q(X_i)}$ in place of the ratio gives $H(P^n, Q^n) = n H(P,
Q)$. **End of proof.**

KL is therefore a *rate*: bits of mismatch per sample. Check: $P = (0.5, 0.4,
0.1)$, $Q$ uniform, $n = 3$ gives $3 \times 0.2240 = 0.6721$ bits.672 = 3 \times 0.224$. Note that if $P^n$ and $Q^n$ had been arbitrary joint
pmfs (not products) the identity would fail; Theorem 5 is a statement about
independence.

### 4.9 KL as a rate: the law-of-large-numbers view

Additivity says the total log-likelihood ratio of $n$ i.i.d. samples has
expectation $nD$. The law of large numbers upgrades this from expectation to
typical behavior: for $x_1, x_2, \dots \overset{\text{iid}}{\sim} P$ with
$\operatorname{supp} P \subseteq \operatorname{supp} Q$,

$$ \frac{1}{n} \sum_{i=1}^{n} \log \frac{P(x_i)}{Q(x_i)} \;\longrightarrow\; D(P \,\Vert\, Q) \qquad (n \rightarrow \infty), $$

almost surely, because the summands $\log \tfrac{P(x_i)}{Q(x_i)}$ are i.i.d.,
bounded (finitely many values, all finite under the support hypothesis), with
mean $D(P \Vert Q)$, exactly the hypotheses of the strong law.

**Flag.** The law of large numbers is *not* proved in this lecture; it is
treated in prob05. A single simulation illustrates the convergence: $P = (0.5, 0.4,
0.1)$, $Q = (\tfrac13, \tfrac13, \tfrac13)$, $1000$ draws, running average of
$\log \tfrac{P(x_i)}{Q(x_i)}$ (bits) recorded at $n = 1, 2, 3, 5, 8, 12, 20, 30,
50, 80, 120, 200, 300, 500, 700, 1000$:

| $n$ | 1 | 2 | 3 | 5 | 8 | 12 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|
| avg | $-1.737$ | $-1.737$ | $-0.963$ | $-0.408$ | $-0.116$ | $0.037$ | $-0.008$ | $0.157$ |
| $n$ | 50 | 80 | 120 | 200 | 300 | 500 | 700 | 1000 |
| avg | $0.078$ | $0.042$ | $0.127$ | $0.171$ | $0.192$ | $0.205$ | $0.211$ | $0.211$ |

The first two draws were the rare outcome $3$, whose single-sample log-ratio is
$\log \tfrac{0.1}{1/3} = -1.737$ bits, so the running average starts far below
the limit and climbs toward $D = 0.224$; at $n = 1000$ it sits at $0.211$. The
individual summands range from $-1.737$ to $\log \tfrac{0.5}{1/3} = 0.585$, so
single draws can be "wrong-signed" while the average is not: $D \geq 0$ is a
statement about the mean.

### 4.10 $f$-divergences: Definition, Theorem 6, and the zoo

KL is one member of a family that shares the Jensen proof.

**Definition ($f$-divergence [9], [10]).** Let $f : (0, \infty) \rightarrow
\mathbb{R}$ be convex with $f(1) = 0$. For pmfs $P, Q$ with $\operatorname{supp}
P \subseteq \operatorname{supp} Q$,

$$ D_f(P \,\Vert\, Q) = \sum_{x \in \operatorname{supp} Q} Q(x)\, f\Bigl(\frac{P(x)}{Q(x)}\Bigr). $$

KL is the case $f(t) = t \log t$: $\sum_x Q(x) \tfrac{P(x)}{Q(x)} \log
\tfrac{P(x)}{Q(x)} = D(P \Vert Q)$. (Terms with $P(x) = 0 < Q(x)$ contribute
$Q(x) f(0)$, with $f(0) = \lim_{t \downarrow 0} f(t)$, which is $0$ for $t \log
t$.)

**Theorem 6 ($f$-divergences are non-negative).** $D_f(P \Vert Q) \geq 0$, with
equality if $P = Q$; if $f$ is strictly convex at $1$, equality holds *only* if
$P = Q$.

**Proof.** Jensen with weights $Q(x)$ (a pmf) and points $t_x = P(x)/Q(x)$,
whose $Q$-mean is $\sum_x Q(x) \tfrac{P(x)}{Q(x)} = \sum_x P(x) = 1$:

$$ \sum_x Q(x)\, f\Bigl(\frac{P(x)}{Q(x)}\Bigr)
   \;\overset{(\text{Jensen})}{\geq}\; f\Bigl(\sum_x Q(x) \frac{P(x)}{Q(x)}\Bigr) = f(1) = 0. $$

If $P = Q$ all $t_x = 1$ and every term is $f(1) = 0$. If $f$ is strictly convex
at $1$ (no supporting line at $1$ touches $f$ elsewhere), Jensen is tight only
when all $t_x = 1$, i.e. $P = Q$. **End of proof.**

**The zoo, on the running example.** $P = (0.5, 0.4, 0.1)$, $Q = (\tfrac13,
\tfrac13, \tfrac13)$; all logs base 2. Every entry below was recomputed from the
definition.

| $f(t)$ | name | $D_f(P \Vert Q)$ | computation |
|---|---|---|---|
| $t \log t$ | KL $D(P \Vert Q)$ | $0.224$ | Section 4.2 |
| $-\log t$ | reverse KL $D(Q \Vert P)$ | $0.296$ | $\sum_x Q(x) \log \tfrac{Q(x)}{P(x)}$, Section 4.2 |
| $\tfrac12 \lvert t - 1 \rvert$ | total variation $\tfrac12 \sum_x \lvert P(x) - Q(x) \rvert$ | $0.233$ | $0.0833 + 0.0333 + 0.1167$ |
| $(t-1)^2$ | $\chi^2$, $\sum_x \tfrac{(P(x) - Q(x))^2}{Q(x)}$ | $0.260$ | $0.0833 + 0.0133 + 0.1633$ |
| $\tfrac12\bigl[t \log \tfrac{2t}{1+t} + \log \tfrac{2}{1+t}\bigr]$ | Jensen-Shannon $\tfrac12 D(P \Vert M) + \tfrac12 D(Q \Vert M)$, $M = \tfrac{P+Q}{2}$ | $0.062$ | $M = (0.4167, 0.3667, 0.2167)$; $\tfrac12(0.0702) + \tfrac12(0.0540)$ |

Two checks that the $f$'s are the right ones: with $t = P/Q$, $Q \cdot \tfrac12
\lvert t - 1 \rvert = \tfrac12 \lvert P - Q \rvert$ and $Q\,(t-1)^2 = (P-Q)^2 /
Q$; for Jensen-Shannon, $Q \cdot \tfrac12 [t \log \tfrac{2t}{1+t} + \log
\tfrac{2}{1+t}] = \tfrac12 P \log \tfrac{2P}{P+Q} + \tfrac12 Q \log
\tfrac{2Q}{P+Q}$, whose sum over $x$ is $\tfrac12 D(P \Vert M) + \tfrac12 D(Q
\Vert M)$. Total variation is bounded by $1$ and symmetric; Jensen-Shannon is
bounded by $1$ bit and symmetric; KL and $\chi^2$ are neither. All five vanish
iff $P = Q$.

### 4.11 What KL alone brings

Every $f$-divergence is non-negative and zero exactly at $P = Q$ (Theorem 6), so
non-negativity does not single out KL. Three properties in this lecture do:

- **Additive** over independent samples: $D(P^n \Vert Q^n) = n D(P \Vert Q)$
  (Theorem 5). Total variation, for instance, is not: it is bounded by $1$ for
  any $n$.

- **Decomposes** the cross-entropy: $H(P, Q) = H(P) + D(P \Vert Q)$, with a
  $P$-only constant (Theorem 4). This is what turns "minimize the training loss"
  into "minimize a divergence".

- Its integrand is a **surprisal difference**, $\log \tfrac{1}{Q(x)} - \log
  \tfrac{1}{P(x)}$: the guessing bill of Section 3, the betting and coding costs
  of Section 5.

**Left open (flag).** Is KL the *only* $f$-divergence with these properties? No
uniqueness theorem is stated, and none is proved here. What is settled
today is the direction of use: $D(P \Vert Q)$ is the price of believing $Q$ in a
$P$ world, in log-wealth and bits (Section 5), in training loss (Section 6), and
inside distillation, RLHF and VAE objectives (Section 7).

## 5. Betting, Coding, Predicting

### 5.1 Setup: red or black

A binary game. RED wins with probability $p$ and BLACK with probability $1-p$;
take $p \leq 1/2$, so BLACK is the favorite. This assumption is used only to fix
which corner maximizes $\mathbb{E}[S]$ below, not for any theorem. The odds are
2-for-1 on both colors: the money bet on the winning color is doubled and the
rest is lost. With budget $B$, bet $qB$ on red and $(1-q)B$ on black, where
$q \in [0,1]$. The wealth after one round is the random variable

$$ S = \begin{cases}
   2qB & \text{if red wins, with probability } p, \\
   2(1-q)B & \text{if black wins, with probability } 1-p.
   \end{cases} $$

### 5.2 First try: maximize expected wealth, and why it ruins you

$$ \mathbb{E}[S] = p \cdot 2qB + (1-p) \cdot 2(1-q)B
   = 2B\left[(1-p) + q(2p-1)\right]. $$

This is *linear* in $q$ with slope $2B(2p-1)$, which is negative for $p < 1/2$. A
linear function on $[0,1]$ is maximized at an endpoint, here $q = 0$: all-in on
black, with $\mathbb{E}[S] = 2(1-p)B > B$.

Now repeat the all-in strategy over $n$ independent rounds, reinvesting
everything each time. You are still solvent after $n$ rounds only if black won
every round:

$$ \Pr(\text{alive after } n \text{ bets}) = (1-p)^{n} \to 0
   \quad \text{as } n \to \infty, \text{ for } p > 0, $$

$$ S_n = \begin{cases}
   2^{n} B & \text{with probability } (1-p)^{n}, \\
   0 & \text{otherwise.}
   \end{cases} $$

So ruin is certain in the limit, even though $\mathbb{E}[S_n] = (2(1-p))^{n} B$
*grows exponentially*. There is no contradiction: the expectation is carried
entirely by the single all-wins path, whose probability vanishes. Expected wealth
is the wrong objective for repeated betting because it is blind to ruin.

### 5.3 The fix: maximize expected log-wealth

Two reasons to score wealth on the logarithmic scale.

- $\log 0 = -\infty$, so any strategy with positive ruin probability gets
  objective $-\infty$; maximizing $\mathbb{E}[\log S]$ automatically excludes
  ruin.
- Wealth *multiplies* across rounds, so log-wealth *adds*:
  $\log S_n = \log B + \sum_{k=1}^{n} \log(\text{growth factor of round } k)$.
  Averages of sums are what the law of large numbers controls, which is what
  makes "growth rate" a meaningful per-round quantity (Section 5.5).

Compute the objective, splitting the logarithms of products:

$$ \mathbb{E}[\log S] = p \log(2qB) + (1-p) \log(2(1-q)B), $$

$$ \mathbb{E}[\log S] = p[\log 2B + \log q] + (1-p)[\log 2B + \log(1-q)], $$

$$ \mathbb{E}[\log S] = \log 2B
   - \left(p \log \frac{1}{q} + (1-p) \log \frac{1}{1-q}\right). $$

The bracket is exactly the cross-entropy $H((p, 1-p), (q, 1-q))$ of the betting
fractions against the true win probabilities, and Theorem 1 already tells us its
unique minimizer.

### 5.4 Theorem 7: proportional betting, binary case

**Theorem 7 (proportional betting).** In the binary game with odds 2 and
$0 < p < 1$, the objective $\mathbb{E}[\log S]$ is maximized over $q \in [0,1]$
uniquely at $q = p$, and

$$ \max_q \mathbb{E}[\log S] = \log 2B - h_2(p), $$

where $h_2(p) = p \log \frac{1}{p} + (1-p) \log \frac{1}{1-p}$ is the binary
entropy function. Moreover, for any $q$,

$$ \mathbb{E}[\log S_{\text{opt}}] - \mathbb{E}[\log S_q]
   = D((p, 1-p) \Vert (q, 1-q)). $$

*Proof.* Apply the decomposition $H(P,Q) = H(P) + D(P \Vert Q)$ (Theorem 4) to
the bracket, with $P = (p, 1-p)$ and $Q = (q, 1-q)$:

$$ \mathbb{E}[\log S] = \log 2B - h_2(p) - D((p, 1-p) \Vert (q, 1-q)). $$

Only the last term depends on $q$; by Theorem 2 it is non-negative, with equality
if and only if $(q, 1-q) = (p, 1-p)$, that is $q = p$. Both claims follow. The
endpoints are consistent: $q \in \{0,1\}$ with $0 < p < 1$ gives $D = +\infty$
and indeed $\mathbb{E}[\log S] = -\infty$, so the all-in strategies are
infinitely bad on the logarithmic scale. **End of proof.**

Bet your beliefs, in exact proportion: the optimal split copies the probability
vector, regardless of the (fair) odds. And the cost of betting the wrong beliefs
$Q$ is precisely the KL divergence from your beliefs to the truth. This is the
second costume of the same quantity after the guessing bill of Section 3; code
lengths (Section 5.8) and next-token prediction (Section 5.9) follow. The log-optimal criterion is due to Kelly [4], whose
1956 paper set up exactly this correspondence between information rate and wealth
growth.

### 5.5 Doubling rate

**Definition (doubling rate, binary game).** For betting fractions $(q, 1-q)$,

$$ W = \log 2 - \left(p \log \frac{1}{q} + (1-p) \log \frac{1}{1-q}\right)
   = \mathbb{E}\left[\log \frac{S}{B}\right], $$

the expected logarithmic growth factor of one round: the budget-free part of
$\mathbb{E}[\log S] = \log B + W$.

The informal statements $S \approx B \times 2^{W}$ and
$S_n \approx B \times 2^{nW}$ mean the following. Repeat the same strategy over
$n$ independent identically distributed rounds, reinvesting the full bankroll.
The per-round growth factors $G_k = S_k / S_{k-1}$ are i.i.d. with
$\mathbb{E}[\log G_k] = W$, and

$$ \frac{1}{n} \log \frac{S_n}{B} = \frac{1}{n} \sum_{k=1}^{n} \log G_k
   \to W \quad \text{almost surely}, $$

by the strong law of large numbers, which is treated later in this course
(Lecture 5). Equivalently $S_n = B \cdot 2^{n(W + o(1))}$: log-wealth grows
linearly at slope $W$ bits per bet, so wealth grows or decays exponentially at
rate $W$. Three regimes: $W > 0$ exponential growth, $W = 0$ treading water,
$W < 0$ exponential ruin. Note that this is the *typical*, almost-sure exponent,
not the exponent of $\mathbb{E}[S_n]$; Section 5.2 showed those can disagree
wildly.

### 5.6 Theorem 8: horse racing

Generalize to $M$ horses. Horse $i$ wins with probability $p_X(i)$; the odds are
$M$-for-1 on every horse, that is, uniform fair odds; the gambler splits the
budget as $(Q(1)B, \dots, Q(M)B)$ where $Q$ is a pmf. Winner takes all: if horse
$i$ wins then $S = M Q(i) B$.

**Theorem 8 (proportional betting, $M$ horses).**

$$ \mathbb{E}[\log S] = \log B + \log M - \sum_{i=1}^{M} p_X(i) \log \frac{1}{Q(i)}
   = \log B + \log M - H(p_X) - D(p_X \Vert Q), $$

maximized uniquely at $Q = p_X$, with maximum $\log B + \log M - H(p_X)$; the
loss for betting $Q$ instead is exactly $D(p_X \Vert Q)$. The doubling rate of
strategy $Q$ is

$$ W(Q) = \log M - H(p_X) - D(p_X \Vert Q). $$

*Proof.* Expand by LOTUS and split the logarithm of the triple product:

$$ \mathbb{E}[\log S] = \sum_{i=1}^{M} p_X(i) \log (M Q(i) B)
   = \sum_{i=1}^{M} p_X(i) [\log M + \log B + \log Q(i)]. $$

The constants pull out, since $\sum_i p_X(i) = 1$, leaving

$$ \mathbb{E}[\log S] = \log B + \log M
   - \sum_{i=1}^{M} p_X(i) \log \frac{1}{Q(i)}
   = \log B + \log M - H(p_X, Q). $$

Apply $H(p_X, Q) = H(p_X) + D(p_X \Vert Q)$ (Theorem 4); only $D$ depends on
$Q$, and Theorem 2 finishes as before. **End of proof.**

Theorem 7 is the case $M = 2$. Note that $W^{*} = \log M - H(p_X)$ can be
negative: at uniform fair odds the game is profitable only if the race is
*predictable enough*, that is $H(p_X) < \log M$, meaning $p_X$ is non-uniform;
against a perfectly uniform race the best doubling rate is 0. Uniform-$Q$ check:
$D(p_X \Vert \text{uniform}) = \log M - H(p_X) = W^{*}$, so the uniform bettor
has $W = W^{*} - W^{*} = 0$ exactly. Betting $B/M$ on each horse at $M$-for-1
odds returns the budget unchanged, deterministically.

### 5.7 The three-horse race, fully computed

Win probabilities $p = (1/2, 1/4, 1/4)$ and odds 3-for-1. First,
$H(p) = \frac12 \cdot 1 + \frac14 \cdot 2 + \frac14 \cdot 2 = 1.5$ bits, so

$$ W^{*} = \log 3 - H(p) = 1.58496 - 1.5 = 0.08496 \approx 0.085
   \text{ bits per race}. $$

Over 100 races the optimal bettor, using $Q = p$, multiplies wealth by
$2^{100 W^{*}} = 2^{8.496} \approx 361$. (Rounding the exponent to
$100 \times 0.085 = 8.5$ instead gives $2^{8.5} \approx 362$.)

Three gamblers, each with $D(p \Vert Q)$ computed from the definition:

- $Q = p = (1/2, 1/4, 1/4)$: $D = 0$, so $W = W^{*} \approx +0.085$, and 100
  races multiply wealth by about 361.
- $Q = (1/3, 1/3, 1/3)$: by the uniform-$Q$ shortcut
  $D(p \Vert Q) = \log 3 - H(p) \approx 0.085$, so $W = W^{*} - D = 0$ exactly.
  This gambler treads water, multiplying wealth by 1 forever, and as noted above
  this is deterministic, not merely true on average.
- $Q = (1/4, 1/4, 1/2)$, with favorite and longshot swapped:

$$ D(p \Vert Q) = \tfrac12 \log \frac{1/2}{1/4} + \tfrac14 \log \frac{1/4}{1/4}
   + \tfrac14 \log \frac{1/4}{1/2}
   = \tfrac12 (1) + \tfrac14 (0) + \tfrac14 (-1) = 0.25 \text{ bits}, $$

  so $W = 0.08496 - 0.25 \approx -0.165$, and 100 races multiply wealth by
  $2^{-16.504} \approx 1.08 \times 10^{-5}$, roughly one part in 93,000. Same
  race, same odds: beliefs alone separate a 361-fold fortune from near-total
  ruin.

The classifier analogy is now exact: a model that outputs label probabilities is
a gambler betting a pmf on the outcome, and Section 6 charges it the same
penalty. First, two more costumes.

### 5.8 Coding costume: code lengths and the Shannon code

Suppose symbols $x \in \mathcal{X}$ arrive i.i.d. from $P$ and are to be written
down in binary, one codeword per symbol, so that a concatenation of codewords
can be decoded unambiguously (a *prefix code*: no codeword is a prefix of
another). A model $Q$ suggests the **Shannon code**: give symbol $x$ a codeword
of length

$$ \ell_Q(x) = \Bigl\lceil \log \frac{1}{Q(x)} \Bigr\rceil \text{ bits}. $$

**Kraft inequality (stated, not proved, flag).** A prefix code with codeword
lengths $\ell_1, \dots, \ell_M$ exists if and only if $\sum_i 2^{-\ell_i} \leq
1$. This is the code-existence theorem of Cover & Thomas [1, Ch. 5]; it is
flagged here and not proved in this course.

Shannon lengths satisfy Kraft: $\sum_x 2^{-\lceil \log 1/Q(x) \rceil} \leq
\sum_x 2^{-\log 1/Q(x)} = \sum_x Q(x) = 1$. So the Shannon code for $Q$ exists.

**Proposition (expected code length under mismatch).** For any $Q$ with
$\operatorname{supp} P \subseteq \operatorname{supp} Q$,

$$ H(P) + D(P \,\Vert\, Q) \;\leq\; \mathbb{E}_P[\ell_Q(X)] \;<\; H(P) + D(P \,\Vert\, Q) + 1. $$

**Proof.** Pointwise, $\log \tfrac{1}{Q(x)} \leq \lceil \log \tfrac{1}{Q(x)}
\rceil < \log \tfrac{1}{Q(x)} + 1$. Take expectations under $P$: the outer terms
become $H(P, Q)$ and $H(P, Q) + 1$, and $H(P, Q) = H(P) + D(P \Vert Q)$ by
Theorem 4. **End of proof.**

So the coder who believes $Q$ pays $D(P \Vert Q)$ extra bits per symbol, plus at
most one bit of integer rounding. The rounding bit is an artifact that block
coding removes (code $n$ symbols at once and use Theorem 5, $H(P^n, Q^n) = n
H(P, Q)$: the overhead is $< 1$ bit per *block*, i.e. $< 1/n$ per symbol); the
$D(P \Vert Q)$ is not an artifact and never goes away. Numbers for $P = (0.5,
0.4, 0.1)$:

- $Q = P$: lengths $\lceil \log 2 \rceil, \lceil \log 2.5 \rceil, \lceil \log 10
  \rceil = (1, 2, 4)$; $\mathbb{E}[\ell] = 0.5 + 0.8 + 0.4 = 1.70$ bits; floor
  $H(P) = 1.361$; Kraft sum $\tfrac12 + \tfrac14 + \tfrac1{16} = 0.8125 \leq 1$.

- $Q$ uniform: lengths $\lceil \log 3 \rceil = (2, 2, 2)$; $\mathbb{E}[\ell] =
  2.00$ bits; floor $H(P, Q) = \log 3 = 1.585 = 1.361 + 0.224$; Kraft sum
  $0.75$.

### 5.9 Predicting costume: language models and perplexity

A language model assigns, at each position $t$, a pmf $Q(\cdot \mid x_{< t})$
over the vocabulary of $K$ tokens. Its training loss on a text $x_1, \dots, x_T$
is the average surprisal of the true next token,

$$ \ell_t = \log \frac{1}{Q(x_t \mid x_{< t})}, \qquad \text{loss} = \frac{1}{T} \sum_{t=1}^{T} \ell_t, $$

a cross-entropy per token (PyTorch reports it in nats). Each $\ell_t$ is a
single-sample cross-entropy loss in the sense of Section 6.1, with the
conditional pmf as the model's bet.

**Definition (perplexity).**

$$ \mathrm{PPL} = 2^{\,\text{CE in bits}} = e^{\,\text{CE in nats}}. $$

The two forms agree because $\text{CE}_{\text{nats}} = \text{CE}_{\text{bits}}
\cdot \ln 2$ and $2^{a} = e^{a \ln 2}$; perplexity is base-free.

If the model spreads its guess uniformly over $K$ tokens, $\text{CE} = \log K$
bits and $\mathrm{PPL} = K$: $K = 2, 10, 50{,}000$ give $1$, $3.3219$, $15.6096$
bits ($0.6931$, $2.3026$, $10.8198$ nats) and perplexities $2$, $10$,
$50{,}000$. Read a general $\mathrm{PPL}$ as the *effective number of equally
likely next tokens* the model is choosing among.

### 5.10 Shannon's guessing game in the new costume

The three costumes meet on one token. Let $P$ be the true next-token pmf at some
position and $Q$ the model's, so $\text{CE} = H(P, Q)$ at that step.

- **Coding:** CE per token is the bits per token a Shannon code built from $Q$
  spends compressing the text (Section 5.8, up to the rounding bit).

- **Betting:** a race with $K$ horses (tokens) at fair odds $K$-for-$1$, betting
  $Q$: by Theorem 8 with $M = K$,

$$ W = \log K - H(P, Q) = \log K - \text{CE} = \log \frac{K}{\mathrm{PPL}}, \qquad 2^{W} = \frac{K}{\mathrm{PPL}}. $$

Lower perplexity: fewer bits per token, faster doubling.

**Caveat (flag).** Theorem 8 assumes i.i.d. races; text is not i.i.d. The
identity $W = \log K - H(P, Q)$ holds exactly for the *one-step* expected log-
growth at each position (the proof of Theorem 8 is a single expectation and
never uses independence), so over a text $W$ is a per-token average of one-step
doubling rates. The almost-sure growth interpretation of Section 5.5 would need
an ergodic-type law of large numbers, which is not claimed.

## 6. Cross-Entropy Loss

### 6.1 Classification setup

Inputs $x \in \mathcal{X}$, for instance $\mathbb{R}^{n}$ for images; labels
$y \in [M] = \{1, \dots, M\}$. A probabilistic classifier is a map
$f : \mathcal{X} \to \mathcal{M}$, where $\mathcal{M}$ is the set of pmfs on
$[M]$, the probability simplex. So $f(x) = (f(x)_1, \dots, f(x)_M)$ with
$f(x)_i \geq 0$ and $\sum_{i=1}^{M} f(x)_i = 1$, and $f(x)_i$ is read as the
model's believed probability that $x$ has label $i$. In practice a network
produces arbitrary real scores called logits, and the softmax layer maps them
into $\mathcal{M}$; softmax outputs are strictly positive, a fact that matters
below.

**Definition (cross-entropy loss).** For prediction $f(x)$ and true label $y$,

$$ \ell(f(x), y) = \log \frac{1}{f(x)_y}, $$

the surprisal of the true label under the model's pmf, equal to $+\infty$ if
$f(x)_y = 0$.

Only the probability assigned to the *true* label enters; how the remaining mass
is spread among wrong labels is irrelevant to this sample's loss.

### 6.2 Three-class example

True label $y = \text{cat}$, and three models bet on (cat, dog, ship):

- Confident and right, betting $(0.99, 0.005, 0.005)$: loss
  $\log \frac{1}{0.99} \approx 0.0145$ bits.
- Decent, betting $(0.7, 0.2, 0.1)$: loss
  $\log \frac{1}{0.7} \approx 0.5146$ bits.
- Confused, betting $(0.3, 0.4, 0.3)$: loss
  $\log \frac{1}{0.3} \approx 1.7370$ bits.

The confused model would even *misclassify*, since its largest coordinate is dog,
yet its loss is finite. A model betting $f(x)_{\text{cat}} = 0$ would take
infinite loss regardless of anything else.

### 6.3 Three candidate losses; proper scoring rules; log loss is strictly proper

Section 1 asked why $\log 1/f(x)_y$ rather than some other decreasing function
of the mass on the true label. Three candidates, all satisfying "higher belief
on the truth, lower loss":

$$ \underbrace{1 - f(x)_y}_{\text{linear}}, \qquad
   \underbrace{\sum_{i=1}^{M} \bigl(f(x)_i - \mathbb{1}[i = y]\bigr)^2}_{\text{Brier (squared error to one-hot)}}, \qquad
   \underbrace{\log \tfrac{1}{f(x)_y}}_{\text{log}}. $$

A criterion is needed. The classical one asks: if the forecaster *knows* the
truth $P$, does the loss reward reporting it?

**Definition (proper and strictly proper scoring rule [12]).** Let $\ell(Q, y)$
be a loss for reporting the pmf $Q$ when outcome $y$ occurs, and define the
expected loss under the truth $P$,

$$ L(P, Q) = \mathbb{E}_{Y \sim P}\bigl[\ell(Q, Y)\bigr] = \sum_{i} P_i\, \ell(Q, i). $$

$\ell$ is *proper* if $L(P, P) \leq L(P, Q)$ for all $P, Q$, and *strictly
proper* if moreover equality holds only when $Q = P$. (Honesty is optimal, and
for strictly proper rules uniquely so.)

**Proposition (log loss is strictly proper).** For $\ell(Q, y) = \log 1/Q_y$,

$$ L(P, Q) = \sum_i P_i \log \frac{1}{Q_i} = H(P, Q)
   \;\overset{(\text{Thm 4})}{=}\; H(P) + D(P \,\Vert\, Q)
   \;\overset{(\text{Thm 2})}{\geq}\; H(P) = L(P, P), $$

with equality iff $D(P \Vert Q) = 0$ iff $Q = P$. **End of proof.** This is the
mismatch theorem (Theorem 1) in its third costume: the cost of the lie is
exactly $D(P \Vert Q)$.

### 6.4 Linear is not proper, Brier is proper, and locality singles out the log

**Linear loss is not proper.** With $\ell(Q, y) = 1 - Q_y$,

$$ L(P, Q) = \sum_i P_i (1 - Q_i) = 1 - \sum_i P_i Q_i, $$

which is *linear* in $Q$ on the simplex, hence minimized at a vertex: $Q$ one-
hot on $\arg\max_i P_i$, with value $1 - \max_i P_i$. Unless $P$ is itself one-
hot, this beats $L(P, P) = 1 - \sum_i P_i^2$, so honesty loses. For $P = (0.7,
0.2, 0.1)$: honest $Q = P$ scores $1 - (0.49 + 0.04 + 0.01) = 0.460$; all-in $Q
= (1, 0, 0)$ scores $0.300$.

**Brier score is strictly proper.** With $\ell(Q, i) = \sum_j (Q_j -
\mathbb{1}[j = i])^2 = \sum_j Q_j^2 - 2 Q_i + 1$,

$$ L(P, Q) = \sum_i P_i \Bigl(\sum_j Q_j^2 - 2 Q_i + 1\Bigr)
   = \sum_j Q_j^2 - 2 \sum_j P_j Q_j + 1
   \;\overset{(\pm \sum_j P_j^2)}{=}\; \sum_j (Q_j - P_j)^2 + \Bigl(1 - \sum_j P_j^2\Bigr), $$

and $1 - \sum_j P_j^2 = \sum_j P_j (1 - P_j)$ since $\sum_j P_j = 1$. The first
sum is $\geq 0$ with equality iff $Q = P$; the second is $P$-only. Hence
strictly proper. **End of proof.** For $P = (0.7, 0.2, 0.1)$, $\sum_j P_j(1-P_j)
= 0.21 + 0.16 + 0.09 = 0.460$: $Q = P$ scores $0.460$; $Q = (1,0,0)$ adds $0.3^2
+ 0.2^2 + 0.1^2 = 0.14$ and scores $0.600$.

**The three scores compared.** Truth $P = (0.7, 0.2, 0.1)$; expected loss $L(P,
Q)$, log in bits:

| report $Q$ | log | linear | Brier |
|---|---|---|---|
| $P = (0.7, 0.2, 0.1)$ | $H(P) = 1.157$ | $0.460$ | $0.460$ |
| one-hot $(1, 0, 0)$ | $+\infty$ | $0.300$ | $0.600$ |
| uniform $(\tfrac13, \tfrac13, \tfrac13)$ | $\log 3 = 1.585$ | $0.667$ | $0.667$ |

($H(0.7, 0.2, 0.1) = 0.7 \log \tfrac{1}{0.7} + 0.2 \log 5 + 0.1 \log 10 \approx
0.3602 + 0.4644 + 0.3322 = 1.1568$; uniform Brier: $(\tfrac13 - 0.7)^2 +
(\tfrac13 - 0.2)^2 + (\tfrac13 - 0.1)^2 + 0.46 = 0.2067 + 0.46 = 0.6667$.) Only
the linear loss prefers the lie; both log and Brier put the honest report at the
top of their columns.

**Locality, and why the log.** Both log and Brier are strictly proper, so
properness alone does not force the logarithm. The distinguishing property is
*locality*: the log loss reads only $Q_y$, the mass on the outcome that
happened; the Brier score reads every coordinate, so its penalty depends on how
the remaining mass is spread among outcomes that did not occur. The classical
theorem: for $M \geq 3$ outcomes, the only (suitably regular) strictly proper
scoring rules that depend on $Q$ only through $Q_y$ are the affine transforms of
the log score, $a \log Q_y + b$ with $a > 0$.

**Flag.** This uniqueness theorem is *stated, not proved* here.
References: Bernardo [11] (the characterization of the logarithmic score as the
unique smooth, local, proper score), and the survey of Gneiting & Raftery [12].
The restriction $M \geq 3$ is genuine: for $M = 2$ every scoring rule is
trivially local, since $Q_2 = 1 - Q_1$, and the (proper) Brier score is then a
counterexample to uniqueness. Strictly proper + local = log loss: the reciprocal
and the logarithm in $\log 1/Q_y$ are forced, not chosen.

### 6.5 One-hot labels are pmfs; Theorem 9

**Definition (one-hot vector).** For $y \in [M]$, the one-hot vector
$y^{(o)} \in \mathbb{R}^{M}$ has coordinates $y^{(o)}_i = 1$ if $i = y$ and
$y^{(o)}_i = 0$ otherwise. It is a valid pmf on $[M]$: the ground-truth
distribution, deterministic at $y$, with $H(y^{(o)}) = 0$.

Both the label and the prediction are now pmfs on $[M]$, so their KL divergence
is a natural performance measure, and it turns out to *be* the loss.

**Theorem 9 (the cross-entropy loss is a KL divergence).**

$$ \ell(f(x), y) = D(y^{(o)} \Vert f(x)). $$

*Proof.* Expand the definition and use the convention $0 \log \frac{0}{q} = 0$
from Section 4.1 on every coordinate $i \neq y$, where $y^{(o)}_i = 0$:

$$ D(y^{(o)} \Vert f(x)) = \sum_{i=1}^{M} y^{(o)}_i \log \frac{y^{(o)}_i}{f(x)_i}
   = 1 \cdot \log \frac{1}{f(x)_y} = \ell(f(x), y). $$

Exactly one term survives, the true label's surprisal. The absolute-continuity
requirement of Section 4.1 here reads $f(x)_y > 0$; softmax guarantees it, and
both sides equal $+\infty$ otherwise, so the identity holds in all cases.
**End of proof.**

Mind the argument order: the truth sits in the *first* slot,
$D(\text{truth} \Vert \text{model})$. That is the direction in which zeros of the
model are punished infinitely (Section 4.2), which is the behavior a loss should
have. The reverse direction $D(f(x) \Vert y^{(o)})$ would be $+\infty$ whenever
the model hedges at all, that is whenever $f(x)_i > 0$ for some $i \neq y$, which
is useless as a loss.

### 6.6 Soft labels: the same story via Theorem 4

Theorem 4 applied to a label distribution $P$ (one-hot or not) and the
prediction $Q = f(x)$ reads $H(P, f(x)) = H(P) + D(P \Vert f(x))$. Two
specializations:

- **One-hot label:** $H(y^{(o)}) = 0$, so $H\bigl(y^{(o)}, f(x)\bigr) =
  D\bigl(y^{(o)} \Vert f(x)\bigr)$, cross-entropy and KL *coincide*, and both
  equal the loss of Theorem 9. This is why the loss is legitimately called
  either name.

- **Soft label** $y^{(\text{soft})}$ (label smoothing [6], distillation [7];
  Section 7.3): now

$$ D\bigl(y^{(\text{soft})} \,\Vert\, f(x)\bigr)
   = H\bigl(y^{(\text{soft})}, f(x)\bigr) - H\bigl(y^{(\text{soft})}\bigr), $$

so CE and KL differ by the constant $H(y^{(\text{soft})})$, fixed by the data.
Training on either gives the same gradients.

**Soft-label numbers.** With $y^{(\text{soft})} = (0.6, 0.3, 0.1)$ and
$f(x) = (0.7, 0.2, 0.1)$:

$$ H(y^{(\text{soft})}, f(x))
   = 0.6 \log \tfrac{1}{0.7} + 0.3 \log \tfrac{1}{0.2} + 0.1 \log \tfrac{1}{0.1}
   \approx 0.3087 + 0.6966 + 0.3322 \approx 1.3375 \text{ bits}, $$

$$ H(y^{(\text{soft})})
   = 0.6 \log \tfrac{1}{0.6} + 0.3 \log \tfrac{1}{0.3} + 0.1 \log \tfrac{1}{0.1}
   \approx 0.4422 + 0.5211 + 0.3322 \approx 1.2955 \text{ bits}, $$

$$ D(y^{(\text{soft})} \Vert f(x))
   = 0.6 \log \tfrac{0.6}{0.7} + 0.3 \log \tfrac{0.3}{0.2}
   + 0.1 \log \tfrac{0.1}{0.1}
   \approx -0.1334 + 0.1755 + 0 \approx 0.0421 \text{ bits}. $$

Indeed $1.3375 = 1.2955 + 0.0421$ up to rounding. Note again a negative
individual KL term.

### 6.7 Punchline: minimizing cross-entropy is minimizing KL

Fix the label distribution $P$, one-hot or soft, and optimize the model
$Q = f(x)$. Since $H(P)$ contains no $Q$,

$$ \arg\min_{Q} H(P, Q) = \arg\min_{Q} [H(P) + D(P \Vert Q)]
   = \arg\min_{Q} D(P \Vert Q), $$

and by Theorem 2 the common minimizer is $Q = P$, where $D = 0$ and
cross-entropy attains its floor $H(P)$, which is Theorem 1 again.

So training with cross-entropy loss *is* pulling the model's pmf toward the label
distribution, with disagreement measured in KL. Three details.

- **Achievability of zero loss.** For a one-hot label, zero loss requires
  $f(x) = y^{(o)}$ exactly. A softmax over finite logits outputs strictly
  positive coordinates, so it can approach but never reach zero loss: the
  infimum is 0 and is not attained. This is one practical motivation for label
  smoothing, whose smoothed target lies in the interior of the simplex and *is*
  attainable.
- **Base and scale invariance.** Changing the logarithm base multiplies the loss
  by a positive constant (bits against nats, Section 1); adding the constant
  $H(P)$ or not is the difference between cross-entropy and KL. Neither changes
  the argmin, so PyTorch's nat-based cross-entropy, the bit-based formulas here,
  and "KL to the label" all train identically.
- **Why the logarithm and the reciprocal, answer assembled.**
  $\log \frac{1}{Q}$ is not an arbitrary decreasing function. It is the
  surprisal: the unique pricing, up to the base, under which the true
  distribution is the cheapest model (Theorem 1), wrong beliefs bleed wealth at
  rate $D$ (Theorems 7 and 8), it is the unique local strictly proper score
  (Section 6.4, cited), and the loss of a classifier is exactly the divergence
  to the truth (Theorem 9). The alternatives $1 - f(x)_y$ and the Brier score
  admit no KL identity: the Brier score decomposes into a squared Euclidean
  distance plus a $P$-only constant (Section 6.4), the linear loss into nothing
  useful, and, unlike the logarithm, both assign a *finite* penalty to declaring
  the truth impossible.

**Partly left open.** Why measure disagreement between pmfs by *this* divergence
rather than another ($\chi^2$, total variation, Wasserstein, ...)? Section 4.11
lists what KL alone brings among the $f$-divergences (additivity, the cross-
entropy decomposition, the surprisal integrand) but proves no uniqueness
theorem; Section 7.4 collects what remains open. KL's role as the exponent in
large-deviation and hypothesis-testing limits is developed later in the course;
see [1, Ch. 2, 11] and [2] for the classical answers.

### 6.8 Population view: Theorem 10 and the Bayes-optimal classifier

So far one sample. Let the data be a random pair $(X, Y) \sim P_{XY}$ with $Y
\in [M]$, write $P_{Y \mid X = x}$ for the true conditional pmf of the label
given the input, and let a classifier $f$ map each $x$ to a pmf $f(x)$ on $[M]$.
Its *risk* is the expected loss $R(f) = \mathbb{E}\bigl[\ell(f(X), Y)\bigr]$.

**Theorem 10 (population decomposition).** If $f(x)_y > 0$ whenever $P(y \mid x)
> 0$ (softmax guarantees this),

$$ R(f) \;=\; \underbrace{\mathbb{E}_X\bigl[H(P_{Y \mid X})\bigr]}_{\text{irreducible}}
   \;+\; \underbrace{\mathbb{E}_X\bigl[D(P_{Y \mid X} \,\Vert\, f(X))\bigr]}_{\geq 0,\ \text{the model's fault}}. $$

**Proof.** Condition on $X$ (the tower property of expectation) and expand the
inner expectation by LOTUS over $Y \sim P_{Y \mid X}$:

$$ R(f) = \mathbb{E}_X\Bigl[\mathbb{E}\bigl[\ell(f(X), Y) \,\big|\, X\bigr]\Bigr]
   = \mathbb{E}_X\Bigl[\sum_{y} P(y \mid X) \log \frac{1}{f(X)_y}\Bigr]
   = \mathbb{E}_X\bigl[H(P_{Y \mid X},\, f(X))\bigr]. $$

For each fixed $x$ this is a cross-entropy between the true conditional and the
prediction, so Theorem 4 applies pointwise: $H(P_{Y \mid X = x}, f(x)) = H(P_{Y
\mid X = x}) + D(P_{Y \mid X = x} \Vert f(x))$. Take $\mathbb{E}_X$ of both
sides. **End of proof.**

The first term depends on the data only; prob03 names it the conditional entropy
$H(Y \mid X)$. It is the loss floor: zero training loss is *not* the goal when
$H(P_{Y \mid X}) > 0$, i.e. when the label is genuinely uncertain given the
input.

**Corollary (Bayes-optimal classifier).** $R(f)$ is minimized iff $D(P_{Y \mid
X} \Vert f(X)) = 0$ almost surely, i.e. iff $f(x) = P(Y = \cdot \mid X = x)$ for
($P_X$-almost) every $x$; the minimum risk is $\mathbb{E}_X[H(P_{Y \mid X})]$.

**Proof.** The second term of Theorem 10 is an expectation of a non-negative
quantity (Theorem 2), so it is $\geq 0$ with equality iff the quantity is $0$
a.s., and $D(P_{Y \mid X = x} \Vert f(x)) = 0$ iff $f(x) = P_{Y \mid X = x}$
(Theorem 2 again). **End of proof.**

Two readings. First, one-hot training labels are *samples* from $P_{Y \mid X}$,
not the conditional pmf itself; the population risk nevertheless recovers the
conditional pmf, so CE training targets $P(Y \mid X)$ even though no training
example ever shows a probability. Second, CE-trained outputs are therefore meant
to be *calibrated probabilities*, not merely argmax scores: the loss charges
confidence errors even when the argmax is right.

**Worked example, verified.** One input $x$ with $P(Y = 1 \mid x) = 0.7$, so the
floor is $h_2(0.7) = 0.7 \log \tfrac{1}{0.7} + 0.3 \log \tfrac{1}{0.3} \approx
0.3602 + 0.5211 = 0.8813$ bits:

| prediction $f(x)$ | risk at $x$ (bits) | KL term |
|---|---|---|
| $(0.7, 0.3)$ calibrated | $0.881$ | $0$ |
| $(0.95, 0.05)$ overconfident | $0.7 \log \tfrac{1}{0.95} + 0.3 \log \tfrac{1}{0.05} \approx 0.0518 + 1.2966 = 1.348$ | $0.467$ |
| $(0.5, 0.5)$ hedged | $0.7 + 0.3 = 1.000$ | $0.119$ |

Right argmax, wrong confidence: the overconfident model pays $0.467$ bits above
the floor, more than the fully hedged one ($0.119$).

### 6.9 Maximum likelihood = minimum cross-entropy = minimum KL

Samples $x_1, \dots, x_n \overset{\text{iid}}{\sim} P$; the *empirical pmf* is
$\hat P_n(x) = \tfrac{1}{n} \#\{i : x_i = x\}$. For a model $Q$, the negative
average log-likelihood is

$$ \frac{1}{n} \sum_{i=1}^{n} \log \frac{1}{Q(x_i)}
   \;\overset{(\text{group equal } x_i)}{=}\; \sum_{x} \hat P_n(x) \log \frac{1}{Q(x)}
   = H(\hat P_n, Q)
   \;\overset{(\text{Thm 4})}{=}\; H(\hat P_n) + D(\hat P_n \,\Vert\, Q). $$

Left side: maximum likelihood is minimum cross-entropy against the empirical
pmf. Right side: $H(\hat P_n)$ is data-only, so maximum likelihood is minimum KL
*from the data* to the model, $\arg\min_Q D(\hat P_n \Vert Q)$. (The first
equality needs $Q(x_i) > 0$ for every observed $x_i$, i.e. $\operatorname{supp}
\hat P_n \subseteq \operatorname{supp} Q$; otherwise the likelihood is $0$ and
both sides are $+\infty$.) Section 4.9 adds the large-$n$ reading: $\tfrac1n
\sum_i \log \tfrac{P(x_i)}{Q(x_i)} \rightarrow D(P \Vert Q)$, so with enough
data the MLE objective converges to the population KL, up to the $Q$-free
entropy term.

### 6.10 Softmax, the gradient (Theorem 11), log-sum-exp, and why not squared error

**Definition (softmax).** For logits $z \in \mathbb{R}^M$,

$$ s_i(z) = \frac{e^{z_i}}{\sum_{j=1}^{M} e^{z_j}}, \qquad s_i(z) > 0, \quad \sum_i s_i(z) = 1. $$

The cross-entropy loss on logits, in nats, as `nn.CrossEntropyLoss` computes it:
$\ell(z, y) = -\ln s_y(z) = -z_y + \ln \sum_j e^{z_j}$.

**Theorem 11 (gradient of CE on logits).**

$$ \frac{\partial \ell(z, y)}{\partial z_i} = s_i(z) - \mathbb{1}[i = y]. $$

**Proof.** $\tfrac{\partial}{\partial z_i}(-z_y) = -\mathbb{1}[i = y]$, and
$\tfrac{\partial}{\partial z_i} \ln \sum_j e^{z_j} = \tfrac{e^{z_i}}{\sum_j
e^{z_j}} = s_i(z)$ by the chain rule. Add. **End of proof.**

The gradient is the predicted pmf minus the one-hot truth: a *residual*, with
entries summing to $\sum_i s_i - 1 = 0$, and it never saturates, the true-label
entry is $s_y - 1 \in (-1, 0)$, largest in magnitude exactly when the model is
most wrong. Example: $z = (2, 1, 0)$, $y = 1$: $s = (0.6652, 0.2447, 0.0900)$,
loss $-\ln 0.6652 = 0.4076$ nats, gradient $(-0.3348, 0.2447, 0.0900)$. Working
in bits instead of nats multiplies loss and gradient by $1/\ln 2 \approx
1.4427$.

**Why logits: log-sum-exp stability.** Computing probabilities first and taking
the log second fails numerically: $e^{1000}$ overflows a double (Python raises
`OverflowError: math range error`). The identity

$$ \ln \sum_j e^{z_j} = m + \ln \sum_j e^{z_j - m}, \qquad m = \max_j z_j, $$

(pull $e^{m}$ out of the sum) makes every exponent $\leq 0$, so nothing
overflows and at least one term equals $1$, so nothing underflows to $\ln 0$.
For $z = (1000, 0, 0)$: $1000 + \ln(1 + 2e^{-1000}) = 1000.0$ in floating point.

This is why `nn.CrossEntropyLoss(logits, y)` takes raw logits, not
probabilities: it applies log-softmax internally via this identity. Its output
is in nats; divide by $\ln 2 \approx 0.6931$ for bits.

**Why not squared error on the softmax output?** Differentiating $s_y$ with
respect to its own logit (from the quotient rule, or from Theorem 11's
calculation) gives $\partial s_y / \partial z_y = s_y (1 - s_y)$. Any loss
written as a function of $s_y$ inherits this factor by the chain rule, e.g. for
$(1 - s_y)^2$ the gradient in $z_y$ is $-2(1 - s_y)\, s_y (1 - s_y)$. Cross-
entropy's $-\ln s_y$ contributes $-1/s_y$, which *cancels* the $s_y$ and leaves
$s_y - 1$ (Theorem 11).

| $s_y$ (mass on truth) | CE gradient $s_y - 1$ | softmax factor $s_y(1 - s_y)$ |
|---|---|---|
| $0.001$ (confidently wrong) | $-0.999$ | $0.001$ |
| $0.5$ | $-0.5$ | $0.25$ |
| $0.9$ | $-0.1$ | $0.09$ |

Squared error on softmax outputs learns slowest exactly when the model is most
wrong (the factor is $0.001$ at $s_y = 0.001$); cross-entropy's gradient is
largest there. This is the optimization-side reason for the log, complementing
the statistical ones.

**Why log, settled.** The four answers of this lecture: $\log 1/Q$ is
*surprisal*, the guessing, coding and betting cost (Theorems 1, 7, 8); it is the
only strictly proper *local* score (Section 6.4, cited); its population
minimizer is the true conditional $P(Y \mid X)$ (Theorem 10); and its gradient
on logits is the residual $s - y^{(o)}$, computed stably (Theorem 11). Cross-
entropy loss is KL in disguise, not an arbitrary choice.

## 7. KL Across Deep Learning

### 7.1 Forward vs reverse: the support argument

Section 4.2 showed the two directions can differ wildly. Fitting a model $Q$ to
a target $P$, the two choices fail in opposite ways (Minka [13]):

- **Forward** $D(P \Vert Q) = \sum_x P(x) \log \tfrac{P(x)}{Q(x)}$: wherever
  $P(x) > 0$ and $Q(x) \approx 0$ the term explodes (Section 4.1: $+\infty$ at
  $Q(x) = 0$). So $Q$ must cover everything $P$ allows, *zero-avoiding, mode-
  covering*. This is the direction of MLE and CE training (Sections 6.8-6.9).

- **Reverse** $D(Q \Vert P) = \sum_x Q(x) \log \tfrac{Q(x)}{P(x)}$: wherever
  $P(x) \approx 0$, $Q(x)$ must be $\approx 0$ too or the term explodes; but
  where $P(x) > 0$ and $Q(x) = 0$ the term is $0$ by convention. So $Q$ may drop
  modes of $P$ for free, *zero-forcing, mode-seeking*.

**A two-Gaussian example (numerical experiment, not a theorem, flag).**
Target $P = \tfrac12 \mathcal{N}(-2, 0.5^2) + \tfrac12 \mathcal{N}(2, 0.5^2)$
and candidates $Q = \mathcal{N}(\mu, \sigma^2)$, both discretized on the grid $x
\in \{-6, -5.75, \dots, 6\}$ ($49$ points) and normalized to pmfs, so that the
discrete theory of Section 4 applies verbatim. Grid search over $\mu \in [-4,
4]$ (step $0.1$) and $\sigma \in [0.2, 4]$ (step $0.05$), KL in nats:

- Forward $\min_{\mu,\sigma} D(P \Vert Q) = 0.7204$ nats at $\mu = 0$, $\sigma =
  2.10$: one wide Gaussian straddling both bumps, mass in the empty valley. (The
  moment-matched $\sigma$ is $2.0616$; the objective is flat there: $0.7208$ at
  $\sigma = 2.05$, $0.7209$ at $2.15$.)

- Reverse $\min_{\mu,\sigma} D(Q \Vert P) = 0.6931$ nats at $\mu = 2$, $\sigma =
  0.50$, tied exactly with $\mu = -2$: one bump, the other dropped. The value is
  $\ln 2$ to four decimals, and for a reason: where $Q$ has mass, $P \approx
  \tfrac12 Q$, so $\log \tfrac{Q}{P} \approx \ln 2$ throughout.

- Cross-evaluation: $D(P \Vert Q_{\text{rev}}) = 15.31$ nats (forward KL
  punishes the dropped mode severely) and $D(Q_{\text{fwd}} \Vert P) = 2.03$
  nats (reverse KL punishes the mass in the valley).

The third decimal depends on the discretization; the qualitative picture,
forward covers, reverse seeks, does not. Same two distributions, opposite fits.

### 7.2 The two directions in practice

| direction | objective | where |
|---|---|---|
| forward $D(P_{\text{data}} \Vert Q_\theta)$ | $\min_\theta H(\hat P_n, Q_\theta)$ | MLE; CE training (Theorem 10, Section 6.9) |
| reverse $D(q_\phi \Vert p)$ | $\min_\phi D\bigl(q_\phi(z \mid x) \,\Vert\, p(z \mid x)\bigr)$ | variational inference; VAE encoder [15] |
| reverse $D(\pi \Vert \pi_{\text{ref}})$ | $\max_\pi \mathbb{E}_\pi[r] - \beta\, D(\pi \,\Vert\, \pi_{\text{ref}})$ | RLHF policy penalty [14] |

The practical dividing line: the forward direction is an expectation under $P$,
so it needs *samples* of $P$ (data) and nothing else about $P$; the reverse
direction is an expectation under the model $Q$, so it needs only the ability to
*evaluate* $P$ at the model's own samples, and only up to a multiplicative
constant, since an unknown normalizer $Z$ in $P = \tilde P / Z$ contributes the
additive constant $\ln Z$ to $\mathbb{E}_Q[\log \tfrac{Q}{P}]$, which does not
move the argmin. Posteriors $p(z \mid x) = p(x, z) / p(x)$ are exactly such
unnormalized targets, which is why variational inference is reverse-KL.

### 7.3 The zoo: where the KL/CE term hides

Continuous latent variables appear below; the definitions of Section 4 carry
over with sums replaced by integrals over densities, and Theorem 2 holds by the
same Jensen argument. That extension is used here without a separate proof
(flag).

- **LM pretraining:** $\tfrac{1}{T} \sum_t \log \tfrac{1}{Q(x_t \mid x_{< t})}$
  (Section 5.9). Forward: the data plays $P$.

- **Knowledge distillation** (Hinton et al. [7]): the student is trained toward
  the teacher's softened pmf, $D\bigl(\mathrm{softmax}(z_{\text{teacher}} / T)
  \,\Vert\, \mathrm{softmax}(z_{\text{student}} / T)\bigr)$ at temperature $T$.
  By Theorem 4 this equals the cross-entropy against the soft target minus the
  teacher's entropy, a constant in the student's parameters, so training on
  either is equivalent (Section 6.6). Forward: the teacher plays $P$.

- **Label smoothing** (Szegedy et al. [6]): $H\bigl((1-\varepsilon)\, y^{(o)} +
  \varepsilon / M,\; f(x)\bigr)$. For $\varepsilon = 0.1$, $M = 3$ the target is
  $(0.9 + 0.0333, 0.0333, 0.0333) = (0.9333, 0.0333, 0.0333)$: full support,
  attainable by a softmax (Section 6.7). Forward: the smoothed label plays $P$.

- **RLHF** (Ouyang et al. [14]): the per-sample reward is $r(x, y) - \beta \log
  \tfrac{\pi(y \mid x)}{\pi_{\text{ref}}(y \mid x)}$; taking the expectation
  under the policy's own samples $y \sim \pi(\cdot \mid x)$ gives
  $\mathbb{E}_\pi[r] - \beta\, D(\pi \Vert \pi_{\text{ref}})$, since
  $\mathbb{E}_{y \sim \pi}\bigl[\log \tfrac{\pi}{\pi_{\text{ref}}}\bigr]$ is by
  definition the KL from $\pi$ to $\pi_{\text{ref}}$. Reverse: the model's own
  distribution sits on the left, penalizing the policy for putting mass where
  the reference does not.

- **VAE ELBO** (Kingma & Welling [15]): for an encoder $q(z \mid x)$ and a
  generative model $p(x, z) = p(z)\, p(x \mid z)$,

$$ \log p(x) = \underbrace{\mathbb{E}_{q(z \mid x)}\bigl[\log p(x \mid z)\bigr] - D\bigl(q(z \mid x) \,\Vert\, p(z)\bigr)}_{\text{ELBO}} + D\bigl(q(z \mid x) \,\Vert\, p(z \mid x)\bigr) \;\geq\; \text{ELBO}. $$

**Proof.** Since $\log p(x)$ does not depend on $z$, $\log p(x) =
\mathbb{E}_q[\log p(x)] = \mathbb{E}_q\bigl[\log \tfrac{p(x, z)}{p(z \mid
x)}\bigr] = \mathbb{E}_q\bigl[\log \tfrac{p(x, z)}{q(z \mid x)}\bigr] +
\mathbb{E}_q\bigl[\log \tfrac{q(z \mid x)}{p(z \mid x)}\bigr]$. The second term
is $D(q(z \mid x) \Vert p(z \mid x)) \geq 0$ (Theorem 2). In the first, write
$p(x, z) = p(x \mid z)\, p(z)$: $\mathbb{E}_q[\log p(x \mid z)] +
\mathbb{E}_q\bigl[\log \tfrac{p(z)}{q(z \mid x)}\bigr] = \mathbb{E}_q[\log p(x
\mid z)] - D(q(z \mid x) \Vert p(z))$. **End of proof.**

Maximizing the ELBO over the encoder minimizes the reverse KL $D(q(z \mid x)
\Vert p(z \mid x))$ to the intractable posterior (Section 7.2), and the ELBO's
own KL term $D(q(z \mid x) \Vert p(z))$ is again reverse, the model's $q$ on the
left.

- **Diffusion models:** the training objective is a sum of KL divergences
  between Gaussians, which have a closed form; developed in prob08.

### 7.4 Questions left open

- Is KL the only $f$-divergence that is additive over independent samples
  (Section 4.11)? No uniqueness theorem was stated or proved.

- Locality forces the log for $M \geq 3$ (Section 6.4): cited [11], [12], not
  proved.

- GAN training is a divergence *game*: in the original formulation of Goodfellow
  et al. [16] the optimal discriminator turns the generator's objective into
  $2\,\mathrm{JS}(P_{\text{data}} \Vert Q_\theta) - \log 4$, the Jensen-Shannon
  divergence of the zoo (Section 4.10). Another $f$, same Jensen proof of non-
  negativity.

The definitions of this lecture keep earning their keep: joint and conditional
entropy and mutual information (prob03) are all expressible as KL divergences of
the right pairs.

## 8. References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 2 covers relative entropy, the
   information inequality, the log-sum inequality and convexity of $D$;
   Chapter 5 covers the Kraft inequality and the Shannon code; Chapter 6 covers gambling
   and the doubling rate, and is the horse-race treatment followed here.
2. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System
   Technical Journal*, vol. 27, pp. 379-423 and 623-656, 1948. DOI
   10.1002/j.1538-7305.1948.tb01338.x
   (https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). Entropy and surprisal.
3. S. Kullback and R. A. Leibler, "On Information and Sufficiency," *Annals of
   Mathematical Statistics*, vol. 22, no. 1, pp. 79-86, 1951. DOI
   10.1214/aoms/1177729694 (https://doi.org/10.1214/aoms/1177729694). Origin of
   the KL divergence.
4. J. L. Kelly, Jr., "A New Interpretation of Information Rate," *Bell System
   Technical Journal*, vol. 35, no. 4, pp. 917-926, 1956. DOI
   10.1002/j.1538-7305.1956.tb03809.x
   (https://doi.org/10.1002/j.1538-7305.1956.tb03809.x). Log-optimal
   proportional betting and the growth-rate criterion of Section 5.
5. J. L. W. V. Jensen, "Sur les fonctions convexes et les inegalites entre les
   valeurs moyennes," *Acta Mathematica*, vol. 30, pp. 175-193, 1906. DOI
   10.1007/BF02418571 (https://doi.org/10.1007/BF02418571). Jensen's inequality,
   proved by induction in the Lecture 1 note.
6. C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens and Z. Wojna, "Rethinking the
   Inception Architecture for Computer Vision," CVPR 2016. arXiv:1512.00567
   (https://arxiv.org/abs/1512.00567). Label smoothing.
7. G. Hinton, O. Vinyals and J. Dean, "Distilling the Knowledge in a Neural
   Network," NeurIPS 2014 Deep Learning Workshop. arXiv:1503.02531
   (https://arxiv.org/abs/1503.02531). Knowledge distillation: training against
   a teacher's soft labels.
8. D. J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*,
   Cambridge University Press, 2003. Free online at
   https://www.inference.org.uk/mackay/itila/. A gentler parallel treatment of
   relative entropy and Gibbs' inequality.
9. I. Csiszar, "Information-type measures of difference of probability
   distributions and indirect observation," *Studia Scientiarum Mathematicarum
   Hungarica*, vol. 2, pp. 299-318, 1967. (Origin of $f$-divergences, with [10].
   No stable online copy was located when these notes were revised; cited from
   the secondary literature.)
10. S. M. Ali and S. D. Silvey, "A General Class of Coefficients of Divergence
   of One Distribution from Another," *Journal of the Royal Statistical Society,
   Series B*, vol. 28, no. 1, pp. 131-142, 1966. DOI:
   https://doi.org/10.1111/j.2517-6161.1966.tb00626.x. (Independent origin of
   $f$-divergences.)
11. J. M. Bernardo, "Expected Information as Expected Utility," *The Annals of
   Statistics*, vol. 7, no. 3, 1979. DOI:
   https://doi.org/10.1214/aos/1176344689. (Characterization of the logarithmic
   score as the unique smooth, local, proper scoring rule; Section 6.4.)
12. T. Gneiting and A. E. Raftery, "Strictly Proper Scoring Rules, Prediction,
   and Estimation," *Journal of the American Statistical Association*, vol. 102,
   no. 477, pp. 359-378, 2007. DOI: https://doi.org/10.1198/016214506000001437.
   (Survey of proper scoring rules, including the log, Brier and locality
   results of Section 6.4.)
13. T. Minka, "Divergence Measures and Message Passing," Microsoft Research
   Technical Report MSR-TR-2005-173, 2005. https://www.microsoft.com/en-
   us/research/publication/divergence-measures-and-message-passing/. (Forward vs
   reverse KL, zero-avoiding vs zero-forcing; Section 7.1.)
14. L. Ouyang et al., "Training language models to follow instructions with
   human feedback," NeurIPS 2022. arXiv: https://arxiv.org/abs/2203.02155. (The
   RLHF objective with a per-token KL penalty to the reference policy; Section
   7.3.)
15. D. P. Kingma and M. Welling, "Auto-Encoding Variational Bayes," ICLR 2014.
   arXiv: https://arxiv.org/abs/1312.6114. (The variational autoencoder and the
   ELBO; Section 7.3.)
16. I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S.
   Ozair, A. Courville, Y. Bengio, "Generative Adversarial Networks," NeurIPS
   2014. arXiv: https://arxiv.org/abs/1406.2661. (The minimax game whose
   optimal-discriminator value is a Jensen-Shannon divergence; Section 7.4.)
