class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check the rows
        for row in range(len(board)):  # looping over rows
            x = set()
            for entry in range(len(board[0])):
                if board[row][entry] != ".":
                    if board[row][entry] not in x:
                        x.add(board[row][entry])
                    else:
                        return False

        for col in range(len(board[0])):  # looping over cols
            x = set()
            for entry in range(len(board)):  # loop over rows [first idx]
                if board[entry][col] != ".":
                    if board[entry][col] not in x:
                        x.add(board[entry][col])
                    else:
                        return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # check a 3 x 3 grid
                x = set()
                for row in range(i, i + 3, 1):
                    for col in range(j, j + 3, 1):
                        if board[row][col] != ".":
                            if board[row][col] not in x:
                                x.add(board[row][col])
                            else:
                                return False

        return True
