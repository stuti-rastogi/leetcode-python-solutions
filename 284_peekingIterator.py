# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self._hasNext = iterator.hasNext()
        self._peak = None
        if self._hasNext:
            self._peak = iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._peak

    def next(self):
        """
        :rtype: int
        """
        result = self._peak
        if self.iter.hasNext():
            self._peak = self.iter.next()
        else:
            self._hasNext = False
        return result
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._hasNext

# class PeekingIterator(object):
#     def __init__(self, iterator):
#         self.iter = iterator
#         self.temp = self.iter.next() if self.iter.hasNext() else None

#     def peek(self):
#         return self.temp

#     def next(self):
#         ret = self.temp
#         self.temp = self.iter.next() if self.iter.hasNext() else None
#         return ret

#     def hasNext(self):
#         return self.temp is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].