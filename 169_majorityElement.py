class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         counts = {}
#         n = len(nums)
#         for x in nums:
#             if (x in counts):
#                 counts[x] += 1
#             else:
#                 counts[x] = 1
#         #print (counts)
        
#         for x in counts:
#             if (counts[x] > math.floor(n/2)):
#                 return x
#         return 0

        flag = 0
        majority = -1
        for num in nums:
            if (flag == 0):
                flag = 1
                majority = num
            else:
                if (num == majority):
                    flag = flag + 1
                else:
                    flag = flag - 1
        return majority