# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
#         curA, curB = headA, headB
#         lenA, lenB = 0, 0
#         while curA:
#             lenA = lenA + 1
#             curA = curA.next
#         while curB:
#             lenB = lenB + 1
#             curB = curB.next

#         curA, curB = headA, headB
#         if lenA > lenB:
#             for i in range(lenA-lenB):
#                 curA = curA.next
#         elif lenB > lenA:
#             for i in range(lenB-lenA):
#                 curB = curB.next
#         while curB != curA:
#             curB = curB.next
#             curA = curA.next
#         return curA


        pointer_a, pointer_b = headA, headB

        while pointer_a is not pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next
        return pointer_a