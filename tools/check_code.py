#!/usr/bin/env python3
"""Re-run every Python example and compare it with the output pasted in the file.

A "Simulate It" example in this book is a ```python block followed by the
word "Output:" and a ```text block holding what the code printed. This script
runs each such block in a fresh Python process and checks that it prints
exactly what the file says. Run it after editing any code or output.

Usage:
    python3 tools/check_code.py                  # check every module folder
    python3 tools/check_code.py FILE_OR_DIR ...  # check some files or folders

Needs numpy, scipy and matplotlib. Exit code: 1 if any block differs or fails.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIR = re.compile(r"```python\n(.*?)```\s*\n\s*Output:\s*\n\s*```text\n(.*?)```", re.S)


def run_block(code):
    """Run code in a fresh interpreter and return (exit code, stdout, stderr)."""
    with tempfile.TemporaryDirectory() as folder:
        script = Path(folder) / "block.py"
        script.write_text(code, encoding="utf-8")
        done = subprocess.run([sys.executable, "-I", str(script)], capture_output=True,
                              text=True, timeout=900, cwd=folder)
    return done.returncode, done.stdout, done.stderr


def check_file(path):
    text = path.read_text(encoding="utf-8")
    checked = bad = 0
    for match in PAIR.finditer(text):
        code, expected = match.group(1), match.group(2)
        checked += 1
        code_run, out, err = run_block(code)
        if code_run != 0 or out.strip() != expected.strip():
            bad += 1
            line = text[:match.start()].count("\n") + 1
            print(f"MISMATCH {path.relative_to(ROOT)}:{line} (exit code {code_run})")
            print("  expected:", expected.strip().splitlines()[:3])
            print("  got:     ", (out or err).strip().splitlines()[:3])
    return checked, bad


def main(argv):
    targets = [Path(a).resolve() for a in argv[1:]] or sorted(ROOT.glob("[0-9][0-9]-*"))
    files = []
    for t in targets:
        files += sorted(t.rglob("*.md")) if t.is_dir() else [t]
    checked = bad = 0
    for f in files:
        c, b = check_file(f)
        checked, bad = checked + c, bad + b
    print(f"\nChecked {checked} code and output pair(s) in {len(files)} file(s): {bad} mismatch(es).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
