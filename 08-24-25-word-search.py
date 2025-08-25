class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, idx):
            
            # word found, return true
            if idx >= len(word):
                return True

            # boundary check
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited:
                return False

            # character not equal
            if board[r][c] != word[idx]:
                return False
            
            # found char, now search in all directions
            visited.add((r, c))
            return_val = dfs(r+1, c, idx + 1) or dfs(r-1, c, idx + 1) or dfs(r, c+1, idx + 1) or dfs(r, c-1, idx + 1)
            visited.remove((r,c))
            return return_val

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False
            