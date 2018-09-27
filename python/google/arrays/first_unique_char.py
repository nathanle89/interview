"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_string = len(s)
        char_counter = {}
        for char in s:
            char_counter[char] = char_counter.get(char, 0) + 1

        result_index = -1
        for i in range(0, length_string):
            if char_counter[s[i]] == 1:
                result_index = i
                break

        return result_index

solution = Solution()

print(solution.firstUniqChar("loveleetcode"))
