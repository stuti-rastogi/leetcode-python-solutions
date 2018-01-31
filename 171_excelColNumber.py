class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        power = n-1
        result = 0
        for i in range(n):
            value = ord(s[i])-64
            result = result + (value * pow(26, power))
            power = power - 1
        return result  