class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        if n < 0:
            n = n * -1
            x = 1.0/x
        result = 1
        while n:
            if (n%2):
                result = result * x
            x = x * x
            n = n >> 1
        return result