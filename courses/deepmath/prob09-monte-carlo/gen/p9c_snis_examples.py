#!/usr/bin/env python3
"""prob09 Part 04 (P3): exact finite-state / finite-batch numbers for SNIS and weight diagnostics.

Deterministic (exact rational arithmetic, no random numbers; no seed needed).
Run:  python3 gen/p9c_snis_examples.py
Feeds slides S78, S122 (note), S70, S79, S81 of prob09-monte-carlo.html and their note articles.
"""
from fractions import Fraction as F
from math import comb

def ess(ws):
    s = sum(ws); s2 = sum(w * w for w in ws)
    return s * s / s2

print("== S78: one draw exposes SNIS bias (E12) ==")
pt = {"a": F(3), "b": F(1)}            # unnormalized target tilde p
Z = sum(pt.values())
p = {k: v / Z for k, v in pt.items()}
q = {"a": F(1, 2), "b": F(1, 2)}
f = {"a": F(1), "b": F(0)}
wt = {k: pt[k] / q[k] for k in pt}      # tilde w = tilde p / q
w = {k: p[k] / q[k] for k in pt}        # normalized ratio w = p / q
mu = sum(p[k] * f[k] for k in pt)
print("Z =", Z, " p =", p, " tilde w =", wt, " w =", w, " mu =", mu)
e_sn1 = sum(q[k] * (wt[k] * f[k] / wt[k]) for k in pt)   # n = 1: SNIS = f(X1)
for k in pt:
    print(f"  draw {k}: prob {q[k]}, tilde w {wt[k]}, SNIS estimate {wt[k]*f[k]/wt[k]}")
print("E[SNIS, n=1] =", e_sn1, " target mu =", mu, " bias =", e_sn1 - mu)

def snis_two_state(n, fa, fb):
    """exact E and MSE of SNIS and ordinary IS for n iid draws from q in the two-state toy"""
    fv = {"a": F(fa), "b": F(fb)}
    m = sum(p[k] * fv[k] for k in pt)
    Esn = Msn = Eis = Mis = F(0)
    for ka in range(n + 1):            # ka draws land on state a
        pr = comb(n, ka) * q["a"] ** ka * q["b"] ** (n - ka)
        num = ka * wt["a"] * fv["a"] + (n - ka) * wt["b"] * fv["b"]
        den = ka * wt["a"] + (n - ka) * wt["b"]          # always > 0 here (both weights positive)
        sn = num / den
        is_ = (ka * w["a"] * fv["a"] + (n - ka) * w["b"] * fv["b"]) / n
        Esn += pr * sn; Msn += pr * (sn - m) ** 2
        Eis += pr * is_; Mis += pr * (is_ - m) ** 2
    return m, Esn, Msn, Eis, Mis

print("\n== S122 note: no universal ranking, same two-state toy, n = 1 ==")
for fa, fb in [(1, 0), (0, 1)]:
    m, Esn, Msn, Eis, Mis = snis_two_state(1, fa, fb)
    print(f"  f=({fa},{fb}): mu={m}  E[IS]={Eis} MSE[IS]={Mis}  E[SNIS]={Esn} MSE[SNIS]={Msn}")
print("  constant f=(1,1): SNIS =", snis_two_state(1, 1, 1)[1], "exactly; IS MSE =", snis_two_state(1, 1, 1)[4])

print("\n== S122 note: n * bias of SNIS vs formal expansion -E_q[w^2 (f - mu)] (f=(1,0)) ==")
lead = -sum(q[k] * w[k] ** 2 * (f[k] - mu) for k in pt)
print("  formal leading constant -E_q[w^2(f-mu)] =", lead, "=", float(lead))
for n in [1, 2, 5, 10, 50, 200]:
    m, Esn, *_ = snis_two_state(n, 1, 0)
    print(f"  n={n:4d}: bias = {float(Esn - m):+.6f}   n*bias = {float(n*(Esn - m)):+.6f}")

print("\n== S70 / S79: five-weight batch (E19) ==")
batch = [F(1, 10), F(2, 10), F(1, 10), F(1, 10), F(95, 10)]
tot = sum(batch)
shares = [b / tot for b in batch]
print("weights", [float(b) for b in batch], " total", tot)
print("normalized shares", [float(s) for s in shares], " sum", sum(shares))
print("sum w^2 =", float(sum(b*b for b in batch)), " ESS = (sum w)^2/sum w^2 =", ess(batch), "=", f"{float(ess(batch)):.10f}")
print("1/sum(bar w^2) =", f"{float(1/sum(s*s for s in shares)):.10f}")
# bar geometry for the SVG (axis y=300 baseline, 100% = 250 px)
for i, s in enumerate(shares, 1):
    h = float(s) * 250
    print(f"  bar {i}: share {float(s):.2f} height {h:.2f} y {300-h:.2f}")
print("equal weights n=5: ESS =", ess([F(1)] * 5), "; one positive weight: ESS =", ess([F(0)] * 4 + [F(1)]))

print("\n== S81: healthy ESS, missed support (E19) ==")
pS = {x: F(1, 4) for x in (1, 2, 3, 4)}
qS = {x: (F(1, 3) if x <= 3 else F(0)) for x in (1, 2, 3, 4)}
fS = {x: F(1 if x == 4 else 0) for x in (1, 2, 3, 4)}
muS = sum(pS[x] * fS[x] for x in pS)
wS = {x: pS[x] / qS[x] for x in (1, 2, 3)}
print("target mu =", muS, " observed weights w = p/q on {1,2,3}:", wS)
for n in [1, 5, 100]:
    ws = [F(3, 4)] * n          # every draw lands in {1,2,3}, each with weight 3/4
    print(f"  n={n}: bar w_i = {ws[0]/sum(ws)}, ESS = {ess(ws)}, IS estimate = {sum(wi*0 for wi in ws)/n}, SNIS = 0")
print("  E_q[w] =", sum(qS[x] * wS[x] for x in (1, 2, 3)), "(not 1: missing target mass 1/4)")

print("\n== S74 note: q covers f*p but not all of p -> SNIS limit is wrong ==")
f1 = {x: F(1 if x == 1 else 0) for x in (1, 2, 3, 4)}       # f = 1{x=1}
mu1 = sum(pS[x] * f1[x] for x in pS)
num = sum(qS[x] * wS[x] * f1[x] for x in (1, 2, 3))          # E_q[w f]
den = sum(qS[x] * wS[x] for x in (1, 2, 3))                  # E_q[w]
print(f"  f=1{{x=1}}: mu={mu1}; ordinary IS mean E_q[w f]={num} (correct); SNIS limit E_q[w f]/E_q[w]={num/den} (wrong)")

print("\n== S75 note: P(all sampled weights zero) = (1 - Q(tilde p > 0))^n ==")
for pi_, n in [(F(1, 2), 1), (F(1, 2), 10)]:
    print(f"  Q(tilde p>0)={pi_}, n={n}: P(total=0) = {(1-pi_)**n}")
