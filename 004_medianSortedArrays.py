class Solution:
    # O(m+n) solution with O(m+n) space as well
    ################################################################################
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     nums = []
    #     if not nums1:
    #         nums = nums2
    #     elif not nums2:
    #         nums = nums1
    #     else:
    #         m = len(nums1)
    #         n = len(nums2)

    #         i = j = 0

    #         while (i < m and j < n):
    #             if (nums1[i] < nums2[j]):
    #                 nums.append(nums1[i])
    #                 i += 1
    #             else:
    #                 nums.append(nums2[j])
    #                 j += 1
    #         if (j == n):
    #             nums = nums + nums1[i:]
    #         if (i == m):
    #             nums = nums + nums2[j:]

    #     l = len(nums)
    #     if (l%2 != 0):
    #         # odd length
    #         return nums[l//2]
    #     else:
    #         return (nums[l//2] + nums[l//2 - 1])/2

    # O(m+n) solution with no additional space
    ################################################################################
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     m = len(nums1)
    #     n = len(nums2)

    #     totalLen = m+n
    #     if totalLen % 2 == 1:
    #         # start counting from 1, so we need the (n//2 + 1)th element
    #         medianCount = totalLen//2
    #         oddCount = True
    #     else:
    #         # for even we need to take avg of (n//2)th and (n//2 + 1)th element
    #         medianCount = totalLen//2 - 1
    #         oddCount = False

    #     nums1It = 0
    #     nums2It = 0
    #     count = 0
    #     median = None

    #     while nums1It < m and nums2It < n:
    #         if nums1[nums1It] < nums2[nums2It]:
    #             nextNum = nums1[nums1It]
    #             nums1It += 1
    #         else:
    #             nextNum = nums2[nums2It]
    #             nums2It += 1

    #         if count == medianCount:
    #             if oddCount:
    #                 return nextNum
    #             else:
    #                 median = nextNum
    #         elif count == medianCount+1:
    #             return (median + nextNum) / 2

    #         count += 1

    #     if nums1It == m:
    #         if oddCount:
    #             return nums2[nums2It:][(medianCount-count)]
    #         else:
    #             if median:
    #                 return (median+nums2[nums2It:][(medianCount-count+1)]) / 2
    #             else:
    #                 return (nums2[nums2It:][(medianCount-count)] + nums2[nums2It:][(medianCount-count+1)]) / 2
    #     else:
    #         if oddCount:
    #             return nums1[nums1It:][(medianCount-count)]
    #         else:
    #             if median:
    #                 return (median+nums1[nums1It:][(medianCount-count+1)]) / 2
    #             else:
    #                 return (nums1[nums1It:][(medianCount-count)] + nums1[nums1It:][(medianCount-count+1)]) / 2

    """
    (1) i + j == m - i + n - j (or: m - i + n - j + 1)
        if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
    (2) B[j-1] <= A[i] and A[i-1] <= B[j]
    - i is the NUMBER of elements of A in the left half, and j is the NUMBER of elements of B in the left half (not index)
    - in case of odd (m+n), we want left half to have more elements than right always so we can return max element of left,
    which we need to find for even case as well
    - j = (m+n+1)//2 - i for both even and odd (m+n) case because //2 rounds down
        - If m+n = 8, j = 9//2 - i, which is 4 - i (length of left half = i+j = 4)
        - If m+n = 7, j = 8//2 - i, which is 4 - i (length of left half = i+j = 4, right is length 3)
    """
    # O(lg(min(m,n))) solution with no additional space
    ################################################################################
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        iLeft = 0
        iRight = m
        halfLen = (m+n+1) // 2
        while iLeft <= iRight:
            i = (iLeft + iRight) // 2
            j = halfLen - i
            if i < m and nums2[j-1] > nums1[i]:
                iLeft = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                iRight = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1], nums2[j-1])

                if (m+n) % 2 == 1:
                    return maxLeft

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                return (minRight + maxLeft) / 2
