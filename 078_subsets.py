class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # using python itertools
        # result = []
        # for i in range(0, len(nums)+1):
        #     result = result + list(itertools.combinations(nums, i))
        # return result
    
        result = [[]]
        for i in nums:
            current = []
            for subset in result:
                current.append(subset + [i])
            result = result + current
        return result