class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leading_index = 0
        trailing_index = len(s) - 1

        valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        valid_char_map = {}
        for char in valid_char:
            valid_char_map[char] = True

        while leading_index < trailing_index:
            leading_char = s[leading_index]
            trailing_char = s[trailing_index]

            if leading_char not in valid_char_map:
                leading_index += 1

            if trailing_char not in valid_char_map:
                trailing_index -= 1

            if trailing_char in valid_char_map and leading_char in valid_char_map:
                if leading_char.lower() == trailing_char.lower():
                    leading_index += 1
                    trailing_index -= 1
                else:
                    return False


        return True

solution = Solution()

print(solution.isPalindrome("race a car"))
