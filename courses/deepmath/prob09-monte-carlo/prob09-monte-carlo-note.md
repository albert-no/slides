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

(placeholder, P3)
<!-- END S73 -->

<!-- BEGIN S74 -->
### 45. Compute Unnormalized Weights [S74]

(placeholder, P3)
<!-- END S74 -->

<!-- BEGIN S75 -->
### 46. Normalize Only a Positive Total [S75]

(placeholder, P3)
<!-- END S75 -->

<!-- BEGIN S76 -->
### 47. Two Averages Form One Ratio [S76]

(placeholder, P3)
<!-- END S76 -->

<!-- BEGIN S77 -->
### 48. The Ratio Converges to the Target [S77]

(placeholder, P3)
<!-- END S77 -->

<!-- BEGIN S78 -->
### 49. One Draw Exposes SNIS Bias [S78]

(placeholder, P3)
<!-- END S78 -->

<!-- BEGIN S122 -->
### 50. Normalization Does Not Guarantee Improvement [S122]

(placeholder, P3)
<!-- END S122 -->

<!-- BEGIN S70 -->
### 51. One Draw Can Dominate the Weights [S70]

(placeholder, P3)
<!-- END S70 -->

<!-- BEGIN S79 -->
### 52. Effective Sample Size Summarizes Imbalance [S79]

(placeholder, P3)
<!-- END S79 -->

<!-- BEGIN S81 -->
### 53. Healthy ESS Can Miss Missing Support [S81]

(placeholder, P3)
<!-- END S81 -->

<!-- BEGIN S82 -->
### 54. Choose the Estimator by What Is Known [S82]

(placeholder, P3)
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
