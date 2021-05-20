class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedNums = sorted(nums, reverse=True)
        n = len(nums)
        mid = n // 2
        nums[1::2] = sortedNums[:mid]
        nums[::2] = sortedNums[mid:]
