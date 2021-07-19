# https://briangordon.github.io/2014/08/the-skyline-problem.html

'''
Our final solution, then, in O(nlogn) time, is as follows.

First, sort the critical points.
Then scan across the critical points from left to right.
When we encounter the left edge of a rectangle, we add that rectangle to the heap with its height as the key.
When we encounter the right edge of a rectangle, we remove that rectangle from the heap.
(This requires keeping external pointers into the heap.)
Finally, any time we encounter a critical point,
after updating the heap we set the height of that critical point to the value peeked from the top of the heap.

Update (Feb 2019): Ivan Malison points out that you don’t actually need to keep external pointers into the heap.
Instead, as you scan, when you hit the left edge of a building you add it to the heap,
and when you hit the right edge of a building you pop nodes off the top of the heap repeatedly
until the top node is a building whose right edge is still ahead.
With this strategy, your heap may contain buildings which have already ended,
but it doesn’t matter because you’ll discard them as soon as they’re at the top of the heap.
'''

from heapq import *

class Solution:
    def getSkyline(self, LRH):
        criticalPoints = set([b[0]for b in LRH])
        criticalPoints.update(set([b[1] for b in LRH]))

        result = []
        activeSet = []
        i = 0
        numBuildings = len(LRH)

        # sorted(criticalPoints) is now a list
        for point in sorted(criticalPoints):
            # all rectangles that started before this CP can determine its height
            while (i < numBuildings) and (LRH[i][0] <= point):
                # heap key is height but max heap
                heappush(activeSet, (-LRH[i][2], LRH[i][1]))
                i = i+1

            # remove rectangles that ended before this point
            while activeSet and activeSet[0][1] <= point:
                heappop(activeSet)

            # if anything left, this CP gets the max height of rectangles active at this CP
            if (activeSet):
                h = -activeSet[0][0]
            else:
                h = 0

            if not result:
                result.append([point, h])
            else:
                # combine same height CPs
                if (h != result[-1][1]):
                    result.append([point, h])

        return result

