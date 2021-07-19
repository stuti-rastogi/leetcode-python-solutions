import bisect

class MyCalendarThree:
    def __init__(self):
        self.timeline = []
        self.overlap_count = {}
        self.max_overlap = 0

    def book(self, start: int, end: int) -> int:
        start_idx = bisect.bisect_left(self.timeline, start)
        end_idx = bisect.bisect_left(self.timeline, end)

        if start not in self.overlap_count:
            prev_start_count = self.overlap_count[self.timeline[start_idx-1]] if (start_idx-1) >= 0 else 0
            self.overlap_count[start] = prev_start_count
            self.timeline.insert(start_idx, start)
            end_idx += 1

        if end not in self.overlap_count:
            prev_end_count = self.overlap_count[self.timeline[end_idx-1]] if (end_idx-1) >= 0 else 0
            self.overlap_count[end] = prev_end_count
            self.timeline.insert(end_idx, end)

        for idx in range(start_idx, end_idx):
            val = self.timeline[idx]
            self.overlap_count[val] += 1
            self.max_overlap = max(self.max_overlap, self.overlap_count[val])

        return self.max_overlap
