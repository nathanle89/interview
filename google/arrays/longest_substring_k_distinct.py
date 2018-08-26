"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        end = 0
        max_length = 0
        char_count_dict = {}

        while end < len(s):
            if s[end] not in char_count_dict:
                char_count_dict[s[end]] = 1
            else:
                char_count_dict[s[end]] += 1

            while len(char_count_dict) > k:
                char_count_dict[s[start]] -= 1
                if char_count_dict[s[start]] == 0:
                    del char_count_dict[s[start]]
                start += 1

            max_length = max([max_length, end - start + 1])

            end += 1

        return max_length

solution = Solution()

print(solution.lengthOfLongestSubstringKDistinct("karappa", 1))
