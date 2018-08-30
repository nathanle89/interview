"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None or len(a) == 0:
            return b
        if b is None or len(b) == 0:
            return a

        index_a = len(a) - 1
        index_b = len(b) - 1
        output = ""
        remainder = None
        while index_a >= 0 and index_b >= 0:
            sum_val, remainder = self.addTwoBits(a[index_a], b[index_b], remainder)
            output = sum_val + output

            index_a -= 1
            index_b -= 1

        leftover = None
        remaining_num = None
        remaining_index = None
        if index_a >= 0 or index_b >= 0:
            if index_a >= 0:
                leftover = a[0:index_a+1]
                remaining_num = a
                remaining_index = index_a
            else:
                leftover = b[0:index_b+1]
                remaining_num = b
                remaining_index = index_b


        if leftover:
            if remaining_index >= 0:
                while remaining_index >= 0:
                    sum_val, remainder = self.addTwoBits(remaining_num[remaining_index], "0", remainder)
                    output = sum_val + output

                    remaining_index -= 1
            else:
                output = leftover + output

        if remainder:
            output = "1" + output

        return output

    def addTwoBits(self, bit_a, bit_b, previous_remainder):
        output = ""
        remainder = None
        if bit_a == '0' and bit_b == '0':
            if previous_remainder:
                output = "1"
                remainder = None
            else:
                output = "0"
        elif (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1'):
            if previous_remainder:
                output = "0"
                remainder = "1"
                # Keep the remainder as "1"
            else:
                output = "1"
        else:
            if previous_remainder:
                output = "1"
                # Keep the remainder as "1"
            else:
                output = "0"

            remainder = "1"

        return output, remainder

solution = Solution()

print solution.addBinary("1010", "1011")
