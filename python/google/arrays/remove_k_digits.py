"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution(object):

    # This is a brute-force solution O(k*n) or O(n^2)
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        return self.helper(num, k)

    def helper(self, num, k):
        if k == 0:
            return num

        if len(num) == k:
            return "0"

        current_min = 2**32
        while k > 0:
            for i in range(len(str(num))):
                new_num = str(num)[:i] + str(num)[i+1:]
                if int(new_num) < current_min:
                    current_min = int(new_num)
            num = current_min
            k -= 1

        return current_min

    # This method uses a stack and the property that the left most digit is always the largest
    def removeKdigitsLinear(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)

        # This basically means all the leading digits are small and removing the trailing digits will
        # make it smallest. Ex: 112
        while k > 0:
            stack.pop()
            k -= 1

        if len(stack) == 0:
            return "0"
        else:
            # We also need to strip leading zeroes
            # and handle the case where stripping 0 makes it empty string
            return "".join(stack).lstrip('0') or "0"




solution = Solution()

print solution.removeKdigitsLinear("10200", 1)

