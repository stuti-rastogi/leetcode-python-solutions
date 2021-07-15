class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        if not cols:
            return 0

        result = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        result += 1
                    else:
                        cellValue = min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1]) + matrix[row][col]
                        result += cellValue
                        matrix[row][col] = cellValue

        return result
