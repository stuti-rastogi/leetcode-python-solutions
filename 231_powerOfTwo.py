class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n > 0):
            return (not n & (n-1))
        return False
        
#         if (n < 1):
#             return False
        
#         b = str(bin(n))
#         b = b.replace('0b','')
#         b = b.replace('0','')
        
#         return (len(b) == 1)