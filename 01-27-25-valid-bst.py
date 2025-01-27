# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTHelper(root, max, min):
            if not root:
                return True
            
            if root.val <= min:
                return False
            
            if root.val >= max:
                return False
            
            return isValidBSTHelper(root.left, root.val, min) and isValidBSTHelper(root.right, max, root.val)
        
        return isValidBSTHelper(root, float('infinity'), -1 * float('infinity'))
                