import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root, heights=[]):
        self.seen = collections.defaultdict(int)
        self.repeated_nodes = []
        self.__dfs(root)
        return self.repeated_nodes

    def __dfs(self, node):
        if not node:
            return "None"
        else:
            left = self.__dfs(node.left)
            right = self.__dfs(node.right)
            cur = str(node.val) + '-' + left + '-'+ right
            self.seen[cur] += 1
            if self.seen[cur] == 2:
                self.repeated_nodes.append(node)
            return cur
