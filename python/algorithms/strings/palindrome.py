class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leading_index = 0
        trailing_index = len(s) - 1

        valid_char_map = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))

        while leading_index < trailing_index:
            if s[leading_index] not in valid_char_map:
                leading_index += 1
            elif s[trailing_index] not in valid_char_map:
                trailing_index -= 1
            else:
                if s[leading_index].lower() == s[trailing_index].lower():
                    leading_index +=1
                    trailing_index -= 1
                else:
                    return False

        return True

solution = Solution()

print(solution.isPalindrome("abbabba"))
