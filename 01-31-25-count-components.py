class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each node is initially a parent of itself
        par = [i for i in range(n)]
        count = n

        def find(n1):
            cur = par[n1] # Current parent of the node
            while cur != par[cur]: # While node is not a parent of itself
                cur = par[cur]
            return cur
        
        def union(n1, n2): # Connect two components
            par1, par2 = find(n1), find(n2)
            par[par1] = par2

        for e1, e2 in edges:
            if find(e1) != find(e2):
                print(find(e1), find(e2))
                union(e1, e2)
                print(par)
                count -=1
        
        return count
