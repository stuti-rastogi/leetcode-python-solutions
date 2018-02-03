# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # stack = []
        # if (not head):
        #     return True
        # curr = head
        # while (curr):
        #     stack.append(curr.val)
        #     curr = curr.next
        # curr = head
        # while (curr):
        #     if (curr.val != stack.pop()):
        #         return False
        #     curr = curr.next
        # return True
        
        # O(1) space solution
        if not head or not head.next:
            return True
        curr = head
        count = 1
        # length of list
        while curr.next:
            curr = curr.next
            count = count + 1
            
        # reversing first half of list
        p = head
        curr = head
        half = count / 2        
        while half > 0:            
            tmp = p.next
            if p != head:
                 p.next = curr 
            else:
                p.next = None
            curr = p
            p = tmp            
            half -= 1
        
        # pointer to beginning of second half
        if count % 2 == 0:
            secondHalf = p
        else:
            secondHalf = p.next
        
        # curr was last element of first half
        p = curr
        while p:
            if p.val != secondHalf.val:
                return False
            p = p.next
            secondHalf = secondHalf.next
        return True