class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:            
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, par):

            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei != par:
                    if not dfs(nei, node):
                        return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n

                
