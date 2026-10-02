# 06 · Invert or Blur an Image

`image` is a rectangular grayscale image: an integer matrix with every value in `0..255`.
`operation` is either `"invert"` or `"blur"`. Return a **new** matrix of the same shape.

**`"invert"`** — reflect across the vertical axis (reverse every row):

```
1 2 3       3 2 1
4 5 6  ->   6 5 4
```

**`"blur"`** — each output pixel is the average of its **8 surrounding neighbours** that lie inside the image
(the centre pixel itself is **not** included), **rounded down**. A pixel with no neighbours (only possible
in a `1 x 1` image) keeps its original value. All blurred values are computed from the original image.

```python
def transform_image(image: list[list[int]], operation: str) -> list[list[int]]
```

## Examples

```
image = [[1,2,3],[4,5,6]], operation = "invert"  -> [[3,2,1],[6,5,4]]
image = [[1,2,3],[4,5,6]], operation = "blur"    -> [[3,3,4],[2,3,3]]
image = [[200]],           operation = "blur"    -> [[200]]
```
For the blur, pixel `(0,0)` has in-bounds neighbours `2, 4, 5` → `11 // 3 = 3`;
pixel `(0,1)` has `1, 3, 4, 5, 6` → `19 // 5 = 3`.

## Constraints

- `1 <= rows, cols <= 200`
- `0 <= image[r][c] <= 255`

## Notes on this version

⚠️ This is the least certain reconstruction. Known: a `0..255` grayscale matrix, a horizontal-flip
"inversion", and an 8-neighbour blur with an explicit rounding rule and isolated-pixel rule. The exact blur
arithmetic was **not** available, so this version picks: exclude the centre, average only in-bounds
neighbours, floor, isolated pixel unchanged. If the real prompt differs (e.g. includes the centre or rounds
to nearest), read it carefully — the structure of the solution is the same.
