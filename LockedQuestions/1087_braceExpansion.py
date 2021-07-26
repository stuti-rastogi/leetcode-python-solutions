class Solution:
     def expand(self, S: str) -> List[str]:
        res = []
        def helper(S, word, idx):
            if idx == len(S):
                res.append(word)
            else:
                if S[idx] == "{":
                    j = idx + 1
                    while S[j] != "}":
                        j += 1
                    for letter in sorted(S[idx+1:j].split(',')):
                        helper(S, word+letter, j+1)
                else:
                    helper(S, word + S[idx], idx+1)
        helper(S, word="", idx=0)
        return sorted(res)


#     def expand(self, s: str) -> List[str]:
#         strings = [""]
#         s_len = len(s)

#         idx = 0
#         while idx < s_len:
#             if s[idx] == '{':
#                 # look for the closing brace
#                 idx += 1
#                 possible_chars = []
#                 while s[idx] != '}':
#                     if s[idx] != ',':
#                         possible_chars.append(s[idx])
#                     idx += 1
#             else:
#                 possible_chars = [s[idx]]

#             len_strings = len(strings)
#             new_strings = []
#             for char in possible_chars:
#                 for i in range(len_strings):
#                     new_strings.append(strings[i] + char)
#             strings = new_strings
#             idx += 1

#         return sorted(strings)
