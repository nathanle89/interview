"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        mapping = {1e9: "Billion", 1e6: "Million", 1e3: "Thousand", 1e2: "Hundred",
               90:  "Ninety", 80:  "Eighty", 70:  "Seventy",
               60:  "Sixty", 50:  "Fifty", 40:  "Forty",
               30:  "Thirty", 20:  "Twenty", 19: "Nineteen",
               18:  "Eighteen", 17: "Seventeen", 16: "Sixteen",
               15:  "Fifteen", 14: "Fourteen", 13: "Thirteen",
               12:  "Twelve", 11:  "Eleven", 10:  "Ten",
               9:   "Nine", 8:   "Eight", 7:   "Seven",
               6:   "Six", 5:   "Five", 4: "Four", 3: "Three",
               2: "Two", 1: "One", 0: "Zero"}

        sorted_key = [1e9,1e6,1e3,1e2,90,80,70,60,50,40,30,20, 19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

        return self.helper(num, mapping, sorted_key)

    def helper(self, num, mapping, sorted_key):
        front = ""
        back = ""
        for divider in sorted_key:
            if num <= 20:
                return mapping[num]
            d, r = divmod(num, divider)
            d = int(d)
            r = int(r)
            if not d:
                continue

            if divider >= 100:
                front += self.helper(d, mapping, sorted_key) + " "
            else:
                front += ""

            if r:
                back += " " + self.helper(r, mapping, sorted_key)
            else:
                back += ""

            return front + mapping[divider] + back

solution = Solution()

print(solution.numberToWords(3295))

