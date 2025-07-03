class Solution:
    def trap(self, height: List[int]) -> int:

        # prefix arrays

        # placed before
        prefix = [0] * len(height)
        
        # placed after
        suffix = [0] * len(height)

        res = [0] * len(height)

        l = 0
        cur_max = 0
        while l < len(height):
            if l == 0:
                prefix[l] = height[l]
                cur_max = height[l]
                l = l + 1
                continue
            cur_max = max(cur_max, height[l])
            prefix[l] = cur_max  
            l = l + 1

        
        r = len(height) - 1
        cur_max = 0
        while r >= 0:
            if r == len(height) - 1:
                suffix[r] = height[r]
                cur_max = height[r]
                r = r - 1
                continue
            cur_max = max(cur_max, height[r])   
            suffix[r] = cur_max
            r = r - 1
        

        for i in range(len(height)):
            res[i] = min(prefix[i], suffix[i]) - height[i]
            if res[i] < 0:
                res[i] = 0
        
        print(prefix)
        print(suffix)
        print(res)

        return sum(res)

                