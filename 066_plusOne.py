class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # result = []
        # if (not digits):
        #     return 1
        # carry = 0
        # n = len(digits)
        # for i in range(n-1, -1, -1):
        #     ans = digits[i] + carry
        #     if (i == n-1):
        #         ans += 1
        #     if (ans > 9):
        #         ans = ans % 10
        #         carry = 1
        #     else:
        #         carry = 0
        #     result.append(ans)
        # if (carry == 1 and ans == 0):
        #     result.append(1)
        # return (list(reversed(result)))
    
        n = len(digits)
        for i in range(n-1, -1, -1):
            if (digits[i] != 9):
                digits[i] += 1
                break
            digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits