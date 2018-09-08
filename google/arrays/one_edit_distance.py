"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

class Solution:
    def isOneEditDistance(self, A, B):
        lengthA = len(A)
        lengthB = len(B)

        if lengthA == 0 and lengthB == 0:
            return False

        if lengthA > lengthB:
            return self.isOneEditDistance(B, A)

        # B should always be larger
        if lengthB - lengthA > 1:
            return False

        index = 0
        diff = lengthB - lengthA

        while index < lengthA and A[index] == B[index]:
            index += 1

        if index == lengthA:
            return diff > 0

        if diff == 0:
            index += 1

        while index < lengthA and A[index] == B[index + diff]:
            index += 1

        return index == lengthA