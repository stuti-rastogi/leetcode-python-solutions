class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result
