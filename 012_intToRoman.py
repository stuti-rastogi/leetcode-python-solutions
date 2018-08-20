class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        nums = [1, 5, 10, 50, 100, 500, 1000]
        vals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        
        if not num:
            return ""
        
        result = ""
        i = len(vals) - 1
        while num > 0:
            quotient = num // nums[i]
            if quotient < 4:
                result = result + (quotient * vals[i])
            elif quotient == 4:
                result = result + vals[i] + vals[i+1]       # will not happen for 1000 ever, so not out of range
            elif quotient < 9:
                result = result + vals[i+1] + (vals[i] * (quotient - 5))
            else:
                result = result + vals[i] + vals[i+2]       # for 9, 90, 900
            
            num = num % nums[i]
            i = i - 2
        return result