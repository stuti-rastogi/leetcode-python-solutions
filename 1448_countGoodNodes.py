# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count_good_nodes = 0
        if not root:
            return count_good_nodes
        curr_max_val = float('-inf')
        values = [curr_max_val, count_good_nodes]
        self.goodNodesRec(root, values)
        return values[1]

    def goodNodesRec(self, root, values):
        original_max_val = values[0]
        if root.val >= values[0]:
            values[1] += 1
            values[0] = max(values[0], root.val)
        if root.left:
            self.goodNodesRec(root.left, values)
        if root.right:
            self.goodNodesRec(root.right, values)
        values[0] = original_max_val