# Lever v1 (hydraulic circuit driving a pivoted lever): task package

Subdomain: Mechanical Engineering: fluid power / mechanisms · Image: `lever_v1.png` · GTFA: 321 · Status: draft

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
The figure, drawn to scale, shows a horizontal rigid lever at the top and an ISO 1219 hydraulic circuit below it. All numerical data are in the figure: the pump is marked 36 L/min, the left cylinder Ø80/Ø56 and the right cylinder Ø63/Ø50 (bore/rod, mm). Five baseline dimensions run above the lever. Each starts at the lever's left end and ends at a feature: 150, 250, 450, 700 and 1000 mm. The 1000 mm dimension ends at the right tip, which is marked L.

Four pins lie on the lever, at 150, 250, 450 and 700 mm from the left end. The pin at 450 mm sits on the apex of a triangular clevis standing on a hatched ground block. The pin at 250 mm has only a coil spring hanging from it, ending on a small separate hatched block. The rod of the left cylinder rises to the pin at 150 mm, and the rod of the right cylinder rises to the pin at 700 mm. Both cylinders stand vertically below the lever, with their bodies at the bottom and pistons drawn as double lines; each rod is drawn running down through the upper chamber of its body to the piston, so the upper chamber is the rod end and the lower chamber the cap end.

The directional valve has three envelopes, with ports A and B on top and P and T underneath, drawn on the centre envelope. Solenoid Y1 is at the left end and Y2 at the right end. The left envelope has two crossed diagonal arrows (P to B, A to T); the centre envelope has all ports blocked; the right envelope has two parallel arrows (P to A, B to T). The pump feeds P through a line on which a relief valve tees off at a dot to its own tank (its dashed pilot leaves its inlet at a separate dot), and T drops to a tank.

From port B a line rises to a dot. From there one horizontal line runs left to the bottom (cap) port of the left cylinder, and another runs right, up the far right side and into the right cylinder's side port, which lies above its piston. The bottom (cap) port of the right cylinder drops, runs left and descends to port A, crossing the B line with a hop.

The left cylinder's side port, above its piston, runs right to a dot. From this dot one line descends through a check valve (seat apex on top, ball below), then hops over a horizontal drain line and ends at a dot on the B line. A second line goes right from the same dot and descends through a box containing a check valve (seat apex at the bottom, ball above) to a dot on the drain line. A dashed pilot line leaves the left side of that box and descends to its own dot on the drain line. The drain line runs left, crossing the left cylinder's supply line with a hop, to a tank.

The task prompt, not the image, specifies the conditions: Y1 is energised and Y2 de-energised; the pump delivers its marked flow and the relief valve stays closed; at the instant shown the lever is horizontal and both cylinders are vertical; leakage, compressibility and line losses are ignored; lines connect only at dots. It asks for the speed of point L in mm/s to 3 significant figures.
```

## Step 9: Step-by-step solution
```
Step 1: Data and conditions. The prompt states that Y1 is energised and Y2 de-energised, the relief valve stays closed, the lever is horizontal and both cylinders are vertical at the instant shown, and leakage, compressibility and line losses are ignored. The figure gives Q = 36 L/min = 600000 mm^3/s, left cylinder X Ø80/Ø56, right cylinder Y Ø63/Ø50, and baseline positions from the lever's left end: X pin 150 mm, spring pin 250 mm, clevis pin 450 mm, Y pin 700 mm, L 1000 mm.

Step 2: Observation of the lever. The only pin carried by a rigid ground support is the one at 450 mm on the triangular clevis, so it is the pivot. The pin at 250 mm is held only by a spring. The arms from the pivot are therefore a_X = 450 − 150 = 300 mm, a_Y = 700 − 450 = 250 mm and a_L = 1000 − 450 = 550 mm. X lies left of the pivot and Y right of it, so when X extends (pushing up), the right side of the lever goes down and Y retracts.

Step 3: Observation of the circuit. Y1 at the left end brings in the left envelope, whose crossed arrows connect P to B and A to T. Line B feeds the cap of X and the rod-end (side) port of Y. Y's cap drains through A to tank. X's rod-end oil can leave only through the check valve, whose line hops the drain line and joins line B at a dot. The pilot-operated check opens only if its pilot is pressurised, and its pilot's only dot is on the drain line (tank pressure), so it stays closed. X's rod-end oil therefore returns to the supply (regeneration).

Step 4: Continuity at line B, with v_X = ω a_X and v_Y = ω a_Y.
A_X,cap = π(80^2)/4 = 5026.55 mm^2; A_X,rod = π(56^2)/4 = 2463.01 mm^2; A_X,ann = 2563.54 mm^2.
A_Y,ann = π(63^2 − 50^2)/4 = 1153.75 mm^2.
Q + v_X A_X,ann = v_X A_X,cap + v_Y A_Y,ann, so Q = ω (a_X A_X,rod + a_Y A_Y,ann).
Denominator: 300 × 2463.01 + 250 × 1153.75 = 738903 + 288437 = 1.02734 × 10^6 mm^3.
ω = 600000/1.02734 × 10^6 = 0.584033 rad/s.

Step 5: Speeds. v_X = 0.584033 × 300 = 175.210 mm/s; v_Y = 0.584033 × 250 = 146.008 mm/s; v_L = 0.584033 × 550 = 321.218 mm/s.
Cross-check (continuity at line B): inflow Q + X rod-end return = 600000 + 175.210 × 2563.54 = 600000 + 449157 = 1049157 mm^3/s; outflow X cap + Y rod end = 175.210 × 5026.55 + 146.008 × 1153.75 = 880700 + 168457 = 1049157 mm^3/s.

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

With these conditions the answer is uniquely determined (321), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

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
