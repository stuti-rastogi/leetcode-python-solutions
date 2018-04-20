class Solution(object):
    # do BFS till reach target
    # store length to each path
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        front = set([beginWord])
        end = set([endWord])
        wordlist = set(wordList)
        seen = set([beginWord]+[endWord])
        if endWord not in wordlist:
            return 0
        charstring = list(string.lowercase)         # all lowercase letters in alphabet
        length = 1 
        while front:
            if len(front) > len(end):
                front, end = end, front
            temp = set()
            for word in front:
                for i in range(len(word)):
                    for char in charstring:
                        newword = word[:i] + char  + word[i+1:]
                        if newword in end:
                            return length+1
                        if newword in wordlist and newword not in seen:
                            seen.add(newword)
                            temp.add(newword)
            front = temp
            length +=1
        return 0