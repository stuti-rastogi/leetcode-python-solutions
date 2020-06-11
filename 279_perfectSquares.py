class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0

        # dp[i] is answer for i
        dp = [0]

        # need dp[n]
        for i in range(1,n+1):
            # we want to see if we can do better than adding 'i' 1s
            minCount = i
            # j is the perfect square's root that we subtract, max it can be is i's square root
            # anything larger will give a negative index
            for j in range(1,int(i**0.5)+1):
                # either we have best, or we can subtract a perfect square and get a better result
                minCount = min(minCount, dp[i-(j*j)] + 1)
            dp.append(minCount)
        return dp[n]