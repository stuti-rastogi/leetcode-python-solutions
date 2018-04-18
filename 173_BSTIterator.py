# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        
        return False
        
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        tempRoot = node.right
        
        while tempRoot:
            self.stack.append(tempRoot)
            tempRoot = tempRoot.left
        
        return node.val

###### My solution ######

#     def populate (self, root):
#         while (root):
#             self.stack.append(root)
#             root = root.left

#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.stack = []
#         self.populate(root)
    
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         if (self.stack):
#             return True
#         return False
        

#     def next(self):
#         """
#         :rtype: int
#         """
#         ans = self.stack.pop()
#         self.populate(ans.right)
#         return ans.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())