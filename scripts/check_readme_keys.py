"""Compare the README layer diagrams with the keymap, key by key.

Usage: python3 scripts/check_readme_keys.py [README.md] [config/corne.keymap]

Each binding is turned into the label the README should show (see the tables
below). A new kind of binding raises KeyError: add its label to a table.
"""
import re, sys

readme, keymap = (sys.argv[1:3] + ["README.md", "config/corne.keymap"][len(sys.argv[1:3]):])

# keymap: bindings per layer, in position order 0..41
src = open(keymap).read().replace("___", "&trans").replace("XXX", "&none")
layers = []
for body in re.findall(r"bindings\s*=\s*<\n(.*?)>;", src, re.S):
    body = re.sub(r"//.*", "", body)
    layers.append([" ".join(b.split()) for b in re.findall(r"&\w+(?:\s+(?!&)[^\s&]+)*", body)])

# README: cells of each diagram, in the same order
text = open(readme).read()
diagrams = []
for block in re.findall(r"```\n(╭.*?)\n```", text, re.S):
    cells = []
    for line in block.split("\n"):
        if "│" in line and "─" not in line:
            cells += [c.strip() for c in line.strip().strip("│").replace("│   │", "│").split("│")]
    diagrams.append(cells)

MODS = {"LALT": "Alt", "LGUI": "GUI", "LCTRL": "Ctl", "LSHIFT": "Sft", "RSHIFT": "Sft", "RCTRL": "Ctl", "RGUI": "GUI"}
CHARS = {"SEMI": ";", "COMMA": ",", "DOT": ".", "MINUS": "-", "PLUS": "+", "SQT": "'", "DQT": '"', "EXCL": "!",
         "PRCNT": "%", "FSLH": "/", "EQUAL": "=", "LPAR": "(", "RPAR": ")", "GRAVE": "`", "BSLH": "\\",
         "TILDE": "~", "PIPE": "|", "CARET": "^", "LBKT": "[", "RBKT": "]", "DOLLAR": "$", "LT": "<", "GT": ">",
         "HASH": "#", "AMPS": "&", "AT": "@", "LBRC": "{", "RBRC": "}", "STAR": "*",
         "A_ACUTE": "á", "E_ACUTE": "é", "I_ACUTE": "í", "O_ACUTE": "ó", "U_ACUTE": "ú",
         "O_UMLAUT": "ö", "U_UMLAUT": "ü", "O_DOUBLE_ACUTE": "ő", "U_DOUBLE_ACUTE": "ű"}
PLAIN = {"DEL": "Del", "BSPC": "Bksp", "ESC": "Esc", "RET": "Enter", "SPACE": "Space", "LGUI": "Super",
         "LALT": "Alt", "LCTRL": "Ctrl", "LSHIFT": "Shift", "LEFT": "Left", "DOWN": "Down", "UP": "Up", "RIGHT": "Right",
         "HOME": "Home", "END": "End", "PG_UP": "PgUp", "PG_DN": "PgDn", "LS(LGUI)": "GUI+Sft",
         "LC(HU_Z)": "Undo", "LC(HU_X)": "Cut", "LC(HU_C)": "Copy", "LC(HU_V)": "Paste"}
LAYERS = {"L_SYS": "SYS", "L_NUM": "NUM", "L_SYM": "SYM", "L_NAV": "NAV", "L_HUN": "HUN"}
WHOLE = {"&trans": "___", "&none": "", "&td_shift": "Shift*", "&soft_off": "Off 5s", "&sys_reset": "Reset",
         "&bootloader": "Boot", "&bt BT_CLR": "BT clr", "&bt BT_DISC": "BT dis",
         "&lt_rep L_NAV 0": "Rep/NAV", "&lt_hun L_HUN TAB": "Tab/HUN"}

def label(b):
    if b in WHOLE: return WHOLE[b]
    if m := re.fullmatch(r"&bt BT_SEL (\d)", b): return "BT " + m.group(1)
    if m := re.fullmatch(r"&mo (L_\w+)", b): return LAYERS[m.group(1)]
    if m := re.fullmatch(r"&hm[lr] (\w+) HU_(\w)", b): return m.group(2).lower() + "·" + MODS[m.group(1)]
    if m := re.fullmatch(r"&kp HU_N(\d)", b): return m.group(1)
    if m := re.fullmatch(r"&kp HU_(\w)", b): return m.group(1).lower()
    if m := re.fullmatch(r"&kp HU_(\w+)", b): return CHARS[m.group(1)]
    if m := re.fullmatch(r"&kp (F\d+)", b): return m.group(1)
    if m := re.fullmatch(r"&kp (.+)", b): return PLAIN[m.group(1)]
    raise KeyError(b)

names = ["base", "num", "sym", "nav", "sys", "hun"]
bad = 0
print(f"keymap layers: {len(layers)}, README diagrams: {len(diagrams)}")
for name, keys, cells in zip(names, layers, diagrams):
    expected = [label(b) for b in keys]
    diffs = [(i, e, c) for i, (e, c) in enumerate(zip(expected, cells)) if e != c and not (e == "Super" and c == "GUI")]  # &kp LGUI is "Super" on the thumb
    status = "OK" if len(cells) == 42 and not diffs else "MISMATCH"
    print(f"{name:5} keys={len(keys)} cells={len(cells)} {status}")
    for i, e, c in diffs:
        bad += 1
        print(f"   position {i}: keymap says {e!r}, README shows {c!r}")
sys.exit(1 if bad or len(layers) != len(diagrams) else 0)
