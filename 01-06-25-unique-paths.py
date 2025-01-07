class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # This is going to be the old row
        # m x n
        for i in range(m-1): # Over the corresponding rows
            newRow = [1] * n;
            for j in range(n-2, -1, -1): # Over all corresponding entries (except first)
                # Add from below, and to the right
                newRow[j] = newRow[j+1] + row[j]
            row = newRow; # Update the current row being checked
            # On the outside, we will have to 
    
        return row[0]