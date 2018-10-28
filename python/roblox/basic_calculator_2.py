class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        number = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                number = 10 * number + int(s[i])
            elif s[i] == '+':
                stack.append(number)
                number = 0
            elif s[i] == '-':
                stack.append(-number)
                number = 0
            elif s[i] == '*':
                stack[-1] *= number
                number = 0
            elif s[i] == '/':
                stack[-1] /= number
                number = 0

        result = sum(stack)
        return result

solution = Solution()
print solution.calculate("1 + 2 * 3")
