class Solution:
    def isValidSudoku(self, board):
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i, c),(i//3,j//3,c)]
        return len(seen) == len(set(seen))

        # return (self.is_row_valid(board) and
        #         self.is_col_valid(board) and
        #         self.is_square_valid(board))

#     def is_row_valid(self, board):
#         for row in board:
#             if not self.is_unit_valid(row):
#                 return False
#         return True

#     def is_col_valid(self, board):
#         for col in zip(*board):
#             if not self.is_unit_valid(col):
#                 return False
#         return True

#     def is_square_valid(self, board):
#         for i in (0, 3, 6):
#             for j in (0, 3, 6):
#                 square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#                 if not self.is_unit_valid(square):
#                     return False
#         return True

#     def is_unit_valid(self, unit):
#         unit = [i for i in unit if i != '.']
#         return len(set(unit)) == len(unit)