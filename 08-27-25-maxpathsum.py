# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-infinity')
        
        def dfs(root):

            if not root:
                return 0
            
            left = dfs(root.left) # left max sum
            right = dfs(root.right) # right max sum
            
            print(root.val)

            left = max(0, left) # if negative, don't take
            right = max(0, right) # if negative, don't take

            nonlocal res
            res = max(res, root.val + left + right)

            return max(root.val + left, root.val + right) # return max - only one branch

        dfs(root)

        return res

