"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):

    # O(n^2) solution
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums = len(nums)

        if length_nums <= 1:
            return length_nums

        # This means every element is a longest subsequence of itself
        sequence_counter_list = [1] * length_nums

        start_index = 0
        end_index = 1

        while end_index < length_nums:
            if start_index == end_index:
                end_index += 1
                start_index = 0
            else:
                if nums[end_index] > nums[start_index]:
                    sequence_counter_list[end_index] = max([sequence_counter_list[end_index], sequence_counter_list[start_index] + 1])
                start_index += 1

        return max(sequence_counter_list)

    # O(nlogn) solution using Binary Search
    def lengthOfLISFast(self, nums):
        length_nums = len(nums)

        if length_nums <= 1:
            return length_nums

        # This increasing sequence list stores the index of each value
        increasing_sequence_last_index = []
        for i in range(length_nums):
            if len(increasing_sequence_last_index) == 0:
                increasing_sequence_last_index.append(i)
                continue

            if nums[i] > nums[increasing_sequence_last_index[-1]]:
                increasing_sequence_last_index.append(i)
            else:
                # Simple check for the first item to optimize for Binary Search
                if nums[i] < nums[increasing_sequence_last_index[0]]:
                    increasing_sequence_last_index[0] = i
                else:
                    # Binary Search to replace the ceiling
                    index_to_replace = self.binarySearchUpperBoundList(increasing_sequence_last_index, nums, nums[i])
                    increasing_sequence_last_index[index_to_replace] = i

        return len(increasing_sequence_last_index)

    def binarySearchUpperBoundList(self, sequence_indices, nums, target):
        start = 0
        end = len(sequence_indices) - 1

        while start < end:
            mid = (start + end) / 2
            if nums[sequence_indices[mid]] == target:
                return mid
            if mid == start or mid == end:
                break
            if nums[sequence_indices[mid]] < target:
                start = mid
            elif nums[sequence_indices[mid]] > target:
                end = mid

        # return the uppberbound
        return end


solution = Solution()

# print(solution.lengthOfLISFast([10,9,2,5,3,7,101,18]))
# print(solution.lengthOfLISFast([3,4,-1,5,8,2,3,12,7,9,10]))
print(solution.lengthOfLISFast([4,10,4,3,8,9]))

