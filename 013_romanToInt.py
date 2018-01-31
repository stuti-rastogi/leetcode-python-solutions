class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        n = len(s)
        for i in range(n-1):
            val0 = values[s[i]]
            val1 = values[s[i+1]]
            if (val0 < val1):
                result = result - val0
            else:
                result = result + val0
        result = result + values[s[n-1]]
        return result