class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()
        pacific_visited = set()
        atlantic_visited = set()
        rows = len(heights)
        cols = len(heights[0])

        def bfs(cur_set, visited_set, r, c, prev):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited_set or heights[r][c] < prev:
                # print(r,c, "x")
                return
                
            cur_set.add((r,c))
            visited_set.add((r,c))
            
            bfs(cur_set, visited_set, r + 1, c, heights[r][c])
            bfs(cur_set, visited_set, r - 1, c, heights[r][c])
            bfs(cur_set, visited_set, r, c + 1, heights[r][c])
            bfs(cur_set, visited_set, r, c - 1, heights[r][c])


        # WRONG ITERATION indices. DO again
        for i in range(cols):
            bfs(pacific, pacific_visited, 0, i, -1)
        for i in range(rows):
            bfs(pacific, pacific_visited, i, 0, -1)
        for i in range(cols):
            bfs(atlantic, atlantic_visited, rows - 1, i, -1)
        for i in range(rows):
            bfs(atlantic, atlantic_visited, i, cols - 1, -1)
        
        return list(pacific & atlantic)

        
