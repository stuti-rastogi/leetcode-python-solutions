class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #return target in [element for row in matrix for element in row]
        
        # O(m+n)
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = n - 1
        while (row < m and col >= 0):
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                row = row + 1
            else:
                col = col - 1
        return False