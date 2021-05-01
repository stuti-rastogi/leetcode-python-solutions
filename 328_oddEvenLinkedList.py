# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        evenHead = head.next
        odd = head
        even = evenHead
        current = head.next.next

        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head

        # more complicated, but accepted
        # if not head:
        #     return None
        # tail = head
        # n = 1
        # while tail.next:
        #     tail = tail.next
        #     n = n + 1
        # curr = head
        # i = 0
        # if n > 2:
        #     while (i < n-1):
        #         evenNode = curr.next
        #         curr.next = evenNode.next
        #         tail.next = evenNode
        #         tail = tail.next
        #         i += 2
        #         curr = curr.next
        #     tail.next = None
        # return head