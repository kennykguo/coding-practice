# 05 · Leaves Remaining After Wind Gusts

`garden` is a rectangular integer matrix; `garden[r][c]` is the number of leaves on cell `(r, c)`.

`gusts` is a string of directions, processed in order:

| char | shift |
|------|-------|
| `U`  | every leaf moves one row up (row − 1) |
| `D`  | every leaf moves one row down (row + 1) |
| `L`  | every leaf moves one column left (col − 1) |
| `R`  | every leaf moves one column right (col + 1) |

Each gust shifts **every leaf still in the garden** one cell in that direction. Leaves pushed past the
boundary are gone permanently (they don't come back if the wind reverses). Leaves may pile up on the same cell.

After all gusts, return the total number of leaves still in the garden.

```python
def remaining_leaves(garden: list[list[int]], gusts: str) -> int
```

## Examples

```
garden = [[1, 2, 3],
          [4, 5, 6]]
gusts = "R"     -> 12      # 3 and 6 blow off the right edge; 1+2+4+5
gusts = "RL"    -> 12      # the lost leaves don't return

garden = [[1, 2], [3, 4]], gusts = ""   -> 10
```

## Constraints

- `1 <= rows, cols <= 300`
- `0 <= garden[r][c] <= 10^4`
- `0 <= len(gusts) <= 10^5`

## Notes on this version

Well established: garden of counts, directional gusts, loss at the boundary, return the remaining sum.
Only `R` is confirmed by the original example; the full `U/D/L/R` alphabet, empty-gust behaviour and bounds
were filled in for this practice set.
