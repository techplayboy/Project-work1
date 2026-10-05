"""
Pulley v1 — front elevation of a hoist with a stepped drum and four ropes.

Topology encoded in the drawing (NOT stated in the prompt). Fastenings are filled dots;
a rope crossing a bar without a dot is not fastened to it. Straps (thick lines) carry
pulley axles to their member.
  Rope 1: free end (x=0.65, pulled down 1.2 m/s) -> over F1 (ceiling) -> round PA (strap to
          bar A) -> up to the OUTER groove of drum D, leaving the drum's LEFT side.
  Rope 2: INNER groove of D, leaving its RIGHT side -> down (crossing bar A) round PB (strap up
          to bar B) -> up (crossing bar B) to a dot on the UNDERSIDE of bar A.
  Rope 3: ceiling dot -> down (crossing A and B) round PC (strap down to block C) -> up round PF,
          a pulley just under the ceiling whose long strap runs DOWN to bar A -> down to a dot on
          top of bar A.
  Rope 4: dot on top of C -> up over F2 (ceiling) -> down round PB2 (strap up to bar B) -> up
          (crossing B) to a ceiling dot.
  Drum radii: outer 150 mm, inner 60 mm.  GTFA vC = -343 mm/s. See verify.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
from matplotlib.patches import Arc  # noqa: E402
from drawkit import *  # noqa: E402,F403

OUT = Path(__file__).with_name("pulley_v1.png")
fig, ax = new_canvas(11, 12.5)
RL = 1.6          # rope line width
ST = 4.2          # strap line width
YCEIL = 10.0


def rope(pts):
    line(ax, pts, lw=RL, z=6)


def strap(p0, p1):
    line(ax, [p0, p1], lw=ST, z=5)


def pulley(x, y, rho, top_wrap):
    """Pulley disc with axle; rope wrap arc on the top (fixed-type) or bottom (hanging-type)."""
    circle(ax, x, y, rho, z=7)
    ax.plot([x], [y], marker="o", ms=4.5, color=EDGE, zorder=9)
    t1, t2 = (0, 180) if top_wrap else (180, 360)
    ax.add_patch(Arc((x, y), 2 * rho, 2 * rho, theta1=t1, theta2=t2, color=EDGE, lw=RL + 1.2, zorder=8))


def bar(x0, x1, yc, lab, h=0.3, lab_xy=None):
    box(ax, x0, yc - h / 2, x1 - x0, h, z=4)
    lx, ly = lab_xy if lab_xy else (x0 - 0.18, yc)
    txt(ax, lx, ly, lab, ha="right" if not lab_xy else "center", fs=17)


# ---------------- ceiling ----------------
ground_hatch(ax, -0.1, YCEIL, 9.2, 0.35)

# ---------------- drum D (fixed axle) ----------------
DX, DY, RO, RI = 3.0, 9.0, 0.75, 0.30
strap((DX, DY), (DX, YCEIL)); dot(ax, DX, YCEIL)
circle(ax, DX, DY, RO, z=7)
circle(ax, DX, DY, RI, z=7)
ax.plot([DX], [DY], marker="o", ms=5, color=EDGE, zorder=9)
ax.add_patch(Arc((DX, DY), 2 * RO, 2 * RO, theta1=90, theta2=180, color=EDGE, lw=RL + 1.2, zorder=8))
ax.add_patch(Arc((DX, DY), 2 * RI, 2 * RI, theta1=0, theta2=90, color=EDGE, lw=RL + 1.2, zorder=8))
txt(ax, DX + 0.95, DY + 0.55, "$150\\,\\mathrm{mm}$", ha="left", fs=12)
line(ax, [(DX + 0.93, DY + 0.5), (DX + 0.53, DY + 0.53)], lw=0.9, z=9)
txt(ax, DX - 0.95, DY + 0.55, "$60\\,\\mathrm{mm}$", ha="right", fs=12)
line(ax, [(DX - 0.93, DY + 0.5), (DX - 0.21, DY + 0.21)], lw=0.9, z=9)

# ---------------- fixed pulleys F1, F2 ----------------
F1 = (1.0, 9.2, 0.35)
F2 = (7.35, 9.3, 0.35)
for (x, y, p) in (F1, F2):
    strap((x, y), (x, YCEIL)); dot(ax, x, YCEIL)
    pulley(x, y, p, top_wrap=True)

# ---------------- bars A, B and block C ----------------
YA, YB = 6.0, 4.4
bar(1.0, 6.65, YA, "A", lab_xy=(1.22, YA - 0.45))
bar(2.6, 8.55, YB, "B")
box(ax, 4.6, 1.3, 2.7, 0.9, z=4)
txt(ax, 5.95, 1.75, "C", fs=17)

# ---------------- moving pulleys ----------------
PA = (1.80, 6.8, 0.45)            # strap down to bar A (pulley sits above A)
PF = (6.10, 8.6, 0.35)            # high pulley, long strap down to bar A
PB = (3.65, 3.6, 0.35)            # strap up to bar B
PB2 = (8.05, 3.7, 0.35)           # strap up to bar B
PC = (5.40, 2.75, 0.35)           # strap down to C
strap((PA[0], PA[1]), (PA[0], YA + 0.15)); dot(ax, PA[0], YA + 0.15)
strap((PF[0], PF[1]), (PF[0], YA + 0.15)); dot(ax, PF[0], YA + 0.15)
strap((PB[0], PB[1]), (PB[0], YB - 0.15)); dot(ax, PB[0], YB - 0.15)
strap((PB2[0], PB2[1]), (PB2[0], YB - 0.15)); dot(ax, PB2[0], YB - 0.15)
strap((PC[0], PC[1]), (PC[0], 2.2)); dot(ax, PC[0], 2.2)
pulley(*PA, top_wrap=False)
pulley(*PF, top_wrap=True)
pulley(*PB, top_wrap=False)
pulley(*PB2, top_wrap=False)
pulley(*PC, top_wrap=False)

# ---------------- rope 1 ----------------
xE = F1[0] - F1[2]
rope([(xE, 2.7), (xE, F1[1])])
rope([(F1[0] + F1[2], F1[1]), (F1[0] + F1[2], PA[1])])
rope([(PA[0] + PA[2], PA[1]), (PA[0] + PA[2], DY)])           # to outer groove, left side
arrow(ax, xE, 3.3, 0, -0.9, lw=2.0, scale=20)
txt(ax, xE + 0.2, 2.3, "$1.2\\,\\mathrm{m/s}$", ha="left", fs=13)

# ---------------- rope 2 ----------------
rope([(DX + RI, DY - 0.9), (DX + RI, PB[1])])                 # inner groove, right side
line(ax, [(DX + RI, DY), (DX + RI, DY - 0.9)], lw=RL, z=8)   # drawn over the outer disc
rope([(PB[0] + PB[2], PB[1]), (PB[0] + PB[2], YA - 0.15)])
dot(ax, PB[0] + PB[2], YA - 0.15)

# ---------------- rope 3 ----------------
rope([(PC[0] - PC[2], YCEIL), (PC[0] - PC[2], PC[1])]); dot(ax, PC[0] - PC[2], YCEIL)
rope([(PC[0] + PC[2], PC[1]), (PC[0] + PC[2], PF[1])])
rope([(PF[0] + PF[2], PF[1]), (PF[0] + PF[2], YA + 0.15)]); dot(ax, PF[0] + PF[2], YA + 0.15)

# ---------------- rope 4 ----------------
rope([(F2[0] - F2[2], 2.2), (F2[0] - F2[2], F2[1])]); dot(ax, F2[0] - F2[2], 2.2)
rope([(F2[0] + F2[2], F2[1]), (F2[0] + F2[2], PB2[1])])
rope([(PB2[0] + PB2[2], PB2[1]), (PB2[0] + PB2[2], YCEIL)]); dot(ax, PB2[0] + PB2[2], YCEIL)

save_png(fig, ax, str(OUT), xlim=(-0.4, 9.4), ylim=(1.0, 10.6),
         tiles_dir="/tmp/claude-0/-home-user-Project-work1/f59a2cfe-32ca-5f2f-841c-18103fedd135/scratchpad/tiles")
