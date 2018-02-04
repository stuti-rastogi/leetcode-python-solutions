class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        # return int(format(n, '032b')[::-1], 2)
        
        output = 0
        for _ in range(32):
            b = n % 2
            output = output * 2 + b
            n = n / 2
        return output