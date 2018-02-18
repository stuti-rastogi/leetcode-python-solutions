# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def createArray(self, root, elements):
        if not root:
            return
        
        self.createArray(root.left, elements)
        elements.append(root.val)
        self.createArray(root.right, elements)
        
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        
        count = self.countNodes(root.left)
        # print (root.val)
        # print ("Count: " + str(count))
        if (k <= count):
            return self.kthSmallest(root.left, k)
        elif (k > count+1):
            return self.kthSmallest(root.right, k - count - 1)
        else:
            return root.val
        # #inorder traversal
        # elements = []
        # self.createArray(root, elements)
        # return elements[k-1]