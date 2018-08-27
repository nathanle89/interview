"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        while num > 0:
            if num >= 1000:
                output += "M"
                num -= 1000
            elif 900 <= num < 1000:
                output += "CM"
                num -= 900
            elif 400 <= num < 500:
                output += "CD"
                num -= 400
            elif 90 <= num < 100:
                output += "XC"
                num -= 90
            elif 40 <= num < 50:
                output += "XL"
                num -= 40
            elif num == 9:
                output += "IX"
                num -= 9
            elif num == 4:
                output += "IV"
                num -= 4
            elif 500 <= num < 900:
                output += "D"
                num -= 500
            elif 100 <= num < 400:
                output += "C"
                num -= 100
            elif 50 <= num < 90:
                output += "L"
                num -= 50
            elif 10 <= num < 40:
                output += "X"
                num -= 10
            elif 5 <= num < 9:
                output += "V"
                num -= 5
            else:
                output += "I"
                num -= 1

        return output

solution = Solution()
print(solution.intToRoman(1994))
