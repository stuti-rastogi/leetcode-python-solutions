# O(n) solution

# class Solution:
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if (not nums):
#             return [-1, -1]
#         try:
#             start = nums.index(target)
#             if (start == -1):
#                 return [-1, -1]
#             n = len(nums)
#             for i in range(start+1, n):
#                 if (nums[i] != target):
#                     end = i - 1
#                     return [start, end]

#             end = n - 1
#             return [start, end]
#         except:
#             return [-1, -1]
  
# O(log n) solution
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(findLow):
            low = 0
            high = n
            while(low < high):
                mid = (low+high)//2
                if (nums[mid] == target and findLow) or (nums[mid] > target):
                    high = mid
                else:
                    low = mid + 1
            return low
        
        n = len(nums)
        if n == 0:
            return [-1,-1]
        
        leftPos = findPosition(True)
        
        if (leftPos == n) or (nums[leftPos] != target):
            return [-1,-1]
        
        rightPos = findPosition(False)-1
        
        return [leftPos, rightPos]
