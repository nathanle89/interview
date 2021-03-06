"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        temp = -1 # for storing previous value at a given slot
        for i in range(len(nums)):
            if nums[i] - 1 == i:
                continue

            if nums[i] > 0:
                # check item at index i - 1
                if len(nums) >= nums[i]:
                    # We have a slot for nums[i]
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]

            while temp > 0:
                if len(nums) >= temp:
                    if nums[temp - 1] == temp:
                        break

                    # We have a slot for nums[i]
                    copied_temp = temp
                    temp = nums[copied_temp - 1]
                    nums[copied_temp - 1] = copied_temp
                else:
                    # Cant fit temp in the nums array so throw it away
                    break

        # loop through one more time
        counter = 0
        for i in range(len(nums)):
            counter += 1
            if nums[i] - 1 != i:
                return counter
        return counter + 1

solution = Solution()

print solution.firstMissingPositive([3,4,-1,1])