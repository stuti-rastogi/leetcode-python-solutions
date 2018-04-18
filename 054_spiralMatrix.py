class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    
        result = []
        if not matrix:
            return result
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        while (len(result) < m*n):
            i = top
            for j in range(left, right+1):
                result.append(matrix[i][j])
            top = top+1
            if (len(result) == m*n):
                break
            for i in range(top, bottom+1):
                result.append(matrix[i][j])
            right = right-1
            if (len(result) == m*n):
                break
            for j in range(right,left-1,-1):
                result.append(matrix[i][j])
            bottom = bottom-1
            if (len(result) == m*n):
                break
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][j])
            left = left+1
            if (len(result) == m*n):
                break
        
        return result
                