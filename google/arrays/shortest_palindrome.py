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

        bytearray_s = bytearray(s, 'utf8')

        leading_index = 0
        trailing_index = length_s - 1

        while leading_index < trailing_index:
            if chr(bytearray_s[leading_index]) != chr(bytearray_s[trailing_index]):
                bytearray_s.insert(leading_index, bytearray_s[trailing_index])
                trailing_index += 1
            else:
                leading_index += 1
                trailing_index -= 1

        return str(bytearray_s)

    def shortestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        if r == s:
            return s
        kmp = [0] * len(s)
        i = 0
        j = 1
        while j < len(s):
            if r[j] == s[i]:
                i += 1
                kmp[j] = i
                j += 1
            else:
                if i > 0:
                    i = kmp[i-1]
                else:
                    kmp[j] = 0
                    j += 1
        pre = r[:len(r) - kmp[-1]]
        return pre + s

solution = Solution()

print(solution.shortestPalindrome("aabba"))
print(solution.shortestPalindrome2("aabba"))