# Pulley v1: test result (tested with the 0.8 m/s version, GTFA −229)

Both blocks were **correct (−229)**, so the task fails Pass@4.

| Block | Answer | Reading |
|---|---|---|
| 1 | −229 | All four ropes traced correctly; "elevated pulley on bar A" recognised; drum sides and grooves correct |
| 2 | −229 | Same reading, with rope equations written as average-velocity relations at each pulley |

## Why it was solved
1. **Each rope is one continuous, unbranched line.** Tracing rope by rope maps one-to-one onto the drawing, and the models' standard rope-length method is exactly that.
2. **Distinct line styles leak the topology.** The thick strap made PF's carrier obvious; a unique line style works like a label.
3. **Ropes 3 and 4 linked only two bodies each**, so the "4×4 system" collapsed into a substitution chain (v_A = 2v_C, v_B = −v_C/2).
4. **The prompt rule "fastened only at dots" made non-fastened crossings trivial to read.**

## Rule for the next design
Use local ambiguities that need a default to resolve (a datum, a pivot vs a nearby pin, a pilot dot on a tank line, a hop followed by a dot, the active envelope), not long but clean traces. Avoid unique line styles for the decisive element.
