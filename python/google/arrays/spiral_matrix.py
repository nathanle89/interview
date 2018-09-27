"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):

        if not matrix:
            return []

        row_length = len(matrix)

        if row_length == 0:
            return []

        col_length = len(matrix[0])

        start_row = 0
        start_col = 0

        end_row = row_length - 1
        end_col = col_length - 1
        results = []
        while start_col <= end_col and start_row <= end_row:
            # Top surrounding
            for i in range(start_col, end_col + 1):
                results.append(matrix[start_row][i])

            # right surrounding
            for i in range(start_row + 1, end_row + 1):
                results.append(matrix[i][end_col])

            # bottom surrounding
            if start_row < end_row:
                for i in reversed(range(start_col, end_col)):
                    results.append(matrix[end_row][i])

            # left surrounding
            if start_col < end_col:
                for i in reversed(range(start_row + 1, end_row)):
                    results.append(matrix[i][start_col])

            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1

        return results
solution = Solution()

print solution.spiralOrder([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
    [ 10, 11, 12 ]
])

print solution.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
])