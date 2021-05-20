class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 0

        minValue = nums[0]
        maxValue = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if (nums[i] < 0):
                maxValue, minValue = minValue, maxValue

            maxValue = max(nums[i], nums[i] * maxValue)
            minValue = min(nums[i], nums[i] * minValue)

            result = max(result, maxValue)

        return result