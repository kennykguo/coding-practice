class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            

            # out of bounds, or not part of the island
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return

            print(r,c)
            grid[r][c] = "0" # visit by setting it to zero
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)
            return
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1": # 1
                    bfs(i,j) 
                    res +=1
        
        
        return res

