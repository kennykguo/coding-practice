"""
Run every `pyex` example block in a .tex file and check the expected-result comments.

  python3 check_examples.py [file.tex ...]      (default: python-review.tex)

Comment markers (on the last line of a top-level statement, or alone on the next line):
  # -> VALUE          the expression's value must equal VALUE
  # -> raises NAME    the statement must raise the exception NAME
  # prints: TEXT      the statement must print TEXT (stripped; use " | " between lines)
Each block runs in a fresh namespace. A statement without a marker must not raise.
"""
import ast
import contextlib
import io
import os
import re
import sys

ARROW = re.compile(r"#\s*->\s*(.*?)\s*$")
PRINTS = re.compile(r"#\s*prints:\s*(.*?)\s*$")
DEFAULT_RECURSION_LIMIT = sys.getrecursionlimit()
BLOCK = re.compile(r"\\begin\{pyex\}\n(.*?)\\end\{pyex\}", re.S)


def matches(value, expected, ns):
    try:
        if eval(expected, dict(ns)) == value:
            return True
    except Exception:
        pass
    text = repr(value)
    if text == expected:
        return True
    if "..." in expected:  # wildcard for reprs with addresses
        pattern = ".*".join(re.escape(part) for part in expected.split("..."))
        return re.fullmatch(pattern, text) is not None
    return False


def run_block(code):
    sys.setrecursionlimit(DEFAULT_RECURSION_LIMIT)  # blocks must not leak global state into each other
    errors = []
    ns = {"__name__": "__example__"}
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return [f"syntax error: {e}"]
    lines = code.splitlines()
    body = tree.body
    for i, stmt in enumerate(body):
        last = lines[stmt.end_lineno - 1]
        src = ast.get_source_segment(code, stmt)
        arrow, prints = ARROW.search(last), PRINTS.search(last)
        if not (arrow or prints) and stmt.end_lineno < len(lines):
            below = lines[stmt.end_lineno].strip()   # a "# -> value" comment on its own line below
            if below.startswith("#"):
                arrow, prints = ARROW.search(below), PRINTS.search(below)
        if i + 1 < len(body) and body[i + 1].lineno == stmt.end_lineno:
            arrow = prints = None  # a marker belongs to the LAST statement on its line
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                if isinstance(stmt, ast.Expr):
                    value = eval(compile(ast.Expression(stmt.value), "<ex>", "eval"), ns)
                else:
                    exec(compile(ast.Module([stmt], []), "<ex>", "exec"), ns)
                    value = None
        except Exception as e:
            if arrow and arrow.group(1).startswith("raises "):
                want = arrow.group(1).split()[1]
                if type(e).__name__ != want:
                    errors.append(f"line {stmt.lineno}: raised {type(e).__name__}, expected {want}: {src}")
            else:
                errors.append(f"line {stmt.lineno}: unexpected {type(e).__name__}: {e}: {src}")
            continue
        if arrow:
            expected = arrow.group(1)
            if expected.startswith("raises "):
                errors.append(f"line {stmt.lineno}: expected {expected}, nothing raised: {src}")
            elif not isinstance(stmt, ast.Expr):
                errors.append(f"line {stmt.lineno}: '# ->' on a statement that is not an expression: {src}")
            elif not matches(value, expected, ns):
                errors.append(f"line {stmt.lineno}: got {value!r}, expected {expected}: {src}")
        if prints:
            got = " | ".join(line.rstrip() for line in out.getvalue().strip().splitlines())
            if got != prints.group(1):
                errors.append(f"line {stmt.lineno}: printed {got!r}, expected {prints.group(1)!r}: {src}")
    return errors


def main():
    files = sys.argv[1:] or [os.path.join(os.path.dirname(os.path.abspath(__file__)), "python-review.tex")]
    total = failed = checks = 0
    for path in files:
        tex = open(path).read()
        for m in BLOCK.finditer(tex):
            total += 1
            code = m.group(1)
            checks += sum(bool(ARROW.search(l) or PRINTS.search(l)) for l in code.splitlines())
            errs = run_block(code)
            if errs:
                failed += 1
                tex_line = tex.count("\n", 0, m.start()) + 2
                print(f"{os.path.basename(path)}:{tex_line}")
                for e in errs:
                    print("   ", e)
    print(f"\n{total - failed}/{total} example blocks pass ({checks} checked results)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
