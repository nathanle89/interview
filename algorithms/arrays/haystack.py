class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        kmp = self.kmpArray(needle)

        current_haystack_index = 0
        current_needle_index = 0

        while current_haystack_index < len(haystack):
            if current_needle_index == len(needle):
                return current_haystack_index - len(needle)

            if needle[current_needle_index] == haystack[current_haystack_index]:
                current_haystack_index += 1
                current_needle_index += 1
            else:
                if current_needle_index == 0:
                    current_haystack_index += 1
                else:
                    current_needle_index = kmp[current_needle_index - 1]
        if current_needle_index == len(needle) and current_haystack_index == len(haystack):
            return current_haystack_index - len(needle)
        else:
            return -1

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
print(solution.strStr("aaaaa", "bba"))
