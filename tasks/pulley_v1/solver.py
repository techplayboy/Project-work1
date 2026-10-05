"""
Rope-length kinematics for planar pulley systems with vertical rope runs.

Node forms (y measured upward):
  ("end", body, h)              rope end fixed to `body` at height h ("G" = ceiling, "E" = free end)
  ("over", body, h)             rope passes round a pulley whose axle is carried by `body`, at height h
  ("drum", drum, h, r, s)       rope end wound on the groove of radius r of drum `drum` (fixed axle);
                                s = +1 if positive drum rotation pays rope OUT, -1 if it winds rope IN
Each rope:  sum_k sign(h_k - h_k+1) (v_k - v_k+1)  +  sum_drum s r w  = 0
"""
import numpy as np


def solve(unknown_bodies, drums, ropes, given, want):
    unk = list(unknown_bodies) + list(drums)
    idx = {k: i for i, k in enumerate(unk)}
    M, b = [], []
    for rope in ropes:
        row, c = np.zeros(len(unk)), 0.0
        for p, q in zip(rope, rope[1:]):
            sg = np.sign(p[2] - q[2])
            for node, f in ((p, sg), (q, -sg)):
                bd = "G" if node[0] == "drum" else node[1]
                if bd == "G":
                    continue
                if bd in given:
                    c -= f * given[bd]
                else:
                    row[idx[bd]] += f
        for node in rope:
            if node[0] == "drum":
                row[idx[node[1]]] += node[4] * node[3]
        M.append(row); b.append(c)
    M, b = np.array(M), np.array(b)
    if M.shape[0] != M.shape[1] or np.linalg.matrix_rank(M) < len(unk):
        return float("nan")
    return float(np.linalg.solve(M, b)[idx[want]])
