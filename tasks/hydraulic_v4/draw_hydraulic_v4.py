"""
Hydraulic v4 — ISO 1219 circuit: bleed-off, series feed, flow divider, regeneration.

Topology encoded in the drawing (NOT stated in the prompt). Y1 energised, Y2 off:
  Pump 1 (36 L/min) -> P line (relief 2 tees off, closed) -> DCV 3 port P.
  DCV 3: solenoid Y1 drawn on the RIGHT; the right envelope has CROSSED arrows
         (P->B, A->T); left envelope parallel (P->A, B->T); centre closed.
  Line B: rises, runs LEFT hopping over line A, tee (dot) to bleed-off FCV 8
         (8 L/min, to tank), continues to the CAP port of cylinder 4
         (cylinder 4 is drawn with its rod exiting LEFT, so its cap end is on the right).
  Rod port of cyl 4 -> inlet of flow divider 7. Divider LEFT outlet (60 %) runs at the
         lower level to the cap of cylinder 5; RIGHT outlet (40 %) rises higher (hopping
         the 60 % line) to the cap of cylinder 6.
  Cyl 5 rod port -> junction J: (a) check valve 9 (free flow J -> cyl 5 cap line),
         (b) pilot-operated check 10 down to line A (free flow A -> J only).
  POCV 10 pilot (dashed) starts at a DOT on the vertical of line A, just above the
         point where line B hops A; it then rises in line with B's riser and hops line A.
         Line A is at tank pressure (A->T) -> POCV 10 stays closed -> cyl 5 regenerates.
  Cyl 6 rod port -> line A -> T -> tank.
  Bores / rods: cyl 4 80/56, cyl 5 63/40, cyl 6 40/28 (mm).
  GTFA v5 = 114 mm/s. See verify.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
from matplotlib.patches import Arc, Circle, Polygon  # noqa: E402
from drawkit import *  # noqa: E402,F403

OUT = Path(__file__).with_name("hydraulic_v4.png")
fig, ax = new_canvas(16, 12.5)
R = 0.14          # hop radius
DASH = (0, (5, 3))


def hline(y, x0, x1, hops=(), ls="-", lw=LW):
    """Horizontal line with hops (semicircles) at the given x positions."""
    xs = sorted(hops, reverse=x0 > x1)
    s = 1 if x1 > x0 else -1
    cur = x0
    for h in xs:
        line(ax, [(cur, y), (h - s * R, y)], ls=ls, lw=lw)
        ax.add_patch(Arc((h, y), 2 * R, 2 * R, theta1=0, theta2=180, color=EDGE, lw=lw,
                         ls=ls if ls != "-" else "solid", zorder=3))
        cur = h + s * R
    line(ax, [(cur, y), (x1, y)], ls=ls, lw=lw)


def vline(x, y0, y1, hops=(), ls="-", lw=LW):
    ys = sorted(hops, reverse=y0 > y1)
    s = 1 if y1 > y0 else -1
    cur = y0
    for h in ys:
        line(ax, [(x, cur), (x, h - s * R)], ls=ls, lw=lw)
        ax.add_patch(Arc((x, h), 2 * R, 2 * R, theta1=-90, theta2=90, color=EDGE, lw=lw,
                         ls=ls if ls != "-" else "solid", zorder=3))
        cur = h + s * R
    line(ax, [(x, cur), (x, y1)], ls=ls, lw=lw)


def cylinder(x0, x1, y, h, rod_left, name, dims):
    box(ax, x0, y, x1 - x0, h)
    L = x1 - x0
    pw = 0.05 * L
    px = x0 + 0.55 * L if rod_left else x0 + 0.40 * L
    box(ax, px, y, pw, h)
    rh = 0.26 * h
    if rod_left:
        box(ax, x0 - 0.9, y + h / 2 - rh / 2, px - (x0 - 0.9), rh, z=3.5)
    else:
        box(ax, px + pw, y + h / 2 - rh / 2, (x1 + 0.9) - (px + pw), rh, z=3.5)
    txt(ax, (x0 + x1) / 2, y + h + 0.38, name, fs=16)
    txt(ax, (x0 + x1) / 2, y + h + 0.85, dims, fs=13)


def check(xc, yc, free="left", s=0.22):
    """ISO check valve: ball + V seat; free flow is from the seat apex toward the ball."""
    d = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}[free]
    bx, by = xc + d[0] * 0.10, yc + d[1] * 0.10
    ax.add_patch(Circle((bx, by), s * 0.75, facecolor="white", edgecolor=EDGE, lw=LW, zorder=6))
    ap = (xc - d[0] * 0.35, yc - d[1] * 0.35)               # seat apex
    px, py = -d[1], d[0]
    m1 = (xc + px * s * 1.2 - d[0] * 0.02, yc + py * s * 1.2 - d[1] * 0.02)
    m2 = (xc - px * s * 1.2 - d[0] * 0.02, yc - py * s * 1.2 - d[1] * 0.02)
    line(ax, [m1, ap, m2], z=6)


def solenoid(x, y, w=0.7, h=0.75, lab=""):
    box(ax, x, y, w, h)
    line(ax, [(x + 0.15, y), (x + w - 0.15, y + h)], lw=1.4, z=6)
    return lab


# ---------------- cylinders (top) ----------------
YC, HC = 10.2, 1.25
cylinder(1.2, 4.9, YC, HC, True, "4", "$\\varnothing 80\\,/\\,\\varnothing 56$")
cylinder(6.4, 10.0, YC, HC, False, "5", "$\\varnothing 63\\,/\\,\\varnothing 40$")
cylinder(11.9, 14.6, YC, HC, False, "6", "$\\varnothing 40\\,/\\,\\varnothing 28$")
C4_ROD, C4_CAP = 1.55, 4.55
C5_CAP, C5_ROD = 6.75, 9.65
C6_CAP, C6_ROD = 12.25, 14.25

# ---------------- DCV 3 ----------------
VX, VY, SQ, VH = 6.6, 2.6, 1.35, 1.35
for i in range(3):
    box(ax, VX + i * SQ, VY, SQ, VH)
o1, o2 = 0.32, 1.03                       # port offsets inside each square
# left square: parallel P->A, B->T
line(ax, [(VX + o1, VY + 0.2), (VX + o1, VY + VH - 0.2)], z=6)
arrow(ax, VX + o1, VY + VH - 0.45, 0, 0.25)
line(ax, [(VX + o2, VY + VH - 0.2), (VX + o2, VY + 0.2)], z=6)
arrow(ax, VX + o2, VY + 0.45, 0, -0.25)
# centre square: all ports blocked
cx = VX + SQ
for dx in (o1, o2):
    line(ax, [(cx + dx, VY + VH), (cx + dx, VY + VH - 0.4)], z=6)
    line(ax, [(cx + dx - 0.15, VY + VH - 0.4), (cx + dx + 0.15, VY + VH - 0.4)], z=6)
    line(ax, [(cx + dx, VY), (cx + dx, VY + 0.4)], z=6)
    line(ax, [(cx + dx - 0.15, VY + 0.4), (cx + dx + 0.15, VY + 0.4)], z=6)
# right square: crossed P->B, A->T
rx = VX + 2 * SQ
line(ax, [(rx + o1, VY + 0.2), (rx + o2, VY + VH - 0.2)], z=6)
arrow(ax, rx + o2 - 0.2, VY + VH - 0.48, 0.17, 0.25)
line(ax, [(rx + o1, VY + VH - 0.2), (rx + o2, VY + 0.2)], z=6)
arrow(ax, rx + o2 - 0.2, VY + 0.48, 0.17, -0.25)
solenoid(VX - 0.7, VY + 0.3)
solenoid(VX + 3 * SQ, VY + 0.3)
txt(ax, VX - 0.35, VY - 0.3, "Y2", fs=14)
txt(ax, VX + 3 * SQ + 0.35, VY - 0.3, "Y1", fs=14)
txt(ax, VX + SQ / 2, VY + VH + 0.35, "3", fs=16)
PA, PB = cx + o1, cx + o2                 # port x for A/P and B/T
txt(ax, PA - 0.22, VY + VH + 0.2, "A", fs=12)
txt(ax, PB + 0.22, VY + VH + 0.2, "B", fs=12)
txt(ax, PA - 0.22, VY - 0.2, "P", fs=12)
txt(ax, PB + 0.22, VY - 0.2, "T", fs=12)

# ---------------- pump 1, relief 2, tanks ----------------
YP = 1.9
pc = (2.0, 1.1)
ax.add_patch(Circle(pc, 0.5, facecolor="white", edgecolor=EDGE, lw=LW, zorder=4))
ax.add_patch(Polygon([(pc[0], pc[1] + 0.48), (pc[0] - 0.22, pc[1] + 0.1), (pc[0] + 0.22, pc[1] + 0.1)],
                     closed=True, facecolor=EDGE, edgecolor=EDGE, zorder=5))
line(ax, [(pc[0], pc[1] + 0.5), (pc[0], YP)])
line(ax, [(pc[0], pc[1] - 0.5), (pc[0], 0.3)])
tank(ax, pc[0], 0.3, w=0.8)
txt(ax, pc[0] - 0.75, pc[1], "1", ha="right", fs=16)
txt(ax, pc[0] - 0.75, pc[1] - 0.55, "$36\\,\\mathrm{L/min}$", ha="right", fs=13)
dot(ax, pc[0], YP)
# relief valve 2 on the P line
rvx = 3.4
dot(ax, rvx, YP)
line(ax, [(rvx, YP), (rvx, 1.5)])
box(ax, rvx - 0.35, 0.65, 0.7, 0.85)
line(ax, [(rvx, 0.8), (rvx, 1.35)], lw=1.4, z=6)
arrow(ax, rvx, 1.15, 0, -0.25, lw=1.4)
spring(ax, rvx + 0.35, 1.07, rvx + 0.95, n=4, amp=0.13)
line(ax, [(rvx, 0.65), (rvx, 0.3)])
tank(ax, rvx, 0.3, w=0.8)
txt(ax, rvx - 0.5, 1.07, "2", ha="right", fs=16)
# P line to DCV (FCV branch at x=5.2 hops over it)
X_FCV = 5.2
hline(YP, pc[0], PA, hops=[X_FCV])
line(ax, [(PA, YP), (PA, VY)])
# T line
line(ax, [(PB, VY), (PB, 1.0)])
tank(ax, PB, 1.0, w=0.8)

# ---------------- line B ----------------
YB = 4.7
line(ax, [(PB, VY + VH), (PB, YB)])
hline(YB, PB, C4_CAP, hops=[PA])
dot(ax, X_FCV, YB)
vline(C4_CAP, YB, YC, hops=[8.15, 8.85])            # up to cap of cyl 4 (cap on right)
# bleed-off FCV 8 on its branch (down to tank, hopping the P line)
fy0, fy1 = 2.75, 3.85
vline(X_FCV, YB, fy1)
box(ax, X_FCV - 0.38, fy0, 0.76, fy1 - fy0)
ax.add_patch(Arc((X_FCV - 0.22, (fy0 + fy1) / 2), 0.3, 0.7, theta1=-60, theta2=60, color=EDGE, lw=1.4, zorder=6))
ax.add_patch(Arc((X_FCV + 0.22, (fy0 + fy1) / 2), 0.3, 0.7, theta1=120, theta2=240, color=EDGE, lw=1.4, zorder=6))
arrow(ax, X_FCV - 0.28, fy0 + 0.12, 0.56, 0.86, lw=1.3, scale=11)
line(ax, [(X_FCV, fy0 + 0.05), (X_FCV, fy0 + 0.0)], z=6)
vline(X_FCV, fy0, 0.75, hops=[YP])
tank(ax, X_FCV, 0.75, w=0.8)
txt(ax, X_FCV - 0.5, fy1 - 0.15, "8", ha="right", fs=16)
txt(ax, X_FCV - 0.5, fy0 + 0.25, "$8\\,\\mathrm{L/min}$", ha="right", fs=13)

# ---------------- line A ----------------
YA = 5.7
line(ax, [(PA, VY + VH), (PA, YA)])                        # B hops this riser at YB
dot(ax, PA, 5.25)                                          # pilot take-off on line A
hline(YA, PA, C6_ROD, hops=[PB])
line(ax, [(C6_ROD, YA), (C6_ROD, YC)])                     # cyl 6 rod side -> A

# ---------------- cylinder 4 rod -> flow divider 7 ----------------
FDX, FDY, FDW, FDH = 2.0, 6.5, 1.3, 1.1
line(ax, [(C4_ROD, YC), (C4_ROD, 6.0), (FDX + FDW / 2, 6.0), (FDX + FDW / 2, FDY)])
box(ax, FDX, FDY, FDW, FDH)
o_l, o_r = FDX + 0.33, FDX + FDW - 0.33
line(ax, [(FDX + FDW / 2, FDY + 0.1), (FDX + FDW / 2, FDY + 0.45)], lw=1.4, z=6)
arrow(ax, FDX + FDW / 2, FDY + 0.45, o_l - (FDX + FDW / 2), FDH - 0.6, lw=1.4, scale=11)
arrow(ax, FDX + FDW / 2, FDY + 0.45, o_r - (FDX + FDW / 2), FDH - 0.6, lw=1.4, scale=11)
txt(ax, FDX - 0.25, FDY + FDH / 2, "7", ha="right", fs=16)
txt(ax, o_l - 0.12, FDY + FDH + 0.28, "$60\\,\\%$", ha="right", fs=12)
txt(ax, o_r + 0.12, FDY + FDH + 0.28, "$40\\,\\%$", ha="left", fs=12)
Y60, Y40 = 8.15, 8.85
line(ax, [(o_l, FDY + FDH), (o_l, Y60)])
vline(o_r, FDY + FDH, Y40, hops=[Y60])
hline(Y60, o_l, C5_CAP, hops=[o_r, C4_CAP])
line(ax, [(C5_CAP, Y60), (C5_CAP, YC)])
hline(Y40, o_r, C6_CAP, hops=[C4_CAP, C5_CAP, C5_ROD])
line(ax, [(C6_CAP, Y40), (C6_CAP, YC)])

# ---------------- cylinder 5 rod: check 9 and POCV 10 ----------------
YJ = 9.45
line(ax, [(C5_ROD, YC), (C5_ROD, YJ)])
dot(ax, C5_ROD, YJ)
dot(ax, C5_CAP, YJ)
hline(YJ, C5_ROD, C5_CAP)
check(8.2, YJ, free="left")
txt(ax, 8.2, YJ + 0.42, "9", fs=16)
# POCV 10 between J and line A
py0, py1 = 6.55, 7.75
vline(C5_ROD, YJ, py1, hops=[Y40])
box(ax, C5_ROD - 0.4, py0, 0.8, py1 - py0)
check(C5_ROD, (py0 + py1) / 2, free="up")
line(ax, [(C5_ROD, py0), (C5_ROD, py0 + 0.12)], z=6)
line(ax, [(C5_ROD, py1), (C5_ROD, py1 - 0.12)], z=6)
line(ax, [(C5_ROD, py0), (C5_ROD, YA)])
dot(ax, C5_ROD, YA)
txt(ax, C5_ROD + 0.55, py1 - 0.2, "10", ha="left", fs=16)
# pilot (dashed): dot on A riser -> right -> up in line with B riser -> hops A -> into POCV
YPIL = (py0 + py1) / 2 - 0.25
line(ax, [(PA, 5.25), (PB, 5.25)], ls=DASH, lw=1.5)
vline(PB, 5.25, YPIL, hops=[YA], ls=DASH, lw=1.5)
line(ax, [(PB, YPIL), (C5_ROD - 0.4, YPIL)], ls=DASH, lw=1.5)

save_png(fig, ax, str(OUT), xlim=(-0.2, 16.0), ylim=(-0.1, 12.6))
