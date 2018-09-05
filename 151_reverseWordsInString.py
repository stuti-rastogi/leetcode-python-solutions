class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
        
#         s = s.strip()
#         n = len(s)
#         if not s:
#             return ""
        
#         result = ""
#         end = n-1
#         i = n - 1
#         while (i >= 0):
#             # print (i, end)
#             if s[i] == ' ':
#                 result = result + s[i+1:end+1]
#                 result = result + ' '
#                 # print (result)
#                 end = i-1
#                 while (s[end] == ' '):
#                     end = end-1
#                 i = end
#             else:
#                 i = i - 1
#         result = result + s[:end+1]
#         return result.strip()