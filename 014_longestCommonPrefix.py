class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if (not strs):
        #     return ""
        # n = len(strs)
        # for x in strs:
        #     if (not x):
        #         return ""
        # toCheck = strs[0][0]
        # result = ""
        # pos = 0
        # while (True):
        #     i = 0
        #     for i in range(n):
        #         if (len(strs[i])) <= pos:
        #             return result
        #         if (strs[i][pos] != toCheck):
        #             return result
        #         if (i == n-1):
        #             result = result + toCheck
        #             if (pos == len(strs[0])-1):
        #                 return result
        #             toCheck = strs[0][pos+1]
        #             pos = pos + 1
        # return result
        
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)