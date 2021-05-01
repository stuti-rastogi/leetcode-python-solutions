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

        # seen = set()
        # for x in nums:
        #     if x in seen:
        #         return True
        #     seen.add(x)
        # return False

        return len(set(nums)) < len(nums)

        # nums.sort()
        # n = len(nums)
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
