#!/usr/bin/env python3
"""Check relative links in Markdown files, and find files that are still empty.

Usage:
    python3 tools/check_links.py                  # check every .md file
    python3 tools/check_links.py FILE_OR_DIR ...  # check some files or folders

For every link like [text](path) or [text](path#anchor) it checks that:
  - the target file exists (web links starting with http are skipped)
  - the #anchor matches a heading in the target file (GitHub's anchor rules)
It also reports Markdown files that are empty.

Exit code: 1 if any problem is found, 0 otherwise.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", ".claude"}

LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")


def github_anchor(heading):
    """Turn a heading into GitHub's anchor: lowercase, drop punctuation, spaces to '-'."""
    text = heading.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors_of(path, cache={}):
    if path not in cache:
        found, counts, fence = set(), {}, None
        for line in path.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if m:
                fence = None if fence and m.group(1)[0] == fence else (fence or m.group(1)[0])
                continue
            if fence:
                continue
            h = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
            if h:
                base = github_anchor(h.group(1))
                n = counts.get(base, 0)
                found.add(base if n == 0 else f"{base}-{n}")
                counts[base] = n + 1
        cache[path] = found
    return cache[path]


def check_file(path, problems):
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        problems.append(f"{path.relative_to(ROOT)}: EMPTY file")
        return
    no_code = re.sub(r"```.*?```", "", text, flags=re.S)
    no_code = re.sub(r"`[^`\n]*`", "", no_code)
    for line_no, line in enumerate(no_code.split("\n"), 1):
        for target in LINK.findall(line):
            if re.match(r"^[a-z]+:", target):
                continue
            file_part, _, anchor = target.partition("#")
            dest = (path.parent / file_part).resolve() if file_part else path
            rel = path.relative_to(ROOT)
            if not dest.exists():
                problems.append(f"{rel}: broken link -> {target}")
                continue
            if anchor and dest.suffix == ".md" and anchor not in anchors_of(dest):
                problems.append(f"{rel}: missing anchor -> {target}")


def iter_files(args):
    targets = [Path(a) for a in args] if args else [ROOT]
    for t in targets:
        t = t.resolve()
        if t.is_dir():
            for p in sorted(t.rglob("*.md")):
                if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts):
                    yield p
        elif t.suffix == ".md":
            yield t


def main(argv):
    problems = []
    files = list(iter_files(argv[1:]))
    for p in files:
        check_file(p, problems)
    for msg in problems:
        print(msg)
    print(f"\nChecked {len(files)} file(s): {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
