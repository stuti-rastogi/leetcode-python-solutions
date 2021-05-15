class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        # use first row as "cols" array, use first column as "rows" array
        # to do that, first store what needs to be done of first row/col
        # i.e., do they contain zeroes

        firstRowZeros = False
        firstColZeros = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                firstColZeros = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZeros = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if firstRowZeros:
            for j in range(n):
                matrix[0][j] = 0
        if firstColZeros:
            for i in range(m):
                matrix[i][0] = 0

        return

############ O(m+n) space ############

#         if not matrix:
#             return
#         m = len(matrix)
#         n = len(matrix[0])

#         # O(m+n) space
#         rows = [False] * m
#         cols = [False] * n

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     rows[i] = True
#                     cols[j] = True

#         for i in range(m):
#             if rows[i]:
#                 for j in range(n):
#                     matrix[i][j] = 0

#         for j in range(n):
#             if cols[j]:
#                 for i in range(m):
#                     matrix[i][j] = 0

#         return