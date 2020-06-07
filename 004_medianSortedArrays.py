# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums = []
#         if not nums1:
#             nums = nums2
#         elif not nums2:
#             nums = nums1
#         else:
#             m = len(nums1)
#             n = len(nums2)
            
#             i = j = 0
            
#             while (i < m and j < n):
#                 if (nums1[i] < nums2[j]):
#                     nums.append(nums1[i])
#                     i += 1
#                 else:
#                     nums.append(nums2[j])
#                     j += 1
#             if (j == n):
#                 nums = nums + nums1[i:]
#             if (i == m):
#                 nums = nums + nums2[j:]
        
#         l = len(nums)
#         if (l%2 != 0):
#             # odd length
#             return nums[l//2]
#         else:
#             return (nums[l//2] + nums[l//2 - 1])/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m,n = n,m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2