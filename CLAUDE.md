# Project-work1 — Project Lumière task authoring

This repo holds adversarial image + text evaluation tasks for vision-language models
(Engineering and CS subdomains). **For any task design, drawing, packaging, model-response
analysis or QC Justification work, use the `lumiere-task` skill** in
`.claude/skills/lumiere-task/` — it holds the rules, templates and checking scripts.

- One folder per task: `tasks/<task_name>/` with `draw_<task>.py`, `verify.py`, the PNG,
  `TASK_PACKAGE.md`, and `responses/` for pasted model outputs.
- Python deps: `pip install matplotlib numpy pillow`.
- Before handover: `python3 .claude/skills/lumiere-task/scripts/check_package.py tasks/<t>/TASK_PACKAGE.md --image tasks/<t>/<img>.png`
  and look at the rendered PNG.
- After every test result, append a row to `.claude/skills/lumiere-task/references/attempt-log.md`.
