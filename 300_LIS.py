# class Solution:
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        # O(n^2) complexity
#         if not nums:
#             return 0

#         n = len(nums)
#         aux = [1] * n
#         for i in range(n):
#             for j in range(i):
#                 if (nums[j] < nums[i] and aux[i] < aux[j] + 1):
#                     aux[i] = aux[j] + 1

#         return max(aux)

class Solution:
    def lengthOfLIS(self, nums):
        '''
        O(nlogn) Binary Search+Greedy
        '''
        def binarySearch(arr, target):
            '''
            find the position of this num
            '''
            low = 0
            high = len(arr)

            while (low < high):
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    low = mid+1
                else:
                    high = mid

            if low == len(arr):
                return low-1
            return low


        if not nums:
            return 0

        sequence = [nums[0]]

        for num in nums:
            if num < sequence[0]:
                sequence[0] = num
            elif num > sequence[-1]:
                sequence.append(num)
            else:
                sequence[binarySearch(sequence, num)] = num

        return len(sequence)
