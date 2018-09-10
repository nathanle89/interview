"""
Check if a string S is a substring of string T using KMP algorithm

input: T = "asdabcedadwod", S = "abce"

"""

class Solution:
    def isSubString(self, S, T):
        kmp = self.kmpArray(S)
        if len(S) > len(T):
            return False

        current_T_index = 0
        current_S_index = 0

        while current_T_index < len(T):
            if current_S_index == len(S):
                return True

            if S[current_S_index] == T[current_T_index]:
                current_T_index += 1
                current_S_index += 1
            else:
                if current_S_index == 0:
                    current_T_index += 1
                else:
                    current_S_index = kmp[current_S_index - 1]

        return current_S_index == len(S) and current_T_index == len(T)

    def kmpArray(self, S):
        if len(S) == 1:
            return [0]
        kmp = [0] * len(S)
        i = 0
        j = 1
        while j < len(S):
            if S[i] == S[j]:
                kmp[j] = i + 1
                j += 1
                i += 1
            else:
                if i > 0:
                    i = kmp[i - 1]
                else:
                    kmp[j] = 0
                    j += 1
        return kmp

solution = Solution()
print solution.isSubString("abce", "asdabcedadwod")
print solution.isSubString("absce", "asdabcedadwod")
print solution.isSubString("bcgl", "abcbcglx")
print solution.isSubString("bcdgl", "abcbcglx")

print solution.isSubString("abcaby", "abxabcabcaby")
print solution.isSubString("abcdabcy", "abcxabcdabxabcdabcdabcy")