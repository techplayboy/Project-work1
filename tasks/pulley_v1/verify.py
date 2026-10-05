"""
verify.py — pulley v1 (three blocks, stepped drum, four ropes). GTFA + misreads.

Correct reading (y up, free end pulled DOWN at U):
  Rope 1: free end E -> over fixed F1 -> round PA (strap to A) -> up to the OUTER groove
          of drum D (leaves the drum on its LEFT side).
  Rope 2: INNER groove of D (leaves on the RIGHT side, so opposite sense to rope 1)
          -> down round PB (strap up to B) -> up to a dot on the UNDERSIDE of bar A.
  Rope 3: ceiling dot -> down round PC (strap down to C) -> up round PF (high pulley whose
          long strap goes DOWN to bar A) -> down to a dot on top of bar A.
  Rope 4: dot on top of C -> up over fixed F2 -> down round PB2 (strap up to B) -> up to ceiling.
Unknowns: vA, vB, vC, drum w.  Four rope-length equations.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))
sys.path.insert(0, str(HERE))
import numpy as np  # noqa: E402
from misreads import Misread, fmt_sig, report  # noqa: E402
from solver import solve  # noqa: E402

SIG = 3
U = 1.2                     # m/s, free end pulled down
R, r = 0.150, 0.060         # drum groove radii, m
H = dict(A=6.0, B=4.6, C=2.4)


def ropes(m=()):
    m = set(m)
    rR, rr = (r, R) if "groove_swap" in m else (R, r)
    s2 = +1 if "same_sense" in m else -1
    pf = "G" if "PF_fixed" in m else "A"
    pb = "A" if "PB_hanger_A" in m else ("C" if "PB_hanger_C" in m else "B")
    pc = "B" if "PC_hanger_B" in m else "C"
    pa = "G" if "PA_fixed" in m else "A"
    r2end = ("end", "G", 10.0) if "r2_to_ceiling" in m else ("end", "A", 6.3)
    rope1 = [("end", "E", 3.0), ("over", "G", 9.5), ("over", pa, 6.0), ("drum", "D", 9.5, rR, +1)]
    rope2 = [("drum", "D", 9.5, rr, s2), ("over", pb, 4.6), r2end]
    rope3 = [("end", "G", 10.0), ("over", pc, 2.4), ("over", pf, 8.6), ("end", "A", 6.3)]
    rope4 = [("end", "C", 2.7), ("over", "G", 9.5), ("over", "B", 4.6), ("end", "G", 10.0)]
    return [rope1, rope2, rope3, rope4]


def v(m=(), want="C"):
    return solve(["A", "B", "C"], ["D"], ropes(m), {"E": -U}, want)


def closed_form():
    """Hand derivation (y up, w = drum rate, vE = -U):
       rope 1: -vE - 2 vA + R w = 0
       rope 2: -r w - 2 vB + vA = 0
       rope 3: -2 vC + vA = 0          -> vA = 2 vC
       rope 4: -vC - 2 vB = 0          -> vB = -vC / 2
       => w = (vA - 2 vB)/r = 3 vC / r ;  U - 4 vC + 3 (R/r) vC = 0
       => vC = -U / (3 R/r - 4)"""
    return -U / (3 * R / r - 4)


if __name__ == "__main__":
    g = v()
    assert abs(g - closed_form()) < 1e-12
    print({k: round(v(want=k), 6) for k in "ABCD"})
    print(f"GTFA vC = {g:.6g} m/s = {g*1000:.6g} mm/s -> {fmt_sig(g*1000, SIG)}")
    rows = [
        Misread("drum ropes read as same winding sense", v(("same_sense",)) * 1000),
        Misread("PB strap read as hanging from A", v(("PB_hanger_A",)) * 1000),
        Misread("PA read as a fixed pulley", v(("PA_fixed",)) * 1000),
        Misread("drum grooves swapped", v(("groove_swap",)) * 1000),
        Misread("PC strap read as hanging from B", v(("PC_hanger_B",)) * 1000),
        Misread("high pulley PF read as fixed to ceiling", v(("PF_fixed",)) * 1000),
        Misread("rope 2 end read as anchored to ceiling", v(("r2_to_ceiling",)) * 1000),
    ]
    report(g * 1000, rows, sig=SIG, signed=True)
