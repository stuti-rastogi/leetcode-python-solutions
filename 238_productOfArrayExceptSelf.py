class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (not nums):
            return None
        
        n = len(nums)
        result = [1] * n
        prod = 1
        for i in range(n):
            result[i] = result[i] * prod
            prod = prod * nums[i]
            
        prod = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * prod
            prod = prod * nums[i]
        return result
            