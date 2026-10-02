# 09 · Count Valid Sequences

You're given an integer `n` and a list of forbidden pairs `pairs`, where each pair is `[a, b]` with
`a != b`.

Consider every non-empty sequence of **consecutive** integers drawn from `1..n`, i.e. every
`(l, l+1, ..., r)` with `1 <= l <= r <= n`.

A sequence is **invalid** if it contains both numbers of any forbidden pair. Return the number of valid
sequences.

```python
def count_valid_sequences(n: int, pairs: list[list[int]]) -> int
```

## Examples

```
n = 4, pairs = [[1,3]]   -> 8
```
Valid: `(1) (2) (3) (4) (1,2) (2,3) (3,4) (2,3,4)`. `(1,2,3)` and `(1,2,3,4)` contain both 1 and 3.

```
n = 3, pairs = []                 -> 6
n = 5, pairs = [[1,2],[4,5]]      -> 8
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= len(pairs) <= 10^5`
- `1 <= a, b <= n`, `a != b`; pairs may be given in either order and may repeat

## Notes on this version

The statement is complete; only the bounds and signature were chosen for this practice set.
