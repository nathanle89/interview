class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        #score_table
        score_table = [[None] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(len(word1)):
            score_table[i][0] = i

        for i in range(len(word2)):
            score_table[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    score_table[i][j] = score_table[i - 1][j - 1]
                else:
                    score_table[i][j] = min(score_table[i - 1][j - 1], score_table[i - 1][j], score_table[i][j - 1]) + 1

        return score_table[-1][-1]
