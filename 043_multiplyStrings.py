class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1) * int(num2))
        
        if '0' in (num1, num2):
            return '0'
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m):
            for j in range(n):
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                res[i+j+1] += (d1*d2)%10
                res[i+j] += (d1*d2)//10
        for i in range(m + n - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] = res[i] % 10
        return ''.join(str(x) for x in res) if res[0] else ''.join(str(x) for x in res[1:])