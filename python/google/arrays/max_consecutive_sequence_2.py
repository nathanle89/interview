"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length_nums = len(nums)

        if length_nums == 0:
            return 0

        current_max = 0
        max_previous_index = 0
        max_current_index = 0
        previous_index = 0
        current_index = 0
        current_counter = 0
        for i in range(0, len(nums)):
            num = nums[i]
            if num == 0:
                current_counter = 0
            else:
                if current_counter == 0:
                    previous_index = i
                    # Flipping from 0 to one

                current_counter += 1
            current_index = i
            if current_counter > current_max:
                max_previous_index = previous_index
                max_current_index = current_index
                current_max = current_counter

        new_count_forward = current_max
        if max_current_index + 1 < length_nums:
            # Try flipping next index
            nums[max_current_index+1] = 1
            for i in range(max_current_index+1, length_nums):
                if nums[i] == 1:
                    new_count_forward += 1
                else:
                    break

        new_count_backward = current_max
        if max_previous_index - 1 >= 0:
            # Try flipping next index
            nums[max_previous_index - 1] = 1
            for i in range(max_previous_index - 1, -1, -1):
                if nums[i] == 1:
                    new_count_backward += 1
                else:
                    break

        # Edge case
        if max_previous_index == max_current_index and nums[max_current_index] == 0:
            return 1

        return max([current_max, new_count_backward, new_count_forward])

solution = Solution()

print(solution.findMaxConsecutiveOnes([0]))