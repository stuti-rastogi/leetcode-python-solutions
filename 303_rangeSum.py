class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.sums = []
        else:
            self.sums = [0] * len(nums)
            self.sums[0] = nums[0]
            for i in range(1, len(nums)):
                self.sums[i] = self.sums[i-1] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.sums:
            return None
        if (i > 0):
            return (self.sums[j] - self.sums[i-1])
        else:
            return self.sums[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)