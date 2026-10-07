# Lever v1 (hydraulic circuit driving a pivoted lever): task package

Subdomain: Mechanical Engineering: fluid power / mechanisms · Image: `lever_v1.png` · GTFA: 321 · Status: **tested: both models failed (184, 184)**

---

## Author notes (NOT submitted)

### Why this structure (lessons from pulley v1, solved by both models with −229)
- **Pulley v1:** each rope was one continuous, unbranched line, so the models' standard rope-by-rope method traced it perfectly. The thick strap on PF acted as a label.
- **Lever v1 replaces long clean traces with local ambiguities** that a model resolves with a textbook default. These are exactly the traps that worked in the playbook's hydraulic v4 (both failed):
  - dimensions all measured from one end;
  - a pin next to the true pivot;
  - regeneration through a hop followed by a dot;
  - a pilot whose only dot is on a tank line.
- **Coupled:** the lever ties the two cylinder speeds through the pivot geometry, so the flow balance cannot be solved without the lever, and the lever's rate cannot be found without the flow balance. There is no stage-by-stage route.
- **No symbol hints in the prompt:** no check-valve convention, no pilot logic, no component names or numbers. The only rule is "lines are connected only at dots", which is needed for defensibility.
- **Drawn to scale** (1 unit = 100 mm): lever positions and cylinder bores and rods are at true proportion.
- **Distractor format:** the GTFA is whole (321), and all five distractors are whole (|value| ≥ 100).

### Correct model (1 DOF, lever rate ω, instant shown)
- Arms from the true pivot (450): a_X = 300, a_Y = 250, a_L = 550.
- Continuity at the supply node: Q + v_X·A_X,ann (regeneration) = v_X·A_X,cap + v_Y·A_Y,ann.
- That reduces to Q = ω(a_X·A_X,rod + a_Y·A_Y,ann), with v_L = ω·a_L = 321.218 mm/s.

### Trap table
| # | Read | Correct reading (what is drawn) | Textbook default / misread | Misread v_L (mm/s) | Distance |
|---|---|---|---|---|---|
| 1 | Pivot | Pin on the hatched triangular clevis at 450 | The pin at 250 (on a spring to a hatched block) read as the pivot | 588 | 83 % |
| 2 | Lever dimensions | Baselines from the lever's left end | Read as arms from the pivot (150, 700, 1000) | 510 | 59 % |
| 3 | X rod-end line | Check valve down, hop over the drain, dot on the supply: regeneration | Hop read as joining the drain, so the rod side vents to tank | 184 | 43 % |
| 4 | Pilot of the pilot-operated check | Its only dot is on the drain line, so it stays closed | Read as taken from the supply line just below, so it opens and there is no regeneration | 184 | 43 % |
| 5 | Port of cylinder Y fed by the supply | Side port above the piston (rod end) | Supply into the cap end (default) | 217 | 32 % |
| 6 | Active envelope | Y1 on the left, next to the crossed-arrow envelope (P→B) | Parallel envelope (P→A), so only Y's cap is fed | 423 | 32 % |

Reads 3 and 4 are independent traps that lead to the same value. All values are reproduced by `verify.py` and `model.py`.

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
Consider the lever actuator shown, consisting of a rigid lever and an ISO $1219$ hydraulic circuit, drawn to scale, with the lever dimensions in millimetres and each cylinder marked $\varnothing$bore $/$ $\varnothing$rod in millimetres. Solenoid $\text{Y1}$ is energised and solenoid $\text{Y2}$ is de-energised. The pump delivers the flow marked and the relief valve remains closed. At the instant shown the lever is horizontal and both cylinders are vertical. Ignore leakage, fluid compressibility and line losses. Lines are connected only at dots. Determine the speed of point $\text{L}$ in $\text{mm/s}$, reported to $3$ significant figures.

The answer should be expressed in $\text{mm/s}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

## Step 6: GTFA
```
321
```

## Step 7: Image description
```
The figure, drawn to scale, shows a rigid lever, drawn horizontal, at the top and an ISO 1219 hydraulic circuit below it. All numerical data are in the figure: the pump is marked 36 L/min, the left cylinder Ø80/Ø56 and the right cylinder Ø63/Ø50 (bore/rod, mm). Five baseline dimensions run above the lever. Each starts at the lever's left end and ends at a feature: 150, 250, 450, 700 and 1000 mm. The 1000 mm dimension ends at the right tip, which is marked L.

Four pins lie on the lever, at 150, 250, 450 and 700 mm from the left end. The pin at 450 mm sits on the apex of a rigid triangular clevis standing on a hatched ground block, and it is the lever's only fixed pivot. The pin at 250 mm is not supported rigidly: its only attachment is a coil spring down to a small separate hatched block, which does not fix the lever's position, so the arms of the lever are measured from the pin at 450 mm. The rod of the left cylinder rises to the pin at 150 mm, and the rod of the right cylinder rises to the pin at 700 mm. Both cylinders stand vertically below the lever, with their bodies at the bottom and pistons drawn as double lines; each rod is drawn running down through the upper chamber of its body to the piston, so the upper chamber is the rod end and the lower chamber the cap end.

The directional valve has three envelopes, with ports A and B on top and P and T underneath, drawn on the centre envelope. Solenoid Y1 is at the left end and Y2 at the right end. The left envelope, next to Y1, has two crossed diagonal arrows (P to B, A to T); the centre envelope has all ports blocked; the right envelope, next to Y2, has two parallel arrows (P to A, B to T). With Y1 energised and Y2 de-energised, the left envelope is the active spool position, so P is connected to B and A is connected to T. The pump feeds P through a line on which a relief valve tees off at a dot to its own tank (its dashed pilot leaves its inlet at a separate dot), and T drops to a tank.

From port B a line rises to a dot. From there one horizontal line runs left to the bottom (cap) port of the left cylinder, and another runs right, up the far right side and into the right cylinder's side port, which lies above its piston. The bottom (cap) port of the right cylinder drops, runs left and descends to port A, crossing the B line with a hop.

The left cylinder's side port, above its piston, runs right to a dot. From this dot one line descends through a check valve (seat apex on top, ball below), then hops over a horizontal drain line and ends at a dot on the B line. A second line goes right from the same dot and descends through a box containing a check valve (seat apex at the bottom, ball above) to a dot on the drain line. A dashed pilot line leaves the left side of that box and descends to its own dot on the drain line. The drain line runs left, crossing the left cylinder's supply line with a hop, to a tank.
```

## Step 9: Step-by-step solution
```
Step 1: Record the operating conditions given in the prompt: solenoid Y1 is energised, solenoid Y2 is de-energised, the pump delivers its marked flow, the relief valve remains closed, the lever is horizontal and both cylinders are vertical at the instant shown, leakage, fluid compressibility and line losses are ignored, and lines are connected only at dots.

Step 2: State the constant used: π is taken as 3.142 (4 significant figures), as the prompt requires for unstated fundamental constants.

Step 3: Read the pump flow from the figure and convert it: Q = 36 L/min = 36 × 10^6 mm^3 / 60 s = 600000 mm^3/s.

Step 4: Read the size of the left cylinder (X) from the figure: Ø80/Ø56, so its bore D_X = 80 mm and its rod d_X = 56 mm.

Step 5: Read the size of the right cylinder (Y) from the figure: Ø63/Ø50, so its bore D_Y = 63 mm and its rod d_Y = 50 mm.

Step 6: Read the lever positions from the baseline dimensions, all measured from the lever's left end: X rod pin at 150 mm, spring pin at 250 mm, clevis pin at 450 mm, Y rod pin at 700 mm and point L at 1000 mm.

Step 7: Identify the pivot: the pin at 450 mm sits on a rigid triangular clevis on a hatched ground block, whereas the pin at 250 mm is attached only through a coil spring and cannot fix the lever, so the lever pivots about the pin at 450 mm.

Step 8: Compute the moment arm of cylinder X about the pivot: a_X = 450 − 150 = 300 mm (left of the pivot).

Step 9: Compute the moment arm of cylinder Y about the pivot: a_Y = 700 − 450 = 250 mm (right of the pivot).

Step 10: Compute the moment arm of point L about the pivot: a_L = 1000 − 450 = 550 mm (right of the pivot).

Step 11: Identify the active valve position: Y1 at the left end of the valve is energised, so the left envelope is active, and its crossed arrows connect P to B and A to T.

Step 12: Trace the first branch of line B: from port B the line reaches a dot and runs left to the bottom (cap) port of cylinder X.

Step 13: Trace the second branch of line B: from the same dot the line runs right and enters the side port of cylinder Y above its piston, which is Y's rod end because the rod runs through that chamber.

Step 14: Trace line A: the bottom (cap) port of cylinder Y runs to port A, crossing line B with a hop, so Y's cap end drains through A to T and the tank.

Step 15: Determine the state of the pilot-operated check valve on X's rod-end line: its dashed pilot line ends at a dot on the drain line, which is at tank pressure, so the valve stays closed in its blocked direction.

Step 16: Trace the remaining exit from X's rod end: the line through the plain check valve hops over the drain line and ends at a dot on line B, so X's rod-end oil returns to the supply line (regeneration).

Step 17: Determine the motion of cylinder X: supply into X's cap extends X, lifting the lever's left side.

Step 18: Determine the motion of cylinder Y: supply into Y's rod end retracts Y, pulling the lever's right side down, which is the same rotational sense as Step 17, so the lever turns about the pivot with a single angular velocity ω.

Step 19: Write the speed of cylinder X from rigid-lever kinematics: v_X = a_X ω = 300 ω.

Step 20: Write the speed of cylinder Y from rigid-lever kinematics: v_Y = a_Y ω = 250 ω.

Step 21: Write the speed of point L from rigid-lever kinematics: v_L = a_L ω = 550 ω.

Step 22: Compute the cap area of X: A_X,cap = π D_X^2 / 4 = 3.142 × 80^2 / 4 = 5027.20 mm^2.

Step 23: Compute the rod area of X: A_X,rod = π d_X^2 / 4 = 3.142 × 56^2 / 4 = 2463.33 mm^2.

Step 24: Compute the annulus area of X: A_X,ann = A_X,cap − A_X,rod = 5027.20 − 2463.33 = 2563.87 mm^2.

Step 25: Compute the cap area of Y: A_Y,cap = π D_Y^2 / 4 = 3.142 × 63^2 / 4 = 3117.65 mm^2.

Step 26: Compute the rod area of Y: A_Y,rod = π d_Y^2 / 4 = 3.142 × 50^2 / 4 = 1963.75 mm^2.

Step 27: Compute the annulus area of Y: A_Y,ann = A_Y,cap − A_Y,rod = 3117.65 − 1963.75 = 1153.90 mm^2.

Step 28: Write continuity for line B (incompressible, no leakage): inflow = pump flow + X rod-end return and outflow = X cap inflow + Y rod-end inflow, so Q + v_X A_X,ann = v_X A_X,cap + v_Y A_Y,ann.

Step 29: Rearrange using A_X,cap − A_X,ann = A_X,rod: Q = v_X A_X,rod + v_Y A_Y,ann.

Step 30: Substitute the speeds from Steps 19 and 20: Q = ω (a_X A_X,rod + a_Y A_Y,ann).

Step 31: Evaluate the first term: a_X A_X,rod = 300 × 2463.33 = 738999 mm^3.

Step 32: Evaluate the second term: a_Y A_Y,ann = 250 × 1153.90 = 288475 mm^3.

Step 33: Add the two terms: 738999 + 288475 = 1.02747 × 10^6 mm^3.

Step 34: Solve for the angular velocity: ω = 600000 / (1.02747 × 10^6) = 0.583959 rad/s.

Step 35: Compute the speed of point L: v_L = 550 × 0.583959 = 321.177 mm/s.

Step 36: Compute the cylinder speeds for a check: v_X = 300 × 0.583959 = 175.188 mm/s and v_Y = 250 × 0.583959 = 145.990 mm/s.

Step 37: Evaluate the inflow to line B: Q + v_X A_X,ann = 600000 + 175.188 × 2563.87 = 1.04916 × 10^6 mm^3/s.

Step 38: Evaluate the outflow from line B: v_X A_X,cap + v_Y A_Y,ann = 175.188 × 5027.20 + 145.990 × 1153.90 = 1.04916 × 10^6 mm^3/s, which equals the inflow, so continuity is satisfied.

Step 39: Round v_L = 321.177 mm/s to 3 significant figures: 321 mm/s.

Final Answer: 321
```

## Step 10: Distractors
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

1. 588
2. 510
3. 184
4. 217
5. 423
```

| Distractor | Misread |
|---|---|
| 588 | Spring pin at 250 mm read as the pivot |
| 510 | Baseline dimensions read as arms from the pivot |
| 184 | No regeneration (hop read as a junction to the drain, or pilot read from the supply) |
| 217 | Supply read as entering Y's cap end |
| 423 | Parallel envelope taken as active (only Y's cap fed) |

## Step 8: Model failure templates (fill from the real response)

Error type: Connectivity / topology error (use Spatial for misread 2 alone)

### Misread 1: spring pin read as the pivot (588)
```
The response fails by misreading which lever pin is the pivot (topological confusion). Its circuit reading and continuity equation are correct. However, it states "<quote>", taking the pin at 250 mm as the fulcrum, so its arms are 100, 450 and 750 mm and it obtains v_L = 588 mm/s. In the drawing, the pin at 250 mm carries only a coil spring to a separate hatched block. The only rigid ground support is the triangular clevis under the pin at 450 mm. With arms 300, 250 and 550 mm, Q = ω(300 × 2463.01 + 250 × 1153.75) gives ω = 0.584033 rad/s and v_L = 321 mm/s. The misread gives 588 instead of the correct 321.
```

### Misread 2: baselines read as arms (510)
```
The response fails by misreading the datum of the lever dimensions (spatial confusion). It states "<quote>", using 150, 700 and 1000 mm as the arms of X, Y and L about the pivot, and obtains v_L = 510 mm/s. In the drawing, every dimension line starts at the extension line at the lever's left end, not at the pivot at 450 mm, so the arms are 300, 250 and 550 mm and v_L = 321 mm/s. The misread gives 510 instead of the correct 321.
```

### Misread 3: no regeneration (184)
```
The response fails by misreading the connection of the left cylinder's rod-end line (topological confusion). It states "<quote>", sending the rod-end oil to tank, so Q = ω(300 × 5026.55 + 250 × 1153.75) and v_L = 184 mm/s. In the drawing, the line below the check valve crosses the drain line with a hop (no connection) and ends at a dot on line B, so the rod-end oil returns to the supply. The pilot of the pilot-operated check has its only dot on the drain line, so that valve stays closed. With regeneration, Q = ω(300 × 2463.01 + 250 × 1153.75) and v_L = 321 mm/s. The misread gives 184 instead of the correct 321.
```

### Misread 5: Y fed at the cap (217)
```
The response fails by misreading which port of the right cylinder receives the supply (topological confusion). It states "<quote>", using A_Y,cap = 3117.25 mm^2 in the continuity equation, and obtains v_L = 217 mm/s. In the drawing, the long branch from line B enters the right cylinder's side port above its piston (the rod end), while its bottom (cap) port drains to A. With A_Y,ann = 1153.75 mm^2, v_L = 321 mm/s. The misread gives 217 instead of the correct 321.
```

## QC Justification: Science Judge
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity, or that units and precision are missing [or quotes the author attestation, which is not part of the prompt]. The saved prompt defines the system: "Consider the lever actuator shown, consisting of a rigid lever and an ISO 1219 hydraulic circuit, drawn to scale, ...". It states the conditions verbatim: "Solenoid Y1 is energised and solenoid Y2 is de-energised. The pump delivers the flow marked and the relief valve remains closed. At the instant shown the lever is horizontal and both cylinders are vertical." It names exactly one requested quantity, with units and precision: "Determine the speed of point L in mm/s, reported to 3 significant figures." The closing boilerplate repeats them.

With these conditions the answer is uniquely determined (321), as shown in the step-by-step solution. Step 1 of the solution restates the conditions and attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

## QC Justification: Image Description Checker (pivot / pilot)
```
The Image Description Checker finding is incorrect; the description matches the figure, and no change to the image or answer is required.

Pivot: the pin at 450 mm sits on the apex of a rigid triangular clevis on a hatched ground block. The pin at 250 mm connects only to a coil spring, which cannot fix the lever's position. All five dimensions share one extension line at the lever's left end, so they are measured from that end.

Pilot: the dashed pilot line of the boxed check valve descends to a filled dot on the drain line. The B line runs below the drain line and has no dot under the pilot. With lines connected only at dots, the pilot sees drain (tank) pressure.

The description has been made explicit on these points; the topology, values and GTFA (321) are unchanged.
```

## Model responses log
| Response | Final answer | Stated reading | Reproduced? | Usable for Step 8? |
|---|---|---|---|---|
| Response 1 | 184 | Pilot-operated check "piloted open by the pressure line from Port B", rod end of the left cylinder to reservoir | Yes, exactly (330000000/(571812.5π) = 183.701) | **Yes: chosen** |
| Response 2 | 184 | Same reading (calls it a "pilot-operated counterbalance check valve") | Yes, exactly | Yes |

## QC Justification: Image Description Checker, findings on the description (rebuttal / changes made)
```
Finding 1 (MISSING_SOLVE_CRITICAL_DETAIL, active envelope): accepted and corrected in the description. The description now states that the left envelope, next to Y1, is the active spool position when Y1 is energised and Y2 de-energised, so P is connected to B and A to T. The figure already shows this: the crossed-arrow envelope is the one adjacent to the Y1 solenoid at the left end of the valve.

Finding 2 (IRRELEVANT_DETAIL, spring): the detail is required to solve the task, so it is retained. Two lever pins sit on hatched ground blocks; the pin at 250 mm is attached to its block only through a coil spring, while the pin at 450 mm sits on a rigid triangular clevis. The spring is therefore the evidence that the pin at 250 mm is not the pivot, which fixes the lever arms (300, 250 and 550 mm from the pin at 450 mm) and hence the speed of point L. The description now states this relevance explicitly.

Finding 3 (META_COMMENTARY): accepted. The closing paragraph about where the conditions come from has been removed; the description now describes only the figure, including that the lever is drawn horizontal and the cylinders vertical.

The topology, values and GTFA (321) are unchanged.
```

## QC Justification: Science Judge (AMBIGUOUS_PROMPT + UNSTATED_ASSUMPTION, after testing)
```
Both Science Judge findings are incorrect and require no change to the task.

Finding 1 (AMBIGUOUS_PROMPT) states that the prompt requests no engineering quantity, and it quotes nothing from the prompt ("Quote: N/A"). The saved prompt names exactly one quantity, with its units and precision: "Determine the speed of point L in mm/s, reported to 3 significant figures." The closing boilerplate repeats this: "The answer should be expressed in mm/s. Report your final answer as a 3 significant figure number without units." Point L is labelled at the right tip of the lever in the figure, so the requested quantity and the unique final answer (321) are defined. Both checker-model responses identified and computed this same quantity (each reported a speed of point L in mm/s), which confirms that the request is unambiguous.

Finding 2 (UNSTATED_ASSUMPTION) states that "the relief valve stays closed" cannot be inferred without relief-setting and load data. It does not need to be inferred: it is an explicit condition given in the prompt, which states verbatim "The pump delivers the flow marked and the relief valve remains closed." The prompt therefore stipulates that the full marked pump flow (36 L/min) enters the circuit, so no relief setting or load data are required. The quoted wording comes from Step 1 of the solution, which restates the prompt's conditions and attributes them to the prompt.

With these stated conditions the answer is uniquely determined (321), as shown in the step-by-step solution. Both findings are artefacts of the prompt text not being fully evaluated, not omissions in the task.
```
