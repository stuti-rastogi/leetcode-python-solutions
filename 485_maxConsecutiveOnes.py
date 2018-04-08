class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        result = 0
        current = 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                if (current == 0):
                    continue
                else:
                    if (current > result):
                        result = current
                    current = 0
            if (nums[i] == 1):
                current = current + 1
        
        if (current > result):
            result = current
        
        return result