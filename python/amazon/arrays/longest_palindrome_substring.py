class Solution(object):
    ## Optimal answer for this problem is O(n^2) and O(1) space
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        result = ""
        for i in range(len(s)):
            # Expand from the center for odd case
            current_palindrome = self.palindromeExpanding(s, i, i)
            if len(current_palindrome) > len(result):
                result = current_palindrome

            current_palindrome = self.palindromeExpanding(s, i, i + 1)
            if len(current_palindrome) > len(result):
                result = current_palindrome

        return result

    def palindromeExpanding(self, s, center_left, center_right):
        while center_left >= 0 and center_right < len(s) and s[center_left] == s[center_right]:
            center_left -= 1
            center_right += 1
        # We do center_left + 1 becuase center_left already decrement in the loop
        # The same thing for center_right but we do the bracket version so we dont need to substract one
        return s[center_left + 1: center_right]

solution = Solution()

print solution.longestPalindrome("babad")
