#!/usr/bin/env python3
"""
check_package.py — lint a Lumière TASK_PACKAGE.md (and optionally the image) against the
platform field rules before handover.

Sections are found by headings "## Step <n> ..." and the FIRST fenced code block under each
is taken as the paste-ready field (layout of templates/TASK_PACKAGE.md).

    python3 .claude/skills/lumiere-task/scripts/check_package.py tasks/x/TASK_PACKAGE.md --image tasks/x/x.png

Exit code 1 if any ERROR.
"""
import argparse
import re
import sys
from pathlib import Path

BOILER_RE = re.compile(
    r"The answer should be expressed in \$\\text\{[^}]+\}\$\. Report your final answer as a "
    r"\$(\d)\$ significant figure number without units\. Any intermediate calculations should be "
    r"carried out to \$6\$ significant figures\. All unstated fundamental constants should be used "
    r"to \$4\$ significant figures\.\s*$"
)
DISTRACTOR_NOTE = ("Distractors (incorrect answers only). Note that in testing we provided the "
                   "model all potential answers, including the GTFA.")
DESC_CLOSE = "The task prompt, not the image, specifies the conditions"

META_REFS = [r"in the image", r"provided image", r"as per image", r"image\s*\$?\d", r"attached image",
             r"the image (?:above|below|attached)", r"in the (?:attached|provided) figure"]
CONNECTION_WORDS = [r"in series", r"in parallel", r"common shaft", r"bypass", r"regenerat",
                    r"feedback from", r"connected to", r"\bfeeds\b", r"joined to", r"is fixed to",
                    r"meshes with", r"recycle(?:d)? to", r"tied to"]
BAD_UNICODE = "×−–°µ±≤≥·÷√πΩ"


def sections(md):
    """Map step number -> (section text, first fenced block or None)."""
    out = {}
    heads = list(re.finditer(r"^##\s+Step\s+(\d+)\b.*$", md, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(md)
        nxt = re.search(r"^##\s+(?!#)", md[h.end():end], re.M)
        body = md[h.end(): h.end() + nxt.start()] if nxt else md[h.end():end]
        m = re.search(r"^```[^\n]*\n(.*?)^```", body, re.S | re.M)
        out.setdefault(int(h.group(1)), (body, m.group(1).rstrip("\n") if m else None))
    return out


def num(s):
    s = s.strip().replace("$", "").replace(",", "").replace("−", "-")
    try:
        return float(s)
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package")
    ap.add_argument("--image", action="append", default=[])
    a = ap.parse_args()

    md = Path(a.package).read_text()
    S = sections(md)
    msgs = []
    E = lambda s: msgs.append("ERROR " + s)
    W = lambda s: msgs.append("WARN  " + s)

    def field(n, name):
        if n not in S or S[n][1] is None:
            E(f"Step {n} ({name}): no fenced code block found")
            return None
        t = S[n][1]
        if re.search(r"<[A-Za-z≥][^>\n]{0,80}>", t):
            W(f"Step {n} ({name}): unfilled <placeholder> remains")
        return t

    # ---- Step 3
    s3 = field(3, "source/licence")
    if s3 and "Original — internal lab image" not in s3 and "CC BY" not in s3 and "CC0" not in s3:
        E("Step 3: neither 'Original — internal lab image' nor a CC BY/CC0 licence")
    if s3 and re.search(r"\bNC\b|\bND\b|BioRender|All Rights Reserved|patent", s3, re.I):
        E("Step 3: prohibited licence/source")

    # ---- Step 4
    p = field(4, "prompt")
    sig = None
    if p:
        n = len(p)
        msgs.append(f"{'ERROR' if n > 2000 else 'INFO '} Step 4: prompt length {n}/2000")
        for r in META_REFS:
            if re.search(r, p, re.I):
                E(f"Step 4: meta-reference /{r}/ (NON_FOUNDATIONAL_REFERENCE)")
        for r in CONNECTION_WORDS:
            if re.search(r, p, re.I):
                W(f"Step 4: connection word /{r}/ — prompt must give conditions, not topology")
        bad = sorted({c for c in p if c in BAD_UNICODE})
        if bad:
            E(f"Step 4: Unicode math characters {bad} — use LaTeX")
        if "`" in p:
            E("Step 4: backtick inline code")
        if p.count("$") % 2:
            E("Step 4: odd number of $ — unbalanced LaTeX")
        m = BOILER_RE.search(p)
        if not m:
            E("Step 4: does not end with the exact boilerplate")
        else:
            sig = int(m.group(1))
            if sig > 3 or sig < 1:
                E(f"Step 4: significant figures {sig} (must be 1–3)")
        body = BOILER_RE.sub("", p)
        bare = [t for t in re.findall(r"(?<![\w$\\{.])\d+(?:\.\d+)?(?![\w}$])",
                                      re.sub(r"\$[^$]*\$", "", body))]
        if bare:
            W(f"Step 4: numbers outside LaTeX: {bare[:8]}")
        if re.search(r"\b(?:the|a|an)\s+Dijkstra'?s\b", p):
            W("Step 4: 'the Dijkstra's algorithm' — write 'perform Dijkstra's algorithm'")
        if len(re.findall(r"\b(?:Determine|Find|Calculate|Compute|What is)\b", p)) > 1:
            W("Step 4: more than one question verb — exactly one requested quantity")
        if not re.search(r"\bConsider the\b", p):
            W("Step 4: does not use 'Consider the ... shown' framing")

    # ---- Step 6
    g = field(6, "GTFA")
    gval = None
    if g:
        g = g.strip()
        if "\n" in g or len(g.split()) > 8 or g.endswith("."):
            E("Step 6: GTFA must be a bare number or short exact answer, not a sentence")
        gval = num(g)
        if gval is not None and sig:
            digits = re.sub(r"[^0-9]", "", g.lstrip("-")).lstrip("0")
            if "." in g and len(digits) != sig:
                W(f"Step 6: GTFA '{g}' shows {len(digits)} s.f., prompt asks {sig}")
            elif "." not in g and len(digits.rstrip("0")) > sig:
                E(f"Step 6: GTFA '{g}' has more than {sig} significant figures")

    # ---- Step 7
    d = field(7, "description")
    if d:
        wc = len(re.findall(r"\S+", d))
        msgs.append(f"{'ERROR' if wc < 200 else 'INFO '} Step 7: description {wc} words (≥200)")
        if DESC_CLOSE in d or re.search(r"\btask prompt\b|\bthe prompt\b", d, re.I):
            E("Step 7: description refers to the prompt (Image Description Checker: META_COMMENTARY); "
              "describe only the figure")
        if re.search(r"\btrap\b|\bmisread|\bdistractor|\btrick", d, re.I):
            E("Step 7: description points out the trap")

    # ---- Step 9
    s = field(9, "solution")
    if s:
        if not re.search(r"^Step 1:", s, re.M):
            E("Step 9: no 'Step 1:'")
        steps = [int(x) for x in re.findall(r"^Step (\d+):", s, re.M)]
        if steps != list(range(1, len(steps) + 1)):
            E(f"Step 9: step numbering not consecutive {steps}")
        last = [l for l in s.splitlines() if l.strip()][-1].strip()
        if not last.startswith("Final Answer:"):
            E("Step 9: last line must be 'Final Answer: <GTFA>'")
        elif g and last != f"Final Answer: {g}":
            E(f"Step 9: '{last}' does not match GTFA '{g}'")

    # ---- Step 10
    dt = field(10, "distractors")
    if dt:
        if DISTRACTOR_NOTE not in dt:
            E("Step 10: required note missing or altered")
        items = [re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", l).strip()
                 for l in dt.replace(DISTRACTOR_NOTE, "").splitlines() if l.strip()]
        if len(items) != 5:
            E(f"Step 10: {len(items)} distractors (need exactly 5)")
        if len(set(items)) != len(items):
            E("Step 10: duplicate distractors")
        if g and g in items:
            E("Step 10: a distractor equals the GTFA")
        if gval:
            for it in items:
                v = num(it.split()[0]) if it else None
                if v is not None and abs(v - gval) / abs(gval) < 0.25:
                    W(f"Step 10: distractor {it} is within 25% of GTFA {g}")
        # Distractor Format Checker (FORMAT_MISMATCH): decimals vs whole-number GTFA, and vice versa
        if g is not None:
            g_whole = "." not in g
            vals = []
            for it in items:
                tok = it.split()[0] if it else ""
                if num(tok) is None:
                    continue
                vals.append(num(tok))
                if ("." not in tok) != g_whole:
                    E(f"Step 10: distractor {tok} format ({'decimal' if '.' in tok else 'whole'}) "
                      f"does not match GTFA {g} ({'whole' if g_whole else 'decimal'}) -> FORMAT_MISMATCH")
            for i in range(len(vals)):
                for j in range(i + 1, len(vals)):
                    va, vb = vals[i], vals[j]
                    if max(abs(va), abs(vb)) and abs(va - vb) / max(abs(va), abs(vb)) < 0.10:
                        W(f"Step 10: distractors {va:g} and {vb:g} are within 10% of each other")

    # ---- Step 8 (optional, may be templates)
    if 8 in S and re.search(r"Response \$\d", S[8][0]):
        E("Step 8: write 'Response 1', not 'Response $1$'")

    # ---- images
    if a.image:
        sys.path.insert(0, str(Path(__file__).parent))
        from drawkit import check_png
        if len(a.image) > 5:
            E("more than 5 images")
        for im in a.image:
            r = check_png(im)
            msgs += [f"{x.split()[0]:5} image {im}: {' '.join(x.split()[1:])}" for x in r]
            if not r:
                msgs.append(f"INFO  image {im}: RGB, white background — still inspect it visually")

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    msgs.sort(key=lambda m: order[m.split()[0]])
    print("\n".join(msgs) or "no findings")
    errs = sum(m.startswith("ERROR") for m in msgs)
    print(f"\n{errs} error(s), {sum(m.startswith('WARN') for m in msgs)} warning(s)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
