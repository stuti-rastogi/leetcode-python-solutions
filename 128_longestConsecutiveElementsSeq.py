class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # O(nlgn)
        # if not nums:
        #     return 0
        
        # nums.sort()
        # numsLen = len(nums)
        
        # longestConsecutiveLen = 1
        # currConsecutiveLen = 1
        
        # for i in range(numsLen):
        #     if nums[i] == nums[i-1] + 1:
        #         currConsecutiveLen += 1
        #     elif nums[i] != nums[i-1]:
        #         longestConsecutiveLen = max(longestConsecutiveLen, currConsecutiveLen)
        #         currConsecutiveLen = 1
                
        # return max(longestConsecutiveLen, currConsecutiveLen)
        
        # O(n) solution
        # to have O(1) lookups
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                # this means x is potentially the start of a sequence
                y = x + 1
                # keep checking x+1, x+2, x+3, ... for however far we can go
                while y in nums:
                    y += 1
                # length of current sequences is just y-x
                best = max(best, y - x)
        return best