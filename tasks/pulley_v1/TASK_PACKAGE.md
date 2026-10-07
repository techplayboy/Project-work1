# Pulley v1 (stepped drum, three members, four ropes): task package

Subdomain: Mechanical Engineering: kinematics / mechanisms · Image: `pulley_v1.png` · GTFA: -343 · Status: **RETIRED: both models solved the 0.8 m/s version (see responses/RESULT.md)**

---

## Author notes (NOT submitted)

### Why this structure (lessons from hydraulic v4, solved by both models)
- **Hydraulic v4 could be solved one stage at a time, and the prompt explained the symbols.** Here the speed of C needs all four rope equations at once (a 4×4 system with the drum rate), and the prompt gives no symbol hints beyond "thin = rope, thick = strap, fastened only at dots".
- **The models matched labels to the nearest endpoint instead of tracing lines.** Here no label sits next to a topology decision. The bars are long and crossed by five rope runs that are not fastened to them. The decisive fastenings are at the far ends of long runs (PF's strap, rope 2's end under A).
- **The models fill gaps with textbook defaults.** Every read below contradicts one: a pulley next to the ceiling is fixed; a rope end near a bar is fastened to it; a pulley belongs to the nearest member; both drum ropes wind the same way.
- **Counter-intuitive answer:** pulling the free end DOWN moves block C DOWN (−343 mm/s), while bar B rises.

### Correct equations (y up, ω = drum rate, v_E = −1.2 m/s)
- Rope 1: −v_E − 2v_A + Rω = 0
- Rope 2: −rω − 2v_B + v_A = 0
- Rope 3: −2v_C + v_A = 0
- Rope 4: −v_C − 2v_B = 0

Solution: v_C = −U/(3R/r − 4) = −1.2/3.5 = −0.342857 m/s.

### Trap table
| # | Read | Correct reading (what is drawn) | Textbook default / misread | Misread answer (mm/s) | Distance |
|---|---|---|---|---|---|
| 1 | High pulley PF | Long thick strap runs DOWN to bar A (moving pulley) | Pulley near the ceiling is fixed | −800 | 133 % |
| 2 | Drum winding sense | Rope 1 leaves the outer groove on the LEFT, rope 2 the inner groove on the RIGHT, so they wind in opposite senses | Same sense (differential hoist default) | +104 | 130 % |
| 3 | Drum groove assignment | Rope 1 on the 150 mm groove, rope 2 on the 60 mm groove | Swapped | +429 | 225 % |
| 4 | Pulley PC carrier | Strap goes DOWN to C | Hung from bar B, which it sits under | −600 | 75 % |
| 5 | Pulley PB carrier | Strap UP to bar B; rope 2's other run continues up to A | PB read as carried by A | +133 | 139 % |
| 6 | Rope 2 end | Dot on the UNDERSIDE of bar A | Runs on to the ceiling | +800 | 333 % |
| 7 | Pulley PA carrier | Strap DOWN to bar A | Read as fixed | −160 | 53 % |

Every misread still gives a unique solution. All values are reproduced by `verify.py` (`python3 tasks/pulley_v1/verify.py`).

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
Consider the hoisting arrangement shown in front elevation. The hatched band is a fixed ceiling; $\text{A}$ and $\text{B}$ are rigid bars and $\text{C}$ is a rigid block, each of which translates only vertically without rotating; and the stepped drum turns freely on a fixed axle, with the radii of its two grooves marked. Thin lines are ropes and thick lines are pulley straps, and a rope or strap is fastened to a member only where it ends at a filled dot. The free end of the rope is pulled downward at the speed marked. All ropes are inextensible, remain taut, run vertically between pulleys, and do not slip on the drum. Determine the velocity of block $\text{C}$ in $\text{mm/s}$, reported to $3$ significant figures, taking upward as positive and downward as negative.

The answer should be expressed in $\text{mm/s}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

## Step 6: GTFA
```
-343
```

## Step 7: Image description
```
The figure is a front elevation of a hoisting arrangement. A hatched ceiling band runs across the top. Below it are two long horizontal rigid bars, A (upper) and B (lower), and a rigid block C at the bottom right. Thin lines are ropes, and thick lines are straps that carry pulley axles; every fastening is a filled dot. All numerical data are in the figure: the free rope end at the far left carries a downward arrow marked 1.2 m/s, and the stepped drum has two concentric grooves whose radii are marked 60 mm (inner circle) and 150 mm (outer circle).

Fixed elements: three members hang from the ceiling on short thick straps, each ending at a dot on the ceiling. From left to right they are pulley F1, the stepped drum, and pulley F2 near the right.

Rope 1 hangs from the far left free end (the arrow), rises to F1, passes over its top, and descends on F1's right side. It wraps under pulley PA, whose short strap goes down to a dot on top of bar A. It then rises on PA's right side and ends tangent to the LEFT side of the drum's OUTER (150 mm) circle.

Rope 2 leaves the RIGHT side of the drum's INNER (60 mm) circle, drawn across the outer disc. It descends, crossing bar A without a dot, and wraps under pulley PB. PB's short strap goes UP to a dot on the underside of bar B. The rope rises on PB's right side, crosses bar B without a dot, and ends at a dot on the UNDERSIDE of bar A.

Rope 3 starts at a ceiling dot to the right of the drum. It descends, crossing bars A and B without dots, and wraps under pulley PC, whose short strap goes DOWN to a dot on top of block C. It rises on PC's right side, crossing B and A without dots, to a pulley PF that sits just below the ceiling. PF is not fastened to the ceiling: its long thick strap runs straight DOWN to a dot on top of bar A. The rope passes over PF and descends on its right side to a second dot on top of bar A.

Rope 4 starts at a dot on top of block C near its right end. It rises, crossing bar B without a dot, passes over the fixed pulley F2, and descends on F2's right side. It wraps under pulley PB2, whose short strap goes UP to a dot on the underside of bar B. It then rises, crossing bar B without a dot, to a ceiling dot.

The task prompt, not the image, specifies the conditions: bars A and B and block C translate vertically without rotating; the stepped drum turns freely on a fixed axle; ropes are inextensible, taut, vertical between pulleys and do not slip on the drum; and a rope or strap is fastened only where it ends at a filled dot. It asks for the velocity of block C in mm/s to 3 significant figures, upward positive.
```

## Step 9: Step-by-step solution
```
Step 1: Data and conditions. The prompt states that A, B and C translate vertically, the drum turns freely on a fixed axle, ropes are inextensible and taut and do not slip on the drum, fastenings exist only at dots, and upward is positive. The figure gives the free-end speed of 1.2 m/s downward (v_E = −1.2 m/s) and drum groove radii R = 150 mm and r = 60 mm.

Step 2: Observation of the carriers. F1, F2 and the drum hang from the ceiling (fixed). PA and PF are carried by bar A (PF's long strap runs down to A). PB and PB2 are carried by bar B. PC is carried by block C.

Step 3: Observation of the ropes. Rope 1: free end, over F1, under PA, to the left side of the 150 mm groove. Rope 2: right side of the 60 mm groove, under PB, to the underside of A. Rope 3: ceiling, under PC, over PF, to the top of A. Rope 4: top of C, over F2, under PB2, to the ceiling. Ropes 1 and 2 leave the drum on opposite sides, so a drum rotation ω pays out rope 1 at Rω while it winds in rope 2 at rω.

Step 4: Rope-length (inextensibility) equations, with y upward.
Rope 1: −v_E − 2v_A + Rω = 0
Rope 2: −rω − 2v_B + v_A = 0
Rope 3: −2v_C + v_A = 0, so v_A = 2v_C
Rope 4: −v_C − 2v_B = 0, so v_B = −v_C/2

Step 5: Solve. From rope 2, rω = v_A − 2v_B = 2v_C + v_C = 3v_C, so ω = 3v_C/r. Substituting into rope 1: 1.2 − 4v_C + (R/r)(3v_C) = 0, i.e. 1.2 − 4v_C + 7.5v_C = 0 with R/r = 2.5. Therefore v_C = −1.2/3.5 = −0.342857 m/s.
Then v_A = −0.685714 m/s, v_B = +0.171429 m/s and ω = −17.1429 rad/s.
Cross-check, rope 1: 1.2 − 2(−0.685714) + 0.150(−17.1429) = 1.2 + 1.37143 − 2.57143 = 0.
Block C moves downward at 342.857 mm/s.

Final Answer: -343
```

## Step 10: Distractors
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

1. -800
2. 429
3. 104
4. -600
5. 133
```

| Distractor | Misread |
|---|---|
| −800 | High pulley PF read as fixed to the ceiling |
| 429 | Drum grooves swapped (rope 1 on 60 mm, rope 2 on 150 mm) |
| 104 | Both drum ropes read as winding in the same sense |
| −600 | Pulley PC read as hanging from bar B |
| 133 | Pulley PB read as carried by bar A |

Reserve misreads: 800 (rope 2 read as running on to the ceiling), −160 (PA read as fixed). All misread values are whole numbers at 3 s.f., matching the GTFA format.

## Step 8: Model failure templates (fill from the real response)

Error type: Connectivity / topology error

### Misread 1: PF read as fixed (−800)
```
The response fails by misreading the carrier of the pulley just below the ceiling on the right (topological confusion). Its equations for ropes 1, 2 and 4 are correct. However, it states "<quote>", treating that pulley as fixed, so its rope 3 equation becomes −2v_C − v_A = 0 (v_A = −2v_C) and it obtains v_C = −800 mm/s. In the drawing, that pulley has no strap to the ceiling: its long thick strap runs straight down to a dot on top of bar A, so it moves with A. Rope 3 then gives v_A = 2v_C, and the four equations give v_C = −1.2/3.5 = −0.342857 m/s = −343 mm/s. The misread gives −800 instead of the correct −343.
```

### Misread 2: drum ropes read as same sense (104)
```
The response fails by misreading how the two ropes leave the stepped drum (topological confusion). It states "<quote>", so both ropes pay out together and it uses −v_E − 2v_A + Rω = 0 with −2v_B + v_A + rω = 0, giving v_C = 104 mm/s. In the drawing, rope 1 leaves the 150 mm groove on the drum's left side and rope 2 leaves the 60 mm groove on its right side, so one rotation pays out rope 1 while winding in rope 2. With opposite senses, the solution is v_C = −343 mm/s. The misread gives 104 instead of the correct −343.
```

### Misread 3: grooves swapped (429)
```
The response fails by misreading which drum groove carries which rope (spatial confusion). It states "<quote>", putting rope 1 on the 60 mm groove and rope 2 on the 150 mm groove, so R/r is inverted (0.4 instead of 2.5) and v_C = 429 mm/s. In the drawing, rope 1 is tangent to the outer circle (marked 150 mm) on the left, and rope 2 is tangent to the inner circle (marked 60 mm) on the right and is drawn across the outer disc. With R/r = 2.5, v_C = −1.2/(3 × 2.5 − 4) = −343 mm/s. The misread gives 429 instead of the correct −343.
```

## QC Justification: Science Judge
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity, or that units and precision are missing [or quotes the author attestation, which is not part of the prompt]. The saved prompt defines the system: "Consider the hoisting arrangement shown in front elevation. ...". It states the conditions verbatim: "The free end of the rope is pulled downward at the speed marked. All ropes are inextensible, remain taut, run vertically between pulleys, and do not slip on the drum." It names exactly one requested quantity, with units and precision: "Determine the velocity of block C in mm/s, reported to 3 significant figures, taking upward as positive and downward as negative." The closing boilerplate repeats the units and significant figures.

With these conditions the answer is uniquely determined (-343), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

## QC Justification: Image Description Checker (pulley PF)
```
The Image Description Checker finding is incorrect; the description matches the figure, and no change to the image or answer is required.

The pulley just below the ceiling on the right has no strap or dot at the ceiling: there is a visible gap between its rim and the ceiling band. Its only strap is the long thick line from its axle straight down to a filled dot on top of bar A. The other ceiling-mounted members (F1, the drum and F2) each have a short thick strap ending at a dot on the ceiling, and this pulley has none. It is therefore carried by bar A and moves with it.

The description has been made explicit on this point; the topology, values and GTFA (-343) are unchanged.
```

## Model responses log
| Response | Final answer | Stated reading | Reproduced? | Usable for Step 8? |
|---|---|---|---|---|
