# Gearbox v4 (three coupled planetary sets): task package

Subdomain: Mechanical Engineering: power transmission · Image: `gearbox_v4.png` · GTFA: -337 · Status: draft

---

## Author notes (NOT submitted)

### Playbook row
- **Image type:** kinematic half-section of a three-set planetary gearbox with two clutches (K1, K2) and two brakes (F1, F2).
- **Coupling idea:** the three Willis equations form a cycle. PG1 involves (X, Y), PG2 involves (Y, Z) and PG3 involves (X, Z), so no set can be solved alone, and the output needs all three.
- **Counter-intuitive feature:** the output runs in reverse (−337 rpm) even though no idler is drawn. PG1 has a stepped planet with a basic ratio of magnitude below 1 (0.914), which is impossible for a simple set.
- **Self-check routes closed:**
  - The modules differ per set.
  - The double-planet set has no simple tooth-sum relation.
  - The drawing is schematic, not to scale, so radii cannot be checked.
  - Only one input speed is given; no intermediate speeds appear.
- **Sensitivity note:** the answer is nearly insensitive to PG3's ratio (that term cancels to first order). That is why the stepped planet went into PG1, not PG3.

Rotating groups (correct reading), with K1 and F2 engaged:

| Group | Members |
|---|---|
| A = 1450 | shaft A, K1 drum, R1, S3 |
| X | S1, inner sleeve, C3 (left plate) |
| Y | C1, outer sleeve, S2 |
| Z | C2 (both pins), outer drum, R3 (flange + dot), D |
| 0 | R2 (via F2) |

### Trap table
| # | Read | Correct reading (what is drawn) | Textbook default / misread | Misread answer | Distance |
|---|---|---|---|---|---|
| 1 | Is S1 on shaft A? | A passes under S1 with a gap; S1 sits on the inner sleeve | Suns on the input / common central shaft | −615 | 82% |
| 2 | PG2 planet type | Two planets, each on its own pin (double planet), e = +94/28 | Single planet, e = −94/28 | 230 | 168% |
| 3 | PG2 planet type (alt.) | Double planet | Stepped planet, e = −(94/21)(18/28) | 262 | 178% |
| 4 | What F2 holds | F2 holds ring R2 (z94) | Brake holds the sun | −2500 | 643% |
| 5 | Output member | D comes from the outer drum = C2 + R3 | Output from the carrier (C3) | 196 | 158% |
| 6 | Inner shaft ends at PG3 | A ends in S3; the sleeve rises to C3's left plate | Ends swapped (A to C3, sleeve to S3) | −2870 | 751% |
| 7 | PG1 planet type | Stepped planet (z13 and z32 on one pin), e = −(81/32)(13/36) | Simple planet, e = −81/36 | −442 | 31% |
| 8 | Where K1 lands | K1 drum goes to ring R1 (z81) | K1 drives carrier C1 (R1 on the sleeve) | −1610 | 378% |

All values are reproduced by `verify.py` (`python3 tasks/gearbox_v4/verify.py`). The reduced system is uniquely solvable for every misread.

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
Consider the planetary gearbox shown as a schematic kinematic half-section above the dash-dot axis of rotation, in which each gear is drawn as a rectangle marked with its tooth number $z$ and module $m$ in millimetres, gear rectangles that share an edge are in mesh, a horizontal line ending inside a planet gear is its pin, hatched blocks are the stationary housing, and $\text{K1}$, $\text{K2}$, $\text{F1}$ and $\text{F2}$ are friction shift elements. Clutch $\text{K1}$ and brake $\text{F2}$ are fully engaged with no slip, and clutch $\text{K2}$ and brake $\text{F1}$ are fully released. Shaft A is driven at the speed marked. All gears are spur gears, the drawing is not to scale, and every planet turns freely on its pin. Lines are joined only where they meet at a corner or at a dot, a line that passes beneath a gear is not attached to it, and planet gears threaded on the same pin line rotate as one rigid body. Determine the rotational speed of shaft D. Take a speed as positive when it is in the same sense as the rotation of shaft A, and negative otherwise.

The answer should be expressed in $\text{rpm}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

## Step 6: GTFA
```
-337
```

## Step 7: Image description
```
The figure is a schematic kinematic half-section of a three-set planetary gearbox drawn above a horizontal dash-dot axis of rotation. Gears are drawn as rectangles labelled with tooth number z and module m; rectangles sharing an edge are in mesh. All numerical data (tooth numbers, modules and the input speed 1450 rpm) are printed in the figure.

Shaft A enters at the lower left on the innermost horizontal line, marked "A" and "1450 rpm". Near the left end a vertical disk rises from shaft A (junction dot on A). At the top of this disk, clutch pack K1 (two thick vertical plates) connects it to a horizontal drum that runs right and descends into the top of ring gear z81, m 2.5. Lower on the same disk, clutch pack K2 connects it to a short riser that drops to a second horizontal line just above shaft A: the inner sleeve.

Left set: sun z36, m 2.5 stands on the inner sleeve. Shaft A passes beneath it with a visible gap and is not attached. Directly above the sun is planet z13, m 2.5. To its right, on the same horizontal pin line, is the taller planet z32, m 2.5, whose top edge meets the ring z81, m 2.5. So z13 and z32 form one stepped planet on a single pin: z13 meshes the sun and z32 meshes the ring. The pin line continues right to a vertical carrier plate, which drops to a third horizontal line (the outer sleeve) at a corner and runs right to the middle set.

Middle set: sun z28, m 2 stands on the outer sleeve. Above it, in one column, are planet z18, m 2, planet z21, m 2 and ring z94, m 2. Planet z18 has its own pin and planet z21 has its own pin, at different heights. Both pins run right to one vertical carrier plate: the lower pin meets it at a corner and the upper pin at a dot. This is a double-planet set: z18 meshes the sun and z21; z21 meshes z18 and the ring. Ring z94 is connected upward to brake F2, whose opposite plate is on a hatched housing block. The carrier plate continues upward to the outermost horizontal drum, which runs right over the right-hand set. Brake F1 sits on this drum against a second hatched housing block. The drum descends at the far right to the level of shaft A and continues right as output shaft D. Shaft A and shaft D are collinear but separate: there is a gap between the end of A and the descending drum.

Right set: sun z31, m 3 stands directly on the end of shaft A; A terminates inside this sun. Above it are planet z21, m 3 and ring z73, m 3. The planet's pin runs left to a vertical plate that drops at a corner onto the inner sleeve, so the inner sleeve rises here as the carrier of this set. The ring z73 has a horizontal flange running right that meets the descending output drum at a dot.

The task prompt, not the image, specifies the conditions: K1 and F2 are fully engaged with no slip; K2 and F1 are fully released; shaft A is driven at the marked speed; all gears are spur gears; the drawing is not to scale; planets turn freely on their pins; lines are joined only at corners or dots; a line passing beneath a gear is not attached to it; and planet gears on the same pin line rotate as one rigid body. It asks for the rotational speed of shaft D in rpm to 3 significant figures, positive in the sense of shaft A.
```

## Step 9: Step-by-step solution
```
Step 1: Data and conditions. The prompt states that K1 and F2 are engaged, K2 and F1 are released, shaft A is driven at the marked speed, and speeds are positive in the sense of A. The figure gives n_A = 1450 rpm and the tooth numbers: left set sun 36, stepped planet 13/32, ring 81 (m 2.5); middle set sun 28, inner planet 18, outer planet 21, ring 94 (m 2); right set sun 31, planet 21, ring 73 (m 3).

Step 2: Observation of the input side. Shaft A carries the disk to K1 and K2. With K1 engaged, A drives the drum that ends in ring 81, so n_R1 = 1450 rpm. K2 is released, so the inner sleeve is not driven by A. Shaft A passes beneath suns 36 and 28 without attachment and ends fixed in sun 31, so n_S3 = 1450 rpm.

Step 3: Observation of the remaining connections. Sun 36 sits on the inner sleeve, which rises at the right set as the carrier plate C3: n_S1 = n_C3 = X. The left carrier C1 drops to the outer sleeve, which carries sun 28: n_C1 = n_S2 = Y. In the middle set, planets 18 and 21 are on separate pins (a double planet), and both pins go to carrier C2. C2 rises to the outer drum, which receives the flange of ring 73 at a dot and descends to output D: n_C2 = n_R3 = n_D = Z. F2 is engaged on ring 94: n_R2 = 0. In the left set, 13 and 32 share one pin (a stepped planet).

Step 4: Willis equations, (n_S − n_C) = e (n_R − n_C).
Left (stepped): e1 = −(81/32)(13/36) = −0.914063.
Middle (double planet): e2 = +94/28 = +3.35714.
Right (simple): e3 = −73/31 = −2.35484.
PG1: X − Y = −0.914063 (1450 − Y)
PG2: Y − Z = 3.35714 (0 − Z), so Y = −2.35714 Z
PG3: 1450 − X = −2.35484 (Z − X)

Step 5: Solve. From PG1, X = 1.91406 Y − 1325.39 = −4.51172 Z − 1325.39. From PG3, 1450 + 2.35484 Z = 3.35484 X = −15.1361 Z − 4446.47. Therefore 17.4909 Z = −5896.47 and Z = −337.116 rpm. Then Y = 794.631 rpm and X = 195.582 rpm.
Cross-check: PG1 gives 195.582 − 794.631 = −599.049 and −0.914063 (1450 − 794.631) = −599.049. PG3 gives 1450 − 195.582 = 1254.42 and −2.35484 (−337.116 − 195.582) = 1254.42. The output turns opposite to A at 337 rpm.

Final Answer: -337
```

## Step 10: Distractors
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

1. -442
2. -615
3. 230
4. 196
5. -1610
```

| Distractor | Misread |
|---|---|
| −442 | PG1 stepped planet read as a simple planet (e1 = −81/36) |
| −615 | Shaft A read as fixed to sun 36 (PG1 locks up) |
| 230 | PG2 double planet read as a single planet (e2 = −94/28) |
| 196 | Output read from carrier C3 (inner sleeve) instead of the drum |
| −1610 | K1 read as driving carrier C1, with ring 81 on the sleeve |

Reserve misreads: −2500 (F2 read as holding sun 28), −2870 (inner shaft ends swapped at the right set), 262 (PG2 read as a stepped planet).

## Step 8: Model failure templates (fill from the real response)

Error type: Connectivity / topology error

### Misread 7: stepped planet read as simple (−442)
```
The response fails by misreading the left planetary set (topological confusion). Its treatment of the middle double-planet set, the brake on ring 94 and the output drum is correct. However, it states "<quote>", treating planets 13 and 32 as <separate / a simple planet>, so it uses e1 = −81/36 = −2.25000 and obtains <equation> = −442. In the drawing, gears 13 and 32 sit side by side on one horizontal pin line: 13 shares an edge with sun 36 and 32 shares an edge with ring 81, forming a single stepped planet. With this reading, e1 = −(81/32)(13/36) = −0.914063, and the coupled Willis equations give n_D = −337.116 rpm = −337. The misread gives −442 instead of the correct −337.
```

### Misread 1: shaft A read as carrying sun 36 (−615)
```
The response fails by misreading which shaft carries sun 36 (topological confusion). It states "<quote>", so the left set has both sun and ring at 1450 rpm and locks solid. That gives n_S2 = 1450 rpm and n_D = 1450/(1 − 94/28) = −615. In the drawing, sun 36 stands on the inner sleeve, the second horizontal line, while shaft A runs beneath it with a visible gap and terminates only in sun 31 at the right set. With the correct reading, n_D = −337. The misread gives −615 instead of the correct −337.
```

### Misread 2: double planet read as single (230)
```
The response fails by misreading the middle planetary set (topological confusion). It states "<quote>", so it uses (n_S2 − n_C2)/(n_R2 − n_C2) = −94/28, giving n_S2 = 4.35714 n_D and, with the other two sets, n_D = 230. In the drawing, planets 18 and 21 each have their own pin at different heights, both joined to carrier plate C2; 18 meshes the sun and 21, and 21 meshes the ring. This double-planet set has e = +94/28, so n_S2 = −2.35714 n_D and n_D = −337. The misread gives 230 instead of the correct −337.
```

### Misread 5: output read from carrier C3 (196)
```
The response fails by misreading which member drives shaft D (topological confusion). Its three Willis equations are correct, but it states "<quote>", taking D from the right-hand carrier and reporting n_C3 = 195.582 ≈ 196. In the drawing, the right carrier's plate drops onto the inner sleeve on the left side of that set. Shaft D is the continuation of the outer drum, which descends on the far right and receives ring 73's flange at a dot. With D = n_C2 = n_R3, the answer is −337. The misread gives 196 instead of the correct −337.
```

## QC Justification: Science Judge
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity [or quotes the author attestation, which is not part of the prompt]. The saved prompt defines the system: "Consider the planetary gearbox shown as a schematic kinematic half-section above the dash-dot axis of rotation, ...". It states the conditions verbatim: "Clutch K1 and brake F2 are fully engaged with no slip, and clutch K2 and brake F1 are fully released. Shaft A is driven at the speed marked." It names exactly one requested quantity: "Determine the rotational speed of shaft D. Take a speed as positive when it is in the same sense as the rotation of shaft A, and negative otherwise.", in rpm to 3 significant figures.

With these conditions the answer is uniquely determined (-337), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

## QC Justification: Image Description Checker (stepped vs double planet)
```
The Image Description Checker finding is incorrect; the description matches the figure, and no change to the image or answer is required.

In the middle set, planets z18 and z21 are stacked in one column and each has its own horizontal pin at a different height (the lower pin meets the carrier plate at a corner, the upper pin at a dot). A stepped planet would need both gears on one pin line, side by side axially, which is how the left set is drawn (z13 and z32 share one pin line). The middle set therefore has a double planet: z18 meshes sun z28 and planet z21, and z21 meshes ring z94. Conversely, the left set cannot be a double planet, because z13 and z32 share a single pin and z13 does not touch ring z81.

The description has been made explicit on these points; the topology, values and GTFA (-337) are unchanged.
```

## Model responses log
| Response | Final answer | Stated reading | Reproduced? | Usable for Step 8? |
|---|---|---|---|---|
