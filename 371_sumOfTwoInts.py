class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return sum ([a,b])

        # 32 bits
        MASK = 0xFFFFFFFF
        # 2^31 - 1
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            carry = a & b
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a