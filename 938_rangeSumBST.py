class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low or root.val > high:
            currSum = 0
        else:
            currSum = root.val
        if root.val > low:
            currSum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            currSum += self.rangeSumBST(root.right, low, high)
        return currSum
