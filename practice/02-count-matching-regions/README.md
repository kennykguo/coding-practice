# 02 · Count Matching Regions in Two Binary Grids

You're given two rectangular binary grids `grid1` and `grid2` of the **same dimensions**, each a list of
strings. `'1'` is a filled cell, `'0'` an empty cell.

A **region** is a maximal group of `'1'` cells connected horizontally or vertically (diagonal contact does
**not** connect cells).

A region of `grid1` **matches** a region of `grid2` if the two regions contain exactly the same set of
`(row, col)` coordinates. Return the number of matching regions.

```python
def count_matching_regions(grid1: list[str], grid2: list[str]) -> int
```

## Examples

```
grid1 = ["001",      grid2 = ["001",
         "011",               "011",
         "100"]               "101"]
-> 1
```
The upper-right region differs (`grid2` also contains `(2,2)`), but the isolated `(2,0)` region is
identical in both.

```
grid1 = ["11","11"], grid2 = ["11","11"]   -> 1
grid1 = grid2 = ["101","010","101"]         -> 5   (five single-cell regions)
```

## Constraints

- `1 <= rows, cols <= 300`
- both grids have the same shape and contain only `'0'` and `'1'`

## Notes on this version

The statement is essentially complete. The function name and size bounds were chosen for this practice
set. Watch out for recursion depth on large regions.
