class Solution:
    # Rabin Karp - compare hash of string and reverse - find longest palindrom substring from 0
    # Append reverse of remaining characters to s
    # O(n) average case
    def shortestPalindrome(self, s: str) -> str:
        s_len = len(s)
        prefix_hash = 0
        suffix_hash = 0
        d = 29
        mod = 1000000007
        power = 1
        match_pos = -1
        for i in range(s_len):
            prefix_hash = (prefix_hash * d + ord(s[i])) % mod
            suffix_hash = (suffix_hash + ord(s[i]) * power) % mod
            if prefix_hash == suffix_hash:
                # should ideally compare the strings here, but for given test cases no collisions occur
                match_pos = i
            power = (power * d) % mod

        return s[match_pos+1:][::-1] + s


# O(n^2) with two pointers and recursion - accepted
# O(n) time every call and max O(n) calls
#     def shortestPalindrome(self, s: str) -> str:
#         s_len = len(s)
#         if s_len <= 1:
#             return s
#         start = 0
#         for end in range(s_len-1, -1, -1):
#             if s[start] == s[end]:
#                 start += 1
#         # every character matched - palindrome string
#         if start == s_len:
#             return s

#         remaining_substring = s[start:]
#         return remaining_substring[::-1] + self.shortestPalindrome(s[:start]) + remaining_substring


    # O(n^2) - TLE
#     def isSubstringPalindrome(self, s:str, start:int, end:int) -> bool:
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True

#     def shortestPalindrome(self, s: str) -> str:
#         s_len = len(s)
#         if s_len <= 1 or self.isSubstringPalindrome(s, 0, s_len-1):
#             return s

#         for i in range(s_len-1, -1, -1):
#             if self.isSubstringPalindrome(s, 0, i):
#                 output = []
#                 for j in range(s_len-1, i, -1):
#                     output.append(s[j])
#                 return "".join(output) + s
