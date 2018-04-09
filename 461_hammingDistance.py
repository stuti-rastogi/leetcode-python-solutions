class Solution:
    def hammingDistance(self, x, y):
        # x = x ^ y
        # y = 0
        # while (x):
        #     y = y + 1
        #     x = x & (x-1)
        # return y
        
        return bin(x ^ y).count('1')
        
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        