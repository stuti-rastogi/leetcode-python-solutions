# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # even - L to R
        # odd - R to L
        
        if (not root):
            return []
        level = 0
        currstack = [root]
        result = []
        nextstack = []
        currlist = []
        
        while(currstack):
            while (currstack):
                node = currstack.pop()
                if (node):
                    currlist.append(node.val)
                    if (level == 0):
                        nextstack.append(node.left)
                        nextstack.append(node.right)
                    if (level == 1):
                        nextstack.append(node.right)
                        nextstack.append(node.left)
            result.append(currlist)
            level = (level + 1) % 2 
            currstack = nextstack
            nextstack = []
            currlist = []
        
        return result[:-1]