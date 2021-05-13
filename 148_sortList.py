# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitList(self, head):
        # slow pointer keeps track of last element in first half
        slow = None
        fast = head
        while (fast and fast.next):
            if not slow:
                slow = head
            else:
                slow = slow.next
            fast = fast.next.next

        # next of slow is the "mid" - head of second half
        mid = slow.next
        slow.next = None
        return mid


    def mergeSortedLists(self, l1, l2):
        head = curr = ListNode(0)
        while (l1 and l2):
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next


    def sortList(self, head: ListNode) -> ListNode:
        # Merge sort
        # 1. Find mid
        # 2. Merge sorted lists
        
        # length 0 or 1
        if not head or not head.next:
            return head
        mid = self.splitList(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeSortedLists(left, right)
