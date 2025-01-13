class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        print(rows)
        print(cols)

        for row in rows:
            # Zero out the row
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        

        for col in cols:
            # Zero out the row
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
