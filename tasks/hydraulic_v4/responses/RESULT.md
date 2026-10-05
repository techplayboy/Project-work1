# Hydraulic v4: test result

Both checker models were **correct (114)**, so the task fails Pass@4.

| Block | Final answer | Reads made |
|---|---|---|
| 1 | 114 | Y1 on the right gives the crossed envelope; FCV bleeds 8 L/min off B; B enters cylinder 4's cap; 60 % goes to cylinder 5; pilot taken from A, so valve 10 is closed and cylinder 5 regenerates |
| 2 | 114 | Same reads. It called the 60 % outlet the "upper line" (it is the lower one) but still sent it to cylinder 5, so it matched the label to the endpoint rather than tracing the line |

## Why it was solved
1. **The prompt handed over the rules.** The check-valve direction convention, the pilot-operated check logic, "all three cylinders are moving", and the component names and numbers were all in the prompt. Model 2 quoted our check-valve sentence verbatim.
2. **It could be solved stage by stage.** Valve 3 → FCV → cylinder 4 → divider → cylinder 5 is a chain; each stage has local, unambiguous evidence.
3. **Clean features were read correctly:** junction dots (FCV tee, pilot source), solenoid labels next to their envelopes, the rod direction, and labels printed beside the outlets.
4. **The hop trap had no effect.** The model never traced the outlet lines; it mapped the 60 % label to the nearest cylinder, which here was correct.

## Rules for the next design
- Fully coupled linear system (≥3 simultaneous constraints), with no stage solvable alone.
- No symbol conventions, component names or function hints in the prompt beyond what an expert needs.
- Labels must not sit next to the element whose topology they reveal; endpoints must not be the nearest element.
- Long paths that pass other elements and end next to decoys.
