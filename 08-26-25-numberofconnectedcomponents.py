class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        # adj = {i:[] for i in range(n)}
        # for n1, n2 in edges:
        #     if n1 > n2:
        #         adj[n1].append(n2)
        #     else:
        #         adj[n2].append(n1)


        # finds the deepest parent
        def find(n):
            while n != par[n]:
                n = par[n]
            return n


        # connects two edges together
        def union(n1, n2):
            par1 = find(n1)
            par2 = find(n2)
            if par1 == par2: # same parent, don't need to subtract
                return 0
            else: # diff parent, subtract
                # parent is always the smaller node for convention
                if par1 < par2:
                    par[par2] = par1
                else:
                    par[par1] = par2
                return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        print(par)

        return res
            