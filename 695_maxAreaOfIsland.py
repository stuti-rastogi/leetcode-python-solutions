class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= numRows or col >= numCols:
                return 0

            if not grid[row][col]:
                return 0

            grid[row][col] = 0
            area = 1

            area += dfs(row+1, col)
            area += dfs(row-1, col)
            area += dfs(row, col+1)
            area += dfs(row, col-1)
            return area


        maxArea = 0
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea
