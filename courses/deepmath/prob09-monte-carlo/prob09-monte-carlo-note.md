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

(placeholder, P1)
<!-- END S04 -->

<!-- BEGIN S06 -->
### 5. Sample, Evaluate, Average [S06]

(placeholder, P1)
<!-- END S06 -->

<!-- BEGIN S26 -->
### 6. Six Draws Give a Noisy Estimate [S26]

(placeholder, P1)
<!-- END S26 -->

<!-- BEGIN S16 -->
### 7. Monte Carlo Reuses the Sample Mean [S16]

(placeholder, P1)
<!-- END S16 -->

<!-- BEGIN S19 -->
### 8. Unbiased Does Not Mean Accurate [S19]

(placeholder, P1)
<!-- END S19 -->

<!-- BEGIN S22 -->
### 9. Averaging Reduces RMSE [S22]

(placeholder, P1)
<!-- END S22 -->

<!-- BEGIN S114 -->
### 10. Estimating the Error Bar [S114]

(placeholder, P1)
<!-- END S114 -->

<!-- BEGIN S115 -->
### 11. Approximate Intervals, Exact Guarantees [S115]

(placeholder, P1)
<!-- END S115 -->

<!-- BEGIN S24 -->
### 12. Bounded Averages Concentrate [S24]

(placeholder, P1)
<!-- END S24 -->

<!-- BEGIN S33 -->
### 13. The Rate Is Not the Cost [S33]

(placeholder, P1)
<!-- END S33 -->

<!-- BEGIN S37 -->
### 14. Tensor Grids Grow With Dimension [S37]

(placeholder, P1)
<!-- END S37 -->

<!-- BEGIN S116 -->
### 15. Rare Events Need Relative Error [S116]

(placeholder, P1)
<!-- END S116 -->

<!-- BEGIN S41 -->
### 16. 02 · Change the Sampler [S41]

(placeholder, INT)
<!-- END S41 -->

<!-- BEGIN S43 -->
### 17. Most Draws Miss the Tail [S43]

**Message.** A rare-event probability with a known answer shows why plain sampling wastes almost every draw.

Target: $X \sim \mathrm{Exp}(1)$ (rate 1), density $p(x) = e^{-x}$ for $x \ge 0$. Integrand: $f(x) = \mathbf{1}\{x > 10\}$.

$$\mu = \Pr_p(X > 10) = \int_{10}^\infty e^{-x}\,dx = e^{-10} \approx 0.0000454.$$

About 1 draw in 22,026 lands in the event on average ($1/\mu = e^{10} \approx 22{,}026.47$). The answer is known, so it is a benchmark for estimators.

Figure: the exact density $e^{-x}$ on 0 to 14. Beyond $x = 10$ (shaded "event") it is invisible at this scale. An inset magnifies the tail from 10 to 14 with a vertical axis from 0 to $5 \times 10^{-5}$; the shaded area under it is $e^{-10}$.

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

**Message.** If $q$ never visits a region where $fp \ne 0$, the estimator is wrong for every sample size.

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

Figure: log-scale plot of $fw$ for $x$ from 8 to 20. Zero up to 10; $1.23 \times 10^{-3}$ at $x = 10$ (about $27\mu$), falling to about $1.5 \times 10^{-7}$ at 20. A dashed line marks $\mu = e^{-10}$; the curve crosses it near $x = 13.7$.

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

1. Validity: $q > 0$ wherever $fp \ne 0$. Gives: unbiased, same $\mu$. $\mathrm{Exp}(0.1)$: positive on all $x \ge 0$ (passes).
2. Precision: $\int f^2p^2/q$ finite and small. Gives: small RMSE per draw. $\mathrm{Exp}(0.1)$: relative variance 13.3 vs 22,025 (passes).

Valid is not the same as useful: a covering $q$ can have larger, even infinite, variance.

Sources: E04; E11.
<!-- END S54 -->

<!-- BEGIN S55 -->
### 31. 03 · Control Proposal Risk [S55]

(placeholder, INT)
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

$$q^*(x) = \frac{\mathbf{1}\{x > 10\}\,e^{-x}}{e^{-10}} = e^{-(x-10)}, \quad x > 10.$$

Each draw: $fw^* = e^{-10}$ exactly, so the variance is 0. This is an oracle benchmark built from the known answer. Sign-changing $f$: usually $c^2 - \mu^2 > 0$.

Figure: $q^*$ is zero below 10, jumps to 1 at $x = 10$ and decays exponentially; a strip below shows schematic draws, all past 10, each with $fw^* = e^{-10}$.

Sources: E04; our calculation; figure `gen/p9b_figs.py` -> `fig/p9b-oracle.svg`.
<!-- END S63 -->

<!-- BEGIN S64 -->
### 38. The Oracle Needs a Normalizer [S64]

**Message.** Evaluating the optimal weight requires $c$, which for a one-sign integrand is the answer itself.

Dependency loop (diagram): $c = \mu$ (unknown target) -> $q^* = fp/c$ -> weight $w^* = p/q^* = c$ on $x > 10$ -> estimate $\mu$ -> back to $c$. The weight needs $c$, and $c$ is the answer.

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

**Message.** A finite first moment gives convergence; only a finite second moment gives variance, RMSE and CLT error bars.

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
