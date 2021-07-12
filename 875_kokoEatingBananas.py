class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        def hoursToComplete(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        while start < end:
            mid = (start + end) // 2
            if hoursToComplete(mid) > h:
                start = mid +  1
            else:
                end = mid
        return start

