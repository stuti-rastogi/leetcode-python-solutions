class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            xdiff = abs(p2[0] - p1[0])
            ydiff = abs(p2[1] - p1[1])
            if (xdiff == 0 or ydiff == 0):
                time = time + xdiff + ydiff
            else:
                diagonal = min(xdiff, ydiff)
                time = time + diagonal
                if (xdiff != ydiff):
                    time = time + max(abs(ydiff - diagonal), abs(xdiff - diagonal))
        return time