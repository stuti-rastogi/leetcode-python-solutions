class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num += 1
        res = [0, 1]
        while (len(res) < num):
            res += [n+1 for n in res]
        return res[:num]
    
        # return [bin(i).count('1') for i in range(num+1)]