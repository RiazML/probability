#!/usr/bin/env python3
"""Check that the math in Markdown files renders on GitHub AND in VS Code.

GitHub renders math with MathJax, after its Markdown parser has already
touched the text. VS Code's preview renders math with KaTeX. Some LaTeX that
works in one breaks in the other. This script enforces the safe subset that
was tested in both renderers. The rules are explained in .claude/rules/latex.md.

Usage:
    python3 tools/check_math.py                  # check every .md file
    python3 tools/check_math.py FILE_OR_DIR ...  # check some files or folders

Exit code: 1 if any ERROR is found, 0 otherwise. WARNINGs never fail.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv"}

# Commands tested to compile in both KaTeX (VS Code) and MathJax (GitHub).
# To add one: test it on GitHub and in VS Code first, then add it here AND to
# the whitelist in .claude/rules/latex.md.
ALLOWED = set("""
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi
psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
sum prod int iint lim limsup liminf sup inf max min log ln exp sin cos tan det
Pr arg
le leq ge geq ne neq lt gt approx sim simeq cong equiv propto to rightarrow
leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow implies iff mapsto
in notin ni subset subseteq supset supseteq subsetneq cup cap setminus
emptyset varnothing mid perp parallel not colon triangleq
pm mp times cdot div ast star circ bullet
dots ldots cdots vdots ddots
infty partial nabla forall exists neg lnot prime ell
land lor wedge vee top bot
mathbb mathbf mathcal mathrm mathit mathsf mathtt boldsymbol
text textbf textit operatorname
bar overline hat widehat tilde widetilde vec dot ddot underline overbrace
underbrace
frac dfrac tfrac binom dbinom tbinom sqrt
left right big Big bigg Bigg bigl bigr Bigl Bigr
lbrace rbrace langle rangle lvert rvert lVert rVert vert Vert
lfloor rfloor lceil rceil
quad qquad thinspace negthinspace enspace hspace
begin end cr hline displaystyle textstyle
overset underset stackrel xrightarrow xleftarrow boxed
bigcup bigcap bigvee bigwedge
""".split())

# Commands that are known to break in at least one renderer.
BANNED = {
    "color": "not available on GitHub; use **bold** text outside the math",
    "textcolor": "not available on GitHub",
    "cancel": "not available on GitHub",
    "medspace": "not available on GitHub; use \\thinspace or \\quad",
    "thickspace": "not available on GitHub; use \\quad",
    "mspace": "not available in VS Code",
    "tag": "breaks on GitHub; write \\qquad \\text{(1)} instead",
    "label": "no cross-references; refer to equations in words",
    "ref": "no cross-references; refer to equations in words",
    "eqref": "no cross-references; refer to equations in words",
    "newcommand": "macros are not shared between formulas; write it out",
    "renewcommand": "macros are not shared between formulas; write it out",
    "def": "macros are not shared between formulas; write it out",
    "require": "not available in VS Code",
    "bm": "use \\boldsymbol",
    "over": "use \\frac{a}{b}",
    "choose": "use \\binom{n}{k}",
}

BAD_ENVS = {"align", "align*", "equation", "equation*", "gather", "gather*",
            "multline", "eqnarray"}

# Replacements for "backslash + punctuation", which GitHub's Markdown parser
# turns into the bare punctuation before MathJax ever sees it.
PUNCT_FIX = {
    "{": "use \\lbrace", "}": "use \\rbrace",
    ",": "use \\thinspace", ";": "use \\quad or '\\ '", ":": "use \\quad or '\\ '",
    "!": "delete it (or use \\negthinspace)", "|": "use \\Vert",
    "%": "write the percent sign outside the math",
    "#": "write it outside the math", "&": "use \\text{ and }",
    "$": "write money as words, outside the math", "_": "avoid underscores in \\text{}",
}


class Report:
    def __init__(self):
        self.errors = 0
        self.warnings = 0

    def add(self, level, path, line_no, msg):
        if level == "ERROR":
            self.errors += 1
        else:
            self.warnings += 1
        try:
            rel = path.relative_to(ROOT)
        except ValueError:
            rel = path
        print(f"{rel}:{line_no}: {level}: {msg}")


def strip_array_specs(tex):
    """Remove column specs like \\begin{array}{c|cc}, where '|' is allowed."""
    return re.sub(r"\\begin\{array\}\{[^}]*\}", r"\\begin{array}{}", tex)


def check_tex(tex, *, display, path, line_no, rep, in_table=False):
    """Check one formula (without its $ delimiters)."""
    lines = tex.split("\n")
    body = strip_array_specs(tex)

    # Backslash commands and backslash + punctuation.
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == "\\":
            nxt = body[i + 1] if i + 1 < len(body) else ""
            if nxt == "\\":
                # '\\' survives on GitHub only at the end of a display line.
                after = body[i + 2:].split("\n", 1)[0].strip()
                if not display:
                    rep.add("ERROR", path, line_no,
                            "'\\\\' inside inline math; move it to display math or use \\cr")
                elif after:
                    rep.add("ERROR", path, line_no,
                            "'\\\\' in the middle of a line breaks on GitHub; "
                            "end the line after it, or use \\cr")
                i += 2
                continue
            if nxt.isalpha():
                m = re.match(r"[A-Za-z]+", body[i + 1:])
                name = m.group(0)
                if name in BANNED:
                    rep.add("ERROR", path, line_no, f"\\{name}: {BANNED[name]}")
                elif name not in ALLOWED:
                    rep.add("WARNING", path, line_no,
                            f"\\{name} is not in the tested whitelist; test it on GitHub "
                            "and in VS Code, then add it to tools/check_math.py")
                i += 1 + len(name)
                continue
            if nxt in PUNCT_FIX:
                rep.add("ERROR", path, line_no,
                        f"'\\{nxt}' breaks on GitHub: {PUNCT_FIX[nxt]}")
            elif nxt and nxt not in " \n":
                rep.add("ERROR", path, line_no,
                        f"'\\{nxt}' (backslash + punctuation) breaks on GitHub")
            i += 2
            continue
        i += 1

    if "*" in body:
        rep.add("ERROR", path, line_no, "'*' in math can become italics on GitHub; use \\ast")
    if "|" in body:
        where = " (it also splits the table cell)" if in_table else ""
        rep.add("ERROR", path, line_no,
                f"bare '|' in math{where}; use \\mid, \\lvert x \\rvert or \\vert")
    if re.search(r"<(?=[A-Za-z/!?])", body):
        rep.add("ERROR", path, line_no,
                "'<' directly before a letter looks like an HTML tag to GitHub; "
                "put a space after it or use \\lt")
    non_ascii = sorted({c for c in body if ord(c) > 127})
    if non_ascii:
        rep.add("ERROR", path, line_no,
                f"non-ASCII characters in math {non_ascii}; use LaTeX commands (\\mu, \\le, ...)")
    depth = 0
    for c in re.sub(r"\\[{}]", "", body):
        depth += c == "{"
        depth -= c == "}"
        if depth < 0:
            break
    if depth != 0:
        rep.add("ERROR", path, line_no, "unbalanced { } in math")
    for env in re.findall(r"\\begin\{([^}]*)\}", body):
        if env in BAD_ENVS:
            rep.add("ERROR", path, line_no,
                    f"\\begin{{{env}}}: use \\begin{{aligned}} inside $$ ... $$")
        if not display:
            rep.add("WARNING", path, line_no,
                    f"\\begin{{{env}}} in inline math is hard to read; use display math")
    if re.search(r"\\mathbb\{1\}", body):
        rep.add("WARNING", path, line_no, "\\mathbb{1} looks different in each renderer; use \\mathbf{1}")
    if display and any(not ln.strip() for ln in lines[1:-1]):
        rep.add("ERROR", path, line_no, "blank line inside display math breaks it")


def remove_code_spans(text):
    return re.sub(r"(`+)(.+?)\1", lambda m: " " * len(m.group(0)), text)


def is_blank(line):
    return re.sub(r"^\s*(>\s*)*", "", line).strip() == ""


def check_file(path, rep):
    lines = path.read_text(encoding="utf-8").split("\n")
    fence = None            # current code fence marker, e.g. "```"
    details = 0             # depth of <details> blocks
    display_open = None     # line number where a multi-line $$ block opened
    display_buf = []

    for idx, raw in enumerate(lines):
        n = idx + 1
        prev_line = lines[idx - 1] if idx > 0 else ""
        next_line = lines[idx + 1] if idx + 1 < len(lines) else ""

        # Fenced code blocks are skipped (text diagrams and Python code live there).
        m = re.match(r"^\s*(`{3,}|~{3,})(.*)$", raw)
        if fence:
            if m and m.group(1).startswith(fence[0]) and len(m.group(1)) >= len(fence) \
                    and not m.group(2).strip():
                fence = None
            continue
        if m and display_open is None:
            fence = m.group(1)
            info = m.group(2).strip().lower()
            if info.startswith("math"):
                rep.add("ERROR", path, n, "```math blocks do not render in VS Code; use $$ ... $$")
            continue

        # Text inside a blockquote: drop the '>' markers.
        quoted = bool(re.match(r"^\s*>", raw))
        line = re.sub(r"^\s*(>\s?)+", "", raw) if quoted else raw
        stripped = line.strip()
        in_list = bool(re.match(r"^( {2,}|\t)", line)) and not quoted

        # Inside a multi-line $$ block.
        if display_open is not None:
            if stripped == "$$":
                check_tex("\n".join(display_buf), display=True, path=path,
                          line_no=display_open, rep=rep)
                if not is_blank(next_line):
                    rep.add("ERROR", path, n, "add a blank line after the closing $$")
                display_open = None
                display_buf = []
            else:
                if "$" in stripped:
                    rep.add("ERROR", path, n, "'$' inside display math")
                display_buf.append(stripped)
            continue

        details += len(re.findall(r"<details\b", line, re.I))
        details -= len(re.findall(r"</details>", line, re.I))

        no_code = remove_code_spans(line)

        if stripped == "$$":
            if in_list or details > 0:
                rep.add("ERROR", path, n,
                        "multi-line $$ inside a list or <details> does not render on GitHub; "
                        "write it on ONE line: $$ ... $$ (use \\cr for new rows)")
            if not is_blank(prev_line):
                rep.add("ERROR", path, n, "add a blank line before the opening $$")
            display_open = n
            display_buf = []
            continue

        if stripped.startswith("$$"):
            if not (stripped.endswith("$$") and len(stripped) > 4 and stripped.count("$$") == 2):
                rep.add("ERROR", path, n, "a $$ line must be just '$$' or a full '$$ ... $$'")
                continue
            check_tex(stripped[2:-2].strip(), display=True, path=path, line_no=n, rep=rep)
            if not is_blank(prev_line):
                rep.add("ERROR", path, n, "add a blank line before $$ ... $$")
            if not is_blank(next_line):
                rep.add("ERROR", path, n, "add a blank line after $$ ... $$")
            continue

        if "$$" in no_code:
            rep.add("ERROR", path, n, "$$ must start its own line (display math only)")
            continue

        if re.search(r"\\\(|\\\[", no_code) and "$" not in no_code:
            if re.search(r"\\\([^)]*\\\)|\\\[[^\]]*\\\]", no_code):
                rep.add("ERROR", path, n, "\\( \\) and \\[ \\] do not render on GitHub; use $ and $$")
        if "$`" in no_code:
            rep.add("ERROR", path, n, "$`...`$ does not render in VS Code; use $...$")

        # Inline math.
        dollars = [i for i, c in enumerate(no_code) if c == "$" and (i == 0 or no_code[i - 1] != "\\")]
        if stripped.startswith("#") and dollars:
            rep.add("ERROR", path, n, "no math in headings (it breaks links to the heading)")
            continue
        if len(dollars) % 2:
            rep.add("ERROR", path, n,
                    "odd number of '$' (unclosed math, or money written with '$'); "
                    "write money as words, e.g. '5 dollars'")
            continue
        if re.search(r"\\\$", no_code):
            rep.add("WARNING", path, n, "escaped '\\$' found; write money as words instead")
        in_table = stripped.startswith("|")
        for a, b in zip(dollars[0::2], dollars[1::2]):
            tex = no_code[a + 1:b]
            if not tex.strip():
                rep.add("ERROR", path, n, "empty math $$")
                continue
            if tex[0].isspace() or tex[-1].isspace():
                rep.add("ERROR", path, n, f"no space just inside the dollars: write ${tex.strip()}$")
            before = no_code[a - 1] if a > 0 else " "
            after = no_code[b + 1] if b + 1 < len(no_code) else " "
            if before.isalnum():
                rep.add("ERROR", path, n, "put a space before the opening $")
            if after.isalnum():
                rep.add("ERROR", path, n,
                        "a letter or digit right after the closing $ stops the math "
                        "from rendering; add a space or a hyphen")
            check_tex(tex, display=False, path=path, line_no=n, rep=rep, in_table=in_table)

    if display_open is not None:
        rep.add("ERROR", path, display_open, "display math opened with $$ but never closed")
    if fence:
        rep.add("ERROR", path, len(lines), "code fence opened but never closed")


def iter_files(args):
    targets = [Path(a) for a in args] if args else [ROOT]
    for t in targets:
        t = t.resolve()
        if t.is_dir():
            for p in sorted(t.rglob("*.md")):
                if not SKIP_DIRS.intersection(p.parts):
                    yield p
        elif t.suffix == ".md":
            yield t


def main(argv):
    rep = Report()
    files = list(iter_files(argv[1:]))
    for p in files:
        check_file(p, rep)
    print(f"\nChecked {len(files)} file(s): {rep.errors} error(s), {rep.warnings} warning(s).")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
