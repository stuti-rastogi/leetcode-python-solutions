class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos0 = -1
        pos1 = -1
        pos2 = -1
        for i in range(len(nums)):
            if nums[i] == 2:
                pos2 = pos2 + 1
                nums[pos2] = 2
            elif nums[i] == 1:
                pos1 = pos1 + 1
                pos2 = pos2 + 1
                nums[pos2] = 2
                nums[pos1] = 1
            elif nums[i] == 0:
                pos0 = pos0 + 1
                pos1 = pos1 + 1
                pos2 = pos2 + 1
                nums[pos2] = 2
                nums[pos1] = 1
                nums[pos0] = 0
                
 
        return