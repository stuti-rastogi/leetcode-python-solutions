from collections import Counter
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # if (n == 0 or n == 1):
        #     return n
        # index = 0
        # for i in range(n-1):
        #     if (nums[i] != nums[i+1]):
        #         nums[index] = nums[i]
        #         index = index + 1
        # nums[index] = nums[n-1]
        # return (index+1)
        
        # [:] creates a copy so might not be acceptable
        nums[:] = sorted(list(set(nums)))
        return len(nums)