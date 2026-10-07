"""
Lever v1 — ISO 1219 circuit driving a rigid lever (to scale: 1 unit = 100 mm).

Topology encoded in the drawing (NOT stated in the prompt). Y1 energised, Y2 de-energised.
  Valve: Y1 on the LEFT; the left envelope has CROSSED arrows (P->B, A->T).
  Supply (line B) -> cap of cylinder X (Ø80/Ø56, left) and, via a long branch round the right,
         -> ROD-END port of cylinder Y (Ø63/Ø50, right).
  Cylinder X rod-end port -> junction J:
         (a) down through check valve (free downward) -> HOP over the drain line -> DOT on supply;
         (b) right, down through the pilot-operated check (free upward only) -> DOT on drain line.
         The dashed pilot's only dot is on the drain line (0.35 above the supply line).
  Cylinder Y cap -> line A (hops the supply line) -> T -> tank.
  Lever: true pivot = pin on the hatched clevis at 450 mm; the pin at 250 mm carries only a
         spring to a hatched block. All dimensions are baselines from the lever's LEFT END.
         X pin 150, Y pin 700, point L at the tip 1000.
  GTFA v_L = 321 mm/s. See verify.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
from matplotlib.patches import Arc, Circle, Polygon  # noqa: E402
from drawkit import *  # noqa: E402,F403

OUT = Path(__file__).with_name("lever_v1.png")
TILES = "/tmp/claude-0/-home-user-Project-work1/f59a2cfe-32ca-5f2f-841c-18103fedd135/scratchpad/tiles"
fig, ax = new_canvas(13, 13)
R = 0.13
DASH = (0, (5, 3))


def hline(y, x0, x1, hops=(), ls="-", lw=LW):
    s = 1 if x1 > x0 else -1
    cur = x0
    for h in sorted(hops, reverse=s < 0):
        line(ax, [(cur, y), (h - s * R, y)], ls=ls, lw=lw)
        ax.add_patch(Arc((h, y), 2 * R, 2 * R, theta1=0, theta2=180, color=EDGE, lw=lw, zorder=3))
        cur = h + s * R
    line(ax, [(cur, y), (x1, y)], ls=ls, lw=lw)


def vline(x, y0, y1, hops=(), ls="-", lw=LW):
    s = 1 if y1 > y0 else -1
    cur = y0
    for h in sorted(hops, reverse=s < 0):
        line(ax, [(x, cur), (x, h - s * R)], ls=ls, lw=lw)
        ax.add_patch(Arc((x, h), 2 * R, 2 * R, theta1=-90, theta2=90, color=EDGE, lw=lw, zorder=3))
        cur = h + s * R
    line(ax, [(x, cur), (x, y1)], ls=ls, lw=lw)


def check(xc, yc, free, s=0.2):
    """ISO check valve: ball + V seat; free flow from the seat apex toward the ball."""
    d = {"up": (0, 1), "down": (0, -1)}[free]
    ax.add_patch(Circle((xc, yc + d[1] * 0.09), s * 0.72, facecolor="white", edgecolor=EDGE, lw=LW, zorder=6))
    ap = (xc, yc - d[1] * 0.32)
    line(ax, [(xc - s * 1.15, yc - d[1] * 0.02), ap, (xc + s * 1.15, yc - d[1] * 0.02)], z=6)


def vspring(x, y_top, y_bot, n=7, amp=0.14):
    pts, dy = [(x, y_top)], (y_top - y_bot) / (n + 1)
    for i in range(n):
        pts.append((x + (amp if i % 2 == 0 else -amp), y_top - dy * (i + 1)))
    pts.append((x, y_bot))
    line(ax, pts, lw=1.5)


def dim(x1, y, text):
    """Baseline dimension from the lever's left end (x=0) to x1 at height y."""
    line(ax, [(0, y), (x1, y)], lw=0.9, z=2)
    for xa, dx in ((0, 1), (x1, -1)):
        ax.annotate("", xy=(xa, y), xytext=(xa + dx * 0.25, y),
                    arrowprops=dict(arrowstyle="-|>", lw=0.9, color=EDGE, mutation_scale=10), zorder=2)
    line(ax, [(x1, 8.15), (x1, y + 0.12)], lw=0.7, z=2)
    txt(ax, x1 / 2, y + 0.16, text, fs=12)


def cylinder(xc, bore, rod, y0, h, y_lever):
    box(ax, xc - bore / 2, y0, bore, h)
    box(ax, xc - bore / 2, y0 + 0.55 * h, bore, 0.06)                          # piston
    box(ax, xc - rod / 2, y0 + 0.55 * h + 0.06, rod, y_lever - (y0 + 0.55 * h + 0.06), z=3.5)


# ---------------- lever, pins, supports ----------------
YL = 8.0
box(ax, 0.0, YL - 0.11, 10.0, 0.22, z=5)
for x in (1.5, 2.5, 4.5, 7.0):
    ax.add_patch(Circle((x, YL), 0.08, facecolor="white", edgecolor=EDGE, lw=1.4, zorder=7))
ax.add_patch(Polygon([(4.5, YL), (4.18, 7.3), (4.82, 7.3)], closed=True, facecolor="white",
                     edgecolor=EDGE, lw=LW, zorder=4))
ground_hatch(ax, 4.0, 7.05, 1.0, 0.25)
vspring(2.5, YL - 0.1, 6.95)
ground_hatch(ax, 2.2, 6.7, 0.6, 0.25)
line(ax, [(10.0, YL + 0.18), (10.0, YL + 0.42)], lw=1.2)
txt(ax, 10.18, YL + 0.36, "L", ha="left", fs=17)

# ---------------- baseline dimensions (from the left end) ----------------
line(ax, [(0, 8.15), (0, 10.25)], lw=0.7, z=2)
for i, (x, t) in enumerate(((1.5, "150"), (2.5, "250"), (4.5, "450"), (7.0, "700"), (10.0, "1000"))):
    dim(x, 8.5 + 0.42 * i, t)

# ---------------- cylinders ----------------
cylinder(1.5, 0.80, 0.56, 4.4, 2.0, YL - 0.11)            # X: Ø80/Ø56
cylinder(7.0, 0.63, 0.50, 4.6, 2.0, YL - 0.11)            # Y: Ø63/Ø50
txt(ax, 1.0, 5.2, "$\\varnothing 80\\,/\\,\\varnothing 56$", ha="right", fs=12)
txt(ax, 6.55, 5.4, "$\\varnothing 63\\,/\\,\\varnothing 50$", ha="right", fs=12)
X_CAP, X_ROD = (1.5, 4.4), (1.9, 6.1)
Y_CAP, Y_ROD = (7.0, 4.6), (7.315, 6.3)

# ---------------- valve ----------------
VX, VY, SQ, VH = 3.3, 1.6, 1.3, 1.3
for i in range(3):
    box(ax, VX + i * SQ, VY, SQ, VH)
o1, o2 = 0.27, 1.03
# left square (next to Y1): crossed P->B, A->T
line(ax, [(VX + o1, VY + 0.18), (VX + o2, VY + VH - 0.18)], z=6)
arrow(ax, VX + o2 - 0.18, VY + VH - 0.45, 0.15, 0.24)
line(ax, [(VX + o1, VY + VH - 0.18), (VX + o2, VY + 0.18)], z=6)
arrow(ax, VX + o2 - 0.18, VY + 0.45, 0.15, -0.24)
# centre: blocked
cx = VX + SQ
for dx in (o1, o2):
    line(ax, [(cx + dx, VY + VH), (cx + dx, VY + VH - 0.38)], z=6)
    line(ax, [(cx + dx - 0.14, VY + VH - 0.38), (cx + dx + 0.14, VY + VH - 0.38)], z=6)
    line(ax, [(cx + dx, VY), (cx + dx, VY + 0.38)], z=6)
    line(ax, [(cx + dx - 0.14, VY + 0.38), (cx + dx + 0.14, VY + 0.38)], z=6)
# right square: parallel P->A, B->T
rx = VX + 2 * SQ
line(ax, [(rx + o1, VY + 0.18), (rx + o1, VY + VH - 0.18)], z=6)
arrow(ax, rx + o1, VY + VH - 0.42, 0, 0.24)
line(ax, [(rx + o2, VY + VH - 0.18), (rx + o2, VY + 0.18)], z=6)
arrow(ax, rx + o2, VY + 0.42, 0, -0.24)
for xs in (VX - 0.7, VX + 3 * SQ):
    box(ax, xs, VY + 0.28, 0.7, 0.74)
    line(ax, [(xs + 0.14, VY + 0.28), (xs + 0.56, VY + 1.02)], lw=1.4, z=6)
txt(ax, VX - 0.35, VY - 0.28, "Y1", fs=14)
txt(ax, VX + 3 * SQ + 0.35, VY - 0.28, "Y2", fs=14)
PA, PB = cx + o1, cx + o2
for xp, lab, yy in ((PA - 0.2, "A", VY + VH + 0.18), (PB + 0.2, "B", VY + VH + 0.18),
                    (PA - 0.2, "P", VY - 0.18), (PB + 0.2, "T", VY - 0.18)):
    txt(ax, xp, yy, lab, fs=11)

# ---------------- pump, relief, tanks ----------------
pc = (1.0, 0.75)
ax.add_patch(Circle(pc, 0.38, facecolor="white", edgecolor=EDGE, lw=LW, zorder=4))
ax.add_patch(Polygon([(pc[0], pc[1] + 0.36), (pc[0] - 0.17, pc[1] + 0.07), (pc[0] + 0.17, pc[1] + 0.07)],
                     closed=True, facecolor=EDGE, edgecolor=EDGE, zorder=5))
txt(ax, pc[0] - 0.5, pc[1], "$36\\,\\mathrm{L/min}$", ha="right", fs=12)
YPL = 1.2
line(ax, [(pc[0], pc[1] + 0.38), (pc[0], YPL)])
line(ax, [(pc[0], pc[1] - 0.38), (pc[0], 0.12)])
tank(ax, pc[0], 0.12, w=0.6)
dot(ax, pc[0], YPL)
rvx = 2.2
dot(ax, rvx, YPL)
line(ax, [(rvx, YPL), (rvx, 1.0)])
box(ax, rvx - 0.25, 0.35, 0.5, 0.65)
line(ax, [(rvx, 0.45), (rvx, 0.9)], lw=1.3, z=6)
arrow(ax, rvx, 0.75, 0, -0.2, lw=1.3, scale=11)
spring(ax, rvx + 0.25, 0.67, rvx + 0.7, n=4, amp=0.1)
line(ax, [(rvx, 0.35), (rvx, 0.12)])
tank(ax, rvx, 0.12, w=0.6)
line(ax, [(pc[0], YPL), (PA, YPL), (PA, VY)])
line(ax, [(PB, VY), (PB, 0.6)])
tank(ax, PB, 0.6, w=0.6)

# ---------------- supply (line B) ----------------
YS, YD = 3.5, 3.85
line(ax, [(PB, VY + VH), (PB, YS)])
dot(ax, PB, YS)
hline(YS, PB, X_CAP[0])
vline(X_CAP[0], YS, X_CAP[1], hops=[YD])
line(ax, [(PB, YS), (7.9, YS), (7.9, Y_ROD[1]), (Y_ROD[0], Y_ROD[1])])

# ---------------- line A from cylinder Y cap ----------------
line(ax, [(Y_CAP[0], Y_CAP[1]), (Y_CAP[0], 4.15), (PA, 4.15)])
vline(PA, 4.15, VY + VH, hops=[YS])

# ---------------- cylinder X rod-end: regeneration check and pilot-operated check ----------------
JX = 3.0
line(ax, [X_ROD, (JX, X_ROD[1])])
dot(ax, JX, X_ROD[1])
vline(JX, X_ROD[1], YS, hops=[YD])
dot(ax, JX, YS)
check(JX, 5.15, free="down")
PX = 3.85
line(ax, [(JX, X_ROD[1]), (PX, X_ROD[1]), (PX, 5.7)])
box(ax, PX - 0.32, 4.55, 0.64, 1.15)
check(PX, 5.12, free="up")
line(ax, [(PX, 4.55), (PX, YD)])
dot(ax, PX, YD)
# drain line to tank (left)
hline(YD, PX, 0.45)
line(ax, [(0.45, YD), (0.45, 3.1)])
tank(ax, 0.45, 3.1, w=0.6)
# pilot (dashed): from the box side down to a dot on the drain line
line(ax, [(PX - 0.32, 5.35), (3.42, 5.35), (3.42, YD)], ls=DASH, lw=1.4)
dot(ax, 3.42, YD)

save_png(fig, ax, str(OUT), xlim=(-0.3, 10.6), ylim=(-0.1, 10.5), tiles_dir=TILES)
