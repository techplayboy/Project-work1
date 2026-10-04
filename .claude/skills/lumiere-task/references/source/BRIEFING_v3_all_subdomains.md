# Project Lumière: Task Authoring Briefing v3 (all subdomains)

This briefing is self-contained and applies to **every Engineering and Computer Science subdomain**. It combines the original handover rules with what was learned from real checker-model responses. The worked examples so far are mechanical (hydraulic circuits and gearboxes), but the principles are domain-agnostic. Section 6 translates them into each subdomain.

Read all of it before building or reviewing a task.

---

## 1. What the job is

I author image + text evaluation tasks for frontier vision-language models in Engineering and CS subdomains. Each task pairs an image with a prompt that has **exactly one verifiable answer**, reachable only by reading the image correctly. Usually the image is one I make myself, with Python/matplotlib or similar.

**The goal is for the models to misread the image and get the wrong answer.**

**The difficulty bar is Pass@4.** The checker models get four attempts. If any attempt is correct, the task fails the difficulty check. A trap that works half the time is useless; a task needs several independent traps.

---

## 2. Platform workflow (10 steps)

| Step | Field | Notes |
|---|---|---|
| 1 | Setup | — |
| 2 | Subdomain | Choose the one that matches the image and the expertise required |
| 3 | Source and License | Self-made: "Original — internal lab image" |
| 4 | Image & Prompt | Upload the image(s) and paste the prompt |
| 5 | Model response | The platform returns the checker models' answers |
| 6 | GTFA | Ground-truth final answer |
| 7 | Image description | At least 200 words; must be solvable from the description alone |
| 8 | Model failure mode + justification | Written from a real wrong response |
| 9 | Step-by-step solution | Golden solution |
| 10 | Distractors | Exactly 5 |

Steps 3, 4, 6, 7, 9 and 10 can be drafted in advance. Steps 5 and 8 wait for the model responses. After Step 5, the platform shows "Model Failure Selection": pick one failed response to justify.

---

## 3. Failure modes

**Valid (what the project collects) — all are misreadings of the image:**
1. **Topology / connectivity**: what connects to what (circuits, networks, graphs, mechanisms, process flows, structures). This is the highest priority and the most reliable.
2. **Spatial / geometric confusion**: misattributing dimensions, angles, positions or datums.
3. **Axis / panel / channel confusion**: wrong axis, curve, legend entry or subplot.
4. **Scale / magnification**: carrying the wrong scale across panels, or log vs linear.
5. **Miscounting in dense fields**: nodes, members, teeth, layers, cells.
6. **Signal-vs-artifact discrimination.**

**Invalid (don't count):**
- Reasoning errors (wrong physics or algorithm, bad algebra).
- OCR errors (reading "1.4" as "14"). Picking the wrong tick mark *is* valid; mistyping a label is not.
- Knowledge gaps (anything after 31 Dec 2025).

Step 8 error type: usually **Connectivity / topology error**. Use the matching spatial, axis or counting category when that's the misread.

---

## 4. How the checker models actually behave (learned from real responses)

These patterns were found by reproducing every wrong model answer numerically. They are about how the models read diagrams, so they carry across domains.

1. **Their maths and algorithms are rarely what fails.** Every wrong answer so far reproduces exactly from the connections the model stated: correct equations, correct algebra, correct algorithm steps. Failures were misreads. So multi-step or coupled computation is safe to use: it adds work without adding the risk of a disqualifying reasoning error.

2. **They decompose when they can.** If the problem splits into independent parts (stage by stage, branch by branch, subgraph by subgraph), they solve each part cleanly and win. If no part can be solved alone, every link has to be traced, and that's where they slip.
   - Gearbox v1 could be decomposed: solved.
   - v2 was partly coupled: one model failed.
   - v3 was fully coupled: both failed.

3. **Where the drawing is dense, they fill gaps with textbook defaults.** They state the default as fact, without hedging. Examples seen:

   | Domain | Default the models assumed |
   |---|---|
   | Gear trains | Suns on a common central shaft; the brake holds the sun; output from the carrier; like members joined to like |
   | Hydraulics | Rods drawn on the standard side; valve envelope; a line connects to the nearest line |

   Expected in other domains: ground at the bottom, current flowing left to right, the arrow on an edge points the usual way, the nearest legend entry belongs to a curve, a support is pinned, loads act at centroids.

4. **They trace the ends of a long element, not its path.** Long connectors are where they guess: drums, sleeves, wires, pipes, edges that pass over or under other elements. In gearbox v3, one model swapped which drum ended where.

5. **They check whether the result is physically sensible, never their own connections.** They verify centre distances, units and signs, but never go back to re-trace a connection when the answer looks ordinary.

6. **Clear features get read correctly:** labels, printed values, clearly separate elements, hatching. A clear feature can be one trap among several, but never carries a task alone.

7. **Different models fall into different traps.** Under Pass@4, every attempt has to fall into at least one trap, so the number of independent traps is what counts:
   - about 4 traps failed the difficulty check;
   - 6 traps beat both models.

8. **Blank responses happen** (timeouts on very long reasoning). A blank isn't a usable failure; justify a real wrong answer.

9. **The platform's checker models misread images too.** The Image Description Checker mistook a double planet (two pins) for a stepped planet (one pin). The description must give **geometric evidence** (radii, gaps, which side a line enters from, hop vs dot, arrow direction), not just names, so a rebuttal is easy.

---

## 5. Design principles (domain-agnostic)

1. **Every misread must give a positive, plausible answer.** An impossible result makes the model re-read and fix itself. Examples: negative flow, efficiency above 1, a negative resistance, a probability above 1, a path cost below the minimum edge, an absurd magnitude. Signed answers are fine when the sign convention is stated.
2. **Every misread must leave the problem solvable with one answer.** If a misread over- or under-constrains the system (an unsolvable circuit, a disconnected graph, a mechanism with no fixed member), the model notices. Check each misread in code: rank of the linear system, graph connectivity, and so on.
3. **Keep every misread ≥25% away from the GTFA** (or a different discrete answer), so it can't be accepted within tolerance.
4. **Design against textbook defaults.** For each read, write down the conventional layout, then draw the opposite in the densest region of the image.
5. **Couple everything.** No part can be solved alone, and the requested quantity needs every link.
6. **Use at least 6 independent reads,** each with its own plausible wrong answer.
7. **Route connections long and nested.** Pass them over, under or alongside other elements, and end them next to a decoy element.
8. **Label only what the prompt needs to refer to** (switches, ports, component numbers, named nodes). Don't label intermediate members in a way that hands over the topology.
9. **Never describe topology in the prompt.** Give conditions (switch states, engaged elements, loads, inputs), never connections.
10. **Close the self-check routes.**
    - Avoid number coincidences that reveal pairings (equal sums, symmetric values).
    - Withhold states that would let a balance or conservation check expose a wrong mapping.
11. **Prefer counter-intuitive answers:** reversal, overdrive, regeneration, a negative feedback sign, a non-greedy path, a load path that bypasses the obvious member.
12. **Make it defensible.** Every connection must be unambiguous to a careful human expert (junction dots vs hops, separate pins, arrowheads, dimension datums). The task must survive the checker and a human reviewer.
13. **Use self-made images.** Public figures carry recall risk: models may have read the source paper.

---

## 6. Subdomain playbook

The same method applies everywhere:
1. Find the structure to misread.
2. List the textbook defaults.
3. Contradict them where the drawing is dense.
4. Couple everything so nothing can be solved alone.

| Subdomain | Good image types | Defaults to attack / traps | Coupling idea |
|---|---|---|---|
| **Mechanical: power transmission** | Kinematic sections of gear trains, planetary sets with clutches and brakes | Common sun shaft; brake on the sun; carrier output; separate pins vs stepped planet; nested drums and sleeves | ≥3 planetary sets linked so the Willis equations must be solved together *(proven: gearbox v3)* |
| **Mechanical: fluid power** | ISO 1219 hydraulic/pneumatic circuits | Hop vs junction dot; pilot line from an unexpected line; active valve envelope; rod on the non-standard side; check-valve direction | Series cylinders + regeneration + pilot-operated checks *(proven: hydraulic v3)* |
| **Mechanical: mechanisms** | Linkages, slider-cranks, cam layouts | Which pivot is grounded; which link carries which angle; coupler vs rocker | Multi-loop linkage where the output needs every loop |
| **Mechanical: machine elements** | Bolt groups, welded brackets, shafts with features | Load offset from an edge datum, not the centroid; which bolts or features carry load | Eccentric load + non-uniform pattern + edge datum |
| **Civil / structural** | Trusses, frames, beams with supports and hinges | Pinned vs roller vs fixed support symbols; an internal hinge; members crossing without a joint; load on a joint vs on a member | Statically determinate frame with an internal hinge, where the reaction needs the whole structure |
| **Electrical: circuits** | Schematics (resistor networks, op-amp stages, transistor biasing) | Crossing wires without a dot; the ground node; which terminal is which; a bridge rotated from the standard orientation; component orientation (diode, polarity) | A bridge or multi-loop network solvable only by nodal analysis of the whole circuit |
| **Electrical: power systems** | Single-line diagrams, transformer connections | Breaker states; Δ/Y winding orientation; which bus a feeder lands on | Ring or meshed network with switches whose states are given in the prompt |
| **Electronics / digital logic** | Gate-level schematics, flip-flop chains, MUX trees | Bubble (inversion) on an input vs an output; crossing vs joined wires; clock edge; MSB/LSB order; feedback taken from Q vs Q̄ | Sequential circuit where the state after N clocks needs every gate |
| **Control systems** | Block diagrams, signal-flow graphs | Sign at a summing junction; a pickoff point before vs after a block; a feedback path that skips a block; a forward path drawn right-to-left | Nested loops where Mason's rule needs every loop and its touching relationships |
| **Chemical / process** | PFDs and P&IDs with recycle and bypass streams | Recycle return point; bypass around a unit; which stream a splitter feeds; valve open/closed | Recycle + purge + bypass, so the mass balance needs every stream |
| **Thermal / energy** | Cycle schematics (Rankine, refrigeration, heat pump), heat-exchanger networks | Component order on the hot/cold side; which state sits at which inlet; regenerator cross-connections | Cycle with regeneration and a split, so states can't be read off in sequence |
| **Aerospace / dynamics** | Free-body diagrams, multi-body systems, mass–spring–damper networks | Which body a spring or damper attaches to; force direction; a series vs parallel spring arrangement drawn ambiguously | Coupled multi-DOF system where an eigenvalue or response needs every element |
| **CS: graphs and algorithms** | Directed/weighted graphs, flow networks, state machines | Edge direction (arrowhead at the far end); edges crossing without a node; weight-label placement near a different edge; self-loops; parallel edges | Shortest path or max-flow where the optimum uses an edge that crossing or label placement makes easy to miss |
| **CS: data structures** | Trees, heaps, linked structures, hash tables | Left vs right child; pointer targets crossing; null vs a link to a distant node | A traversal or operation sequence whose result depends on every pointer |
| **CS: architecture / systems** | Datapaths, pipelines, memory hierarchies, network topologies | MUX select lines; forwarding paths; which bus or link a component sits on; crossing buses | Instruction trace or routing outcome that needs every path |
| **Data / plots (any domain)** | Multi-panel plots, dual axes, log scales | Left vs right axis; legend mapping; log vs linear; a panel scale carried over; tick reading | Value combining reads from two panels with different scales |

When working in a new subdomain, first write its row out in this format, with at least 6 candidate reads, before drawing anything.

---

## 7. Hard rules by field

### Image (Step 4 upload)
- PNG or JPEG (maximum 5 images), solid **white** background, no transparency. With matplotlib, save as RGB:
  `Image.open(f).convert("RGB").save(f)`
- Native resolution, no post-processing, no over-cropping. Use `bbox_inches="tight"` with a small `pad_inches`.
- Schematic or diagram style, with all needed numbers in the image. No helper annotations.
- **Accepted:** schematics (fluid power, electrical, logic, process), engineering drawings with dimensions and hatching, analysis diagrams (FBDs, trusses, block diagrams), mechanism and kinematic sections, graphs/networks, labelled plots with axes, units and legends.
- **Rejected:** shaded 3D renders, CAD viewport screenshots, photos of hardware, dark backgrounds, images with no numbers.
- **Three-question test:**
  1. Does the image carry the measurements?
  2. Is there structure to misread?
  3. Would two experts read the same value off it?
- Render it and inspect it before handing over. Check for label collisions, clipping, and leader lines crossing elements.
- matplotlib gotchas:
  - White-filled patches paint over lower-zorder lines, so set zorder explicitly.
  - Labels near crossings need manual offsets.
  - Check the PNG, not the code.

### Source and License (Step 3)
```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```
External images are discouraged because of recall risk. If you use one, only CC BY / CC BY-SA / CC0 are allowed; verify the figure-level licence. NC, ND, All Rights Reserved, BioRender and patent drawings are prohibited.

### Prompt (Step 4)
- At most 2000 characters, answerable only with the image, expert-grade.
- Hand-solvable at graphing-calculator level, with no code. If iteration is needed, name the method and the number of iterations.
- State every assumption, constant (including π and e), unit, sign or direction convention, and tie-break rule.
- **Never write "in the image", "the provided image" or "as per Image 1"** (this triggers NON_FOUNDATIONAL_REFERENCE). Use "Consider the ... shown".
- LaTeX for every problem number and label:
  - `$3$`, `$4.12 \, \text{V}$`, `$5 \, \mu\text{m}$`
  - no Unicode ×, no inline code
  - units non-italic with `\,`
- Watch the grammar ("in case of a tie"; "perform Dijkstra's algorithm").
- **Must end exactly with:**
  ```
  The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $N$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
  ```
  N is at most 3 and matches the data. For non-numeric answers (a path, a set, a state), state the exact answer format instead.

**Tight prompt pattern (conditions only):**
```
Consider the [system] shown as [diagram type], in which [what the markings and symbols mean]. [Operating state: switch, valve or clutch states; inputs; loads; initial conditions]. [Idealisations]. [Rule closing the key ambiguity, e.g. "elements are connected only where joined by a dot" / "a gear rotates with a shaft only where drawn attached" / "edges are directed as drawn"]. Determine [one quantity of one named element]. [Sign or direction convention; tie-break rule].

[boilerplate]
```
- Exactly one requested quantity.
- No connection words: no "in series", "common shaft", "feedback from Q̄", "bypass", "regenerative".
- Put the input values in the image where you can, so the image is required.
- The ambiguity-closing rule doesn't help the models (they ignore it), but it defends the task against "ambiguous" findings.

### GTFA (Step 6)
A bare number rounded to the requested significant figures (e.g. `-926`), or a short exact answer (a word, a list, a path). Never a sentence.

### Image description (Step 7)
- **At least 200 words.** Solvable without the image. Describe what is drawn; don't point out the trap.
- Give **geometric evidence** for every connection that matters: dots vs hops, gaps, which pin goes through which centre, arrowhead ends, which side a line enters from, axis assignment.
- Say that all numerical data are in the figure (or which values come from the prompt).
- **End with:** "The task prompt, not the image, specifies the conditions: <list>. It asks for <quantity> in <units> to <N> significant figures." This pre-empts the Science Judge bug.

### Model failure justification (Step 8)
- Written from a **real** wrong response: quote its wrong statement and its wrong equation or step.
- Pick the response with a clear, quotable image misread. Never pick a blank or a reasoning error.
- Before writing, **reproduce the model's answer from its stated reading.** If it reproduces exactly, the failure is a pure misread.
- Skeleton:
  ```
  The response fails by misreading <what> (<topological / spatial / axis> confusion). Its <correct parts> are correct. However, it states "<quote>", so <wrong equation or step with numbers> = <wrong answer>. In the drawing, <what is actually drawn, with the evidence>. With this reading, <correct equation> = <GTFA>. The misread gives <wrong> instead of the correct <GTFA>.
  ```
- Write "Response 1", not "Response $1$".

### Step-by-step solution (Step 9)
- "Step 1:", "Step 2:", and so on.
- **Step 1:** the conditions from the prompt and the data from the figure.
- **Steps 2–3:** observation only (what the drawing shows: connections, states, values).
- Then name the principle or algorithm, and give the equations or steps, intermediate values to 6 significant figures, and a cross-check.
- Last line exactly: `Final Answer: <GTFA>`

### Distractors (Step 10)
- Exactly 5, unique, none equal to the GTFA, each tied to a named misread.
- **After testing, swap in the models' actual wrong answers.**
- Word-for-word note above the list:
  ```
  Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.
  ```

---

## 8. Known platform issues and standard responses

### Science Judge: AMBIGUOUS_PROMPT / UNSTATED_ASSUMPTION ("no task or requested quantity")
- **Cause:** the judge evaluates the attestation checkbox text or an empty prompt view, not the saved prompt. It often re-fires after saving a later step.
- **First:** reload the page and confirm the Step 4 field holds the full prompt. If it doesn't, re-paste it. If it does, write a QC Justification:
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity [or quotes the author attestation, which is not part of the prompt]. The saved prompt defines the system: "<quote first sentence>". It states the conditions verbatim: "<quote conditions>". It names exactly one requested quantity: "<quote question + convention + units + sig figs>".

With these conditions the answer is uniquely determined (<GTFA>), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

### Image Description Checker: HALLUCINATED_DETAIL (it misreads the image)
- Check the drawing first. If the checker is wrong, don't change the image or the answer.
- Make the description more explicit with geometric evidence, then rebut point by point:
  - what the figure shows, with numbers;
  - why the checker's reading is physically or logically impossible;
  - any misquote in the finding.

---

## 9. Attempt log (evidence behind the lessons)

| Task | Answer | Result | Lesson |
|---|---|---|---|
| Carnot battery COP (public figure) | — | Both failed; accepted | A component in a non-textbook position works |
| Carnot battery round-trip (public figure) | — | Failed Pass@2 | Only one real read; the paper describes the states |
| Excavator regeneration (public figure) | — | Solved | The paper was recalled; the prompt described the mode |
| Gear train, equal modules | — | Solved | Tooth-count sums leaked the meshing |
| Hydraulic series v1 | 183 | Both failed | Hop vs junction trap |
| Hydraulic v2 | 129 | Failed Pass@4 | Too few independent reads |
| Hydraulic v3 | 177 | Blank + 92.7 | Pilot line from an unexpected riser + rods on the non-standard side |
| Gearbox v1 (two-stage) | −406 | Both solved | Could be solved stage by stage; obvious fixed members |
| Gearbox v2 (two coupled sets) | 1980 | One failed, one solved | Coupling helps; defaults are the attack surface |
| Gearbox v3 (three coupled sets) | −926 | **Both failed** (1180, 1340) | Six reads against defaults beat both models |

---

## 10. What to deliver for a new task (any subdomain)

1. **The subdomain playbook row** (Section 6 format) with at least 6 candidate reads, written before drawing.
2. **`draw_<task>.py`**: the script that makes the image. Its docstring encodes the full structure (topology, states, values).
3. **`verify.py`**:
   - an independent GTFA;
   - every misread, with its value, its distance from the GTFA, and a check that the misread problem still has exactly one solution.
4. **`TASK_PACKAGE.md`**:
   - **Author notes (not submitted):** a trap table with each read, the correct reading, the default/misread and its answer.
   - **Steps 3, 4, 6, 7, 9 and 10**, each in a code block ready to paste.
   - **Step 8 templates** for the likely misreads.
   - **QC Justifications.**
5. **Pre-handover checks:**
   - the prompt is ≤2000 characters;
   - the description is ≥200 words with the closing paragraph;
   - every misread is plausible, solvable and ≥25% away from the GTFA;
   - the image has been rendered and inspected.

**When model responses come back:**
1. Extract each block's final answer.
2. Reproduce each wrong answer from that model's stated reading.
3. Recommend which response to justify and why.
4. Write the final Step 8.
5. Update the distractors with the real wrong answers.

If the models solved it, say so plainly, list which reads they got right, and build a harder version that targets the defaults they relied on.

---

## 11. Authoring checklist

**Design**
- [ ] Subdomain playbook row written; at least 6 independent reads, each against a default
- [ ] Coupled: no part solvable alone
- [ ] Every misread computed: plausible, solvable with one answer, ≥25% from the GTFA
- [ ] Self-check routes closed; answer counter-intuitive if possible

**Image**
- [ ] White background, inspected; no label collisions
- [ ] Every connection unambiguous to a careful expert
- [ ] Only elements the prompt refers to are labelled

**Prompt**
- [ ] ≤2000 characters; no "in the image"; conditions only, never connections
- [ ] One quantity; convention and tie-break stated; LaTeX throughout; exact boilerplate

**Package**
- [ ] GTFA verified in code
- [ ] Description ≥200 words, with geometric evidence and the closing paragraph
- [ ] Solution: Step 1 data, Steps 2–3 observation, ends "Final Answer:"
- [ ] 5 distractors with the required note
- [ ] QC Justifications ready

**After testing**
- [ ] Wrong answers reproduced from the models' stated reading
- [ ] Step 8 quotes the model's own wrong statement and equation or step
- [ ] Real wrong answers swapped into the distractors
