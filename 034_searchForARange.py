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
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        
        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]