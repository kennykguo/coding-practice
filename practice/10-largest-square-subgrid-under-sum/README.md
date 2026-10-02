# 10 · Largest Square Subgrid Under a Sum Limit

You're given a 2D integer matrix `grid` and an integer `max_sum`.

A side length `k` is **valid** if **every** contiguous `k x k` square subgrid of `grid` has sum
`<= max_sum`. (Every square of that size — not "there exists one".)

Return the largest valid `k`, or `0` if even `k = 1` is not valid.

```python
def largest_square_side(grid: list[list[int]], max_sum: int) -> int
```

## Examples

```
grid = [[1,1,1],
        [1,1,1],
        [1,1,1]], max_sum = 4   -> 2
```
Every `2x2` square sums to 4; the only `3x3` square sums to 9.

```
grid = [[1,2],[3,4]], max_sum = 4   -> 1     # the 2x2 sums to 10
grid = [[5,0],[0,0]], max_sum = 4   -> 0     # the 1x1 square [5] already exceeds the limit
```

## Constraints

- `1 <= rows, cols <= 300`
- `0 <= grid[r][c] <= 10^4`
- `0 <= max_sum <= 10^12`

## Notes on this version

The "every square of size k must satisfy the limit" rule is from the original. The examples, signature,
bounds, and the assumption that values are **non-negative** were filled in for this practice set. (If
negative values were allowed you couldn't rely on validity being monotonic in `k`.)
