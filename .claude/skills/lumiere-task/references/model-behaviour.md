# How the checker models behave

Learned by reproducing every wrong answer numerically from the model's stated reading.
These are about how models *read diagrams*, so they transfer across domains. Add new
observations at the bottom with the task that showed them.

1. **Their maths/algorithms rarely fail.** Every wrong answer so far reproduces exactly from the
   connections the model stated. So coupled, multi-step computation is safe: it adds work without
   risking a disqualifying reasoning error. (This supersedes the older "keep the maths to 2–3
   operations" advice — but keep each *individual* step standard and hand-solvable.)
2. **They decompose when they can.** Independent parts get solved cleanly. Gearbox v1
   (decomposable) — solved; v2 (partly coupled) — one failed; v3 (fully coupled) — both failed.
3. **Where the drawing is dense, they fill gaps with textbook defaults** and state them as fact:

   | Domain | Default assumed |
   |---|---|
   | Gear trains | Suns on a common central shaft; brake holds the sun; output from the carrier; like members joined to like |
   | Hydraulics | Rods on the standard side; valve envelope; a line connects to the nearest line |
   | Expected elsewhere | Ground at the bottom; current flows left→right; arrows point the usual way; nearest legend entry owns a curve; supports pinned; loads at centroids |

4. **They trace the ends of a long element, not its path.** Drums, sleeves, wires, pipes, edges
   passing over/under other elements are where they guess (gearbox v3: swapped which drum ended where).
5. **They sanity-check the result (units, sign, centre distance), never re-trace connections** when
   the answer looks ordinary — hence misreads must give ordinary answers.
6. **Clear features are read correctly**: labels, printed values, well-separated elements,
   hatching. A clear feature can be one trap among several, never the whole task.
7. **Different models fall into different traps.** Under Pass@4 every attempt must hit at least one
   trap; count independent traps. ~4 traps failed the difficulty check; 6 beat both models.
8. **Blank responses happen** (timeouts on very long reasoning). Not usable for Step 8.
9. **Platform checkers misread too.** The Image Description Checker read a double planet (two pins)
   as a stepped planet (one pin). Descriptions need geometric evidence for rebuttal.

## Shortcuts the models use, and counters

| Shortcut | Counter |
|---|---|
| Recall of a source paper | Self-made images only |
| Arithmetic coincidences (equal tooth sums, symmetric values) | Unequal modules/scales; no pairings that add up |
| Textbook layout recognition | Non-standard arrangement; fixed member in an unusual place |
| Plausibility check on the answer | Counter-intuitive true answer; ordinary-looking misreads |
| Self-consistency / balance check | Withhold the states that enable it |
| Prompt leaking topology | Conditions only, never connections or mode names |
| Decomposition | Couple every part so nothing is solvable alone |

## Observations log

| Date | Task | Observation |
|---|---|---|
| — | gearbox v3 | Both models assumed common sun shaft + carrier output; swapped drum ends |
| — | hydraulic v3 | Pilot line from an unexpected riser + rods on the non-standard side caught the response that answered |
| 2026-10 | hydraulic v4 | **Prompt rules are crutches.** Both models quoted our symbol-convention sentences verbatim and used them as a checklist. State only what defensibility needs (e.g. "fastened only at dots"), not how each symbol works |
| 2026-10 | hydraulic v4 | **Label-to-endpoint matching beats hop traps.** A model described the 60 % outlet as the "upper line" (wrong) yet mapped it correctly, because the label sat at the outlet and the line ended at the nearest cylinder. A routing trap only works if the labelled end and the far end are not the nearest pair |
| 2026-10 | hydraulic v4 | **Sequential chains get solved.** Five reads in a chain, each with local evidence, were all made correctly. Prefer simultaneous systems (rope-length sets, Willis cycles, nodal networks) |
| 2026-10 | playbook | **They take prompt wording at face value** (a model assumed "pilot above tank" without tracing where the pilot starts) |
| 2026-10 | playbook | **They compare dimensions against pixel scale**, so draw to scale |
