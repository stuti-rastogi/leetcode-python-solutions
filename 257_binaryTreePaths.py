# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        ans = []
        curr = str(root.val)
        checkLeft = self.binaryTreePaths(root.left)
        checkRight = self.binaryTreePaths(root.right)
        if (checkLeft):
            for x in checkLeft:
                toAdd = curr + "->" + x
                ans.append(toAdd)
            
        if (checkRight):
            for x in checkRight:
                toAdd = curr + "->" + x
                ans.append(toAdd)
        
        # no children, this is leaf
        if (not checkLeft and not checkRight):
            ans.append(curr)
            
        return ans