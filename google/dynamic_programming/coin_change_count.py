"""
Given input = [1,2,5], amount = 11

Print out how many unique ways to represent the amount given the number of coins

"""

class Solution:
    def coinChangeCount(self, coins, amount):
        return self.helper(coins, amount, 0, {})

    def helper(self, coins, amount, i, memo):
        key = str(amount) + str(i)
        if i == len(coins):
            return 0
        if key in memo:
            return memo[key]
        if amount == 0:
            return 1
        if amount < 0:
            return 0

        result_left = self.helper(coins, amount - coins[i], i, memo)
        key = str(amount - coins[i]) + str(i)
        memo[key] = result_left

        result_right = self.helper(coins, amount, i + 1, memo)
        key = str(amount) + str(i + 1)
        memo[key] = result_right

        return result_left + result_right

    def coinChangeCountIterative(self, coins, amount):
        memo = [0] * (amount + 1)
        memo[0] = 1
        for coin in coins:
            for i in range(1, len(memo)):
                if i - coin >= 0:
                    memo[i] += memo[i - coin]

        return memo[-1]

solution = Solution()

print solution.coinChangeCount([1,2,5], 900)
print solution.coinChangeCountIterative([1,2,5], 1000)
