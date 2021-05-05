class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while (True):
            sumOfSquaredDigits = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                sumOfSquaredDigits += digit**2
            if sumOfSquaredDigits == 1:
                return True
            if sumOfSquaredDigits in seen:
                return False
            seen.add(sumOfSquaredDigits)
            n = sumOfSquaredDigits


#         seen = []
#         while (True):
#             print (seen)
#             digits = self.getDigits(n)
#             total = 0
#             print ("Digits: " + str(digits))
#             for i in digits:
#                 total += int(pow(i,2))
#             if (total in seen):
#                 return False
#             if (total == 1):
#                 return True
#             seen.append(total)
#             n = total
            
    
#     def getDigits(self, n):
#         digits = []
#         while (n > 0):
#             digits.append(n%10)
#             n = n//10
#         return digits