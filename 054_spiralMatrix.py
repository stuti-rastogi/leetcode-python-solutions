class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        result = []
        aimNumber = m * n

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        while True:
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top = top + 1
            if len(result) == aimNumber:
                return result

            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right = right - 1
            if len(result) == aimNumber:
                return result

            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
            bottom = bottom - 1
            if len(result) == aimNumber:
                return result

            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
            left = left + 1
            if len(result) == aimNumber:
                return result
