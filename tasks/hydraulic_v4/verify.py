"""
verify.py — hydraulic v4 (bleed-off + series + flow divider + regeneration).

Correct reading (Y1 energised, Y2 de-energised):
  DCV 3: the envelope next to Y1 (drawn on the RIGHT) is active; it is drawn with
         crossed arrows, so P->B and A->T.
  Pump 1 (Q) -> P -> B.  Bleed-off FCV 8 tees into line B (dot) -> tank: passes Qf.
  Line B -> CAP port of cylinder 4 (cyl 4 drawn with its rod exiting LEFT, cap on right).
  Rod port of cyl 4 -> inlet of flow divider 7 (hops over line B).
  Divider outlet marked p2 % -> cap of cylinder 5 ; outlet (100-p2) % -> cap of cylinder 6
         (the two outlet lines cross with a hop).
  Cyl 5 rod port -> junction: (a) check valve 9, free flow rod -> cap of cyl 5;
         (b) pilot-operated check 10 to line A, free flow only A -> rod.
  POCV 10 pilot (dashed) is taken from line A (tank pressure) -> stays closed.
  => cylinder 5 is regenerative:  v5 = q5 / A_rod5.
  Cyl 6 rod -> line A -> T.
Requested: speed of the piston of cylinder 5 in mm/s.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
from misreads import Misread, fmt_sig, report  # noqa: E402

SIG = 3
LPM = 1e6 / 60.0                      # L/min -> mm^3/s
D = dict(Q=36.0, Qf=8.0, p5=0.60,      # pump, FCV setting (L/min), divider share to cyl 5
         b4=80.0, r4=56.0, b5=63.0, r5=40.0, b6=40.0, r6=28.0)


def area(d):
    return math.pi * d * d / 4


def v5(d=D, envelope="PB", fcv="bleedB", cyl4="capright", split="p5", regen=True, dims5=("b5", "r5")):
    A4c, A4r = area(d["b4"]), area(d["b4"]) - area(d["r4"])
    b5, r5 = d[dims5[0]], d[dims5[1]]
    A5c, A5rod = area(b5), area(r5)
    Q = d["Q"] * LPM
    if envelope == "PA":           # parallel box read as active: pump to line A -> POCV free flow -> cyl 5 rod side
        q = Q                       # FCV now on the tank-connected line B: no bleed
        return q / (A5c - A5rod)    # cyl 5 retracts on its annulus
    q_in4 = {"bleedB": Q - d["Qf"] * LPM, "none": Q, "meterin": d["Qf"] * LPM}[fcv]
    if cyl4 == "capright":
        v4 = q_in4 / A4c; q_out4 = v4 * A4r
    else:                           # misread: line B enters the rod side
        v4 = q_in4 / A4r; q_out4 = v4 * A4c
    share = d["p5"] if split == "p5" else 1 - d["p5"]
    q5 = share * q_out4
    return q5 / A5rod if regen else q5 / A5c


if __name__ == "__main__":
    g = v5()
    # independent closed form
    A4c = area(80); A4r = A4c - area(56)
    g2 = (28 * LPM) * (A4r / A4c) * 0.60 / area(40)
    assert abs(g - g2) < 1e-9 * g
    print(f"GTFA v5 = {g:.6g} mm/s -> {fmt_sig(g, SIG)}\n")
    rows = [
        Misread("1 parallel envelope active (P->A)", v5(envelope="PA")),
        Misread("2 cyl 4 read rod-left/cap-left (B to rod side)", v5(cyl4="capleft")),
        Misread("3 FCV read on line A (no bleed)", v5(fcv="none")),
        Misread("4 FCV read as meter-in on B", v5(fcv="meterin")),
        Misread("5 divider outlets swapped (40 % to cyl 5)", v5(split="other")),
        Misread("6 POCV pilot read from B (open, no regen)", v5(regen=False)),
        Misread("7 cyl 5 / cyl 6 dimensions swapped", v5(dims5=("b6", "r6"))),
    ]
    report(g, rows, sig=SIG, signed=False)
    A4c, A4r, A5c, A5r = area(80), area(80) - area(56), area(63), area(40)
    q4 = 28 * LPM; v4 = q4 / A4c; q4o = v4 * A4r; q5 = 0.6 * q4o
    print(f"\nA4c={A4c:.6g} A4ann={A4r:.6g} A5c={A5c:.6g} A5rod={A5r:.6g} A5ann={A5c-A5r:.6g}")
    print(f"q_in4={q4:.6g} v4={v4:.6g} q_out4={q4o:.6g} q5={q5:.6g} q6={0.4*q4o:.6g} v5={q5/A5r:.6g}")
    print(f"check: cyl5 cap inflow = q5 + v5*A5ann = {q5 + q5/A5r*(A5c-A5r):.6g} = v5*A5c = {q5/A5r*A5c:.6g}")
