"""
verify.py — lever v1 (hydraulic circuit driving a rigid lever, 1 DOF). GTFA + misreads.

Correct reading (Y1 energised -> envelope next to Y1 = crossed arrows: P->B, A->T):
  Line B (supply) -> cap of cylinder X (left, Ø80/Ø56, rod up to lever pin at 150 mm from left end O)
                  -> ROD-END port of cylinder Y (right, Ø63/Ø50, rod up to lever pin at 700 mm).
  Cylinder X rod-end port -> junction -> check valve (free toward supply) -> HOP over the
                  drain line -> DOT on the supply line: regeneration.
                  -> pilot-operated check to the drain line; its pilot's only dot is on the
                  drain (tank) line -> stays closed.
  Cylinder Y cap -> line A -> T -> tank.
  Lever: true pivot P (grounded clevis) at 450 mm; S at 250 mm is a pin with a spring to the
  ceiling (not a pivot). All dimensions are baselines from the left end O.
  1 DOF: Q = w (aX * A_Xrod + aY * A_Yann);  v_L = w * aL.
"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
sys.path.insert(0, str(HERE))
from misreads import Misread, fmt_sig, report  # noqa: E402
from model import D, MIS, vL  # noqa: E402

SIG = 3


def closed_form():
    Q = 36e6 / 60                                  # mm^3/s
    aX, aY, aL = 450 - 150, 700 - 450, 1000 - 450
    AXrod = math.pi * 56 ** 2 / 4
    AYann = math.pi * (63 ** 2 - 50 ** 2) / 4
    w = Q / (aX * AXrod + aY * AYann)
    return w * aL, w, aX, aY, aL, AXrod, AYann


if __name__ == "__main__":
    g = vL()
    g2, w, aX, aY, aL, AXrod, AYann = closed_form()
    assert abs(g - g2) < 1e-9 * g
    print(f"aX={aX} aY={aY} aL={aL}  A_Xrod={AXrod:.6g}  A_Yann={AYann:.6g}")
    print(f"denominator={aX*AXrod + aY*AYann:.6g}  w={w:.6g} rad/s")
    print(f"vX={w*aX:.6g}  vY={w*aY:.6g}  vL={g:.6g} mm/s -> GTFA {fmt_sig(g, SIG)}\n")
    rows = [Misread(n, vL(**kw)) for n, kw in MIS if not kw.get("swap_dims")]
    rows.append(Misread("POCV pilot read from supply (opens -> no regen)", vL(regen=False),
                        note="same value as the hop read; a second independent route to the same value"))
    report(g, rows, sig=SIG, signed=False)
