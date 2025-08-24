class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        matching = {}
        for char in t:
            matching[char] = matching.get(char, 0) + 1
        n = len(matching)

        current = {}
        count = 0
        shortest = float("infinity")
        res = ""
        l = 0
        r = 0

        while r < len(s):

            print(current)

            # get a sub window by incrementing r
            current[s[r]] = current.get(s[r], 0) + 1

            # get a matching window
            if s[r] in matching and current[s[r]] == matching[s[r]]:
                count += 1
            
            while count == n: # matching substring
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    res = s[l:r + 1]

                current[s[l]] -= 1
                if s[l] in matching and current[s[l]] < matching[s[l]]:
                    count -= 1

                l += 1

            r += 1
        return res
                        

                    
                   

                


            
