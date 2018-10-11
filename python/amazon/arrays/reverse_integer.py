class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        lower = -2**31
        upper = 2**31 - 1
        is_negative = False
        if x < 0:
            is_negative = True

        byte_array_x = bytearray(str(abs(x)))

        start = 0
        end = len(byte_array_x) - 1
        while start < end:
            tmp = byte_array_x[start]
            byte_array_x[start] = byte_array_x[end]
            byte_array_x[end] = tmp
            start += 1
            end -= 1

        # Remove zeroes
        while str(byte_array_x[0]) == '0':
            del byte_array_x[0]

        x = int(str(byte_array_x))
        if is_negative:
            x *= -1

        if x < lower or x > upper:
            return 0

        return x



