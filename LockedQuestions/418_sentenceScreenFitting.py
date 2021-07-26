class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence_with_spaces = ' '.join(sentence) + ' '
        sentence_len = len(sentence_with_spaces)
        sentence_ptr = 0
        for i in range(rows):
            # last char for this row
            sentence_ptr += cols-1
            if sentence_with_spaces[sentence_ptr % sentence_len] == ' ':
                # we ended on a space - move to next line with next char
                sentence_ptr += 1
            elif sentence_with_spaces[(sentence_ptr+1) % sentence_len] == ' ':
                 # next char is a space, we ended on last letter of a word -
                 # move to next line with first letter of next word skipping the space
                sentence_ptr += 2
            else:
                # ended in the middle of a word - need to go back to beginning of this word
                while sentence_ptr > 0 and sentence_with_spaces[(sentence_ptr-1) % sentence_len] != ' ':
                    sentence_ptr -= 1

        return sentence_ptr // sentence_len
