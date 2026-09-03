# Deep Learning Math, Lecture 1: Probability Foundations and Entropy

**About this file.** Screen-reader edition of the Lecture 1 companion note. It is
plain Markdown in linear reading order: no figures, no tables of layout, all
mathematics written in LaTeX. Section numbers match the HTML note
(`prob01-foundations-note.html`), so you can refer to "Section 4.3" in class and
mean the same place. Nothing else is needed to read it.

**Notation.** $\log$ means logarithm base 2, and entropies are measured in bits.
$\ln$ is the natural logarithm. Uppercase $X$ is a random variable, lowercase $x$
a value it takes. $p_X$ is the probability mass function of $X$, and
$\mathcal{X}$ its alphabet (the set of values it can take), with
$M = |\mathcal{X}|$. Throughout, $0 \log 0 = 0$.

**Contents.**

1. Why probability
2. Probability review
3. Random variables
4. Entropy
5. Properties of entropy
6. References

## 1. Why Probability?

Every object of deep learning is a probabilistic object. Two claims make this
precise.

**Data are samples.** A dataset $x_1, \dots, x_n$ is modeled as $n$ independent
draws from an unknown distribution $P$ on a sample space $\Omega$ (the space of
all possible images, all possible sentences, and so on). Learning means
inferring structure of $P$, such as its high-mass regions or its conditionals
given a label, from these finitely many draws. The assumption that the draws are
independent and identically distributed is itself a modeling choice: it fails for
time series, for curated datasets, and for feedback loops. Later lectures
(random processes, concentration) study what follows when it holds and what
happens when it is relaxed.

**Models are distributions.** A classifier does not output a label; it outputs a
probability mass function over labels, a so-called soft label. The softmax layer
exists precisely to turn arbitrary real scores into a valid pmf. A generative
model *is* a distribution over $\Omega$ that we can sample from. A reinforcement
learning policy is a conditional distribution over actions given a state.

The technical goal of this lecture is one number: the entropy $H(X)$, which
summarizes how uncertain a distribution is. We establish its exact range,
$0 \leq H(X) \leq \log M$, and the proof technique behind that range, Jensen's
inequality, which recurs all course long: in the non-negativity of KL divergence
(Lecture 2) and in the evidence lower bound of generative modeling.

## 2. Probability Review

### 2.1 Sample space, events, and the event collection

The **sample space** $\Omega$ is the set of all possible outcomes of an
experiment. An **event** $E$ is a subset of $\Omega$; saying "$E$ occurred" means
the realized outcome $\omega$ satisfies $\omega \in E$. The **event collection**
$\mathcal{F}$ is a family of subsets of $\Omega$, namely the events to which we
are willing to assign probabilities.

In a fully rigorous treatment $\mathcal{F}$ must be a **$\sigma$-algebra**:

1. $\Omega \in \mathcal{F}$;
2. if $E \in \mathcal{F}$ then the complement $E^c \in \mathcal{F}$;
3. if $E_1, E_2, \dots \in \mathcal{F}$ then $\bigcup_{i=1}^{\infty} E_i \in \mathcal{F}$.

These closure properties guarantee that logical combinations of legitimate
questions ("not $E$", "$E_1$ or $E_2$") are again legitimate questions.

When $\Omega$ is finite or countable, which covers every example in this lecture,
one may always take $\mathcal{F} = 2^{\Omega}$, the collection of *all* subsets,
and measurability is a non-issue. The distinction only bites for uncountable
$\Omega$, for instance $\Omega = [0,1]$, where not every subset can consistently
be assigned a probability. This course stays discrete until differential entropy
in Lecture 3.

### 2.2 Probability measure: axioms and first consequences

A **probability measure** is a map $P : \mathcal{F} \to [0,1]$ satisfying the
Kolmogorov axioms:

1. $P(E) \geq 0$ for every $E \in \mathcal{F}$;
2. $P(\Omega) = 1$;
3. countable additivity: if $E_1, E_2, \dots$ are pairwise disjoint events, then

$$ P\left(\bigcup_{i=1}^{\infty} E_i\right) = \sum_{i=1}^{\infty} P(E_i). $$

Two familiar facts are consequences of the axioms, not axioms themselves.

**Fact: $P(\emptyset) = 0$.** Take $E_1 = \Omega$ and $E_i = \emptyset$ for
$i \geq 2$ in axiom 3. Then $1 = P(\Omega) = 1 + \sum_{i \geq 2} P(\emptyset)$,
which forces $P(\emptyset) = 0$.

**Fact (monotonicity): a larger event has larger probability.** If
$A \subseteq B$, write $B = A \cup (B \setminus A)$, a disjoint union. Additivity
gives $P(B) = P(A) + P(B \setminus A) \geq P(A)$, since the second term is
non-negative by axiom 1.

The triple $(\Omega, \mathcal{F}, P)$ is the complete probabilistic model. For
finite $\Omega$ with $\mathcal{F} = 2^{\Omega}$, specifying $P$ is the same as
specifying the numbers $P(\{\omega\})$ for each outcome $\omega$, non-negative
and summing to 1; then $P(E) = \sum_{\omega \in E} P(\{\omega\})$.

### 2.3 Example: fair coin

Here $\Omega = \{H, T\}$ and
$\mathcal{F} = \{\emptyset, \{H\}, \{T\}, \{H,T\}\}$, all four subsets. The
measure $P(\emptyset) = 0$, $P(\{H\}) = P(\{T\}) = 1/2$, $P(\{H,T\}) = 1$
satisfies the axioms. Additivity is what forces
$P(\{H,T\}) = P(\{H\}) + P(\{T\}) = 1$, so the only free choice was the single
number $P(\{H\})$.

### 2.4 Example: images as sample spaces, and the counting

A $5 \times 5$ binary image is a point of $\Omega = \{0,1\}^{5 \times 5}$, so
$|\Omega| = 2^{25} \approx 3.4 \times 10^{7}$. Taking the event collection to be
the full power set, and using that a set with $N$ elements has exactly $2^{N}$
subsets (each element is independently in or out), we get
$|\mathcal{F}| = 2^{2^{25}}$: already unimaginably large for a toy image.

**Notation warning.** $[0,1]$ is the real interval, an uncountable set, while
$\{0,1\}$ is a two-element set. A probability measure maps *into* $[0,1]$; binary
pixels live *in* $\{0,1\}$.

The same counting applied to real datasets:

- MNIST: $\Omega = \{0,\dots,255\}^{28 \times 28}$, so
  $|\Omega| = 256^{784} = 2^{6272} \approx 10^{1888}$.
- CIFAR-10: $\Omega = \{0,\dots,255\}^{3 \times 32 \times 32}$, so
  $|\Omega| = 2^{24576} \approx 10^{7398}$.
- ImageNet at $224 \times 224$ RGB: $|\Omega| = 2^{1204224} \approx 10^{362508}$.

The conversion used is $2^{k} = 10^{k \log_{10} 2}$ with
$\log_{10} 2 \approx 0.30103$.

**Why the sizes matter.** The number of atoms in the observable universe is
roughly $10^{80}$. No dataset can ever cover even a vanishing fraction of
$\Omega$, and a uniform distribution over $\Omega$ would make every dataset
useless: a uniformly random pixel array is noise with overwhelming probability.
Real data distributions concentrate enormous mass on a tiny, structured subset,
the natural images. That concentration is exactly the structure a model tries to
learn, and it is why generative modeling is possible at all despite the
astronomical ambient space.

## 3. Random Variables

### 3.1 Definition

A **random variable** is a map $X : \Omega \to \mathbb{R}$: it converts an
outcome into a number. The rigorous definition adds a measurability requirement,
that $\{\omega : X(\omega) \leq t\} \in \mathcal{F}$ for every $t \in \mathbb{R}$,
so that probabilities of statements about $X$ are defined. With
$\mathcal{F} = 2^{\Omega}$ on a discrete space every map is measurable, so the
condition is automatic here.

**Notation.** Uppercase $X$ is the random variable, which is a function;
lowercase $x$ is a realization, which is a number. The expression "$X = x$"
abbreviates the event $\{\omega \in \Omega : X(\omega) = x\}$.

Two examples. On $\Omega = \{0,1\}^{5 \times 5}$, let $X(\omega)$ be the number
of 1-pixels in $\omega$; a small hand-drawn digit "2" on that grid has
$X(\omega) = 11$. On $\Omega = \{H,T\}^{7}$, let $X$ count occurrences of the
pattern $HT$, so $X(HTHTHHH) = 2$. Both illustrate that a random variable
deliberately *discards* information: many distinct outcomes share one value.

### 3.2 Probability mass function

The **probability mass function** (pmf) of $X$ is

$$ p_X(x) = \Pr(X = x) = P\left(\{\omega : X(\omega) = x\}\right). $$

Write $\mathcal{X}$ for the set of values $X$ can take, called its alphabet or
support. Since the events $\{X = x\}$ for $x \in \mathcal{X}$ partition $\Omega$,
additivity gives $\sum_{x \in \mathcal{X}} p_X(x) = 1$, and $p_X(x) \geq 0$
always. Conversely, any such collection of numbers is the pmf of some random
variable.

In this sense the pmf **completely characterizes** the random variable: any
question about probabilities of $X$-values is answered by $p_X$ alone, and the
underlying triple $(\Omega, \mathcal{F}, P)$ is no longer needed. From Section 4
on, we work exclusively with pmfs.

### 3.3 Expectation and the law of the unconscious statistician

The **expectation** of a discrete random variable $X$ is the
probability-weighted average

$$ \mathbb{E}[X] = \sum_{x \in \mathcal{X}} x \, p_X(x), $$

for example $\mathbb{E}[X] = \frac{1}{6}(1+2+3+4+5+6) = 3.5$ for a fair die. For
infinite alphabets the sum must converge absolutely for the expectation to be
well defined; all sums in this lecture do.

The next identity is used constantly, since entropy itself is defined through it.

**Proposition (LOTUS, the law of the unconscious statistician).** For any
function $f : \mathcal{X} \to \mathbb{R}$,

$$ \mathbb{E}[f(X)] = \sum_{x \in \mathcal{X}} f(x) \, p_X(x). $$

*Proof.* Define the new random variable $Y = f(X)$, with alphabet
$\mathcal{Y} = f(\mathcal{X})$. Its pmf is obtained by additivity over the
disjoint events $\{X = x\}$ for $x$ in the preimage $f^{-1}(y)$:

$$ p_Y(y) = \Pr(f(X) = y) = \sum_{x \,:\, f(x) = y} p_X(x). $$

Apply the definition of expectation to $Y$ and substitute:

$$ \mathbb{E}[f(X)] = \sum_{y \in \mathcal{Y}} y \, p_Y(y)
   = \sum_{y \in \mathcal{Y}} \sum_{x \,:\, f(x) = y} y \, p_X(x). $$

Inside the inner sum $y = f(x)$, so this equals

$$ \sum_{y \in \mathcal{Y}} \sum_{x \,:\, f(x) = y} f(x) \, p_X(x)
   = \sum_{x \in \mathcal{X}} f(x) \, p_X(x), $$

the last step because the preimages $f^{-1}(y)$, for $y \in \mathcal{Y}$,
partition $\mathcal{X}$: every $x$ appears in the double sum exactly once.
**End of proof.**

The name is a joke: people apply the formula unconsciously, as if it were the
definition of $\mathbb{E}[f(X)]$, when the definition actually requires first
finding the pmf of $f(X)$. The proposition says the shortcut is legitimate.

## 4. Entropy

Setting for the rest of the lecture: $X$ is a discrete random variable with pmf
$p_X$ on a finite alphabet, canonically $\mathcal{X} = \{0, 1, \dots, M-1\}$,
except where an infinite alphabet is explicitly allowed (Section 4.8).

### 4.1 Surprisal

**Definition (surprisal).** The surprisal of $X$ at the outcome $x$ is

$$ S(x) = \log \frac{1}{p_X(x)} = -\log p_X(x). $$

Motivating example: let $X$ indicate a serious earthquake ($X = 1$) versus a
normal day ($X = 0$). Observing $X = 0$, an outcome with $p_X(0) \approx 1$,
carries essentially no surprise; observing the rare $X = 1$ is very surprising.
Surprise should be large exactly when $p_X(x)$ is small, which $-\log p_X(x)$
delivers: it is 0 at $p = 1$ and tends to $+\infty$ as $p \to 0^{+}$.

### 4.2 Why the logarithm?

Three properties single out $\log(1/p)$ among decreasing functions of $p$.

- **Certainty is unsurprising:** $p = 1$ implies $S = 0$.
- **Monotonicity:** $S$ is strictly decreasing in $p$.
- **Independent surprises add:** if two independent events have probabilities $p$
  and $q$, the pair has probability $pq$, and
  $\log \frac{1}{pq} = \log \frac{1}{p} + \log \frac{1}{q}$.

The logarithm is essentially the only continuous function turning products into
sums (Cauchy's functional equation), so additivity of information across
independent observations forces the log.

There is a deeper axiomatic justification. Shannon's original paper [2] and later
Khinchin-style axiom systems show that continuity, monotonicity in $M$ for
uniform distributions, and a grouping (recursivity) axiom characterize
$H(X) = -\sum p \log p$ up to the base of the logarithm. This course does not
develop the axiomatics. Other information measures exist and are useful, notably
the **Renyi entropy** of order $\alpha \geq 0$, $\alpha \neq 1$:

$$ H_\alpha(X) = \frac{1}{1-\alpha} \log \sum_{x \in \mathcal{X}} p_X(x)^{\alpha}, $$

which recovers Shannon entropy in the limit $\alpha \to 1$ [4].

### 4.3 Entropy: definition and conventions

**Definition (entropy).** The entropy of $X$ is its expected surprisal:

$$ H(X) = \mathbb{E}[S(X)] = \mathbb{E}[-\log p_X(X)]
   = \sum_{x \in \mathcal{X}} p_X(x) \log \frac{1}{p_X(x)}. $$

The middle expression applies LOTUS with $f(x) = -\log p_X(x)$; note that the pmf
appears both as the weighting and inside the function being averaged.

Two conventions.

**Base 2, unit "bits".** All logarithms are base 2 unless stated otherwise. Base
$e$ gives units called nats; since $\log_2 t = \ln t / \ln 2$, entropies convert
by the constant factor $1/\ln 2 \approx 1.4427$, and every theorem in this
lecture is base-independent.

**The convention $0 \log 0 = 0$.** Terms with $p_X(x) = 0$ are defined to
contribute 0; equivalently, the sum runs only over the support
$\{x : p_X(x) > 0\}$. This is not arbitrary, it is continuity:

$$ \lim_{t \to 0^{+}} t \log \frac{1}{t} = 0, $$

because, by l'Hopital's rule,

$$ \lim_{t \to 0^{+}} t \ln t = \lim_{t \to 0^{+}} \frac{\ln t}{1/t}
   = \lim_{t \to 0^{+}} \frac{1/t}{-1/t^{2}} = \lim_{t \to 0^{+}} (-t) = 0. $$

So an impossible outcome adds nothing to the uncertainty, and $H$ is a continuous
function of the pmf on the probability simplex, boundary included. The convention
quietly matters in several proofs below (equality conditions, and the endpoints of
the binary entropy function).

**Two readings of the same number.** Entropy is the *uncertainty* about $X$
before observing it, and equally the *amount of information* gained by observing
it. Resolving uncertainty and acquiring information are the same event viewed
from opposite sides of the observation.

### 4.4 Worked examples

**Fair coin.** With $p_X(H) = p_X(T) = 1/2$, both surprisals equal
$\log 2 = 1$, so

$$ H(X) = \tfrac12 \log 2 + \tfrac12 \log 2 = 1 \text{ bit}. $$

One fair coin toss is the unit of uncertainty.

**Biased coin.** With $p_X(0) = 0.01$ and $p_X(1) = 0.99$,

$$ H(X) = 0.01 \log \frac{1}{0.01} + 0.99 \log \frac{1}{0.99}
   = 0.01 \times 6.644 + 0.99 \times 0.0145 \approx 0.081 \text{ bits}. $$

The rare outcome is individually very surprising ($\log 100 \approx 6.64$ bits)
but carries weight only 0.01; the common outcome is nearly unsurprising. Both
terms are small, for different reasons, so a heavily biased coin is nearly
deterministic in entropy terms. Comparing the two coins, $H = 1$ bit against
$H \approx 0.081$ bits, agrees with the intuition that the fair coin is far more
uncertain.

**Binary entropy function.** For $X \sim \mathrm{Bernoulli}(p)$,

$$ h_2(p) = -p \log p - (1-p) \log (1-p). $$

Its graph on $[0,1]$ is a symmetric dome: $h_2(0) = h_2(1) = 0$ (by the
$0 \log 0$ convention), it satisfies $h_2(p) = h_2(1-p)$ because swapping the
labels of the two outcomes cannot change uncertainty, and it peaks at $p = 1/2$
with $h_2(1/2) = 1$. The peak is a special case of the maximum-entropy theorem
below, or of the concavity computed in Section 5.2. For instance
$h_2(0.01) \approx 0.081$, as above.

**Fair die.** Uniform on 6 faces, $p_X(x) = 1/6$, every surprisal equals
$\log 6$, so

$$ H(X) = \sum_{x=1}^{6} \tfrac16 \log 6 = \log 6 \approx 2.585 \text{ bits}. $$

In general a uniform distribution on $M$ values has entropy exactly $\log M$: the
constant surprisal makes the average trivial. This is the equality case of
Theorem 3.

**Three outcomes.** The pmf $p = (1/2, 1/4, 1/4)$ has surprisals $(1, 2, 2)$
bits, so

$$ H(X) = \tfrac12 \cdot 1 + \tfrac14 \cdot 2 + \tfrac14 \cdot 2 = 1.5 \text{ bits}, $$

between the fair coin (1 bit) and the uniform distribution on 3 symbols
($\log 3 \approx 1.585$ bits). Dyadic pmfs like this one, with all masses powers
of $1/2$, are exactly those whose surprisals are integers; they reappear when
entropy is connected to optimal code lengths [1, Ch. 5].

### 4.5 The guessing game

Alice picks a number uniformly from $\{0, \dots, 7\}$ and Bob asks yes/no
questions. Compare two questions:

- Q1: "Is your number in $\{0,1,2,3\}$?" The answer is yes with probability
  $1/2$.
- Q2: "Is your number in $\{3,6\}$?" The answer is yes with probability $1/4$.

The *answer* to each question is itself a binary random variable, and its entropy
measures how much Bob expects to learn:

$$ H(\text{answer to Q1}) = h_2(\tfrac12) = 1 \text{ bit}, $$

$$ H(\text{answer to Q2}) = h_2(\tfrac14)
   = \tfrac14 \cdot 2 + \tfrac34 \log \tfrac43 \approx 0.811 \text{ bits}. $$

Q1 is the more informative question. A question whose answer Bob can already
half-guess, and Q2 is "no" three times out of four, teaches him less on average.
A perfectly balanced question extracts the maximum of 1 bit per answer.

**Twenty-questions view.** Balanced questions build a binary tree. The root holds
all eight candidates, each question splits every node in half, and after three
levels each leaf holds a single number; the candidate set shrinks
$8 \to 4 \to 2 \to 1$. Bob's answers trace one root-to-leaf path. For Alice's
number 5: "in $\{1,2,3,4\}$?" no, "in $\{5,6\}$?" yes, "is it 5?" yes, so the
three answers form a 3-bit string naming the leaf. Each question is worth exactly
one bit in two senses that agree here: the answer is $\mathrm{Bernoulli}(1/2)$,
whose entropy is $h_2(1/2) = 1$, and the candidate set halves. Consistently,
$H(X) = \log 8 = 3$ bits for uniform Alice.

This is the operational meaning of entropy, made precise by source-coding theory:
entropy is the average number of optimal yes/no questions, equivalently code
bits, needed to determine $X$ [1, Ch. 5]. For non-uniform $X$ the statement holds
up to less than one extra question per symbol, and is exact in the dyadic case.

**Converse: no strategy can do better.** A deterministic strategy asking $k$
yes/no questions produces at most $2^{k}$ distinct answer strings. If it always
identifies $X$, distinct outcomes must produce distinct strings, so
$2^{k} \geq |\mathcal{X}| = 8$, that is $k \geq \log 8 = 3$. An unbalanced
question does strictly worse on average: its answer has entropy $h_2(q) < 1$ for
$q \neq 1/2$, so it removes less than one bit of the $\log 8$ bits of uncertainty
and more questions are needed in expectation.

### 4.6 Two dice

Two pmfs on the same six faces:

- $D_1 = (1/9, 1/9, 1/9, 2/9, 2/9, 2/9)$, mildly non-uniform: three faces carry
  $1/9$ each and three carry $2/9$ each, so the bar chart is nearly flat.
- $D_2 = (1/2, 1/4, 1/8, 1/16, 1/32, 1/32)$, strongly concentrated and dyadic: a
  halving staircase in which one face alone carries half the mass.

Their entropies:

$$ H(D_1) = 3 \cdot \tfrac19 \log 9 + 3 \cdot \tfrac29 \log \tfrac92
   = \tfrac13 \log 9 + \tfrac23 \log 4.5 \approx 1.057 + 1.447 \approx 2.503 \text{ bits}, $$

$$ H(D_2) = \tfrac12 \cdot 1 + \tfrac14 \cdot 2 + \tfrac18 \cdot 3
   + \tfrac{1}{16} \cdot 4 + \tfrac{1}{32} \cdot 5 + \tfrac{1}{32} \cdot 5
   = \frac{31}{16} \approx 1.938 \text{ bits}. $$

$D_1$ is the more uncertain die because it is closer to uniform. Both entropies
sit below $\log 6 \approx 2.585$, foreshadowing the maximum-entropy theorem.
Flatness of the pmf is exactly what the number scores.

### 4.7 Examples from AI

**Classifier soft labels.** A digit classifier over labels $\{0,\dots,4\}$
outputs a pmf $f(x)$, a soft guess much like a weather forecast. For two images:

$$ f(x_1) = (0.6, 0.1, 0.1, 0.1, 0.1), \qquad
   H(f(x_1)) = 0.6 \log \tfrac{1}{0.6} + 4 \times 0.1 \log 10 \approx 1.771 \text{ bits}, $$

$$ f(x_2) = (0.4, 0.4, 0.2, 0, 0), \qquad
   H(f(x_2)) = 2 \times 0.4 \log 2.5 + 0.2 \log 5 \approx 1.522 \text{ bits}, $$

where the two zero entries of $f(x_2)$ contribute nothing by the $0 \log 0$
convention. Entropy ranks $x_1$ as the harder sample: its mass is spread over all
five labels, while $f(x_2)$ has effectively a three-label support. The comparison
is not obvious by inspection, since $f(x_2)$ has the smaller gap between its two
leading probabilities, which is precisely why a scalar summary is useful.

**Data valuation and active learning.** Which unlabeled sample is most helpful to
train on next? One classical answer scores each candidate by the entropy of the
model's current soft label and prioritizes high-entropy, most-confused samples,
on the grounds that these are the ones the model can learn most from. This is
uncertainty sampling [6].

**Exploration versus exploitation.** Strip reinforcement learning down to its
smallest interesting case, the $K$-armed bandit [7]. There are $K$ strategies
called arms; arm $a$ pays a random reward with unknown mean $\mu_a$. At each
round $t$ the learner picks $A_t$ and observes one noisy sample $R_t$ with
$\mathbb{E}[R_t \mid A_t = a] = \mu_a$. Performance is measured by *regret*
against the best fixed arm:

$$ \mathcal{R}_T = T \max_a \mu_a - \sum_{t=1}^{T} \mathbb{E}[\mu_{A_t}]. $$

The tension is structural: the only way to learn $\mu_a$ is to play $a$. After
$n_a$ pulls the estimate $\hat\mu_a$ carries a confidence width of order
$\sqrt{\log T / n_a}$, which shrinks only for arms the learner keeps choosing. A
purely greedy learner, always playing $\arg\max_a \hat\mu_a$, can therefore lock
onto a suboptimal arm permanently: one unlucky early sample of the genuinely best
arm $B$ drags $\hat\mu_B$ down, $B$ is never pulled again, and the error is never
corrected.

A concrete picture of that state: arm $A$ has 40 pulls and a tight confidence
interval around a good value; arm $B$ has 3 pulls and an interval so wide that its
upper end sits above $A$'s estimate. Arm $B$ *might* be better, and no amount of
thinking settles it; only rounds spent on $B$ do.

Both sides of the trade cost something. Pulling $B$ gives up the reward $A$ would
reliably have paid, an exploration cost that is bounded and one-off. Never
pulling $B$ risks a fixed per-round shortfall $\mu_B - \mu_A$ for the rest of
time, which is linear regret. Lai and Robbins showed the trade-off cannot be
dodged: any strategy that is uniformly good must pull each suboptimal arm
$\Omega(\log T)$ times [8]. Upper-confidence-bound rules, which play the arm with
the largest $\hat\mu_a + \sqrt{2 \log t / n_a}$ and are thus optimistic in the
face of uncertainty, match that rate [9]. The $\varepsilon$-greedy rule and
Thompson sampling are the other standard answers. Full reinforcement learning
adds states and delayed rewards on top, but the dilemma is already complete here.

This is where entropy enters. Rather than hand-tuning when to deviate, modern
deep reinforcement learning objectives add an entropy bonus
$\beta H(\pi(\cdot \mid s))$ to the reward; this is entropy regularization in A3C
and PPO, and soft actor-critic maximizes reward *plus* policy entropy [10]. A
high-entropy policy keeps probability on every action, so every action's estimate
keeps improving, and exploration becomes a term in the objective instead of a
heuristic.

**Explorativeness of a policy.** With strategies $\{A, B, C, D, E\}$ and a
current belief that $A$ is best, compare two stochastic policies
$S_1 = (0.6, 0.1, 0.1, 0.1, 0.1)$ and $S_2 = (0.4, 0.4, 0.2, 0, 0)$. These are
numerically the same pmfs as the soft labels above, so
$H(S_1) \approx 1.771 > H(S_2) \approx 1.522$. Policy $S_1$ is the more
explorative one: it reserves probability for every option, while $S_2$ can never
try $D$ or $E$.

### 4.8 Exercise: geometric distribution, solved

Let $X$ be geometric with $p = 1/2$, so $p_X(x) = 2^{-x}$ for
$x \in \{1, 2, 3, \dots\}$. This is a valid pmf since
$\sum_{x \geq 1} 2^{-x} = 1$. It is our first infinite-alphabet example, so the
entropy sum is an infinite series and convergence must be checked.

The surprisal of outcome $x$ is $\log 2^{x} = x$ bits, exactly the outcome
itself. Hence

$$ H(X) = \sum_{x=1}^{\infty} p_X(x) \cdot x = \mathbb{E}[X]. $$

It remains to evaluate $\mathbb{E}[X] = \sum_{x \geq 1} x \, 2^{-x}$. Let
$T = \sum_{x=1}^{\infty} x \, 2^{-x}$, which converges by the ratio test. Then

$$ T - \tfrac12 T = \sum_{x=1}^{\infty} x \, 2^{-x}
   - \sum_{x=1}^{\infty} x \, 2^{-(x+1)}
   = \sum_{x=1}^{\infty} x \, 2^{-x} - \sum_{x=2}^{\infty} (x-1) \, 2^{-x}
   = \sum_{x=1}^{\infty} 2^{-x} = 1, $$

so $T/2 = 1$, giving $\mathbb{E}[X] = 2$ and therefore $H(X) = 2$ bits.
**End of proof.**

**Remark.** This is an infinite alphabet with finite entropy. Note
$\log |\mathcal{X}| = \infty$ here, so the maximum-entropy bound of Section 5 is
vacuous; it genuinely requires finite $M$ to say anything. There even exist pmfs
on $\{1,2,\dots\}$ with $H(X) = \infty$, for example
$p_X(x) \propto 1/(x \log^{2} x)$, so finiteness of entropy on infinite alphabets
is a real hypothesis, not a formality.

## 5. Properties of Entropy

### 5.1 Theorem 1: non-negativity

**Theorem 1.** $H(X) \geq 0$, with equality if and only if $X$ is deterministic,
that is $p_X(x^{*}) = 1$ for a single value $x^{*}$.

*Proof.* Every probability satisfies $0 \leq p_X(x) \leq 1$, so
$1/p_X(x) \geq 1$ on the support and every surprisal is at least $\log 1 = 0$. An
expectation of a non-negative random variable is non-negative:

$$ H(X) = \mathbb{E}\left[\log \frac{1}{p_X(X)}\right] \geq \mathbb{E}[\log 1] = 0. $$

*Equality.* $H(X) = \sum_x p_X(x) \log \frac{1}{p_X(x)}$ is a sum of non-negative
terms, so it vanishes if and only if every term vanishes, that is
$p_X(x) \log \frac{1}{p_X(x)} = 0$ for all $x$, which means every $p_X(x)$ is 0 or
1. Indeed the factor $p_X(x)$ kills the term at 0, by the $0 \log 0$ convention,
and the logarithm kills it at 1, while strictly in between both factors are
strictly positive. Since the masses sum to 1 and each is 0 or 1, exactly one
value $x^{*}$ has $p_X(x^{*}) = 1$: $X$ is deterministic. Conversely a
deterministic $X$ has the single term $1 \cdot \log 1 = 0$. **End of proof.**

So zero entropy characterizes "no randomness at all". The next question is which
pmf sits at the *top* of the scale. The dome shape of $h_2$ suggests the uniform
one; proving it needs a tool.

### 5.2 Background: convexity and concavity

**Definition.** A function $f : I \to \mathbb{R}$ on an interval $I$ is
**convex** if for all $x, y \in I$ and all $\lambda \in [0,1]$,

$$ \lambda f(x) + (1-\lambda) f(y) \geq f(\lambda x + (1-\lambda) y), $$

and **concave** if the reverse inequality ($\leq$) holds. Geometrically, convex
means every chord lies on or above the graph, and concave means every chord lies
on or below it. The function is *strictly* convex or concave if the inequality is
strict whenever $x \neq y$ and $0 < \lambda < 1$. Note $f$ is concave if and only
if $-f$ is convex. Standard examples: $x^{2}$ is convex, and $\log x$ and
$h_2(p)$ are concave.

**Lemma (second-derivative test).** If $f$ is twice differentiable on an interval
and $f''(t) \leq 0$ throughout, then $f$ is concave; if $f''(t) < 0$ throughout,
$f$ is strictly concave. The signs reverse for convexity.

*Proof.* Fix $x < y$ and $\lambda \in (0,1)$, and let
$z = \lambda x + (1-\lambda) y$, so that $z - x = (1-\lambda)(y-x)$ and
$y - z = \lambda (y-x)$, both positive. By the mean value theorem there are
$\xi_1 \in (x, z)$ and $\xi_2 \in (z, y)$ with

$$ f(z) - f(x) = f'(\xi_1)(z-x), \qquad f(y) - f(z) = f'(\xi_2)(y-z). $$

Since $f'' \leq 0$, the derivative $f'$ is non-increasing, and $\xi_1 < \xi_2$
gives $f'(\xi_1) \geq f'(\xi_2)$. Therefore

$$ \lambda (f(z) - f(x)) = \lambda (1-\lambda)(y-x) f'(\xi_1)
   \geq \lambda (1-\lambda)(y-x) f'(\xi_2) = (1-\lambda)(f(y) - f(z)), $$

and rearranging yields $f(z) \geq \lambda f(x) + (1-\lambda) f(y)$, which is
concavity. If $f'' < 0$ then $f'$ is strictly decreasing, the middle inequality
is strict, and $f$ is strictly concave. **End of proof.**

**The key example.** On $(0,\infty)$ the function $f(t) = \log t$ has
$f''(t) = -1/(t^{2} \ln 2) < 0$, so the logarithm is *strictly* concave. This
single fact powers Theorem 3 and, in Lecture 2, the non-negativity of KL
divergence.

**Exercise, solved: $h_2$ is concave.** For $p \in (0,1)$, differentiate
$h_2(p) = -p \log p - (1-p) \log(1-p)$:

$$ h_2'(p) = -\log p - \frac{1}{\ln 2} + \log (1-p) + \frac{1}{\ln 2}
   = \log \frac{1-p}{p}, $$

$$ h_2''(p) = \frac{1}{\ln 2}\left(-\frac{1}{1-p} - \frac{1}{p}\right)
   = -\frac{1}{p(1-p)\ln 2} < 0. $$

So $h_2$ is strictly concave on $(0,1)$, and by continuity with the endpoint
convention it is concave on $[0,1]$. As a byproduct $h_2'(p) = 0$ if and only if
$p = 1/2$, confirming the peak at the fair coin. The convexity of $x^{2}$ is the
same test: $(x^{2})'' = 2 > 0$.

### 5.3 Theorem 2: Jensen's inequality

**Theorem 2 (Jensen [3]).** Let $f$ be concave and let $X$ be a random variable
taking finitely many values in the domain of $f$. Then

$$ \mathbb{E}[f(X)] \leq f(\mathbb{E}[X]). $$

For convex $f$ the inequality reverses. If $f$ is strictly concave, equality
holds if and only if $X$ is constant, that is, all its probability mass sits on
one point.

**How to read it.** Concavity compares a two-point mixture with the function
value at the two-point average. Jensen upgrades this to an arbitrary pmf: the
weighted average of function values, $\mathbb{E}[f(X)] = \sum_i p_i f(x_i)$,
never exceeds the function evaluated at the weighted average input,
$f(\sum_i p_i x_i)$. Jensen is the many-point generalization of the definition,
and the proof is exactly an induction that reduces many points to two.

*Proof (induction on the support size $M$).* The claim for a pmf
$(p_1, \dots, p_M)$ on points $(x_1, \dots, x_M)$ reads

$$ \sum_{i=1}^{M} p_i f(x_i) \leq f\left(\sum_{i=1}^{M} p_i x_i\right). $$

*Base case $M = 1$:* both sides equal $f(x_1)$.

*Base case $M = 2$:* with $p_2 = 1 - p_1$ the claim reads

$$ p_1 f(x_1) + (1-p_1) f(x_2) \leq f(p_1 x_1 + (1-p_1) x_2), $$

which is precisely the definition of concavity with $\lambda = p_1$.

*Induction step.* Assume the claim for every pmf on $M-1$ points and take a pmf
on $M$ points. If $p_M = 1$ the claim is the trivial $M = 1$ case, so assume
$p_M < 1$ and peel off the $M$-th atom:

$$ \sum_{i=1}^{M} p_i f(x_i)
   = p_M f(x_M) + (1-p_M) \sum_{i=1}^{M-1} q_i f(x_i),
   \qquad q_i = \frac{p_i}{1-p_M}. $$

The renormalized weights satisfy $q_i \geq 0$ and
$\sum_{i=1}^{M-1} q_i = (1-p_M)/(1-p_M) = 1$, so they form a valid pmf on $M-1$
points. Apply the induction hypothesis to the inner sum:

$$ p_M f(x_M) + (1-p_M) \sum_{i=1}^{M-1} q_i f(x_i)
   \leq p_M f(x_M) + (1-p_M) f\left(\sum_{i=1}^{M-1} q_i x_i\right). $$

Then apply two-point concavity with $\lambda = p_M$ to recombine:

$$ p_M f(x_M) + (1-p_M) f\left(\sum_{i=1}^{M-1} q_i x_i\right)
   \leq f\left(p_M x_M + (1-p_M) \sum_{i=1}^{M-1} q_i x_i\right)
   = f\left(\sum_{i=1}^{M} p_i x_i\right), $$

the last equality because $(1-p_M) q_i = p_i$. This is
$\mathbb{E}[f(X)] \leq f(\mathbb{E}[X])$. **End of proof.**

**Equality for strictly concave $f$.** If $X$ is constant, both sides are $f$ of
that constant, so equality holds. Conversely, suppose $X$ takes two distinct
values $x \neq y$ with positive probabilities. Group the outcomes: run the
argument with mass $p = \Pr(X = x) > 0$ on $x$ and mass $1-p$ on the conditional
mixture of everything else. Tracing the induction, the final recombination step
applies two-point concavity to two distinct points with interior weight, which is
*strict* for strictly concave $f$; hence
$\mathbb{E}[f(X)] < f(\mathbb{E}[X])$.

A slicker proof in the differentiable case, worth remembering: strict concavity
gives the supporting-line bound $f(t) \leq f(m) + f'(m)(t-m)$ with equality only
at $t = m$, where $m = \mathbb{E}[X]$; now take expectations of both sides.

**Why we care.** Today it gives maximum entropy. Next lecture it gives
$D(P \Vert Q) \geq 0$. Throughout machine learning, whenever an expectation is
trapped under a logarithm, as in log-likelihoods and the evidence lower bound,
Jensen moves the expectation inside at the cost of an inequality in a known
direction.

### 5.4 Theorem 3: maximum entropy

**Theorem 3.** For a random variable $X$ on a finite alphabet $\mathcal{X}$ with
$|\mathcal{X}| = M$,

$$ H(X) \leq \log |\mathcal{X}| = \log M, $$

with equality if and only if $X$ is uniform on $\mathcal{X}$, that is
$p_X(x) = 1/M$ for all $x$.

*Proof.* A subtlety first: we may assume $p_X(x) > 0$ for all
$x \in \mathcal{X}$. If some values had zero mass, restrict to the support
$\mathcal{X}' = \{x : p_X(x) > 0\}$. By the $0 \log 0$ convention $H$ is
unchanged, and $\log |\mathcal{X}'| \leq \log M$, so proving the bound on the
support proves it on $\mathcal{X}$. This also shows equality forces full support,
as discussed below.

Apply Jensen to the positive random variable $1/p_X(X)$, using the strictly
concave function $\log$:

$$ H(X) = \mathbb{E}\left[\log \frac{1}{p_X(X)}\right]
   \leq \log \mathbb{E}\left[\frac{1}{p_X(X)}\right]. $$

Evaluate the inner expectation by LOTUS (Section 3.3) with $f(x) = 1/p_X(x)$; the
pmf cancels itself:

$$ \mathbb{E}\left[\frac{1}{p_X(X)}\right]
   = \sum_{x \in \mathcal{X}} p_X(x) \cdot \frac{1}{p_X(x)}
   = \sum_{x \in \mathcal{X}} 1 = M. $$

Combining the two displays gives $H(X) \leq \log M$. **End of proof.**

*Equality.* The only inequality used was Jensen with the strictly concave $\log$,
which is tight if and only if the random quantity inside is constant:
$1/p_X(x) = c$ for all $x$ in the support, that is $p_X(x) = 1/c$ there. Summing
to 1 over the support forces $c$ to equal the size of the support; and to reach
the full bound $\log M$, rather than the logarithm of a smaller support, the
support must be all of $\mathcal{X}$. Hence $p_X(x) = 1/M$ for every $x$: the
uniform distribution. Conversely the uniform distribution attains $H = \log M$ by
the fair-die computation. **End of proof.**

*Sanity checks.* Fair coin: $H = 1 = \log 2$, tight because uniform. Biased coin:
$0.081 < 1$. The two dice: $H(D_1) \approx 2.503$ and $H(D_2) \approx 1.938$,
both below $\log 6 \approx 2.585$, with the flatter $D_1$ closer to the ceiling.
Fair die: exactly $\log 6$, tight. Soft labels: 1.771 and 1.522, both below
$\log 5 \approx 2.322$. The theorem also explains the guessing game: a uniform
Alice is the hardest opponent, since $\log M$ is simultaneously the number of
bits needed to index $M$ items and the entropy of a uniform pick, and any
non-uniform strategy of Alice's would lower the entropy and give Bob structure to
exploit.

*Scale of uncertainty.* Theorems 1 and 3 together bracket every pmf on $M$
symbols,

$$ 0 \leq H(X) \leq \log M, $$

with the deterministic distributions at the floor and the uniform distribution
alone at the ceiling. Entropy turns the question "how random is this pmf?" into a
position on one axis.

### 5.5 Bridge to Lecture 2

The surprisal $\log \frac{1}{p_X(x)}$ uses the *true* pmf. A learned model only
has a guess $Q$, so one can ask how $\mathbb{E}[\log \frac{1}{Q(X)}]$, the
*cross-entropy* of $Q$ against $p_X$, compares with $H(X)$. The same Jensen
pattern applied to $\mathbb{E}[\log \frac{Q(X)}{p_X(X)}]$ shows the mismatched
description is never cheaper:

$$ \mathbb{E}\left[\log \frac{1}{Q(X)}\right] \geq H(X), $$

with equality if and only if $Q = p_X$, and the gap defines the KL divergence
$D(p_X \Vert Q) \geq 0$. That theorem, its $p_X(x) = 0$ edge case, and the
gambling interpretation are the content of Lecture 2 (`prob02-kl-crossentropy`)
and its note.

## 6. References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 2 covers entropy and its
   properties, Chapter 5 source coding and the twenty-questions interpretation,
   Chapter 6 gambling.
2. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System
   Technical Journal*, vol. 27, pp. 379-423 and 623-656, 1948. DOI
   10.1002/j.1538-7305.1948.tb01338.x
   (https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). Origin of entropy and
   of the axiomatic characterization of $-\sum p \log p$.
3. J. L. W. V. Jensen, "Sur les fonctions convexes et les inegalites entre les
   valeurs moyennes," *Acta Mathematica*, vol. 30, pp. 175-193, 1906. DOI
   10.1007/BF02418571 (https://doi.org/10.1007/BF02418571). Jensen's inequality.
4. A. Renyi, "On Measures of Entropy and Information," in *Proceedings of the
   Fourth Berkeley Symposium on Mathematical Statistics and Probability*, vol. 1,
   pp. 547-561, University of California Press, 1961. The Renyi entropy family.
5. D. J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*,
   Cambridge University Press, 2003. Free online at
   https://www.inference.org.uk/mackay/itila/. A gentler parallel treatment of
   entropy, surprisal, and the guessing-game view.
6. B. Settles, "Active Learning Literature Survey," Computer Sciences Technical
   Report 1648, University of Wisconsin-Madison, 2009.
   https://burrsettles.com/pub/settles.activelearning.pdf. Entropy-based
   uncertainty sampling.
7. R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd
   ed., MIT Press, 2018. Free online at
   http://incompleteideas.net/book/the-book-2nd.html. Chapter 2 covers the
   $K$-armed bandit, the exploration-exploitation dilemma, $\varepsilon$-greedy
   and UCB.
8. T. L. Lai and H. Robbins, "Asymptotically Efficient Adaptive Allocation
   Rules," *Advances in Applied Mathematics*, vol. 6, no. 1, pp. 4-22, 1985. DOI
   10.1016/0196-8858(85)90002-8
   (https://doi.org/10.1016/0196-8858(85)90002-8). The $\Omega(\log T)$ regret
   lower bound: exploration is provably unavoidable.
9. P. Auer, N. Cesa-Bianchi, and P. Fischer, "Finite-time Analysis of the
   Multiarmed Bandit Problem," *Machine Learning*, vol. 47, pp. 235-256, 2002.
   DOI 10.1023/A:1013689704352 (https://doi.org/10.1023/A:1013689704352). UCB1
   and its $O(\log T)$ regret.
10. T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, "Soft Actor-Critic:
    Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic
    Actor," ICML 2018. arXiv:1801.01290 (https://arxiv.org/abs/1801.01290).
    Policy entropy as an explicit term in the RL objective.
11. Datasets mentioned in Section 2.4: MNIST (Y. LeCun, C. Cortes, C. J. C.
    Burges, http://yann.lecun.com/exdb/mnist/); CIFAR-10 (A. Krizhevsky,
    "Learning Multiple Layers of Features from Tiny Images," 2009,
    https://www.cs.toronto.edu/~kriz/cifar.html); ImageNet (J. Deng et al.,
    "ImageNet: A Large-Scale Hierarchical Image Database," CVPR 2009, DOI
    10.1109/CVPR.2009.5206848, https://doi.org/10.1109/CVPR.2009.5206848).
