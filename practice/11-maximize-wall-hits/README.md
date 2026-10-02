# 11 · Maximize Wall Hits

You stand on an infinite number line at integer position `0`.

Walls sit at half-integer positions (e.g. `-1.5`, `0.5`, `3.5`), so each wall lies between two adjacent
integers. `walls[i]` has thickness `thickness[i]`.

Each move takes you exactly one integer step left or right:
- if the step crosses no wall, it costs `1` energy;
- if it crosses a wall of thickness `t`, it costs `t` energy and counts as **one hit**.

Walls are never destroyed. You may change direction whenever you like and cross the same wall repeatedly;
every crossing is another hit. You don't have to use all your energy.

Return the maximum number of hits achievable with total cost `<= energy`.

```python
def max_wall_hits(walls: list[float], thickness: list[int], energy: int) -> int
```

## Examples

```
walls = [-1.5, 0.5, 1.5, 5.5], thickness = [2, 4, 8, 3], energy = 3   -> 1
```
`0 -> -1` costs 1, then `-1 -> -2` crosses the `-1.5` wall for 2. Total cost 3, one hit.

```
walls = [0.5], thickness = [2], energy = 7   -> 3     # cross back and forth 3 times (cost 6)
walls = [2.5], thickness = [1], energy = 2   -> 0     # 2 energy only gets you to position 2
```

## Constraints

- `0 <= len(walls) <= 10^5`, `len(thickness) == len(walls)`
- wall positions are distinct values `k + 0.5` with `-10^9 <= k < 10^9`
- `1 <= thickness[i] <= 10^9`
- `0 <= energy <= 10^12`

## Notes on this version

The full mechanics are from the original; only the signature and bounds were chosen here.
