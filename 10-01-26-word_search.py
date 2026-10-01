class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, current, idx):
            if current == word:
                return True

            visited.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                rchr = r + dr
                cchr = c + dc

                if (
                    rchr >= 0
                    and rchr < rows
                    and cchr >= 0
                    and cchr < cols
                    and (rchr, cchr) not in visited
                    and board[rchr][cchr] == word[idx]
                ):
                    if dfs(rchr, cchr, current + board[rchr][cchr], idx + 1):
                        return True

            visited.remove((r, c))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, board[i][j], 1):
                        return True

        return False
