# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sametree(root, subroot):
            # both missing
            if not root and not subroot:
                return True

            # both exist, and same val
            if root and subroot and root.val == subroot.val:
                return sametree(root.left, subroot.left) and sametree(root.right, subroot.right)
            return False

        def issubtree(root, subroot):
            if not root:
                return False
            
            if sametree(root, subroot):
                return True
            
            return issubtree(root.left, subroot) or issubtree(root.right, subroot)
        
        return issubtree(root, subRoot)
            