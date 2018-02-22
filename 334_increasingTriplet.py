class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        min1 = float('inf')
        min2 = float('inf')
        
        for x in nums:
            if (x <= min1):
                min1 = x
            elif (x <= min2):
                min2 = x
            else:
                return True
        return False