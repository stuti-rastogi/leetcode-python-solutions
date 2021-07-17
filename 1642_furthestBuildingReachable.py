class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_heap = []
        num_buildings = len(heights)
        ladders_avail = ladders
        bricks_avail = bricks

        for idx in range(num_buildings-1):
            height_diff = heights[idx+1] - heights[idx]
            if height_diff <= 0:
                continue
            if ladders_avail > 0:
                heapq.heappush(ladder_heap, height_diff)
                ladders_avail -= 1
            else:
                if not ladder_heap or ladder_heap[0] >= height_diff:
                    bricks_avail -= height_diff
                else:
                    smaller_height_ladder = heapq.heappop(ladder_heap)
                    heapq.heappush(ladder_heap, height_diff)
                    bricks_avail -= smaller_height_ladder
                if bricks_avail < 0:
                    return idx

        return num_buildings - 1

# class Solution:
#     def isReachable(self, building, possible_climbs, bricks, ladders):
#         bricks_avail = bricks
#         ladders_avail = ladders

#         for climb, idx in possible_climbs:
#             if idx > building:
#                 continue
#             if bricks_avail >= climb:
#                 bricks_avail -= climb
#             elif ladders_avail > 0:
#                 ladders_avail -= 1
#             else:
#                 return False
#         return True

#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         possible_climbs = []
#         num_buildings = len(heights)

#         for idx in range(num_buildings-1):
#             height_diff = heights[idx+1]-heights[idx]
#             if height_diff > 0:
#                 possible_climbs.append((height_diff, idx+1))

#         possible_climbs.sort()

#         low = 0
#         high = num_buildings - 1

#         while low < high:
#             mid = (low + high + 1) // 2
#             if self.isReachable(mid, possible_climbs, bricks, ladders):
#                 low = mid
#             else:
#                 high = mid -1
#         return low