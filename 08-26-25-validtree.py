class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()

        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)
        
        def dfs(node, prev):

            # check if we visited the node (cycle detected)
            if node in visited:
                return False
            
            # visit the node
            visited.add(node)

            # visit its neighbours recursively
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        res = dfs(0, None)

        print(visited)
        print(res)

        return res and len(visited) == n

