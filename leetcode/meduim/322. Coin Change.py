from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = amount + 1
        dp = [max_value] * max_value
        dp[0] = 0

        for value in range(1, amount+1):
            for coin in coins:
                if value - coin == 0:
                    dp[value] = 1
                if value - coin > 0:
                    dp[value] = min(dp[value], dp[value - coin] + 1)

        return dp[amount] if dp[amount] < max_value else -1





s= Solution()

assert s.coinChange(coins = [1,2,5], amount = 11) == 3
assert s.coinChange(coins = [2], amount = 3) == -1
assert s.coinChange(coins = [1], amount = 0) == 0