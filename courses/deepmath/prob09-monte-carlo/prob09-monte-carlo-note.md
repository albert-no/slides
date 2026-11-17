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

**Message.** Logged responses were drawn from a behavior policy $\pi_b$, while the quantity we want is an expectation under the current policy $\pi_\theta$.

Figure (schematic): three boxes in a row. Left, amber: "behavior $\pi_b(\cdot\mid c)$", the policy that generated the logged responses. Middle, blue: "current $\pi_\theta(\cdot\mid c)$", the policy being trained. Right: the estimate $\mathbb{E}_{X\sim\pi_\theta(\cdot\mid c)}[R(c,X)]$. A solid arrow labelled "samples $x_1,\dots,x_n$" runs from the behavior box to the estimate; a dashed arrow labelled "target only / no fresh samples" runs from the current box to the estimate.

Fix a prompt $c$ and a reward $R(c,x)$ that does not change during the update. The samples come from $\pi_b$ but the expectation is under $\pi_\theta$: the importance-sampling setting from earlier in the lecture.

Details. The behavior policy is a data-collection distribution, not automatically the reference policy a regularizer compares against (slide 80). Later slides drop $c$ by convention; every policy is then conditional on the same fixed prompt. The example is response-level, like a bandit; how a policy change alters which states or prompts are visited in a multi-step environment is outside it.

Sources. Owen, Monte Carlo theory, methods and examples, Ch. 9, Sec. 9.1 (E04); Mohamed, Rosca, Figurnov, Mnih, JMLR 21(132), 2020 (E07); Ouyang et al., NeurIPS 2022 (E10). Diagram: original schematic.
<!-- END S100 -->

<!-- BEGIN S101 -->
### 77. Importance Weights Correct the Mismatch [S101]

**Message.** Weighting each logged response by $w=\pi_\theta/\pi_b$ recovers the current-policy expectation, provided $\pi_b$ covers every response $\pi_\theta$ can produce.

The generic identity $\mathbb{E}_p[f]=\mathbb{E}_q[(p/q)f]$ is relabelled with target $p=\pi_\theta$ and proposal $q=\pi_b$:

$$\mathbb{E}_{\pi_\theta}[R(c,X)]=\mathbb{E}_{\pi_b}\big[w(X)\,R(c,X)\big],\qquad w(x)=\frac{\pi_\theta(x\mid c)}{\pi_b(x\mid c)}.$$

The current policy is on top, the data-generating policy underneath, both evaluated at the logged response. Coverage: $\pi_b(x\mid c)>0$ wherever $\pi_\theta(x\mid c)>0$. Estimator: $\frac1n\sum_i w(x_i)R(c,x_i)$.

Details. With $\pi_b$ and $R$ fixed and differentiation under the expectation justified, $\nabla_\theta\mathbb{E}_{\pi_\theta}[R]=\mathbb{E}_{\pi_b}[w R s_\theta]$ with score $s_\theta=\nabla_\theta\ln\pi_\theta(X\mid c)$, because $\nabla_\theta w=w s_\theta$. Unbiasedness needs integrability; a useful error bar needs finite variance, which coverage alone does not give. Clipped or self-normalized versions are different estimators with separate bias and variance questions.

Sources. Owen Ch. 9, Sec. 9.1, Theorem 9.1 (E04); Mohamed et al., JMLR 2020, Secs. 4.2-4.3, 5.2-5.3 (E07).
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

Left column: tokens independent under $\pi_b$; each $\mathbb{E}[w_t]=1$; each $\mathbb{E}[w_t^2]=1.1$; hence $\mathbb{E}[w^2]=1.1^T$. "Exact formula, not a measured model."

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
### 82. Reward Tuning Uses This Toolkit [S106]

**Message.** A simplified reward-plus-KL objective from reinforcement learning from human feedback (RLHF) is built from the same pieces: Monte Carlo averages, score-function gradients and a fixed reference.

$$\max_\theta\ \mathbb{E}_{X\sim\pi_\theta}[r(X)]-\beta\,D_{\mathrm{KL}}(\pi_\theta\|\pi_{\text{ref}}),\qquad \beta\ge0.$$

The first term is the learned reward, held fixed; the second is the penalty against the fixed SFT reference. The prompt $c$ is fixed and dropped; $r$ is a reward model fitted to human comparisons; $\pi_{\text{ref}}$ is the supervised fine-tuned (SFT) model. Historical InstructGPT case, simplified; not a survey of current methods.

Details. The source objective also has $\gamma\,\mathbb{E}_{x\sim D_{\text{pretrain}}}[\log\pi_\phi^{\text{RL}}(x)]$; $\gamma=0$ gives "PPO", PPO-ptx adds the pretraining term, omitted here. The paper writes $r_\theta$ for the reward model and $\pi_\phi$ for the policy.

Gradient. On a finite support with positive differentiable $\pi_\theta$, fixed positive $\pi_{\text{ref}}$, fixed $r$, $\beta$:

$$J(\theta)=\sum_x\pi_\theta(x)\Big(r(x)-\beta\ln\frac{\pi_\theta(x)}{\pi_{\text{ref}}(x)}\Big).$$

Differentiating gives $\sum_x\nabla\pi_\theta\,r$, then $-\beta\sum_x\nabla\pi_\theta\ln(\pi_\theta/\pi_{\text{ref}})$, then $-\beta\sum_x\pi_\theta\nabla\ln\pi_\theta=-\beta\nabla 1=0$. With $\nabla\pi_\theta=\pi_\theta s_\theta$,

$$\nabla J=\mathbb{E}_{\pi_\theta}\Big[\Big(r-\beta\ln\frac{\pi_\theta}{\pi_{\text{ref}}}\Big)s_\theta\Big].$$

The score form holds by normalization, not by treating the log ratio as a fixed reward. A finite-difference check on a three-outcome softmax agrees to $1.2\times10^{-10}$. Continuous spaces need their own regularity assumptions. This is not a derivation of PPO's clipped surrogate.

Sources. Ouyang et al., "Training language models to follow instructions with human feedback," NeurIPS 2022; arXiv:2203.02155v1, Sec. 3.5 "Models", RL paragraph, eq. (2) (E10). Mohamed et al., JMLR 2020, Secs. 4.2-4.3 (E07), Sec. 7.4.3 (E08). Our calculation (E21), checked by gen/p9e_kl_counterexample.py.
<!-- END S106 -->

<!-- BEGIN S104 -->
### 83. A Surrogate Is Not a Hard Constraint [S104]

**Message.** PPO's clipping changes the objective being optimized; it does not force every realized probability ratio to stay in $[1-\epsilon,1+\epsilon]$.

$$\min\big(r\hat A,\ \mathrm{clip}(r,1-\epsilon,1+\epsilon)\hat A\big),\qquad r=\frac{\pi_\theta(a\mid s)}{\pi_{\theta_{\text{old}}}(a\mid s)}.$$

Proximal policy optimization (PPO); $\hat A$ is the estimated advantage of action $a$ in state $s$.

Figure (Schulman et al. 2017, Figure 1, unmodified): two panels plotting one term of $L^{\mathrm{CLIP}}$ against $r$, red dot at $r=1$. Left, $\hat A>0$: the term rises linearly until $r=1+\epsilon$, then is flat. Right, $\hat A<0$: the term is flat for $r<1-\epsilon$, then falls linearly. Where flat, there is no gain from moving $r$ further, but realized $r$ can still leave $[1-\epsilon,1+\epsilon]$; the clipped objective is not the exact IS identity.

Details. Equation (7) of the source:

$$L^{\mathrm{CLIP}}(\theta)=\hat{\mathbb{E}}_t\Big[\min\big(r_t(\theta)\hat A_t,\ \mathrm{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t\big)\Big],$$

with example value $\epsilon=0.2$. The ratio is per action, conditional on the state, against the old policy that collected the batch; it is not the full-sequence weight of slide 78. Clipping is sign-sensitive through the min. Section 4 describes a separate adaptive KL-penalty variant with $\mathrm{KL}[\pi_{\theta_{\text{old}}},\pi_\theta]$, against the old policy rather than a fixed reference. No universal safety claim follows.

Sources. Schulman, Wolski, Dhariwal, Radford, Klimov, "Proximal Policy Optimization Algorithms," arXiv:1707.06347v2 (2017), Sec. 3, eq. (7), Figure 1; Sec. 4, eq. (8) (E09). Figure: unmodified 300-dpi crops of Figure 1, page 3 of v2 (fig/p9e-ppo-fig1-pos.png, fig/p9e-ppo-fig1-neg.png).
<!-- END S104 -->

<!-- BEGIN S109 -->
### 84. One Target, Different Estimators [S109]

(placeholder, INT)
<!-- END S109 -->

<!-- BEGIN S113 -->
### 85. Closer [S113]

(placeholder, INT)
<!-- END S113 -->
