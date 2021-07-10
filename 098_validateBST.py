# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBSTHelper(self, root: TreeNode, minValue: int, maxValue: int) -> bool:
        if not root:
            return True
        if root.val <= minValue or root.val >= maxValue:
            return False
        return (self.isValidBSTHelper(root.left, minValue, min(maxValue, root.val))
                and self.isValidBSTHelper(root.right, max(minValue, root.val), maxValue))

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
