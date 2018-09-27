"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 1
        if s[0] == "0":
            return 0

        num_mapping = {
            "1": "A",
            "2": "B",
            "3": "C",
            "4": "D",
            "5": "E",
            "6": "F",
            "7": "G",
            "8": "H",
            "9": "I",
            "10": "J",
            "11": "K",
            "12": "L",
            "13": "M",
            "14": "N",
            "15": "O",
            "16": "P",
            "17": "Q",
            "18": "R",
            "19": "S",
            "20": "T",
            "21": "U",
            "22": "V",
            "23": "W",
            "24": "X",
            "25": "Y",
            "26": "Z"
        }
        return self.helper(s, num_mapping, {})

    def helper(self, s, num_mapping, memo):
        if s == "":
            return 1
        if s in memo:
            return memo[s]
        if s[0] == "0":
            return 0

        result = 0
        result += self.helper(s[1:], num_mapping, memo)
        if len(s) > 1 and s[0:2] in num_mapping:
            result += self.helper(s[2:], num_mapping, memo)

        memo[s] = result

        return result

solution = Solution()

print solution.numDecodings("101")
