class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        l, r = 0, len(heights) - 1

        while l <= r:

            current = min(heights[r], heights[l]) * (r - l)
            res = max(res, current)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        

        return res