class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        # Every 5 adds one trailing zero since we have many 2s to combine with (hence / by 5)
        # Same goes for 25, 125, 625 and so on so every iteration keep dividing by 5
        # 25 has 2 5s but we add 1 per 25 since there is a repeat count from multiple of 5
        while (n > 0):
            n = n // 5
            count = count + n
        return count