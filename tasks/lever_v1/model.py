"""Lever v1 model: hydraulic circuit + rigid lever (1 DOF). Correct reading and misreads."""
import math

LPM = 1e6 / 60
D = dict(Q=36.0, bX=80.0, rX=56.0, bY=63.0, rY=50.0,
         xX=150.0, xS=250.0, xP=450.0, xY=700.0, xL=1000.0)  # baseline dims from left end O


def A(d):
    return math.pi * d * d / 4


def vL(d=D, pivot="P", datum="O", regen=True, y_port="rod", envelope="ok", swap_dims=False):
    bX, rX, bY, rY = (d["bY"], d["rY"], d["bX"], d["rX"]) if swap_dims else (d["bX"], d["rX"], d["bY"], d["rY"])
    xp = d["xS"] if pivot == "S" else d["xP"]
    if datum == "O":
        aX, aY, aL = abs(xp - d["xX"]), abs(d["xY"] - xp), abs(d["xL"] - xp)
    else:                                   # printed baseline values taken as arms from the pivot
        aX, aY, aL = d["xX"], d["xY"], d["xL"]
    AXc, AXr, AYc, AYr = A(bX), A(rX), A(bY), A(rY)
    AXa, AYa = AXc - AXr, AYc - AYr
    Q = d["Q"] * LPM
    if envelope == "swap":                 # P->A: supply reaches only Y's cap; X's cap exhausts via B->T and
        k = aY * AYc                       # X's rod side refills from the drain through the POCV free direction
    else:
        kX = (AXc - AXa) if regen else AXc  # regeneration: X rod outflow returns to supply
        kY = AYa if y_port == "rod" else AYc
        k = aX * kX + aY * kY
    w = Q / k
    return w * aL


MIS = [
    ("pivot read at the spring pin S", dict(pivot="S")),
    ("baseline dimensions read as arms from pivot", dict(datum="pivot")),
    ("no regeneration (X rod side to tank)", dict(regen=False)),
    ("supply read into Y cap end", dict(y_port="cap")),
    ("other valve envelope active", dict(envelope="swap")),
    ("X / Y bore-rod labels swapped", dict(swap_dims=True)),
]

if __name__ == "__main__":
    g = vL()
    print("GTFA vL =", g)
    for n, kw in MIS:
        v = vL(**kw)
        print(f"{n:46s} {v:10.4f}  {abs(v-g)/g*100:6.1f}%")
