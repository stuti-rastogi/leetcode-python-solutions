class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            if leftSum == (totalSum-leftSum-nums[i]):
                return i
            leftSum += num
        return -1

#         numsLen = len(nums)
#         leftSums = [0 for _ in range(numsLen)]
#         rightSums = [0 for _ in range(numsLen)]

#         for i in range(1, numsLen):
#             leftSums[i] = leftSums[i-1] + nums[i-1]

#         for i in range(numsLen-2, -1, -1):
#             rightSums[i] = rightSums[i+1] + nums[i+1]

#         for i in range(numsLen):
#             if leftSums[i] == rightSums[i]:
#                 return i
#         return -1
