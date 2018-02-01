class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # while (n > 1):
        #     n = n / 3
        # if (n == 1):
        #     return True
        # return False
        
        return n > 0 and 1162261467 % n == 0