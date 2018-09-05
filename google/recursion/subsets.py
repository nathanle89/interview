"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
    [3],
    [1],
    [2],
    [1,2,3],
    [1,3],
    [2,3],
    [1,2],
    []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        return self.helper(nums, [], 0)

    def helper(self, nums, current_sets, i):
        if i == len(nums):
            return [current_sets]

        results = []
        used_i_set = list(current_sets)
        used_i_set.append(nums[i])
        include_i_sets = self.helper(nums, used_i_set, i + 1)

        dont_include_i_sets = self.helper(nums, list(current_sets), i + 1)

        results.extend(include_i_sets)
        results.extend(dont_include_i_sets)

        return results

solution = Solution()

print solution.subsets([1,2,2])