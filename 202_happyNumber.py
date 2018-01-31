class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash_set = set()
        
        while True:
            calc_num = 0
            while n > 0:
                mod = n % 10
                calc_num += mod * mod
                n //= 10
            
            if calc_num == 1:
                return True
            
            if calc_num in hash_set:
                return False
            else:
                hash_set.add(calc_num)
                n = calc_num
                
                
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