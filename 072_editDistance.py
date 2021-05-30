class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1Len = len(word1)
        # word2Len = len(word2)

        # minimumChanges = [[0 for _ in range(word2Len+1)] for _ in range(word1Len+1)]

        # for i in range(word1Len+1):
        #     for j in range(word2Len+1):
        #         if i == 0:
        #             minimumChanges[i][j] = j
        #         elif j == 0:
        #             minimumChanges[i][j] = i
        #         elif word1[i-1] == word2[j-1]:
        #             minimumChanges[i][j] = minimumChanges[i-1][j-1]
        #         else:
        #             minimumChanges[i][j] = 1 + min(
        #                                     minimumChanges[i-1][j-1], 
        #                                     minimumChanges[i][j-1],
        #                                     minimumChanges[i-1][j]
        #                                     )

        # return minimumChanges[word1Len][word2Len]

        # Optimized - only O(n) storage
        word1Len = len(word1)
        word2Len = len(word2)
        
        minimumChanges = [[0 for _ in range(word2Len+1)] for _ in range(2)]
        
        
        for i in range(word1Len+1):
            for j in range(word2Len+1):
                if i == 0:
                    minimumChanges[i%2][j] = j
                elif j == 0:
                    minimumChanges[i%2][j] = i
                elif word1[i-1] == word2[j-1]:
                    minimumChanges[i%2][j] = minimumChanges[(i-1)%2][j-1]
                else:
                    minimumChanges[i%2][j] = 1 + min(
                                            minimumChanges[(i-1)%2][j-1], 
                                            minimumChanges[i%2][j-1],
                                            minimumChanges[(i-1)%2][j]
                                            )
                    
        return minimumChanges[word1Len%2][word2Len]

        # Recursive
        # memo = {}
        # def dfs(x,y,m,n):
        #     if (m,n) in memo:
        #         return memo[(m,n)]
        #     if m == 0:
        #         return n
        #     elif n == 0:
        #         return m
        #     if x[m-1] == y[n-1]:
        #         memo[(m,n)] = dfs(x,y,m-1,n-1)
        #     else:
        #         memo[(m,n)] = 1 + min(dfs(x,y,m,n-1), dfs(x,y,m-1,n), dfs(x,y,m-1,n-1))
        #     return memo[(m,n)]
        # return dfs(word1, word2, len(word1), len(word2))
