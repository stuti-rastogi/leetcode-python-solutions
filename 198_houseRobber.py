class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if (not nums):
        #     return 0
        # n = len(nums)
        # if (n == 1):
        #     return nums[0]
        # if (n == 2):
        #     ans = max(nums[0], nums[1])
        #     return ans
        # theft = nums[0]
        # for i in range (n-2):
        #     theft = max(nums[i] + self.rob(nums[i+2:]), self.rob(nums[i+1:]), theft)
        # return theft
        
#         if (not nums):
#             return 0
#         robIt = 0
#         dontRobIt = 0
        
#         for n in nums:
#             theft = dontRobIt + n
#             dontRobIt = max(dontRobIt, robIt)
#             robIt = theft
            
#         return max(robIt, dontRobIt)
    
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(now, last + i)
        return now
        