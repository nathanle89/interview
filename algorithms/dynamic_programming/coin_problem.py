class Solution:
    def all_possible_combinations(self, n):
        # Given infinite quarters, dimes, nickels, pennies
        # Generate all possible combinations to represent n cents
        return self.helper(n, (), 25)

    def helper(self, n, current_tuple, denom):
        if denom == 25:
            next_denom = 10
        elif denom == 10:
            next_denom = 5
        elif denom == 5:
            next_denom = 1
        else:
            for i in range(0, n):
                current_tuple += (1,)
            return [list(current_tuple)]

        i = 0
        ways = []
        while i * denom <= n:
            new_tupe = current_tuple

            for j in range(0, i):
                new_tupe += (denom,)

            ways.extend(self.helper(n - i * denom, new_tupe, next_denom))
            i += 1

        return ways

solution = Solution()

print(len(solution.all_possible_combinations(200)))
