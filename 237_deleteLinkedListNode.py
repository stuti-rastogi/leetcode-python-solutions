# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node is the node to be deleted, no access to head of list
        # copy next value to current node
        # delete next node
        node.val = node.next.val
        node.next = node.next.next
        return