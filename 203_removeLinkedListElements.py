# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        curr = new_head

        while curr:
            next_node = curr.next
            while next_node and next_node.val == val:
                next_node = next_node.next
            curr.next = next_node
            curr = curr.next

        return new_head.next


        # sentinel = ListNode(0)
        # sentinel.next = head

        # prev, curr = sentinel, head
        # while curr:
        #     if curr.val == val:
        #         prev.next = curr.next
        #     else:
        #         prev = curr
        #     curr = curr.next

        # return sentinel.next