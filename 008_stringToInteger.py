class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            is_negative = True
            start_index = 1
        elif s[0] == '+':
            is_negative = False
            start_index = 1
        else:
            is_negative = False
            start_index = 0

        str_len = len(s)

        value = 0
        for index in range(start_index, str_len):
            if not s[index].isdigit():
                break
            digit_val = ord(s[index]) - ord('0')
            value = (value * 10) + digit_val

        if is_negative:
            value *= -1

        # Value will not overflow because python3 does not technically have restriction on size
        # Cannot use sys.maxint as that is for 64 bit
        max_val = 2**31 - 1
        min_val = -2**31

        if value < min_val:
            value = min_val

        if value > max_val:
            value = max_val

        return value

