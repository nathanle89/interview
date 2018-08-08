class Solution:
    def reverseString(self, s):

        byte_array = bytearray(s, 'utf8')
        string_len = len(byte_array)
        current_index = 0
        back_index = string_len - 1

        while current_index < back_index:
            leading_char = byte_array[current_index]
            trailing_char = byte_array[back_index]
            byte_array[current_index] = trailing_char
            byte_array[back_index] = leading_char

            current_index += 1
            back_index -= 1

        return str(byte_array)

solution = Solution()

print(solution.reverseString("hello"))
