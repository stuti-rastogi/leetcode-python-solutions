class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort inplace - O(1) space, violating constraint 1, O(nlgn) time
        # nums.sort()
        # for i in range(0, len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        
        # use set - O(n) extra space, O(n) time, violating constraint 2
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen.add(i)
        
        # slow, fast pointer (cycle detection) - O(n) time, O(1) space
        slow = nums[0]              # 1
        fast = nums[nums[0]]        # 2
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
