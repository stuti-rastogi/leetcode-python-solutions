# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # def findNext(self, curr):
    #     if (not curr):
    #         return
    #     if (curr.next == None):
    #         if (curr.left):
    #             curr.left.next = curr.right
    #         if (curr.right):
    #             curr.right.next = None
    #     else:
    #         if (curr.left):
    #             curr.left.next = curr.right
    #         if (curr.right):
    #             curr.right.next = curr.next.left
    #     self.findNext(curr.left)
    #     self.findNext(curr.right)
    #     return
    
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # if not root:
        #     return None
        # root.next = None
        # self.findNext(root)
        
        if not root: 
            return None
        while root and root.left:
            nex = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = nex
        
    