"""
Given input = [1,2,5], amount = 11

Print out minimum coin required to represent the amount given the number of coins

"""

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def coinChange(self, coins, amount):
        return self.helper(coins, amount, {})

    def helper(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]

        minimum = (2**31) - 1
        for coin in coins:
            intermediate = self.helper(coins, amount - coin, memo)
            if intermediate >= 0 and intermediate < minimum:
                minimum = intermediate + 1

        if minimum == (2**31) - 1:
            result = -1
        else:
            result = minimum

        memo[amount] = result

        return result

solution = Solution()

print solution.coinChange([1, 2], 4)




