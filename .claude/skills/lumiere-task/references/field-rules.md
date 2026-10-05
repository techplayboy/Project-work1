# Field rules (platform Steps 1–10)

| Step | Field | Draft in advance? |
|---|---|---|
| 1 | Setup | — |
| 2 | Subdomain | yes — the one matching the image and expertise |
| 3 | Source and License | yes |
| 4 | Image & Prompt | yes |
| 5 | Model response | platform returns the checker answers; then "Model Failure Selection" |
| 6 | GTFA | yes |
| 7 | Image description | yes |
| 8 | Model failure mode + justification | **no** — from a real wrong response |
| 9 | Step-by-step solution | yes |
| 10 | Distractors | yes, then update with real wrong answers |

---

## Image (uploaded in Step 4)

- PNG or JPEG, max 5 images. Solid **white**, non-transparent background. Save as RGB:
  `Image.open(f).convert("RGB").save(f)` (`drawkit.save_png` does this).
- Native resolution, no post-processing (no sharpening/colour correction), no over-cropping.
  `bbox_inches="tight"`, small `pad_inches` (~0.2).
- Schematic/diagram style, black on white, **all needed numbers in the image**, no helper annotations.
- Accepted: schematics (fluid power, electrical, logic, process), engineering drawings with
  dimensions/hatching, analysis diagrams (FBDs, trusses, block diagrams), kinematic sections,
  graphs/networks, labelled plots with axes, units, legends.
- Rejected: shaded 3D renders, CAD viewport screenshots, photos, dark backgrounds, no numbers.
- Three-question test: (1) image carries the measurements? (2) structure to misread?
  (3) two experts would read the same value?
- matplotlib gotchas: white-filled patches paint over lower-zorder lines (set zorder
  explicitly; internal symbols at zorder ≥6); labels near crossings need manual offsets;
  **check the PNG, not the code**. Read the zoom tiles too (`save_png(tiles_dir=...)`):
  a letter sitting on a rope was missed in the downscaled view of pulley v1.

## Step 3 — Source and License

Self-made (default):
```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```
External images are discouraged (recall risk). Only CC BY / CC BY-SA / CC0, verified at
figure level (caption third-party credits; PDF copyright block). Prohibited: NC, ND,
All Rights Reserved, BioRender, patent drawings. External template in `qc-templates.md`.

## Step 4 — Prompt

- ≤2000 characters. Answerable only with the image. Expert-grade.
- Hand-solvable at non-programmable graphing-calculator level. If iteration is needed, name the
  method and the number of iterations.
- State every assumption, idealisation, constant (including $\pi$, $e$), unit, sign/direction
  convention, reading convention for plots ("to the nearest tick mark"), and tie-break rule.
- **Never** "in the image", "the provided image", "as per Image 1", "attached image"
  (NON_FOUNDATIONAL_REFERENCE). Use "Consider the ... shown".
- LaTeX for every problem number and label: `$3$`, `$4.12 \, \text{V}$`, `$5 \, \mu\text{m}$`,
  `$\text{K1}$`, `$10 \times 10^{-4}$`. No Unicode ×/−/°/µ, no backtick inline code, units
  non-italic with `\,`. Be consistent within a task. Tasks are sent back for LaTeX errors.
- Grammar: "in case of a tie"; "perform Dijkstra's algorithm".
- Exactly **one** requested quantity. No connection words.
- **Put the units and significant figures in the question sentence too** ("Determine ... in
  $\text{mm/s}$, reported to $3$ significant figures."), as well as in the boilerplate. The
  Science Judge sometimes sees only the first paragraph and raises SPECIFICITY_MISSING
  ("neither final-answer units nor significant-figure precision is specified").
- The ambiguity-closing rule (e.g. "elements are connected only where joined by a dot") doesn't
  help the models, but defends against "ambiguous" findings — include it.

Tight pattern:
```
Consider the [system] shown as [diagram type], in which [what markings and symbols mean]. [Operating state: switch/valve/clutch states; inputs; loads; initial conditions]. [Idealisations]. [Rule closing the key ambiguity]. Determine [one quantity of one named element] in $\text{[UNITS]}$, reported to $N$ significant figures. [Sign or direction convention; tie-break rule].

The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $N$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

**Exact boilerplate ending** (N ≤ 3 and matching the data precision):
```
The answer should be expressed in $\text{[UNITS]}$. Report your final answer as a $N$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```
For non-numeric answers (a path, a set, a state) replace it with an exact answer-format
statement (e.g. "Report the path as a sequence of node labels separated by commas, e.g. A, C, D.").

## Step 6 — GTFA

A bare number rounded to the requested significant figures (e.g. `-926`, `1980`, `50.7`), or a
short exact answer (word, list, path). Never a sentence.

## Step 7 — Image description

- **≥200 words**; solvable from the description alone (models under test only see the image, so
  detail here costs nothing).
- Describe what is drawn; do **not** point out the trap.
- **Geometric evidence** for every connection that matters: junction dot vs hop, gaps, which pin
  passes through which centre, radii, arrowhead end, which side a line enters from, axis
  assignment, which datum a dimension starts from. Names alone are not enough — the platform's
  checker misreads images too and you will need to rebut it.
- State that all numerical data are in the figure (or which come from the prompt). Give the full
  state-to-component mapping where relevant.
- **End with**: "The task prompt, not the image, specifies the conditions: <list>. It asks for
  <quantity> in <units> to <N> significant figures."

## Step 8 — Model failure mode + justification

- From a **real** wrong response; never a blank/timeout or a reasoning error.
- Reproduce the model's number from its stated reading first.
- Error type: usually **Connectivity / topology error**; otherwise the matching spatial, axis or
  counting category.
- Write "Response 1", not "Response $1$". Skeleton in `qc-templates.md`.

## Step 9 — Step-by-step solution

- "Step 1:", "Step 2:", ... consistently.
- **Step 1**: conditions from the prompt and data from the figure (say which is which — pre-empts
  GROUNDING_GAP).
- **Steps 2–3**: observation only (what the drawing shows: connections, states, values).
- Then name the principle/algorithm, equations with numbers, intermediates to 6 s.f., a cross-check.
- Last line exactly: `Final Answer: <GTFA>`

## Step 10 — Distractors

- Exactly 5, unique, none equal to the GTFA, each tied to a named misread. Plausible to a
  non-expert, dismissable by an expert.
- **Same format as the GTFA.** A whole-number GTFA (241, −1260) with a decimal distractor (62.6)
  raises FORMAT_MISMATCH (MAJOR ERROR). Design misreads with |value| ≥ 100 so that they are whole
  at 3 s.f. Swap in a model's real wrong answer only if it already fits the format.
  `check_package.py` raises an ERROR for this, and `misreads.py` flags it.
- After testing, swap in the models' actual wrong answers.
- Word-for-word note above the list:
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.
```
