# Space optimized, instead of m*n space of entire matrix, use only 2 rows
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        text1_len = len(text1)
        text2_len = len(text2)

        curr_row = [0 for _ in range(text1_len)]
        prev_row = [0 for _ in range(text1_len)]

        for idx2 in range(text2_len):
            for idx1 in range(text1_len):
                if text1[idx1] == text2[idx2]:
                    prev_val = prev_row[idx1-1] if (idx1 >= 1) else 0
                    curr_row[idx1] = prev_val + 1
                else:
                    prev_val1 = prev_row[idx1]
                    prev_val2 = curr_row[idx1-1] if idx1 >= 1 else 0
                    curr_row[idx1] = max(prev_val1, prev_val2)
            prev_row, curr_row = curr_row, prev_row

        return prev_row[text1_len-1]
