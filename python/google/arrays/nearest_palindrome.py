"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        pass
        # if n is None or n == "":
        #     return n
        #
        # if len(n) == 1:
        #     return str(int(n) - 1)
        #
        # byte_array = bytearray(n, 'utf8')
        # result = self.getNearestHelper(byte_array)
        #
        # if n[-2:] == "00" or n == '10':
        #     # Try the lower nearest
        #     n = str(int(n) - 1)
        # elif n[-2:] == "11" or n[-1] == "1":
        #     # Try the lower nearest
        #     n = str(int(n) - 2)
        #
        # elif n[-2:] == "99" or n[-1] == "9":
        #     # Try the lower nearest
        #     n = str(int(n) + 2)
        #
        #
        # length_n = len(n)
        # prefix_index = length_n/2


        # return result

    def getNearestHelper(self, byte_array):
        if len(byte_array) == 1:
            return str(byte_array)

        length = len(byte_array)
        left = (length - 1) / 2
        right = left

        if length % 2 == 0:
            right += 1

        while left >= 0 and right < length:
            if chr(byte_array[left]) != byte_array[right]:
                byte_array[right] = byte_array[left]
            left -= 1
            right += 1
        return str(byte_array)

solution = Solution()

print(solution.nearestPalindromic("19"))

