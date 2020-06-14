# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxVal = -sys.maxsize - 1

        def maxPathVal(node: TreeNode) -> int:
            # no contribution to path
            if not node:
                return 0

            # if a node is negative we don't want to consider it
            # take 0 instead
            leftMax = max(maxPathVal(node.left), 0)
            rightMax = max(maxPathVal(node.right), 0)

            # this is a potential path with node included
            newVal = node.val + leftMax + rightMax
            self.maxVal = max(newVal, self.maxVal)

            # to include node in a path, we can't choose both left & right
            # that would be branching!
            # so pick the max of the two children and carry that for path upwards
            return node.val + max(leftMax, rightMax)

        maxPathVal(root)
        return self.maxVal
