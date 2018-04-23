class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        dic = {}
        
        for i, value in enumerate(nums):
            if value in dic and (i - dic[value]) <= k:
                return True
            dic[value] = i
        
        return False