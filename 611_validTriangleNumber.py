class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0

        # other is the side compare pairs against
        for other in range(n-1, 1, -1):
            first = 0
            second = other - 1
            while first < second:
                if nums[first] + nums[second] <= nums[other]:
                    # need to increase LHS
                    first += 1
                else:
                    # condition satisfied for (first, second, other) and 
                    # all pairs (first+1, second, other)...(second-1, second, other)
                    count += (second - first)
                    second -= 1
        return count
