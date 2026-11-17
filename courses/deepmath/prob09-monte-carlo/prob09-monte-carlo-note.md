# Deep Learning Math 9 - Monte Carlo and Importance Sampling (Lecture Note)

**About this file.** This is a linear, screen-reader-friendly edition of the Lecture 9 companion note. It is text only: every figure, chart and table of the original has been replaced by a description or by a list that reads in order, and all mathematics is written in LaTeX. Section numbers match the original note, so a reference to "Section 7.6" means the same place in both editions. Nothing else is needed to read it.

<!-- PREAMBLE (INT) -->

<!-- BEGIN S01 -->
### 1. Monte Carlo & Importance Sampling [S01]

(placeholder, INT)
<!-- END S01 -->

<!-- BEGIN S02 -->
### 2. Contents [S02]

(placeholder, INT)
<!-- END S02 -->

<!-- BEGIN S03 -->
### 3. 01 · Estimate an Expectation [S03]

(placeholder, INT)
<!-- END S03 -->

<!-- BEGIN S04 -->
### 4. A Known Model, a Hard Average [S04]

**Message.** Being able to draw from a model does not make its averages easy to compute.

The slide is a three-box flow. The first box is the sampler $p$: here a language model, from which drawing one reply $X$ is easy. The second box is a fixed scoring rule $f$: evaluating one reply, $f(X)$, is also easy. The third box, drawn with a dashed red border, is the target $\mu = \mathbb E_p[f(X)]$, the average score over all replies the model could produce. That number is what we want, and it is the hard part. The rest of Part 01 turns the two easy boxes into an estimate of the hard one.

The three roles stay fixed for the whole lecture: $X$ is the random outcome, $p$ is the distribution we sample from, $f$ is a fixed function we can evaluate, and $\mu$ is the number we want.

**Details.**

**Why the average is hard.** A reply of $T$ tokens over a vocabulary $V$ is one of $|V|^T$ sequences, so the exact average is a sum with $|V|^T$ terms. Writing $p$ down is not the obstacle; summing over its support is. "Hard" on the slide means *no convenient closed form and too many terms to sum*, not "uncomputable".

**Numerical difficulty is not a missing antiderivative.** A closed form may exist and still be expensive to evaluate, or an integral may have no elementary antiderivative yet be easy to compute numerically in one dimension. Whether a given expectation has a closed form depends on the pair $(p, f)$: some nonlinear functions of a Gaussian have no closed-form expectation, and some non-Gaussian expectations do. No general rule by family is claimed here.

**Link to prob08.** prob08 closed with a bridge slide: Gaussian models gave closed-form answers, many expectation integrals in more general models do not, and the remedy is to replace $\int g(x) f_X(x)\,dx$ by an average of $g$ over IID samples. This lecture takes that remedy and asks how accurate it is and what it costs.

**Sources.**

E01: prob08's closing bridge slide, course repository at commit b20ab73. E02: Owen, *Monte Carlo theory, methods and examples*, Ch. 1-2. The $|V|^T$ count is direct counting; the language-model setting is an illustration, not a cited system.
<!-- END S04 -->

<!-- BEGIN S06 -->
### 5. Sample, Evaluate, Average [S06]

**Message.** An expectation can be estimated by averaging evaluations at random draws.

The slide shows the recipe as three numbered boxes. Step 1, *sample*: draw $X_1, \dots, X_n$ independently from $p$. Step 2, *evaluate*: compute $f(X_1), \dots, f(X_n)$. Step 3, *average*: report $\frac1n \sum_i f(X_i)$ as the estimate of $\mu$. Each step uses only an easy box from the previous slide.

The recipe needs draws from $p$, not a formula for the density $p(x)$. A language model, a simulator or a physical experiment can supply draws even when nobody can write down the probability of a given outcome. Whether the average is any good is a separate question; the next slides answer it, and only under stated conditions.

**Details.**

**IID in plain words.** "Independent and identically distributed": each draw comes from the same $p$, and no draw influences another. Re-using one draw twice, or changing the sampler mid-run, breaks it.

**Hold $f$ fixed.** The function $f$ must be chosen before the draws are made and kept the same for every draw. If $f$ is tuned after looking at the sample, the average estimates something else, and the error guarantees below do not apply.

**Integrability.** The target exists only if $\mathbb E_p|f(X)| \lt \infty$. The slide states this as an assumption; S16 makes it part of the formal estimator.

**Sources.**

E01: sample-mean facts from prob05 (pp. 39, 46, 93), course repository at commit b20ab73. E02: Owen, Ch. 1-2, Section 2.1.
<!-- END S06 -->

<!-- BEGIN S26 -->
### 6. Six Draws Give a Noisy Estimate [S26]

**Message.** With six points the recipe gives a number, but nothing yet about how close it is.

The figure shows the square $[-1,1]^2$ with the unit disk inside it. Four points sit inside the disk (filled blue) and two outside (hollow grey). Take $X$ uniform on the square and $f(X) = 4 \cdot \mathbf 1\{X \text{ in disk}\}$. The disk covers $\pi/4$ of the square, so $\mu = 4 \cdot \pi/4 = \pi$. Four hits out of six give $\hat\mu_6 = 4 \cdot 4/6 = 8/3 \approx 2.67$.

The six points are hand-chosen to show the recipe. They are not a random run, and one estimate of $8/3$ against a true $\pi$ says nothing about how often the recipe is that far off. That needs the distribution of the estimator, which comes next.

**Details.**

**Full ledger.** For each point, compare $x^2 + y^2$ with 1:

- $(0.5, 0.5)$: $0.50$, in
- $(-0.9, 0.8)$: $1.45$, out
- $(0.2, -0.6)$: $0.40$, in
- $(-0.4, 0.1)$: $0.17$, in
- $(0.8, -0.7)$: $1.13$, out
- $(0.3, 0.9)$: $0.90$, in

Four hits, so $\hat\mu_6 = 4 \cdot \tfrac46 = \tfrac83$.

**No inference from this run.** A hand-picked sample does not support an error bar or a confidence statement. For genuinely IID uniform draws, $Y = 4\cdot\mathbf 1\{\text{hit}\}$ has $\mathbb E[Y] = \pi$ and $\mathrm{Var}(Y) = \pi(4 - \pi) \approx 2.6968$; S19 and S22 use these exact values.

**Sources.**

E17: six hand-chosen points and their hit count, recomputed from exact disk geometry. Figure: inline SVG; coordinates and the ledger printed by `gen/p9a_part01.py` (deterministic, no random draws).
<!-- END S26 -->

<!-- BEGIN S16 -->
### 7. Monte Carlo Reuses the Sample Mean [S16]

**Message.** Renaming $Y_i = f(X_i)$ turns the Monte Carlo estimator into an ordinary sample mean.

The display labels each part of the estimator. $\hat\mu_n$ is the estimate of $\mu$; $\frac1n\sum_{i=1}^n$ is the average; $f(X_i)$ is the $i$th evaluation, renamed $Y_i$. With $X_1, \dots, X_n$ IID from $p$, the $Y_i$ are IID scalars, and $\hat\mu_n = \bar Y_n$. Every fact about sample means now applies without new proofs.

The recall card states the two facts needed first: if $\mathbb E|Y_1| \lt \infty$, then $\mathbb E[\bar Y_n] = \mathbb E[Y_1]$ and $\bar Y_n \to \mathbb E[Y_1]$ by the law of large numbers. The two bullets keep the two moment conditions apart. A finite first moment is enough for $\mu$ to exist and for the LLN. A finite variance $\sigma_f^2 = \mathrm{Var}_p(f(X))$ is an extra assumption, and it is what error rates need.

**Details.**

**Definition.** Let $p$ be a distribution and $f$ a fixed function with $\mathbb E_p|f(X)| \lt \infty$. Set $\mu = \mathbb E_p[f(X)]$. For $X_1, \dots, X_n$ IID from $p$, the Monte Carlo estimator is

$$\hat\mu_n = \frac1n \sum_{i=1}^n f(X_i).$$

**Why $Y_i$ are IID.** A fixed function of independent, identically distributed inputs gives independent, identically distributed outputs. This is why $f$ must not depend on the sample.

**Consistency.** Under $\mathbb E|Y_1| \lt \infty$ alone, the strong law of large numbers gives $\hat\mu_n \to \mu$ with probability 1. It is imported from prob05, not reproved, and it says nothing about how fast.

**Notation.** $\sigma_f^2$ is the population variance of $f(X)$ under $p$, a fixed unknown number. The observed sample spread $s_Y$ appears only on S114.

**Sources.**

E01: sample-mean expectation, variance, LLN and CLT in prob05 (pp. 39, 46, 93), commit b20ab73. E02: Owen, Ch. 1-2, Section Section 2.1-2.2 (first absolute moment for the mean and LLN, finite variance for RMSE and CLT).
<!-- END S16 -->

<!-- BEGIN S19 -->
### 8. Unbiased Does Not Mean Accurate [S19]

**Message.** The estimator is right on average at every $n$, yet a single run can be far off.

The top line is linearity of expectation: $\mathbb E[\hat\mu_n] = \frac1n\sum_i \mathbb E_p[f(X_i)] = \mu$, for every $n$, including $n = 1$.

The bar chart shows the exact distribution of $\hat\mu_6$ for six IID darts. The estimate is $4K/6$, where $K$, the number of hits, is Binomial$(6, \pi/4)$. The x-axis lists the seven possible values $0, \tfrac23, \tfrac43, 2, \tfrac83, \tfrac{10}3, 4$; bar heights are their probabilities. The large bars are $0.096$ at 2, $0.263$ at $\tfrac83$, $0.385$ at $\tfrac{10}3$ and $0.235$ at 4. A dashed red line marks the mean, $\pi$, which falls between $\tfrac83$ and $\tfrac{10}3$. No possible value equals $\pi$, and about 35% of runs miss it by at least 0.5. Unbiasedness is a statement about the centre of this distribution, not about any single run.

**Details.**

**Proof of unbiasedness.** Each $X_i \sim p$, so $\mathbb E[f(X_i)] = \mu$. Linearity gives

$$\mathbb E[\hat\mu_n] = \frac1n\sum_{i=1}^n \mathbb E[f(X_i)] = \frac1n \cdot n\mu = \mu.$$

Independence is not used: identically distributed draws with $\mathbb E|f(X)| \lt \infty$ suffice for this identity. Independence matters for the variance on S22.

**Bias and variance.** In prob07's decomposition, mean squared error is squared bias plus variance. Here the bias is zero, so all of the error is variance. That is the quantity averaging must shrink.

**Exact numbers.** $\Pr(|\hat\mu_6 - \pi| \ge 0.5) = 0.3523$ and the RMSE at $n = 6$ is $0.6704$, both from the Binomial$(6, \pi/4)$ law.

**Sources.**

E01: bias-variance and the sample mean, prob07 (pp. 98, 102), commit b20ab73. E17: darts setup. Figure: inline SVG; probabilities and bar coordinates printed by `gen/p9a_part01.py` (exact Binomial probabilities, no random draws).
<!-- END S19 -->

<!-- BEGIN S22 -->
### 9. Averaging Reduces RMSE [S22]

**Message.** With IID draws and finite variance, the typical error falls like $1/\sqrt n$.

The first line states both assumptions: IID draws, and finite $\sigma_f^2 = \mathrm{Var}_p(f(X))$. The display defines the root-mean-squared error, $\mathrm{RMSE}(\hat\mu_n) = \sqrt{\mathbb E[(\hat\mu_n - \mu)^2]}$. Because the estimator is unbiased, this equals its standard deviation, $\sigma_f/\sqrt n$.

The plot shows this exact formula for the darts, where $\sigma_f = \sqrt{\pi(4-\pi)} \approx 1.64$. Both axes are logarithmic: $n$ from 10 to $10^6$ across, RMSE from 1 down to $10^{-3}$. On log-log axes the curve is a straight line. Two marked points read $0.164$ at $n = 100$ and $0.0164$ at $n = 10^4$: one hundred times as many draws make the RMSE ten times smaller.

**Details.**

**Variance of the average.** For independent $Y_i$ with common variance $\sigma_f^2$, the covariances vanish and

$$\mathrm{Var}(\bar Y_n) = \frac{1}{n^2}\sum_{i=1}^n \mathrm{Var}(Y_i) = \frac{\sigma_f^2}{n}.$$

Unbiasedness makes the squared bias zero, so $\mathrm{RMSE}^2 = \mathrm{Var}(\hat\mu_n) = \sigma_f^2/n$.

**Darts numbers.** $\sigma_f^2 = \pi(4 - \pi) \approx 2.6968$, $\sigma_f \approx 1.642$. RMSE: $0.519$ at $n = 10$, $0.164$ at $10^2$, $0.0164$ at $10^4$, $0.00164$ at $10^6$.

**What RMSE is not.** RMSE describes the spread over many repeated runs. It is not a bound on the error of the run in hand: a single run can miss by several RMSEs. Bounds that hold with stated probability come on S115 and S24.

**Sources.**

E02: Owen, Ch. 1-2, Section Section 2.1-2.2 (variance $\sigma_f^2/n$ under finite variance). E01: prob05 sample-mean variance (p. 39), prob07 MSE decomposition (pp. 98, 102), commit b20ab73. E17: $\pi(4-\pi)$. Figure: inline SVG; RMSE values and coordinates printed by `gen/p9a_part01.py`.
<!-- END S22 -->

<!-- BEGIN S114 -->
### 10. Estimating the Error Bar [S114]

**Message.** The sample itself estimates the standard error, but only the typical spread, not this run's error.

The assumptions come first: IID evaluations, finite variance, and at least two draws. The flow then reads left to right. The observed data $Y_1, \dots, Y_n$ give the sample variance $s_Y^2 = \frac{1}{n-1}\sum_i (Y_i - \bar Y_n)^2$, and dividing its square root by $\sqrt n$ gives the estimated standard error $\widehat{\mathrm{SE}} = s_Y/\sqrt n$.

The next line separates the two quantities. The true standard error $\sigma_f/\sqrt n$ uses the unknown population SD $\sigma_f$; the observed $s_Y$ is our estimate of it. The highlight states the limit: $\widehat{\mathrm{SE}}$ estimates how far runs typically land from $\mu$, not the error $|\hat\mu_n - \mu|$ of the run in hand.

**Details.**

**Units.** $s_Y$ and $\widehat{\mathrm{SE}}$ have the units of $f$; $s_Y^2$ has squared units. Report the SE, not the variance, next to the estimate.

**Why $n - 1$.** With divisor $n - 1$, $\mathbb E[s_Y^2] = \sigma_f^2$ for IID data with finite variance. That needs $n \ge 2$.

**Example of the right data.** The formula applies to genuinely IID evaluations, for instance a fixed scoring rule applied to independently sampled model replies. It does not apply to the six hand-chosen darts on S26.

**Unseen tails.** $s_Y$ is always finite, because it is computed from finitely many numbers. It cannot show that $\sigma_f$ is finite. If rare draws carry very large values that the sample never hit, $s_Y$ will understate the spread.

**Sources.**

E02: Owen, Ch. 1-2, Section Section 2.1-2.2 and 2.7-2.8 (estimated standard error, its assumptions). E01: prob05 sample-mean variance (p. 39), commit b20ab73.
<!-- END S114 -->

<!-- BEGIN S115 -->
### 11. Approximate Intervals, Exact Guarantees [S115]

**Message.** An error bar can be a large-$n$ approximation or a finite-$n$ guarantee; they answer different questions.

The left card is the usual interval $\bar Y_n \pm 1.96\,\widehat{\mathrm{SE}}$. Its coverage is about 95% when $n$ is large, under IID draws with $0 \lt \sigma_f^2 \lt \infty$. It is an approximation; a large $n$ alone does not certify that the normal approximation is accurate for the integrand at hand.

The right card is Chebyshev's inequality applied to $\bar Y_n$: $\Pr(|\bar Y_n - \mu| \ge \epsilon) \le \sigma_f^2/(n\epsilon^2)$. It holds at every $n$, but it needs the true $\sigma_f^2$, or a proven upper bound on it. Plugging in the observed $s_Y^2$ voids the guarantee. The bottom line names the difference: approximate coverage against a guaranteed tail bound.

**Details.**

**Where 1.96 comes from.** By the CLT, $\sqrt n(\bar Y_n - \mu)/\sigma_f$ is approximately standard normal for large $n$. Replacing $\sigma_f$ by $s_Y$ (studentization) keeps the same limit. The value 1.96 is the 0.975 quantile of the standard normal, $1.95996$ to five decimals.

**Chebyshev.** Apply $\Pr(|Z - \mathbb E Z| \ge \epsilon) \le \mathrm{Var}(Z)/\epsilon^2$ to $Z = \bar Y_n$, with $\mathrm{Var}(\bar Y_n) = \sigma_f^2/n$. Setting the right side to $\delta$ gives a sufficient sample size:

$$n \ge \frac{\sigma_f^2}{\delta\,\epsilon^2}.$$

**Darts.** With the known $\sigma_f^2 = \pi(4-\pi)$, $\epsilon = 0.01$ and $\delta = 0.05$, $n \ge 539{,}353.24$, so $n = 539{,}354$ suffices. This is sufficient, not minimal. It uses a known variance as a teaching benchmark.

**Consistency is weaker.** Chebyshev also shows $\Pr(|\bar Y_n - \mu| \ge \epsilon) \to 0$ for each fixed $\epsilon$, which is the weak law. It gives no interval for one run.

**Sources.**

E02: Owen, Ch. 1-2, Section Section 2.7-2.8 (asymptotic intervals versus nonasymptotic bounds). E01: CLT in prob05 (p. 93), commit b20ab73. E17: Chebyshev sample size 539,354. Quantile and arithmetic printed by `gen/p9a_part01.py`.
<!-- END S115 -->

<!-- BEGIN S24 -->
### 12. Bounded Averages Concentrate [S24]

**Message.** If $f$ has a known range, Hoeffding gives a finite-sample bound with no variance needed.

The recall card restates prob06's Hoeffding inequality for IID $W_i \in [0,1]$: $\Pr(|\bar W_n - \mathbb E W_1| \ge t) \le 2e^{-2nt^2}$. If instead $Y_i \in [a, b]$ with $a \lt b$, rescale with $W_i = (Y_i - a)/(b - a)$ and $t = \epsilon/(b - a)$. The display gives the result: $\Pr(|\bar Y_n - \mu| \ge \epsilon) \le 2\exp(-2n\epsilon^2/(b-a)^2)$.

For the darts, $Y \in [0, 4]$. With $\epsilon = 0.01$ and $\delta = 0.05$, $n \ge 295{,}111$ suffices. The range must be known in advance, not estimated from the sample, and $f$ must be fixed before sampling.

**Details.**

**Rescaling.** $W_i \in [0,1]$ and $\bar W_n - \mathbb E W_1 = (\bar Y_n - \mu)/(b - a)$, so the event $|\bar Y_n - \mu| \ge \epsilon$ is the event $|\bar W_n - \mathbb E W_1| \ge \epsilon/(b-a)$.

**Inverting for $n$.** Set $2\exp(-2n\epsilon^2/(b-a)^2) \le \delta$:

$$n \ge \frac{(b-a)^2 \ln(2/\delta)}{2\epsilon^2}.$$

Darts: $(b-a)^2 = 16$, $\ln 40 = 3.688879$, so $n \ge 295{,}110.36$, rounded up to $295{,}111$. At that $n$ the bound equals $0.05$.

**Comparison.** Chebyshev with the known variance needed $539{,}354$ (S115), about $1.83$ times as many. Both are sufficient sample sizes from upper bounds, not minimal ones, and neither says how a particular run behaves. For scale, the RMSE at $n = 295{,}111$ is about $0.0030$.

**Edge case.** If $Y$ is constant, $a = b$ is not allowed, but no bound is needed: $\bar Y_n = \mu$ exactly.

**Fixed versus data-selected $f$.** The bound holds for one $f$ chosen before sampling. If $f$ is picked among many candidates using the same sample, the bound no longer applies to the picked one.

**Sources.**

E01: Hoeffding on $[0,1]$, prob06 (p. 18), commit b20ab73; prob06 states it on $[0,1]$, and the $[a,b]$ form is the rescaling above. E17: Hoeffding sample size 295,111. Arithmetic printed by `gen/p9a_part01.py`.
<!-- END S24 -->

<!-- BEGIN S33 -->
### 13. The Rate Is Not the Cost [S33]

**Message.** Dimension is absent from the $1/\sqrt n$ exponent, but not from the constant or the cost.

For $X \in \mathbb R^d$, the display splits the budget in two. The error is $\mathrm{RMSE} = \sigma_f(d)/\sqrt n$, where the overbrace warns that $\sigma_f(d)$ may grow with $d$. The work is $n \times c(d)$, where $c(d)$ is the cost of one draw plus one evaluation. The bullet explains why $d$ is missing from the exponent: the proof on S22 only used the scalars $Y_i = f(X_i)$, never the space $X$ lives in.

The highlight is the takeaway: a dimension-free rate is not a dimension-free budget.

**Details.**

**What the proof never asked.** The variance argument needs IID draws and finite $\sigma_f^2$. It does not need $f$ to be smooth or continuous, and it does not refer to $d$.

**Where $d$ can enter.** Two places. The variance $\sigma_f^2$ is a property of $f$ under $p$ and can grow with $d$. The cost $c(d)$ of producing and scoring one draw usually grows with $d$; for a language model, with reply length. Neither is controlled by the theorem.

**Sources.**

E02: Owen, Ch. 1-2 (the $\sigma_f/\sqrt n$ rate; E02 explicitly does not establish dimension-independent cost or variance). E03: Owen, Ch. 7, Section Section 7.1, 7.4.
<!-- END S33 -->

<!-- BEGIN S37 -->
### 14. Tensor Grids Grow With Dimension [S37]

**Message.** For a tensor grid the error exponent shrinks with $d$; for Monte Carlo it does not.

The formula line sets the comparison. A tensor grid with $m$ points per axis uses $N = m^d$ evaluations, and for a smooth $f$ its error scales like $N^{-2/d}$. Monte Carlo with $N$ evaluations has RMSE scaling like $N^{-1/2}$.

The plot is schematic, with every constant set to 1. Both axes are logarithmic: evaluations $N$ from 1 to $10^8$ across, error from 1 down to $10^{-4}$. Each scaling is a straight line from the top left. The solid blue MC line has slope $-1/2$ and reaches $10^{-4}$ at $N = 10^8$. Three red dashed grid lines have slope $-2/d$: the dotted $d = 2$ line drops twice as steeply and reaches $10^{-4}$ already at $N = 10^4$; the $d = 8$ line ends at $10^{-2}$; the $d = 20$ line ends near $10^{-0.8}$, barely below 1. The grid's error is deterministic; MC's is an RMSE. The plot compares exponents, not runtimes.

**Details.**

**The $N = m^d$ argument.** In one dimension the midpoint rule with $m$ cells has error of order $m^{-2}$ for a sufficiently smooth integrand. The tensor product of $d$ such rules keeps error of order $m^{-2}$ but uses $N = m^d$ points. Substituting $m = N^{1/d}$ gives error of order $N^{-2/d}$. The constant depends on derivatives of $f$.

**Points per axis.** At $N = 10^8$: $m = 10^4$ for $d = 2$, $m = 10$ for $d = 8$, and $m \approx 2.5$ for $d = 20$, already fewer than three points per axis.

**The $d = 4$ case.** At $d = 4$, $-2/d = -1/2$: the grid has MC's exponent, which is why the plot shows $d = 2, 8, 20$ instead. Equal exponents are not a wall-clock threshold. Constants, smoothness and the cost per evaluation decide which method is cheaper at a given accuracy, and higher-order or non-tensor rules change the exponents.

**Limits.** This is one comparison for smooth integrands on regular tensor grids. It does not show that grids fail at any particular dimension, and it ignores quasi-Monte Carlo and other methods outside this lecture.

**Sources.**

E03: Owen, *Monte Carlo theory, methods and examples*, Ch. 7, Section Section 7.1 and 7.4 (tensor midpoint scaling; no universal dimension threshold). Figure: inline SVG, schematic with unit constants; line end points and points per axis printed by `gen/p9a_part01.py`.
<!-- END S37 -->

<!-- BEGIN S116 -->
### 15. Rare Events Need Relative Error [S116]

**Message.** For a rare event the absolute error is small, but the error relative to the answer is huge.

The running rare event: $X \sim \mathrm{Exp}(1)$ and $Y = \mathbf 1\{X \gt 10\}$, so $\mu = \rho = \Pr(X \gt 10) = e^{-10} \approx 4.5 \times 10^{-5}$. One indicator has variance $\rho(1-\rho)$, which is tiny. The useful scale is relative: $\mathrm{RMSE}/|\mu| = \sqrt{(1-\rho)/(n\rho)}$, which is large unless $n$ is far above $1/\rho$.

The plot shows per-draw spreads against the event probability $\rho$, both axes logarithmic: $\rho$ from $10^{-6}$ to $0.5$ across, values from $10^{-3}$ to $10^3$ up, with a grey dashed reference line at 1. The dashed blue curve is the absolute SD $\sigma_f = \sqrt{\rho(1-\rho)}$; it falls as the event gets rarer. The solid red curve is the relative SD $\sigma_f/\rho$; it rises. A vertical dotted line marks $\rho = e^{-10}$, where the absolute SD is about $0.0067$ and the relative SD about $148$. Dividing either by $\sqrt n$ gives the RMSE. For a relative RMSE of at most $0.1$, ordinary Monte Carlo needs $n \ge 2{,}202{,}547$.

**Details.**

**Calculation.** $Y$ is Bernoulli$(\rho)$, so $\mathrm{Var}(Y) = \rho(1-\rho)$ and

$$\frac{\mathrm{RMSE}(\hat\mu_n)}{\rho} = \sqrt{\frac{\rho(1-\rho)}{n\rho^2}} = \sqrt{\frac{1-\rho}{n\rho}}.$$

At $\rho = e^{-10}$: $\rho = 4.539993 \times 10^{-5}$, $\rho(1-\rho) = 4.539787 \times 10^{-5}$, absolute SD $0.006738$. The per-draw relative variance is $(1-\rho)/\rho = e^{10} - 1 = 22025.4657948$, relative SD $148.41$.

**Sample size.** Relative RMSE $\le 0.1$ means $(e^{10}-1)/n \le 0.01$, so $n \ge 2{,}202{,}546.58$, rounded up to $2{,}202{,}547$. For scale, $1/\rho \approx 22{,}026$ draws produce one hit on average.

**Two errors, two scales.** An absolute RMSE of $0.0067/\sqrt n$ looks small next to 1, but $\mu$ itself is about $4.5 \times 10^{-5}$. A run of $10^4$ draws sees no hit with probability $0.635$, and then reports $\hat\mu = 0$: a tiny absolute error and a 100% relative error. Relative error is defined only for $\mu \ne 0$.

Changing the sampler so that the event is no longer rare is the subject of Part 02, which reuses this exact setup.

**Sources.**

E11: running rare event $p = \mathrm{Exp}(1)$, $f = \mathbf 1\{x \gt 10\}$, $\mu = e^{-10}$; ordinary relative variance $e^{10} - 1 = 22025.4657948$ and $n \ge 2{,}202{,}547$ (our calculation). Figure: inline SVG; curve points, marker values and sample size printed by `gen/p9a_part01.py`.
<!-- END S116 -->

<!-- BEGIN S41 -->
### 16. 02 · Change the Sampler [S41]

(placeholder, INT)
<!-- END S41 -->

<!-- BEGIN S43 -->
### 17. Most Draws Miss the Tail [S43]

(placeholder, P2)
<!-- END S43 -->

<!-- BEGIN S44 -->
### 18. A Rare Event Needs Many Samples [S44]

(placeholder, P2)
<!-- END S44 -->

<!-- BEGIN S45 -->
### 19. Visit Useful Outcomes More Often [S45]

(placeholder, P2)
<!-- END S45 -->

<!-- BEGIN S50 -->
### 20. Correct Each Visit's Weight [S50]

(placeholder, P2)
<!-- END S50 -->

<!-- BEGIN S46 -->
### 21. Importance Sampling Preserves the Target [S46]

(placeholder, P2)
<!-- END S46 -->

<!-- BEGIN S47a -->
### 22. Proof: Cancel the Proposal [S47a]

(placeholder, P2)
<!-- END S47a -->

<!-- BEGIN S47b -->
### 23. Proof (continued): Check the Missing Region [S47b]

(placeholder, P2)
<!-- END S47b -->

<!-- BEGIN S48 -->
### 24. Missing Support Cannot Be Repaired [S48]

(placeholder, P2)
<!-- END S48 -->

<!-- BEGIN S49 -->
### 25. Average the Weighted Integrand [S49]

(placeholder, P2)
<!-- END S49 -->

<!-- BEGIN S117 -->
### 26. A Practical Exponential Proposal [S117]

(placeholder, P2)
<!-- END S117 -->

<!-- BEGIN S118 -->
### 27. More Tail Visits, Corrected Weights [S118]

(placeholder, P2)
<!-- END S118 -->

<!-- BEGIN S119 -->
### 28. Compute the Proposal's Error [S119]

(placeholder, P2)
<!-- END S119 -->

<!-- BEGIN S120 -->
### 29. Same Target, Less Relative Error [S120]

(placeholder, P2)
<!-- END S120 -->

<!-- BEGIN S54 -->
### 30. Coverage and Variance Are Different [S54]

(placeholder, P2)
<!-- END S54 -->

<!-- BEGIN S55 -->
### 31. 03 · Control Proposal Risk [S55]

(placeholder, INT)
<!-- END S55 -->

<!-- BEGIN S56 -->
### 32. The Second Moment Decides [S56]

(placeholder, P2)
<!-- END S56 -->

<!-- BEGIN S57 -->
### 33. Follow the Weighted Integrand [S57]

(placeholder, P2)
<!-- END S57 -->

<!-- BEGIN S59 -->
### 34. The Optimal Proposal [S59]

(placeholder, P2)
<!-- END S59 -->

<!-- BEGIN S60 -->
### 35. Proof: A Common Lower Bound [S60]

(placeholder, P2)
<!-- END S60 -->

<!-- BEGIN S61 -->
### 36. Proof (continued): Attain the Bound [S61]

(placeholder, P2)
<!-- END S61 -->

<!-- BEGIN S63 -->
### 37. One-Sign Integrands Permit Zero Variance [S63]

(placeholder, P2)
<!-- END S63 -->

<!-- BEGIN S64 -->
### 38. The Oracle Needs a Normalizer [S64]

(placeholder, P2)
<!-- END S64 -->

<!-- BEGIN S66 -->
### 39. Light Tails Can Destroy Variance [S66]

(placeholder, P2)
<!-- END S66 -->

<!-- BEGIN S68 -->
### 40. A Finite Mean, an Infinite Second Moment [S68]

(placeholder, P2)
<!-- END S68 -->

<!-- BEGIN S121 -->
### 41. Consistency Is Not an Error Bar [S121]

(placeholder, P2)
<!-- END S121 -->

<!-- BEGIN S69 -->
### 42. Check the Integrand, Not Just Weights [S69]

(placeholder, P2)
<!-- END S69 -->

<!-- BEGIN S72 -->
### 43. 04 · Remove the Normalizer [S72]

(placeholder, INT)
<!-- END S72 -->

<!-- BEGIN S73 -->
### 44. The Target Is Known Up to Z [S73]

**Message.** An unnormalized density fixes the shape of the target but not its height, so the ratio $p/q$ cannot be evaluated.

**Slide.** $p=\tilde p/Z$ with $\tilde p\ge 0$ and target $\mu=E_p[f(X)]$; $Z$ is unknown but neither zero nor infinite. Figure: a dependency chain. $\tilde p(x)$ can be evaluated; $Z$ is unknown with $0<Z<\infty$; therefore $p=\tilde p/Z$ cannot be evaluated, and the IS weight $w=p/q$ is blocked without $Z$.

Often we can evaluate $\tilde p(x)$ but cannot compute $Z=\int\tilde p(x)\,dx$. In Bayes' rule the posterior is prior times likelihood divided by an evidence integral; only the numerator is available pointwise. Writing $p\propto\tilde p$ gives $p(x)/q(x)=\tilde p(x)/(Z\,q(x))$, which still contains the unknown $Z$, so ordinary IS is blocked.

**Details.** Assume $\tilde p\ge 0$ and $0<Z<\infty$. Unknown means not computed; $Z$ is a fixed finite positive number. $Z=0$ leaves no target; $Z=\infty$ is an improper target, outside the theorems here. The mean also needs $E_p|f(X)|<\infty$.

**Sources.** E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Figure: our dependency diagram, no data.
<!-- END S73 -->

<!-- BEGIN S74 -->
### 45. Compute Unnormalized Weights [S74]

**Message.** Every computable weight is the true weight times the same unknown $Z$.

**Slide.** Draw $X_i$ iid from $q$; $\tilde w_i=\tilde p(X_i)/q(X_i)=Z\,w_i$ with $w_i=p(X_i)/q(X_i)$. Support: $q>0$ wherever $\tilde p>0$, not only where $fp\ne 0$.

One $\tilde w_i$ alone is useless as an estimate of $w_i$, but $Z$ is the same for every draw, so it can cancel in a ratio.

**Details.** Self-normalization needs full target support because its denominator estimates the whole mass $Z$; ordinary IS only needs $q>0$ where $fp\ne 0$. Example (our calculation): $p$ uniform on $\{1,2,3,4\}$, $q$ uniform on $\{1,2,3\}$, $f=1\{x=1\}$, $\mu=1/4$. Ordinary IS mean $E_q[wf]=1/4$ is correct; the self-normalized limit $E_q[wf]/E_q[w]=(1/4)/(3/4)=1/3$ is wrong. Draws where $\tilde p=0$ are allowed: they get weight 0 and are wasted, not harmful.

**Sources.** E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Support example: `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S74 -->

<!-- BEGIN S75 -->
### 46. Normalize Only a Positive Total [S75]

**Message.** Dividing by the sampled total cancels $Z$, but the estimator exists only when that total is positive.

**Slide.** When $\sum_j\tilde w_j>0$: $\hat\mu_{\mathrm{SN}}=\sum_i\tilde w_i f(X_i)/\sum_j\tilde w_j=\sum_i\bar w_i f(X_i)$ with $\bar w_i=\tilde w_i/\sum_j\tilde w_j=w_i/\sum_j w_j$. Shares sum to one, no extra division by $n$. All sampled weights zero: undefined, not silently 0.

$Z$ appears above and below the bar and cancels. The estimate is a weighted average of the $f(X_i)$.

**Details.** Weights are nonnegative since $\tilde p\ge 0$ and $q(X_i)>0$. If all are zero the formula is $0/0$; report the event or apply a documented convention. Full support does not prevent this, since $q$ may put mass where $\tilde p=0$: if $q$ gives probability $\pi$ to $\{\tilde p>0\}$, then $P(\text{total}=0)=(1-\pi)^n$. With $\pi=1/2$: $1/2$ at $n=1$, $1/1024$ at $n=10$ (our calculation).

**Sources.** E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Probabilities: `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S75 -->

<!-- BEGIN S76 -->
### 47. Two Averages Form One Ratio [S76]

**Message.** SNIS is a ratio of two unbiased averages computed from the same draws.

**Slide.** Conditions line, then a figure: the same draws feed two averages, $A_n=\frac1n\sum\tilde w_i f(X_i)$ with mean $\int\tilde p f=Z\mu$, and $B_n=\frac1n\sum\tilde w_i$ with mean $\int\tilde p=Z$; the two are labelled "shared, so dependent" and combine into $A_n/B_n=\hat\mu_{\mathrm{SN}}$. Each average is unbiased; the ratio is not: $E[A_n/B_n]\ne E[A_n]/E[B_n]$ in general.

Under full support, $E_q[\tilde w f]=\int\tilde p f\,dx=Z\mu$ and $E_q[\tilde w]=\int\tilde p\,dx=Z$, so the ratio of means is $\mu$.

**Details.** Full support makes the integrals over $\{q>0\}$ include all target mass. Integrability: $E_q|\tilde w f|=Z\,E_p|f|<\infty$. Division is nonlinear and $A_n$, $B_n$ share draws, so the mean of the ratio differs from the ratio of means in general; slide 49 gives an exact case.

**Sources.** E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Figure: our flow diagram, no data.
<!-- END S76 -->

<!-- BEGIN S77 -->
### 48. The Ratio Converges to the Target [S77]

**Message.** Both averages converge, the denominator's limit $Z$ is positive, so the ratio converges to $\mu$.

**Slide.** Three steps: $A_n\to Z\mu$ a.s. (strong LLN); $B_n\to Z$ a.s. (strong LLN); $A_n/B_n\to\mu$ a.s. ($u/v$ continuous where $v\ne 0$). Positive limit $Z$: eventually $B_n>0$. A limit only: no finite-$n$ unbiasedness, and finite batches can still total zero.

**Details.** Conditions: $0<Z<\infty$; $q>0$ wherever $\tilde p>0$; $E_p|f|<\infty$, giving $E_q|\tilde w f|=Z\,E_p|f|<\infty$ and $E_q\tilde w=Z$. Pathwise: if $a_n\to a$ and $b_n\to b\ne 0$ then $a_n/b_n\to a/b$; on the probability-one event where both averages converge, $B_n>Z/2>0$ for all large $n$. "Large" depends on the path, so no fixed $n$ guarantees $B_n>0$ (slide 46), and convergence says nothing about $E[\hat\mu_{\mathrm{SN}}]$ at fixed $n$ (slide 49).

**Sources.** E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10.
<!-- END S77 -->

<!-- BEGIN S78 -->
### 49. One Draw Exposes SNIS Bias [S78]

**Message.** With one draw, SNIS returns $f(X_1)$, whose mean is $1/2$, not the target $3/4$.

**Slide.** States $a,b$; $\tilde p=(3,1)$, $Z=4$, $p=(3/4,1/4)$, $q=(1/2,1/2)$, $f=(1,0)$, $\mu=3/4$. Figure: one draw branches to $a$ (probability 1/2, weight 6, estimate $(6\cdot 1)/6=1$) and $b$ (probability 1/2, weight 2, estimate $(2\cdot 0)/2=0$); result box: mean 1/2, target 3/4. Exact, $n=1$: the weight cancels, so $\hat\mu_{\mathrm{SN}}=f(X_1)$. Generally biased, not always: constant $f$ or $q=p$ gives no bias.

Bias $=-1/4$. Both denominators are positive, so the bias is not caused by an undefined case.

**Details.** Exact enumeration, not a simulation. Ordinary IS with known $Z$ uses $w=(3/2,1/2)$, returns $3/2$ or $0$, mean $3/4$: unbiased. At $n=2$ the SNIS bias is $-1/8$ (our calculation). If $f\equiv c$, $\hat\mu_{\mathrm{SN}}=c$; if $q=p$, all $\tilde w_i=Z$ and SNIS is the plain mean.

**Sources.** E12: our calculation (direct enumeration); estimator from E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Numbers: `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S78 -->

<!-- BEGIN S122 -->
### 50. Normalization Does Not Guarantee Improvement [S122]

**Message.** Removing $Z$ trades one obstacle for a ratio-estimator problem: SNIS is not unbiased in general, and neither estimator always has smaller error.

**Slide.** Comparison of ordinary IS and SNIS:

- Unknown $Z$: IS blocked; SNIS cancels it.
- Consistent: IS if $q$ covers $fp$; SNIS if $q$ covers $p$.
- Unbiased at finite $n$: IS yes; SNIS not in general.
- Smaller error: no universal ranking either way.

Consistency in both columns also needs $E_p|f(X)|<\infty$. Self-normalization does not automatically reduce variance.

**Details.** Two-state example of slide 49 at $n=1$, exact MSE (our calculation):

- $f=(1,0)$, $\mu=3/4$: IS $9/16$, SNIS $5/16$ (SNIS better).
- $f=(0,1)$, $\mu=1/4$: IS $1/16$, SNIS $5/16$ (IS better).
- $f\equiv 1$: SNIS exact; IS $1/4$.

A second-order Taylor (delta-method) expansion of $A_n/B_n$ around $(Z\mu,Z)$ suggests $\mathrm{Bias}\approx -E_q[w^2(f-\mu)]/n$. This is a heuristic: a theorem needs extra moments (e.g. finite $E_q[w^2]$, $E_q[w^2f^2]$) and control of $B_n$ near zero, without which $E[\hat\mu_{\mathrm{SN}}]$ may not exist. In the toy the constant is $-3/16=-0.1875$, and exact $n\cdot$bias is:

- $n=1,2$: $-0.25$
- $n=5$: $-0.2177$; $n=10$: $-0.2023$
- $n=50$: $-0.1903$; $n=200$: $-0.1882$

**Sources.** E04: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.1, Theorem 9.1, pp. 4-6. E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. MSE values and bias table: `gen/p9c_snis_examples.py` (exact fractions, no randomness). The expansion is our derivation, checked numerically in this toy only.
<!-- END S122 -->

<!-- BEGIN S70 -->
### 51. One Draw Can Dominate the Weights [S70]

**Message.** When one weight dwarfs the rest, a batch of five draws behaves almost like one draw.

**Slide.** Weights $\tilde w=(.1,.2,.1,.1,9.5)$, total 10. Bar chart of shares $\bar w_i$ against sample index $i=1..5$: $.01,.02,.01,.01$ and a red bar of $.95$ for sample 5 (illustrative batch, not data). Sample 5 holds 95% of the normalized weight. Its contribution $\bar w_5 f(X_5)$ depends on $f$; no proof of infinite variance.

**Details.** Draw $i$ contributes $\bar w_i f(X_i)$: if $f(X_5)=0$ it contributes nothing, and opposite signs can cancel, so this is not "95% of the estimate". One uneven batch does not prove $E_q[w^2]=\infty$; a finite-second-moment proposal can produce one by chance, and a batch can look even while support is missing (slide 53).

**Sources.** E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12. E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S70 -->

<!-- BEGIN S79 -->
### 52. Effective Sample Size Summarizes Imbalance [S79]

**Message.** The effective sample size (ESS) turns weight imbalance into one number between $1$ and $n$.

**Slide.** For nonnegative weights with positive total, $\mathrm{ESS}=(\sum\tilde w_i)^2/\sum\tilde w_i^2=1/\sum\bar w_i^2$, with $1\le\mathrm{ESS}\le n$. Two bar panels: equal weights (each share 1/5, ESS $=5$) and the slide-51 batch (ESS $=100/90.32\approx 1.11$). Weight balance only: not $n$ independent draws, not an error bar for $f$.

Scaling all weights by one constant leaves ESS unchanged, so $Z$ does not matter.

**Details.** Bounds: with $\bar w_i\ge 0$, $\sum\bar w_i=1$, Cauchy-Schwarz gives $1\le n\sum\bar w_i^2$, so ESS $\le n$ (equality iff all shares $1/n$); $\bar w_i^2\le\bar w_i$ gives $\sum\bar w_i^2\le 1$, so ESS $\ge 1$ (equality iff one share is 1). Zero weights drop out, so ESS is at most the number of positive weights. Batch: $.0001+.0004+.0001+.0001+.9025=.9032$. Empirical vs population: $\mathrm{ESS}/n=(\frac1n\sum w_i)^2/(\frac1n\sum w_i^2)\to 1/E_q[w^2]$ by the strong law when $E_q[w^2]<\infty$; one batch can be far from $n/E_q[w^2]$. ESS ignores $f$, so it is not an integrand-specific error estimate.

**Sources.** E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12. E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S79 -->

<!-- BEGIN S81 -->
### 53. Healthy ESS Can Miss Missing Support [S81]

**Message.** If $q$ never visits part of the target, the weights can all be equal, so ESS reports $n$ while the estimate is wrong.

**Slide.** $p$ uniform on $\{1,2,3,4\}$, $q$ uniform on $\{1,2,3\}$. Figure: four states with outlined target bars of height 1/4 and grey proposal bars of height 1/3 on states 1-3, each labelled $w=3/4$; state 4 has a dashed red $q=0$ bar marked "never drawn"; $f=1\{x=4\}$ is marked above state 4. Result box: ESS $=n$, estimate 0, target 1/4. Equal weights, so $\bar w_i=1/n$: IS and SNIS both return 0. Failed assumption: $q(4)=0<p(4)$, so the theorem is not refuted.

**Details.** Every draw has $w=(1/4)/(1/3)=3/4$ and $f(X_i)=0$, so both estimates are 0 for every $n$, with probability one. $E_q[w]=3/4$: a quarter of target mass is missing, invisible to SNIS because shares are renormalized. IS needs $q>0$ where $fp\ne 0$ and SNIS needs $q>0$ where $p>0$; both fail at state 4. A region covered with tiny probability can also go unvisited in many batches; this example shows the missing-support case only, not every tail pathology.

**Sources.** E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness). E04: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.1, Theorem 9.1, pp. 4-6. E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12.
<!-- END S81 -->

<!-- BEGIN S82 -->
### 54. Choose the Estimator by What Is Known [S82]

**Message.** Choose the simplest estimator whose requirements you can actually meet.

**Slide.** Decision flow with three questions. Sample $p$ and evaluate $f$? Yes: ordinary MC, $\frac1n\sum f(X_i)$, $X_i\sim p$. No: evaluate normalized $p/q$ and sample $q$? Yes: IS, $\frac1n\sum w_i f(X_i)$, $X_i\sim q$. No: only $\tilde p/q$, with full support and positive total? Yes: SNIS, $\sum\tilde w_i f(X_i)/\sum\tilde w_j$. Available is not efficient: error still depends on $q$ and $f$.

**Details.** Bayesian posteriors are proportional to prior times likelihood, with an evidence integral as normalizer, so posterior expectations with a proposal $q$ fall in the SNIS branch, provided the posterior is proper ($0<Z<\infty$) and $q$ covers its support. Each branch only says what can be computed; for ordinary IS the second moment is $\int f^2p^2/q$. Weight diagnostics (slides 51-53) detect some failures but certify none.

**Sources.** E02: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 1-2 (posted PDF), Secs. 2.1-2.2, 2.7-2.8, https://artowen.su.domains/mc/Ch-intro.pdf (accessed 2026-11-17). E04: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.1, Theorem 9.1, pp. 4-6. E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Figure: our decision diagram, no data.
<!-- END S82 -->

<!-- BEGIN S83 -->
### 55. 05 · Differentiate Expectations [S83]

(placeholder, INT)
<!-- END S83 -->

<!-- BEGIN S84 -->
### 56. The Distribution Now Changes [S84]

(placeholder, P4)
<!-- END S84 -->

<!-- BEGIN S85 -->
### 57. Frozen Samples Hide the Derivative [S85]

(placeholder, P4)
<!-- END S85 -->

<!-- BEGIN S123 -->
### 58. A Gaussian Sample Is a Recipe [S123]

(placeholder, P4)
<!-- END S123 -->

<!-- BEGIN S124 -->
### 59. Differentiate Along the Sampling Path [S124]

(placeholder, P4)
<!-- END S124 -->

<!-- BEGIN S125 -->
### 60. Check the Gaussian Gradient [S125]

(placeholder, P4)
<!-- END S125 -->

<!-- BEGIN S126 -->
### 61. Discrete Draws Need Another Route [S126]

(placeholder, P4)
<!-- END S126 -->

<!-- BEGIN S86 -->
### 62. The Log-Derivative Identity [S86]

(placeholder, P4)
<!-- END S86 -->

<!-- BEGIN S87 -->
### 63. Reward Times Score Gives the Gradient [S87]

(placeholder, P4)
<!-- END S87 -->

<!-- BEGIN S88 -->
### 64. Proof: Expand the Expectation [S88]

(placeholder, P4)
<!-- END S88 -->

<!-- BEGIN S89 -->
### 65. Proof (continued): Differentiate the Finite Sum [S89]

(placeholder, P4)
<!-- END S89 -->

<!-- BEGIN S90 -->
### 66. Proof (continued): Read an Expectation [S90]

(placeholder, P4)
<!-- END S90 -->

<!-- BEGIN S92 -->
### 67. Average the Gradient Contributions [S92]

(placeholder, P4)
<!-- END S92 -->

<!-- BEGIN S93 -->
### 68. A Two-Action Policy [S93]

(placeholder, P4)
<!-- END S93 -->

<!-- BEGIN S94 -->
### 69. Both Routes Give the Same Derivative [S94]

(placeholder, P4)
<!-- END S94 -->

<!-- BEGIN S96a -->
### 70. The Score Has Mean Zero [S96a]

(placeholder, P4)
<!-- END S96a -->

<!-- BEGIN S96b -->
### 71. A Valid Baseline Preserves the Gradient [S96b]

(placeholder, P4)
<!-- END S96b -->

<!-- BEGIN S97 -->
### 72. This Baseline Removes the Toy's Variance [S97]

(placeholder, P4)
<!-- END S97 -->

<!-- BEGIN S127 -->
### 73. A Bad Baseline Adds Variance [S127]

(placeholder, P4)
<!-- END S127 -->

<!-- BEGIN S128 -->
### 74. Two Gradient Estimators, Different Requirements [S128]

(placeholder, P4)
<!-- END S128 -->

<!-- BEGIN S99 -->
### 75. 06 · Reuse Samples Responsibly [S99]

(placeholder, INT)
<!-- END S99 -->

<!-- BEGIN S100 -->
### 76. Old Samples, a New Target [S100]

(placeholder, P5)
<!-- END S100 -->

<!-- BEGIN S101 -->
### 77. Importance Weights Correct the Mismatch [S101]

(placeholder, P5)
<!-- END S101 -->

<!-- BEGIN S102 -->
### 78. Sequence Ratios Multiply [S102]

(placeholder, P5)
<!-- END S102 -->

<!-- BEGIN S103 -->
### 79. Compounding Mismatch Can Destroy Efficiency [S103]

(placeholder, P5)
<!-- END S103 -->

<!-- BEGIN S129 -->
### 80. Behavior and Reference Are Different Roles [S129]

(placeholder, P5)
<!-- END S129 -->

<!-- BEGIN S105 -->
### 81. KL Is Not a Variance Certificate [S105]

(placeholder, P5)
<!-- END S105 -->

<!-- BEGIN S106 -->
### 82. Reward Tuning Uses This Toolkit [S106]

(placeholder, P5)
<!-- END S106 -->

<!-- BEGIN S104 -->
### 83. A Surrogate Is Not a Hard Constraint [S104]

(placeholder, P5)
<!-- END S104 -->

<!-- BEGIN S109 -->
### 84. One Target, Different Estimators [S109]

(placeholder, INT)
<!-- END S109 -->

<!-- BEGIN S113 -->
### 85. Closer [S113]

(placeholder, INT)
<!-- END S113 -->
