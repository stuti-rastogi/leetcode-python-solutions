class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        len_pairs = len(pairs)
        longest_chain = [1] * len_pairs

        for index in range(len_pairs):
            for prev_index in range(index):
                if pairs[prev_index][1] < pairs[index][0]:
                    longest_chain[index] = max(longest_chain[index], longest_chain[prev_index] + 1)

        return max(longest_chain)
