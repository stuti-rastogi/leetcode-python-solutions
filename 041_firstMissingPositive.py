class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
#         if not nums:
#             return 1

#         nums = sorted(nums)
#         n = len(nums)

#         i = 0
#         while (i < n and nums[i] <= 0):
#             i += 1

#         potential = 1
#         while (i < n):
#             if (nums[i] > potential):
#                 return potential
#             elif not (potential > nums[i]):
#                 potential += 1
#             i += 1
#         return potential

        if not nums:
            return 1

        # array of size l: answer has to be something from [1...L+1]
        # to make length l+1
        nums.append(0)
        n = len(nums)

        # discard elements outside range of possible answers
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        # use the array to store frequency of the element
        # %n helps deal with duplicates
        # [1,1,3,0]
        # i=0 => nums[nums[0]%n] += n => nums[1] = 1+4 = 5
        # i=1 => nums[nums[1]%n] += n => nums[5%4] = nums[1] = 5+4 = 9
        for i in range(n):
            nums[nums[i]%n] += n

        # element that wasn't seen will have the original value 
        # in that position which is < n, hence el // n = 0
        for i in range(1,n):
            if nums[i]//n == 0:
                return i
        return n
