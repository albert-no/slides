# Deep Learning Math, Lecture 4: Random Processes and Markov Chains

**About this file.** Screen-reader edition of the Lecture 4 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob04-random-processes-note.html`). Matrices are written out row
by row in words as well as in LaTeX where that helps, and the numeric evolution
table is written as a list. Nothing else is needed to read it.

**Convention alert, used everywhere.** Transition matrices here are
**column-stochastic**: $P_{u,v} = \Pr(X_i = u \mid X_{i-1} = v)$, columns sum to
1, distributions are column vectors, and one step is $\pi_i = P \pi_{i-1}$. Most
textbooks (for instance references 2 and 3) use the row convention; to translate,
transpose everything, so that $P_{\text{here}} = P_{\text{book}}^\top$ and the
book's row-vector update $\pi P$ becomes our $P\pi$.

**Notation.** $X^n = (X_1, \dots, X_n)$ and $x^n = (x_1, \dots, x_n)$;
$x_{i-k}^{i-1} = (x_{i-k}, \dots, x_{i-1})$. $\mathcal{X}$ is a finite alphabet.
$\mathbf{1}$ is the all-ones column vector, $J = \mathbf{1}\mathbf{1}^\top$ the
all-ones matrix, $I$ the identity, $\Delta_n$ the probability simplex in
$\mathbb{R}^n$, and $\|w\|_1 = \sum_u |w_u|$. $\overset{d}{=}$ means equality of
joint pmfs. $\pi^\star$ is a stationary distribution, $\pi_\infty$ a limiting
distribution. All random variables take finitely many values unless a
counterexample says otherwise.

**Background used.** Entropy from Lecture 1, KL divergence and the
cross-entropy loss from Lecture 2, conditional distributions, Bayes' rule and the
three-variable Markov chain $X - Y - Z$ from Lecture 3. These are cited, not
re-proved.

**Contents.**

1. Why sequences
2. Random processes
3. Markov processes
4. Transition matrices
5. Evolution in time
6. Stationary processes
7. Stationary distributions
8. Limiting distributions
9. Discrete diffusion
10. References

## 1. Why Sequences?

Lectures 1 to 3 built tools for one or two random variables at a time: entropy
$H(X)$, divergence $D(P \Vert Q)$, mutual information $I(X;Y)$ and conditional
distributions. Three motivating systems -- a language model emitting token after
token, a diffusion model corrupting an image step by step, a random surfer
hopping link to link -- are all instances of a single new object: a *sequence* of
random variables $X_1, X_2, X_3, \dots$ evolving in time. Two genuinely new
questions arise that no single snapshot can answer: **how do successive steps
depend on each other**, and **where does the sequence settle in the long run**?

The headline, delivered in Sections 7 and 8: for a well-behaved chain the
long-run distribution $\pi^\star$ is characterized *algebraically*, as a solution
of $\pi^\star = P\pi^\star$, an eigenvector of the transition matrix for
eigenvalue 1. Long-run behavior is linear algebra, not simulation. Section 9 then
cashes this in for generative modeling: a discrete diffusion model is nothing but
a Markov chain whose limiting distribution is deliberately chosen to be easy to
sample.

Two running examples carry every computation: a **binary chain** (flip with
probability $\alpha$, stay with $1 - \alpha$; numbers at $\alpha = \frac14$) and
a **three-state rotation chain** ($A \to B \to C \to A$ with probability
$\frac12$, stay with probability $\frac12$). Both are solved completely by hand
below.

## 2. Random Processes

### 2.1 Definition, with the fine print

**Definition (discrete-time random process).** A random process is a sequence of
random variables

$$ \mathbf{X} = \{X_n\}_{n=1}^{\infty}, $$

all defined on a common probability space, each $X_n$ taking values in a common
finite alphabet $\mathcal{X}$. The index $n$ is read as *time* (step, token
position, iteration). The process is described by its *finite-dimensional
distributions*: the joint pmfs
$P_{X^n}(x^n) = P_{X_1, \dots, X_n}(x_1, \dots, x_n)$ for every $n$.

**Fine print.** (i) The joint pmfs must be *consistent*: marginalizing
$P_{X^{n+1}}$ over $x_{n+1}$ must return $P_{X^n}$, which is automatic when, as
here, the pmfs come from one underlying space. (ii) Conversely, that any
consistent family of finite-dimensional distributions really is realized by a
process on some probability space is the *Kolmogorov extension theorem*, used
silently and not proved; see [6, Thm. A.3.1]. For everything in this lecture,
finite windows $X^n$ suffice, so nothing below depends on this subtlety.

### 2.2 The i.i.d. process, and the coin-flip check

**Definition (i.i.d. process).** $\mathbf{X}$ is *independent and identically
distributed* if all $X_n$ share one marginal pmf $P_X$ and every joint pmf
factorizes into marginals:

$$ P_{X^n}(x^n) = \prod_{i=1}^{n} P_{X}(x_i)
   \qquad \text{for all } n, x^n. $$

The weaker form $\prod_i P_{X_i}(x_i)$ allows per-index marginals;
"identically distributed" additionally makes them all equal. Both properties are
used later, for instance in Section 6.

**Coin example.** A fair coin flipped four times gives, for the string HTHH,

$$ P(\mathrm{HTHH})
   = \tfrac12 \cdot \tfrac12 \cdot \tfrac12 \cdot \tfrac12 = \tfrac{1}{16}, $$

and identically for each of the $2^4 = 16$ length-4 strings: the uniform
distribution on $\{\mathrm{H},\mathrm{T}\}^4$.

### 2.3 Why "neighbors reveal nothing" under i.i.d.

*Claim.* Under i.i.d. the conditional pmf of one symbol given all the others
equals its marginal. *Proof:* for any $i$ and any values $x^n$ with positive
probability of the conditioning event,

$$ P(X_i = x_i \mid X_j = x_j, \; j \neq i)
   = \frac{\prod_{j=1}^{n} P_X(x_j)}{\prod_{j \neq i} P_X(x_j)}
   = P_X(x_i), $$

using the factorization in both numerator and denominator; the denominator is the
joint of the others, obtained by summing the factorized joint over $x_i$, which
pulls out $\sum_{x_i} P_X(x_i) = 1$. **End of proof.**

Real text violates this massively. In the corrupted string "my na_e is Albert"
every reader fills in the letter **m** from the neighbors, so text is not i.i.d.
On the spectrum of models, first-order Markov is the first tractable step away
from i.i.d. toward rich correlation; Sections 3 and 6 refine this spectrum twice.

## 3. Markov Processes

### 3.1 First-order Markov property, stated precisely

**Definition (1st-order Markov process).** $\mathbf{X}$ is a 1st-order Markov
process if for every $i \geq 2$ and every $x^i$ such that
$P_{X^{i-1}}(x^{i-1}) > 0$,

$$ P_{X_i \mid X^{i-1}}(x_i \mid x^{i-1})
   = P_{X_i \mid X_{i-1}}(x_i \mid x_{i-1}). $$

Two conditions the compact form leaves implicit: the identity is required for
*every* step $i$ and *every* history of positive probability (conditional pmfs
are undefined on zero-probability histories, so nothing is required there); and it
is a statement about conditional *distributions*, so it must hold for every value
$x_i$. In words: given the present $X_{i-1}$, the further past $X^{i-2}$ is
irrelevant to $X_i$. This is the process version of the three-variable Markov
chain $X - Y - Z$ from Lecture 3; indeed the definition says exactly that
$X^{i-2} - X_{i-1} - X_i$ forms a Markov triple for every $i$. The i.i.d. case is
the degenerate instance in which even $X_{i-1}$ is irrelevant.

### 3.2 The random walk is Markov, and a general recipe

The walk: $X_0 = 0$ and $X_n = X_{n-1} \pm 1$ with probability $\frac12$ each,
the signs chosen fresh each step. Its Markov property is an instance of a lemma
worth isolating, because it covers every recursively generated process at once.

**Lemma A (recursion implies Markov).** Let $Z_1, Z_2, \dots$ be independent
random variables, independent of $X_0$, and define $X_n = g_n(X_{n-1}, Z_n)$ for
deterministic functions $g_n$. Then $\{X_n\}$ is a 1st-order Markov process.

*Proof.* Fix $i$ and a positive-probability history $x^{i-1}$ (indexing from 0;
the argument is the same from 1). The history $X^{i-1} = x^{i-1}$ is an event
determined by $(X_0, Z_1, \dots, Z_{i-1})$ only, since each $X_k$ is, by
unwinding the recursion, a function of $(X_0, Z_1, \dots, Z_k)$. Hence $Z_i$ is
independent of that event, and

$$ P(X_i = x_i \mid X^{i-1} = x^{i-1})
   = P\left(g_i(x_{i-1}, Z_i) = x_i \mid X^{i-1} = x^{i-1}\right)
   = P\left(g_i(x_{i-1}, Z_i) = x_i\right). $$

The result depends on the history only through $x_{i-1}$; conditioning on
$X_{i-1} = x_{i-1}$ alone gives the same value by the identical computation
(average the display over histories ending in $x_{i-1}$). **End of proof.**

For the walk, $g(x,z) = x + z$ with $Z_n = \pm 1$ uniform. Numerically: given
$X_{101} = 51$, the next state is 52 or 50 with probability $\frac12$ each, and
the extra datum $X_{100} = 50$ changes nothing, which is exactly the display
above with $g(51, \pm 1) \in \{52, 50\}$.

### 3.3 Markov factorization: Proposition 1

**Imported lemma (chain rule of probability, Lecture 3).** For any process and
any $x^n$ with $P_{X^n}(x^n) > 0$,

$$ P_{X^n}(x^n) = \prod_{i=1}^{n} P_{X_i \mid X^{i-1}}(x_i \mid x^{i-1}), $$

with the convention that the $i = 1$ factor is the unconditional
$P_{X_1}(x_1)$ (empty conditioning). Proof: telescope the definition of
conditional pmf, $P_{X_i \mid X^{i-1}} = P_{X^i} / P_{X^{i-1}}$, and cancel. If
$P_{X^n}(x^n) = 0$ the identity holds too, reading any undefined factor past the
first zero as irrelevant: the first vanishing factor already makes the product 0.

**Proposition 1 (Markov factorization).** For a 1st-order Markov process,

$$ P_{X^n}(x^n) = \prod_{i=1}^{n} P_{X_i \mid X_{i-1}}(x_i \mid x_{i-1}), $$

again with the $i = 1$ factor read as $P_{X_1}(x_1)$.

*Proof.* If $P_{X^n}(x^n) > 0$, every prefix has positive probability, so every
factor in the chain rule is defined; apply the Markov property to each factor
with $i \geq 2$. Chain rule first, then the Markov property term by term:

$$ P_{X^n}(x^n)
   = \prod_{i=1}^{n} P_{X_i \mid X^{i-1}}(x_i \mid x^{i-1})
   = \prod_{i=1}^{n} P_{X_i \mid X_{i-1}}(x_i \mid x_{i-1}). $$

If $P_{X^n}(x^n) = 0$, let $i^\ast$ be the first index whose prefix probability
vanishes; the factor at $i^\ast$, conditional on the positive-probability prefix
$x^{i^\ast - 1}$, is 0, so the right-hand side is 0 as well. **End of proof.**

**Converse: factorization is a characterization.** If a process satisfies
$P_{X^n}(x^n) = \prod_i Q_i(x_i \mid x_{i-1})$ for every $n$ and some conditional
pmfs $Q_i$, then it is 1st-order Markov, and $Q_i = P_{X_i \mid X_{i-1}}$
wherever defined. *Proof:* divide the length-$i$ factorization by the
length-$(i-1)$ one, on positive-probability histories, to get
$P_{X_i \mid X^{i-1}}(x_i \mid x^{i-1}) = Q_i(x_i \mid x_{i-1})$, whose right
side depends on the history only through $x_{i-1}$; averaging over compatible
histories identifies it with $P_{X_i \mid X_{i-1}}(x_i \mid x_{i-1})$, exactly as
in Lemma A. **End of proof.** This equivalence is what lets Section 9 treat
"define the process by its transition kernel" and "assume the Markov property"
interchangeably.

**Why it matters, with the count.** With alphabet size $m = 27$ and length
$n = 10$, the full joint table has
$m^n = 27^{10} = 205{,}891{,}132{,}094{,}649 \approx 2.06 \times 10^{14}$
entries, versus $m^2 = 729$ for the one-step table. The one-step table is the
next section's transition matrix.

### 3.4 $k$th-order Markov processes

**Definition ($k$th-order Markov).** For every $i$ and every positive-probability
history,

$$ P_{X_i \mid X^{i-1}}(x_i \mid x^{i-1})
   = P_{X_i \mid X_{i-k}^{i-1}}(x_i \mid x_{i-k}^{i-1}), $$

where $x_{i-k}^{i-1} = (x_{i-k}, \dots, x_{i-1})$ is the length-$k$ recent past;
for $i \leq k$ the window is truncated at the start of the sequence (condition on
all of $x^{i-1}$), so the requirement is vacuous there.

**Proposition 2** ($k$th-order factorization) follows exactly as Proposition 1:
chain rule, then shorten each factor with $i > k$ by the defining property,
keeping the truncated factors for $i \leq k$; the same truncation convention
applies to the displayed product.

The parameter count generalizes the $m^2$ of Section 3.3: one needs a conditional
distribution for each of $m^k$ contexts, that is, a table of $m^k (m-1)$ free
parameters -- the exponential blow-up in $k$. A transformer with a length-$k$
context window is exactly a $k$th-order model whose table is *compressed* into
network weights rather than stored; that is an illustration only, and these notes
stay with the exact finite-state case.

## 4. Transition Matrices

### 4.1 Homogeneity, and the two standing assumptions

From here on, two assumptions hold for the rest of the lecture:

- **Finite state space:** $X_i \in \mathcal{X} = \{1, \dots, n\}$ for all $i$.
  Note the collision of notation: $n$ is now the number of *states*, no longer a
  sequence length.
- **Time-homogeneity:** the transition rule
  $P_{X_i \mid X_{i-1}}(u \mid v)$ is the same function of $(u,v)$ for every $i$.
  A Markov process with this property is called a (time-)*homogeneous Markov
  chain*.

Homogeneity is what makes "the" transition matrix meaningful; without it there
would be a different matrix $P^{(i)}$ at each step, and Theorem 2 below would
read $\pi_t = P^{(t)} \cdots P^{(1)} \pi_0$ instead of a clean power. Section 9's
*reverse-time* chain is a natural example that is Markov but not homogeneous.

### 4.2 The transition matrix and the column convention

**Definition (transition matrix).** The $n \times n$ matrix $P$ with entries

$$ P_{u,v} = \Pr(X_i = u \mid X_{i-1} = v), $$

independent of $i$ by homogeneity. Column $v$ holds the distribution of the next
state given the current state $v$; row $u$ collects all the ways to arrive at
$u$. Every entry is non-negative, and every **column sums to one**:

$$ \sum_{u=1}^{n} P_{u,v}
   = \sum_{u=1}^{n} \Pr(X_i = u \mid X_{i-1} = v) = 1, $$

because conditional on $X_{i-1} = v$ the next state is *some* element of
$\mathcal{X}$ and the conditional pmf sums to 1. A non-negative matrix with unit
column sums is called *column-stochastic*. Compactly:
$\mathbf{1}^\top P = \mathbf{1}^\top$.

A *probability vector* is $\pi \in \mathbb{R}^n$ with $\pi(u) \geq 0$ and
$\sum_u \pi(u) = 1$; the set of all of them is the simplex $\Delta_n$, a closed
and bounded (compact) subset of $\mathbb{R}^n$ -- compactness is used in the
existence proof of Section 7.4. The *state distribution at time $i$* is the
probability vector $\pi_i$ with entries $(\pi_i)_u = \Pr(X_i = u)$; $\pi_0$ is
the initial distribution, chosen by the modeler. Note that $P$ maps probability
vectors to probability vectors: non-negativity is clear, and
$\mathbf{1}^\top (P\pi) = (\mathbf{1}^\top P)\pi = \mathbf{1}^\top \pi = 1$.

**Source-notes discrepancy, for the record.** The LaTeX source's binary-chain
example defines its transition probabilities self-contradictorily: it states
$p_{X_i \mid X_{i-1}}(0 \mid 1) = p_{X_i \mid X_{i-1}}(1 \mid 0) = \alpha$ *and*
$p_{X_i \mid X_{i-1}}(1 \mid 0) = p_{X_i \mid X_{i-1}}(0 \mid 1) = 1 - \alpha$,
the same two conditionals twice, a copy-paste slip. The intended reading, and the
one the stated matrix implements, is: *flip* with probability $\alpha$
($P_{0,1} = P_{1,0} = \alpha$), *stay* with probability $1 - \alpha$
($P_{0,0} = P_{1,1} = 1 - \alpha$). All numerics below are consistent with this
reading.

### 4.3 Theorem 1: one step is one multiplication

**Theorem 1 (one-step evolution).** For every $i \geq 1$: $\pi_i = P \pi_{i-1}$.

*Proof.* Fix a state $u$. The events $\{X_{i-1} = v\}$, $v = 1, \dots, n$,
partition the sample space, so the law of total probability gives

$$ \Pr(X_i = u)
   = \sum_{v=1}^{n} \Pr(X_{i-1} = v) \, \Pr(X_i = u \mid X_{i-1} = v), $$

where terms with $\Pr(X_{i-1} = v) = 0$ are read as 0, their conditional factor
being undefined but multiplied by zero mass. Renaming the factors as
$(\pi_{i-1})_v$ and $P_{u,v}$,

$$ \Pr(X_i = u) = \sum_{v=1}^{n} P_{u,v} \, (\pi_{i-1})_v
   = (P \pi_{i-1})_u, $$

the row-$u$-times-vector formula. As $u$ was arbitrary,
$\pi_i = P\pi_{i-1}$. **End of proof.**

The proof uses only total probability and homogeneity; the Markov property is not
needed for the *marginal* flow. Markovianity is what makes $P$ alone determine
all *joint* statistics (Proposition 1), which Sections 6 and 7 need.

### 4.4 Binary chain: both steps by hand

States $\{0,1\}$; flip probability $\alpha$, at the running value
$\alpha = \frac14$. The matrix has first row $(1-\alpha, \; \alpha)$ and second
row $(\alpha, \; 1-\alpha)$:

$$ P = \begin{pmatrix} 1-\alpha & \alpha \\ \alpha & 1-\alpha \end{pmatrix}
     = \begin{pmatrix} 3/4 & 1/4 \\ 1/4 & 3/4 \end{pmatrix}. $$

Column sums $(1-\alpha) + \alpha = 1$: stochastic. It is symmetric,
$P^\top = P$. Start pinned at 0, $\pi_0 = [1, 0]^\top$:

$$ \pi_1 = P\pi_0 = \left[1-\alpha, \; \alpha\right]^\top
   = \left[\tfrac34, \; \tfrac14\right]^\top, $$

$$ \pi_2 = P\pi_1
   = \left[(1-\alpha)^2 + \alpha^2, \; 2\alpha(1-\alpha)\right]^\top
   = \left[\tfrac{9}{16} + \tfrac{1}{16}, \;
     2 \cdot \tfrac14 \cdot \tfrac34\right]^\top
   = \left[\tfrac58, \; \tfrac38\right]^\top. $$

Sanity: the entries sum to
$(1-\alpha)^2 + 2\alpha(1-\alpha) + \alpha^2 = ((1-\alpha) + \alpha)^2 = 1$. The
probabilistic reading of the top entry -- return to 0 in two steps by staying
twice or flipping twice -- is exactly the two-path expansion of $(P^2)_{0,0}$.

The running value satisfies $\alpha < \frac12$; the theory below needs only
$0 < \alpha < 1$. At $\alpha = \frac12$ the chain mixes in one step; for
$\alpha > \frac12$ it converges with oscillation, the error factor $1 - 2\alpha$
of Section 8 being negative. The excluded endpoints are $\alpha = 0$ (reducible:
never leaves its start) and $\alpha = 1$ (periodic: Section 8.2).

### 4.5 Three-state chain: the matrix read off the diagram

Stay with probability $0.5$, otherwise rotate $A \to B \to C \to A$. Ordering
states $(A, B, C)$ and filling *columns*, so that each column is the current
state, the matrix has rows $(0.5, 0, 0.5)$, then $(0.5, 0.5, 0)$, then
$(0, 0.5, 0.5)$:

$$ P = \begin{pmatrix}
     0.5 & 0 & 0.5 \\
     0.5 & 0.5 & 0 \\
     0 & 0.5 & 0.5
   \end{pmatrix}. $$

Check each column: from $A$, stay at $A$ with probability $0.5$ or move to $B$
with probability $0.5$, giving column $(0.5, 0.5, 0)^\top$; from $B$, stay or
move to $C$; from $C$, stay or move to $A$. All columns sum to 1. This $P$ is
*not* symmetric, since $P_{B,A} = 0.5 \neq 0 = P_{A,B}$, but it is *doubly
stochastic* (rows also sum to 1), which is what Section 7.8 actually needs: the
rotation chain rides on that weaker property rather than on symmetry. It returns
in Section 7 with its surprise: started uniformly it never moves.

## 5. Evolution in Time

### 5.1 Theorem 2, by induction

**Theorem 2 ($t$-step evolution).** For every $t \geq 0$: $\pi_t = P^t \pi_0$.

*Proof.* Induction on $t$. Base case $t = 0$: $P^0 = I$ and $\pi_0 = I\pi_0$.
Induction step: assume $\pi_{t-1} = P^{t-1}\pi_0$; then by Theorem 1,

$$ \pi_t = P \pi_{t-1} = P (P^{t-1}\pi_0) = P^t \pi_0, $$

using associativity of matrix multiplication. Homogeneity enters through
Theorem 1's use of the *same* $P$ at every step. **End of proof.**

### 5.2 $t$-step transitions and the Chapman-Kolmogorov equation

First a lemma extending the Markov property from "next step" to "whole future",
used both here and in Section 9.3.

**Lemma B (block Markov property).** For a Markov chain, for any $i$, any
$s \geq 1$, and any positive-probability values: conditioned on $X_i = v$, the
future block $(X_{i+1}, \dots, X_{i+s})$ is independent of the past $X^{i-1}$; in
particular

$$ \Pr(X_{i+s} = u \mid X_i = v, \, X^{i-1} = x^{i-1})
   = \Pr(X_{i+s} = u \mid X_i = v). $$

*Proof.* By Proposition 1, the conditional pmf of the future given the whole
history is a product of one-step factors that depend on the history only through
$v$:

$$ P\left(x_{i+1}, \dots, x_{i+s} \mid x^{i-1}, v\right)
   = \frac{\prod_{j=1}^{i+s} P(x_j \mid x_{j-1})}
          {\prod_{j=1}^{i} P(x_j \mid x_{j-1})}
   = \prod_{j=i+1}^{i+s} P(x_j \mid x_{j-1}), $$

writing $P(x_j \mid x_{j-1})$ for the one-step conditionals, the $j = 1$ factor
unconditional. The right side does not involve $x^{i-1}$, which is precisely
conditional independence of the future block from the past given the present;
summing over intermediate coordinates $x_{i+1}, \dots, x_{i+s-1}$ preserves this
and yields the displayed marginal statement. **End of proof.**

**Proposition 3 ($t$-step transition probabilities; Chapman-Kolmogorov).** For a
homogeneous chain, for all $i, t \geq 0$,

$$ \Pr(X_{i+t} = u \mid X_i = v) = (P^t)_{u,v}, $$

and consequently, for all $s, t \geq 0$,

$$ (P^{s+t})_{u,w} = \sum_{v=1}^{n} (P^s)_{u,v} \, (P^t)_{v,w}. $$

*Proof.* First claim by induction on $t$: trivial at $t = 0$; for the step, split
on the state one step before the end and use total probability, then Lemma B
(with the roles of past and present at times $i$ and $i + t - 1$) to reduce the
conditioning, then homogeneity:

$$ \Pr(X_{i+t} = u \mid X_i = v)
   = \sum_{z} \Pr(X_{i+t} = u \mid X_{i+t-1} = z, X_i = v) \,
     \Pr(X_{i+t-1} = z \mid X_i = v) $$

$$ = \sum_{z} P_{u,z} \, (P^{t-1})_{z,v}
   = (P \cdot P^{t-1})_{u,v} = (P^t)_{u,v}, $$

terms with $\Pr(X_{i+t-1} = z \mid X_i = v) = 0$ being read as 0. The second
claim is now pure algebra, $P^{s+t} = P^s P^t$ written entrywise, but its
probabilistic content is the useful part: to go from $w$ to $u$ in $s + t$ steps,
condition on the state $v$ after the first $t$ steps and sum over it.
**End of proof.**

### 5.3 Numeric evolution

Binary chain, $\alpha = \frac14$, $\pi_0 = [1,0]^\top$. Iterating
$\pi_t = P\pi_{t-1}$ by hand: with $p_t = \Pr(X_t = 0)$, the top row of the
update reads

$$ p_{t+1} = \tfrac34 p_t + \tfrac14 (1 - p_t) = \tfrac14 + \tfrac12 p_t. $$

Five steps, each given as time, then the recursion, then
$(\Pr(X_t = 0), \Pr(X_t = 1))$:

- $t = 0$: initial condition; $(1, \; 0)$.
- $t = 1$: $\frac14 + \frac12 = \frac34$; $(0.75, \; 1/4)$.
- $t = 2$: $\frac14 + \frac38 = \frac58$; $(0.625, \; 3/8)$.
- $t = 3$: $\frac14 + \frac{5}{16} = \frac{9}{16}$;
  $(0.5625, \; 7/16)$.
- $t = 4$: $\frac14 + \frac{9}{32} = \frac{17}{32}$;
  $(0.53125, \; 15/32)$.

The gaps to $\frac12$ are $\frac12, \frac14, \frac18, \frac{1}{16},
\frac{1}{32}$: exactly halving each step, since the recursion gives
$p_{t+1} - \frac12 = \frac12 (p_t - \frac12)$. So in closed form

$$ p_t = \tfrac12 + \tfrac12 \left(\tfrac12\right)^t, $$

and Section 8.5 re-derives this from the eigendecomposition, identifying the
factor $\frac12$ as the second eigenvalue $1 - 2\alpha$. Started at state 1
instead, the mirror-image curve is
$\frac12 - \frac12 (\frac12)^t$, exactly the reflection, by the symmetry of $P$
under swapping the two states. Both curves approach $\frac12$.

## 6. Stationary Processes

### 6.1 Definition, and an equivalence used silently

**Definition (stationary process).** $\mathbf{X}$ is *stationary* if for all
$i \geq 1$ and all window lengths $m \geq 1$,

$$ (X_i, \dots, X_{i+m-1}) \overset{d}{=} (X_{i+1}, \dots, X_{i+m}), $$

where $\overset{d}{=}$ means equality of joint pmfs:
$P_{X_i^{i+m-1}}(x^m) = P_{X_{i+1}^{i+m}}(x^m)$ for every
$x^m \in \mathcal{X}^m$.

Shifting by one step for every window is equivalent to shifting by *any* number
of steps: iterating the definition $k$ times gives
$(X_i, \dots, X_{i+m-1}) \overset{d}{=} (X_{i+k}, \dots, X_{i+k+m-1})$ for all
$k \geq 0$, by induction on $k$, each application shifting the same fixed window
length $m$. This stronger-looking form -- the clock has no origin, all statistics
invariant under any time shift -- is the standard textbook definition
[1, Ch. 4]. Taking $m = 1$: all marginals coincide,
$X_1 \overset{d}{=} X_2 \overset{d}{=} \cdots$. An i.i.d. process is stationary,
its joints being products of one fixed marginal, invariant under shifts.

### 6.2 The random walk is not stationary

Already the $m = 1$ consequence fails. With $X_0 = 0$ and independent $\pm 1$
steps:

- $X_1 = +1$ or $-1$, each with probability $\frac12$.
- $X_2 = +2$ with probability $\frac14$, $0$ with probability $\frac12$, $-2$
  with probability $\frac14$ (two up-down orderings give 0).
- $X_3 = \pm 3$ with probability $\frac18$ each and $\pm 1$ with probability
  $\frac38$ each, since $\binom{3}{1} = 3$ paths out of 8 reach each of
  $\pm 1$.

The supports already differ, so $X_1 \overset{d}{=} X_2$ fails and the process is
not stationary. Quantitatively, the "more random over time" intuition is variance
growth: $X_t$ is a sum of $t$ independent steps of variance 1, so
$\operatorname{Var}(X_t) = t$, since variances of independent summands add.

The walk's state space is infinite, namely $\mathbb{Z}$, which is fine here,
stationarity being defined without finiteness, but note it sits outside the
finite-state standing assumption of Sections 4 to 9; it is used only as a
counterexample.

### 6.3 Markov and stationary are independent axes

**Markov, not stationary:** the random walk (memory one by Lemma A; not
stationary by Section 6.2). Also any chain started off a stationary distribution,
for example the binary chain from $\pi_0 = [1,0]^\top$, where Section 5.3 shows
$\pi_0 \neq \pi_1$.

**Stationary, not Markov of any order:** flip a fair coin once to choose a bias
$B \in \{\frac14, \frac34\}$, each with probability $\frac12$; given $B = b$, let
$X_1, X_2, \dots$ be i.i.d. Bernoulli($b$).

*It is stationary:* for any window, conditioning on $B$ gives a product pmf that
depends only on the window's *values*, not its location:

$$ \Pr(X_i = x_1, \dots, X_{i+m-1} = x_m)
   = \mathbb{E}\left[B^{s} (1-B)^{m-s}\right],
   \qquad s = \sum_j x_j, $$

independent of $i$.

*It is not 1st-order Markov:* with moments $\mathbb{E}[B] = \frac12$,
$\mathbb{E}[B^2] = \frac12(\frac{1}{16} + \frac{9}{16}) = \frac{5}{16}$, and
$\mathbb{E}[B^3] = \frac12(\frac{1}{64} + \frac{27}{64}) = \frac{7}{32}$:

$$ \Pr(X_3 = 1 \mid X_2 = 1)
   = \frac{\mathbb{E}[B^2]}{\mathbb{E}[B]} = \frac{5/16}{1/2} = \frac58, $$

$$ \Pr(X_3 = 1 \mid X_2 = 1, X_1 = 1)
   = \frac{\mathbb{E}[B^3]}{\mathbb{E}[B^2]} = \frac{7/32}{5/16}
   = \frac{7}{10}. $$

Since $\frac58 \neq \frac{7}{10}$, the extra past changes the prediction and the
Markov property fails. The same moment computation with longer histories shows no
finite memory $k$ suffices: every additional observed 1 pushes the posterior on
$B$ further toward $\frac34$. Statistically, the past is evidence about the hidden
$B$, and evidence accumulates forever.

So the two properties are genuinely orthogonal: *short memory* versus
*time-invariant statistics*. Placing "stationary" between $k$th-order Markov and
"practical" on a spectrum is a statement about the *stationary* members of each
class -- an i.i.d. process is a stationary 1st-order Markov chain, and so on. As
the random walk shows, Markov alone does not imply stationary, so the
containments are along the axis of assumption strength for modeling, not set
inclusion of all processes.

## 7. Stationary Distributions

### 7.1 Worked: the rotation chain, uniform start

Initial distribution $\pi_1 = [\frac13, \frac13, \frac13]^\top$ (this example is
indexed from 1, following the source). Who can land on $A$? Only $A$ (stay, with
probability $\frac12$) and $C$ (rotate, with probability $\frac12$):

$$ \Pr(X_2 = A) = \tfrac13 \cdot \tfrac12 + \tfrac13 \cdot \tfrac12
   = \tfrac13. $$

Identically for the others, by the same two-term split ($B$ receives from $A$ and
$B$; $C$ from $B$ and $C$), or in one shot as the matrix product

$$ P\pi_1 = \left[\tfrac16 + \tfrac16, \; \tfrac16 + \tfrac16, \;
   \tfrac16 + \tfrac16\right]^\top
   = \left[\tfrac13, \tfrac13, \tfrac13\right]^\top = \pi_1. $$

So $\pi_t = [\frac13, \frac13, \frac13]^\top$ for all $t$, by induction.

### 7.2 From "marginals never move" to "the process is stationary"

Equal marginals alone do not give equal window distributions in general; what
closes the gap is homogeneity.

**Lemma C.** A homogeneous Markov chain is a stationary process if and only if
its marginals satisfy $\pi_i = \pi_1$ for all $i$, that is, if and only if
$P\pi_1 = \pi_1$.

*Proof.* Forward direction: stationarity with window length 1 gives equal
marginals directly, and Theorem 1 turns "equal for all $i$" into
$P\pi_1 = \pi_1$.

Converse: by Proposition 1 started at index $i$, which is legitimate since by
Lemma B the process from time $i$ onward is again a Markov chain with the same
one-step rule, the pmf of any window is

$$ \Pr(X_i = x_1, X_{i+1} = x_2, \dots, X_{i+m-1} = x_m)
   = \pi_i(x_1) \prod_{j=2}^{m} P_{x_j, x_{j-1}}. $$

The transition factors are the same for every $i$, by homogeneity, and
$\pi_i(x_1) = \pi_1(x_1)$ by hypothesis; so the window pmf does not depend on
$i$, which is stationarity. **End of proof.**

This is the honest content of "a Markov chain becomes a stationary process when
started from the right distribution", and it motivates the central definition.

**Definition (stationary distribution).** A probability vector $\pi^\star$ with

$$ \pi^\star = P \pi^\star. $$

A fixed point of one-step evolution: start there, stay there -- and by Lemma C,
starting there makes the chain a stationary process.

**A pinned start fails.** From $\pi_1 = [1,0,0]^\top$ in the rotation chain, one
multiplication gives $\pi_2 = $ column $A$ of $P = [\frac12, \frac12, 0]^\top
\neq \pi_1$, so $X_1 \overset{d}{=} X_2$ fails and the process is not
stationary. Same matrix, different start, different verdict: stationarity of the
process is a property of the pair (chain, initial distribution).

### 7.3 Irreducible and aperiodic, defined precisely

**Definition (irreducible).** $P$ is irreducible if for every ordered pair of
states $(u,v)$ there exists $t \geq 1$ with $(P^t)_{u,v} > 0$: every state can
reach every state in some number of steps.

**Definition (period, aperiodic).** The period of a state $u$ is
$\gcd\{t \geq 1 : (P^t)_{u,u} > 0\}$, the greatest common divisor of all
possible return times. The chain is aperiodic if every state has period 1. In an
irreducible chain all states share one period [2, Lem. 1.6], so it suffices to
check one state.

Handy sufficient condition: a self-loop, $P_{u,u} > 0$, makes state $u$ have
period 1. Checks for the running examples: the binary chain with
$0 < \alpha < 1$ is irreducible (since $P_{1,0} = \alpha > 0$ and back) and
aperiodic (since $P_{0,0} = 1 - \alpha > 0$); the rotation chain is irreducible
($A \to B \to C \to A$ with positive probability) and aperiodic (self-loops
$\frac12$). The broken cases: an unreachable island state kills irreducibility;
the deterministic 2-cycle, the $\alpha = 1$ binary chain, has return times
$\{2, 4, 6, \dots\}$, hence period 2, killing aperiodicity.

### 7.4 Theorem 3: existence and uniqueness, with the roles of the assumptions separated

The usual statement is "finite-state, irreducible, aperiodic implies a stationary
initial distribution exists", with proof beyond the course. In fact the three
assumptions do three different jobs, and the first two jobs are provable with
only undergraduate tools. Both are done here; aperiodicity is needed only for
*convergence* (Section 8.4).

**Theorem 3a (existence: finiteness alone suffices).** Every finite-state chain,
with no irreducibility or aperiodicity needed, has at least one stationary
distribution.

*Proof (Cesaro averaging).* Pick any $\pi_0 \in \Delta_n$ and let
$\pi_t = P^t \pi_0$. Form the running averages

$$ \mu_T = \frac{1}{T} \sum_{t=0}^{T-1} \pi_t \; \in \; \Delta_n, $$

a convex combination of probability vectors, hence one itself. The simplex
$\Delta_n$ is closed and bounded in $\mathbb{R}^n$, so by Bolzano-Weierstrass
some subsequence $\mu_{T_k} \to \mu \in \Delta_n$. Now compute how far $\mu_T$ is
from being fixed; the sum telescopes:

$$ P\mu_T - \mu_T = \frac{1}{T}\sum_{t=0}^{T-1} (\pi_{t+1} - \pi_t)
   = \frac{\pi_T - \pi_0}{T},
   \qquad \left\| P\mu_T - \mu_T \right\|_1 \leq \frac{2}{T}
   \; \longrightarrow \; 0, $$

since any two probability vectors differ by at most 2 in $\ell_1$ norm. The map
$\mu \mapsto P\mu - \mu$ is continuous, being linear, so along the subsequence
$P\mu - \mu = \lim (P\mu_{T_k} - \mu_{T_k}) = 0$: $\mu$ is stationary.
**End of proof.**

**Theorem 3b (irreducible implies positive and unique).** If $P$ is irreducible,
every stationary distribution has all entries strictly positive, and the
stationary distribution is unique.

*Proof, positivity.* Let $\pi = P\pi$, hence $\pi = P^t\pi$ for all $t$
(Theorem 2 with $\pi_0 = \pi$). Some entry is positive, say $\pi_v > 0$. For any
state $u$, irreducibility supplies $t$ with $(P^t)_{u,v} > 0$, and then

$$ \pi_u = \sum_{w} (P^t)_{u,w} \, \pi_w
   \; \geq \; (P^t)_{u,v} \, \pi_v \; > \; 0. $$

*Proof, uniqueness.* Let $\pi$ and $\mu$ both be stationary; both are entrywise
positive. Set $c = \min_u \pi_u / \mu_u$, attained at some state $u^\ast$, and
let $\nu = \pi - c\mu$. Then $\nu \geq 0$ entrywise, $\nu_{u^\ast} = 0$, and
$P\nu = P\pi - cP\mu = \pi - c\mu = \nu$ by linearity. Suppose $\nu \neq 0$, so
that some $\nu_v > 0$. The positivity argument above used only that $\nu \geq 0$,
$P^t \nu = \nu$, and some entry is positive -- not normalization -- so it applies
verbatim and forces $\nu_{u^\ast} > 0$, a contradiction. Hence $\nu = 0$, that
is $\pi = c\mu$; summing entries, $1 = c \cdot 1$, so $\pi = \mu$.
**End of proof.**

**Counterexamples showing the assumptions are sharp.**

- *Reducible chain, non-unique $\pi^\star$:* $P = I$ on two states. Every
  probability vector is stationary -- existence, consistent with Theorem 3a, but
  a whole segment of fixed points. Long-run behavior then genuinely depends on
  the start.
- *Periodic chain:* the $\alpha = 1$ binary chain, with first row $(0, 1)$ and
  second row $(1, 0)$. It is irreducible, so by Theorems 3a and 3b a unique
  stationary distribution exists, namely $[\frac12, \frac12]^\top$, yet from a
  pinned start the chain *never converges* to it (Section 8.2). Aperiodicity is
  exactly what rules this out; it plays no role in existence or uniqueness.
- *Infinite state space:* the random walk on $\mathbb{Z}$ has *no* stationary
  distribution, by a shift-invariance argument: any fixed point would have to
  give every integer equal mass, and no pmf on infinitely many states can. This
  is where finiteness earns its place.

### 7.5 Eigenvector reading, and where $\lambda = 1$ sits in the spectrum

Comparing $\pi^\star = P\pi^\star$ with $Pv = \lambda v$: a stationary
distribution is an eigenvector of $P$ with eigenvalue 1, normalized to lie in the
simplex, with non-negative entries summing to 1. Two facts, each with a one-line
proof.

**Lemma D.** For any column-stochastic $P$: (i) 1 is an eigenvalue of $P$; (ii)
every eigenvalue $\lambda$ of $P$ satisfies $|\lambda| \leq 1$.

*Proof.* (i) Unit column sums mean $\mathbf{1}^\top P = \mathbf{1}^\top$, so 1 is
an eigenvalue of $P^\top$; a matrix and its transpose have the same
characteristic polynomial, $\det(P - \lambda I) = \det(P^\top - \lambda I)$,
hence the same eigenvalues. An eigen*vector* for 1 lying in the simplex is
supplied by Theorem 3a. (ii) If $Pv = \lambda v$ with $v \neq 0$, take $\ell_1$
norms:

$$ |\lambda| \, \|v\|_1 = \|Pv\|_1
   = \sum_u \left| \sum_w P_{u,w} v_w \right|
   \leq \sum_w |v_w| \sum_u P_{u,w}
   = \|v\|_1, $$

so $|\lambda| \leq 1$, using the triangle inequality, swapping the sums, and unit
column sums. **End of proof.**

This is the elementary edge of the **Perron-Frobenius theorem**, stated honestly
and not proved: for an irreducible non-negative matrix, the spectral radius is
itself an eigenvalue, simple, with an entrywise-positive eigenvector; if in
addition the chain is aperiodic (the matrix is *primitive*), every other
eigenvalue has modulus strictly less than 1 [5, Ch. 8], [2, Ch. 12]. Theorem 3b
above recovers the "simple, positive eigenvector" part for stochastic matrices
without the general machinery; the strict gap $|\lambda_2| < 1$ is what makes the
convergence in Section 8 geometric.

### 7.6 Binary chain: eigen-analysis by hand

**Eigenvalues.**

$$ \det(P - \lambda I) = (1 - \alpha - \lambda)^2 - \alpha^2
   = (1 - 2\alpha - \lambda)(1 - \lambda), $$

by $a^2 - b^2 = (a-b)(a+b)$ with $a = 1 - \alpha - \lambda$ and $b = \alpha$.
Roots: $\lambda_1 = 1$ and $\lambda_2 = 1 - 2\alpha$, which is $\frac12$ at
$\alpha = \frac14$. Both satisfy Lemma D.

**Eigenvector for $\lambda_1 = 1$.** $(P - I)v = 0$ reads
$-\alpha v_1 + \alpha v_2 = 0$, both rows being multiples of this, so
$v_1 = v_2$; normalizing to the simplex,
$\pi^\star = [\frac12, \frac12]^\top$. Multiply-back check at
$\alpha = \frac14$: $P\pi^\star = [\frac38 + \frac18, \frac18 + \frac38]^\top =
[\frac12, \frac12]^\top$.

**Eigenvector for $\lambda_2 = 1 - 2\alpha$.**
$(P - (1-2\alpha)I)v = 0$ reads $\alpha v_1 + \alpha v_2 = 0$, so
$v \propto [1, -1]^\top$. Note $\mathbf{1}^\top v = 0$: eigenvectors for
eigenvalues other than 1 of a column-stochastic matrix always have zero
entry-sum, since $\mathbf{1}^\top v = \mathbf{1}^\top P v = \lambda \,
\mathbf{1}^\top v$ forces $(1 - \lambda) \mathbf{1}^\top v = 0$. This is why the
error direction carries no probability mass.

### 7.7 Rotation chain: stationary solve, plus its full spectrum

The three rows of $\pi^\star = P\pi^\star$:

$$ \pi_A = \tfrac12 \pi_A + \tfrac12 \pi_C, \qquad
   \pi_B = \tfrac12 \pi_A + \tfrac12 \pi_B, \qquad
   \pi_C = \tfrac12 \pi_B + \tfrac12 \pi_C. $$

Subtract $\frac12 \pi_A$ from the first and double: $\pi_A = \pi_C$; likewise
$\pi_B = \pi_A$ and $\pi_C = \pi_B$. All equal; the normalization
$\pi_A + \pi_B + \pi_C = 1$ gives
$\pi^\star = [\frac13, \frac13, \frac13]^\top$, exactly the uniform start of
Section 7.1 -- no coincidence, but now a theorem, by Lemma C. By Theorem 3b it is
the *only* stationary distribution of this chain.

**The other two eigenvalues are complex.** Write $P = \frac12 I + \frac12 C$
where $C$ is the cyclic permutation matrix sending
$A \mapsto B \mapsto C \mapsto A$. $C$ has eigenvalues the cube roots of unity
$1, \omega, \bar\omega$ with $\omega = e^{2\pi i/3}$, so $P$ has eigenvalues
$\frac12(1+1) = 1$ and $\frac12(1 + \omega)$, $\frac12(1 + \bar\omega)$. Their
modulus:

$$ \left| \tfrac12 (1 + \omega) \right|
   = \tfrac12 \left| \tfrac12 + i \tfrac{\sqrt3}{2} \right|
   = \tfrac12 \cdot 1 = \tfrac12, $$

with argument plus or minus 60 degrees. So this chain also forgets its start at
geometric rate $\frac12$ per step, but *spiraling*: the error component rotates
by 60 degrees while shrinking by half each step, which is why its trajectories
circle the uniform point rather than approaching it monotonically. Complex second
eigenvalues are the norm, not the exception, for chains with a preferred
direction of circulation.

### 7.8 The symmetric-$P$ exercise, and the sharper statement

**Exercise.** If $P^\top = P$, the uniform vector
$\pi^\star = [\frac1n, \dots, \frac1n]^\top$ is stationary.

*Solution.* Symmetry converts the always-true unit *column* sums into unit *row*
sums: $\sum_v P_{u,v} = \sum_v P_{v,u} = 1$. Then for each state $u$,

$$ (P\pi^\star)_u = \sum_{v=1}^{n} P_{u,v} \cdot \frac1n
   = \frac1n \sum_{v=1}^{n} P_{u,v} = \frac1n. $$

**End of proof.**

**Sharper statement.** The proof used only unit row sums, so: *uniform is
stationary if and only if $P$ is doubly stochastic*, columns *and* rows summing
to 1. For the "only if" direction, $(P\pi^\star)_u = \frac1n$ forces row sums 1.
Symmetric stochastic matrices are doubly stochastic, but not conversely: the
rotation chain of Section 7.7 is doubly stochastic and asymmetric, which is the
honest reason all three running examples share the uniform fixed point. The
binary chain and Section 9's noising matrix are genuinely symmetric; the rotation
chain rides on the weaker property.

### 7.9 Random surfer

In the PageRank picture, states are pages, transitions follow links, and a page's
score is its entry of $\pi^\star$: where a surfer clicking forever spends its
time. This is an illustration rather than today's math, and correctly so. A raw
web graph is neither irreducible (dead ends, disconnected pieces) nor aperiodic,
so the actual algorithm mixes the link-following matrix with a uniform teleport
matrix,

$$ P_{\text{PR}} = (1 - d) \, P_{\text{links}}
   + d \cdot \tfrac1n \mathbf{1}\mathbf{1}^\top, $$

with damping $d \approx 0.15$, making every entry positive, hence irreducible and
aperiodic, so that Theorem 3 applies and iteration converges [7]. Note the
structural identity with Section 9's noising matrix: both are "mostly structured,
a little uniform", and positivity is doing the same job in both.

## 8. Limiting Distributions

### 8.1 Definition

**Definition (limiting distribution).** If the entrywise limit exists,

$$ \pi_\infty = \lim_{t \to \infty} \pi_t
   = \lim_{t \to \infty} P^t \pi_0. $$

"Entrywise" means each coordinate $(\pi_t)_u$, a sequence of real numbers,
converges. Then $\pi_\infty$ is automatically a probability vector: entries are
limits of non-negative numbers, and
$\sum_u (\pi_\infty)_u = \lim_t \sum_u (\pi_t)_u = 1$, since with finitely many
coordinates limit and finite sum interchange. In general $\pi_\infty$ may depend
on $\pi_0$; for the reducible chain $P = I$, $\pi_\infty = \pi_0$ for every
start.

### 8.2 The limit may not exist: the periodic counterexample

Binary chain at the excluded extreme $\alpha = 1$, always flip. From
$\pi_0 = [1,0]^\top$ the iterates are

$$ [1, 0]^\top \to [0, 1]^\top \to [1, 0]^\top \to [0, 1]^\top \to \cdots, $$

so $(\pi_t)_0 = 1, 0, 1, 0, \dots$ has no limit. This is precisely the period-2
chain of Section 7.3, and it separates two notions worth keeping apart: its
stationary distribution exists and is unique, being $[\frac12, \frac12]^\top$ by
Theorems 3a and 3b since the chain is irreducible, but the limiting distribution
from a pinned start does not exist. Stationary is about *standing still if started
there*; limiting is about *being approached*.

### 8.3 Theorem 4: limits are stationary

**Theorem 4 (limiting implies stationary).** If $\pi_\infty = \lim_t \pi_t$
exists, then $\pi_\infty = P \pi_\infty$.

*Proof.* Take $t \to \infty$ in the identity $\pi_{t+1} = P\pi_t$ (Theorem 1).
Left side: $\{\pi_{t+1}\}$ is the same sequence as $\{\pi_t\}$ shifted by one, so
it has the same limit $\pi_\infty$, a shifted convergent sequence converging to
the same limit. Right side: each entry of $P\pi_t$ is a *finite* linear
combination $\sum_v P_{u,v} (\pi_t)_v$ of convergent real sequences, so it
converges to the same combination of the limits,
$\sum_v P_{u,v} (\pi_\infty)_v = (P\pi_\infty)_u$, by the limit laws for sums and
scalar multiples; equivalently, the linear map $P$ is continuous. Equating the
two limits gives $\pi_\infty = P\pi_\infty$. **End of proof.**

**Implication, stated carefully.** The candidates for long-run behavior are
exactly the solutions of the eigenvector equation, computable without simulation.
The converse fails in two distinct ways: a stationary distribution may exist
while no limit does (the periodic chain, Section 8.2), and limits may exist but
differ by starting point (the reducible chain $P = I$). Ruling out both failure
modes is exactly the job of aperiodicity and irreducibility, which brings us to
the convergence theorem.

### 8.4 The convergence theorem, with a complete elementary proof

Both starts of the binary chain converge to $\pi^\star$; that is a theorem, and
at this level it can be proved in full. The engine is a contraction estimate due
to Doeblin.

**Lemma E (Doeblin contraction).** Suppose every entry of the column-stochastic
matrix $P$ satisfies $P_{u,v} \geq \delta > 0$. Then for any two probability
vectors $\mu, \nu$:

$$ \| P\mu - P\nu \|_1 \; \leq \; (1 - n\delta) \, \| \mu - \nu \|_1. $$

*Proof.* Let $w = \mu - \nu$; its entries sum to 0, since both inputs sum to 1.
Because $\sum_v w_v = 0$, we may subtract the constant $\delta$ from every matrix
entry without changing the product:

$$ (Pw)_u = \sum_v P_{u,v} w_v = \sum_v (P_{u,v} - \delta) \, w_v. $$

Every modified entry $P_{u,v} - \delta$ is non-negative by hypothesis, so the
triangle inequality gives
$|(Pw)_u| \leq \sum_v (P_{u,v} - \delta)|w_v|$. Sum over $u$ and swap the sums:

$$ \|Pw\|_1 \leq \sum_v |w_v| \sum_u (P_{u,v} - \delta)
   = \sum_v |w_v| \, (1 - n\delta) = (1 - n\delta)\|w\|_1, $$

column sums being 1 with each column losing $\delta$ exactly $n$ times. Note
$\delta \leq \frac1n$ always, since a column of $n$ entries each at least
$\delta$ sums to 1; so the factor $1 - n\delta$ lies in $[0,1)$.
**End of proof.**

**Theorem 5 (fundamental convergence theorem, finite case).** Let $P$ be
irreducible and aperiodic on $n$ states, with stationary distribution
$\pi^\star$, unique by Theorems 3a and 3b. Then for *every* initial distribution
$\pi_0$,

$$ \pi_t \; \longrightarrow \; \pi^\star \qquad (t \to \infty), $$

and the convergence is geometric: there are constants $C$ and $\rho < 1$ with
$\|\pi_t - \pi^\star\|_1 \leq C\rho^{\,t}$.

*Proof.* A standard number-theoretic fact, imported: irreducible plus aperiodic
implies some power $P^r$ has *all entries strictly positive* [2, Prop. 1.7]. Let
$\delta > 0$ be the least entry of $P^r$ and $\theta = 1 - n\delta < 1$. Since
$\pi^\star = P^r \pi^\star$, Lemma E applied to $P^r$ gives, for any
$t = qr + s$ with $0 \leq s < r$,

$$ \|\pi_t - \pi^\star\|_1
   = \left\| (P^r)^q (P^s \pi_0) - (P^r)^q \pi^\star \right\|_1
   \leq \theta^{\,q} \, \| P^s\pi_0 - \pi^\star \|_1
   \leq 2 \theta^{\,q} \leq 2 \theta^{\,t/r - 1}, $$

using Lemma E $q$ times, then the crude bound 2 on the $\ell_1$ distance of
probability vectors. This is the claim with $\rho = \theta^{1/r}$ and
$C = 2/\theta$. **End of proof.**

Binary chain reality check: $P$ itself has least entry $\delta = \alpha =
\frac14$ with $n = 2$, so Lemma E contracts by $1 - 2\alpha = \frac12$ per step,
*exactly* the second eigenvalue. For this chain the Doeblin bound is tight, which
the closed form below confirms.

### 8.5 Rate via the second eigenvalue

Decompose the pinned start in the eigenbasis of Section 7.6 and apply $P^t$. In
full, for general $\alpha$ and general start $\pi_0 = [p_0, 1 - p_0]^\top$:

**Decomposition.** $\{\pi^\star, [1,-1]^\top\}$ is a basis of $\mathbb{R}^2$,
eigenvectors for distinct eigenvalues being independent. Writing
$\pi_0 = a \pi^\star + b [1,-1]^\top$ and matching entries:
$a(\frac12) + b = p_0$ and $a(\frac12) - b = 1 - p_0$. Adding gives $a = 1$, the
mass constraint again, only $\pi^\star$ carrying entry-sum; subtracting gives
$b = p_0 - \frac12$. For $p_0 = 1$: $b = \frac12$, that is

$$ [1, 0]^\top = \underbrace{\left[\tfrac12, \tfrac12\right]^\top}_{\pi^\star}
   + \tfrac12 \underbrace{[1, -1]^\top}_{\text{error direction}}, $$

which checks out since $\frac12 + \frac12 = 1$ and $\frac12 - \frac12 = 0$.

**Apply $P^t$**, by linearity and then the eigenvalue action
$P^t v = \lambda^t v$, proved by iterating $Pv = \lambda v$:

$$ \pi_t = P^t \pi_0
   = \pi^\star + \left(p_0 - \tfrac12\right)(1 - 2\alpha)^t \, [1, -1]^\top, $$

that is,

$$ \Pr(X_t = 0) = \tfrac12 + \left(p_0 - \tfrac12\right)(1 - 2\alpha)^t. $$

**Verification at $\alpha = \frac14$, $p_0 = 1$:**
$\Pr(X_t = 0) = \frac12 + \frac12 (\frac12)^t = 1, \frac34, \frac58,
\frac{9}{16}, \frac{17}{32}, \dots$, the Section 5.3 list exactly, and the same
closed form obtained there from the scalar recursion. With $p_0 = 0$, starting at
state 1, $\frac12 - \frac12(\frac12)^t = 0, \frac14, \frac38, \dots$, the
mirror-image curve.

**The general principle.** For an irreducible aperiodic chain, order the
eigenvalues $1 = \lambda_1 > |\lambda_2| \geq \cdots \geq |\lambda_n|$, strict by
Perron-Frobenius (Section 7.5). The error $\pi_t - \pi^\star$ is eventually
dominated by the $\lambda_2$-component, so

$$ \|\pi_t - \pi^\star\| = O\left(t^{m-1} |\lambda_2|^t\right), $$

where $m$ is the multiplicity of $\lambda_2$, the polynomial factor appearing
only when $P$ is not diagonalizable. The gap $1 - |\lambda_2|$ is the *spectral
gap*, the central quantity of mixing-time theory [2, Ch. 12]. Eigenvalue 1 says
where the chain settles; eigenvalue 2 says how fast.

## 9. Discrete Diffusion

### 9.1 The forward (noising) chain

Data first: $X_0 \sim p_0$, the data distribution on $n$ symbols. For sequences
of tokens, apply the construction independently to each coordinate; today's math
is the single-symbol case. The forward process is the homogeneous Markov chain
with the noising matrix: keep the symbol with probability $1 - \epsilon$,
otherwise jump to one of the other $n-1$ symbols uniformly,

$$ P_{u,v} = \begin{cases}
     1 - \epsilon & u = v \\
     \dfrac{\epsilon}{n-1} & u \neq v,
   \end{cases}
   \qquad 0 < \epsilon < 1. $$

**Sanity checks.** Column sums:
$(1 - \epsilon) + (n-1)\cdot\frac{\epsilon}{n-1} = 1$, so it is stochastic.
Symmetry: $P_{u,v} = P_{v,u}$ for all $u,v$. Moreover every entry is strictly
positive, so the chain is irreducible and aperiodic outright, and Theorems 3a,
3b and 5 all apply with $r = 1$.

A form that makes everything below transparent: with $J = \mathbf{1}\mathbf{1}^\top$
the all-ones matrix and $u = \frac1n \mathbf{1}$ the uniform vector,

$$ P = (1 - \beta) \, I + \frac{\beta}{n} J,
   \qquad \beta = \frac{n \epsilon}{n-1}. $$

*Check:* the diagonal is $(1-\beta) + \frac{\beta}{n}
= 1 - \beta\frac{n-1}{n} = 1 - \epsilon$, and the off-diagonal is
$\frac{\beta}{n} = \frac{\epsilon}{n-1}$. Interpretation: with probability
$1 - \beta$ keep the symbol, with probability $\beta$ *resample uniformly from
all $n$ symbols* -- resampling may land on the same symbol, which is why
$\beta > \epsilon$. This uniform-kernel form is exactly the discrete-diffusion
transition of [8, 9, 10].

### 9.2 Pure noise is uniform: stationary, unique, and the exact rate

**Stationarity.** $P$ is symmetric, so by the Section 7.8 exercise the uniform
vector $\pi^\star = u = [\frac1n, \dots, \frac1n]^\top$ is stationary; by
Theorem 3b, irreducible because all entries are positive, it is the *unique*
stationary distribution.

**Exact evolution.** Decompose any start as $\pi_0 = u + (\pi_0 - u)$, where the
error $v = \pi_0 - u$ has $\mathbf{1}^\top v = 1 - 1 = 0$, hence
$Jv = \mathbf{1}(\mathbf{1}^\top v) = 0$. Then

$$ Pv = (1-\beta)v + \frac{\beta}{n} J v = (1 - \beta) v,
   \qquad P u = u, $$

so every zero-sum vector is an eigenvector with eigenvalue
$\lambda_2 = 1 - \beta = 1 - \frac{n\epsilon}{n-1}$, of multiplicity $n-1$, and
by linearity, exactly:

$$ \pi_t = P^t \pi_0
   = u + \left(1 - \frac{n\epsilon}{n-1}\right)^{t} (\pi_0 - u), $$

$$ \|\pi_t - u\|_1
   = \left|1 - \frac{n\epsilon}{n-1}\right|^{t} \, \|\pi_0 - u\|_1
   \leq 2 |\lambda_2|^t. $$

For $0 < \epsilon < 1$ we have $|\lambda_2| < 1$ -- the extreme
$\lambda_2 = -1$ needs $\epsilon = 1$ *and* $n = 2$, the periodic flip chain
again -- so $\pi_t \to u$ geometrically *whatever the data distribution $p_0$
was*. Consistency check at $n = 2$: $\lambda_2 = 1 - 2\epsilon$, the binary
chain's second eigenvalue with $\alpha = \epsilon$.

This upgrades the two qualitative claims -- the limiting distribution is uniform
whatever $p_0$ was, and for large $N$ we have $\pi_N \approx \pi^\star$ -- to a
closed form with an explicit error bound: to make $\|\pi_N - u\|_1 \leq \eta$ it
suffices that

$$ N \geq \frac{\log(2/\eta)}{\log(1/|\lambda_2|)}. $$

That is the principled answer to "how long must the forward chain run": long
enough for $|\lambda_2|^N$ to be negligible. Data dissolving into noise is this
formula in pixels; each step multiplies the structured part of the distribution
by $\lambda_2$.

### 9.3 What the denoiser is really approximating

The learned reverse step is written $X_t \approx f_\theta(X_{t+1}, t)$, and
training data comes free from running the forward chain on real data. The object
being approximated has an exact formula. By Bayes' rule applied to one forward
step,

$$ \Pr(X_t = x \mid X_{t+1} = y)
   = \frac{\Pr(X_{t+1} = y \mid X_t = x) \, \Pr(X_t = x)}{\Pr(X_{t+1} = y)}
   = \frac{P_{y,x} \, \pi_t(x)}{\pi_{t+1}(y)}, $$

whenever $\pi_{t+1}(y) > 0$, guaranteed here for $t \geq 1$ since all entries of
$P$ are positive. Note this *reverse kernel depends on $t$* through $\pi_t$: the
reverse chain is Markov, by the next lemma, but *not homogeneous*, even though
the forward chain is. Early in the forward process $\pi_t$ still resembles the
data and the reverse step must be data-like; late in the process
$\pi_t \approx u$ and the reverse kernel degenerates toward the forward one. This
is exactly why the network takes the step index $t$ as an input.

**Lemma F (reversed chains are Markov).** If $(X_0, \dots, X_N)$ is a Markov
chain, so is the reversed sequence $(X_N, X_{N-1}, \dots, X_0)$.

*Proof.* The Markov property of the forward chain says, by Lemma B, that given
$X_s$ the past $X^{s-1}$ and the future $(X_{s+1}, \dots, X_N)$ are conditionally
independent. Conditional independence is symmetric between the two blocks, since
$P(a, c \mid b) = P(a \mid b) P(c \mid b)$ treats $a$ and $c$ identically. But
"given the present, past and future independent" is also exactly the Markov
property of the *reversed* sequence, whose past is the forward future.
Concretely,

$$ \Pr(X_{s-1} = a \mid X_s = b, X_{s+1} = c_1, \dots, X_N = c_{N-s})
   = \Pr(X_{s-1} = a \mid X_s = b), $$

since given $X_s = b$ the left block $\{X_{s-1} = a\}$ is independent of the
right block. **End of proof.**

So generation by repeatedly undoing steps is not a heuristic: the reverse-time
process is a bona fide inhomogeneous Markov chain, and its transition kernels are
the Bayes posteriors above. What is learned, and where the approximation enters:
the true posterior depends on $p_0$, through $\pi_t = P^t p_0$, which is unknown;
the network $f_\theta(\cdot, t)$ is trained to imitate it from forward-corrupted
data samples.

Two honest gaps between the schematic and practice: (i) real discrete-diffusion
models output a *distribution* over symbols and sample from it, or predict $X_0$
directly and re-noise, rather than a single point estimate
$\tilde X_t = f_\theta(\tilde X_{t+1}, t)$; the training loss is a
cross-entropy-type objective, Lecture 2's loss deployed once per step [8, 9];
(ii) practical schedules make $\epsilon$ depend on $t$, an inhomogeneous forward
chain, and the analysis of Section 9.2 goes through with
$\prod_s \lambda_2(\epsilon_s)$ in place of $\lambda_2^t$.

### 9.4 The generation algorithm, and why it works

**Generation.** (1) Sample $\tilde X_N$ uniform. (2) For $t = N-1, \dots, 0$, set
$\tilde X_t = f_\theta(\tilde X_{t+1}, t)$. (3) Output $\tilde X_0$.

**Why it works, assembled from today's theorems.** The forward chain makes
$\pi_N$ provably close to uniform, by Section 9.2's bound with the rate from
Theorem 5's machinery, so replacing the true $\pi_N$ by the uniform distribution
in step (1) incurs a controlled error, and the uniform distribution is trivially
samplable. If each learned kernel matches the true reverse kernel (Section 9.3),
then by Lemma F running them in sequence reproduces the joint law of the reversed
chain, and the marginal of its final output is exactly $p_0$. Every ingredient --
pure noise is uniform, how large $N$ must be, why undoing steps is legitimate --
is a statement about Markov chains, stationary distributions and limits: the
chain picks its noise distribution for free.

**Pointers, deliberately out of scope here.** This uniform-kernel discrete
diffusion is the framework of Sohl-Dickstein et al. [8] specialized to finite
alphabets, developed as multinomial diffusion by Hoogeboom et al. [10] and
generalized (uniform, absorbing and structured kernels) as D3PM by Austin et al.
[9]. The continuous, Gaussian counterpart, DDPM [11], is Lecture 8, where the
teaser is cashed in with moment-generating-function tools.

## 10. References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 4 covers stationary processes,
   Markov chains and stationary distributions, and is the source notes' primary
   reference; entropy rates, which this lecture stops short of, are also there.
2. D. A. Levin and Y. Peres, with E. L. Wilmer, *Markov Chains and Mixing
   Times*, 2nd ed., American Mathematical Society, 2017. DOI 10.1090/mbk/107
   (https://doi.org/10.1090/mbk/107); free copy at
   https://pages.uoregon.edu/dlevin/MARKOV/. Chapter 1 has irreducibility,
   aperiodicity and Proposition 1.7 used in Theorem 5; Chapter 4 the convergence
   theorem; Chapter 12 the spectral gap and eigenvalue rates.
3. J. R. Norris, *Markov Chains*, Cambridge University Press, 1997. DOI
   10.1017/CBO9780511810633 (https://doi.org/10.1017/CBO9780511810633). Standard
   first course; row-vector convention, so transpose to compare, per
   Section 4.2.
4. R. Durrett, *Probability: Theory and Examples*, 5th ed., Cambridge University
   Press, 2019. DOI 10.1017/9781108591034
   (https://doi.org/10.1017/9781108591034). The measure-theoretic foundations
   used silently in Section 2.1: the Kolmogorov extension theorem, and Markov
   chains in Chapter 5.
5. R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge
   University Press, 2013. Chapter 8 covers Perron-Frobenius theory for
   non-negative matrices, cited at statement level in Section 7.5.
6. O. Kallenberg, *Foundations of Modern Probability*, 3rd ed., Springer, 2021.
   DOI 10.1007/978-3-030-61871-1 (https://doi.org/10.1007/978-3-030-61871-1).
   Alternative source for the extension theorem and for stationarity in full
   generality.
7. S. Brin and L. Page, "The Anatomy of a Large-Scale Hypertextual Web Search
   Engine," *Computer Networks and ISDN Systems*, vol. 30, pp. 107-117, 1998.
   DOI 10.1016/S0169-7552(98)00110-X
   (https://doi.org/10.1016/S0169-7552(98)00110-X). PageRank; the damping
   construction of Section 7.9.
8. J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan and S. Ganguli, "Deep
   Unsupervised Learning using Nonequilibrium Thermodynamics," ICML 2015.
   arXiv:1503.03585 (https://arxiv.org/abs/1503.03585). The original diffusion
   framework, including a binomial, discrete forward chain.
9. J. Austin, D. D. Johnson, J. Ho, D. Tarlow and R. van den Berg, "Structured
   Denoising Diffusion Models in Discrete State-Spaces," NeurIPS 2021.
   arXiv:2107.03006 (https://arxiv.org/abs/2107.03006). D3PM: the uniform
   transition matrix of Section 9.1 is their uniform kernel, up to the
   row-column transpose.
10. E. Hoogeboom, D. Nielsen, P. Jaini, P. Forre and M. Welling, "Argmax Flows
    and Multinomial Diffusion: Learning Categorical Distributions," NeurIPS
    2021. arXiv:2102.05379 (https://arxiv.org/abs/2102.05379). Multinomial
    diffusion: the resample-uniform form of Section 9.1.
11. J. Ho, A. Jain and P. Abbeel, "Denoising Diffusion Probabilistic Models,"
    NeurIPS 2020. arXiv:2006.11239 (https://arxiv.org/abs/2006.11239). DDPM, the
    Gaussian counterpart, treated in Lecture 8.
