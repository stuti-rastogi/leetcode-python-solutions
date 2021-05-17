# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if (not intervals):
            return []

        sortedIntervals = sorted(intervals, key = lambda x: x.start)
        result = []
        result.append(sortedIntervals[0])
        for interval in sortedIntervals[1:]:
            if (interval.start <= result[-1].end):
                result[-1].end = max(interval.end, result[-1].end)
            else:
                result.append(interval)
        return result