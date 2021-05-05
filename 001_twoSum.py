class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute-force solution, accepted
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                return [i, d[target-num]]
            d[num] = i