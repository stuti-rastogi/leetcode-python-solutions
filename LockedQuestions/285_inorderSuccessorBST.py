# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def treeMinimum(self, root):
        """
            Find the minimum value in the tree rooted at root
        """
        # minimum is the left-most child
        while (root.left):
            root = root.left
        return root


    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # if node has a right child, successor is the minimum in the right subtree
        if p.right:
            return self.treeMinimum(p.right)
        else:
            # keep going up the parents till we reach the first ancestor for which
            # p is in the left subtree
            node = root
            candidate = None
            while node != p:
                if p.val < node.val:
                    candidate = node
                    node = node.left
                else:
                    node = node.right
            return candidate
