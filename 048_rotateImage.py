class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # transpose and flip  
        if not matrix:
            return [[]]
        
        n = len(matrix)
        
        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # flip
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
                # matrix[i].reverse()

#          matrix[:] = zip(*matrix[::-1])
        
#         n = len(matrix)
#         result =[]
        
#         for c in range(n):
#             r = n-1
#             for i in range(n):
#                 result.append(matrix[r][c])
#                 r = r - 1
#             matrix.append(result)
#             result = []

#         for _ in range(n):
#             matrix.remove(matrix[0])