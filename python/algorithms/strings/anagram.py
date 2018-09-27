class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = {}
        t_counter = {}

        for char in s:
            s_counter[char] = s_counter.get(char, 0) + 1

        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        if len(s_counter) != len(t_counter):
            return False

        for key, value in s_counter.iteritems():
            if key not in t_counter:
                return False

            if t_counter[key] != value:
                return False

        return True

