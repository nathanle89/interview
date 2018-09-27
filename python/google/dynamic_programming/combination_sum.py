"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
    [7],
    [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
    [2,2,2,2],
    [2,3,3],
    [3,5]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(candidates, [], 0, target, {})

    def helper(self, candidates, current_combination, i, target, memo):
        if target == 0:
            return [current_combination]
        # if key in memo:
        #     return memo[key]
        if i == len(candidates):
            return [] # Fail to build

        results = []

        if candidates[i] <= target:
            # Use i
            new_combination = list(current_combination)
            new_combination.append(candidates[i])
            use_i_results = self.helper(candidates, new_combination, i, target - candidates[i], memo)
            results.extend(use_i_results)

        # Dont use i
        new_combination = list(current_combination)
        dont_use_i_results = self.helper(candidates, new_combination, i+1, target, memo)
        results.extend(dont_use_i_results)

        return results

solution = Solution()

print solution.combinationSum([1,2], 4)
