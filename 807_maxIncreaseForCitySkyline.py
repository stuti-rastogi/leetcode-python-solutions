class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        left = [max(x) for x in grid]
        top = [max([_[i] for _ in grid]) for i in range(len(grid[0]))]
        inc = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                inc = inc + min(left[i], top[j]) - grid[i][j]
        return inc