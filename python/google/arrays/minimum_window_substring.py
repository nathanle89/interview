"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        target_counter = {}
        for char in t:
            target_counter[char] = target_counter.get(char, 0) + 1
        required_distinct_char = len(target_counter)

        window_counter = {}
        string_length = len(s)
        start_pointer = 0
        end_pointer = 0
        result_string = ""
        current_char_counter = 0
        while end_pointer < string_length:
            new_char = s[end_pointer]
            window_counter[new_char] = window_counter.get(new_char, 0) + 1

            if new_char in target_counter and window_counter[new_char] == target_counter[new_char]:
                current_char_counter += 1

            while current_char_counter == required_distinct_char and start_pointer < string_length:
                if result_string == "":
                    result_string = s[start_pointer:end_pointer+1]

                removing_char = s[start_pointer]
                start_pointer += 1
                window_counter[removing_char] = window_counter.get(removing_char, 0) - 1

                if removing_char in target_counter and window_counter[removing_char] < target_counter[removing_char]:
                    current_char_counter -= 1

                if current_char_counter == required_distinct_char and len(result_string) > len(s[start_pointer:end_pointer+1]):
                    result_string = s[start_pointer:end_pointer+1]

            end_pointer += 1
        return result_string

solution = Solution()

print solution.minWindow("A", "B")
