# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    ################################
    ########### METHOD 1 ###########
    ################################

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
        if (k <= count):
            return self.kthSmallest(root.left, k)
        elif (k > count+1):
            return self.kthSmallest(root.right, k - count - 1)
        else:
            return root.val

    ################################
    ########### METHOD 2 ###########
    ################################

    # def createArray(self, root, elements):
    #     if not root:
    #         return

    #     self.createArray(root.left, elements)
    #     elements.append(root.val)
    #     self.createArray(root.right, elements)

    # def kthSmallest(self, root, k):
    #     #inorder traversal
    #     elements = []
    #     self.createArray(root, elements)
    #     return elements[k-1]

    ################################
    ########### METHOD 3 ###########
    ################################

    # def recursive (self, root):
    #     if not root:
    #         return

    #     self.recursive(root.left)
    #     self.k = self.k - 1

    #     if self.k == 0:
    #         self.ans = root.val
    #         return

    #     self.recursive(root.right)

    # def kthSmallest(self, root, k):
    #     """
    #     :type root: TreeNode
    #     :type k: int
    #     :rtype: int
    #     """
    #     self.k = k
    #     self.ans = 0
    #     self.recursive(root)
    #     return self.ans

    ################################
    ########### METHOD 4 ###########
    ################################

    # def kthSmallest(self, root, k):
    #     stack = []
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left

    #         root = stack.pop()
    #         k = k - 1
    #         if k == 0:
    #             return root.val

    #         root = root.right
