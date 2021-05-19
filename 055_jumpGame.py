class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return not goal


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         #set an initial jumps avail
#         jumps_avail = 0
#         for i in range(0,len(nums)):
#             #checks if we are at the end will guarantee term if len==1
#             if i == len(nums) - 1:
#                 return True
#             #check if you should break out of your current jump selection for a larger jump
#             elif nums[i] >= jumps_avail:
#                 jumps_avail = nums[i]
#             #take away one from your jump as you move to the next index
#             else:
#                 jumps_avail -= 1
#             #stuck at a 0 and cant jump
#             if jumps_avail == 0:
#                 return False