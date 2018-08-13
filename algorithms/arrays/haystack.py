class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_needle = len(needle)
        length_haystack = len(haystack)
        if length_needle == 0:
            return 0

        first_matching_index = -1
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0] and i + length_needle <= length_haystack and haystack[i:i+length_needle] == needle:
                first_matching_index = i
                break

        if first_matching_index >= 0:
            result = first_matching_index
            for char in needle:
                if first_matching_index <= length_haystack - 1 and char == haystack[first_matching_index]:
                    first_matching_index += 1
                else:
                    return -1

            return result
        else:
            return -1

solution = Solution()
print(solution.strStr("mississippi", "issip"))
