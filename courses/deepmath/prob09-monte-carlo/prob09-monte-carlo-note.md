# Deep Learning Math 9 - Monte Carlo and Importance Sampling (Lecture Note)

**About this file.** This is the text-only, screen-reader-friendly edition of the Lecture 9 companion note. It has one section per slide, in slide order, each headed by the slide number, title and slide ID in brackets; the HTML note has the same sections. Every figure and table is described in words or linearized into lists, and all mathematics is written in LaTeX. Nothing else is needed to read it.

Companion to `prob09-monte-carlo.html` (@@N@@ slides; no fixed duration). Audience: junior undergraduate AI majors who have seen expectation, variance, the law of large numbers and concentration in prob01-prob08. Each section opens with a one-sentence message, then explains the slide, then gives details and sources.

**Conventions.** $X$ is a random outcome; $f$ a fixed integration function with target $\mu=\mathbb E_p[f(X)]$; $R$ the reward in the policy examples and $r$ the learned reward in the RLHF example (the PPO slide uses $r$ for its ratio, as in the cited figure, and says so). $p$ is the target and $q$ the proposal; $w=p/q$ is the normalized density ratio, $\tilde w=\tilde p/q$ the unnormalized one, and $\bar w_i$ the normalized share of draw $i$. $\sigma_f$ is the population standard deviation and $s_Y$ the observed sample standard deviation. $\theta$ denotes model parameters; the behavior policy $\pi_b$ and the reference policy $\pi_{\text{ref}}$ are never interchanged. Exponential distributions use the rate parameter. $\ln$ is the natural logarithm and KL is measured in nats. Results proved in earlier lectures are cited, not re-proved.

## Opening

<!-- BEGIN S01 -->
### 1. Monte Carlo & Importance Sampling [S01]

**Message.** Monte Carlo turns an expectation into a computation; choosing or reweighting the sampler changes the error, not the target.

Lecture 9 of Deep Learning Math, for junior undergraduates in AI. It builds on the earlier lectures' expectation, variance, the law of large numbers and concentration, and asks one practical question throughout: when an average has no convenient closed form, how do we estimate it, and what can we honestly say about the error?
<!-- END S01 -->

<!-- BEGIN S02 -->
### 2. Contents [S02]

**Message.** Five decisions organize the lecture.

1. Estimate an Expectation: why machine learning needs averages (a population loss, a generator's pass rate), the ordinary Monte Carlo estimator, what it targets, and how far one run can land from it.
2. Change the Sampler: sample from a different distribution and correct with importance weights.
3. Control Proposal Risk: when a proposal helps and when it makes the error infinite.
4. Remove the Normalizer: self-normalized weights when the target is known only up to a constant, with possible finite-sample bias.
5. Reuse Samples in RL: the same ratio when reinforcement-learning data come from a different policy.

<!-- END S02 -->

## Part 1 - Estimate an Expectation

<!-- BEGIN S03 -->
### 3. Part 1: Estimate an Expectation [S03]

**Message.** First separate the number we want from the randomness of its estimate.

This part does not re-teach probability. It takes the expectation, the sample mean and its variance as known, and asks two questions: why machine learning keeps needing averages it cannot compute exactly, and what an estimate built from random draws promises: what it targets, how its error shrinks, how to report that error from the data, and why rare events need relative error.
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

**Integrability.** The target exists only if $\mathbb E_p|f(X)| \lt \infty$. The slide states this as an assumption; slide 7 makes it part of the formal estimator.

**Sources.**

E01: sample-mean facts from prob05 (pp. 39, 46, 93), course repository at commit b20ab73. E02: Owen, Ch. 1-2, Section 2.1.
<!-- END S06 -->

<!-- BEGIN S26 -->
### 6. Six Points Illustrate the Recipe [S26]

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

**No inference from this run.** A hand-picked sample does not support an error bar or a confidence statement. For genuinely IID uniform draws, $Y = 4\cdot\mathbf 1\{\text{hit}\}$ has $\mathbb E[Y] = \pi$ and $\mathrm{Var}(Y) = \pi(4 - \pi) \approx 2.6968$; slides 8 and 9 use these exact values.

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

**Notation.** $\sigma_f^2$ is the population variance of $f(X)$ under $p$, a fixed unknown number. The observed sample spread $s_Y$ appears only on slide 10.

**Sources.**

E01: sample-mean expectation, variance, LLN and CLT in prob05 (pp. 39, 46, 93), commit b20ab73. E02: Owen, Ch. 1-2, Sections 2.1-2.2 (first absolute moment for the mean and LLN, finite variance for RMSE and CLT).
<!-- END S16 -->

<!-- BEGIN S19 -->
### 8. Unbiased Does Not Mean Accurate [S19]

**Message.** The estimator is right on average at every $n$, yet a single run can be far off.

The top line is linearity of expectation: $\mathbb E[\hat\mu_n] = \frac1n\sum_i \mathbb E_p[f(X_i)] = \mu$, for every $n$, including $n = 1$.

The bar chart shows the exact distribution of $\hat\mu_6$ for six IID darts. The estimate is $4K/6$, where $K$, the number of hits, is Binomial$(6, \pi/4)$. The x-axis lists the seven possible values $0, \tfrac23, \tfrac43, 2, \tfrac83, \tfrac{10}3, 4$; bar heights are their probabilities. The large bars are $0.096$ at 2, $0.263$ at $\tfrac83$, $0.385$ at $\tfrac{10}3$ and $0.235$ at 4. A dashed red line marks the mean, $\pi$, which falls between $\tfrac83$ and $\tfrac{10}3$. No possible value equals $\pi$, and about 35% of runs miss it by at least 0.5. Unbiasedness is a statement about the centre of this distribution, not about any single run.

**Details.**

**Proof of unbiasedness.** Each $X_i \sim p$, so $\mathbb E[f(X_i)] = \mu$. Linearity gives

$$\mathbb E[\hat\mu_n] = \frac1n\sum_{i=1}^n \mathbb E[f(X_i)]$$

$$= \frac1n \cdot n\mu = \mu.$$

Independence is not used: identically distributed draws with $\mathbb E|f(X)| \lt \infty$ suffice for this identity. Independence matters for the variance on slide 9.

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

**What RMSE is not.** RMSE describes the spread over many repeated runs. It is not a bound on the error of the run in hand: a single run can miss by several RMSEs. Bounds that hold with stated probability come on slides 11 and 12.

**Sources.**

E02: Owen, Ch. 1-2, Sections 2.1-2.2 (variance $\sigma_f^2/n$ under finite variance). E01: prob05 sample-mean variance (p. 39), prob07 MSE decomposition (pp. 98, 102), commit b20ab73. E17: $\pi(4-\pi)$. Figure: inline SVG; RMSE values and coordinates printed by `gen/p9a_part01.py`.
<!-- END S22 -->

<!-- BEGIN S114 -->
### 10. Estimating the Error Bar [S114]

**Message.** The sample itself estimates the standard error, but only the typical spread, not this run's error.

The assumptions come first: IID evaluations, finite variance, and at least two draws. The flow then reads left to right. The observed data $Y_1, \dots, Y_n$ give the sample variance $s_Y^2 = \frac{1}{n-1}\sum_i (Y_i - \bar Y_n)^2$, and dividing its square root by $\sqrt n$ gives the estimated standard error $\widehat{\mathrm{SE}} = s_Y/\sqrt n$.

The next line separates the two quantities. The true standard error $\sigma_f/\sqrt n$ uses the unknown population SD $\sigma_f$; the observed $s_Y$ is our estimate of it. The highlight states the limit: $\widehat{\mathrm{SE}}$ estimates how far runs typically land from $\mu$, not the error $|\hat\mu_n - \mu|$ of the run in hand.

**Details.**

**Units.** $s_Y$ and $\widehat{\mathrm{SE}}$ have the units of $f$; $s_Y^2$ has squared units. Report the SE, not the variance, next to the estimate.

**Why $n - 1$.** With divisor $n - 1$, $\mathbb E[s_Y^2] = \sigma_f^2$ for IID data with finite variance. That needs $n \ge 2$.

**Example of the right data.** The formula applies to genuinely IID evaluations, for instance a fixed scoring rule applied to independently sampled model replies. It does not apply to the six hand-chosen darts on slide 6.

**Unseen tails.** $s_Y$ is always finite, because it is computed from finitely many numbers. It cannot show that $\sigma_f$ is finite. If rare draws carry very large values that the sample never hit, $s_Y$ will understate the spread.

**Sources.**

E02: Owen, Ch. 1-2, Sections 2.1-2.2 and 2.7-2.8 (estimated standard error, its assumptions). E01: prob05 sample-mean variance (p. 39), commit b20ab73.
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

E02: Owen, Ch. 1-2, Sections 2.7-2.8 (asymptotic intervals versus nonasymptotic bounds). E01: CLT in prob05 (p. 93), commit b20ab73. E17: Chebyshev sample size 539,354. Quantile and arithmetic printed by `gen/p9a_part01.py`.
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

Darts: $(b-a)^2 = 16$, $\ln 40 = 3.688879$, so $n \ge 295{,}110.36$, rounded up to $295{,}111$. At that $n$ the bound is at most $0.05$.

**Comparison.** Chebyshev with the known variance needed $539{,}354$ (slide 11), about $1.83$ times as many. Both are sufficient sample sizes from upper bounds, not minimal ones, and neither says how a particular run behaves. For scale, the RMSE at $n = 295{,}111$ is about $0.0030$.

**Edge case.** If $Y$ is constant, $a = b$ is not allowed, but no bound is needed: $\bar Y_n = \mu$ exactly.

**Fixed versus data-selected $f$.** The bound holds for one $f$ chosen before sampling. If $f$ is picked among many candidates using the same sample, the bound no longer applies to the picked one.

**Sources.**

E01: Hoeffding on $[0,1]$, prob06 (p. 18), commit b20ab73; prob06 states it on $[0,1]$, and the $[a,b]$ form is the rescaling above. E17: Hoeffding sample size 295,111. Arithmetic printed by `gen/p9a_part01.py`.
<!-- END S24 -->

<!-- BEGIN S116 -->
### 15. Rare Events Need Relative Error [S116]

**Message.** For a rare event the absolute error can be small while the error relative to the answer is large.

Let $Y$ indicate an event of probability $\rho$, so $Y \sim \mathrm{Bernoulli}(\rho)$ and $\mu = \rho$. For a rare event, one indicator has a small variance $\rho(1-\rho)$. The useful scale is relative: $\mathrm{RMSE}/|\mu| = \sqrt{(1-\rho)/(n\rho)}$, which is small only when $n$ is large compared with $1/\rho$. At fixed $n$ and $0 \lt \rho \le 1/2$, a rarer event has a lower absolute RMSE but a higher relative RMSE. Both are distribution-level RMSEs, not the error of one realized run.

The plot shows per-draw spreads against the event probability $\rho$, both axes logarithmic: $\rho$ from $10^{-6}$ to $0.5$ across, values from $10^{-3}$ to $10^3$ up, with a grey dashed reference line at 1. The dashed blue curve is the absolute SD $\sigma_f = \sqrt{\rho(1-\rho)}$; it falls as the event gets rarer. The solid red curve is the relative SD $\sigma_f/\rho$; it rises. At $\rho = 1/2$ the absolute SD is $1/2$ and the relative SD is $1$, so the curves do not meet on the displayed range. Dividing either by $\sqrt n$ gives the RMSE.

**Details.**

**Calculation.** $Y$ is Bernoulli$(\rho)$, so $\mathrm{Var}(Y) = \rho(1-\rho)$ and

$$\frac{\mathrm{RMSE}(\hat\mu_n)}{\rho} = \sqrt{\frac{\rho(1-\rho)}{n\rho^2}}$$

$$= \sqrt{\frac{1-\rho}{n\rho}}.$$

**Two errors, two scales.** An absolute RMSE of $\sqrt{\rho(1-\rho)/n}$ looks small next to 1, but $\mu = \rho$ may be smaller still. A run of $n$ draws sees no hit with probability $(1-\rho)^n$, and then reports $\hat\mu = 0$: a small absolute error and a 100% relative error. Relative error is defined only for $\mu \ne 0$.

Part 02 puts numbers on this with a concrete rare event and then changes the sampler so that the event is no longer rare.

**Sources.**

Our calculation (Bernoulli variance). Figure: inline SVG; curve points printed by `gen/p9a_part01.py`.
<!-- END S116 -->

## Part 2 - Change the Sampler

<!-- BEGIN S41 -->
### 16. Part 2: Change the Sampler [S41]

**Message.** Visit useful outcomes more often without changing the target.

Part 01 ended with a rare event whose relative error ordinary sampling cannot control at a reasonable sample size. The fix is to draw from a different distribution that visits the important region more often, and to correct each draw by a weight so that the average still targets the original expectation.
<!-- END S41 -->

<!-- BEGIN S43 -->
### 17. Most Draws Miss the Tail [S43]

**Message.** A rare-event probability with a known answer shows why plain sampling wastes almost every draw.

Target: $X \sim \mathrm{Exp}(1)$ (rate 1), density $p(x) = e^{-x}$ for $x \ge 0$. Integrand: $f(x) = \mathbf{1}\{x > 10\}$.

$$\mu = \Pr_p(X > 10) = \int_{10}^\infty e^{-x}\,dx = e^{-10} \approx 0.0000454.$$

About 1 draw in 22,026 lands in the event on average ($1/\mu = e^{10} \approx 22{,}026.47$). The answer is known, so it is a benchmark for estimators.

Figure: the exact density $e^{-x}$ on 0 to 14. Beyond $x = 10$ (shaded "event") it is invisible at this scale. An inset magnifies the tail from 10 to 14 with a vertical axis from 0 to $5 \times 10^{-5}$; the shaded patch under it is the tail up to $x = 14$. The tail continues beyond the displayed range; its whole area past 10 is $e^{-10}$.

Sources: our calculation (E11 setup); numbers `gen/p9b_calc.py`; figure `gen/p9b_figs.py` -> `fig/p9b-tail.svg`.
<!-- END S43 -->

<!-- BEGIN S44 -->
### 18. A Rare Event Needs Many Samples [S44]

**Message.** For 10% relative RMSE on $\mu = e^{-10}$, ordinary Monte Carlo needs about 2.2 million draws.

Each draw is Bernoulli($\mu$), variance $\mu(1-\mu)$. Relative RMSE of the mean of $n$ draws:

$$\frac{\mathrm{RMSE}}{\mu} = \sqrt{\frac{1-\mu}{n\mu}} \le 0.1 \iff n \ge 100\,\frac{1-\mu}{\mu} = 100\,(e^{10}-1) \approx 2{,}202{,}546.6.$$

The factor $(1-\mu)/\mu = e^{10} - 1 \approx 22{,}025$ is the relative variance of one draw.

Result: ordinary MC needs $n \ge 2{,}202{,}547$. This is a spread target, not a 95% guarantee and not a runtime.

Sources: E02 (Owen, Ch. 2, sections 2.1-2.2); E11; `gen/p9b_calc.py`.
<!-- END S44 -->

<!-- BEGIN S45 -->
### 19. Visit Useful Outcomes More Often [S45]

**Message.** Importance sampling draws from a different distribution $q$ that visits the event more often, while the target $\mu$ stays fixed.

A proposal $q$ is a new sampler that changes where draws land. Same $p$, $f$ and $\mu$: the target does not move. A plain average of $f$ under $q$ estimates $\mathbb{E}_q[f]$, not $\mu$, so each draw must be corrected.

Figure (schematic, hand-placed dots, not simulated draws): a number line from 0 to 14 with the event $x > 10$ shaded. Top row: draws from $p$, crowded near 0, none past 10. Bottom row: draws from $q$, spread out, several past 10.

Sources: E04 (Owen, Ch. 9, section 9.1); figure `gen/p9b_figs.py` -> `fig/p9b-visits.svg`.
<!-- END S45 -->

<!-- BEGIN S50 -->
### 20. Correct Each Visit's Weight [S50]

**Message.** The weight $w = p/q$ scales each draw by how much the proposal over- or under-visits its location.

$$w(x) = \frac{p(x)}{q(x)} \quad \text{where } q(x) > 0.$$

Target on top, proposal below. Where $q$ under-visits, $w > 1$; where it over-visits, $w < 1$. For continuous $x$ this is a ratio of densities, not a probability.

Figure (illustrative values chosen by hand): three outcomes a, b, c. Target $p$ = 0.50, 0.30, 0.20; proposal $q$ = 0.25, 0.25, 0.50; weights $w$ = 2, 1.2, 0.4.

Detail: $\mathbb{E}_q[w] = \Pr_p(q(X) > 0) \le 1$, with equality when $q > 0$ wherever $p > 0$. Notation: $w = p/q$ normalized ratio; $\tilde w$ unnormalized ratio; $\bar w$ normalized sampled share.

Sources: E04; figure `gen/p9b_figs.py` -> `fig/p9b-ratio.svg`.
<!-- END S50 -->

<!-- BEGIN S46 -->
### 21. Importance Sampling Preserves the Target [S46]

**Message.** Under integrability and a coverage condition, the weighted integrand has the same mean under $q$ as $f$ has under $p$.

**Theorem (importance-sampling identity).** Assume $\mathbb{E}_p|f(X)| < \infty$ and $q(x) > 0$ wherever $f(x)p(x) \ne 0$ (except a null set). With $w = p/q$ on $\{q > 0\}$:

$$\mathbb{E}_{X\sim p}[f(X)] = \mathbb{E}_{X\sim q}[f(X)\,w(X)].$$

Ordinary IS also needs $p/q$ computable at each draw, including normalizers. The identity equates means only; it says nothing about variance.

Sources: E04, Owen, *Monte Carlo theory, methods and examples*, Ch. 9, section 9.1, Theorem 9.1.
<!-- END S46 -->

<!-- BEGIN S47a -->
### 22. Proof: Cancel the Proposal [S47a]

**Message.** Writing the $q$-expectation as an integral cancels $q$, leaving $\int fp$ over the region where $q > 0$.

Draws from $q$ land in $\{q > 0\}$ with probability 1. By LOTUS and then cancelling $q$:

$$\mathbb{E}_q[f w] = \int_{\{q>0\}} f\,\frac{p}{q}\,q\,dx = \int_{\{q>0\}} f\,p\,dx.$$

The domain is still $\{q > 0\}$: the region $\{q = 0\}$ is not yet counted. Since $\mathbb{E}_p|f| < \infty$, every integral converges absolutely.

Sources: E04 (Theorem 9.1); LOTUS from E01 (prob01).
<!-- END S47a -->

<!-- BEGIN S47b -->
### 23. Proof (continued): Check the Missing Region [S47b]

**Message.** The unsampled region contributes nothing because $fp = 0$ there, so the two expectations agree.

So far: $\mathbb{E}_q[fw] = \int_{\{q>0\}} fp\,dx$. Split the line into $\{q > 0\}$ (sampled, computed) and $\{q = 0\}$ (never sampled):

$$\mathbb{E}_p[f] = \int_{\{q>0\}} fp\,dx + \int_{\{q=0\}} fp\,dx = \mathbb{E}_q[f w] + 0.$$

The second integral is 0 because the support condition makes $fp = 0$ on $\{q = 0\}$. QED. Only $fp$ must vanish there: $p > 0$ is allowed where $f = 0$.

Sources: E04 (Theorem 9.1).
<!-- END S47b -->

<!-- BEGIN S48 -->
### 24. Missing Support Cannot Be Repaired [S48]

**Message.** In this four-state example, missing the only contributing state makes every estimate zero instead of $1/4$.

- $p$ uniform on {1, 2, 3, 4}; $f = \mathbf{1}\{x = 4\}$; target $\mu = 1/4$.
- $q$ uniform on {1, 2, 3}, so $q(4) = 0$.
- Each draw: $w = (1/4)/(1/3) = 3/4$ and $f = 0$.

$$\hat\mu_{\mathrm{IS}} = 0 \ne 1/4 \quad \text{for every } n.$$

More draws cannot help: state 4 is never visited. Here $\mathbb{E}_q[w] = 3/4$. The coverage condition fails, so this is not a counterexample to the theorem.

Figure: four states. Target bars of height 1/4 on states 1-4; dashed proposal bars of height 1/3 on states 1-3 and none on state 4, which is shaded and labelled "f = 1 only here" and "q = 0".

Sources: E19 (our calculation); `gen/p9b_calc.py`; figure `gen/p9b_figs.py` -> `fig/p9b-support.svg`.
<!-- END S48 -->

<!-- BEGIN S49 -->
### 25. Average the Weighted Integrand [S49]

**Message.** The importance-sampling estimator draws from $q$, weights each value of $f$ by $p/q$, and divides by $n$.

Recipe (flow diagram): draw $X_i \sim q$ -> evaluate $f$, $p$, $q$ -> form $Y_i = f(X_i)\,w(X_i)$ -> average over $n$.

$$\hat\mu_{\mathrm{IS}} = \frac{1}{n}\sum_{i=1}^n f(X_i)\,w(X_i), \qquad X_1,\dots,X_n \overset{\text{iid}}{\sim} q.$$

Unbiased under the identity's conditions: $\mathbb{E}[\hat\mu_{\mathrm{IS}}] = \mathbb{E}_q[fw] = \mu$. Divide by $n$, not by the sum of weights. Extra cost over plain MC: evaluate $p$ and $q$.

Sources: E04.
<!-- END S49 -->

<!-- BEGIN S117 -->
### 26. A Practical Exponential Proposal [S117]

**Message.** A heavier-tailed exponential, $q = \mathrm{Exp}(0.1)$, is a simple valid proposal for the rare event.

Target $p = \mathrm{Exp}(1)$, same event $x > 10$. Proposal:

$$q(x) = 0.1\,e^{-0.1x}, \quad x \ge 0.$$

Both densities are positive on all $x \ge 0$, so support is covered. The normalizer 0.1 is known: no unknown $\mu$ inside $q$. Rate 0.1 is an illustrative choice, not optimal.

Figure: both exact densities on 0 to 14 with a log-scale vertical axis ($1$ down to $10^{-6}$). The target falls in a straight line to about $10^{-6}$; the proposal stays between $10^{-1}$ and $10^{-2}$, far above the target in the shaded event region.

Sources: E11; figure `gen/p9b_figs.py` -> `fig/p9b-proposal.svg`.
<!-- END S117 -->

<!-- BEGIN S118 -->
### 27. More Tail Visits, Corrected Weights [S118]

**Message.** The proposal hits the event about 37% of the time, and each hit carries a weight that corrects for the oversampling.

$$\Pr_q(X > 10) = e^{-1} \approx 0.37, \qquad w(x) = \frac{e^{-x}}{0.1\,e^{-0.1x}} = 10\,e^{-0.9x}.$$

About 8,100 times more tail hits than under $p$ ($e^9 \approx 8{,}103$). The contribution $fw$ is 0 below 10; above, it is $10e^{-0.9x}$ and varies with $x$. More hits alone do not prove lower variance.

Figure: log-scale plot of $fw$ for $x$ from 8 to 20. Zero up to 10; $1.23 \times 10^{-3}$ just above $x = 10$ (about $27\mu$), falling to about $1.5 \times 10^{-7}$ at 20. A dashed line marks $\mu = e^{-10}$; the curve crosses it near $x = 13.7$.

Sources: E11; `gen/p9b_calc.py`; figure `gen/p9b_figs.py` -> `fig/p9b-contrib.svg`.
<!-- END S118 -->

<!-- BEGIN S119 -->
### 28. Compute the Proposal's Error [S119]

**Message.** For the exponential proposal the second moment has a closed form; at rate 0.1 the relative variance per draw is about 13.3.

One draw's second moment for $q = \mathrm{Exp}(\lambda)$, finite only for $0 < \lambda < 2$:

$$\mathbb{E}_q[(fw)^2] = \int_{10}^\infty \frac{p(x)^2}{q(x)}\,dx = \frac{1}{\lambda}\int_{10}^\infty e^{-(2-\lambda)x}\,dx = \frac{e^{-10(2-\lambda)}}{\lambda(2-\lambda)}.$$

$$\frac{\mathbb{E}_q[(fw)^2]}{\mu^2} = \frac{e^{10\lambda}}{\lambda(2-\lambda)}; \quad \text{at } \lambda = 0.1: \ \frac{e}{0.19} \approx 14.3067.$$

Relative variance per draw: $14.3067 - 1 \approx 13.3067$ (ordinary MC: 22,025).

Sources: E11 (our calculation using E04's second-moment identity); `gen/p9b_calc.py`.
<!-- END S119 -->

<!-- BEGIN S120 -->
### 29. Same Target, Less Relative Error [S120]

**Message.** At the same accuracy target, the exponential proposal needs 1,331 draws against 2,202,547.

Draws needed for relative RMSE at most 0.1, same $\mu = e^{-10}$: $n = \lceil \text{relative variance}/0.01 \rceil$.

- Ordinary MC: $22{,}025.5 \to n = 2{,}202{,}547$.
- IS with $q = \mathrm{Exp}(0.1)$: $13.31 \to n = 1{,}331$.

Figure: two horizontal bars on a log scale from 1 to $10^7$; the ordinary-MC bar reaches about $2.2 \times 10^6$, the IS bar about $1.3 \times 10^3$. Shorter bar = fewer draws.

Exact-formula calculation, not measured runtime; neither is a 95% guarantee. The ratio (about 1,655) is not presented as a speedup.

Sources: E11; `gen/p9b_calc.py`; figure `gen/p9b_figs.py` -> `fig/p9b-budget.svg`.
<!-- END S120 -->

<!-- BEGIN S54 -->
### 30. Coverage and Variance Are Different [S54]

**Message.** A proposal must pass two separate checks: coverage for correctness, a small second moment for precision.

1. Validity: $q > 0$ wherever $fp \ne 0$, with $\mathbb{E}_p|f(X)|<\infty$. Gives: unbiased, same $\mu$. $\mathrm{Exp}(0.1)$: positive on all $x \ge 0$ (passes).
2. Precision: $\int f^2p^2/q$ finite and small. Gives: small RMSE per draw. $\mathrm{Exp}(0.1)$: relative variance 13.3 vs 22,025 (passes).

Valid is not the same as useful: a covering $q$ can have larger, even infinite, variance.

**Details.** Missing coverage can bias the estimator, as in the four-state example. An infinite second moment leaves a covering, integrable estimator unbiased and consistent but with no finite RMSE; a large but finite second moment gives a large but finite RMSE.

Sources: E04; E11.
<!-- END S54 -->

## Part 3 - Control Proposal Risk

<!-- BEGIN S55 -->
### 31. Part 3: Control Proposal Risk [S55]

**Message.** A correct mean is not enough for reliable Monte Carlo.

Part 02 showed a practical proposal that keeps the target and cuts the relative error. This part asks why it works and how another proposal can fail: the second moment of the weighted integrand decides the error, the best proposal follows the integrand, and a proposal with lighter tails than the target can leave the estimate unbiased but with infinite variance.
<!-- END S55 -->

<!-- BEGIN S56 -->
### 32. The Second Moment Decides [S56]

**Message.** The variance of importance sampling is set by one integral, $\int f^2p^2/q$, which the choice of $q$ controls.

$\hat\mu_{\mathrm{IS}}$ is a sample mean of $Y = fw$ under $q$:

$$\mathrm{Var}(\hat\mu_{\mathrm{IS}}) = \frac{1}{n}\left(\int \frac{f(x)^2 p(x)^2}{q(x)}\,dx - \mu^2\right).$$

The integral equals $\mathbb{E}_q[(fw)^2]$ and is what $q$ changes; $\mu^2$ is fixed. Valid when the integral is finite. An infinite integral means infinite variance and no finite RMSE. The criterion contains $f^2$: weights alone do not decide.

Sources: E04; E02.
<!-- END S56 -->

<!-- BEGIN S57 -->
### 33. Follow the Weighted Integrand [S57]

**Message.** To keep $\int f^2p^2/q$ small, place proposal mass where $|f|p$ is large, not where $p$ is large.

$f^2p^2/q$ is large where $|f|p$ is big and $q$ small. So aim $q$ at $|f|p$, not at $p$. Absolute value: a density is never negative. Intuition here, not yet an optimality proof.

Figure (illustration, $p = \mathcal{N}(0,1)$, $f(x) = x$, exact curves): grey $p$ peaked at 0; dashed red signed product $fp$, negative on the left; shaded blue $|f|p$ with two lobes near $x = \pm 1$ and zero at $x = 0$, where $p$ peaks.

Sources: E04; figure `gen/p9b_figs.py` -> `fig/p9b-weighted.svg`.
<!-- END S57 -->

<!-- BEGIN S59 -->
### 34. The Optimal Proposal [S59]

**Message.** The proposal proportional to $|f|p$ minimizes the variance, and the minimum is $c^2 - \mu^2$ with $c = \mathbb{E}_p|f|$.

**Theorem (optimal proposal).** Let $c = \mathbb{E}_p|f(X)| \in (0, \infty)$. Among densities $q$ with $q > 0$ wherever $fp \ne 0$, the per-draw variance $\mathrm{Var}_q(fw)$ is minimized by

$$q^*(x) = \frac{|f(x)|\,p(x)}{c}, \qquad \min_q \mathrm{Var}_q(fw) = c^2 - \mu^2.$$

With $n$ draws: $\mathrm{Var}(\hat\mu_{\mathrm{IS}}) = (c^2 - \mu^2)/n$, for $f$ of any sign. A formula, not yet a usable sampler: $q^*$ contains $c$.

Sources: E04, Owen, Ch. 9, section 9.1, optimal-density discussion, pp. 4-6.
<!-- END S59 -->

<!-- BEGIN S60 -->
### 35. Proof: A Common Lower Bound [S60]

**Message.** Jensen's inequality gives every admissible proposal the same floor, $\mathbb{E}_q[(fw)^2] \ge c^2$.

Recall: $\mathbb{E}[Z^2] \ge (\mathbb{E}Z)^2$, with equality iff $Z$ is a.s. constant. Take $Z = |f(X)|\,w(X)$ with $X \sim q$:

$$\mathbb{E}_q[(fw)^2] = \mathbb{E}_q[Z^2] \ge (\mathbb{E}_q Z)^2 = (\mathbb{E}_p|f(X)|)^2 = c^2,$$

using the identity applied to $|f|$. $|f|p \ne 0$ exactly where $fp \ne 0$, so coverage is the same. Same floor for every admissible $q$; equality iff $|f|w$ is constant $q$-a.s.

Sources: E04; Jensen from E01 (prob01).
<!-- END S60 -->

<!-- BEGIN S61 -->
### 36. Proof (continued): Attain the Bound [S61]

**Message.** Under $q^*$ the quantity $|f|w^*$ equals $c$ at every draw, so the floor is reached.

Floor: $\mathbb{E}_q[(fw)^2] \ge c^2$ for every admissible $q$. Plug in $q^* = |f|p/c$:

$$|f(x)|\,w^*(x) = \frac{|f(x)|\,p(x)}{q^*(x)} = c \quad \text{wherever } q^*(x) > 0,$$

so $\mathbb{E}_{q^*}[(fw^*)^2] = c^2$ and $\mathrm{Var}_{q^*}(fw^*) = c^2 - \mu^2$. QED.

The sign of $f$ may flip; the magnitude stays $c$. $q^*$ is a density ($\int |f|p/c = 1$) and is zero only where $fp = 0$.

Sources: E04.
<!-- END S61 -->

<!-- BEGIN S63 -->
### 37. One-Sign Integrands Permit Zero Variance [S63]

**Message.** For the nonnegative rare-event indicator, the optimal proposal gives every draw the exact answer.

Indicator $f \ge 0$, so $c = \mu = e^{-10}$:

$$q^*(x) = \frac{\mathbf{1}\{x > 10\}\,e^{-x}}{e^{-10}} = \mathbf{1}\{x > 10\}\,e^{-(x-10)}.$$

Each draw: $fw^* = e^{-10}$ exactly, so the variance is 0. This is an oracle benchmark built from the known answer. Sign-changing $f$: usually $c^2 - \mu^2 > 0$.

Figure: $q^*$ is zero below 10, jumps to 1 at $x = 10$ and decays exponentially; a strip below shows schematic draws, all past 10, each with $fw^* = e^{-10}$.

Sources: E04; our calculation; figure `gen/p9b_figs.py` -> `fig/p9b-oracle.svg`.
<!-- END S63 -->

<!-- BEGIN S64 -->
### 38. The Oracle Needs a Normalizer [S64]

**Message.** Evaluating the optimal weight requires $c$, which is $|\mu|$ for a one-sign integrand and $\mu$ for this nonnegative indicator.

Dependency loop (diagram): $c = \mu$ (unknown target) -> $q^* = fp/c$ -> weight $w^* = p/q^* = c$ on $x > 10$ -> estimate $\mu$. Line below: circular, the weight needs $c$, and here $c = \mu$ is the answer.

Two different capabilities: sample $q^*$, or evaluate its normalized weight. Here the tail is known: $X = 10 + \mathrm{Exp}(1)$ samples $q^*$, and $c = e^{-10}$ is computable. In harder problems $c$ is unknown, so $w^*$ cannot be evaluated.

Sources: E04, Owen, Ch. 9, section 9.1.
<!-- END S64 -->

<!-- BEGIN S66 -->
### 39. Light Tails Can Destroy Variance [S66]

**Message.** A proposal with a lighter tail than the target produces weights that grow without bound.

New integrand $f(x) = x$; $p = \mathrm{Exp}(1)$, $\mu = 1$. Proposal $q = \mathrm{Exp}(2)$, $q(x) = 2e^{-2x}$:

$$w(x) = \frac{e^{-x}}{2e^{-2x}} = \frac{e^x}{2}.$$

Both positive on $x \ge 0$: the identity is valid. Growing weights are a warning, not yet a proof.

Figure: exact densities on 0 to 4. $q$ starts at 2 and falls fast; $p$ starts at 1. They cross at $x = \ln 2$; beyond it $q < p$, so the tail is under-visited (shaded).

Sources: E18; figure `gen/p9b_figs.py` -> `fig/p9b-light.svg`.
<!-- END S66 -->

<!-- BEGIN S68 -->
### 40. A Finite Mean, an Infinite Second Moment [S68]

**Message.** With $q = \mathrm{Exp}(2)$ the estimator is unbiased, but its variance is infinite, so its RMSE is infinite at every $n$.

$f(x) = x$, $p = \mathrm{Exp}(1)$, $q = \mathrm{Exp}(2)$, $w = e^x/2$:

$$\mathbb{E}_q[Xw] = \int_0^\infty x\cdot\tfrac{e^x}{2}\cdot 2e^{-2x}\,dx = \int_0^\infty x e^{-x}\,dx = 1,$$

$$\mathbb{E}_q[(Xw)^2] = \int_0^\infty x^2\cdot\tfrac{e^{2x}}{4}\cdot 2e^{-2x}\,dx = \int_0^\infty \tfrac{x^2}{2}\,dx = \infty.$$

For the mean, the cancellation leaves $e^{-x}$; for the square, it leaves no decay. Unbiased, yet the variance is infinite: RMSE is infinite at every $n$. (Bare weights also have $\mathbb{E}_q[w^2] = \infty$, but the criterion is the one with $f^2$.)

Sources: E18 (direct integration).
<!-- END S68 -->

<!-- BEGIN S121 -->
### 41. Consistency Is Not an Error Bar [S121]

**Message.** This integrable example converges, but its infinite second moment rules out finite RMSE and the usual finite-variance CLT error bar.

Same estimator: $Y_i = X_i\,w(X_i)$ iid under $q = \mathrm{Exp}(2)$.

- $\mathbb{E}_q|Y| < \infty$ (holds) -> LLN: $\hat\mu_{\mathrm{IS}} \to \mu$ (holds).
- $\mathbb{E}_q[Y^2] < \infty$ (fails) -> variance, RMSE, CLT error bars (unavailable).

It converges, but the usual finite-variance error tools do not apply. A calm batch, or a small sample variance, does not prove a finite second moment.

Sources: E02, Owen, Ch. 2, sections 2.1-2.2; E18.
<!-- END S121 -->

<!-- BEGIN S69 -->
### 42. Check the Integrand, Not Just Weights [S69]

**Message.** A heavier proposal, $\mathrm{Exp}(1/2)$, gives a finite variance; the deciding integral includes $f^2$, not just the weights.

Same $f(x) = x$, $p = \mathrm{Exp}(1)$; heavier proposal $q = \mathrm{Exp}(1/2)$:

$$\mathbb{E}_q[(fw)^2] = \int_0^\infty x^2\,\frac{e^{-2x}}{\tfrac12 e^{-x/2}}\,dx = 2\int_0^\infty x^2 e^{-3x/2}\,dx = \frac{32}{27}.$$

Variance per draw $32/27 - 1 = 5/27$, vs 1 for ordinary MC. The criterion is $\int f^2p^2/q < \infty$; the bare $\mathbb{E}_q[w^2] = 4/3$ is a different number. Heavier tails are a heuristic, not a guarantee for every $f$.

Sources: E18 (checked with $\int_0^\infty x^2 e^{-ax}\,dx = 2/a^3$); `gen/p9b_calc.py`.
<!-- END S69 -->

## Part 4 - Remove the Normalizer

<!-- BEGIN S72 -->
### 43. Part 4: Remove the Normalizer [S72]

**Message.** An unknown normalizing constant changes the estimator and its guarantees.

Ordinary importance sampling needs the normalized ratio $p/q$. Often the target is known only up to a constant, $p = \tilde p / Z$ with $Z$ unknown. Dividing by the total weight removes $Z$, but the result is a ratio of two averages: consistent, yet generally biased at finite sample sizes, and its weight diagnostics have blind spots.
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

**Slide.** Conditions line, then a figure: the same draws feed two averages, $A_n=\frac1n\sum\tilde w_i f(X_i)$ with mean $\int\tilde p f=Z\mu$, and $B_n=\frac1n\sum\tilde w_i$ with mean $\int\tilde p=Z$; the two are labelled "generally dependent" and combine into $A_n/B_n=\hat\mu_{\mathrm{SN}}$. Each average is unbiased; the ratio is not: $E[A_n/B_n]\ne E[A_n]/E[B_n]$ in general.

Under full support, $E_q[\tilde w f]=\int\tilde p f\,dx=Z\mu$ and $E_q[\tilde w]=\int\tilde p\,dx=Z$, so the ratio of means is $\mu$.

**Details.** Full support makes the integrals over $\{q>0\}$ include all target mass. Integrability: $E_q|\tilde w f|=Z\,E_p|f|<\infty$. Expectation does not commute with taking a ratio: division is nonlinear and $A_n$, $B_n$, built from the same draws, are generally dependent, so the mean of the ratio differs from the ratio of means in general; slide 49 gives an exact case.

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
- Consistent: IS if $q$ covers $fp$; SNIS if $q$ covers all of $p$.
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

**Message.** One draw holds 95% of the normalized weight; its contribution still depends on $f$.

**Slide.** Weights $\tilde w=(.1,.2,.1,.1,9.5)$, total 10. Bar chart of shares $\bar w_i$ against sample index $i=1..5$: $.01,.02,.01,.01$ and a red bar of $.95$ for sample 5 (illustrative batch, not data). Sample 5 holds 95% of the normalized weight. Its contribution $\bar w_5 f(X_5)$ depends on $f$; no proof of infinite variance.

**Details.** Draw $i$ contributes $\bar w_i f(X_i)$: if $f(X_5)=0$ it contributes nothing, and opposite signs can cancel, so this is not "95% of the estimate". One uneven batch does not prove $E_q[w^2]=\infty$; a finite-second-moment proposal can produce one by chance, and a batch can look even while support is missing (slide 53).

**Sources.** E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12. E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S70 -->

<!-- BEGIN S79 -->
### 52. Effective Sample Size Summarizes Imbalance [S79]

**Message.** The effective sample size (ESS) turns weight imbalance into one number between $1$ and $n$.

**Slide.** For nonnegative weights with positive total, $\mathrm{ESS}=(\sum\tilde w_i)^2/\sum\tilde w_i^2=1/\sum\bar w_i^2$, with $1\le\mathrm{ESS}\le n$. Two bar panels: equal weights (each share 1/5, ESS $=5$) and the slide-51 batch (ESS $=100/90.32\approx 1.11$). Weight balance only: not $n$ independent draws, not an error bar for $f$.

Scaling all weights by one constant leaves ESS unchanged, so $Z$ does not matter.

**Details.** Bounds: with $\bar w_i\ge 0$, $\sum\bar w_i=1$, Cauchy-Schwarz gives $1\le n\sum\bar w_i^2$, so ESS $\le n$ (equality iff all shares $1/n$); $\bar w_i^2\le\bar w_i$ gives $\sum\bar w_i^2\le 1$, so ESS $\ge 1$ (equality iff one share is 1). Zero weights drop out, so ESS is at most the number of positive weights. Batch: $.0001+.0004+.0001+.0001+.9025=.9032$. Empirical vs population: $\mathrm{ESS}/n=(\frac1n\sum w_i)^2/(\frac1n\sum w_i^2)\to (E_q[w])^2/E_q[w^2]$ by the strong law when $E_q[w^2]<\infty$. This equals $1/E_q[w^2]$ only when $w=p/q$ with $q$ covering all of $p$, so that $E_q[w]=1$; in the four-state example ($q$ misses state 4), $w=3/4$ on the support of $q$, $E_q[w]=3/4$, $E_q[w^2]=9/16$, and the limit is 1, not 16/9. One batch can be far from the population value. ESS ignores $f$, so it is not an integrand-specific error estimate.

**Sources.** E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12. E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness).
<!-- END S79 -->

<!-- BEGIN S81 -->
### 53. Healthy ESS Can Miss Missing Support [S81]

**Message.** If $q$ never visits part of the target, the weights can all be equal, so ESS reports $n$ while the estimate is wrong.

**Slide.** $p$ uniform on $\{1,2,3,4\}$, $q$ uniform on $\{1,2,3\}$. Figure: four states with outlined target bars of height 1/4 and grey proposal bars of height 1/3 on states 1-3, each labelled $w=3/4$; state 4 has a dashed red $q=0$ bar marked "never drawn"; $f=1\{x=4\}$ is marked above state 4. Result box: ESS $=n$, estimate 0, target 1/4. Equal weights, so $\bar w_i=1/n$: IS and SNIS both return 0. Failed assumption: $q(4)=0\lt p(4)$, so the theorem is not refuted.

**Details.** Every draw has $w=(1/4)/(1/3)=3/4$ and $f(X_i)=0$, so both estimates are 0 for every $n$, with probability one. $E_q[w]=3/4$: a quarter of target mass is missing, invisible to SNIS because shares are renormalized. IS needs $q>0$ where $fp\ne 0$ and SNIS needs $q>0$ where $p>0$; both fail at state 4. A region covered with tiny probability can also go unvisited in many batches; this example shows the missing-support case only, not every tail pathology.

**Sources.** E19: our calculation, `gen/p9c_snis_examples.py` (exact fractions, no randomness). E04: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.1, Theorem 9.1, pp. 4-6. E06: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.3, eqs (9.13)-(9.14), pp. 11-12.
<!-- END S81 -->

<!-- BEGIN S82 -->
### 54. What You Can Compute Decides What Is Available [S82]

**Message.** What you can compute decides which estimators are available; it does not decide which is best.

**Slide.** Lead line: each row lists sufficient inputs; several rows can hold at once. A capability map with three independent rows, not a decision tree. Can sample $p$ and evaluate $f$: ordinary MC, $\frac1n\sum f(X_i)$, $X_i\sim p$. Can sample $q$ and evaluate normalized $p/q$, with $q>0$ wherever $fp\neq 0$: IS, $\frac1n\sum w_i f(X_i)$, $X_i\sim q$. Can sample $q$ and evaluate $\tilde p/q$, with $q>0$ wherever $p>0$ and a positive total: SNIS, $\sum\tilde w_i f(X_i)/\sum\tilde w_j$. Closing line: these requirements tell us which estimators are available, not which is best.

A well-chosen $q$ can beat ordinary Monte Carlo even when sampling $p$ is possible, as the rare-event example showed.

**Details.** Bayesian posteriors are proportional to prior times likelihood, with an evidence integral as normalizer, so posterior expectations with a proposal $q$ fall in the SNIS row, provided the posterior is proper ($0<Z<\infty$) and $q$ covers its support. Each row only says what can be computed; for ordinary IS the second moment is $\int f^2p^2/q$. Weight diagnostics (slides 51-53) detect some failures but certify none.

**Sources.** E02: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 1-2 (posted PDF), Secs. 2.1-2.2, 2.7-2.8, https://artowen.su.domains/mc/Ch-intro.pdf (accessed 2026-11-17). E04: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.1, Theorem 9.1, pp. 4-6. E05: A. B. Owen, *Monte Carlo theory, methods and examples*, Ch. 9 (posted PDF), https://artowen.su.domains/mc/Ch-var-is.pdf, Sec. 9.2, Theorem 9.2, eqs (9.6)-(9.10), pp. 8-10. Figure: our capability map, no data.
<!-- END S82 -->

## Part 5 - Reuse Samples in RL

<!-- BEGIN S99 -->
### 75. Part 5: Reuse Samples in RL [S99]

**Message.** Reusing data introduces a second distribution, not a new target.

In reinforcement learning (RL), samples collected under one policy are reused to evaluate another. The correction is the importance ratio of Part 02, now a product over the steps of a sequence. This part applies that toolkit to a scoped, historical RLHF example; it is not a survey of reinforcement-learning methods.
<!-- END S99 -->

<!-- BEGIN S100 -->
### 76. Old Samples, a New Target [S100]

**Message.** Logged responses were drawn from a behavior policy $\pi_b$, while the quantity we want is an expectation under the current policy $\pi_\theta$.

Figure (schematic): three boxes. On the left, stacked: the upper box, amber, "behavior $\pi_b(\cdot\mid c)$", the policy that generated the logged responses; the lower box, blue, "current $\pi_\theta(\cdot\mid c)$", the policy being trained. On the right, a tall box: the estimate $\mathbb{E}_{X\sim\pi_\theta(\cdot\mid c)}[R(c,X)]$. A solid arrow labelled "samples $x_1,\dots,x_n$" runs from the behavior box to the estimate; a dashed arrow labelled "target only / no fresh samples" runs from the current box to the estimate.

Fix a prompt $c$ and a reward $R(c,x)$ that does not change during the update. The samples come from $\pi_b$ but the expectation is under $\pi_\theta$: the importance-sampling setting from earlier in the lecture.

Details. The behavior policy is a data-collection distribution, not automatically the reference policy a regularizer compares against (slide [[S129]]). Later slides drop $c$ by convention; every policy is then conditional on the same fixed prompt. The example is response-level, like a bandit; how a policy change alters which states or prompts are visited in a multi-step environment is outside it.

Sources. Owen, Monte Carlo theory, methods and examples, Ch. 9, Sec. 9.1 (E04); Ouyang et al., NeurIPS 2022 (E10). Diagram: original schematic.
<!-- END S100 -->

<!-- BEGIN S101 -->
### 77. Importance Weights Correct the Mismatch [S101]

**Message.** Weighting each logged response by $w=\pi_\theta/\pi_b$ recovers the current-policy expectation, provided $\pi_b$ covers every response $\pi_\theta$ can produce.

The generic identity $\mathbb{E}_p[f]=\mathbb{E}_q[(p/q)f]$ is relabelled with target $p=\pi_\theta$ and proposal $q=\pi_b$:

$$\mathbb{E}_{\pi_\theta}[R(c,X)]=\mathbb{E}_{\pi_b}\big[w(X)\,R(c,X)\big],\qquad w(x)=\frac{\pi_\theta(x\mid c)}{\pi_b(x\mid c)}.$$

The current policy is on top, the data-generating policy underneath, both evaluated at the logged response. Coverage: $\pi_b(x\mid c)>0$ wherever $\pi_\theta(x\mid c)>0$. Estimator: $\frac1n\sum_i w(x_i)R(c,x_i)$.

Details. The behavior policy $\pi_b$, the reward $R$ and the current parameters $\theta$ are held fixed while the estimate is formed. Unbiasedness needs integrability of $wR$; a useful error bar needs finite variance, which coverage alone does not give. Clipped or self-normalized versions are different estimators with separate bias and variance questions.

Sources. Owen Ch. 9, Sec. 9.1, Theorem 9.1 (E04).
<!-- END S101 -->

<!-- BEGIN S102 -->
### 78. Sequence Ratios Multiply [S102]

**Message.** For an autoregressive policy the sequence weight is a product of per-token conditional ratios, each with the same history in numerator and denominator.

Figure (schematic): a row of chips $c, x_1, x_2, x_3, \dots, x_T$ with $x_3$ highlighted; under each token chip is its ratio $w_t$. An amber bracket spans $c, x_1, x_2$ and is labelled "history of $x_3$".

$$w(x)=\prod_{t=1}^{T}w_t,\qquad w_t=\frac{\pi_\theta(x_t\mid c,x_{<t})}{\pi_b(x_t\mid c,x_{<t})}.$$

This is the chain rule, exact, with no independence assumed: each factor depends on its own prefix.

Details. The slide fixes the length $T$. With variable lengths the end-of-sequence (EOS) token is part of the modeled sequence, so its ratio is one more factor; dropping it silently changes the weight. The score of a sequence is a sum of token scores, $s_\theta(x)=\sum_t\nabla_\theta\ln\pi_\theta(x_t\mid c,x_{<t})$, while the weight is a product of token ratios.

Sources. Chain rule: course prerequisites (E01); ratio orientation: Owen Ch. 9, Sec. 9.1 (E04). Diagram: original schematic.
<!-- END S102 -->

<!-- BEGIN S103 -->
### 79. Compounding Mismatch Can Destroy Efficiency [S103]

**Message.** In an explicit independent-token toy, a per-token weight second moment of only 1.1 compounds to $1.1^T$, about 13,781 at $T=100$.

Left column: weight factors $w_t$ independent under $\pi_b$ (here because both policies factor position by position); each $\mathbb{E}[w_t]=1$; each $\mathbb{E}[w_t^2]=1.1$; hence $\mathbb{E}[w^2]=1.1^T$. "Exact formula, not a measured model."

Figure: $\mathbb{E}_{\pi_b}[w^2]$ on a log vertical axis (ticks 1, 10, $10^2$, $10^3$, $10^4$) against length $T$ from 0 to 100. The curve is a straight line from 1 at $T=0$; red points mark $T=50$ ($\approx117$) and $T=100$ ($\approx13{,}781$).

Details. Each behavior token is binary with $\pi_b=(1/2,1/2)$; the target token has $\pi_\theta=((1+\sqrt{0.1})/2,(1-\sqrt{0.1})/2)$, independently across positions. Then $w_t\in\{1\pm\sqrt{0.1}\}$ with probability 1/2 each, so $\mathbb{E}[w_t]=1$ and $\mathbb{E}[w_t^2]=1.1$. Independence gives $\mathbb{E}[(\prod_t w_t)^2]=1.1^T$: 117.39 at $T=50$, 13,780.61 at $T=100$. The population proxy $n/\mathbb{E}[w^2]$ at $n=10^6$, $T=100$ is about 72.6; it is not an observed effective sample size, not a count of independent samples and not an error guarantee. Real autoregressive token ratios depend on the shared prefix, so the expectation of the product need not factor; no universal exponential law for language models follows.

Sources. Our calculation (E20); Owen Ch. 9, Sec. 9.3, eqs. (9.13)-(9.14) (E06). Figure and numbers: gen/p9e_compounding.py (closed form), output fig/p9e-compounding.svg.
<!-- END S103 -->

<!-- BEGIN S129 -->
### 80. Behavior and Reference Are Different Roles [S129]

**Message.** Sampling correction compares $\pi_\theta$ with the behavior policy $\pi_b$; regularization compares $\pi_\theta$ with the reference policy $\pi_{\text{ref}}$.

Figure (schematic): three boxes. Amber "behavior $\pi_b$, generated the data"; blue "current $\pi_\theta$, being trained"; green "reference $\pi_{\text{ref}}$, fixed anchor". An amber bracket joins behavior and current: "correction: $w=\pi_\theta/\pi_b$, reweights samples from $\pi_b$". A green bracket joins current and reference: "penalty: $D_{\mathrm{KL}}(\pi_\theta\|\pi_{\text{ref}})$, keeps $\pi_\theta$ near $\pi_{\text{ref}}$".

The policies may coincide at the start; their jobs and later values differ. Being near $\pi_{\text{ref}}$ says nothing about the weights against $\pi_b$.

Details. The reference stays fixed while the behavior policy is whichever policy produced the current rollouts. In the historical InstructGPT example (slide 82) the reference is the fixed supervised fine-tuned (SFT) model; the behavior policy is the rollout policy, not automatically that fixed model.

Sources. Ouyang et al., NeurIPS 2022; arXiv:2203.02155v1, Sec. 3.5, eq. (2) (E10). Schulman et al., arXiv:1707.06347v2, Sec. 3 (E09). Owen Ch. 9, Sec. 9.1 (E04). Diagram: original schematic.
<!-- END S129 -->

<!-- BEGIN S105 -->
### 81. KL Is Not a Variance Certificate [S105]

**Message.** A KL drift penalty and the weight second moment measure different things; a small KL does not upper-bound $\mathbb{E}_{\pi_b}[w^2]$.

Drift penalty (reference): $D_{\mathrm{KL}}(\pi_\theta\|\pi_{\text{ref}})=\mathbb{E}_{\pi_\theta}[\ln(\pi_\theta(X)/\pi_{\text{ref}}(X))]$. Weight cost (behavior): $\mathbb{E}_{\pi_b}[w^2]=\mathbb{E}_{\pi_b}[(\pi_\theta(X)/\pi_b(X))^2]$. Two-state example with $\pi_b=\pi_{\text{ref}}$: KL about 0.0017 nats, $\mathbb{E}[w^2]$ about 10,001. Natural log; KL in nats.

Details. Take $\pi_\theta=p=(0.9999,0.0001)$ and $\pi_b=\pi_{\text{ref}}=q=(1-10^{-12},10^{-12})$, both with full support. Then $D_{\mathrm{KL}}(p\|q)=0.0017420731$ nats and $\mathbb{E}_q[w^2]=\sum_x p(x)^2/q(x)=10000.9998$; the rare outcome contributes $10^{-8}/10^{-12}=10^4$. Jensen gives $\ln\mathbb{E}_q[w^2]\ge D_{\mathrm{KL}}(p\|q)$, a lower bound (here $e^{\mathrm{KL}}\approx1.0017$); used in reverse it cannot certify tame weights. KL is not useless: it measures drift from the reference, a different property.

Sources. Our calculation (E14) with the KL definition from the course prerequisites (E01); Ouyang et al., NeurIPS 2022 (E10). Numbers: gen/p9e_kl_counterexample.py.
<!-- END S105 -->

<!-- BEGIN S106 -->
### 82. RL Objectives Contain Expectations [S106]

**Message.** A simplified reward-plus-KL objective from reinforcement learning from human feedback (RLHF) is a combination of expectations under the current policy, so evaluating it is a Monte Carlo problem, and an importance-sampling problem when the responses are old.

$$\max_\theta\ \mathbb{E}_{X\sim\pi_\theta}[r(X)]-\beta\,D_{\mathrm{KL}}(\pi_\theta\|\pi_{\text{ref}}),\qquad \beta\ge0.$$

The first term is the learned reward, held fixed; the second is the penalty against the fixed SFT reference. The prompt $c$ is fixed and dropped; $r$ is a reward model fitted to human comparisons; $\pi_{\text{ref}}$ is the supervised fine-tuned (SFT) model. Both terms are expectations under $\pi_\theta$: the reward term directly, and the KL term because $D_{\mathrm{KL}}(\pi_\theta\|\pi_{\text{ref}})=\mathbb{E}_{\pi_\theta}[\ln(\pi_\theta(X)/\pi_{\text{ref}}(X))]$ (slide [[S105]]). With fresh responses from the current policy, a plain Monte Carlo average estimates the objective; with responses logged under a behavior policy, each term is reweighted by $w=\pi_\theta/\pi_b$ as on slide [[S101]]. Historical InstructGPT case, simplified; not a survey of current methods.

Details. The source objective also has $\gamma\,\mathbb{E}_{x\sim D_{\text{pretrain}}}[\log\pi_\phi^{\text{RL}}(x)]$; $\gamma=0$ gives "PPO", PPO-ptx adds the pretraining term, omitted here. The paper writes $r_\theta$ for the reward model and $\pi_\phi$ for the policy.

Estimating the objective. At a fixed $\theta$, write $g_\theta(x)=r(x)-\beta\ln(\pi_\theta(x)/\pi_{\text{ref}}(x))$, so $J(\theta)=\mathbb{E}_{\pi_\theta}[g_\theta(X)]$. With IID responses $x_1,\dots,x_n$ from $\pi_\theta$, $\frac1n\sum_i g_\theta(x_i)$ is unbiased for $J(\theta)$ when $\mathbb{E}_{\pi_\theta}|g_\theta|<\infty$; its error bar needs finite variance, as in Part 01. With IID responses from a fixed behavior policy $\pi_b$ that covers $\pi_\theta$, $\frac1n\sum_i w(x_i)g_\theta(x_i)$ is unbiased under the conditions of slide [[S101]], and its variance can be large or infinite (slides [[S103]], [[S105]]). Estimating the objective's value is not optimizing it: how $\theta$ is updated, for example by PPO's clipped surrogate on the next slide, is a separate step this lecture does not derive.

Sources. Ouyang et al., "Training language models to follow instructions with human feedback," NeurIPS 2022; arXiv:2203.02155v1, Sec. 3.5 "Models", RL paragraph, eq. (2) (E10). Importance-sampling identity and conditions: Owen Ch. 9, Sec. 9.1, Theorem 9.1 (E04). The estimators are the lecture's own Monte Carlo and importance-sampling averages applied to this objective.
<!-- END S106 -->

<!-- BEGIN S104 -->
### 83. A Surrogate Is Not a Hard Constraint [S104]

**Message.** PPO's clipping changes the objective being optimized; it does not force every realized probability ratio to stay in $[1-\epsilon,1+\epsilon]$.

$$\min\big(r\hat A,\ \mathrm{clip}(r,1-\epsilon,1+\epsilon)\hat A\big),\qquad r=\frac{\pi_\theta(a\mid s)}{\pi_{\theta_{\text{old}}}(a\mid s)}.$$

Proximal policy optimization (PPO); $\hat A$ is the estimated advantage of action $a$ in state $s$: how much better ($\hat A>0$) or worse ($\hat A<0$) taking $a$ turned out than what the policy expected on average in state $s$. How $\hat A$ is estimated is outside this lecture; reading the figure needs only its sign.

Figure (Schulman et al. 2017, Figure 1, unmodified): two panels plotting one term of $L^{\mathrm{CLIP}}$ against $r$, red dot at $r=1$. Left, $\hat A>0$: the term rises linearly until $r=1+\epsilon$, then is flat. Right, $\hat A<0$: the term is flat for $r<1-\epsilon$, then falls linearly. Where flat, there is no gain from moving $r$ further, but realized $r$ can still leave $[1-\epsilon,1+\epsilon]$; the clipped objective is not the exact IS identity.

Details. Equation (7) of the source:

$$L^{\mathrm{CLIP}}(\theta)=\hat{\mathbb{E}}_t\Big[\min\big(r_t(\theta)\hat A_t,\ \mathrm{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t\big)\Big],$$

with example value $\epsilon=0.2$. The ratio is per action, conditional on the state, against the old policy that collected the batch; it is not the full-sequence weight of slide [[S102]]. Clipping is sign-sensitive through the min. Section 4 describes a separate adaptive KL-penalty variant with $\mathrm{KL}[\pi_{\theta_{\text{old}}},\pi_\theta]$, against the old policy rather than a fixed reference. No universal safety claim follows.

Sources. Schulman, Wolski, Dhariwal, Radford, Klimov, "Proximal Policy Optimization Algorithms," arXiv:1707.06347v2 (2017), Sec. 3, eq. (7), Figure 1; Sec. 4, eq. (8) (E09). Figure: unmodified 300-dpi crops of Figure 1, page 3 of v2 (fig/p9e-ppo-fig1-pos.png, fig/p9e-ppo-fig1-neg.png).
<!-- END S104 -->

## Closing

<!-- BEGIN S109a -->
### 84. Choose an Expectation Estimator by Its Requirements [S109a]

**Message.** For an expectation, the ingredients you can compute decide which estimators are available; the conditions they meet decide what you can honestly claim.

The slide opens with the shared setting: target $\mu=\mathbb E_p[f(X)]$, IID draws, and $\mathbb E_p|f(X)|<\infty$. Below it is a three-column table, read row by row:

- Ordinary MC. Needs: draws from $p$. Claim: unbiased; RMSE $\sigma_f/\sqrt{n}$ if $\sigma_f<\infty$.
- Importance sampling. Needs: draws from $q$, an evaluable normalized ratio $p/q$, and $q>0$ wherever $fp\neq 0$. Claim: unbiased; the variance is finite only if $\mathbb E_q[(fw)^2]<\infty$.
- Self-normalized IS. Needs: $\tilde p\propto p$, $q>0$ wherever $p>0$, and a positive total of the sampled weights. Claim: consistent; generally biased at finite $n$.

The slide has no highlight line. The lecture's warning is said aloud: unbiased or consistent is not low error; check the second moment.

Full coverage of $p$ is enough for importance sampling but not necessary; first-moment validity and finite variance are separate checks. The self-normalized bias has exceptions, such as constant $f$ or $q=p$.

Question for the room: which row fits each earlier example (darts for $\pi$; $\mathbb P(X>10)$ with $X\sim\mathrm{Exp}(1)$, where ordinary MC is also available; a target known up to its normalizer)?

Formula reference:

- Ordinary MC: $\hat\mu_n = \frac1n\sum_{i=1}^n f(X_i)$, $X_i\sim p$ IID, $\mathbb E_p|f(X)|<\infty$; unbiased, and with finite variance $\sigma_f^2$, $\mathrm{RMSE}=\sigma_f/\sqrt n$.
- Importance sampling: $\hat\mu_{\mathrm{IS}} = \frac1n\sum_i w(X_i) f(X_i)$, $w=p/q$, $X_i\sim q$ IID; unbiased when $q>0$ wherever $fp\neq 0$ and $\mathbb E_p|f(X)|<\infty$; finite variance only if $\mathbb E_q[w^2f^2]<\infty$.
- Self-normalized IS: $\hat\mu_{\mathrm{SN}} = \sum_i \tilde w_i f(X_i)/\sum_j\tilde w_j$, $\tilde w=\tilde p/q$, $X_i\sim q$ IID; requires $q>0$ wherever $p>0$, a proper target ($0<Z<\infty$), $\mathbb E_p|f(X)|<\infty$ and a positive denominator; consistent under these conditions, generally biased at finite $n$.

Prerequisites in the series (optional): prob01 (LOTUS, Jensen), prob02 (KL), prob04 (chain rule of probability), prob05 (mean and variance of a sample mean, LLN, Chebyshev, CLT), prob06 (Hoeffding), prob07 (MSE decomposition, bias), prob08 (Gaussian machinery, the substrate for the Gaussian path $X=\theta+\varepsilon$).

Sources: summary of results sourced on the earlier slides (E02, E04-E06); prerequisite locations E01.
<!-- END S109a -->

<!-- BEGIN S113 -->
### 86. Closer [S113]

**Message.** The target stays the same; the sampler and the estimator decide the error.

The closing slide shows the importance-sampling identity $\mathbb E_p[f(X)] = \mathbb E_q[f(X)\,p(X)/q(X)]$ and "Questions?". Closing cue: before trusting a Monte Carlo number, name what it needs and what error claim it supports. Further reading is in the References.
<!-- END S113 -->

## References

1. A. B. Owen, *Monte Carlo theory, methods and examples*, chapters posted online (accessed 2026-11-17): Ch. 1-2 for the Monte Carlo estimator and its error, https://artowen.su.domains/mc/Ch-intro.pdf ; Ch. 7 (Sections 7.1, 7.4) for tensor-grid quadrature, https://artowen.su.domains/mc/Ch-quadrature.pdf ; Ch. 9 for importance sampling (Section 9.1, Theorem 9.1 and the optimal density), self-normalized importance sampling (Section 9.2, Theorem 9.2) and weight diagnostics (Section 9.3, eqs. 9.13-9.14), https://artowen.su.domains/mc/Ch-var-is.pdf
2. C. P. Robert, G. Casella, *Monte Carlo Statistical Methods*, 2nd ed., Springer, 2004. Further reading on Monte Carlo integration and importance sampling, and on the MCMC methods this lecture does not cover. https://doi.org/10.1007/978-1-4757-4145-2
3. S. Mohamed, M. Rosca, M. Figurnov, A. Mnih, "Monte Carlo Gradient Estimation in Machine Learning," *JMLR* 21(132), 2020. Pathwise and score-function estimators and their assumptions (Sections 4.2-4.3, 5.2-5.3), baselines (Section 7.4.3). https://jmlr.org/papers/volume21/19-346/19-346.pdf
4. D. P. Kingma, M. Welling, "Auto-Encoding Variational Bayes," ICLR 2014, Section 2.3: the reparameterization trick. https://arxiv.org/abs/1312.6114
5. R. J. Williams, "Simple statistical gradient-following algorithms for connectionist reinforcement learning," *Machine Learning* 8:229-256, 1992. The REINFORCE estimator, for historical background. https://doi.org/10.1007/BF00992696
6. J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov, "Proximal Policy Optimization Algorithms," arXiv:1707.06347v2, 2017. Section 3 clipped surrogate objective, eq. (7) and Figure 1; Section 4 KL-penalty variant. https://arxiv.org/abs/1707.06347
7. L. Ouyang et al., "Training language models to follow instructions with human feedback," NeurIPS 2022. The reward-plus-KL RL objective, arXiv:2203.02155v1 Section 3.5, eq. (2). https://arxiv.org/abs/2203.02155
8. R. S. Sutton, A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. Further reading on policy-gradient methods and baselines. http://incompleteideas.net/book/the-book.html
9. Companion notes in this series, read at commit b20ab73: prob01 (LOTUS, Jensen), prob02 (KL divergence), prob04 (chain rule of probability), prob05 (mean and variance of a sample mean, LLN, Chebyshev, CLT), prob06 (Hoeffding), prob07 (MSE decomposition, estimator bias), prob08 (Gaussian machinery).
