"""prob09 Part 01 (P1): every number and plotted coordinate on slides S26-S116b.

Deterministic formula data only: no random numbers are drawn, so no seed is needed.
Run:  python3 gen/p9a_part01.py          (prints the ledger; rewrites fig/p9a-rare-sd.svg)
Sources for the inputs: prior job (2026-11-17) evidence E17 (six hand-chosen darts,
darts bounds); job 2026-11-18 evidence E03 (generic rare-event toy rho = 0.001, n = 1000).
The exponential rare event of Part 02 (e^-10) is computed in gen/p9b_calc.py, not here.
"""
import os
import math
from statistics import NormalDist

PI = math.pi

# ---------- S26: six hand-chosen darts (E17) ----------
darts = [(0.5, 0.5), (-0.9, 0.8), (0.2, -0.6), (-0.4, 0.1), (0.8, -0.7), (0.3, 0.9)]
hits = 0
print("S26 darts ledger (x, y, x^2+y^2, in?)")
for x, y in darts:
    r2 = x * x + y * y
    inside = r2 <= 1
    hits += inside
    # SVG (viewBox 400x440): square [-1,1]^2 -> centre (200,200), half-side 180
    print(f"  ({x:+.1f},{y:+.1f})  r2={r2:.2f}  {'in ' if inside else 'out'}  svg=({200+180*x:.1f},{200-180*y:.1f})")
print(f"  hits={hits}/6  estimate 4*hits/6 = {4*hits/6:.6f}  (8/3 = {8/3:.6f})")

# ---------- darts population quantities: f(x) = 4 * 1{|x| <= 1}, X ~ Unif[-1,1]^2 ----------
rho_d = PI / 4
var_f = PI * (4 - PI)                 # Var(4 * Bernoulli(pi/4)) = 16 rho (1 - rho)
sd_f = math.sqrt(var_f)
print(f"\nDarts: rho=pi/4={rho_d:.6f}  sigma_f^2=pi(4-pi)={var_f:.10f}  sigma_f={sd_f:.6f}")

# ---------- S19: exact distribution of the n = 6 darts estimate ----------
print("\nS19 exact pmf of hat mu_6 = 4K/6, K ~ Bin(6, pi/4); SVG x=120+190*v, y=300-650*P")
mean = 0.0
for k in range(7):
    pk = math.comb(6, k) * rho_d**k * (1 - rho_d)**(6 - k)
    v = 4 * k / 6
    mean += v * pk
    print(f"  k={k} value={v:.4f} P={pk:.4f}  bar x={120+190*v:.1f} top y={300-650*pk:.1f}")
print(f"  mean={mean:.6f} (pi={PI:.6f}); mu line x={120+190*PI:.1f}; P(hat mu_6 = pi) = 0")
print(f"  P(|hat mu_6 - pi| >= 0.5) = {sum(math.comb(6,k)*rho_d**k*(1-rho_d)**(6-k) for k in range(7) if abs(4*k/6-PI) >= 0.5):.4f}")
print(f"  RMSE at n=6 = {sd_f/math.sqrt(6):.4f}")

# ---------- S22: exact RMSE curve sigma_f / sqrt(n) ----------
print("\nS22 RMSE = sigma_f/sqrt(n); SVG x=150+156*(log10 n - 1), y=20+75*(-log10 RMSE)")
for n in [10, 100, 10**4, 10**6]:
    r = sd_f / math.sqrt(n)
    print(f"  n={n:>8}  RMSE={r:.6f}  svg=({150+156*(math.log10(n)-1):.1f},{20+75*(-math.log10(r)):.1f})")

# ---------- S115: CLT quantile and Chebyshev (known variance) ----------
z = NormalDist().inv_cdf(0.975)
eps, delta = 0.01, 0.05
n_cheb = var_f / (delta * eps**2)
print(f"\nS115 z_0.975={z:.5f}; Chebyshev n >= pi(4-pi)/(delta eps^2) = {n_cheb:.2f} -> {math.ceil(n_cheb)}")

# ---------- S24: Hoeffding, range [0,4] ----------
a, b = 0.0, 4.0
n_hoef = (b - a)**2 * math.log(2 / delta) / (2 * eps**2)
print(f"S24 ln(2/delta)=ln 40={math.log(40):.6f}; Hoeffding n >= {n_hoef:.2f} -> {math.ceil(n_hoef)}")
nh = math.ceil(n_hoef)
print(f"  check bound at n={nh}: 2exp(-2 n eps^2/16) = {2*math.exp(-2*nh*eps**2/16):.6f}")
print(f"  ratio Chebyshev/Hoeffding = {math.ceil(n_cheb)/nh:.3f}")
print(f"  RMSE at n={nh}: {sd_f/math.sqrt(nh):.5f}")

# ---------- S116a / S116b: generic rare event, rho = 0.001, n = 1000 (job E03) ----------
rho, n = 0.001, 1000
print(f"\nS116a rare event: rho={rho}, n={n}")
print(f"  expected hits n*rho = {n*rho:g}")
p0 = (1 - rho) ** n
print(f"  P(no hit) = (1-rho)^n = 0.999^1000 = {p0:.10f}  (~{100*p0:.0f}%)")
print(f"  zero-hit run: estimate 0; absolute error = {abs(0-rho):g}; relative error = {abs(0-rho)/rho:.0%}")
abs_rmse = math.sqrt(rho * (1 - rho) / n)
rel_rmse = math.sqrt((1 - rho) / (n * rho))
print(f"\nS116b absolute RMSE sqrt(rho(1-rho)/n) = {abs_rmse:.12f}")
print(f"  relative RMSE sqrt((1-rho)/(n rho)) = {rel_rmse:.9f}  (~{100*rel_rmse:.0f}%); approx 1/sqrt(n rho) = {1/math.sqrt(n*rho):.4f}")
n10 = (1 - rho) / (rho * 0.1 ** 2)
print(f"  relative RMSE <= 0.10 needs n >= (1-rho)/(0.01 rho) = {n10:.6f} -> n >= {math.ceil(n10 - 1e-9):,}")
print(f"  expected hits at n = 99,900: {99900*rho:.1f};  relative RMSE there = {math.sqrt((1-rho)/(99900*rho)):.6f}")

# ---------- S116b notes figure: per-draw absolute and relative SD vs rho (moved from old S116) ----------
# x = 150 + 135 (log10 rho + 6) for rho in [1e-6, 1/2]; y = 20 + 40 (3 - log10 value)
X = lambda lr: 150 + 135 * (lr + 6)
Yc = lambda v: 20 + 40 * (3 - math.log10(v))
def pts(fn):
    out = []
    for i in range(0, 31):
        lr = -6 + i * (math.log10(0.5) + 6) / 30
        out.append(f"{X(lr):.1f},{Yc(fn(10**lr)):.1f}")
    return " ".join(out)
abs_pts = pts(lambda r: math.sqrt(r * (1 - r)))
rel_pts = pts(lambda r: math.sqrt((1 - r) / r))
print("\nS116b-note figure (fig/p9a-rare-sd.svg): log-log, rho in [1e-6, 1/2]")
for r in [1e-6, 1e-3, 0.5]:
    print(f"  rho={r:g}: absolute SD={math.sqrt(r*(1-r)):.6g}  relative SD={math.sqrt((1-r)/r):.6g}")
print("  absolute SD points:", abs_pts)
print("  relative SD points:", rel_pts)
xr = X(math.log10(rho))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" font-family="Noto Sans, Arial, sans-serif" font-size="24" role="img" aria-labelledby="t d">
<title id="t">Per-draw absolute and relative SD of an event indicator</title>
<desc id="d">Log-log plot against event probability rho from 10^-6 to 1/2. Absolute SD sqrt(rho(1-rho)) rises with rho from 0.001 to 0.5; relative SD sqrt((1-rho)/rho) falls from about 1000 to 1. The curves do not meet on this range. Generated by gen/p9a_part01.py.</desc>
<!-- generated by gen/p9a_part01.py; exact formula curves, no random draws -->
<rect width="1000" height="340" fill="#fff"/>
<line x1="150" y1="265" x2="940" y2="265" stroke="#222" stroke-width="2.5"/>
<line x1="150" y1="265" x2="150" y2="10" stroke="#222" stroke-width="2.5"/>
<line x1="150" y1="140" x2="930" y2="140" stroke="#bbb" stroke-width="2" stroke-dasharray="6 6"/>
<line x1="{xr:.1f}" y1="12" x2="{xr:.1f}" y2="265" stroke="#999" stroke-width="2" stroke-dasharray="4 6"/>
<polyline fill="none" stroke="#c0392b" stroke-width="4.5" points="{rel_pts}"/>
<polyline fill="none" stroke="#003876" stroke-width="4.5" stroke-dasharray="14 8" points="{abs_pts}"/>
<g stroke="#222" stroke-width="2">
<line x1="141" y1="20" x2="150" y2="20"/><line x1="141" y1="140" x2="150" y2="140"/><line x1="141" y1="260" x2="150" y2="260"/>
<line x1="150" y1="265" x2="150" y2="274"/><line x1="420" y1="265" x2="420" y2="274"/><line x1="690" y1="265" x2="690" y2="274"/>
</g>
<g fill="#555" text-anchor="end">
<text x="132" y="28">10³</text><text x="132" y="148">1</text><text x="132" y="268">10⁻³</text>
</g>
<g fill="#555" text-anchor="middle">
<text x="150" y="300">10⁻⁶</text><text x="420" y="300">10⁻⁴</text><text x="690" y="300">10⁻²</text>
<text x="{xr:.1f}" y="330" fill="#777">ρ = 0.001</text>
</g>
<text x="930" y="300" fill="#555" text-anchor="end">event probability ρ</text>
<text x="600" y="62" fill="#c0392b" font-weight="700">relative SD √((1−ρ)/ρ)</text>
<text x="600" y="232" fill="#003876" font-weight="700">absolute SD √(ρ(1−ρ))</text>
</svg>
'''
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fig", "p9a-rare-sd.svg")
with open(out, "w") as fh:
    fh.write(svg)
print(f"  wrote fig/p9a-rare-sd.svg; rho=0.001 guide at x={xr:.1f}")
