# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        if not root:
            return paths

        sum_so_far = root.val
        path = [root.val]

        def dfs(node, sum_so_far, path):
            if not node.right and not node.left and sum_so_far == targetSum:
                paths.append(path[:])
                return
            if node.left:
                sum_so_far += node.left.val
                path.append(node.left.val)
                dfs(node.left, sum_so_far, path)
                sum_so_far -= node.left.val
                path.pop()
            if node.right:
                sum_so_far += node.right.val
                path.append(node.right.val)
                dfs(node.right, sum_so_far, path)
                sum_so_far -= node.right.val
                path.pop()

        dfs(root, sum_so_far, path)
        return paths