class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur_path = set()
        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(r, c, cur_word):
            print(cur_word)
            # Success
            if cur_word == word:
                return True

            # Invalid case
            if r < 0 or r>= num_rows or c < 0 or  c >= num_cols or (r,c) in cur_path:
                return False
            
            # Add to the path
            cur_path.add((r,c))

            # Recursively go through all cases
            if (dfs(r + 1, c, cur_word + board[r][c]) 
            or dfs(r - 1, c, cur_word + board[r][c]) 
            or dfs(r, c + 1, cur_word + board[r][c])
            or dfs(r , c - 1, cur_word + board[r][c])):
                return True

            # Backtrack
            cur_path.remove((r,c))
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, ""):
                    return True
        return False
