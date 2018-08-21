"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leading_index = 0
        trailing_index = len(s) - 1

        valid_char_map = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))

        while leading_index < trailing_index:
            if s[leading_index] not in valid_char_map:
                leading_index += 1
            elif s[trailing_index] not in valid_char_map:
                trailing_index -= 1
            else:
                if s[leading_index].lower() == s[trailing_index].lower():
                    leading_index +=1
                    trailing_index -= 1
                else:
                    return False

        return True

solution = Solution()

print(solution.isPalindrome("race a car"))
