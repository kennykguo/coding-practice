class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        l, r = 0, len(heights) - 1

        res = 0

        while l<=r:
            area = min(heights[l], heights[r]) * (r - l)
            print(area)

            res = max(area, res)

            if heights[l] > heights[r]:
                r -= 1
            
            else:
                l+= 1

        
        return res



