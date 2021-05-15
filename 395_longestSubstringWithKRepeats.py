class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        uniqueChars = set(s)
        for c in uniqueChars:
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # all unique chars have freq >= k already
        return len(s)