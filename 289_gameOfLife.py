# class Solution:
#     def gameOfLife(self, board):
#         """
#         :type board: List[List[int]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
        
#         # 100 - 1 to 1
#         # 101 - 1 to 0
#         # 102 - 0 to 1
#         # 103 - 0 to 0
        
#         m = len(board)
#         n = len(board[0])
        
#         for i in range(m):
#             for j in range(n):
#                 countAliveNeighbors = 0
#                 for x in range(-1,2):
#                     for y in range(-1,2):
#                         if (x == 0 and y == 0):
#                             continue            # ignore the cell itself
#                         if (i+x >= 0 and i+x < m and j+y >= 0 and j+y < n):
#                             neighbor = board[i+x][j+y]
#                             if (neighbor == 1 or neighbor == 100 or neighbor == 101):
#                                 countAliveNeighbors = countAliveNeighbors + 1
                
#                 if (board[i][j] == 1):
#                     if (countAliveNeighbors < 2 or countAliveNeighbors > 3):
#                         board[i][j] == 101
#                     else:
#                         board[i][j] = 100
#                 else:
#                     if (countAliveNeighbors == 3):
#                         board[i][j] = 102
#                     else:
#                         board[i][j] = 103
        
#         for i in range(m):
#             for j in range(n):
#                 if (board[i][j] == 100 or board[i][j] == 102):
#                     board[i][j] = 1
#                 else:
#                     board[i][j] = 0

#class Solution:
#     def gameOfLife(self, board):
#         """
#         :type board: List[List[int]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 count = self.judge(board, i, j)
#                 #print(count)
#                 if board[i][j] & 1 and (count == 2 or count == 3):
#                     board[i][j] = 3
#                 elif (not board[i][j] & 1) and count == 3:
#                     board[i][j] = 2
           
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 board[i][j] >>= 1
        
#     def judge(self, board, m, n):
#         count = 0
#         for i in range(m-1, m+2):
#             for j in range(n-1, n+2):
#                 if 0<=i<len(board) and 0<=j<len(board[0]):
#                     if board[i][j]&1:
#                         count += 1
#         count -= board[m][n] & 1
#         return count

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getLiveNeighbors(board, x, y, m, n):
            live_count = 0
            
            if x > 0 and board[x-1][y] == 1:
                live_count += 1
            if x > 0 and y > 0 and board[x-1][y-1] == 1:
                live_count += 1
            if x > 0 and y < n and board[x-1][y+1] == 1:
                live_count += 1

            if x < m and board[x+1][y] == 1:
                live_count += 1
            if x < m and y > 0 and board[x+1][y-1] == 1:
                live_count += 1
            if x < m and y < n and board[x+1][y+1] == 1:
                live_count += 1
            
            if y > 0 and board[x][y-1] == 1:
                live_count += 1
            if y < n and board[x][y+1] == 1:
                live_count += 1
            return live_count
        
        m, n = len(board)-1, len(board[0])-1
        to_update = {}
        for i in range(m+1):
            for j in range(n+1):
                cell = board[i][j]
                neighbor_count = getLiveNeighbors(board, i, j, m, n)
                if cell == 1 and neighbor_count < 2: to_update[(i,j)] = 0
                elif cell == 1 and neighbor_count > 3: to_update[(i,j)] = 0
                elif cell == 0 and neighbor_count == 3: to_update[(i,j)] = 1
                    
        for (i, j), value in to_update.items(): board[i][j] = value