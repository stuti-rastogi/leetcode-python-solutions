class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        lh = len(haystack)
        ln = len(needle)

        if not needle:
            return 0
        if not haystack or lh < ln:
            return -1

        index = 0
        if needle in haystack:
            first = needle[0]
            for c in haystack:
                if c == first:
                    if haystack[index:index+ln] == needle:
                        return index
                index = index + 1
        return -1