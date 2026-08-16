# privacy/lectures/05-unlearning/ — Machine unlearning

Two-part lecture on machine unlearning, split at the LLM boundary. **Part I** (`unlearning1-foundations.html`) — definitions, certified deletion (full derivation with proofs), and classical/classification unlearning + metrics. **Part II** (`unlearning2-llm.html`) — LLM unlearning methods and benchmarks/failures. Theory covered: three nested definitions, Newton-step certified deletion (Theorem 1 with two proved lemmas), Gaussian certification (Theorem 2), Sekhari capacity (Theorem 3), SISA cost model (Proposition 3), the certification-caps-every-metric bound (Proposition 4), GA collapse, NPO bounded-loss, plus the full classification + LLM + benchmark + lab thread. Source: `privacy/slide.pdf` and `privacy/privacy.md` reference table.

The folder's `hw4sol.pdf` is the 5-problem homework (P1 Neyman–Pearson, P2 DP⇒MIA, P3 Yeom gap, P4 influence unlearning, P5 certified Gaussian). Its hints/roadmaps are taught **inside the Part I slides** with **no "Homework 4 / Problem N" labels** (2026-06 decision, preserved): the influence→Newton→certification block is the P4/P5 walk-through, and the MIA recall/Proposition-4 block carries P1–P3. (Do not edit `hw4sol.pdf`; the hints live in the deck.)

## Files

| Deck | Topic |
|---|---|
| `unlearning1-foundations.html` | **Part I** (104 slides) — motivation · three definitions · certified/Newton (proved) · SISA · classification algorithms · metrics-as-hypothesis-test |
| `unlearning2-llm.html` | **Part II** (29 slides) — LLM methods · benchmarks · failures · lab |

---

## unlearning1-foundations.html (Part I — before LLMs) — 104 slides

| Part | Topic | Slide | Line |
|---|---|---|---|
| | Title · Contents — Part I | 1–2 | `:51`, `:62` |
| **01** — Motivation, definition | RTBF, three definitions, relations, assumptions, influence→Newton (proved), Gaussian certification, Sekhari capacity, SISA | 3–66 | `:95-1150` |
| | §01 divider | 3 | `:95` |
| | The Central Question | 4 | `:103` |
| | Why This Became Urgent (lawsuits / GDPR Art. 17 / Carlini·Cooper cite) | 5 | `:119` |
| | Three Definitions That Do Not Work | 6 | `:141` |
| | Roadmap — Section 01 | 7 | `:155` |
| | The Gold Standard: Retrain From Scratch | 8 | `:174` |
| | **Definition 1 — Data Deletion Operation** (Ginart 2019) | 9 | `:190` |
| | Deletion as a Commuting Diagram (SVG) | 10 | `:202` |
| | **Definition 2 — Exact Unlearning** | 11 | `:240` |
| | **Definition 3 — $(\varepsilon,\delta)$-Certified Unlearning** | 12 | `:255` |
| | How the Three Definitions Sit (nested-sets SVG) | 13 | `:269` |
| | **Proposition 1 — exact ⟹ certified** (+ proof) | 14 | `:291` |
| | **Proposition 2 — DP gives certification for free** (+ proof) | 15 | `:305` |
| | Counterexample — certified and useless | 16 | `:319` |
| | What a Certificate Does and Does Not Buy | 17 | `:334` |
| | Certified Unlearning Is **Not** Differential Privacy | 18 | `:357` |
| | Corollary — certification needs a utility partner | 19 | `:378` |
| | Standing Convention · the $1/n$ vs $1/(n-1)$ choice | 20–21 | `:394`, `:409` |
| | Assumptions A1–A3 · what $\lambda$-strong convexity buys | 22–23 | `:426`, `:441` |
| | Newton derivation — LOO target, continuous path $L_t$, IFT, term-by-term, sign | 24–28 | `:459-537` |
| | Influence Unlearning: the update · read as Newton's method | 29–30 | `:538`, `:553` |
| | **Theorem 1 — one Newton step suffices**, residual $MG^2/(2\lambda^3n^2)$ (Guo 2020) | 31 | `:568` |
| | Proof of Theorem 1 — outline · **Lemma 1** · **Lemma 2** (2-slide proof) · combining | 32–37 | `:583-672` |
| | The Picture in Parameter Space (SVG) · which Hessian · never form $H^{-1}$ | 38–40 | `:673`, `:700`, `:714` |
| | **Lemma 3 — $\ell_2$ sensitivity $\le 2G/(\lambda n)$** (+ proof) · reading it · why over pairs | 41–43 | `:727`, `:742`, `:763` |
| | Recall — the Gaussian mechanism | 44 | `:778` |
| | **Theorem 2 — certified deletion by output noise** (+ proof) | 45 | `:792` |
| | What Guo et al. *actually* prove (objective perturbation) | 46 | `:806` |
| | The punchline $1/n^2$ vs $1/n$ · noise-vs-$n$ log-log (SVG) · why not just DP | 47–49 | `:819`, `:836`, `:858` |
| | Deletions arrive in a sequence | 50 | `:879` |
| | **Theorem 3 — deletion capacity** (Sekhari 2021, Thm. 2) · where it comes from · proof sketch · budget SVG · separation from DP | 51–55 | `:894-979` |
| | When Influence Functions Fail (Basu 2021) · can certification reach deep nets | 56–57 | `:980`, `:994` |
| | The other route: change how you train · Shards and Slices (SVG) | 58–59 | `:1010`, `:1027` |
| | **Proposition 3 — the SISA cost model** (+ 3-slide proof) | 60–63 | `:1055-1107` |
| | Reading the cost model · what sharding really costs | 64–65 | `:1108`, `:1123` |
| | Section 01 — what we proved | 66 | `:1137` |
| **02** — Classification algorithms | catalog, geometries, SCRUB, SalUn, $\ell_1$, RURK, verification | 67–81 | `:1151-1393` |
| | §02 divider · what breaks outside convexity | 67–68 | `:1151`, `:1159` |
| | Catalog — retraining-style · structured (tables, "certified?" column) | 69–70 | `:1180`, `:1194` |
| | FT, GA, RL — three geometries · FF and IU — one-shot moves | 71–72 | `:1208`, `:1222` |
| | **SCRUB** — two signs · why it does not blow up | 73–74 | `:1238`, `:1255` |
| | **SalUn** — saliency mask · reading the mask (SVG) | 75–76 | `:1272`, `:1287` |
| | **$\ell_1$-sparse** · why sparsity would help | 77–78 | `:1313`, `:1326` |
| | Residual knowledge under perturbation · **RURK** | 79–80 | `:1342`, `:1358` |
| | The Verification Problem (bridge into §03) | 81 | `:1372` |
| **03** — Classification metrics | metric-as-test, MIA recall, Proposition 4, converse, two-sided, IDI, COLA, benchmark | 82–104 | `:1394-1760` |
| | §03 divider · an unlearning metric is a hypothesis test | 82–83 | `:1394`, `:1402` |
| | The chain every metric follows (SVG) · the standard suite | 84–85 | `:1419`, `:1449` |
| | MIA as an unlearning probe | 86 | `:1466` |
| | **Recall — three facts about membership tests** (NP optimal test, Yeom $\Delta/B$ floor, DP cap) | 87 | `:1481` |
| | **Proposition 4 — certification caps every metric** (+ proof) · corollary: a passing score is not evidence | 88–90 | `:1494`, `:1506`, `:1518` |
| | The converse fails — head distillation (table) | 91 | `:1532` |
| | The test is two-sided · both sides of the target (SVG) | 92–93 | `:1547`, `:1568` |
| | **IDI** (lab, AAAI 2026) · reading the index · what it sees that outputs do not (table) | 94–96 | `:1601`, `:1617`, `:1632` |
| | Over-unlearning is not hypothetical | 97 | `:1649` |
| | **COLA** — collapse + align (lab) · COLA in numbers | 98–99 | `:1665`, `:1678` |
| | SalUn benchmark table (CIFAR-10 / ResNet-18, 10% random) · reading it correctly | 100–101 | `:1692`, `:1707` |
| | What a defensible evaluation looks like | 102 | `:1722` |
| | Takeaways — Part I · closer → Part II | 103–104 | `:1735`, `:1748` |

## unlearning2-llm.html (Part II — LLM unlearning)

| Part | Topic | Line |
|---|---|---|
| | Title (`for an LLM to Forget?`) · Contents | `:28`, `:39` |
| **01** — LLM unlearning | GA collapse, NPO, SimNPO, ME+GD, IDK, ELM, LUNAR | `:63-241` |
| | Why LLMs are different | `:72` |
| | **GA / Knowledge Unlearning** | `:87` |
| | **Why GA collapses** — gradient blow-up | `:103` |
| | **NPO** (DPO-style negative branch) | `:118` |
| | **NPO bounded loss** — sigmoid saturation | `:134` |
| | **SimNPO** (reference-free, length-normalized) | `:150` |
| | **ME+GD** (uniform KL) | `:166` |
| | Who's Harry Potter (Eldan) | `:181` |
| | TOFU IDK refusal | `:197` |
| | ELM concept erasure (main-figure image `ELM.png`) | `:214` |
| | LUNAR activation redirection (consolidated math) | `:227` |
| **02** — Benchmarks and failures | TOFU/WMDP/RWKU/MUSE, position, lab | `:241-431` |
| | TOFU (main-figure image `tofu.png`) | `:250` |
| | WMDP (main-figure image `WMDP.png`) | `:264` |
| | RWKU (main-figure image `RWKU.png`) | `:277` |
| | MUSE six-way (main-figure image `MUSE.png`) | `:290` |
| | Benign relearning (Hu) | `:303` |
| | Syntactic relearning (lab) | `:316` |
| | Cooper "doesn't do what you think" — 5 mismatches (each glossed) | `:329` |
| | Are we making progress? (Triantafillou 2024 NeurIPS competition) | `:346` |
| | Position (lab) — term overused (Yoon, Jun, No; ICML 2026) | `:362` |
| | DUSK — shared knowledge (lab, main-figure image `DUSK.png`, ACL 2026 Findings) | `:382` |
| | R-TOFU — reasoning models (lab, main-figure image `r-tofu.png`) | `:393` |
| | Random thoughts | `:406` |
| | Takeaways | `:420` |

**Key formulas (Part I):** Certified $(\varepsilon,\delta)$ two-sided inequality `1:260-263`; leave-one-out target `1:402`; continuous path $L_t$ `1:481`; influence via IFT, $\theta'(0)=\tfrac1n H^{-1}\nabla\ell$ `1:517`; the plus sign, explained `1:527`; influence-unlearning update `1:543`; same update as a Newton step `1:563`; Theorem 1 residual $MG^2/(2\lambda^3n^2)$ `1:573`; Newton error identity (Lemma 2) `1:632`; Hessian-choice discrepancy $G\kappa/(\lambda^2n^2)$ `1:707`; $\ell_2$-sensitivity $2G/(\lambda n)$ `1:731`; recall Gaussian mechanism `1:783`; certified $\sigma \ge \eta\sqrt{2\ln(1.25/\delta)}/\varepsilon$ `1:800`; unlearning noise $\propto 1/n^2$ `1:826`; Sekhari deletion capacity `1:900`; SISA cost $n(R+1)(2R+1)/(6SR)$ `1:1103`; SCRUB KL `1:1241`; SalUn mask `1:1277-1280`; $\ell_1$-sparse `1:1318`; RURK `1:1363`; Proposition 4 TV cap `1:1500`; IDI `1:1606`.

**Key figures (Part I, all inline `u1-` SVG; no bitmap figures):** commuting diagram `1:202`; three definitions as nested sets `1:269`; LOO path + Newton step + residual gap `1:673`; noise-vs-$n$ log-log ($1/n^2$ against $1/n$) `1:836`; deletion capacity as a consumed budget `1:938`; SISA shard/slice grid `1:1027`; SalUn mask `1:1287`; metrics-as-test-statistics chain `1:1419`; two-sided target number line `1:1568`. Five `<!-- TODO real figure: … -->` markers sit above the SCRUB, SalUn, RURK, IDI and COLA slides — source PDFs were not available offline; the two lab ones need Albert's copies.

**Key formulas (Part II):** GA gradient blow-up `2:107`; NPO `2:121`; NPO bounded gradient `2:138`; SimNPO `2:154`; ME+GD `2:172`; LUNAR redirection (aligned) `2:235`.

**Key theorems (Part I — every one stated *and* proved on slides):**

| Result | Statement | Proof |
|---|---|---|
| Definition 1 — deletion operation (Ginart 2019) | `1:190` | — |
| Definition 2 — exact unlearning | `1:240` | — |
| Definition 3 — $(\varepsilon,\delta)$-certified | `1:255` | — |
| Proposition 1 — exact ⟹ certified | `1:291` | same slide |
| Proposition 2 — DP ⟹ certified (identity map) | `1:305` | same slide; counterexample `1:319` |
| **Theorem 1** — one Newton step, residual $MG^2/(2\lambda^3n^2)$ (Guo 2020) | `1:568` | `1:583-672` (outline, Lemma 1, Lemma 2 ×2, combine) |
| Lemma 1 — $\lVert\theta_o-\theta_{-z}\rVert \le G/(\lambda n)$ | `1:598` | same slide |
| Lemma 2 — Newton squares the error, $(M/2\lambda)\lVert e\rVert^2$ | `1:613` | `1:627`, `1:642` |
| Lemma 3 — $\ell_2$ sensitivity $\le 2G/(\lambda n)$ | `1:727` | same slide |
| **Theorem 2** — certified deletion by output noise | `1:792` | same slide; honesty note `1:806` |
| **Theorem 3** — deletion capacity (Sekhari 2021, Thm. 2) | `1:894` | sketch `1:922`; DP separation `1:962` |
| **Proposition 3** — SISA expected cost model | `1:1055` | `1:1068`, `1:1083`, `1:1094` |
| **Proposition 4** — certification caps every bounded metric | `1:1494` | `1:1506`; corollary `1:1518` |
| NPO bounded-divergence (Part II) | `2:142` | — |

**Homework-4 in-deck (woven, not labeled):** the influence→Newton→certification block `1:459-818` is the long-form walkthrough of the influence-unlearning (P4) and certified-Gaussian (P5) problems; the MIA problems (P1 Neyman–Pearson optimal test, P2 DP⇒MIA cap, P3 Yeom gap floor) live on the recall card **"Recall — Three Facts About Membership Tests"** `1:1481` and the Proposition-4 block that follows. No "Homework 4 / Problem N" labels appear on slides — the outline flows inside the lecture content.

**Lab papers cited:** IDI/COLA — Jeon, Jeung, Kim, No, Choi, *An Information Theoretic Evaluation Metric for Strong Unlearning*, AAAI 2026 (Part I `1:1601`, `1:1665`); R-TOFU (EMNLP 2025, main-figure image); DUSK (ACL 2026 Findings, main-figure image); syntactic relearning (ICLR 2026); position paper (Yoon, Jun, No; ICML 2026) — all Part II. (SEPS slide dropped 2026-06.)

**Companion note — `unlearning1-notes.html`** (non-standard plural filename; do **not** rename). 46 entries covering all 104 slides, each badged with the slide or slide range it serves. Structure: `.toc` two-column index with slide-range badges, then one `.slide-note` block per teaching beat (`.snum` / `.stag` / `.timing` / `<h3>`, body of `.say` spoken lines, `.board` derivations, `.ask` anticipated questions, `.key` highlights, `.sec-label` on the three section dividers). Total spoken budget ≈ 110 min. Board-work entries worth knowing about: the $1/n$ vs $1/(n-1)$ identity; assumptions A1–A3 and the two jobs of strong convexity; the Lemma-2 integral identity; the Guo objective-perturbation caveat; the Sekhari risk decomposition; the SISA double sum; the Proposition-4 signed-measure proof.

**Audit history.** 2026-05 visual audit: split Newton-Step theorem 1→2 slides; consolidated LUNAR math. 2026-06 revision: every `.cite` shortened to one rendered line; "Why Now" GDPR **Art. 17** confirmed + lawsuits one-per-line + Carlini·Cooper cite; Newton block expanded 2→8 slides; **fixed sign error** on influence-function slide ($+\tfrac1n H^{-1}\nabla\ell$). 2026-06 split: single 63-slide `unlearning.html` retired and split into Part I (`unlearning1-foundations.html`) and Part II (`unlearning2-llm.html`); Part II sections renumbered 01/02. 2026-06 reorder: moved the influence-function slide from §02 up to lead into the Newton block (so the Newton step no longer feels sudden); folded the homework hints into the natural flow (removed the explicit "Homework 4" roadmap slides; the MIA problems became "MIA: Optimal Test and Its Limits"). Part I now 36 slides, Part II 32. 2026-06 benchmark figures: embedded each benchmark's **actual main-figure image** — `tofu.png` (pretrained→finetuned→unlearned pipeline), `WMDP.png` (bio/chem/cyber three-domain pie, 3,668 Q), `RWKU.png` (forget/neighbor/MIA/utility framework), `MUSE.png` (six-way data-owner/deployer grid), `DUSK.png` (forget-all vs forget-unique Venn partitions) — figure dominant + one-line caption (`cite cite-left` added locally); glossed each of Cooper's 5 mismatches; sharpened the Triantafillou "progress" takeaway; **removed the Pawelczyk verification-hardness slide**; venues updated — DUSK → ACL 2026 Findings, position paper → ICML 2026 accepted (Position Track) with an "Accepted · ICML 2026" pill. Part II now 31 slides. (Image PNGs live alongside the deck; `bundle.py` base64-inlines them for the standalone build.) 2026-06 trim: **removed the Guardrail/ECO slide**; replaced ELM's bullet explanation with its main-figure image (`elm.png`). Part II now 30 slides. 2026-06 trim 2: **removed the SEPS slide**; added R-TOFU main-figure image (`r-tofu.png`); on the position slide removed the "Accepted · ICML 2026" pill, corrected authors to **Yoon, Jun, No**, and tightened the proposal wording. Part II now 29 slides.

**2026-08 math-detail revision (Part I only; Part II untouched).** Part I **36 → 104 slides**, `unlearning1-notes.html` **36 → 46 entries**. Added: three numbered definitions with a nested-set figure; Propositions 1–2 with proofs, a certified-and-useless counterexample, and an explicit "certified ≠ DP" slide; a standing-convention slide and the $1/n$ vs $1/(n-1)$ note; assumptions A1–A3 stated before use; the influence derivation carried through the IFT term by term with the sign explained; Theorem 1 proved in full via Lemma 1 and a two-slide Lemma 2 (Newton error identity, curvature-gap bound); the which-Hessian discrepancy and a "you never form $H^{-1}$" (CG / LiSSA) slide; Lemma 3 proved; Theorem 2 proved by reduction to the Gaussian mechanism, with a separate slide on what Guo et al. *actually* prove (objective perturbation, not output noise); Theorem 3 restated in the paper's correct form with a proof sketch, a budget figure and the DP separation; an honest "when influence functions fail" pair (Basu 2021); SISA made quantitative by Proposition 3 with a three-slide proof; §02 given per-method geometry and a "certified? no" column plus a verification-problem bridge; §03 reframed so that every metric is a **test statistic** for $H_0:\theta_u \sim \mathcal{A}(\mathcal{D}_r)$, with Proposition 4 (certification caps every bounded metric) proved, its vacuity corollary, the head-distillation converse, and the two-sided target made explicit. **Corrections made during the audit** (all previously on slides or in the notes): fabricated SalUn benchmark row `2.85/99.62/93.93/14.39/1.15` → the paper's `1.55/99.88/93.93/13.28/1.13`; Sekhari capacity mis-stated as linear in $\varepsilon$ with $\sqrt d$ → $c\,n\sqrt{\varepsilon}/(d\log(1/\delta))^{1/4}$; Guo certification mis-attributed to output perturbation; COLA's two stages described wrongly on both counts; IDI citation had wrong authors/title/venue; RURK citation wrong; an unverifiable IDI baseline value $-0.110$ removed (the verified pair is $-0.349$ / $-0.060$). The old "MIA: Optimal Test and Its Limits" slide became a recall card plus Proposition 4. Verified by full 104-page headless-Chrome render at `-r 60`; nine layout defects found and fixed (one slide split, one unfilled Bézier, six label-overlap groups, one clipped label).

---

## Cross-references

- **Homework `hw4sol.pdf`** (5-problem) is taught from the Part I slides, woven in without "Homework 4 / Problem N" labels: the influence→Newton→certification block `unlearning1-foundations.html:459-818` is the long-form walkthrough of the influence-unlearning + certified-Gaussian problems, and the MIA problems (NP optimal test, DP⇒MIA cap, Yeom gap floor) live on the recall card `1:1481` and Proposition 4 `1:1494`. The deck holds the hints; the PDF is left untouched (do not edit it).
- **Memorization** is the motivating signal — lawsuits in `privacy/lectures/03-memorization/memorization-diffusion.html:140`, Cooper's framing in `privacy/lectures/03-memorization/memorization-llm.html:384`. Both reused on Part I "Why This Became Urgent" `1:119`.
- **MIA-Efficacy** as evaluation reuses the threshold attacks defined in `privacy/lectures/04-mia/mia1-foundations.html` and the LiRA-style calibration from `privacy/lectures/04-mia/mia4-modern.html`. Part I does **not** restate that theory: slide `1:1481` is a recall card only, and the new content is Proposition 4 `1:1494` — the cap those results imply for *unlearning* metrics.
- **DP** as the parent of certified unlearning — see `privacy/lectures/01-dp/dp8-fl.html:375` (or the $(\varepsilon,\delta)$-DP definition in `privacy/lectures/01-dp/dp4-approximate-dp.html:81`). Theorem 2 `1:792` reduces to the Gaussian mechanism recalled at `1:778`; the "certified ≠ DP" slide `1:357` and the capacity separation `1:962` mark the boundary in the other direction.
- **Influence function** also referenced beyond IU — Sekhari capacity follows from the same first-order analysis.
- **Diffusion-LLM watermarking (dgMARK)** is a sibling lab thread — see `talks/kics260521dllm/kics260521dllm.html:707`. Watermark deck `privacy/lectures/06-watermark/watermark.html` is the broader context.
