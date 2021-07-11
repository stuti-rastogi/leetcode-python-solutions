# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        serialization = '*'.join(map(str, preorder(root)))
        return serialization


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = [int(s) for s in data.split('*') if s]

        def constructBST(maxVal):
            if not vals or vals[0] > maxVal:
                return None
            val = vals.pop(0)
            root = TreeNode(val)
            root.left = constructBST(val)
            root.right = constructBST(maxVal)
            return root

        return constructBST(float('inf'))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
