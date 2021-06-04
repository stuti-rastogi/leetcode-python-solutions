class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) time, O(1) space
        duplicates = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                duplicates.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return duplicates

        # O(n) time, O(n) space
        # seen = set()
        # duplicates = []

        # for num in nums:
        #     if num in seen:
        #         duplicates.append(num)
        #     else:
        #         seen.add(num)
        # return duplicates

        # O(nlgn) time, O(1) space
        # nums.sort()
        # n = len(nums)
        # duplicates = []

        # for i in range(1, n):
        #     if nums[i] == nums[i-1]:
        #         duplicates.append(nums[i])

        # return duplicates
