class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 0
        
        maxSum = nums[0]
        continuous = nums[0]
        n = len(nums)
        for i in range(1,n):
            newSum = nums[i] + continuous
            if (newSum > nums[i]):
                continuous = newSum
            else:
                continuous = nums[i]
            if (continuous > maxSum):
                maxSum = continuous
        return maxSum

        ##### Alternate Solution #####
        # for i in range(len(nums) - 1):
        #     if nums[i] > 0:
        #         nums[i+1] += nums[i]
        # return max(nums)