# 03 · Count Routes Through Four Shop Types

There are `n` shops numbered `0..n-1`. Every shop has one of exactly four types: `shops[i]` ∈ `{0, 1, 2, 3}`.
`roads` is a list of **undirected** roads `[a, b]` between shops.

A **route** is a sequence of 4 shops `p0 -> p1 -> p2 -> p3` where each consecutive pair is joined by a road
and the route visits **one shop of each of the four types exactly once** (so the four shops are distinct and
their types are a permutation of `0,1,2,3`; the order of types along the route doesn't matter).

Routes are **ordered**: a route and its reverse count separately. Return the number of routes.

```python
def count_routes(shops: list[int], roads: list[list[int]]) -> int
```

## Examples

```
shops = [0, 1, 2, 3]
roads = [[0,1], [1,2], [2,3]]
-> 2        # 0->1->2->3 and 3->2->1->0
```

```
shops = [0, 1, 2, 3]
roads = [[0,1], [1,2], [2,3], [3,0]]   (a 4-cycle)
-> 8        # 4 starting points x 2 directions
```

```
shops = [0, 0, 1, 2]
roads = [[0,1], [1,2], [2,3]]
-> 0        # no shop of type 3
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= len(roads) <= 10^5`
- no self-loops, no duplicate roads
- the answer can be large (Python ints are fine)

## Notes on this version

Well established: four shop types, a road graph, counting routes that use each type exactly once.
Filled in for this practice set: roads are undirected, reversed routes count as distinct, and the bounds.
