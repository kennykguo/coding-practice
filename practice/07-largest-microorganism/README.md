# 07 · Largest Microorganism After Consumption

Microorganisms stand in a line, left to right. Organism `i` has family `families[i]` (a string) and a
positive size `sizes[i]`.

The simulation runs in **rounds**. At the start of each round every living organism is marked as
*not participated*. Then scan the current line **left to right**; for the organism being considered:

1. If it has a **left** neighbour that has not participated this round and is **strictly smaller**, it
   consumes the left neighbour.
2. Otherwise, if it has a **right** neighbour that has not participated this round and is **strictly
   smaller**, it consumes the right neighbour.
3. Otherwise nothing happens.

When an organism consumes another:
- the eater's size increases by the eaten organism's size;
- the eaten organism is removed immediately (adjacency changes right away for the rest of the scan);
- the eater is marked as *participated* for the rest of this round.

Continue the scan with the next organism to the right of the one just considered. Rounds repeat until a
full round passes with no consumption.

Return the largest surviving organism as the string `"<family> <size>"`. If several survivors tie for the
largest size, return the **leftmost** one.

```python
def largest_organism(families: list[str], sizes: list[int]) -> str
```

## Examples

```
families = ["A", "B", "C"], sizes = [3, 1, 2]   -> "A 6"
```
Round 1: `A(3)` eats `B(1)` → `A(4)`, participated. `C(2)`'s left neighbour `A` has participated, no right
neighbour → nothing. Round 2: `A(4)` eats `C(2)` → `A(6)`. Round 3: nothing happens.

```
families = ["A", "B"], sizes = [5, 5]            -> "A 5"   (strictly smaller only; tie → leftmost)
families = ["X", "Y", "Z"], sizes = [1, 2, 3]    -> "Y 3"
```
Round 1: `X(1)` can't eat. `Y(2)` eats `X(1)` → `Y(3)`. `Z(3)`'s left neighbour has participated.
Round 2: `Y(3)` and `Z(3)` are equal, so nothing happens; the tie goes to the leftmost.

## Constraints

- `1 <= n <= 20`
- `1 <= sizes[i] <= 1000`
- family names are short strings and may repeat

## Notes on this version

The comparison, participation rule, scan order, left priority, growth and output format are from the
original. The exact wording for termination and tie-breaking wasn't visible; this version uses "repeat
until a round has no consumption" and "tie → leftmost".
