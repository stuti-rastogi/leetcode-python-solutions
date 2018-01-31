class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # total = (n * (n+1))/2
        # sum = 0
        # for x in nums:
        #     sum += x
        # return total-sum
        
        return (1+len(nums)) * len(nums)/2 - sum(nums)