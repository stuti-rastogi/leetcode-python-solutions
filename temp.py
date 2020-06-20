from typing import List
import collections

class Solution:
    def __init__(self):
        pass

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if not flights:
            return -1
        
        graph = collections.defaultdict(list)
        for flight in flights:
            graph[flight[0]].append([flight[1], flight[2]])
        
        print (graph)
        
        if src not in graph:
            return -1
        
        def findPath(src: int, stops: int, currVal: int) -> int:
            if stops > K:
                if src == dst:
                    return currVal
                return -1
            if not graph[src]:
                return -1
            newVal = 10001
            for neighbor in graph[src]:
                if (src == 6 and neighbor[0] == 8):
                    print ("YES")
                if neighbor[0] == dst:
                    newVal = min(newVal, currVal + neighbor[1])
                else:
                    pathVal = findPath(neighbor[0], stops+1, currVal + neighbor[1])
                    if pathVal == -1:
                        continue
                    newVal = min(newVal, currVal + pathVal)
            print ("Returning newVal: " + str(newVal))
            return newVal        
        
        # print (graph)
        result = findPath(src, 0, 0)
        if result == 10001:
            return -1
        return result

if __name__ == "__main__":
    solution = Solution()
    solution.findCheapestPrice(10, 
            [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 
            6, 0, 7)