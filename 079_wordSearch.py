class Solution:
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

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def possible(i, j, m, n):
            pos = []
            if 0 <= i - 1:
                pos.append((i-1, j))
            if i + 1 < m:
                pos.append((i + 1, j))
            if 0 <= j - 1:
                pos.append((i, j-1))
            if j + 1 < n:
                pos.append((i, j + 1))
            return pos
        
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        l = len(word)
        if l == 0:
            return False
        
        def find(count, i, j, m, n, l):
            if count == l - 1:
                return True
            pos = possible(i, j, m, n)
            for x, y in pos:
                if board[x][y] == word[count + 1]:
                    board[x][y] = None
                    if find(count + 1, x, y, m, n, l):
                        return True
                    board[x][y] = word[count + 1]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = None
                    if find(0, i, j, m, n, l):
                        return True
                    board[i][j] = word[0]
        return False