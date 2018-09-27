class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        found_non_whitespace_char = False
        found_negative_leading_char = False
        number_value = ""
        for char in str:
            if found_negative_leading_char and char == '-':
                break

            if found_non_whitespace_char:
                if char.isdigit():
                    number_value += char
                else:
                    break

            if char != ' ' and not found_non_whitespace_char:
                found_non_whitespace_char = True

                if char == '-':
                    found_negative_leading_char = True
                elif char.isdigit():
                    number_value += char
                elif char == '+':
                    continue
                else:
                    break

        if len(number_value) > 0:
            result = int(number_value)

            if found_negative_leading_char:
                result *= -1

            return max([min([2**31 - 1, result]), -2**31])

        else:
            return 0

solution = Solution()

print(solution.myAtoi("+1"))
