class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0

        for coin in coins:
            for amt in range(coin, amount + 1):
                amounts[amt] = min(amounts[amt], amounts[amt - coin] + 1)

        if amounts[amount] == float('inf'):
            return -1
        return amounts[amount]
