class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        len_search_word = len(searchWord)
        for i, word in enumerate(words):
            if word[:len_search_word] == searchWord:
                return i+1
        return -1