class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
 
        n = len(nums)
        i = n - 1
        j = -1
        
        while (i > 0):
            if nums[i] > nums[i-1]:
                j = i - 1
                break
            i = i - 1
        
        for i in range(n-1, -1, -1):
            if (nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                nums[j+1:] = sorted(nums[j+1:])
                return