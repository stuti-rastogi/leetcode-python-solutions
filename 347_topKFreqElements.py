from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return None
        # return [i[0] for i in Counter(nums).most_common(k)]
        return [x for x, count in sorted(Counter(nums).items(), key = lambda y: y[1], reverse = True)[ : k]]
        