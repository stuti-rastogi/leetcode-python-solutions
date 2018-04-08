class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        num_nextGreat = {}
        
        for num in nums2:
            while stack and num>stack[-1]:
                num_nextGreat[stack[-1]] = num
                stack.pop()
            stack.append(num)
        
        res = []
        for num in nums1:
            if num in num_nextGreat:
                res.append(num_nextGreat[num])
            else:
                res.append(-1)
        return res
    
#         if (not nums1):
#             return []

#         result = []
#         for x in nums1:
#             pos = nums2.index(x)
#             found = False
#             for right in nums2[pos+1:]:
#                 if (right > x):
#                     result.append(right)
#                     found = True
#                     break
#             if not found:
#                 result.append(-1)
        
#         return result
            