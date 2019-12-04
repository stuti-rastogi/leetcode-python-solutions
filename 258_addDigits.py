class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        if num == 0:
            return 0
        else:
            return (num-1)%9 + 1

        # while True:
        #     n = num
        #     num = 0
        #     while (n > 0):
        #         num = num + n%10
        #         n = n/10
        #     if (num < 10):
        #         break
        # return num