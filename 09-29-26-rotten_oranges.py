from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        duplicates = set()
        res = -1

        # initial set
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:  # rotten
                    q.append((i, j))
                    duplicates.add((i, j))

        # num of non-rotten
        non_rotten = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    non_rotten += 1

        if len(q) == 0:
            if non_rotten == 0:
                return 0
            else:
                return -1

        while q:
            for _ in range(len(q)):
                (r, c) = q.popleft()

                # infect
                for del_r in range(-1, 2, 2):
                    # new values
                    cur_r = r + del_r
                    cur_c = c

                    # in bounds
                    if cur_r < rows and cur_r >= 0:
                        # check no duplicates
                        if (cur_r, cur_c) not in duplicates and grid[cur_r][cur_c] == 1:
                            grid[cur_r][cur_c] = 2  # infect
                            q.append((cur_r, cur_c))  # add to queue
                            duplicates.add((cur_r, cur_c))  # add to duplicates to avoid cycles

                for del_c in range(-1, 2, 2):
                    # new values
                    cur_r = r
                    cur_c = c + del_c

                    # in bounds
                    if cur_c < cols and cur_c >= 0:
                        # check no duplicates
                        if (cur_r, cur_c) not in duplicates and grid[cur_r][cur_c] == 1:
                            grid[cur_r][cur_c] = 2  # infect
                            q.append((cur_r, cur_c))  # add to queue
                            duplicates.add((cur_r, cur_c))  # add to duplicates to avoid cycles
            res += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # fresh
                    return -1

        return res
