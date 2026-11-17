#!/usr/bin/env python3
"""prob09 Part 05 (P4) -- exact checks for every number on slides S93-S127 and S123-S126.

Deterministic. Exact arithmetic (fractions) for the two-action toy; numerical
quadrature plus one seeded Monte Carlo illustration for the Gaussian example.
Run:  python3 gen/p9d_gradient_checks.py
Inputs: two actions a1 (reward 1), a0 (reward 0); pi_theta(a1) = sigmoid(theta);
        theta = 0 for the baseline toy; baselines b in {0, 1/2, 2};
        Gaussian X = theta + eps, eps ~ N(0,1), R(x) = x^2, theta = 1; seed 20261117.
"""
from fractions import Fraction as F
import math, random

def sig(t):
    return 1.0 / (1.0 + math.exp(-t))

print("== Two-action policy (S126, S93, S94) ==")
for t in (0.0, 1.0):
    print(f"theta={t:g}: pi(a1)=sigma={sig(t):.4f}, pi(a0)={1-sig(t):.4f}, "
          f"J=sigma={sig(t):.4f}, J'=sigma(1-sigma)={sig(t)*(1-sig(t)):.4f}")
# finite-difference check of sigma' = sigma(1-sigma) at theta = 0 and 1
for t in (0.0, 1.0):
    h = 1e-6
    fd = (sig(t + h) - sig(t - h)) / (2 * h)
    print(f"  central difference J'({t:g}) = {fd:.6f}")

# exact toy at theta = 0
s1, p1, R1 = F(1, 2), F(1, 2), F(1)        # action a1: score 1 - sigma, prob sigma, reward 1
s0, p0, R0 = F(-1, 2), F(1, 2), F(0)       # action a0: score -sigma, prob 1 - sigma, reward 0
Es = p1 * s1 + p0 * s0
print(f"theta=0 scores: s(a1)={s1}, s(a0)={s0}; E[s]={Es}")
print(f"contributions R*s: a1 -> {R1*s1}, a0 -> {R0*s0}; mean = {p1*R1*s1 + p0*R0*s0}")

print("\n== Baselines on the toy (S97, S127) ==")
def stats(b):
    g1, g0 = (R1 - b) * s1, (R0 - b) * s0
    m = p1 * g1 + p0 * g0
    v = p1 * (g1 - m) ** 2 + p0 * (g0 - m) ** 2
    return g1, g0, m, v
for b in (F(0), F(1, 2), F(2)):
    g1, g0, m, v = stats(b)
    formula = (b - F(1, 2)) ** 2 / 4
    print(f"b={b}: g(a1)={g1}, g(a0)={g0}, mean={m}, Var={v}, (b-1/2)^2/4={formula}")
    assert v == formula and m == F(1, 4)
Es2 = p1 * s1**2 + p0 * s0**2
ERs2 = p1 * R1 * s1**2 + p0 * R0 * s0**2
bstar = ERs2 / Es2
print(f"b* = E[R s^2]/E[s^2] = {ERs2}/{Es2} = {bstar}")
for b in (F(0), F(1, 2), F(1), F(2)):
    better = b * (b - 2 * bstar) < 0
    print(f"  b={b}: b(b-2b*)={b*(b-2*bstar)}, improves on b=0: {better}; "
          f"Var(g_b)-Var(g_0)={stats(b)[3]-stats(F(0))[3]}")

print("\n== Gaussian pathwise check (S125) ==")
theta = 1.0
# E[(theta+eps)^2] by composite Simpson on [-12, 12]
N, L = 24000, 12.0
hgrid = 2 * L / N
def phi(e):
    return math.exp(-e * e / 2) / math.sqrt(2 * math.pi)
def simpson(fn):
    s = fn(-L) + fn(L)
    for k in range(1, N):
        s += (4 if k % 2 else 2) * fn(-L + k * hgrid)
    return s * hgrid / 3
J = simpson(lambda e: (theta + e) ** 2 * phi(e))
dJ = simpson(lambda e: 2 * (theta + e) * phi(e))
var2X = simpson(lambda e: (2 * (theta + e) - 2 * theta) ** 2 * phi(e))
print(f"theta={theta:g}: J = E[X^2] = {J:.6f} (theta^2+1 = {theta**2+1:g}); "
      f"E[2X] = {dJ:.6f} (2 theta = {2*theta:g}); Var(2X) = {var2X:.6f} (4)")
rng = random.Random(20261117)
draws = [2 * (theta + rng.gauss(0.0, 1.0)) for _ in range(5)]
print("seed 20261117, five pathwise contributions 2X:", ", ".join(f"{d:.2f}" for d in draws))
