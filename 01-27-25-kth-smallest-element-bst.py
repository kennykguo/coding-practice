# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []
        # Compute inorder traversal

        def inordertraversal(root):
            if root.left:
                inordertraversal(root.left);
            res.append(root.val);
            if root.right:
                inordertraversal(root.right);
        
        inordertraversal(root)
        print(res)
        return res[k-1]

