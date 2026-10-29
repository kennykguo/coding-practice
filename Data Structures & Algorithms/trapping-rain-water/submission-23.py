class Solution:
    def trap(self, height: List[int]) -> int:
        
        # min (height[i-1], height[i+1]) is the amount of water that can be trapped there

        # find tallest bars l,r in o(n)
        res = 0
        l, r = 0, len(height)-1
        heightl_max = height[l]
        heightr_max = height[r]
        while l <= r:
            # when i move l or r, i need to find that max value of l and r, then subtract the height at that point, that's how much water is there


            # hmm, would recommend moving in the direction that is lower
            # if left height is lower than the right height, i want to move that ptr, same goes for right height
            if height[l] < height[r]:
                res += max(min(heightl_max, heightr_max) - height[l], 0)
                l+=1
                heightl_max = max(heightl_max, height[l])

            else:
                res += max(min(heightl_max, heightr_max) - height[r], 0)
                r-=1
                heightr_max = max(heightr_max, height[r])
        
        return res