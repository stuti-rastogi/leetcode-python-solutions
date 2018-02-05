class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        k = k % len(nums)
        reverse(0, len(nums)-1)
        reverse(k, len(nums)-1)
        reverse(0, k-1)