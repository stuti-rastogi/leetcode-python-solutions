class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if not x:
        #     return x
        # sign = x // abs(x)
        # output = 0
        # x = abs(x)
        # while x:
        #     x, digit = divmod(x, 10)
        #     output = (10 * output) + digit
        #     if output > (2**31 - 1):
        #         return 0
        # return sign * output


        neg = False
        if x < 0:
            x = -x
            neg = True

        y = str(x)[::-1]
        x = int(y)
        if neg:
            x = -x

        if x > 2**31-1 or x < -(2**31):
            x = 0

        return x