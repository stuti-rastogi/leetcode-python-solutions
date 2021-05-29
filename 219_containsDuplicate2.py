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

        # Set Approach
        #####################
        # if k == 0:
        #     return False
        
        # numsLen = len(nums)
        # window = set()
        
        # for index in range(numsLen):
        #     if nums[index] in window:
        #         return True
        #     if len(window) == k:
        #         window.remove(nums[index-k])
        #     window.add(nums[index])
        # return False