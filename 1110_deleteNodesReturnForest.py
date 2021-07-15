# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

LEFT = 0
RIGHT = 1

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res


#         stack = [root]
#         parent_nodes = {root: (None, -1)}
#         val_nodes = {}

#         while (stack):
#             curr_node = stack.pop()
#             val_nodes[curr_node.val] = curr_node
#             if curr_node.left:
#                 parent_nodes[curr_node.left] = (curr_node, LEFT)
#                 stack.append(curr_node.left)
#             if curr_node.right:
#                 parent_nodes[curr_node.right] = (curr_node, RIGHT)
#                 stack.append(curr_node.right)

#         forest = []
#         for val in to_delete:
#             del_node = val_nodes[val]
#             parent_node, is_right = parent_nodes[del_node]
#             if parent_node:
#                 if is_right:
#                     parent_node.right = None
#                 else:
#                     parent_node.left = None
#             else:
#                 parent_nodes.pop(del_node)

#             if del_node.left:
#                 parent_nodes[del_node.left] = (None, -1)
#             if del_node.right:
#                 parent_nodes[del_node.right] = (None, -1)

#         for node in parent_nodes:
#             if not parent_nodes[node][0]:
#                 forest.append(node)

#         return forest
