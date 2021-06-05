class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        len_s = len(s)
        if len_s < k+1:
            return len_s

        left = 0
        right = 0
        max_len = k
        positions = {}

        while right < len_s:
            positions[s[right]] = right
            right += 1
            if len(positions) > k:
                leftmost_index_key = min(positions, key=positions.get)
                leftmost_index = positions[leftmost_index_key]
                positions.pop(leftmost_index_key)
                left = leftmost_index + 1
            max_len = max(max_len, right - left)

        return max_len
