#!/usr/bin/env python3
"""Two robots share an elevator ride. One line of awkward small talk.

The program writes exactly one line to /output/entry.txt: the small talk
itself. Nothing else is written.
"""

import os

REMARK = "We have been riding together for three floors and neither of us has pressed a button. I respect the commitment to nowhere."


def _check(text):
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} chars, gate needs 1-200")
    if any(ch in text for ch in "\t\r\n"):
        raise SystemExit("line must be a single line, no tab or newline inside")
    if text != text.strip():
        raise SystemExit("line must not start or end with whitespace")


def main():
    _check(REMARK)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(REMARK)


if __name__ == "__main__":
    main()
