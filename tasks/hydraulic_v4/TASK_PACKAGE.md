# Hydraulic v4 (bleed-off, series feed, flow divider, regeneration): task package

Subdomain: Mechanical Engineering: fluid power · Image: `hydraulic_v4.png` · GTFA: 114 · Status: draft

---

## Author notes (NOT submitted)

### Playbook row
- **Image type:** ISO 1219 circuit with three cylinders. Pump 1 feeds 4/3 solenoid valve 3. Bleed-off FCV 8 is on the working line. Cylinder 4's rod-side outflow feeds flow divider 7, which supplies cylinders 5 and 6. Cylinder 5 has check valve 9 and pilot-operated check valve 10.
- **Coupling:** the cylinder 5 speed needs every link in the chain: active envelope → which line is pressurised → FCV position → which port of cylinder 4 is fed → divider outlet mapping → pilot source (regeneration or not) → which dimensions belong to cylinder 5. Every link is a separate read, and the chain has no shortcut.
- **Counter-intuitive feature:** cylinder 5 moves faster than cylinder 4 (114 vs 92.8 mm/s), even though it receives only 60 % of cylinder 4's small annulus outflow, because it regenerates.
- **Self-check routes closed:**
  - No speeds, pressures or flows other than the pump, FCV and divider values are given.
  - Every misread gives an ordinary cylinder speed (32–440 mm/s).
- **Dense region:** around valve 3's A/B ports:
  - B hops over A's riser.
  - FCV 8 tees into B just left of that hop.
  - The pilot of valve 10 starts at a dot on A's riser, 0.55 above the hop, then rises exactly in line with B's riser.

### Trap table
| # | Read | Correct reading (what is drawn) | Textbook default / misread | Misread answer | Distance |
|---|---|---|---|---|---|
| 1 | Active envelope of valve 3 | Y1 is on the RIGHT; the right envelope has crossed arrows, so P→B, A→T | Y1 on the left / parallel envelope (P→A) active | 322 | 184 % |
| 2 | Which end of cylinder 4 is fed | Rod exits LEFT, so line B enters the cap end (right) | Cap on the left / B enters the rod side | 437 | 285 % |
| 3 | FCV 8 junction | Dot on line B (bleed-off of the working flow) | Tee on line A / hop read as not connected, so no bleed | 146 | 29 % |
| 4 | FCV 8 function | Bleed-off branch to tank | Meter-in, in series on B (8 L/min reaches cylinder 4) | 32.5 | 71 % |
| 5 | Divider outlet mapping | Left outlet (60 %) runs lower and reaches cylinder 5; the 40 % riser hops it to reach cylinder 6 | Outlets swapped at the hop | 75.8 | 33 % |
| 6 | Pilot source of valve 10 | Dot on line A (tank pressure), so valve 10 stays closed and cylinder 5 regenerates | Pilot read as continuing B's riser (pressurised), so it opens and there is no regeneration | 45.8 | 60 % |
| 7 | Dimension attribution | Cylinder 5 is Ø63/Ø40 | Cylinder 6's Ø40/Ø28 used | 232 | 104 % |

All values are reproduced by `verify.py` (`python3 tasks/hydraulic_v4/verify.py`). Every misread still gives a single, determined speed.

---

## Step 2: Subdomain
```
Mechanical Engineering
```

## Step 3: Source and License
```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```

## Step 4: Prompt
```
Consider the hydraulic circuit shown in ISO $1219$ symbols, in which components are numbered, each cylinder is marked with its bore and rod diameters in millimetres as $\varnothing$bore $/$ $\varnothing$rod, and the pump delivery, the flow-control setting and the flow-divider outlet shares are marked beside their symbols. Solenoid $\text{Y1}$ of valve $3$ is energised and solenoid $\text{Y2}$ is de-energised, and all three cylinders are moving and none has reached the end of its stroke. Treat pump $1$ as delivering exactly its marked flow, relief valve $2$ as closed, flow-control valve $8$ as pressure compensated so that it passes exactly its marked flow, and flow divider $7$ as splitting its inlet flow exactly in the marked shares. Check valves have zero cracking pressure, free flow through a check-valve symbol is from the apex of its seat towards its ball, and a pilot-operated check valve opens in its blocked direction only when its dashed pilot line is pressurised. Ignore leakage, fluid compressibility and line losses, and take any line open to the tank as being at zero gauge pressure. Lines are connected only at dots, and a semicircular hop is a crossing without connection. Determine the speed of the piston of cylinder $5$.

The answer should be expressed in $\text{mm/s}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

## Step 6: GTFA
```
114
```

## Step 7: Image description
```
The figure is an ISO 1219 hydraulic circuit drawn in black on white. Ten components are numbered, and all numerical data are printed in the figure: pump 1 delivers 36 L/min; flow-control valve 8 is marked 8 L/min; flow divider 7 has its left outlet marked 60 % and its right outlet marked 40 %; cylinder 4 is marked Ø80/Ø56, cylinder 5 Ø63/Ø40 and cylinder 6 Ø40/Ø28 (bore/rod, mm).

Along the bottom, fixed pump 1 draws from a tank and discharges upward to a horizontal pressure line, marked by a dot. Relief valve 2 tees off this line at a second dot and drains to its own tank. The pressure line runs right to port P of directional valve 3. On the way, it passes a vertical line from valve 8 with a semicircular hop, so it is not connected there.

Valve 3 is a 4/3 valve with three envelopes. Its ports are drawn on the centre envelope: A and B on top (A left, B right), P and T below (P left, T right). The centre envelope has all four ports blocked. The left envelope has two parallel vertical arrows: P to A, and B to T. The right envelope has two crossed diagonal arrows: P to B, and A to T. Solenoid Y2 is drawn on the left end and solenoid Y1 on the right end. Port T drops to a tank.

Line B rises from port B, turns left, hops over the vertical riser from port A, and meets a dot from which a branch descends through valve 8 to a tank (this branch hops the pressure line). Line B then continues left and rises to the right-hand port of cylinder 4. Cylinder 4's piston rod exits from its left end, so this right-hand port is the cap end. Cylinder 4's left-hand (rod-end) port drops, runs right and enters the bottom inlet of flow divider 7.

Line A rises from port A. At a dot on this riser, a dashed pilot line leaves to the right. Above the dot, line A turns right and runs horizontally to the rod-end port of cylinder 6. The dashed pilot line runs right to a point vertically above port B; this is a separate line from line B, which turns left at a lower level, so a gap separates them. The pilot then rises, hops over line A, and enters the left side of the box of pilot-operated check valve 10.

From divider 7, the left (60 %) outlet rises to the lower of two horizontal lines. That line hops the right outlet's riser and the rising part of line B, and reaches the left-hand (cap-end) port of cylinder 5. The right (40 %) outlet rises to the upper horizontal line, which hops line B, cylinder 5's cap line and cylinder 5's rod line, and reaches the cap-end port of cylinder 6. Cylinders 5 and 6 have rods exiting to the right.

Cylinder 5's rod-end port drops to a dot. From there, check valve 9 runs left to a dot on cylinder 5's cap line. Its seat apex points right and its ball is on the left, so it gives free flow from the rod end to the cap end. From the same dot, a line descends, hopping the upper divider line, through valve 10 to a dot on line A. In valve 10, the seat apex points down and the ball is above, so free flow is from line A upward to cylinder 5's rod end only.

The task prompt, not the image, specifies the conditions: Y1 is energised and Y2 de-energised; all cylinders are moving; the pump delivers exactly its marked flow; relief valve 2 is closed; valve 8 passes exactly its marked flow; divider 7 splits exactly in the marked shares; check valves have zero cracking pressure, with free flow from seat apex to ball; a pilot-operated check opens only when its pilot is pressurised; leakage, compressibility and line losses are ignored; lines open to tank are at zero gauge pressure; lines connect only at dots, and hops are crossings. It asks for the speed of the piston of cylinder 5 in mm/s to 3 significant figures.
```

## Step 9: Step-by-step solution
```
Step 1: Data and conditions. The prompt states that Y1 is energised and Y2 de-energised, all cylinders are moving, the relief valve is closed, valve 8 passes exactly its setting, and divider 7 splits exactly in its marked shares. The figure gives Q = 36 L/min = 600000 mm^3/s, valve 8 = 8 L/min = 133333 mm^3/s, divider shares 60 % (left outlet) and 40 % (right outlet), and bore/rod of cylinder 4 = 80/56 mm, cylinder 5 = 63/40 mm and cylinder 6 = 40/28 mm.

Step 2: Observation of valve 3 and the supply lines. Y1 is on the right of valve 3, so energising it brings the right envelope into use. That envelope's crossed arrows connect P to B and A to T. Line B therefore carries the pump flow, and line A drains to tank. Valve 8 is connected at a dot on line B and drains to tank (its crossing with the pressure line is a hop), so it bleeds 8 L/min off line B. Line B ends at the right-hand port of cylinder 4, which is the cap end because that cylinder's rod exits to the left.

Step 3: Observation of the downstream connections. The rod end of cylinder 4 feeds divider 7. The 60 % outlet reaches the cap of cylinder 5; the 40 % outlet hops over it and reaches the cap of cylinder 6. The rod end of cylinder 5 can discharge only through check valve 9 (free flow into its own cap line) or through valve 10. Valve 10's pilot is taken from a dot on line A, which is at tank pressure, so valve 10 stays closed in the rod-to-A direction. Cylinder 5 therefore operates with its rod-end oil returned to its cap end.

Step 4: Continuity at cylinder 4. Cap area A4c = π(80^2)/4 = 5026.55 mm^2; annulus A4a = π(80^2 − 56^2)/4 = 2563.54 mm^2. Inflow = 600000 − 133333 = 466667 mm^3/s, so v4 = 466667/5026.55 = 92.8404 mm/s, and rod-end outflow q4 = 92.8404 × 2563.54 = 238000 mm^3/s.

Step 5: Divider and cylinder 5. q5 = 0.60 × 238000 = 142800 mm^3/s (and 95200 mm^3/s goes to cylinder 6). For cylinder 5, the cap inflow is q5 plus the rod-end return: v5 A5c = q5 + v5 (A5c − A5r), so v5 = q5/A5r, with rod area A5r = π(40^2)/4 = 1256.64 mm^2. Therefore v5 = 142800/1256.64 = 113.637 mm/s.
Cross-check: the cap inflow is 113.637 × 3117.25 = 354233 mm^3/s, and q5 + rod-end return = 142800 + 113.637 × 1860.61 = 354233 mm^3/s.

Final Answer: 114
```

## Step 10: Distractors
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

1. 146
2. 75.8
3. 45.8
4. 322
5. 232
```

| Distractor | Misread |
|---|---|
| 146 | FCV 8 read as not on line B (no bleed-off) |
| 75.8 | Divider outlets swapped at the hop (40 % to cylinder 5) |
| 45.8 | Pilot of valve 10 read as coming from line B, so valve 10 opens and there is no regeneration |
| 322 | Parallel envelope taken as active (P→A), so cylinder 5 is driven on its annulus |
| 232 | Cylinder 6's dimensions (Ø40/Ø28) used for cylinder 5 |

Reserve misreads: 437 (line B read as entering cylinder 4's rod end), 32.5 (valve 8 read as meter-in).

## Step 8: Model failure templates (fill from the real response)

Error type: Connectivity / topology error

### Misread 6: pilot read from line B (45.8)
```
The response fails by misreading the pilot connection of valve 10 (topological confusion). Its valve-envelope reading, bleed-off of 8 L/min and divider split are correct. However, it states "<quote>", treating the dashed pilot as fed from pressurised line B, so valve 10 opens, cylinder 5's rod end drains to tank, and v5 = 142800/3117.25 = 45.8 mm/s. In the drawing, the dashed pilot starts at a dot on the riser from port A. Line B turns left at a lower level and hops this riser, and a gap separates B's corner from the pilot. Line A is open to tank, so valve 10 stays closed and the rod-end oil returns through check valve 9: v5 = 142800/1256.64 = 113.637 = 114 mm/s. The misread gives 45.8 instead of the correct 114.
```

### Misread 3: no bleed-off (146)
```
The response fails by misreading the connection of flow-control valve 8 (topological confusion). It states "<quote>", so it feeds the full 600000 mm^3/s into cylinder 4 and obtains v5 = 0.6 × (600000/5026.55) × 2563.54/1256.64 = 146 mm/s. In the drawing, valve 8's branch leaves line B at a junction dot, just left of where B hops the riser from port A, and drains to tank. Its only other crossing, with the pressure line, is a hop. The 8 L/min is bled off the working flow: v5 = 0.6 × (466667/5026.55) × 2563.54/1256.64 = 114 mm/s. The misread gives 146 instead of the correct 114.
```

### Misread 5: divider outlets swapped (75.8)
```
The response fails by misreading the outlet routing of flow divider 7 (topological confusion). It states "<quote>", assigning the 40 % outlet to cylinder 5, so q5 = 0.4 × 238000 = 95200 mm^3/s and v5 = 95200/1256.64 = 75.8 mm/s. In the drawing, the left outlet marked 60 % rises to the lower horizontal line, which runs to cylinder 5's cap port. The right outlet marked 40 % rises past it with a hop to the upper line, which leads to cylinder 6. With 60 %, v5 = 142800/1256.64 = 114 mm/s. The misread gives 75.8 instead of the correct 114.
```

### Misread 1: wrong envelope (322)
```
The response fails by misreading which envelope of valve 3 is active (topological confusion). It states "<quote>", using the parallel-arrow envelope (P to A), so the pump flow goes through valve 10's free direction into cylinder 5's rod end, giving v = 600000/1860.61 = 322 mm/s. In the drawing, solenoid Y1 is at the right end of valve 3, next to the envelope with crossed arrows (P to B, A to T). With Y1 energised, line B is pressurised and the cylinder 5 speed is 114 mm/s. The misread gives 322 instead of the correct 114.
```

## QC Justification: Science Judge
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity [or quotes the author attestation, which is not part of the prompt]. The saved prompt defines the system: "Consider the hydraulic circuit shown in ISO 1219 symbols, ...". It states the conditions verbatim: "Solenoid Y1 of valve 3 is energised and solenoid Y2 is de-energised, and all three cylinders are moving and none has reached the end of its stroke." It names exactly one requested quantity: "Determine the speed of the piston of cylinder 5.", in mm/s to 3 significant figures.

With these conditions the answer is uniquely determined (114), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

## QC Justification: Image Description Checker (pilot source)
```
The Image Description Checker finding is incorrect; the description matches the figure, and no change to the image or answer is required.

The dashed pilot line of valve 10 begins at a solid junction dot on the vertical riser from port A of valve 3. Line B rises from port B only to the level where it turns left and hops over the A riser. The pilot's vertical dashed segment lies above port B, but it starts above B's corner with a visible gap and is drawn dashed, while B is solid. A pilot cannot connect to B without a junction dot, and the prompt states that lines connect only at dots. The pilot is therefore at line A's pressure, which is tank pressure with Y1 energised.

The description has been made explicit on this point; the topology, values and GTFA (114) are unchanged.
```

## Model responses log
| Response | Final answer | Stated reading | Reproduced? | Usable for Step 8? |
|---|---|---|---|---|
