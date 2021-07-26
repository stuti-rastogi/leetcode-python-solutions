import heapq

class Solution:
    def calculate_distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [tuple[1] for tuple in heap]

        # point_distances = list(map(self.calculate_distance, points))
#         point_priorities = []
#         num_points = len(points)
#         for i in range(num_points):
#             point_priorities.append((self.calculate_distance(points[i]), points[i]))

#         return [item[1] for item in heapq.nsmallest(k, point_priorities)]
