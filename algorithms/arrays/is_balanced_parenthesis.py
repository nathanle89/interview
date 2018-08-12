class Solution:
    def is_balanced_paren(self, input):

        stack = []

        for char in input:
            if char == '(':
                stack.append('(')
            elif char == ')':
                if len(stack) > 0:
                    stack.pop() # pop at the end
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True

solution = Solution()

print(solution.is_balanced_paren('(()()'))
