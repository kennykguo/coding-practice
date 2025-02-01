# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left_max = max(dfs(root.left), 0) # Ignore the subtree if negative
            right_max = max(dfs(root.right), 0) # Ignore the subtree if negative

            res[0] = max(res[0], right_max + root.val + left_max) # Store max of current subtree

            return max(right_max, left_max) + root.val # Store the biggest branch, and add the current node's val, to return to upper recursion calls
        
        dfs(root)
        return res[0]
        

        