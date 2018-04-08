# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [root] 
        ans = 0
        
        while any(queue):
            ans = queue[0].val
            queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
        return ans