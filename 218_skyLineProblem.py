,rfrom heapq import *

class Solution:
    def getSkyline(self, LRH):
        criticalPoints = set([b[0]for b in LRH])
        criticalPoints.update(set([b[1] for b in LRH]))
        
        result = []
        activeSet = []
        i = 0
        numBuildings = len(LRH)
        
        for point in sorted(criticalPoints):
            while (i < numBuildings) and (LRH[i][0] <= point):
                heappush(activeSet, (-LRH[i][2], LRH[i][1]))
                i = i+1
            
            while activeSet and activeSet[0][1] <= point:
                heappop(activeSet)
               
            if (activeSet):
                h = -activeSet[0][0]
            else:
                h = 0
            
            if not result:
                result.append([point, h])
            else:
                if (h != result[-1][1]):
                    result.append([point, h])
        return result