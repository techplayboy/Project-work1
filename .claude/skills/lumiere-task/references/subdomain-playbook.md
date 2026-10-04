# Subdomain playbook

Method everywhere: (1) find the structure to misread, (2) list the textbook defaults,
(3) contradict them where the drawing is dense, (4) couple everything so nothing is solvable alone.

Before drawing in any subdomain, write its row in this format with **≥6 candidate reads**:

```
Subdomain:
Image type:
Reads (≥6):  # | read | textbook default | what we draw instead | misread answer
Coupling idea:
Requested quantity (one):
Counter-intuitive feature:
Self-check routes to close:
```

| Subdomain | Good image types | Defaults to attack / traps | Coupling idea |
|---|---|---|---|
| **Mech: power transmission** | Kinematic sections of gear trains, planetary sets with clutches/brakes | Common sun shaft; brake on the sun; carrier output; separate pins vs stepped planet; nested drums and sleeves | ≥3 planetary sets linked so the Willis equations must be solved together *(proven: gearbox v3)* |
| **Mech: fluid power** | ISO 1219 hydraulic/pneumatic circuits | Hop vs junction dot; pilot line from an unexpected line; active valve envelope; rod on the non-standard side; check-valve direction | Series cylinders + regeneration + pilot-operated checks *(proven: hydraulic v3)* |
| **Mech: mechanisms** | Linkages, slider-cranks, cam layouts | Which pivot is grounded; which link carries which angle; coupler vs rocker | Multi-loop linkage where the output needs every loop |
| **Mech: machine elements** | Bolt groups, welded brackets, shafts with features | Load offset from an edge datum, not the centroid; which bolts/features carry load | Eccentric load + non-uniform pattern + edge datum |
| **Civil / structural** | Trusses, frames, beams with supports and hinges | Pinned vs roller vs fixed symbols; internal hinge; members crossing without a joint; load on joint vs member | Determinate frame with an internal hinge where the reaction needs the whole structure |
| **Electrical: circuits** | Resistor networks, op-amp stages, transistor biasing | Crossing wires without a dot; ground node; terminal identity; rotated bridge; diode/polarity orientation | Bridge or multi-loop network solvable only by nodal analysis of the whole circuit |
| **Electrical: power systems** | Single-line diagrams, transformer connections | Breaker states; Δ/Y orientation; which bus a feeder lands on | Ring/meshed network with switch states given in the prompt |
| **Electronics / digital logic** | Gate-level schematics, flip-flop chains, MUX trees | Bubble on input vs output; crossing vs joined wires; clock edge; MSB/LSB order; feedback from Q vs Q̄ | Sequential circuit whose state after N clocks needs every gate |
| **Control systems** | Block diagrams, signal-flow graphs | Summing-junction sign; pickoff before vs after a block; feedback skipping a block; forward path drawn right-to-left | Nested loops where Mason's rule needs every loop and touching relation |
| **Chemical / process** | PFDs and P&IDs with recycle and bypass | Recycle return point; bypass around a unit; which stream a splitter feeds; valve open/closed | Recycle + purge + bypass so the mass balance needs every stream |
| **Thermal / energy** | Rankine/refrigeration/heat-pump cycles, HX networks | Component order on hot/cold side; which state at which inlet; regenerator cross-connections | Cycle with regeneration and a split so states can't be read in sequence |
| **Aerospace / dynamics** | FBDs, multi-body, mass–spring–damper networks | Which body a spring/damper attaches to; force direction; series vs parallel springs drawn ambiguously | Coupled multi-DOF system where an eigenvalue/response needs every element |
| **CS: graphs and algorithms** | Directed/weighted graphs, flow networks, state machines | Arrowhead at the far end; edges crossing without a node; weight label near a different edge; self-loops; parallel edges | Shortest path / max-flow where the optimum uses an edge that crossing or label placement makes easy to miss |
| **CS: data structures** | Trees, heaps, linked structures, hash tables | Left vs right child; crossing pointer targets; null vs link to a distant node | Traversal or operation sequence whose result depends on every pointer |
| **CS: architecture / systems** | Datapaths, pipelines, memory hierarchies, network topologies | MUX select lines; forwarding paths; which bus a component sits on; crossing buses | Instruction trace or routing outcome that needs every path |
| **Data / plots (any)** | Multi-panel plots, dual axes, log scales | Left vs right axis; legend mapping; log vs linear; panel scale carried over; tick reading | Value combining reads from two panels with different scales |

## Proven designs (summaries)

### Gearbox v3 — three coupled planetary sets (GTFA −926, both models failed: 1180, 1340)
Six reads against defaults: sun not on the common shaft, brake not on the sun, output not from the
carrier, double planet (two pins) vs stepped, nested drums ending next to decoys, clutch halves
landing on unexpected members. Willis equations of all three sets must be solved together.

### Gearbox v2 — two coupled sets (GTFA 1980 rpm; one model failed)
Shaft A 1450 rpm → K1 → R1 drum (z80, m2.5); K2 (released) → sun shaft (S1 z28 m2.5, S2 z52 m2) →
F1 (released). PG1 single planet z26 on C1; C1 drum runs over PG2, fixed to R2 (z92 m2) → output D.
PG2 double planet (z10 inner, z10 outer, separate pins) on C2 → F2 (engaged).
(n_S − n_C1)/(n_R1 − n_C1) = −80/28; n_S/n_R2 = +92/52 (C2 = 0); n_C1 = n_R2 = n_D →
n_D = 1984.21 → 1980 (overdrive). Distractors: 736 (double read as single), 820 (K1→sun),
1070 (F2 grounds sun), 1450 (direct drive), 3510 (sun shaft as output).

### Hydraulic series circuit (handover reference script in `references/source/HANDOVER_v1.md` §11)
Rod side of cyl 4 → cap side of cyl 5; bypass cap4→cap5 through a check valve oriented to block.
Bore 100/rod 70, bore 80, pump 30 L/min → v₂ = 50.7 mm/s. Distractors 99.5, 63.7, 74.2, 150, 195.
v3 added a pilot-operated check with the pilot from an unexpected riser and all rods on the left.
