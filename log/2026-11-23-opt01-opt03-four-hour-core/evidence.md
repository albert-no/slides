# Evidence register

Append-only. Checked 2026-11-23. Cutoff: 2026-11-23; textbook results, not a recent-literature survey. No generated figure commissioned yet.

## E01 — Existing course and reusable material
- Claim: audience is junior undergraduate AI majors; mathematical/rigorous mode. Baseline opt01 has 119 slides and opt03 has 134. opt01 contains the required SVD/EYM prerequisites. opt03 notes already include a quantitative nonconvex stationarity bound.
- Source/version: repo commit `99cf2a220a92c83e938167c05745af15d9bafe13`; `courses/deepmath/OUTLINE.md`, sections opt01 and opt03; opt01 note §§3–4, 6–7; opt03 note §§6.4–6.5, 7–8.
- Setup: counts include title, contents, dividers and closer; page map in job.md.
- Limits: existing decks/notes are inventory, not independent mathematical authority. In particular do not carry over informal claims that random initialization alone guarantees convergence to a local minimum.
- Label: illustrative example (course inventory, not an external empirical result).

## E02 — SVD foundations and spectral approximation
- Claim: orthogonal changes of coordinates expose singular values; SVD is a sum of rank-one terms; truncation minimizes spectral-norm rank-k error.
- Source/version: Deisenroth, Faisal and Ong, *Mathematics for Machine Learning*, CUP 2020, online draft 2024-01-15. https://mml-book.github.io/book/mml-book.pdf ; §3.1 norms, §4.5 SVD, §4.6 pp129–133, Definition 4.23, Theorems 4.24–4.25. Text verified from the official PDF.
- Setup: real finite matrices, singular values sorted nonincreasingly, k below rank. Spectral norm is maximum Euclidean stretch. For rank at most k the optimum is attained by truncated SVD.
- Limits: theorem gives an optimizer, not uniqueness; not a missing-data completion theorem. Figures 4.11–4.12 are optional illustration sources, not planned data claims.
- Label: published result.

## E03 — EYM in the spectral and Frobenius norms
- Claim: for rank(A)=r, 0<=k<r, A_k attains minimum error over rank(B)<=k. Spectral error is sigma_(k+1); squared Frobenius error is sum_(i>k) sigma_i^2.
- Source/version: Rich Wilkinson, *Multivariate Statistics*, MATH3030, §3.5.1 Propositions 3.10–3.11 and §3.5.2 Theorem 3.1 and spectral proof, live version checked 2026-11-23. https://rich-d-wilkinson.github.io/MATH3030/3-5-lowrank.html
- Setup: fully observed real matrix, unweighted error; the same A_k works for both measures.
- Limits: the source's on-page proof treats the spectral case. Full Frobenius derivation is preserved in baseline opt01 note §7.4 (min-max/Weyl route), to be independently checked in review. Do not present discarded-energy achievability alone as proof of optimality. No uniqueness claim needed. No promise of downstream predictive performance or matrix completion.
- Label: published result.

## E04 — Smooth convex GD
- Claim: for differentiable L-smooth convex f on R^d, with a minimizer x*, fixed step 1/L gives f(x_T)-f* <= L||x_0-x*||^2/(2T), T>=1. This is a sublinear function-gap guarantee.
- Source/version: Garrigos and Gower, *Handbook of Convergence Theorems for (Stochastic) Gradient Methods*, v3, 2024-03-09, §3.1 Theorem 3.4, equations (14)–(16). https://arxiv.org/html/2301.11235v3#S3.SS1
- Setup: Euclidean norm, unconstrained full-gradient descent, L>0, attained optimum.
- Limits: not a geometric rate under mere convexity, not the same as an O(1/T) iterate-distance bound.
- Label: published result.

## E05 — Strong convexity upgrades the rate
- Claim: under additional mu-strong convexity, 0<mu<=L, squared iterate distance contracts by q=1-mu/L at step 1/L. Smoothness bounds function gap by (L/2)||x_T-x*||^2, hence geometric decay to the unique optimum.
- Source/version: Garrigos and Gower v3, §3.2 Theorem 3.6, Remark 3.7 and first-order proof. https://arxiv.org/html/2301.11235v3#S3.SS2
- Setup: same unconstrained smooth GD as E04. For mu=L, one-step conclusion; otherwise 0<q<1.
- Limits: called linear convergence in optimization terminology (geometric/exponential in iteration count). No independent PL assumption or co-coercivity theorem is necessary for the proposed teaching route (E07).
- Label: published result.

## E06 — Nonconvex: stationarity, not local optimality
- Claim: if f is L-smooth and f>=f_low, fixed step 1/L yields min_(0<=t<T)||grad f(x_t)||^2 <= 2L(f(x_0)-f_low)/T. For gradient norm <=epsilon this gives O(epsilon^-2) iterations.
- Source/version: Cornell CS4787/5777 Fall 2026, Lecture 5, sections “Lipschitz continuous gradient assumption (or the L-smoothness assumption)”, “Convergence of GD”, and following question on optimality. https://www.cs.cornell.edu/courses/cs4787/2026fa/lectures/lecture5.html ; checked 2026-11-23.
- Setup: differentiable objective on R^d, full gradients, global smoothness and lower bound. Use exactly T gradients indexed 0 through T-1. Lower-bound formulation follows the telescoping proof; attaining f_low is unnecessary.
- Limits: O(1/T) is for best squared gradient norm, not function error, last gradient, local-minimum error, or convergence of the iterate sequence. No generic local-minimum guarantee. Source's informal “smallest gradient ... 1/T” is rendered explicitly as squared gradient in this job.
- Label: published result; lower-bound formulation is a direct specialization of the displayed proof.

## E07 — One proof route, without co-coercivity or PL
- Claim: use descent, one distance identity, then telescope or contract.
- Sources: E04–E05 and direct algebra below; proposed pedagogical derivation, not an extra assumed theorem.
- Setup: alpha=1/L; g_t=grad f(x_t), D_t=||x_t-x*||^2, Delta_t=f(x_t)-f*. The same equations apply to convex with mu=0 and strongly convex with mu>0.
- Derivation:
  1. Smoothness: f(x_(t+1)) <= f(x_t)-||g_t||^2/(2L).
  2. Tangent/quadratic lower bound: Delta_t <= <g_t,x_t-x*>-(mu/2)D_t.
  3. Distance expansion: (L/2)(D_t-D_(t+1))=<g_t,x_t-x*>-||g_t||^2/(2L).
  4. Combine: Delta_(t+1) <= (L/2)(D_t-D_(t+1))-(mu/2)D_t.
  5. Convex: sum and use decreasing Delta to get E04. Strongly convex: Delta_(t+1)>=0 gives D_(t+1)<=(1-mu/L)D_t; unroll and use smoothness at x* to get E05.
- Limits: do not replace the E05 prefactor (L/2)D_0 by Delta_0 without proving the stronger function-gap contraction. Nonconvex uses only step 1 plus a lower bound, not steps 2–5.
- Label: our calculation.

## E08 — Examples distinguish error metrics and convergence targets
- Claim/setup: A=[[3,0],[4,5]] has A^T A=[[25,20],[20,25]], singular values sqrt(45), sqrt(5), and A_1=[[1.5,1.5],[4.5,4.5]]. Residual squared Frobenius error is 5; retained energy is 45/50=90%. The identical spectral/Frobenius residual here is special to rank-one residual. A separate diagonal example diag(5,3,1) at k=1 gives spectral error 3 and Frobenius error sqrt(10).
- Source: own exact calculation; first example adapted from frozen opt01 note §7.5. Not measured data.
- Claim/setup: baseline GD quadratic f(x)=2*x_1^2+(1/2)*x_2^2 has L=4, mu=1. Step 1/4 sets the first coordinate to zero and multiplies the second by 3/4. Actual function decay after the first step is (9/16)^t up to index shift, not the generic upper-bound factor 3/4.
- Claim/setup: f(x)=1-cos(x) is globally 1-smooth and nonnegative. GD started at x_0=pi stays at a strict local maximum since f'(pi)=0 and f''(pi)=-1. This disproves an unconditional local-minimum guarantee, not a statement about typical initialization.
- Sources: own exact differentiation and arithmetic. No external performance claims.
- Limits: example rates are not worst-case bounds. No diagram has been generated. If rendered as generated figures later, slides must supply a repo regeneration path and these exact inputs; purely schematic drawings must be labelled as such.
- Label: illustrative example / our calculation.

## E09 — Exact arithmetic for the chosen teaching examples
- Claim/setup: vector (3,4) has l1 norm 7, l2 norm 5 and linfinity norm 4. With C=[[1,1],[2,2]], range(C)=span((1,2)), null(C)=span((1,-1)), rank(C)=1.
- Claim/setup: for E08's A, take V=[(1,1),(-1,1)]/sqrt(2), U=[(1,3),(-3,1)]/sqrt(10), Sigma=diag(3sqrt(5),sqrt(5)). Columns are orthonormal, Av_i=sigma_i*u_i, and U Sigma V^T=A. A's eigenvalues are 3 and 5, unlike its singular values.
- Claim/setup: for E08's quadratic, x_0=(2,2), x_1=(0,3/2), x_2=(0,9/8). Function values are 10, 9/8, 81/128; squared distances to zero are 8, 9/4, 81/64. The first contraction differs from later ones; later squared-distance/function-gap ratios are 9/16, bounded above by the generic q=3/4. Euclidean Lipschitz constant of grad f is 4 since ||diag(4,1)z||<=4||z||, equality in the first coordinate; the strong-convexity remainder is 2h_1^2+(1/2)h_2^2 >= (1/2)||h||^2, so mu=1.
- Source: exact direct arithmetic/differentiation, cross-checked with frozen opt01 pp13,17,45–50 and opt03 pp83–84. This is illustration, not a measured dataset.
- Limits: do not confuse A's eigenvalues with the eigenvalues 45 and 5 of A^T A. Do not replace the generic GD upper bound with this example's exact rate.
- Label: our calculation / illustrative example. For new figure generation slides must report code path and parameters; no figure produced in planning.
