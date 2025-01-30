class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            # Check bounding counditions
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
                return False
            
            if grid[r][c] == "0":
                return False
            
            grid[r][c] = "0"

            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)
            return True
        

        res = 0

        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res += 1
        
        return res

            