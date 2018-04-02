class Solution(object):
    store = [0]
    def numSquares(self, n):
        dp = self.store
        while (len(dp) <= n):
            dp = dp + min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]