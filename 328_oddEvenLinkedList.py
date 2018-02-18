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
        
        oddHead = head
        evenHead = head.next
        odd = oddHead
        even = evenHead
        current = head.next.next
        
        while(current):
            odd.next = current
            odd = odd.next
            even.next = current.next
            even = even.next
            if not current.next:
                break
            current = current.next.next
            
        odd.next = evenHead
        return oddHead