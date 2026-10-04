"""
verify.py — independent GTFA and misread table for <task name>.

Copy into tasks/<task>/verify.py. Encode the CORRECT reading as data, write one solve()
that takes a reading, then express every misread as a modified reading. Compute the GTFA
two ways (e.g. linear solve + closed form) and assert they agree.

Run:  python3 tasks/<task>/verify.py
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

# ---- data drawn in the figure -------------------------------------------------
DATA = dict(
    # e.g. n_A=1450.0, zS1=28, zR1=80, ...
)

# ---- the correct reading (topology / states) ----------------------------------
CORRECT = dict(
    # e.g. K1="A->R1", F2="C2", output="R2", planet2="double",
)


def build(reading, d=DATA):
    """Return (A, b) of the linear system for this reading."""
    raise NotImplementedError


def solve(reading):
    A, b = build(reading)
    x = np.linalg.solve(A, b)
    return x  # pick the requested quantity below


def requested(x):
    raise NotImplementedError


def closed_form():
    """Independent route to the GTFA (hand derivation)."""
    raise NotImplementedError


if __name__ == "__main__":
    g = requested(solve(CORRECT))
    g2 = closed_form()
    assert abs(g - g2) < 1e-6 * max(1, abs(g)), (g, g2)
    print(f"GTFA (two methods agree): {g:.6g} -> {fmt_sig(g, SIG)}\n")

    def mis(name, **changes):
        r = {**CORRECT, **changes}
        A, b = build(r)
        ok = unique_solution(A, b)
        val = requested(np.linalg.lstsq(A, b, rcond=None)[0]) if ok else float("nan")
        return Misread(name, val, solvable=ok)

    rows = [
        # mis("double planet read as stepped", planet2="stepped"),
        # mis("K1 joins A to sun shaft", K1="A->S"),
    ]
    report(g, rows, sig=SIG, signed=True)

    # ---- reproduce real model answers here after testing --------------------
    # print("Response 1 reading ->", fmt_sig(requested(solve({**CORRECT, ...})), SIG))
