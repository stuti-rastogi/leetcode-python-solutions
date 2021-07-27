# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        num_groups = count // k
        prev = None
        curr = head
        last_node = None

        for _ in range(num_groups):
            reverse_count = 0
            while reverse_count < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                reverse_count += 1
            if last_node:
                last_node.next = prev
            else:
                head = prev
            for _ in range(k-1):
                prev = prev.next

            last_node = prev
            prev = None

        last_node.next = curr
        return head

