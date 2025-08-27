"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        node_to_copy = {}

        def dfs(cur):
            
            if cur in node_to_copy:
                return
            
            
            # clone current node
            new_node = Node(cur.val, []) # no neighbours
            node_to_copy[cur] = new_node # add to dict

            # clone neighbours
            for nei in cur.neighbors: # old copy
                dfs(nei)
                node_to_copy[cur].neighbors.append(node_to_copy[nei])
        
        if not node:
            return None
        dfs(node)
        print(node_to_copy)
        return node_to_copy[node]
        


            

            

            