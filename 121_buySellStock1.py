class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        low = float('inf')
        for price in prices:
            low = min(low, price)
            profit = price - low
            maxProfit = max(maxProfit, profit)
        return maxProfit
