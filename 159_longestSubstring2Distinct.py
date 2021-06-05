class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        strlen = len(s)
        if strlen < 3:
            return strlen

        left = 0
        right = 0
        maxlen = 2
        positions = {}

        while right < strlen:
            positions[s[right]] = right
            right += 1
            if len(positions) == 3:
                # leftmost character
                leftmost_index_key = min(positions, key=positions.get)
                leftmost_index = positions[leftmost_index_key]
                positions.pop(leftmost_index_key)
                left = leftmost_index + 1
            # right + 1 already done
            maxlen = max(maxlen, right - left)

        return maxlen
