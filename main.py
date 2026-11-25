# One Line, Big Laugh — make.fun bounty
# u-coral-404-one-line-big-laugh-328fb857
#
# This program writes exactly one funny line to /output/entry.txt:
# a single line, 1-200 characters, no trailing newline. The gate
# counts characters, so the program validates the text against the
# gate before writing it.
#
# Line draft history (revision notes, kept so the choice is auditable):
#   * v1 smart-fridge intervention (task's example): a decent setup,
#     but the punchline sprawls over three clauses and the fridge
#     talking is a familiar smart-home gag.
#   * v2 smart speaker / meaning of life / ad for therapy: sharp
#     twist, but the joke leans on the reader knowing voice
#     assistants serve ads; the payoff is a shrug, not an image.
#   * v3 (final) dog / treat jar / locks / rent in bacon: wins.
#     Setup is one domestic image everyone knows (dog vs treat jar),
#     then it escalates twice — the dog changes the locks, then
#     charges rent — and the final detail (payable in bacon) is the
#     surprise that sticks in the head. Every word earns its place;
#     "figured out" beats "learned to open" because the dog is the
#     schemer, not the student.
#
# Python 3.13, stdlib only, no network, no local imports.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py

import os
from pathlib import Path

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The line: one sentence, setup then two escalating turns.
LINE = "My dog figured out the treat jar, changed the locks, and now charges me rent in bacon."

# The gate: UTF-8 text, 1 to 200 characters, not only whitespace,
# a single line. Refuse to write anything that fails it.
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"line is {len(LINE)} characters, gate needs 1-200")
if not LINE.strip() or "\n" in LINE or "\r" in LINE:
    raise SystemExit("line must be one non-blank line")

Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")

print(f"wrote entry.txt ({len(LINE)} characters): {LINE}")
