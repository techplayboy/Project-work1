# <Task name> — task package

Subdomain: <subdomain>  ·  Image: `<image>.png`  ·  GTFA: <GTFA>  ·  Status: draft / submitted / result

---

## Author notes (NOT submitted)

### Playbook row
- Image type:
- Coupling idea (why nothing is solvable alone):
- Counter-intuitive feature:
- Self-check routes closed:

### Trap table
| # | Read | Correct reading (what is drawn) | Textbook default / misread | Misread answer | Distance |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

All values reproduced by `verify.py`.

---

## Step 2 — Subdomain
```
<subdomain>
```

## Step 3 — Source and License
```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```

## Step 4 — Prompt
```
Consider the <system> shown as <diagram type>, in which <what markings and symbols mean>. <Operating state>. <Idealisations>. <Rule closing the key ambiguity>. Determine <one quantity of one named element> in $\text{<UNITS>}$, reported to $3$ significant figures. <Sign convention; tie-break rule>.

The answer should be expressed in $\text{<UNITS>}$. Report your final answer as a $3$ significant figure number without units. Any intermediate calculations should be carried out to $6$ significant figures. All unstated fundamental constants should be used to $4$ significant figures.
```

## Step 6 — GTFA
```
<GTFA>
```

## Step 7 — Image description
```
<≥200 words. What is drawn, with geometric evidence for every connection that matters (dot vs hop, gaps, pins through centres, arrowhead ends, sides lines enter from, datums, axis assignment). State that all numerical data are in the figure.>

The task prompt, not the image, specifies the conditions: <list>. It asks for <quantity> in <units> to <N> significant figures.
```

## Step 9 — Step-by-step solution
```
Step 1: <Conditions from the prompt; data from the figure.>

Step 2: <Observation only: what the drawing shows.>

Step 3: <Observation only: remaining connections/states.>

Step 4: <Principle/algorithm and equations.>

Step 5: <Numbers, intermediates to 6 s.f.; cross-check.>

Final Answer: <GTFA>
```

## Step 10 — Distractors
```
Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA.

1. <value>
2. <value>
3. <value>
4. <value>
5. <value>
```

| Distractor | Misread |
|---|---|
| | |

## Step 8 — Model failure templates (fill from the real response)

Error type: Connectivity / topology error

### If the model makes misread #1
```
The response fails by misreading <what> (topological confusion). Its <correct parts> are correct. However, it states "<quote>", so <wrong equation with numbers> = <wrong answer>. In the drawing, <what is drawn, with evidence>. With this reading, <correct equation> = <GTFA>. The misread gives <wrong> instead of the correct <GTFA>.
```

## QC Justification — Science Judge
```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity. The saved prompt defines the system: "<quote>". It states the conditions verbatim: "<quote>". It names exactly one requested quantity: "<quote>".

With these conditions the answer is uniquely determined (<GTFA>), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

## Model responses log
| Response | Final answer | Stated reading | Reproduced? | Usable for Step 8? |
|---|---|---|---|---|
