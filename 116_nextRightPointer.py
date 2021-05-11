# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr:
            # since perfect binary tree
            if not curr.left:
                return root
            node = curr
            child = None
            while node:
                if child:
                    child.next = node.left
                child = node.left.next = node.right
                node = node.next
            curr = curr.left


#         if not root:
#             return None
#         currLevel = [root]
#         while (currLevel):
#             nextLevel = []
#             levelSize = len(currLevel)
#             for i in range(levelSize):
#                 if i == levelSize-1:
#                     currLevel[i].next = None
#                 else:
#                     currLevel[i].next = currLevel[i+1]
#                 if currLevel[i].left:
#                     nextLevel.append(currLevel[i].left)
#                 if currLevel[i].right:
#                     nextLevel.append(currLevel[i].right)
#             currLevel = nextLevel
#         return root