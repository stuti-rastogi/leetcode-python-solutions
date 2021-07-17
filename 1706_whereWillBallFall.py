class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        '''
            grid[i][j] == 1:
                grid[i][j+1] == 1 -> True
                grid[i][j+1] == -1 -> False
            grid[i][j] == -1:
                grid[i][j-1] == 1 -> False
                grid[i][j-1] == -1 -> True
        '''

        rows = len(grid)
        cols = len(grid[0])

        possible_path = {}

        def go_down(row, col):
            if (row, col) in possible_path:
                return possible_path[(row, col)]

            if row == rows:
                possible_path[(row, col)] = col
                return possible_path[(row, col)]

            if (col == 0 and grid[row][col] == -1) or (col == cols-1 and grid[row][col] == 1):
                possible_path[(row, col)] = -1
                return possible_path[(row, col)]

            if grid[row][col] == 1:
                possible_path[(row, col)] = go_down(row+1, col+1) if grid[row][col+1] == 1 else -1
            else:
                possible_path[(row, col)] = go_down(row+1, col-1) if grid[row][col-1] == -1 else -1

            return possible_path[(row, col)]


        output = [-1 for _ in range(cols)]
        for col in range(cols):
            output[col] = go_down(0, col)

        return output
