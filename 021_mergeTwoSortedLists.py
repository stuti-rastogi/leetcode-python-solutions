# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## RECURSIVE ##
        # if (not l1):
        #     return l2
        # if (not l2):
        #     return l1
        # while (l1 and l2):
        #     if (l1.val < l2.val):
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #         return l1
        #     else:
        #         l2.next = self.mergeTwoLists(l1, l2.next)
        #         return l2

        ## ITERATIVE ##
        # dummy node at the start
        head = curr = ListNode(500)

        while (l1 and l2):
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        # discard the dummy node
        return head.next