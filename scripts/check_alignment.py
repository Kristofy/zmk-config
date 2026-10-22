"""Check box-drawing diagrams for alignment.

Usage: python3 scripts/check_alignment.py README.md config/corne.keymap

For every block of lines that contains box-drawing characters:
  - each vertical bar in a content line must sit on a junction of the
    border line above or below it
  - in keymap binding grids (code lines between comment borders), every
    binding must start right after a cell boundary and end before the next
Columns are measured in display width; East Asian "ambiguous" characters
(arrows, ▽, ·, box lines) are reported because some fonts draw them 2 wide.
"""
import re, sys, unicodedata

JUNCTIONS = set("┬┼┤├╮╭╯╰┴│")
BOX = set("─│┬┼┤├╮╭╯╰┴")

def width(ch):
    return 2 if unicodedata.east_asian_width(ch) in "WF" else 1

def cols(line, chars):
    out, x = [], 0
    for ch in line:
        if ch in chars:
            out.append(x)
        x += width(ch)
    return out

def is_border(line):
    return "─" in line

def check_file(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    problems = []
    ambiguous = set()
    i = 0
    while i < len(lines):
        if not any(c in BOX for c in lines[i]):
            i += 1
            continue
        # a block: consecutive lines that are box lines or keymap code lines between them
        start = i
        while i < len(lines) and (any(c in BOX for c in lines[i]) or
               (lines[i].strip().startswith("&") or lines[i].strip().startswith("___") or lines[i].strip().startswith("XXX"))):
            i += 1
        block = list(range(start, i))
        for n in block:
            for ch in lines[n]:
                if ch not in BOX and unicodedata.east_asian_width(ch) == "A":
                    ambiguous.add(ch)
        borders = [n for n in block if is_border(lines[n])]
        for n in block:
            line = lines[n]
            if is_border(line):
                continue
            above = [b for b in borders if b < n][-1:]
            below = [b for b in borders if b > n][:1]
            sets = [set(cols(lines[b], JUNCTIONS)) for b in above + below]
            # a column counts only if every adjacent border has a junction there
            allowed = set.intersection(*sets) if sets else set()
            if "│" in line:
                bad = [c for c in cols(line, "│") if c not in allowed]
                if bad:
                    problems.append((n + 1, f"bar at column(s) {bad} not on a border junction", line))
            elif line.strip() and not line.lstrip().startswith("//"):
                # keymap code line: bindings must start 2 columns after a junction
                ref = sorted(allowed)
                starts = [m.start() for m in re.finditer(r"(?<![\w(])(?:&|___|XXX)", line)]
                for s in starts:
                    if s - 2 not in allowed:
                        problems.append((n + 1, f"binding at column {s} does not start 2 after a junction", line))
                for m in re.finditer(r"\S+(?: \S+)*", line):
                    nxt = [r for r in ref if r > m.start()]
                    if nxt and m.end() > nxt[0]:
                        problems.append((n + 1, f"'{m.group()}' runs past the cell border at column {nxt[0]}", line))
    return problems, ambiguous

ok = True
for path in sys.argv[1:]:
    problems, ambiguous = check_file(path)
    print(f"== {path}: {len(problems)} problem(s)")
    for ln, msg, line in problems:
        ok = False
        print(f"  line {ln}: {msg}\n    {line}")
    if ambiguous:
        print("  ambiguous-width characters (may render 2 wide in some fonts):", " ".join(sorted(ambiguous)))
sys.exit(0 if ok else 1)
