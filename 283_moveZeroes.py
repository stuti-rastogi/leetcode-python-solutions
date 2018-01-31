class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        for j in range(n):
            if (nums[j]):
                nums[index] = nums[j]
                index = index + 1
            
        for i in range(index, n):
            nums[i] = 0