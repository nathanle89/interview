class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        self.backtrack(ans, '', 0, 0, N)
        return ans

    def backtrack(self, answers, current_string, left, right, N):
        if len(current_string) == 2 * N:
            answers.append(current_string)
            return
        if left < N:
            self.backtrack(answers, current_string + '(', left+1, right, N)
        if right < left:
            self.backtrack(answers, current_string + ')', left, right+1, N)

solution = Solution()

print solution.generateParenthesis(3)