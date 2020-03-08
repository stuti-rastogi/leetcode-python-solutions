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

        # all numbers of array are 1 to n
        # so can keep cycling through the array if nums[i] is next
        # index to visit
        # but not nums[0], so that should be entry point
        
        # Test case: [2, 5, 1, 3, 5, 7, 6, 4]
        slow = nums[0]
        fast = nums[0]

        while True:
            # slow pointer goes to index pointed by nums[i]
            slow = nums[slow]
            # fast pointer does that twice
            fast = nums[nums[fast]]
            # because there is a duplicate, their values become same at some
            # point in the cycle
            if slow == fast:
                break

        # now start from the beginning and the two pointers meet at the entry
        # of the cycle which is actually the duplicate
        p1 = nums[0]
        p2 = fast
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1