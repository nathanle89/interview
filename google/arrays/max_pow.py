class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        is_negative = False
        if n < 0:
            is_negative = True
            n = -1 * n

        result = 1
        while n > 0:
            if n % 2:
                result *= x
            x *= x
            n /= 2

        if is_negative:
            return 1./result
        else:
            return result

solution = Solution()

print(solution.myPow(1, 222222210))
