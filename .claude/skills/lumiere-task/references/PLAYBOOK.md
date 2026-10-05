# Project Lumière: Task Authoring Playbook

This playbook combines the three briefing documents (Handover, Briefing v2, Briefing v3) with what we learned building and testing **Hydraulic v4** and **Gearbox v4**. Use it as the single reference for building, submitting and repairing a task.

---

## 1. The job in one paragraph

Each task pairs an image I draw myself with a prompt that has exactly one verifiable numerical answer, which can only be reached by reading the image correctly. The checker models get **Pass@4**: if any of the four attempts is correct, the task is rejected. The goal is a task where every attempt **misreads the image** (topology, geometry, axis or count) and lands on a plausible wrong number. Reasoning errors, OCR slips and knowledge gaps don't count as failures.

---

## 2. The platform workflow (10 steps)

| Step | Field | When it's written | Key rule |
|---|---|---|---|
| 1 | Setup | — | — |
| 2 | Subdomain | Before building | Match the image and the expertise it requires (for example, Mechanical Engineering) |
| 3 | Source and License | In advance | Self-made: `Original — internal lab image / N/A / N/A` |
| 4 | Image & Prompt | In advance | PNG on white; prompt ≤ 2000 characters; exact closing text |
| 5 | Model response | Platform | Wait for both blocks |
| 6 | GTFA | In advance | Bare number at the requested significant figures |
| 7 | Image description | In advance | ≥ 200 words, with geometric evidence and a closing conditions paragraph |
| 8 | Failure mode + justification | After Step 5 | Written from a real wrong response, quoting it |
| 9 | Step-by-step solution | In advance | Step 1 is data, Steps 2–3 are observation, last line `Final Answer:` |
| 10 | Distractors | In advance; revise after testing | Exactly 5, one misread each, **same format as the GTFA** |

---

## 3. How each task is carried out (the process)

### Phase A: Choose
1. Choose the subdomain and the task family (gearbox, hydraulic, linkage, truss and so on).
2. Write the **playbook row**: image type, the textbook defaults to attack, how the parts will be coupled, and at least **6 candidate reads**.

### Phase B: Design the numbers (before drawing anything)
3. Model the correct system and **each misread as its own system**, in code (`model.py`).
4. Search the parameters (tooth counts, bores, flows, dimensions) until every misread:
   - gives a **plausible** answer, never impossible or absurd;
   - still has **exactly one solution** (check the rank of the linear system);
   - is **≥ 25% away** from the GTFA (aim for ≥ 50%);
   - is distinct from every other misread (≥ 10% apart);
   - has **|value| ≥ 100** when the GTFA is a whole number, so each distractor is naturally a whole number at 3 s.f.
5. Close the self-check routes: use unequal modules, avoid tooth-count sums that reveal the meshing, and withhold any data that would let a balance check expose a wrong reading.
6. Prefer a **counter-intuitive answer**: reversal, overdrive, regeneration, flow amplification.

### Phase C: Draw
7. Write `draw_<task>.py`. Its docstring records the full topology, which is never put in the prompt.
8. Render the image, **look at the PNG** and fix label collisions and clipping. Re-render until it is clean.
9. Image rules: white background, saved as RGB with `Image.open(f).convert("RGB").save(f)`, `bbox_inches="tight"`, explicit z-order, black on white, every number in the figure, and labels only on elements the prompt refers to.

### Phase D: Verify
10. Write `verify.py`: compute the GTFA two ways (closed form and a linear solve), then list every misread with its value, its 3-s.f. form, its % distance and a uniqueness check.

### Phase E: Package (`TASK_PACKAGE.md`)
11. **Author notes** (not submitted): the playbook row, the topology and a trap table (read → correct reading → misread → value → Δ).
12. Steps 3, 4, 6, 7, 9 and 10, each in a paste-ready code block.
13. Step 8 templates for the likely misreads.
14. A QC Justification and rebuttal points for the Image Description Checker.
15. **Pre-handover checks**, run in code: prompt ≤ 2000 characters, no banned phrases, exact closing text, description ≥ 200 words, misreads checked.
16. Deliver the PNG, the package and the scripts, and save them to the project under `tasks/<task>/`.

### Phase F: After testing (when the model responses come back)
17. Pull out each block's final answer.
18. **Rebuild each wrong answer from that model's own stated reading.** If it reproduces exactly, the failure is a pure misread.
19. Choose the response for Step 8 (see §8). Write Step 8, quoting the model's own words and equation.
20. Update the distractors (see §7), then update the project notes with which reads the models got right and which caught them.
21. If the models solved it, say so plainly, list the reads they got right, and build a harder version.

---

## 4. Prompt rules (Step 4)

- **Pattern:** `Consider the [system] shown as [diagram type], in which [what the symbols mean]. [Operating conditions]. [Idealisations]. [Rule that closes the key ambiguity]. Determine [one quantity of one named element]. [Sign convention].`
- Give **conditions, never connections**. Write "K1 and F2 engaged", never "common shaft", "in series", "bypass" or "regenerative".
- Never write "in the image", "the provided image" or "as per Image 1". Write "Consider the … shown".
- Put every number and label in LaTeX: `$3$`, `$\text{K1}$`, `$1450 \, \text{rpm}$`. No Unicode × and no inline code.
- State every constant (π to the precision you used), every unit and the sign convention.
- Ask for exactly one quantity.
- It must end with this text:
```
The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $N$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

---

## 5. Image description rules (Step 7)

- At least 200 words, detailed enough to solve the task without the image.
- Give **geometric evidence** for every connection that matters: dot vs hop, which side a line enters from, separate pins vs one pin, where a sleeve starts and ends, which datum a dimension starts from.
- Describe what is drawn and never point out a trap.
- Say that the numbers are in the figure.
- **End with this paragraph:** "The task prompt, not the image, specifies the conditions: … It asks for … in … to N significant figures."

---

## 6. Solution rules (Step 9)

- Step 1: the data and conditions (the prompt gives the conditions; the figure gives the numbers).
- Steps 2–3: observation only (connections, states, planet type, fixed member).
- Then name the principle (Willis, continuity, lever kinematics), with intermediate values to 6 s.f. and a cross-check.
- The last line is exactly `Final Answer: <GTFA>`.

---

## 7. Distractor rules (Step 10), with the lessons we learned

- Exactly 5, all unique, none equal to the GTFA.
- **Each one is the exact computed result of one named misread of the drawing.** Never a rounded model answer and never a filler value.
- **The format must match the GTFA.** The Distractor Format Checker raises FORMAT_MISMATCH (MAJOR ERROR) when the GTFA is a whole number (for example 241 or −1260) and a distractor is a decimal such as 62.6.
  - Fix: choose misreads whose 3-s.f. value is already a whole number (|value| ≥ 100), and design the data in Phase B so that enough misreads land there.
- After testing, swap in a model's real wrong answer **only if** it already fits the GTFA's format.
- This note goes above the list, word for word:
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.
```

---

## 8. Step 8: choosing and writing the failure justification

**How to choose the response:**
1. Rebuild every wrong answer from its stated reading.
2. Prefer the response whose error is a **clear, quotable misread of the drawing** (a pilot line, a dot or hop, a datum, a planet type).
3. Avoid responses whose failure depends on a convention (for example, which valve envelope a solenoid selects), which a reviewer could call a knowledge gap. Never choose a blank response or a reasoning error.

**Skeleton** (error type: **Connectivity / topology error**; for a datum misread alone, use Spatial):
```
The response fails by misreading <what> (topological confusion). Its <correct parts> are correct. However, it states "<quote>", so <wrong equation with numbers> = <wrong>. In the drawing, <what is actually drawn, with geometric evidence>. The correct value is <equation> = <GTFA>. The misread gives <wrong> instead of the correct <GTFA>.
```
Write "Response 1", not "Response $1$".

---

## 9. Known platform issues and standard fixes

| Checker / finding | Cause | Fix |
|---|---|---|
| Science Judge: AMBIGUOUS_PROMPT / UNSTATED_ASSUMPTION | It reads the attestation checkbox or an empty prompt view | Reload the page and confirm the prompt is saved, then submit the QC Justification (template below) |
| Image Description Checker: HALLUCINATED_DETAIL | The checker misreads the image | Don't change the task. Rebut point by point with geometric evidence |
| Distractor Format Checker: FORMAT_MISMATCH | Decimal distractors with a whole-number GTFA | Replace them with whole-number misread values (§7) |

**QC Justification template:**
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity, or quotes the author attestation, which is not part of the prompt. The saved prompt defines the system: "<first sentence>". It states the conditions verbatim: "<conditions>". It names exactly one requested quantity: "<question + convention>", expressed in <units> to <N> significant figures.

With these conditions the answer is uniquely determined (<GTFA>), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and the requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

---

## 10. What the checker models actually do

1. Their maths is rarely what fails. Every wrong answer so far rebuilds exactly from the model's own stated reading.
2. They split the problem into parts when they can, so **couple everything** so that no stage can be solved alone.
3. They fill gaps with **textbook defaults** and state them as fact.
4. They trace the **ends** of long members, not the path between them.
5. They check whether the answer is plausible (sign, magnitude, centre distances) but **never re-trace a connection** when the answer looks ordinary.
6. They take prompt wording at face value. In Hydraulic v4 the model assumed "pilot above tank" without tracing where the pilot line starts.
7. They compare dimensions against pixel scale, so **draw to scale**.
8. Different models fall into different traps, so with Pass@4 you need **≥ 6 independent reads**.

---

## 11. Task record and lessons

| Task | GTFA | Result | What we learned |
|---|---|---|---|
| Gearbox v1 | −406 | Solved | Stages that can be solved one at a time get beaten |
| Gearbox v2 | 1980 | One model failed | Coupling helps |
| Gearbox v3 | −926 | Both failed | Six reads against textbook defaults works |
| Hydraulic v3 | 177 | One blank, one wrong (92.7) | A pilot line from an unexpected line works |
| **Hydraulic v4** | **241 mm/s** | **Both failed (64.7, 50.3)** | See below |
| **Gearbox v4** | **−1260 rpm** | Submitted, awaiting results | Three coupled sets, 7 reads |

**Hydraulic v4 in detail:**
- **Reads the models got right (no longer traps on their own):** the bypass check on the flow control valve, the cylinder rod on the non-standard side, and the rod-to-rod series line.
- **Traps that worked:** a pilot line whose only dot is on a tank line; regeneration through a hop followed by a dot; lever dimensions all measured from one end; and which valve envelope is active.
- **Final distractors:** 428, 382, 623, 142, 164 (whole numbers, one misread each).

---

## 12. Trap catalogue by family

**Planetary gearbox:** a sun on a sleeve rather than the common shaft; a double planet (two pins) vs a stepped planet; a brake holding a drum or carrier rather than the sun; the output on a sleeve flange while the shaft sticking out is the sun shaft to a brake; a clutch to a drum vs to the shaft; drums nested at different radii that end on non-adjacent rings.

**Hydraulic circuit:** a hop vs a dot; a pilot line starting on an unexpected line; the active valve envelope; a cylinder rod on the non-standard side; check valve direction; regeneration paths; series lines that land on the far port; lever dimensions from one datum; a spring pin next to the true pivot.

**Other subdomains (from Briefing v3):** electrical circuits (crossings without dots, ground node), digital logic (inversion bubbles, Q vs Q̄), control block diagrams (summing-junction signs, pick-off position), process diagrams (recycle and bypass return points), trusses (support symbols, internal hinges), graphs (arrowhead direction, label placement).

---

## 13. Final checklist

**Design**
- [ ] Playbook row with ≥ 6 independent reads, each against a textbook default
- [ ] Fully coupled: no part can be solved alone
- [ ] Every misread checked in code: plausible, uniquely solvable, ≥ 25% from the GTFA
- [ ] The GTFA's format is known (whole number or decimal), and the misreads match it
- [ ] Self-check routes closed

**Image**
- [ ] White background, RGB, rendered and inspected, no label collisions
- [ ] Every connection unambiguous to a careful expert
- [ ] Drawn to scale; only the elements the prompt refers to are labelled

**Prompt**
- [ ] ≤ 2000 characters, no "in the image", conditions only, exactly one quantity
- [ ] LaTeX throughout, sign convention stated, exact closing text

**Package**
- [ ] GTFA verified two ways in code
- [ ] Description ≥ 200 words, with geometric evidence and the closing paragraph
- [ ] Solution: Step 1 data, Steps 2–3 observation, ends with `Final Answer:`
- [ ] 5 distractors, each one misread, in the same format as the GTFA
- [ ] QC Justification and rebuttal points ready

**After testing**
- [ ] Wrong answers rebuilt from the models' stated readings
- [ ] Step 8 quotes the model and avoids failures that depend on a convention
- [ ] Distractors updated, still in the GTFA's format
- [ ] Project notes updated
