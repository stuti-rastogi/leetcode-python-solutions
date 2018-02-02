class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ans = []
        # for i in range(len(nums)):
        #     x = nums[i]
        #     lookFor = target - x
        #     if (lookFor in nums):
        #         pos = nums.index(lookFor)
        #         if (pos == i):
        #             continue
        #         ans.append(i)
        #         ans.append(pos)
        #         break
        # return ans
        
        d = {}
        for i, x in enumerate(nums):
            check = target - x
            if check in d:
                pos = d[check]
                break
            else:
                d[x] = i

        return [pos, i]