"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        dedup = set()
        results = self.helper(nums, [], 0)
        final_results = []
        for result in results:
            result.sort()
            tuple_result = tuple(result)
            if tuple_result in dedup:
                continue
            else:
                final_results.append(result)
                dedup.add(tuple_result)
        return final_results

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