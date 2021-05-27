class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        positive = (dividend < 0) is (divisor < 0) # 1
        dividend, divisor = abs(dividend), abs(divisor) # 2
        res = 0 # 3

        while dividend >= divisor: # 4
            curr_divisor, num_divisors = divisor, 1 # 5
            while dividend >= curr_divisor: # 6
                dividend -= curr_divisor # 7
                res += num_divisors # 8 
                curr_divisor += curr_divisor # 9
                num_divisors += num_divisors # 10

        if not positive: # 11
            res = -res # 12

        return res
