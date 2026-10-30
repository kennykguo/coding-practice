class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        current  = {}

        l = 0
        r = 0
        unique = 0
        res = 0
        total = 0

        while r < len(s):
            
            current[s[r]] = current.get(s[r], 0) + 1 # add 1
            total = max(current[s[r]], total) # maximum # of chars in our window
            print(s[r])

            while (r - l + 1) - total > k:
                print(total)
                print(current)
                current[s[l]] -= 1
                l+=1
            
            res = max(res, r - l + 1)
            r+= 1

        return res
