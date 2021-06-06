class Solution:
    def __init__(self):
        # making this class variable so this computation is not repeated for every input
        self.counts = [0] * 32
        self.counts[0] = 1
        self.counts[1] = 2           # count of numbers with 2 bits with no consecutive ones
        for i in range(2, 32):
            # counts[n] = counts[n-1]<followed by 0> + counts[n-2]<followed by 01>
            self.counts[i] = self.counts[i-1] + self.counts[i-2]


    def findIntegers(self, n: int) -> int:
        total_nums = 0
        prev_bit = 0
        # since n is max 10^9
        i = 30

        while i >= 0:
            msb = n & (1 << i)
            if msb != 0:
                # we need to add all numbers assuming 0 here, count[i-1]
                total_nums += self.counts[i]
                if prev_bit == 1:
                    # remove this number and stop here. Any number henceforth will have consecutive ones
                    total_nums -= 1
                    break
                # update prev_bit to current
                prev_bit = 1
            else:
                prev_bit = 0
            i -= 1

        return total_nums + 1
