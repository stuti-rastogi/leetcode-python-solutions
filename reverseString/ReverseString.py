class ReverseString(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # faster solution
        s1 = list(s)
        s1.reverse()
        return ''.join(s1)

        # alternate solution
        # return s[::-1]		# -1 steps in reverse