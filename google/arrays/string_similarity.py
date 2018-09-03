"""

print how many operation it takes to convert String A to String B

A: asdaw
B: oldawj

"""

class Solution:
    def edit_distance_score(self, A, B):

        if (A is None or A == "") and (B is None or B == ""):
            return 0

        if (A is None or A == ""):
            return len(B)

        if (B is None or B == ""):
            return len(A)

        # Also add the empty string to avoid null check
        score_table = [[None] * (len(A) + 1) for i in range(len(B) + 1)]

        # Populate the first row and first column:
        for i in range(len(B) + 1):
            score_table[i][0] = i

        for i in range(len(A) + 1):
            score_table[0][i] = i

        for i in range(1, len(B) + 1):
            for j in range(1, len(A) + 1):
                if B[i-1] == A[j-1]:
                    # Grab the diagonal value
                    score_table[i][j] = score_table[i-1][j-1]
                else:
                    # Minimum of the three + 1
                    score_table[i][j] = min([score_table[i-1][j-1], score_table[i-1][j], score_table[i][j-1]]) + 1

        return score_table

solution = Solution()

print solution.edit_distance_score("abcdef", "azced")



