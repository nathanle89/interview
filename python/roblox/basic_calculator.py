class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        number = 0
        sign = 1
        stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                number = 10 * number + int(s[i])
            elif s[i] == '+':
                result += sign * number
                number = 0
                sign = 1
            elif s[i] == '-':
                result += sign * number
                number = 0
                sign = -1
            elif s[i] == '(':
                # Capture the full result and the sign
                # 12 - (......)

                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')':
                # calculate whatever inside the (...)
                # 12 - (......)
                result += sign * number
                previous_sign = stack.pop()
                previous_result = stack.pop()

                result *= previous_sign
                result += previous_result
                # Begin the next expression
                number = 0

        # Make sure we dont have anything remaining
        if number != 0:
            result += sign * number

        return result

solution = Solution()

print(solution.calculate(" 1 + 1 "))
print(solution.calculate(" 2-1 + 2 "))
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
print(solution.calculate("-1+2"))
