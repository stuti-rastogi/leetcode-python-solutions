class Solution(object):
    def wordBreak(self, s, words):
        wordSet = set()
        for word in words:
            wordSet.add(word)

        dp = [False] * len(s)
        for i in range(len(s)):
            if dp[i - 1] or i == 0:
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] in wordSet:
                        dp[j - 1] = True
        
        return dp[-1]
#     def _word_break(self, s, words, start, seen):
#         if start == len(s):
#             return True
#         if start in seen:
#             return False
#         for i in range(start+1, len(s)+1):
#             if i in seen:
#                 continue
#             sub = s[start:i]
#             if sub in words and self._word_break(s, words, i, seen):
#                 return True
#         seen.add(start)
#         return False

#     def wordBreak(self, s, words):
#         return self._word_break(s, set(words), 0, set())