# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # O(nlogk) time and O(n) space
        # minPriorityQueue = PriorityQueue()
        # for l in lists:
        #     if l:
        #         minPriorityQueue.put((l.val, id(l), l))

        # curr = head = ListNode(0)
        # while not minPriorityQueue.empty():
        #     value, _, node = minPriorityQueue.get()
        #     curr.next = ListNode(value)
        #     curr = curr.next
        #     node = node.next
        #     if node:
        #         minPriorityQueue.put((node.val, id(node), node))
        # return head.next

        # O(nlogn) time for sorting and O(n) space for new array/linked list
        allNodes = []
        for l in lists:
            while l:
                allNodes.append(l.val)
                l = l.next

        allNodes.sort()
        curr = head = ListNode(0)
        for value in allNodes:
            curr.next = ListNode(value)
            curr = curr.next

        return head.next

