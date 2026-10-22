# ZMK config: Corne

Firmware for a **Corne v3** (42 keys, wireless split) with two **nice!nano v2**
controllers, built with [ZMK](https://zmk.dev) **v0.3**.

The layout is **Colemak-DH** with home row mods, built for typing English,
Hungarian and code, and for window management with the mouse in the right hand.

> [!IMPORTANT]
> The computer must use the **Hungarian** keyboard layout. The keymap sends each
> character as the key that produces it on a Hungarian layout (`HU_*` keycodes),
> so on a US layout most symbols come out wrong.

## Files

| Path | What it is |
|---|---|
| [`config/corne.keymap`](config/corne.keymap) | The keymap: layers, home row mods and the other special keys. This is the file you edit. |
| [`config/features/keys_hu.h`](config/features/keys_hu.h) | `HU_*` keycodes: which key produces which character on a Hungarian layout. Generated, don't edit. |
| [`config/corne.conf`](config/corne.conf) | Firmware options: sleep timeout, soft off. |
| [`config/west.yml`](config/west.yml) | Dependencies and their versions: ZMK and [zmk-helpers](https://github.com/urob/zmk-helpers). |
| [`build.yaml`](build.yaml) | Which firmware files the build produces: left half, right half, settings reset. |
| [`.github/workflows/build.yml`](.github/workflows/build.yml) | Builds the firmware on GitHub on every push. |
| [`scripts/`](scripts/) | Checks that the keymap grids and README diagrams line up and match the keymap. |

## Layers

`___` falls through to the layer below (as in the keymap), an empty key does nothing.
`a·Alt` is `a` on tap, Alt on hold. `Rep/NAV` is Repeat on tap, the NAV layer on hold.

### Base

Colemak-DH. `Shift*`: hold for Shift, tap for Caps Word, double tap for Caps Lock.

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│  Del  │   q   │   w   │   f   │   p   │   b   │   │   j   │   l   │   u   │   y   │   ;   │  Bksp │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  Esc  │ a·Alt │ r·GUI │ s·Ctl │ t·Sft │   g   │   │   m   │ n·Sft │ e·Ctl │ i·GUI │ o·Alt │ Enter │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│ Shift*│   z   │   x   │   c   │   d   │   v   │   │   k   │   h   │   ,   │   .   │   -   │  SYS  │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │Rep/NAV│Tab/HUN│  NUM  │   │ Space │  SYM  │ Super │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

### Number: hold `NUM`

The top row is the Hungarian number row (0 left of 1). The right hand has a
numpad with `+ . , -`. On the left, plain mods and extra digits make
Meta/Ctrl/Alt + digit work with the left hand alone; `GUI+Sft` is for
"move window to desktop N".

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│   0   │   1   │   2   │   3   │   4   │   5   │   │   6   │   7   │   8   │   9   │   +   │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │  Alt  │  GUI  │  Ctrl │ Shift │   1   │   │   .   │   4   │   5   │   6   │   ,   │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │GUI+Sft│   3   │   0   │   9   │   2   │   │   0   │   1   │   2   │   3   │   -   │  ___  │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │  ___  │  ___  │  ___  │   │  ___  │  ___  │  ___  │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

### Symbol: hold `SYM`

The top row is what Shift + the number row types on a Hungarian keyboard, and
the brackets are where a Hungarian keyboard has them.

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│       │   '   │   "   │   +   │   !   │   %   │   │   /   │   =   │   (   │   )   │   `   │       │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│   \   │   ~   │   |   │   ^   │   [   │   ]   │   │  Left │  Down │   Up  │ Right │   $   │       │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│       │   <   │   >   │   #   │   &   │   @   │   │       │   {   │   }   │       │   *   │       │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │  ___  │  ___  │  ___  │   │  ___  │  ___  │  ___  │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

### Nav: hold `Rep/NAV`

`Fn` is on the same key as digit `n` on the number layer. Hold a mod on the left
and press arrows on the right, e.g. Meta+Ctrl+← to switch desktops.

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│  F10  │   F1  │   F2  │   F3  │   F4  │   F5  │   │   F6  │   F7  │   F8  │   F9  │  F11  │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │  Alt  │  GUI  │  Ctrl │ Shift │       │   │  Left │  Down │   Up  │ Right │  F12  │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │  Undo │  Cut  │  Copy │       │ Paste │   │  Home │  PgDn │  PgUp │  End  │       │       │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │  ___  │  ___  │  ___  │   │  ___  │  ___  │  ___  │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

### System: hold `SYS`

Reset and bootloader are on both halves, because each half is flashed separately.

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│ Off 5s│  BT 0 │  BT 1 │  BT 2 │  BT 3 │  BT 4 │   │       │       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│ BT clr│       │       │       │       │ Reset │   │ Reset │       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│ BT dis│       │       │       │       │  Boot │   │  Boot │       │       │       │       │       │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │       │       │       │   │       │       │       │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

### Hungarian: hold `Tab/HUN`

Accents grouped by vowel. All other keys fall through, so rolling straight from
an accent into the next letter or Space works.

```
╭───────┬───────┬───────┬───────┬───────┬───────╮   ╭───────┬───────┬───────┬───────┬───────┬───────╮
│  ___  │  ___  │  ___  │  ___  │  ___  │  ___  │   │  ___  │   ű   │   ü   │   ú   │   ö   │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │  ___  │  ___  │  ___  │  ___  │  ___  │   │  ___  │   á   │   é   │   í   │   ó   │  ___  │
├───────┼───────┼───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┼───────┼───────┤
│  ___  │  ___  │  ___  │  ___  │  ___  │  ___  │   │  ___  │  ___  │  ___  │  ___  │   ő   │  ___  │
╰───────┴───────┴───────┼───────┼───────┼───────┤   ├───────┼───────┼───────┼───────┴───────┴───────╯
                        │  ___  │  ___  │  ___  │   │  ___  │  ___  │  ___  │
                        ╰───────┴───────┴───────╯   ╰───────┴───────┴───────╯
```

## How the special keys behave

**Home row mods** use urob's ["timeless" settings](https://github.com/urob/zmk-config):

- A mod only activates when the next key is on the **other** hand or a thumb.
  Rolls within one hand always type letters.
- Pressed right after another key (within 150 ms), it is always a letter.
- For mod + a key on the **same** hand (e.g. Ctrl+C), use the other hand's mod.
  The NUM and NAV layers have plain mods for digits, F-keys and arrows, and
  NAV has undo/cut/copy/paste for one-handed use.

**Thumb keys**

- `Rep/NAV`: tap repeats the last key (handy for double letters). Hold for the
  NAV layer after a short pause; during fast typing it is always Repeat.
- `Tab/HUN`: tap for Tab, hold for accents. Pressing an accent key while holding
  always gives the accent, whatever order you release the keys in.
- `Super`: a plain Super/Meta key. It works with keys on both hands, which tiling
  window managers need. Tapped alone it opens the KDE launcher.

## Editing the keymap

- **Change a key**: find it in the layer's grid in `corne.keymap`. Use `HU_*`
  keycodes for characters (`&kp HU_AT`, not `&kp AT`). Plain keys like `ESC`,
  `LEFT`, `F5` or `LCTRL` don't depend on the layout. For a modifier combination,
  wrap the key: `&kp LC(HU_C)` is Ctrl+C.
- **Pass-through and dead keys**: `___` falls through to the layer below,
  `XXX` does nothing.
- **Key positions**: properties like `hold-trigger-key-positions` use the names
  in the diagram at the top of the keymap (`LT0`, `RM1`, `LH0`, ...).
- **Add a layer**: add a `#define L_NAME n` and a layer node. The number must
  match the node's position in the keymap, counting from 0.
- **Tune timing**: the home row mods' settings are in `MAKE_HRM`, so one change
  applies to both hands. If mods trigger by accident, raise `tapping-term-ms`;
  if letters come out as mods while typing fast, raise `require-prior-idle-ms`.
- The layer grids and the README diagrams are maintained by hand. After editing,
  run the checks below: they catch misaligned columns and README diagrams that
  no longer match the keymap.

  ```sh
  python3 scripts/check_alignment.py README.md config/corne.keymap
  python3 scripts/check_readme_keys.py
  ```

  Use plain ASCII in the diagrams (the accented letters are fine): symbols like
  arrows or `▽` are drawn wider than one column by some fonts.

## Building and flashing

1. Push to GitHub. The **Actions** tab builds the firmware (about 3 minutes).
2. Download the `firmware` artifact from the finished run, or:
   `gh run download <run-id>`
3. Flash each half separately:
   1. Connect the half by USB.
   2. Hold `SYS` and press the half's `Boot` key, or double-tap its reset button.
   3. Copy `corne_left-nice_nano_v2-zmk.uf2` (or `corne_right-…`) onto the
      drive that appears.

If the halves stop connecting to each other, flash
`settings_reset-nice_nano_v2-zmk.uf2` to both halves, then the normal firmware
again. This also clears the Bluetooth pairings.

## Upgrading ZMK

ZMK, zmk-helpers and the build workflow are pinned to `v0.3` in
[`config/west.yml`](config/west.yml) and
[`.github/workflows/build.yml`](.github/workflows/build.yml), so updates on
ZMK's `main` can't break the build. To upgrade, change all three to the new
version together. From **v0.4** the board name in [`build.yaml`](build.yaml)
also changes, from `nice_nano_v2` to `nice_nano//zmk`
([details](https://zmk.dev/blog/2025/12/09/zephyr-4-1)).

## Learning more

- [ZMK docs](https://zmk.dev/docs): [hold-tap](https://zmk.dev/docs/keymaps/behaviors/hold-tap),
  [tap dance](https://zmk.dev/docs/keymaps/behaviors/tap-dance),
  [caps word](https://zmk.dev/docs/keymaps/behaviors/caps-word),
  [key repeat](https://zmk.dev/docs/keymaps/behaviors/key-repeat),
  [list of keycodes](https://zmk.dev/docs/keymaps/list-of-keycodes)
- [urob's zmk-config](https://github.com/urob/zmk-config): where the home row
  mod settings come from
- [zmk-helpers](https://github.com/urob/zmk-helpers): the `ZMK_HOLD_TAP` macros
  and key position names
- [Colemak-DH](https://colemakmods.github.io/mod-dh/)
