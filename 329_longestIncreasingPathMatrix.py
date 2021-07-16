class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(matrix)
        cols = len(matrix[0])

        path_len = [[0 for _ in range(cols)] for _ in range(rows)]
        max_path_len = 0

        def dfs(row, col):
            if path_len[row][col] != 0:
                return path_len[row][col]

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (0 <= new_row < rows and 0 <= new_col < cols
                    and matrix[new_row][new_col] > matrix[row][col]):
                    path_len[row][col] = max(path_len[row][col], dfs(new_row, new_col))

            path_len[row][col] += 1
            return path_len[row][col]

        for row in range(rows):
            for col in range(cols):
                max_path_len = max(max_path_len, dfs(row, col))

        return max_path_len
