class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return bin(n).count('1')

        # Without Python functions
        count = 0
        while n:
            n = n & (n-1)
            count = count + 1
        return count