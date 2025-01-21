class Solution:

    def encode(self, strs: List[str]) -> str:
        res  = ""
        for word in strs:
            res += str(len(word))
            res += '#'
            res += word
        
        return res

    def decode(self, s: str) -> List[str]:

        print(s)

        res = []

        l, r = 0,0

        while r < len(s):

            l = r

            while (s[r] != '#'):
                
                length = int(s[l:r+1])

                r += 1
            
            r += 1

            res.append(s[r:r+length])

            r += length

        return res
