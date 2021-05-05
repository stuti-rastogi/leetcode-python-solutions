class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = {0: 0, 1: 1, 2: 2}
        # Top-Down
        return self.climbStairsRec(n, dp)

        # Bottom-Up
        # for i in range(n+1):
        #     if i not in dp:
        #         dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]


    def climbStairsRec(self, n, dp):
        if n in dp:
            return dp[n]
        dp[n] = self.climbStairsRec(n-1, dp) + self.climbStairsRec(n-2, dp)
        return dp[n]]


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