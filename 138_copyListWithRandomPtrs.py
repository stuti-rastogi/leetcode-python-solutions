"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        copies = collections.defaultdict(lambda: Node(0))
        copies[None] = None
        curr = head
        while curr:
            copies[curr].val = curr.val
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next
        return copies[head]

#         newHead = Node(head.val)
#         copies = {head: newHead}
        
#         curr = head.next
#         newCurr = newHead
#         while curr:
#             newNode = Node(curr.val)
#             copies[curr] = newNode
#             newCurr.next = newNode
            
#             newCurr = newCurr.next
#             curr = curr.next
            
#         newCurr = newHead
#         curr = head
#         while curr:
#             if curr.random:
#                 newCurr.random = copies[curr.random]
#             curr = curr.next
#             newCurr = newCurr.next
#         return newHead
