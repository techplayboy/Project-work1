"""
misreads — check that every trap in a Lumière task is usable.

A misread is usable only if it gives a POSITIVE (or convention-plausible), ordinary-looking
answer, leaves a uniquely solvable problem, and is >= 25 % from the GTFA. Use from verify.py:

    import sys; sys.path.insert(0, ".claude/skills/lumiere-task/scripts")
    from misreads import Misread, report, round_sig, unique_solution

    gtfa = solve(correct_reading)
    rows = [
        Misread("double planet read as stepped", solve(stepped), solvable=True),
        Misread("K1 joins A to sun shaft", solve(k1_sun), solvable=unique_solution(A, b)),
    ]
    report(gtfa, rows, sig=3, signed=True)

`signed=True` when a negative answer is legitimate under a stated sign convention (then the
check is that the misread is not absurd in magnitude, and a sign flip alone is flagged).
"""
import math
from dataclasses import dataclass, field

try:
    import numpy as np
except ImportError:  # numpy only needed for unique_solution
    np = None


def round_sig(x, sig=3):
    if x == 0 or not math.isfinite(x):
        return x
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)


def fmt_sig(x, sig=3):
    r = round_sig(x, sig)
    if abs(r) >= 10 ** (sig - 1):
        return str(int(round(r)))
    return f"{r:.{sig}g}"


def unique_solution(A, b=None, tol=1e-9):
    """True if the linear system A x = b has exactly one solution (full rank, consistent)."""
    A = np.atleast_2d(np.asarray(A, float))
    n = A.shape[1]
    rA = np.linalg.matrix_rank(A, tol)
    if b is None:
        return rA == n
    Ab = np.column_stack([A, np.asarray(b, float)])
    return rA == n and np.linalg.matrix_rank(Ab, tol) == rA


@dataclass
class Misread:
    name: str
    value: float | str
    solvable: bool = True          # misread problem still has exactly one answer?
    note: str = ""
    flags: list = field(default_factory=list)


def report(gtfa, rows, sig=3, signed=False, min_dist=0.25, max_ratio=20.0):
    """Print the trap table and return True if every misread is usable."""
    discrete = isinstance(gtfa, str)
    g_r = gtfa if discrete else round_sig(gtfa, sig)
    print(f"GTFA = {gtfa if discrete else f'{gtfa:.6g}'}  ->  reported {g_r if discrete else fmt_sig(gtfa, sig)}")
    print(f"{'#':>2}  {'misread':<44} {'value':>12} {'dist':>8}  flags")
    ok = True
    seen = {}
    for i, m in enumerate(rows, 1):
        m.flags = []
        if discrete or isinstance(m.value, str):
            dist_s = "—"
            if m.value == gtfa:
                m.flags.append("EQUALS GTFA")
            key = m.value
        else:
            v = m.value
            if not math.isfinite(v):
                m.flags.append("NON-FINITE")
                dist = float("nan")
            else:
                dist = abs(v - gtfa) / abs(gtfa) if gtfa else float("inf")
                if dist < min_dist:
                    m.flags.append(f"<{int(min_dist*100)}% FROM GTFA")
                if not signed and v <= 0:
                    m.flags.append("NON-POSITIVE (model will self-correct)")
                if signed and gtfa and round_sig(v, sig) == -round_sig(gtfa, sig):
                    m.flags.append("PURE SIGN FLIP (looks like a convention slip)")
                if gtfa and v and (abs(v / gtfa) > max_ratio or abs(gtfa / v) > max_ratio):
                    m.flags.append("ABSURD MAGNITUDE?")
                if round_sig(v, sig) == g_r:
                    m.flags.append("ROUNDS TO GTFA")
                if abs(g_r) >= 10 ** (sig - 1) and abs(round_sig(v, sig)) < 10 ** (sig - 1):
                    m.flags.append(f"NOT WHOLE AT {sig} S.F. (GTFA is whole; FORMAT_MISMATCH as distractor)")
            dist_s = f"{dist*100:6.1f}%"
            key = round_sig(v, sig)
        if key in seen:
            m.flags.append(f"DUPLICATES #{seen[key]}")
        if not (discrete or isinstance(m.value, str)) and math.isfinite(m.value):
            for j, o in enumerate(rows[:i - 1], 1):
                ov = o.value
                if isinstance(ov, (int, float)) and math.isfinite(ov) and max(abs(ov), abs(m.value)) and \
                        abs(ov - m.value) / max(abs(ov), abs(m.value)) < 0.10 and round_sig(ov, sig) != key:
                    m.flags.append(f"<10% FROM #{j}")
        seen.setdefault(key, i)
        if not m.solvable:
            m.flags.append("NOT UNIQUELY SOLVABLE (model will notice)")
        val_s = m.value if isinstance(m.value, str) else fmt_sig(m.value, sig)
        print(f"{i:>2}  {m.name[:44]:<44} {val_s:>12} {dist_s:>8}  {', '.join(m.flags) or 'ok'}")
        if m.note:
            print(f"    {m.note}")
        ok &= not m.flags
    n_ok = sum(1 for m in rows if not m.flags)
    print(f"\nusable misreads: {n_ok}/{len(rows)}  (target >= 6 independent reads)")
    if n_ok < 6:
        print("WARN fewer than 6 usable reads — Pass@4 history says this is not enough")
    return ok
