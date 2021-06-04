# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        heights = {}
        self.getHeight(root, heights)

        heights = {key:val for key,val in sorted(heights.items(), key = lambda x: x[0])}

        allLeaves = []
        for height in heights:
            allLeaves.append(heights[height])
        return allLeaves

    def getHeight(self, root, heights) -> int:
        if not root:
            return -1

        leftHeight = self.getHeight(root.left, heights)
        rightHeight = self.getHeight(root.right, heights)

        currHeight = max(leftHeight, rightHeight) + 1

        if currHeight in heights:
            heights[currHeight].append(root.val)
        else:
            heights[currHeight] = [root.val]
        return currHeight





#     def findLeaves(self, root: TreeNode) -> List[List[int]]:
#         all_leaves = []
#         while True:
#             leaves = []
#             if not self.deleteLeaves(root, None, leaves):
#                 all_leaves.append(leaves)
#                 break
#             all_leaves.append(leaves)
#         return all_leaves

#     def deleteLeaves(self, root, parent, leaves):
#         if not root.left and not root.right:
#             # this is a leaf
#             leaves.append(root.val)
#             if parent and parent.right == root:
#                 parent.right = None
#             elif parent and parent.left == root:
#                 parent.left = None
#             else:
#                 return False
#         else:
#             # has at least one child
#             if root.left:
#                 self.deleteLeaves(root.left, root, leaves)
#             if root.right:
#                 self.deleteLeaves(root.right, root, leaves)
#         return True