# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            if not root1 and not root2: # Both dne
                return True
            if not root1 and root2: # Left dne
                return False
            if root1 and not root2: # Right dne
                return False
            # Both exist, recursive
            if root1.val != root2.val:
                return False
            
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        
        q = deque([root])

        while q:
            # Pop the current node from the left
            node = q.popleft()

            if not node:
                continue
            
            # Add the left and right nodes
            q.append(node.left)
            q.append(node.right)
            
            if isSameTree(node, subRoot):
                return True
        
        return False


