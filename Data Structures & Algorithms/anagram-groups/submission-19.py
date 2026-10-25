class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        
        final = {}

        for x in strs:
            cur = {}

            for ch in x:
                cur[ch] = cur.get(ch, 0) + 1
            
            key = str(sorted(cur.items()))
            if key not in final:
                final[key] = []
            final[key].append(x)
        
        # print(final)
        return [v for v in final.values()]
