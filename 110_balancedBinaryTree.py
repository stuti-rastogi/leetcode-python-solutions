from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkHeightBalanced(self, root: TreeNode) -> Tuple[int, bool]:
        if not root:
            return (0, True)
        r_height, r_balanced = self.checkHeightBalanced(root.right)
        l_height, l_balanced = self.checkHeightBalanced(root.left)

        if not r_balanced or not l_balanced:
            return (0, False)

        return (max(r_height, l_height) + 1, abs(r_height-l_height) <= 1)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.checkHeightBalanced(root)[1]
