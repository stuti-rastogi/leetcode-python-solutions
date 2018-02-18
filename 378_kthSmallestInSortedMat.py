class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted([element for row in matrix for element in row])[k-1]

        # sort - O(nlogn)