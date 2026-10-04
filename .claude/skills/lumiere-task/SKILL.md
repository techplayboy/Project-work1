---
name: lumiere-task
description: Author, verify and package Project Lumière adversarial image+text evaluation tasks for vision-language models in any Engineering or Computer Science subdomain (gear trains, hydraulics, circuits, logic, control, process, structures, graphs, data structures, plots). Use when asked to design or build a new Lumière task, draw a task image with matplotlib, write the prompt / GTFA / image description / step-by-step solution / distractors, analyse checker-model responses, write a Step 8 model-failure justification, make a harder version after models solved a task, or answer a Science Judge / Image Description Checker finding with a QC Justification.
---

# Project Lumière: task authoring

You build image + text tasks that frontier VLMs **misread**. Each task pairs a self-drawn
image with a prompt that has **exactly one verifiable answer**, reachable only by reading
the image correctly. Difficulty bar is **Pass@4**: if any of four attempts is right, the
task fails. One trap is never enough; design for **≥6 independent reads**.

Reference files (load when the step needs them):

| File | Load when |
|---|---|
| `references/field-rules.md` | Writing any platform field (Steps 3–10), LaTeX, boilerplate |
| `references/model-behaviour.md` | Designing traps; analysing model responses |
| `references/subdomain-playbook.md` | Starting a task in any subdomain |
| `references/qc-templates.md` | Step 8 text, QC Justifications, licence fields |
| `references/attempt-log.md` | Before designing: what beat / failed to beat the models. Append new results here |
| `templates/TASK_PACKAGE.md` | Skeleton for the deliverable |
| `templates/verify_template.py` | Skeleton for `verify.py` |
| `scripts/drawkit.py` | Drawing primitives (hop, junction dot, ground hatch, arrows, save-as-RGB) |
| `scripts/misreads.py` | Misread table: distance from GTFA, sign, plausibility, uniqueness, solvability |
| `scripts/check_package.py` | Lint a finished `TASK_PACKAGE.md` (+ image) before handover |
| `references/source/` | Original briefings, verbatim. `BRIEFING_v3` supersedes the others where they conflict (Pass@4 not Pass@2; coupled multi-step maths is fine) |

## Non-negotiables (memorise)

1. **Valid failures are misreads of the image** — topology/connectivity (best), spatial/geometric,
   axis/panel/legend, scale, miscount, signal-vs-artifact. Reasoning errors, OCR slips and
   post-2025 knowledge gaps do **not** count.
2. **Every misread gives a positive, plausible answer** that still leaves a uniquely solvable
   problem, and sits **≥25% from the GTFA** (or a different discrete answer). An absurd or
   unsolvable misread makes the model re-read and self-correct.
3. **Couple everything.** If the problem decomposes (stage by stage, branch by branch), the models
   solve it. Coupled computation is safe: their maths rarely fails, their reading does.
4. **Attack textbook defaults in the densest region.** Models fill gaps with defaults and state
   them as fact. Write down the default for each read, then draw the opposite.
5. **Prompt gives conditions, never connections.** No "in series", "common shaft", "bypass",
   "regenerative", "feedback from Q̄", "connected to".
6. **Close self-check routes**: no number coincidences that reveal pairings, withhold states that
   allow a balance check. Prefer counter-intuitive answers (overdrive, reversal, non-greedy path).
7. **Defensible**: every connection unambiguous to a careful expert (dot vs hop, separate pins,
   arrowheads, datums). Self-made images only (recall risk with public figures).
8. **Prompt** ≤2000 chars, all numbers in LaTeX, never "in the image"/"provided image"/"Image 1",
   ends with the exact boilerplate (see `field-rules.md`).

## Workflow A — new task

1. **Playbook row first.** Read `subdomain-playbook.md` and `attempt-log.md`. Write the subdomain
   row: image type, ≥6 candidate reads, the textbook default each one attacks, the coupling idea.
2. **Design the structure and numbers.** For every read, compute the misread answer *before
   drawing*. Iterate the data until every misread is positive, plausible, solvable, ≥25% away,
   and no two misreads collide. Use `scripts/misreads.py` (copy `templates/verify_template.py`
   into the task folder as `verify.py`). Verify the GTFA by an independent method (e.g. a
   linear solve, plus a closed form).
3. **Draw** `draw_<task>.py` using `scripts/drawkit.py`. The docstring encodes the full
   structure (topology, states, values). Route connections long and nested, ending next to
   decoys; label only what the prompt refers to; put input values in the image.
4. **Render and inspect the PNG** with the Read tool (look at it — do not trust the code):
   label collisions, clipping, white patches hiding lines, every dot/hop where intended, every
   number legible. Fix and re-render until clean.
5. **Write `TASK_PACKAGE.md`** from `templates/TASK_PACKAGE.md`: author trap table, Steps 3, 4,
   6, 7, 9, 10 paste-ready in code blocks, Step 8 templates per likely misread, QC Justifications.
6. **Lint**: `python3 .claude/skills/lumiere-task/scripts/check_package.py tasks/<task>/TASK_PACKAGE.md --image tasks/<task>/<image>.png`.
   Fix every ERROR; consider every WARN.
7. Hand over: image, prompt, GTFA, trap table summary. Commit the task folder.

Lay out each task as `tasks/<task_name>/` containing `draw_<task>.py`, `verify.py`,
`<image>.png`, `TASK_PACKAGE.md`, and later `responses/` with pasted model outputs.

## Workflow B — model responses come back

1. Extract each response's final answer (note blanks/timeouts — never usable for Step 8).
2. For each wrong answer, identify the stated reading (quote it) and **reproduce the number
   exactly** from that reading in `verify.py`. Exact reproduction ⇒ pure misread ⇒ valid.
   If it doesn't reproduce, look for a reasoning error and avoid that response.
3. Recommend which response to justify (clearest quotable image misread) and why.
4. Write Step 8 with the skeleton in `qc-templates.md`; pick the error type
   (usually *Connectivity / topology error*).
5. Swap the real wrong answers into the distractors (keep 5, unique, ≠ GTFA).
6. Append a row to `references/attempt-log.md` (task, GTFA, result, lesson) and, if a new
   default or behaviour was observed, add it to `model-behaviour.md`.

If the models **solved it**: say so plainly, list which reads they got right and which default
or shortcut let them, then design a harder version (more coupling, more reads against the
defaults they relied on, close the self-check route they used).

## Workflow C — platform findings

- *Science Judge AMBIGUOUS_PROMPT / UNSTATED_ASSUMPTION* ("no task or requested quantity", or
  quoting the attestation checkbox): first ask the user to reload and confirm the Step 4 field holds
  the full prompt; if it does, use the QC Justification in `qc-templates.md`. No task change.
- *Image Description Checker HALLUCINATED_DETAIL*: re-check the drawing first. If the checker is
  wrong, keep image and answer; add geometric evidence to the description and rebut point by
  point (what is drawn with numbers, why the checker's reading is impossible, any misquote).

## Pre-handover checklist

- [ ] Playbook row with ≥6 independent reads, each against a default; nothing solvable alone
- [ ] Every misread computed: positive/plausible, uniquely solvable, ≥25% from GTFA
- [ ] GTFA verified two ways in code
- [ ] PNG rendered, white RGB background, inspected; no collisions; only needed labels
- [ ] Prompt ≤2000 chars, conditions only, one quantity, convention + tie-break, LaTeX, boilerplate
- [ ] Description ≥200 words, geometric evidence, closing "The task prompt, not the image, ..." paragraph
- [ ] Solution: Step 1 data, Steps 2–3 observation, principle, 6-s.f. intermediates, `Final Answer: <GTFA>`
- [ ] 5 distractors with the exact note; QC Justifications ready
- [ ] `check_package.py` passes with no ERROR
