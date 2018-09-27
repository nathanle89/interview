"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return []

        row_length = len(matrix)
        if row_length == 0:
            return []

        col_length = len(matrix[0])

        is_up = True
        results = []
        for i in range(0, row_length):
            if i == 0:
                for j in range(0, col_length):
                    diagonal_results = []
                    diagonal_results.append(matrix[i][j]) # First node

                    # Append diagonal
                    current_index = j - 1
                    for k in range(i + 1, row_length):
                        if current_index < 0:
                            break
                        diagonal_results.append(matrix[k][current_index])
                        current_index -= 1

                    if is_up:
                        diagonal_results.reverse()

                    results.extend(diagonal_results)
                    if is_up:
                        is_up = False
                    else:
                        is_up = True
            else:
                diagonal_results = []
                diagonal_results.append(matrix[i][-1])

                # Append diagonal
                current_index = col_length - 1 - 1
                for k in range(i + 1, row_length):
                    if current_index < 0:
                        break
                    diagonal_results.append(matrix[k][current_index])
                    current_index -= 1

                if is_up:
                    diagonal_results.reverse()

                results.extend(diagonal_results)
                if is_up:
                    is_up = False
                else:
                    is_up = True

        return results

solution = Solution()
matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
print(solution.findDiagonalOrder(matrix))
