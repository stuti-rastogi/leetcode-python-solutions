class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # return int(math.sqrt(x))
        # return int(x ** 0.5)
        
        if (x == 0):
            return 0
        if (x == 1):
            return 1
        
        start = 1
        end = x
        result = 0
        
        while (start <= end):
            mid = (start + end) // 2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                end = mid - 1
            else:
                result = mid
                start = mid + 1
        return result