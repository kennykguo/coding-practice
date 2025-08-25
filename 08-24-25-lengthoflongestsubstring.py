class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        current = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            
            # check if the current char exists already
            while s[r] in current:
                current.remove(s[l])
                l += 1
            
            
            current.add(s[r]) # add the current char

            res = max(res, r - l + 1)
            r += 1
        
        return res

            
            