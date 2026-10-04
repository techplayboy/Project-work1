"""
verify.py — gearbox v4 (three coupled planetary sets). Independent GTFA + misread table.

Correct reading (what the drawing shows), K1 + F2 engaged, K2 + F1 released:
  Rotating groups:  A (input, 1450 rpm) = {shaft A, K1 drum, R1, S3}
                    X = {S1, inner sleeve, C3}
                    Y = {C1, outer sleeve, S2}
                    Z = {C2 (both pins), outer drum, R3, output D}
                    0 = {R2 via F2}
  PG1 stepped planet: S1=X, C1=Y, R1=A      (S1-C1) = -(zR1/zPb)(zPa/zS1) (R1-C1)
  PG2 double planet:  S2=Y, C2=Z, R2=0      (S2-C2) = +k2 (R2-C2),  k2 = zR2/zS2
  PG3 simple planet:  S3=A, C3=X, R3=Z      (S3-C3) = -k3 (R3-C3),  k3 = zR3/zS3
  Requested: speed of D = Z, positive in the sense of A.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve()
while not (ROOT / ".claude").exists() and ROOT != ROOT.parent:
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / ".claude/skills/lumiere-task/scripts"))

import numpy as np
from misreads import Misread, fmt_sig, report, unique_solution

SIG = 3
nA = 1450.0
z = dict(S1=36, Pa=13, Pb=32, R1=81,    # m = 2.5, STEPPED planet (Pa meshes S1, Pb meshes R1, one pin)
         S2=28, Pi=18, Po=21, R2=94,     # m = 2, DOUBLE planet (inner Pi meshes S2, outer Po meshes R2)
         S3=31, P3=21, R3=73)            # m = 3, simple planet
k1, k2, k3 = z["R1"] / z["S1"], z["R2"] / z["S2"], z["R3"] / z["S3"]

# basic (signed) train values  e = (S-C)/(R-C)
E_SINGLE1 = -(z["R1"] / z["Pb"]) * (z["Pa"] / z["S1"])     # PG1 stepped planet (correct)
E_SINGLE3 = -k3
E_DOUBLE2 = +k2
E_STEPPED2 = -(z["Pi"] / z["S2"]) * (z["R2"] / z["Po"])   # misread: Pi and Po on one pin

CORRECT = [("X", "Y", "A"), ("Y", "Z", "0"), ("A", "X", "Z")]
IDX = {"X": 0, "Y": 1, "Z": 2}


def build(sets, e=(E_SINGLE1, E_DOUBLE2, E_SINGLE3)):
    """Each set (S, C, R) gives S - C - e(R - C) = 0. Members are X/Y/Z, 'A' or '0'."""
    M, b = np.zeros((3, 3)), np.zeros(3)
    for i, ((S, C, R), ei) in enumerate(zip(sets, e)):
        for m, c in ((S, 1.0), (C, -1.0 + ei), (R, -ei)):
            if m == "A":
                b[i] -= c * nA
            elif m != "0":
                M[i, IDX[m]] += c
    return M, b


def solve(sets, out="Z", e=(E_SINGLE1, E_DOUBLE2, E_SINGLE3)):
    M, b = build(sets, e)
    if not unique_solution(M, b):
        return float("nan"), False
    return np.linalg.solve(M, b)[IDX[out]], True


def closed_form():
    # Y = (1-k2) Z ; X = (1+p) Y - p A ; A + k3 Z = (1+k3) X   with p = -E_SINGLE1
    p = -E_SINGLE1
    return nA * (1 + p + p * k3) / ((1 + p) * (1 + k3) * (1 - k2) - k3)


def mis(name, sets=CORRECT, out="Z", e=(E_SINGLE1, E_DOUBLE2, E_SINGLE3), note=""):
    v, ok = solve(sets, out, e)
    return Misread(name, v, solvable=ok, note=note)


if __name__ == "__main__":
    g, _ = solve(CORRECT)
    g2 = closed_form()
    assert abs(g - g2) < 1e-9 * abs(g), (g, g2)
    M, b = build(CORRECT)
    x = np.linalg.solve(M, b)
    print(f"e1={E_SINGLE1:.6g} k2={k2:.6g} k3={k3:.6g}")
    print(f"X={x[0]:.6g}  Y={x[1]:.6g}  Z=D={x[2]:.6g}   (two methods agree)")
    print(f"GTFA -> {fmt_sig(g, SIG)} rpm\n")

    rows = [
        mis("1 shaft A fixed to S1 where it passes", [("A", "Y", "A"), ("Y", "Z", "0"), ("A", "X", "Z")],
            note="PG1 locks: Y = A, so Z = A/(1-k2)"),
        mis("2 PG2 read as single-planet set", e=(E_SINGLE1, -k2, E_SINGLE3)),
        mis("3 PG2 read as stepped planet (one pin)", e=(E_SINGLE1, E_STEPPED2, E_SINGLE3)),
        mis("4 F2 read as holding S2 (default)", [("X", "0", "A"), ("0", "Z", "Y"), ("A", "X", "Z")],
            note="C1=S2=0; Y now stands for the freed ring R2 (fixed by the PG2 row alone)"),
        mis("5 output taken from carrier C3 (default)", out="X"),
        mis("6 inner shaft ends swapped (A->C3, sleeve->S3)", [("X", "Y", "A"), ("Y", "Z", "0"), ("X", "A", "Z")]),
        mis("8 PG1 stepped read as simple planet", e=(-k1, E_DOUBLE2, E_SINGLE3)),
        mis("7 K1 read as driving C1 (R1 on sleeve)", [("X", "A", "Y"), ("Y", "Z", "0"), ("A", "X", "Z")]),
    ]
    report(g, rows, sig=SIG, signed=True)
