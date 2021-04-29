# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepth_helper(root, 0)
        # without helper method:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def maxDepth_helper(self, root, maxDepth):
        if (not root):
            return maxDepth
        return max(self.maxDepth_helper(root.left, maxDepth+1), self.maxDepth_helper(root.right, maxDepth+1))
