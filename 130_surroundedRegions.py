class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m , n  = len(board) , len(board[0])

        def dfs(i,j):
            if board[i][j] == "O":
                board[i][j] = 'D'
                for x , y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<m and 0<=y<n:
                        dfs(x,y) 

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for i in range(n):
            dfs(0 ,i)
            dfs(m-1 ,i)

        for i in range(m):
            for j in range(n):
                if board[i][j]== 'D' :
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"