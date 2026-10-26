# Deep Learning Math, Midterm Review: Tools for Seeing (Notes)

**About this file.** Companion note to the midterm review lecture for the
2026 midterm (exam of October 20, 2026). It holds what the lecture states
briefly or skips: every solution written out in full sentences, the
derivations the slides compress into one line, the general formulas behind the
plotted curves, and a re-derivation of every number on the slides. The
Markdown edition (`midterm26-review-note.md`) is the screen-reader version:
linear reading order, all mathematics in LaTeX, tables written as lists. The
HTML note (`midterm26-review-note.html`) has the same text and section numbers.

**Conventions.** As in the exam, entropy $H$ and mutual information $I$ are in
bits: $\log$ is base 2 and $\ln$ is the natural logarithm. $h(\cdot)$ is
differential entropy. $\mathrm{Bern}(p)$ is the Bernoulli distribution,
$\mathrm{Bin}(k, p)$ the binomial, $\mathrm{Unif}$ the uniform distribution.
$D(p\|q) = \sum_k p_k \log (p_k / q_k)$ is the KL divergence and
$H_2(p) = -p\log p - (1-p)\log(1-p)$ the binary entropy function.

**Contents.**

1. Why learn mathematical tools
2. Problem 1(a): where n coin flips hide their bits
3. Problem 1(b): does mixing add uncertainty
4. Problem 1(c): noisy labels
5. Problem 1(d): shuffling by moving the top card
6. Problem 2: label smoothing versus confidence penalty
7. Problem 3: heavy tails and the median of means
8. What we expect from you
9. References

## 1 Why learn mathematical tools

### 1.1 Tools serve understanding

Mathematics hands us tools; the tools let us understand what we see. The loop
the lecture opens with has three steps: learn a tool (a new mathematical idea),
apply it to a phenomenon, and see the phenomenon clearly enough to explain,
predict or decide. A sharper question then calls for the next tool, and the
loop starts again. The goal of an exam problem is therefore not the
computation itself but the better view of the phenomenon that the computation
buys.

This course is one turn of that loop. Entropy, mutual information, KL
divergence and the tail inequalities are the tools of this course. Later
courses will add many more, and after graduation you will meet tools that do
not exist yet. The habit to build is the same every time: learn the tool, then
use it to understand and see the world.

### 1.2 Two layers

The course has two layers.

- The bottom layer is the tools you must be able to compute: entropy $H(X)$,
  mutual information $I(X;Y)$, KL divergence $D(p\|q)$, and the inequalities
  (Jensen, Markov, Chebyshev, Chernoff), together with techniques such as the
  chain rule, symmetry and union-style counting.
- The top layer is the phenomena those tools explain: how much information is
  hidden in data, what a signal reveals, how two models mismatch, and when
  averages fail.

The exam requires the bottom layer; the point of the course is the top layer.
Every problem below is read through the same four steps: the **motivation**
(what phenomenon we care about), the **tool** (which measure or inequality
captures it), the **computation** (the exam-level mathematics), and the
**intuition** (what the result says about the world).

## 2 Problem 1(a): where n coin flips hide their bits

### 2.1 Statement and motivation

Let $X_1, \dots, X_n$ be i.i.d. $\mathrm{Bern}(\tfrac12)$, $X^n = (X_1, \dots, X_n)$,
and $K = \sum_i X_i$ the number of ones. The problem asks to show

$$ H(X^n \mid K) \ge n - \log(n+1). $$

A summary statistic, here the count $K$, replaces the raw data in countless
pipelines. The question is how much of the information the summary keeps. The
data $X^n$ has two parts: how many ones there are, and where they are.

### 2.2 Solution

Because $K$ is a function of $X^n$, adding it changes nothing:
$H(X^n, K) = H(X^n)$. The $n$ flips are independent fair bits, so
$H(X^n) = n$. The chain rule then splits the joint entropy the other way:

$$ n = H(X^n) = H(X^n, K) = H(K) + H(X^n \mid K). $$

$K$ takes the $n+1$ values $0, 1, \dots, n$, and a random variable with $n+1$
possible values has entropy at most $\log(n+1)$, with equality only for the
uniform distribution. Hence

$$ H(X^n \mid K) = n - H(K) \ge n - \log(n+1). $$

### 2.3 Bound H(K), do not compute it

The exact value is

$$ H(K) = -\sum_{k=0}^{n} \binom{n}{k} 2^{-n} \log\Big(\binom{n}{k} 2^{-n}\Big), $$

a sum that is tedious to evaluate and has no simple form. Evaluating it is
unnecessary: the problem only needs the *order* of $H(K)$, and the crude bound
$\log(n+1)$ already gives it. The values, in bits and rounded:

- $n = 10$: exact $H(K) \approx 2.71$, bound $\log 11 \approx 3.46$, total $n = 10$.
- $n = 100$: exact $H(K) \approx 4.37$, bound $\log 101 \approx 6.66$, total $n = 100$.
- $n = 1000$: exact $H(K) \approx 6.03$, bound $\log 1001 \approx 9.97$, total $n = 1000$.

The bound is loose by a factor of about two for large $n$, but both numbers are
logarithmic while the total is linear, and that is the whole story. This is a
general lesson: when a quantity is hard to compute, bound it; a bound that is
off by a constant factor still tells you which terms dominate.

**Where the asymptotic comes from.** $K$ has mean $n/2$ and variance $n/4$,
and for large $n$ it is close to a Gaussian with these parameters on the
integer lattice. A Gaussian with variance $\sigma^2$ has differential entropy
$\tfrac12 \log(2\pi e \sigma^2)$, and for a lattice of spacing one the
discrete entropy is close to the differential entropy. With $\sigma^2 = n/4$:

$$ H(K) = \tfrac12 \log\big(\tfrac{\pi e n}{2}\big) + o(1). $$

This gives $2.71$, $4.37$ and $6.03$ bits at $n = 10, 100, 1000$, matching the
exact values to the precision shown, and is about half of $\log(n+1)$ for large $n$.

### 2.4 Intuition

With $n = 100$ fair flips carrying $100$ bits, the count keeps at most
$6.66$ bits and the order of the ones keeps at least $93.3$. Almost all of the
information is in *where* the ones are, not *how many* there are. A summary
statistic usually throws information away; know what you discard.

## 3 Problem 1(b): does mixing add uncertainty

### 3.1 Statement and motivation

$X$ and $Y$ are continuous with densities $f_X, f_Y$, and $Z$ has density
$f_Z = \tfrac12 f_X + \tfrac12 f_Y$. Prove or disprove:
$h(Z) \le \max\{h(X), h(Y)\}$.

Mixtures are everywhere: data pooled from two sources, mixture models,
populations made of subpopulations. The question is whether a mixture can be
more uncertain than each of its parts. Mixing adds a new question that neither
part has: which source did $Z$ come from?

### 3.2 Counterexample

The statement is false. Take $X \sim \mathrm{Unif}[0,1]$ and
$Y \sim \mathrm{Unif}[10,11]$. Each density equals $1$ on an interval of length
one, so

$$ h(X) = -\int_0^1 1 \cdot \log 1 \, dx = 0, \qquad h(Y) = 0. $$

$Z$ has density $\tfrac12$ on $[0,1] \cup [10,11]$, a set of total length $2$,
and $0$ elsewhere. Hence

$$ h(Z) = -\int f_Z \log f_Z = -2 \cdot \tfrac12 \log \tfrac12 = 1 > 0 = \max\{h(X), h(Y)\}. $$

### 3.3 Derivation: name the hidden label

The extra bit has a name. Introduce a label $W \sim \mathrm{Bern}(\tfrac12)$
that picks the source: given $W = 0$, $Z$ is drawn from $f_X$; given $W = 1$,
from $f_Y$. The marginal density of $Z$ is then exactly
$\tfrac12 f_X + \tfrac12 f_Y$, so this is the same $Z$. Assume $h(X)$ and
$h(Y)$ are finite.

**Step 1: the conditional entropy.** Given the label, $Z$ is just $X$ or just
$Y$, so

$$ h(Z \mid W) = \tfrac12 h(Z \mid W = 0) + \tfrac12 h(Z \mid W = 1) = \tfrac12 h(X) + \tfrac12 h(Y). $$

**Step 2: entropy equals conditional entropy plus information.** For the
continuous $Z$ and the discrete $W$, mutual information is defined as
$I(Z;W) = h(Z) - h(Z \mid W)$, so

$$ h(Z) = h(Z \mid W) + I(Z;W). $$

**Step 3: bound the information.** Mutual information is symmetric and can be
written the other way, through the discrete label:
$I(Z;W) = H(W) - H(W \mid Z)$. Two facts bound it.

- $I(Z;W) \ge 0$: conditioning never increases entropy (equivalently, mutual
  information is a KL divergence and KL is non-negative).
- $I(Z;W) \le H(W) = 1$: $H(W \mid Z) \ge 0$ because $W$ is discrete. $Z$
  cannot reveal more about the label than the label holds.

Combining the three steps:

$$ \tfrac12 h(X) + \tfrac12 h(Y) \le h(Z) \le \tfrac12 h(X) + \tfrac12 h(Y) + 1. $$

### 3.4 When each bound is attained

- **Upper bound, $I(Z;W) = 1$.** This needs $H(W \mid Z) = 0$: seeing $Z$
  determines the label. That happens exactly when the supports do not overlap,
  $f_X(z) f_Y(z) = 0$ for almost every $z$, as in the counterexample. Mixing
  then adds a full bit.
- **Lower bound, $I(Z;W) = 0$.** This needs $Z$ independent of $W$, which
  means $f_X = f_Y$ almost everywhere: $X$ and $Y$ have the same distribution,
  and $Z$ says nothing about which source it came from.
- **Partial overlap.** In between, $W$ is partly hidden by $Z$, and mixing adds
  strictly between $0$ and $1$ bit.

In words: mixing two sources adds at most the entropy of *which source*, and
it adds all of it when the sources can be told apart.

The upper bound also explains why the original claim fails: when $h(X) = h(Y)$
the average equals the maximum, so any positive $I(Z;W)$ pushes $h(Z)$ above
$\max\{h(X), h(Y)\}$.

## 4 Problem 1(c): noisy labels

### 4.1 Statement and motivation

$X$ is uniform on $K \ge 2$ classes. A noisy label $Y$ equals $X$ with
probability $1 - \varepsilon$; with probability $\varepsilon$ it is drawn
uniformly from the other $K - 1$ classes. (i) Compute $I(X;Y)$ at
$\varepsilon = 0$ and $\varepsilon = 1$ and show both are nonzero. (ii) Find
$\varepsilon$ with $I(X;Y) = 0$.

Real datasets carry wrong labels from annotator errors. The question is how
much a noisy label still tells us about the truth. Guess first: is a label that
is always wrong useless?

### 4.2 The channel and the general formula

The channel is $P(Y = y \mid X = x) = 1 - \varepsilon$ if $y = x$ and
$\varepsilon/(K-1)$ if $y \ne x$. **$Y$ is uniform**: for each $y$,

$$ P(Y = y) = \tfrac1K (1 - \varepsilon) + \tfrac{K-1}{K} \cdot \tfrac{\varepsilon}{K-1} = \tfrac1K. $$

So $H(X) = H(Y) = \log K$. Given $X = x$, the label is correct with
probability $1 - \varepsilon$ and otherwise uniform over $K - 1$ wrong classes,
so

$$ H(Y \mid X) = H_2(\varepsilon) + \varepsilon \log(K - 1), $$

and therefore, for every $\varepsilon \in [0,1]$,

$$ I(X;Y) = H(Y) - H(Y \mid X) = \log K - H_2(\varepsilon) - \varepsilon \log(K-1). $$

This is the formula behind the plotted curves for $K = 2$ and $K = 10$.

### 4.3 Part (i)

**$\varepsilon = 0$.** $Y = X$, so $H(X \mid Y) = 0$ and
$I(X;Y) = \log K > 0$. A perfect label gives all $\log K$ bits.

**$\varepsilon = 1$.** The label is always wrong. Hearing $Y = y$ rules out
class $y$ and leaves $X$ uniform on the other $K - 1$ classes, so
$H(X \mid Y) = \log(K-1)$ and

$$ I(X;Y) = \log K - \log(K-1) = \log \tfrac{K}{K-1} > 0. $$

For $K = 4$ this is $\log \tfrac43 \approx 0.415$ bits; for $K = 10$ it is
$\log \tfrac{10}{9} \approx 0.15$ bits. The general formula agrees:
$H_2(1) = 0$.

### 4.4 Why a liar gives information

Information is how much $Y$ changes your belief about $X$. Before hearing the
label, $K$ classes are equally likely. After hearing $Y = y$ from a consistent
liar, class $y$ is ruled out and $K - 1$ remain. A consistent liar is
*predictable*, and predictability is dependence. Only for $K = 2$ does
eliminating one class pin down the truth: flip the label ($1 \to 2$,
$2 \to 1$) and you recover $X$ exactly, a full bit. Mutual information
measures dependence, not correctness.

### 4.5 Part (ii): when is a label truly useless

$I(X;Y) = 0$ if and only if $X$ and $Y$ are independent, which here means the
conditional law $P(Y = \cdot \mid X = x)$ is the same for every $x$. That law
puts $1 - \varepsilon$ on $x$ and $\varepsilon/(K-1)$ on every other class; it
can only be the same for every $x$ if it is uniform:

$$ 1 - \varepsilon = \frac{\varepsilon}{K-1} \iff \varepsilon = \frac{K-1}{K}. $$

At this value $Y$ is uniform whatever $X$ is, so $I(X;Y) = 0$. A check with the
general formula: at $\varepsilon = (K-1)/K$,
$H_2(\varepsilon) = \log K - \tfrac{K-1}{K} \log(K-1)$, and the formula gives
exactly $0$.

The useless error rate is $\tfrac12$ only for $K = 2$; for $K = 10$ it is
$0.9$. Labels that are wrong 60 percent of the time with $K = 10$ still carry
$\log 10 - H_2(0.6) - 0.6 \log 9 \approx 0.45$ bits. Useless means independent,
not "often wrong". The information curve dips to zero at
$\varepsilon = (K-1)/K$ and rises again toward $\log \tfrac{K}{K-1}$ at
$\varepsilon = 1$.

## 5 Problem 1(d): shuffling by moving the top card

### 5.1 Statement and motivation

A deck of $n$ cards is shuffled by one move, repeated independently:

1. **State:** the ordering of the $n$ cards, one of $n!$ possible states.
2. **Move:** take the top card and reinsert it at one of $n$ positions, each
   with probability $\tfrac1n$.
3. **Positions:** on top (the deck is unchanged), after the first remaining
   card, after the second, and so on, down to the bottom.
4. **Repeat:** the orderings $X_0, X_1, X_2, \dots$ form a Markov chain.

Show that the uniform distribution over the $n!$ orderings is stationary.

A fair shuffle should not prefer any ordering. The key idea is symmetry: after
renaming the cards, every ordering is in exactly the same situation, so the
only fair candidate is uniform. The proof turns that guess into one count.

### 5.2 Solution: count the predecessors

Write $P(\tau \to \sigma)$ for the one-step transition probability and
$U(\sigma) = 1/n!$. We need $\sum_\tau U(\tau) P(\tau \to \sigma) = U(\sigma)$
for every $\sigma$.

- **Out of any ordering.** From $\tau$, the $n$ insertion positions give $n$
  *different* orderings, each with probability $\tfrac1n$. So every transition
  probability is $0$ or $\tfrac1n$, and each row of the transition matrix sums
  to one.
- **Into any ordering.** Undo the move: pick any one of the $n$ cards of
  $\sigma$ and move it to the top. This produces exactly $n$ distinct
  predecessors $\tau$ of $\sigma$. Picking the top card of $\sigma$ gives
  $\tau = \sigma$, the "reinsert on top" move.

Therefore

$$ \sum_\tau U(\tau) P(\tau \to \sigma) = n \cdot \frac{1}{n!} \cdot \frac1n = \frac{1}{n!} = U(\sigma). $$

### 5.3 Doubly stochastic, not symmetric

The count says each *column* of the transition matrix also sums to one: the
matrix is **doubly stochastic**. For any doubly stochastic matrix the uniform
distribution is stationary, since
$\sum_\tau \tfrac{1}{N} P(\tau \to \sigma) = \tfrac1N \cdot 1$.

The matrix is **not symmetric**, and symmetry is not what the proof uses. For
$n = 3$, label orderings by top-to-bottom reading. From $123$ the top card $1$
can go to the bottom, giving $231$, so $P(123 \to 231) = \tfrac13$. But from
$231$ the top card is $2$, and moving it anywhere never produces $123$, so
$P(231 \to 123) = 0$. Column sums of one, not symmetry, make uniform
stationary. (By enumeration, the matrix is likewise asymmetric for
$n = 4$ and $n = 5$.)

The full $6 \times 6$ matrix for $n = 3$ (rows are "from", columns are "to",
in the order $123, 132, 213, 231, 312, 321$), listing for each row the three
orderings it reaches with probability $\tfrac13$:

- From $123$: $123$, $213$, $231$.
- From $132$: $132$, $312$, $321$.
- From $213$: $213$, $123$, $132$.
- From $231$: $231$, $321$, $312$.
- From $312$: $312$, $132$, $123$.
- From $321$: $321$, $231$, $213$.

Every ordering appears in exactly three rows, so every column sums to one.

### 5.4 Repeat the move: any start ends uniform

Stationarity says the uniform distribution does not change under one move. The
stronger and more useful fact is that repeating the move from **any** initial
ordering drives the distribution of $X_t$ to uniform. Two properties give this
by the convergence theorem for finite Markov chains.

- **Irreducible:** every ordering can be reached from every other. Moving top
  cards to chosen depths can build any target ordering from the bottom up.
- **Aperiodic:** the "reinsert on top" move leaves the deck unchanged with
  probability $\tfrac1n$, a self-loop at every state, which breaks any cycle.

A finite irreducible aperiodic chain converges to its unique stationary
distribution from any start, so the uniform distribution found above is the
limit.

The lecture shows this for $n = 3$ starting from $123$. Computed exactly:

- After 1 move: $\tfrac13$ on each of $123, 213, 231$; $0$ elsewhere.
- After 2 moves: $\tfrac29$ on $123, 213, 231$; $\tfrac19$ on $132, 312, 321$.
- After 3 moves: $\tfrac{5}{27}$ and $\tfrac{4}{27}$ on the same two groups.
- After 5 moves: $\tfrac{41}{243}$ and $\tfrac{40}{243}$, against $\tfrac16 = \tfrac{40.5}{243}$.

In this example each probability is off from $\tfrac16$ by exactly
$\tfrac{1}{2 \cdot 3^t}$ after $t$ moves: the convergence is geometric, but it
never becomes exactly uniform in finite time. *How fast* the chain gets close
to uniform for large $n$ is a separate question, the subject of mixing-time
theory, and is not part of this problem.

### 5.5 Takeaway

Symmetric dynamics suggest the uniform distribution; one counting step
verifies it. The same idea covers the random walk on a regular graph and the
design of MCMC samplers. Symmetry turns an $n! \times n!$ eigenvector problem
into a single count.

## 6 Problem 2: label smoothing versus confidence penalty

### 6.1 Setup and motivation

A classifier for $K \ge 2$ classes outputs $q = (q_1, \dots, q_K)$ with all
$q_k > 0$. Let $y$ be the true label and $u = (\tfrac1K, \dots, \tfrac1K)$ the
uniform distribution. The plain cross-entropy loss is $-\log q_y$.

**Cross-entropy always wants more confidence.** $-\log q_y$ is strictly
decreasing in $q_y$ all the way to $q_y = 1$, so training pushes the output
toward a one-hot vector. That is a problem because a probability of $0.999$ on
a wrong answer gives no warning sign, wrong labels in the data get memorized
with full confidence, and downstream decisions such as thresholds and
abstention trust these numbers. A model is over-confident when its predicted
probabilities exceed its actual accuracy; we want reported probabilities to
mean something.

**Design challenge.** "Confident" means far from uniform, that is, low entropy.
Two natural ways to encode "stay near uniform" follow, and you should be able
to invent both yourself.

- **Label smoothing (LS).** Soften the target by mixing the one-hot vector with
  $u$. For $0 < \varepsilon < 1$, the smoothed target $o^{(\varepsilon)}$ has
  $o^{(\varepsilon)}_y = 1 - \varepsilon + \varepsilon/K$ and
  $o^{(\varepsilon)}_k = \varepsilon/K$ for $k \ne y$, and
  $L_{\mathrm{LS}}(q) = -\sum_k o^{(\varepsilon)}_k \log q_k$. Example:
  $K = 5$, $\varepsilon = 0.2$, $y = 1$ gives the target $0.84$ on class 1 and
  $0.04$ on each other class. $o^{(0)}$ is the one-hot vector, so
  $\varepsilon = 0$ recovers $-\log q_y$.
- **Confidence penalty (CP).** Keep the one-hot target and subtract an entropy
  bonus: for $\beta > 0$, $L_{\mathrm{CP}}(q) = -\log q_y - \beta H(q)$ with
  $H(q) = -\sum_k q_k \log q_k$. A peaked $q$ earns a small bonus, a spread $q$
  a large one.

Both come from one intuition. The problem asks whether they behave the same.

### 6.2 Part (a): two KL identities

**Label smoothing.** The smoothed target is a mixture,
$o^{(\varepsilon)} = (1 - \varepsilon) o^{(0)} + \varepsilon u$: its $y$-entry
is $(1-\varepsilon) + \varepsilon/K$ and its other entries $\varepsilon/K$.
Cross-entropy is linear in the target, and $o^{(0)}$ keeps only the $k = y$
term, so

$$ L_{\mathrm{LS}}(q) = -\sum_k o^{(\varepsilon)}_k \log q_k = (1-\varepsilon)(-\log q_y) + \varepsilon \Big( -\sum_k \tfrac1K \log q_k \Big). $$

Add and subtract $\sum_k \tfrac1K \log \tfrac1K = -\log K$ in the second term:

$$ -\sum_k \tfrac1K \log q_k = \sum_k \tfrac1K \log \frac{1/K}{q_k} - \sum_k \tfrac1K \log \tfrac1K = D(u\|q) + \log K. $$

**Confidence penalty.** Directly from the definition,

$$ D(q\|u) = \sum_k q_k \log \frac{q_k}{1/K} = \sum_k q_k \log q_k + \log K = \log K - H(q), $$

so entropy is distance from uniform, read backwards, and
$-\beta H(q) = \beta D(q\|u) - \beta \log K$. Together:

$$ L_{\mathrm{LS}}(q) = (1-\varepsilon)(-\log q_y) + \varepsilon D(u\|q) + \varepsilon \log K, $$

$$ L_{\mathrm{CP}}(q) = -\log q_y + \beta D(q\|u) - \beta \log K. $$

**Same intuition, opposite KL directions.** Both losses add a KL penalty toward
uniform, but label smoothing puts $u$ in the *first* slot, $D(u\|q)$, and the
confidence penalty puts it in the *second*, $D(q\|u)$. The coefficients differ
too: CP keeps the full cross-entropy, LS scales it by $1 - \varepsilon$.
Pereyra et al. [1] noted this KL-direction link between the two regularizers.

### 6.3 Part (b): push to full confidence

Fix $y$ and let $q_y \to 1$, so $q_k \to 0$ for every $k \ne y$. Both limits
come straight from the definitions by splitting off the true-label term.

**$D(u\|q)$.** The weights are the fixed numbers $\tfrac1K$:

$$ D(u\|q) = \sum_k \tfrac1K \log \frac{1/K}{q_k} = \tfrac1K \log \frac{1}{K q_y} + \sum_{k \ne y} \tfrac1K \log \frac{1}{K q_k}. $$

The first term tends to $-\tfrac1K \log K$. Each term of the sum has fixed
weight $\tfrac1K$ multiplying $\log \tfrac{1}{K q_k} \to \infty$. Hence
$D(u\|q) \to \infty$.

**$D(q\|u)$.** The weights are the $q_k$ themselves:

$$ D(q\|u) = \sum_k q_k \log \frac{q_k}{1/K} = q_y \log(K q_y) + \sum_{k \ne y} q_k \log(K q_k). $$

The first term tends to $\log K$. Each term of the sum is
$q_k \log K + q_k \log q_k \to 0$, because $q \log q \to 0$ as $q \to 0$.
Hence $D(q\|u) \to \log K$, which is finite. Equivalently,
$D(q\|u) = \log K - H(q)$ and $H(q) \to 0$.

**Who holds the weights decides the behavior.** In $D(u\|q)$ a fixed weight
multiplies an exploding logarithm; in $D(q\|u)$ the shrinking weight $q_k$
tames it.

**The losses.** Summarizing the four limits:

- $D(u\|q) \to \infty$: the terms $k \ne y$, $\tfrac1K \log \tfrac{1}{K q_k}$, blow up.
- $D(q\|u) \to \log K$: it equals $\log K - H(q)$, and $H(q) \to 0$.
- $L_{\mathrm{LS}}(q) \to \infty$: $(1-\varepsilon)(-\log q_y) \to 0$ but
  $\varepsilon D(u\|q) \to \infty$.
- $L_{\mathrm{CP}}(q) \to 0$: $0 + \beta \log K - \beta \log K$.

Full confidence costs infinitely much under label smoothing and has finite
loss under the confidence penalty. For $K = 2$ the lecture plots the two
unweighted KL terms against $q_y \in [0.5, 1)$: $D(u\|q)$ blows up while
$D(q\|u)$ stays below $\log 2 = 1$ bit.

### 6.4 Part (c)(i): both discourage over-confidence

Without regularization the loss $-\log q_y$ keeps decreasing as $q_y \to 1$.
Each regularized loss adds a penalty that grows as $q$ becomes confident.

**Label smoothing sets a target confidence below one.** For any target
distribution $p$, cross-entropy splits as
$-\sum_k p_k \log q_k = H(p) + D(p\|q)$. With $p = o^{(\varepsilon)}$:

$$ L_{\mathrm{LS}}(q) = H(o^{(\varepsilon)}) + D(o^{(\varepsilon)}\|q). $$

The first term does not depend on $q$ and the second is non-negative and zero
only at $q = o^{(\varepsilon)}$. So the minimizer is $q = o^{(\varepsilon)}$,
whose confidence $q_y = 1 - \varepsilon + \varepsilon/K$ is strictly less than
one.

**The confidence penalty makes one-hot non-optimal.** Start at the one-hot
vector and move a small mass $\delta$ off the true label, spreading it evenly:
$q_y = 1 - \delta$ and $q_k = \delta/(K-1)$ for $k \ne y$. Then

$$ -\log q_y = -\log(1-\delta) = O(\delta), $$

because $-\ln(1-\delta) = \delta + \delta^2/2 + \cdots$; in bits this is
$\delta / \ln 2 + O(\delta^2)$. This is where the $-\log(1-\delta)$ term comes
from: it is the cross-entropy price of lowering $q_y$ from $1$ to $1-\delta$.
The entropy of the new $q$ is

$$ H(q) = -(1-\delta)\log(1-\delta) - (K-1) \cdot \frac{\delta}{K-1} \log \frac{\delta}{K-1} = -(1-\delta)\log(1-\delta) + \delta \log \frac{K-1}{\delta}. $$

The first term is $O(\delta)$ and
$\delta \log \tfrac{K-1}{\delta} = \delta \log \tfrac1\delta + \delta \log(K-1)$,
so $H(q) = \delta \log \tfrac1\delta + O(\delta)$. Therefore, for fixed $K$ and
fixed $\beta > 0$,

$$ L_{\mathrm{CP}}(q) = -\log q_y - \beta H(q) = -\beta\, \delta \log \tfrac1\delta + O(\delta), $$

which is negative for all sufficiently small $\delta > 0$, because
$\delta \log \tfrac1\delta$ dominates $\delta$ as $\delta \to 0$. The loss at
the one-hot vector is $0$, so moving away lowers the loss: the entropy bonus
beats the cross-entropy near full confidence, and the fully confident
prediction is never optimal.

### 6.5 Part (c)(ii): which is more aggressive

Label smoothing is the more aggressive one near full confidence, for fixed
$\varepsilon, \beta > 0$. By (b), as $q_y \to 1$, $L_{\mathrm{LS}} \to \infty$.
More precisely, every term of $D(u\|q)$ is at least $-\tfrac1K \log K$
(because $q_k \le 1$), so for each $k$

$$ D(u\|q) \ge \tfrac1K \log \tfrac{1}{q_k} - \log K, $$

and a near-zero probability on any class is punished without bound. The
confidence penalty, in contrast, never exceeds $\beta \log K$, since
$0 \le D(q\|u) \le \log K$, and $L_{\mathrm{CP}} \to 0$ stays finite. Label
smoothing builds an unbounded barrier near full confidence; the confidence
penalty charges a bounded price. This is a statement about the regime near
full confidence, not a ranking at every confidence level or for every choice
of the coefficients.

### 6.6 Consequences and lesson

Knowing the math of each term predicts side effects.

- With label smoothing, a single example with a freely chosen $q$ has its
  optimum at $q = o^{(\varepsilon)}$, which gives every wrong class exactly
  $\varepsilon/K$.
- Müller, Kornblith and Hinton [2] report that label smoothing improves
  calibration, yet a teacher trained with label smoothing makes a worse
  teacher for knowledge distillation.
- The confidence penalty is capped at $\beta \log K$: for small $\beta$ it is a
  mild nudge.

The lesson is a four-step recipe for designing your own algorithm: state the
**intuition** ("do not be over-confident"), **translate** it into mathematics
(a smoothed target or an entropy bonus), **analyze** the result (limits,
boundedness, KL direction), and **choose** the behavior you actually want. The
same motivation led to two different algorithms.

## 7 Problem 3: heavy tails and the median of means

### 7.1 Light tails and why the sample mean works

Most textbook distributions are light-tailed. For a standard Gaussian $Z$ the
Chernoff bound gives $P(Z \ge t) \le e^{-t^2/2}$ for $t \ge 0$; the exact
values are $P(Z \ge 1) \approx 0.16$, $P(Z \ge 3) \approx 1.3 \times 10^{-3}$
and $P(Z \ge 5) \approx 2.9 \times 10^{-7}$. Extreme values are astronomically
rare.

For light-tailed i.i.d. data the sample mean works for two reasons: outliers
are so rare that they almost never appear in the sample, and averaging dilutes
the few that do. The Chernoff bound makes this quantitative:
$P(|\bar X_n - \mu| \ge a) \le 2 e^{-cn}$ for a fixed $a > 0$ and some
$c > 0$ depending on $a$ and the distribution. A fixed-size error in the mean
has probability exponentially small in $n$. The question of Problem 3 is what
happens when outliers are not rare.

### 7.2 Heavy tails

One common definition: a distribution is heavy-tailed when its tail decays
more slowly than every exponential. The power law, or Pareto tail, is the
standard example: $P(X > x) = x^{-\alpha}$ for $x \ge 1$. Problem 3 uses
$\alpha = 3$.

**The MGF is infinite.** For $\alpha = 3$, $X$ has density
$f(x) = 3x^{-4}$ on $x \ge 1$, and for every $t > 0$

$$ \mathbb{E}[e^{tX}] = \int_1^\infty e^{tx}\, 3x^{-4}\, dx = \infty, $$

because $e^{tx}$ grows faster than any power of $x$, so the integrand
eventually exceeds $1$. With no finite MGF for $t > 0$, the Chernoff bound
cannot be applied to $X$ directly.

**Which moments exist.** For $p < 3$,
$\mathbb{E}[X^p] = \int_1^\infty x^p \cdot 3x^{-4} dx = \tfrac{3}{3-p}$, and
for $p \ge 3$ the integral diverges. So the mean ($\tfrac32$) and the second
moment ($3$) are finite, but $\mathbb{E}[X^3] = \infty$.

**Twenty orders of magnitude.** At $x = 10$ the heavy tail is
$10^{-3}$ while the standard Gaussian tail is about $7.6 \times 10^{-24}$.

**Where heavy tails live.** Clauset, Shalizi and Newman [3] test power-law
fits on empirical data sets; for wildfire sizes and earthquake intensities in
US data, and for the net worth of the richest Americans, an exponential fit
is ruled out. In deep learning, Simsekli, Sagun and Gurbuzbalaban [4] report
heavy-tailed stochastic-gradient noise in the networks they study.

**Why it matters.** In disaster planning the worst year matters, not the
average year. History underestimates: the biggest event may not be in your
data yet. Light-tailed models call such events "once in the age of the
universe". Under heavy tails, extreme values drive the very averages we
estimate.

**Polynomial versus exponential.** The gap between a polynomial and an
exponential tail is not close:

- $n = 10$: $1/n^3 = 10^{-3}$, $e^{-n} \approx 4.5 \times 10^{-5}$, ratio about $22$.
- $n = 50$: $1/n^3 = 8 \times 10^{-6}$, $e^{-n} \approx 1.9 \times 10^{-22}$, ratio about $4 \times 10^{16}$.
- $n = 100$: $1/n^3 = 10^{-6}$, $e^{-n} \approx 3.7 \times 10^{-44}$, ratio about $3 \times 10^{37}$.

### 7.3 The problem

$X \ge 1$ with $P(X > x) = x^{-3}$ for $x \ge 1$; $X_1, \dots, X_n$ are
i.i.d. copies and $\bar X_n = \tfrac1n \sum_i X_i$. The hint allows
$\mathbb{E}[W] = \int_0^\infty P(W > w)\, dw$ for $W \ge 0$. The plan: (a) the
mean and variance exist; (b) yet $\bar X_n$ concentrates only polynomially;
(c) the median of means concentrates exponentially; (d) why the median wins.

### 7.4 Part (a): moments from the tail

Apply the hint to $W = X^2 \ge 0$ and substitute $s = x^2$, $ds = 2x\,dx$:

$$ \mathbb{E}[X^2] = \int_0^\infty P(X^2 > s)\, ds = \int_0^\infty P(X > \sqrt s)\, ds = \int_0^\infty 2x\, P(X > x)\, dx. $$

Since $P(X > x) = 1$ for $0 \le x < 1$,

$$ \mu = \int_0^\infty P(X > x)\,dx = 1 + \int_1^\infty x^{-3}\, dx = 1 + \tfrac12 = \tfrac32, $$

$$ \mathbb{E}[X^2] = \int_0^1 2x\,dx + \int_1^\infty 2x \cdot x^{-3}\, dx = 1 + 2 = 3, $$

so $\sigma^2 = 3 - \tfrac94 = \tfrac34$. The density $f(x) = 3x^{-4}$ gives the
same values.

**Finite variance, infinite MGF.** With $\sigma^2 = \tfrac34$, Chebyshev's
inequality and the law of large numbers apply: $\bar X_n \to \mu$. The variance
also gives ordinary fluctuations of order $1/\sqrt n$. The issue is not
whether the mean converges but how fast the probability of a *fixed-size*
error decays, and that is governed by rare large values, where
$\mathbb{E}[X^3] = \infty$ and $\mathbb{E}[e^{tX}] = \infty$.

### 7.5 Part (b): one big sample moves the mean

All $X_i \ge 1 > 0$, so $\bar X_n \ge X_1/n$. If the single sample $X_1$ is at
least $n(\mu + a)$, then $\bar X_n \ge \mu + a$ regardless of the others.
Hence

$$ P(\bar X_n \ge \mu + a) \ge P\big(X_1 \ge n(\mu + a)\big) = \big(n(\mu+a)\big)^{-3}, $$

using $P(X \ge x) = P(X > x) = x^{-3}$ for $x \ge 1$ ($X$ has a density, so
the boundary has probability zero). Chebyshev gives the matching upper bound:

$$ P(\bar X_n \ge \mu + a) \le P(|\bar X_n - \mu| \ge a) \le \frac{\sigma^2}{n a^2} = \frac{3}{4 n a^2}. $$

So for fixed $a > 0$ the probability is sandwiched between $n^{-3}$ and $n^{-1}$
rates.

- It tends to zero: the law of large numbers holds.
- No bound of the form $C e^{-cn}$ with fixed $C, c > 0$ can hold for all large
  $n$, because $(n(\mu+a))^{-3} \gg C e^{-cn}$ eventually.

This rules out exponential fixed-error tails; the exact polynomial rate is not
established by these two bounds. The lecture's illustration: $n = 20$ samples
near the true mean $\mu = 1.5$ plus one outlier give $\bar X_n \approx 1.94$.
The mean converges, but slowly: outliers keep distracting it.

### 7.6 Can we beat the sample mean

Outliers are not negligible: under a heavy tail they will appear. One outlier
can move the mean arbitrarily far, while the median moves far only if half of
the values do. The idea: let the outliers vote, but only once each.

**The median-of-means estimator.**

1. Split the $n = km$ samples into $k$ groups of $m$.
2. Compute the group means $\bar X^{(1)}, \dots, \bar X^{(k)}$.
3. Output $\hat\mu = \mathrm{median}(\bar X^{(1)}, \dots, \bar X^{(k)})$.

Fix $a > 0$ and call group $j$ **bad** if $|\bar X^{(j)} - \mu| \ge a$. An
outlier lands in one group and spoils that one vote; the median stays within
the good interval $(\mu - a, \mu + a)$ as long as more than half the group
means remain there.

### 7.7 Part (c)(i): each group is rarely bad

**Show:** if $m \ge 6/a^2$, each group is bad with probability at most
$\tfrac18$.

$\bar X^{(j)}$ is the mean of $m$ i.i.d. copies of $X$, so its variance is
$\sigma^2/m$. By Chebyshev,

$$ P(|\bar X^{(j)} - \mu| \ge a) \le \frac{\sigma^2}{m a^2} = \frac{3}{4 m a^2} \le \frac34 \cdot \frac16 = \frac18 \qquad \text{when } m \ge 6/a^2. $$

Only Chebyshev is needed here: finite variance suffices per group.

### 7.8 Part (c)(ii): failure needs half the groups bad

**Show:** if $|\hat\mu - \mu| \ge a$, then at least $k/2$ groups are bad.

Prove the contrapositive. Suppose fewer than $k/2$ groups are bad. Then more
than half of the group means lie in $(\mu - a, \mu + a)$. If
$\hat\mu \ge \mu + a$, all of those means would lie strictly below $\hat\mu$,
so more than half of the values would be strictly below the median. That
contradicts the defining property of a median: at least half of the values are
at or above it. The case $\hat\mu \le \mu - a$ is symmetric. So
$|\hat\mu - \mu| < a$. Writing $Z$ for the number of bad groups,

$$ \{|\hat\mu - \mu| \ge a\} \subseteq \{Z \ge k/2\}. $$

### 7.9 Part (c)(iii): Chernoff on the bad count

**Show:** with the worst case $Z \sim \mathrm{Bin}(k, \tfrac18)$, for every
$t > 0$, $P(Z \ge k/2) \le \big(e^{-t/2}(\tfrac78 + \tfrac18 e^t)\big)^k$.

For $t > 0$ the map $z \mapsto e^{tz}$ is increasing, so
$\{Z \ge k/2\} = \{e^{tZ} \ge e^{tk/2}\}$, and Markov's inequality gives

$$ P(Z \ge \tfrac k2) = P(e^{tZ} \ge e^{tk/2}) \le e^{-tk/2}\, \mathbb{E}[e^{tZ}]. $$

Write $Z = \sum_{j=1}^k B_j$ with independent $B_j \sim \mathrm{Bern}(\tfrac18)$.
The Bernoulli MGF is $\mathbb{E}[e^{tB_j}] = \tfrac78 + \tfrac18 e^t$, and
independence turns the MGF of the sum into a product of $k$ equal factors:
$\mathbb{E}[e^{tZ}] = (\tfrac78 + \tfrac18 e^t)^k$. Combining,

$$ P(Z \ge \tfrac k2) \le \Big(e^{-t/2}\big(\tfrac78 + \tfrac18 e^t\big)\Big)^k. $$

**Why the worst case is enough.** The groups use disjoint samples, so the
events "group $j$ is bad" are independent, each with probability
$p \le \tfrac18$. A binomial count with a smaller success probability is
stochastically smaller, so $P(Z \ge k/2)$ can only decrease when $p < \tfrac18$.

### 7.10 Part (c)(iv): exponential in n

**Show:** with $e^t = 7$ the bound is $(\sqrt7/4)^k$; with
$m = \lceil 6/a^2 \rceil$, $P(|\hat\mu - \mu| \ge a)$ decays exponentially in
$n$.

With $e^t = 7$, $e^{-t/2} = 1/\sqrt7$ and

$$ e^{-t/2}\big(\tfrac78 + \tfrac18 \cdot 7\big) = \frac{1}{\sqrt7} \cdot \frac74 = \frac{\sqrt7}{4} \approx 0.661 < 1. $$

**Why $e^t = 7$.** Write $s = e^t$ and minimize
$g(s) = s^{-1/2}(\tfrac78 + \tfrac18 s)$ over $s > 1$. Then
$g'(s) = s^{-3/2}\big(\tfrac{s}{16} - \tfrac{7}{16}\big)$, which vanishes at
$s = 7$, a minimum. So $e^t = 7$ is the best choice in (iii).

Combining (ii), (iii) and (iv), with $m = \lceil 6/a^2 \rceil$ so that (i)
applies,

$$ P(|\hat\mu - \mu| \ge a) \le P(Z \ge \tfrac k2) \le \Big(\frac{\sqrt7}{4}\Big)^k = \Big(\frac{\sqrt7}{4}\Big)^{n/m}. $$

With $m$ fixed by $a$, the number of groups $k = n/m$ grows linearly in $n$,
so the bound decays exponentially in $n$.

### 7.11 The numbers

Take $a = 0.5$, so $m = \lceil 6/0.25 \rceil = 24$ and $k = n/24$. Compare a
*lower* bound on the mean's failure probability, $(n(\mu+a))^{-3}$ on
$P(\bar X_n \ge \mu + a)$, with an *upper* bound on the median of means'
failure probability, $(\sqrt7/4)^k$ on $P(|\hat\mu - \mu| \ge 0.5)$:

- $n = 2{,}400$: the mean fails with probability at least about $9.0 \times 10^{-12}$; the median of means at most about $1.1 \times 10^{-18}$.
- $n = 24{,}000$: the mean at least about $9.0 \times 10^{-15}$; the median of means at most about $3.1 \times 10^{-180}$.

Because one column is a lower bound and the other an upper bound, the
comparison is fair to the sample mean: the true gap is at least this large.

### 7.12 Part (d): why the median of means wins

A single sufficiently large sample can push $\bar X_n$ above $\mu + a$, and
under a heavy tail such a sample appears with only polynomially small
probability. The median of means traps any huge sample in a single group,
where it spoils only one vote. The median fails only if at least half of the
independent groups fail at once, a coin-flip large deviation with exponentially
small probability. Each group is unlikely to be bad; having at least half bad
is exponentially unlikely.

### 7.13 Robust estimation in practice

- Median of means achieves sub-Gaussian error bounds assuming only finite
  variance; Lugosi and Mendelson [5] survey this line of work.
- The trimmed mean drops the extremes and then averages.
- In distributed learning, the coordinate-wise median or trimmed mean of the
  workers' gradients resists faulty or adversarial workers; Yin, Chen,
  Ramchandran and Bartlett [6] analyze these rules.

The shared principle: a minority cannot move the median.

## 8 What we expect from you

- **Compute:** entropy, mutual information, KL divergence, moments, bounds.
- **Apply:** the right inequality at the right step.
- **Explain:** what the result means, in words.
- **Predict:** the behavior before the computation.

The tools are weapons. Use them to understand.

## 9 References

The citation strings below are the ones used on the slides.

1. Pereyra, Tucker, Chorowski, Kaiser, Hinton, "Regularizing Neural Networks by Penalizing Confident Output Distributions", 2017.
2. Müller, Kornblith, Hinton, "When Does Label Smoothing Help?", NeurIPS 2019.
3. Clauset, Shalizi, Newman, "Power-Law Distributions in Empirical Data", SIAM Review, 2009.
4. Simsekli, Sagun, Gurbuzbalaban, "A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks", ICML 2019.
5. Lugosi, Mendelson, "Mean Estimation and Regression under Heavy-Tailed Distributions: A Survey", FoCM 2019.
6. Yin, Chen, Ramchandran, Bartlett, "Byzantine-Robust Distributed Learning: Towards Optimal Statistical Rates", ICML 2018.
