# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        sum_so_far = root.val

        def dfs(node, sum_so_far):
            if not node.right and not node.left:
                return True if sum_so_far == targetSum else False
            if node.left:
                sum_so_far += node.left.val
                if dfs(node.left, sum_so_far):
                    return True
                sum_so_far -= node.left.val
            if node.right:
                sum_so_far += node.right.val
                if dfs(node.right, sum_so_far):
                    return True
                sum_so_far -= node.right.val
            return False

        return dfs(root, sum_so_far)
