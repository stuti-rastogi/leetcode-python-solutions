# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head
        second = None
        while first:
            prev = second
            second = first.next
            if not second:
                return head
            nextNode = second.next
            second.next = first
            first.next = nextNode
            if not prev:
                head = second
            else:
                prev.next = second
            first = first.next
            second = second.next
        return head
