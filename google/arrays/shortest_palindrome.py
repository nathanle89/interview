"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length_s = len(s)

        if length_s == 0:
            return ""

        rev_s = s[::-1]
        giant_string = s + "#" + rev_s # This Trick for '#' is used to force the longest possible suffix of Reversed String and longest possible prefix of Original String
        kmp_matching_table = self.partial_matching_table(giant_string)

        number_of_char_to_remove = kmp_matching_table[-1]
        return rev_s[:-number_of_char_to_remove] + s

    def partial_matching_table(self, string):
        kmp = [0] * len(string)
        i = 0
        j = 1

        while j < len(string):
            if string[i] == string[j]:
                kmp[j] = i + 1
                i += 1
                j += 1
            else:
                if i > 0:
                    i = kmp[i - 1]
                else:
                    kmp[j] = 0
                    j += 1

        return kmp


solution = Solution()

print(solution.shortestPalindrome("aabba"))

# print (solution.partial_matching_table("aabaabaaa"))
