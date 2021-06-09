# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversalRec(self, root, row, col, columns):
        if not root:
            return

        columns[col].append((row, root.val))
        self.verticalTraversalRec(root.left, row+1, col-1, columns)
        self.verticalTraversalRec(root.right, row+1, col+1, columns)


    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        columns = collections.defaultdict(list)

        if not root:
            return []

        self.verticalTraversalRec(root, 0, 0, columns)

        # sort by column first, and then sort each column
        verticalOrder = []
        for col in sorted(columns):
            nodes = sorted(columns[col])
            verticalOrder.append([node[1] for node in nodes])
        return verticalOrder


    # O(nlgn) solution
    # def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    #     # list of nodes - (col, row, value)
    #     nodes = []
    #     if not root:
    #         return []

    #     def BFS(root):
    #         queue = collections.deque([(root, 0, 0)])
    #         while queue:
    #             node, row, col = queue.popleft()
    #             if node:
    #                 nodes.append((col, row, node.val))
    #                 queue.append((node.left, row+1, col-1))
    #                 queue.append((node.right, row+1, col+1))

    #     BFS(root)
    #     nodes.sort()

    #     columns = collections.OrderedDict()
    #     for col, row, val in nodes:
    #         if col in columns:
    #             columns[col].append(val)
    #         else:
    #             columns[col] = [val]

    #     return list(columns.values())
