"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            mid = (end_index + start_index) / 2

            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[end_index]:
                    # Pivot is on the left
                    if nums[mid] < target and target <= nums[end_index]:
                        start_index = mid + 1
                    else:
                        end_index = mid - 1
                else:
                    # Pivot is on the right
                    if nums[mid] < target or target <= nums[end_index]:
                        start_index = mid + 1
                    else:
                        end_index = mid - 1

        return -1

nums = [3,4,5,6,1,2]

solution = Solution()

print(solution.search(nums, 2))
