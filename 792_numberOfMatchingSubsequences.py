class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = [[] for _ in range(26)]
        count = 0

        for word in words:
            it = iter(word)
            pos = ord(next(it))-ord('a')
            # it points here to next letter word is waiting for
            heads[pos].append(it)

        for letter in s:
            letter_pos = ord(letter)-ord('a')
            words_to_update = heads[letter_pos]
            heads[letter_pos] = []
            for word_it in words_to_update:
                next_letter = next(word_it, None)
                if next_letter:
                    pos = ord(next_letter)-ord('a')
                    heads[pos].append(word_it)
                else:
                    count += 1

        return count
