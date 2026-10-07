# Attempt log

Evidence behind the lessons. Read before designing; **append a row after every test result.**

| # | Task | Subdomain | GTFA | Result | Lesson |
|---|---|---|---|---|---|
| 1 | Compound epicyclic, equal modules | Mech: transmission | — | Solved | Tooth-count sums leaked the meshing; model recognised the Wolfrom layout and sanity-checked the reduction |
| 2 | Carnot battery COP (public MDPI figure) | Thermal | — | Both failed; accepted | Component in a non-textbook position (MSHP on the low-pressure side) works. Prompt wording "loop that also supplies MSHE" leaked the key read |
| 3 | Carnot battery round-trip (public) | Thermal | — | Failed Pass@2 | Only one real read; paper describes the states in words |
| 4 | Round-trip, 5 chained reads | Thermal | 1.13 | Both failed (1.16) | Two traps first self-corrected (x = 1.82, negative heat); redesigned data so wrong split gives x = 0.750 |
| 5 | Excavator regeneration (public, 2020) | Fluid power | — | Solved | Paper recalled; prompt described the operating mode |
| 6 | Hydraulic series v1 | Fluid power | 183 | Both failed (141, 79.6) | Hop vs junction trap |
| 7 | Hydraulic v2 | Fluid power | 129 | Failed Pass@4 | Too few independent reads |
| 8 | Hydraulic v3 | Fluid power | 177 | Blank + 92.7 | Pilot line from an unexpected riser + rods on the non-standard side; wrong valve envelope / A–B hop |
| 9 | Gearbox v1 (two-stage) | Mech: transmission | −406 | Both solved | Solvable stage by stage; obvious fixed members; models checked centre distances |
| 10 | Gearbox v2 (two coupled sets) | Mech: transmission | 1980 | One failed, one solved | Coupling helps; defaults are the attack surface |
| 11 | Gearbox v3 (three coupled sets) | Mech: transmission | −926 | **Both failed** (1180, 1340) | Six reads against defaults beat both models |

## New results

| # | Task | Subdomain | GTFA | Result | Lesson |
|---|---|---|---|---|---|
| 12 | Hydraulic v4 (bleed-off, series, divider, regen) | Fluid power | 114 | **Both solved** (114, 114) | Sequential chain, so each stage could be solved locally. The prompt spelled out the symbol conventions (check-valve direction, pilot logic, 'all cylinders moving'), and the models quoted them back. Dots, solenoid labels and outlet labels were read correctly; the hop swap trap did nothing because the model mapped the outlet label to its endpoint |
| 13 | Pulley v1 (stepped drum, 4 ropes, 3 members) | Mechanisms / kinematics | −229 (tested at 0.8 m/s) | **Both solved** (−229, −229) | Each rope is one unbranched line, so the rope-by-rope method maps 1:1 onto the drawing. The thick strap made PF's carrier obvious (a unique line style is a label). Two ropes tied only pairs of bodies, so the system collapsed into substitutions |
| 14 | Lever v1 (hydraulic circuit + pivoted lever) | Fluid power / mechanisms | 321 | pending | Built from lesson 13 + playbook traps: datum dims from the left end, spring pin beside the pivot, regeneration via hop then dot, pilot dot on the drain line, rod-end feed of Y, active envelope; 1-DOF coupling of the flow balance and lever |


### Results from the user's playbook (separate builds with the same names, not the `tasks/` folders here)
| Task | GTFA | Result | Lesson |
|---|---|---|---|
| Hydraulic v4 (playbook build) | 241 mm/s | **Both failed** (64.7, 50.3) | Worked: a pilot line whose only dot is on a tank line; regeneration through a hop then a dot; lever dimensions all measured from one end; the active envelope. No longer traps on their own: a bypass check on the FCV, a rod on the non-standard side, a rod-to-rod series line. Final distractors 428, 382, 623, 142, 164 (all whole) |
| Gearbox v4 (playbook build) | −1260 rpm | Submitted, awaiting | Three coupled sets, 7 reads |

<!-- Append: | n | task | subdomain | GTFA | result (answers) | lesson | -->
