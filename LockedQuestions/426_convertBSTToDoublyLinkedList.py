"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        head = None
        tail = None

        def treeToDoublyListHelper(node):
            nonlocal head, tail
            if not node:
                return
            treeToDoublyListHelper(node.left)
            if tail:
                node.left = tail
                tail.right = node
            else:
                head = node
            tail = node
            treeToDoublyListHelper(node.right)

        treeToDoublyListHelper(root)
        head.left = tail
        tail.right = head
        return head
