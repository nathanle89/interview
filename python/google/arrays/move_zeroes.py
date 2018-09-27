"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums):
        current_non_zero_index = 0
        length_nums = len(nums)
        for i in range(0, length_nums):
            if nums[i] != 0:
                nums[current_non_zero_index] = nums[i]
                current_non_zero_index += 1

        for i in range(current_non_zero_index, length_nums):
            nums[i] = 0


solution = Solution()
nums = [0,1,0,3,12]

solution.moveZeroes(nums)
print(nums)
