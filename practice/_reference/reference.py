"""
SPOILERS: reference solutions (and brute-force checkers) for every problem.
The judge never imports this file; it only exists to (re)generate tests.json.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations
import sys


# ---------------------------------------------------------------- 01
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left (clockwise)


def _step(grid, r, c, d, cmd):
    """Apply one command. Returns new (r, c, d) or None if the move is invalid."""
    if cmd == 'L':
        return r, c, (d - 1) % 4
    if cmd == 'R':
        return r, c, (d + 1) % 4
    dr, dc = DIRS[d]
    if cmd == 'B':
        dr, dc = -dr, -dc
    nr, nc = r + dr, c + dc
    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or grid[nr][nc] == '#':
        return None
    return nr, nc, d


def _find(grid, ch):
    for r, row in enumerate(grid):
        c = row.find(ch)
        if c != -1:
            return r, c


def can_repair(grid, program):
    start, target = _find(grid, 'S'), _find(grid, 'T')
    # prefix[i] = state before executing program[i] (None if already invalid)
    prefix = [(start[0], start[1], 0)]
    for cmd in program:
        s = prefix[-1]
        prefix.append(None if s is None else _step(grid, *s, cmd))
    for i, old in enumerate(program):
        if prefix[i] is None:
            break
        for new in 'FBLR':
            if new == old:
                continue
            s = _step(grid, *prefix[i], new)
            j = i + 1
            while s is not None and j < len(program):
                s = _step(grid, *s, program[j])
                j += 1
            if s is not None and (s[0], s[1]) == target:
                return True
    return False


def can_repair_brute(grid, program):
    start, target = _find(grid, 'S'), _find(grid, 'T')
    for i in range(len(program)):
        for new in 'FBLR':
            if new == program[i]:
                continue
            p = program[:i] + new + program[i + 1:]
            s = (start[0], start[1], 0)
            for cmd in p:
                s = _step(grid, *s, cmd)
                if s is None:
                    break
            if s is not None and (s[0], s[1]) == target:
                return True
    return False


# ---------------------------------------------------------------- 02
def _regions(grid):
    R, C = len(grid), len(grid[0])
    seen = [[False] * C for _ in range(R)]
    out = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1' and not seen[r][c]:
                seen[r][c] = True
                stack, cells = [(r, c)], []
                while stack:
                    a, b = stack.pop()
                    cells.append((a, b))
                    for da, db in DIRS:
                        x, y = a + da, b + db
                        if 0 <= x < R and 0 <= y < C and grid[x][y] == '1' and not seen[x][y]:
                            seen[x][y] = True
                            stack.append((x, y))
                out.append(frozenset(cells))
    return out


def count_matching_regions(grid1, grid2):
    return len(set(_regions(grid1)) & set(_regions(grid2)))


# ---------------------------------------------------------------- 03
def count_routes(shops, roads):
    n = len(shops)
    cnt = [[0] * 4 for _ in range(n)]
    for a, b in roads:
        cnt[a][shops[b]] += 1
        cnt[b][shops[a]] += 1
    total = 0
    for a, b in roads:
        ta, tb = shops[a], shops[b]
        if ta == tb:
            continue
        x, y = [t for t in range(4) if t != ta and t != tb]
        # middle edge a-b in both orientations: (p, a, b, q) and (q, b, a, p)
        k = cnt[a][x] * cnt[b][y] + cnt[a][y] * cnt[b][x]
        total += 2 * k
    return total


def count_routes_brute(shops, roads):
    n = len(shops)
    adj = [set() for _ in range(n)]
    for a, b in roads:
        adj[a].add(b)
        adj[b].add(a)
    total = 0
    for a in range(n):
        for b in adj[a]:
            for c in adj[b]:
                for d in adj[c]:
                    if len({a, b, c, d}) == 4 and {shops[a], shops[b], shops[c], shops[d]} == {0, 1, 2, 3}:
                        total += 1
    return total


# ---------------------------------------------------------------- 04
def first_player_score(cards):
    n = len(cards)
    pre = [0]
    for x in cards:
        pre.append(pre[-1] + x)
    # dp[i] for current length: best score for player to move on cards[i:i+L]
    dp = list(cards)
    for L in range(2, n + 1):
        nd = []
        for i in range(n - L + 1):
            tot = pre[i + L] - pre[i]
            nd.append(tot - min(dp[i + 1], dp[i]))
        dp = nd
    return dp[0]


def first_player_score_brute(cards):
    @lru_cache(None)
    def f(i, j):
        if i > j:
            return 0
        tot = sum(cards[i:j + 1])
        return tot - min(f(i + 1, j), f(i, j - 1))
    return f(0, len(cards) - 1)


# ---------------------------------------------------------------- 05
GUST = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def remaining_leaves(garden, gusts):
    R, C = len(garden), len(garden[0])
    r = c = 0
    lo_r = hi_r = lo_c = hi_c = 0
    for g in gusts:
        dr, dc = GUST[g]
        r += dr
        c += dc
        lo_r, hi_r = min(lo_r, r), max(hi_r, r)
        lo_c, hi_c = min(lo_c, c), max(hi_c, c)
    r0, r1 = -lo_r, R - 1 - hi_r
    c0, c1 = -lo_c, C - 1 - hi_c
    if r0 > r1 or c0 > c1:
        return 0
    return sum(sum(row[c0:c1 + 1]) for row in garden[r0:r1 + 1])


def remaining_leaves_brute(garden, gusts):
    R, C = len(garden), len(garden[0])
    g = [row[:] for row in garden]
    for ch in gusts:
        dr, dc = GUST[ch]
        ng = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    ng[nr][nc] += g[r][c]
        g = ng
    return sum(map(sum, g))


# ---------------------------------------------------------------- 06
def transform_image(image, operation):
    if operation == 'invert':
        return [row[::-1] for row in image]
    R, C = len(image), len(image[0])
    out = []
    for r in range(R):
        row = []
        for c in range(C):
            s = k = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        s += image[r + dr][c + dc]
                        k += 1
            row.append(s // k if k else image[r][c])
        out.append(row)
    return out


# ---------------------------------------------------------------- 07
def largest_organism(families, sizes):
    line = [[f, s] for f, s in zip(families, sizes)]
    while True:
        done = [False] * len(line)  # participated flags, parallel to line
        ate = False
        i = 0
        while i < len(line):
            cur = line[i]
            if i > 0 and not done[i - 1] and line[i - 1][1] < cur[1]:
                cur[1] += line[i - 1][1]
                del line[i - 1]
                del done[i - 1]
                done[i - 1] = True
                ate = True
                # current now sits at i-1; next organism is at i
            elif i + 1 < len(line) and not done[i + 1] and line[i + 1][1] < cur[1]:
                cur[1] += line[i + 1][1]
                del line[i + 1]
                del done[i + 1]
                done[i] = True
                ate = True
                i += 1
            else:
                i += 1
        if not ate:
            break
    best = line[0]
    for o in line:
        if o[1] > best[1]:
            best = o
    return f"{best[0]} {best[1]}"


# ---------------------------------------------------------------- 08
def find_endpoint(edges, start):
    nxt = {u: v for u, v in edges}
    seen = {start}
    cur = start
    while cur in nxt:
        if nxt[cur] in seen:
            return cur
        cur = nxt[cur]
        seen.add(cur)
    return cur


# ---------------------------------------------------------------- 09
def count_valid_sequences(n, pairs):
    need = [0] * (n + 2)  # need[r] = largest min-element among pairs whose max is r
    for a, b in pairs:
        lo, hi = min(a, b), max(a, b)
        need[hi] = max(need[hi], lo)
    total = 0
    left = 1
    for r in range(1, n + 1):
        left = max(left, need[r] + 1)
        total += r - left + 1
    return total


def count_valid_sequences_brute(n, pairs):
    total = 0
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            if all(not (l <= a <= r and l <= b <= r) for a, b in pairs):
                total += 1
    return total


# ---------------------------------------------------------------- 10
def largest_square_side(grid, max_sum):
    R, C = len(grid), len(grid[0])
    P = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        acc = 0
        for c in range(C):
            acc += grid[r][c]
            P[r + 1][c + 1] = P[r][c + 1] + acc

    def ok(k):
        for r in range(k, R + 1):
            Pr, Pk = P[r], P[r - k]
            for c in range(k, C + 1):
                if Pr[c] - Pk[c] - Pr[c - k] + Pk[c - k] > max_sum:
                    return False
        return True

    lo, hi = 0, min(R, C)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def largest_square_side_brute(grid, max_sum):
    R, C = len(grid), len(grid[0])
    best = 0
    for k in range(1, min(R, C) + 1):
        if all(sum(grid[a][b] for a in range(r, r + k) for b in range(c, c + k)) <= max_sum
               for r in range(R - k + 1) for c in range(C - k + 1)):
            best = k
    return best


# ---------------------------------------------------------------- 11
def max_wall_hits(walls, thickness, energy):
    best = 0
    for side in (1, -1):
        ws = sorted((abs(w) - 0.5, t) for w, t in zip(walls, thickness) if w * side > 0)
        inner_cost = 0  # thickness of walls already crossed on this side
        for j, (dist, t) in enumerate(ws):
            dist = int(dist)
            base = (dist - j) + inner_cost  # plain steps + walls crossed to reach w_j
            rem = energy - base
            if rem < t:
                break  # cannot even cross this wall; farther walls cost more
            best = max(best, j + rem // t)
            inner_cost += t
    return best


def max_wall_hits_brute(walls, thickness, energy):
    wall = {}
    for w, t in zip(walls, thickness):
        wall[int(w - 0.5)] = t  # wall between k and k+1 keyed by k

    @lru_cache(None)
    def f(p, e):
        best = 0
        for q in (p - 1, p + 1):
            k = min(p, q)
            cost = wall.get(k, 1)
            hit = 1 if k in wall else 0
            if cost <= e:
                best = max(best, hit + f(q, e - cost))
        return best
    return f(0, energy)


# ---------------------------------------------------------------- 12
def sort_median_backward(x, v):
    n = len(x)
    order = sorted(range(n), key=lambda i: x[i])
    mid = n // 2
    m = x[order[mid]]
    g = [0.0] * n
    dm = 0.0
    for i, idx in enumerate(order):
        g[idx] = v[i] / m
        dm -= v[i] * x[idx] / (m * m)
    g[order[mid]] += dm
    return g


def sort_median_numeric(x, v, h=1e-6):
    def f(xx):
        s = sorted(xx)
        m = s[len(s) // 2]
        return sum(vi * si / m for vi, si in zip(v, s))
    out = []
    for i in range(len(x)):
        a, b = list(x), list(x)
        a[i] += h
        b[i] -= h
        out.append((f(a) - f(b)) / (2 * h))
    return out


sys.setrecursionlimit(100000)
