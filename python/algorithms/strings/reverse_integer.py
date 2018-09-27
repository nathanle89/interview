class Solution:
    def reverseInteger(self, integer):
        lower_limit = 2**31 * -1
        upper_limit = 2**31 - 1

        string_integer = str(abs(integer))
        result = int(string_integer[::-1])

        if integer < 0:
            result *= -1

        if result > upper_limit or result < lower_limit:
            return 0

        return result

solution = Solution()

print(solution.reverseInteger(-210))
