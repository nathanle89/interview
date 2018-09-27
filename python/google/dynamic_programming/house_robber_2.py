"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Split this problem into 2 sub problem
        sub_problem_1 = nums[0:-1]
        sub_problem_2 = nums[1:]
        return max([self.rob_heper(sub_problem_1), self.rob_heper(sub_problem_2)])

    def rob_heper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_max = 0
        current_max = 0
        for num in nums:
            temp = current_max
            current_max = max([previous_max + num, current_max])
            previous_max = temp

        return current_max

solution = Solution()
nums = [1,2, 1, 1]
nums = [2,7,9,3,1]
nums = [1,2]
nums = [1,1]
nums = [2,3, 2]
print solution.rob(nums)