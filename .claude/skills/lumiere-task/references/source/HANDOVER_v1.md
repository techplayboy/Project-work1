# Project Lumiere — Task Authoring Handover

Working reference for authoring adversarial multimodal engineering tasks.
Distilled from a full authoring session: what the rules are, what was tried,
what failed, and why.

**Status at handover:** several tasks built and submitted; two accepted through
Science Judge after disagreement; one failed Pass@2 on difficulty. Current
direction is self-generated matplotlib diagrams (reason in §7).

---

## 1. What the project is

Author image + text evaluation tasks that frontier vision-language models get
wrong, in Engineering and CS subdomains. Each task pairs an image with a prompt
that has exactly one verifiable numerical answer, solvable only by reading the
image.

**The difficulty bar is a Pass@2 check:** the checker models get two attempts.
The task only counts as hard enough if it fails. A trap that fires ~50% of the
time survives one attempt but not two.

---

## 2. Task structure (platform workflow, 10 steps)

| Step | Field | Notes |
|---|---|---|
| 1 | *(setup)* | — |
| 2 | Select your subdomain | Dropdown |
| 3 | Source and License | See §5 |
| 4 | Image & Prompt | Upload + prompt text |
| 5 | Model response | Platform returns checker model answers |
| 6 | GTFA | Ground-truth final answer |
| 7 | Image description | Min 200 words, must be solvable from description alone |
| 8 | Model failure mode and justification | Written from real model output |
| 9 | Step-by-step solution | Golden solution |
| 10 | Distractors | Exactly 5 |

Steps 3, 4, 6, 7, 9, 10 can be drafted in advance. Steps 5 and 8 wait for the
platform to return model responses.

---

## 3. Failure modes

### Valid (what the project collects)

All are **misreadings of the image**:

1. **Topological confusion** — what connects to what (circuit, network,
   structure). Highest priority, most reliable.
2. **Spatial / geometric confusion** — misattributing dimensions, angles,
   positions.
3. **Axis / panel confusion** — wrong axis, channel or panel. Valid but lower
   priority.
4. **Magnification / scale interpretation** — carrying the wrong scale across
   panels.
5. **Miscounting in dense fields**.
6. **Signal-vs-artifact discrimination**.

### Invalid (do not count)

- **Reasoning errors** — wrong physics, misapplied equation, bad algebra.
- **OCR errors** — reading "1.4" as "14". (Picking the wrong tick mark *is*
  valid; mistyping a label is not.)
- **Knowledge gaps** — anything published after **31 December 2025**.

**Consequence:** keep the maths short. Two or three operations. The less
reasoning a task requires, the less likely a reviewer reclassifies the failure.

---

## 4. The core design principle

> **A wrong reading must produce a positive, plausible number.**

This is the single most important lesson from the session. If a misread yields
a negative heat flow, a flow fraction above 1, an impossible area, or an absurd
magnitude, the model notices, goes back, and fixes it. The trap self-corrects
and the task passes.

**Always test every misread numerically before building the task.** Compute
what each wrong reading gives. If any is impossible, change the data until all
of them look ordinary.

### Corollaries

- **Withhold the states that enable a self-check.** In the Carnot battery task,
  leaving out $h_5$ and $h_{16}$ removed the energy-balance route to confirming
  a mapping.
- **Never describe topology in the prompt.** Describing the operating mode
  ("both 2/2 valves energised, proportional valve in neutral") effectively
  handed over the flow path. Give *conditions*, never *connections*.
- **Answers that defy intuition help.** A round-trip efficiency above 1, or an
  output faster than input, works against a model that sanity-checks toward the
  expected direction.
- **Chain multiple independent reads.** One trap at ~70% reliability clears
  Pass@2 often. Five independent reads at 70% each clears ~17% of the time,
  and twice in a row far less.

---

## 5. Hard rules

### Images

**Pass:**
- Schematics: hydraulic/pneumatic circuits (ISO 1219), process flow diagrams,
  single-line diagrams, block diagrams
- Engineering drawings: orthographic views with proper dimension lines,
  section views with hatching, assembly drawings with balloon numbers
- Analysis diagrams: beam/frame diagrams, free-body diagrams, truss layouts,
  kinematic diagrams
- Mechanism sections: gear trains with tooth counts, shaft layouts
- Data figures: labelled plots with axes, units, ticks, legend, scale bars

**Fail:**
- Rendered/shaded 3D views, product visuals, concept art
- CAD viewport screenshots (including measurement overlays)
- Dark or photographic backgrounds
- Photographs of hardware
- Anything with no numbers on it

**Technical constraints:**
- PNG or JPEG only, max 5 images per task
- Solid **white** background, non-transparent
- No post-processing: no sharpening, enhancement, colour correction
- No added annotations that help the model
- Preserve all axis labels, scale bars, legends, ladder markings
- High resolution, no over-cropping

**The three-question test for any candidate image:**
1. Does it carry the measurements? (If every number is in the prompt, the image
   is decoration.)
2. Is there structure to misread? (Connections, load paths, crossings.)
3. Could two engineers read the same value off it? (Dimension lines with
   arrowheads and datums: yes. Perspective render: no.)

### Licensing

Licensing is the **most common rejection reason**.

**Acceptable:** self-created originals; CC BY 2.0/3.0/4.0; CC BY-SA; CC0;
"Original — internal lab image".

**Prohibited:** CC BY-NC, CC BY-ND, CC BY-NC-ND, All Rights Reserved,
BioRender figures (hard block even inside a CC BY paper), patent drawings
(licence position unclear).

**Checks:**
- Figure licence can differ from paper licence — read the figure caption for
  third-party credits.
- Open access ≠ free to reuse. Verify the specific CC designation.
- The licence version in page metadata can be wrong. Read the copyright block
  in the PDF itself (usually last page): *"© YEAR by the authors. Licensee
  MDPI... Creative Commons Attribution (CC BY) license
  (http://creativecommons.org/licenses/by/4.0/)"*.
- Keep the source/licence fields consistent: licence **link** field gets
  `https://creativecommons.org/licenses/by/4.0/`, not the DOI.

### Prompt

- **Image-dependent**: unanswerable from text alone.
- **Unambiguous**: state all modelling assumptions, constants, units,
  significant figures. Test: could an engineer in the same subdomain
  independently reach the same number?
- **Reading conventions stated** for plots ("to the nearest tick mark"). If a
  reviewer would need a straight edge, it's ambiguous.
- **Expert-grade**: genuine domain knowledge required.
- **Max 2000 characters.**
- **Hand-solvable**: models have no Python. Non-programmable graphing
  calculator level. If iteration is needed, name the method and iteration count.
- **All constants given in the prompt**, including $\pi$ and $e$.
- **No meta-references** — these trigger `NON_FOUNDATIONAL_REFERENCE`:
  - Bad: "as per Image 1", "the provided image", "in the image attached"
  - Good: "Consider the Carnot battery shown", "For the directed graph shown"
- **Grammar**: watch articles. "in case of **a** tie"; "perform Dijkstra's
  algorithm" (not "the Dijkstra's algorithm").

### Required ending boilerplate (exact)

```
The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $[1, 2, \text{ or } 3]$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

Requested sig figs must match the precision of the given data. Never more
than 3.

### LaTeX / KaTeX

- Every number tied to the problem in LaTeX: `$4$`, not `4`.
- No Unicode (`×`), no inline code, no unrendered math.
  `$10 \times 10^{-4}$`, never `10*10^-4` or `` `10*10^-4` ``.
- Units non-italic with an explicit space: `$4.12 \, \text{V}$`.
  Pick one formatting method and be consistent within a task.
- Greek letters exempt from the non-italic rule: `$5 \, \mu\text{m}$`,
  `$12 \, {\rm m}\Omega$`.
- In the failure justification, write "Response 1" not "Response $1$".
- **Tasks get sent back for LaTeX errors in the prompt.**

### Step-by-step solution

- Number steps consistently: "Step 1:", "Step 2:", ...
- **Step 1 records the data given in the prompt** and states that the figure
  carries no numerical values (this pre-empts `GROUNDING_GAP` findings).
- **Next one or two steps are observation only** — anchor in the image.
- Then name the engineering principle explicitly, plug in numbers, show results.
- Final line: `Final Answer: <GTFA verbatim>`.

### GTFA

A number, word, short phrase, or list. Never a sentence that could be worded
several ways.

### Distractors

- Exactly **5**, all unique, none equal to the GTFA.
- Plausible to a non-expert, dismissable by an expert.
- Anchor to real misreads. **Mine actual model failures for distractor values.**
- Required note above the list, verbatim:

```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.
```

### Image description (Step 7)

- **Minimum 200 words.**
- Must be detailed enough to solve the prompt **without seeing the image**.
- Must give the full state-to-component mapping (which state is at which
  component's inlet/outlet).
- Describe values that appear in the image; do **not** interpret or flag the trap.
- If the numbers come from the prompt rather than the figure, say so explicitly:
  *"The figure contains no numerical property values; the enthalpies ... are
  given in the prompt text, not in the image."* This closes grounding findings.
- Close with a paragraph restating the prompt's assumptions and the requested
  quantity. This pre-empts the Science Judge bug (§9).

The models under test only see the image, so detail here costs nothing.

---

## 6. Attempt log — how models beat each version

Read this before designing anything. Each entry is a real failure.

### Attempt 1 — compound epicyclic gear train (self-made, matplotlib)
**Result:** Model 1 solved it.
**How:** Used equal modules throughout, so tooth sums gave the mesh pairing away
($z_A + z_C = z_E - z_C = z_D - z_B = 48$). It also recognised the Wolfrom
layout from memory and sanity-checked that $1450 \to 194$ rpm was a plausible
reduction. It barely read the drawing.
**Lesson:** arithmetic coincidences leak topology. Use unequal modules.

### Attempt 2 — same gear train, v2
**Fixes:** different modules per stage; sun *fixed* on a bolted sleeve; carrier
as input; output faster than input to defeat the reduction prior.
**Result:** untested — direction changed to public images.

### Attempt 3 — Carnot battery heat pump COP (MDPI Fig 6)
**Result:** both models failed. Accepted.
**Trap:** MSHP sits on the low-pressure side between states 6 and 1, not after
the compressor. Model 1 used $h_2 - h_3$ (textbook position). Valid topology
error.
**Weakness found later:** the prompt said "the molten salt loop that also
supplies MSHE", which told the model to trace the loop — the one read that
mattered.

### Attempt 4 — Carnot battery round-trip efficiency
**Result:** failed Pass@2 on difficulty.
**Why:** only one read was genuinely required. Also the paper (2023, within
knowledge cutoff) describes the state sequence in words.

### Attempt 5 — round-trip efficiency, 5 chained reads
**Self-review found:** two of the five traps self-corrected. Taking the LTR cold
side as the AC branch gave $x = 1.82$ (impossible). Assuming the textbook heater
position gave *negative* heat. Both signalled the error.
**Fix:** redesigned data so the wrong split gives $x = 0.750$ — perfectly
plausible.
**Result:** both models failed. Model 1 answered $1.16$ vs GTFA $1.13$;
it placed MSHE before the turbine and never used $h_7$. Its own consistency
check passed on the wrong layout — proof the data gave no warning.

### Attempt 6 — excavator flow regeneration circuit (MDPI Energies Fig 6)
**Result:** Model 1 solved it first try.
**Why:** the paper is from 2020 and states $p_{1r}(A_1 - A_2) = p_1 A_1$
in the text. Worse, the prompt described the operating mode, which handed over
the regeneration topology.
**Lesson:** for public images, assume the model has read the paper. And never
describe the mode.

### Summary of model shortcuts observed

| Shortcut | Counter |
|---|---|
| Recall of the source paper | Self-made images, or replace all numbers and ask something the paper never answers |
| Arithmetic coincidences in given data | Unequal modules/scales; no pairing that adds up |
| Textbook layout recognition | Non-standard arrangements; fixed member in an unusual place |
| Plausibility check on the answer | Make the true answer counter-intuitive |
| Self-consistency check | Withhold the states that enable the balance |
| Prompt leaking topology | Give conditions only, never connections |

---

## 7. Why self-generated images

Public images carry the recall problem (Attempts 3–6). Searching for a figure
with the right numbers *and* the right trap *and* a clean licence takes longer
than drawing one.

**matplotlib output:**
- black on white, native resolution, no post-processing → satisfies every image
  rule by construction
- licensed as original work → Step 3 becomes "Original — internal lab image",
  source and reference fields "N/A"
- no model has ever seen it
- full control over where the trap sits

**Setup:** Anaconda, or `pip install matplotlib numpy pillow`. Run the script,
upload the PNG.

### Gotchas found while drawing

- **Z-order:** `Rectangle` patches with white fill (zorder 4) paint over lines
  drawn later at default zorder 3. Internal valve symbols need explicit
  `zorder=6` or they vanish.
- **Label collisions:** check the rendered PNG, not the code. Labels near line
  crossings need manual offsets.
- **Save as RGB:** `Image.open(...).convert("RGB").save(...)` strips the alpha
  channel so the background is genuinely opaque white.
- Always `bbox_inches="tight"` with a small `pad_inches` so nothing clips.

---

## 8. Task type catalogue

Six designs, all Mechanical Engineering, all hand-solvable, all with the
plausible-wrong-answer property.

### 1. Series cylinder circuit with a blocking check valve ★ recommended
Rod side of cylinder 1 feeds cap side of cylinder 2. A bypass joins the two cap
sides through a check valve oriented to **block**.
- Ask: extension speed of cylinder 2
- Correct: $v_2 = Q A_{1,\text{rod}} / (A_{1,\text{cap}} A_{2,\text{cap}})$
- Misreads: pump flow straight into cylinder 2; cross-connection read rod-to-rod;
  check valve treated as open; answering cylinder 1; area ratio inverted
- Why: models read check-valve direction poorly and default to "connected"

### 2. Compound gear train, unusual arrangement
Axial section, unequal modules per stage, fixed member somewhere unexpected.
- Ask: output shaft speed
- Misreads: which gear the sun meshes; which member is grounded; compound planet
  read as simple
- Print tooth counts only, never centre distances

### 3. Linkage with a non-obvious ground pivot
Four-bar or slider-crank, two pivots close together, only one hatched as ground.
- Ask: output link velocity at the instant shown
- Misreads: wrong pivot as ground; angle attributed to wrong link; coupler/rocker
  confused

### 4. Bracket with offset load and edge datum
Bolt group where the load line is offset from the centroid, dimensioned from an
edge rather than the centroid.
- Ask: force on the most heavily loaded bolt
- Misreads: arm from wrong datum; centroid assumed at plate centre; printed
  offset used directly as the arm
- Answer scales smoothly with the arm, so a wrong datum looks normal

### 5. Shaft with a dense field of similar features
Sectional elevation: shoulders, circlip grooves, bearing seats, keyways.
- Ask: reaction at a named support, or torque past a section
- Misreads: miscounting which features carry load
- **Weakest of the six** — a miscount can shade into a reasoning error

### 6. Pipe network with a crossing that isn't a junction
Bridge arcs at the crossing, a genuine tee nearby.
- Ask: flow in a named branch, or pressure drop between two points
- Misreads: crossing read as junction; hop read as connection

---

## 9. Known platform issues

### Science Judge misreads the prompt field

**Symptom:** two MAJOR ERROR findings that recur on every submission:
- `AMBIGUOUS_PROMPT` — quoting *"My prompt is self-contained: it is unambiguous
  and fully solvable without external resources or internet access."*
- `UNSTATED_ASSUMPTION` — claiming the modelling assumptions are absent

**Cause:** the quoted sentence is the **author attestation checkbox text**, not
the prompt. The judge is evaluating the checklist instead of the saved prompt.

**Handling:** this was confirmed by a human reviewer ("Both findings are
resolved"). The task came back only because the QC Justification block was left
empty. Fill it in — the findings themselves need no task change.

**Two defences:**
1. Fill the QC Justification block (template in §10).
2. Add a closing paragraph to the image description restating the assumptions
   and requested quantity. The judge *does* read that field, so both findings
   clear even when it can't see the prompt.

Also verify after a page reload that the prompt field actually holds the full
text. If it's empty, the judge is right.

---

## 10. Reusable templates

### QC Justification (adapt the quoted prompt text)

```
Both Science Judge findings are incorrect and require no change to the task.

Finding 1 quotes the author attestation statement ("My prompt is self-contained..."), which is not part of the prompt. The prompt asks a specific engineering question and names one quantity: "<quote the question verbatim>", reported as <units> to <n> significant figures.

Finding 2 states the idealizations are absent. The prompt states them verbatim: "<quote the assumptions sentence verbatim>".

The image description's final paragraph also restates these conditions and the requested quantity, and Step 1 of the golden solution attributes them to the prompt.

Both findings are artefacts of the prompt text not being evaluated, and not omissions in the task.
```

### Image description closing paragraph

```
The task prompt, not the image, specifies the conditions for the analysis: <list assumptions>. The prompt asks for <quantity>, defined as <definition>, reported to $N$ significant figures.
```

### Model failure justification skeleton

```
The response fails by misreading the connections in the layout (topological confusion). Its <list what it got right> are correct, but it assigns <quantity> to <wrong reading>:

$$<the model's wrong equation with numbers>$$

In the layout, <what the drawing actually shows>. The correct <quantity> is therefore <correct equation> = <value>. The misread gives <wrong answer> instead of the correct <GTFA>.
```

Error type to select: **Connectivity / topology error** (for topology misreads).

### Licence fields (external CC BY)

```
Image source:   External — open-access (CC BY)
License type:   CC BY 4.0
License link:   https://creativecommons.org/licenses/by/4.0/
Article DOI:    https://doi.org/<doi>
Published in:   <Journal> (<Publisher>), Vol. <v>, Issue <i>, Article <n>, <year>
```

### Licence fields (self-made)

```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```

---

## 11. Working matplotlib script

Series cylinder circuit (task type 1). Produces `image1.png`.

```python
"""
Series (synchronising) cylinder circuit - ISO 1219 style, drawn with matplotlib.

Topology encoded in the drawing:
  Pump 1 -> relief 2 -> DCV 3 (shown in the extend position: P->A, B->T)
  DCV port A          -> CAP side of cylinder 4
  ROD side of cyl 4   -> CAP side of cylinder 5      (series cross-connection)
  ROD side of cyl 5   -> DCV port B -> tank
  Bypass cap4 -> cap5 through check valve 6, oriented to BLOCK that direction

Outputs image1.png : black on white, native resolution, no post-processing.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle
from PIL import Image

LW, EDGE, FS = 1.8, "black", 16
fig, ax = plt.subplots(figsize=(14.5, 10.5), dpi=200)
fig.patch.set_facecolor("white")

# ---- vertical levels ----
Y_TANK   = 0.50
Y_TEE    = 0.95     # DCV tank return run
Y_PUMP   = 2.60     # pump / relief pressure run
Y_CYL    = 8.10     # cylinder bottom edge
Y_CROSS  = 7.30     # rod4 -> cap5 series line
Y_BYPASS = 6.40     # bypass through check valve 6
Y_PORTA  = 5.60     # DCV A -> cap4
Y_PORTB  = 5.15     # rod5 -> DCV B


def line(pts, lw=LW, z=3):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=EDGE, lw=lw, solid_capstyle="round", zorder=z)


def box(x, y, w, h, lw=LW, z=4):
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=EDGE,
                           lw=lw, zorder=z))


def dot(x, y):
    ax.plot([x], [y], marker="o", ms=6.5, color=EDGE, zorder=8)


def txt(x, y, s, ha="center", va="center", fs=FS):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=EDGE, zorder=9)


def arrow(x, y, dx, dy, lw=LW):
    ax.annotate("", xy=(x + dx, y + dy), xytext=(x, y),
                arrowprops=dict(arrowstyle="-|>", lw=lw, color=EDGE,
                                mutation_scale=15), zorder=8)


def tank(x, y=Y_TANK, w=1.05):
    line([(x - w / 2, y), (x + w / 2, y)])
    line([(x - w / 2 + 0.17, y - 0.18), (x + w / 2 - 0.17, y - 0.18)], lw=1.4)


def spring(x0, y0, x1, n=6, amp=0.20):
    pts, dx = [(x0, y0)], (x1 - x0) / (n + 1)
    for i in range(n):
        pts.append((x0 + dx * (i + 1), y0 + (amp if i % 2 == 0 else -amp)))
    pts.append((x1, y0))
    line(pts, lw=1.4)


def cylinder(x, L, H, name):
    """Double-acting cylinder on Y_CYL, rod exits right. Returns cap/rod port x."""
    box(x, Y_CYL, L, H)
    pw, px, pr = 0.05 * L, x + 0.44 * L, 0.24 * H
    box(px, Y_CYL, pw, H)                                         # piston
    box(px + pw, Y_CYL + H / 2 - pr / 2, (x + L + 0.30 * L) - (px + pw), pr)
    cap_x, rod_x = x + 0.11 * L, x + 0.87 * L
    txt(x + L / 2, Y_CYL + H + 0.42, name)
    txt(cap_x - 0.34, Y_CYL - 0.36, "A")
    txt(rod_x + 0.34, Y_CYL - 0.36, "B")
    return cap_x, rod_x


# ---------------- cylinders ----------------
c4_cap, c4_rod = cylinder(1.30, 4.10, 1.35, "4")
c5_cap, c5_rod = cylinder(8.30, 4.10, 1.35, "5")

# ---------------- directional control valve 3 ----------------
vx, vy, vw, vh = 4.20, 3.10, 3.60, 1.60
sq = vw / 3
for i in range(3):
    box(vx + i * sq, vy, sq, vh)

# left square: extend position (P->A, B->T), parallel arrows
line([(vx + 0.35, vy + 0.30), (vx + 0.35, vy + 1.05)], z=6)
arrow(vx + 0.35, vy + 0.92, 0, 0.24)
line([(vx + 0.85, vy + 1.30), (vx + 0.85, vy + 0.55)], z=6)
arrow(vx + 0.85, vy + 0.68, 0, -0.24)

# centre square: closed centre, all ports blocked
cx0 = vx + sq
for dx in (0.35, 0.85):
    line([(cx0 + dx, vy + vh), (cx0 + dx, vy + vh - 0.45)], z=6)
    line([(cx0 + dx - 0.20, vy + vh - 0.45), (cx0 + dx + 0.20, vy + vh - 0.45)], z=6)
    line([(cx0 + dx, vy), (cx0 + dx, vy + 0.45)], z=6)
    line([(cx0 + dx - 0.20, vy + 0.45), (cx0 + dx + 0.20, vy + 0.45)], z=6)

# right square: retract position (P->B, A->T), crossed arrows
rx0 = vx + 2 * sq
line([(rx0 + 0.30, vy + 0.30), (rx0 + 0.90, vy + 1.05)], z=6)
arrow(rx0 + 0.77, vy + 0.89, 0.15, 0.19)
line([(rx0 + 0.90, vy + 0.30), (rx0 + 0.30, vy + 1.05)], z=6)
arrow(rx0 + 0.43, vy + 0.89, -0.15, 0.19)

# solenoid (left) and return spring (right)
box(vx - 0.85, vy + 0.35, 0.85, 0.90)
line([(vx - 0.85, vy + 0.35), (vx, vy + 1.25)], lw=1.4)
spring(vx + vw, vy + 0.80, vx + vw + 0.90)
line([(vx + vw + 0.90, vy + 0.42), (vx + vw + 0.90, vy + 1.18)], lw=1.4)
txt(vx - 1.35, vy + vh / 2, "3", ha="right")

pA_x, pB_x = vx + 0.35, vx + 0.85
txt(pA_x - 0.32, vy + vh + 0.30, "A")
txt(pB_x + 0.34, vy + vh + 0.30, "B")
txt(pA_x - 0.32, vy - 0.30, "P")
txt(pB_x + 0.34, vy - 0.30, "T")

# ---------------- pump 1 and relief valve 2 ----------------
pc = (1.45, 1.55)
ax.add_patch(Circle(pc, 0.62, facecolor="white", edgecolor=EDGE, lw=LW, zorder=4))
ax.add_patch(Polygon([(pc[0], pc[1] + 0.60), (pc[0] - 0.28, pc[1] + 0.14),
                      (pc[0] + 0.28, pc[1] + 0.14)], closed=True,
                     facecolor=EDGE, edgecolor=EDGE, zorder=5))
txt(pc[0] - 1.00, pc[1], "1", ha="right")
line([(pc[0], pc[1] + 0.62), (pc[0], Y_PUMP)])
line([(pc[0], pc[1] - 0.62), (pc[0], Y_TANK)])
tank(pc[0])

rvx, rvy, rvw, rvh = 2.70, 1.05, 0.90, 1.10
box(rvx, rvy, rvw, rvh)
line([(rvx + 0.45, rvy + 0.24), (rvx + 0.45, rvy + 0.84)], lw=1.5, z=6)
arrow(rvx + 0.45, rvy + 0.58, 0, -0.28, lw=1.5)
spring(rvx + rvw, rvy + rvh / 2, rvx + rvw + 0.85, n=5, amp=0.17)
line([(rvx + rvw + 0.85, rvy + 0.20), (rvx + rvw + 0.85, rvy + 0.90)], lw=1.4)
txt(rvx - 0.30, rvy + rvh / 2, "2", ha="right")
line([(rvx + 0.45, Y_PUMP), (rvx + 0.45, rvy + rvh)])
line([(rvx + 0.45, rvy), (rvx + 0.45, Y_TANK)])
tank(rvx + 0.45)

dot(pc[0], Y_PUMP)
dot(rvx + 0.45, Y_PUMP)
line([(pc[0], Y_PUMP), (pA_x, Y_PUMP), (pA_x, vy)])          # P line

# ---------------- tank return from port T ----------------
line([(pB_x, vy), (pB_x, Y_TEE), (9.40, Y_TEE), (9.40, Y_TANK)])
tank(9.40)

# ---------------- main working lines ----------------
line([(pA_x, vy + vh), (pA_x, Y_PORTA), (c4_cap, Y_PORTA), (c4_cap, Y_CYL)])
line([(c4_rod, Y_CYL), (c4_rod, Y_CROSS), (c5_cap, Y_CROSS), (c5_cap, Y_CYL)])
line([(pB_x, vy + vh), (pB_x, Y_PORTB), (c5_rod, Y_PORTB), (c5_rod, Y_CYL)])

# ---------------- bypass with check valve 6 (blocks this direction) ------------
dot(c4_cap, Y_BYPASS)
dot(c5_cap, Y_CROSS)
line([(c4_cap, Y_BYPASS), (c5_cap, Y_BYPASS), (c5_cap, Y_CROSS)])
cv_x = 5.60
ax.add_patch(Circle((cv_x, Y_BYPASS), 0.32, facecolor="white", edgecolor=EDGE,
                    lw=LW, zorder=5))
line([(cv_x + 0.32, Y_BYPASS - 0.50), (cv_x + 0.32, Y_BYPASS + 0.50)])   # seat right
txt(cv_x, Y_BYPASS - 0.85, "6")

ax.set_xlim(0.05, 14.30)
ax.set_ylim(0.05, 10.30)
ax.set_aspect("equal")
ax.axis("off")
plt.savefig("image1.png", dpi=200, facecolor="white", bbox_inches="tight",
            pad_inches=0.20)
Image.open("image1.png").convert("RGB").save("image1.png")
print("saved image1.png")
```

### Verified numbers for this circuit

Cylinder 4: bore $100 \, \text{mm}$, rod $70 \, \text{mm}$.
Cylinder 5: bore $80 \, \text{mm}$. Pump $30 \, \text{L/min}$.

```
A1cap = 7854.00 mm^2   A1rod = 4005.54 mm^2
A2cap = 5026.56 mm^2   A2rod = 3436.12 mm^2
v1 = Q/A1cap        = 63.6618 mm/s
Q2 = A1rod * v1     = 255000 mm^3/s
v2 = Q2/A2cap       = 50.7305 -> GTFA 50.7 mm/s
```

Distractors, all positive and plausible:

| Value | Misread |
|---|---|
| $99.5$ | Pump flow taken straight into cylinder 5 |
| $63.7$ | Answers cylinder 4 instead |
| $74.2$ | Cross-connection read as rod-to-rod |
| $150$ | Check valve read as open, both paths summed |
| $195$ | Area ratio inverted |

---

## 12. Authoring checklist

Before building:
- [ ] Task type chosen; trap identified
- [ ] Every misread computed numerically — **all positive and plausible?**
- [ ] Self-check routes closed (withhold enabling states)
- [ ] Answer counter-intuitive if possible
- [ ] Multiple independent reads chained

Image:
- [ ] White background, PNG, native resolution, no post-processing
- [ ] Rendered and visually inspected: no label collisions, nothing clipped
- [ ] Carries the topology/geometry, no helper annotations
- [ ] Licence verified at figure level

Prompt:
- [ ] Under 2000 characters
- [ ] No meta-references to the image
- [ ] All assumptions, constants, units, sig figs stated
- [ ] Topology **not** described
- [ ] All numbers in LaTeX, units non-italic with `\,` spacing
- [ ] Exact boilerplate at the end

Package:
- [ ] GTFA verified independently (two methods, ideally in code)
- [ ] Solution Step 1 records prompt data; Steps 2–3 observation only
- [ ] Final line is `Final Answer: <GTFA>`
- [ ] Image description ≥200 words, solvable alone, closing assumptions paragraph
- [ ] 5 unique distractors with the required note
- [ ] QC Justification ready for the Science Judge findings

After submission:
- [ ] Model responses pasted back
- [ ] Failure justification quotes the actual wrong equation
- [ ] Error type set to Connectivity / topology error (if applicable)
- [ ] Model's wrong answer swapped into the distractor list

---

## 13. Open questions

1. **Are self-made images accepted on this queue?** "Original — internal lab
   image" is listed as acceptable, but recent submissions all went in as
   external CC BY. Confirm before investing in matplotlib tasks.
2. **Pass@2 semantics.** Whether it means "at least one of two attempts correct"
   or something else was never fully confirmed. Design for reliable failure
   either way.
3. **Second trap for the series circuit.** One topology read may not survive
   Pass@2. Adding a counterbalance valve on the return line would force a second
   read (which line is pressurised).
