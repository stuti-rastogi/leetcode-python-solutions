class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def wordBreakRecursive(s):
            if s in memo:
                return memo[s]
            if not s:
                return []
            
            output = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                elif len(word) == len(s):
                    output.append(word)
                else:
                    remainingOutput = wordBreakRecursive(s[len(word):])
                    for words in remainingOutput:
                        output.append(word + ' ' + words)
            memo[s] = output
            return output
            
        return wordBreakRecursive(s)
