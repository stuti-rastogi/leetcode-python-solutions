# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        while root.left:
            root = root.left
            depth += 1
        return depth

    def nodeExists(self, index: int, depth: int, root: TreeNode) -> bool:
        left = 0
        right = 2**depth - 1
        for _ in range(depth):
            mid = (left + right) // 2
            if index <= mid:
                root = root.left
                right = mid
            else:
                root = root.right
                left = mid+1
        return root is not None


    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = self.calculateDepth(root)
        if depth == 0:
            return 1

        internalNodes = 2**depth - 1
        low = 0
        high = 2**depth - 1

        while low <= high:
            mid = (low + high) // 2
            if self.nodeExists(mid, depth, root):
                low = mid + 1
            else:
                high = mid - 1

        return internalNodes + low



    # def countNodes(self, root: TreeNode) -> int:
    #     return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0