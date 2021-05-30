class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        seen = set()
        uniqueIslands = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= numRows or col >= numCols:
                return
            if (row, col) in seen or not grid[row][col]:
                return

            seen.add((row, col))
            currentIsland.append((row-startRow, col-startCol))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(numRows):
            for col in range(numCols):
                currentIsland = []
                startRow = row
                startCol = col
                dfs(row, col)
                if currentIsland:
                    # need to change to tuple so it is hashable and can be added to set
                    uniqueIslands.add(tuple(currentIsland))

        return len(uniqueIslands)


# class Solution:
#     def numDistinctIslands(self, grid: List[List[int]]) -> int:
#         # Do a DFS to find all cells in the current island.
#         def dfs(row, col, direction):
#             if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
#                 return
#             if (row, col) in seen or not grid[row][col]:
#                 return
#             seen.add((row, col))
#             path_signature.append(direction)
#             dfs(row + 1, col, "D")
#             dfs(row - 1, col, "U")
#             dfs(row, col + 1, "R")
#             dfs(row, col - 1, "L")
#             path_signature.append("0")

#         # Repeatedly start DFS's as long as there are islands remaining.
#         seen = set()
#         unique_islands = set()
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 path_signature = []
#                 dfs(row, col, "0")
#                 if path_signature:
#                     unique_islands.add(tuple(path_signature))

#         return len(unique_islands)
