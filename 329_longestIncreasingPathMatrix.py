class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        lengths = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            lengths.append(row)

        def pathStart(i,j):
            possible = []
            
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                possible.append([i-1, j])
            if i+1 < m and matrix[i][j] < matrix[i+1][j]:
                possible.append([i+1, j])
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                possible.append([i, j-1])
            if j+1 < n and matrix[i][j] < matrix[i][j+1]:
                possible.append([i, j+1])
            
            maxLength = 1
            # we have reached end of path
            if not possible:
                return maxLength
            for x,y in possible:
                if lengths[x][y] == 0:
                    lengths[x][y] = pathStart(x,y)
                maxLength = max(maxLength, lengths[x][y]+1)
            return maxLength
        
        maxPathLen = 0
        for i in range(m):
            for j in range(n):
                if lengths[i][j] == 0:
                    lengths[i][j] = pathStart(i,j)
        
        for i in range(m):
            for j in range(n):
                maxPathLen = max(maxPathLen, lengths[i][j])
        
        return maxPathLen