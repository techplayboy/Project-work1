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

| 12 | Hydraulic v4 (bleed-off, series, divider, regen) | Fluid power | 114 | **Both solved** (114, 114) | Sequential chain, so each stage could be solved locally. The prompt spelled out the symbol conventions (check-valve direction, pilot logic, 'all cylinders moving'), and the models quoted them back. Dots, solenoid labels and outlet labels were read correctly; the hop swap trap did nothing because the model mapped the outlet label to its endpoint |
| 13 | Pulley v1 (stepped drum, 4 ropes, 3 members) | Mechanisms / kinematics | −229 | pending | Built from lesson 12: 4×4 coupled system, minimal prompt conventions, long ropes crossing bars without dots, pulley near the ceiling strapped to a moving bar |

<!-- Append: | n | task | subdomain | GTFA | result (answers) | lesson | -->
