import bisect

class MyCalendarTwo:
    """
    Similar approach as for Cal III

    Track unique start, end times in a list that can be binary searched

    Model processing of insert as 2 steps:

    1) processing of a new unique time by "inheriting" existing overlap its containing context
    2) account for new overlaps due to adding the new interval
    """

    def __init__(self):
        self.timeline = []
        self.overlap_cnt = {}

    def book(self, start: int, end: int) -> bool:
        start_idx = bisect.bisect_left(self.timeline, start)
        end_idx = bisect.bisect_left(self.timeline, end)

        for idx in range(start_idx, end_idx):
            val = self.timeline[idx]
            if self.overlap_cnt[val] >= 2:
                return False

        if start not in self.overlap_cnt:
            # Initialize start count same as prev element
            # For current interval being added, count of all points
            # overlapping it will be incremented in last line, not here
            self.overlap_cnt[start] = self.overlap_cnt[self.timeline[start_idx-1]] if (start_idx-1) >= 0 else 0
            self.timeline.insert(start_idx, start)
            # account for insertion of start
            end_idx +=1

        if end not in self.overlap_cnt:
            self.overlap_cnt[end] = self.overlap_cnt[self.timeline[end_idx-1]]
            self.timeline.insert(end_idx, end)

        # Increment EVERY point in between start_idx and end_idx
        # signifying that new interval overlapped these points
        for idx in range(start_idx, end_idx):
            val = self.timeline[idx]
            if self.overlap_cnt[val] + 1 >= 3:
                return False
            self.overlap_cnt[val] += 1
        return True






# class MyCalendarTwo:

#     def __init__(self):
#         self.bookings = []
#         self.double_bookings = []

#     def book(self, start: int, end: int) -> bool:
#         for event_start, event_end in self.double_bookings:
#             if start < event_end and end > event_start:
#                 return False
#         for booking_start, booking_end in self.bookings:
#             if start < booking_end and end > booking_start:
#                 self.double_bookings.append((max(start, booking_start), min(end, booking_end)))
#         self.bookings.append((start, end))
#         return True


# # Your MyCalendarTwo object will be instantiated and called as such:
# # obj = MyCalendarTwo()
# # param_1 = obj.book(start,end)