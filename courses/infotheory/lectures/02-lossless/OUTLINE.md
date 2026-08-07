# infotheory/lectures/02-lossless/ — Lossless compression (3 lectures)

Three-lecture series. Variable-length codes, AEP and Shannon source coding, Markov sources and universal compression. Paired with `-note.html` companions.

## Files

| Deck | Note | Topic |
|---|---|---|
| `lossless1-codes.html` | `lossless1-codes-note.html` | Variable-length codes, Kraft, Shannon, Huffman |
| `lossless2-aep-arithmetic.html` | `lossless2-aep-arithmetic-note.html` | AEP, source coding theorem, arithmetic coding |
| `lossless3-markov-universal.html` | `lossless3-markov-universal-note.html` | Markov, entropy rate, LZ78, universal coding |

---

## lossless1-codes.html — Codes, Kraft, Huffman

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:25, :36` |
| **01 — Codes & rate** | UD, prefix-free, trees | `:64-154` |
| | Setup | `:71` |
| | Expected rate | `:79` |
| | Example — UD code | `:91` |
| | Example — non-UD code | `:99` |
| | Why prefix-free? (motivation) | `:107` |
| | Prefix-free codes as trees | `:122` |
| **02 — Kraft inequality** | Existence statement | `:158-283` |
| | Wishlist question (motivation) | `:165` |
| | Kraft as interval packing (intuition) | `:183` |
| | **Theorem — Kraft** | `:213` |
| | Proof — necessity | `:224` |
| | Proof — sufficiency | `:233` |
| | What Kraft buys (interpretation + greedy technique) | `:244` |
| | **Theorem — Kraft–McMillan** | `:252` |
| | Proof — Kraft–McMillan | `:262` |
| | Corollary — $L \ge H(X)$ | `:272` |
| **03 — Shannon code** | $\lceil\log 1/p\rceil$, mismatch | `:285-385` |
| | Shannon code definition | `:292` |
| | **Theorem — entropy bound $H \le L < H+1$** (+ proof) | `:301` |
| | Why the gap is under 1 bit (intuition + ceiling technique) | `:311` |
| | Example — dyadic | `:339` |
| | Example — non-dyadic | `:353` |
| | Mismatch — coding for wrong distribution | `:362` |
| | Example — mismatch cost | `:373` |
| **04 — Huffman code** | Optimal prefix-free | `:387-528` |
| | Why merge the two rarest? (motivation) | `:394` |
| | Huffman algorithm | `:410` |
| | Worked example — step by step | `:422` |
| | Worked example — codewords | `:434` |
| | The exchange argument (intuition + reusable technique) | `:449` |
| | Optimality — two lemmas | `:464` |
| | Proof — Lemma 1 | `:477` |
| | Proof — Lemma 2 | `:485` |
| | **Theorem — Huffman is optimal** | `:493` |
| | Huffman vs entropy — 1-bit gap | `:502` |
| | Block coding — preview | `:510` |
| Recap | | `:517` |

**Key:** Kraft `:213`; Kraft–McMillan `:252`; entropy bound proof `:301`; Huffman optimality `:493`.

### Note (`lossless1-codes-note.html`)
- UD vs prefix-free with example
- Kraft as interval packing (arithmetic-coding bridge)
- Greedy Kraft sufficiency walk
- Why $T^k$ in Kraft–McMillan
- Entropy-bound clean derivation
- Shannon worst case
- Operational reading of mismatch
- Exchange argument as reusable technique (scheduling, matroids)
- Huffman optimality proof detail
- Block coding cost tradeoff

---

## lossless2-aep-arithmetic.html — AEP, Source coding, Arithmetic

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:25, :37` |
| **01 — AEP** | Typical sets, three properties | `:64-183` |
| | Motivation | `:72` |
| | Motivational example — concrete biased coin | `:80` |
| | Intuition — typical ≠ most probable (LLN reading) | `:91` |
| | **Theorem — AEP** (+ WLLN technique callout) | `:98` |
| | **Definition — typical set** | `:109` |
| | Three properties of $A_\varepsilon^{(n)}$ | `:119` |
| | Proof — property 1 (high probability) | `:132` |
| | Proof — property 2 (upper bound) | `:139` |
| | Proof — property 3 (lower bound) | `:147` |
| | Picture — volume counting | `:155` |
| | Example — Bernoulli source | `:174` |
| **02 — Source coding theorem** | Achievability + converse | `:186-297` |
| | Block code — setup | `:194` |
| | **Theorem — Shannon source coding** | `:205` |
| | Intuition — two directions (entropy as hard floor) | `:219` |
| | Achievability — idea | `:234` |
| | Achievability — error → 0 | `:244` |
| | Converse — $R<H$ fails | `:253` |
| | Converse — continued | `:261` |
| | Proof pattern — covering / counting (technique) | `:273` |
| | Zero-error case | `:288` |
| **03 — Arithmetic coding** | Map sequence to interval | `:297-387` |
| | Motivation — Huffman wastes up to 1 bit | `:305` |
| | Why arithmetic coding | `:312` |
| | Construction — recursive subdivision | `:323` |
| | Intuition — spending a probability budget (technique) | `:334` |
| | Example — encoding "AB" | `:360` |
| | From interval to bits | `:370` |
| | Example — decoding | `:378` |
| **04 — Optimality** | $L \le H + 2$ per block | `:387-451` |
| | **Lemma — truncation length** | `:395` |
| | Proof — truncation length | `:405` |
| | **Theorem — arithmetic coding bound** | `:413` |
| | Comparison — three codes | `:424` |
| Recap / Next | | `:436, :447` |

**Key:** AEP `:98`; typical set `:109`; source coding theorem `:205`; arithmetic coding bound `:413`.

### Note (`lossless2-aep-arithmetic-note.html`)
- Concrete biased coin — typical vs most probable
- Two proof patterns — covering / counting (reused across IT)
- Spending a probability budget — recursive subdivision technique
- Strong AEP (Birkhoff/SMB)
- Method of types
- Why "equipartition"
- Bernoulli numerical bounds
- Source coding theorem — both directions detail
- Arithmetic coding length proof
- Practical implementation issues
- Connection to LLM-based compression

---

## lossless3-markov-universal.html — Markov, Universal Coding

| Section | Slide | Line |
|---|---|---|
| Title / Contents | | `:25, :36` |
| **01 — Sources with memory** | Markov chains, stationarity | `:64-147` |
| | i.i.d. is not enough (English motivation) | `:71` |
| | **First-order Markov definition** | `:79` |
| | Intuition — state screens the past (SVG) | `:89` |
| | Example — two-state chain | `:117` |
| | Joint entropy of Markov chain | `:125` |
| | $k$-th order Markov | `:133` |
| **02 — Entropy rate** | Fundamental limit | `:148-216` |
| | **Definition — entropy rate** | `:156` |
| | Intuition — why the limit exists (Fekete flavor) | `:167` |
| | **Theorem — limits exist and agree** | `:175` |
| | Stationary Markov — closed form (avg one-step $H$) | `:186` |
| | Example — two-state chain | `:194` |
| | Coding a Markov source | `:205` |
| **03 — Universal coding** | Two-pass schemes, redundancy | `:217-262` |
| | The universal problem | `:225` |
| | Two-pass scheme | `:234` |
| | Redundancy = mismatch cost (KL callback) | `:246` |
| | Lower bound on redundancy | `:254` |
| **04 — Lempel–Ziv** | LZ78, optimality | `:263-348` |
| | The LZ idea | `:271` |
| | LZ78 algorithm | `:283` |
| | Worked example (+ dictionary $\Theta(n/\log n)$) | `:294` |
| | Intuition — parsing learns the source | `:308` |
| | **Theorem — asymptotic optimality** | `:316` |
| | Proof idea — LZ78 (phrase-counting) | `:327` |
| | Practical note — what real codecs do | `:338` |
| Recap series + Next | | `:350, :362` |

**Key:** Markov definition `:79`; entropy rate `:156`; Markov entropy rate closed form `:186`; LZ78 algorithm `:283`; LZ78 optimality `:316`. Stationary process notation $\mathbf{X}$ (KaTeX doesn't render `\mathscr`). 33 slides.

### Note (`lossless3-markov-universal-note.html`)
- Stationarity vs ergodicity
- Both-limits-agree detail (+ Fekete/subadditivity route)
- Two-state chain $\pi$ verification
- KT mixture universal code
- Context tree weighting
- LZ78 proof sketch (+ why phrase-counting bounds compression, $\Theta(n/\log n)$)
- LZ77 vs LZ78 in practice
- Modern LLM-based compression
