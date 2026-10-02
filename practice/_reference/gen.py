"""
Regenerates tests.json.gz for every problem from the reference solutions.
Usage: python3 practice/_reference/gen.py
"""
import gzip
import json
import os
import random
import string

from reference import *
from reference import _step

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(folder, func, samples, hidden, compare="exact"):
    cases = []
    for i, args in enumerate(samples, 1):
        cases.append({"name": f"sample {i}", "hidden": False, "args": args, "expected": func(*args)})
    for i, args in enumerate(hidden, 1):
        cases.append({"name": f"hidden {i}", "hidden": True, "args": args, "expected": func(*args)})
    path = os.path.join(ROOT, folder, "tests.json.gz")
    with gzip.open(path, "wt") as f:
        json.dump({"function": func.__name__, "compare": compare, "cases": cases}, f, separators=(",", ":"))
    print(f"{folder}: {len(cases)} cases, {os.path.getsize(path) // 1024} KB")


# ---------------------------------------------------------------- 01
def gen_01(R):
    def random_grid(r, c, p_wall):
        return [['#' if R.random() < p_wall else '.' for _ in range(c)] for _ in range(r)]

    def walk_case(r, c, length, p_wall, corrupt=True):
        """Random valid walk from S; T placed where it ends; then corrupt one command."""
        while True:
            g = random_grid(r, c, p_wall)
            sr, sc = R.randrange(r), R.randrange(c)
            g[sr][sc] = '.'
            s = (sr, sc, 0)
            prog = []
            for _ in range(length):
                opts = [cmd for cmd in 'FFFBLR' if _step(g, *s, cmd) is not None]
                cmd = R.choice(opts)
                prog.append(cmd)
                s = _step(g, *s, cmd)
            if (s[0], s[1]) != (sr, sc):
                break
        g[sr][sc] = 'S'
        g[s[0]][s[1]] = 'T'
        if corrupt:
            i = R.randrange(length)
            prog[i] = R.choice([x for x in 'FBLR' if x != prog[i]])
        return [[''.join(row) for row in g], ''.join(prog)]

    def random_case(r, c, length, p_wall):
        g = random_grid(r, c, p_wall)
        (a, b), (x, y) = R.sample([(i, j) for i in range(r) for j in range(c)], 2)
        g[a][b], g[x][y] = 'S', 'T'
        return [[''.join(row) for row in g], ''.join(R.choice('FBLR') for _ in range(length))]

    samples = [
        [["..T", ".#.", "S.."], "FFRFL"],
        [["T..", "...", "..S"], "LFFRBF"],
        [["S#T"], "RF"],
    ]
    hidden = []
    hidden.append([["TS"], "L"])            # must still replace: L->F? goes up (invalid)...
    hidden.append([["S", "T"], "B"])        # already correct; must change it
    hidden.append([["T", "S"], "B"])
    hidden.append([[".T.", "#S#"], "RRF"])
    for _ in range(10):
        hidden.append(walk_case(R.randint(2, 6), R.randint(2, 6), R.randint(1, 12), 0.2))
    for _ in range(6):
        hidden.append(random_case(R.randint(2, 5), R.randint(2, 5), R.randint(1, 8), 0.15))
    for _ in range(6):
        hidden.append(walk_case(R.randint(10, 30), R.randint(10, 30), R.randint(50, 200), 0.25))
    hidden.append(walk_case(4, 4, 6, 0.0, corrupt=False))
    # large stress: open 50x50 grid, 1000 commands
    for _ in range(3):
        hidden.append(walk_case(50, 50, 1000, 0.05))
    big = random_case(50, 50, 1000, 0.0)
    big[1] = 'L' * 999 + 'F'   # hard to break early
    hidden.append(big)
    write("01-repair-one-movement-instruction", can_repair, samples, hidden)


# ---------------------------------------------------------------- 02
def gen_02(R):
    def rand_grid(r, c, p):
        return [[('1' if R.random() < p else '0') for _ in range(c)] for _ in range(r)]

    def mutate(g, k):
        g = [row[:] for row in g]
        for _ in range(k):
            a, b = R.randrange(len(g)), R.randrange(len(g[0]))
            g[a][b] = '1' if g[a][b] == '0' else '0'
        return g

    J = lambda g: [''.join(r) for r in g]
    samples = [
        [["001", "011", "100"], ["001", "011", "101"]],
        [["11", "11"], ["11", "11"]],
        [["101", "010", "101"], ["101", "010", "101"]],
    ]
    hidden = [
        [["0"], ["0"]], [["1"], ["1"]], [["1"], ["0"]],
        [["110", "011"], ["100", "011"]],
        [["111", "101", "111"], ["111", "111", "111"]],
        [["1010", "1010"], ["1010", "0010"]],
    ]
    for _ in range(10):
        r, c = R.randint(1, 8), R.randint(1, 8)
        g = rand_grid(r, c, R.choice([0.3, 0.45, 0.6]))
        hidden.append([J(g), J(mutate(g, R.randint(0, 4)))])
    for _ in range(4):
        r, c = R.randint(30, 80), R.randint(30, 80)
        g = rand_grid(r, c, 0.45)
        hidden.append([J(g), J(mutate(g, R.randint(1, 40)))])
    g = rand_grid(300, 300, 0.4)
    hidden.append([J(g), J(mutate(g, 50))])
    g = [['1'] * 300 for _ in range(300)]          # one giant region (recursion depth trap)
    hidden.append([J(g), J(g)])
    g = [['1' if (r % 2 == 0 or c == (0 if r % 4 == 1 else 299)) else '0' for c in range(300)] for r in range(300)]
    hidden.append([J(g), J(g)])                    # long snake region
    write("02-count-matching-regions", count_matching_regions, samples, hidden)


# ---------------------------------------------------------------- 03
def gen_03(R):
    def rand_graph(n, m):
        es = set()
        while len(es) < m:
            a, b = R.randrange(n), R.randrange(n)
            if a != b:
                es.add((min(a, b), max(a, b)))
        return [list(e) for e in es]

    samples = [
        [[0, 1, 2, 3], [[0, 1], [1, 2], [2, 3]]],
        [[0, 1, 2, 3], [[0, 1], [1, 2], [2, 3], [3, 0]]],
        [[0, 0, 1, 2], [[0, 1], [1, 2], [2, 3]]],
    ]
    hidden = [
        [[0], []], [[0, 1, 2], [[0, 1], [1, 2]]],
        [[3, 2, 1, 0, 1], [[0, 1], [1, 2], [2, 3], [3, 4]]],
        [[0, 1, 2, 3], [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]],
        [[1, 0, 2, 3, 0], [[0, 1], [1, 2], [2, 3], [0, 4]]],
    ]
    for _ in range(10):
        n = R.randint(4, 12)
        m = R.randint(0, n * (n - 1) // 2)
        hidden.append([[R.randint(0, 3) for _ in range(n)], rand_graph(n, m)])
    for _ in range(3):
        n = R.randint(200, 2000)
        hidden.append([[R.randint(0, 3) for _ in range(n)], rand_graph(n, R.randint(n, 3 * n))])
    n = 100000
    hidden.append([[R.randint(0, 3) for _ in range(n)], rand_graph(n, 100000)])
    # two hubs: naive enumeration of neighbor pairs is ~4e8
    n = 40002
    shops = [1, 2] + [R.choice([0, 3]) for _ in range(n - 2)]
    roads = [[0, 1]] + [[0, i] for i in range(2, 20002)] + [[1, i] for i in range(20002, n)]
    hidden.append([shops, roads])
    # star with all four types
    n = 60001
    shops = [0] + [R.randint(1, 3) for _ in range(n - 1)]
    roads = [[0, i] for i in range(1, n)] + [[i, i + 1] for i in range(1, 20000)]
    hidden.append([shops, roads])
    write("03-count-four-shop-routes", count_routes, samples, hidden)


# ---------------------------------------------------------------- 04
def gen_04(R):
    samples = [[[1, 9, 10, 5, 6, 4]], [[5, 3]], [[2, 2, 2, 2]]]
    hidden = [[[1, 100]], [[100, 1, 1, 100]], [[3, 9, 1, 2]], [[1, 1000, 1, 1, 1000, 1]]]
    for _ in range(10):
        hidden.append([[R.randint(1, 20) for _ in range(2 * R.randint(1, 8))]])
    for _ in range(4):
        hidden.append([[R.randint(1, 10 ** 4) for _ in range(2 * R.randint(50, 300))]])
    for _ in range(3):
        hidden.append([[R.randint(1, 10 ** 9) for _ in range(1000)]])
    write("04-optimal-first-player-card-score", first_player_score, samples, hidden)


# ---------------------------------------------------------------- 05
def gen_05(R):
    rg = lambda r, c, hi: [[R.randint(0, hi) for _ in range(c)] for _ in range(r)]
    samples = [
        [[[1, 2, 3], [4, 5, 6]], "R"],
        [[[1, 2, 3], [4, 5, 6]], "RL"],
        [[[1, 2], [3, 4]], ""],
    ]
    hidden = [
        [[[7]], ""], [[[7]], "U"], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], "DU"],
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], "LRRL"], [[[5, 5, 5]], "UD"],
    ]
    for _ in range(10):
        hidden.append([rg(R.randint(1, 6), R.randint(1, 6), 9), ''.join(R.choice('UDLR') for _ in range(R.randint(0, 10)))])
    for _ in range(3):
        hidden.append([rg(R.randint(50, 100), R.randint(50, 100), 1000), ''.join(R.choice('UDLR') for _ in range(R.randint(100, 1000)))])
    # big grid, long gust sequence that stays balanced (simulation is far too slow)
    for _ in range(3):
        s = []
        for _ in range(50000):
            d = R.choice('UL')
            s.append(d)
            s.append({'U': 'D', 'L': 'R'}[d])
        R.shuffle(s)
        hidden.append([rg(300, 300, 10 ** 4), ''.join(s)])
    hidden.append([rg(300, 300, 10 ** 4), 'R' * 299 + 'L' * 99999])
    write("05-leaves-after-wind-gusts", remaining_leaves, samples, hidden)


# ---------------------------------------------------------------- 06
def gen_06(R):
    rg = lambda r, c: [[R.randint(0, 255) for _ in range(c)] for _ in range(r)]
    samples = [
        [[[1, 2, 3], [4, 5, 6]], "invert"],
        [[[1, 2, 3], [4, 5, 6]], "blur"],
        [[[200]], "blur"],
    ]
    hidden = [
        [[[7]], "invert"], [[[10, 20]], "blur"], [[[0], [255], [0]], "blur"],
        [[[255] * 3] * 3, "blur"], [[[1, 2], [3, 4]], "invert"],
    ]
    for _ in range(12):
        hidden.append([rg(R.randint(1, 7), R.randint(1, 7)), R.choice(["invert", "blur"])])
    for op in ("invert", "blur"):
        hidden.append([rg(150, 200), op])
    write("06-invert-or-blur-image", transform_image, samples, hidden)


# ---------------------------------------------------------------- 07
def gen_07(R):
    samples = [
        [["A", "B", "C"], [3, 1, 2]],
        [["A", "B"], [5, 5]],
        [["X", "Y", "Z"], [1, 2, 3]],
    ]
    hidden = [
        [["A"], [10]], [["A", "B"], [1, 2]], [["A", "B", "C"], [2, 1, 3]],
        [["A", "B", "C", "D"], [1, 3, 1, 3]], [["P", "Q", "R"], [4, 4, 4]],
        [["A", "B", "C", "D", "E"], [5, 4, 3, 2, 1]],
        [["A", "B", "C", "D", "E"], [1, 2, 3, 4, 5]],
        [["A", "B", "C", "D", "E"], [2, 1, 2, 1, 2]],
    ]
    for _ in range(18):
        n = R.randint(2, 20)
        fams = [R.choice(string.ascii_uppercase[:R.randint(2, 8)]) for _ in range(n)]
        hidden.append([fams, [R.randint(1, R.choice([5, 20, 1000])) for _ in range(n)]])
    write("07-largest-microorganism", largest_organism, samples, hidden)


# ---------------------------------------------------------------- 08
def gen_08(R):
    samples = [
        [[[1, 3], [7, 3], [3, 4], [4, 6], [2, 6], [6, 9], [9, 5]], 1],
        [[[0, 1], [1, 2], [2, 0]], 0],
        [[[0, 1], [1, 2], [2, 3], [3, 1]], 0],
    ]
    hidden = [
        [[], 0], [[[0, 1]], 1], [[[0, 0]], 0], [[[1, 2]], 0], [[[0, 1], [1, 1]], 0],
        [[[0, 1], [1, 2], [2, 1]], 2], [[[3, 2], [2, 1], [1, 0]], 3],
    ]
    def functional(n, p_none):
        es = [[u, R.randrange(n)] for u in range(n) if R.random() > p_none]
        R.shuffle(es)
        return es
    for _ in range(12):
        n = R.randint(2, 12)
        hidden.append([functional(n, R.choice([0.0, 0.2, 0.5])), R.randrange(n)])
    n = 100000
    perm = list(range(n))
    R.shuffle(perm)
    chain = [[perm[i], perm[i + 1]] for i in range(n - 1)]
    R.shuffle(chain)
    hidden.append([chain, perm[0]])                               # long path to endpoint
    cyc = chain + [[perm[-1], perm[n // 2]]]
    R.shuffle(cyc)
    hidden.append([cyc, perm[0]])                                 # long tail into a big cycle
    ring = [[i, (i + 1) % n] for i in range(n)]
    hidden.append([ring, 12345])
    hidden.append([functional(n, 0.0), R.randrange(n)])
    write("08-network-endpoint-or-cycle", find_endpoint, samples, hidden)


# ---------------------------------------------------------------- 09
def gen_09(R):
    samples = [[4, [[1, 3]]], [3, []], [5, [[1, 2], [4, 5]]]]
    hidden = [[1, []], [2, [[1, 2]]], [2, [[2, 1]]], [6, [[5, 2], [1, 3]]], [5, [[1, 5]]], [4, [[1, 3], [1, 3]]]]
    for _ in range(12):
        n = R.randint(2, 30)
        hidden.append([n, [R.sample(range(1, n + 1), 2) for _ in range(R.randint(0, 8))]])
    hidden.append([100000, []])
    hidden.append([100000, [[1, 100000]]])
    for k in (10, 1000, 100000):
        n = 100000
        hidden.append([n, [R.sample(range(1, n + 1), 2) for _ in range(k)]])
    hidden.append([100000, [[i, i + 50] for i in range(1, 99951, 7)]])
    write("09-count-valid-sequences", count_valid_sequences, samples, hidden)


# ---------------------------------------------------------------- 10
def gen_10(R):
    rg = lambda r, c, hi: [[R.randint(0, hi) for _ in range(c)] for _ in range(r)]
    samples = [
        [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 4],
        [[[1, 2], [3, 4]], 4],
        [[[5, 0], [0, 0]], 4],
    ]
    hidden = [
        [[[7]], 7], [[[7]], 6], [[[0, 0, 0]], 0], [[[1, 1, 1], [1, 9, 1], [1, 1, 1]], 12],
        [[[1, 1, 1], [1, 9, 1], [1, 1, 1]], 17],
    ]
    for _ in range(12):
        r, c = R.randint(1, 7), R.randint(1, 7)
        g = rg(r, c, 9)
        hidden.append([g, R.randint(0, sum(map(sum, g)))])
    for _ in range(3):
        g = rg(R.randint(250, 300), R.randint(250, 300), 10 ** 4)
        k = R.randint(5, 120)
        hidden.append([g, k * k * 5000])
    g = [[1] * 300 for _ in range(300)]
    hidden.append([g, 300 * 300])
    hidden.append([g, 299 * 299])
    write("10-largest-square-subgrid-under-sum", largest_square_side, samples, hidden)


# ---------------------------------------------------------------- 11
def gen_11(R):
    samples = [
        [[-1.5, 0.5, 1.5, 5.5], [2, 4, 8, 3], 3],
        [[0.5], [2], 7],
        [[2.5], [1], 2],
    ]
    hidden = [
        [[], [], 100], [[0.5], [5], 4], [[0.5, -0.5], [3, 2], 10], [[3.5], [1], 3],
        [[3.5], [1], 4], [[0.5, 1.5], [5, 1], 9], [[-0.5], [1], 0],
    ]
    for _ in range(14):
        ks = R.sample(range(-10, 10), R.randint(1, 8))
        hidden.append([[k + 0.5 for k in ks], [R.randint(1, 8) for _ in ks], R.randint(0, 40)])
    for _ in range(2):
        n = 100000
        ks = R.sample(range(-10 ** 9, 10 ** 9), n)
        hidden.append([[k + 0.5 for k in ks], [R.randint(1, 10 ** 9) for _ in ks], R.randint(10 ** 9, 10 ** 12)])
    n = 100000
    ks = list(range(-n // 2, n // 2))
    hidden.append([[k + 0.5 for k in ks], [R.randint(1, 3) for _ in ks], 10 ** 12])
    write("11-maximize-wall-hits", max_wall_hits, samples, hidden)


# ---------------------------------------------------------------- 12
def gen_12(R):
    samples = [
        [[3.0, 2.0, 1.0], [1.0, 1.0, 1.0]],
        [[5.0], [2.0]],
        [[1.0, 4.0, 2.0, 8.0, 3.0], [0.5, -1.0, 2.0, 0.0, 1.0]],
    ]
    hidden = [[[-2.0], [1.0]], [[-3.0, -1.0, -2.0], [1.0, 2.0, 3.0]], [[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]]]
    def case(n, spread):
        while True:
            x = [k / 1000 for k in R.sample(range(-spread * 1000, spread * 1000), n)]
            if abs(sorted(x)[n // 2]) > 0.5:
                return [x, [round(R.uniform(-5, 5), 3) for _ in range(n)]]
    for _ in range(12):
        hidden.append(case(2 * R.randint(0, 6) + 1, 50))
    for _ in range(3):
        hidden.append(case(99999, 10 ** 4))
    write("12-backprop-sort-median", sort_median_backward, samples, hidden, compare="float_list")


if __name__ == "__main__":
    for i, g in enumerate([gen_01, gen_02, gen_03, gen_04, gen_05, gen_06, gen_07, gen_08, gen_09, gen_10, gen_11, gen_12], 1):
        g(random.Random(1000 + i))
