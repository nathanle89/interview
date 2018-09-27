class Solution:
    def nums_subsets(self, X, total):
        return self.helper(X, total, {})

    def helper(self, X, total, mem):
        length_set = len(X)
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif length_set == 0:
            return 0

        ways = 0
        for i in range(0, length_set):
            key = str(i) + str(total - X[i])
            if key in mem:
                out = mem[key]
            else:
                out = self.nums_subsets(X[i+1:], total - X[i])
                mem[key] = out

            ways += out

        return ways

solution = Solution()

print(solution.nums_subsets([2,4,6,10,9,1], 16))
