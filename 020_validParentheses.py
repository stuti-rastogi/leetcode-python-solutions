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

# cleaner and faster
# class Solution:
#     def isValid(self, s: str) -> bool:
#         pairs = {')':'(', '}':'{', ']':'['}
#         stack = []
#         for c in s:
#             if c not in pairs:
#                 stack.append(c)
#             else:
#                 if stack and stack[-1] == pairs[c]:
#                     stack.pop()
#                 else:
#                     return False
#         return stack == []