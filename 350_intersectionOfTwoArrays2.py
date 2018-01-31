from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#         c1 = Counter(nums1)
#         c2 = Counter(nums2)
        
#         result = []
#         for i in c1.keys():
#             if i in c2.keys():
#                 for _ in range(min(c1[i], c2[i])):
#                     result.append(i)
#         return result
    
        elem_counter = {}
        for num in nums1:
            if num in elem_counter:
                elem_counter[num] += 1
            else:
                elem_counter[num] = 1
        
        intersect_list = []
        for num in nums2:
            if num in elem_counter:
                elem_counter[num] -= 1
                if elem_counter[num] == 0:
                    del elem_counter[num]
                intersect_list.append(num)
        
        return intersect_list