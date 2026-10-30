class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        current = {}
        l = 0
        res = 0
        r = 0

        while r < len(s):
            
            current[s[r]] = current.get(s[r], 0) + 1 # add the current char

            # check if we're over capacity
            while current[s[r]] > 1:
                current[s[l]] = current[s[l]] - 1 # reduce that val to 1
                l+=1
            
            res = max(res, r - l + 1)
            r +=1
        
        return res

            

            