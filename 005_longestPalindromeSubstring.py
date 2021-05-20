# DP solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = ''
        maxLen = 0
        n = len(s)
        # palindrome[i][j] = True if s[i:j+1] is a palindrome
        palindrome = [[False for _ in range(n)] for _ in range(n)]

        # all substrings of length 1 are palindromes
        for i in range(n):
            palindrome[i][i] = True
            maxLen = 1
            maxPalindrome = s[i]

        # base case for length 2 substrings
        for i in range(n-1):
            if s[i] == s[i+1]:
                palindrome[i][i+1] = True
                maxPalindrome = s[i:i+2]
                maxLen = 2

        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and palindrome[i+1][j-1]:
                    palindrome[i][j] = True
                    if j-i+1 > maxLen:
                        maxPalindrome = s[i:j+1]
                        maxLen = j-i+1

        return maxPalindrome

# Expanding centers solution
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def expand(left:int, right:int):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right +=1
#             return s[left + 1:right]

#         if len(s) < 2 or s == s[::-1]:
#             return s
#         result = ''
#         for i in range(len(s) - 1):
#             # check center as between s[i] & s[i+1]
#             # check center as s[i+1] between s[i] & s[i+2]
#             result = max(result,
#                             expand(i, i+1),
#                             expand(i, i+2),
#                             key=len)
#         return result