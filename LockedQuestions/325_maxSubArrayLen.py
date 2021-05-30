class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # computing prefix sum array but storing the index as well in hashmap
        # for faster search using the value

        prefixSums = {}
        prefixSums[0] = -1
        longestLength = 0
        runningSum = 0
        for i, num in enumerate(nums):
            runningSum += num
            if runningSum - k in prefixSums:
                longestLength = max(longestLength, i - prefixSums[runningSum - k])
            if runningSum not in prefixSums:
                prefixSums[runningSum] = i

        return longestLength
