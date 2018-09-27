"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return self.plusOneHelper(digits)

    def plusOneHelper(self, digits):
        result = list(digits)
        last_number = result[-1]

        if last_number < 9:
            last_number += 1
            result[-1] = last_number
        else:
            digits_length_minus_one = len(result) - 1

            if digits_length_minus_one == 0:
                result = [1, 0]
            else:
                updated = self.plusOneHelper(digits[0:-1])
                updated.append(0)
                result = updated

        return result

solution = Solution()

print(solution.plusOne([1,9,9,9]))
