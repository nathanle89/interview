class Solution(object):
    def longestCommonPrefix(self, strs):

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        first_string = strs[0]

        if len(first_string) == 0:
            return ""

        index = 0

        while True:
            found = False
            for i in range(1, len(strs)):
                str_i = strs[i]
                if index == len(str_i) or index == len(first_string) or str_i[index] != first_string[index]:
                    found = True
                    break
            if found:
                break

            index += 1

        if index > 0:
            return first_string[0:index]
        else:
            return ""

solution = Solution()
print(solution.longestCommonPrefix(["a","ac"]))
