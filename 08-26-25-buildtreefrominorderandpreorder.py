# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def build(preorder, inorder):
            # find the first entry of preorder in inorder
            if not preorder or not inorder:
                return
            print(preorder)
            print(inorder)
            root_val = preorder[0]

            pivot = inorder.index(root_val)

            # create the node
            root = TreeNode(root_val)
            root.left = build(preorder[1:pivot+1], inorder[:pivot])
            root.right = build(preorder[pivot+1:], inorder[pivot+1:])
            return root
        
        return build(preorder, inorder)