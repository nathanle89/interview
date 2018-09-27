import resource, sys
sys.setrecursionlimit(10**6)

class Solution(object):
    def fibonacci(self, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if k == 0:
            return 0
        elif k == 1:
            return 1
        elif k == 2:
            return 1

        n_minus_one_val = 1
        n_minus_two_val = 1
        result = 0
        for i in range(2, k):
            result = n_minus_two_val + n_minus_one_val
            n_minus_two_val = n_minus_one_val
            n_minus_one_val = result

        return result

    def fibonacciDP(self, k):
        return self.helper(k, {})

    def helper(self, k, memo):
        if k in memo:
            return memo[k]
        if k == 0:
            return 0
        elif k == 1:
            return 1
        elif k == 2:
            return 1

        left = self.helper(k - 1, memo)
        memo[k - 1] = left

        right = self.helper(k - 2, memo)
        memo[k - 2] = right

        return left + right


solution = Solution()

print(solution.fibonacci(1500))
print(solution.fibonacciDP(1500)) ## BANH DZU stack overflow
