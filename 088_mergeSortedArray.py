class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        # if (not nums1 or m == 0):
        #     nums1 = nums2
        #     return
        
        i = 0
        j = 0
        len1 = m
        while (i < len1 and j < n):
            if (nums1[i] < nums2[j]):
                i = i + 1
            else:
                nums1.insert(i, nums2[j])
                j = j + 1
                len1 = len1 + 1
        # print ("Len1: " + str(len1))
        # print ("i: " + str(i))
        # print ("j: " + str(j))
        if (i == len1):
            for ind in range(j, n):
                nums1.append(nums2[ind])
        return
                
        