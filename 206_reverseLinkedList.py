# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if (not head):
        #     return None
        # prev = None
        # curr = head
        # ahead = curr.next
        # while (curr):
        #     curr.next = prev
        #     prev = curr
        #     curr = ahead
        #     if (ahead):
        #         ahead = ahead.next
        
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev