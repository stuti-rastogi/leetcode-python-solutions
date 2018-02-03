class Solution:
    # def countAndSay(self, n):
    #     """
    #     :type n: int
    #     :rtype: str
    #     """
    #     s = '1'
    #     for _ in range(n - 1):
    #         s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
    #     return s
    
    def countAndSay(self, n):
        res = '1'
        for i in range(1, n):
            res = self.helper(res)
        return res

    def helper(self, s):
        if s == '':
            return s
        count = 1
        say = s[0]
        res = ''
        for i in range(1, len(s)):
            if say != s[i]:
                res += str(count) + say
                count = 1
                say = s[i]
            else:
                count += 1
        res += str(count) + say
        return res