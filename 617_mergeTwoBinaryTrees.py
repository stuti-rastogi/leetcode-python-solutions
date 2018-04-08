class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (not t1 and not t2):
            return None
        
        if (not t1):
            return t2
        
        if (not t2):
            return t1
        
        root1 = t1.val
        root2 = t2.val
        
        result = TreeNode(root1 + root2)
        result.left = self.mergeTrees(t1.left, t2.left)
        result.right = self.mergeTrees(t1.right, t2.right)
        
        return result