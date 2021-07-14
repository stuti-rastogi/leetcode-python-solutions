class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longest_chain_map = {}
        words.sort(key=len)

        longest_chain_value = 1
        for word in words:
            curr_len = 1
            for idx in range(len(word)):
                predecessor_str = word[:idx] + word[idx+1:]
                if predecessor_str in longest_chain_map:
                    predecessor_len = longest_chain_map[predecessor_str]
                else:
                    predecessor_len = 0
                curr_len = max(curr_len, predecessor_len + 1)
            longest_chain_map[word] = curr_len
            longest_chain_value = max(longest_chain_value, curr_len)
        return longest_chain_value

        # Concise
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        # return max(dp.values())