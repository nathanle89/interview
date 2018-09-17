class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n, {})

    def helper(self, n, memo):
        if n == 1:
            return 1

        if n == 2:
            return 2

        ways = 0
        for i in range(1, 3):
            remaining_stairs = n - i
            if remaining_stairs in memo:
                ways += memo[remaining_stairs]
            else:
                result = self.helper(n - i, memo)
                memo[remaining_stairs] = result
                ways += result

        return ways

solution = Solution()

print(solution.climbStairs(5))
