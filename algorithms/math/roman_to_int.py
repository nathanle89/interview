class Solution:

    def romanToInt(self, s):
        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        string_len = len(s)
        for i in range(0, len(s)):
            char = s[i]
            current_value = roman_value[char]

            if i < string_len - 1:
                next_char = s[i+1]

                if char == 'I' and (next_char == 'V' or next_char == 'X'):
                    result -= current_value

                elif char == 'X' and (next_char == 'L' or next_char == 'C'):
                    result -= current_value

                elif char == 'C' and (next_char == 'D' or next_char == 'M'):
                    result -= current_value
                else:
                    result += current_value
            else:
                result += current_value

        return result

solution = Solution()

print(solution.romanToInt('MCMXCIV'))
