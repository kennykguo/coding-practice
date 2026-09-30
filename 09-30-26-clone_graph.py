"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        cur_to_node = {}

        def dfs(node):  # pass in original graph node
            # if we alr found this node from the original graph, then skip it
            if node in cur_to_node:
                return cur_to_node[node]  # return the new node

            else:  # not existing, create the new node for the new graph
                new_node = Node(node.val)
                cur_to_node[node] = new_node  # map original node to new node

            # explore the current node, and add its neighbours
            for nei in node.neighbors:  # traverse through original node's neighbours
                if nei not in cur_to_node:
                    dfs(nei)
                new_node.neighbors.append(cur_to_node[nei])

        if not node:
            return None
        dfs(node)
        return cur_to_node[node]
