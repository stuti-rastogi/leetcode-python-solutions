class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # mapping = {}
        # for i in range(len(s)):
        #     for key, value in mapping.items():
        #         if (key == s[i]):
        #             if (value != t[i]):
        #                 return False
        #         else:
        #             if (value == t[i]):
        #                 if (key != s[i]):
        #                     return False
        #     mapping[s[i]] = t[i]
        # return True

        l = len(s)
        if l != len(t):
            return False
        d = {}  #mapping
        for i, letter in enumerate(s):
            if letter not in d.keys():
                d[letter] = t[i]
            else:
                if d[letter] != t[i]:
                    return False

        d2 = {}  #mapping
        for i, letter in enumerate(t):
            if letter not in d2.keys():
                d2[letter] = s[i]
            else:
                if d2[letter] != s[i]:
                    return False
        return True
