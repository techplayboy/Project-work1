# Lever v1: test result

**Both blocks failed: 184 and 184 (GTFA 321).** Both reproduce exactly from the stated reading:
v_L = 550 × 600000 / (300 × 1600π + 250 × 367.25π) = 330000000 / (571812.5π) = 183.701 → 184,
which is misread 4 (pilot read as taken from line B, so no regeneration).

| Block | Answer | Reads right | Read wrong |
|---|---|---|---|
| 1 | 184 | Pivot at 450 (spring pin ignored); arms 300/250/550 from the left-end datum; Y1 → crossed envelope (P→B, A→T); Y fed at its rod end | "The rod end of the left cylinder discharges to the reservoir through the pilot-operated check valve (piloted open by the pressure line from Port B)" |
| 2 | 184 | Same | "The rod end of Cylinder 1 connects to a pilot-operated counterbalance check valve that is piloted open by the pressure in the line from port B, discharging fluid directly to the reservoir (tank)" |

## What worked / did not
- **Worked (both models):** the pilot line whose only dot is on the drain line, 0.35 above the supply line. Both assumed the textbook default "pilot taken from the pressure line" and never traced where the dashed line starts. Neither checked the hop-then-dot regeneration path.
- **Did not work:** the spring pin beside the pivot, the baseline datum, the active envelope, and Y's rod-end port were all read correctly.

Chosen for Step 8: Response 1 (clear quote, pure topology misread, not convention-dependent).
