# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append("N")
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            
        dfs(root)
        return ",".join(res)
        
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        print(data)
        data = data.split(",")
        i = 0

        def dfs():
            
            nonlocal i

            # empty
            if data[i] == "N":
                return None

            print(i)
            # create the node
            root = TreeNode(data[i])
            i+=1
            root.left = dfs()
            i+=1
            root.right = dfs()
            return root

        return dfs()