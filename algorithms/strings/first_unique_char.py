class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_length = len(s)
        char_count_map = {}
        for i in range(0, string_length):
            char_count_map[s[i]] = char_count_map.get(s[i], 0) + 1

        for i in range(0, string_length):
            if char_count_map[s[i]] == 1:
                return i

        return -1

solution = Solution()
print(solution.firstUniqChar("loveleetcode"))
