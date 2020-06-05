class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low = 0
        high = n-1
        
        i = 0
        while (i <= high):
            if nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            elif nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            else:
                i += 1
        return
            
#         pos0 = -1
#         pos1 = -1
#         pos2 = -1
        
#         for el in nums:
#             if el == 2:
#                 pos2 += 1
#                 nums[pos2] = 2
#             elif el == 1:
#                 pos2 += 1
#                 pos1 += 1
#                 nums[pos2] = 2
#                 nums[pos1] = 1
#             else:
#                 pos2 += 1
#                 pos1 += 1
#                 pos0 += 1
#                 nums[pos2] = 2
#                 nums[pos1] = 1
#                 nums[pos0] = 0
#         return
    