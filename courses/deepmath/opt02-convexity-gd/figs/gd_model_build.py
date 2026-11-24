"""Coordinates for the S34a/S34b/S34c build in opt02-convexity-gd.html
("Start at the Current Point" / "Smoothness Adds an Upper Model" / "Minimize the Model, Then Step").
Run: python3 gd_model_build.py  -> prints polyline point lists, marker positions and checks.

Exact inputs (evidence E09 of job 2026-11-24-opt01-opt02-polish; our calculation, illustrative only):
  f(u)  = u^2            (f' = 2u is 2-Lipschitz, so f is 2-smooth and hence L-smooth for L = 3)
  x     = u0 = -0.6,  g = f'(u0) = -1.2,  L = 3
  tangent T(u) = f(u0) + g (u - u0)
  model   Q(u) = f(u0) + g (u - u0) + (L/2)(u - u0)^2,   Q - f = (1/2)(u + 0.6)^2 >= 0
  model minimizer u+ = u0 - g/L = -0.2;  Q(u+) = f(u0) - g^2/(2L) = 0.12;  f(u+) = 0.04;  argmin f = 0.
Frame (shared by all three slides): viewBox 0 0 760 360,
  X = 360 + 340 u,  Y = 295 - 420 v  (axis v = 0 at Y = 295); curves drawn only where v <= 0.65.
The frame is a pure rescaling of the old S34 frame (same curve, point and L).
"""

f = lambda u: u * u
u0, L = -0.6, 3.0
g = 2 * u0
T = lambda u: f(u0) + g * (u - u0)
Q = lambda u: f(u0) + g * (u - u0) + 0.5 * L * (u - u0) ** 2
X = lambda u: 360 + 340 * u
Y = lambda v: 295 - 420 * v
VMAX = 0.65


def poly(fn, a, b, n=60):
    out = []
    for i in range(n + 1):
        u = a + (b - a) * i / n
        if fn(u) <= VMAX + 1e-9:
            out.append(f"{X(u):.1f},{Y(fn(u)):.1f}")
    return " ".join(out)


up = u0 - g / L
# checks
assert abs(up + 0.2) < 1e-12
assert abs(Q(up) - (f(u0) - g * g / (2 * L))) < 1e-12 and abs(Q(up) - 0.12) < 1e-12
assert abs(f(up) - 0.04) < 1e-12
grid = [-2 + 4 * i / 4000 for i in range(4001)]
assert all(Q(u) - f(u) >= -1e-12 for u in grid)
assert all(abs((Q(u) - f(u)) - 0.5 * (u + 0.6) ** 2) < 1e-12 for u in grid)
assert all(T(u) <= f(u) + 1e-12 for u in grid)  # tangent lies below f (f convex): no upper bound
assert min(grid, key=Q) - up < 1e-3

print("f      :", poly(f, -0.81, 0.81))
print("Q      :", poly(Q, -0.80, 0.40))
ua, ub = -0.83, -0.28
print("tangent:", f"x1={X(ua):.1f} y1={Y(T(ua)):.1f} x2={X(ub):.1f} y2={Y(T(ub)):.1f}")
print("x      :", f"({X(u0):.1f}, {Y(f(u0)):.1f})")
print("x+ on Q:", f"({X(up):.1f}, {Y(Q(up)):.1f})", " on f:", f"({X(up):.1f}, {Y(f(up)):.1f})")
print("argmin f:", f"({X(0):.1f}, {Y(0):.1f})")
print("checks ok")
