# Evidence map — foundations and calculations

Cutoff: 2026-11-18. The previous job's reviewed mathematical sources remain available in `log/2026-11-17-prob09-major-revision/evidence.md` at baseline5f4b1d9. Entries here identify the new teaching uses and distinguish published facts from our examples. No frontier literature survey is proposed.

## E01 — Baseline and prerequisites

- **Label:** repository evidence.
- Baseline5f4b1d99c5d799785752aa12c494715c3b21327b; target deck has86 pages. Directly inspected all title/ID entries and the requested slide bodies.
- `courses/deepmath/prob02-kl-crossentropy/prob02-kl-crossentropy-note.html`: §4.5 Theorem3 (CE=entropy+KL), §6.6 Theorem7 (one-hot CE=KL), §6.8 expected-loss decomposition. The target branch contains the current course foundation at b20ab73.
- `courses/deepmath/prob07-estimation/prob07-estimation-note.html`: §7 MLE/empirical CE and §§5,8 Bayes/MAP. prob05 supplies sample-mean variance, prob06 concentration and prob08 Gaussian construction, as mapped in the prior job's E01.
- Reuse via brief content-named recalls; no re-proving these results or editing previous decks. Some older note prose describes KL direction loosely: the displayed convention to reuse is D(P||Q), truth/data first, model second.

## E02 — CE/KL is the motivation; MC is the computational step

- **Label:** published identity plus course interpretation.
- Goodfellow, Bengio & Courville, *Deep Learning* (2016), §3.13, eq.(3.51): https://www.deeplearningbook.org/contents/prob.html ; inspected 2026-11-18. Course one-hot specialization: E01, prob02 Theorem7.
- For a fixed model Q_theta, L(theta)=E_P[-ln Q_theta(X)]=H(P)+D(P||Q_theta), with well-defined finite terms. If the target is a one-hot label, H=0 and CE equals KL exactly. Natural log gives nats.
- For IID draws from P, the mean negative log likelihood estimates L(theta). Sampling a minibatch with replacement uniformly from a fixed dataset estimates the empirical average; it is not automatically an unbiased estimate of population risk for a model fitted on those same data. A fixed model/fresh evaluation sample is the clean unbiasedness setup here.
- **Not established:** that an arbitrary CE is literally a KL without its entropy term, that model-generated samples estimate a data-distribution expectation without correction, or that MC is itself an optimization algorithm.

## E03 — Standard error and generic rare events

- **Label:** published sample-mean result; our exact Bernoulli example.
- Owen, *Monte Carlo theory, methods and examples*, Ch.2 §§2.1-2.4, especially finite-variance error and Bernoulli rare-event discussion (printed pp24-25): https://artowen.su.domains/mc/Ch-intro.pdf ; inspected 2026-11-18.
- SE is **standard error**, the standard deviation of the estimator over repeated samples. For IID Y_i=f(X_i) with finite variance, SE(mean)=sigma_f/sqrt(n); estimate by s_Y/sqrt(n), n>=2. It is not the standard deviation of individual outcomes and not this realized run's absolute error.
- Proposed toy: rho=.001, n=1000 Bernoulli draws. Expected hits=1; P(no hits)=.999^1000=.3676954248. A zero-hit run estimates0 rather than.001: absolute error.001 and relative error100%. Absolute RMSE=.000999499875; relative RMSE=.999499875. Ten-percent relative RMSE requires n>=99,900, not a95% confidence guarantee.
- Exact formulas: absolute RMSE=sqrt(rho(1-rho)/n), relative RMSE=sqrt((1-rho)/(n*rho)); on0<rho<=1/2, at fixed n, rarer events lower absolute RMSE and raise relative RMSE. Do not transfer that monotonic statement to individual runs.
- Reproduce with the existing `courses/deepmath/prob09-monte-carlo/gen/p9a_part01.py`, extended by slides for the chosen new example. No stochastic simulation or seed needed. The old exponential example and its separate2,202,547-draw calculation remain later.

## E04 — Contribution, target and optimal proposal

- **Label:** published IS result and existing exact example.
- Owen Ch.9 §9.1, Theorem9.1 and optimal-density discussion, pp4-6: https://artowen.su.domains/mc/Ch-var-is.pdf . Source was checked in the prior job (E04/E11/E24); direct web refetch on2026-11-18 returned403, so no claim of a fresh successful PDF retrieval. The identity and the following calculations were independently rechecked algebraically.
- For X~q, Y=f(X)w(X), w=p/q: Y is one weighted contribution; mu=E_p f=E_q Y is the target, and the estimator is the average of Y. Coverage and integrability are required. A horizontal mu line is the mean under q, not a density, and Y(x) need not equal it pointwise.
- In S118: p=Exp(1), q=Exp(.1), f=1{x>10}. Y(x)=1{x>10}10 exp(-.9x), mu=exp(-10). Both plot objects must be named in words.
- Proposal intuition: minimize the second moment integral f²p²/q by allocating q to |f|p. S57's p=N(0,1), f=x gives a two-lobed |x|phi(x), not a peak at0. The signed fp curve is secondary to this message. |f|p is not itself normalized. With signed f this does not give a constant signed contribution.
- Existing reproducibility: `gen/p9b_calc.py`, `gen/p9b_figs.py`; retain their domain conditions and distinguish exact curves from schematic draw marks.

## E05 — Why zero variance is possible

- **Label:** published optimal-IS consequence; our explanatory construction.
- Same Owen locator as E04; previous job E04/E11. For nonnegative f with0<mu=integral fp<infinity, q*=fp/mu gives f(X)p(X)/q*(X)=mu, q*-almost surely. Every weighted contribution is the same constant, so its variance and the sample-mean variance are0. X itself can remain random. For general one-sign f, q*=|f|p/c gives the same constant mu; sign-changing f generally does not.
- Tail indicator: q* is10+Exp(1). X has variance1, but Y=f(X)w*(X)=exp(-10) identically. One or many such contributions average to the known target exactly.
- **Limit:** the oracle density/weight uses the unknown normalizer mu in general. This is a benchmark showing what variance means, not a practical universal method for discovering an unknown expectation from one draw. S64 supplies that limitation and must remain adjacent.
- Proposed exhibit: different schematic X values all mapped to the same Y. Use fixed labelled values, explicitly illustrative; formula/figure reproducible in `gen/p9b_figs.py` if built.

## E06 — Heavier tails are not the universal criterion

- **Label:** our exact calculation using the IS second-moment theorem.
- Target p=Exp(1), integrand f=x, proposal q_lambda=Exp(lambda), lambda>0. Coverage holds for every lambda. Weighted second moment = (1/lambda) integral_0^infinity x² exp(-(2-lambda)x) dx =2/[lambda(2-lambda)^3] for0<lambda<2; it is infinite forlambda>=2. mu=1, so variance is this minus1.
- Checks: lambda=.5 gives5/27=.185185; lambda=1 gives1; lambda=1.5 gives29/3=9.666667 (lighter than p, yet finite); lambda=2 givesinfinity. An excessively heavy proposal lambda=.1 has variance1.915877, worse than ordinary MC. Thus heavier can help here, is not necessary for finite variance, and does not by itself guarantee low variance.
- General criterion: q covers fp for validity and integral f²p²/q<infinity for finite variance. It depends on f as well as p and q. No blanket tail-order rule for all integrands follows.
- Inputs and computation: extend existing `gen/p9b_calc.py`/`gen/p9b_figs.py` if these numbers/curves are used. Exact formulas, no random seed. Sources: E04 and prior job E18.

## E07 — A concrete unknown-Z posterior

- **Label:** Bayesian framework is published; proposed logistic-normal toy and arithmetic are our example, not a published experiment.
- Stan User's Guide (page identifies v2.40), “How Stan Works”, “Target log density”: https://mc-stan.org/docs/stan-users-guide/how-stan-works.html ; “Regression Models”, “Logistic and probit regression”: https://mc-stan.org/docs/stan-users-guide/regression.html . Inspected2026-11-18. These support posterior proportionality and logistic/Bernoulli likelihoods, not a claim that Stan's sampler is ordinary IS.
- Let theta~N(0,1), and conditional on theta observe two independent successes y1=y2=1 with Pr(y=1|theta)=s(theta)=1/(1+exp(-theta)). Known prior density phi and likelihood s² give unnormalized posterior tilde p(theta)=phi(theta)s(theta)². Z=integral phi(t)s(t)²dt is positive and finite but not needed by the estimator.
- Target: posterior predictive probability of another success, mu=E_post[s(theta)]. Proposal q=phi is sampleable and covers the target; unnormalized weight tilde p/q=s². SNIS estimate=sum s(theta_i)^3 / sum s(theta_i)^2 for IID theta_i~N(0,1). All weights are positive, bounded; the proper target and bounded integrand give the usual consistency assumptions.
- Optional validation only: deterministic Simpson integration on[-12,12] with12,000 and24,000 panels agrees to about14 digits: Z=.29337903585809, numerator=.19006855378714, mu=.64786003959422. A numerical reference is not an input to SNIS. Do not claim Z is mathematically unknowable or that quadrature cannot solve this intentionally small example. No elementary-closed-form impossibility claim is needed.
- Reproducibility if adopted: slides adds `courses/deepmath/prob09-monte-carlo/gen/p9f_unknown_z.py` (planned, not yet created), with the model, quadrature limits/panel counts and any illustrative evaluation points stated. Any displayed random batch requires a recorded seed; a deterministic example must say it is illustrative. No MCMC tutorial.

## E08 — Preserve the RL application without the gradient chapter

- **Label:** established IS identity and existing published application sources.
- Existing S100-S105/S129: logged responses under behavior pi_b, target pi_theta, exact correction w=pi_theta/pi_b subject to coverage/integrability. Fixed theta during evaluation; response ratios factor by the chain rule without token independence. Product-second-moment toy needs independent weight factors under behavior, as already qualified.
- Existing S106: Ouyang et al., *Training language models to follow instructions with human feedback*, arXiv:2203.02155v1 §3.5 eq.(2), https://arxiv.org/abs/2203.02155 ; the source/version locator was corrected and verified in prior job E22. The simplified fixed-prompt reward-plus-KL objective remains illustrative; PPO-ptx's pretraining term is omitted and labelled.
- Existing S104: Schulman et al., *Proximal Policy Optimization Algorithms*, arXiv:1707.06347v2 §3 eq.(7), Fig.1, https://arxiv.org/abs/1707.06347 . Prior job E09 verifies the unchanged figure crop and the distinction between clipping the surrogate and imposing a hard constraint on realized ratios.
- Remove score-function/pathwise derivations and their summary. Explain the retained objective as an expectation one must estimate; do not imply ordinary IS alone is a complete RL optimizer. Advantage on the PPO figure needs a brief meaning (“better/worse than expected in that state”), not a reinstated baseline proof. No new method claims or latest-system examples.

## E09 — Conditional classification version of the motivation

- **Label:** specialization of E01/E02 by conditioning; our teaching formulation.
- At a fixed labelled input (x,y), CE(delta_y, q_theta(.|x)) = D(delta_y || q_theta(.|x)) = -log q_theta(y|x), provided the model gives the observed label positive probability. This is the exact one-hot statement from prob02, not the claim that every cross-entropy equals KL.
- With a fixed classifier and IID labelled evaluation data from P_data, L(theta)=E[-log q_theta(Y|X)] is estimated by the sample mean of these per-example losses, under the usual integrability condition. If displaying the general decomposition, it is H_P(Y|X)+E_X D(P(.|X)||q_theta(.|X)), assuming finite terms. Do not identify this with an unqualified KL between a joint data distribution and a conditional model.
- On the slides, use the one-hot identity and the expected-loss-to-average step; leave the general decomposition and fixed-model/held-out-data qualification explanation in the notes, with a short fixed-model condition on the main slide. This avoids making three different probability spaces look interchangeable.

## E10 — Concrete generator-evaluation motivation

- **Label:** illustrative application of expectation/MC, not a reported experiment or benchmark.
- Fix one prompt and a generative model p. Let A be outputs passing a specified deterministic format check, and f(x)=1{x in A}. Then mu=Pr_p(X in A)=E_p f(X), estimated by the average pass indicator over IID model draws. Independent random sampling, a fixed model and a fixed checker are the setup; a deterministic decoder does not by itself supply IID draws from that model distribution.
- Source: the expectation identity/MC sampling result E03 and the current baseline S04's fixed-prompt generator example. No generated data or external performance number is proposed. The format-check rate is only the chosen evaluation criterion, not a comprehensive model-quality score.
- Exhibit: original sampler → fixed check → pass-rate expectation schematic, not an empirical plot. No new figure generator is needed unless slides elects to display numerical samples, in which case its deterministic inputs or random seed must be recorded.

## E11 — Reviewed implementation and reproducibility, round1

- **Label:** repository evidence and independently rerun calculations; not new empirical research.
- Candidate `6cf17f6ccb63bb3622267bf0993e67e2068867a8` (integration/content `4eceaf9`) contains70 slides with matching70 HTML-note and70 ASCII-Markdown sections, in identical ID order. Baseline `5f4b1d99c5d799785752aa12c494715c3b21327b` had86. All23 requested/dependent retirements and three parent splits are accounted for; newIDsS130–S133.
- All seven remaining Python generators were rerun in a disposable archive of the exact candidate: `p9a_part01.py`, `p9b_calc.py`, `p9b_figs.py`, `p9c_snis_examples.py`, `p9e_compounding.py`, `p9e_kl_counterexample.py`, `p9f_unknown_z.py`, under `courses/deepmath/prob09-monte-carlo/gen/`. All exited0 and every generated figure remained byte-identical.
- P1 exact Bernoulli inputs rho=.001,n=1000 reproduce P(nohit)=.3676954248, relative RMSE=.999499875 and99,900 draws for10%relative RMSE. The existing per-draw spread plot is now `fig/p9a-rare-sd.svg` in the note, with the two unequal rho=.5 endpoints correctly described.
- P2 exact curves/checks reproduce contribution10exp(-.9x) above10; oracle schematic locations10.3,11.2,12.7,15.0 all giveY=exp(-10); variance5/27 and29/3 for rates.5 and1.5. `p9b-identical.svg` uses schematic locations, not random draws; `p9b-var.svg` shows exact variance magnitudes. Weight-magnitude and integrand distinctions are retained.
- P3 implemented the planned model exactly. Simpson[-12,12] at12,000/24,000 panels reproduces Z=.29337903585809, numerator=.19006855378714 and predictive mu=.64786003959422; panel-doubling differences are below1e-14. The additional illustrative batch uses Python `random.Random(20261118).gauss`, n=10,000, producing SNIS estimate.6480 and ESS6529. Quadrature is validation only, never an SNIS input. `fig/p9f-bayes.svg` reproduces exactly; prior/product peaks are.399/.139 on the plotted grid. No inference of an error bar from the single batch.
- Limits: exact regeneration validates arithmetic/provenance, not all teaching wording. Review-r1 identifies two short-message precision issues despite correct displayed formulas. Retained source claims were checked against this and the prior verified evidence registers; no claim of a newly successful fetch of OwenCh9.
