class NumArray:

    def __init__(self, nums: List[int]):
        numsLen = len(nums)
        self.sumsFromLeft = [0] * numsLen
        self.sumsFromLeft[0] = nums[0]
        for i in range(1, numsLen):
            self.sumsFromLeft[i] = self.sumsFromLeft[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.sumsFromLeft[right] - self.sumsFromLeft[left-1]
        else:
            return self.sumsFromLeft[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
