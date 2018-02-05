class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if (not x):
        #     return x
        # ans = ""
        # if (x < 0):
        #     x = -1 * x
        #     ans = ans + "-"
        # while (x > 0):
        #     digit = x % 10
        #     ans = ans + str(digit)
        #     x = x // 10
        # ansInt = int(ans)
        # if (ansInt > (2**31 - 1) or ansInt < (-2**31)):
        #     return 0
        # return ansInt
    
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