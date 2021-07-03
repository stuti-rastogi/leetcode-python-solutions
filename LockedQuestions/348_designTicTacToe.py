class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            value = 1
        else:
            value = -1
        self.rows[row] += value
        self.cols[col] += value
        if row == col:
            self.diagonal += value
        if row + col == self.n - 1:
            self.antidiagonal += value
                
        if (
                abs(self.rows[row]) == self.n 
                or abs(self.cols[col]) == self.n 
                or abs(self.diagonal) == self.n
                or abs(self.antidiagonal) == self.n
            ):
            return player
        
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)