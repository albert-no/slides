# Deep Learning Math, Lecture 3: Mutual Information and Data Processing

**About this file.** Screen-reader edition of the Lecture 3 companion note. Plain
Markdown in linear reading order, all mathematics in LaTeX. Section numbers match
the HTML note (`prob03-mutual-information-note.html`). Tables in the HTML note are
written out here as labelled lists, cell by cell. Nothing else is needed to read
it.

**Notation.** $\log$ is base 2 and information is in bits. $p_{X,Y}$ is a joint
pmf, $p_X$ and $p_Y$ its marginals, $p_{X|Y}$ a conditional pmf. $H$ is entropy,
$h$ differential entropy, $D(\cdot \Vert \cdot)$ the KL divergence (`\Vert` is the
double bar), $I(X;Y)$ mutual information with a semicolon between its arguments.
$h_2(p) = p \log \frac{1}{p} + (1-p) \log \frac{1}{1-p}$ is the binary entropy
function. $X \perp Y$ means "$X$ and $Y$ are independent"; $X - Y - Z$ means "the
triple is a Markov chain". $X^n = (X_1, \dots, X_n)$, and $X^{i-1}$ is the first
$i-1$ coordinates. $\oplus$ is XOR (addition modulo 2).

**Background used.** Entropy, LOTUS, Jensen and maximum entropy from Lecture 1;
KL divergence, the information inequality and cross-entropy from Lecture 2. These
are cited, not re-proved.

**Contents.**

1. Why mutual information
2. Joint random variables
3. Joint and conditional entropy
4. Mutual information
5. Data processing
6. Differential entropy
7. Maximum entropy
8. References

## 1. Why Mutual Information?

A feedforward network maps an input $X$ through representations
$Z_1, Z_2, \dots$ to a prediction. Each layer is a *channel*: a possibly random
map from what enters to what leaves. The tools of the first two lectures,
$H(X)$ for one variable's uncertainty and $D(P \Vert Q)$ for the gap between two
candidate distributions of one variable, cannot yet express the questions this
picture raises: how much does the label say about the image, how much of $X$
remains in a feature $Z$, how much uncertainty is left after observing $Y$. All
of these are questions about a *pair* of random variables, so this lecture builds
the joint machinery first and then defines the answer, mutual information
$I(X;Y)$.

The headline result is the data processing inequality: along any pipeline
$X \to Z_1 \to Z_2$,

$$ I(X; Z_2) \leq I(X; Z_1) \leq H(X). $$

The first inequality is Theorem 7 (Section 5.4) applied to the Markov chain
$X - Z_1 - Z_2$; the second is immediate from the definition, since
$I(X; Z_1) = H(X) - H(X|Z_1)$ and $H(X|Z_1) \geq 0$. Processing can destroy
information about the input, never create it.

The lecture ends on the continuous side of the same story: differential entropy,
its quirks, and the fact that under an energy budget the Gaussian is the
maximally random density, which is why Gaussian noise is the canonical worst case
in AI models.

## 2. Joint Random Variables

### 2.1 Joint pmf, marginals, conditionals

**Definition (joint pmf).** Let $X \in \mathcal{X}$ and $Y \in \mathcal{Y}$ be
discrete random variables on a common probability space, with $\mathcal{X}$ and
$\mathcal{Y}$ finite or countable alphabets. Their joint pmf is

$$ p_{X,Y}(x, y) = \Pr(X = x, \, Y = y), \qquad
   x \in \mathcal{X}, \; y \in \mathcal{Y}, $$

a single table over all pairs, with $p_{X,Y}(x,y) \geq 0$ and
$\sum_{x,y} p_{X,Y}(x,y) = 1$. The alphabets may differ, for instance
$X \in [M]$ and $Y \in [N]$.

The joint determines everything about the pair. In particular the **marginals**
are recovered by summing out the partner:

$$ p_X(x) = \sum_{y \in \mathcal{Y}} p_{X,Y}(x, y)
   = \sum_{y \in \mathcal{Y}} p_{X|Y}(x|y) \, p_Y(y)
   = \mathbb{E}\left[p_{X|Y}(x|Y)\right], $$

where the middle form uses the conditional pmf defined next and the last form
reads it as an expectation over the random $Y$. This "average the conditionals"
identity is the total probability rule; it recurs in Lecture 7 as the tower
property. Summing out $y$ gives $p_X$, summing out $x$ gives $p_Y$. The converse
fails: the marginals do *not* determine the joint. Section 4.2's product
distribution $p_X p_Y$ has the same marginals as $p_{X,Y}$ but is in general a
different table.

**Definition (conditional pmf).** For any $y$ with $p_Y(y) > 0$,

$$ p_{X|Y}(x|y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}, $$

a valid pmf over $x$ for each fixed $y$: non-negative, and summing to
$p_Y(y)/p_Y(y) = 1$.

**Degenerate case.** If $p_Y(y) = 0$ the conditional $p_{X|Y}(\cdot|y)$ is
undefined, being $0/0$. It may be assigned arbitrarily without affecting any
expectation, because every average below weights it by $p_{X,Y}(x,y) = 0$. All
conditional-entropy sums in this note therefore run over
$\{y : p_Y(y) > 0\}$ only.

**Running example**, used for every worked number in this lecture:
$X, Y \in \{0,1\}$ with joint pmf

- $p_{X,Y}(0,0) = 1/4$ and $p_{X,Y}(0,1) = 1/4$, so the row for $x = 0$ sums to
  $p_X(0) = 1/2$;
- $p_{X,Y}(1,0) = 1/2$ and $p_{X,Y}(1,1) = 0$, so the row for $x = 1$ sums to
  $p_X(1) = 1/2$;
- the column for $y = 0$ sums to $p_Y(0) = 1/4 + 1/2 = 3/4$, the column for
  $y = 1$ sums to $p_Y(1) = 1/4 + 0 = 1/4$, and all four cells sum to 1.

Conditioning on $Y = 0$, whose column mass is $3/4$:
$p_{X|Y}(0|0) = \frac{1/4}{3/4} = \frac13$ and
$p_{X|Y}(1|0) = \frac{1/2}{3/4} = \frac23$. The pair is dependent, since
$p_{X,Y}(1,1) = 0 \neq \frac12 \cdot \frac14 = p_X(1) \, p_Y(1)$.

### 2.2 Independence, and three exercises solved

**Definition (independence).** $X$ and $Y$ are independent, written
$X \perp Y$, if and only if

$$ p_{X,Y}(x, y) = p_X(x) \, p_Y(y)
   \quad \text{for all } x \in \mathcal{X}, \; y \in \mathcal{Y}. $$

Equivalently, $p_{X|Y}(x|y) = p_X(x)$ for every $y$ with $p_Y(y) > 0$: observing
$Y$ does not move the distribution of $X$.

**Exercise 1 (linearity of expectation).** For any
$f : \mathcal{X} \to \mathbb{R}$, $g : \mathcal{Y} \to \mathbb{R}$ and *any*
joint distribution,

$$ \mathbb{E}\left[f(X) + g(Y)\right]
   = \sum_{x, y} p_{X,Y}(x,y) \left[f(x) + g(y)\right], $$

$$ = \sum_{x} f(x) \sum_{y} p_{X,Y}(x,y)
   + \sum_{y} g(y) \sum_{x} p_{X,Y}(x,y)
   = \mathbb{E}[f(X)] + \mathbb{E}[g(Y)], $$

where the inner sum in the first term is $p_X(x)$ and in the second is $p_Y(y)$.
**End of proof.**

No independence was used: the sum split before the pmf was ever factored. This is
what lets every "merge two expectations" step in the entropy proofs below proceed
without assumptions.

**Exercise 2 (factorization criterion).** Suppose
$p_{X,Y}(x,y) = \phi_1(x) \, \phi_2(y)$ for all $x, y$, where $\phi_1, \phi_2$
are any non-negative functions, not necessarily pmfs. Let
$c_1 = \sum_x \phi_1(x)$ and $c_2 = \sum_y \phi_2(y)$. Summing the factorization
over $y$, then over $x$, then over both:

$$ p_X(x) = \phi_1(x) \, c_2, \qquad p_Y(y) = c_1 \, \phi_2(y),
   \qquad 1 = c_1 c_2. $$

Hence
$p_X(x) \, p_Y(y) = \phi_1(x) \, \phi_2(y) \, c_1 c_2
= \phi_1(x) \, \phi_2(y) = p_{X,Y}(x,y)$,
so the pair is independent. **End of proof.** The moral: to certify independence
one never needs to normalize the factors.

**Exercise 3 (products of expectations).** If $X \perp Y$ then for any $f, g$,

$$ \mathbb{E}\left[f(X) \, g(Y)\right]
   = \sum_{x,y} p_X(x) \, p_Y(y) \, f(x) \, g(y)
   = \left(\sum_x p_X(x) f(x)\right) \left(\sum_y p_Y(y) g(y)\right), $$

which is $\mathbb{E}[f(X)] \, \mathbb{E}[g(Y)]$. **End of proof.**

Unlike Exercise 1, this one genuinely needs independence: the double sum factors
only because the pmf does. The converse fails.
$\mathbb{E}[XY] = \mathbb{E}[X] \mathbb{E}[Y]$, which is Exercise 3 for the
specific functions $f = g = \mathrm{id}$, is mere *uncorrelatedness*;
Section 4.5 gives an uncorrelated but dependent pair.

### 2.3 Random vectors; supervised learning as a joint distribution

For more than two variables, stack them: $X^n = (X_1, \dots, X_n)$ in
$\mathcal{X}^n$ with $p_{X^n}(x^n) = \Pr(X_1 = x_1, \dots, X_n = x_n)$, one pmf
over all $n$-tuples, subject to the same rules: marginalize by summing out
coordinates, condition by renormalizing, factor when independent.

A supervised-learning data point is a pair $(X, Y)$ with $X$ a random vector,
for instance Lecture 1's five-by-five binary image
$X^{25} \in \{0,1\}^{25}$, and $Y \in \{0, \dots, 9\}$ a label. Classification is
the task of learning the conditional pmf $p_{Y|X}(y|x)$. A trained network
outputs $f(X) = (\hat y_0, \dots, \hat y_9)$ with the hope that
$\hat y_i = \Pr(Y = i \mid X)$. For an ambiguous digit the honest answer is a
genuinely spread conditional, for example mass split between 1 and 7, which is
information the argmax alone discards. This is the Lecture 2 cross-entropy story
restated jointly: the loss compares the model's conditional to the true one, per
input.

## 3. Joint and Conditional Entropy

### 3.1 Joint entropy

**Definition (joint entropy).** For jointly distributed $X, Y$ with joint pmf
$p_{X,Y}$,

$$ H(X, Y) = \mathbb{E}\left[\log \frac{1}{p_{X,Y}(X, Y)}\right]
   = \sum_{x, y} p_{X,Y}(x, y) \log \frac{1}{p_{X,Y}(x, y)}, $$

with the usual convention $0 \log \frac{1}{0} = 0$, so that zero cells contribute
nothing; equivalently the sum runs over the support.

This is nothing new: it is Lecture 1's entropy applied to the single random
variable $(X,Y)$ whose alphabet is the product
$\mathcal{X} \times \mathcal{Y}$. So
$0 \leq H(X,Y) \leq \log(|\mathcal{X}| \, |\mathcal{Y}|)$ and every Lecture 1
property applies verbatim. The expectation is expanded by LOTUS on pairs:
$\mathbb{E}[f(X,Y)] = \sum_{x,y} p_{X,Y}(x,y) f(x,y)$. (The source scribe notes'
displayed definition drops the $\log$ in the summed form, a typo; the version
above is correct.)

**Worked on the running table, in full.** Three nonzero cells,
$\frac14, \frac14, \frac12$:

$$ H(X,Y) = \tfrac14 \log 4 + \tfrac14 \log 4 + \tfrac12 \log 2
   = \tfrac12 + \tfrac12 + \tfrac12 = 1.5 \text{ bits}. $$

The marginals: $p_X = (\frac12, \frac12)$ gives $H(X) = 1$ bit exactly, and
$p_Y = (\frac34, \frac14)$ gives the binary entropy

$$ H(Y) = h_2\left(\tfrac14\right)
   = \tfrac34 \log \tfrac43 + \tfrac14 \log 4
   = 0.75 \times 0.41504 + 0.5 \approx 0.81128 \text{ bits}. $$

So $H(X,Y) = 1.5 < 1.81128 = H(X) + H(Y)$, and the strict gap of $0.31128$ bits
is the pair's shared information, named in Section 4.

### 3.2 Theorem 1: additivity under independence

**Theorem 1 (additivity).** If $X \perp Y$ then $H(X, Y) = H(X) + H(Y)$.

*Proof, in three steps, with every sum shown.* Independence lets us replace the
joint pmf inside the logarithm:

$$ H(X,Y) = \sum_{x,y} p_{X,Y}(x,y) \log \frac{1}{p_X(x) \, p_Y(y)}. $$

Split the logarithm of the product, using
$\log \frac{1}{ab} = \log \frac1a + \log \frac1b$, and use linearity
(Exercise 1's split, applied to the two functions $\log \frac{1}{p_X(x)}$ and
$\log \frac{1}{p_Y(y)}$):

$$ H(X,Y) = \sum_{x,y} p_{X,Y}(x,y) \log \frac{1}{p_X(x)}
   + \sum_{x,y} p_{X,Y}(x,y) \log \frac{1}{p_Y(y)}. $$

In each double sum the logarithm depends on one variable only, so sum out the
other one first; the inner sum collapses the joint to a marginal:

$$ H(X,Y) = \sum_{x} \log \frac{1}{p_X(x)} \sum_{y} p_{X,Y}(x,y)
   + \sum_{y} \log \frac{1}{p_Y(y)} \sum_{x} p_{X,Y}(x,y)
   = H(X) + H(Y), $$

since the first inner sum is $p_X(x)$ and the second is $p_Y(y)$.
**End of proof.**

**Note the weight.** Independence was used only *inside* the logarithm; the
averaging weight stayed $p_{X,Y}$ throughout, and the marginalization step is
valid for any joint. Both facts are reused in the chain-rule proof, where no
independence is available.

**$n$ variables.** If $X_1, \dots, X_n$ are mutually independent, that is
$p_{X_1,\dots,X_n} = \prod_{i=1}^n p_{X_i}$, the same three moves (factor, split
into $n$ sums, marginalize each) give
$H(X_1, \dots, X_n) = \sum_{i=1}^n H(X_i)$. Formally, induct on $n$: the pair
$((X_1,\dots,X_{n-1}), X_n)$ is independent, so apply Theorem 1 and then the
inductive hypothesis.

**The converse question**, whether $H(X,Y) = H(X) + H(Y)$ implies independence,
is answered affirmatively in Section 4.4 once $I(X;Y)$ exists.

### 3.3 The guessing game returns

Lecture 1's game: Alice picks $X$ uniform on $\{1, \dots, 8\}$, so $H(X) = 3$
bits. Bob's three questions define the answer bits
$Y_1 = \mathbf{1}\{X \in \{5,6,7,8\}\}$,
$Y_2 = \mathbf{1}\{X \in \{1,2,5,6\}\}$,
$Y_3 = \mathbf{1}\{X \in \{1,3,5,7\}\}$,
where $\mathbf{1}\{\cdot\}$ is 1 when the event holds and 0 otherwise. Each set
has four of the eight equally likely elements, so each
$Y_i \sim \mathrm{Bern}(\frac12)$ and $H(Y_i) = 1$ bit.

The triple is independent because the map $X \mapsto (Y_1, Y_2, Y_3)$ is a
bijection from $\{1,\dots,8\}$ onto $\{0,1\}^3$: the three questions are the
three bits of $X - 1$ in disguise, and each of the 8 answer patterns has exactly
one preimage. Hence

$$ p_{Y_1,Y_2,Y_3}(y_1, y_2, y_3) = \tfrac18
   = p_{Y_1}(y_1) \, p_{Y_2}(y_2) \, p_{Y_3}(y_3)
   \quad \text{for all } (y_1,y_2,y_3), $$

and Theorem 1 gives $H(Y_1, Y_2, Y_3) = 3 = H(X)$: each question earns exactly
one bit, and after three the total equals the uncertainty in $X$, consistent with
the answers determining $X$ exactly.

A fourth question, "is $X \in \{4,5,6,7\}$?" with answer bit $Y_4$, *overlaps*
the first: $Y_1$ and $Y_4$ are dependent, so part of $Y_4$'s bit is already
delivered by $Y_1$, and $H(Y_1, Y_4)$ should fall strictly below
$H(Y_1) + H(Y_4) = 2$. Quantifying "the additional information in $Y_4$ once
$Y_1$ is known" is precisely what conditional entropy is for; the numbers are
finished in Section 3.5.

### 3.4 Conditional entropy and the chain rule

**Definition (conditional entropy).**

$$ H(X|Y) = \mathbb{E}\left[\log \frac{1}{p_{X|Y}(X|Y)}\right]
   = \sum_{x, y} p_{X,Y}(x, y) \log \frac{1}{p_{X|Y}(x|y)}, $$

the surprisal priced by the *conditional* pmf but averaged with the *joint* pmf:
both $X$ and $Y$ are random in the expectation.

The sum runs over pairs with $p_{X,Y}(x,y) > 0$, which forces $p_Y(y) > 0$, so
every conditional that appears is well defined and the degenerate columns of
Section 2.1 never enter. Since each term has $p_{X|Y}(x|y) \in (0, 1]$, every
summand is non-negative, hence $H(X|Y) \geq 0$, with $H(X|Y) = 0$ if and only if
$X$ is a deterministic function of $Y$, that is, each conditional puts all its
mass on one point.

**Two-stage reading.** Group the sum by $y$. With
$H(X|Y{=}y) = \sum_x p_{X|Y}(x|y) \log \frac{1}{p_{X|Y}(x|y)}$ the ordinary
entropy of the conditional pmf,

$$ H(X|Y) = \sum_{y} p_Y(y) \, H(X \mid Y = y), $$

an entropy per column of the table, weighted by column mass. Proof: substitute
$p_{X,Y}(x,y) = p_Y(y) \, p_{X|Y}(x|y)$ into the definition and pull $p_Y(y)$
out of the inner sum. Both readings are used interchangeably below.

**Worked on the running table, both directions.** Conditioning on $X$: given
$X = 0$, $Y \sim (\frac12, \frac12)$ with entropy 1; given $X = 1$,
$Y \sim (1, 0)$ with entropy 0. So

$$ H(Y|X) = \tfrac12 \cdot 1 + \tfrac12 \cdot 0 = 0.5 \text{ bits}. $$

Conditioning on $Y$: given $Y = 0$, $X \sim (\frac13, \frac23)$ with entropy

$$ h_2\left(\tfrac13\right) = \tfrac13 \log 3 + \tfrac23 \log \tfrac32
   \approx 0.52832 + 0.38998 = 0.91830, $$

and given $Y = 1$, $X \sim (1, 0)$ with entropy 0. So

$$ H(X|Y) = \tfrac34 \times 0.91830 + \tfrac14 \times 0
   \approx 0.68872 \text{ bits}. $$

Note $H(X|Y) \neq H(Y|X)$: conditioning is not symmetric. The two remainders
differ even though, by the chain rule next, the two *totals* agree.

**Theorem 2 (chain rule).** For any jointly distributed $X, Y$,

$$ H(X, Y) = H(X) + H(Y|X) = H(Y) + H(X|Y). $$

*Proof.* Start from the right-hand side of the first identity; merge the two
expectations by linearity (Exercise 1, no independence needed), then merge the
two logarithms, then apply the product rule of probability
$p_{X,Y}(x,y) = p_X(x) \, p_{Y|X}(y|x)$, valid on the support:

$$ H(X) + H(Y|X)
   = \mathbb{E}\left[\log \tfrac{1}{p_X(X)}
   + \log \tfrac{1}{p_{Y|X}(Y|X)}\right]
   = \mathbb{E}\left[\log \tfrac{1}{p_X(X) \, p_{Y|X}(Y|X)}\right], $$

$$ = \mathbb{E}\left[\log \tfrac{1}{p_{X,Y}(X, Y)}\right] = H(X, Y). $$

The second identity is the same computation with the roles of $X$ and $Y$
exchanged. **End of proof.**

Contrast with Theorem 1: additivity needed independence to put $p_X p_Y$ inside
the logarithm; the chain rule needs nothing, because $p_X \, p_{Y|X}$ *always*
equals the joint. Check on the table: $H(X) + H(Y|X) = 1 + 0.5 = 1.5$ and
$H(Y) + H(X|Y) \approx 0.81128 + 0.68872 = 1.5 = H(X,Y)$. Two roads, one total.

**General chain rule** (stated here for later use, for instance Lecture 7's Fano
proof): iterating Theorem 2 on the pair $((X_1, \dots, X_{k-1}), X_k)$,

$$ H(X_1, \dots, X_n)
   = \sum_{i=1}^{n} H\left(X_i \mid X_1, \dots, X_{i-1}\right), $$

with the $i = 1$ term read as $H(X_1)$. Theorem 1 is the special case where
independence makes every conditional entropy unconditional.

### 3.5 The guessing-game exercise, worked

**Computing $H(Y_2|Y_1)$.** $Y_1$ and $Y_2$ are independent, being two
coordinates of the bijection in Section 3.3, so each conditional distribution of
$Y_2$ is its marginal $\mathrm{Bern}(\frac12)$ and $H(Y_2|Y_1) = H(Y_2) = 1$
bit: an independent question retains its full value.

**Computing $H(Y_4|Y_1)$.** Build the joint of $(Y_1, Y_4)$ by counting outcomes
of $X$, each of the 8 values having mass $\frac18$. Recall $y_1 = 1$ means
$X \geq 5$ and $y_4 = 1$ means $X \in \{4,5,6,7\}$. The four cells:

- $y_1 = 1, y_4 = 1$: $X \in \{5,6,7\}$, mass $3/8$.
- $y_1 = 1, y_4 = 0$: $X = 8$, mass $1/8$.
- $y_1 = 0, y_4 = 1$: $X = 4$, mass $1/8$.
- $y_1 = 0, y_4 = 0$: $X \in \{1,2,3\}$, mass $3/8$.

Given $y_1 = 1$, whose mass is $\frac12$, we get $Y_4 \sim (\frac34, \frac14)$
with entropy $h_2(\frac34) = h_2(\frac14) \approx 0.81128$. Given $y_1 = 0$,
$Y_4 \sim (\frac14, \frac34)$, the same entropy. Hence

$$ H(Y_4 \mid Y_1)
   = \tfrac12 \times 0.81128 + \tfrac12 \times 0.81128
   \approx 0.811 \text{ bits}, $$

$$ H(Y_1, Y_4) = H(Y_1) + H(Y_4|Y_1) \approx 1 + 0.811 = 1.811 \text{ bits}. $$

Since $Y_4 \sim \mathrm{Bern}(\frac12)$ as well, because $\{4,5,6,7\}$ has four
elements, $H(Y_4) = 1$, and the overlap costs
$H(Y_1) + H(Y_4) - H(Y_1, Y_4) \approx 0.189$ bits, which by Section 4 is
exactly $I(Y_1; Y_4)$.

### 3.6 Theorem 3: data processing I, processing cannot add entropy

**Theorem 3 (data processing I).** For any deterministic function $f$ on
$\mathcal{X}$,

$$ H(X) \geq H\left(f(X)\right). $$

*Proof.* Expand the single object $H(X, f(X))$ by the chain rule in both orders.
Order one:

$$ H\left(X, f(X)\right) = H(X) + H\left(f(X) \mid X\right) = H(X), $$

because given $X = x$ the value $f(X) = f(x)$ is a constant, and a deterministic
outcome has zero entropy: $H(f(X)|X{=}x) = 0$ for every $x$, hence the average is
0. Order two:

$$ H\left(X, f(X)\right)
   = H\left(f(X)\right) + H\left(X \mid f(X)\right)
   \geq H\left(f(X)\right), $$

since conditional entropy is non-negative (Section 3.4). Equating the two
expansions gives the claim. **End of proof.**

**Equality analysis.** Equality holds if and only if $H(X \mid f(X)) = 0$, that
is, if and only if $X$ is determined by $f(X)$, equivalently if and only if $f$
is *injective on the support of $X$*: each attained value $t = f(x)$ has a single
preimage among outcomes of positive probability. The phrase "one-to-one and onto"
is sufficient, but surjectivity is not actually needed, and injectivity is only
needed on the support. Relabelings lose nothing; genuinely many-to-one maps on
the support (pooling, argmax, quantization) strictly drop entropy. This "expand
one joint entropy both ways" trick returns as the engine of Fano's inequality in
Lecture 7.

## 4. Mutual Information

### 4.1 Definition and the three equivalent forms

**Definition (mutual information).** For jointly distributed discrete $X, Y$,

$$ I(X; Y) = H(X) - H(X|Y). $$

Before observing $Y$ the uncertainty about $X$ is $H(X)$; afterwards $H(X|Y)$
remains on average; the drop is what $Y$ told us about $X$. Two further forms are
equivalent by the chain rule (Theorem 2), substituting
$H(X|Y) = H(X,Y) - H(Y)$:

$$ I(X; Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X, Y). $$

The third form is the Venn reading: two circles of areas $H(X)$ and $H(Y)$ inside
a box of area $H(X,Y)$; the overlap is $I(X;Y)$ and the private parts are
$H(X|Y)$ and $H(Y|X)$. The picture is a faithful mnemonic for *two* variables,
since every region is non-negative by Theorem 5 below and Section 3.4, but
Section 5.5's XOR example shows it has no faithful three-variable version, as the
"triple overlap" region would need to be negative. Treat it as bookkeeping, not
as set theory.

**Two special cases from the definition alone.**

- **Self-information.** $I(X; X) = H(X) - H(X|X) = H(X) - 0 = H(X)$. Observing
  $X$ removes all of its own uncertainty; entropy is the mutual information of a
  variable with itself, the case where the two circles coincide.
- **Independence implies zero.** If $X \perp Y$ then $p_{X|Y}(x|y) = p_X(x)$ for
  all relevant $y$, so $H(X|Y) = H(X)$ and $I(X;Y) = 0$. The converse, that zero
  mutual information forces independence, needs the KL form, next.

### 4.2 The KL form

**Proposition.**

$$ I(X; Y)
   = \mathbb{E}\left[\log \frac{p_{X,Y}(X, Y)}{p_X(X) \, p_Y(Y)}\right]
   = D\left(p_{X,Y} \, \Vert \, p_X \, p_Y\right), $$

the KL divergence (Lecture 2 note, Section 4.1) between the true joint and the
*product of its own marginals*, which is the distribution with the same marginals
but the dependence deleted.

*Derivation.* Merge the two expectations defining $I$ by linearity, then combine
the logarithms:

$$ H(X) - H(X|Y)
   = \mathbb{E}\left[\log \tfrac{1}{p_X(X)}
   - \log \tfrac{1}{p_{X|Y}(X|Y)}\right]
   = \mathbb{E}\left[\log \frac{p_{X|Y}(X|Y)}{p_X(X)}\right]. $$

Then multiply numerator and denominator by $p_Y(Y)$ and recognize
$p_{X|Y} \, p_Y = p_{X,Y}$:

$$ = \mathbb{E}\left[\log \frac{p_{X,Y}(X, Y)}{p_X(X) \, p_Y(Y)}\right]
   = \sum_{x,y} p_{X,Y}(x,y)
     \log \frac{p_{X,Y}(x,y)}{p_X(x) \, p_Y(y)}
   = D(p_{X,Y} \Vert p_X p_Y), $$

the last step being LOTUS on the pair alphabet. **End of proof.**

**Support bookkeeping.** The sum runs over the support of $p_{X,Y}$, and there
the marginals are automatically positive, since $p_{X,Y}(x,y) > 0$ forces
$p_X(x) \geq p_{X,Y}(x,y) > 0$. So unlike a general KL divergence this one can
never be $+\infty$ through a vanishing denominator: absolute continuity of the
joint with respect to its own product-of-marginals is automatic. In particular
$I(X;Y)$ is always finite for finite alphabets, bounded by
$\min\{H(X), H(Y)\} \leq \log \min\{|\mathcal{X}|, |\mathcal{Y}|\}$.

### 4.3 Theorems 4 and 5: symmetry and non-negativity

**Theorem 4 (symmetry).** $I(X; Y) = I(Y; X)$.

*Proof.* Route through the third form, which is visibly symmetric:

$$ I(X;Y) = H(X) - H(X|Y)
   = H(X) - \left(H(X,Y) - H(Y)\right)
   = H(X) + H(Y) - H(X,Y), $$

and reading that backwards through the chain rule the other way gives
$H(Y) - H(Y|X) = I(Y; X)$. **End of proof.** Alternatively, the KL form is
symmetric in $X$ and $Y$ term by term.

What $X$ tells about $Y$ is exactly what $Y$ tells about $X$. This is not obvious
from the asymmetric-looking definition, and it is false for the two conditional
entropies separately: Section 3.4 had $0.5 \neq 0.689$.

**Theorem 5 (non-negativity).** $I(X; Y) \geq 0$, with equality if and only if
$X \perp Y$.

*Proof.* By Section 4.2, $I(X;Y) = D(p_{X,Y} \Vert p_X p_Y)$, a KL divergence
between two pmfs on the pair alphabet $\mathcal{X} \times \mathcal{Y}$. The
information inequality (Lecture 2 note, Theorem 2, proved there by Jensen on the
strictly concave logarithm, zero-mass cases included) gives $D \geq 0$ with
equality if and only if the two arguments are equal as pmfs:

$$ I(X;Y) = 0 \iff p_{X,Y}(x,y) = p_X(x) \, p_Y(y)
   \text{ for all } x, y \iff X \perp Y. $$

**End of proof.**

This settles the converse left open in Section 4.1: mutual information is a
genuine, assumption-free *independence test*. It is zero exactly at independence
and strictly positive at any dependence whatsoever.

**Corollary (conditioning cannot increase entropy).** Rearranging
$I(X;Y) = H(X) - H(X|Y) \geq 0$,

$$ H(X|Y) \leq H(X), \qquad \text{with equality if and only if } X \perp Y. $$

**The average is essential: a pointwise counterexample.** The corollary bounds
the *expected* posterior entropy; an individual observation can perfectly well
raise uncertainty. Take $Y$ Bernoulli with $p_Y(0) = \frac14$ and
$p_Y(1) = \frac34$, and let $X \mid Y{=}0 \sim (\frac12, \frac12)$ while
$X \mid Y{=}1 = 0$ deterministically. The joint is
$p(0,0) = p(1,0) = \frac18$, $p(0,1) = \frac34$, $p(1,1) = 0$; marginally
$p_X = (\frac78, \frac18)$, so

$$ H(X) = h_2\left(\tfrac18\right)
   = \tfrac18 \log 8 + \tfrac78 \log \tfrac87
   \approx 0.375 + 0.16856 = 0.54356 \text{ bits}, $$

$$ H(X \mid Y{=}0) = 1 > H(X) \approx 0.544,
   \qquad H(X \mid Y{=}1) = 0, $$

$$ H(X|Y) = \tfrac14 \cdot 1 + \tfrac34 \cdot 0 = 0.25 \leq H(X). $$

The unlikely observation $y = 0$ *increases* uncertainty about $X$ beyond the
prior, from $0.544$ to a full bit, yet the average over observations still
shrinks it, as Theorem 5 guarantees. "Observation never hurts" is a statement
about expectations only.

### 4.4 The running table and the Section 3 exercise, closed

**Worked $I(X;Y)$, three routes.** All ingredients were computed in Section 3:

$$ I(X;Y) = H(X) - H(X|Y) = 1 - 0.68872 = 0.31128, $$

$$ I(X;Y) = H(Y) - H(Y|X) = 0.81128 - 0.5 = 0.31128, $$

$$ I(X;Y) = H(X) + H(Y) - H(X, Y) = 1.81128 - 1.5 = 0.31128. $$

Three routes, one number: about $0.311$ bits shared. Likewise in the guessing
game, $I(Y_1; Y_4) = 2 - 1.811 = 0.189$ bits, the overlap cost of Section 3.5,
now named.

**Additivity converse (Section 3.2's exercise).** Yes:
$H(X,Y) = H(X) + H(Y)$ implies independence. By the third form the hypothesis
says exactly $I(X;Y) = 0$, and Theorem 5's equality case forces
$p_{X,Y} = p_X p_Y$. So Theorem 1 is in fact an equivalence: entropy is additive
*precisely* for independent pairs.

### 4.5 What mutual information buys in AI, and a dependence correlation misses

Mutual information is a nonlinear dependence detector in invariant units, bits,
which is what makes quantities like $I(Z; Y)$, the label information a learned
feature retains, meaningful across architectures. This is the currency of the
information-bottleneck analysis of deep networks [4, 5].

The closing contrast, made precise: zero correlation does *not* imply
independence, but zero mutual information does (Theorem 5). A standard example of
the gap: $X$ uniform on $\{-1, 0, 1\}$ and $Y = X^2$. Then
$\mathbb{E}[XY] = \mathbb{E}[X^3] = \frac13(-1 + 0 + 1) = 0
= \mathbb{E}[X]\mathbb{E}[Y]$,
so the pair is uncorrelated; yet $Y$ is a function of $X$, and since
$H(Y|X) = 0$,

$$ I(X; Y) = H(Y) - H(Y|X) = h_2\left(\tfrac13\right)
   \approx 0.918 \text{ bits}, $$

where $p_Y = (\frac13, \frac23)$ on $\{0, 1\}$. Cross-check via the other form:
$H(X) - H(X|Y) = \log 3 - \frac23 \cdot 1 = 1.58496 - 0.66667 = 0.91830$, which
agrees. Strongly dependent, and invisible to correlation.

## 5. Data Processing

### 5.1 Two lemmas

**Lemma A (redundant conditioning is free).** For any deterministic $f$,

$$ H\left(Y \mid X, f(X)\right) = H(Y \mid X). $$

*Proof.* The pair $(X, f(X))$ takes only values of the form $(x, f(x))$ with
positive probability, and on such a value the conditioning event
$\{X = x, \, f(X) = f(x)\}$ equals $\{X = x\}$, so
$p_{Y|X, f(X)}(y \mid x, f(x)) = p_{Y|X}(y|x)$ for every $y$. The two
conditional entropies are therefore averages of identical per-event entropies
with identical weights. **End of proof.** Equivalently: $(X, f(X))$ and $X$
generate the same information, each determining the other, and conditional
entropy depends only on what the condition determines.

**Lemma B (conditioning cannot increase conditional entropy).** For any
$X, Y, W$,

$$ H(Y \mid X, W) \leq H(Y \mid W). $$

*Proof.* The gap is a conditional mutual information (Section 5.5's definition,
second form): $H(Y|W) - H(Y|X,W) = I(X; Y \mid W)$, and

$$ I(X; Y \mid W) = \sum_{w} p_W(w) \; I\left(X; Y \mid W = w\right) \geq 0, $$

because each $I(X; Y \mid W{=}w)$ is the ordinary mutual information of the pair
under the conditional joint $p_{X,Y|W}(\cdot,\cdot|w)$, hence non-negative by
Theorem 5. **End of proof.** Equality holds if and only if $X \perp Y$ given $W$.

### 5.2 Theorem 6: data processing II

**Theorem 6 (data processing II).** For any deterministic $f$ on $\mathcal{X}$,

$$ I(X; Y) \geq I\left(f(X); Y\right). $$

*Proof.* Insert the redundant condition, then relax the stronger one. By
Lemma A,

$$ I(X; Y) = H(Y) - H(Y|X) = H(Y) - H\left(Y \mid X, f(X)\right), $$

and by Lemma B with $W = f(X)$,

$$ H(Y) - H\left(Y \mid X, f(X)\right)
   \geq H(Y) - H\left(Y \mid f(X)\right) = I\left(f(X); Y\right). $$

**End of proof.**

**Reading, equality, and no converse.** Transforming $X$ (pooling, quantizing,
hand-crafting features) can at best *preserve* information about $Y$. It can
still help optimization or generalization, which is a statement about
learnability, not about information content. Equality holds if and only if
Lemma B is tight, that is, if and only if $X \perp Y$ given $f(X)$, equivalently
if and only if $f(X)$ is a *sufficient statistic* of $X$ for $Y$, meaning the
chain $X - f(X) - Y$ is Markov. There is no converse inequality:
$I(f(X); Y)$ can be anything from $I(X;Y)$, for a sufficient $f$ such as an
injective one, down to 0, for a constant $f$, with $I(X;Y)$ unchanged. So knowing
the processed information tells you nothing about the raw information.

### 5.3 Markov chains: the formal package

**Definition (Markov chain, or Markov triplet).** $X - Y - Z$ holds if and only
if $X$ and $Z$ are conditionally independent given $Y$:

$$ p_{X,Z|Y}(x, z \mid y) = p_{X|Y}(x|y) \; p_{Z|Y}(z|y) $$

for all $x, z$ and all $y$ with $p_Y(y) > 0$. As in Section 2.1, nothing is
required at values of $y$ with zero mass.

Three equivalent formulations, each proved below.

- (i) $p_{Z|X,Y}(z|x,y) = p_{Z|Y}(z|y)$ whenever $p_{X,Y}(x,y) > 0$: once $Y$ is
  known, $X$ is useless for predicting $Z$.
- (ii) The joint factors as $p_{X,Y,Z} = p_Y \cdot p_{X|Y} \cdot p_{Z|Y}$ on the
  support.
- (iii) $Z - Y - X$: the chain reads the same in both directions.

*Proof of the equivalences.* Definition implies (i): divide the definition by
$p_{X|Y}(x|y)$, legal when $p_{X,Y}(x,y) > 0$ since then $p_{X|Y}(x|y) > 0$,

$$ p_{Z|X,Y}(z|x,y) = \frac{p_{X,Z|Y}(x,z|y)}{p_{X|Y}(x|y)} = p_{Z|Y}(z|y). $$

(i) implies (ii): $p_{X,Y,Z} = p_{X,Y} \cdot p_{Z|X,Y}
= p_Y \, p_{X|Y} \, p_{Z|Y}$ on the support. (ii) implies the definition: divide
by $p_Y(y)$. The definition is equivalent to (iii) because it is literally
symmetric under swapping the roles of $X$ and $Z$. **End of proof.**

Instances: any pipeline where $Z$ is computed from $Y$ alone. Data to
representation to prediction; image to compressed file to reconstruction; signal
to channel output to decoder output. The deterministic case $Z = f(Y)$ is the
special case where $p_{Z|Y}(\cdot|y)$ is a point mass; randomized processing,
where $Z$ is drawn from any kernel depending only on $y$, is equally allowed,
which makes this strictly more general than data processing II.

### 5.4 Theorem 7: data processing III

**Theorem 7 (data processing III).** If $X - Y - Z$ then

$$ I(Y; Z) \geq I(X; Z), \qquad \text{and likewise} \qquad
   I(X; Y) \geq I(X; Z). $$

*Proof of the first.* Formulation (i) with the roles as stated says
$H(Z|Y) = H(Z|X,Y)$: the extra condition $X$ changes no conditional of $Z$, and
one averages as in Lemma A. Then, using Lemma B with $W = X$,

$$ I(Y; Z) = H(Z) - H(Z|Y) = H(Z) - H(Z \mid X, Y)
   \geq H(Z) - H(Z|X) = I(X; Z). $$

*The second* follows by symmetry: $X - Y - Z$ if and only if $Z - Y - X$
(equivalence (iii)), and applying the first inequality to the reversed chain
gives $I(Y; X) \geq I(Z; X)$, that is $I(X;Y) \geq I(X;Z)$ by Theorem 4.
**End of proof.** (The source scribe notes state this theorem with the inequality
reversed, as $I(Z;X) \geq I(Z;Y)$, while their proof derives
$I(Y;Z) \geq I(X;Z)$: a statement-level typo. The version above is the correct
direction.)

**Data processing II as a special case.** Given any $X, Y$ and deterministic $f$,
the triple $Y - X - f(X)$ is Markov, since given $X$ the value $f(X)$ is a
constant and hence conditionally independent of anything. Reversing it,
$f(X) - X - Y$ is Markov, and Theorem 7's first inequality on this chain reads
$I(X; Y) \geq I(f(X); Y)$, which is exactly Theorem 6.

Chaining Theorem 7 down a deep net $X \to Z_1 \to Z_2 \to \cdots$, where each
layer sees only its predecessor so that every contiguous triple is Markov, yields
the monotone decay

$$ I(X; Z_1) \geq I(X; Z_2) \geq \cdots $$

Layers only forget. Training chooses *which* information survives; the data
processing inequality caps *how much*.

### 5.5 Conditional mutual information

**Definition (conditional mutual information).**

$$ I(X; Z \mid Y) = H(X|Y) - H(X \mid Y, Z) = H(Z|Y) - H(Z \mid Y, X), $$

the information between $X$ and $Z$ once $Y$ is known. The two forms agree by the
same chain-rule algebra as Theorem 4, applied conditionally.

By the identity used in Lemma B's proof,
$I(X;Z|Y) = \sum_y p_Y(y) \, I(X;Z \mid Y{=}y) \geq 0$, and it vanishes if and
only if every conditional joint factors:

$$ I(X; Z \mid Y) = 0 \iff X \perp Z \text{ given } Y
   \iff X - Y - Z \text{ is Markov}. $$

Conditional mutual information is thus the *quantitative measure of how far a
triple is from being a Markov chain*.

**Does conditioning shrink mutual information?** For entropy, conditioning never
increases the average (Section 4.3). The analogous guess
$I(X; Z \mid Y) \leq I(X; Z)$ is **false in general**, and so is the reverse: no
inequality holds either way. Both strict orders occur.

**Counterexample (the XOR triple): conditioning can create dependence.** Let
$X, Z$ be independent and identically distributed $\mathrm{Bern}(\frac12)$, and
let $Y = X \oplus Z$ be their parity. Three steps.

*Step 1.* $I(X; Z) = 0$ by construction:
$p_{X,Z}(x,z) = \frac14 = p_X(x) \, p_Z(z)$ for all four pairs.

*Step 2.* $H(Z|Y) = 1$. From the four equally likely triples
$(x, z, x \oplus z)$: given $Y = 0$, the pair $(X,Z)$ is $(0,0)$ or $(1,1)$
equally likely, so $Z \mid Y{=}0 \sim \mathrm{Bern}(\frac12)$; given $Y = 1$,
$(X,Z)$ is $(0,1)$ or $(1,0)$ equally likely, so
$Z \mid Y{=}1 \sim \mathrm{Bern}(\frac12)$. Hence
$H(Z|Y) = \frac12 \cdot 1 + \frac12 \cdot 1 = 1$ bit: the parity alone says
nothing about either coin.

*Step 3.* XOR is its own inverse, so $Y = X \oplus Z$ if and only if
$Z = X \oplus Y$; given $(X, Y)$ the value of $Z$ is determined and
$H(Z \mid Y, X) = 0$. Therefore

$$ I(X; Z \mid Y) = H(Z|Y) - H(Z \mid Y, X) = 1 - 0 = 1 > 0 = I(X; Z). $$

Note also that given $Y$ the pair $(X, Z)$ is far from conditionally independent
even though each is marginally still fair:
$p_{X,Z|Y}(0,0|0) = \frac12 \neq \frac14
= p_{X|Y}(0|0) \, p_{Z|Y}(0|0)$.

This is the "explaining away" pattern: two independent causes are coupled by
conditioning on their common effect. Once the alarm's state is known, learning
one cause changes the odds of the other. It is also the promised failure of the
three-variable Venn diagram: the would-be triple-overlap
$I(X;Z) - I(X;Z|Y) = 0 - 1 = -1$ bit is negative, so no area diagram can
represent this triple.

**Opposite direction.** On a Markov chain $X - Y - Z$ the conditional mutual
information is 0 while $I(X;Z)$ can be large; the extreme case
$X = Y = Z$, a single fair bit, gives $I(X; Z \mid Y) = 0 < 1 = I(X; Z)$.
Together with the XOR triple this completes the claim: no general relationship
holds between $I(X;Z|Y)$ and $I(X;Z)$.

### 5.6 Chain rule for mutual information

**Proposition (chain rule for $I$).**

$$ I(X, Y; \, Z) = I(X; Z) + I(Y; Z \mid X), $$

where $I(X,Y;Z)$ is the mutual information between the pair $(X,Y)$, treated as
one variable, and $Z$.

*Proof.* Add and subtract $H(Z|X)$:

$$ I(X, Y; Z) = H(Z) - H(Z \mid X, Y) $$

$$ = \left[H(Z) - H(Z|X)\right]
   + \left[H(Z|X) - H(Z \mid X, Y)\right]
   = I(X; Z) + I(Y; Z \mid X). $$

**End of proof.**

First $X$'s contribution about $Z$, then $Y$'s *fresh* contribution given $X$.
The total is order-free: starting from $Y$ instead gives
$I(X,Y;Z) = I(Y;Z) + I(X; Z|Y)$, the same left side with a different split. On
the XOR triple, with $Z$ in the role of the target, this reads $0 + 1 = 1 + 0$, a
consistency check.

Iterating over the coordinates of a vector,

$$ I(X^n; Y) = \sum_{i=1}^{n} I\left(X_i; \, Y \mid X^{i-1}\right),
   \qquad X^{i-1} = (X_1, \dots, X_{i-1}), $$

proved by induction: split $(X^{n-1}, X_n)$ with the two-variable rule and apply
the hypothesis to $X^{n-1}$. Each term is what coordinate $i$ adds about $Y$
given the past. This is the workhorse decomposition for sequences (pixels,
tokens, time steps), and every term is non-negative, so information about $Y$
only accumulates as coordinates are revealed.

## 6. Differential Entropy

### 6.1 Densities, and what changes when mass becomes density

**Definition (cdf, pdf).** For a real-valued $X$ the cumulative distribution
function is $F_X(x) = \Pr(X \leq x)$. If $F_X$ is differentiable, the probability
density function is

$$ f_X(x) = \frac{\partial}{\partial x} F_X(x), \qquad
   \Pr(a \leq X \leq b) = \int_a^b f_X(x) \, dx. $$

Probability is *area* under $f_X$, never a value of it: $f_X(x)$ can exceed 1,
for instance $\mathrm{Unif}(0, \frac12)$ has density 2, and $\Pr(X = x) = 0$ for
every point. All statements in this section assume $X$ has a density, that is, an
absolutely continuous law; mixed or discrete parts break the formulas, as noted
in Section 6.3.

**Change of variables.** This is the first genuinely new phenomenon. If $Y = aX$
with $a \neq 0$ then for $a > 0$ we have
$F_Y(y) = \Pr(aX \leq y) = F_X(y/a)$, and differentiating,
$f_Y(y) = \frac1a f_X(y/a)$; for $a < 0$ the cdf flips, becoming
$F_Y(y) = 1 - F_X(y/a)$, and the derivative picks up the sign. Both cases
together:

$$ f_Y(y) = \frac{1}{|a|} \, f_X\!\left(\frac{y}{a}\right), $$

which is conservation of probability, $|f_X(x) \, dx| = |f_Y(y) \, dy|$ with
$|dx/dy| = 1/|a|$: stretch the axis by $a$ and the density must compress by
$|a|$ to keep the total area 1. For example $\mathrm{Unif}(0,1)$ becomes
$\mathrm{Unif}(0,2)$: twice as wide, half as tall. Generally, for a bijective
differentiable $g$ and $Y = g(X)$,

$$ f_Y(y) = f_X\left(g^{-1}(y)\right)
   \left|\frac{d}{dy} g^{-1}(y)\right|. $$

Discrete pmfs never needed a correction factor: masses just move with their
labels. This stretch factor is the sole source of every quirk of differential
entropy below.

### 6.2 KL divergence and mutual information go through unchanged

**Definition (KL divergence for densities).** For densities $f, g$ on
$\mathbb{R}$,

$$ D(f \, \Vert \, g) = \mathbb{E}_f\left[\log \frac{f(X)}{g(X)}\right]
   = \int f(x) \log \frac{f(x)}{g(x)} \, dx \; \in \; [0, +\infty], $$

with the Lecture 2 conventions transplanted: the integrand is 0 where $f = 0$,
and $D = +\infty$ unless $g > 0$ almost everywhere (in the Lebesgue sense) that
$f > 0$, which is absolute continuity, written $f \ll g$.

**Theorem (information inequality, continuous).** $D(f \Vert g) \geq 0$, with
equality if and only if $f = g$ almost everywhere.

*Proof, by Jensen, exactly as in Lecture 2 with sums replaced by integrals.*

$$ D(f \Vert g) = -\int f(x) \log \frac{g(x)}{f(x)} \, dx
   \geq -\log \int f(x) \, \frac{g(x)}{f(x)} \, dx $$

$$ = -\log \int_{\{f > 0\}} g(x) \, dx \geq -\log 1 = 0. $$

**End of proof.** The logarithm is concave, so $-\log$ is convex and Jensen
reverses; the final integral is at most 1 since $g$ integrates to 1 over all of
$\mathbb{R}$. This is the same two-inequality structure as the rigorous discrete
proof in the Lecture 2 note, Section 3.4. Equality in Jensen requires $g/f$
constant $f$-almost everywhere, and equality in the last step requires $g$ to
carry no mass off $\{f > 0\}$; together these give $f = g$ almost everywhere.

**Continuous mutual information.** Define it through the KL form, with no entropy
needed:

$$ I(X; Y) = \mathbb{E}\left[
     \log \frac{f_{X,Y}(X, Y)}{f_X(X) \, f_Y(Y)}\right]
   = D\left(f_{X,Y} \, \Vert \, f_X f_Y\right) \geq 0, $$

non-negativity being immediate from the theorem above, with equality if and only
if $f_{X,Y} = f_X f_Y$ almost everywhere, that is, independence (Theorem 11
below). As in Section 4.2, absolute continuity of the joint with respect to the
product of its own marginals holds automatically wherever $f_{X,Y} > 0$.

**Mutual information is discretization-proof.** Chop $\mathbb{R}$ into bins of
width $\Delta$ and let $X^\Delta$ be the index of $X$'s bin, so that
$P_{X^\Delta}(i) = \Pr(i\Delta \leq X \leq (i{+}1)\Delta)
\approx \Delta \, f_X(x_i)$
for a point $x_i$ in bin $i$; this is exact for some $x_i$ by the mean value
theorem when $f_X$ is continuous. Then

$$ I(X^\Delta; Y^\Delta)
   = \mathbb{E}\left[
     \log \frac{P_{X^\Delta,Y^\Delta}}{P_{X^\Delta} \, P_{Y^\Delta}}\right]
   \approx \mathbb{E}\left[
     \log \frac{\Delta^2 \, f_{X,Y}(X,Y)}
     {\Delta f_X(X) \cdot \Delta f_Y(Y)}\right]
   = \mathbb{E}\left[\log \frac{f_{X,Y}}{f_X f_Y}\right]. $$

The bin widths cancel *exactly* in the ratio, and
$I(X^\Delta; Y^\Delta) \to I(X;Y)$ as $\Delta \to 0$ [1, Sec. 8.5]. Mutual
information survives the continuum limit with no correction: it is the same
physical quantity in both worlds.

### 6.3 Theorem 8 and the definition of differential entropy

**Theorem 8 (discretization).** With $X^\Delta$ as above and $f_X$
Riemann-integrable,

$$ H(X^\Delta) = h(X) - \log \Delta + o(1) \qquad (\Delta \to 0), $$

where the **differential entropy** is

$$ h(X) = \mathbb{E}\left[\log \frac{1}{f_X(X)}\right]
   = \int f_X(x) \log \frac{1}{f_X(x)} \, dx. $$

*Proof.* By the mean value theorem pick $x_i$ in bin $i$ with
$P_{X^\Delta}(i) = \Delta f_X(x_i)$ exactly. Then

$$ H(X^\Delta) = \sum_i \Delta f_X(x_i) \log \frac{1}{\Delta f_X(x_i)}
   = \sum_i \Delta \, f_X(x_i) \log \frac{1}{f_X(x_i)}
   \; - \; \log \Delta \sum_i \Delta f_X(x_i), $$

where the last sum equals 1 and the first sum is a Riemann sum for the $h(X)$
integral, hence converges to $h(X)$. **End of proof.** Statements of this
identity that absorb the approximation into $P \approx \Delta f$ are the same
result informally written; the version above is the precise limit statement
[1, Thm 8.3.1].

**Reading it.** As $\Delta \to 0$ we have $-\log \Delta \to +\infty$, so
$H(X^\Delta) \to \infty$: an exact real number carries infinitely many bits,
since finer bins mean more distinguishable outcomes. Differential entropy is the
finite remainder once the grid's own contribution $-\log \Delta$ is subtracted:
*entropy relative to the grid*, not an absolute information content. Concretely,
$h$ compares $X$'s spread to a unit-length reference, and
$H(X^\Delta) \approx h(X) + 10$ bits at $\Delta = 2^{-10}$, of which 10 bits are
pure grid.

**Existence caveats.** The defining integral need not converge. $h$ can be
$+\infty$ for very heavy tails, for instance
$f(x) \propto 1/(x \ln^2 x)$ on $[e, \infty)$; it can be $-\infty$ when mass
concentrates on arbitrarily small sets; and it can fail to exist when positive
and negative parts both diverge. Also, $h$ is only defined for distributions
*with a density*: a discrete or mixed $X$ has $H(X^\Delta)$ bounded, or growing
by a different law, and no $h$. All theorems below implicitly assume the relevant
differential entropies are finite.

### 6.4 Worked examples and the three exhibits

**Uniform.** $U \sim \mathrm{Unif}(a,b)$ has density $\frac{1}{b-a}$ on
$[a,b]$, so

$$ h(U) = \int_a^b \frac{1}{b-a} \log (b-a) \, dx = \log(b - a). $$

Checks: $\mathrm{Unif}(0,1)$ gives $h = \log 1 = 0$, and $\mathrm{Unif}(0,2)$
gives $h = \log 2 = 1$ bit.

**Exhibit 1: $h$ can be negative.** $U \sim \mathrm{Unif}(0, \frac12)$ has
$h(U) = \log \frac12 = -1$ bit. There is no contradiction with $H \geq 0$: $h$
is the grid-normalized part, and a variable concentrated on a set shorter than
unit length sits *below* the reference. Indeed
$H(X^\Delta) = -1 - \log \Delta$ is still positive for every
$\Delta < \frac12$.

**Exhibit 2: no relabeling invariance.** Discrete entropy depends only on the
multiset of probabilities: for one-to-one $f$, $H(f(X)) = H(X)$, the equality
case of data processing I. For example $X_1 \in \{1,2,3\}$ with
$p = (0.4, 0.5, 0.1)$ and $X_2 = 2X_1 \in \{2,4,6\}$ have identical entropies.
Continuously this fails: $U \sim \mathrm{Unif}(0,1)$ and
$V = 2U \sim \mathrm{Unif}(0,2)$ have $h(U) = 0 \neq 1 = h(V)$. The bijection
$u \mapsto 2u$ stretched the axis and thereby *manufactured* differential
entropy. In general $h$ is **not invariant under bijections**: for a smooth
bijective $g$, plugging the change-of-variables formula into the definition gives

$$ h(g(X)) = h(X) + \mathbb{E}\left[\log |g'(X)|\right], $$

the average log-stretch being added.

**Exhibit 3: the scaling law, the quirk quantified.** For $a \neq 0$, using
$f_{aX}(y) = \frac{1}{|a|} f_X(y/a)$ evaluated at $y = aX$,

$$ h(aX) = \mathbb{E}\left[\log \frac{1}{f_{aX}(aX)}\right]
   = \mathbb{E}\left[\log \frac{|a|}{f_X(X)}\right]
   = h(X) + \log |a|. $$

This is consistent with both earlier exhibits: $a = 2$ adds 1 bit, and
$|a| < 1$ subtracts. Translation, by contrast, is free: $f_{X+c}(y) = f_X(y - c)$
has the same shape, so $h(X + c) = h(X)$.

**Summary of the contrast** between discrete $H$ and differential $h$:

- Non-negative: yes for $H$; **no** for $h$ (Exhibit 1).
- Relabeling or scale invariant: yes for $H$; **no** for $h$ (Exhibits 2 and 3).
- Translation invariant: yes for $H$, as a relabeling; yes for $h$.

**Gaussian differential entropy, in full.** For
$X \sim \mathcal{N}(\mu, \sigma^2)$ with
$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \, e^{-(x-\mu)^2/2\sigma^2}$, the
surprisal is a quadratic,

$$ \log \frac{1}{f(x)}
   = \log \sqrt{2\pi\sigma^2} + \frac{(x-\mu)^2}{2\sigma^2} \log e, $$

where the factor $\log e$ converts the exponent from nats. Taking expectations
with $\mathbb{E}[(X-\mu)^2] = \sigma^2$,

$$ h(X) = \tfrac12 \log(2\pi\sigma^2) + \tfrac12 \log e
   = \tfrac12 \log\left(2\pi e \sigma^2\right). $$

By translation invariance the mean drops out. Numerically at $\sigma = 1$,
$\frac12 \log_2(2\pi e) = \frac12 \log_2 17.0795
\approx \frac12 \times 4.0942 \approx 2.047$ bits. It grows like $\log \sigma$,
as the scaling law demands, since
$\mathcal{N}(0,\sigma^2) = \sigma \cdot \mathcal{N}(0,1)$ adds $\log \sigma$.

A same-variance lineup, all at variance 1: the Gaussian has $h \approx 2.047$
bits; the Laplace density with $b = 1/\sqrt2$ has
$h = \log_2(2be) = \log_2(\sqrt2 \, e) = \frac12 + \log_2 e \approx 1.943$ bits;
and the uniform of variance 1, whose width is $\sqrt{12}$, has
$h = \log_2 \sqrt{12} \approx 1.792$ bits. The Gaussian tops both, previewing
Section 7.

### 6.5 Conditional differential entropy and the continuous theorems

**Definition (conditional differential entropy).**

$$ h(X|Y) = \mathbb{E}\left[\log \frac{1}{f_{X|Y}(X|Y)}\right]
   = \int f_{X,Y}(x, y) \log \frac{1}{f_{X|Y}(x|y)} \, dx \, dy, $$

with $f_{X|Y}(x|y) = f_{X,Y}(x,y)/f_Y(y)$ where $f_Y(y) > 0$.

Scaling passes through conditioning: for fixed $y$, the variable
$aX \mid Y{=}y$ has density $\frac{1}{|a|} f_{X|Y}(\cdot/a \mid y)$, so the same
computation as Exhibit 3 gives $h(aX \mid Y) = h(X|Y) + \log|a|$. Unlike its
discrete counterpart, $h(X|Y)$ can be negative; but the identity
$I(X;Y) = h(X) - h(X|Y)$, from the same merge-the-logarithms derivation as
Section 4.2 with densities, together with $I \geq 0$ still gives
$h(X|Y) \leq h(X)$: conditioning cannot increase differential entropy either.

**Theorem 9 (mutual information ignores rescaling).** For $a \neq 0$,
$I(aX; Y) = I(X; Y)$.

*Proof.* Both entropy terms shift by the same amount and the shifts cancel:

$$ I(aX; Y) = h(aX) - h(aX \mid Y)
   = \left(h(X) + \log|a|\right) - \left(h(X|Y) + \log|a|\right) = I(X;Y). $$

**End of proof.** More generally the same cancellation works for any bijective
smooth $g$ with $\mathbb{E}[\log|g'(X)|]$ finite, giving
$I(g(X); Y) = I(X;Y)$: mutual information is invariant under invertible
reparametrization of either argument.

This resolves the quirks. $aX$ tells about $Y$ exactly what $X$ does, and $I$
agrees; units, normalization and feature scaling leave $I$ untouched.
Differential entropy alone is coordinate-bound bookkeeping, while *differences*
of $h$, such as $I$, are the physical quantities.

**Theorem 10 (chain rule for $h$).** $h(X_1, X_2) = h(X_1) + h(X_2 \mid X_1)$.

*Proof.* The joint density factors as marginal times conditional,
$f_{X_1,X_2} = f_{X_1} \cdot f_{X_2|X_1}$, exactly as for pmfs; split the
logarithm and the expectation:

$$ h(X_1, X_2) = \mathbb{E}\left[\log \tfrac{1}{f_{X_1,X_2}}\right]
   = \mathbb{E}\left[\log \tfrac{1}{f_{X_1}(X_1)}\right]
   + \mathbb{E}\left[\log \tfrac{1}{f_{X_2|X_1}(X_2|X_1)}\right]. $$

**End of proof.**

**Theorem 11 (independence test, continuous).** $X \perp Y$ if and only if
$I(X;Y) = 0$.

*Proof.* $I(X;Y) = D(f_{X,Y} \Vert f_X f_Y)$, and the continuous information
inequality (Section 6.2) vanishes if and only if its arguments agree almost
everywhere, that is $f_{X,Y} = f_X f_Y$ almost everywhere, which is exactly
independence for continuous variables. **End of proof.**

**Theorem 12 (data processing inequality, continuous).** If $X - Y - Z$, with
conditional densities factoring as in Section 5.3, then $I(X; Y) \geq I(X; Z)$
and $I(Y;Z) \geq I(X;Z)$.

*Proof, the discrete skeleton verbatim with $h$ in place of $H$.* Markov gives
$f_{Z|X,Y} = f_{Z|Y}$, hence $h(Z|Y) = h(Z \mid X, Y)$, and conditioning is
still non-increasing, by the conditional version obtained from conditional mutual
information being non-negative and integrated over the conditioning variable, as
in Lemma B:

$$ I(Y; Z) = h(Z) - h(Z|Y) = h(Z) - h(Z \mid X, Y)
   \geq h(Z) - h(Z|X) = I(X; Z), $$

and the $I(X;Y)$ bound follows by chain reversal as in Theorem 7.
**End of proof.** (The source scribe notes' version of this proof carries two
typos: the statement's inequality written as $I(X;Y) \geq I(Z;X)$, and the middle
line written $h(Z|Y,Z)$ for $h(Z|Y,X)$. The version above is corrected.)

## 7. Maximum Entropy

### 7.1 Recall, and the bounded-support exercise solved

Lecture 1's discrete result: for $X \in \{1, \dots, K\}$, $H(X) \leq \log K$
with equality if and only if $X$ is uniform, proved there by comparing to the
flat candidate. The continuous analogue must first decide *over which family* to
maximize $h$, since without any constraint $h$ is unbounded: a spread-out
$\mathrm{Unif}(0, L)$ has $h = \log L \to \infty$.

**Exercise (bounded support), solved.** If $X \in [a,b]$ with probability 1 and
has density $f$, then $h(X) \leq \log(b-a)$, with equality if and only if
$X \sim \mathrm{Unif}(a,b)$.

*Proof.* Let $u = \frac{1}{b-a}$ on $[a,b]$ be the uniform density. Then

$$ 0 \leq D(f \, \Vert \, u)
   = \int_a^b f(x) \log \frac{f(x)}{1/(b-a)} \, dx
   = -h(X) + \log(b - a), $$

since $\log \frac{1}{u} = \log(b-a)$ is constant and $f$ integrates to 1.
Rearranged, $h(X) \leq \log(b-a)$, with equality if and only if
$D(f \Vert u) = 0$, that is $f = u$ almost everywhere. **End of proof.** Flat
wins on a box, mirroring the discrete result, with $\log(b-a)$ playing the role
of $\log K$.

**Unbounded support needs a budget.** The standard constraint is the second
moment, $\mathbb{E}[X^2] \leq P$, read as average energy or power at most $P$,
following the channel-coding tradition [1, Ch. 9]. The question: which density is
maximally random under it?

### 7.2 Theorem 13: the Gaussian maximizes differential entropy

**Theorem 13 (maximum differential entropy).** Among all densities $f$ with
$\mathbb{E}_f[X^2] \leq P$,

$$ h(X) \leq h\left(\mathcal{N}(0, P)\right) = \tfrac12 \log(2\pi e P), $$

with equality if and only if $X \sim \mathcal{N}(0, P)$.

*Proof, expanded.* This is the compare-to-the-candidate argument, run once with
the constraint as an inequality so that the case $\mathbb{E}_f[X^2] < P$ is
covered too. Let $f$ be any density with $\mathbb{E}_f[X^2] \leq P$ and finite
$h(f)$, and let $g(x) = \frac{1}{\sqrt{2\pi P}} \, e^{-x^2/2P}$ be the
$\mathcal{N}(0, P)$ density. (The source scribe notes write the normalization as
$\frac{1}{2\pi P}$, a typo for $\frac{1}{\sqrt{2\pi P}}$.)

*Step 1: expand the KL divergence.* Split the log-ratio; the second term is
$h(f)$:

$$ D(f \, \Vert \, g)
   = \mathbb{E}_f\left[\log \frac{f(X)}{g(X)}\right]
   = \mathbb{E}_f\left[\log \frac{1}{g(X)}\right] - h(f). $$

*Step 2: the key step.* The Gaussian's surprisal is a *quadratic*, so its
$f$-average depends on $f$ only through $\mathbb{E}_f[X^2]$:

$$ \mathbb{E}_f\left[\log \frac{1}{g(X)}\right]
   = \log \sqrt{2\pi P} + \frac{\mathbb{E}_f[X^2]}{2P} \log e
   \leq \log \sqrt{2\pi P} + \frac{P}{2P} \log e, $$

using the budget $\mathbb{E}_f[X^2] \leq P$. The right-hand side is what the same
two lines give with $f$ replaced by $g$ itself, for which
$\mathbb{E}_g[X^2] = P$ exactly, so it equals
$\mathbb{E}_g[\log \frac{1}{g(X)}] = h(g) = \frac12 \log(2\pi e P)$.

*Step 3: conclude.* Chain the two steps with the information inequality:

$$ 0 \leq D(f \, \Vert \, g)
   = \mathbb{E}_f\left[\log \tfrac{1}{g(X)}\right] - h(f)
   \leq h(g) - h(f), $$

so $h(f) \leq h(g)$. *Equality* forces both inequalities tight:
$D(f \Vert g) = 0$ gives $f = g$ almost everywhere, which then makes the budget
tight automatically, $\mathbb{E}_f[X^2] = P$; conversely $f = g$ plainly attains
it. Only the Gaussian. **End of proof.**

**Remarks.**

- **Where the tightness lives.** The proof works because $\log \frac1g$ is
  exactly the constrained statistic, a quadratic: the constraint
  $\mathbb{E}[X^2] \leq P$ is precisely what the Gaussian's log-density measures.
  This is the same skeleton as $H \leq \log K$, where the constant
  $\log \frac1u$ encodes "no constraint beyond support", and as the
  bounded-support exercise. The general principle, that the maximum-entropy
  density under linear constraints on statistics $T_i$ is proportional to
  $\exp(\sum_i \lambda_i T_i(x))$, is Jaynes' maximum-entropy principle [6].
- **Variance versus second moment.** Under a variance budget
  $\mathrm{Var}(X) \leq \sigma^2$ with free mean, the winner is
  $\mathcal{N}(\mu, \sigma^2)$ for any $\mu$, by translation invariance of $h$:
  apply the theorem to $X - \mathbb{E}[X]$, noting
  $\mathbb{E}[(X - \mathbb{E}X)^2] = \mathrm{Var}(X)$. Under the raw
  second-moment budget the mean is forced to 0, since a nonzero mean wastes
  budget without adding entropy:
  $\mathbb{E}[X^2] = \mathrm{Var}(X) + (\mathbb{E}X)^2$.
- **Why Gaussians are everywhere in AI.** With only an energy scale known, the
  Gaussian is the least-assuming, maximally random noise model, and as worst-case
  noise nothing hides more information at fixed power. The same-variance lineup
  of Section 6.4, $2.047$ against $1.943$ against $1.792$ bits, is Theorem 13 in
  three data points. Diffusion models corrupt data toward the maximally random
  distribution at the given variance; that story continues in Lecture 4 for
  discrete diffusion and Lecture 8 for Gaussian diffusion.

## 8. References

1. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed.,
   Wiley-Interscience, 2006. DOI 10.1002/047174882X
   (https://doi.org/10.1002/047174882X). Chapter 2 covers joint and conditional
   entropy, chain rules, mutual information, conditional mutual information and
   the data processing inequality; Chapter 8 covers differential entropy, the
   discretization theorem 8.3.1 and maximum entropy. This is the treatment
   followed here.
2. C. E. Shannon, "A Mathematical Theory of Communication," *Bell System
   Technical Journal*, vol. 27, pp. 379-423 and 623-656, 1948. DOI
   10.1002/j.1538-7305.1948.tb01338.x
   (https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). Origin of entropy,
   conditional entropy, and the quantity $H(X) - H(X|Y)$; also of the Gaussian
   maximum-entropy result, Section 20.
3. S. Kullback and R. A. Leibler, "On Information and Sufficiency," *Annals of
   Mathematical Statistics*, vol. 22, no. 1, pp. 79-86, 1951. DOI
   10.1214/aoms/1177729694 (https://doi.org/10.1214/aoms/1177729694). The
   divergence underlying the KL form of mutual information and every
   non-negativity argument above.
4. N. Tishby, F. C. Pereira and W. Bialek, "The Information Bottleneck Method,"
   Proceedings of the 37th Allerton Conference, 1999. arXiv:physics/0004057
   (https://arxiv.org/abs/physics/0004057). The trade-off between $I(Z;Y)$ and
   $I(Z;X)$ behind the feature-quality and "layers only forget" discussion.
5. R. Shwartz-Ziv and N. Tishby, "Opening the Black Box of Deep Neural Networks
   via Information," 2017. arXiv:1703.00810 (https://arxiv.org/abs/1703.00810).
   The layer-as-Markov-chain reading of a deep net and the empirical study of
   $I(X; Z_\ell)$ along training; empirically contested, but the framing used in
   Section 5.
6. E. T. Jaynes, "Information Theory and Statistical Mechanics," *Physical
   Review*, vol. 106, no. 4, pp. 620-630, 1957. DOI 10.1103/PhysRev.106.620
   (https://doi.org/10.1103/PhysRev.106.620). The maximum-entropy principle
   generalizing Section 7's theorem.
7. D. J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*,
   Cambridge University Press, 2003. Free online at
   https://www.inference.org.uk/mackay/itila/. A gentler parallel treatment of
   joint and conditional entropy and mutual information, Chapter 8.
