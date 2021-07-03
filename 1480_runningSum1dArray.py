class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        for i in range(1, numsLen):
            nums[i] += nums[i-1]
        return nums
