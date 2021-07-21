# O(nlgn) solution
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         # pre-process
#         processedIntervals = []
#         for interval in intervals:
#             processedIntervals.append((interval[0], 0))
#             processedIntervals.append((interval[1], 1))

#         processedIntervals.sort(key=lambda x: (x[0], -x[1]))
#         maxCount = 0
#         currCount = 0

#         for point in processedIntervals:
#             if point[1] == 0:
#                 currCount += 1
#                 maxCount = max(currCount, maxCount)
#             else:
#                 currCount -= 1

#         return maxCount


# O(nlgn) solution - priority queue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        freeRooms = []
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(freeRooms, intervals[0][1])

        for interval in intervals[1:]:
            if freeRooms[0] <= interval[0]:
                heapq.heappop(freeRooms)

            heapq.heappush(freeRooms, interval[1])

        return len(freeRooms)