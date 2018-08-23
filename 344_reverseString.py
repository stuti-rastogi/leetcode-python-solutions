class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # return s[::-1]
        result = ""
        if not s:
            return result
        n = len(s)
        for i in range(n-1, -1, -1):
            result = result + (s[i])
        return result