# class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # using python itertools
#         # result = []
#         # for i in range(0, len(nums)+1):
#         #     result = result + list(itertools.combinations(nums, i))
#         # return result
    
#         result = [[]]
#         for i in nums:
#             current = []
#             for subset in result:
#                 current.append(subset + [i])
#             result = result + current
#         return result

class Solution(object):
    def subsets(self, nums):
        def backtrack(first, curr):
            # print k, result
            # if we have a current combination of length k, add this to result
            if len(curr) == k:
                result.append(curr[:])

            # for each of the element consider a new combination adding this
            # element in
            # at the end remove this and move to next
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        result = []
        n = len(nums)
        # idea of backtracking is to iterate over all possible
        # sizes of subsets (0 to n)
        for k in range(n+1):
            backtrack(0, [])
        return result
