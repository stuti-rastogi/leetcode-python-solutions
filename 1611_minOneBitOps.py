import math

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        k = int(math.log2(n))
        total_steps = 2 ** (k+1) - 1
        remaining_steps = self.minimumOneBitOperations(n - (1 << k))
        return total_steps - remaining_steps
