class Solution(object):
    def __init__(self):
        self.caching = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        ways = 0
        for i in range(1, 3):
            remaining_stairs = n - i
            if remaining_stairs in self.caching:
                ways += self.caching[remaining_stairs]
            else:
                result = self.climbStairs(n - i)
                self.caching[remaining_stairs] = result
                ways += result

        return ways

solution = Solution()

print(solution.climbStairs(35))
