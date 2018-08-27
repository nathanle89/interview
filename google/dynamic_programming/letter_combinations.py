"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        char_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        return self.helper(digits, char_mapping, {})

    def helper(self, digits, char_mapping, memo):

        if len(digits) == 1:
            return list(char_mapping[digits])
        if len(digits) == 0:
            return []

        results = []
        digit = digits[0]
        mapping = char_mapping[digit]

        for letter in mapping:
            sub_digits = digits[1:]
            if sub_digits in memo:
                sub_results = memo[sub_digits]
            else:
                sub_results = self.helper(sub_digits, char_mapping, memo)
                memo[sub_digits] = sub_results

            for result in sub_results:
                results.append(letter + result)

        return results

solution = Solution()

print(solution.letterCombinations("233"))
