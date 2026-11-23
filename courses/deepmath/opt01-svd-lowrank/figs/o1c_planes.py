"""Geometry for the opt01 slide S87 "Two Planes in R^3 Share a Line".

Exact 3D construction, then one fixed oblique projection to the SVG viewBox.
  S1 = {z = 0}                     spanned by e1=(1,0,0), e2=(0,1,0); patch |x|,|y| <= 1
  S2 = span{d, e}, d=(1,0.3,0), e=(0,-0.6,1); patch d*t + e*s, |t| <= 1, |s| <= SMAX
  S1 cap S2 = span{d}  (a point t*d + s*e has z = s, so z = 0 forces s = 0)
  w  = 0.8 * d/|d|  (drawn arrow; any nonzero multiple of d lies in both planes)
Projection: X = OX + x*EX[0] + y*EY[0] + z*EZ[0],  Y = OY + x*EX[1] + y*EY[1] + z*EZ[1].
Run: python3 o1c_planes.py  -> prints polygon/line coordinates and overlay percentages.
"""
import math

W, H = 1040, 470
OX, OY = 520, 235
EX, EY, EZ = (300, 30), (-170, 75), (0, -175)
SMAX = 0.7

def proj(p):
    x, y, z = p
    return (OX + x*EX[0] + y*EY[0] + z*EZ[0], OY + x*EX[1] + y*EY[1] + z*EZ[1])

def add(a, b, ca=1, cb=1):
    return tuple(ca*u + cb*v for u, v in zip(a, b))

d, e = (1, 0.3, 0), (0, -0.6, 1)
s1 = [(1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0)]
s2 = [add(d, e, 1, SMAX), add(d, e, 1, -SMAX), add(d, e, -1, -SMAX), add(d, e, -1, SMAX)]
nd = math.sqrt(sum(c*c for c in d))
w = tuple(0.8*c/nd for c in d)

# invariants: the line and w lie in both planes
for p in [d, w, tuple(-c for c in d)]:
    assert abs(p[2]) < 1e-12                       # in S1 (z = 0)
    # in S2: solve p = t d + s e; z gives s = p[2]; then p - s e must be parallel to d
    s = p[2]; r = add(p, e, 1, -s); t = r[0]/d[0]
    assert all(abs(r[i] - t*d[i]) < 1e-12 for i in range(3))

fmt = lambda pts: " ".join(f"{proj(p)[0]:.0f},{proj(p)[1]:.0f}" for p in pts)
print("S1 polygon:", fmt(s1))
print("S2 polygon:", fmt(s2))
a, b = proj(tuple(-c for c in d)), proj(d)
print(f"shared line: {a[0]:.0f},{a[1]:.0f} -> {b[0]:.0f},{b[1]:.0f}")
o, wp = proj((0, 0, 0)), proj(w)
print(f"origin {o}, w tip {wp[0]:.0f},{wp[1]:.0f}")
for name, p in [("origin", o), ("w tip", wp)]:
    print(name, f"left {100*p[0]/W:.1f}% top {100*p[1]/H:.1f}%")
for name, pts in [("S1", s1), ("S2", s2)]:
    xs = [proj(p)[0] for p in pts]; ys = [proj(p)[1] for p in pts]
    print(name, "bbox", min(xs), max(xs), min(ys), max(ys))
