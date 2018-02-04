class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.minimum = float("Inf")
        

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#         self.minimum = min(self.minimum, x)

#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.stack.pop()
#         if (self.stack):
#             self.minimum = min(self.stack)
#         else:
#             self.minimum = float('Inf')
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         if (self.stack):
#             return self.stack[-1]
#         return -1
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.minimum

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            minVal = x
        else:
            minVal = min(self.stack[-1][1],x)
        
        self.stack.append((x,minVal))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()