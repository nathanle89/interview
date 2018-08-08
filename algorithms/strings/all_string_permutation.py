class Solution:
    def permutation(self, string):
        return self.permutationHelper("", string)

    def permutationHelper(self, prefix, string):
        if len(string) == 1:
            return [prefix + string]
        else:
            results = []
            for i in range(0, len(string)):
                results.extend(self.permutationHelper(prefix + string[i], string[0:i]+string[i+1:]))
            return results

solution = Solution()

print(solution.permutation("abcd"))