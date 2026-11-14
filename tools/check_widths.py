#!/usr/bin/env python3
"""Report ASCII diagram lines that are wider than 76 characters.

Only lines inside ```text blocks are checked (diagrams live there). 76
characters fits a phone screen and a split editor.

Usage:
    python3 tools/check_widths.py                  # check every module folder
    python3 tools/check_widths.py FILE_OR_DIR ...  # check some files or folders

Exit code: 1 if any line is too wide, 0 otherwise.
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT = 76


def width(line):
    """Count characters, ignoring combining marks."""
    return sum(0 if unicodedata.combining(c) else 1 for c in line)


def check_file(path):
    problems = 0
    in_block = False
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if re.match(r"^\s*```", line):
            in_block = (not in_block) and line.strip().startswith("```text")
            continue
        if in_block and width(line) > LIMIT:
            print(f"{path.relative_to(ROOT)}:{number}: width {width(line)} (limit {LIMIT})")
            problems += 1
    return problems


def main(argv):
    targets = [Path(a).resolve() for a in argv[1:]] or sorted(ROOT.glob("[0-9][0-9]-*"))
    files = []
    for t in targets:
        files += sorted(t.rglob("*.md")) if t.is_dir() else [t]
    total = sum(check_file(f) for f in files)
    print(f"\nChecked {len(files)} file(s): {total} line(s) too wide.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
