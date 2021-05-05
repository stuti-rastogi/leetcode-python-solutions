class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # METHOD I: Python functions
        # return int(format(n, '032b')[::-1], 2)

        # METHOD II: Arithmetic
        output = 0
        for _ in range(32):
            b = n % 2
            output = output * 2 + b
            n = n / 2
        return output

        # METHOD III: Bit manipulation
        reverse = 0
        power = 31
        while n:
            bit = n & 1
            reverse = reverse | (bit << power)
            n = n >> 1
            power -= 1
        return reverse