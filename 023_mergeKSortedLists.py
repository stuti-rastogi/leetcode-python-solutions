import queue
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        point = ListNode(0)
        head = point
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        
        for x in sorted(vals):
            point.next = ListNode(x)
            point = point.next
        
        return head.next