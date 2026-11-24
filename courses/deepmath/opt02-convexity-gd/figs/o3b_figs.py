"""Coordinates for the o3b- inline SVG figures in opt02-convexity-gd.html (slides S95, S65, S110).
Run: python3 o3b_figs.py  -> prints polyline point lists and invariant checks.
Exact inputs:
  S95  f(u) = max(|u|-1, 0)^2  (convex, 2-smooth, argmin = [-1,1]); x_t = 2.9, x* = 1.
       X = 320 + 75u, Y = 270 - 33 f.
  S65  generic scalar illustration (our choice, not tied to any other example):
       phi(s) = s^2 (curvature 2); illustrative mu = 1, L = 3, so mu < 2 < L;
       anchor s0 = -1; floor = phi(s0)+phi'(s0)(s-s0)+(mu/2)(s-s0)^2;
       lid = same with L/2. Residual above the tangent: r(s) = (s-s0)^2, and
       (mu/2)(s-s0)^2 <= r(s) <= (L/2)(s-s0)^2. X = 320 + 110 s, Y = 300 - 28 v;
       viewBox 640x385, curves clipped to y >= 20. Slide labels show only mu and L.
  S110 shapes 1/T and q^T with illustrative q = 0.8, T = 1..24, log10 scale.
       X = 80 + 22(T-1), Y = 30 + 80(-log10 e). Not GD output; shapes only.
"""
import math

def pts(xs, fx, X, Y):
    return " ".join(f"{X(x):.1f},{Y(fx(x)):.1f}" for x in xs)

def rng(a, b, n):
    return [a + (b - a) * i / n for i in range(n + 1)]

# S95
f = lambda u: max(abs(u) - 1, 0) ** 2
X1 = lambda u: 320 + 75 * u
Y1 = lambda v: 270 - 33 * v
print("S95 f:", pts(rng(-3.6, 3.6, 72), f, X1, Y1))
print("S95 x_t:", X1(2.9), Y1(f(2.9)), " x*:", X1(1), Y1(0))

# S65
phi = lambda s: s * s
MU, LL = 1.0, 3.0
s0 = -1.0
dphi = 2 * s0
floor = lambda s: phi(s0) + dphi * (s - s0) + 0.5 * MU * (s - s0) ** 2
lid = lambda s: phi(s0) + dphi * (s - s0) + 0.5 * LL * (s - s0) ** 2
X2 = lambda s: 320 + 110 * s
Y2 = lambda v: 300 - 28 * v
ss = rng(-2.6, 2.4, 50)
assert min(Y2(floor(s)) for s in ss) < 350 and max(Y2(phi(s)) for s in ss) <= 300
for name, g in [("phi", phi), ("floor", floor), ("lid", lid)]:
    print("S65", name + ":", pts(ss, g, X2, Y2))
# invariants: floor <= phi <= lid everywhere on a fine grid, equality only at s0
grid = rng(-2.6, 2.4, 5000)
assert all(floor(s) <= phi(s) + 1e-12 and phi(s) <= lid(s) + 1e-12 for s in grid)
# residual above the tangent is trapped between (mu/2)h^2 and (L/2)h^2
tan = lambda s: phi(s0) + dphi * (s - s0)
assert MU < 2 < LL
assert all(0.5 * MU * (s - s0) ** 2 - 1e-12 <= phi(s) - tan(s) <= 0.5 * LL * (s - s0) ** 2 + 1e-12 for s in grid)
print("S65 anchor:", X2(s0), Y2(phi(s0)))

# S110
X3 = lambda T: 80 + 22 * (T - 1)
Y3 = lambda e: 30 + 80 * (-math.log10(e))
Ts = list(range(1, 25))
print("S110 1/T:", " ".join(f"{X3(T):.1f},{Y3(1/T):.1f}" for T in Ts))
Q = 0.8
print("S110 q^T:", " ".join(f"{X3(T):.1f},{Y3(Q**T):.1f}" for T in Ts))
print("S110 q^T label anchor T=16:", X3(16), round(Y3(Q**16), 1))
print("checks ok")
