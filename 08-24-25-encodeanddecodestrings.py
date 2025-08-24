class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

        
    def decode(self, s: str) -> List[str]:
        
        l, r = 0, 0
        res = []
        print(s)

        while r < len(s):
            
            # get the number
            while s[r] != "#":
                r += 1
            
            # slice total
            print(l)
            print(r)
            length = int(s[l:r])

            r += 1 # move past hashtag

            res.append(s[r:r+length])
            r = r + length
            l = r
        
        return res
            
            