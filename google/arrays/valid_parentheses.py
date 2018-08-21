"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false
"""

class Solution:
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                current_paren = stack.pop()
                if (current_paren == '(' and char != ')') or (current_paren == '[' and char != ']') or (current_paren == '{' and char != '}'):
                    return False

        if len(stack) > 0:
            return False

        return True

