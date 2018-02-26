class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return -1
        # if len(nums) == 1:
        #     return 0
        # for i in range(len(nums)):
        #     if i == 0 and nums[i] >= nums[i+1]:
        #         return i
        #     if i == len(nums)-1 and nums[i] >= nums[i-1]:
        #         return i
        #     elif nums[i] >= nums[i-1] and nums[i] >= nums[i+1]:
        #         return i
        # return -1

        # shorter:
        # n = len(nums)
        # for i in range(1, n):
        #     if (nums[i] < nums[i-1]):
        #         return (i-1)
        # return n-1
        
        # O(lgn) complexity:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if end == start + 1:
                return start if nums[start] > nums[end] else end
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid - 1
            else:
                start = mid + 1
        return start