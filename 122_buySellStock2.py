class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        if (not prices):
            return maxProfit
        currentSlice = 0
        low = prices[0]
        
        for el in prices:
            diff = el - low
            if (diff > currentSlice):
                currentSlice = diff
            else:
                maxProfit = maxProfit + currentSlice
                low = el
                currentSlice = 0
                
        return currentSlice + maxProfit