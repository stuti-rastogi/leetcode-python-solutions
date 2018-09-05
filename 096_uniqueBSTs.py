class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # result = [0] * (n+1)
        # result[0] = 1
        # for i in range(1, n+1):
        #     for j in range(i):
        #         result[i] = result[i] + (result[j] * result[i - j - 1])
        # return result[n]
        
        # Catalan number
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))