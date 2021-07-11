# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n in Solution.memo:
            return self.memo[n]
        trees = []
        remainingNum = n - 1
        for i in range(1, remainingNum, 2):
            subTrees = self.allPossibleFBT(i)
            remainingSubTrees = self.allPossibleFBT(remainingNum-i)
            for tree in subTrees:
                for otherTree in remainingSubTrees:
                    root = TreeNode(0)
                    root.left = tree
                    root.right = otherTree
                    trees.append(root)

        Solution.memo[n] = trees

        return Solution.memo[n]
