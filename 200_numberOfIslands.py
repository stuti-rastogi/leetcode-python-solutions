class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            numRows = len(grid)
            numCols = len(grid[0])
            
            for nxt in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxtR = row + nxt[0]
                nxtC = col + nxt[1]
                
                if (0 <= nxtR < numRows) and (0 <= nxtC < numCols):
                    if grid[nxtR][nxtC] == "1":
                        dfs(nxtR, nxtC)
            
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num += 1
                    dfs(i, j)
                    
        return num