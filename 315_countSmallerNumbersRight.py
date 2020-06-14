class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        sorted_arr = [nums[-1]]
        result = [0]
        n = len(nums)

        for i in range(n-2,-1,-1):
            num = nums[i]
            idx = bisect_left(sorted_arr, num)
            result.append(idx)
            sorted_arr.insert(idx, num)

        return reversed(result)