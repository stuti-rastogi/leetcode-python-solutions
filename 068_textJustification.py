class Solution:
    def _breakIntoLines(self, words: List[str], maxWidth: int) -> List[List[str]]:
        allLines = []
        charCount = 0
        # list of strings for easy append
        currLine = []

        for word in words:
            wordLen = len(word)
            if wordLen + charCount > maxWidth:
                # start a new line
                allLines.append(currLine)
                charCount = 0
                currLine = []
            currLine.append(word)
            charCount += (wordLen+1)

        allLines.append(currLine)
        return allLines


    def _generateSpaces(self, line: List[str], idx: int, numLines: int, maxWidth: int) -> List[str]:
        spaces = maxWidth - sum([len(word) for word in line])
        numWords = len(line)
        countSpaces = numWords - 1

        # both these cases need left justification
        if numWords > 1 and idx != numLines-1:
            minSpace = spaces // countSpaces
            remainingSpaces = spaces - (minSpace * countSpaces)
            spacesToFill = [minSpace for _ in range(countSpaces)]
            for x in range(remainingSpaces):
                spacesToFill[x] += 1
            # for the last word
            spacesToFill.append(0)
        else:
            # left justified cases
            extraSpace = spaces - countSpaces
            spacesToFill = [1 for _ in range(countSpaces)]
            # for the last word, fill remaining width with space
            spacesToFill.append(extraSpace)

        return spacesToFill


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        allLines = self._breakIntoLines(words, maxWidth)
        numLines = len(allLines)
        for idx, line in enumerate(allLines):
            spacesToFill = self._generateSpaces(line, idx, numLines, maxWidth)
            newLine = []
            for j, word in enumerate(line):
                newLine.append(word)
                newLine.append(' ' * spacesToFill[j])
            allLines[idx] = newLine

        return list(map(lambda x: ''.join(x), allLines))