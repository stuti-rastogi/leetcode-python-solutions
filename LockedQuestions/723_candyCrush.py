class Solution:
    def isStable(self, board, numRows, numCols):
        positions = set()
        for row in range(numRows):
            for col in range(numCols):
                if board[row][col]:
                    if col > 1 and (board[row][col] == board[row][col-1] == board[row][col-2]):
                        positions = positions.union({(row, col), (row, col-1), (row, col-2)})
                        # positions.add((row, col))
                        # positions.add((row, col-1))
                        # positions.add((row, col-2))
                    if row > 1 and (board[row][col] == board[row-1][col] == board[row-2][col]):
                        positions = positions.union({(row, col), (row-1, col), (row-2, col)})
                        # positions.add((row, col))
                        # positions.add((row-1, col))
                        # positions.add((row-2, col))

        return positions

    def crush(self, board, positions):
        for (row, col) in positions:
            board[row][col] = 0

    def fall(self, board, numRows, numCols):
        for col in range(numCols):
            # start from bottom most 0
            zeroIdx = numRows-1
            for row in range(numRows-1, -1, -1):
                if board[row][col]:
                    board[zeroIdx][col] = board[row][col]
                    zeroIdx -= 1

            for row in range(zeroIdx+1):
                board[row][col] = 0


    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        numRows = len(board)
        numCols = len(board[0])

        while True:
            positions = self.isStable(board, numRows, numCols)
            if not positions:
                break

            self.crush(board, positions)
            self.fall(board, numRows, numCols)

        return board
