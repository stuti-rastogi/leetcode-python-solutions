class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP solution, O(mn) time and space
#         count = []
#         for i in range(m):
#             count.append([])
#             for j in range(n):
#                 count[i].append(0)
        
#         for i in range(m):
#             for j in range(n):
#                 if (i == 0 and j == 0):
#                     count[i][j] = 1
#                 else:
#                     count[i][j] = count[i-1][j] + count[i][j-1]
#         return count[m-1][n-1]

		# Math solution
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)