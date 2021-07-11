# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        idx = 0
        n = len(preorder)

        def helper(maxValue):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]
            if val > maxValue:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = helper(val)
            root.right = helper(maxValue)
            return root

        return helper(float('inf'))

        # if not preorder:
        #     return None
        # rootVal = preorder[0]
        # root = TreeNode(rootVal)
        # if len(preorder) == 1:
        #     return root
        # index = bisect.bisect_left(preorder[1:], preorder[0])
        # root.left = self.bstFromPreorder(preorder[1:index+1])
        # root.right = self.bstFromPreorder(preorder[index+1:])
        # return root
