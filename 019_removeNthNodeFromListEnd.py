# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None

        # make this stop at n+1th index, if head is 0
        first = head
        count = 0
        while first and count <= n:
            first = first.next
            count += 1

        # move both first and second
        # they have n node between them
        # when first becomes None (beyond n of list), second is one node behind nth node from end
        second = head
        while first:
            first = first.next
            second = second.next

        # count == n+1 means exitted naturally
        if second == head and count != n+1:
            head = second.next
        else:
            second.next = second.next.next

        return head
