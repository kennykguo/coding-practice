class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        
        def pacific(r, c, prev):
         
            if r < 0 or c < 0: # reach pacific
                return True

            if r  >= rows or c >= cols or heights[r][c] > prev or (r,c) in visited:
                return False

            visited.add((r,c))
            res = (pacific(r+1, c, heights[r][c]) or
                pacific(r-1, c, heights[r][c]) or 
                pacific(r, c+1, heights[r][c]) or 
                pacific(r, c-1, heights[r][c]))
            visited.remove((r,c))
            return res
        
        def atlantic(r, c, prev):
          
            if r >= rows or c >= cols: # reach atlantic
                return True

            if r < 0 or c < 0 or heights[r][c] > prev or (r,c) in visited:
                return False

            visited.add((r,c))
            res = (atlantic(r+1, c, heights[r][c]) or
                atlantic(r-1, c, heights[r][c]) or 
                atlantic(r, c+1, heights[r][c]) or 
                atlantic(r, c-1, heights[r][c]))
            visited.remove((r,c))
            return res
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific(i,j, float("infinity")) and atlantic(i,j, float("infinity")):
                    res.append([i,j])
        return res



        
            
