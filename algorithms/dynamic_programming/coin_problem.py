class Solution:
    def all_possible_combinations(self, n):
        # Given infinite quarters, dimes, nickels, pennies
        # Generate all possible combinations to represent n cents
        return self.helper(n, [], [25,10,5,1], 0)

    def helper(self, n, current_coins, coins, i):
        if i == len(coins) and n > 0:
            return []
        if i == len(coins) and n == 0:
            return [current_coins]

        tmp = list(current_coins)
        use_coin_i = []
        if n >= coins[i]:
            tmp.append(coins[i])
            use_coin_i.extend(self.helper(n - coins[i], tmp, coins, i))

        dont_user_coin_i = self.helper(n, current_coins, coins, i + 1)

        result = dont_user_coin_i + use_coin_i
        return result

solution = Solution()

print(solution.all_possible_combinations(10))
