# 12 · Backpropagation Through Sort and Median

Define

```python
def f(x):
    return np.sort(x) / np.median(x)
```

For example, `x = [3, 2, 1]` gives `sort(x) = [1, 2, 3]`, `median(x) = 2`, so `f(x) = [0.5, 1.0, 1.5]`.

You're given the input vector `x` and the upstream gradient `v = dL/dy` where `y = f(x)`.
Return `dL/dx` as a list of floats (same length and order as `x`).

```python
def sort_median_backward(x: list[float], v: list[float]) -> list[float]
```

You may use plain Python (numpy is fine too, if you have it installed). Aim for `O(n log n)`.

## Examples

```
x = [3.0, 2.0, 1.0], v = [1.0, 1.0, 1.0]   -> [0.5, -1.0, 0.5]
x = [5.0],           v = [2.0]             -> [0.0]           # f(x) = x/x = 1 is constant
x = [1.0, 4.0, 2.0, 8.0, 3.0]
v = [0.5, -1.0, 2.0, 0.0, 1.0]             -> [0.1667, 0.0, -0.3333, 0.3333, -0.7222]
```
There are two gradient paths: through the sorting permutation (each `y_i` depends on one sorted element),
and through the median in the denominator (which only the median element receives).

## Constraints

- `1 <= n <= 10^5`, `n` is **odd**
- all values of `x` are distinct, and the median is non-zero
- answers are checked with tolerance `1e-6` (relative or absolute)

## Notes on this version

The statement is complete; the signature and bounds were chosen for this practice set.
