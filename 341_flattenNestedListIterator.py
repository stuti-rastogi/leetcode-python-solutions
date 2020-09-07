# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# no reversing, pop from front
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList
    
    def next(self) -> int:
        return self.stack.pop(0)
        
    
    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[0].isInteger():
                return True
            curr = self.stack.pop(0)
            self.stack = curr.getList() + self.stack
        return False


# class NestedIterator(object):
#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.mainList = nestedList[::-1]

#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.mainList.pop().getInteger()
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         while self.mainList:
#             top = self.mainList[-1]
#             if (top.isInteger()):
#                 return True
#             self.mainList = self.mainList[:-1] + top.getList()[::-1]
#         return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())