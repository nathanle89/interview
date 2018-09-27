"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        current_longest = ""
        for i in range(len(s)):
            # Odd case
            output = self.helper(s, i, i)
            if len(output) > len(current_longest):
                current_longest = output

            output = self.helper(s, i, i + 1)
            if len(output) > len(current_longest):
                current_longest = output
        return current_longest

    # Left and right starts from the middle going out
    # This pattern is checking palindrome is outward
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

solution = Solution()

print solution.longestPalindrome("eabcb")
