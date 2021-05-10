class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def findMinLength(strs):
            if not strs:
                return 0
            minLength = float('inf')
            for s in strs:
                if len(s) < minLength:
                    minLength = len(s)
            return minLength

        minLength = findMinLength(strs)
        if minLength == 0:
            return ""
        result = ""

        for pos in range(minLength):
            prefix = strs[0][pos]
            for i in range(len(strs)):
                if strs[i][pos] != prefix:
                    return result
            result += prefix
        return result


        # if not strs:
        #     return ''
        # for i, chars in enumerate(zip(*strs)):
        #     if len(set(chars)) > 1:
        #         return strs[0][:i]
        # return min(strs)