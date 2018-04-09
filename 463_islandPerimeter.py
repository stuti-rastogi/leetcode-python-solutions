class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if (not grid):
            return 0

        border = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    border = border + 4

                    # if i > 0 and grid[i-1][j] == 1:
                    #     border = border - 1
                    # if j > 0 and grid[i][j-1] == 1:
                    #     border = border - 1
                    # if i < m-1 and grid[i+1][j] == 1:
                    #     border = border - 1
                    # if j < n-1 and grid[i][j+1] == 1:
                    #     border = border - 1

                    if i > 0 and grid[i-1][j] == 1:
                        border = border - 2
                    if j > 0 and grid[i][j-1] == 1:
                        border = border - 2
        
        return border