"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        cur_nodes = {}


        def dfs(node):
            
            if not node:
                return
                
            if node in cur_nodes:
                return cur_nodes[node]
            
            # print(node.val)
            # if node == prev:
            #     return
            
            # Copy the current node
            new_node = Node(node.val, [])
            cur_nodes[node] = new_node

            # Traverse through all of its neighbours, add the nodes to a ref dictionary, and add it to the new node's neighbours
            for nei in node.neighbors:
                x = dfs(nei)
                new_node.neighbors.append(x)
            return new_node
        
        return dfs(node)