class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # iterative
        result = [[]]
        for n in nums:
            new_permutations = []
            # each current configuration has to have this n inserted in it
            for permutation in result:
                # insert current n at all possible positions (including front and back)
                for i in range(len(permutation) + 1):
                    new_permutations.append(permutation[:i] + [n] + permutation[i:])
            result = new_permutations
        return list(set(tuple(i) for i in result))
        
#         if not nums:
#             return []
        
#         nums.sort()
#         n = len(nums)
#         res = [nums[:]]
#         i = n-1
#         while i > 0:
#             if nums[i-1] < nums[i]:
#                 j = n-1
#                 while nums[j] <= nums[i-1]:
#                     j -= 1
#                 nums[i-1], nums[j] = nums[j], nums[i-1]
#                 nums[i:] = sorted(nums[i:])
#                 res.append(nums[:])
#                 i = n-1
#             else:
#                 i -= 1
        
#         return res