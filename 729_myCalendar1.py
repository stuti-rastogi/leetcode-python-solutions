class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book_helper(self, s, e, node):
        if node == None:
            self.root = TreeNode(s, e)
            return True

        if s >= node.end:
            if not node.right:
                node.right = TreeNode(s, e)
                return True
            else:
                return self.book_helper(s, e, node.right)
        elif e <= node.start:
            if not node.left:
                node.left = TreeNode(s, e)
                return True
            else:
                return self.book_helper(s, e, node.left)
        else:
            return False


    def book(self, start: int, end: int) -> bool:
        return self.book_helper(start, end, self.root)



# class MyCalendar:

#     def __init__(self):
#         self.bookings = []

#     def book(self, start: int, end: int) -> bool:
#         for booking_start, booking_end in self.bookings:
#             if booking_start < end and start < booking_end:
#                 return False
#         self.bookings.append((start, end))
#         return True


# # Your MyCalendar object will be instantiated and called as such:
# # obj = MyCalendar()
# # param_1 = obj.book(start,end)