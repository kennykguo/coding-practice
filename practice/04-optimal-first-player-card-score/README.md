# 04 · Optimal First-Player Card Score

You're given an even-length array `cards` of positive integers laid out in a row. Two players can see every
card and both play optimally (each maximizes their own total).

Player 1 moves first. On each turn the current player removes either the **leftmost** or the **rightmost**
remaining card and adds its value to their score. Players alternate until no cards remain.

Return **Player 1's final score** (the absolute score, not the difference and not who wins).

```python
def first_player_score(cards: list[int]) -> int
```

## Examples

```
cards = [1, 9, 10, 5, 6, 4]   -> 18
cards = [5, 3]                -> 5
cards = [2, 2, 2, 2]          -> 4
```

## Constraints

- `2 <= len(cards) <= 1000`, `len(cards)` is even
- `1 <= cards[i] <= 10^9`

## Notes on this version

Essentially the original problem; only the bounds were chosen for this practice set.
