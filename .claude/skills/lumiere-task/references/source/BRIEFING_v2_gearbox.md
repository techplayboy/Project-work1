# Briefing: Project Lumière (Engineering) task authoring

This brief tells you what I'm doing, the rules, what has already been tried, and what to hand back. Read all of it before replying. If I also attach `PROJECT_LUMIERE_HANDOVER.md`, it has the full rules; this brief summarises them and adds what we've learned since.

---

## 1. The job

I write image + text evaluation tasks for frontier vision-language models, in Mechanical Engineering. Each task is:

- an image I make myself with Python/matplotlib, and
- a prompt with exactly one verifiable numerical answer that can only be reached by reading the image correctly.

**The goal is for the models to misread the image and get the wrong number.** The platform runs checker models (**Pass@4**: four attempts). If any attempt is correct, the task fails the difficulty check and is rejected. A trap that only works half the time is not enough.

**Valid failures are misreadings of the image:** connectivity/topology (what joins what), spatial/geometric errors, wrong axis or panel, miscounting.
**Invalid failures:** reasoning errors (wrong physics, bad algebra), OCR mistakes (reading "1.4" as "14"), and knowledge gaps. Keep the maths short so a reviewer can't reclassify a misread as a reasoning error.

---

## 2. Design principles (learned the hard way)

1. **Every misread must give a positive, plausible number.** If a wrong reading gives something negative, impossible or absurd, the model notices, re-reads and corrects itself. Compute every misread numerically before building. Keep each one at least ~25% away from the correct answer so it isn't accepted within tolerance.
2. **Chain several independent reads.** One trap gets beaten. You need 4–5 reads, each of which the model has to get right.
3. **Never describe topology in the prompt.** Give conditions (which solenoid is energised, which clutch is engaged), never connections (what feeds what).
4. **Close the self-check routes.** Don't let tooth-count sums, energy balances or centre distances reveal the topology through arithmetic.
5. **Counter-intuitive answers help**, for example an output faster than the input or a reversed direction.
6. **Clean drawings get read correctly.** Models trace well-separated, clearly drawn members without trouble. What has caught them:
   - line crossings with hops (not connected) next to real junctions (dots),
   - a pilot or control line that starts on a different line than you'd expect,
   - valve envelopes where the active side has to be worked out,
   - nested or concentric members that run past each other.

---

## 3. Attempt log from this session

| Task | Result | What happened |
|---|---|---|
| Hydraulic series circuit v1 (GTFA 183) | Models failed (141, 79.6) | A/B line-hop misread caught them |
| Hydraulic series circuit v2 (GTFA 129) | **Failed Pass@4** | At least one attempt solved it. The Science Judge also flagged the attestation text (platform bug, answered with a QC Justification) |
| Hydraulic v3 (GTFA 177): pilot-operated check, all rods on the left | Block 1 blank (failed to respond twice); Block 2 answered 92.7 (wrong valve envelope / A–B hop) | Resubmitted |
| Gearbox v1, two-stage compound epicyclic (GTFA −406) | **Both models correct** | Each stage could be solved on its own, and the fixed members were obvious. The models even checked centre distances |
| **Gearbox v2** (GTFA 1980) | **Not tested yet: the current task** | See §6 |

---

## 4. Hard rules for each field

### Image
- PNG with a solid white background, saved as RGB with no alpha (`Image.open(f).convert("RGB").save(f)`). Native resolution, no post-processing.
- Schematic or kinematic style, black on white, with all numbers drawn in the image.
- No annotations that help the model.
- Render it and look at it: check for label collisions and clipping.
- Source/licence field (Step 3):
  ```
  Image source:   Original — internal lab image
  License type:   N/A
  Reference:      N/A
  ```

### Prompt (Step 4)
- At most 2000 characters. Answerable only with the image.
- State every assumption, constant (including π if used), unit and sign convention.
- **Never write "in the image", "the provided image" or "as per Image 1"** (this triggers NON_FOUNDATIONAL_REFERENCE). Write "Consider the gearbox shown ..." instead.
- Every number in LaTeX: `$3$`, `$1450 \, \text{rpm}$`, `$\text{K1}$`. No Unicode × and no inline code.
- **Must end with this exact text** (fill in units and the number of significant figures, never more than 3):
  ```
  The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $N$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
  ```

### GTFA (Step 6)
A bare number, rounded to the requested significant figures.

### Image description (Step 7)
- **At least 200 words.** Detailed enough to solve the task without the image. Describe what is drawn; don't point out the trap.
- Say that all numerical data are in the figure (or say which ones come from the prompt).
- **End with a paragraph** restating the prompt's conditions and the requested quantity, starting "The task prompt, not the image, specifies the conditions ...". This pre-empts the Science Judge bug.

### Model failure justification (Step 8)
- Written from the **real** wrong model response.
- Error type: **Connectivity / topology error**.
- Shape: "The response fails by misreading <what> (topological confusion). It <wrong reading + its wrong equation with numbers>. In the drawing, <what is actually drawn>. The correct value is <equation> = <GTFA>. The misread gives <wrong> instead of <GTFA>."
- Write "Response 1", not "Response $1$".
- Choose the response whose error is clearly a misread of the image. Don't choose a blank response or a reasoning error.

### Step-by-step solution (Step 9)
- Steps are numbered "Step 1:", "Step 2:", and so on.
- Step 1 records the data and conditions: the prompt gives the conditions and the figure carries the numbers.
- Steps 2–3 are observation only (what the drawing shows).
- Then the principle and the numbers, with intermediate values to 6 significant figures.
- The last line is exactly `Final Answer: <GTFA>`.

### Distractors (Step 10)
- Exactly 5, all unique, none equal to the GTFA, each tied to a real misread.
- After testing, swap in the models' actual wrong answers.
- This note goes above the list, word for word:
  ```
  Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.
  ```

### QC Justification (for the Science Judge bug)
The Science Judge often raises AMBIGUOUS_PROMPT or UNSTATED_ASSUMPTION by quoting the **author attestation checkbox** ("My prompt is self-contained..." / "The prompt can only be solved with the information in the image"). That text is not the prompt. The fix is a QC Justification that:
1. says the finding quotes the attestation, not the prompt,
2. quotes the prompt's conditions and question word for word, and
3. points to the description's closing paragraph and to Step 1 of the solution.

No change to the task is needed.

---

## 5. What to deliver when I ask for a new task

1. **A matplotlib script** that draws the image. Its docstring encodes the topology.
2. **A `verify.py`** that computes the GTFA independently (for example with a linear solve) and every misread value, with its % distance from the GTFA.
3. **A `TASK_PACKAGE.md`** containing:
   - **Author notes (not submitted):** a trap table with each read, the correct reading and the misread → value.
   - **Step 3:** source and licence.
   - **Step 4:** the prompt, in a code block ready to paste.
   - **Step 6:** the GTFA.
   - **Step 7:** the image description.
   - **Step 9:** the solution.
   - **Step 10:** the distractors plus a table explaining each one.
   - **Step 8:** templates for the most likely misreads.
   - **A QC Justification.**
4. Before handing over, check:
   - the prompt is ≤2000 characters,
   - the description is ≥200 words,
   - every misread is positive and well away from the GTFA,
   - the image has been rendered and inspected.

When I paste model responses back:
- Extract Model 1's and Model 2's final answers.
- Say which one to use for Step 8 and why.
- Write the Step 8 text from it.
- Update the distractors with the real wrong answers.

If both models got it right, say so plainly. Explain which reads they got right, then propose and build a harder version.

---

## 6. Current task: gearbox v2 (submitted for testing, no results yet)

**Design:** two planetary sets sharing one sun shaft (like an automatic transmission), with clutches K1 and K2 and brakes F1 and F2. The prompt says K1 and F2 are engaged and K2 and F1 are released.

**Topology drawn (not stated in the prompt):**
- **Shaft A** (1450 rpm) has a disk out to clutch K1; K1's other half is the drum of ring R1 (z80, m2.5). Shaft A ends at clutch K2; K2's other half is the common sun shaft.
- **Sun shaft:** S1 (z28, m2.5) and S2 (z52, m2). It runs right through the C2 sleeve and output D to brake F1.
- **PG1:** single planet z26 on carrier C1. C1's plate and drum run right over PG2 and are fixed to ring R2 (z92, m2). R2's end disk leads to the hollow output shaft D (flange).
- **PG2 is a double-planet set:** inner z10 meshes S2 and the outer z10; outer z10 meshes R2. Each sits on its own pin on carrier C2. C2's sleeve runs inside D to brake F2.

**Solution:**
- PG1: (n_S − n_C1)/(n_R1 − n_C1) = −80/28
- PG2 with C2 = 0: n_S/n_R2 = +92/52
- n_R1 = 1450 and n_C1 = n_R2 = n_D
- Solving gives n_S = 3510.53 and **n_D = 1984.21 rpm → GTFA 1980** (overdrive, same sense as A).

**Misreads and distractors:**

| Value | Misread |
|---|---|
| 736 | Double planet read as a single or stepped planet |
| 820 | K1 read as joining A to the sun shaft |
| 1070 | F2 read as grounding the sun shaft |
| 1450 | K1 read as joining A to the C1 drum (direct drive) |
| 3510 | Sun shaft read as the output |

**Prompt (as submitted):**
```
Consider the planetary gearbox shown as a kinematic axial section, in which each gear is marked with its tooth number $z$ and module $m$ in millimetres, hatched blocks are the stationary housing, and $\text{K1}$, $\text{K2}$, $\text{F1}$ and $\text{F2}$ are friction shift elements. Clutch $\text{K1}$ and brake $\text{F2}$ are fully engaged with no slip, and clutch $\text{K2}$ and brake $\text{F1}$ are fully released. Shaft A is driven at the speed marked. All gears are spur gears at standard centre distances, and all planets turn freely on their pins. Determine the rotational speed of shaft D. Take a speed as positive when it is in the same sense as the rotation of shaft A, and negative otherwise.

The answer should be expressed in $\text{rpm}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

**Next step:** when I paste the model responses for gearbox v2, analyse them as described in §5. The full package (description, solution, Step 8 templates, QC Justification) is in `TASK_PACKAGE.md`, which I'll attach with the image `gearbox_v2.png`.
