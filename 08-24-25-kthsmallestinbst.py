# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque()
        node = root
        
        while q or node:

            while node:
                q.append(node)
                node = node.left
            
            # pop an element and visit
            node = q.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right
        
        return -1
                

            

            
