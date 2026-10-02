# Timed Practice Set

12 problems, each in its own folder:

```
NN-problem-name/
  README.md        problem statement, examples, constraints, notes on what's reconstructed
  solution.py      your solution (starts as a stub)
  test.py          runs the judge on this problem
  tests.json.gz    sample + hidden tests (gzipped so the answers aren't sitting in plain view)
```

## Workflow

1. Read `README.md`, write your function in `solution.py` (keep the given name and signature).
2. Run the tests from the problem folder:
   ```bash
   python3 test.py
   ```
   or from anywhere: `python3 practice/judge.py 4` (number or folder name).
3. Every test reports `PASS`, `WRONG ANSWER`, `RUNTIME ERROR` or `TIME LIMIT EXCEEDED` (4 s per test).
   Failing **sample** tests show input/expected/got. Failing **hidden** tests only show the verdict, like
   a real assessment. Add `--reveal` once you want to see them.
4. `ACCEPTED` means every sample and hidden test passed.

Other flags: `--samples` (run only the visible examples), `--time-limit 2` (tighter timing).
`python3 practice/judge.py` with no problem runs everything and prints a scoreboard.

Hidden tests include edge cases and large inputs sized so that the straightforward brute force times out
where an efficient approach is expected (problems 03, 05, 08, 09, 10, 11, 12).

## Problems

| # | Problem | Function |
|---|---------|----------|
| 01 | [Repair One Movement Instruction](01-repair-one-movement-instruction/README.md) | `can_repair` |
| 02 | [Count Matching Regions in Two Binary Grids](02-count-matching-regions/README.md) | `count_matching_regions` |
| 03 | [Count Routes Through Four Shop Types](03-count-four-shop-routes/README.md) | `count_routes` |
| 04 | [Optimal First-Player Card Score](04-optimal-first-player-card-score/README.md) | `first_player_score` |
| 05 | [Leaves Remaining After Wind Gusts](05-leaves-after-wind-gusts/README.md) | `remaining_leaves` |
| 06 | [Invert or Blur an Image](06-invert-or-blur-image/README.md) | `transform_image` |
| 07 | [Largest Microorganism After Consumption](07-largest-microorganism/README.md) | `largest_organism` |
| 08 | [Network Endpoint or Cycle Boundary](08-network-endpoint-or-cycle/README.md) | `find_endpoint` |
| 09 | [Count Valid Sequences](09-count-valid-sequences/README.md) | `count_valid_sequences` |
| 10 | [Largest Square Subgrid Under a Sum Limit](10-largest-square-subgrid-under-sum/README.md) | `largest_square_side` |
| 11 | [Maximize Wall Hits](11-maximize-wall-hits/README.md) | `max_wall_hits` |
| 12 | [Backpropagation Through Sort and Median](12-backprop-sort-median/README.md) | `sort_median_backward` |

Some statements were reconstructed from partial descriptions. Each README ends with a "Notes on this
version" section that says which rules are well established and which were filled in. Problems 01, 03 and
06 rely most on filled-in details.

## Spoilers

`_reference/` contains reference solutions and the test generator (`python3 _reference/gen.py` rebuilds
every `tests.json.gz`). Don't open it until you're done with a problem.
