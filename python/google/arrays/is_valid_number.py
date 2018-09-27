"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"e" => False
".1" => true
"-.4" => true
"3-2" => false
".-4" => false

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.

Question to ask:

"0..1" => True/False
"2ee10" => True or False
"1  2" => True or False
"1. 3" => true or false


Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False

        stripped_s = s.strip()

        if len(stripped_s) == 0:
            return False

        valid_number_set = set(list("0123456789"))
        valid_non_number_set = set(list("+-e."))
        encounter_dot = False
        encounter_e = False
        seen_number = False
        trailing_numbers = 0

        for i in range(0, len(stripped_s)):
            char = stripped_s[i]
            if char in valid_number_set or char in valid_non_number_set:
                if char in valid_number_set:
                    if not seen_number:
                        seen_number = True

                    if trailing_numbers:
                        trailing_numbers = False

                if char == '.':
                    if encounter_dot or encounter_e:
                        return False

                    encounter_dot = True

                if char == '-' or char == '+':
                    if i != 0 and stripped_s[i - 1] != 'e':
                        return False

                if char == 'e':
                    trailing_numbers = True
                    if not seen_number or encounter_e:
                        return False
                    encounter_e = True

            else:
                return False

        if encounter_dot and not seen_number:
            return False

        if trailing_numbers:
            return False

        return True

solution = Solution()
print(solution.isNumber("-.4"))
