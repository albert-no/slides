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
