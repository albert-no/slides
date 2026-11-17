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

**Message.** In this part the parameter $\theta$ no longer weights a fixed sample; it changes the distribution $p_\theta$ that generates the sample, and we want the derivative of an average with respect to that change.

Until now the distribution we sampled from was fixed, and Monte Carlo estimated one number. Now the distribution itself carries a parameter. The quantity of interest is the expected reward

$$J(\theta) = \mathbb{E}_{X \sim p_\theta}\big[R(X)\big],$$

where the reward $R$ is a fixed function: it does not depend on $\theta$. The only way $\theta$ affects $J$ is through which values of $X$ tend to be drawn. The goal of this part is $\nabla_\theta J(\theta)$, the direction in which to move $\theta$ to raise the average reward.

The figure on the slide reads left to right: parameters $\theta$ set the distribution $p_\theta$, the distribution produces a random draw $X$, and the draw receives the reward $R(X)$. Averaging that reward over $X \sim p_\theta$ gives $J(\theta)$.

**Details.**

Throughout this part, $\theta$ denotes the parameters, $p_\theta$ a generic distribution (written $\pi_\theta$ in the two-action example), and $R$ the fixed reward used in the gradient examples. Logarithms are natural.

**Sources.**

Problem setup as in Mohamed, Rosca, Figurnov and Mnih, "Monte Carlo Gradient Estimation in Machine Learning," *JMLR* 21(132), 2020 (E07). Figure: drawn for this note.
<!-- END S84 -->

<!-- BEGIN S85 -->
### 57. Frozen Samples Hide the Derivative [S85]

**Message.** Drawing samples once and differentiating their average reward gives no gradient information, because stored numbers contain no $\theta$; the gradient must itself be written as an expectation and then estimated.

Suppose we draw $x_1, \dots, x_n$ from $p_\theta$ and store them. The average $\tfrac1n \sum_i R(x_i)$ is now a fixed number: no $\theta$ appears in it, so its derivative in $\theta$ is zero. Yet $J(\theta)$ does change with $\theta$, because a different $\theta$ would have produced different draws. The figure contrasts the two situations. In the frozen row the link from $\theta$ to the samples is cut. In the live row $\theta$ sets $p_\theta$, and $p_\theta$ decides which $X_i$ appear.

So the answer to "can Monte Carlo estimate $\nabla_\theta J$?" is yes, but not by differentiating stored samples. We first rewrite $\nabla_\theta J(\theta)$ as an expectation of some computable quantity, and then estimate that expectation by sampling. This part gives two such rewrites: the pathwise one and the score-function one.

**Details.**

The two rewrites differ in what they require: the pathwise form needs a differentiable sampling recipe and a differentiable reward, the score-function form needs a differentiable log-probability. Both need the derivative and the expectation to be exchangeable.

**Sources.**

Mohamed et al., JMLR 2020 (E07). Figure: drawn for this note.
<!-- END S85 -->

<!-- BEGIN S123 -->
### 58. A Gaussian Sample Is a Recipe [S123]

**Message.** A Gaussian sample can be produced by a recipe, $X_\theta = \theta + \varepsilon$ with $\varepsilon \sim \mathcal{N}(0,1)$, in which all randomness sits in noise whose law does not depend on $\theta$.

Recall the construction of a Gaussian vector: if $W$ has independent $\mathcal{N}(0,1)$ entries, then $X = DW + \mu$ is Gaussian with mean $\mu$. The scalar case with $D = 1$ and $\mu = \theta$ gives

$$X_\theta = \theta + \varepsilon, \qquad \varepsilon \sim \mathcal{N}(0,1),$$

so $X_\theta$ has distribution $\mathcal{N}(\theta, 1)$. The figure shows the recipe: the noise $\varepsilon$ is drawn from a law that does not involve $\theta$, then $\theta$ is added. Along the addition, $\partial X_\theta / \partial \theta = 1$.

This changes what "differentiate the sample" means. We do not differentiate a stored number. We hold the noise $\varepsilon$ fixed and ask how the output of the recipe moves when $\theta$ moves.

**Details.**

The same idea applies to any recipe $X = T_\theta(\varepsilon)$ with a base noise law free of $\theta$; the Gaussian location shift is the simplest case.

**Sources.**

Gaussian by construction: course prerequisite, prob08 slide 37 "Definition 2 - by Construction" (E01, E15). Figure: drawn for this note.
<!-- END S123 -->

<!-- BEGIN S124 -->
### 59. Differentiate Along the Sampling Path [S124]

**Message.** If $X = T_\theta(\varepsilon)$ with noise law free of $\theta$, the gradient is the expected chain-rule derivative along the sampling path, provided the derivative and expectation may be swapped.

Write the sample as $X = T_\theta(\varepsilon)$. Because the law of $\varepsilon$ does not depend on $\theta$, $J(\theta) = \mathbb{E}_\varepsilon[R(T_\theta(\varepsilon))]$ is an average over a fixed distribution of a function of $\theta$. For scalar $\theta$ and $X$:

$$\nabla_\theta J(\theta) = \mathbb{E}_{\varepsilon}\big[\nabla_\theta R(T_\theta(\varepsilon))\big]$$

(swap of $\nabla$ and $\mathbb{E}$), and by the chain rule

$$\nabla_\theta R(T_\theta(\varepsilon)) = R'(T_\theta(\varepsilon))\,\partial_\theta T_\theta(\varepsilon).$$

The figure shows the forward path $\varepsilon \to X \to R(X)$ and the two backward factors, $\partial_\theta T_\theta(\varepsilon)$ and $R'(X)$, that the chain rule multiplies.

The requirements are visible in the formula: the noise law must be free of $\theta$, $T_\theta$ must be differentiable in $\theta$, and $R$ must be differentiable in $X$. The swap of derivative and expectation is a separate condition; it is not automatic.

**Details.**

For vector $\theta$ and $X$ the chain rule becomes a Jacobian product. A sufficient condition for the swap is that, for $\theta$ in a neighbourhood $U$, $|\nabla_\theta R(T_\theta(\varepsilon))|$ is bounded by a function $g(\varepsilon)$ with $\mathbb{E}[g(\varepsilon)] < \infty$ (dominated convergence).

**Sources.**

Mohamed et al., JMLR 2020, Secs. 5.2-5.3 (E07); D. P. Kingma and M. Welling, "Auto-Encoding Variational Bayes," ICLR 2014, Sec. 2.3 (E15). Figure: drawn for this note.
<!-- END S124 -->

<!-- BEGIN S125 -->
### 60. Check the Gaussian Gradient [S125]

**Message.** For $R(X) = X^2$ with $X = \theta + \varepsilon$, the exact derivative is $2\theta$, and the pathwise contribution $2X$ has exactly that mean.

Analytic check: expand the square and use $\mathbb{E}[\varepsilon] = 0$, $\mathbb{E}[\varepsilon^2] = 1$.

$$J(\theta) = \mathbb{E}\big[\theta^2 + 2\theta\varepsilon + \varepsilon^2\big] = \theta^2 + 1,$$

$$J'(\theta) = 2\theta.$$

Pathwise contribution: hold $\varepsilon$ fixed and differentiate $(\theta + \varepsilon)^2$ in $\theta$, which gives $2(\theta + \varepsilon) = 2X$. Its mean is $2\theta + 2\,\mathbb{E}[\varepsilon] = 2\theta$, the same derivative.

The agreement is about means. A single contribution $2X$ is random: $\operatorname{Var}(2X) = 4\operatorname{Var}(\varepsilon) = 4$. At $\theta = 1$ the target is $2$, while five seeded draws of $2X$ in our generator give $2.28$, $1.66$, $2.14$, $3.38$, $1.42$.

**Details.**

The generator also checks the identity numerically at $\theta = 1$ by quadrature over $\varepsilon$: $J = 2$, $\mathbb{E}[2X] = 2$, $\operatorname{Var}(2X) = 4$.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py` (Simpson quadrature on $[-12, 12]$; seed 20261117 for the five draws).
<!-- END S125 -->

<!-- BEGIN S126 -->
### 61. Discrete Draws Need Another Route [S126]

**Message.** When the outcome is discrete, the sampled action jumps rather than moving smoothly, so there is no useful path derivative; instead we differentiate the probabilities, which do move smoothly.

Take two actions: $a_1$ with reward $1$ and $a_0$ with reward $0$. The policy picks $a_1$ with probability $\sigma(\theta) = 1/(1 + e^{-\theta})$. Then

$$J(\theta) = \sigma(\theta)\cdot 1 + \big(1 - \sigma(\theta)\big)\cdot 0 = \sigma(\theta).$$

The bar chart compares $\theta = 0$, where both actions have probability $\tfrac12$, with $\theta = 1$, where $a_1$ has probability $0.731$ and $a_0$ has $0.269$. Raising $\theta$ moves probability mass toward $a_1$. The actions themselves do not change: each draw is still $a_1$ or $a_0$.

This is why the pathwise route fails here. Any recipe that maps noise to an action produces a value that jumps between two points, so its derivative in $\theta$ carries no information about how the probabilities move.

**Details.**

Concretely, take $U$ uniform on $(0,1)$ and set $A = a_1$ if $U < \sigma(\theta)$, else $a_0$. For almost every fixed $U$, a small change in $\theta$ leaves $A$ unchanged, so the derivative of $R(A)$ in $\theta$ is $0$ almost everywhere. Its expectation is $0$, while $J'(\theta) = \sigma'(\theta) \gt 0$: the naive swap gives the wrong answer because the threshold moves. The values $0.731$ and $0.269$ are $\sigma(1)$ and $1 - \sigma(1)$ to three decimals.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py`. Figure: drawn to scale from those values.
<!-- END S126 -->

<!-- BEGIN S86 -->
### 62. The Log-Derivative Identity [S86]

**Message.** Wherever $p_\theta(x) \gt 0$ is differentiable in $\theta$, the derivative of the probability equals the probability times the parameter score $s_\theta(x) = \nabla_\theta \ln p_\theta(x)$.

By the chain rule for the natural logarithm, with $x$ held fixed,

$$\nabla_\theta \ln p_\theta(x) = \frac{\nabla_\theta\, p_\theta(x)}{p_\theta(x)}.$$

Multiplying both sides by $p_\theta(x)$ gives

$$\nabla_\theta\, p_\theta(x) = p_\theta(x)\, s_\theta(x).$$

The identity needs $p_\theta(x) \gt 0$ (so that the logarithm is defined) and differentiability in $\theta$. The quantity $s_\theta(x) = \nabla_\theta \ln p_\theta(x)$ is the *parameter score*.

It is not the same as the sample-space score $\nabla_x \ln p(x)$, which differentiates in the sample, not in the parameter.

**Details.**

The point of the rewrite is that a derivative of a probability, which is not itself an expectation, becomes a probability-weighted quantity. That weighting is what turns sums into expectations in the next proof.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 4.2 (E07).
<!-- END S86 -->

<!-- BEGIN S87 -->
### 63. Reward Times Score Gives the Gradient [S87]

**Message.** On a fixed finite outcome set with positive differentiable probabilities, the gradient of the expected reward equals the expected reward times score.

**Theorem (score-function identity).** Let $\mathcal{X}$ be a fixed finite set, let $p_\theta(x) \gt 0$ be differentiable in $\theta$ for every $x \in \mathcal{X}$, and let $R : \mathcal{X} \to \mathbb{R}$ be a fixed reward. Then

$$\nabla_\theta\, \mathbb{E}_{X \sim p_\theta}[R(X)] = \mathbb{E}_{X \sim p_\theta}\big[R(X)\, s_\theta(X)\big].$$

Only $\ln p_\theta$ is differentiated; the reward is just evaluated at the drawn outcomes. So $R$ may be discontinuous, a black box, or defined only on a discrete set. The proof follows on the next three slides.

For continuous $X$ the same formula holds under extra conditions: the swap of derivative and integral must be justified, and the support of $p_\theta$ must not move with $\theta$.

**Details.**

A sufficient condition in the continuous case: for $\theta$ in a neighbourhood $U$, $\sup_{\theta \in U} |R(x)\,\nabla_\theta p_\theta(x)| \le g(x)$ with $\int g(x)\,dx < \infty$; dominated convergence then allows the swap. For vector $\theta$ the identity holds componentwise.

**Sources.**

Mohamed et al., JMLR 2020, Secs. 4.2-4.3 (E07).
<!-- END S87 -->

<!-- BEGIN S88 -->
### 64. Proof: Expand the Expectation [S88]

**Message.** On a finite set the expectation is a weighted sum, in which only the weights $p_\theta(x)$ depend on $\theta$.

Write the expectation out:

$$J(\theta) = \sum_{x \in \mathcal{X}} p_\theta(x)\, R(x).$$

Each term is a weight $p_\theta(x)$, which depends on $\theta$, times a number $R(x)$, which does not. The outcome set $\mathcal{X}$ is also fixed.

After this step nothing random remains: the sampling has disappeared into the weights, and we never need the derivative of a drawn $X$.

**Details.**

This is the step that fails to generalize for free: for an infinite or continuous outcome space, the sum becomes an infinite series or an integral.

**Sources.**

Proof as in Mohamed et al., JMLR 2020, Sec. 4.2 (E07), specialized to a finite set.
<!-- END S88 -->

<!-- BEGIN S89 -->
### 65. Proof (continued): Differentiate the Finite Sum [S89]

**Message.** A finite sum may be differentiated term by term, and since $R$ is fixed only the weights are differentiated.

Starting from $J(\theta) = \sum_x p_\theta(x) R(x)$ with finitely many terms:

$$\nabla_\theta J(\theta) = \sum_{x} \nabla_\theta\big[p_\theta(x)\, R(x)\big]$$

(derivative of a finite sum), and since $R(x)$ does not depend on $\theta$,

$$\nabla_\theta J(\theta) = \sum_{x} R(x)\, \nabla_\theta\, p_\theta(x).$$

For integrals or infinite sums this exchange of derivative and sum is exactly the step that needs its own justification.

**Details.**

The sum $\sum_x R(x)\nabla_\theta p_\theta(x)$ is the exact gradient, but it is not yet an expectation: the derivatives $\nabla_\theta p_\theta(x)$ can be negative and do not sum to one, so we cannot sample from them.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 4.2 (E07).
<!-- END S89 -->

<!-- BEGIN S90 -->
### 66. Proof (continued): Read an Expectation [S90]

**Message.** The log-derivative identity puts the weights $p_\theta(x)$ back in front, which turns the sum into an expectation under the current $p_\theta$.

Apply $\nabla_\theta p_\theta(x) = p_\theta(x) s_\theta(x)$, valid because $p_\theta(x) \gt 0$:

$$\sum_{x} R(x)\, \nabla_\theta\, p_\theta(x) = \sum_{x} p_\theta(x)\, R(x)\, s_\theta(x).$$

A sum of $p_\theta(x)$ times a function of $x$ is an expectation under $p_\theta$:

$$\nabla_\theta J(\theta) = \mathbb{E}_{X \sim p_\theta}\big[R(X)\, s_\theta(X)\big]. \qquad \blacksquare$$

The weights are the current probabilities $p_\theta$. So the samples used to estimate the gradient must come from the current $p_\theta$, not from an older or different distribution.

**Details.**

Samples from another distribution can still be used, but only with an importance-sampling correction, which is the subject of the next part.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 4.2 (E07).
<!-- END S90 -->

<!-- BEGIN S92 -->
### 67. Average the Gradient Contributions [S92]

**Message.** The score-function (REINFORCE) estimator averages reward times score over draws from $p_\theta$; under the theorem's conditions it is unbiased for $\nabla_\theta J$.

The recipe in the figure: draw $X_i \sim p_\theta$, compute its reward $R(X_i)$ and its score $s_\theta(X_i)$, multiply the two, and average over $i$:

$$\hat{g}_n = \frac{1}{n}\sum_{i=1}^{n} R(X_i)\, s_\theta(X_i),$$

with $X_1, \dots, X_n$ IID from $p_\theta$. Each term has mean $\mathbb{E}[R(X)s_\theta(X)] = \nabla_\theta J(\theta)$ by the theorem, so $\mathbb{E}[\hat{g}_n] = \nabla_\theta J(\theta)$ (componentwise for vector $\theta$).

What the estimator needs: samples from the current distribution, the reward values at those samples, and the score $\nabla_\theta \ln p_\theta$. It never needs $\nabla R$.

**Details.**

$\hat g_n$ is a plain Monte Carlo average of the contribution $R(X)s_\theta(X)$, so its variance is $\operatorname{Var}(R s_\theta)/n$ per component, as for any sample mean of IID terms.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 4.2 (E07). Figure: drawn for this note.
<!-- END S92 -->

<!-- BEGIN S93 -->
### 68. A Two-Action Policy [S93]

**Message.** A two-action policy with a sigmoid probability gives an exact derivative, $J'(\theta) = \sigma(\theta)(1 - \sigma(\theta))$, against which to check the score-function estimator.

The tree in the figure: the policy $\pi_\theta$ picks $a_1$ (reward $1$) with probability $\sigma(\theta)$ and $a_0$ (reward $0$) with probability $1 - \sigma(\theta)$, where $\sigma(\theta) = 1/(1 + e^{-\theta})$. Then $J(\theta) = \sigma(\theta)$.

Differentiate the sigmoid:

$$\sigma'(\theta) = \frac{e^{-\theta}}{(1 + e^{-\theta})^2} = \sigma(\theta)\big(1 - \sigma(\theta)\big),$$

since $1 - \sigma(\theta) = e^{-\theta}/(1 + e^{-\theta})$.

At $\theta = 0$, $\sigma = \tfrac12$ and $J'(0) = \tfrac14$. The parameter is continuous while the actions are discrete, the situation where the pathwise route fails.

**Details.**

At $\theta = 1$: $\sigma = 0.7311$, $1 - \sigma = 0.2689$ and $J'(1) = 0.1966$; central differences in the generator agree with both values.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py`. Figure: drawn for this note.
<!-- END S93 -->

<!-- BEGIN S94 -->
### 69. Both Routes Give the Same Derivative [S94]

**Message.** On the two-action toy, reward times score has mean $\sigma(1 - \sigma)$, exactly the direct derivative, although each single contribution is $0$ or $\tfrac12$ at $\theta = 0$.

The scores are $s_\theta(a_1) = \frac{d}{d\theta}\ln\sigma(\theta) = 1 - \sigma$ and $s_\theta(a_0) = \frac{d}{d\theta}\ln(1 - \sigma(\theta)) = -\sigma$. Then

$$\mathbb{E}[R\, s_\theta] = \sigma \cdot 1 \cdot (1 - \sigma) + (1 - \sigma)\cdot 0 \cdot(-\sigma)$$

$$= \sigma(1 - \sigma),$$

which matches $J'(\theta)$ from the previous slide.

The number line on the slide shows the two possible single-draw contributions at $\theta = 0$: $0$ for $a_0$ and $\tfrac12$ for $a_1$, each with probability $\tfrac12$. Neither equals the gradient $\tfrac14$; only their mean does. That spread is the variance of the estimator.

**Details.**

At $\theta = 0$ the scores are $\tfrac12$ and $-\tfrac12$, and the variance of one contribution is $\tfrac1{16}$.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py` (exact fractions). Figure: drawn to scale from those values.
<!-- END S94 -->

<!-- BEGIN S96a -->
### 70. The Score Has Mean Zero [S96a]

**Message.** Under the theorem's conditions the score has mean zero, because the probabilities always sum to one.

With a fixed finite $\mathcal{X}$ and $p_\theta \gt 0$ differentiable:

$$\mathbb{E}_{p_\theta}[s_\theta(X)] = \sum_x p_\theta(x)\,\nabla_\theta \ln p_\theta(x)$$

by definition of expectation;

$$= \sum_x \nabla_\theta\, p_\theta(x)$$

by the log-derivative identity;

$$= \nabla_\theta \sum_x p_\theta(x)$$

because the sum is finite; and since the probabilities sum to one,

$$= \nabla_\theta 1 = 0.$$

Mean zero does not mean each score is zero. In the two-action toy at $\theta = 0$ the scores are $\tfrac12$ and $-\tfrac12$; they cancel only on average.

**Details.**

This is the special case $R \equiv 1$ of the score-function identity: the expected reward is constantly $1$, so its gradient is $0$.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 4.2 (E07); toy values from `gen/p9d_gradient_checks.py` (E13).
<!-- END S96a -->

<!-- BEGIN S96b -->
### 71. A Valid Baseline Preserves the Gradient [S96b]

**Message.** Subtracting a constant baseline $b$ from the reward leaves the expected gradient unchanged, because the score has mean zero; it can change the variance in either direction.

For a constant $b$:

$$\mathbb{E}\big[(R(X) - b)\, s_\theta(X)\big]$$

$$= \mathbb{E}\big[R(X)\, s_\theta(X)\big] - b\,\mathbb{E}\big[s_\theta(X)\big]$$

$$= \nabla_\theta J(\theta) - b \cdot 0.$$

The step that pulls $b$ out of the expectation needs $b$ to be fixed before the draw: it must not be a function of the sampled $X$. If the baseline depends on the action, $b(X)$, then $\mathbb{E}[b(X)s_\theta(X)]$ is in general not zero and the cancellation fails.

The mean is preserved for every constant $b$. The variance is not: some baselines lower it, others raise it, as the next two slides show.

**Details.**

A baseline may depend on anything fixed before the draw, for example a state on which the distribution is conditioned: the same argument applied to the conditional distribution gives $\mathbb{E}[s_\theta(X) \mid \text{state}] = 0$.

For scalar $\theta$, write $g_b = (R - b)s_\theta$. Then $\operatorname{Var}(g_b) - \operatorname{Var}(g_0) = \mathbb{E}[s_\theta^2]\; b\,(b - 2b^*)$ with $b^* = \mathbb{E}[R s_\theta^2]/\mathbb{E}[s_\theta^2]$. So $b^*$ minimizes the variance, and a constant $b$ strictly lowers it exactly when $b(b - 2b^*) < 0$. For a vector $\theta$ with one shared scalar baseline, the same calculation for the total variance (the trace) uses $\|s_\theta\|^2$ in place of $s_\theta^2$.

**Sources.**

Mohamed et al., JMLR 2020, Sec. 7.4.3 "Baselines," eq. (61) (E08). Variance formula: our calculation, checked on the toy in `gen/p9d_gradient_checks.py` (E13).
<!-- END S96b -->

<!-- BEGIN S97 -->
### 72. This Baseline Removes the Toy's Variance [S97]

**Message.** On the two-action toy at $\theta = 0$, the baseline $b = \tfrac12$ makes both possible contributions equal to $\tfrac14$, so this estimator has zero variance.

The contribution of one draw is $g_b = (R - b)s_\theta$. At $\theta = 0$ the scores are $\tfrac12$ for $a_1$ and $-\tfrac12$ for $a_0$.

- Without a baseline ($b = 0$): $a_1$ gives $\tfrac12$, $a_0$ gives $0$; mean $\tfrac14$, variance $\tfrac1{16}$.
- With $b = \tfrac12$: $a_1$ gives $(1 - \tfrac12)\cdot\tfrac12 = \tfrac14$, and $a_0$ gives $(0 - \tfrac12)\cdot(-\tfrac12) = \tfrac14$; mean $\tfrac14$, variance $0$.

The figure shows these as two number lines sharing the mean $\tfrac14$: the top line has two dots at $0$ and $\tfrac12$, the bottom line a single dot at $\tfrac14$ for both actions.

This is an exact two-outcome calculation, not an empirical result. Zero variance is special to this toy: here $s_\theta^2 = \tfrac14$ for both actions, so the variance-minimizing $b^* = \mathbb{E}[R s^2]/\mathbb{E}[s^2]$ equals $\mathbb{E}[R] = \tfrac12$.

**Details.**

In general the best constant baseline $b^*$ only minimizes the variance; it reaches zero only when the contribution $(R - b^*)s_\theta$ is the same for every outcome.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py` (exact fractions). Figure: drawn to scale from those values.
<!-- END S97 -->

<!-- BEGIN S127 -->
### 73. A Bad Baseline Adds Variance [S127]

**Message.** On the same toy, $b = 2$ keeps the mean at $\tfrac14$ but raises the variance from $\tfrac1{16}$ to $\tfrac9{16}$: a valid baseline is not automatically a helpful one.

With $b = 2$ at $\theta = 0$, action $a_1$ gives $(1 - 2)\cdot\tfrac12 = -\tfrac12$ and $a_0$ gives $(0 - 2)\cdot(-\tfrac12) = 1$. The mean is still $\tfrac14$; the two values are now farther apart.

For this toy the variance of one contribution is

$$\operatorname{Var}(g_b) = \tfrac14\big(b - \tfrac12\big)^2,$$

which is $\tfrac1{16}$ at $b = 0$, $0$ at $b = \tfrac12$ and $\tfrac9{16}$ at $b = 2$.

The figure shows the two number lines with the same mean: for $b = 0$ the dots sit at $0$ and $\tfrac12$, for $b = 2$ at $-\tfrac12$ (action $a_1$) and $1$ (action $a_0$).

**Details.**

By the general formula $\operatorname{Var}(g_b) - \operatorname{Var}(g_0) = \mathbb{E}[s^2]\, b(b - 2b^*)$ with $\mathbb{E}[s^2] = \tfrac14$ and $b^* = \tfrac12$: $b = \tfrac12$ lowers the variance by $\tfrac1{16}$, $b = 1$ leaves it unchanged, and $b = 2$ raises it by $\tfrac12$.

**Sources.**

Our calculation (E13), `gen/p9d_gradient_checks.py` (exact fractions). Figure: drawn to scale from those values.
<!-- END S127 -->

<!-- BEGIN S128 -->
### 74. Two Gradient Estimators, Different Requirements [S128]

**Message.** Pathwise and score-function estimators target the same gradient but need different things; both need a justified swap of derivative and expectation, and neither always has lower variance.

The decision diagram branches from the target $\nabla_\theta\,\mathbb{E}_{X \sim p_\theta}[R(X)]$ into two routes.

- **Pathwise.** Needs a sampling recipe $X = T_\theta(\varepsilon)$ whose noise law is free of $\theta$, and needs $T_\theta$ and $R$ to be differentiable. Example: for $R = X^2$ with Gaussian $X$, average $2X$.
- **Score function.** Needs $\ln p_\theta(x)$ to be differentiable in $\theta$. The reward is only evaluated, so no $\nabla R$ is needed. Example: for the two-action policy, average $R\,s_\theta$.

Neither route is a universal winner on variance; which one is lower depends on the problem.

**Details.**

The score-function estimator can be combined with a baseline; the pathwise estimator is unavailable when outcomes are discrete or $R$ is not differentiable.

**Sources.**

Mohamed et al., JMLR 2020, Secs. 4.2-4.3 and 5.2-5.3 (E07). Figure: drawn for this note.
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
