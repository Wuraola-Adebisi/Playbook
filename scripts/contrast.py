#!/usr/bin/env python3
"""Contrast ratios for color pairs, with WCAG 2.1 AA verdicts.

Usage:
  python contrast.py "#1a1a1a:#ffffff" "#767676:#ffffff"
      Each argument is foreground:background. Hex only (3 or 6 digits).

  python contrast.py --palette palette.json
      Tests every text color on every surface. Format:
      {
        "text":     {"ink": "#14110f", "muted": "#5c554d"},
        "surfaces": {"ground": "#fbf8f3", "card": "#ffffff", "tint": "#efe6d8"}
      }
      Add "ui": {"line": "#8a8178", "focus": "#3b2fd1"} to also test UI
      boundaries and focus rings against the surfaces (3:1 needed).

Thresholds (WCAG 2.1 AA):
  body text 4.5, large text 3.0 (about 24px, or 19px bold), UI boundaries 3.0.

Exit code is 1 when any body-text pair fails, so it can run in a check script.
Hex values read from images are estimates. Sample them before trusting a result.
"""
import json
import sys


def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(ch * 2 for ch in v)
    if len(v) != 6:
        raise ValueError(f"not a hex color: {value!r}")
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4))


def channel(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (channel(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    l1, l2 = luminance(parse_hex(fg)), luminance(parse_hex(bg))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    return {
        "body": "pass" if r >= 4.5 else "FAIL",
        "large": "pass" if r >= 3.0 else "FAIL",
        "ui": "pass" if r >= 3.0 else "FAIL",
    }


def row(label, fg, bg):
    r = ratio(fg, bg)
    v = verdict(r)
    print(f"{label:<34} {fg:<9} on {bg:<9} {r:5.2f}:1  body {v['body']:<4}  large {v['large']:<4}  ui {v['ui']:<4}")
    return r


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    failed = False

    if argv[0] == "--palette":
        with open(argv[1], encoding="utf-8") as fh:
            palette = json.load(fh)
        surfaces = palette.get("surfaces", {})
        print("Text on surfaces")
        for tname, tval in palette.get("text", {}).items():
            for sname, sval in surfaces.items():
                r = row(f"{tname} on {sname}", tval, sval)
                if r < 4.5:
                    failed = True
        if palette.get("ui"):
            print("\nUI boundaries and focus on surfaces (3:1)")
            for uname, uval in palette["ui"].items():
                for sname, sval in surfaces.items():
                    row(f"{uname} on {sname}", uval, sval)
    else:
        for pair in argv:
            if ":" not in pair:
                print(f"skip {pair!r}: use foreground:background", file=sys.stderr)
                continue
            fg, bg = pair.split(":", 1)
            r = row(pair, fg, bg)
            if r < 4.5:
                failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
