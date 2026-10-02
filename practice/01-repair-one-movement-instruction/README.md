# 01 · Repair One Movement Instruction

A robot moves on a rectangular grid given as a list of strings:

| char | meaning |
|------|---------|
| `S`  | start cell (exactly one) |
| `T`  | target cell (exactly one) |
| `#`  | obstacle |
| `.`  | open cell |

The robot starts on `S` **facing up** (toward row 0). A program is a string of commands:

| cmd | effect |
|-----|--------|
| `F` | move forward one cell in the facing direction |
| `B` | move backward one cell (opposite the facing direction) **without** changing orientation |
| `L` | rotate 90° left (counter-clockwise), stay in place |
| `R` | rotate 90° right (clockwise), stay in place |

Exactly one instruction in the program is wrong. You must choose **exactly one** position and replace
its command with one of the **other three** commands, then replay the whole modified program from the start.

A replay is **invalid** if any move leaves the grid or enters a `#` cell. A replay **succeeds** if it is
valid and the robot's **final** position is `T` (passing through `T` earlier doesn't count; `S`/`T` are
otherwise ordinary open cells).

Return `True` if some single replacement makes the replay succeed, otherwise `False`.

```python
def can_repair(grid: list[str], program: str) -> bool
```

## Examples

```
grid = ["..T",
        ".#.",
        "S.."]
program = "FFRFL"   ->  True
```
`F F` takes S (2,0) up to (0,0); `R` faces right; `F` → (0,1); `L` does nothing useful.
Replacing the final `L` with `F` moves to (0,2) = T.

```
grid = ["T..",
        "...",
        "..S"]
program = "LFFRBF"  ->  True
```
As written, after `LFFR` the robot is at (2,0) facing up, and `B` would move it down off the grid.
Replacing `B` with `F` gives (1,0) then (0,0) = T.

```
grid = ["S#T"]
program = "RF"      ->  False
```
Every single replacement either hits the wall, leaves the grid, or ends on S.

## Constraints

- `1 <= rows, cols <= 50`
- `1 <= len(program) <= 1000`
- `program` contains only `F`, `B`, `L`, `R`

## Notes on this version

The core of the problem (exactly one wrong instruction, replace it, replay, avoid obstacles, reach the
target) is well established. The details here were filled in so it's runnable and may differ from the
real wording: the `S/T/#/.` symbols, the `F/B/L/R` alphabet, starting facing up, "leaving the grid or
hitting `#` invalidates the replay", and "the robot must **end** on `T`".
