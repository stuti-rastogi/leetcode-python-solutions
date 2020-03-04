# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        head = result
        carry = 0
        
        while (l1 or l2):
            addition = 0
            if l1:
                addition = addition + l1.val
            if l2:
                addition = addition + l2.val
            addition = addition + carry
            val = addition % 10
            carry = addition / 10
            result.next = ListNode(val)
            result = result.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry:
            result.next = ListNode(carry)
        
        return head.next