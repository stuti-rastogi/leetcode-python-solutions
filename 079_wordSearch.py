# class Solution:
#     def dfs(self, board, i, j, word):
#         if (len(word) == 0):
#             return True
        
#         m = len(board)
#         n = len(board[0])
        
#         if (i < 0 or i >= m or j < 0 or j >= n):
#             return False
#         if (word[0] != board[i][j]):
#             return False
        
#         curr = board[i][j]
#         board[i][j] = '*'         # to avoid checking again
        
#         # check all 4 directions
#         result = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        
#         board[i][j] = curr
#         return result
    
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         if (not board or not word):
#             return False
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if (board[i][j] == word[0]):
#                     if (self.dfs(board, i, j, word)):
#                         return True
        
#         return False  

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        wordLen = len(word)
        if not rows or not cols or not wordLen:
            return False

        # pos is last found index in word
        def findPath(i, j, pos):
            # already done
            if pos == wordLen-1:
                return True

            neighbors = []
            if (i-1) >= 0:
                neighbors.append([i-1,j])
            if (i+1) < rows:
                neighbors.append([i+1, j])
            if (j-1) >= 0:
                neighbors.append([i,j-1])
            if (j+1) < cols:
                neighbors.append([i,j+1])

            for x,y in neighbors:
                if board[x][y] == word[pos+1]:
                    board[x][y] = None
                    if findPath(x, y, pos+1):
                        return True
                    board[x][y] = word[pos+1]
            return False


        for i in range(rows):
            for j in range(cols):
                # this position could be possible starting point of word
                if board[i][j] == word[0]:
                    # so it can't be reused
                    board[i][j] = None
                    if findPath(i, j, 0):
                        return True
                    # reset
                    board[i][j] = word[0]
        return False