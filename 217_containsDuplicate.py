from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for x in Counter(nums).values():
        #     if (x > 1):
        #         return True
        # return False
        
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True