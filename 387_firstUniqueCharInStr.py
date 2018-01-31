class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # done = []
        # n = len(s)
        # for i in range(n):
        #     found = False
        #     if (i not in done):
        #         for j in range(i+1, n):
        #             if (s[j] == s[i]):
        #                 done.append(j)
        #                 found = True
        #         if (not found):
        #             return i
        # return -1
        
        # letters=[chr(x) for x in range(ord('a'), ord('z')+1)]
        # index=[s.index(l) for l in letters if s.count(l) == 1]
        # return min(index) if len(index) > 0 else -1
        
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])