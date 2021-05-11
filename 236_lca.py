# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse tree using DFS and keep track of parents
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop()
            if not node:
                continue
            parent[node.left] = node
            stack.append(node.left)
            parent[node.right] = node
            stack.append(node.right)

        # Now find ancestors of p and store in a set
        ancestorsP = set()
        while p:
            ancestorsP.add(p)
            p = parent[p]

        # now keep traversing up ancestors of q till first one appears in p
        while q not in ancestorsP:
            q = parent[q]
            
        return q


#         path_p = self.findPath(root, p, [root])[0]
#         path_q = self.findPath(root, q, [root])[0]
#         p_it = 0
#         q_it = 0
#         minLen = min(len(path_p), len(path_q))
#         while p_it < minLen:
#             if path_p[p_it].val != path_q[q_it].val:
#                 return path_p[p_it-1]
#             p_it += 1
#             q_it += 1
#         return path_p[p_it-1]

#     def findPath(self, root, node, path):
#         if root == node:
#             return path, True
#         children = [root.left, root.right]
#         for child in children:
#             if child:
#                 path.append(child)
#                 if self.findPath(child, node, path)[1]:
#                     return path, True
#                 path.pop()
#         return path, False


# if __name__ == "__main__":
#     t0 = TreeNode(0)
#     t1 = TreeNode(1)
#     t2 = TreeNode(2)
#     t3 = TreeNode(3)
#     t4 = TreeNode(4)
#     t5 = TreeNode(5)
#     t6 = TreeNode(6)
#     t7 = TreeNode(7)
#     t8 = TreeNode(8)

#     t7.left = t7.right = None
#     t4.left = t4.right = None
#     t6.left = t6.right = None
#     t0.left = t0.right = None
#     t8.left = t8.right = None

#     t2.left = t7
#     t2.right = t4

#     t5.left = t6
#     t5.right = t2

#     t1.left = t0
#     t1.right = t8

#     t3.left = t5
#     t3.right = t1
