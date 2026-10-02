# 08 · Network Endpoint or Cycle Boundary

You're given a directed graph as a list of edges `[u, v]` (meaning `u -> v`). Every node has **at most one**
outgoing edge. Nodes are non-negative integers; a node may appear in no edge at all.

Starting from `start`, repeatedly follow the unique outgoing edge.

- If you reach a node with **no outgoing edge**, return that node (the endpoint).
- If following the next edge would take you to a node you've **already visited**, stop and return the
  **current node** (the last node before the repeated step).

```python
def find_endpoint(edges: list[list[int]], start: int) -> int
```

## Examples

```
edges = [[1,3],[7,3],[3,4],[4,6],[2,6],[6,9],[9,5]], start = 1   -> 5
```
`1 -> 3 -> 4 -> 6 -> 9 -> 5`, and `5` has no outgoing edge.

```
edges = [[0,1],[1,2],[2,0]], start = 0           -> 2     # 2 -> 0 would repeat 0
edges = [[0,1],[1,2],[2,3],[3,1]], start = 0     -> 3     # 3 -> 1 would repeat 1
```
A self-loop `[x, x]` starting at `x` returns `x`. A `start` with no outgoing edge returns `start`.

## Constraints

- `0 <= len(edges) <= 10^5`
- node ids are in `[0, 2·10^5]`
- each `u` appears as the source of at most one edge

## Notes on this version

Functional traversal, endpoint detection and "last node before a repeated cycle step" are from the original.
The interface and bounds were filled in. Long chains will break recursive solutions.
