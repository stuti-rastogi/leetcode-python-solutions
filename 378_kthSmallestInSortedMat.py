class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # sort - O(nlogn)
        return sorted([element for row in matrix for element in row])[k-1]

        # Heap - O(klogn)
        # minHeap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        # n = len(matrix)
        # heapq.heapify(minHeap)                  # O(logn)
        # element = 0
        # for _ in range(k):
        #     element, i, j = heapq.heappop(minHeap)
        #     if j+1 < n:
        #         heapq.heappush(minHeap, (matrix[i][j+1], i, j+1))
        # return element


        # lo, hi = matrix[0][0], matrix[-1][-1]
        # while lo<hi:
        #     # Calculating mid element of sorted array
        #     mid = (lo+hi)//2
        #     # bisect.bisect_right(iterable, element) gives index of first element that is greater than the targeted value.
        #     # Similarly bisect.bisect_left(iterable, element) gives index of first element that is greater than or equal to the targeted value.
        #     # In the context, bisect.bisect_right(row, mid) gives the index where first element that would be greater than mid.
        #     # This bisect.bisect_right(row, mid) is calculated for all the rows of the matrix to get indices of first element in each row which is greater than mid.
        #     # Summing up these indices would give us the total number of elements that are less than or equal to mid. 
        #     # If number of such elements less than calculated mid is <k then we reduce the search space by increasing low=mid+1 (because for mid we've seen that number of elements <= mid are <k)
        #     # If number of elements less than calculated mid is >=k then we reduce the search space by bringing down high=mid
        #     if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
        #         lo = mid+1
        #     else:
        #         hi = mid
        # return lo

