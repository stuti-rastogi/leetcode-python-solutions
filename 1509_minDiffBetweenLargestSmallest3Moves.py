class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # nums.sort()
        # return min([b-a for a,b in zip(nums[:4], nums[-4:])])

        numsLen = len(nums)
        if numsLen <= 4:
            return 0
        nums.sort()
        # choices -
        #   1. remove biggest 3 elements
        #   2. remove smallest 3 elements
        #   3. remove 1 smallest and 2 biggest elements
        #   4. remove 2 smallest and 1 biggest elements
        # After removing these, get the min and max and keep the minimumDifference

        minDiff = float('inf')
        left = 0
        right = numsLen - 4
        for _ in range(4):
            minDiff = min(minDiff, nums[right] - nums[left])
            left += 1
            right += 1
        return minDiff
