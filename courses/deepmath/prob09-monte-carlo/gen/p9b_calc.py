#!/usr/bin/env python3
"""prob09 Parts 02-03 (P2): every number quoted on slides S43-S69 / S117-S121.

Deterministic closed-form arithmetic (no random draws, no seed needed).
Run:  python3 gen/p9b_calc.py
Running examples (shared with the rest of the deck):
  rare event   p = Exp(1) (rate 1), f(x) = 1{x > 10}, mu = P_p(X > 10) = e^{-10}
  proposal     q = Exp(lam), rate lam = 0.1 (illustrative, not optimized)
  oracle       q* = 10 + Exp(1) for the rare event (S63a/S63b); schematic x values only
  risk example p = Exp(1), f(x) = x, mu = 1; q = Exp(lam) family (S66-S69b):
               E_q[(fw)^2] = 2/[lam(2-lam)^3] for 0 < lam < 2, infinite for lam >= 2;
               lam = 2 (bad), 1/2 (helps), 3/2 (lighter tail, finite), 0.1 (too heavy)
  support      p uniform on {1,2,3,4}, q uniform on {1,2,3}, f = 1{x = 4}
"""
import math
from fractions import Fraction as F

T = 10.0          # threshold, fixed throughout Part 02
LAM = 0.1         # proposal rate
TARGET = 0.1      # relative RMSE target (10%)

mu = math.exp(-T)
print("== Rare event (S43) ==")
print(f"mu = e^-10 = {mu:.10e}  (~{mu:.7f});  1/mu = e^10 = {1/mu:.4f}")

print("== Ordinary MC (S44) ==")
rv_mc = (1 - mu) / mu                       # per-draw relative variance
n_mc = math.ceil(rv_mc / TARGET**2)
print(f"per-draw relative variance (1-mu)/mu = e^10 - 1 = {rv_mc:.7f}")
print(f"relative RMSE sqrt(rv/n) <= 0.1  =>  n >= rv/0.01 = {rv_mc/TARGET**2:.5f}  -> n = {n_mc}")

print("== Proposal q = Exp(0.1) (S117-S118) ==")
pq_tail = math.exp(-LAM * T)
print(f"P_q(X > 10) = e^-1 = {pq_tail:.6f};  P_p(X > 10) = {mu:.4e};  ratio = {pq_tail/mu:.1f}")
print(f"w(x) = p/q = e^-x / (0.1 e^-0.1x) = 10 e^-0.9x;  w(10) = f w at 10 = {10*math.exp(-0.9*T):.6e}")
for x in (10, 12, 15, 20, 25):
    print(f"   f w at x={x}: {10*math.exp(-0.9*x):.4e}   (vs mu {mu:.4e}, ratio {10*math.exp(-0.9*x)/mu:.4f})")
x_eq = -math.log(mu / 10) / 0.9
print(f"   f w = mu at x = {x_eq:.4f}  (contributions above mu for 10<x<{x_eq:.2f})")
# first moment check E_q[f w] = int_10^inf 10 e^-0.9x * 0.1 e^-0.1x dx = int e^-x = e^-10
print(f"E_q[f w] = int_10^inf e^-x dx = {math.exp(-T):.4e} = mu")

print("== Second moment (S119) ==")
def ratio(lam):  # E_q[(fw)^2] / mu^2, valid 0 < lam < 2
    return math.exp(T * lam) / (lam * (2 - lam))
r = ratio(LAM)
rv_is = r - 1
n_is = math.ceil(rv_is / TARGET**2)
print(f"E_q[(fw)^2]/mu^2 = e^(10 lam)/(lam(2-lam)) at lam=0.1: e/0.19 = {r:.10f}")
print(f"E_q[(fw)^2] = {r*mu*mu:.6e}")
# numeric check of the integral by midpoint rule on [10, 400]
N = 400000; a, b = T, 400.0; h = (b - a) / N
num = sum(math.exp(-2*(a+(i+.5)*h)) / (LAM*math.exp(-LAM*(a+(i+.5)*h))) for i in range(N)) * h
print(f"   numeric integral check: {num/mu/mu:.6f}")
print(f"relative variance per draw = {rv_is:.10f}")

print("== Sample budgets (S120) ==")
print(f"n_IS >= {rv_is/TARGET**2:.4f} -> {n_is};  n_MC = {n_mc};  ratio n_MC/n_IS = {n_mc/n_is:.1f}")

print("== Oracle proposal on the rare event (S63a, S63b) ==")
print("q*(x) = 1{x>10} e^-x / e^-10 = e^-(x-10) on x>10, i.e. X = 10 + Exp(1)")
print("Var_q*(X) = Var(Exp(1)) = 1  (X stays random)")
SCHEM = (10.3, 11.2, 12.7, 15.0)     # schematic illustrative x values on S63a (not draws)
for x in SCHEM:
    y = 1.0 * math.exp(-x) / math.exp(-(x - T))     # f(x) p(x) / q*(x)
    assert abs(y - mu) < 1e-18
    print(f"   x = {x:5.1f}: Y = f p/q* = {y:.6e}  (= e^-10 = {mu:.6e})")
print("Y = e^-10 for every x > 10  =>  Var_q*(Y) = 0, Var(mean of n) = 0;  Var_q*(X) = 1")

print("== Risk example (S66, S68, S69a, S69b) ==")
# q = Exp(2): w = e^x/2 ; E_q[Xw] = int x e^-x = 1 ; E_q[(Xw)^2] = int x^2/2 dx = inf
print(f"q=Exp(2): w(x)=e^x/2; densities cross at x=ln 2={math.log(2):.4f}; w(5)={math.exp(5)/2:.2f}, w(10)={math.exp(10)/2:.1f}")
# q = Exp(1/2): E_q[(Xw)^2] = int x^2 e^-2x / (0.5 e^-x/2) = 2 int x^2 e^-1.5x = 2 * 2/1.5^3
m2 = F(2) * F(2) / F(3, 2)**3
print(f"q=Exp(1/2): E_q[(Xw)^2] = 2 * 2/(3/2)^3 = {m2} = {float(m2):.6f}; variance per draw = {m2-1} = {float(m2-1):.6f}")
w2 = F(1) / (F(1, 2) * (2 - F(1, 2)))
print(f"   bare-weight E_q[w^2] = 1/(lam(2-lam)) at lam=1/2 = {w2};  ordinary MC variance of X under Exp(1) = 1")
print(f"   variance ratio ordinary/IS = 1/(5/27) = {F(1)/(m2-1)} = {float(F(1)/(m2-1))}")

print("== Exp(lam) family for f = x (S69a, S69b) ==")
# p^2/q = e^-2x / (lam e^-lam x) = (1/lam) e^-(2-lam)x ;  int x^2 e^-a x = 2/a^3  (a > 0)
def m2_lam(lam):
    lam = F(lam)
    if lam >= 2:
        return None                               # integrand x^2 e^{(lam-2)x}/lam does not decay
    return F(2) / (lam * (2 - lam)**3)
for lam in (F(1, 10), F(1, 2), F(1), F(3, 2), F(2)):
    m = m2_lam(lam)
    if m is None:
        print(f"   lam = {str(lam):>4s}: E_q[(fw)^2] = inf  (lam >= 2)")
        continue
    # midpoint-rule check on [0, 400]
    N = 200000; b = 400.0; h = b / N; l = float(lam)
    num = sum(((i+.5)*h)**2 * math.exp(-2*(i+.5)*h) / (l*math.exp(-l*(i+.5)*h)) for i in range(N)) * h
    print(f"   lam = {str(lam):>4s}: E_q[(fw)^2] = {m} = {float(m):.6f} (numeric {num:.6f}); Var_q(fw) = {m-1} = {float(m-1):.6f}")
print("   lam = 3/2: p^2/q = (2/3) e^{-x/2};  int (2/3) x^2 e^{-x/2} dx = (2/3)*16 = 32/3")
print("   lam = 1 is ordinary MC (q = p): Var = 1; lam = 3/2 lighter tail than p yet finite (29/3 > 1: not efficient)")
v_half, v_tenth = m2_lam(F(1, 2)) - 1, m2_lam(F(1, 10)) - 1
print(f"   S69b: heavier tail P_q(X>t) = e^(-lam t), so Exp(1/10) is heavier than Exp(1/2): "
      f"Var {v_half} = {float(v_half):.4f} -> {v_tenth} = {float(v_tenth):.4f} (worse, and worse than ordinary MC 1)")

print("== Support counterexample (S48) ==")
p = {x: F(1, 4) for x in (1, 2, 3, 4)}
q = {x: F(1, 3) for x in (1, 2, 3)}
f = lambda x: 1 if x == 4 else 0
w = {x: p[x] / q[x] for x in q}
print(f"target mu = sum p f = {sum(p[x]*f(x) for x in p)}; weights on observed states = {set(w.values())}")
print(f"E_q[f w] = {sum(q[x]*f(x)*w[x] for x in q)}  (every draw contributes 0)")
print(f"E_q[w] = {sum(q[x]*w[x] for x in q)}  (= P_p(q>0); q covers p only on 1..3)")
