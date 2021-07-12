class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # equation: yi + yj + |xi - xj| = (yi - xi) + (yj + xj) since xi <= xj
        minHeap = []
        maxValue = -float("inf")
        for x, y in points:
            # pop any point which does not satisfy |xi - xj| <= k
            while minHeap and x - minHeap[0][1] > k:
                heapq.heappop(minHeap)
            if minHeap:
                # negate the expression to get the maximum (y - x)
                maxValue = max(maxValue, -minHeap[0][0] + x + y)
            # we need max (xi - yi) so push -(xi - yi) = yi - xi to minHeap
            heapq.heappush(minHeap, ((x - y), x))
        return maxValue
