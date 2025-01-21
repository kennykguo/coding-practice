class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        
        return res


    def decode(self, s: str) -> List[str]:
        print(s)

        res = []

        l, r = 0, 0

        if s == "#0":
            return [""]
        
        while r < len(s):
            l = r
            while s[r] != '#':
                r += 1
            print(s[l:r])
            length = int(s[l:r])
            r+= 1
            res.append(s[r:r+length])
            r += length
        
        return res

