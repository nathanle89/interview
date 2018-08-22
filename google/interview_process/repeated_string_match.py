"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
import math

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        length_B = len(B)
        length_A = len(A)
        counter = 1

        # Make sure B and A contains the same set of chars
        if not set(B).issubset(set(A)):
            return -1

        tmp = A
        ratios = int(math.ceil(float(length_B) / length_A))

        # Try at least once
        while counter <= ratios:
            if B in tmp:
                return counter
            else:
                tmp += A
                counter += 1

        # x + 1
        if B in tmp:
            return counter
        else:
            return -1

solution = Solution()

print solution.repeatedStringMatch("a", "a")
