# Evidence register

Targeted verification for the November 24 opt01 comments; not a literature survey. Sources checked 2026-11-24. Append-only.

## E01 — Frozen inventory and inherited approval
- Source: repo commit `9fdba016e02405c96fa9d8a9c7224f4612361d16`, opt01 deck/companions, root and Deepmath OUTLINE; parent `log/2026-11-23-opt01-opt03-four-hour-core/review-r3.md` and evidence.md.
- Claim/setup: 68-slide opt01, 150-minute allocation; active opt02 51/90; full-original opt01 archive 119 slides under opt03-backup. Current maximum opt01 ID S123. Existing source map identifies the comment pages unambiguously (job.md).
- Limits: inventory and prior review are not independent mathematical evidence. Reuse already-approved proofs, not the earlier mandate to keep repeated arithmetic that Albert now supersedes.
- Label: illustrative example / repository inventory.

## E02 — Span, orthogonal geometry and SVD construction
- Source: Deisenroth, Faisal and Ong, Mathematics for Machine Learning, CUP 2020, online draft 2024-01-15. https://mml-book.github.io/book/mml-book.pdf . Read official PDF text: §2.7.3 Definition 2.23 and eq. (2.124); §3.4 Definition 3.8 and eqs. (3.29)–(3.32), printed p78; §4.5.1–4.5.2, especially eqs. (4.71)–(4.78), printed pp123–124.
- Claims: range is the set of outputs/column span; square orthogonal maps preserve Euclidean lengths, distances and angles; right singular vectors are orthonormal eigenvectors of A^T A; its positive eigenvalues give squared positive singular values; u_i=A v_i/sigma_i for sigma_i>0.
- Limits: arbitrary p-norms are not rotation-invariant. Completing zero-singular-value directions requires bases, not division by zero. Rectangular matrices do not have an ordinary eigenvalue list. “Eigenvalues differ” must mean generally, not always; symmetric positive-semidefinite matrices can use the same nonnegative spectrum for both (also follows directly from their orthogonal diagonalization).
- Label: published result; positive-semidefinite limiting case is a direct specialization.

## E03 — Approximation and squared energy
- Source: Rich Wilkinson, Multivariate Statistics, MATH3030 §3.5.1 Propositions 3.10–3.11 and §3.5.2 Theorem 3.1. https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html . Read current official course text. Also E02 §4.6 for spectral truncation.
- Claims/setup: fully observed real matrix, unweighted spectral/Frobenius error, sorted singular values; rank-at-most-k truncated SVD achieves spectral error sigma_(k+1) and squared Frobenius error sum_(i>k) sigma_i^2. Total squared Frobenius energy is sum_i sigma_i^2.
- Limits: the page's proof treats only the spectral case. Computing A_k's residual establishes achievability, not the Frobenius lower bound for all competitors. Omit uniqueness claims. The source's “non-examinable” label is its own course policy, not Albert's; use Albert's requested “beyond this lecture's scope,” without inventing exam policy.
- Label: published result.

## E04 — Exact illustrative arithmetic and direct deductions
- Source: direct algebra, with the existing approved illustrations in the baseline opt01 and parent evidence E08/E09; no empirical data.
- Span example: a1=(2,1), a2=(1,2), x=(1,1), hence Ax=a1+a2=(3,3). This is one output, not the entire range.
- Retained S50 example: A=[[3,0],[4,5]]=B+R, B=[[1.5,1.5],[4.5,4.5]], R=[[1.5,-1.5],[-0.5,0.5]]. B and R are orthogonal in the Frobenius inner product; their squared norms are 45 and 5, total 50. These are the SVD rank-one layers, so B retains 90% of squared Frobenius energy. The numbers illustrate reconstruction, not a proof of optimality or real LLM behavior.
- Orthogonal geometry: (Qx)^T(Qy)=x^Ty and ||Q(x-y)||_2=||x-y||_2 when Q^TQ=I; preservation is Euclidean. This need not preserve l1/linfinity (a rotated coordinate vector supplies a counterexample, note-only if useful).
- Energy ratio for nonzero A: R_k=||A_k||_F^2/||A||_F^2=(sum_(i<=k) sigma_i^2)/(sum_i sigma_i^2). Its complement is ||A-A_k||_F^2/||A||_F^2. Choosing the smallest k with R_k>=eta is an energy-budget rule, 0<eta<=1. Not accuracy; “explained variance” needs centered data.
- Two-factor storage: W in R^(m x n), W_k=(U_k Sigma_k)V_k^T=L R, L in R^(m x k), R in R^(k x n). Stored scalar count is k(m+n), versus mn; savings require k(m+n)<mn. Count omits implementation overhead/bias and assumes equal scalar precision. No claim of automatic speedup.
- Removed S122's unique illustration: diag(5,3,1), k=1 leaves residual diag(0,3,1), spectral error 3 and Frobenius error sqrt(10). Preserve this note-only example if not already in the historical archive.
- Label: our calculation / illustrative example. Any regenerated figure must preserve these exact inputs and report its regeneration path; no empirical chart is planned.

## E05 — Brief real LLM weight-compression application
- Venue source, verified author order/year: Xin Wang, Yu Zheng, Zhongwei Wan, Mi Zhang, “SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression,” ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/3104e1ab39875cf54fe1eb4473e7c5a1-Abstract-Conference.html
- Full text read: https://arxiv.org/html/2403.07378v5 , revised 2025-03-16, §2 “SVD for Language Model Compression” and §3/§3.1, eq. (1). Version record: https://arxiv.org/abs/2403.07378v5 . The OpenReview forum returned a browser challenge; the venue proceedings verified the citation instead.
- Claim: SVD-based low-rank approximation is used for post-training LLM weight compression; SVD-LLM is a concrete published example.
- Limits: EYM on W minimizes matrix error, not model quality. The paper considers activation-dependent error ||(W-W')X||_F and uses additional techniques. Do not describe plain truncated SVD as the complete SVD-LLM algorithm or promise preserved accuracy. No performance percentages, model sizes, speedup claims, whitening derivation or fine-tuning tutorial are required here.
- Label: published result (application existence), not a claim that the class theorem certifies downstream accuracy. The proposed factorization/count exhibit is E04's generic algebra, not a redrawing of the paper's algorithm diagram.

## E06 — Modern exposition versus historical attribution, opt02 pp30/41
- Sources: Guillaume Garrigos and Robert M. Gower, Handbook of Convergence Theorems for (Stochastic) Gradient Methods, arXiv:2301.11235v3 (2024), introduction, §3.1 Theorem 3.4, §3.2 Theorem 3.6 / Remark 3.7, §3.4 Bibliographic notes. https://arxiv.org/html/2301.11235v3 . Earlier book metadata: Yurii Nesterov, Introductory Lectures on Convex Optimization: A Basic Course, Springer, 2004. https://link.springer.com/book/10.1007/978-1-4419-8853-9 .
- Claims: G&G supplies the exact smooth-convex and strongly-convex bounds used here at gamma=1/L. It is an exposition of known results, not their original discovery. Its bibliographic notes point to Nesterov (2004) for proofs of both results.
- Limits: Nesterov is an earlier standard reference, not a verified earliest publication. Do not label these “Garrigos–Gower theorems” or claim Nesterov invented GD. Retain G&G for exact constants and Nesterov for the classical treatment; do not import co-coercivity or different step sizes into this lecture.
- Label: published result / bibliographic verification; earliest priority unresolved.

## E07 — Earlier primary textbook draft corroborates classical status
- Source: Yu. Nesterov, Introductory Lectures on Convex Programming, Volume I: Basic course, dated July 2, 1998 on the title page; authored draft mirrored at https://hengshuaiyao.github.io/papers/nesterov03.pdf . Read §2.1.5, printed pp65–67, Theorems 2.1.13 and 2.1.14.
- Claims: this earlier text already presents sublinear smooth-convex and geometric strongly-convex GD convergence. The strongly-convex theorem uses 0<h<=2/(mu+L) and squared-distance factor 1-2h*mu*L/(mu+L).
- Limits: the filename is not the edition date. This is a 1998 draft, not inspected full text of the 2004 published edition. Its theorem numbers/constants must not be copied as an exact citation for the present 1/(2T) convex bound or the simpler q=1-mu/L derivation. Cite the published book at book/chapter level, with G&G supplying the exact formula reference. No earliest-priority conclusion.
- Label: authored primary treatment / bibliographic corroboration.

## E08 — Descent, summability, full gradient convergence and best-iterate rate
- Source for descent and the finite-sum argument: Cornell CS4787/5777 Fall 2026, Lecture 5, “Descent lemma” and “Convergence of GD.” https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html . Source states a minimum value; the weaker lower-bound assumption and limit deduction below are our algebra.
- Setup: differentiable f on R^n with globally L-Lipschitz gradient, L>0; f(x)>=f_low> -infinity; x_(t+1)=x_t-grad f(x_t)/L. For every integer T>=1, sum_(t=0)^(T-1)||grad f(x_t)||^2 <= 2L(f(x_0)-f(x_T)) <= 2L(f(x_0)-f_low).
- Deduction: nonnegative partial sums bounded uniformly in T imply sum_(t>=0)||grad f(x_t)||^2<infinity. Hence the whole sequence of squared gradients, and therefore gradient norms, tends to zero. Elementary justification: infinitely many terms >=epsilon^2 would force divergent partial sums.
- Finite-time bound: minimum over 0<=t<T of squared norms <= their average <= 2L(f(x_0)-f_low)/T. The unsquared best norm is at most the square root. No attained objective minimum required.
- Limits: no last-iterate O(1/T) bound, no convergence of x_t itself, no local/global-minimum guarantee. The rate and asymptotic whole-sequence limit are different statements. Keep finite index ranges consistent; do not inherit a source endpoint typo.
- Label: published descent result plus our explicit deductions, not a new theorem attribution.

## E09 — Elementary upper-model argument and controlled visual builds
- Source: direct completing-the-square identity applied to E08's standard smooth upper bound. With g=grad f(x), Q_x(y)=f(x)+<g,y-x>+(L/2)||y-x||^2 = f(x)-||g||^2/(2L)+(L/2)||y-(x-g/L)||^2. Its minimizer is x-g/L and f there is at most f(x)-||g||^2/(2L).
- Limits: this explains the step given the descent lemma; it does not prove L-Lipschitz gradients imply that lemma. State this boundary; retain the formal implication only as optional note detail. No implicit C2/Hessian assumption and no integral from 0 to 1 in the core narrative.
- Proposed build: existing opt02 S34 curve f(u)=u^2, touch u0=-0.6, admissible L=3; Q(u)=f(u0)+f'(u0)(u-u0)+(3/2)(u-u0)^2. Q-f=(1/2)(u+0.6)^2>=0; Q's minimizer is u0-f'(u0)/3=-0.2. Show symbol labels, not numerical calculations. Parameters are figure provenance only, not a running exercise.
- Regeneration: slides may add `courses/deepmath/opt02-convexity-gd/figs/gd_model_build.py` for this build and update existing `figs/o3b_figs.py` for S65/S110 only. Report actual inputs and paths in work-r1; alternative analytic curves must be verified/documented. No shared scripts.
- S65's generic curvature picture may use a scalar quadratic with curvature strictly between chosen mu and L, but show generic mu/L and give parameters in H2/M2/provenance. S110 may show 1/T versus q^T for an illustrative fixed q in (0,1), independent of the deleted trajectory. Do not present these as data or universal comparison for every T/constant.
- Label: our calculation / illustrative example. Builds are instructor-advanced, readable as static pages and accessible in verbal notes.
