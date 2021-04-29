class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # using library
        # itertools.permutations(nums) - tuples on iterating
        # return list(map(list, itertools.permutations(nums)))

        # recursive
        # if len(nums) == 1:
        #     return [nums]
        # result = []
        # for i in range(len(nums)):
        #     result = result + [[nums[i]] + l for l in self.permute(nums[:i]+nums[i+1:])]
        # return result

        # iterative
        result = [[]]
        for n in nums:
            new_permutations = []
            # each current configuration has to have this n inserted in it
            for permutation in result:
                # insert current n at all possible positions (including front and back)
                for i in range(len(permutation) + 1):
                    new_permutations.append(permutation[:i] + [n] + permutation[i:])
            result = new_permutations
        return result