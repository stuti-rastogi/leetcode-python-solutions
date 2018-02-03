class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {'{' : '}','(' : ')','[' : ']',}
        
        
        stack = []
        if (not s):
            return True
        for x in s:
            if (x in matches.keys()):
                stack.append(x)
            if (x in matches.values()):
                if (not stack):
                    return False
                check = stack.pop()
                if matches[check] != x:
                    return False
        if (stack):
            return False
        return True