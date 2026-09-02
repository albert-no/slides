# Deep Learning Math, Lecture 2: KL Divergence and Cross-Entropy Loss

**About this file.** Screen-reader edition of the Lecture 2 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob02-kl-crossentropy-note.html`). Nothing else is needed to
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
5. Gambling and the doubling rate
6. Cross-entropy loss
7. References

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

**Alternative self-contained proof via the log-sum inequality.** The following
lemma handles all zero-mass edge cases at once and recurs throughout information
theory [1, Thm 2.7.1].

**Lemma (log-sum inequality).** For non-negative numbers $a_1, \dots, a_n$ and
$b_1, \dots, b_n$, with $a = \sum_i a_i$ and $b = \sum_i b_i$,

$$ \sum_{i=1}^{n} a_i \log \frac{a_i}{b_i} \geq a \log \frac{a}{b}, $$

with the conventions of Section 4.1, and with equality if and only if the ratio
$a_i / b_i$ is the same for all $i$ with $b_i > 0$.

*Proof.* If some $b_i = 0$ with $a_i > 0$, the left side is $+\infty$. Discard
indices with $a_i = b_i = 0$, so assume all $b_i > 0$. The function
$f(t) = t \log t$ is strictly convex on $[0,\infty)$, since for $t > 0$ we have
$f''(t) = 1/(t \ln 2) > 0$. Apply Jensen for convex functions with weights
$b_i / b$ to the points $t_i = a_i / b_i$:

$$ \sum_i \frac{b_i}{b} f\left(\frac{a_i}{b_i}\right)
   \geq f\left(\sum_i \frac{b_i}{b} \cdot \frac{a_i}{b_i}\right)
   = f\left(\frac{a}{b}\right). $$

Multiplying both sides by $b$ gives the claim, and strict convexity makes Jensen
tight if and only if all $t_i$ coincide. **End of proof.**

Now take $a_i = P(x_i)$ and $b_i = Q(x_i)$ over all of $\mathcal{X}$. Then
$a = b = 1$, so $D(P \Vert Q) \geq 1 \cdot \log \frac{1}{1} = 0$, with equality
if and only if $P(x)/Q(x)$ is constant, which, since both sum to 1, forces
$P = Q$.

### 4.5 The gap, named: cross-entropy equals entropy plus KL

Split the logarithm inside the cross-entropy sum; each term is finite or
$+\infty$ consistently, by the conventions:

$$ H(P, Q) = \sum_x P(x) \log \frac{1}{Q(x)}
   = \sum_x P(x) \log \left(\frac{1}{P(x)} \cdot \frac{P(x)}{Q(x)}\right), $$

$$ H(P, Q) = \sum_x P(x) \log \frac{1}{P(x)}
   + \sum_x P(x) \log \frac{P(x)}{Q(x)}
   = H(P) + D(P \Vert Q). $$

So the mismatch overpayment *is* the KL divergence. The identity reappears as
Theorem 6 in Section 6.4. In the example of Section 3.2,
$D(P \Vert Q) = 0.1837 - 0.0808 \approx 0.103$ bits.

## 5. Gambling and the Doubling Rate

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

### 5.4 Theorem 3: proportional betting, binary case

**Theorem 3 (proportional betting).** In the binary game with odds 2 and
$0 < p < 1$, the objective $\mathbb{E}[\log S]$ is maximized over $q \in [0,1]$
uniquely at $q = p$, and

$$ \max_q \mathbb{E}[\log S] = \log 2B - h_2(p), $$

where $h_2(p) = p \log \frac{1}{p} + (1-p) \log \frac{1}{1-p}$ is the binary
entropy function. Moreover, for any $q$,

$$ \mathbb{E}[\log S_{\text{opt}}] - \mathbb{E}[\log S_q]
   = D((p, 1-p) \Vert (q, 1-q)). $$

*Proof.* Apply the decomposition $H(P,Q) = H(P) + D(P \Vert Q)$ of Section 4.5 to
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
third costume of the same quantity, after guessing bills and, in Cover and Thomas
Chapter 5, code lengths. The log-optimal criterion is due to Kelly [4], whose
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

### 5.6 Theorem 4: horse racing

Generalize to $M$ horses. Horse $i$ wins with probability $p_X(i)$; the odds are
$M$-for-1 on every horse, that is, uniform fair odds; the gambler splits the
budget as $(Q(1)B, \dots, Q(M)B)$ where $Q$ is a pmf. Winner takes all: if horse
$i$ wins then $S = M Q(i) B$.

**Theorem 4 (proportional betting, $M$ horses).**

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

Apply $H(p_X, Q) = H(p_X) + D(p_X \Vert Q)$ from Section 4.5; only $D$ depends on
$Q$, and Theorem 2 finishes as before. **End of proof.**

Theorem 3 is the case $M = 2$. Note that $W^{*} = \log M - H(p_X)$ can be
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
a gambler betting a pmf on the outcome, and the next section charges it the same
penalty.

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

### 6.3 One-hot labels are pmfs; Theorem 5

**Definition (one-hot vector).** For $y \in [M]$, the one-hot vector
$y^{(o)} \in \mathbb{R}^{M}$ has coordinates $y^{(o)}_i = 1$ if $i = y$ and
$y^{(o)}_i = 0$ otherwise. It is a valid pmf on $[M]$: the ground-truth
distribution, deterministic at $y$, with $H(y^{(o)}) = 0$.

Both the label and the prediction are now pmfs on $[M]$, so their KL divergence
is a natural performance measure, and it turns out to *be* the loss.

**Theorem 5 (the cross-entropy loss is a KL divergence).**

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

### 6.4 Theorem 6: the decomposition, and soft labels

**Theorem 6 (cross-entropy decomposition).** For any pmfs $P$ and $Q$ on $[M]$,
with the usual conventions and both sides possibly $+\infty$ together,

$$ H(P, Q) = H(P) + D(P \Vert Q). $$

*Proof.* Split the log-ratio inside $D$, over the support of $P$, where zero-mass
terms vanish on both sides:

$$ D(P \Vert Q) = \sum_i P(i) \log \frac{P(i)}{Q(i)}
   = \sum_i P(i) \log P(i) + \sum_i P(i) \log \frac{1}{Q(i)}, $$

and the first sum is $-H(P)$ while the second is $H(P,Q)$. So
$D = -H(P) + H(P,Q)$; rearranging gives the claim. **End of proof.**

This is the identity already derived in Section 4.5. (The source scribe notes
drop a factor $p_X(x)$ in one intermediate line of this derivation, a typo; the
computation above is the corrected one.)

Two specializations.

- **One-hot label.** $H(y^{(o)}) = 0$, so
  $H(y^{(o)}, f(x)) = D(y^{(o)} \Vert f(x))$: cross-entropy and KL *coincide*,
  and both equal the loss of Theorem 5. This is why the loss is legitimately
  called either name.
- **Soft label** $y^{(\text{soft})}$, as in label smoothing [6] and distillation
  [7]:

$$ D(y^{(\text{soft})} \Vert f(x))
   = H(y^{(\text{soft})}, f(x)) - H(y^{(\text{soft})}), $$

  so cross-entropy and KL differ by the constant $H(y^{(\text{soft})})$, fixed by
  the data.

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

### 6.5 Punchline: minimizing cross-entropy is minimizing KL

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
  rate $D$ (Theorems 3 and 4), and the loss of a classifier is exactly the
  divergence to the truth (Theorem 5). The alternatives $1 - f(x)_y$ and
  $(1 - f(x)_y)^{2}$ admit no such identity, and, unlike the logarithm, they
  assign a *finite* penalty to declaring the truth impossible.

**Left open, deliberately.** Why measure disagreement between pmfs by *this*
divergence rather than another, such as chi-squared, total variation, or
Wasserstein? KL's privileges, namely the chain rule, its role as the exponent in
large-deviation and hypothesis-testing limits, and its appearance in GAN training
as a relative of the Jensen-Shannon divergence game, are developed later in the
course; see [1, Ch. 2 and 11] and [2] for the classical answers.

## 7. References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 2 covers relative entropy, the
   information inequality and the log-sum inequality; Chapter 6 covers gambling
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
