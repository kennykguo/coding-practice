"""
Local judge for the practice problems.

  python3 practice/judge.py 04            # judge one problem (number or folder name)
  python3 practice/judge.py               # judge every problem, print a scoreboard
  python3 practice/judge.py 04 --samples  # only the visible sample tests
  python3 practice/judge.py 04 --reveal   # show input/expected/output for failing hidden tests too
  python3 practice/judge.py 04 --time-limit 4   # enforce a per-test time limit (off by default)

Each problem folder holds solution.py (yours) and tests.json.gz (samples + hidden tests).
"""
import argparse
import copy
import gzip
import importlib.util
import json
import math
import os
import signal
import sys
import time
import traceback

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TIME_LIMIT = 0  # seconds per test case; 0 = no limit
SLOW_WARNING = 4.0     # flag (but still pass) tests slower than this


class TimeLimitExceeded(Exception):
    pass


def _on_alarm(signum, frame):
    raise TimeLimitExceeded()


def problem_dirs():
    return sorted(d for d in os.listdir(ROOT)
                  if os.path.isdir(os.path.join(ROOT, d)) and d[:2].isdigit())


def resolve(name):
    name = name.rstrip("/").split("/")[-1]
    for d in problem_dirs():
        if d == name or d.startswith(name.zfill(2) + "-"):
            return d
    sys.exit(f"No problem matching '{name}'. Options:\n  " + "\n  ".join(problem_dirs()))


def load_solution(folder):
    path = os.path.join(ROOT, folder, "solution.py")
    spec = importlib.util.spec_from_file_location(f"solution_{folder[:2]}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def same(expected, got, mode):
    if mode == "float_list":
        try:
            got = list(got)
            return len(got) == len(expected) and all(
                math.isclose(float(g), e, rel_tol=1e-6, abs_tol=1e-6) for g, e in zip(got, expected))
        except (TypeError, ValueError):
            return False
    if isinstance(got, tuple):
        got = list(got)
    if isinstance(expected, list) and isinstance(got, list):
        return len(expected) == len(got) and all(same(e, g, mode) for e, g in zip(expected, got))
    if isinstance(expected, bool) or isinstance(got, bool):
        return type(expected) is type(got) and expected == got
    return expected == got


def short(x, limit=400):
    s = json.dumps(x) if not isinstance(x, str) else repr(x)
    return s if len(s) <= limit else s[:limit] + f"... ({len(s)} chars)"


def judge(folder, samples_only=False, reveal=False, time_limit=DEFAULT_TIME_LIMIT, quiet=False):
    with gzip.open(os.path.join(ROOT, folder, "tests.json.gz"), "rt") as f:
        suite = json.load(f)
    cases = [c for c in suite["cases"] if not (samples_only and c["hidden"])]
    log = (lambda *a: None) if quiet else print
    log(f"\n== {folder} ==")

    try:
        mod = load_solution(folder)
        func = getattr(mod, suite["function"])
    except Exception:
        log("  Could not load solution.py:\n" + traceback.format_exc())
        return 0, len(cases), "load error"

    signal.signal(signal.SIGALRM, _on_alarm)
    passed, status, total_time = 0, "", 0.0
    for case in cases:
        args = copy.deepcopy(case["args"])
        verdict, got, err = "PASS", None, None
        start = time.perf_counter()
        try:
            if time_limit > 0:
                signal.setitimer(signal.ITIMER_REAL, time_limit)
            got = func(*args)
        except TimeLimitExceeded:
            verdict = "TIME LIMIT EXCEEDED"
        except NotImplementedError:
            log("  solution not implemented yet (raise NotImplementedError)")
            return 0, len(cases), "not attempted"
        except RecursionError:
            verdict, err = "RUNTIME ERROR", "RecursionError: maximum recursion depth exceeded"
        except Exception:
            verdict, err = "RUNTIME ERROR", traceback.format_exc(limit=-3)
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
        elapsed = time.perf_counter() - start
        total_time += elapsed
        if verdict == "PASS" and not same(case["expected"], got, suite["compare"]):
            verdict = "WRONG ANSWER"
        if verdict == "PASS":
            passed += 1
        slow = "  (slow: would likely time out on a real judge)" if elapsed > SLOW_WARNING else ""
        log(f"  {case['name']:<10} {verdict:<20} {elapsed * 1000:8.1f} ms{slow}")
        if verdict != "PASS" and (not case["hidden"] or reveal):
            log(f"      input:    {short(case['args'])}")
            log(f"      expected: {short(case['expected'])}")
            if verdict == "WRONG ANSWER":
                log(f"      got:      {short(got)}")
            if err:
                log("      " + err.strip().replace("\n", "\n      "))
    status = "ACCEPTED" if passed == len(cases) else "FAILED"
    log(f"  -> {passed}/{len(cases)} passed  [{status}]  total {total_time:.2f}s")
    return passed, len(cases), status


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("problem", nargs="?", help="problem number (e.g. 4) or folder name; omit to run all")
    ap.add_argument("--samples", action="store_true", help="run only the visible sample tests")
    ap.add_argument("--reveal", action="store_true", help="show details of failing hidden tests")
    ap.add_argument("--time-limit", type=float, default=DEFAULT_TIME_LIMIT, help="seconds per test (default: no limit)")
    a = ap.parse_args()

    if a.problem:
        _, _, status = judge(resolve(a.problem), a.samples, a.reveal, a.time_limit)
        sys.exit(0 if status == "ACCEPTED" else 1)

    board = [(d, *judge(d, a.samples, a.reveal, a.time_limit, quiet=True)) for d in problem_dirs()]
    print()
    for d, p, t, s in board:
        print(f"  {d:<42} {p:>3}/{t:<3} {s}")
    print(f"\n  solved {sum(s == 'ACCEPTED' for *_, s in board)}/{len(board)}")


if __name__ == "__main__":
    main()
