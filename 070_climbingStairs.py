class Solution:
    def __init__ (self):
        self.dict = {0:0, 1:1, 2:2}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]

#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if (n <= 0):
#             return 0
#         if (n == 1):
#             return 1
#         if (n == 2):
#             return 2
        
#         # Like Fibonacci starting with 0, 1, 2
#         # to get to n
#         twoSteps = 1    # ways when we took 2 steps
#         oneStep = 2     # ways when we tool 1 step
#         for i in range(3, n+1):
#             count = oneStep + twoSteps
#             twoSteps = oneStep
#             oneStep = count
#         return count