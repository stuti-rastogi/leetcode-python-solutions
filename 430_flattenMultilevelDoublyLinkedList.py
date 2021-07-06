"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        stack = []
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            else:
                if not curr.next and stack:
                    nextNode = stack.pop()
                    curr.next = nextNode
                    nextNode.prev = curr
            curr = curr.next
        return head
