class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [0] * (cols + 1)
        maxSquareLen = 0
        prev = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                curr = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    maxSquareLen = max(maxSquareLen, dp[j])
                else:
                    dp[j] = 0
                prev = curr

        return maxSquareLen * maxSquareLen
