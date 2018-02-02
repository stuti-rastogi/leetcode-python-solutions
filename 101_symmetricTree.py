# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkMirror(root, root)
        
    def checkMirror(self, tree1, tree2):
        if (not tree1 and not tree2):
            return True
        
        if (not tree1 or not tree2):
            return False
        
        if (tree1 and tree2):
            return ((tree1.val == tree2.val) and self.checkMirror(tree1.left, tree2.right) and self.checkMirror(tree1.right,                        tree2.left))
        
        return False