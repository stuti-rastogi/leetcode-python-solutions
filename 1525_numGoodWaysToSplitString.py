class Solution:
    def numSplits(self, s: str) -> int:
        s_len = len(s)
        num_splits = 0
        first_str_map = {}
        second_str_map = {}

        for c in s:
            if c not in second_str_map:
                second_str_map[c] = 0
            second_str_map[c] += 1
        for char_idx in range(s_len-1):
            curr_char = s[char_idx]
            if curr_char not in first_str_map:
                first_str_map[curr_char] = 0
            first_str_map[curr_char] += 1

            second_str_map[curr_char] -= 1
            if second_str_map[curr_char] == 0:
                second_str_map.pop(curr_char)

            if len(first_str_map) == len(second_str_map):
                num_splits += 1

        return num_splits
