# Albert's feedback — 2026-11-18, #claw-slides-review

Verbatim bullets from message34. Pages refer to the 86-slide PR #77 baseline5f4b1d9. Append subsequent instructions; do not edit these entries.

## C01
• I think the motivations of MC are needed. something like “ce loss is indeed KL divergence” or in generative models etc

## C02
• Define SE in page 10

## C03
• Drop page 13-14

## C04
• Page 15 need more detail (add slides if needed)

## C05
• Page 27, what is fw and mu in diagram?

## C06
• Need better slide structure of page 33. It is hard to read. Emphasize the message

## C07
• Page 37, what do you mean by zero variance? How can it be possible?

## C08
• Page 42, what is the message? Q needs to have heavier tail?

## C09
• I want example of unknown Z case (before or after page 44)

## C10
• Page 48, use IID or iid (not Iid)

## C11
• We can drop section 5, I think this is too much

## C12
• I think section 6 is good. I like importance sampling in RL context is interesting.

## Resolution of interactions

- C11 removes baseline Part05 (pp55-74), not the current Part06 application. C12 keeps that RL section, renumbered as Part05, without a prerequisite gradient-estimation tutorial.
- Remove the gradient recap S109b and gradient promises in the title, Contents, notes and outline. Rewrite S106's toolkit line and associated notes to concern estimating the objective/reusing samples, not score-gradient derivations. Keep the scoped historical RLHF/PPO context and its limits.
- C03 is a genuine deletion, not relocation of two slide-equivalent detours into the new motivation. C11 is likewise not a request for a hidden 20-slide gradient tutorial in the companion notes. Removed material remains recoverable in git.
- C01 is compatible with prob02: one-hot CE loss equals KL exactly; general population cross-entropy equals entropy plus forward KL. The MC lesson is the replacement of an expectation by a sample average, not a reproof of CE/KL.
- C04 may expand into a few simple steps; use a generic rare-event toy before the retained exponential case, rather than repeating its exact numbers in advance.
- C07 concerns the variance of weighted contributions/the estimator, not the variance of sampled X. C08 does not authorize the false blanket rule that q must be heavier-tailed than p.

## C13 — 2026-11-18, message36, response to the stages1–3 proposal

can be shorter. You do not need to worry about pacing

### Decision

Proceed with the proposed MC/IS-focused revision and existing PR77 continuation. Albert explicitly removes the duration constraint: neither120 nor150minutes is a target to fill, and a shorter deck is acceptable. No further pacing approval is needed. This does not remove required explanations, mathematical conditions or default-type readability. No merge order.
