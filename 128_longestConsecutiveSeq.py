class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aux = set(nums)
        maxLength = 0
        for el in nums:
            if el-1 not in aux:
                curr = el+1
                length = 1
                while (curr in aux):
                    curr += 1
                    length += 1
                if length > maxLength:
                    maxLength = length
        return maxLength