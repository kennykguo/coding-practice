from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))  # visit current entry

            # loop through 4 possibilities
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # within bounds, and an actual 1
                if (
                    0 <= r + dr < rows
                    and 0 <= c + dc < cols
                    and grid[r + dr][c + dc] == "1"
                ):
                    bfs(r + dr, c + dc)

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1

        return res
