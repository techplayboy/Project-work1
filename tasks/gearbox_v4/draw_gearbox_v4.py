"""
Gearbox v4 — three coupled planetary sets, kinematic half-section (above the centreline).

Topology encoded in the drawing (NOT stated in the prompt):
  Shaft A (1450 rpm, innermost line y=0.5): disk at x=1.2 up to two clutch packs.
      K1 (upper pack): A disk <-> drum y=6.4 -> ring R1                 [engaged]
      K2 (lower pack): A disk <-> left riser of inner sleeve X           [released]
      A runs under S1 and S2 (not attached) and ends fixed to sun S3.
  Inner sleeve X (y=0.95): carries S1, runs under PG2, rises at x=12.95 as the
      LEFT plate of carrier C3.
  Outer sleeve Y (y=1.4): starts at carrier C1's right plate (x=5.0), carries S2.
  PG1 is a STEPPED planet: Pa (z13) meshes S1, Pb (z32) meshes R1, both on ONE pin.
  PG2 is a DOUBLE planet: Pi (z18) meshes S2 and Po; Po (z21) meshes Pi and R2;
      each on its OWN pin; both pins to carrier plate C2 (x=9.3), which rises to the
      outer drum (y=7.2).
  Outer drum (y=7.2) runs over PG3, descends at x=15.0; ring R3's flange joins it
      (dot); it continues down to output shaft D (y=0.5, right).
  F2 grounds ring R2 [engaged];  F1 on the outer drum [released].
  Teeth/modules: PG1 S36 Pa13 Pb32 R81 m2.5 | PG2 S28 Pi18 Po21 R94 m2 | PG3 S31 P21 R73 m3
  GTFA n_D = -337 rpm (reverse). See verify.py.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
from drawkit import *  # noqa: E402,F403

OUT = Path(__file__).with_name("gearbox_v4.png")
GW = 0.45            # gear rectangle width
LFS = 12             # gear label font size

fig, ax = new_canvas(17, 9.5)

Y_A, Y_X, Y_Y = 0.5, 0.95, 1.4
Y_K1, Y_DRUM = 6.4, 7.2


def gear(x, y0, y1, lab, side="left", dy=0.0, dx=0.0):
    box(ax, x - GW / 2, y0, GW, y1 - y0, z=5)
    xt = (x - GW / 2 - 0.12 if side == "left" else x + GW / 2 + 0.12) + dx
    txt(ax, xt, (y0 + y1) / 2 + dy, lab, ha="right" if side == "left" else "left", fs=LFS)


def pack(x, yc, h=0.8, gap=0.16):
    """Friction element: two thick plates facing each other at x, x+gap."""
    for xx in (x, x + gap):
        line(ax, [(xx, yc - h / 2), (xx, yc + h / 2)], lw=4.0, z=6)


def brake(xc, y, w=0.9):
    """Radial friction pair at height y (member plate below, housing plate above)."""
    for yy in (y, y + 0.18):
        line(ax, [(xc - w / 2, yy), (xc + w / 2, yy)], lw=4.0, z=6)
    ground_hatch(ax, xc - w / 2 - 0.2, y + 0.28, w + 0.4, 0.4)


# ---- centreline
line(ax, [(-0.2, 0), (17.2, 0)], lw=1.0, ls=(0, (8, 3, 2, 3)))

# ---- shaft A, disk, clutch packs K1 / K2
line(ax, [(-0.2, Y_A), (13.5, Y_A)])                    # A ... ends in sun S3
line(ax, [(1.2, Y_A), (1.2, Y_K1)])                     # A disk
dot(ax, 1.2, Y_A)
line(ax, [(1.2, Y_K1), (1.45, Y_K1)])
pack(1.45, Y_K1)
line(ax, [(1.61, Y_K1), (3.75, Y_K1), (3.75, 4.7)])     # K1 drum -> R1
txt(ax, 1.53, Y_K1 + 0.75, "K1", fs=14)
line(ax, [(1.2, 2.2), (1.45, 2.2)])
pack(1.45, 2.2, h=0.7)
line(ax, [(1.61, 2.2), (1.85, 2.2), (1.85, Y_X), (12.95, Y_X), (12.95, 3.0)])  # sleeve X -> C3
txt(ax, 1.53, 2.9, "K2", fs=14)

# ---- PG1  stepped planet (sun column x=3.2, ring column x=3.75, one pin y=2.9)
gear(3.2, Y_X, 2.3, "$z\\,36$\n$m\\,2.5$")
gear(3.2, 2.3, 3.5, "$z\\,13$\n$m\\,2.5$")
gear(3.75, 1.7, 4.1, "$z\\,32$\n$m\\,2.5$", side="right", dy=-0.55)
gear(3.75, 4.1, 4.7, "$z\\,81$\n$m\\,2.5$", dy=0.05)
line(ax, [(3.2, 2.9), (5.0, 2.9), (5.0, Y_Y), (8.5, Y_Y)])    # pin -> C1 -> sleeve Y -> S2

# ---- PG2  double planet (x = 8.5)
gear(8.5, Y_Y, 2.4, "$z\\,28$\n$m\\,2$")
gear(8.5, 2.4, 3.4, "$z\\,18$\n$m\\,2$")
gear(8.5, 3.4, 4.4, "$z\\,21$\n$m\\,2$")
gear(8.5, 4.4, 5.0, "$z\\,94$\n$m\\,2$", dy=0.05)
line(ax, [(8.5, 2.9), (9.3, 2.9)])
line(ax, [(8.5, 3.9), (9.3, 3.9)])
line(ax, [(9.3, 2.9), (9.3, Y_DRUM), (15.0, Y_DRUM), (15.0, Y_A), (17.2, Y_A)])  # C2 -> drum -> D
dot(ax, 9.3, 3.9)
line(ax, [(8.5, 5.0), (8.5, 5.45)])
brake(8.5, 5.45)
txt(ax, 7.75, 5.55, "F2", ha="right", fs=14)

# ---- PG3  simple planet (x = 13.5)
gear(13.5, Y_A, 2.2, "$z\\,31$\n$m\\,3$", side="right", dy=0.25)
gear(13.5, 2.2, 3.8, "$z\\,21$\n$m\\,3$", side="right")
gear(13.5, 3.8, 4.4, "$z\\,73$\n$m\\,3$", dy=0.05)
line(ax, [(12.95, 3.0), (13.5, 3.0)])                   # C3 pin (left plate = sleeve X)
line(ax, [(13.5 + GW / 2, 4.1), (15.0, 4.1)])           # R3 flange to drum
dot(ax, 15.0, 4.1)
# F1 on the outer drum (released)
line(ax, [(11.7, Y_DRUM), (11.7, Y_DRUM + 0.2)])
brake(11.7, Y_DRUM + 0.2, w=1.0)
txt(ax, 11.0, Y_DRUM + 0.3, "F1", ha="right", fs=14)

# ---- labels A / D and speed
txt(ax, -0.25, Y_A + 0.42, "A", ha="left", fs=16)
txt(ax, -0.25, Y_A - 0.30, "$1450\\,\\mathrm{rpm}$", ha="left", fs=13)
txt(ax, 17.2, Y_A + 0.42, "D", ha="right", fs=16)

save_png(fig, ax, str(OUT), xlim=(-0.6, 17.5), ylim=(-0.6, 8.4))
