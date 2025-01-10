# DID NOT SOLVE
# Need to get correct indices
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                # Save the top-left value temporarily
                top_left = matrix[l][l + i]

                # Move bottom-left to top-left
                matrix[l][l + i] = matrix[r - i][l]

                # Move bottom-right to bottom-left
                matrix[r - i][l] = matrix[r][r - i]

                # Move top-right to bottom-right
                matrix[r][r - i] = matrix[l + i][r]

                # Move saved top-left to top-right
                matrix[l + i][r] = top_left

            l += 1
            r -= 1
