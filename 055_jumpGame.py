# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         farthestReach = 0
        
#         for i, jump in enumerate(nums):
#             # we can't reach i with the farthest we have got so far
#             if farthestReach < i:
#                 return False
#             if farthestReach >= n-1:
#                 return True
#             farthestReach = max(farthestReach, i + jump)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #set an initial jumps avail
        jumps_avail = 0
        for i in range(0,len(nums)):
            #checks if we are at the end will guarantee term if len==1
            if i == len(nums) - 1:
                return True
            #check if you should break out of your current jump selection for a larger jump
            elif nums[i] >= jumps_avail:
                jumps_avail = nums[i]
            #take away one from your jump as you move to the next index
            else:
                jumps_avail -= 1
            #stuck at a 0 and cant jump
            if jumps_avail == 0:
                return False