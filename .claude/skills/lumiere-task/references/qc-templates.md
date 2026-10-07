# Reusable text templates

## Step 8 — model failure justification

Error type: **Connectivity / topology error** (or the spatial / axis / counting category that
matches the misread).

```
The response fails by misreading <what> (<topological / spatial / axis> confusion). Its <correct parts> are correct. However, it states "<quote>", so <wrong equation or step with numbers> = <wrong answer>. In the drawing, <what is actually drawn, with the evidence>. With this reading, <correct equation> = <GTFA>. The misread gives <wrong> instead of the correct <GTFA>.
```

Rules: quote the model's own wrong statement and its wrong equation/step; reproduce its number
from that reading first; write "Response 1", not "Response $1$"; never pick a blank or a
reasoning error.

Display-equation variant:
```
The response fails by misreading the connections in the layout (topological confusion). Its <list what it got right> are correct, but it assigns <quantity> to <wrong reading>:

$$<the model's wrong equation with numbers>$$

In the layout, <what the drawing actually shows>. The correct <quantity> is therefore <correct equation> = <value>. The misread gives <wrong answer> instead of the correct <GTFA>.
```

## QC Justification — Science Judge AMBIGUOUS_PROMPT / UNSTATED_ASSUMPTION

Cause: the judge evaluates the attestation checkbox text or an empty prompt view, not the saved
prompt; it often re-fires after a later step is saved. **First** reload and confirm the Step 4
field holds the full prompt (re-paste if not). If it does:

```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that the prompt contains no task or requested quantity [or: quotes the author attestation ("My prompt is self-contained..."), which is not part of the prompt]. The saved prompt defines the system: "<quote first sentence>". It states the conditions verbatim: "<quote conditions>". It names exactly one requested quantity: "<quote question + convention + units + sig figs>".

With these conditions the answer is uniquely determined (<GTFA>), as shown in the step-by-step solution. The image description's final paragraph restates the conditions and requested quantity, and Step 1 of the solution attributes them to the prompt.

The finding is an artefact of the prompt text not being evaluated, not an omission in the task.
```

Two-finding variant:
```
Both Science Judge findings are incorrect and require no change to the task.

Finding 1 quotes the author attestation statement ("My prompt is self-contained..."), which is not part of the prompt. The prompt asks a specific engineering question and names one quantity: "<quote the question verbatim>", reported as <units> to <n> significant figures.

Finding 2 states the idealizations are absent. The prompt states them verbatim: "<quote the assumptions sentence verbatim>".

The image description's final paragraph also restates these conditions and the requested quantity, and Step 1 of the golden solution attributes them to the prompt.

Both findings are artefacts of the prompt text not being evaluated, and not omissions in the task.
```

## QC Justification — Science Judge SPECIFICITY_MISSING (units / precision)

Seen on hydraulic v4: "neither final-answer units nor significant-figure precision is
specified", with "Quote: N/A". Same root cause as above (the judge does not see the full
prompt, usually the closing boilerplate paragraph). Reload and confirm the Step 4 field ends
with the boilerplate; then:

```
The Science Judge finding is incorrect and requires no change to the task.

The finding states that neither final-answer units nor significant-figure precision is specified, and it quotes nothing from the prompt ("Quote: N/A"). The saved prompt states both, twice. The question sentence reads: "<question sentence with units and sig figs>". The prompt then closes with the required boilerplate: "The answer should be expressed in <units>. Report your final answer as a <N> significant figure number without units. Any intermediate calculations should be carried out to 6 significant figures. All unstated fundamental constants should be used to 4 significant figures."

The units (<units>), the final precision (<N> significant figures) and the intermediate precision (6 significant figures) are therefore all specified. The image description's final paragraph restates them, and the GTFA (<GTFA>) is given to <N> significant figures.

The finding is an artefact of the prompt text not being fully evaluated, not an omission in the task.
```

## QC Justification — Image Description Checker HALLUCINATED_DETAIL

Check the drawing first. If the checker is wrong, change neither image nor answer; strengthen the
description with geometric evidence, then:

```
The Image Description Checker finding is incorrect; the description matches the figure and no change to the image or answer is required.

The finding claims "<quote finding>". The figure shows <what is drawn, with numbers: radii, pin positions, dots vs hops, arrowhead ends, which side a line enters>. <Why the checker's reading is physically/logically impossible: e.g. a stepped planet would need one pin through both gear centres, but the two gears have centres at different radii (<r1> mm and <r2> mm) with a separate pin through each.> <Any misquote: the description says "<actual text>", not "<quoted text>".>

The description has been made more explicit on this point; the topology, values and GTFA (<GTFA>) are unchanged.
```

## Description closing paragraph: RETIRED

Do not end the description with "The task prompt, not the image, specifies the conditions…". The Image
Description Checker flags it as META_COMMENTARY (MAJOR ERROR, lever v1). Describe the figure only, including
the resolved state of switched elements, and handle Science Judge findings with the QC Justification above.

## Licence fields

Self-made:
```
Image source:   Original — internal lab image
License type:   N/A
Reference:      N/A
```

External CC BY (discouraged — recall risk):
```
Image source:   External — open-access (CC BY)
License type:   CC BY 4.0
License link:   https://creativecommons.org/licenses/by/4.0/
Article DOI:    https://doi.org/<doi>
Published in:   <Journal> (<Publisher>), Vol. <v>, Issue <i>, Article <n>, <year>
```
