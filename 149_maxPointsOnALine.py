# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        if not points:
            return 0
        
        mm = {}
        
        for p in points:
            mm[(p.x,p.y)] = mm.get((p.x,p.y), 0) + 1    # get returns value, else second argument if key not present
        
        P = list(mm.keys())
        
        # all points at same location
        if len(P) == 1:
            return mm[P[0]]
        
        result = 0
        for i in range(len(P) - 1):
            slopes = {}
            for j in range(i+1, len(P)):
                dx = P[i][0] - P[j][0]
                dy = P[i][1] - P[j][1]
                
                if dx == 0:
                    slope = "#"
                elif dy == 0:
                    slope = 0
                else:
                    slope = float(dy) / dx
                
                slopes[slope] = slopes.get(slope, 0) + mm[P[j]]
            
            result = max(result, mm[P[i]] + max(slopes.values()))
        
        return result
        