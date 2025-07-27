# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursively check each
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        # reminder that we only check for nodes with a value greater than the value of node x

        def dfs(root, max_seen, path):

            # root dne
            if not root:
                return

            print(root.val)

            # check if the current value is greater or equal to the current root value
            if max_seen <= root.val:
                max_seen = root.val
                print("greater", root.val)
                path = True
            else:
                path = False
            
            if path:
                nonlocal res
                res += 1
            
            
            dfs(root.left, max_seen, path)
            dfs(root.right, max_seen, path)
            return
        
        dfs(root, root.val, True)
        return res
            

            


            
            
