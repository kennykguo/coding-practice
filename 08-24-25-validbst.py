class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        # all entries on left should be smaller
        # all entries on right should be bigger
        def dfs(root, max_left, min_right):
            
            if not root:
                return True

            if not min_right < root.val < max_left:
                return False
            
            # left, right
            return dfs(root.right, max_left, root.val) and dfs(root.left, root.val, min_right)
        
        return dfs(root, float("infinity"), float("-infinity"))