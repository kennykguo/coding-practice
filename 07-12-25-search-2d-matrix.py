class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # run binary search in both directions


        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid_vertical = (top + bottom ) // 2
            l, r = 0, len(matrix[0]) - 1
            while l <= r: 
                mid = (l + r) // 2
                if target == matrix[mid_vertical][mid]:
                    return True
                elif target > matrix[mid_vertical][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(matrix[0]):
                top = mid_vertical + 1
            else:
                bottom = mid_vertical - 1
        
        return False
