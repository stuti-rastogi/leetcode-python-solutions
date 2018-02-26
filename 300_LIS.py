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
        if not nums:
            return 0
        self.tail_number = [nums[0]]
        
        for i in range(1, len(nums)):  # N
            # case 3, greater than all end elements
            if nums[i] > self.tail_number[-1]:
                self.tail_number.append(nums[i])
                #print(self.tail_number)
            else:                                  # logN
                # case 2: where does this number lie, update the end element there
                pos = self.binarySearch(nums[i])
                self.tail_number[pos] = nums[i]
        
        return len(self.tail_number)

    def binarySearch(self, num):
        '''
        find the first tail larger than num
        '''
        left = 0
        right = len(self.tail_number) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.tail_number[mid] > num:
                    right = mid
            elif self.tail_number[mid] < num:
                    left = mid
            if self.tail_number[mid] == num:
                    right = mid
                    
        if self.tail_number[left] >= num:
            return left
        elif self.tail_number[right] >= num:
            return right
        